---
cp9:
  canonical: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-521/
  description: Troubleshoot HTTP 521 error responses.
  full_title: Error 521 · Cloudflare Support docs
  head_html: <title>Error 521 · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot HTTP 521 error responses."><link rel="canonical" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-521/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-521/index.md"><meta property="og:title" content="Error 521 · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot HTTP 521 error responses."><meta property="og:url" content="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-521/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-521/#page","headline":"Error 521 \u00b7 Cloudflare Support docs","description":"Troubleshoot HTTP 521 error responses.","url":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-521/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-521/
  schema: 1
---
<h2 id="error-521-web-server-is-down">Error 521: web server is down</h2>
<p>Error <code>521</code> occurs when the origin web server refuses connections from Cloudflare. Security solutions at your origin may block legitimate connections from certain <a href="https://www.cloudflare.com/ips">Cloudflare IP addresses</a>.</p>
<h3 id="common-causes">Common causes</h3>
<p>The two most common causes of <code>521</code> errors are:</p>
<ul>
<li>Offlined origin web server application.</li>
<li>Blocked Cloudflare requests.</li>
</ul>
<h3 id="resolution">Resolution</h3>
<p>Contact your hosting provider or site administrator and share the necessary <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/#required-error-details-for-hosting-provider">error details</a> to assist in troubleshooting these common causes:</p>
<ul>
<li>Ensure your origin web server is responsive.</li>
<li>Review origin web server error logs to identify web server application crashes or outages.</li>
<li>Confirm <a href="https://www.cloudflare.com/ips">Cloudflare IP addresses</a> are not blocked or rate limited.</li>
<li>Allow all <a href="https://www.cloudflare.com/ips">Cloudflare IP ranges</a> in your origin web server's firewall or other security software.</li>
<li>Confirm that — if you have your <strong>SSL/TLS mode</strong> set to <strong>Full</strong> or <strong>Full (Strict</strong>) — your origin supports HTTPS and/or you have installed a <a href="/ssl/origin-configuration/origin-ca">Cloudflare Origin Certificate</a> or a certificate matching the <a href="/ssl/origin-configuration/ssl-modes/#custom-ssltls">requirements for these modes</a>.</li>
<li>Ensure that your origin web server application is actively bound and listening on the port required by your SSL/TLS mode: Port 80 for <strong>Flexible</strong>, or Port 443 for <strong>Full</strong> and <strong>Full (Strict)</strong>.</li>
<li>Find additional troubleshooting information on the <a href="https://community.cloudflare.com/t/community-tip-fixing-error-521-web-server-is-down/42461">Cloudflare Community</a>.</li>
</ul>
