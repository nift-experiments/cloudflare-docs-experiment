---
cp9:
  canonical: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1015/
  description: Troubleshoot Cloudflare 1015 error code.
  full_title: Error 1015 · Cloudflare Support docs
  head_html: <title>Error 1015 · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot Cloudflare 1015 error code."><link rel="canonical" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1015/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1015/index.md"><meta property="og:title" content="Error 1015 · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot Cloudflare 1015 error code."><meta property="og:url" content="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1015/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1015/#page","headline":"Error 1015 \u00b7 Cloudflare Support docs","description":"Troubleshoot Cloudflare 1015 error code.","url":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1015/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1015/
  schema: 1
---
<h2 id="error-1015-you-are-being-rate-limited">Error 1015: You are being rate limited</h2>
<p>The website you are trying to visit has received too many requests and has temporarily blocked you from accessing it.</p>
<h3 id="common-cause">Common cause</h3>
<p>The website owner has configured rate limiting rules that restrict how many requests a visitor can make to their site in a given time period. When you exceed this limit, Cloudflare returns a <code>1015</code> error.</p>
<h3 id="resolution">Resolution</h3>
<p><strong>If you are a site visitor:</strong></p>
<ul>
<li>Wait for a period of time, then try accessing the website again later. Do not repeatedly try to access the website within a short period of time, as this may extend the block.</li>
<li>If you are still blocked or need help, contact the website owner or the website's support team directly for help. Cloudflare does not control which visitors are rate limited, the website owner sets these rules.</li>
</ul>
<p><strong>If you are the site owner:</strong></p>
<ul>
<li>Review your current <a href="/waf/rate-limiting-rules/">rate limiting thresholds</a> and adjust your configuration.</li>
<li>If a rate limiting rule is blocking requests in a short time period (for example, one second), try increasing the time period to 10 seconds.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14736.md")
</aside>
