---
cp9:
  canonical: https://developers.cloudflare.com/browser-run/cdp/mcp-clients/
  description: Configure AI coding agents to control Browser Run sessions through the Model Context Protocol (MCP) using the chrome-devtools-mcp package.
  full_title: Using with MCP clients (CDP) · Cloudflare Browser Run docs
  head_html: <title>Using with MCP clients (CDP) · Cloudflare Browser Run docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure AI coding agents to control Browser Run sessions through the Model Context Protocol (MCP) using the chrome-devtools-mcp package."><link rel="canonical" href="https://developers.cloudflare.com/browser-run/cdp/mcp-clients/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/browser-run/cdp/mcp-clients/index.md"><meta property="og:title" content="Using with MCP clients (CDP) · Cloudflare Browser Run docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure AI coding agents to control Browser Run sessions through the Model Context Protocol (MCP) using the chrome-devtools-mcp package."><meta property="og:url" content="https://developers.cloudflare.com/browser-run/cdp/mcp-clients/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Browser Run"><meta name="algolia_product_filter" content="Browser Run"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Browser Run"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/browser-run/cdp/mcp-clients/#page","headline":"Using with MCP clients (CDP) \u00b7 Cloudflare Browser Run docs","description":"Configure AI coding agents to control Browser Run sessions through the Model Context Protocol (MCP) using the chrome-devtools-mcp package.","url":"https://developers.cloudflare.com/browser-run/cdp/mcp-clients/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /browser-run/cdp/mcp-clients/
  schema: 1
