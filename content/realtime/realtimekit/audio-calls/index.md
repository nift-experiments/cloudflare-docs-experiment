---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/audio-calls/
  description: Build audio-only experiences like voice rooms and support lines with RealtimeKit.
  full_title: Audio Only Calls · Cloudflare Realtime docs
  head_html: <title>Audio Only Calls · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Build audio-only experiences like voice rooms and support lines with RealtimeKit."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/audio-calls/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/audio-calls/index.md"><meta property="og:title" content="Audio Only Calls · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build audio-only experiences like voice rooms and support lines with RealtimeKit."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/audio-calls/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/audio-calls/#page","headline":"Audio Only Calls \u00b7 Cloudflare Realtime docs","description":"Build audio-only experiences like voice rooms and support lines with RealtimeKit.","url":"https://developers.cloudflare.com/realtime/realtimekit/audio-calls/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/audio-calls/
  schema: 1
---
<p>RealtimeKit supports voice calls, allowing you to build audio-only experiences such as audio rooms, support lines, or community hangouts.
In these meetings, participants use their microphones and hear others, but cannot use their camera. Voice meetings reduce bandwidth requirements and focus on audio communication.</p>
<h2 id="how-audio-calls-work">How Audio Calls Work</h2>
<p>A participant’s meeting experience is determined by the <strong>Preset</strong> applied to that participant.
To run a voice meeting, ensure all participants join with a Preset that has meeting type set to <code>Voice</code>.</p>
<p>For details on Presets and how to configure them, refer to <a href="/realtime/realtimekit/concepts/preset/">Preset</a>.</p>
<h2 id="pricing">Pricing</h2>
<p>When a participant joins with a <code>Voice</code> meeting type Preset, they are considered an <strong>Audio-Only Participant</strong> for billing. This is different from the billing for Audio/Video Participants.</p>
<p>For detailed pricing information, refer to <a href="/realtime/realtimekit/pricing/">Pricing</a>.</p>
<h2 id="building-audio-experiences">Building Audio Experiences</h2>
<p>You can build voice meeting experiences using either the UI Kit or the Core SDK.</p>
<h3 id="ui-kit">UI Kit</h3>
<p>UI Kit provides a pre-built meeting experience with customization options.</p>
<p>When participants join with a <code>Voice</code> meeting type Preset, UI Kit automatically renders a voice-only interface.
You can use the default meeting UI or build your own UI using UI Kit components.</p>
<p>To get started, refer to <a href="/realtime/realtimekit/ui-kit/">Build using UI Kit</a>.</p>
<h3 id="core-sdk">Core SDK</h3>
<p>Core SDK provides full control to build custom audio-only interfaces. Video-related APIs are non-functional for participants with <code>Voice</code> type Presets.</p>
<p>To get started, refer to <a href="/realtime/realtimekit/core/">Build using Core SDK</a>.</p>
