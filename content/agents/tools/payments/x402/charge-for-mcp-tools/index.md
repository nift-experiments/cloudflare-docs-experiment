---
cp9:
  canonical: https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-mcp-tools/
  description: Charge per tool call in an MCP server using paidTool.
  full_title: Charge for MCP tools · Cloudflare Agents docs
  head_html: <title>Charge for MCP tools · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Charge per tool call in an MCP server using paidTool."><link rel="canonical" href="https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-mcp-tools/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-mcp-tools/index.md"><meta property="og:title" content="Charge for MCP tools · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Charge per tool call in an MCP server using paidTool."><meta property="og:url" content="https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-mcp-tools/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-mcp-tools/#page","headline":"Charge for MCP tools \u00b7 Cloudflare Agents docs","description":"Charge per tool call in an MCP server using paidTool.","url":"https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-mcp-tools/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/tools/payments/x402/charge-for-mcp-tools/
  schema: 1
---
<p>The Agents SDK provides <code>paidTool</code>, a drop-in replacement for <code>tool</code> that adds x402 payment requirements. Clients pay per tool call, and you can mix free and paid tools in the same server.</p>
<h2 id="setup">Setup</h2>
<p>Wrap your <code>McpServer</code> with <code>withX402</code> and use <code>paidTool</code> for tools you want to charge for:</p>
<pre tabindex="0"><code class="language-ts">import { McpServer } from &quot;@modelcontextprotocol/sdk/server/mcp.js&quot;;&#10;import { McpAgent } from &quot;agents/mcp&quot;;&#10;import { withX402, type X402Config } from &quot;agents/x402&quot;;&#10;import { z } from &quot;zod&quot;;&#10;&#10;const X402_CONFIG: X402Config = {&#10;	network: &quot;base&quot;,&#10;	recipient: &quot;0xYourWalletAddress&quot;,&#10;	facilitator: { url: &quot;https://x402.org/facilitator&quot; }, // Payment facilitator URL&#10;	// To learn more about facilitators: https://docs.x402.org/core-concepts/facilitator&#10;};&#10;&#10;export class PaidMCP extends McpAgent&lt;Env&gt; {&#10;	server = withX402(&#10;		new McpServer({ name: &quot;PaidMCP&quot;, version: &quot;1.0.0&quot; }),&#10;		X402_CONFIG,&#10;	);&#10;&#10;	async init() {&#10;		// Paid tool — $0.01 per call&#10;		this.server.paidTool(&#10;			&quot;square&quot;,&#10;			&quot;Squares a number&quot;,&#10;			0.01, // USD&#10;			{ number: z.number() },&#10;			{},&#10;			async ({ number }) =&gt; {&#10;				return { content: [{ type: &quot;text&quot;, text: String(number ** 2) }] };&#10;			},&#10;		);&#10;&#10;		// Free tool&#10;		this.server.tool(&#10;			&quot;echo&quot;,&#10;			&quot;Echo a message&quot;,&#10;			{ message: z.string() },&#10;			async ({ message }) =&gt; {&#10;				return { content: [{ type: &quot;text&quot;, text: message }] };&#10;			},&#10;		);&#10;	}&#10;}&#10;</code></pre>
<h2 id="configuration">Configuration</h2>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>network</code></td>
<td><code>base</code> for production, <code>base-sepolia</code> for testing</td>
</tr>
<tr>
<td><code>recipient</code></td>
<td>Wallet address to receive payments</td>
</tr>
<tr>
<td><code>facilitator</code></td>
<td>Payment facilitator URL (use <code>https://x402.org/facilitator</code>)</td>
</tr>
</tbody>
</table>
<h2 id="paidtool-signature">paidTool signature</h2>
<pre tabindex="0"><code class="language-ts">this.server.paidTool(&#10;	name, // Tool name&#10;	description, // Tool description&#10;	price, // Price in USD (e.g., 0.01)&#10;	inputSchema, // Zod schema for inputs&#10;	annotations, // MCP annotations&#10;	handler, // Async function that executes the tool&#10;);&#10;</code></pre>
<p>When a client calls a paid tool without payment, the server returns 402 with payment requirements. The client pays via x402, retries with payment proof, and receives the result.</p>
<h2 id="testing">Testing</h2>
<p>Use <code>base-sepolia</code> and get test USDC from the <a href="https://faucet.circle.com/">Circle faucet</a>.</p>
<p>For a complete working example, refer to <a href="https://github.com/cloudflare/agents/tree/main/examples/x402-mcp">x402-mcp on GitHub</a>.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/agents/tools/payments/x402/pay-from-agents-sdk/">Pay from Agents SDK</a> — Build clients that pay for tools</li>
<li><a href="/agents/tools/payments/x402/charge-for-http-content/">Charge for HTTP content</a> — Gate HTTP endpoints</li>
<li><a href="/agents/model-context-protocol/guides/remote-mcp-server/">MCP server guide</a> — Build your first MCP server</li>
</ul>
