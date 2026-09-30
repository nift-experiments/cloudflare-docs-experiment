<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 1, 2026</time><h2 id="post-title">AI Gateway consolidates monthly usage invoice line items and standardizes model names</h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p>AI Gateway monthly usage invoices, issued at the beginning of each month for the previous month's usage, now show a single total cost for each model. These invoices no longer break out input and output token quantities and unit prices into separate line items. This change does not apply to invoices for AI Gateway credit purchases.</p>
<p>For example, an invoice that previously included these separate line items:</p>
<ul>
<li><code>anthropic claude-haiku-4-5-20251001 Input Tokens</code>: 40,000 tokens at $0.000001 ($0.04)</li>
<li><code>anthropic claude-haiku-4-5-20251001 Output Tokens</code>: 24,000 tokens at $0.000005 ($0.12)</li>
</ul>
<p>The updated invoice includes one line item: <code>anthropic/claude-haiku-4.5</code>: $0.16.</p>
<p>AI Gateway has also standardized model names across invoices and logs. Model variants that previously appeared with provider-specific version suffixes now use a consistent <code>provider/model</code> identifier.</p>
<p>For more information, refer to the <a href="/ai-gateway/features/unified-billing/">Unified Billing documentation</a> and <a href="/ai-gateway/observability/logging/">AI Gateway logging documentation</a>.</p>
</div></article></div>
