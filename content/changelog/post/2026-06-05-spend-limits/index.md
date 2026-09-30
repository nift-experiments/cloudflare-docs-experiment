<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 5, 2026</time><h2 id="post-title">Control AI costs with spend limits</h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p>AI Gateway now supports spend limits — cost-based budgets that track cumulative dollar spend and block requests when the budget is exceeded. Unlike rate limiting, which caps the number of requests, spend limits track actual cost based on token usage and model pricing.</p>
<p>You can scope limits by model, provider, or custom metadata dimensions. For example, give each user a $200/day budget, cap total gateway spend at $10,000/day, or limit a specific model to $50/day per user. Each rule uses a configurable time window with fixed or sliding enforcement.</p>
<p>Spend limits work with both <a href="/ai-gateway/features/unified-billing/">Unified Billing</a> and <a href="/ai-gateway/configuration/bring-your-own-keys/">BYOK</a> requests for models with known pricing.</p>
<p>For more details, refer to the <a href="/ai-gateway/features/spend-limits/">Spend limits documentation</a>.</p>
</div></article></div>
