<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 25, 2026</time><h2 id="post-title">MCP server portals support MCP 2026-07-28 specification</h2>
<div class="changelog-badges"><span>cloudflare-one</span><span>access</span></div><div class="changelog-body"><p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> support the stateless MCP <code>2026-07-28</code> specification for client and upstream server connections.</p>
<p>The portal's <code>/mcp</code> endpoint automatically accepts stateless MCP <code>2026-07-28</code> requests and earlier 2025 Streamable HTTP clients. When the portal connects to an upstream Streamable HTTP server, it checks for MCP <code>2026-07-28</code> support and falls back to the 2025 handshake when needed. Client and upstream protocol selection are independent, so clients and servers can upgrade separately without portal configuration changes.</p>
<p>SSE connections continue to use the legacy protocol. For details, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#transport">MCP server portal transport and protocol compatibility</a>.</p>
</div></article></div>
