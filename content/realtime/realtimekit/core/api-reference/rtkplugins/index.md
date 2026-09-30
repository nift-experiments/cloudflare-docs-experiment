---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugins/
  description: ''
  full_title: RTKPlugins · Cloudflare Realtime docs
  head_html: <title>RTKPlugins · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugins/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugins/index.md"><meta property="og:title" content="RTKPlugins · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugins/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugins/#page","headline":"RTKPlugins \u00b7 Cloudflare Realtime docs","url":"https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugins/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/core/api-reference/rtkplugins/
  schema: 1
---
<!-- Auto Generated Below -->
<p><a name="module_RTKPlugins"></a></p>
<p>The RTKPlugins module consists of all the plugins in the meeting. It has 2 maps:</p>
<ul>
<li><code>all</code>: Consists of all the plugins in the meeting.</li>
<li><code>active</code>: Consists of the plugins that are currently in use.</li>
</ul>
<ul>
<li><a href="#module_RTKPlugins">RTKPlugins</a>
<ul>
<li><a href="#module_RTKPlugins+all">.all</a></li>
<li><a href="#module_RTKPlugins+active">.active</a></li>
</ul>
</li>
</ul>
<p><a name="module_RTKPlugins+all"></a></p>
<h3 id="meeting-plugins-all">meeting.plugins.all</h3>
All plugins accessible by the current user.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKPlugins"><code>RTKPlugins</code></a><br />
<a name="module_RTKPlugins+active"></a></p>
<h3 id="meeting-plugins-active">meeting.plugins.active</h3>
All plugins that are currently enabled in the room.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKPlugins"><code>RTKPlugins</code></a></p>
