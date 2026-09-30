---
cp9:
  canonical: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-524/
  description: Troubleshoot HTTP 524 error responses.
  full_title: Error 524 · Cloudflare Support docs
  head_html: <title>Error 524 · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot HTTP 524 error responses."><link rel="canonical" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-524/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-524/index.md"><meta property="og:title" content="Error 524 · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot HTTP 524 error responses."><meta property="og:url" content="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-524/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-524/#page","headline":"Error 524 \u00b7 Cloudflare Support docs","description":"Troubleshoot HTTP 524 error responses.","url":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-524/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-524/
  schema: 1
---
<h2 id="error-524-a-timeout-occurred">Error 524: a timeout occurred</h2>
<p>Error <code>524</code> indicates that Cloudflare successfully connected to the origin web server, but the origin did not provide an HTTP response before the default 125 seconds <a href="/fundamentals/reference/connection-limits/">Proxy Read Timeout</a>.</p>
<h3 id="common-causes">Common causes</h3>
<p>This can happen if the origin server is taking too long because it has too much work to do, for example, a large data query, or because the server is struggling for resources and cannot return any data in time.
The error <code>524</code> occurs if the origin web server acknowledges (ACK) the resource request after the connection has been established, but does not send a timely response (within the <a href="/fundamentals/reference/connection-limits/">Proxy Read Timeout</a> delay, 125 seconds by default).</p>
<p>Error <code>524</code> can also indicate that Cloudflare successfully connected to the origin web server to write data, but the write did not complete before the 30 seconds <a href="/fundamentals/reference/connection-limits/">Proxy Write Timeout</a> (or 6.5 seconds in the case of <a href="/images/">Cloudflare Images</a>). This timeout cannot be adjusted.</p>
<h3 id="resolution-at-your-origin">Resolution at your origin</h3>
<p>Here are the options we suggest to work around this issue:</p>
<ul>
<li>
<p><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/#required-error-details-for-hosting-provider">Contact your hosting provider</a> to exclude the following common causes at your origin web server:</p>
<ul>
<li>A long-running process on the origin web server.</li>
<li>An overloaded origin web server.</li>
</ul>
</li>
<li>
<p>Implement status polling of large HTTP processes to avoid hitting this error.</p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14727.md")
</aside>
<h3 id="resolution-on-cloudflare">Resolution on Cloudflare</h3>
<p>Here are some other actions you can take on the Cloudflare side:</p>
<ul>
<li>If you regularly run HTTP requests that take over 125 seconds to complete (for example, large data exports), move those processes behind a <a href="/dns/proxy-status/#dns-only-records">subdomain not proxied (DNS-only, grey clouded)</a> in the Cloudflare <strong>DNS</strong> app.</li>
<li>Enterprise customers can increase the <code>524</code> timeout up to 6,000 seconds:
<ul>
<li>If your content can be cached, you can create a <a href="/cache/how-to/cache-rules/settings/#proxy-read-timeout-enterprise-only">Cache Rule</a> with the <code>Proxy Read Timeout</code> setting. The content needs to be cacheable for the rule to be triggered, but does not need to be cached.</li>
<li>You can increase the <code>proxy_read_timeout</code> setting for the whole zone using the <a href="/api/resources/zones/subresources/settings/methods/edit/">Edit zone setting API endpoint</a>.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14726.md")
</aside>
<h3 id="diagnose-with-origin-analytics">Diagnose with Origin Analytics</h3>
<p>Use <a href="/speed/origin-analytics/">Origin Analytics</a> to monitor origin response times and catch requests approaching your timeout threshold before they result in <code>524</code> errors. If P95 response times are near the <a href="/fundamentals/reference/connection-limits/">Proxy Read Timeout</a>, identify the slow paths in the <strong>Top endpoints</strong> table and optimize them — or increase the timeout for Enterprise zones.</p>
