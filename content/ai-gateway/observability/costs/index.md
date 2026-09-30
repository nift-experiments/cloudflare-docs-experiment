---
cp9:
  canonical: https://developers.cloudflare.com/ai-gateway/observability/costs/
  description: Track and estimate token-based costs across AI providers using AI Gateway cost metrics.
  full_title: Costs · Cloudflare AI Gateway docs
  head_html: <title>Costs · Cloudflare AI Gateway docs</title><meta name="generator" content="Nift"><meta name="description" content="Track and estimate token-based costs across AI providers using AI Gateway cost metrics."><link rel="canonical" href="https://developers.cloudflare.com/ai-gateway/observability/costs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ai-gateway/observability/costs/index.md"><meta property="og:title" content="Costs · Cloudflare AI Gateway docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Track and estimate token-based costs across AI providers using AI Gateway cost metrics."><meta property="og:url" content="https://developers.cloudflare.com/ai-gateway/observability/costs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="AI Gateway"><meta name="algolia_product_filter" content="AI Gateway"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="AI Gateway"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ai-gateway/observability/costs/#page","headline":"Costs \u00b7 Cloudflare AI Gateway docs","description":"Track and estimate token-based costs across AI providers using AI Gateway cost metrics.","url":"https://developers.cloudflare.com/ai-gateway/observability/costs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ai-gateway/observability/costs/
  schema: 1
---
<p>Cost metrics are only available for endpoints where the models return token data and the model name in their responses.</p>
<h2 id="track-costs-across-ai-providers">Track costs across AI providers</h2>
<p>AI Gateway makes it easier to monitor and estimate token based costs across all your AI providers. This can help you:</p>
<ul>
<li>Understand and compare usage costs between providers.</li>
<li>Monitor trends and estimate spend using consistent metrics.</li>
<li>Apply custom pricing logic to match negotiated rates.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/2805.md")
</aside>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="caution">Caution</h3>
@markup("md", "content/.markup/bodies/2804.md")
</aside>
<h2 id="custom-costs">Custom costs</h2>
<p>AI Gateway allows users to set custom costs when operating under special pricing agreements or negotiated rates. Custom costs can be applied at the request level, and when applied, they will override the default or public model costs.
For more information on configuration of custom costs, please visit the <a href="/ai-gateway/configuration/custom-costs/">Custom Costs</a> configuration page.</p>
