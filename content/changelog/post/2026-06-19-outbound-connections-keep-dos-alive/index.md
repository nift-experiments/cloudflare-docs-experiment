<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 19, 2026</time><h2 id="post-title">Outbound connections keep Durable Objects alive</h2>
<div class="changelog-badges"><span>durable-objects</span></div><div class="changelog-body"><p>Durable Objects now remain alive for the duration of active outbound connections created via <a href="/workers/runtime-apis/tcp-sockets/"><code>connect()</code></a> or an outbound WebSocket. Previously, a Durable Object would be evicted after 70-140 seconds of no incoming traffic, even if the object had an open outbound connection, which is a common pattern when streaming responses from a large language model (LLM) over TCP or an outbound WebSocket.</p>
<p>With this change, each active outbound connection prevents eviction. Once all outbound connections close, the standard 70-140 second inactivity window applies before the Durable Object is evicted.</p>
<h4 id="before-streaming-connections-were-cut-off-by-eviction">Before: streaming connections were cut off by eviction</h4>
<p><img src="/assets/upstream/images/durable-objects/outbound-connection-before.svg" alt="Timeline showing a Durable Object evicted 70-140 seconds after the last incoming request, cutting off an in-flight LLM stream while the outbound connection is still open" /></p>
<h4 id="after-active-outbound-connections-keep-the-durable-object-alive">After: active outbound connections keep the Durable Object alive</h4>
<p><img src="/assets/upstream/images/durable-objects/outbound-connection-after.svg" alt="Timeline showing the same outbound stream completing because the active connection keeps the Durable Object alive, with the inactivity window starting only after the connection closes" /></p>
<p>If you are <a href="/agents/">building agents on Cloudflare</a>, this is especially relevant. An agent that streams tokens from an LLM while <a href="/agents/concepts/calling-llms/">calling models</a>, or that performs <a href="/agents/concepts/agentic-patterns/long-running-agents/">long-running tasks</a> over an outbound connection, now stays alive for the duration of that connection instead of being evicted mid-stream.</p>
<p><strong>Limits:</strong></p>
<ul>
<li>Each outbound connection keeps the Durable Object alive for a maximum of <strong>15 minutes</strong>. After 15 minutes, the connection stops preventing eviction (the connection itself continues operating), and the <a href="/durable-objects/concepts/durable-object-lifecycle/">standard eviction rules</a> resume.</li>
<li>The Durable Object's existing <a href="/durable-objects/platform/limits/">per-account instance limits</a> still apply.</li>
</ul>
<p>For more information, refer to <a href="/durable-objects/concepts/durable-object-lifecycle/">Lifecycle of a Durable Object</a>.</p>
</div></article></div>
