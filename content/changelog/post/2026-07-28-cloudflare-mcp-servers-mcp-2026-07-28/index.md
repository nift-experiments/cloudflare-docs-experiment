<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 28, 2026</time><h2 id="post-title">Cloudflare MCP servers support the new MCP 2026-07-28 Specification</h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>Cloudflare's <a href="/agents/model-context-protocol/cloudflare/servers-for-cloudflare/#product-specific-mcp-servers">product-specific MCP servers</a> now support the new MCP 2026-07-28 Specification. Each request runs on a fresh stateless server without an MCP protocol session or protocol-specific Durable Object.</p>
<p>The <code>/mcp</code> endpoint also accepts stateless requests from 2025 Streamable HTTP clients. Most clients can reconnect without configuration changes.</p>
<p>Use <code>/mcp</code> for new connections. Historical <code>/sse</code> URLs continue to work as aliases for the same Streamable HTTP handler, but they no longer serve the deprecated HTTP+SSE transport. If a client forces SSE transport, change it to Streamable HTTP or automatic transport detection.</p>
</div></article></div>
