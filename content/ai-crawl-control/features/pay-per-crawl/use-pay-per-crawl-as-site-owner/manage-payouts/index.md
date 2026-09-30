<pre><code class="language-mermaid">graph LR&#10;A[Enable in&lt;br&gt;account settings] --&gt; B[Set a pay per &lt;br/&gt;crawl price ]&#10;B --&gt; C[Select crawlers&lt;br&gt;to charge]&#10;C --&gt; D[Monitor&lt;br&gt;activity]&#10;D --&gt; E[Manage&lt;br&gt;payouts]:::highlight&#10;classDef highlight fill:#F6821F,color:white&#10;&#10;click A &quot;/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/enable-in-account-settings/&quot;&#10;click B &quot;/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/set-a-pay-per-crawl-price/&quot;&#10;click C &quot;/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/select-crawlers-to-charge/&quot;&#10;click D &quot;/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/monitor-activity/&quot;&#10;</code></pre>
<p>When you're ready to receive payments for your accrued crawler activity, connect your Cloudflare account to Stripe. This step can be completed at any time after enabling pay per crawl.</p>
<h2 id="create-a-new-stripe-account">Create a new Stripe account</h2>
<p>A person with <strong>Administrator</strong> or <strong>Super Administrator</strong> access must set up the Stripe connection:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2763.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="pay-per-crawl-stripe-account-required">Pay Per Crawl Stripe account required</h3>
@markup("md", "content/.markup/bodies/2762.md")
</aside>
<h2 id="billing-lifecycle">Billing lifecycle</h2>
<p>Cloudflare manages the complete billing lifecycle:</p>
<ol>
<li><strong>Charge initiation</strong>: AI crawlers indicate payment intent via request headers</li>
<li><strong>Charge recording</strong>: A charge event is recorded upon successful content delivery (HTTP 200 response)</li>
<li><strong>Aggregation</strong>: Cloudflare aggregates and reconciles all recorded charges</li>
<li><strong>Payout</strong>: Monthly payments to publishers in good standing</li>
</ol>
<h3 id="limitations">Limitations</h3>
<ul>
<li>Your accrued balance is not currently visible in the dashboard. You can request balance updates from your Cloudflare team.</li>
<li>Payouts are subject to settlement periods and minimum payout thresholds.</li>
</ul>
