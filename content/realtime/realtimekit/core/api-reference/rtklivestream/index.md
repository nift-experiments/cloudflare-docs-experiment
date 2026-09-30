---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtklivestream/
  description: ''
  full_title: RTKLivestream · Cloudflare Realtime docs
  head_html: <title>RTKLivestream · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtklivestream/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtklivestream/index.md"><meta property="og:title" content="RTKLivestream · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtklivestream/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtklivestream/#page","headline":"RTKLivestream \u00b7 Cloudflare Realtime docs","url":"https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtklivestream/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/core/api-reference/rtklivestream/
  schema: 1
---
<!-- Auto Generated Below -->
<p><a name="module_RTKLivestream"></a></p>
<p>The RTKLivestream module represents the state of the current livestream, and allows
to start/stop live streams.</p>
<ul>
<li><a href="#module_RTKLivestream">RTKLivestream</a>
<ul>
<li><a href="#module_RTKLivestream+start">.start([livestreamConfig])</a></li>
<li><a href="#module_RTKLivestream+stop">.stop()</a></li>
</ul>
</li>
</ul>
<p><a name="module_RTKLivestream+start"></a></p>
<h3 id="meeting-livestream-start-livestreamconfig">meeting.livestream.start([livestreamConfig])</h3>
Starts livestreaming the meeting.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKLivestream"><code>RTKLivestream</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>[livestreamConfig]</td>
<td><code>StartLivestreamConfig</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKLivestream+stop"></a></p>
<h3 id="meeting-livestream-stop">meeting.livestream.stop()</h3>
Stops livestreaming the meeting.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKLivestream"><code>RTKLivestream</code></a></p>
