<p>If your site is still using deprecated features for <a href="/fundamentals/api/reference/deprecations/#2024-08-05">Auto Minify</a>, turn off Auto Minify via API.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>You will need an <a href="/fundamentals/api/get-started/create-token/">API token</a> with the following permissions:</p>
<ul>
<li><em>Zone</em> &gt; <em>Zone Settings</em> &gt; <em>Edit</em></li>
<li><em>Zone</em> &gt; <em>Zone Settings</em> &gt; <em>Read</em></li>
</ul>
<h2 id="optional-check-zone-status">(Optional) Check zone status</h2>
<p>To check your zone's Auto Minify status, send a <code>GET</code> request to the <code>/zones/{zone_id}/settings/minify</code> endpoint.</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/minify&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;minify&quot;,&#10;		&quot;value&quot;: { &quot;css&quot;: &quot;off&quot;, &quot;html&quot;: &quot;off&quot;, &quot;js&quot;: &quot;off&quot; },&#10;		&quot;modified_on&quot;: null,&#10;		&quot;editable&quot;: true&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>If any of the values in the highlighted line are <code>&quot;on&quot;</code>, then you need to turn them off.</p>
<h2 id="turn-off-auto-minify-using-the-api">Turn off Auto Minify using the API</h2>
<p>To turn off Auto Minify for your zone, send a <code>PATCH</code> request to the <code>/zones/{zone_id}/settings/minify</code> endpoint. The value for <code>success</code> in the response should be <code>true</code>.</p>
<pre><code class="language-bash">curl --request PATCH \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/minify&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{ &quot;value&quot;: { &quot;css&quot;: &quot;off&quot;,&quot;html&quot;: &quot;off&quot;,&quot;js&quot;: &quot;off&quot; } }&#x27;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;minify&quot;,&#10;		&quot;value&quot;: { &quot;js&quot;: &quot;off&quot;, &quot;css&quot;: &quot;off&quot;, &quot;html&quot;: &quot;off&quot; },&#10;		&quot;modified_on&quot;: &quot;2024-11-15T19:32:20.882640Z&quot;,&#10;		&quot;editable&quot;: true&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
