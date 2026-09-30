---
cp9:
  canonical: https://developers.cloudflare.com/cache/how-to/always-online/
  description: Serve cached pages when your origin server is unavailable.
  full_title: Always Online · Cloudflare Cache (CDN) docs
  head_html: <title>Always Online · Cloudflare Cache (CDN) docs</title><meta name="generator" content="Nift"><meta name="description" content="Serve cached pages when your origin server is unavailable."><link rel="canonical" href="https://developers.cloudflare.com/cache/how-to/always-online/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cache/how-to/always-online/index.md"><meta property="og:title" content="Always Online · Cloudflare Cache (CDN) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Serve cached pages when your origin server is unavailable."><meta property="og:url" content="https://developers.cloudflare.com/cache/how-to/always-online/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cache / CDN"><meta name="algolia_product_filter" content="Cache / CDN"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cache / CDN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cache/how-to/always-online/#page","headline":"Always Online \u00b7 Cloudflare Cache (CDN) docs","description":"Serve cached pages when your origin server is unavailable.","url":"https://developers.cloudflare.com/cache/how-to/always-online/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cache/how-to/always-online/
  schema: 1
---
<p>Cloudflare’s Always Online feature is now integrated with the <a href="https://archive.org/">Internet Archive</a> so that visitors can access a portion of your website even when your origin server is unreachable and a Cloudflare-cached version is unavailable. When your origin is unreachable, Always Online checks Cloudflare’s cache for a stale or expired version of your website. If a version does not exist, Cloudflare goes to the Internet Archive to fetch and serve static portions of your website.</p>
<p>When you enable Always Online with Internet Archive integration, Cloudflare shares your hostname and popular URL paths with the archive so that the Internet Archive’s crawler stores the pages you want archived. When submitting targets to the crawler, Cloudflare identifies the most popular URLs found among GET requests that returned a 200 HTTP status code in the previous five hours.</p>
<p>Note that Cloudflare does not save a copy of every page of your website, and it cannot serve dynamic content while your origin is offline. If the requested page is not in the Internet Archive's Wayback Machine, the visitor sees the actual error page caused by the offline origin web server.</p>
<p>When the Internet Archive integration is enabled, Cloudflare tells the Internet Archive what pages to crawl and how often. The pages to crawl, as previously mentioned, are the most popular URLs that were successfully visited in the last five hours. The crawling intervals, to ensure stability of service, are limited by Cloudflare. Limits vary according to your Cloudflare plan.</p>
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
<tr>
<td>Crawl interval</td>
<td>Every 30 days</td>
<td>Every 15 days</td>
<td>Every 5 days</td>
<td>Every 5 days</td>
</tr>
</tbody>
</table>
<h2 id="visitor-experience">Visitor Experience</h2>
<p>When Always Online with Internet Archive integration is enabled, visitors see a banner at the top of the webpage explaining they are visiting an archived version of the website. Visitors can select the Refresh button to check whether the origin has recovered and fresh content is available.</p>
<p>When a visitor requests content and Cloudflare is unable to reach your origin server, Cloudflare returns an HTTP response status code in the range <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-520/">520–527</a>, depending on the issue. These status codes are generated by Cloudflare and indicate that the origin is unreachable. Always Online only activates when Cloudflare cannot connect to your origin — it does not activate when the origin is reachable but returning error responses.</p>
<p>If your origin is reachable and returns a 5xx status code (such as a 520), Always Online will not trigger because the origin is online. Always Online is designed to handle origin unreachability, not origin errors.</p>
<p>When the Internet Archive integration is enabled, Cloudflare checks the archive and serves the most recently archived version of the page.</p>
<p>Visitors who interact with dynamic parts of a website, such as a shopping cart or comment box, will see an error page caused by the offline origin web server.</p>
<h2 id="enable-always-online">Enable Always Online</h2>
<p>Here is how to enable Always Online in the dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Configuration</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Choose the domain that will use Always Online with Internet Archive integration.</li>
<li>Under <strong>Always Online</strong>, set the toggle to <strong>On</strong>.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3813.md")
</aside>
<p>Refer to <a href="/cache/troubleshooting/always-online/">Always Online</a> for best practices, limitations, and FAQs.</p>
