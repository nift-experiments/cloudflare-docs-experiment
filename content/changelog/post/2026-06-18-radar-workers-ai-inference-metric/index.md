<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 18, 2026</time><h2 id="post-title">Updated Workers AI popularity metric in Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> has changed how it measures <a href="/workers-ai/">Workers AI</a> model and task popularity.</p>
<p>Previously, popularity was based on the number of unique accounts running inferences against each model or task. It is now based on the <strong>number of inferences</strong>, giving a more representative view of actual usage volume. This change will affect all new measurements as well as historical data. As a result, the model and task distributions shown on Radar may differ from what you saw previously, and historical trends may shift accordingly.</p>
<p>The <a href="https://radar.cloudflare.com/ai-insights#workers-ai-model-popularity">Workers AI model popularity</a> chart shows the distribution of inferences across models.</p>
<p><img src="/assets/upstream/images/radar/workers-ai-model-popularity.png" alt="Screenshot of the Workers AI model popularity chart on the AI Insights page" /></p>
<p>The <a href="https://radar.cloudflare.com/ai-insights#workers-ai-task-popularity">Workers AI task popularity</a> chart shows the distribution of inferences across tasks.</p>
<p><img src="/assets/upstream/images/radar/workers-ai-task-popularity.png" alt="Screenshot of the Workers AI task popularity chart on the AI Insights page" /></p>
<p>The same data is available via the following API endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/ai/subresources/inference/methods/summary_v2/"><code>/ai/inference/summary/{dimension}</code></a></li>
<li><a href="/api/resources/radar/subresources/ai/subresources/inference/methods/timeseries_groups_v2/"><code>/ai/inference/timeseries_groups/{dimension}</code></a></li>
</ul>
<p>Explore the data on the <a href="https://radar.cloudflare.com/ai-insights">AI Insights page</a>.</p>
</div></article></div>
