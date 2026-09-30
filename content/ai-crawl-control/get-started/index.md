---
cp9:
  canonical: https://developers.cloudflare.com/ai-crawl-control/get-started/
  description: Learn how to set up AI Crawl Control.
  full_title: Get started with Cloudflare AI Crawl Control · Cloudflare AI Crawl Control docs
  head_html: <title>Get started with Cloudflare AI Crawl Control · Cloudflare AI Crawl Control docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to set up AI Crawl Control."><link rel="canonical" href="https://developers.cloudflare.com/ai-crawl-control/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-crawl-control/get-started/index.md"><meta property="og:title" content="Get started with Cloudflare AI Crawl Control · Cloudflare AI Crawl Control docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to set up AI Crawl Control."><meta property="og:url" content="https://developers.cloudflare.com/ai-crawl-control/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Crawl Control"><meta name="algolia_product_filter" content="AI Crawl Control"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="AI Crawl Control"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-crawl-control/get-started/#page","headline":"Get started with Cloudflare AI Crawl Control \u00b7 Cloudflare AI Crawl Control docs","description":"Learn how to set up AI Crawl Control.","url":"https://developers.cloudflare.com/ai-crawl-control/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-crawl-control/get-started/
  schema: 1
---
<p>This guide instructs you on how to:</p>
<ul>
<li>View AI crawlers that are interacting with pages in your domain (a <a href="/fundamentals/concepts/accounts-and-zones/#zones">Cloudflare zone</a>).</li>
<li>Use AI Crawl Control to block individual crawlers from accessing your content.</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/">Cloudflare account</a>.</li>
<li><a href="/fundamentals/manage-domains/add-site/">Connect your domain to Cloudflare</a>.</li>
<li>Make sure your domain is <a href="/fundamentals/concepts/how-cloudflare-works/#cloudflare-as-a-reverse-proxy">proxying traffic through Cloudflare</a>.</li>
</ol>
<h2 id="1-monitor-ai-crawler-activity-at-a-glance"><ol>
<li>Monitor AI crawler activity at a glance</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/1608.md")
</div>
<h2 id="2-block-specific-ai-crawlers"><ol start="2">
<li>Block specific AI crawlers</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="plans"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/1613.md")
</div></div>
<p>For more information, refer to <a href="/ai-crawl-control/features/manage-ai-crawlers/">Manage AI crawlers</a>.</p>
<p>You can also create more complex rules when taking action on AI crawlers, using <a href="/waf/">Cloudflare WAF</a>. For more information on creating more specific rules, refer to <a href="/waf/custom-rules/create-dashboard/">Create a custom rule in the dashboard</a>.</p>
<h2 id="3-explore-detailed-metrics"><ol start="3">
<li>Explore detailed metrics</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/1616.md")
</div></div>
<p>Note that on free plans, the <strong>Metrics</strong> tab only displays metrics for the past 24 hours.</p>
<h2 id="plan-comparison">Plan comparison</h2>
<table>
<thead>
<tr>
<th>All plans</th>
<th>Enterprise plans with Bot Management</th>
</tr>
</thead>
<tbody>
<tr>
<td>AI crawler detection via <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent">user agent strings</a></td>
<td>Advanced AI crawler detection via <a href="/bots/reference/bot-management-variables/#ruleset-engine-fields">Bot Management detection ID</a></td>
</tr>
<tr>
<td>Maximum 24-hour analytics window</td>
<td>Configurable analytics timeframes</td>
</tr>
<tr>
<td>Allow/block controls</td>
<td>Allow/block controls, and the ability to charge AI crawlers using <a href="/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/">pay per crawl</a></td>
</tr>
</tbody>
</table>
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/ai-crawl-control/features/manage-ai-crawlers/">Manage AI crawlers</a> with granular allow/block controls.</li>
<li><a href="/ai-crawl-control/features/analyze-ai-traffic/">Analyze AI traffic</a> to understand crawler patterns and content popularity.</li>
<li><a href="/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/">Explore pay per crawl</a> to test content monetization options (private beta).</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<p>Refer to the following related resources:</p>
<ul>
<li>Cloudflare blog: <a href="https://blog.cloudflare.com/nl-nl/cloudflare-ai-audit-control-ai-content-crawlers/">Start auditing and controlling the AI models accessing your content</a></li>
<li>Block AI crawlers that do not adhere to recommended guidelines using <a href="/bots/additional-configurations/ai-labyrinth/">Cloudflare AI Labyrinth</a>.</li>
<li><a href="/bots/additional-configurations/managed-robots-txt/">Direct AI crawlers with managed robots.txt</a>.</li>
</ul>
