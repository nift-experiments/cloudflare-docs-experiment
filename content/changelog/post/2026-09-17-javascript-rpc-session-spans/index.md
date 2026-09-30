<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 17, 2026</time><h2 id="post-title">Workers traces now automatically include JavaScript RPC session spans</h2>
<div class="changelog-badges"><span>workers</span><span>durable-objects</span></div><div class="changelog-body"><p>Workers traces can now follow JavaScript RPC calls across Worker boundaries and into Durable Objects. Previously, a trace stopped at the caller's RPC boundary. The dashboard now shows the caller-side session and method calls alongside the callee invocation, nested calls, and callbacks into another Worker.</p>
<p>A session span covers the lifetime of a caller-side session and groups calls that reuse it. Individual call spans show each method invocation. Execution colors distinguish the Workers or Durable Object entrypoints involved, while arrows mark outgoing and incoming calls. Together, these details show where time was spent, which calls reused a session, and how returned stubs and callbacks fit into the request.</p>
<p><img src="/assets/upstream/images/workers/changelog/jsrpc-session-spans.png" alt="A Workers trace of a Worker-to-Worker RPC session, showing the session span, the caller's getCounter and increment call spans, and the callee's invocation and matching call spans" /></p>
<p>Enable tracing with one setting in your <a href="/workers/wrangler/configuration/#observability">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17815.md")</div>
<p>Cloudflare records these spans automatically. You do not need to change your application code or add an observability SDK.</p>
<p>For supported spans and attributes, refer to <a href="/workers/observability/traces/spans-and-attributes/">Spans and attributes</a>.</p>
</div></article></div>
