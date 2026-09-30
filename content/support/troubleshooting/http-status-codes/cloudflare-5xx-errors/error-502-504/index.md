---
cp9:
  canonical: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-502-504/
  description: Troubleshoot HTTP 502 error responses.
  full_title: Error 502 or 504 · Cloudflare Support docs
  head_html: <title>Error 502 or 504 · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot HTTP 502 error responses."><link rel="canonical" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-502-504/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-502-504/index.md"><meta property="og:title" content="Error 502 or 504 · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot HTTP 502 error responses."><meta property="og:url" content="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-502-504/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-502-504/#page","headline":"Error 502 or 504 \u00b7 Cloudflare Support docs","description":"Troubleshoot HTTP 502 error responses.","url":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-502-504/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-502-504/
  schema: 1
---
<h2 id="error-502-bad-gateway-or-error-504-gateway-timeout">Error 502 bad gateway or error 504 gateway timeout</h2>
<p>An HTTP <code>502</code> or <code>504</code> error indicates that Cloudflare is unable to establish contact with your origin web server.</p>
<h3 id="common-causes">Common causes</h3>
<p>There are two possible causes:</p>
<ul>
<li><a href="#502504-from-your-origin-web-server"><code>502/504</code> errors from your origin web server</a> (most common).</li>
<li><a href="#502504-from-cloudflare"><code>502/504</code> errors from Cloudflare</a>.</li>
</ul>
<p>You may also see <code>504</code> status codes in logs or analytics caused by <a href="/cache/advanced-configuration/early-hints/#emit-early-hints">cache MISS responses from Early Hints</a>, or by Cloudflare Workers Cache API <a href="https://developers.cloudflare.com/workers/runtime-apis/cache/#errors-1"><code>cache.match</code> operations resulting in cache MISS</a>.</p>
<h3 id="resolution">Resolution</h3>
<p>To resolve <code>502/504</code> errors, it is essential to identify whether the issue originates from your origin web server or Cloudflare. In the following sections, you can find more details for troubleshooting and resolving errors from both sources.</p>
<h4 id="502-504-from-your-origin-web-server">502/504 from your origin web server</h4>
<p>Cloudflare returns a Cloudflare-branded HTTP <code>502</code> or <code>504</code> error when your origin web server responds with a standard HTTP <code>502 bad gateway</code> or <code>504 gateway timeout</code> error:</p>
<p><img src="/assets/upstream/images/support/image1.png" alt="Example of a Cloudflare-branded error 502." /></p>
<p>Contact your hosting provider to troubleshoot these common causes at your origin web server:</p>
<ul>
<li>Ensure the origin server responds to requests for the hostname and domain within the visitor's URL that generated the <code>502</code> or <code>504</code> error.</li>
<li>Investigate excessive server loads, crashes, or network failures.</li>
<li>Identify applications or services that timed out or were blocked.</li>
</ul>
<h4 id="502-504-from-cloudflare">502/504 from Cloudflare</h4>
<p>A <code>502</code> or a <code>504</code> error originating from Cloudflare appears as follows, a blank page without the Cloudflare branding:</p>
<p><img src="/assets/upstream/images/support/image5.png" alt="Example of an unbranded error 502." /></p>
<p>If the error does not mention <code>cloudflare</code>, contact your hosting provider for assistance. Refer to <a href="#502504-from-your-origin-web-server">502/504 errors from your origin</a> for more information.</p>
<p>This error can occur due to a compression issue at the origin, such as when the origin server serves gzip-encoded compressed content but fails to update the <code>content-length</code> header, or if the origin is serving broken gzip compressed content. To diagnose this, you can try disabling compression at your origin to confirm if it resolves the error.</p>
<p>Additionally, in some cases, a particular data center may experience a sudden increase in traffic. To ensure minimal impact for customers, our automated processes will redirect traffic to another data center. These adjustments typically happen seamlessly and take just a few seconds. However, during this process, some clients may experience temporary latency or HTTP <code>502</code> errors. You can find more information about our automated traffic management tools in this <a href="https://blog.cloudflare.com/meet-traffic-manager">blogpost</a>.</p>
<p>If you need further assistance from our Support team, provide the following details to <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a> to avoid delays in processing your inquiry:</p>
<ul>
<li>The timestamp along with the timezone in which the issue occurred.</li>
<li>The URL that resulted in the HTTP <code>502</code> or <code>504</code> response (for example, <code>https://www.example.com/images/icons/image1.png</code>).</li>
<li>The output from browsing to <code>&lt;YOUR_DOMAIN&gt;/cdn-cgi/trace</code>.</li>
</ul>
<h3 id="known-cloudflare-issues-leading-to-http-error-502-or-504">Known Cloudflare issues leading to HTTP Error 502 or 504</h3>
<ul>
<li>
<p>Using <a href="/cloudflare-one/traffic-policies/">Gateway</a> can lead to an HTTP Error <code>502</code> if the origin only partially supports HTTP/2. Refer to <a href="/cloudflare-one/traffic-policies/troubleshooting/#error-502-bad-gateway">Troubleshooting</a> for more details and resolution.</p>
</li>
<li>
<p>You might see a <code>502 Bad Gateway</code> error when connecting to an HTTP or HTTPS application through <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>, with <code>Unable to reach the origin service. The service may be down or it may not be responding to traffic from cloudflared</code>. It means the tunnel itself is connected to the Cloudflare network, but <code>cloudflared</code> cannot reach the origin service defined in your ingress rule. Refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/#i-see-a-502-bad-gateway-error-when-connecting-to-an-http-or-https-application-through-tunnel">tunnel common errors page</a> for more details and resolution.</p>
</li>
<li>
<p>You may see an influx of HTTP Error <code>504</code> with the <code>RequestSource</code> of <code>earlyHintsCache</code> in Cloudflare Logs when Early Hints is enabled, which is expected and benign. Refer to <a href="/cache/advanced-configuration/early-hints/#emit-early-hints">the Early Hints article</a> for more details and resolution.</p>
</li>
<li>
<p>If you use <a href="/smart-shield/configuration/dedicated-egress-ips/">Dedicated CDN Egress IPs</a> to connect to your origin, a <code>502</code> error can also occur when Cloudflare temporarily runs out of available source ports for your Dedicated CDN Egress IPs while opening new connections to your origin. Each Dedicated CDN Egress IP can <a href="/smart-shield/configuration/dedicated-egress-ips/how-it-works/egress-ips/#connections-to-your-origin">support up to 40,000 concurrent connections per origin IP port</a>, so a high volume of concurrent connections to a single origin can exhaust the available ports and cause intermittent <code>502</code> errors, even when your origin is healthy. Dedicated CDN Egress IPs benefit from <a href="/smart-shield/concepts/connection-reuse/">connection reuse and coalescing</a>, which lowers the number of connections opened to your origin and reduces the likelihood of reaching this limit. If you suspect port exhaustion, contact your account team to review your Dedicated CDN Egress IPs capacity and placement.</p>
</li>
</ul>
