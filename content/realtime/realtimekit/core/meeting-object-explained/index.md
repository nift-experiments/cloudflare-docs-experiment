---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/core/meeting-object-explained/
  description: Explore the RealtimeKit meeting object and its namespaces for participants, chat, polls, and media.
  full_title: Meeting Object Explained · Cloudflare Realtime docs
  head_html: <title>Meeting Object Explained · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Explore the RealtimeKit meeting object and its namespaces for participants, chat, polls, and media."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/core/meeting-object-explained/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/core/meeting-object-explained/index.md"><meta property="og:title" content="Meeting Object Explained · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Explore the RealtimeKit meeting object and its namespaces for participants, chat, polls, and media."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/core/meeting-object-explained/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/realtime/realtimekit/core/meeting-object-explained/#page","headline":"Meeting Object Explained \u00b7 Cloudflare Realtime docs","description":"Explore the RealtimeKit meeting object and its namespaces for participants, chat, polls, and media.","url":"https://developers.cloudflare.com/realtime/realtimekit/core/meeting-object-explained/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/core/meeting-object-explained/
  schema: 1
---
<p>The meeting object is the core interface for interacting with a RealtimeKit session. It provides access to participants, local user controls, chat, polls, plugins, and more. This object is returned when you initialize the SDK.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="prerequisites">Prerequisites</h3>
@markup("md", "content/.markup/bodies/12029.md")
</aside>
<p>This guide covers the core namespaces on the meeting object along with the most commonly used properties, methods, and events. Individual namespace references have been linked for more details.</p>
<div class="nb-interactive-component" data-cf-component="RTKSDKSelector"></div>
<h2 id="meeting-object-structure">Meeting Object Structure</h2>
<p>The meeting object contains several properties that organize different aspects of the meeting:</p>
<h3 id="self-local-participant">Self/Local Participant</h3>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12030.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12031.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12032.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12033.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12034.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12035.md")
</div>
<h2 id="remote-participants">Remote participants</h2>
<h3 id="meeting-participants-all-remote-participants"><code>meeting.participants</code> - All Remote Participants</h3>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12036.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12037.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12038.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12039.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12040.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12041.md")
</div>
<h2 id="meeting-metadata">Meeting metadata</h2>
<h3 id="meeting-meta-meeting-metadata"><code>meeting.meta</code> - Meeting Metadata</h3>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12042.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12043.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12044.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12045.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12046.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12047.md")
</div>
<h2 id="chat">Chat</h2>
<h3 id="meeting-chat-chat-messages"><code>meeting.chat</code> - Chat Messages</h3>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12048.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12049.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12050.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12051.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12052.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12053.md")
</div>
<h2 id="polls">Polls</h2>
<h3 id="meeting-polls-polls"><code>meeting.polls</code> - Polls</h3>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12054.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12055.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12056.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12057.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12058.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12059.md")
</div>
<h2 id="plugins">Plugins</h2>
<h3 id="meeting-plugins-plugins"><code>meeting.plugins</code> - Plugins</h3>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12060.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12061.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12062.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12063.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12064.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12065.md")
</div>
<h2 id="ai-features">AI features</h2>
<h3 id="meeting-ai-ai-features"><code>meeting.ai</code> - AI Features</h3>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12066.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12067.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12068.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12069.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12070.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12071.md")
</div>
<h2 id="methods">Methods</h2>
<p>Join or leave a meeting room:</p>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12072.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12073.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12074.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12075.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12076.md")
</div>
<div class="nb-interactive-component" data-cf-component="RTKCodeSnippet">
@markup("md", "content/.markup/bodies/12077.md")
</div>
<h2 id="understanding-ids">Understanding IDs</h2>
<p>RealtimeKit uses two types of identifiers for participants:</p>
<ul>
<li>
<p><strong>Session ID (<code>id</code>)</strong>: Unique identifier for each connection to a meeting. Changes every time a participant joins a new session. On Web platforms, this is called &quot;Peer ID&quot; and stored in <code>meeting.self.id</code> or <code>participant.id</code>. On mobile platforms, this is called &quot;Participant ID&quot; and stored in <code>meeting.localUser.id</code> or <code>participant.id</code>.</p>
</li>
<li>
<p><strong>User ID (<code>userId</code>)</strong>: Persistent identifier for a participant across multiple sessions. Remains the same when a user reconnects. This is stored in <code>meeting.self.userId</code> (Web) or <code>meeting.localUser.userId</code> (Mobile), and <code>participant.userId</code> for remote participants.</p>
</li>
</ul>
<p><strong>When to use each:</strong></p>
<ul>
<li>Use <code>userId</code> when you need to track the same user across different sessions or reconnections (for example, saving user preferences or permissions)</li>
<li>Use <code>id</code> when working with the current session's connections (for example, managing active video streams or real-time participant states)</li>
</ul>
<h2 id="best-practices">Best Practices</h2>
<ul>
<li>
<p><strong>Listen to events instead of polling</strong>: The meeting object emits events when state changes occur. Subscribe to these events rather than continuously checking property values.</p>
</li>
<li>
<p><strong>Work with participant collections</strong>: On Web platforms, use <code>toArray()</code> to convert participant maps to arrays. On mobile platforms, participant collections are already lists that you can iterate through directly.</p>
</li>
<li>
<p><strong>Check connection state</strong>: Always check <code>roomJoined</code> (or <code>meeting.localUser.roomJoined</code> on mobile) before accessing properties or calling methods that require an active session.</p>
</li>
<li>
<p><strong>Handle errors gracefully</strong>: Many methods accept error callbacks. Always implement proper error handling to provide a good user experience.</p>
</li>
</ul>
<h2 id="next-steps">Next Steps</h2>
<p>Now that you understand the meeting object structure, you can use it to build custom meeting experiences. The UI Kit components internally use this same meeting object to provide ready-to-use interfaces. In the next guide, we'll show you how to combine UI Kit components with direct meeting object access to create your own custom UI.</p>
