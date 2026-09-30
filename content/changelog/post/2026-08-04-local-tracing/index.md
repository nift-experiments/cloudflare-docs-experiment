<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 4, 2026</time><h2 id="post-title">AI agents can debug Workers with local tracing</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><code>wrangler dev</code> and <code>vite dev</code> automatically capture structured OpenTelemetry traces and correlated console logs during local Worker invocations.</p>
<h4 id="debug-with-ai-agents">Debug with AI agents</h4>
<p>When the tooling detects an AI agent session, it prints a terminal hint pointing to the <a href="/workers/local-development/local-explorer/#api">Local Explorer API</a> at <code>/cdn-cgi/local/explorer/api</code>. The API serves an OpenAPI schema and exposes a read-only observability query endpoint for discovering telemetry, querying traces and logs, and inspecting binding state.</p>
<p>The agent can identify the exact failing operation, fix the code, rerun the request, and verify the result. This debug loop requires no deployment or temporary logs.</p>
<h4 id="inspect-traces-in-local-explorer">Inspect traces in Local Explorer</h4>
<p>Humans can inspect the same <a href="/workers/observability/traces/">traces</a> and correlated console logs in the Local Explorer browser UI. Each trace shows spans, timing, attributes, and errors.</p>
<p><img src="/assets/upstream/images/workers/observability/local-trace-failed-request.png" alt="Local Explorer showing a failed Worker trace with spans, timing, and errors" /></p>
<p>Automatic spans cover handler calls, outbound <code>fetch()</code> calls, and binding calls. Custom spans appear alongside these automatic spans.</p>
<p>For more details, refer to the <a href="/workers/local-development/local-explorer/">Local Explorer documentation</a>.</p>
</div></article></div>
