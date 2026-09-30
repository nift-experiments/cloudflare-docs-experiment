---
cp9:
  canonical: https://developers.cloudflare.com/smart-shield/configuration/cache-reserve/analytics/
  description: View Cache Reserve storage, read, and write operation metrics.
  full_title: Cache Reserve analytics · Cloudflare Smart Shield docs
  head_html: <title>Cache Reserve analytics · Cloudflare Smart Shield docs</title><meta name="generator" content="Nift"><meta name="description" content="View Cache Reserve storage, read, and write operation metrics."><link rel="canonical" href="https://developers.cloudflare.com/smart-shield/configuration/cache-reserve/analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/smart-shield/configuration/cache-reserve/analytics/index.md"><meta property="og:title" content="Cache Reserve analytics · Cloudflare Smart Shield docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="View Cache Reserve storage, read, and write operation metrics."><meta property="og:url" content="https://developers.cloudflare.com/smart-shield/configuration/cache-reserve/analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Smart Shield"><meta name="algolia_product_filter" content="Smart Shield"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Smart Shield"><meta name="pcx_tags" content="Analytics"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/smart-shield/configuration/cache-reserve/analytics/#page","headline":"Cache Reserve analytics \u00b7 Cloudflare Smart Shield docs","description":"View Cache Reserve storage, read, and write operation metrics.","url":"https://developers.cloudflare.com/smart-shield/configuration/cache-reserve/analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Analytics"]}</script>
  markdown: true
  noindex: false
  route: /smart-shield/configuration/cache-reserve/analytics/
  schema: 1
---
<p>Cache Reserve Analytics provides insights regarding your Cache Reserve usage. It allows you to check what content is stored in Cache Reserve, how often it is being accessed, how long it has been there and how much egress from your origin it is saving you.</p>
<p>You have access to the following metrics:</p>
<ul>
<li><strong>Egress savings (bandwidth)</strong> - is an estimation based on response bytes served from Cache Reserve that did not need to be served from your origin server. These are represented as cache hits.</li>
<li><strong>Requests served by Cache Reserve</strong> - is the number of requests served by Cache Reserve (total).</li>
<li><strong>Data storage summary</strong> - is based on a representative sample of requests. Refer to <a href="/analytics/graphql-api/sampling/">Sampling</a> for more details about how Cloudflare samples data.
<ul>
<li><strong>Current data stored</strong> - is the data stored (currently) over time.</li>
<li><strong>Aggregate storage usage</strong> - is the total of storage used for the selected timestamp.</li>
</ul>
</li>
<li><strong>Operations</strong> - Class A (writes) and Class B (reads) operations over time.</li>
</ul>
