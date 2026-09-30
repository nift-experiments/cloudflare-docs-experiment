---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkconnectedmeetings/
  description: ''
  full_title: RTKConnectedMeetings · Cloudflare Realtime docs
  head_html: <title>RTKConnectedMeetings · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkconnectedmeetings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkconnectedmeetings/index.md"><meta property="og:title" content="RTKConnectedMeetings · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkconnectedmeetings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkconnectedmeetings/#page","headline":"RTKConnectedMeetings \u00b7 Cloudflare Realtime docs","url":"https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkconnectedmeetings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/core/api-reference/rtkconnectedmeetings/
  schema: 1
---
<!-- Auto Generated Below -->
<p><a name="module_RTKConnectedMeetings"></a></p>
<p>This consists of the methods to facilitate connected meetings</p>
<ul>
<li><a href="#module_RTKConnectedMeetings">RTKConnectedMeetings</a>
<ul>
<li><a href="#module_RTKConnectedMeetings+getConnectedMeetings">.getConnectedMeetings()</a></li>
<li><a href="#module_RTKConnectedMeetings+createMeetings">.createMeetings(request)</a></li>
<li><a href="#module_RTKConnectedMeetings+updateMeetings">.updateMeetings(request)</a></li>
<li><a href="#module_RTKConnectedMeetings+deleteMeetings">.deleteMeetings(meetingIds)</a></li>
<li><a href="#module_RTKConnectedMeetings+moveParticipants">.moveParticipants(sourceMeetingId, destinationMeetingId, participantIds)</a></li>
<li><a href="#module_RTKConnectedMeetings+moveParticipantsWithCustomPreset">.moveParticipantsWithCustomPreset(sourceMeetingId, destinationMeetingId, participants)</a></li>
</ul>
</li>
</ul>
<p><a name="module_RTKConnectedMeetings+getConnectedMeetings"></a></p>
<h3 id="meeting-connectedmeetings-getconnectedmeetings">meeting.connectedMeetings.getConnectedMeetings()</h3>
get connected meeting state
<p><strong>Kind</strong>: instance method of <a href="#module_RTKConnectedMeetings"><code>RTKConnectedMeetings</code></a><br />
<a name="module_RTKConnectedMeetings+createMeetings"></a></p>
<h3 id="meeting-connectedmeetings-createmeetings-request">meeting.connectedMeetings.createMeetings(request)</h3>
create connected meetings
<p><strong>Kind</strong>: instance method of <a href="#module_RTKConnectedMeetings"><code>RTKConnectedMeetings</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>request</td>
<td><code>Array.&lt;{title: string}&gt;</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKConnectedMeetings+updateMeetings"></a></p>
<h3 id="meeting-connectedmeetings-updatemeetings-request">meeting.connectedMeetings.updateMeetings(request)</h3>
update meeting title
<p><strong>Kind</strong>: instance method of <a href="#module_RTKConnectedMeetings"><code>RTKConnectedMeetings</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>request</td>
<td><code>Array.&lt;{id: string, title: string}&gt;</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKConnectedMeetings+deleteMeetings"></a></p>
<h3 id="meeting-connectedmeetings-deletemeetings-meetingids">meeting.connectedMeetings.deleteMeetings(meetingIds)</h3>
delete connected meetings
<p><strong>Kind</strong>: instance method of <a href="#module_RTKConnectedMeetings"><code>RTKConnectedMeetings</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>meetingIds</td>
<td><code>Array.&lt;string&gt;</code></td>
</tr>
</tbody>
</table>
<p><a name="module_RTKConnectedMeetings+moveParticipants"></a></p>
<h3 id="meeting-connectedmeetings-moveparticipants-sourcemeetingid-destinationmeetingid-participantids">meeting.connectedMeetings.moveParticipants(sourceMeetingId, destinationMeetingId, participantIds)</h3>
Trigger event to move participants
<p><strong>Kind</strong>: instance method of <a href="#module_RTKConnectedMeetings"><code>RTKConnectedMeetings</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>sourceMeetingId</td>
<td><code>string</code></td>
<td>id of source meeting</td>
</tr>
<tr>
<td>destinationMeetingId</td>
<td><code>string</code></td>
<td>id of destination meeting</td>
</tr>
<tr>
<td>participantIds</td>
<td><code>Array.&lt;string&gt;</code></td>
<td>list of id of the participants</td>
</tr>
</tbody>
</table>
<p><a name="module_RTKConnectedMeetings+moveParticipantsWithCustomPreset"></a></p>
<h3 id="meeting-connectedmeetings-moveparticipantswithcustompreset-sourcemeetingid-destinationmeetingid-participants">meeting.connectedMeetings.moveParticipantsWithCustomPreset(sourceMeetingId, destinationMeetingId, participants)</h3>
Trigger event to move participants with custom preset
<p><strong>Kind</strong>: instance method of <a href="#module_RTKConnectedMeetings"><code>RTKConnectedMeetings</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>sourceMeetingId</td>
<td><code>string</code></td>
<td>id of source meeting</td>
</tr>
<tr>
<td>destinationMeetingId</td>
<td><code>string</code></td>
<td>id of destination meeting</td>
</tr>
<tr>
<td>participants</td>
<td><code>Array.&lt;{id: string, presetId: string}&gt;</code></td>
<td></td>
</tr>
</tbody>
</table>
