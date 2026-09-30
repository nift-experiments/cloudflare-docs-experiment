---
cp9:
  canonical: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-499/
  description: Troubleshoot HTTP 499 error responses.
  full_title: Error 499 · Cloudflare Support docs
  head_html: <title>Error 499 · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot HTTP 499 error responses."><link rel="canonical" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-499/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-499/index.md"><meta property="og:title" content="Error 499 · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot HTTP 499 error responses."><meta property="og:url" content="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-499/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-499/#page","headline":"Error 499 \u00b7 Cloudflare Support docs","description":"Troubleshoot HTTP 499 error responses.","url":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/4xx-client-error/error-499/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/troubleshooting/http-status-codes/4xx-client-error/error-499/
  schema: 1
---
<h2 id="499-client-close-request">499 Client Close Request</h2>
<p>The <code>HTTP 499</code> response code typically occurs when a client terminates the connection before the server is able to respond.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>Examples of <code>499</code> response code include situations where a client times out and closes the connection before the server completes processing, such as during large file uploads or long-running requests. They can also occur due to issues in the TCP three-way handshake, where the client terminates the connection prematurely because of its timeout settings.</p>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<p>The <code>499 Client Closed Request</code> status code is specific to nginx and indicates that the client closed the connection while the server was still processing the request, preventing the server from sending a status code in response. This status code appears in <a href="/logs/">Cloudflare Logs</a> and status code analytics for Enterprise customers.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14743.md")
</aside>
<p>To provide more context, a TCP connection must be established between Cloudflare and the website's origin server before any higher protocol (such as HTTP) begins communication. TCP uses a three-way handshake to establish connection:</p>
<ul>
<li><strong>SYN</strong>: Cloudflare sends a SYN packet to the origin server.</li>
<li><strong>SYN+ACK</strong>: The origin server responds with a SYN+ACK packet.</li>
<li><strong>ACK</strong>: Cloudflare sends an ACK packet back to the origin server.</li>
</ul>
<p>At this point, the connection is established, and both Cloudflare and the origin server can communicate. However, if the origin server does not send a SYN+ACK back to Cloudflare within 19 seconds, Cloudflare retries once more, with another 15-second timeout.</p>
<p>Depending on the client-side timeout settings, the following scenarios can occur:</p>
<ul>
<li><strong>Shorter client timeout (less than 38 seconds)</strong>: If the client has a shorter timeout, it will abandon the connection before Cloudflare completes processing, and a <code>499</code> response code will be logged.</li>
<li><strong>Successful connection (more than 38 seconds)</strong>: If the client has a longer timeout and the TCP connection is successfully established, the HTTP transaction proceeds normally, and Cloudflare returns a standard status code (<code>HTTP 200</code>).</li>
<li><strong>Handshake failure</strong>: If the client has a longer timeout but Cloudflare cannot establish the TCP handshake with the origin server, Cloudflare will return an <code>HTTP 522</code> status code.</li>
</ul>
<h3 id="diagnose-with-origin-analytics">Diagnose with Origin Analytics</h3>
<p>Use <a href="/speed/origin-analytics/">Origin Analytics</a> to check whether slow origin response times are causing clients to close connections prematurely. If P95 origin response times are high, identify the slow endpoints in the <strong>Top endpoints</strong> table and optimize them to reduce <code>499</code> errors.</p>
