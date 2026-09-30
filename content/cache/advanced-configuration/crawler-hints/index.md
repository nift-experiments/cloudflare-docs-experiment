---
cp9:
  canonical: https://developers.cloudflare.com/cache/advanced-configuration/crawler-hints/
  description: Signal search engine crawlers when content changes with IndexNow.
  full_title: Crawler Hints · Cloudflare Cache (CDN) docs
  head_html: <title>Crawler Hints · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Signal search engine crawlers when content changes with IndexNow."><link rel="canonical" href="https://developers.cloudflare.com/cache/advanced-configuration/crawler-hints/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/advanced-configuration/crawler-hints/index.md"><meta property="og:title" content="Crawler Hints · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Signal search engine crawlers when content changes with IndexNow."><meta property="og:url" content="https://developers.cloudflare.com/cache/advanced-configuration/crawler-hints/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/advanced-configuration/crawler-hints/#page","headline":"Crawler Hints \u00b7 Cloudflare Cache (CDN) docs","description":"Signal search engine crawlers when content changes with IndexNow.","url":"https://developers.cloudflare.com/cache/advanced-configuration/crawler-hints/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/advanced-configuration/crawler-hints/
  schema: 1
---
<p>Crawler Hints uses Cloudflare cache signals to tell search engines when your content has likely changed, so they crawl your site at the right time instead of guessing.</p>
<h2 id="background">Background</h2>
<p>Search engines and similar services operate massive networks of bots that crawl the Internet to identify the content most relevant to a user query. Content on the web is always changing though, and search engine crawlers must continually wander the Internet and guess how frequently they should check a site for content updates.</p>
<p>With Crawler Hints, Cloudflare can proactively tell a crawler about the best time to index or when content changes. Additionally, Crawler Hints supports <a href="https://www.indexnow.org/">IndexNow</a>, which allows websites to notify search engines whenever content on their website content is created, updated, or deleted. Crawler Hints uses cache-status <a href="/cache/concepts/cache-responses/#miss"><code>MISS</code></a> to determine when content has likely been updated and sends it to IndexNow's crawler. If an asset's response has an HTTP status code greater than 4xx, the Crawler hints will not report that to <a href="https://www.indexnow.org/">IndexNow</a>.</p>
<h2 id="benefits">Benefits</h2>
<p>Crawler Hints help search engines and other bot-powered services serve the freshest version of your content, which can improve search rankings.</p>
<p>Crawler Hints also reduces unnecessary crawl traffic to your origin, lowering resource consumption and improving site performance.</p>
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
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="enable-crawler-hints">Enable Crawler Hints</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Configuration</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Enable <strong>Crawler Hints</strong>.</li>
</ol>
<p>After enabling Crawler Hints, Cloudflare will begin sending hints to search engines about when they should crawl particular parts of your website.</p>
<h2 id="prevent-indexing-for-a-specific-page">Prevent indexing for a specific page</h2>
<p>When enabled, Crawler Hints is a global setting for your entire website. You can stop a specific page from being indexed by either:</p>
<ul>
<li>Having the origin server send through the header <code>X-Robots-Tag: noindex</code> on any pages that should not be indexed.</li>
<li>Including <code>&lt;meta name=&quot;robots&quot; content=&quot;noindex, nofollow&quot; /&gt;</code> in the HTML of any pages that should not be indexed.</li>
<li>Creating a <a href="/rules/transform/response-header-modification/">Response header Transform Rule</a> in Cloudflare to add the <code>X-Robots-Tag: noindex</code> header instead of doing it from the origin server.</li>
</ul>
