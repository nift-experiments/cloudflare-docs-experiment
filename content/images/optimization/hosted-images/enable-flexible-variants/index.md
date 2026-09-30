<p>Flexible variants allow you to create variants with dynamic resizing which can provide more options than regular variants allow. This option is not enabled by default.</p>
<h2 id="enable-flexible-variants-via-the-cloudflare-dashboard">Enable flexible variants via the Cloudflare dashboard</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Hosted Images</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select the <strong>Delivery</strong> tab.</p>
</li>
<li>
<p>Enable <strong>Flexible variants</strong>.</p>
</li>
</ol>
<h2 id="enable-flexible-variants-via-the-api">Enable flexible variants via the API</h2>
<p>Make a <code>PATCH</code> request to the <a href="/api/resources/images/subresources/v1/subresources/variants/methods/edit/">Update a variant endpoint</a>.</p>
<pre><code class="language-bash">curl --request PATCH https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1/config \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&quot;flexible_variants&quot;: true}&#x27;&#10;</code></pre>
<p>After activation, you can use <a href="/images/optimization/features/#parameters">optimization parameters</a> on any Cloudflare image. For example,</p>
<p><code>https://imagedelivery.net/{account_hash}/{image_id}/w=400,sharpen=3</code></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9470.md")
</aside>
