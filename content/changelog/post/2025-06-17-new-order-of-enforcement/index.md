<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 18, 2025</time><h2 id="post-title">Gateway will now evaluate Network policies before HTTP policies from July 14th, 2025</h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p><a href="/cloudflare-one/traffic-policies/">Gateway</a> will now evaluate <a href="/cloudflare-one/traffic-policies/network-policies/">Network (Layer 4) policies</a> <strong>before</strong> <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP (Layer 7) policies</a>. This change preserves your existing security posture and does not affect which traffic is filtered — but it may impact how notifications are displayed to end users.</p>
<p>This change will roll out progressively between <strong>July 14–18, 2025</strong>. If you use HTTP policies, we recommend reviewing your configuration ahead of rollout to ensure the user experience remains consistent.</p>
<h4 id="updated-order-of-enforcement">Updated order of enforcement</h4>
<p><strong>Previous order:</strong></p>
<ol>
<li>DNS policies</li>
<li>HTTP policies</li>
<li>Network policies</li>
</ol>
<p><strong>New order:</strong></p>
<ol>
<li>DNS policies</li>
<li><strong>Network policies</strong></li>
<li><strong>HTTP policies</strong></li>
</ol>
<h4 id="action-required-review-your-gateway-http-policies">Action required: Review your Gateway HTTP policies</h4>
<p>This change may affect block notifications. For example:</p>
<ul>
<li>You have an <strong>HTTP policy</strong> to block <code>example.com</code> and display a block page.</li>
<li>You also have a <strong>Network policy</strong> to block <code>example.com</code> silently (no client notification).</li>
</ul>
<p>With the new order, the Network policy will trigger first — and the user will no longer see the HTTP block page.</p>
<p>To ensure users still receive a block notification, you can:</p>
<ul>
<li>Add a client notification to your Network policy, or</li>
<li>Use only the HTTP policy for that domain.</li>
</ul>
<hr />
<h4 id="why-we-re-making-this-change">Why we’re making this change</h4>
<p>This update is based on user feedback and aims to:</p>
<ul>
<li>Create a more intuitive model by evaluating network-level policies before application-level policies.</li>
<li>Minimize <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/#error-526-in-the-zero-trust-context">526 connection errors</a> by verifying the network path to an origin before attempting to establish a decrypted TLS connection.</li>
</ul>
<hr />
<p>To learn more, visit the <a href="/cloudflare-one/traffic-policies/order-of-enforcement/">Gateway order of enforcement documentation</a>.</p>
</div></article></div>
