---
cp9:
  canonical: https://developers.cloudflare.com/web-analytics/data-metrics/core-web-vitals/
  description: View Core Web Vitals metrics collected by Web Analytics.
  full_title: Core Web Vitals · Cloudflare Web Analytics docs
  head_html: <title>Core Web Vitals · Cloudflare Web Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="View Core Web Vitals metrics collected by Web Analytics."><link rel="canonical" href="https://developers.cloudflare.com/web-analytics/data-metrics/core-web-vitals/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/web-analytics/data-metrics/core-web-vitals/index.md"><meta property="og:title" content="Core Web Vitals · Cloudflare Web Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="View Core Web Vitals metrics collected by Web Analytics."><meta property="og:url" content="https://developers.cloudflare.com/web-analytics/data-metrics/core-web-vitals/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Web Analytics"><meta name="algolia_product_filter" content="Cloudflare Web Analytics"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare Web Analytics"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/web-analytics/data-metrics/core-web-vitals/#page","headline":"Core Web Vitals \u00b7 Cloudflare Web Analytics docs","description":"View Core Web Vitals metrics collected by Web Analytics.","url":"https://developers.cloudflare.com/web-analytics/data-metrics/core-web-vitals/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /web-analytics/data-metrics/core-web-vitals/
  schema: 1
---
<p><a href="https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/">Core Web Vitals</a> are high-level metrics designed to measure the perceived performance of websites and web applications.</p>
<p>Three core Web Vitals metrics are measured: Largest Contentful Paint, Interaction to Next Paint, and Cumulative Layout Shift. Each of these metrics is automatically assigned a rating of Good, Needs Improvement, or Poor based on the thresholds defined by Google.</p>
<h2 id="access-core-web-vitals">Access Core Web Vitals</h2>
<p>Core Web Vitals enables you to easily pinpoint which elements in a web page are affecting the user's experience while browsing your website, in a visual form. To access Core Web Vitals:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Web Analytics</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your website and select <strong>Core Web Vitals</strong>.</li>
</ol>
<h3 id="core-web-vitals-metrics">Core Web Vitals metrics</h3>
<p>Core Web Vitals is divided into three main sections, each one with information about a specific feature that affects user experience:</p>
<ul>
<li><a href="https://web.dev/optimize-lcp/">Largest Contentful Paint (LCP)</a>: Measures perceived load speed by the user — how long the main content of the page takes to be loaded.</li>
<li><a href="https://web.dev/inp/">Interaction to Next Paint (INP)</a>: Measures user interface responsiveness – how quickly a website responds to user interactions like clicks, taps or key presses.</li>
<li><a href="https://web.dev/optimize-cls/">Cumulative Layout Shift (CLS)</a>: Measures visual stability — to what extent there are unexpected shifts in the page layout during and after page load.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15778.md")
</aside>
<p>Each of these metrics represents an impact to the user experience, which is quantified and graded by Web Analytics.</p>
<p>Cloudflare Web Analytics offers interactive exploration in Core Web Vitals by allowing you to filter data by URL, Browser, Operating System, Country, Element and more.</p>
<h3 id="debug-view">Debug view</h3>
<p>Below each graph, the 'Debug View' section has the top five elements with a negative impact on each metric. Selecting the elements shown in the data table gives you more details about them.</p>
<p>Each table — LCP, INP, and CLS — also shows you the performance of these elements in the 75th percentile (P75) at a glance. Selecting in each row of the table lets you expand the element and have access to more information, including P50, P90 and P99 metrics.</p>
<p>These numbers refer to how an element performs relatively to others in your page. For example, if an element takes 3,900 ms to load and is in the 75 percentile, this means that it is slower to load than 75% of the elements in your page.</p>
<p><img src="/assets/upstream/images/web-analytics/core-web-vitals-debug-view.png" alt="Debug View page" /></p>
<h2 id="information-collected">Information collected</h2>
<p>Web Analytics uses its lightweight JavaScript beacon to collect the information Vitals Explorer uses. It does not use any client-side state, such as cookies or <code>localStorage</code>, to collect usage metrics. Vitals Explorer also does not fingerprint individuals via their IP address, User Agent string, or any other data.</p>
<h3 id="common-data-collected-for-all-core-web-vitals-metrics">Common data collected for all Core Web Vitals metrics</h3>
<h4 id="element">Element</h4>
<p>A CSS selector representing the DOM node. With this string, you can use <code>document.querySelector(&lt;element_name&gt;)</code> in the dev console of your browser to find out which DOM node has a negative impact on your scores/values.</p>
<h4 id="path">Path</h4>
<p>The URL path at the time the Core Web Vitals are captured.</p>
<h4 id="value">Value</h4>
<p><a href="https://web.dev/cls/#layout-shift-score">The metric value</a> for each Core Web Vitals. This value is in milliseconds for LCP or INP and a score for CLS.</p>
<h3 id="additional-data-collected-for-largest-contentful-paint">Additional data collected for Largest Contentful Paint</h3>
<h4 id="url">URL</h4>
<p>The source URL (such as image, text, web fonts).</p>
<h4 id="size">Size</h4>
<p>The source object's size in bytes.</p>
<h3 id="additional-data-collected-for-cumulative-layout-shift">Additional data collected for Cumulative Layout Shift</h3>
<p>Layout information is a JSON value that includes width, height, x axis position, y axis position, left, right, top, and bottom. These values represent the layout shifts that happen on the page.</p>
<h4 id="currentrect">CurrentRect</h4>
<p>Captures the layout information of the DOM element with the largest area, after the shift in the page has occurred. This JSON value is shown as <strong>Current</strong> in the <strong>Debug View</strong> section. To access it, scroll to the <strong>Cumulative Layout Shifts (CLS)</strong> graphic &gt; <strong>Debug View</strong>. Select any element from that table to access the <strong>Layout Shifts</strong> section, where <strong>Current</strong> is presented.</p>
<h4 id="previousrect">PreviousRect</h4>
<p>Captures the layout information of the DOM element with the largest area, before the shift in the page has occurred. This JSON value is shown as <strong>Previous</strong> in the <strong>Debug View</strong> section. To access it, scroll to the <strong>Cumulative Layout Shifts (CLS)</strong> graphic &gt; <strong>Debug View</strong>. Select any element from that table to access the <strong>Layout Shifts</strong> section, where <strong>Previous</strong> is presented.</p>
