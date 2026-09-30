---
cp9:
  canonical: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1000/
  description: Troubleshoot Cloudflare 1000 error code.
  full_title: Error 1000 · Cloudflare Support docs
  head_html: <title>Error 1000 · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot Cloudflare 1000 error code."><link rel="canonical" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1000/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1000/index.md"><meta property="og:title" content="Error 1000 · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot Cloudflare 1000 error code."><meta property="og:url" content="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1000/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1000/#page","headline":"Error 1000 \u00b7 Cloudflare Support docs","description":"Troubleshoot Cloudflare 1000 error code.","url":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1000/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1000/
  schema: 1
---
<h2 id="error-1000-dns-points-to-prohibited-ip">Error 1000: DNS points to prohibited IP</h2>
<p>This error indicates that a Cloudflare DNS record points to a prohibited IP, blocking access to the requested domain.</p>
<h3 id="common-causes">Common causes</h3>
<p>Cloudflare halted the request for one of the following reasons:</p>
<ul>
<li>An A record within your Cloudflare DNS app points to a <a href="https://www.cloudflare.com/ips/">Cloudflare IP address</a>, or a Load Balancer Origin points to a proxied record.</li>
<li>Your Cloudflare DNS A or CNAME record references another reverse proxy (such as an nginx web server that uses the proxy_pass function) that then proxies the request to Cloudflare a second time.</li>
<li>The request <code>X-Forwarded-For</code> header is longer than 100 characters.</li>
<li>The request includes two <code>X-Forwarded-For</code> headers.</li>
<li>The request includes a <code>CF-Connecting-IP</code> header.</li>
<li>A Server Name Indication (SNI) issue or mismatch at the origin.</li>
<li>Your DNS record points to a SaaS provider that uses <a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a> with <a href="/byoip/">BYOIP</a> (Bring Your Own IP). Because the provider's IP addresses are advertised through Cloudflare's network, requests resolve to Cloudflare infrastructure. If the provider has not configured a <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/">custom hostname</a> for your domain, this error is returned.</li>
</ul>
<h3 id="resolution">Resolution</h3>
<ul>
<li>If an A record within your Cloudflare DNS app points to a <a href="https://www.cloudflare.com/ips/">Cloudflare IP address</a>, update the IP address to your origin web server IP address. Reach out to your hosting provider if you need help obtaining the origin IP address.</li>
<li>There is a reverse-proxy at your origin that sends the request back through the Cloudflare proxy. Instead of using a reverse-proxy, contact your hosting provider or site administrator to configure an HTTP redirect at your origin.</li>
<li>If your domain points to a SaaS provider that uses Cloudflare, contact the SaaS provider to verify that a custom hostname is properly configured for your domain. The error originates from the provider's Cloudflare account, not yours.</li>
</ul>
