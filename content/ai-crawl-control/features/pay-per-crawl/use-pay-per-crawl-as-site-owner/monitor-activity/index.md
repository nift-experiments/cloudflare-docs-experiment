<pre><code class="language-mermaid">graph LR&#10;A[Enable in&lt;br&gt;account settings] --&gt; B[Set a pay per &lt;br/&gt;crawl price ]&#10;B --&gt; C[Select crawlers&lt;br&gt;to charge]&#10;C --&gt; D[Monitor&lt;br&gt;activity]:::highlight&#10;D --&gt; E[Manage&lt;br&gt;payouts]&#10;classDef highlight fill:#F6821F,color:white&#10;&#10;click A &quot;/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/enable-in-account-settings/&quot;&#10;click B &quot;/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/set-a-pay-per-crawl-price/&quot;&#10;click C &quot;/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/select-crawlers-to-charge/&quot;&#10;click E &quot;/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/manage-payouts/&quot;&#10;</code></pre>
<p>After configuring pay per crawl, monitor crawler activity to understand how AI crawlers interact with your content, and track your earnings.</p>
<h2 id="view-crawler-activity">View crawler activity</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2761.md")
</div>
<p>The metrics help you understand:</p>
<ul>
<li>Which crawlers are accessing your content</li>
<li>How often they are being charged</li>
<li>Request patterns and trends</li>
<li>Robots.txt violations</li>
</ul>
<p>For detailed information about available metrics, refer to <a href="/ai-crawl-control/features/analyze-ai-traffic/#view-the-metrics-tab">View AI Crawl Control metrics</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="balance-visibility">Balance visibility</h3>
@markup("md", "content/.markup/bodies/2760.md")
</aside>
<h2 id="additional-considerations">Additional considerations</h2>
<h3 id="robots-txt-management">Robots.txt management</h3>
<p>Consider updating your <code>robots.txt</code> file to clearly indicate which pages should remain off-limits, even if AI crawlers are willing to pay for access.</p>
<h3 id="ongoing-optimization">Ongoing optimization</h3>
<p>Do the following to ensure you are using pay per crawl most effectively:</p>
<ul>
<li>Review crawler activity regularly to identify patterns</li>
<li>Adjust pricing based on demand and content value</li>
<li>Modify crawler actions (charge, allow, block) as needed</li>
<li>Monitor for any unusual or unwanted crawler behavior</li>
</ul>
<h2 id="additional-resources">Additional resources</h2>
<ul>
<li><a href="/ai-crawl-control/features/pay-per-crawl/faq">Pay Per Crawl FAQs</a></li>
<li><a href="/ai-crawl-control/features/analyze-ai-traffic/">Analyze AI traffic</a></li>
</ul>
