<p>The Agents SDK includes an MCP client that can pay for x402-protected tools. Use it from your Agents or any MCP client connection.</p>
<pre><code class="language-ts">import { Agent } from &quot;agents&quot;;&#10;import { withX402Client } from &quot;agents/x402&quot;;&#10;import { privateKeyToAccount } from &quot;viem/accounts&quot;;&#10;&#10;export class MyAgent extends Agent {&#10;	// Your Agent definitions...&#10;&#10;	async onStart() {&#10;		const { id } = await this.mcp.connect(`${this.env.WORKER_URL}/mcp`);&#10;		const account = privateKeyToAccount(this.env.MY_PRIVATE_KEY);&#10;&#10;		this.x402Client = withX402Client(this.mcp.mcpConnections[id].client, {&#10;			network: &quot;base-sepolia&quot;,&#10;			account,&#10;		});&#10;	}&#10;&#10;	onPaymentRequired(paymentRequirements): Promise&lt;boolean&gt; {&#10;		// Your human-in-the-loop confirmation flow...&#10;	}&#10;&#10;	async onToolCall(toolName: string, toolArgs: unknown) {&#10;		// The first parameter is the confirmation callback.&#10;		// Set to `null` for the agent to pay automatically.&#10;		return await this.x402Client.callTool(this.onPaymentRequired, {&#10;			name: toolName,&#10;			arguments: toolArgs,&#10;		});&#10;	}&#10;}&#10;</code></pre>
<p>For a complete working example, see <a href="https://github.com/cloudflare/agents/tree/main/examples/x402-mcp">x402-mcp on GitHub</a>.</p>
<h2 id="environment-setup">Environment setup</h2>
<p>Store your private key securely:</p>
<pre><code class="language-sh">&#35; Local development (.dev.vars)&#10;MY_PRIVATE_KEY=&quot;0x...&quot;&#10;&#10;&#35; Production&#10;npx wrangler secret put MY_PRIVATE_KEY&#10;</code></pre>
<p>Use <code>base-sepolia</code> for testing. Get test USDC from the <a href="https://faucet.circle.com/">Circle faucet</a>.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/agents/tools/payments/x402/charge-for-mcp-tools/">Charge for MCP tools</a> — Build servers that charge for tools</li>
<li><a href="/agents/tools/payments/x402/pay-with-tool-plugins/">Pay from coding tools</a> — Add payments to OpenCode or Claude Code</li>
<li><a href="/agents/concepts/agentic-patterns/human-in-the-loop/">Human-in-the-loop guide</a> — Implement approval workflows</li>
</ul>
