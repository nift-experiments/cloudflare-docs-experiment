---
cp9:
  canonical: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-501/
  description: Troubleshoot HTTP 501 error responses.
  full_title: Error 501 · Cloudflare Support docs
  head_html: <title>Error 501 · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot HTTP 501 error responses."><link rel="canonical" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-501/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-501/index.md"><meta property="og:title" content="Error 501 · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot HTTP 501 error responses."><meta property="og:url" content="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-501/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-501/#page","headline":"Error 501 \u00b7 Cloudflare Support docs","description":"Troubleshoot HTTP 501 error responses.","url":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-501/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-501/
  schema: 1
---
<h2 id="error-501-not-implemented">Error 501: not implemented</h2>
<p>Cloudflare Workers returns a <code>501</code> error when a request uses an HTTP method that is not supported by the Workers Runtime.</p>
<h3 id="common-causes">Common causes</h3>
<ul>
<li>A client sent a request to a Workers script using a custom or non-standard HTTP method (methods outside of <code>GET</code>, <code>POST</code>, <code>PUT</code>, etc.).</li>
<li>A typo in the HTTP method (for example, <code>POT</code> instead of <code>POST</code>).</li>
</ul>
<h3 id="resolution">Resolution</h3>
<ul>
<li>Update the client to use a valid, standard <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods">HTTP request method</a>.</li>
</ul>
