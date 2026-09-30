---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/
  description: Access participant data, display videos, and handle events for remote participants in RealtimeKit.
  full_title: Remote Participants · Cloudflare Realtime docs
  head_html: <title>Remote Participants · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Access participant data, display videos, and handle events for remote participants in RealtimeKit."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/index.md"><meta property="og:title" content="Remote Participants · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Access participant data, display videos, and handle events for remote participants in RealtimeKit."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/#page","headline":"Remote Participants \u00b7 Cloudflare Realtime docs","description":"Access participant data, display videos, and handle events for remote participants in RealtimeKit.","url":"https://developers.cloudflare.com/realtime/realtimekit/core/remote-participants/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/core/remote-participants/
  schema: 1
---
<p>This guide explains how to access participant data, display videos, handle events, and manage participant permissions in your RealtimeKit meetings.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="prerequisites">Prerequisites</h3>
@markup("md", "content/.markup/bodies/12525.md")
</aside>
<div class="nb-interactive-component" data-cf-component="RTKSDKSelector"></div>
<p>The participant object contains all information related to a particular participants, including information about the grid and each participants media streams, name, and state variables. It is accessible via <code>meeting.participants</code>.</p>
<h3 id="properties">Properties</h3>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12526.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12527.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12528.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12529.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12530.md")
</div>
<h3 id="access-participant-properties">Access participant properties</h3>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12531.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12532.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12533.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12534.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12535.md")
</div>
<h3 id="access-participant-object">Access participant object</h3>
<p>You can fetch a participant from the <a href="#participant-maps">participant maps</a>.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12536.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12537.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12538.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12539.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12540.md")
</div>
<h2 id="participant-maps">Participant Maps</h2>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12541.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12542.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12543.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12544.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12545.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12546.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12547.md")
</div>
<h2 id="view-modes">View Modes</h2>
<p>The view mode indicates whether participants are populated in <code>ACTIVE_GRID</code> mode or <code>PAGINATED</code> mode.</p>
<ul>
<li><strong><code>ACTIVE_GRID</code> mode</strong> - Participants are automatically replaced in <code>meeting.participants.active</code> based on who is speaking or who has their video turned on</li>
<li><strong><code>PAGINATED</code> mode</strong> - Participants in <code>meeting.participants.active</code> are fixed. Use <code>setPage()</code> to change the active participants</li>
</ul>
<h3 id="set-view-mode">Set view mode</h3>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12548.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12549.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12550.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12551.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12552.md")
</div>
<h3 id="set-page-in-paginated-mode">Set page in paginated mode</h3>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12553.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12554.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12555.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12556.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12557.md")
</div>
<h3 id="monitor-view-mode">Monitor view mode</h3>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12558.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12559.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12560.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12561.md")
</div>
<h2 id="host-controls">Host Controls</h2>
<p>The participant object allows the host several controls. These can be selected while creating the host <a href="/api/resources/realtime_kit/subresources/presets/methods/create/">preset</a>.</p>
<h3 id="media-controls">Media controls</h3>
<p>With the correct permissions, the host can disable media for remote participants.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12562.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12563.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12564.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12565.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12566.md")
</div>
<h3 id="waiting-room-controls">Waiting room controls</h3>
<p>The waiting room allows the host to control which users can join your meeting and when. They can either choose to accept or reject the request.</p>
<p>You can also automate this flow so that users join the meeting automatically when the host joins the meeting, using <a href="/api/resources/realtime_kit/subresources/presets/methods/create/">presets</a>.</p>
<h4 id="accept-waiting-room-request">Accept waiting room request</h4>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12567.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12568.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12569.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12570.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12571.md")
</div>
<h4 id="reject-waiting-room-request">Reject waiting room request</h4>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12572.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12573.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12574.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12575.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12576.md")
</div>
<h3 id="pin-participants">Pin participants</h3>
<p>The host can choose to pin or unpin participants to the grid.</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12577.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12578.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12579.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12580.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12581.md")
</div>
<h3 id="update-participant-permissions">Update participant permissions</h3>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12582.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12583.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12584.md")
</div>
<h2 id="display-participant-videos">Display participant videos</h2>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12585.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12586.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12587.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12588.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12589.md")
</div>
