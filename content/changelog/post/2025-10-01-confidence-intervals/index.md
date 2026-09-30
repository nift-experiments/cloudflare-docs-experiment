<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 1, 2025</time><h2 id="post-title">New Confidence Intervals in GraphQL Analytics API</h2>
<div class="changelog-badges"><span>analytics</span></div><div class="changelog-body"><p>The GraphQL Analytics API now supports confidence intervals for <code>sum</code> and <code>count</code> fields on adaptive (sampled) datasets. Confidence intervals provide a statistical range around sampled results, helping verify accuracy and quantify uncertainty.</p>
<ul>
<li><strong>Supported datasets</strong>: Adaptive (sampled) datasets only.</li>
<li><strong>Supported fields</strong>: All <code>sum</code> and <code>count</code> fields.</li>
<li><strong>Usage</strong>: The confidence <code>level</code> must be provided as a decimal between 0 and 1 (e.g. <code>0.90</code>, <code>0.95</code>, <code>0.99</code>).</li>
<li><strong>Default</strong>: If no confidence level is specified, no intervals are returned.</li>
</ul>
<p>For examples and more details, see the <a href="/analytics/graphql-api/features/confidence-intervals/">GraphQL Analytics API documentation</a>.</p>
</div></article></div>
