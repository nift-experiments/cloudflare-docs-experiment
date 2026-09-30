---
cp9:
  canonical: https://developers.cloudflare.com/use-cases/saas/usage-analytics/
  description: Track usage across tenants for billing, optimization, and insights.
  full_title: Observe customer usage and billing · Cloudflare use cases
  head_html: <title>Observe customer usage and billing · Cloudflare use cases</title><meta name="generator" content="Nift"><meta name="description" content="Track usage across tenants for billing, optimization, and insights."><link rel="canonical" href="https://developers.cloudflare.com/use-cases/saas/usage-analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/use-cases/saas/usage-analytics/index.md"><meta property="og:title" content="Observe customer usage and billing · Cloudflare use cases"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Track usage across tenants for billing, optimization, and insights."><meta property="og:url" content="https://developers.cloudflare.com/use-cases/saas/usage-analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Use cases"><meta name="algolia_product_filter" content="Use cases"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Use cases,Workers Analytics Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/use-cases/saas/usage-analytics/#page","headline":"Observe customer usage and billing \u00b7 Cloudflare use cases","description":"Track usage across tenants for billing, optimization, and insights.","url":"https://developers.cloudflare.com/use-cases/saas/usage-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /use-cases/saas/usage-analytics/
  schema: 1
---
<p>Usage-based billing and per-tenant performance monitoring require detailed analytics broken down by customer. Cloudflare Workers Analytics Engine tracks request counts, latency, and bytes per tenant ID, while Logpush exports detailed logs for compliance and audit trails.</p>
<h2 id="solutions">Solutions</h2>
<h3 id="workers-analytics-engine">Workers Analytics Engine</h3>
<p>Store and query time-series analytics data from Workers. <a href="/analytics/analytics-engine/">Learn more about Workers Analytics Engine</a>.</p>
<ul>
<li><strong>Per-tenant metrics</strong> - Track request counts, latency, and bytes transferred broken down by tenant ID</li>
<li><strong>Billing data</strong> - Query usage data per customer to power usage-based billing calculations</li>
<li><strong>Performance insights</strong> - Identify which tenants are generating the most load or experiencing the most errors</li>
</ul>
<h3 id="logpush">Logpush</h3>
<p>Stream logs from Cloudflare products to external destinations. <a href="/logs/">Learn more about Logpush</a>.</p>
<ul>
<li><strong>Compliance logging</strong> - Export detailed logs to your Security Information and Event Management (SIEM) system or data warehouse for audit trails and enterprise compliance</li>
</ul>
<h2 id="get-started">Get started</h2>
<ol>
<li><a href="/analytics/analytics-engine/get-started/">Workers Analytics Engine get started</a></li>
<li><a href="/logs/logpush/">Configure Logpush</a></li>
</ol>
