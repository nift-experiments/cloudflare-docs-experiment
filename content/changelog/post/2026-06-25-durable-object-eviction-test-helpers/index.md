<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 25, 2026</time><h2 id="post-title">Test Durable Object eviction with new cloudflare:test helpers</h2>
<div class="changelog-badges"><span>durable-objects</span><span>workers</span></div><div class="changelog-body"><p>The <code>@cloudflare/vitest-pool-workers</code> package now includes <code>evictDurableObject</code> and <code>evictAllDurableObjects</code> test helpers, exported from <code>cloudflare:test</code>.</p>
<p>These helpers let you test how a Durable Object behaves across evictions, simulating the production lifecycle where an idle Durable Object can be evicted from memory.</p>
<p>For more context, refer to <a href="/durable-objects/concepts/durable-object-lifecycle/">Lifecycle of a Durable Object</a>.</p>
<pre><code class="language-ts">import { evictDurableObject, evictAllDurableObjects } from &quot;cloudflare:test&quot;;&#10;import { env } from &quot;cloudflare:workers&quot;;&#10;&#10;const id = env.COUNTER.idFromName(&quot;my-counter&quot;);&#10;const stub = env.COUNTER.get(id);&#10;&#10;// Evict the Durable Object instance pointed to by a specific stub&#10;await evictDurableObject(stub);&#10;&#10;// Close WebSockets instead of hibernating them&#10;await evictDurableObject(stub, { webSockets: &quot;close&quot; });&#10;&#10;// Evict all currently-running Durable Objects in evictable namespaces&#10;await evictAllDurableObjects();&#10;</code></pre>
<p>These helpers are available in <code>@cloudflare/vitest-pool-workers@0.16.20</code> and later.</p>
<p>Learn more in the <a href="/workers/testing/vitest-integration/test-apis/#durable-objects">Test APIs reference</a> and the <a href="/durable-objects/examples/testing-with-durable-objects/#testing-eviction">Testing Durable Objects guide</a>.</p>
</div></article></div>
