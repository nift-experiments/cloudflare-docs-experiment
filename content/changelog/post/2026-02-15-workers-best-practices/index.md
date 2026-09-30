<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 15, 2026</time><h2 id="post-title">New Best Practices guide for Workers</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>A new <a href="/workers/best-practices/workers-best-practices/">Workers Best Practices</a> guide provides opinionated recommendations for building fast, reliable, observable, and secure Workers. The guide draws on production patterns, Cloudflare internal usage, and best practices observed from developers building on Workers.</p>
<p>Key guidance includes:</p>
<ul>
<li><strong>Keep your compatibility date current and enable <code>nodejs_compat</code></strong> — Ensure you have access to the latest runtime features and Node.js built-in modules.</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17799.md")</div>
- **Generate binding types with `wrangler types`** — Never hand-write your `Env` interface. Let Wrangler generate it from your actual configuration to catch mismatches at compile time.
- **Stream request and response bodies** — Avoid buffering large payloads in memory. Use `TransformStream` and `pipeTo` to stay within the 128 MB memory limit and improve time-to-first-byte.
- **Use bindings, not REST APIs** — Bindings to KV, R2, D1, Queues, and other Cloudflare services are direct, in-process references with no network hop and no authentication overhead.
- **Use Queues and Workflows for background work** — Move long-running or retriable tasks out of the critical request path. Use Queues for simple fan-out and buffering, and Workflows for multi-step durable processes.
- **Enable Workers Logs and Traces** — Configure observability before deploying to production so you have data when you need to debug.
- **Avoid global mutable state** — Workers reuse isolates across requests. Storing request-scoped data in module-level variables causes cross-request data leaks.
- **Always `await` or `waitUntil` your Promises** — Floating promises cause silent bugs and dropped work.
- **Use Web Crypto for secure token generation** — Never use `Math.random()` for security-sensitive operations.
<p>To learn more, refer to <a href="/workers/best-practices/workers-best-practices/">Workers Best Practices</a>.</p>
</div></article></div>
