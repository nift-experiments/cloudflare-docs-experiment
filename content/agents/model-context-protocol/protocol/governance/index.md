<p>Model Context Protocol (MCP) allows Large Language Models (LLMs) to interact with proprietary data and internal tools. However, as MCP adoption grows, organizations face security risks from &quot;Shadow MCP&quot;, where employees run unmanaged local MCP servers against sensitive internal resources. MCP governance means that administrators have control over which MCP servers are used in the organization, who can use them, and under what conditions.</p>
<h2 id="mcp-server-portals">MCP server portals</h2>
<p>Cloudflare Access provides a centralized governance layer for MCP, allowing you to vet, authorize, and audit every interaction between users and MCP servers.</p>
<p>The <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portal</a> serves as the administrative hub for governance. From this portal, administrators can manage both third-party and internal MCP servers and define policies for:</p>
<ul>
<li><strong>Identity</strong>: Which users or groups are authorized to access specific MCP servers.</li>
<li><strong>Conditions</strong>: The security posture (for example, device health or location) required for access.</li>
<li><strong>Scope</strong>: Which specific tools within an MCP server are authorized for use.</li>
</ul>
<p>Cloudflare Access logs MCP server requests and tool executions made through the portal, providing administrators with visibility into MCP usage across the organization.</p>
<h2 id="remote-mcp-servers">Remote MCP servers</h2>
<p>To maintain a modern security posture, Cloudflare recommends the use of <a href="/agents/model-context-protocol/guides/remote-mcp-server/">remote MCP servers</a> over local installations. Running MCP servers locally introduces risks similar to unmanaged <a href="https://www.cloudflare.com/learning/access-management/what-is-shadow-it/">shadow IT</a>, making it difficult to audit data flow or verify the integrity of the server code. Remote MCP servers give administrators visibility into what servers are being used, along with the ability to control who access them and what tools are authorized for employee use.</p>
<p>You can <a href="/agents/model-context-protocol/guides/remote-mcp-server/">build your remote MCP servers</a> directly on Cloudflare Workers. When both your <a href="#mcp-server-portals">MCP server portal</a> and remote MCP servers run on Cloudflare's network, requests stay on the same infrastructure, minimizing latency and maximizing performance.</p>
