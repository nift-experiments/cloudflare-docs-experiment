<p><a href="/waf/">Web Application Firewall (WAF)</a> allows you to create additional security measures through Cloudflare. As a SaaS provider, you can link custom rules, rate limiting rules, and managed rules to your custom hostnames. This provides more control to keep your domains safe from malicious traffic.</p>
<p>As a SaaS provider, you may want to apply different security measures to different custom hostnames. With WAF for SaaS, you can create multiple WAF configuration that you can apply to different sets of custom hostnames. This added flexibility and security leads to optimal protection across the domains of your end customers.</p>
<hr />
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you can use WAF for SaaS, you need to create a custom hostname. Review <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/">Get started with Cloudflare for SaaS</a> if you have not already done so.</p>
<p>You can also create a custom hostname through the API:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/custom_hostnames \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;hostname&quot;: &quot;&lt;CUSTOM_HOSTNAME&gt;&quot;,&#10;  &quot;ssl&quot;: {&#10;    &quot;wildcard&quot;: false&#10;  }&#10;}&#x27;</code></pre>
<h2 id="1-associate-custom-metadata-to-a-custom-hostname"><ol>
<li>Associate custom metadata to a custom hostname</li>
</ol></h2>
<p>To apply WAF to your custom hostname, you need to create an association between your customer's domain and the WAF configuration that you would like to attach to it. Cloudflare's product, <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/">custom metadata</a> allows you to do this via the API.</p>
<ol>
<li>
<p><a href="/fundamentals/account/find-account-and-zone-ids/">Locate your zone ID</a>, available in the Cloudflare dashboard.</p>
</li>
<li>
<p>Locate your Authentication Key on the <a href="https://dash.cloudflare.com/?to=/:account/profile/api-tokens"><strong>API Tokens</strong></a> page, under <strong>Global API Key</strong>.</p>
</li>
<li>
<p>Locate your custom hostname ID by making a <code>GET</code> call in the API:</p>
</li>
</ol>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/custom_hostnames \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<ol start="4">
<li>Plan your <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/">custom metadata</a>. It is fully customizable. In the example below, we have chosen the tag <code>&quot;security_level&quot;</code> to which we expect to assign three values (low, medium, and high).</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4132.md")
</aside>
<ol start="5">
<li>Make an API call in the format below using your Cloudflare email and the IDs gathered above:</li>
</ol>
<pre class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/custom_hostnames/{custom_hostname_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;custom_metadata&quot;: {&#10;    &quot;customer_id&quot;: &quot;12345&quot;,&#10;    &quot;security_level&quot;: &quot;low&quot;&#10;  }&#10;}&#x27;</code></pre>
<p>This assigns custom metadata to your custom hostname so that it has a security tag associated with its ID.</p>
<h2 id="2-trigger-security-products-based-on-tags"><ol start="2">
<li>Trigger security products based on tags</li>
</ol></h2>
<ol>
<li>
<p>Locate the custom metadata field in the Ruleset Engine where the WAF runs. This can be used to trigger different configurations of products such as <a href="/waf/custom-rules/">WAF custom rules</a>, <a href="/waf/rate-limiting-rules/">rate limiting rules</a>, and <a href="/rules/transform/">Transform Rules</a>.</p>
</li>
<li>
<p>Build your rules either <a href="/waf/custom-rules/create-dashboard/">through the dashboard</a> or via the API. An example rate limiting rule, corresponding to <code>&quot;security_level&quot;</code> low, is shown below as an API call.</p>
</li>
</ol>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/{ruleset_phase}/entrypoint \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;block&quot;,&#10;      &quot;ratelimit&quot;: {&#10;        &quot;characteristics&quot;: [&#10;          &quot;cf.colo.id&quot;,&#10;          &quot;ip.src&quot;&#10;        ],&#10;        &quot;period&quot;: 10,&#10;        &quot;requests_per_period&quot;: 2,&#10;        &quot;mitigation_timeout&quot;: 60&#10;      },&#10;      &quot;expression&quot;: &quot;lookup_json_string(cf.hostname.metadata, \&quot;security_level\&quot;) eq \&quot;low\&quot; and http.request.uri contains \&quot;login\&quot;&quot;&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<p>To build rules through the dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>WAF</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Follow the instructions on the dashboard specific to custom rules, rate limiting rules, or managed rules, depending on your security goal.</p>
</li>
<li>
<p>Once the rule is active, you should see it under the applicable tab (custom rules, rate limiting, or managed rules).</p>
</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4131.md")
</aside>
