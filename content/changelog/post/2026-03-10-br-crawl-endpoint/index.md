<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 10, 2026</time><h2 id="post-title">Crawl entire websites with a single API call using Browser Rendering</h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p><em>Edit: this post has been edited to clarify crawling behavior with respect to site guidance.</em></p>
<p>You can now crawl an entire website with a single API call using <a href="/browser-run/">Browser Rendering</a>'s new <a href="/browser-run/quick-actions/crawl-endpoint/"><code>/crawl</code> endpoint</a>, available in open beta. Submit a starting URL, and pages are automatically discovered, rendered in a headless browser, and returned in multiple formats, including HTML, Markdown, and structured JSON. The endpoint is a <a href="/bots/concepts/bot/verified-bots/">verified bot (intermediary agent)</a> that respects robots.txt and <a href="https://www.cloudflare.com/ai-crawl-control/">AI Crawl Control</a> by default, making it easy for developers to comply with website rules, and making it less likely for crawlers to ignore web-owner guidance. This is great for training models, building RAG pipelines, and researching or monitoring content across a site.</p>
<p>Crawl jobs run asynchronously. You submit a URL, receive a job ID, and check back for results as pages are processed.</p>
<pre><code class="language-sh">&#35; Initiate a crawl&#10;curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://blog.cloudflare.com/&quot;&#10;  }&#x27;&#10;&#10;&#35; Check results&#10;curl -X GET &#x27;https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/crawl/{job_id}&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;apiToken&gt;&#x27;&#10;</code></pre>
<p>Key features:</p>
<ul>
<li><strong>Multiple output formats</strong> - Return crawled content as HTML, Markdown, and structured JSON (powered by <a href="/workers-ai/">Workers AI</a>)</li>
<li><strong>Crawl scope controls</strong> - Configure crawl depth, page limits, and wildcard patterns to include or exclude specific URL paths</li>
<li><strong>Automatic page discovery</strong> - Discovers URLs from sitemaps, page links, or both</li>
<li><strong>Incremental crawling</strong> - Use <code>modifiedSince</code> and <code>maxAge</code> to skip pages that haven't changed or were recently fetched, saving time and cost on repeated crawls</li>
<li><strong>Static mode</strong> - Set <code>render: false</code> to fetch static HTML without spinning up a browser, for faster crawling of static sites</li>
<li><strong>Well-behaved bot</strong> - Honors <code>robots.txt</code> directives, including <code>crawl-delay</code></li>
</ul>
<p>Available on both the Workers Free and Paid plans.</p>
<p><strong>Note</strong>: the /crawl endpoint cannot bypass Cloudflare bot detection or captchas, and self-identifies as a bot.</p>
<p>To get started, refer to the <a href="/browser-run/quick-actions/crawl-endpoint/">crawl endpoint documentation</a>.
If you are setting up your own site to be crawled, review the <a href="/browser-run/reference/robots-txt/">robots.txt and sitemaps best practices</a>.</p>
</div></article></div>
