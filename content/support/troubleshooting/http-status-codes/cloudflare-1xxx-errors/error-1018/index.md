---
cp9:
  canonical: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1018/
  description: Troubleshoot Cloudflare 1018 error code.
  full_title: Error 1018 · Cloudflare Support docs
  head_html: <title>Error 1018 · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot Cloudflare 1018 error code."><link rel="canonical" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1018/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1018/index.md"><meta property="og:title" content="Error 1018 · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot Cloudflare 1018 error code."><meta property="og:url" content="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1018/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1018/#page","headline":"Error 1018 \u00b7 Cloudflare Support docs","description":"Troubleshoot Cloudflare 1018 error code.","url":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1018/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1018/
  schema: 1
---
<h2 id="error-1018-could-not-find-host">Error 1018: Could not find host</h2>
<p>This error indicates that the host could not be found.</p>
<h3 id="common-causes">Common causes</h3>
<ul>
<li>The Cloudflare domain was recently activated and there is a delay propagating the domain's settings to the Cloudflare edge network.</li>
<li>The Cloudflare domain was created via a Cloudflare partner (for example, a hosting provider) and the provider's DNS failed.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14735.md")
</aside>
<h3 id="resolution">Resolution</h3>
<p>Contact <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a> with the following details:</p>
<ul>
<li>Your domain name.</li>
<li>A screenshot of the <code>1018</code> error including the <a href="/fundamentals/reference/cloudflare-ray-id/"><strong>Ray ID</strong></a> mentioned in the error message.</li>
<li>A <a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/">HAR file</a> captured while duplicating the error.</li>
</ul>
