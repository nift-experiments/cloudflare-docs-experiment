<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 25, 2025</time><h2 id="post-title">New Zombie API detection for API Shield</h2>
<div class="changelog-badges"><span>api-shield</span></div><div class="changelog-body"><p>API Shield now automatically detects zombie endpoints — saved endpoints that have not received traffic for an extended period. When detected, the <code>cf-risk-zombie</code> <a href="/api-shield/management-and-monitoring/endpoint-labels/#risk-labels">risk label</a> is applied.</p>
<p>The scan runs daily alongside existing risk scans. Endpoints are labeled after 32 days without traffic.</p>
<p>Zombie endpoints may indicate deprecated or forgotten API surface area that could pose a security risk. Review these endpoints and consider removing them from Endpoint Management if they are no longer in use. Also consider using a <a href="/api-shield/security/schema-validation/#add-validation-by-adding-a-fallthrough-rule">fallthrough rule</a> to prevent communication with endpoints removed from Endpoint Management.</p>
</div></article></div>
