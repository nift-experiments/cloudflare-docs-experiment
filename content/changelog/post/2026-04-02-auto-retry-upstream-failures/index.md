<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 2, 2026</time><h2 id="post-title">Automatically retry on upstream provider failures on AI Gateway</h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p>AI Gateway now supports automatic retries at the gateway level. When an upstream provider returns an error, your gateway retries the request based on the retry policy you configure, without requiring any client-side changes.</p>
<p>You can configure the retry count (up to 5 attempts), the delay between retries (from 100ms to 5 seconds), and the backoff strategy (Constant, Linear, or Exponential). These defaults apply to all requests through the gateway, and per-request headers can override them.</p>
<p><img src="/assets/upstream/images/ai-gateway/auto-retry-changelog.png" alt="Retry Requests settings in the AI Gateway dashboard" /></p>
<p>This is particularly useful when you do not control the client making the request and cannot implement retry logic on the caller side. For more complex failover scenarios — such as failing across different providers — use <a href="/ai-gateway/features/dynamic-routing/">Dynamic Routing</a>.</p>
<p>For more information, refer to <a href="/ai-gateway/configuration/manage-gateway/#retry-requests">Manage gateways</a>.</p>
</div></article></div>
