<p>Use Cloudflare Workers to accept Machine Payments Protocol (MPP) payments. Choose an integration based on the service you want to protect:</p>
<ul>
<li><a href="https://github.com/cloudflare/mpp-proxy"><code>mpp-proxy</code></a> — Charge for HTTP content without changing your origin code. Refer to <a href="/agents/tools/payments/mpp-charge-for-http-content/">Charge for HTTP content</a>.</li>
<li><strong>Worker route</strong> — Add <code>mppx</code> payment middleware to a Worker application.</li>
<li><strong>MCP tool</strong> — Require payment before an MCP tool returns its result.</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<p>Create a <a href="/fundamentals/account/create-account/">Cloudflare account</a>. You also need a payment recipient and an MPP secret key.</p>
<p>The examples use a stablecoin payment method on testnet. For other methods, refer to <a href="https://mpp.dev/payment-methods/">MPP payment methods</a>.</p>
<h2 id="charge-for-a-worker-route">Charge for a Worker route</h2>
<p>Add <code>mppx</code> middleware when you control the Worker application:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2709.md")
</div>
<h2 id="charge-for-an-mcp-tool">Charge for an MCP tool</h2>
<p>Add the MPP transport to an <a href="/agents/model-context-protocol/apis/agent-api/"><code>McpAgent</code></a>:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2712.md")
</div>
<p>To test both payment flows from a Cloudflare Agent, refer to <a href="/agents/tools/payments/mpp/pay-from-agents-sdk/">Pay from the Agents SDK</a>. For production billing patterns, refer to <a href="https://mpp.dev/intents/">MPP payment intents</a>.</p>
