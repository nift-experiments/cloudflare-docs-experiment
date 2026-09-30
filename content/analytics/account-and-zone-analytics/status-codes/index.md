---
cp9:
  canonical: https://developers.cloudflare.com/analytics/account-and-zone-analytics/status-codes/
  description: Analyze HTTP status code distribution per data center.
  full_title: Status codes · Cloudflare Analytics docs
  head_html: <title>Status codes · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Analyze HTTP status code distribution per data center."><link rel="canonical" href="https://developers.cloudflare.com/analytics/account-and-zone-analytics/status-codes/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/account-and-zone-analytics/status-codes/index.md"><meta property="og:title" content="Status codes · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Analyze HTTP status code distribution per data center."><meta property="og:url" content="https://developers.cloudflare.com/analytics/account-and-zone-analytics/status-codes/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Analytics"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/account-and-zone-analytics/status-codes/#page","headline":"Status codes \u00b7 Cloudflare Analytics docs","description":"Analyze HTTP status code distribution per data center.","url":"https://developers.cloudflare.com/analytics/account-and-zone-analytics/status-codes/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/account-and-zone-analytics/status-codes/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3146.md")
</aside>
<p>Status Codes metrics in the Cloudflare dashboard <strong>Analytics</strong> app provide customers with a deeper insight into the distribution of errors that are occurring on their website per data center. A data center facility is where Cloudflare runs its servers that make up our edge network (<a href="https://www.cloudflare.com/network/">current locations</a>).</p>
<p>HTTP status codes that appear in a response passing through our edge are displayed in analytics.</p>
<p>The <code>Origin Status Code</code> can help you investigate issues on your origin. If your origin returns a <code>5xx</code> error, Cloudflare's edge will forward this error to the end user. Comparing the <code>Edge Status Code</code> and <code>Origin Status Code</code> can help determine whether the issue is occurring on your origin or on the Cloudflare edge.</p>
<p>Errors that originate from our edge servers (blank <code>502</code>, <code>503</code>, or <code>504</code> error page with just <code>Cloudflare</code>) are not reported as part of the error analytics.</p>
<p>You can filter out specific error(s) by selecting one or more in the legend. You can also exclude a particular error and it will no longer display as part of the graph.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3145.md")
</aside>
<p><img src="/assets/upstream/images/analytics/status-codes.png" alt="Error analytics by Cloudflare data center" /></p>
<hr />
<h2 id="common-edge-status-codes">Common edge status codes</h2>
<ul>
<li><code>400</code> - Bad Request intercepted at the Cloudflare Edge (for example, missing or bad HTTP header)</li>
<li><code>403</code> - Security functionality (for example, Web Application Firewall, Browser Integrity Check, <a href="/cloudflare-challenges/">Cloudflare challenges</a>, and most 1xxx error codes)</li>
<li><code>409</code> - DNS errors typically in the form of 1000 or 1001 error code</li>
<li><code>413</code> - File size upload exceeded the maximum size allowed (configured in the dashboard under <strong>Network</strong> &gt; <strong>Maximum Upload Size</strong>.)</li>
<li><code>444</code> - Used by Nginx to indicate that the server has returned no information to the client, and closed the connection. This error code is internal to Nginx and is <strong>not</strong> returned to the client.</li>
<li><code>499</code> - Used by Nginx to indicate when a connection has been closed by the client while the server is still processing its request, making the server unable to send a status code back.</li>
</ul>
<p>For more information, refer to <a href="/support/troubleshooting/http-status-codes/4xx-client-error/">4xx Client Error</a>.</p>
<hr />
<h2 id="common-origin-status-codes">Common origin status codes</h2>
<ul>
<li><code>400</code> - Origin rejected the request due to bad, or unsupported syntax sent by the application.</li>
<li><code>404</code> - Only if the origin triggered a 404 response for a request.</li>
<li><code>4xx</code></li>
<li><code>50x</code></li>
</ul>
<p>For more information, refer to <a href="/support/troubleshooting/http-status-codes/4xx-client-error/">4xx Client Error</a> and <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/">Troubleshooting Cloudflare 5XX errors</a>.</p>
<hr />
<h2 id="52x-errors">52x errors</h2>
<ul>
<li><code>520</code> - This is essentially a &quot;catch-all&quot; response for when the origin server returns something unexpected, or something that is not tolerated/cannot be interpreted by our edge (that is, protocol violation or empty response).</li>
<li><code>522</code> - Our edge could not establish a TCP connection to the origin server.</li>
<li><code>523</code> - Origin server is unreachable (for example, the origin IP changed but DNS was not updated, or due to network issues between our edge and the origin).</li>
<li><code>524</code> - Our edge established a TCP connection, but the origin did not reply with a HTTP response before the connection timed out.</li>
<li><code>525</code> - This error indicates that the SSL handshake between Cloudflare and the origin web server failed, either due to a network issue or a certificate issue at the origin.</li>
<li><code>526</code> - The certificate configured at the origin is not valid.</li>
</ul>
<p>For more information, refer to <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/">Troubleshooting Cloudflare 5XX errors</a>.</p>
