---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkmeta/
  description: ''
  full_title: RTKMeta · Cloudflare Realtime docs
  head_html: <title>RTKMeta · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkmeta/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkmeta/index.md"><meta property="og:title" content="RTKMeta · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkmeta/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkmeta/#page","headline":"RTKMeta \u00b7 Cloudflare Realtime docs","url":"https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkmeta/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/core/api-reference/rtkmeta/
  schema: 1
---
<!-- Auto Generated Below -->
<p><a name="module_RTKMeta"></a></p>
<p>This consists of the metadata of the meeting, such as the room name and the title.</p>
<ul>
<li><a href="#module_RTKMeta">RTKMeta</a>
<ul>
<li><a href="#module_RTKMeta+selfActiveTab">.selfActiveTab</a></li>
<li><a href="#module_RTKMeta+broadcastTabChanges">.broadcastTabChanges</a></li>
<li><a href="#module_RTKMeta+viewType">.viewType</a></li>
<li><a href="#module_RTKMeta+meetingStartedTimestamp">.meetingStartedTimestamp</a></li>
<li><a href="#module_RTKMeta+meetingTitle">.meetingTitle</a></li>
<li><a href="#module_RTKMeta+sessionId">.sessionId</a></li>
<li><a href="#module_RTKMeta+meetingId">.meetingId</a></li>
<li><a href="#module_RTKMeta+setBroadcastTabChanges">.setBroadcastTabChanges(broadcastTabChanges)</a></li>
<li><a href="#module_RTKMeta+setSelfActiveTab">.setSelfActiveTab(spotlightTab, tabChangeSource)</a></li>
</ul>
</li>
</ul>
<p><a name="module_RTKMeta+selfActiveTab"></a></p>
<h3 id="meeting-meta-selfactivetab">meeting.meta.selfActiveTab</h3>
Represents the current active tab
<p><strong>Kind</strong>: instance property of <a href="#module_RTKMeta"><code>RTKMeta</code></a><br />
<a name="module_RTKMeta+broadcastTabChanges"></a></p>
<h3 id="meeting-meta-broadcasttabchanges">meeting.meta.broadcastTabChanges</h3>
Represents whether current user is spotlighted
<p><strong>Kind</strong>: instance property of <a href="#module_RTKMeta"><code>RTKMeta</code></a><br />
<a name="module_RTKMeta+viewType"></a></p>
<h3 id="meeting-meta-viewtype">meeting.meta.viewType</h3>
The `viewType` tells the type of the meeting
possible values are: GROUP_CALL| LIVESTREAM | CHAT | AUDIO_ROOM
<p><strong>Kind</strong>: instance property of <a href="#module_RTKMeta"><code>RTKMeta</code></a><br />
<a name="module_RTKMeta+meetingStartedTimestamp"></a></p>
<h3 id="meeting-meta-meetingstartedtimestamp">meeting.meta.meetingStartedTimestamp</h3>
The timestamp of the time when the meeting started.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKMeta"><code>RTKMeta</code></a><br />
<a name="module_RTKMeta+meetingTitle"></a></p>
<h3 id="meeting-meta-meetingtitle">meeting.meta.meetingTitle</h3>
The title of the meeting.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKMeta"><code>RTKMeta</code></a><br />
<a name="module_RTKMeta+sessionId"></a></p>
<h3 id="meeting-meta-sessionid">meeting.meta.sessionId</h3>
(Experimental) The sessionId this meeting object is part of.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKMeta"><code>RTKMeta</code></a><br />
<a name="module_RTKMeta+meetingId"></a></p>
<h3 id="meeting-meta-meetingid">meeting.meta.meetingId</h3>
The room name of the meeting.
<p><strong>Kind</strong>: instance property of <a href="#module_RTKMeta"><code>RTKMeta</code></a><br />
<a name="module_RTKMeta+setBroadcastTabChanges"></a></p>
<h3 id="meeting-meta-setbroadcasttabchanges-broadcasttabchanges">meeting.meta.setBroadcastTabChanges(broadcastTabChanges)</h3>
Sets current user as broadcasting tab changes
<p><strong>Kind</strong>: instance method of <a href="#module_RTKMeta"><code>RTKMeta</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>broadcastTabChanges</td>
<td><code>boolean</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKMeta+setSelfActiveTab"></a></p>
<h3 id="meeting-meta-setselfactivetab-spotlighttab-tabchangesource">meeting.meta.setSelfActiveTab(spotlightTab, tabChangeSource)</h3>
Sets current active tab for user
<p><strong>Kind</strong>: instance method of <a href="#module_RTKMeta"><code>RTKMeta</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>spotlightTab</td>
<td><code>ActiveTab</code></td>
</tr>
<tr>
<td>tabChangeSource</td>
<td><code>TabChangeSource</code></td>
</tr>
</tbody>
</table>
