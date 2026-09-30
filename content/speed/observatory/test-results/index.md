---
cp9:
  canonical: https://developers.cloudflare.com/speed/observatory/test-results/
  description: Interpret Lighthouse scores and Core Web Vitals from Observatory tests.
  full_title: Understand test results · Cloudflare Speed docs
  head_html: <title>Understand test results · Cloudflare Speed docs</title><meta name="generator" content="Nift"><meta name="description" content="Interpret Lighthouse scores and Core Web Vitals from Observatory tests."><link rel="canonical" href="https://developers.cloudflare.com/speed/observatory/test-results/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/speed/observatory/test-results/index.md"><meta property="og:title" content="Understand test results · Cloudflare Speed docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Interpret Lighthouse scores and Core Web Vitals from Observatory tests."><meta property="og:url" content="https://developers.cloudflare.com/speed/observatory/test-results/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Speed"><meta name="algolia_product_filter" content="Speed"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Speed"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/speed/observatory/test-results/#page","headline":"Understand test results \u00b7 Cloudflare Speed docs","description":"Interpret Lighthouse scores and Core Web Vitals from Observatory tests.","url":"https://developers.cloudflare.com/speed/observatory/test-results/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /speed/observatory/test-results/
  schema: 1
---
<p>The test result page shows you how your website performed regarding several key industry metrics. Some of these metrics are presented for synthetic tests and the real user monitoring, and others only apply to synthetic tests or only to real user monitoring.</p>
<h2 id="synthetic-tests-and-real-user-monitoring-metrics">Synthetic tests and real user monitoring metrics</h2>
<p>These metrics are presented for the synthetic tests and they are also collected as part of the real user data.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr>
<td>Time to First Byte (<a href="https://web.dev/ttfb/">TTFB</a>)</td>
<td>Measures the time between the request for a resource and when the first byte of a response begins to arrive.</td>
</tr>
<tr>
<td>First Contentful Paint (<a href="https://web.dev/first-contentful-paint/">FCP</a>)</td>
<td>Measures the time from when the page starts loading to when any part of the page's content is rendered on the screen.</td>
</tr>
<tr>
<td>Largest Contentful Paint (<a href="https://web.dev/lcp/">LCP</a>)</td>
<td>CP reports the render time of the largest image or text block visible within the viewport.</td>
</tr>
<tr>
<td>Cumulative Layout Shift (<a href="https://web.dev/cls/">CLS</a>)</td>
<td>Measures the largest burst of layout shift scores for every unexpected layout shift that occurs during the entire lifespan of a page.</td>
</tr>
</tbody>
</table>
<h2 id="synthetic-tests-metrics">Synthetic tests metrics</h2>
<p>These metrics result from the synthetic tests.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr>
<td>Time to Interactive (<a href="https://web.dev/tti/">TTI</a>)</td>
<td>Measures the time from when the page starts loading to when its main sub-resources have loaded and it is capable of reliably responding to user input quickly.</td>
</tr>
<tr>
<td>Total Blocking Time (<a href="https://web.dev/tbt/">TBT</a>)</td>
<td>Measures the total amount of time between First Contentful Paint (FCP) and Time to Interactive (TTI) where the main thread was blocked for long enough to prevent input responsiveness.</td>
</tr>
<tr>
<td><a href="https://web.dev/speed-index/">Speed index</a></td>
<td>Measures how quickly content is visually displayed during page load.</td>
</tr>
</tbody>
</table>
<h2 id="real-user-monitoring-metrics">Real user monitoring metrics</h2>
<p>These metrics are collected as part of the real user data, as they require real user interaction with a page.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr>
<td>Interaction to Next Paint (<a href="https://web.dev/inp/">INP</a>)</td>
<td>Aims to represent a page's overall responsiveness by measuring all click, tap, and keyboard interactions made with a page.</td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/web-analytics/data-metrics/">Data and metrics</a> for more information about the metrics you can find in the Real User Monitoring dashboard. You can find details about <a href="/web-analytics/data-metrics/core-web-vitals/">Core Web Vitals</a>, the debug view and the data collected.</p>
<h2 id="network-monitoring-metrics">Network monitoring metrics</h2>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr>
<td>Wait Time</td>
<td>Measures the time spent waiting for the server to send back the first byte of a response after a request is made.</td>
</tr>
<tr>
<td>Load Time</td>
<td>Measures the total time it takes for a web page to fully load in a user’s browser from the network.</td>
</tr>
<tr>
<td>Time to First Byte (<a href="https://web.dev/articles/ttfb">TTFB</a>)</td>
<td>Measures the duration between initiating a web page request and receiving the first byte from the server.</td>
</tr>
<tr>
<td>Server Response Time</td>
<td>Measures the time it takes for a server to respond to a request from a user's browser.</td>
</tr>
<tr>
<td>Connect Time</td>
<td>Measures the time taken to establish a connection between the user's browser and the web server.</td>
</tr>
<tr>
<td>TLS Time</td>
<td>Measures the time required to complete the TLS/SSL handshake between the user's browser and the web server.</td>
</tr>
</tbody>
</table>
