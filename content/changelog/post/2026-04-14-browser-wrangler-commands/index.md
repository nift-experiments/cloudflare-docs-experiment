<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 14, 2026</time><h2 id="post-title">Manage Browser Rendering sessions with Wrangler CLI</h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p><a href="/browser-run/">Browser Rendering</a> now supports <code>wrangler browser</code> commands, letting you create, manage, and view browser sessions directly from your terminal, streamlining your workflow. Since Wrangler handles authentication, you do not need to pass API tokens in your commands.</p>
<p>The following commands are available:</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>wrangler browser create</code></td>
<td>Create a new browser session</td>
</tr>
<tr>
<td><code>wrangler browser close</code></td>
<td>Close a session</td>
</tr>
<tr>
<td><code>wrangler browser list</code></td>
<td>List active sessions</td>
</tr>
<tr>
<td><code>wrangler browser view</code></td>
<td>View a live browser session</td>
</tr>
</tbody>
</table>
<p>The <code>create</code> command spins up a browser instance on Cloudflare's network and returns a session URL. Once created, you can connect to the session using any <a href="/browser-run/cdp/">CDP</a>-compatible client like <a href="/browser-run/cdp/puppeteer/">Puppeteer</a>, <a href="/browser-run/cdp/playwright/">Playwright</a>, or <a href="/browser-run/cdp/mcp-clients/">MCP clients</a> to automate browsing, scrape content, or debug remotely.</p>
<pre><code class="language-sh">wrangler browser create&#10;</code></pre>
<p>Use <code>--keepAlive</code> to set the session keep-alive duration (60-600 seconds):</p>
<pre><code class="language-sh">wrangler browser create --keepAlive 300&#10;</code></pre>
<p>The <code>view</code> command auto-selects when only one session exists, or prompts for selection when multiple sessions are available.</p>
<p>All commands support <code>--json</code> for structured output, and because these are CLI commands, you can incorporate them into scripts to automate session management.</p>
<p>For full usage details, refer to the <a href="/browser-run/reference/wrangler-commands/">Wrangler commands documentation</a>.</p>
</div></article></div>
