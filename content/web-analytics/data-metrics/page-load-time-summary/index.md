---
cp9:
  canonical: https://developers.cloudflare.com/web-analytics/data-metrics/page-load-time-summary/
  description: Page load time metrics collected by Web Analytics.
  full_title: Page load time · Cloudflare Web Analytics docs
  head_html: <title>Page load time · Cloudflare Web Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Page load time metrics collected by Web Analytics."><link rel="canonical" href="https://developers.cloudflare.com/web-analytics/data-metrics/page-load-time-summary/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/web-analytics/data-metrics/page-load-time-summary/index.md"><meta property="og:title" content="Page load time · Cloudflare Web Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Page load time metrics collected by Web Analytics."><meta property="og:url" content="https://developers.cloudflare.com/web-analytics/data-metrics/page-load-time-summary/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Web Analytics"><meta name="algolia_product_filter" content="Cloudflare Web Analytics"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Web Analytics"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/web-analytics/data-metrics/page-load-time-summary/#page","headline":"Page load time \u00b7 Cloudflare Web Analytics docs","description":"Page load time metrics collected by Web Analytics.","url":"https://developers.cloudflare.com/web-analytics/data-metrics/page-load-time-summary/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /web-analytics/data-metrics/page-load-time-summary/
  schema: 1
---
<p>Page load time summary gives you an overview of how long your web page takes to load, broken down by area. To access Page load time:</p>
<ol>
<li>Go to <a href="https://dash.cloudflare.com/?to=/:account/web-analytics">Web Analytics</a> from your account home page, and choose a website.</li>
<li>Select <strong>Page load time</strong>.</li>
</ol>
<h2 id="components">Components</h2>
<p>Below is a list of all the components you can inspect:</p>
<h3 id="page-load">Page load</h3>
<p>The total amount of time required to load the page. Note that page load time does not correspond to the sum of the other timings available in Web Analytics. This happens because the page load time also includes timings that are not displayed, such as pre-DNS lookup timings and unattributed gaps between timing metrics.</p>
<h3 id="dns-domainlookupend-domainlookupstart">DNS (<code>domainLookupEnd</code> - <code>domainLookupStart</code>)</h3>
<p>How long a DNS query takes. This could appear as zero for reused connections or content stored in the local cache (memory or disk).</p>
<h3 id="tcp-connectend-connectstart">TCP (<code>connectEnd</code> - <code>connectStart</code>)</h3>
<p>How long it takes to establish a TCP connection with the server. If using HTTPS, this process includes TLS negotiation time.</p>
<h3 id="request-responsestart-requeststart">Request (<code>responseStart</code> - <code>requestStart</code>)</h3>
<p>The time elapsed between making an HTTP request and receiving the first byte of the response.</p>
<h3 id="response-responseend-responsestart">Response (<code>responseEnd</code> - <code>responseStart</code>)</h3>
<p>The time elapsed between the first byte and the last byte of the received response. Think of this as a resource download time.</p>
<h3 id="processing-domcomplete-dominteractive">Processing (<code>domComplete</code> - <code>domInteractive</code>)</h3>
<p>How long it took to render the page. This includes loading any resources that block page rendering, including images, scripts, and style sheets. If this number is big, optimize your document architecture, resource size, or configure settings in the Cloudflare Speed app. This document process can be drilled down more with <code>domInteractive</code>, <code>domContentLoadedEventStart</code>, <code>domContentLoadedEventEnd</code>, and <code>domComplete</code>.</p>
<h3 id="load-event-loadeventend-loadeventstart">Load Event (<code>loadEventEnd</code> - <code>loadEventStart</code>)</h3>
<p>An event triggered by the browser when a document and its resources finish loading. The Load Event duration may be a useful metric if you have additional functions or any logic for the load event.</p>
<p><img src="/assets/upstream/images/web-analytics/dash-web_analytics-page_load_time.png" alt="Web Analytics load time summary page" /></p>
<h2 id="data-collected-for-paint-timings">Data collected for Paint Timings</h2>
<p>To make Web Analytics work, Cloudflare collects several types of data points. These are the additional data points collected for Paint Timings:</p>
<h3 id="first-paint">First Paint</h3>
<p>The time between navigation and when the browser renders the first pixels to the screen.</p>
<h3 id="first-contentful-paint">First Contentful Paint</h3>
<p>Time when the browser renders the first bit of content from the DOM.</p>
