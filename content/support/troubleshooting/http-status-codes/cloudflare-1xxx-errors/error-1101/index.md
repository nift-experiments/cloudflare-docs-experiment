---
cp9:
  canonical: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1101/
  description: Troubleshoot Cloudflare 1101 error code.
  full_title: Error 1101 · Cloudflare Support docs
  head_html: <title>Error 1101 · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot Cloudflare 1101 error code."><link rel="canonical" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1101/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1101/index.md"><meta property="og:title" content="Error 1101 · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot Cloudflare 1101 error code."><meta property="og:url" content="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1101/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1101/#page","headline":"Error 1101 \u00b7 Cloudflare Support docs","description":"Troubleshoot Cloudflare 1101 error code.","url":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1101/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1101/
  schema: 1
---
<h2 id="error-1101-rendering-error">Error 1101: Rendering error</h2>
<p>This error indicates a rendering issue.</p>
<h3 id="common-cause">Common cause</h3>
<p>This error typically occurs when a Cloudflare Worker encounters a runtime JavaScript exception.</p>
<h3 id="debugging">Debugging</h3>
<p>To identify the specific JavaScript exception:</p>
<ol>
<li>Check your Workers logs in the Cloudflare dashboard under <strong>Workers &amp; Pages</strong> &gt; <strong>Your Worker</strong> &gt; <strong>Logs</strong>.</li>
<li>Review the Workers code for potential runtime errors such as:
<ul>
<li>Undefined variables or functions</li>
<li>Type errors</li>
<li>Promise rejections</li>
<li>Network request failures</li>
</ul>
</li>
<li>Test the <a href="/workers/local-development/#local-development">Worker locally</a> with sample requests to reproduce the error.</li>
<li>Refer to <a href="/workers/observability/errors/">Workers error handling</a> for more details on debugging Workers.</li>
</ol>
<h3 id="resolution">Resolution</h3>
<p>Fix the JavaScript exception in your Workers code. If you need assistance, <a href="/support/contacting-cloudflare-support/">provide appropriate issue details</a> to Cloudflare Support, including:</p>
<ul>
<li>The Ray ID from the error page</li>
<li>The Worker name</li>
<li>Recent changes to the Worker code</li>
<li>Steps to reproduce the error</li>
</ul>
<h3 id="related-errors">Related errors</h3>
<ul>
<li><a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1102/">Error 1102</a> - Workers CPU time limit exceeded</li>
<li><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-500/">Error 500</a> - Internal server error (can be caused by Workers exceptions)</li>
</ul>
