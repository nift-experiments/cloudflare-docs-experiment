<ul>
<li><a href="/workers/runtime-apis/cache">Cache Reference</a></li>
<li><a href="/workers/reference/how-the-cache-works/#cache-api">How the Cache works</a>
(note that cache using <code>fetch</code> is unsupported)</li>
</ul>
<h2 id="default-cache">Default Cache</h2>
<p>Access to the default cache is enabled by default:</p>
<pre><code class="language-js">addEventListener(&quot;fetch&quot;, (e) =&gt; {&#10;	e.respondWith(caches.default.match(&quot;http://miniflare.dev&quot;));&#10;});&#10;</code></pre>
<h2 id="named-caches">Named Caches</h2>
<p>You can access a namespaced cache using <code>open</code>. Note that you cannot name your
cache <code>default</code>, trying to do so will throw an error:</p>
<pre><code class="language-js">await caches.open(&quot;cache_name&quot;);&#10;</code></pre>
<h2 id="persistence">Persistence</h2>
<p>By default, cached data is stored in memory. It will persist between reloads,
but not different <code>Miniflare</code> instances. To enable
persistence to the file system, specify the cache persistence option:</p>
<pre><code class="language-js">const mf = new Miniflare({&#10;	cachePersist: true, // Defaults to ./.mf/cache&#10;	cachePersist: &quot;./data&quot;, // Custom path&#10;});&#10;</code></pre>
<h2 id="manipulating-outside-workers">Manipulating Outside Workers</h2>
<p>For testing, it can be useful to put/match data from cache outside a Worker. You
can do this with the <code>getCaches</code> method:</p>
<pre><code class="language-js">import { Miniflare, Response } from &quot;miniflare&quot;;&#10;&#10;const mf = new Miniflare({&#10;	modules: true,&#10;	script: `&#10;  export default {&#10;    async fetch(request) {&#10;      const url = new URL(request.url);&#10;      const cache = caches.default;&#10;      if(url.pathname === &quot;/put&quot;) {&#10;        await cache.put(&quot;https://miniflare.dev/&quot;, new Response(&quot;1&quot;, {&#10;          headers: { &quot;Cache-Control&quot;: &quot;max-age=3600&quot; },&#10;        }));&#10;      }&#10;      return cache.match(&quot;https://miniflare.dev/&quot;);&#10;    }&#10;  }&#10;  `,&#10;});&#10;let res = await mf.dispatchFetch(&quot;http://localhost:8787/put&quot;);&#10;console.log(await res.text()); // 1&#10;&#10;const caches = await mf.getCaches(); // Gets the global caches object&#10;const cachedRes = await caches.default.match(&quot;https://miniflare.dev/&quot;);&#10;console.log(await cachedRes.text()); // 1&#10;&#10;await caches.default.put(&#10;	&quot;https://miniflare.dev&quot;,&#10;	new Response(&quot;2&quot;, {&#10;		headers: { &quot;Cache-Control&quot;: &quot;max-age=3600&quot; },&#10;	}),&#10;);&#10;res = await mf.dispatchFetch(&quot;http://localhost:8787&quot;);&#10;console.log(await res.text()); // 2&#10;</code></pre>
<h2 id="purging">Purging</h2>
<p>You can programmatically purge all entries from a cache using the <code>purgeCache</code> method on the <code>Miniflare</code> instance. This is useful during development when cached assets need to be cleared without restarting the instance:</p>
<pre><code class="language-js">const mf = new Miniflare({ /* options */ });&#10;&#10;// Purge the default cache and get the number of entries purged&#10;const count = await mf.purgeCache();&#10;console.log(`Purged ${count} entries`);&#10;&#10;// Purge a specific named cache&#10;await mf.purgeCache(&quot;my-named-cache&quot;);&#10;</code></pre>
<h2 id="disabling">Disabling</h2>
<p>Both default and named caches can be disabled with the <code>disableCache</code> option.
When disabled, the caches will still be available in the sandbox, they just
won't cache anything. This may be useful during development:</p>
<pre><code class="language-js">const mf = new Miniflare({&#10;	cache: false,&#10;});&#10;</code></pre>
