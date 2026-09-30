<p>To maintain optimal site performance, Cloudflare strongly recommends using single-file (by URL) purging instead of a complete cache purge.</p>
<p>Purging everything instantly clears all resources from your CDN cache in all Cloudflare data centers. Each new request for a purged resource returns to your origin server to validate the resource. If the cached version is no longer valid, Cloudflare fetches the latest version from your origin server and caches it.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3867.md")
</aside>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Configuration</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Under <strong>Purge Cache</strong>, select <strong>Purge Everything</strong>. A warning window appears.</li>
<li>If you agree, select <strong>Purge Everything</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3866.md")
</aside>
<p>For information on rate limits, refer to the <a href="/cache/how-to/purge-cache/#availability-and-limits">Availability and limits</a> section.</p>
<h2 id="resulting-cache-status">Resulting cache status</h2>
<p>Purge Everything invalidates the resource, resulting in the <code>CF-Cache-Status</code> header indicating <a href="/cache/concepts/cache-responses/#expired"><code>EXPIRED</code></a> for subsequent requests.</p>
