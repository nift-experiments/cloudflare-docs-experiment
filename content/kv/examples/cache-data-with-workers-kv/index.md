<p class="article-summary">Cache data or API responses in Workers KV to improve application performance</p>
<p>Workers KV can be used as a persistent, single, global cache accessible from Cloudflare Workers to speed up your application.
Data cached in Workers KV is accessible from all other Cloudflare locations as well, and persists until expiry or deletion.</p>
<p>After fetching data from external resources in your Workers application, you can write the data to Workers KV.
On subsequent Worker requests (in the same region or in other regions), you can read the cached data from Workers KV instead of calling the external API.
This improves your Worker application's performance and resilience while reducing load on external resources.</p>
<p>This example shows how you can cache data in Workers KV and read cached data from Workers KV in a Worker application.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/9519.md")
</aside>
<h2 id="cache-data-in-workers-kv-from-your-worker-application">Cache data in Workers KV from your Worker application</h2>
<p>In the following <code>index.ts</code> file, the Worker fetches data from an external server and caches the response in Workers KV. If the data is already cached in Workers KV, the Worker reads the cached data from Workers KV instead of calling the external API.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9522.md")
</div></div>
<p>This code snippet demonstrates how to read and update cached data in Workers KV from your Worker.
If the data is not in the Workers KV cache, the Worker fetches the data from an external server and caches it in Workers KV.</p>
<p>In this example, we convert HTML to JSON to demonstrate how to cache JSON data with Workers KV, but any type of data
can be cached in Workers KV. For instance, you could cache API responses, HTML content, or any other data that you want to persist across requests.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/languages/rust/">Rust support in Workers</a>.</li>
<li><a href="/kv/get-started/">Using KV in Workers</a>.</li>
</ul>
