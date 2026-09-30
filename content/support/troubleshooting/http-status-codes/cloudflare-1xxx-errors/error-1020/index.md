---
cp9:
  canonical: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1020/
  description: Troubleshoot Cloudflare 1020 error code.
  full_title: Error 1020 · Cloudflare Support docs
  head_html: <title>Error 1020 · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot Cloudflare 1020 error code."><link rel="canonical" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1020/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1020/index.md"><meta property="og:title" content="Error 1020 · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot Cloudflare 1020 error code."><meta property="og:url" content="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1020/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1020/#page","headline":"Error 1020 \u00b7 Cloudflare Support docs","description":"Troubleshoot Cloudflare 1020 error code.","url":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1020/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1020/
  schema: 1
---
<h2 id="error-1020-access-denied">Error 1020: Access denied</h2>
<p>This error indicates that access to the website is denied by a Cloudflare firewall rule.</p>
<h3 id="common-cause">Common cause</h3>
<p>A client or browser is blocked by a Cloudflare customer's Firewall Rules (deprecated).</p>
<h3 id="resolution">Resolution</h3>
<p>If you are not the website owner, provide the website owner with a screenshot of the <code>1020</code> error message you received.</p>
<p>If you are the website owner:</p>
<ol>
<li>Retrieve a screenshot of the 1020 error from your customer.</li>
<li>Search the <a href="/waf/analytics/security-events/">Security Events log</a> (available at <strong>Security</strong> &gt; <strong>Analytics</strong>, in the <strong>Events</strong> tab) for the <a href="/fundamentals/reference/cloudflare-ray-id/">Ray ID</a> or client IP address from the visitor's 1020 error message.</li>
</ol>
<div class="nb-dash-button"></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14734.md")
</aside>
<ol start="3">
<li>Assess the cause of the block and either update the Firewall Rule or allow the visitor's IP address in <a href="/waf/tools/ip-access-rules/">IP Access Rules</a>.</li>
</ol>
