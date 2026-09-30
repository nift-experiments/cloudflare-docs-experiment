---
cp9:
  canonical: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-503/
  description: Troubleshoot HTTP 503 error responses.
  full_title: Error 503 · Cloudflare Support docs
  head_html: <title>Error 503 · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot HTTP 503 error responses."><link rel="canonical" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-503/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-503/index.md"><meta property="og:title" content="Error 503 · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot HTTP 503 error responses."><meta property="og:url" content="https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-503/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-503/#page","headline":"Error 503 \u00b7 Cloudflare Support docs","description":"Troubleshoot HTTP 503 error responses.","url":"https://developers.cloudflare.com/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-503/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-503/
  schema: 1
---
<h2 id="error-503-service-temporarily-unavailable">Error 503: service temporarily unavailable</h2>
<p>HTTP error 503 occurs when your origin web server is overloaded.</p>
<h3 id="common-causes">Common causes</h3>
<p>There are different causes identifiable by the error message or the location of the error:</p>
<ul>
<li>Error does not contain <code>cloudflare</code> or <code>cloudflare-nginx</code> in the HTML response body. In this case, the issue is likely from your origin server.</li>
<li>Error contains <code>cloudflare</code> or <code>cloudflare-nginx</code> in the HTML response body. In this case, the issue may stem from Cloudflare.</li>
<li>Error is only visible in logs or analytics.</li>
</ul>
<h3 id="resolution">Resolution</h3>
<p>To resolve a <code>503</code> error, first determine whether the issue originates from your origin web server or Cloudflare. The following sections provide guidance on troubleshooting both scenarios.</p>
<h4 id="503-error-without-cloudflare-or-cloudflare-nginx">503 Error without <code>cloudflare</code> or <code>cloudflare-nginx</code></h4>
<p>If the error does not contain <code>cloudflare</code> or <code>cloudflare-nginx</code> in the HTML response body, contact your hosting provider to verify if they rate limit requests to your origin web server.</p>
<h4 id="503-error-with-cloudflare-or-cloudflare-nginx">503 Error with <code>cloudflare</code> or <code>cloudflare-nginx</code></h4>
<p>If the error contains <code>cloudflare</code> or <code>cloudflare-nginx</code> in the HTML response body, a connectivity issue occurred in a Cloudflare data center. Provide <a href="/support/contacting-cloudflare-support/">Cloudflare support</a> with the following information:</p>
<ul>
<li>Your domain name</li>
<li>The time and timezone of the <code>503</code> error occurrence</li>
<li>The output of <code>www.example.com/cdn-cgi/trace</code> from the browser where the <code>503</code> error was observed (replace <code>www.example.com</code> with your actual domain and hostname)</li>
</ul>
<h4 id="503-error-only-visible-in-logs-and-analytics">503 Error only visible in logs and analytics</h4>
<p>These errors result from <a href="/speed/optimization/content/speed-brain/#how-speed-brain-works">unsuccessful prefetches from Speed Brain</a> and can be discarded. These errors are not visible to visitors of your website. <a href="/speed/optimization/content/speed-brain/#enable-and-disable-speed-brain">Speed Brain</a> can be disabled for the zone if needed (this feature cannot be disabled for a specific path).</p>
<h3 id="workers-specific-causes">Workers-specific causes</h3>
<p>Error 503 can also occur when using Cloudflare Workers:</p>
<ul>
<li>A Worker exceeds CPU time limits (see <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1102/">Error 1102</a>)</li>
<li>Worker code encounters memory limit issues (see <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1102/">Error 1102</a>)</li>
</ul>
<p>If you are using Workers, check the Workers dashboard for error logs and resource limit issues.</p>
<h2 id="identifying-the-source-of-a-503-error">Identifying the source of a 503 error</h2>
<p>Use the error page content to determine whether a 503 was generated by Cloudflare or your origin server:</p>
<table>
<thead>
<tr>
<th>Signal</th>
<th>Interpretation</th>
</tr>
</thead>
<tbody>
<tr>
<td>Error page HTML contains <code>cloudflare</code> or <code>cloudflare-nginx</code></td>
<td>Generated by Cloudflare — refer to <a href="#503-error-with-cloudflare-or-cloudflare-nginx">503 Error with cloudflare or cloudflare-nginx</a></td>
</tr>
<tr>
<td>Error page HTML does not contain <code>cloudflare</code> or <code>cloudflare-nginx</code></td>
<td>Your origin generated the 503 directly</td>
</tr>
</tbody>
</table>
<h3 id="cloudflare-generated-503">Cloudflare-generated 503</h3>
<p>A Cloudflare-generated 503 indicates a connectivity issue in a Cloudflare data center. Refer to <a href="#503-error-with-cloudflare-or-cloudflare-nginx">503 Error with cloudflare or cloudflare-nginx</a> for next steps, and check <strong>Security</strong> &gt; <strong>Events</strong> for active mitigation events.</p>
<h3 id="origin-generated-503">Origin-generated 503</h3>
<p>If your origin generated a 503, check origin server logs for signs of overload: CPU/memory saturation, exhausted connection pool, or application-level maintenance mode.</p>
