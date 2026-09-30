<p>The Agents SDK provides <code>paidTool</code>, a drop-in replacement for <code>tool</code> that adds x402 payment requirements. Clients pay per tool call, and you can mix free and paid tools in the same server.</p>
<h2 id="setup">Setup</h2>
<p>Wrap your <code>McpServer</code> with <code>withX402</code> and use <code>paidTool</code> for tools you want to charge for:</p>
<pre><code class="language-ts">import { McpServer } from &quot;@modelcontextprotocol/sdk/server/mcp.js&quot;;&#10;import { McpAgent } from &quot;agents/mcp&quot;;&#10;import { withX402, type X402Config } from &quot;agents/x402&quot;;&#10;import { z } from &quot;zod&quot;;&#10;&#10;const X402_CONFIG: X402Config = {&#10;	network: &quot;base&quot;,&#10;	recipient: &quot;0xYourWalletAddress&quot;,&#10;	facilitator: { url: &quot;https://x402.org/facilitator&quot; }, // Payment facilitator URL&#10;	// To learn more about facilitators: https://docs.x402.org/core-concepts/facilitator&#10;};&#10;&#10;export class PaidMCP extends McpAgent&lt;Env&gt; {&#10;	server = withX402(&#10;		new McpServer({ name: &quot;PaidMCP&quot;, version: &quot;1.0.0&quot; }),&#10;		X402_CONFIG,&#10;	);&#10;&#10;	async init() {&#10;		// Paid tool — $0.01 per call&#10;		this.server.paidTool(&#10;			&quot;square&quot;,&#10;			&quot;Squares a number&quot;,&#10;			0.01, // USD&#10;			{ number: z.number() },&#10;			{},&#10;			async ({ number }) =&gt; {&#10;				return { content: [{ type: &quot;text&quot;, text: String(number ** 2) }] };&#10;			},&#10;		);&#10;&#10;		// Free tool&#10;		this.server.tool(&#10;			&quot;echo&quot;,&#10;			&quot;Echo a message&quot;,&#10;			{ message: z.string() },&#10;			async ({ message }) =&gt; {&#10;				return { content: [{ type: &quot;text&quot;, text: message }] };&#10;			},&#10;		);&#10;	}&#10;}&#10;</code></pre>
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
<pre><code class="language-ts">this.server.paidTool(&#10;	name, // Tool name&#10;	description, // Tool description&#10;	price, // Price in USD (e.g., 0.01)&#10;	inputSchema, // Zod schema for inputs&#10;	annotations, // MCP annotations&#10;	handler, // Async function that executes the tool&#10;);&#10;</code></pre>
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
