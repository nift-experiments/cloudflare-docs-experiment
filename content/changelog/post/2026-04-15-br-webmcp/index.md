<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 15, 2026</time><h2 id="post-title">Browser Run adds WebMCP support</h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p><a href="/browser-run/">Browser Run</a> (formerly Browser Rendering) now supports <a href="https://webmachinelearning.github.io/webmcp/">WebMCP</a> (Web Model Context Protocol), a new browser API from the Google Chrome team.</p>
<p>The Internet was built for humans, so navigating as an AI agent today is unreliable. WebMCP lets websites expose structured tools for AI agents to discover and call directly. Instead of slow screenshot-analyze-click loops, agents can call website functions like <code>searchFlights()</code> or <code>bookTicket()</code> with typed parameters, making browser automation faster, more reliable, and less fragile.</p>
<p><img src="/images/browser-run/webMCP.gif" alt="Browser Run lab session showing WebMCP tools being discovered and executed in the Chrome DevTools console to book a hotel" /></p>
<p>With WebMCP, you can:</p>
<ul>
<li><strong>Discover website tools</strong> - Use <code>navigator.modelContextTesting.listTools()</code> to see available actions on any WebMCP-enabled site</li>
<li><strong>Execute tools directly</strong> - Call <code>navigator.modelContextTesting.executeTool()</code> with typed parameters</li>
<li><strong>Handle human-in-the-loop interactions</strong> - Some tools pause for user confirmation before completing sensitive actions</li>
</ul>
<p>WebMCP requires Chrome beta features. We have an experimental pool with browser instances running Chrome beta so you can test emerging browser features before they reach stable Chrome. To start a WebMCP session, add <code>lab=true</code> to your <code>/devtools/browser</code> request:</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/devtools/browser?lab=true&amp;keep_alive=300000&quot; \&#10;  &#45;H &quot;Authorization: Bearer {api_token}&quot;&#10;</code></pre>
<p>Combined with the recently launched <a href="/browser-run/cdp/">CDP endpoint</a>, AI agents can also use WebMCP. Connect an <a href="/browser-run/cdp/mcp-clients/">MCP client</a> to Browser Run via CDP, and your agent can discover and call website tools directly. Here's the same hotel booking demo, this time driven by an AI agent through OpenCode:</p>
<p><img src="/images/browser-run/webMCPagent.gif" alt="Browser Run Live View showing an AI agent navigating a hotel booking site in real time" /></p>
<p>For a step-by-step guide, refer to the <a href="/browser-run/features/webmcp/">WebMCP documentation</a>.</p>
</div></article></div>
