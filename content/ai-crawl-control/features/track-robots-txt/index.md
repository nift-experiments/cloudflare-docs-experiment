---
cp9:
  canonical: https://developers.cloudflare.com/ai-crawl-control/features/track-robots-txt/
  description: Monitor AI crawler interactions with your robots.txt files.
  full_title: Directives · Cloudflare AI Crawl Control docs
  head_html: <title>Directives · Cloudflare AI Crawl Control docs</title><meta name="generator" content="Nift"><meta name="description" content="Monitor AI crawler interactions with your robots.txt files."><link rel="canonical" href="https://developers.cloudflare.com/ai-crawl-control/features/track-robots-txt/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-crawl-control/features/track-robots-txt/index.md"><meta property="og:title" content="Directives · Cloudflare AI Crawl Control docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Monitor AI crawler interactions with your robots.txt files."><meta property="og:url" content="https://developers.cloudflare.com/ai-crawl-control/features/track-robots-txt/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Crawl Control"><meta name="algolia_product_filter" content="AI Crawl Control"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="AI Crawl Control"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-crawl-control/features/track-robots-txt/#page","headline":"Directives \u00b7 Cloudflare AI Crawl Control docs","description":"Monitor AI crawler interactions with your robots.txt files.","url":"https://developers.cloudflare.com/ai-crawl-control/features/track-robots-txt/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-crawl-control/features/track-robots-txt/
  schema: 1
