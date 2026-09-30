---
cp9:
  canonical: https://developers.cloudflare.com/pages/how-to/web-analytics/
  description: Set up Cloudflare Web Analytics on your Pages project with one-click configuration.
  full_title: Enable Web Analytics · Cloudflare Pages docs
  head_html: <title>Enable Web Analytics · Cloudflare Pages docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up Cloudflare Web Analytics on your Pages project with one-click configuration."><link rel="canonical" href="https://developers.cloudflare.com/pages/how-to/web-analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pages/how-to/web-analytics/index.md"><meta property="og:title" content="Enable Web Analytics · Cloudflare Pages docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up Cloudflare Web Analytics on your Pages project with one-click configuration."><meta property="og:url" content="https://developers.cloudflare.com/pages/how-to/web-analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pages"><meta name="algolia_product_filter" content="Pages"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Pages"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pages/how-to/web-analytics/#page","headline":"Enable Web Analytics \u00b7 Cloudflare Pages docs","description":"Set up Cloudflare Web Analytics on your Pages project with one-click configuration.","url":"https://developers.cloudflare.com/pages/how-to/web-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pages/how-to/web-analytics/
  schema: 1
---
<p>Cloudflare Web Analytics provides free, privacy-first analytics for your website without changing your DNS or using Cloudflare’s proxy. Cloudflare Web Analytics helps you understand the performance of your web pages as experienced by your site visitors.</p>
<p>All you need to enable Cloudflare Web Analytics is a Cloudflare account and a JavaScript snippet on your page to start getting information on page views and visitors. The JavaScript snippet (also known as a beacon) collects metrics using the Performance API, which is available in all major web browsers.</p>
<h2 id="enable-on-pages-project">Enable on Pages project</h2>
<p>Cloudflare Pages offers a one-click setup for Web Analytics:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project.
3. Go to **Metrics** and select **Enable** under Web Analytics.
<p>Cloudflare will automatically add the JavaScript snippet to your Pages site on the next deployment.</p>
<h2 id="view-metrics">View metrics</h2>
<p>To view the metrics associated with your Pages project:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Web Analytics</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select the analytics associated with your Pages project.
<p>For more details about how to use Web Analytics, refer to the <a href="/web-analytics/data-metrics/">Web Analytics documentation</a>.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>For Cloudflare to automatically add the JavaScript snippet, your pages need to have valid HTML.</p>
<p>For example, Cloudflare would not be able to enable Web Analytics on a page like this:</p>
<pre tabindex="0"><code class="language-html">Hello world.&#10;</code></pre>
<p>For Web Analytics to correctly insert the JavaScript snippet, you would need valid HTML output, such as:</p>
<pre tabindex="0"><code class="language-html">&lt;!DOCTYPE html&gt;&#10;&lt;html&gt;&#10;	&lt;head&gt;&#10;		&lt;title&gt;Title&lt;/title&gt;&#10;	&lt;/head&gt;&#10;	&lt;body&gt;&#10;&#10;		&lt;p&gt;Hello world.&lt;/p&gt;&#10;&#10;	&lt;/body&gt;&#10;&lt;/html&gt;&#10;</code></pre>
