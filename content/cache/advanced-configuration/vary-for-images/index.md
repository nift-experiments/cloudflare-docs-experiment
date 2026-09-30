<p>The <code>Vary</code> HTTP response header tells Cloudflare that an origin can serve different versions of the same resource depending on the request headers. For images, this allows your origin to serve modern formats like WebP or AVIF to browsers that support them, while continuing to serve JPEG or PNG to others.</p>
<p>When Cloudflare receives a response with image variants, it caches each variant separately. Subsequent requests from browsers with the same image format preferences are served directly from cache without contacting your origin.</p>
<p>Vary for Images works by parsing the <code>Accept</code> header in each request to determine which image format the browser supports, then serving the matching cached variant.</p>
<p>Vary for images is available for Pro, Business, and Enterprise customers.</p>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="file-extensions">File extensions</h2>
<p>You can use vary for images on the file extensions below if the origin server sends the <code>Vary: Accept</code> response header. If the origin server sends <code>Vary: Accept</code> but does not serve the set variant, the response is not cached and displays <code>BYPASS</code> in the cache status in the response header. Additionally, the list of variant types the origin serves for each extension must be configured so that Cloudflare decides which variant to serve without contacting the origin server.</p>
<details class="nb-details"><summary>File extensions enabled for varying</summary><div class="nb-details-body">
@input("content/.markup/bodies/3840.md")
</div></details>
<h2 id="enable-vary-for-images">Enable vary for images</h2>
<p>Vary for Images is enabled through Cloudflare's API by creating a variants rule. In the examples below, learn how to serve JPEG, WebP, and AVIF variants for <code>.jpeg</code> and <code>.jpg</code> extensions.</p>
<h3 id="create-a-variants-rule">Create a variants rule</h3>
<pre class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/cache/variants \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;value&quot;: {&#10;    &quot;jpeg&quot;: [&#10;      &quot;image/webp&quot;,&#10;      &quot;image/avif&quot;&#10;    ],&#10;    &quot;jpg&quot;: [&#10;      &quot;image/webp&quot;,&#10;      &quot;image/avif&quot;&#10;    ]&#10;  }&#10;}&#x27;</code></pre>
<h3 id="modify-to-only-allow-webp-variants">Modify to only allow WebP variants</h3>
<pre class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/cache/variants \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;value&quot;: {&#10;    &quot;jpeg&quot;: [&#10;      &quot;image/webp&quot;&#10;    ],&#10;    &quot;jpg&quot;: [&#10;      &quot;image/webp&quot;&#10;    ]&#10;  }&#10;}&#x27;</code></pre>
<h3 id="delete-the-rule">Delete the rule</h3>
<pre class="nb-api-request"><code class="language-bash">curl --request DELETE \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/cache/variants \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h3 id="get-the-rule">Get the rule</h3>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/cache/variants \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<p>To learn more about purging varied images, refer to <a href="/cache/how-to/purge-cache/purge-varied-images/">Purge varied images</a>.</p>
<h2 id="limitations">Limitations</h2>
<ul>
<li>For Vary for images to work, your image URLs must include the file extension in the path and not the query string. For example the URL <code>https://example.com/image.jpg</code> is compatible but <code>https://example.com/index.php?file=image.jpg</code> is not compatible.</li>
<li>Your origin must return an image type matching the file extension in the URL when a HTTP client sends no <code>Accept</code> header, or an <code>Accept: */*</code> header. Otherwise, you will see <code>CF-Cache-Status: BYPASS</code> in the HTTP response headers.</li>
</ul>
