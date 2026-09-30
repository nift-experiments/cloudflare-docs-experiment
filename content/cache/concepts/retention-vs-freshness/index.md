<p>In the context of Cloudflare CDN (Content Delivery Network), retention and freshness refer to two separate but related concepts. For an object in cache, freshness is how long it should be considered valid without consulting its source, while retention refers to how long it stays in cache before being removed.</p>
<h2 id="retention">Retention</h2>
<p>When a resource is requested, Cloudflare caches it so that subsequent requests can be served without contacting the origin server. If a cached object is not requested again, it is eventually removed to make room for newer, more popular content. This removal process is called eviction.</p>
<p>Cloudflare uses a Least Recently Used (LRU) algorithm to decide which objects to evict when the cache is full. An object's retention period is how long it stays in cache before being evicted. Retention is determined by the object's relative popularity and the size of the cache, and is not configurable.</p>
<h2 id="freshness-ttl">Freshness (TTL)</h2>
<p>Freshness, also known as Time to Live (TTL), determines how long a cache can use an object without checking with the origin again. For example, if an object has a TTL of five minutes, the cache serves it directly for five minutes after first receiving it. After five minutes, Cloudflare must check with the origin to confirm the object is still valid before serving it again. There are a few ways to configure TTLs for resources served through Cloudflare's CDN:</p>
<ul>
<li>
<p>Include <a href="/cache/concepts/cache-control/">Origin Cache Control</a> or <a href="/cache/concepts/cache-control/">CDN Cache Control</a> directives, like <code>max-age</code> or <code>s-maxage</code>, in the origin cache-control response header.</p>
</li>
<li>
<p>Use <a href="/cache/how-to/cache-rules/">Cache Rules</a> or <a href="/cache/interaction-cloudflare-products/workers/">Workers</a>.</p>
</li>
</ul>
<p>If an object in cache is no longer fresh, Cloudflare revalidates it with the origin. When <a href="/cache/concepts/cache-control/#revalidation"><code>stale-while-revalidate</code></a> is set, revalidation happens asynchronously at expiry — visitors continue to be served from cache while Cloudflare fetches a fresh copy in the background. Without this directive, incoming requests wait for the origin to respond before receiving content. The origin can either confirm the cached object is still valid (refreshing its TTL) or return a new version to replace it. Refer to <a href="/cache/concepts/revalidation/">Revalidation</a> for details.</p>