---
<p>You can use the CDP endpoints with AI coding agents through the <a href="https://modelcontextprotocol.io/">Model Context Protocol (MCP)</a>. The <a href="https://github.com/ChromeDevTools/chrome-devtools-mcp">chrome-devtools-mcp</a> package provides an MCP server that allows AI assistants to control and inspect browser sessions.</p>
<p>Before you begin, <a href="/fundamentals/api/get-started/create-token/">create a custom API Token</a> with <code>Browser Rendering - Edit</code> permission.</p>
<h2 id="what-is-mcp">What is MCP?</h2>
<p>The Model Context Protocol (MCP) is an open protocol that enables AI assistants to interact with external tools and services. By configuring an MCP client with Browser Run, your AI coding agent can perform browser automation tasks like navigating to pages, taking screenshots, running performance audits, and debugging JavaScript.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Node.js v20.19 or newer</li>
<li>An MCP-compatible AI client (for example, Claude Desktop, Claude Code, Cursor, OpenCode)</li>
<li>A Browser Run API token with <code>Browser Rendering - Edit</code> permissions</li>
</ul>
<h2 id="configure-your-mcp-client">Configure your MCP client</h2>
<p>Add the following configuration to your MCP client settings file (the exact location depends on your client):</p>
<h3 id="claude-desktop-and-claude-code">Claude Desktop and Claude Code</h3>
<p>Add to <code>claude_desktop_config.json</code> (Claude Desktop) or <code>~/.claude.json</code> (Claude Code):</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;mcpServers&quot;: {&#10;		&quot;browser-rendering&quot;: {&#10;			&quot;command&quot;: &quot;npx&quot;,&#10;			&quot;args&quot;: [&#10;				&quot;-y&quot;,&#10;				&quot;chrome-devtools-mcp@latest&quot;,&#10;				&quot;--wsEndpoint=wss://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/browser-rendering/devtools/browser?keep_alive=600000&quot;,&#10;				&quot;--wsHeaders={\&quot;Authorization\&quot;:\&quot;Bearer &lt;API_TOKEN&gt;\&quot;}&quot;&#10;			]&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="opencode">OpenCode</h3>
<p>Add to <code>.opencode.jsonc</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;mcp&quot;: {&#10;		&quot;browser-rendering&quot;: {&#10;			&quot;type&quot;: &quot;local&quot;,&#10;			&quot;command&quot;: [&#10;				&quot;npx&quot;,&#10;				&quot;-y&quot;,&#10;				&quot;chrome-devtools-mcp@latest&quot;,&#10;				&quot;--wsEndpoint=wss://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/browser-rendering/devtools/browser?keep_alive=600000&quot;,&#10;				&quot;--wsHeaders={\&quot;Authorization\&quot;:\&quot;Bearer &lt;API_TOKEN&gt;\&quot;}&quot;&#10;			],&#10;			&quot;enabled&quot;: true&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="cursor">Cursor</h3>
<p>Add to <code>~/.cursor/mcp.json</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;mcpServers&quot;: {&#10;		&quot;browser-rendering&quot;: {&#10;			&quot;command&quot;: &quot;npx&quot;,&#10;			&quot;args&quot;: [&#10;				&quot;-y&quot;,&#10;				&quot;chrome-devtools-mcp@latest&quot;,&#10;				&quot;--wsEndpoint=wss://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/browser-rendering/devtools/browser?keep_alive=600000&quot;,&#10;				&quot;--wsHeaders={\&quot;Authorization\&quot;:\&quot;Bearer &lt;API_TOKEN&gt;\&quot;}&quot;&#10;			]&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Replace <code>ACCOUNT_ID</code> with your Cloudflare account ID and <code>API_TOKEN</code> with your Browser Run API token. You can obtain these from your Cloudflare dashboard.</p>
<p>For other MCP clients, refer to the <a href="https://github.com/ChromeDevTools/chrome-devtools-mcp/tree/main?tab=readme-ov-file#mcp-client-configuration">chrome-devtools-mcp documentation</a>.</p>
<h2 id="example-usage">Example usage</h2>
<p>After configuring the MCP client, you can ask your AI agent to perform browser tasks:</p>
<pre tabindex="0"><code class="language-txt">Navigate to https://example.com and take a screenshot of the homepage&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">Check the console messages on the current page for any errors&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">Run a Lighthouse audit on https://developers.cloudflare.com&#10;</code></pre>
<h2 id="how-it-works">How it works</h2>
<p>The MCP server connects to Browser Run via WebSocket using the CDP protocol:</p>
<ol>
<li><strong>WebSocket endpoint</strong> - The <code>--wsEndpoint</code> URL connects to the Browser Run service</li>
<li><strong>Authentication</strong> - The <code>--wsHeaders</code> parameter includes your API token for authentication</li>
<li><strong>Keep-alive</strong> - The <code>keep_alive</code> query parameter (in milliseconds) specifies how long the session stays active</li>
<li><strong>MCP protocol</strong> - The server translates MCP tool calls into CDP commands</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="session-management">Session management</h3>
@markup("md", "content/.markup/bodies/3722.md")
</aside>
<h2 id="additional-resources">Additional resources</h2>
<ul>
<li><a href="https://github.com/ChromeDevTools/chrome-devtools-mcp">chrome-devtools-mcp repository</a> - Official MCP server for Chrome DevTools</li>
<li><a href="https://modelcontextprotocol.io/">Model Context Protocol documentation</a> - Learn more about MCP</li>
<li><a href="https://modelcontextprotocol.io/docs/develop/connect-local-servers">Claude Desktop MCP setup</a> - Configure MCP servers in Claude Desktop</li>
<li><a href="https://docs.anthropic.com/en/docs/claude-code/mcp">Claude Code MCP setup</a> - Configure MCP servers in Claude Code</li>
<li><a href="https://cursor.com/docs/mcp">Cursor MCP setup</a> - Configure MCP servers in Cursor</li>
<li><a href="https://opencode.ai/docs/mcp-servers/">OpenCode MCP setup</a> - Configure MCP servers in OpenCode</li>
</ul>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you have questions or encounter an error, see the <a href="/browser-run/faq/">Browser Run FAQ and troubleshooting guide</a>.</p>
