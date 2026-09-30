<p>With <a href="/dns/zone-setups/zone-transfers/cloudflare-as-primary/">outgoing zone transfers</a>, you keep Cloudflare as your primary DNS provider and use one or more secondary providers for increased availability and fault tolerance.</p>
<p>If you want to use DNSSEC with outgoing zone transfers, you should configure <a href="/dns/dnssec/multi-signer-dnssec/">multi-signer DNSSEC</a>. After setting up <a href="/dns/zone-setups/zone-transfers/cloudflare-as-primary/setup/">Cloudflare as primary</a>, follow the steps below to enable DNSSEC.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>Note that:</p>
<ul>
<li>This process requires that your other DNS provider(s) also support multi-signer DNSSEC.</li>
<li>Although you can complete a few steps via the dashboard, currently the whole process can only be completed using the API.</li>
<li>Enabling <strong>DNSSEC</strong> and <strong>Multi-signer DNSSEC</strong> in <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/settings"><strong>DNS Settings</strong></a> only replaces the first step below. You still have to follow the rest of this tutorial to complete the setup.</li>
</ul>
<h2 id="steps">Steps</h2>
<ol>
<li>Use the <a href="/api/resources/dns/subresources/dnssec/methods/edit/">Edit DNSSEC Status endpoint</a> to enable DNSSEC and activate multi-signer DNSSEC for your zone. This is done by setting <code>status</code> to <code>active</code> and <code>dnssec_multi_signer</code> to <code>true</code>, as in the following example.</li>
</ol>
<pre class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/dnssec \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;status&quot;: &quot;active&quot;,&#10;  &quot;dnssec_multi_signer&quot;: true&#10;}&#x27;</code></pre>
<ol start="2">
<li>Add the ZSK(s) of your external provider(s) to Cloudflare by creating a DNSKEY record on your zone.</li>
</ol>
<pre><code class="language-bash">curl &#x27;https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records&#x27; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;type&quot;: &quot;DNSKEY&quot;,&#10;  &quot;name&quot;: &quot;&lt;ZONE_NAME&gt;&quot;,&#10;  &quot;data&quot;: {&#10;    &quot;flags&quot;: 256,&#10;    &quot;protocol&quot;: 3,&#10;    &quot;algorithm&quot;: 13,&#10;    &quot;public_key&quot;: &quot;&lt;PUBLIC_KEY&gt;&quot;&#10;  },&#10;  &quot;ttl&quot;: 3600&#10;}&#x27;&#10;</code></pre>
<ol start="3">
<li>
<p>Once the DNSKEY record is transferred out from Cloudflare to your secondary provider, get Cloudflare's ZSK and manually add it to the DNSKEY record.</p>
<p>Currently, the ZSK is not automatically transferred out. You can use either the API or a query from one of the assigned Cloudflare nameservers to obtain it.</p>
</li>
</ol>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/8079.md")
</div>
<ol start="4">
<li>Add DS records to your registrar, one for each provider. You can see your Cloudflare DS record on the <a href="https://dash.cloudflare.com/?to=/:account/:zone/dns/settings"><strong>DNS Settings</strong></a> page, under <strong>DS Record</strong>.</li>
</ol>
<p>The nameserver settings at your registrar should include the nameservers of all providers you will be using for your multi-signer DNSSEC setup.</p>
