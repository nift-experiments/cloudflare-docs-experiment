---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/concepts/session-lifecycle/
  description: Understand the lifecycle of a peer in a RealtimeKit session from setup to disconnect.
  full_title: Session Lifecycle · Cloudflare Realtime docs
  head_html: <title>Session Lifecycle · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand the lifecycle of a peer in a RealtimeKit session from setup to disconnect."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/concepts/session-lifecycle/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/concepts/session-lifecycle/index.md"><meta property="og:title" content="Session Lifecycle · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand the lifecycle of a peer in a RealtimeKit session from setup to disconnect."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/concepts/session-lifecycle/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/realtime/realtimekit/concepts/session-lifecycle/#page","headline":"Session Lifecycle \u00b7 Cloudflare Realtime docs","description":"Understand the lifecycle of a peer in a RealtimeKit session from setup to disconnect.","url":"https://developers.cloudflare.com/realtime/realtimekit/concepts/session-lifecycle/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/concepts/session-lifecycle/
  schema: 1
---
<p>The <a href="/realtime/realtimekit/concepts/meeting/#session">Session Guide</a> explains what a session is and how to initialize one.
In this guide we will talk about what happens to a peer as they move through a session, when do they go to the setup screen, waitlist screen, ended screen or any other screen, and how you can hook into these events to perform custom actions.</p>
<h3 id="lifecycle-of-a-peer-in-a-session">Lifecycle of a Peer in a Session</h3>
<p><img src="/assets/upstream/images/realtime/realtimekit/peer-lifecycle.svg" alt="Peer Lifecycle In a Session" /></p>
<p>Here’s how the peer lifecycle works:</p>
<ol>
<li><strong>Initialization state</strong>: When the SDK is initialized, the peer first sees a Setup Screen, where they can preview their audio and video before joining.</li>
<li><strong>Join intent</strong>: When the peer decides to join, one of two things happens:
<ul>
<li>If waitlisting is enabled, they are moved to a Waitlist and see a Waitlist screen.</li>
<li>If not waitlisted, they join the session and see the main Meeting screen (Stage), where they can interact with others.</li>
</ul>
</li>
<li><strong>During the session</strong>: The peer can see and interact with others in the main Meeting screen (Stage).</li>
<li><strong>Session transitions</strong>:
<ul>
<li>If the peer is rejected from the waitlist, they see a dedicated Rejected screen.</li>
<li>If the peer is kicked out, they see an Ended screen and the session ends for them.</li>
<li>If the peer leaves voluntarily, or if the meeting ends, they see an Ended screen, and the session ends for them.</li>
</ul>
</li>
</ol>
<p>Each of these screens is built with UI Kit components, which you can fully customize to match your app’s design and requirements.</p>
<p>The UI Kit SDKs automatically handle which notifications or screens to show at each state, so you don’t have to manage these transitions manually.</p>
<p>In upcoming pages, we will see how to hook into these events to perform custom actions and to build your own custom meeting experience.</p>
