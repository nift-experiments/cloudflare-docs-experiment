<p>Operations are performed by Cache Reserve on behalf of the user to write data from the origin to Cache Reserve and to pass that data downstream to other parts of Cloudflare’s network. These operations are managed internally by Cloudflare.</p>
<h4 id="class-a-operations-writes">Class A operations (writes)</h4>
<p>Class A operations are performed based on cache misses from Cloudflare’s CDN. When a request cannot be served from cache, it will be fetched from the origin and written to cache reserve as well as our edge caches on the way back to the visitor.</p>
<h4 id="class-b-operations-reads">Class B operations (reads)</h4>
<p>Class B operations are performed when data needs to be fetched from Cache Reserve to respond to a miss in the edge cache.</p>
<h4 id="purge">Purge</h4>
<p>Asset purges are free operations.</p>
<p>Cache Reserve will be instantly purged along with edge cache when you send a purge by URL request. Refer to <a href="/cache/how-to/purge-cache/">cache configurations</a> for details.</p>
<p>Other purge methods, such as purge by tag, host, prefix, or purge everything will force an attempt to <a href="/cache/concepts/cache-responses/#revalidated">revalidate</a> on the subsequent request for the Cache Reserve asset. Note that assets purged this way will still incur storage costs until their retention TTL expires.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13858.md")
</aside>
