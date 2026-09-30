<pre><code class="language-mermaid">graph LR&#10;A[Set up your&lt;br&gt;Cloudflare Account] --&gt; B[Verify your&lt;br&gt;AI crawler]&#10;B --&gt; C[Discover&lt;br&gt;payable content]&#10;C --&gt; D[Connect to&lt;br&gt;Stripe]:::highlight&#10;D --&gt; E[Crawl pages]&#10;classDef highlight fill:#F6821F,color:white&#10;</code></pre>
<p>Connect your Cloudflare account to Stripe to process payments. Pay per crawl uses Stripe to process payments between AI crawler owners and site owners.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2775.md")
</div>
<p>When you successfully connect Stripe to your account, you will see a green tick ✅ next to <strong>Stripe connection</strong>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="spending-limits">Spending limits</h3>
@markup("md", "content/.markup/bodies/2773.md")
</aside>
<h2 id="billing">Billing</h2>
<p>Charges are recorded upon successful delivery of content that is requested with valid <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/crawl-pages/#21-include-payment-headers">crawler price headers</a>.</p>
<p>Invoices are created and managed via Stripe. Crawlers are responsible for setting and enforcing their own spending limits.</p>
