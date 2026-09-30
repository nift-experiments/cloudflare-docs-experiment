<p>Use <a href="/ai-crawl-control/features/analyze-ai-traffic/">AI Crawl Control analytics</a> to identify which crawlers are accessing your site, then deploy Worker templates to customize how you handle that traffic.</p>
<h2 id="x402-payment-gated-proxy">x402 Payment-Gated Proxy</h2>
<p>The x402-proxy template implements payment-gated access using the <a href="https://www.x402.org/">x402 protocol</a> — an open payment standard built around HTTP 402 (Payment Required). Use it to monetize crawler access, paywall specific routes, or charge bots while letting humans through free.</p>
<p>For setup instructions and Bot Management integration examples, see the <a href="https://github.com/cloudflare/templates/tree/main/x402-proxy-template">template on GitHub</a>.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/x402-proxy-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/ai-crawl-control/reference/bots/">Bot reference</a> — Detection IDs and user agents for common crawlers</li>
<li><a href="/workers/">Cloudflare Workers</a> — Build and deploy serverless applications</li>
<li><a href="https://github.com/cloudflare/templates">Workers templates</a> — More templates on GitHub</li>
<li><a href="/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/">Pay Per Crawl</a> — Native Cloudflare integration for monetizing crawler access</li>
<li><a href="/agents/tools/payments/x402/">x402 payments</a> — Gate resources, charge for MCP tools, add payments to coding agents</li>
</ul>
