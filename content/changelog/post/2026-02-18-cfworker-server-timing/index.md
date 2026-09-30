---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-02-18-cfworker-server-timing/
  description: New updates and improvements at Cloudflare.
  full_title: New cfWorker metric in Server-Timing header · Changelog
  head_html: <title>New cfWorker metric in Server-Timing header · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-02-18-cfworker-server-timing/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="New cfWorker metric in Server-Timing header · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-02-18-cfworker-server-timing/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-18-cfworker-server-timing/#page","headline":"New cfWorker metric in Server-Timing header \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-02-18-cfworker-server-timing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-02-18-cfworker-server-timing/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 18, 2026</time><h2 id="post-title">New cfWorker metric in Server-Timing header</h2>
<div class="changelog-badges"><span>analytics</span></div><div class="changelog-body"><p>The Server-Timing header now includes a new <code>cfWorker</code> metric that measures time spent executing Cloudflare Workers, including any subrequests performed by the Worker. This helps developers accurately identify whether high Time to First Byte (TTFB) is caused by Worker processing or slow upstream dependencies.</p>
<p>Previously, Worker execution time was included in the <code>edge</code> metric, making it harder to identify true edge performance. The new <code>cfWorker</code> metric provides this visibility:</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>edge</code></td>
<td>Total time spent on the Cloudflare edge, including Worker execution</td>
</tr>
<tr>
<td><code>origin</code></td>
<td>Time spent fetching from the origin server</td>
</tr>
<tr>
<td><code>cfWorker</code></td>
<td>Time spent in Worker execution, including subrequests but excluding origin fetch time</td>
</tr>
</tbody>
</table>
<h4 id="example-response">Example response</h4>
<pre tabindex="0"><code class="language-txt">Server-Timing: cdn-cache; desc=DYNAMIC, edge; dur=20, origin; dur=100, cfWorker; dur=7&#10;</code></pre>
<p>In this example, the edge took 20ms, the origin took 100ms, and the Worker added just 7ms of processing time.</p>
<h4 id="availability">Availability</h4>
<p>The <code>cfWorker</code> metric is enabled by default if you have <a href="/web-analytics/">Real User Monitoring (RUM)</a> enabled. Otherwise, you can enable it using <a href="/rules/">Rules</a>.</p>
<p>This metric is particularly useful for:</p>
<ul>
<li><strong>Performance debugging</strong>: Quickly determine if latency is caused by Worker code, external API calls within Workers, or slow origins.</li>
<li><strong>Optimization targeting</strong>: Identify which component of your request path needs optimization.</li>
<li><strong>Real User Monitoring (RUM)</strong>: Access detailed timing breakdowns directly from response headers for client-side analytics.</li>
</ul>
<p>For more information about Server-Timing headers, refer to the <a href="https://www.w3.org/TR/server-timing/">W3C Server Timing specification</a>.</p>
</div></article></div>
