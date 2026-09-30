<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 21, 2025</time><h2 id="post-title">New Robots.txt tab for tracking crawler compliance</h2>
<div class="changelog-badges"><span>ai-crawl-control</span></div><div class="changelog-body"><p>AI Crawl Control now includes a <strong>Robots.txt</strong> tab that provides insights into how AI crawlers interact with your <code>robots.txt</code> files.</p>
<h4 id="what-s-new">What's new</h4>
<p>The Robots.txt tab allows you to:</p>
<ul>
<li>Monitor the health status of <code>robots.txt</code> files across all your hostnames, including HTTP status codes, and identify hostnames that need a <code>robots.txt</code> file.</li>
<li>Track the total number of requests to each <code>robots.txt</code> file, with breakdowns of successful versus unsuccessful requests.</li>
<li>Check whether your <code>robots.txt</code> files contain <a href="https://contentsignals.org/">Content Signals</a> directives for AI training, search, and AI input.</li>
<li>Identify crawlers that request paths explicitly disallowed by your <code>robots.txt</code> directives, including the crawler name, operator, violated path, specific directive, and violation count.</li>
<li>Filter <code>robots.txt</code> request data by crawler, operator, category, and custom time ranges.</li>
</ul>
<h4 id="take-action">Take action</h4>
<p>When you identify non-compliant crawlers, you can:</p>
<ul>
<li>Block the crawler in the <a href="/ai-crawl-control/features/manage-ai-crawlers/">Crawlers tab</a></li>
<li>Create custom <a href="/waf/">WAF rules</a> for path-specific security</li>
<li>Use <a href="/rules/url-forwarding/">Redirect Rules</a> to guide crawlers to appropriate areas of your site</li>
</ul>
<p>To get started, go to <strong>AI Crawl Control</strong> &gt; <strong>Robots.txt</strong> in the Cloudflare dashboard. Learn more in the <a href="/ai-crawl-control/features/track-robots-txt/">Track robots.txt documentation</a>.</p>
</div></article></div>
