<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 12, 2026</time><h2 id="post-title">MCP protocol detection and AI Security dashboard</h2>
<div class="changelog-badges"><span>gateway</span><span>cloudflare-one</span></div><div class="changelog-body"><p>Cloudflare Gateway now automatically detects <a href="https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/">Model Context Protocol (MCP)</a> traffic flowing through your network. MCP is the standard protocol used by AI agents to connect to external tools and data sources. Gateway identifies MCP requests by inspecting protocol-specific headers and payload characteristics.</p>
<h4 id="mcp-policy-selector">MCP policy selector</h4>
<p>A new <strong>Is MCP</strong> selector (<code>experimental.is_mcp</code>) is available in <a href="/cloudflare-one/traffic-policies/http-policies/#is-mcp">HTTP policies</a>. Use this selector to build Gateway rules that allow, block, or isolate MCP traffic.</p>
<p>This selector is currently in beta and may change before general availability.</p>
<p>For example, the following policy blocks MCP traffic that does not arrive through an approved <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP portal</a>:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Is MCP</td>
<td>is</td>
<td><em>True</em></td>
<td>And</td>
<td>Block</td>
</tr>
<tr>
<td>Traffic Source</td>
<td>is not</td>
<td><em>MCP portal</em></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p><img src="/assets/upstream/images/changelog/gateway/gateway-block-unknown-mcp.png" alt="Example Gateway policy that blocks MCP traffic not arriving through an MCP portal" /></p>
<h4 id="ai-security-report">AI security report</h4>
<p>A new <strong>AI security report</strong> dashboard under <strong>Insights &amp; Logs &gt; Dashboards</strong> provides visibility into MCP usage across your organization. The dashboard includes:</p>
<ul>
<li>Total MCP request volume, unique users, and unique MCP servers</li>
<li>A timeseries chart of unique MCP servers observed over time</li>
<li>A summary of Gateway policies that target MCP traffic</li>
</ul>
<p><img src="/assets/upstream/images/changelog/gateway/gateway-mcp-dashboard.png" alt="AI security report dashboard showing MCP detection data including total MCP requests, users, servers, and Gateway policies for MCP" /></p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a>.</p>
</div></article></div>
