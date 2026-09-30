<p>This walkthrough connects Visual Studio Code directly to the Cloudflare API using the <a href="https://github.com/cloudflare/mcp-server-cloudflare">Cloudflare MCP server</a>. By the end, you can create a DNS record by typing a sentence, without leaving the editor.</p>
<p>The Cloudflare MCP server at <code>mcp.cloudflare.com</code> exposes the Cloudflare API to any MCP-capable agent. The Visual Studio Code Copilot agent connects to it, and you run API calls from natural language.</p>
<p>For the condensed version, refer to the <a href="/agent-setup/visual-studio-code/">Visual Studio Code quick start</a>.</p>
<h2 id="before-you-start">Before you start</h2>
<ul>
<li>Visual Studio Code, fully up to date. A version mismatch between the editor and the Copilot extension is the most common source of agent-mode errors.</li>
<li>GitHub Copilot. Any GitHub account works, and the free tier is enough.</li>
<li>A Cloudflare account you are comfortable pointing an agent at. Use a demo account. The reason becomes clear at the authorization step.</li>
</ul>
<h2 id="connect-visual-studio-code-to-the-cloudflare-api">Connect Visual Studio Code to the Cloudflare API</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/1840.md")
</div>
<p>You now have an AI agent with read and write access to Cloudflare services in the account, driven entirely from Visual Studio Code.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/agent-setup/visual-studio-code/">Visual Studio Code quick start</a> — condensed setup, tips, FAQ, and troubleshooting.</li>
<li><a href="https://github.com/cloudflare/mcp-server-cloudflare">Cloudflare MCP server</a> — domain-specific MCP servers.</li>
<li><a href="/api/">Cloudflare API</a> — the full REST API reference.</li>
</ul>
