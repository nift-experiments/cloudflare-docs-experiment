---
cp9:
  canonical: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1002/
  description: Troubleshoot Cloudflare 1002 error code.
  full_title: Error 1002 · Cloudflare Support docs
  head_html: <title>Error 1002 · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot Cloudflare 1002 error code."><link rel="canonical" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1002/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1002/index.md"><meta property="og:title" content="Error 1002 · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot Cloudflare 1002 error code."><meta property="og:url" content="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1002/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1002/#page","headline":"Error 1002 \u00b7 Cloudflare Support docs","description":"Troubleshoot Cloudflare 1002 error code.","url":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1002/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1002/
  schema: 1
---
<h2 id="error-1002-dns-points-to-prohibited-ip">Error 1002: DNS points to Prohibited IP</h2>
<p>This error indicates that a Cloudflare DNS record points to a prohibited IP, preventing proper domain resolution.</p>
<h3 id="common-causes">Common causes</h3>
<ul>
<li>A DNS record in your Cloudflare DNS app points to one of <a href="https://www.cloudflare.com/ips/">Cloudflare's IP addresses</a>.</li>
<li>An incorrect target is specified for a CNAME record in your Cloudflare DNS app.</li>
<li>Your domain is not on Cloudflare but has a CNAME that refers to a Cloudflare domain.</li>
</ul>
<h3 id="resolution">Resolution</h3>
<p>Update your Cloudflare A or CNAME record to point to your origin IP address instead of a Cloudflare IP address:</p>
<ol>
<li>
<p>Contact your hosting provider to confirm your origin IP address or CNAME record target.</p>
</li>
<li>
<p>In the Cloudflare dashboard, go to the <strong>Records</strong> page.</p>
</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="3">
<li>Select the domain that generates error 1002.</li>
<li>Select the <strong>DNS</strong> app.</li>
<li>Select <strong>Value</strong> for the A record to update.</li>
<li>Update the A record.</li>
</ol>
<p>To ensure your origin web server does not proxy its own requests through Cloudflare, configure your origin webserver to resolve your Cloudflare domain to:</p>
<ul>
<li>The internal NAT'd IP address, or</li>
<li>The public IP address of the origin web server.</li>
</ul>
<h2 id="error-1002-restricted">Error 1002: Restricted</h2>
<p>This error indicates that the domain resolves to a restricted or disallowed IP address.</p>
<h3 id="common-cause">Common cause</h3>
<p>The Cloudflare domain resolves to a local or disallowed IP address or an IP address not associated with the domain.</p>
<h3 id="resolution-1">Resolution</h3>
<p>If you own the website:</p>
<ol>
<li>Confirm your origin web server IP addresses with your hosting provider,</li>
<li>Log in to your Cloudflare account, and</li>
<li>Update the A records in the Cloudflare DNS app to the IP address confirmed by your hosting provider.</li>
</ol>
