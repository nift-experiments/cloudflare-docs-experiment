<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>December 18, 2025</time><h2 id="post-title">Improved accuracy of cached request classification in analytics</h2>
<div class="changelog-badges"><span>analytics</span></div><div class="changelog-body"><p>The cached/uncached classification logic used in Zone Overview analytics has been updated to improve accuracy.</p>
<p>Previously, requests were classified as &quot;cached&quot; based on an overly broad condition that included blocked 403 responses, Snippets requests, and other non-cache request types. This caused inflated cache hit ratios — in some cases showing near-100% cached — and affected approximately 15% of requests classified as cached in rollups.</p>
<p>The condition has been removed from the Zone Overview page. Cached/uncached classification now aligns with the heuristics used in <a href="/analytics/account-and-zone-analytics/zone-analytics/">HTTP Analytics</a>, so only requests genuinely served from cache are counted as cached.</p>
<p><strong>What changed:</strong></p>
<ul>
<li><strong>Zone Overview</strong> — Cache ratios now reflect actual cache performance.</li>
<li><strong>HTTP Analytics</strong> — No change. HTTP Analytics already used the correct classification logic.</li>
<li><strong>Historical data</strong> — This fix applies to new requests only. Previously logged data is not retroactively updated.</li>
</ul>
</div></article></div>
