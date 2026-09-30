<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 10, 2025</time><h2 id="post-title">Crawler drilldowns with extended actions menu</h2>
<div class="changelog-badges"><span>ai-crawl-control</span></div><div class="changelog-body"><p>AI Crawl Control now supports per-crawler drilldowns with an extended actions menu and status code analytics. Drill down into Metrics, Cloudflare Radar, and Security Analytics, or export crawler data for use in <a href="/waf/custom-rules/">WAF custom rules</a>, <a href="/rules/url-forwarding/">Redirect Rules</a>, and robots.txt files.</p>
<h4 id="what-s-new">What's new</h4>
<h4 id="status-code-distribution-chart">Status code distribution chart</h4>
<p>The <strong>Metrics</strong> tab includes a status code distribution chart showing HTTP response codes (2xx, 3xx, 4xx, 5xx) over time. Filter by individual crawler, category, operator, or time range to analyze how specific crawlers interact with your site.</p>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-status-codes.png" alt="AI Crawl Control status code distribution chart" /></p>
<h4 id="extended-actions-menu">Extended actions menu</h4>
<p>Each crawler row includes a three-dot menu with per-crawler actions:</p>
<ul>
<li><strong>View Metrics</strong> — Filter the AI Crawl Control Metrics page to the selected crawler.</li>
<li><strong>View on Cloudflare Radar</strong> — Access verified crawler details on Cloudflare Radar.</li>
<li><strong>Copy User Agent</strong> — Copy user agent strings for use in WAF custom rules, Redirect Rules, or robots.txt files.</li>
<li><strong>View in Security Analytics</strong> — Filter Security Analytics by detection IDs (Bot Management customers).</li>
<li><strong>Copy Detection ID</strong> — Copy detection IDs for use in WAF custom rules (Bot Management customers).</li>
</ul>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-crawler-info.png" alt="AI Crawl Control crawler actions menu" /></p>
<h4 id="get-started">Get started</h4>
<ol>
<li>Log in to the Cloudflare dashboard, and select your account and domain.</li>
<li>Go to <strong>AI Crawl Control</strong> &gt; <strong>Metrics</strong> to access the status code distribution chart.</li>
<li>Go to <strong>AI Crawl Control</strong> &gt; <strong>Crawlers</strong> and select the three-dot menu for any crawler to access per-crawler actions.</li>
<li>Select multiple crawlers to use bulk copy buttons for user agents or detection IDs.</li>
</ol>
<p>Learn more about <a href="/ai-crawl-control/">AI Crawl Control</a>.</p>
</div></article></div>
