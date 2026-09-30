<p>The MCP server <a href="https://cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/">(Model Context Protocol)</a> for Digital Experience Monitoring (DEX) is an AI tool that allows customers to ask a question like, &quot;Show me the connectivity and performance metrics for the device used by carly‌@acme.com&quot;, and receive an answer that contains data from the DEX API.</p>
<p>Any Cloudflare One customer using a Free, Pay-as-you-go, or Enterprise account can access the DEX MCP server.</p>
<p>There are two primary options for connecting to the DEX MCP server:</p>
<ul>
<li><a href="#cloudflare-ai-playground">In Cloudflare's AI Playground</a></li>
<li><a href="#ai-assistant">With your preferred AI assistant</a></li>
</ul>
<h2 id="cloudflare-ai-playground">Cloudflare AI Playground</h2>
<p>Cloudflare's AI Playground allows you to quickly try out the DEX MCP server.</p>
<p>You can test the DEX MCP server in less than one minute by visiting the AI Playground's website.</p>
<ol>
<li>Copy the URL for the DEX MCP server: <code>https://dex.mcp.cloudflare.com/mcp</code>.</li>
<li>Open <a href="https://playground.ai.cloudflare.com">playground.ai.cloudflare.com</a> in a browser.</li>
<li>Find the section in the left sidebar titled <strong>MCP Servers</strong>.</li>
<li>Paste the URL for the DEX MCP server into the URL input box and select <strong>Connect</strong>.</li>
<li>Authenticate your Cloudflare account, and then start asking questions about your DEX data.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4971.md")
</aside>
<h2 id="ai-assistant">AI Assistant</h2>
<p>You can get a more flexible and robust experience by configuring the DEX MCP server with your preferred AI assistant (for example, Claude, Gemini, or ChatGPT).</p>
<p>If you have any issues during the configuration process, you can ask your AI assistant for help with configuring an MCP server via URL.</p>
<h3 id="claude">Claude</h3>
<p>You need a Claude Pro account (or higher subscription) to configure an MCP server.</p>
<ol>
<li>Download the <a href="https://claude.ai/download">Claude desktop client</a>.</li>
<li>Open the Claude desktop client, and log in or set up an account.</li>
<li>Expand the left sidebar menu, and select <strong>Claude Code</strong>.</li>
<li>Under <strong>Desktop app</strong>, select <strong>Developer</strong> to show the <strong>Local MCP servers</strong> page.</li>
<li>Select <strong>Edit Config</strong> and open the <code>claude_desktop_config.json</code> file in a text editor of your choice.</li>
<li>Copy the JSON configuration for the DEX MCP server and paste it into <code>claude_desktop_config.json</code>. Save the file.</li>
</ol>
<pre><code class="language-json">{&#10;	&quot;globalShortcut&quot;: &quot;&quot;,&#10;	&quot;mcpServers&quot;: {&#10;		&quot;cloudflare-dex-analysis&quot;: {&#10;			&quot;command&quot;: &quot;npx&quot;,&#10;			&quot;args&quot;: [&quot;mcp-remote&quot;, &quot;https://dex.mcp.cloudflare.com/mcp&quot;]&#10;		}&#10;	}&#10;}&#10;</code></pre>
<ol start="7">
<li>Fully close Claude by using the task manager to stop any background processes related to Claude.</li>
<li>Open Claude, and your DEX MCP server configuration should appear on the <strong>Local MCP servers</strong> page.</li>
<li>Authenticate your Cloudflare account and allow the DEX MCP server.</li>
<li>You can start asking Claude questions about DEX. As a simple test, you can ask &quot;Are you connected to the DEX MCP server&quot;.</li>
</ol>
<h3 id="gemini-cli">Gemini CLI</h3>
<p>All tiers of Google AI Free, Pro, and Ultra offer an MCP server integration via the Gemini CLI.</p>
<p>You will need to use a CLI of your choice and npm or homebrew to install and access the Gemini CLI.</p>
<ol>
<li>
<p>Visit the GitHub page for the <a href="https://github.com/google-gemini/gemini-cli">Gemini CLI</a> and follow the installation instructions.</p>
</li>
<li>
<p>Navigate to the <code>settings.json</code> file for your Gemini CLI install and open it in a text editor of your choice.</p>
<details>
  <summary>File path for the `settings.json` file</summary>
- Windows: `%USERPROFILE%\.gemini\settings.json`
- Mac and Linux: `~/.gemini/settings.json`
</details>
</li>
<li>
<p>Copy the JSON configuration for the DEX MCP server and paste it into <strong>settings.json</strong>. Save the file.</p>
</li>
</ol>
<pre><code class="language-json">{&#10;	&quot;globalShortcut&quot;: &quot;&quot;,&#10;	&quot;mcpServers&quot;: {&#10;		&quot;cloudflare-dex-analysis&quot;: {&#10;			&quot;command&quot;: &quot;npx&quot;,&#10;			&quot;args&quot;: [&quot;mcp-remote&quot;, &quot;https://dex.mcp.cloudflare.com/mcp&quot;]&#10;		}&#10;	}&#10;}&#10;</code></pre>
<ol start="4">
<li>Run Gemini in your CLI of choice.</li>
<li>If everything is working as expected, the Gemini CLI will show the following message:<br/>
<code>Using: 1 MCP server (ctrl+t to view)</code></li>
<li>Authenticate the email associated with your Cloudflare account in the Gemini CLI.</li>
<li>You can start asking the Gemini CLI questions about DEX. As a simple test, you can ask &quot;Are you connected to the DEX MCP server&quot;.</li>
</ol>
<h3 id="chatgpt">ChatGPT</h3>
<p>You need a ChatGPT Pro or Business account to configure an MCP server. ChatGPT Free and Plus do not support MCP servers.</p>
<ol>
<li>Download the <a href="https://chatgpt.com/features/desktop">ChatGPT desktop app</a>.</li>
<li>Open the ChatGPT desktop app, and log in or set up an account.</li>
<li>Open the <strong>Settings</strong> menu and select <strong>Connectors</strong>.</li>
<li>Select the option to create a new Connector.</li>
<li>Provide a <strong>Name</strong> (like <code>DEX MCP</code>), <strong>Description</strong> (optional), and <strong>MCP Server URL</strong> for the Connector. The DEX MCP Server URL is: <code>https://dex.mcp.cloudflare.com/mcp</code>.</li>
<li>Create the new Connector.</li>
<li>Before you ask ChatGPT a question about DEX, select the <strong>+</strong> (plus) button next to the ChatGPT prompt box.</li>
<li>Select <strong>Use Connectors</strong> &gt; <strong>Add Sources</strong>, then select the DEX MCP as a source.</li>
<li>You can start asking ChatGPT questions about DEX. As a simple test, you can ask &quot;Are you connected to the DEX MCP server&quot;.</li>
</ol>
