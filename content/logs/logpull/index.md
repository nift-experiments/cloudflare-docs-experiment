---
cp9:
  canonical: https://developers.cloudflare.com/logs/logpull/
  description: Pull request logs via the Logpull REST API.
  full_title: Logpull · Cloudflare Logs docs
  head_html: <title>Logpull · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Pull request logs via the Logpull REST API."><link rel="canonical" href="https://developers.cloudflare.com/logs/logpull/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/logpull/index.md"><meta property="og:title" content="Logpull · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Pull request logs via the Logpull REST API."><meta property="og:url" content="https://developers.cloudflare.com/logs/logpull/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Logs"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/logpull/#page","headline":"Logpull \u00b7 Cloudflare Logs docs","description":"Pull request logs via the Logpull REST API.","url":"https://developers.cloudflare.com/logs/logpull/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/logpull/
  schema: 1
---
<p>Cloudflare Logpull is a REST API for consuming request logs over HTTP. These logs contain data related to the connecting client, the request path through the Cloudflare network, and the response from the origin web server. This data is useful for enriching existing logs on an origin server. Logpull is available to customers on the Enterprise plan.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10479.md")
</aside>
<p>Review the following content to learn more about Logpull.</p>
<ul class="directory-listing"><li><a href="/logs/logpull/understanding-the-basics/">Understanding the basics</a></li><li><a href="/logs/logpull/enabling-log-retention/">Enabling log retention</a></li><li><a href="/logs/logpull/requesting-logs/">Requesting logs</a></li><li><a href="/logs/logpull/additional-details/">Additional details</a></li></ul>
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
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h3 id="limitation">Limitation</h3>
<p>Logpull is unavailable when the Customer Metadata Boundary (CMB) is set outside the US region. Specifically, it does not work when CMB is restricted to the EU-only setting. For more details, refer to the <a href="/data-localization/">Cloudflare Data Localization</a> documentation.</p>
