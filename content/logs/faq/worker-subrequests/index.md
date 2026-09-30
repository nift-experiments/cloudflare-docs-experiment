---
cp9:
  canonical: https://developers.cloudflare.com/logs/faq/worker-subrequests/
  description: Why origin fields appear on Worker subrequest log entries and how to correlate them with the initial request.
  full_title: Worker subrequests · Cloudflare Logs docs
  head_html: <title>Worker subrequests · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Why origin fields appear on Worker subrequest log entries and how to correlate them with the initial request."><link rel="canonical" href="https://developers.cloudflare.com/logs/faq/worker-subrequests/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/faq/worker-subrequests/index.md"><meta property="og:title" content="Worker subrequests · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Why origin fields appear on Worker subrequest log entries and how to correlate them with the initial request."><meta property="og:url" content="https://developers.cloudflare.com/logs/faq/worker-subrequests/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Faq"><meta name="algolia_content_type" content="Faq"><meta name="pcx_additional_products" content="Logs"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/faq/worker-subrequests/#page","headline":"Worker subrequests \u00b7 Cloudflare Logs docs","description":"Why origin fields appear on Worker subrequest log entries and how to correlate them with the initial request.","url":"https://developers.cloudflare.com/logs/faq/worker-subrequests/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/faq/worker-subrequests/
  schema: 1
---
<p><a href="/logs/faq/">❮ Back to FAQ</a></p>
<h3 id="why-are-the-origin-fields-empty-on-the-initial-request-when-a-worker-makes-a-subrequest">Why are the origin fields empty on the initial request when a Worker makes a subrequest?</h3>
<p>When a request hits a zone with a Worker, the initial HTTP request log represents the end-user request to the Worker. If that Worker later makes a <code>fetch()</code> request to your origin, Cloudflare writes a second HTTP request log for that Worker subrequest.</p>
<p>Because the initial log entry only covers the request from the client to the Worker, <code>OriginResponseStatus</code> is <code>0</code> and <code>OriginIP</code> is empty on that entry. Those fields are populated on the second log entry, which represents the Worker-to-origin fetch. For more on what <code>OriginResponseStatus=0</code> means in different contexts, refer to <a href="/logs/faq/504-origin-status-0/">504 responses with origin status 0 in Logpush</a>.</p>
<h3 id="what-the-two-log-entries-represent">What the two log entries represent</h3>
<table>
<thead>
<tr>
<th>Log entry</th>
<th>Typical <code>ClientRequestSource</code> value</th>
<th>What it represents</th>
<th>Origin fields</th>
</tr>
</thead>
<tbody>
<tr>
<td>Initial request</td>
<td><code>eyeball</code></td>
<td>End-user request to the Worker</td>
<td><code>OriginResponseStatus</code> is <code>0</code>, <code>OriginIP</code> is empty</td>
</tr>
<tr>
<td>Worker subrequest</td>
<td><code>edgeWorkerFetch</code></td>
<td>Worker <code>fetch()</code> request to the origin</td>
<td>Set when the origin is contacted</td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/logs/reference/clientrequestsource/">ClientRequestSource field</a> for the full list of possible <code>ClientRequestSource</code> values.</p>
<h3 id="how-the-two-entries-are-linked">How the two entries are linked</h3>
<p>Each log entry has its own <code>RayID</code>. The Worker subrequest also includes <code>ParentRayID</code>, which is the <code>RayID</code> of the request that triggered it — its immediate parent.</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Initial request</th>
<th>Worker subrequest</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>RayID</code></td>
<td>Unique request ID for the end-user request</td>
<td>Unique request ID for the subrequest</td>
</tr>
<tr>
<td><code>ParentRayID</code></td>
<td>Empty</td>
<td><code>RayID</code> of the request that triggered it</td>
</tr>
</tbody>
</table>
<p>To correlate the two records:</p>
<ol>
<li>Find the initial request and note its <code>RayID</code>.</li>
<li>Search for log entries where <code>ParentRayID</code> equals that <code>RayID</code>.</li>
<li>Review the matching subrequest log entry for <code>OriginIP</code>, <code>OriginResponseStatus</code>, and other origin fields.</li>
</ol>
<p>One end-user request can produce multiple Worker subrequest log entries. Each subrequest gets its own <code>RayID</code>, and each of those log entries uses the triggering request's <code>RayID</code> as its <code>ParentRayID</code>.</p>
<p><code>ParentRayID</code> is single-level — it points to the immediate parent, not the original end-user request. In a single-Worker setup this distinction does not matter because the parent is the end-user request. When Workers are chained (for example, Worker A calls Worker B which calls the origin), Worker B's subrequest log has Worker A's <code>RayID</code> as its <code>ParentRayID</code>, not the end-user's. To trace the full chain back to the end-user request, follow each <code>ParentRayID</code> one level at a time.</p>
<p>Using the initial request together with the matching subrequest entries lets you reconstruct the full request path from client to Worker to origin.</p>
<h3 id="example">Example</h3>
<pre tabindex="0"><code class="language-txt">&#35; Initial request&#10;ClientRequestSource: eyeball&#10;RayID: 7b52f2c4f9f64c1a&#10;ParentRayID:&#10;OriginResponseStatus: 0&#10;&#10;&#35; Worker subrequest&#10;ClientRequestSource: edgeWorkerFetch&#10;RayID: 7b52f2c4f9f64c1b&#10;ParentRayID: 7b52f2c4f9f64c1a&#10;OriginResponseStatus: 200&#10;OriginIP: 192.0.2.10&#10;</code></pre>
<h3 id="when-there-is-no-second-log-entry">When there is no second log entry</h3>
<p>If the Worker does not make a <code>fetch()</code> request to the origin, there is no Worker-to-origin log entry to correlate. For example, the Worker may return a response directly without contacting the origin.</p>
<h3 id="recommended-fields-to-include-in-logpush">Recommended fields to include in Logpush</h3>
<p>To investigate Worker subrequests more easily, include these fields in your HTTP request logs:</p>
<ul>
<li><code>RayID</code></li>
<li><code>ParentRayID</code></li>
<li><code>ClientRequestSource</code></li>
<li><code>OriginIP</code></li>
<li><code>OriginResponseStatus</code></li>
</ul>
