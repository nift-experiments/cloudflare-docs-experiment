---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/core/manage-participants-in-a-session/
  description: Use RealtimeKit host controls to mute, pin, or remove participants in a live session.
  full_title: Manage Participants in a Session · Cloudflare Realtime docs
  head_html: <title>Manage Participants in a Session · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Use RealtimeKit host controls to mute, pin, or remove participants in a live session."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/core/manage-participants-in-a-session/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/core/manage-participants-in-a-session/index.md"><meta property="og:title" content="Manage Participants in a Session · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use RealtimeKit host controls to mute, pin, or remove participants in a live session."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/core/manage-participants-in-a-session/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/core/manage-participants-in-a-session/#page","headline":"Manage Participants in a Session \u00b7 Cloudflare Realtime docs","description":"Use RealtimeKit host controls to mute, pin, or remove participants in a live session.","url":"https://developers.cloudflare.com/realtime/realtimekit/core/manage-participants-in-a-session/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/core/manage-participants-in-a-session/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="prerequisites">Prerequisites</h3>
@markup("md", "content/.markup/bodies/12112.md")
</aside>
<p>Use RealtimeKit host controls to manage other participants in a live session. You can mute audio or video, pin a participant, or remove participants from the session.
These actions require specific host control permissions enabled in the local participant's <a href="/realtime/realtimekit/concepts/preset/">Preset</a>.
Before you show UI controls or call these methods, verify that the local participant has the necessary permissions.
In this guide, the <strong>local participant</strong> refers to the user performing the actions.</p>
<div class="nb-interactive-component" data-cf-component="RTKSDKSelector"></div>
<h3 id="select-a-remote-participant">Select a remote participant</h3>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12113.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12114.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12115.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12116.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12117.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12118.md")
</div>
<h2 id="mute-audio">Mute audio</h2>
<p>Mute audio of participants when you need to manage background noise, moderate a classroom or webinar, or prevent interruptions during a session.
This action requires the <strong>Mute Audio</strong> (<code>disable_participant_audio</code>) host control permission enabled in the local participant's preset.</p>
<h3 id="mute-a-participant">Mute a participant</h3>
<p>To mute a specific participant's audio:</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12120.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12122.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12124.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12125.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12126.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12127.md")
</div>
<h3 id="mute-all-participants">Mute all participants</h3>
<p>This affects all participants, including the local participant. To mute audio for all participants in the session:</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12129.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12131.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12133.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12134.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12135.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12136.md")
</div>
<h2 id="disable-video">Disable video</h2>
<p>Disable video of participants when you need to moderate a session, enforce privacy, or prevent unwanted video during a classroom or webinar.
This action requires the <strong>Mute Video</strong> (<code>disable_participant_video</code>) host control permission enabled in the local participant's preset.</p>
<h3 id="disable-video-for-a-participant">Disable video for a participant</h3>
<p>To disable a specific participant's video:</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12138.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12140.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12142.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12143.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12144.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12145.md")
</div>
<h3 id="disable-video-for-all-participants">Disable video for all participants</h3>
<p>This affects all participants, including the local participant. To disable video for all participants in the session:</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12147.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12149.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12151.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12152.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12153.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12154.md")
</div>
<h2 id="pin-participants">Pin participants</h2>
<p>Pin a participant to highlight them, such as a webinar presenter or classroom teacher. This is a session-wide action. All participants will see the pinned participant as the focus.
This action requires the <strong>Pin Participant</strong> (<code>pin_participant</code>) host control permission enabled in the local participant's preset.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12111.md")
</aside>
<h3 id="pin-a-participant">Pin a participant</h3>
<p>To pin a participant in a session:</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12156.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12158.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12160.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12161.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12162.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12163.md")
</div>
<h3 id="unpin-a-participant">Unpin a participant</h3>
<p>Unpin a participant when you need to undo the highlight and return the session to a standard grid or active speaker view.
To unpin a pinned participant in a session:</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12165.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12167.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12169.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12170.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12171.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12172.md")
</div>
<h2 id="remove-participants">Remove participants</h2>
<p>Remove participants from the session when you need to moderate disruptive behavior or enforce session rules.
This action requires the <strong>Kick Participants</strong> (<code>kick_participant</code>) host control permission enabled in the local participant's preset.</p>
<h3 id="remove-a-participant">Remove a participant</h3>
<p>To remove a specific participant from the session:</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12174.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12176.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12178.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12179.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12180.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12181.md")
</div>
<h3 id="remove-all-participants">Remove all participants</h3>
<p>This removes everyone from the session, including the local participant. This ends the session for everyone.</p>
<p>For a complete end-a-session flow, refer to <a href="/realtime/realtimekit/core/end-a-session/">End a session</a>.</p>
<p>To remove all participants from the session:</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12183.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12185.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@input("content/.markup/bodies/12187.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12188.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12189.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12190.md")
</div>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Review how presets control permissions in <a href="/realtime/realtimekit/concepts/preset/">Preset</a>.</li>
<li>Review error handling details in <a href="/realtime/realtimekit/core/error-codes/">Error Codes</a>.</li>
</ul>
