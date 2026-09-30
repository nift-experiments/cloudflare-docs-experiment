---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkstage/
  description: ''
  full_title: RTKStage · Cloudflare Realtime docs
  head_html: <title>RTKStage · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkstage/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkstage/index.md"><meta property="og:title" content="RTKStage · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkstage/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkstage/#page","headline":"RTKStage \u00b7 Cloudflare Realtime docs","url":"https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkstage/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/core/api-reference/rtkstage/
  schema: 1
---
<!-- Auto Generated Below -->
<p><a name="module_RTKStage"></a></p>
<p>The RTKStage module represents a class to mange the RTKStage of the meeting
RTKStage refers to a virtual area, where participants stream are visible to other participants.
When a participant is off stage, they are not producing media
but only consuming media from participants who are on RTKStage</p>
<ul>
<li><a href="#module_RTKStage">RTKStage</a>
<ul>
<li><a href="#module_RTKStage+peerId">.peerId</a></li>
<li><a href="#module_RTKStage+getAccessRequests">.getAccessRequests()</a></li>
<li><a href="#module_RTKStage+requestAccess">.requestAccess()</a></li>
<li><a href="#module_RTKStage+cancelRequestAccess">.cancelRequestAccess()</a></li>
<li><a href="#module_RTKStage+grantAccess">.grantAccess()</a></li>
<li><a href="#module_RTKStage+denyAccess">.denyAccess()</a></li>
<li><a href="#module_RTKStage+join">.join()</a></li>
<li><a href="#module_RTKStage+leave">.leave()</a></li>
<li><a href="#module_RTKStage+kick">.kick(userIds)</a></li>
</ul>
</li>
</ul>
<p><a name="module_RTKStage+peerId"></a></p>
<h3 id="meeting-stage-peerid">meeting.stage.peerId</h3>
Returns the peerId of the current user
<p><strong>Kind</strong>: instance property of <a href="#module_RTKStage"><code>RTKStage</code></a><br />
<a name="module_RTKStage+getAccessRequests"></a></p>
<h3 id="meeting-stage-getaccessrequests">meeting.stage.getAccessRequests()</h3>
Method to fetch all RTKStage access requests from viewers
<p><strong>Kind</strong>: instance method of <a href="#module_RTKStage"><code>RTKStage</code></a><br />
<a name="module_RTKStage+requestAccess"></a></p>
<h3 id="meeting-stage-requestaccess">meeting.stage.requestAccess()</h3>
Method to send a request to privileged users to join the stage
<p><strong>Kind</strong>: instance method of <a href="#module_RTKStage"><code>RTKStage</code></a><br />
<a name="module_RTKStage+cancelRequestAccess"></a></p>
<h3 id="meeting-stage-cancelrequestaccess">meeting.stage.cancelRequestAccess()</h3>
Method to cancel a previous RTKStage join request
<p><strong>Kind</strong>: instance method of <a href="#module_RTKStage"><code>RTKStage</code></a><br />
<a name="module_RTKStage+grantAccess"></a></p>
<h3 id="meeting-stage-grantaccess">meeting.stage.grantAccess()</h3>
Method to grant access to RTKStage.
	This can be in response to a RTKStage Join request but it can be called on other users as well
<p><code>permissions.acceptStageRequests</code> privilege required</p>
<p><strong>Kind</strong>: instance method of <a href="#module_RTKStage"><code>RTKStage</code></a><br />
<a name="module_RTKStage+denyAccess"></a></p>
<h3 id="meeting-stage-denyaccess">meeting.stage.denyAccess()</h3>
Method to deny access to RTKStage.
This should be called in response to a RTKStage Join request
<p><strong>Kind</strong>: instance method of <a href="#module_RTKStage"><code>RTKStage</code></a><br />
<a name="module_RTKStage+join"></a></p>
<h3 id="meeting-stage-join">meeting.stage.join()</h3>
Method to join the stage
Users either need to have the permission in the preset or must be accepted by a privileged
user to call this method
<p><strong>Kind</strong>: instance method of <a href="#module_RTKStage"><code>RTKStage</code></a><br />
<a name="module_RTKStage+leave"></a></p>
<h3 id="meeting-stage-leave">meeting.stage.leave()</h3>
Method to leave the stage
Users must either be on the stage already or be accepted to join the stage
to call this method
<p><strong>Kind</strong>: instance method of <a href="#module_RTKStage"><code>RTKStage</code></a><br />
<a name="module_RTKStage+kick"></a></p>
<h3 id="meeting-stage-kick-userids">meeting.stage.kick(userIds)</h3>
Method to kick a user off the stage
<p><code>permissions.acceptStageRequests</code> privilege required</p>
<p><strong>Kind</strong>: instance method of <a href="#module_RTKStage"><code>RTKStage</code></a></p>
<table>
<thead>
<tr>
<th>Param</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr>
<td>userIds</td>
<td><code>Array.&lt;string&gt;</code></td>
</tr>
</tbody>
</table>
