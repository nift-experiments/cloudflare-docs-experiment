---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-04-17-radar-ai-insights-updates/
  description: New updates and improvements at Cloudflare.
  full_title: AI Insights updates on Cloudflare Radar · Changelog
  head_html: <title>AI Insights updates on Cloudflare Radar · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-04-17-radar-ai-insights-updates/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="AI Insights updates on Cloudflare Radar · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-04-17-radar-ai-insights-updates/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-17-radar-ai-insights-updates/#page","headline":"AI Insights updates on Cloudflare Radar \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-04-17-radar-ai-insights-updates/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-04-17-radar-ai-insights-updates/
  schema: 1
---
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
