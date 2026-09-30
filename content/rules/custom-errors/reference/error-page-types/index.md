---
cp9:
  canonical: https://developers.cloudflare.com/rules/custom-errors/reference/error-page-types/
  description: Types of error pages you can customize with custom error rules.
  full_title: Error page types · Cloudflare Rules docs
  head_html: <title>Error page types · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Types of error pages you can customize with custom error rules."><link rel="canonical" href="https://developers.cloudflare.com/rules/custom-errors/reference/error-page-types/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/custom-errors/reference/error-page-types/index.md"><meta property="og:title" content="Error page types · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Types of error pages you can customize with custom error rules."><meta property="og:url" content="https://developers.cloudflare.com/rules/custom-errors/reference/error-page-types/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/custom-errors/reference/error-page-types/#page","headline":"Error page types \u00b7 Cloudflare Rules docs","description":"Types of error pages you can customize with custom error rules.","url":"https://developers.cloudflare.com/rules/custom-errors/reference/error-page-types/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/custom-errors/reference/error-page-types/
  schema: 1
---
<table>
<thead>
<tr>
<th>Page type</th>
<th>Description</th>
<th>API identifier</th>
</tr>
</thead>
<tbody>
<tr>
<td>WAF block</td>
<td>The page displayed when visitors are blocked by a <a href="/waf/">Web Application Firewall</a> rule. This page returns a <code>403</code> status code.</td>
<td><code>waf_block</code></td>
</tr>
<tr>
<td>IP/Country block</td>
<td>The page displayed when a request originates from a <a href="/waf/tools/ip-access-rules/">blocked IP address or country</a>. This page returns a <code>403</code> status code.</td>
<td><code>ip_block</code></td>
</tr>
<tr>
<td>IP/Country challenge</td>
<td>Presents a challenge to visitors from specified IP addresses or countries. This page returns a <code>403</code> status code. For more information, refer to <a href="/waf/tools/ip-access-rules/">IP Access rules</a>.</td>
<td><code>country_challenge</code></td>
</tr>
<tr>
<td>500 class errors</td>
<td>500 class error pages are displayed when a web server is unable to process a request. For more information, refer to <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/">Cloudflare 5xx errors</a>.</td>
<td><code>500_errors</code></td>
</tr>
<tr>
<td>1000 class errors</td>
<td>1000 class error pages are displayed when a domain’s configuration, security settings, or origin setup prevents Cloudflare from completing a request. For more information, refer to <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/">Cloudflare 1xxx errors</a>.</td>
<td><code>1000_errors</code></td>
</tr>
<tr>
<td>Managed challenge / I'm Under Attack Mode</td>
<td>Presents different types of challenges to a visitor depending on the nature of their request and your security settings. This page returns a <code>403</code> status code. For more information, refer to <a href="/fundamentals/reference/under-attack-mode/">Under Attack mode</a>.</td>
<td><code>managed_challenge</code></td>
</tr>
<tr>
<td>Rate limiting block</td>
<td>Displayed to visitors when they have been blocked by a <a href="/waf/rate-limiting-rules/">rate limiting rule</a>. This page returns a <code>429</code> status code.</td>
<td><code>ratelimit_block</code></td>
</tr>
</tbody>
</table>
