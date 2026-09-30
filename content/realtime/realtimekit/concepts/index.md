---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/concepts/
  description: Core concepts and terminology for RealtimeKit including apps, meetings, participants, and presets.
  full_title: Concepts · Cloudflare Realtime docs
  head_html: <title>Concepts · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Core concepts and terminology for RealtimeKit including apps, meetings, participants, and presets."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/concepts/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/concepts/index.md"><meta property="og:title" content="Concepts · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Core concepts and terminology for RealtimeKit including apps, meetings, participants, and presets."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/concepts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/realtime/realtimekit/concepts/#page","headline":"Concepts \u00b7 Cloudflare Realtime docs","description":"Core concepts and terminology for RealtimeKit including apps, meetings, participants, and presets.","url":"https://developers.cloudflare.com/realtime/realtimekit/concepts/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/concepts/
  schema: 1
---
<p>This page outlines the core concepts and key terminology used throughout RealtimeKit.</p>
<h3 id="app">App</h3>
<p>An App represents a <strong>workspace</strong> within RealtimeKit. It groups together your meetings, participants, presets, recordings, and other configuration under an isolated namespace.</p>
<p>Treat each App like an environment-specific container—most teams create one App for staging and another for production to avoid mixing data.</p>
<h3 id="meeting">Meeting</h3>
<p>A Meeting is a <strong>re-usable virtual room</strong> that you can join anytime.
Every time participants join a meeting, a new <a href="/realtime/realtimekit/concepts#session">session</a> is created.</p>
<p>A session is marked <code>ENDED</code> shortly after the last participant leaves. A meeting can have only <strong>one active session</strong> at any given time.</p>
<p>For more information about meetings, refer to <a href="/realtime/realtimekit/concepts#meeting">Meetings</a>.</p>
<h3 id="session">Session</h3>
<p>A Session is the <strong>live instance of a meeting</strong>. It is created when the first participant joins a meeting and ends shortly after the last participant leaves.</p>
<p>Each session is independent, with its own participants, chat, and recordings. It also inherits the configurations set while creating the meeting - <code>record on start</code>, <code>persist_chat</code>, and more.</p>
<p>Example - A recurring “Weekly Standup” <strong>meeting will generate a new session</strong> every time participants join.</p>
<h3 id="participant">Participant</h3>
<p>A <strong>Participant</strong> is created when you add a user to a meeting via the <a href="/api/resources/realtime_kit/subresources/meetings/methods/add_participant/">Add participant API</a>. This API call returns a unique <code>authToken</code> that the client-side SDK uses to join the session and authenticate the user.</p>
<blockquote>
<p><strong>Note:</strong> Please do not re-use auth tokens for participants.</p>
</blockquote>
<p>For more information about participants, refer to <a href="/realtime/realtimekit/concepts/participant/">Participants</a>.</p>
<h3 id="preset">Preset</h3>
<p>A Preset is a reusable set of permissions that defines the experience and the UI’s look and feel for a participant.</p>
<p>Created at the App level, it can be applied to any participant across any meeting in that App.</p>
<p>It also defines the meeting type a user joins—video call, audio call, or webinar. Participants in the same meeting can use different presets to create flexible roles.
Example: In a large ed-tech class:</p>
<ul>
<li><strong>Teacher</strong> will join with a <code>webinar-host</code> preset, allowing them to share their media and providing host controls.</li>
<li><strong>Students</strong> will join with a <code>webinar-participant</code> preset, which restricts them from sharing media but allows them to use features like chat.</li>
<li><strong>Teaching assistant</strong> will join with a <code>group-call-host</code> preset, enabling them to share their media but not have full control.</li>
</ul>
<p>It also lets you customize the UI’s look and feel, including colors and themes, so the experience matches your application's branding.</p>
<p>For more information about presets, refer to <a href="/realtime/realtimekit/concepts/preset/">Presets</a>.</p>
