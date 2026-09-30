<h2 id="optimize-cache-ratios">Optimize cache ratios</h2>
<p>Your cache ratio measures how often Cloudflare serves content from cache instead of contacting your origin server. A higher ratio means faster responses for visitors and less traffic to your origin.</p>
<p>Depending on the <a href="/cache/concepts/cache-responses/">cache status</a> you receive, you can make modifications to improve your cache ratio.</p>
<ul>
<li><strong>Dynamic</strong>: The resource was not eligible for caching. This is the default response for many file types including HTML. To cache additional content, refer to <a href="/cache/how-to/cache-rules/">Cache Rules</a>.</li>
<li><strong>Revalidated</strong>: The resource was in cache but Cloudflare confirmed with your origin that it was still current before serving it. To address an atypical quantity of revalidated content, consider <a href="/cache/how-to/cache-rules/settings/#edge-ttl">increasing your Edge Cache TTLs</a> (how long Cloudflare considers cached content fresh before checking your origin).</li>
<li><strong>Expired</strong>: The cached resource's TTL elapsed before it was requested again. Consider <a href="/cache/how-to/cache-rules/settings/#edge-ttl">extending Edge Cache TTLs</a> for these resources via a Cache Rule, or configure your origin to return <a href="/cache/concepts/cache-control/">revalidation headers</a> (<code>Last-Modified</code> or <code>ETag</code>) so Cloudflare can confirm content is still current without downloading it again.</li>
<li><strong>Miss</strong>: The resource was not found in cache and was served from your origin. Although tricky to optimize, there are a few potential remedies:
<ul>
<li><a href="/cache/how-to/tiered-cache/#enable-tiered-cache">Enable Tiered Cache</a> to check an upper-tier Cloudflare data center before contacting your origin server.</li>
<li><a href="/cache/how-to/cache-rules/examples/custom-cache-key/">Create a custom cache key</a> so that multiple URLs match the same cached resource, for example by ignoring the query string.</li>
</ul>
</li>
</ul>
<h2 id="troubleshoot-cache-performance-with-example-reports">Troubleshoot cache performance with example reports</h2>
<p>Use <a href="/cache/performance-review/cache-analytics/">Cache Analytics</a> to identify cache performance issues. The following examples show how to filter for common problems and resolve them.</p>
<ul>
<li>
<p>Not caching HTML.</p>
<ul>
<li>Identify the issue: Select <strong>Add filter</strong> and select <strong>Cache status equals Dynamic</strong>.</li>
<li>Resolution: Set a Cloudflare Cache Rule to <a href="/cache/how-to/cache-rules/examples/cache-everything/">cache dynamic content</a>.</li>
</ul>
</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3800.md")
</aside>
<ul>
<li>
<p>Short cache expiration TTL.</p>
<ul>
<li>Identify the issue: Select <strong>Add filter</strong> and select <strong>Cache status equals Revalidated</strong>.</li>
<li>Resolution: <a href="/cache/how-to/cache-rules/examples/edge-ttl/">Increase Cloudflare's Edge Cache TTL via a Cache Rule</a>.</li>
</ul>
</li>
<li>
<p>Need to enable Tiered Cache or custom cache key.</p>
<ul>
<li>Identify the issue: Select <strong>Add filter</strong> and select <strong>Cache status equals Miss</strong>.</li>
<li>Resolution: <a href="/cache/how-to/tiered-cache/#enable-tiered-cache">Enable Tiered Cache</a> or <a href="/cache/how-to/cache-rules/examples/custom-cache-key/">create a custom cache key</a>.</li>
</ul>
</li>
</ul>
