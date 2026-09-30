<p>You can instantly purge their cache by URL prefix or path separators in their URL. For an example URL like <code>https://www.example.com/foo/bar/baz/qux.jpg</code>, valid purge requests include:</p>
<ul>
<li><code>www.example.com</code></li>
<li><code>www.example.com/foo</code></li>
<li><code>www.example.com/foo/bar</code></li>
<li><code>www.example.com/foo/bar/baz</code></li>
<li><code>www.example.com/foo/bar/baz/qux.jpg</code></li>
</ul>
<p>Purging by prefix is useful in different scenarios, such as:</p>
<ul>
<li>Purging everything within a directory.</li>
<li>Increasing control over cached objects in a path.</li>
<li>Simplifying the number of purge calls sent.</li>
</ul>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Configuration</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Under <strong>Purge Cache</strong>, select <strong>Custom Purge</strong>. The <strong>Custom Purge</strong> window appears.</li>
<li>Under <strong>Purge by</strong>, select <strong>Prefix</strong>.</li>
<li>Follow the syntax instructions.
<ul>
<li>One prefix per line.</li>
<li>Maximum 100 prefixes per request.</li>
</ul>
</li>
<li>Enter the appropriate value(s) in the text field using the format shown in the example.</li>
<li>Select <strong>Purge</strong>.</li>
</ol>
<p>For information on rate limits, refer to the <a href="/cache/how-to/purge-cache/#availability-and-limits">Availability and limits</a> section.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/3864.md")
</aside>
<h2 id="resulting-cache-status">Resulting cache status</h2>
<p>Purging by prefix deletes the resource, causing <code>CF-Cache-Status</code> header to show <a href="/cache/concepts/cache-responses/#miss"><code>MISS</code></a> for the subsequent request.</p>
<p>If <a href="/cache/how-to/tiered-cache/">tiered cache</a> is used, purging by prefix may return <code>EXPIRED</code>, as the lower tier tries to revalidate with the upper tier to reduce load on the latter.
Depending on whether the upper tier has the resource or not, and whether the end user is reaching the lower tier or the upper tier, <code>EXPIRED</code> or <code>MISS</code> are returned.</p>
<h2 id="limitations">Limitations</h2>
<p>There are several limitations regarding purge by prefix:</p>
<ul>
<li>Path separators are limited to 31 for a prefix <code>(example.com/a/b/c/d/e/f/g/h/i/j/k/l/m…)</code>.</li>
<li>Purge requests are limited to 100 prefixes per request.</li>
<li><a href="/api/resources/cache/methods/purge/">Purge rate-limits apply</a>.</li>
<li>URI query strings &amp; fragments cannot purge by prefix:
<ul>
<li><code>www.example.com/foo?a=b</code> (query string)</li>
<li><code>www.example.com/foo#bar</code> (fragment)</li>
</ul>
</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning-1">Warning</h3>
@markup("md", "content/.markup/bodies/3863.md")
</aside>
<h2 id="purge-by-prefix-normalization">Purge by prefix normalization</h2>
<p>Using purge by prefix normalization, when a purge by prefix request comes into Cloudflare for a normalized URL path, the purge service respects the <a href="/rules/normalization/">URL normalization</a> and purges the normalized URL.</p>
<h3 id="how-does-url-normalization-work">How does URL Normalization work</h3>
<p>Take the following website as an example: <code>https://cloudflare.com/انشاء-موقع-الكتروني/img_1.jpg</code>. The table below shows you how Cloudflare’s cache views these paths with <a href="/rules/normalization/">normalization on/off</a>.</p>
<table>
<tbody>
<th colspan="5" rowspan="1">
      Request from visitor to EDGE
</th>
<th colspan="5" rowspan="1">
      What Cloudflare cache sees with Normalize Incoming URLs ON
</th>
<th colspan="5" rowspan="1">
      What Cloudflare cache sees with Normalize Incoming URLs OFF
</th>
<tr>
<td colspan="5" rowspan="1">
        <code>https://cloudflare.com/انشاء-موقع-الكتروني/img_1.jpg</code>
</td>
<td colspan="5" rowspan="1">
        <code>https://cloudflare.com/%D8%A7%D9%86%D8%B4%D8%A7%D8%A1-%D9%85%D9%88%D9%82%D8%B9-%D8%A7%D9%84%D9%83%D8%AA%D8%B1%D9%88%D9%86%D9%8A/img_1.jpg</code>
</td>
<td colspan="5" rowspan="1">
        <code>https://cloudflare.com/انشاء-موقع-الكتروني/img_1.jpg</code>
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
        <code>https://cloudflare.com/%D8%A7%D9%86%D8%B4%D8%A7%D8%A1-%D9%85%D9%88%D9%82%D8%B9-%D8%A7%D9%84%D9%83%D8%AA%D8%B1%D9%88%D9%86%D9%8A/img_1.jpg</code>
</td>
<td colspan="5" rowspan="1">
        <code>https://cloudflare.com/%D8%A7%D9%86%D8%B4%D8%A7%D8%A1-%D9%85%D9%88%D9%82%D8%B9-%D8%A7%D9%84%D9%83%D8%AA%D8%B1%D9%88%D9%86%D9%8A/img_1.jpg</code>
</td>
<td colspan="5" rowspan="1">
        <code>https://cloudflare.com/%D8%A7%D9%86%D8%B4%D8%A7%D8%A1-%D9%85%D9%88%D9%82%D8%B9-%D8%A7%D9%84%D9%83%D8%AA%D8%B1%D9%88%D9%86%D9%8A/img_1.jpg</code>
</td>
</tr>
<tr>
<td colspan="5" rowspan="1">
        <code>https://cloudflare.com/hello/img_1.jpg</code>
</td>
<td colspan="5" rowspan="1">
        <code>https://cloudflare.com/hello/img_1.jpg</code>
</td>
<td colspan="5" rowspan="1">
        <code>https://cloudflare.com/hello/img_1.jpg</code>
</td>
</tr>
</tbody>
</table>
<p>As shown above, with URL normalization <strong>ON</strong>, visitors to the two URLs, <code>https://cloudflare.com/%D8%A7%D9%86%D8%B4%D8%A7%D8%A1-%D9%85%D9%88%D9%82%D8%B9-%D8%A7%D9%84%D9%83%D8%AA%D8%B1%D9%88%D9%86%D9%8A/img_1.jpg</code> and <code>https://cloudflare.com/انشاء-موقع-الكتروني/img_1.jpg</code>, will be served the same cached asset. Purging <code>https://cloudflare.com/%D8%A7%D9%86%D8%B4%D8%A7%D8%A1-%D9%85%D9%88%D9%82%D8%B9-%D8%A7%D9%84%D9%83%D8%AA%D8%B1%D9%88%D9%86%D9%8A/img_1.jpg</code> will instantly purge that asset for both visitors.</p>
