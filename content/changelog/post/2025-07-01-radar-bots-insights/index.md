<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 1, 2025</time><h2 id="post-title">Bot &amp; Crawler Insights in Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><h4 id="web-crawlers-insights">Web crawlers insights</h4>
<p><a href="/radar/"><strong>Radar</strong></a> now offers expanded insights into web crawlers, giving you greater visibility into aggregated trends in crawl and refer activity.</p>
<p>We have introduced the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/bots/subresources/web_crawlers/methods/summary/"><code>/bots/crawlers/summary/{dimension}</code></a>: Returns an overview of crawler HTTP request distributions across key dimensions.</li>
<li><a href="/api/resources/radar/subresources/bots/subresources/web_crawlers/methods/timeseries_groups/"><code>/bots/crawlers/timeseries_groups/{dimension}</code></a>: Provides time-series data on crawler request distributions across the same dimensions.</li>
</ul>
<p>These endpoints allow analysis across the following dimensions:</p>
<ul>
<li><code>user_agent</code>: Parsed data from the <code>User-Agent</code> header.</li>
<li><code>referer</code>: Parsed data from the <code>Referer</code> header.</li>
<li><code>crawl_refer_ratio</code>: Ratio of HTML page crawl requests to HTML page referrals by platform.</li>
</ul>
<h4 id="broader-bot-insights">Broader bot insights</h4>
<p>In addition to crawler-specific insights, Radar now provides a broader set of bot endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/bots/"><code>/bots/</code></a>: Lists all bots.</li>
<li><a href="/api/resources/radar/subresources/bots/methods/get/"><code>/bots/{bot_slug}</code></a>: Returns detailed metadata for a specific bot.</li>
<li><a href="/api/resources/radar/subresources/bots/methods/timeseries/"><code>/bots/timeseries</code></a>: Time-series data for bot activity.</li>
<li><a href="/api/resources/radar/subresources/bots/methods/summary/"><code>/bots/summary/{dimension}</code></a>: Returns an overview of bot HTTP request distributions across key dimensions.</li>
<li><a href="/api/resources/radar/subresources/bots/methods/timeseries_groups/"><code>/bots/timeseries_groups/{dimension}</code></a>: Provides time-series data on bot request distributions across the same dimensions.</li>
</ul>
<p>These endpoints support filtering and breakdowns by:</p>
<ul>
<li><code>bot</code>: Bot name.</li>
<li><code>bot_operator</code>: The organization or entity operating the bot.</li>
<li><code>bot_category</code>: Classification of bot type.</li>
</ul>
<p>The previously available <code>verified_bots</code> endpoints have now been deprecated in favor of this set of bot insights APIs.
While current data still focuses on verified bots, we plan to expand support for unverified bot traffic in the future.</p>
<p>Learn more about the new Radar bot and crawler insights in our <a href="https://blog.cloudflare.com/ai-search-crawl-refer-ratio-on-radar">blog post</a>.</p>
</div></article></div>
