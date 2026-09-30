---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugin/
  description: ''
  full_title: RTKPlugin · Cloudflare Realtime docs
  head_html: <title>RTKPlugin · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugin/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugin/index.md"><meta property="og:title" content="RTKPlugin · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugin/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugin/#page","headline":"RTKPlugin \u00b7 Cloudflare Realtime docs","url":"https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkplugin/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/core/api-reference/rtkplugin/
  schema: 1
---
<!-- Auto Generated Below -->
<p><a name="module_RTKPlugin"></a></p>
<p>The RTKPlugin module represents a single plugin in the meeting.
A plugin can be obtained from one of the plugin arrays in <code>meeting.plugins</code>.
For example,</p>
<pre tabindex="0"><code class="language-ts">const plugin1 = meeting.plugins.active.get(pluginId);&#10;const plugin2 = meeting.plugins.all.get(pluginId);&#10;</code></pre>
<ul>
<li><a href="#module_RTKPlugin">RTKPlugin</a>
<ul>
<li><a href="#module_RTKPlugin+component">.component</a></li>
<li><a href="#module_RTKPlugin+activateForSelf">.activateForSelf()</a></li>
<li><a href="#module_RTKPlugin+deactivateForSelf">.deactivateForSelf()</a></li>
<li><a href="#module_RTKPlugin+activate">.activate()</a></li>
<li><a href="#module_RTKPlugin+deactivate">.deactivate()</a></li>
</ul>
</li>
</ul>
<p><a name="module_RTKPlugin+component"></a></p>
<h3 id="plugin-component">plugin.component</h3>
The component for this plugin, as provided in the plugin config.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKPlugin"><code>RTKPlugin</code></a><br />
<a name="module_RTKPlugin+activateForSelf"></a></p>
<h3 id="plugin-activateforself">plugin.activateForSelf()</h3>
**Kind**: instance method of [<code>RTKPlugin</code>](#module_RTKPlugin)  
<a name="module_RTKPlugin+deactivateForSelf"></a>
<h3 id="plugin-deactivateforself">plugin.deactivateForSelf()</h3>
**Kind**: instance method of [<code>RTKPlugin</code>](#module_RTKPlugin)  
<a name="module_RTKPlugin+activate"></a>
<h3 id="plugin-activate">plugin.activate()</h3>
Activate this plugin for all participants.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKPlugin"><code>RTKPlugin</code></a><br />
<a name="module_RTKPlugin+deactivate"></a></p>
<h3 id="plugin-deactivate">plugin.deactivate()</h3>
Deactivate this plugin for all participants.
<p><strong>Kind</strong>: instance method of <a href="#module_RTKPlugin"><code>RTKPlugin</code></a></p>
