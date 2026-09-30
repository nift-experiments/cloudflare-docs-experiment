<h1 id="changelog">Changelog</h1>

<h2 id="up-to-10x-faster-cached-queries-for-hyperdrive"><a href="/changelog/post/2024-12-11-hyperdrive-caching-at-edge/">Up to 10x faster cached queries for Hyperdrive</a></h2>
<p><em>2024-12-11</em></p>
<p>Hyperdrive now caches queries in all Cloudflare locations, decreasing cache hit latency by up to 90%.</p>
<p>When you make a query to your database and Hyperdrive has cached the query results, Hyperdrive will now return the results from the nearest cache. By caching data closer to your users, the latency for cache hits reduces by up to 90%.</p>
<p>This reduction in cache hit latency is reflected in a reduction of the session duration for all queries (cached and uncached) from Cloudflare Workers to Hyperdrive, as illustrated below.</p>
<p><img src="/assets/upstream/images/hyperdrive/changelog/hyperdrive-edge-caching-metrics.png" alt="Hyperdrive edge caching improves average session duration for database queries" /></p>
<p><em>P50, P75, and P90 Hyperdrive session latency for all client connection sessions (both cached and uncached queries) for Hyperdrive configurations with caching enabled during the rollout period.</em></p>
<p>This performance improvement is applied to all new and existing Hyperdrive configurations that have caching enabled.</p>
<p>For more details on how Hyperdrive performs query caching, refer to the <a href="/hyperdrive/concepts/how-hyperdrive-works/#3-query-caching">Hyperdrive documentation</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/storage/4/">Previous</a><span>Page 5 of 5</span></nav>
