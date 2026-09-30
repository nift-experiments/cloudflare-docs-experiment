<p>The Images batch API lets you make several requests in sequence while bypassing Cloudflare’s global API rate limits.</p>
<p>To use the Images batch API, you will need to obtain a batch token and use the token to make several requests. The requests authorized by this batch token are made to a separate endpoint and do not count toward the global API rate limits. Each token is subject to a rate limit of 200 requests per second. You can use multiple tokens if you require higher throughput to the Cloudflare Images API.</p>
<p>To obtain a token, you can use the new <code>images/v1/batch_token</code> endpoint as shown in the example below.</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v1/batch_token&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;&#10;&#35; Response:&#10;{&#10;  &quot;result&quot;: {&#10;    &quot;token&quot;: &quot;&lt;BATCH_TOKEN&gt;&quot;,&#10;    &quot;expiresAt&quot;: &quot;2023-08-09T15:33:56.273411222Z&quot;&#10;  },&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>After getting your token, use it to make requests for:</p>
<ul>
<li><a href="/api/resources/images/subresources/v1/methods/create/">Upload an image</a> - <code>POST /images/v1</code></li>
<li><a href="/api/resources/images/subresources/v1/methods/delete/">Delete an image</a> - <code>DELETE /images/v1/{identifier}</code></li>
<li><a href="/api/resources/images/subresources/v1/methods/get/">Image details</a> - <code>GET /images/v1/{identifier}</code></li>
<li><a href="/api/resources/images/subresources/v1/methods/edit/">Update image</a> - <code>PATCH /images/v1/{identifier}</code></li>
<li><a href="/api/resources/images/subresources/v2/methods/list/">List images V2</a> - <code>GET /images/v2</code></li>
<li><a href="/api/resources/images/subresources/v2/subresources/direct_uploads/methods/create/">Direct upload V2</a> - <code>POST /images/v2/direct_upload</code></li>
</ul>
<p>These options use a different host and a different path with the same method, request, and response bodies.</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/images/v2&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<pre><code class="language-bash">curl &quot;https://batch.imagedelivery.net/images/v1&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;BATCH_TOKEN&gt;&quot;&#10;</code></pre>
