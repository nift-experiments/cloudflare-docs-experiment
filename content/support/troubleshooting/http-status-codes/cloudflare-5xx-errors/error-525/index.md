---
cp9:
  canonical: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-525/
  description: Troubleshoot HTTP 525 error responses.
  full_title: Error 525 · Cloudflare Support docs
  head_html: <title>Error 525 · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot HTTP 525 error responses."><link rel="canonical" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-525/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-525/index.md"><meta property="og:title" content="Error 525 · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot HTTP 525 error responses."><meta property="og:url" content="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-525/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-525/#page","headline":"Error 525 \u00b7 Cloudflare Support docs","description":"Troubleshoot HTTP 525 error responses.","url":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-525/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-525/
  schema: 1
---
<h2 id="error-525-ssl-handshake-failed">Error 525: SSL handshake failed</h2>
<p>This error indicates that the SSL handshake between Cloudflare and the origin web server failed.</p>
<h3 id="common-causes">Common causes</h3>
<p>Error <code>525</code> occurs when these two conditions are true:</p>
<ul>
<li>The <a href="https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/">SSL handshake</a> fails between Cloudflare and the origin web server.</li>
<li><a href="/ssl/origin-configuration/ssl-modes"><em>Full</em> or <em>Full (Strict)</em></a> <strong>SSL</strong> is set in the <strong>Overview</strong> tab of your Cloudflare <strong>SSL/TLS</strong> app.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14724.md")
</aside>
<h3 id="resolution">Resolution</h3>
<p>Contact your hosting provider to exclude the following common causes at your origin web server:</p>
<ul>
<li>No valid SSL certificate is installed.</li>
<li>Port <code>443</code> (or another custom secure port) is not open.</li>
<li>No <span class="nb-glossary-tooltip" title="Server Name Indication (SNI)">SNI</span> support.</li>
<li>The <a href="/ssl/origin-configuration/cipher-suites/">cipher suites</a> used by Cloudflare do not match the cipher suites supported by the origin web server.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14723.md")
</aside>
<ul>
<li>
<p>Verify that a certificate is installed on your origin server. For details on running tests, refer to <a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/#troubleshoot-requests-with-curl">Troubleshoot requests with curl</a>. If no certificate is installed, you can generate and install a free <a href="/ssl/origin-configuration/origin-ca">Cloudflare origin CA certificate</a> to encrypt traffic between Cloudflare and your origin web server.</p>
</li>
<li>
<p><a href="/ssl/edge-certificates/additional-options/cipher-suites/">Review the cipher suites</a> used by your server to ensure they are compatible with Cloudflare.</p>
</li>
<li>
<p>Check your server's error logs from the timestamps when <code>525</code> errors occur to identify any issues causing the connection to be reset during the SSL handshake.</p>
</li>
</ul>
<h3 id="diagnose-with-origin-analytics">Diagnose with Origin Analytics</h3>
<p>Use <a href="/speed/origin-analytics/">Origin Analytics</a> to check whether SSL handshake failures are affecting specific endpoints. The <strong>Origin status codes</strong> chart shows when Cloudflare received no HTTP response from your origin (<code>originResponseStatus</code> of <code>0</code>), which can indicate TLS negotiation failures. Cross-reference these timestamps with your origin SSL error logs to pinpoint the cause.</p>
