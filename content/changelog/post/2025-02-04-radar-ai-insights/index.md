<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 4, 2025</time><h2 id="post-title">Expanded AI insights in Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> has expanded its AI insights with new API endpoints for Internet services rankings, robots.txt analysis, and AI inference data.</p>
<h4 id="internet-services-ranking">Internet services ranking</h4>
<p>Radar now provides <a href="/radar/glossary/#internet-services-ranking">rankings for Internet services</a>, including Generative AI platforms, based on anonymized 1.1.1.1 resolver data.
Previously limited to the annual Year in Review, these insights are now available daily via the <a href="/api/resources/radar/subresources/ranking/subresources/internet_services/">API</a>, through the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/ranking/subresources/internet_services/methods/top/"><code>/ranking/internet_services/top</code></a> show service popularity at a specific date.</li>
<li><a href="/api/resources/radar/subresources/ranking/subresources/internet_services/methods/timeseries_groups/"><code>/ranking/internet_services/timeseries_groups</code></a> track ranking trends over time.</li>
</ul>
<h4 id="robots-txt">Robots.txt</h4>
<p>Radar now analyzes <a href="/radar/glossary/#robotstxt">robots.txt</a> files from the top 10,000 domains, identifying AI bot access rules.
AI-focused user agents from <a href="https://github.com/ai-robots-txt/ai.robots.txt">ai.robots.txt</a> are categorized as:</p>
<ul>
<li><strong>Fully allowed/disallowed</strong> if directives apply to all paths (<code>*</code>).</li>
<li><strong>Partially allowed/disallowed</strong> if restrictions apply to specific paths.</li>
</ul>
<p>These insights are now available weekly via the <a href="/api/resources/radar/subresources/robots_txt/">API</a>, through the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/robots_txt/subresources/top/subresources/user_agents/methods/directive/"><code>/robots_txt/top/user_agents/directive</code></a> to get the top AI user agents by directive.</li>
<li><a href="/api/resources/radar/subresources/robots_txt/subresources/top/methods/domain_categories/"><code>/robots_txt/top/domain_categories</code></a> to get the top domain categories by robots.txt files.</li>
</ul>
<h4 id="workers-ai">Workers AI</h4>
<p>Radar now provides insights into public AI inference models from <a href="/workers-ai/">Workers AI</a>, tracking usage trends across <strong>models</strong> and <strong>tasks</strong>.
These insights are now available via the <a href="/api/resources/radar/subresources/ai/subresources/inference/">API</a>, through the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/ai/subresources/inference/subresources/summary/"><code>/ai/inference/summary/{dimension}</code></a> to view aggregated <code>model</code> and <code>task</code> popularity.</li>
<li><a href="/api/resources/radar/subresources/ai/subresources/inference/subresources/timeseries_groups/"><code>/ai/inference/timeseries_groups/{dimension}</code></a> to track changes over time for <code>model</code> or <code>task</code>.</li>
</ul>
<p>Learn more about the new Radar AI insights in our <a href="https://blog.cloudflare.com/expanded-ai-insights-on-cloudflare-radar/">blog post</a>.</p>
</div></article></div>
