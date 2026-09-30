<p>The <a href="https://github.com/cloudflare/mpp-proxy">mpp-proxy</a> template is a Cloudflare Worker that sits in front of any HTTP backend. When a request hits a protected route, the proxy returns a <code>402</code> response with an MPP payment challenge. After the client pays, the proxy verifies the payment, forwards the request to your origin, and issues a 1-hour session cookie.</p>
<p>Deploy the mpp-proxy template to your Cloudflare account:</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/mpp-proxy"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a></li>
<li>An HTTP backend to gate</li>
<li>A wallet address to receive payments</li>
</ul>
<h2 id="configuration">Configuration</h2>
<p>Define protected routes in <code>wrangler.jsonc</code>:</p>
<pre><code class="language-jsonc">{&#10;	&quot;vars&quot;: {&#10;		&quot;PAY_TO&quot;: &quot;0xYourWalletAddress&quot;,&#10;		&quot;TEMPO_TESTNET&quot;: false,&#10;		&quot;PAYMENT_CURRENCY&quot;: &quot;0x20c000000000000000000000b9537d11c60e8b50&quot;,&#10;		&quot;PROTECTED_PATTERNS&quot;: [&#10;			{&#10;				&quot;pattern&quot;: &quot;/premium/*&quot;,&#10;				&quot;amount&quot;: &quot;0.01&quot;,&#10;				&quot;description&quot;: &quot;Access to premium content for 1 hour&quot;&#10;			}&#10;		]&#10;	}&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2657.md")
</aside>
<h2 id="selective-gating-with-bot-management">Selective gating with Bot Management</h2>
<p>With <a href="/bots/">Bot Management</a>, the proxy can charge crawlers while keeping the site free for humans:</p>
<pre><code class="language-jsonc">{&#10;	&quot;pattern&quot;: &quot;/content/*&quot;,&#10;	&quot;amount&quot;: &quot;0.25&quot;,&#10;	&quot;description&quot;: &quot;Content access for 1 hour&quot;,&#10;	&quot;bot_score_threshold&quot;: 30,&#10;	&quot;except_detection_ids&quot;: [120623194, 117479730]&#10;}&#10;</code></pre>
<p>Requests with a bot score at or below <code>bot_score_threshold</code> are directed to the paywall. Use <code>except_detection_ids</code> to allowlist specific crawlers by <a href="/ai-crawl-control/reference/bots/">detection ID</a>.</p>
<h2 id="deploy">Deploy</h2>
<p>Clone the template, edit <code>wrangler.jsonc</code>, and deploy:</p>
<pre><code class="language-sh">git clone https://github.com/cloudflare/mpp-proxy&#10;cd mpp-proxy&#10;npm install&#10;npx wrangler secret put JWT_SECRET&#10;npx wrangler secret put MPP_SECRET_KEY&#10;npx wrangler deploy&#10;</code></pre>
<p>For full configuration options, proxy modes, and Bot Management examples, refer to the <a href="https://github.com/cloudflare/mpp-proxy">mpp-proxy README</a>.</p>
<h2 id="custom-worker-endpoints">Custom Worker endpoints</h2>
<p>To add MPP middleware directly to a Worker, refer to <a href="/agents/tools/payments/mpp/accept-payments/#charge-for-a-worker-route">Accept payments with MPP</a>.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="https://mpp.dev">mpp.dev</a> — Protocol specification</li>
<li><a href="/ai-crawl-control/features/pay-per-crawl/">Pay Per Crawl</a> — Cloudflare-native monetization without custom code</li>
</ul>
