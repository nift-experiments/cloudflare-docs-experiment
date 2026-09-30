<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 17, 2026</time><h2 id="post-title">AI Insights updates on Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> adds three new features to the <a href="https://radar.cloudflare.com/ai-insights">AI Insights</a> page, expanding visibility into how AI bots, crawlers, and agents interact with the web.</p>
<h4 id="adoption-of-ai-agent-standards">Adoption of AI agent standards</h4>
<p>The AI Insights page now includes an <a href="https://radar.cloudflare.com/ai-insights#adoption-of-ai-agent-standards">adoption of AI agent standards</a> widget that tracks how websites adopt agent-facing standards. The data is filterable by domain category and updated weekly on Mondays.
This data is also available through the <a href="/api/resources/radar/subresources/agent_readiness/methods/summary/">Agent Readiness API reference</a>.</p>
<p><img src="/assets/upstream/images/radar/agent-readiness-adoption-chart.png" alt="Screenshot of the adoption of AI agent standards chart" /></p>
<p><a href="https://radar.cloudflare.com/scan">URL Scanner</a> reports now include an <strong>Agent readiness</strong> tab that evaluates a scanned URL against the criteria used by the <a href="https://isitagentready.com/">Agent Readiness score tool</a>.</p>
<p><img src="/assets/upstream/images/radar/agent-readiness-url-scanner.png" alt="Screenshot of the URL Scanner agent readiness tab" /></p>
<p>For more details, refer to the <a href="https://blog.cloudflare.com/agent-readiness/">Agent Readiness blog post</a>.</p>
<h4 id="markdown-for-agents-savings">Markdown for Agents savings</h4>
<p>A new <a href="https://radar.cloudflare.com/ai-insights#markdown-for-agents-savings">savings gauge</a> shows the median response-size reduction when serving Markdown instead of HTML to AI bots and crawlers. This highlights the bandwidth and token savings that <a href="/fundamentals/reference/markdown-for-agents/">Markdown for Agents</a> provides.</p>
<div style="max-width: 300px;">
<p><img src="/assets/upstream/images/radar/markdown-for-agents-savings.png" alt="Screenshot of the Markdown for Agents savings gauge" /></p>
</div>
<p>For more details, refer to the <a href="/api/resources/radar/subresources/ai/subresources/markdown_for_agents/methods/summary">Markdown for Agents API reference</a>.</p>
<h4 id="response-status">Response status</h4>
<p>The new <a href="https://radar.cloudflare.com/ai-insights#response-status">response status widget</a> displays the distribution of HTTP response status codes returned to AI bots and crawlers. Results are groupable by individual status code (200, 403, 404) or by category (2xx, 3xx, 4xx, 5xx).</p>
<p>The same widget is available on each verified bot's detail page (only available for AI bots), for example <a href="https://radar.cloudflare.com/bots/directory/google#response-status">Google</a>.</p>
<p><img src="/assets/upstream/images/radar/ai-response-status.png" alt="Screenshot of the response status distribution widget" /></p>
<p>Explore all three features on the <a href="https://radar.cloudflare.com/ai-insights">Cloudflare Radar AI Insights</a> page.</p>
</div></article></div>
