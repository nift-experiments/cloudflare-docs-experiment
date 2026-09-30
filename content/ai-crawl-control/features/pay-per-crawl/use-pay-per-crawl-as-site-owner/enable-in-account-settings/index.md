<pre><code class="language-mermaid">graph LR&#10;A[Enable in&lt;br&gt;account settings]:::highlight --&gt; B[Set a pay per &lt;br/&gt;crawl price ]&#10;B --&gt; C[Select crawlers&lt;br&gt;to charge]&#10;C --&gt; D[Monitor&lt;br&gt;activity]&#10;D --&gt; E[Manage&lt;br&gt;payouts]&#10;classDef highlight fill:#F6821F,color:white&#10;&#10;click B &quot;/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/set-a-pay-per-crawl-price/&quot;&#10;click C &quot;/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/select-crawlers-to-charge/&quot;&#10;click D &quot;/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/monitor-activity/&quot;&#10;click E &quot;/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/manage-payouts/&quot;&#10;</code></pre>
<h2 id="prerequisites">Prerequisites</h2>
<p>To configure pay per crawl, you must have the following:</p>
<ul>
<li><strong>Cloudflare account</strong>: You need an active Cloudflare account with domains added</li>
<li><strong>Domain on Cloudflare</strong>: Your domain must be using Cloudflare's nameservers, or have DNS records managed by Cloudflare</li>
<li><strong>Administrator access</strong>: You need Administrator or Super Administrator permissions for account-level configuration</li>
</ul>
<h2 id="configure-domain-access">Configure domain access</h2>
<p>An Administrator or Super Administrator with access to all domains must select which domains should show the pay per crawl controls:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2765.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="visibility-vs-security">Visibility vs Security</h3>
@markup("md", "content/.markup/bodies/2764.md")
</aside>
<p>After completing these steps, domain administrators can set a pay per crawl price and enable pay per crawl for their specific domains.</p>
