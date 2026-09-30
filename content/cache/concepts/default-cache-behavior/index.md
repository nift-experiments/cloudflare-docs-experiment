<p>Cloudflare respects the origin web server’s cache headers in the following order unless an <a href="/cache/how-to/cache-rules/settings/#edge-ttl">Edge Cache TTL cache rule</a> overrides the headers. Refer to the <a href="/cache/how-to/configure-cache-status-code/#edge-ttl">Edge TTL</a> section for details on default TTL behavior.</p>
<ul>
<li>Cloudflare <strong>does not</strong> cache the resource when:
<ul>
<li>The <code>Cache-Control</code> header is set to <code>private</code>, <code>no-store</code>, <code>no-cache</code>, or <code>max-age=0</code>.</li>
<li>The <a href="/cache/concepts/cache-behavior/#interaction-of-set-cookie-response-header-with-cache">Set-Cookie header</a> exists.</li>
<li>The HTTP request method is anything other than a <code>GET</code>.</li>
</ul>
</li>
<li>Cloudflare <strong>does</strong> cache the resource when:
<ul>
<li>The <code>Cache-Control</code> header is set to <code>public</code> and <code>max-age</code> is greater than 0.</li>
<li>The <code>Expires</code> header is set to a future date.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3818.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3817.md")
</aside>
<p>When <a href="/cache/concepts/cache-control/">Origin Cache Control</a> is enabled on an Enterprise customer’s website, it indicates that Cloudflare should strictly respect <code>Cache-Control</code> directives received from the origin server. Free, Pro and Business customers have this feature enabled by default. For a list of directives and behaviors when Origin Cache-Control is enabled or disabled, refer to <a href="/cache/concepts/cache-control/#cache-control-directives">Cache-Control directives</a>.</p>
<h2 id="client-side-range-requests">Client-side range requests</h2>
<p>Clients can use the HTTP <code>Range</code> header to request part of a file. Cloudflare can serve these requests from complete or partial cached files. Response behavior depends on the request method, range syntax, conditional headers, content encoding, and cache eligibility.</p>
<p>For complete response and origin requirements, refer to <a href="/cache/reference/range-requests/">Range request behavior</a>.</p>
<h2 id="request-collapsing">Request collapsing</h2>
<p>When multiple requests arrive simultaneously at a single Cloudflare data center for the same asset that is not in cache (a cache miss), Cloudflare uses a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/3819.md")
</div> to avoid sending duplicate requests to your origin. Only the first request is forwarded to the origin to fetch the asset. The remaining requests wait for the first request to complete, after which the response is [streamed](https://blog.cloudflare.com/introducing-concurrent-streaming-acceleration/) to all waiting requests.
<p>The cache lock ensures that Cloudflare only sends one request at a time to the origin for a given asset from a single location in Cloudflare's network, preventing the origin from receiving excessive traffic.</p>
<h2 id="default-cached-file-extensions">Default cached file extensions</h2>
<p>Cloudflare only caches based on file extension and not by MIME type. The Cloudflare CDN does not cache HTML or JSON by default. Additionally, by default Cloudflare caches a website's robots.txt.</p>
<table>
<thead>
<tr>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>7Z</td>
<td>CSV</td>
<td>GIF</td>
<td>MIDI</td>
<td>PNG</td>
<td>TIF</td>
<td>ZIP</td>
</tr>
<tr>
<td>AVI</td>
<td>DOC</td>
<td>GZ</td>
<td>MKV</td>
<td>PPT</td>
<td>TIFF</td>
<td>ZST</td>
</tr>
<tr>
<td>AVIF</td>
<td>DOCX</td>
<td>ICO</td>
<td>MP3</td>
<td>PPTX</td>
<td>TTF</td>
<td></td>
</tr>
<tr>
<td>APK</td>
<td>DMG</td>
<td>ISO</td>
<td>MP4</td>
<td>PS</td>
<td>WEBM</td>
<td></td>
</tr>
<tr>
<td>BIN</td>
<td>EJS</td>
<td>JAR</td>
<td>OGG</td>
<td>RAR</td>
<td>WEBP</td>
<td></td>
</tr>
<tr>
<td>BMP</td>
<td>EOT</td>
<td>JPG</td>
<td>OTF</td>
<td>SVG</td>
<td>WOFF</td>
<td></td>
</tr>
<tr>
<td>BZ2</td>
<td>EPS</td>
<td>JPEG</td>
<td>PDF</td>
<td>SVGZ</td>
<td>WOFF2</td>
<td></td>
</tr>
<tr>
<td>CLASS</td>
<td>EXE</td>
<td>JS</td>
<td>PICT</td>
<td>SWF</td>
<td>XLS</td>
<td></td>
</tr>
<tr>
<td>CSS</td>
<td>FLAC</td>
<td>MID</td>
<td>PLS</td>
<td>TAR</td>
<td>XLSX</td>
<td></td>
</tr>
</tbody>
</table>
<p>To cache additional content, refer to <a href="/cache/how-to/cache-rules/">Cache Rules</a> to create a rule to cache everything.</p>
<h2 id="edge-ttl">Edge TTL</h2>
<p>By default, Cloudflare caches certain HTTP response codes with the following Edge Cache TTL when a <code>cache-control</code> directive or <code>expires</code> response header are not present.</p>
<table>
<thead>
<tr>
<th>HTTP status code</th>
<th>Default TTL</th>
</tr>
</thead>
<tbody>
<tr>
<td>200, 206, 301</td>
<td>120m</td>
</tr>
<tr>
<td>302, 303</td>
<td>20m</td>
</tr>
<tr>
<td>404, 410</td>
<td>3m</td>
</tr>
</tbody>
</table>
<p>All other status codes are not cached by default.</p>
<h2 id="customization-options-and-limits">Customization options and limits</h2>
<p>Cloudflare’s CDN provides several cache customization options:</p>
<ul>
<li>Caching behavior for individual URLs via <a href="/cache/how-to/cache-rules/">Cache Rules</a></li>
</ul>
<div class="nb-dash-button"></div>
<ul>
<li>Customize caching with <a href="/workers/reference/how-the-cache-works/">Cloudflare Workers</a></li>
<li>Adjust caching level, cache TTL, and more in the Caching page in the Cloudflare dashboard:</li>
</ul>
<div class="nb-dash-button"></div>
<h3 id="upload-limits">Upload limits</h3>
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
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Max upload size</td>
<td>100 MB</td>
<td>100 MB</td>
<td>200 MB</td>
<td>Up to 5 GB</td>
</tr>
</tbody>
</table>
<p>Customers can adjust the <strong>Maximum Upload Size</strong> from the zone's <strong>Network</strong> page. Enterprise customers can self-serve any value up to 5 GB. Uploads larger than 5 GB require additional configuration — contact your account team or <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3816.md")
</aside>
<p>If you require a larger upload, you can group requests into smaller chunks, upload the full resource through a <a href="/dns/proxy-status/">DNS-only (unproxied) DNS record</a> or <a href="/billing/manage/change-plan/">upgrade your plan</a>.</p>
<h3 id="cacheable-size-limits">Cacheable size limits</h3>
<p>Cloudflare cacheable file limits:</p>
<ul>
<li>Free, Pro and Business customers have a limit of 512 MB.</li>
<li>For Enterprise customers the default maximum cacheable file size is 5 GB. Contact your account team or <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a> to request a limit increase.</li>
</ul>
<h2 id="when-does-cloudflare-cache-successfully">When does Cloudflare cache successfully?</h2>
<p>The connection status between visitors and Cloudflare can vary, affecting whether Cloudflare caches the content or not. If Cloudflare has already established a connection to the origin and started fetching the content, it will continue to retrieve and cache the entire content, even if the visitor disconnects midway. However, if a visitor disconnects before the origin responds to Cloudflare's request, no content will have been fetched yet, so Cloudflare will not start caching the content.</p>
