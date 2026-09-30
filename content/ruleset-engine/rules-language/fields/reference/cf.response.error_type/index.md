<h1 id="cf-response-error-type">cf.response.error_type</h1>

**Data type:** String

<p>A string with the type of error in the response being returned.</p>

<p>The default value is an empty string (<code>&quot;&quot;</code>).</p>
<p>The available values are the following:</p>
<ul>
<li><code>&quot;managed_challenge&quot;</code></li>
<li><code>&quot;iuam&quot;</code></li>
<li><code>&quot;legacy_challenge&quot;</code></li>
<li><code>&quot;ip_ban&quot;</code></li>
<li><code>&quot;waf&quot;</code></li>
<li><code>&quot;5xx&quot;</code></li>
<li><code>&quot;1xxx&quot;</code></li>
<li><code>&quot;always_online&quot;</code></li>
<li><code>&quot;country_challenge&quot;</code></li>
<li><code>&quot;ratelimit&quot;</code></li>
</ul>
<p>You can use this field to customize the response for a specific type of error (for example, all 1XXX errors or all WAF block actions).</p>
<p><strong>Note</strong>: This field is only available in <a href="/rules/transform/response-header-modification/">Response Header Transform Rules</a> and <a href="/rules/custom-errors/">Custom Errors</a>.</p>

<h2 id="categories">Categories</h2>

- Response

**Keywords:** response, cloudflare

