---
cp9:
  canonical: https://developers.cloudflare.com/waf/tools/browser-integrity-check/
  description: Block requests with suspicious HTTP headers using Browser Integrity Check.
  full_title: Browser Integrity Check · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Browser Integrity Check · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Block requests with suspicious HTTP headers using Browser Integrity Check."><link rel="canonical" href="https://developers.cloudflare.com/waf/tools/browser-integrity-check/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/tools/browser-integrity-check/index.md"><meta property="og:title" content="Browser Integrity Check · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Block requests with suspicious HTTP headers using Browser Integrity Check."><meta property="og:url" content="https://developers.cloudflare.com/waf/tools/browser-integrity-check/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/tools/browser-integrity-check/#page","headline":"Browser Integrity Check \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Block requests with suspicious HTTP headers using Browser Integrity Check.","url":"https://developers.cloudflare.com/waf/tools/browser-integrity-check/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/tools/browser-integrity-check/
  schema: 1
---
<p>Cloudflare's Browser Integrity Check (BIC) looks for common HTTP headers abused most commonly by spammers and denies access to your page.</p>
<p>It also challenges visitors without a user agent or with a non-standard user agent such as commonly used by abusive bots, crawlers, or visitors.</p>
<p>Browser Integrity Check is enabled by default.</p>
<h2 id="disable-browser-integrity-check">Disable Browser Integrity Check</h2>
<h3 id="disable-globally">Disable globally</h3>
<p>To disable BIC globally for your zone:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15344.md")
</div>
<h3 id="disable-selectively">Disable selectively</h3>
<p>To disable BIC selectively, you can skip Browser Integrity Check using a <a href="/waf/custom-rules/skip/">custom rule with a skip action</a>.</p>
<p>Also, use a <a href="/rules/configuration-rules/">configuration rule</a> to selectively enable or disable this feature for certain sections of your website using a filter expression (such as a matching hostname or request URL path).</p>
