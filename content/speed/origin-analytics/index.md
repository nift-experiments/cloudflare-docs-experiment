---
cp9:
  canonical: https://developers.cloudflare.com/speed/origin-analytics/
  description: See how your origin server responds to Cloudflare. Identify slow endpoints, monitor response times, and diagnose errors.
  full_title: Origin Analytics · Cloudflare Speed docs
  head_html: <title>Origin Analytics · Cloudflare Speed docs</title><meta name="generator" content="Nift"><meta name="description" content="See how your origin server responds to Cloudflare. Identify slow endpoints, monitor response times, and diagnose errors."><link rel="canonical" href="https://developers.cloudflare.com/speed/origin-analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/speed/origin-analytics/index.md"><meta property="og:title" content="Origin Analytics · Cloudflare Speed docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="See how your origin server responds to Cloudflare. Identify slow endpoints, monitor response times, and diagnose errors."><meta property="og:url" content="https://developers.cloudflare.com/speed/origin-analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Speed"><meta name="algolia_product_filter" content="Speed"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Speed"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/speed/origin-analytics/#page","headline":"Origin Analytics \u00b7 Cloudflare Speed docs","description":"See how your origin server responds to Cloudflare. Identify slow endpoints, monitor response times, and diagnose errors.","url":"https://developers.cloudflare.com/speed/origin-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /speed/origin-analytics/
  schema: 1
---
<p>Origin Analytics shows how your origin server responds to Cloudflare, using data collected at the edge without an agent on your origin.</p>
<p>Use Origin Analytics to identify slow endpoints, monitor origin response times, and diagnose errors. When something goes wrong, Origin Analytics shows whether the source is your origin, the network path, or Cloudflare. For common error codes, refer to <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/">Cloudflare 5xx errors</a>.</p>
<h2 id="view-origin-analytics">View Origin Analytics</h2>
<p>To open the Origin Analytics tab:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and select your account and domain.</li>
<li>Go to <strong>Speed</strong> &gt; <strong>Origin Analytics</strong>.</li>
</ol>
<h2 id="metrics">Metrics</h2>
<p>The dashboard displays the following metrics, derived from your zone's edge logs.</p>
<h3 id="origin-response-time">Origin response time</h3>
<p>Use this metric to spot slowdowns and catch requests approaching your timeout threshold before they result in <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-524/">524 errors</a>.</p>
<p>Origin response time shows how long your origin takes to respond to Cloudflare, measured at the 50th, 95th, and 99th percentiles. A reference line indicates your zone's configured origin timeout.</p>
<p>The clock starts when Cloudflare decides the request must go to origin (a cache miss) and stops when Cloudflare receives the response headers — not the full body — back from your origin. It includes DNS resolution, TCP and TLS handshakes, request transmission, origin processing, and response receipt. If <a href="/argo-smart-routing/">Argo Smart Routing</a> or <a href="/cache/how-to/tiered-cache/">Tiered Cache</a> is enabled, the metric also includes time spent routing through those services.</p>
<p>Because this measures the full upstream round trip, Origin Analytics shows higher response times than your origin's own monitoring tools (for example, Grafana or Datadog), which measure only server-side processing time.</p>
<h3 id="origin-status-codes">Origin status codes</h3>
<p>Use this metric to understand what your origin actually returned when users report errors. The error code the end user sees can differ from what your origin returned, because Cloudflare wraps certain origin failures in its own error codes (such as <code>520</code>, <code>522</code>, or <code>524</code>).</p>
<p>Origin Analytics shows both values: the response code from your origin (<code>originResponseStatus</code>) and the code Cloudflare served to the end user (<code>edgeResponseStatus</code>). Status codes are grouped by class (2xx, 3xx, 4xx, 5xx) and shown over time.</p>
<p>The following table shows common scenarios where these values differ:</p>
<table>
<thead>
<tr>
<th>What happened</th>
<th><code>originResponseStatus</code></th>
<th><code>edgeResponseStatus</code></th>
</tr>
</thead>
<tbody>
<tr>
<td>Origin returned <code>200</code> with malformed headers</td>
<td><code>200</code></td>
<td><code>520</code></td>
</tr>
<tr>
<td>Origin returned a server error</td>
<td><code>503</code></td>
<td><code>503</code> or <code>520</code></td>
</tr>
<tr>
<td>Origin closed the connection mid-response</td>
<td><code>0</code></td>
<td><code>520</code></td>
</tr>
<tr>
<td>Origin did not respond in time</td>
<td><code>0</code></td>
<td><code>524</code></td>
</tr>
<tr>
<td>TCP connection to origin failed</td>
<td><code>0</code></td>
<td><code>522</code></td>
</tr>
<tr>
<td>Request served from cache</td>
<td><code>0</code></td>
<td><code>200</code></td>
</tr>
<tr>
<td>Worker handled the request</td>
<td><code>0</code></td>
<td>Varies</td>
</tr>
</tbody>
</table>
<p>A status code of <code>0</code> means Cloudflare did not receive an HTTP response from the origin. This can indicate a connection failure, a timeout, or that the request was served from cache or handled by a <a href="/workers/">Worker</a> before reaching the origin.</p>
<h3 id="top-endpoints">Top endpoints</h3>
<p>Use this table to narrow down which specific path is causing slowdowns or errors. Request paths are ranked by P95 response time, error rate, request volume, or TCP failure rate.</p>
<h2 id="common-diagnostic-flows">Common diagnostic flows</h2>
<p>The following table describes how to use Origin Analytics to investigate common origin errors.</p>
<table>
<thead>
<tr>
<th>Issue</th>
<th>What to check</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-524/">524 timeout errors</a></td>
<td>Origin response time chart. If P95 is approaching the timeout threshold, identify slow paths in the <strong>Top endpoints</strong> table.</td>
</tr>
<tr>
<td><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-522/">522 connection errors</a></td>
<td>Verify that your firewall allows <a href="https://www.cloudflare.com/ips/">Cloudflare IP ranges</a> and that your origin is listening on the expected port.</td>
</tr>
<tr>
<td><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-520/">520 unknown errors</a></td>
<td>Origin status code chart. If the origin returned a <code>200</code> but Cloudflare served a <code>520</code>, the origin response was malformed (for example, oversized headers or an early connection close).</td>
</tr>
</tbody>
</table>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/">Cloudflare 5xx errors</a> — diagnose specific error codes like 520, 522, and 524.</li>
<li><a href="/logs/logpush/">Logpush</a> — export per-request logs with origin timing fields not available in the dashboard.</li>
<li><a href="/analytics/graphql-api/">GraphQL Analytics API</a> — query origin metrics programmatically, including fields not shown in the dashboard.</li>
<li><a href="/speed/observatory/dashboard/">Observatory dashboard</a> — monitor end-user performance with synthetic tests and real user data.</li>
</ul>
