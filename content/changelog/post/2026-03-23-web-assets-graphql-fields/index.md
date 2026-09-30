<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 23, 2026</time><h2 id="post-title">Web Assets fields now available in GraphQL Analytics API</h2>
<div class="changelog-badges"><span>api-shield</span></div><div class="changelog-body"><p>Two new fields are now available in the <code>httpRequestsAdaptive</code> and <code>httpRequestsAdaptiveGroups</code> <a href="/analytics/graphql-api/">GraphQL Analytics API</a> datasets:</p>
<ul>
<li><code>webAssetsOperationId</code> — the ID of the <a href="/api-shield/management-and-monitoring/">saved endpoint</a> that matched the incoming request.</li>
<li><code>webAssetsLabelsManaged</code> — the <a href="/api-shield/management-and-monitoring/endpoint-labels/#managed-labels">managed labels</a> mapped to the matched operation at the time of the request (for example, <code>cf-llm</code>, <code>cf-log-in</code>). At most 10 labels are returned per request.</li>
</ul>
<p>Both fields are empty when no operation matched. <code>webAssetsLabelsManaged</code> is also empty when no managed labels are assigned to the matched operation.</p>
<p>These fields allow you to determine, per request, which Web Assets operation was matched and which managed labels were active. This is useful for troubleshooting downstream security detection verdicts — for example, understanding why <a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a> did or did not flag a request.</p>
<p>Refer to <a href="/api-shield/management-and-monitoring/endpoint-labels/#analytics">Endpoint labeling service</a> for GraphQL query examples.</p>
</div></article></div>
