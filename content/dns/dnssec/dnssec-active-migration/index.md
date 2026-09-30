<p>Follow this tutorial to migrate an existing DNS zone to Cloudflare without having to disable DNSSEC.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/7697.md")
</aside>
<p>This is an advanced procedure and assume some familiarity with <a href="/dns/concepts/">DNS concepts</a>, <a href="/fundamentals/api/">API operations</a>, and basic setup steps. Assumed knowledge that is not detailed in this tutorial can be referenced through the linked content in each of the steps.</p>
<h2 id="requirement">Requirement</h2>
<p>The provider you are migrating from must allow you to add DNSKEY records on the zone apex and use these records in responses to DNS queries.</p>
<h2 id="1-set-up-cloudflare"><ol>
<li>Set up Cloudflare</li>
</ol></h2>
<ol>
<li>
<p><a href="/fundamentals/manage-domains/add-site/">Add your zone to Cloudflare</a>.</p>
<p>To add your zone using the API, refer to the <a href="/api/resources/zones/methods/create/">Create Zone endpoint</a>.</p>
</li>
<li>
<p><a href="/dns/manage-dns-records/how-to/create-dns-records/">Review the records found by the automatic scan</a> or <a href="/dns/manage-dns-records/how-to/import-and-export/">import your zone file</a>.</p>
<p>To import the zone file using the API, refer to the <a href="/api/resources/dns/subresources/records/methods/import/">Import DNS Records endpoint</a>.</p>
</li>
<li>
<p>On the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/settings"><strong>DNS Settings</strong></a> page, select <strong>Enable DNSSEC</strong>. Or use the following <a href="/api/resources/dns/subresources/dnssec/methods/edit/">API request</a>.</p>
</li>
</ol>
<pre class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/dnssec \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;status&quot;: &quot;active&quot;&#10;}&#x27;</code></pre>
<ol start="4">
<li>On the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/settings"><strong>DNS Settings</strong></a> page, enable <strong>Multi-signer DNSSEC</strong>. Or use the following <a href="/api/resources/dns/subresources/dnssec/methods/edit/">API request</a>.</li>
</ol>
<pre class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/dnssec \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;dnssec_multi_signer&quot;: true&#10;}&#x27;</code></pre>
<h2 id="2-cross-import-zsks"><ol start="2">
<li>Cross-import ZSKs</li>
</ol></h2>
<ol>
<li>Add the <a href="https://www.cloudflare.com/learning/dns/dns-records/dnskey-ds-records/">ZSK</a> of your previous provider to Cloudflare by creating a DNSKEY record on your zone.</li>
</ol>
<p>You can do this <a href="/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records">on the dashboard</a> or through the <a href="/api/resources/dns/subresources/records/methods/create/">Create DNS Record endpoint</a>, as in the following example.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;type&quot;: &quot;DNSKEY&quot;,&#10;  &quot;name&quot;: &quot;&lt;ZONE_NAME&gt;&quot;,&#10;  &quot;data&quot;: {&#10;    &quot;flags&quot;: 256,&#10;    &quot;protocol&quot;: 3,&#10;    &quot;algorithm&quot;: 13,&#10;    &quot;public_key&quot;: &quot;&lt;PUBLIC_KEY&gt;&quot;&#10;  },&#10;  &quot;ttl&quot;: 3600&#10;}&#x27;</code></pre>
<ol start="2">
<li>Get Cloudflare's ZSK using either the API or a query from one of the assigned Cloudflare nameservers.</li>
</ol>
<p>API example:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/zones/{zone_id}/dnssec/zsk \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot;&#10;</code></pre>
<p>Command line query example:</p>
<pre><code class="language-sh">dig &lt;ZONE_NAME&gt; dnskey @&lt;CLOUDFLARE_NAMESERVER&gt; +noall +answer | grep 256&#10;</code></pre>
<ol start="3">
<li>Add Cloudflare's ZSK that you fetched in the last step to your previous provider.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7696.md")
</aside>
<h2 id="3-set-up-registrar"><ol start="3">
<li>Set up registrar</li>
</ol></h2>
<ol>
<li>Add Cloudflare DS record to your registrar. You can see your Cloudflare DS record on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/settings"><strong>DNS Settings</strong></a> page, under <strong>DS Record</strong>.</li>
<li>Add Cloudflare assigned nameservers to your registrar. You can see your Cloudflare nameservers on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/records"><strong>DNS Records</strong></a> page</li>
</ol>
<p>At this point your zone is in a <a href="/dns/dnssec/multi-signer-dnssec/">multi-signer DNSSEC setup</a>.</p>
<h2 id="4-remove-previous-provider"><ol start="4">
<li>Remove previous provider</li>
</ol></h2>
<ol>
<li>Remove your previous provider's DS record from your registrar.</li>
<li>Remove your previous provider's nameservers from your registrar.</li>
<li>After waiting at least one and a half times the <a href="https://www.cloudflare.com/learning/cdn/glossary/time-to-live-ttl/">TTL</a> of your previous provider DS record, you can remove the DNSKEY record (containing your previous provider ZSK) that you added to your Cloudflare zone in <a href="#2-cross-import-zsks">step 2</a>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7694.md")
</aside>
