<p>Use the Cloudflare Agents SDK to pay MPP services. The <code>mppx</code> SDK handles payment retries for HTTP requests and Model Context Protocol (MCP) tool calls.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Create a <a href="/agents/getting-started/">Cloudflare Agents project</a>. Fund an account for the payment method that the service accepts.</p>
<h2 id="configure-payments">Configure payments</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2704.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2702.md")
</aside>
<h2 id="pay-an-http-service">Pay an HTTP service</h2>
<p>Create a payment-aware client in <code>onStart()</code>. Restrict automatic payments to trusted origins:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2705.md")
</div>
<p>Free endpoints pass through unchanged. Paid endpoints trigger the payment retry and return a <code>Payment-Receipt</code> header.</p>
<h2 id="pay-an-mcp-tool">Pay an MCP tool</h2>
<p>Connect the Agent with <code>addMcpServer()</code>. Wait for the connection before wrapping its client:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2706.md")
</div>
<p>If <code>paidSearch()</code> returns an <code>authUrl</code>, send the user to that URL and retry after authorization.</p>
<p>The wrapper retries a paid tool call with an MPP Credential. The result includes the MPP Receipt as <code>result.receipt</code>.</p>
<p>By default, both clients pay compatible Challenges automatically. Use <code>onChallenge</code> for HTTP or <code>onPaymentRequired</code> for MCP when a payment needs approval. Challenge amounts are integer base units, not decimal display values.</p>
<h2 id="pay-x402-services">Pay x402 services</h2>
<p>The <code>mppx</code> HTTP client also recognizes x402 Challenges. Configure an x402-compatible EVM method next to the MPP method. The service does not need changes. For configuration, refer to <a href="https://mpp.dev/guides/use-mpp-with-x402">Use MPP with x402</a>.</p>
<p>To accept payments, refer to <a href="/agents/tools/payments/mpp/accept-payments/">Accept payments with MPP</a>. For MCP connection options, refer to the <a href="/agents/model-context-protocol/apis/client-api/">MCP client API</a>.</p>
