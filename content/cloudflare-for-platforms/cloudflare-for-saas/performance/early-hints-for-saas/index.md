<p><a href="/cache/advanced-configuration/early-hints/">Early Hints</a> allows the browser to begin loading resources while the origin server is compiling the full response. This improves webpage’s loading speed for the end user. As a SaaS provider, you may prioritize speed for some of your custom hostnames. Using custom metadata, you can <a href="/cache/advanced-configuration/early-hints/#enable-early-hints">enable Early Hints</a> per custom hostname.</p>
<hr />
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you can employ Early Hints for SaaS, you need to create a custom hostname. Review <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/">Get Started with Cloudflare for SaaS</a> if you have not already done so.</p>
<hr />
<h2 id="enable-early-hints-per-custom-hostname-via-the-api">Enable Early Hints per custom hostname via the API</h2>
<ol>
<li>
<p><a href="/fundamentals/account/find-account-and-zone-ids/">Locate your zone ID</a>, available in the Cloudflare dashboard.</p>
</li>
<li>
<p>Locate your Authentication Key on the <a href="https://dash.cloudflare.com/?to=/:account/profile/api-tokens"><strong>API Tokens</strong></a> page, under <strong>Global API Key</strong>.</p>
</li>
<li>
<p>If you are <a href="/api/resources/custom_hostnames/methods/create/">creating a new custom hostname</a>, make an API call such as the example below, specifying <code>&quot;early_hints&quot;: &quot;on&quot;</code>:</p>
</li>
</ol>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/custom_hostnames \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;hostname&quot;: &quot;&lt;CUSTOM_HOSTNAME&gt;&quot;,&#10;  &quot;ssl&quot;: {&#10;    &quot;method&quot;: &quot;http&quot;,&#10;    &quot;type&quot;: &quot;dv&quot;,&#10;    &quot;settings&quot;: {&#10;      &quot;http2&quot;: &quot;on&quot;,&#10;      &quot;min_tls_version&quot;: &quot;1.2&quot;,&#10;      &quot;tls_1_3&quot;: &quot;on&quot;,&#10;      &quot;early_hints&quot;: &quot;on&quot;&#10;    },&#10;    &quot;bundle_method&quot;: &quot;ubiquitous&quot;,&#10;    &quot;wildcard&quot;: false&#10;  }&#10;}&#x27;</code></pre>
<ol start="4">
<li>For an existing custom hostname, locate the <code>id</code> of that hostname via a <code>GET</code> call:</li>
</ol>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/custom_hostnames \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<ol start="5">
<li>Then make an API call such as the example below, specifying <code>&quot;early_hints&quot;: &quot;on&quot;</code>:</li>
</ol>
<pre class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/custom_hostnames/{custom_hostname_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;		&quot;ssl&quot;: {&#10;			&quot;method&quot;: &quot;http&quot;,&#10;			&quot;type&quot;: &quot;dv&quot;,&#10;			&quot;settings&quot;: {&#10;				&quot;http2&quot;: &quot;on&quot;, // Note: These settings will be set to default if not included when updating early hints&#10;				&quot;min_tls_version&quot;: &quot;1.2&quot;,&#10;				&quot;tls_1_3&quot;: &quot;on&quot;,&#10;				&quot;early_hints&quot;: &quot;on&quot;&#10;				}&#10;			},&#10;	}&#x27;</code></pre>
<p>Currently, all options within <code>settings</code> are required in order to prevent those options from being set to default. You can pull the current settings state prior to updating Early Hints by leveraging the output that returns the <code>id</code> for the hostname.</p>
