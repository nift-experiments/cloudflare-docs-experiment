<p><a href="https://mpp.dev">Machine Payments Protocol (MPP)</a> is an open protocol for machine-to-machine payments. It standardizes the HTTP <code>402 Payment Required</code> status code with a formal authentication scheme proposed to the <a href="https://paymentauth.org">IETF</a>. MPP gives agents, applications, and people one interface to pay for a service in the same HTTP request.</p>
<p>MPP is payment-method agnostic. It supports stablecoins, cards through Stripe, and custom payment methods. A service can offer more than one method.</p>
<h2 id="how-it-works">How it works</h2>
<ol>
<li>An Agent or HTTP client requests a paid resource.</li>
<li>The service returns <code>402 Payment Required</code> with a payment Challenge.</li>
<li>The client fulfills the payment.</li>
<li>The client retries with a payment Credential.</li>
<li>The service returns the resource with a payment Receipt.</li>
</ol>
<p>HTTP services exchange payment data in authentication headers. Model Context Protocol (MCP) tools use the same flow through JSON-RPC.</p>
<h2 id="payment-intents">Payment intents</h2>
<p>MPP defines three payment intents:</p>
<ul>
<li><strong><code>charge</code></strong> — Collect a one-time payment.</li>
<li><strong><code>session</code></strong> — Charge for measured usage.</li>
<li><strong><code>subscription</code></strong> — Sell recurring access.</li>
</ul>
<p>For more information, refer to <a href="https://mpp.dev/intents/">MPP payment intents</a>.</p>
<h2 id="compatibility-with-x402">Compatibility with x402</h2>
<p>MPP is backwards-compatible with <a href="/agents/tools/payments/x402/">x402</a>. MPP clients can consume existing x402 services without changes to those services.</p>
<h2 id="build-on-cloudflare">Build on Cloudflare</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/2707.md")
</div>
<h2 id="sdks">SDKs</h2>
<p>MPP provides SDKs for TypeScript, Python, Rust, Go, and Ruby. The Cloudflare guides use the TypeScript <a href="https://mpp.dev/sdk/typescript/"><code>mppx</code> SDK</a>.</p>
<p>For current packages and integrations, refer to the <a href="https://mpp.dev/sdk/">MPP SDK documentation</a>.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="https://mpp.dev">mpp.dev</a> — Protocol documentation and guides</li>
<li><a href="https://paymentauth.org">IETF specification</a> — Payment HTTP Authentication Scheme</li>
<li><a href="/ai-crawl-control/features/pay-per-crawl/">Pay Per Crawl</a> — Cloudflare-native web content monetization</li>
</ul>
