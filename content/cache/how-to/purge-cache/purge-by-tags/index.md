<p>Cache-tag purging makes multi-file purging easier because you can instantly bulk purge by adding cache-tags to your assets, such as webpages, image files, and more.</p>
<h2 id="general-workflow-for-cache-tags">General workflow for cache-tags</h2>
<ol>
<li>Add tags to the <code>Cache-Tag</code> HTTP response header from your origin web server for your web content, such as pages, static assets, etc.</li>
<li><a href="/dns/proxy-status/">Ensure your web traffic is proxied</a> through Cloudflare.</li>
<li>Cloudflare associates the tags in the <code>Cache-Tag</code> HTTP header with the content being cached.</li>
<li>Use specific cache-tags to instantly purge your Cloudflare CDN cache of all content containing that cache-tag from your dashboard or <a href="/api/resources/cache/methods/purge/">using our API</a>.</li>
<li>Cloudflare forces a <a href="/cache/concepts/cache-responses/#miss">cache MISS</a> on content with the purged cache-tag.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/3868.md")
</aside>
<h2 id="add-cache-tag-http-response-headers">Add Cache-Tag HTTP response headers</h2>
<p>You add cache-tags to your web content in <code>Cache-Tag</code> HTTP response headers to allow the client and server to pass additional information in requests or responses. HTTP headers consist of a specific case-insensitive name followed by a colon <code>:</code> and the valid value, for example, <code>Cache-Tag:tag1,tag2,tag3</code>. Use commas to separate the tags when you want to use multiple cache-tags.</p>
<p>When your content reaches our edge network, Cloudflare:</p>
<ul>
<li>Removes the <code>Cache-Tag</code> HTTP header before sending the response to your website visitor or passing the response to a <a href="/workers/">Worker</a>. Your end users or Worker never see <code>Cache-Tag</code> HTTP headers on your Cloudflare-enabled website.</li>
<li>Removes whitespaces from the header and any before and after cache-tag names: <code>tag1</code>, <code>tag2</code> and <code>tag1,tag2</code> are considered the same.</li>
<li>Removes all repeated and trailing commas before applying cache-tags: <code>tag1,,,tag2</code> and <code>tag1,tag2</code> are considered the same.</li>
</ul>
<h2 id="a-few-things-to-remember">A few things to remember</h2>
<ul>
<li>A single HTTP response can have more than one <code>Cache-Tag</code> HTTP header field.</li>
<li>The minimum length of a cache-tag is one byte.</li>
<li>Individual tags do not have a maximum length, but the aggregate <code>Cache-Tag</code> HTTP header cannot exceed 16 KB after the header field name, which is approximately 1,000 unique tags. Length includes whitespace and commas but does not include the header field name.</li>
<li>For cache purges, the maximum length of a cache-tag in an API call is 1,024 characters.</li>
<li>The <code>Cache-Tag</code> HTTP header must only contain printable ASCII encoded characters.</li>
<li>Spaces are not allowed in cache-tags.</li>
<li>Case is not sensitive. For example, <code>Tag1</code> and <code>tag1</code> are considered the same.</li>
</ul>
<h2 id="purge-using-cache-tags">Purge using cache-tags</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Configuration</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Under <strong>Purge Cache</strong>, select <strong>Custom Purge</strong>. The <strong>Custom Purge</strong> window appears.</li>
<li>Under <strong>Purge by</strong>, select <strong>Tag</strong>.</li>
<li>In the text box, enter your tags to use to purge the cached resources. To purge multiple cache-tagged resources, separate each tag with a comma or have one tag per line. You can purge up to 100 tags at a time.</li>
<li>Select <strong>Purge</strong>.</li>
</ol>
<p>For information on rate limits, refer to the <a href="/cache/how-to/purge-cache/#availability-and-limits">Availability and limits</a> section.</p>
<h2 id="resulting-cache-status">Resulting cache status</h2>
<p>Purging by tag deletes the resource, resulting in the <code>CF-Cache-Status</code> header being set to <a href="/cache/concepts/cache-responses/#miss"><code>MISS</code></a> for subsequent requests.</p>
<p>If <a href="/cache/how-to/tiered-cache/">Tiered Cache</a> is used, purging by tag may return <code>EXPIRED</code>, as the lower tier tries to revalidate with the upper tier to reduce load on the latter.
Depending on whether the upper tier has the resource or not, and whether the end user is reaching the lower tier or the upper tier, <code>EXPIRED</code> or <code>MISS</code> are returned.</p>