---
<p>The <strong>Directives</strong> tab in AI Crawl Control provides insights into how AI crawlers interact with your <span class="nb-glossary-tooltip" title="robots.txt">�CODE0�</span> files across your hostnames. You can monitor request patterns, verify file availability, identify crawlers that violate your directives, and assess your site's readiness for AI agents.</p>
<p>To access directives insights:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and select your account and domain.</li>
<li>Go to <strong>AI Crawl Control</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="3">
<li>Go to the <strong>Directives</strong> tab.</li>
</ol>
<h2 id="check-managed-robots-txt-status">Check managed robots.txt status</h2>
<p>The status card at the top of the tab shows whether Cloudflare is managing your <code>robots.txt</code> file.</p>
<p>When enabled, Cloudflare will include directives to block common AI crawlers used for training and include its <a href="/bots/additional-configurations/managed-robots-txt/#content-signals-policy">Content Signals Policy</a> in your <code>robots.txt</code>. For more details on how Cloudflare manages your <code>robots.txt</code> file, refer to <a href="/bots/additional-configurations/managed-robots-txt/">Managed <code>robots.txt</code></a>.</p>
<h2 id="filter-robots-txt-request-data">Filter robots.txt request data</h2>
<p>You can apply filters at the top of the tab to narrow your analysis of robots.txt requests:</p>
<ul>
<li>Filter by specific crawler name (for example, Googlebot or specific AI bots).</li>
<li>Filter by the entity running the crawler to understand direct licensing opportunities or existing agreements.</li>
<li>Filter by general use cases (for example, AI training, general search, or AI assistant).</li>
<li>Select a custom time frame for historical analysis.</li>
</ul>
<p>The values in all tables and metrics will update according to your filters.</p>
<h2 id="monitor-robots-txt-availability">Monitor robots.txt availability</h2>
<p>The <strong>Robots.txt availability</strong> table shows the historical request frequency and health status of <code>robots.txt</code> files across your hostnames over the selected time frame.</p>
<table>
<thead>
<tr>
<th>Column</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Path</td>
<td>The specific hostname's <code>robots.txt</code> file being requested. Paths are listed from the most requested to the least.</td>
</tr>
<tr>
<td>Requests</td>
<td>The total number of requests made to this path. Requests are broken down into:<br/>- <strong>Successful:</strong> HTTP status codes below 400 (including <strong>200 OK</strong> and redirects).<br/>- <strong>Unsuccessful:</strong> HTTP status codes of 400 or above.</td>
</tr>
<tr>
<td>Status</td>
<td>The HTTP status code from pinging the <code>robots.txt</code> file.</td>
</tr>
<tr>
<td>Content Signals</td>
<td>An indicator showing whether the <code>robots.txt</code> file contains <a href="https://contentsignals.org/">Content Signals</a>, directives for usage in AI training, search, or AI input.</td>
</tr>
</tbody>
</table>
<p>From this table, you can take the following actions:</p>
<ul>
<li>Monitor for a high number of unsuccessful requests, which suggests that crawlers are having trouble accessing your <code>robots.txt</code> file.
<ul>
<li>If the <strong>Status</strong> is <code>404 Not Found</code>, create a <code>robots.txt</code> file to provide clear directives.</li>
<li>If the file exists, check for upstream WAF rules or other security settings that may be blocking access.</li>
</ul>
</li>
<li>If the <strong>Content Signals</strong> column indicates that signals are missing, add them to your <code>robots.txt</code> file. You can do this by following the <a href="https://contentsignals.org/">Content Signals</a> instructions or by enabling <a href="/bots/additional-configurations/managed-robots-txt/">Managed <code>robots.txt</code></a> to have Cloudflare manage them for you.</li>
</ul>
<h2 id="track-robots-txt-violations">Track robots.txt violations</h2>
<p>The <strong>Robots.txt violations</strong> table identifies AI crawlers that have requested paths explicitly disallowed by your <code>robots.txt</code> file. This helps you identify non-compliant crawlers and take appropriate action.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="how-violations-are-calculated">How violations are calculated</h3>
@markup("md", "content/.markup/bodies/2727.md")
</aside>
<table>
<thead>
<tr>
<th>Column</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Crawler</td>
<td>The name of the bot that violated your <code>robots.txt</code> directives. The operator of the crawler is listed directly beneath the crawler name.</td>
</tr>
<tr>
<td>Path</td>
<td>The specific URL or path the crawler attempted to access that was disallowed by your <code>robots.txt</code> file.</td>
</tr>
<tr>
<td>Directive</td>
<td>The exact line from your <code>robots.txt</code> file that disallowed access to the path.</td>
</tr>
<tr>
<td>Violations</td>
<td>The count of HTTP requests made to the disallowed path/directive pair within the selected time frame.</td>
</tr>
</tbody>
</table>
<p>When you identify crawlers violating your <code>robots.txt</code> directives, you have several options:</p>
<ul>
<li>Navigate to the <a href="/ai-crawl-control/features/manage-ai-crawlers/"><strong>Crawlers</strong> tab</a> to permanently block the non-compliant crawler.</li>
<li>Use <a href="/waf/">Cloudflare WAF</a> to create a path-specific security rules for the violating crawler.</li>
<li>Use <a href="/rules/url-forwarding/">Redirect Rules</a> to guide violating crawlers to an appropriate area of your site.</li>
</ul>
<h2 id="check-agent-readiness">Check Agent Readiness</h2>
<p>The <strong>Agent Readiness</strong> card helps you assess how well your site is configured for AI agents. Select <strong>Check readiness score</strong> to scan your site against emerging standards for AI agent interaction, including:</p>
<ul>
<li><strong>Robots.txt configuration</strong>: Whether your site has a valid <code>robots.txt</code> file with appropriate directives</li>
<li><strong>Markdown for Agents</strong>: Whether your site supports content negotiation for AI-optimized content delivery</li>
<li><strong>Content Signals Policy</strong>: Whether your site signals content usage preferences to AI crawlers</li>
</ul>
<p>The scan is powered by <a href="https://isitagentready.com">isitagentready.com</a>. Results include recommendations for improving your site's compatibility with AI agents and crawlers.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/ai-crawl-control/features/manage-ai-crawlers/">Manage AI crawlers</a></li>
<li><a href="/ai-crawl-control/features/analyze-ai-traffic/">Analyze AI traffic</a></li>
<li><a href="/waf/">Cloudflare WAF</a></li>
</ul>
