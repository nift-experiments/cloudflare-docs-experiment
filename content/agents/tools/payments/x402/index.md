<p><a href="https://www.x402.org/">x402</a> is a payment standard built around HTTP 402 (Payment Required). Services return a 402 response with payment instructions, and clients pay programmatically without accounts, sessions, or API keys.</p>
<h2 id="how-it-works">How it works</h2>
<ol>
<li>A client requests a resource — <code>GET /resource</code>.</li>
<li>The server returns <code>402 Payment Required</code> with a <code>PAYMENT-REQUIRED</code> header containing Base64-encoded payment details: the price, accepted token, network, and merchant address.</li>
<li>The client constructs a signed payment payload and retries the request with a <code>PAYMENT-SIGNATURE</code> header.</li>
<li>The server verifies the payment payload — directly or by calling a <a href="#the-facilitator">facilitator</a> — and settles the transaction on-chain.</li>
<li>The server returns the resource with a <code>PAYMENT-RESPONSE</code> header containing settlement confirmation.</li>
</ol>
<h2 id="key-components">Key components</h2>
<h3 id="client">Client</h3>
<p>The client is any entity that requests a paid resource: a human-operated app, an AI agent, or a programmatic service. Clients need only a crypto wallet — no accounts, credentials, or session tokens to manage.</p>
<h3 id="server">Server</h3>
<p>The server defines payment requirements in the <code>402</code> response, verifies incoming payment payloads, settles the transaction, and serves the resource. The x402 SDKs and a facilitator handle most of this automatically.</p>
<h3 id="the-facilitator">The facilitator</h3>
<p>The facilitator is an optional but recommended third-party service that abstracts blockchain interaction. Rather than connecting to a node directly, the server delegates two operations:</p>
<ul>
<li><strong><code>POST /verify</code></strong> — Confirms the client's payment payload is valid before the server fulfills the request.</li>
<li><strong><code>POST /settle</code></strong> — Submits the verified payment transaction to the blockchain.</li>
</ul>
<p>The facilitator does not hold funds. It verifies and broadcasts the client's pre-signed transaction on behalf of the server. <code>https://x402.org/facilitator</code> is the public facilitator operated by Coinbase and is used in all Cloudflare examples. <a href="https://www.x402.org/ecosystem?filter=facilitators">Multiple facilitators</a> are available across different networks.</p>
<h2 id="payment-schemes-and-networks">Payment schemes and networks</h2>
<p>x402 uses payment <strong>schemes</strong> to define how a payment is constructed and settled on a given network.</p>
<table>
<thead>
<tr>
<th>Scheme</th>
<th>Networks</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/x402-foundation/x402/blob/main/specs/schemes/exact/scheme_exact.md"><code>exact</code></a></td>
<td>EVM, Solana, Aptos, Stellar, Hedera, Sui</td>
<td>Transfers a fixed token amount — typically <a href="https://eips.ethereum.org/EIPS/eip-20">ERC-20</a> USDC on EVM — to the merchant address.</td>
</tr>
<tr>
<td><a href="https://github.com/x402-foundation/x402/blob/main/specs/schemes/upto/scheme_upto.md"><code>upto</code></a></td>
<td>EVM</td>
<td>Authorizes a maximum amount; the actual charge is determined at settlement time based on resource consumption.</td>
</tr>
</tbody>
</table>
<p>Supported networks include Base, Ethereum, Polygon, Optimism, Arbitrum, Avalanche, Solana, Aptos, Stellar, and Sui. Use <code>base-sepolia</code> for testing with free test USDC from the <a href="https://faucet.circle.com/">Circle Faucet</a>.</p>
<h2 id="charge-for-resources">Charge for resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/2699.md")
</div>
<h2 id="pay-for-resources">Pay for resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/2700.md")
</div>
<h2 id="sdks">SDKs</h2>
<table>
<thead>
<tr>
<th>Package</th>
<th>Install</th>
<th>Use</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>x402-hono</code></td>
<td><code>npm install x402-hono</code></td>
<td>Hono middleware for Worker servers</td>
</tr>
<tr>
<td><code>@x402/fetch</code></td>
<td><code>npm install @x402/fetch</code></td>
<td>Fetch wrapper with automatic payment handling</td>
</tr>
<tr>
<td><code>@x402/evm</code></td>
<td><code>npm install @x402/evm</code></td>
<td>EVM payment scheme support</td>
</tr>
<tr>
<td><code>agents/x402</code></td>
<td>Included in <code>agents</code></td>
<td>MCP client with x402 payment support</td>
</tr>
</tbody>
</table>
<h2 id="related">Related</h2>
<ul>
<li><a href="https://x402.org">x402.org</a> — Protocol specification</li>
<li><a href="https://github.com/x402-foundation/x402">x402 GitHub</a> — Open source SDK</li>
<li><a href="https://github.com/cloudflare/agents/tree/main/examples">x402 examples</a> — Complete working code</li>
<li><a href="/ai-crawl-control/features/pay-per-crawl/">Pay Per Crawl</a> — Cloudflare-native monetization</li>
</ul>
