---
cp9:
  canonical: https://developers.cloudflare.com/d1/observability/billing/
  description: Track D1 billing metrics including rows read, rows written, and storage usage across your account.
  full_title: Billing · Cloudflare D1 docs
  head_html: <title>Billing · Cloudflare D1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Track D1 billing metrics including rows read, rows written, and storage usage across your account."><link rel="canonical" href="https://developers.cloudflare.com/d1/observability/billing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/d1/observability/billing/index.md"><meta property="og:title" content="Billing · Cloudflare D1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Track D1 billing metrics including rows read, rows written, and storage usage across your account."><meta property="og:url" content="https://developers.cloudflare.com/d1/observability/billing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="D1"><meta name="algolia_product_filter" content="D1"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="D1"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/d1/observability/billing/#page","headline":"Billing \u00b7 Cloudflare D1 docs","description":"Track D1 billing metrics including rows read, rows written, and storage usage across your account.","url":"https://developers.cloudflare.com/d1/observability/billing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /d1/observability/billing/
  schema: 1
---
<p>D1 exposes analytics to track billing metrics (rows read, rows written, and total storage) across all databases in your account.</p>
<p>The metrics displayed in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> are sourced from Cloudflare's <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. You can access the metrics <a href="/d1/observability/metrics-analytics/#query-via-the-graphql-api">programmatically</a> via GraphQL or HTTP client.</p>
<h2 id="view-metrics-in-the-dashboard">View metrics in the dashboard</h2>
<p>Total account billable usage analytics for D1 are available in the Cloudflare dashboard. To view current and past metrics for an account:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Billing</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Go to **Billable Usage**.
<p>From here you can view charts of your account's D1 usage on a daily or month-to-date timeframe.</p>
<p>Note that billable usage history is stored for a maximum of 30 days.</p>
<h2 id="billing-notifications">Billing Notifications</h2>
<p>Usage-based billing notifications are available within the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> for users looking to monitor their total account usage.</p>
<p>Notifications on the following metrics are available:</p>
<ul>
<li>Rows Read</li>
<li>Rows Written</li>
</ul>
