---
cp9:
  canonical: https://developers.cloudflare.com/cache/performance-review/cache-analytics/
  description: View cache hit rates and bandwidth savings in Cache Analytics.
  full_title: Cache Analytics · Cloudflare Cache (CDN) docs
  head_html: <title>Cache Analytics · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="View cache hit rates and bandwidth savings in Cache Analytics."><link rel="canonical" href="https://developers.cloudflare.com/cache/performance-review/cache-analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/performance-review/cache-analytics/index.md"><meta property="og:title" content="Cache Analytics · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="View cache hit rates and bandwidth savings in Cache Analytics."><meta property="og:url" content="https://developers.cloudflare.com/cache/performance-review/cache-analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/performance-review/cache-analytics/#page","headline":"Cache Analytics \u00b7 Cloudflare Cache (CDN) docs","description":"View cache hit rates and bandwidth savings in Cache Analytics.","url":"https://developers.cloudflare.com/cache/performance-review/cache-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/performance-review/cache-analytics/
  schema: 1
---
<p>Cache Analytics shows how much of your site's traffic is served from Cloudflare's cache versus your origin server. When content is served from cache, visitors get faster page loads and your origin web server handles less traffic. Use Cache Analytics to identify resources that are <a href="/cache/concepts/cache-responses/#miss">missing from cache</a>, <a href="/cache/concepts/cache-responses/#expired">expired</a> (cached copy is outdated), or <a href="/cache/concepts/cache-responses/#noneunknown">ineligible for caching</a> (not eligible for caching). You can filter by hostname, review the top URLs that miss cache, and query up to three days of data.</p>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Retention period</td>
<td>N/A</td>
<td>7 days</td>
<td>30 days</td>
<td>30 days</td>
</tr>
</tbody>
</table>
<h2 id="access-cache-analytics">Access Cache Analytics</h2>
<p>In the Cloudflare dashboard, go to the <strong>Caching</strong> page.</p>
<div class="nb-dash-button"></div>
<h2 id="requests-vs-data-transfer">Requests vs Data Transfer</h2>
<p>You can decide whether to focus on <strong>Requests</strong> or <strong>Data Transfer</strong>:</p>
<ul>
<li><strong>Requests</strong> (default view) helps assess performance. Each cache <a href="/cache/concepts/cache-responses/#miss">MISS</a> means the request must go to your origin server instead of being served from Cloudflare's cache, which adds latency.</li>
<li><strong>Data Transfer</strong> is useful for cost analysis, since most hosting providers charge for data sent from their servers (egress bandwidth).</li>
</ul>
<p>You can switch between these views while keeping other analytics filters applied.</p>
<p>For best practices related to Cache Analytics, refer to <a href="/cache/performance-review/cache-performance/">Cache performance</a>.</p>
<h2 id="add-filters">Add filters</h2>
<p>Create filters to narrow the data to specific traffic segments. Example filters include <strong>Cache status</strong>, <strong>Host</strong>, <strong>Path</strong>, or <strong>Content type</strong>.</p>
<p>To add filters, under <strong>Cache Performance</strong>, select <strong>Add filter</strong>. Select <strong>Apply</strong> when you are done.</p>
<h2 id="review-cache-status">Review cache status</h2>
<p>The <strong>Requests summary</strong> graph shows how your traffic changes over time, such as in response to a high-traffic event or a recent configuration change. The Requests summary is based on a sample of requests, not the full dataset. Totals are extrapolated from the sample to represent overall traffic. For more information on how sampling works, refer to <a href="/analytics/sampling/">Understanding sampling in Cloudflare Analytics</a>.</p>
<p><strong>Served by Cloudflare</strong> indicates content served by Cloudflare that did not require contacting your origin web server. <strong>Served by Origin</strong> indicates traffic served from the origin web server.</p>
<p>Revalidated requests — where Cloudflare checks with your origin to confirm cached content is still current — are counted differently depending on the view. In the <strong>Data Transfer</strong> view, revalidated requests count as <strong>Served by Cloudflare</strong> because the response body is served from cache, not re-downloaded from the origin. In the <strong>Requests</strong> view, revalidated requests count as <strong>Served by Origin</strong> because Cloudflare still contacts the origin server to verify the content.</p>
<p><strong>Cache status</strong> graphs break down why traffic is served from Cloudflare versus the origin web server, organized by content type.</p>
<p>For a breakdown of cache statuses and their descriptions, refer to <a href="/cache/concepts/cache-responses/">Cloudflare cache responses</a>.</p>
<h2 id="review-requests-by-source">Review requests by source</h2>
<p>Cache Analytics shows the most frequent values (top N) for several request attributes. Apply filters before reviewing these metrics to focus on specific traffic. For example, filtering to only view traffic with an Expired or Revalidated cache status shows which URLs were primarily responsible for those statuses.</p>
<h3 id="empty-content-types">Empty content types</h3>
<p>Finding an <strong>empty</strong> content type in your analytics is common. Responses to redirect status codes (<code>301</code>/<code>302</code>) typically do not include content, so they have no content type. Similarly, many HTTP error responses, such as <code>403</code>, do not return <code>text/html</code> and are also reported as empty.</p>
