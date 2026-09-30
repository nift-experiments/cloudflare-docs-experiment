<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 26, 2026</time><h2 id="post-title">Code Mode for MCP server portals</h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> support <a href="/agents/model-context-protocol/codemode/">Code Mode MCP server patterns</a>, a technique that reduces context window usage by replacing individual tool definitions with a single code execution tool. Code Mode is turned on by default on all portals.</p>
<p>To turn it off, edit the portal in <strong>Access controls</strong> &gt; <strong>AI controls</strong> and turn off <strong>Code Mode</strong> under <strong>Basic information</strong>.</p>
<p>When Code Mode is active, the portal exposes a single <code>code</code> tool instead of listing every tool from every upstream MCP server. The connected AI agent writes JavaScript that calls typed <code>codemode.*</code> methods for each upstream tool. The generated code runs in an isolated <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker</a> environment, keeping authentication credentials and environment variables out of the model context.</p>
<p>To use Code Mode, append <code>?codemode=search_and_execute</code> to your portal URL when connecting from an MCP client:</p>
<pre><code class="language-txt">https://&lt;subdomain&gt;.&lt;domain&gt;/mcp?codemode=search_and_execute&#10;</code></pre>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode">Code Mode</a>.</p>
</div></article></div>
