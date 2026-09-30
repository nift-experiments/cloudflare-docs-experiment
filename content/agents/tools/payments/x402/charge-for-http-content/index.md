<p>The x402-proxy template is a Cloudflare Worker that sits in front of any HTTP backend. When a request hits a protected route, the proxy returns a 402 response with payment instructions. After the client pays, the proxy verifies the payment and forwards the request to your origin.</p>
<p>Deploy the x402-proxy template to your Cloudflare account:</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/x402-proxy-template"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a></li>
<li>An HTTP backend to gate</li>
<li>A wallet address to receive payments</li>
</ul>
<h2 id="configuration">Configuration</h2>
<p>Define protected routes in <code>wrangler.jsonc</code>:</p>
<pre><code class="language-json">{&#10;	&quot;vars&quot;: {&#10;		&quot;PAY_TO&quot;: &quot;0xYourWalletAddress&quot;,&#10;		&quot;NETWORK&quot;: &quot;base-sepolia&quot;,&#10;		&quot;PROTECTED_PATTERNS&quot;: [&#10;			{&#10;				&quot;pattern&quot;: &quot;/api/premium/*&quot;,&#10;				&quot;price&quot;: &quot;$0.10&quot;,&#10;				&quot;description&quot;: &quot;Premium API access&quot;&#10;			}&#10;		]&#10;	}&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2701.md")
</aside>
<h2 id="selective-gating-with-bot-management">Selective gating with Bot Management</h2>
<p>With <a href="/bots/">Bot Management</a>, the proxy can charge crawlers while keeping the site free for humans:</p>
<pre><code class="language-json">{&#10;	&quot;pattern&quot;: &quot;/content/*&quot;,&#10;	&quot;price&quot;: &quot;$0.10&quot;,&#10;	&quot;description&quot;: &quot;Content access&quot;,&#10;	&quot;bot_score_threshold&quot;: 30,&#10;	&quot;except_detection_ids&quot;: [117479730]&#10;}&#10;</code></pre>
<p>Requests with a bot score at or below <code>bot_score_threshold</code> are directed to the paywall. Use <code>except_detection_ids</code> to allowlist specific crawlers by <a href="/ai-crawl-control/reference/bots/">detection ID</a>.</p>
<h2 id="deploy">Deploy</h2>
<p>Clone the template, edit <code>wrangler.jsonc</code>, and deploy:</p>
<pre><code class="language-sh">git clone https://github.com/cloudflare/templates&#10;cd templates/x402-proxy-template&#10;npm install&#10;npx wrangler deploy&#10;</code></pre>
<p>For full configuration options and Bot Management examples, refer to the <a href="https://github.com/cloudflare/templates/tree/main/x402-proxy-template">template README</a>.</p>
<h2 id="custom-worker-endpoints">Custom Worker endpoints</h2>
<p>For more control, add x402 middleware directly to your Worker using Hono:</p>
<pre><code class="language-ts">import { Hono } from &quot;hono&quot;;&#10;import { paymentMiddleware } from &quot;x402-hono&quot;;&#10;&#10;const app = new Hono&lt;{ Bindings: Env }&gt;();&#10;&#10;app.use(&#10;	paymentMiddleware(&#10;		&quot;0xYourWalletAddress&quot; as `0x${string}`,&#10;		{&#10;			&quot;/premium&quot;: {&#10;				price: &quot;$0.10&quot;,&#10;				network: &quot;base-sepolia&quot;,&#10;				config: { description: &quot;Premium content&quot; },&#10;			},&#10;		},&#10;		{ url: &quot;https://x402.org/facilitator&quot; },&#10;	),&#10;);&#10;&#10;app.get(&quot;/premium&quot;, (c) =&gt; c.json({ message: &quot;Thanks for paying!&quot; }));&#10;&#10;export default app;&#10;</code></pre>
<p>Refer to the <a href="https://github.com/cloudflare/agents/tree/main/examples/x402">x402 Workers example</a> for a complete implementation.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/ai-crawl-control/features/pay-per-crawl/">Pay Per Crawl</a> — Native Cloudflare monetization without custom code</li>
<li><a href="/agents/tools/payments/x402/charge-for-mcp-tools/">Charge for MCP tools</a> — Charge per tool call instead of per request</li>
<li><a href="https://x402.org">x402.org</a> — Protocol specification</li>
</ul>
