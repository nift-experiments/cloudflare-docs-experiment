---
cp9:
  canonical: https://developers.cloudflare.com/realtime/
  description: Build scalable real-time applications with Cloudflare Realtime products including RealtimeKit, SFU, and TURN.
  full_title: Overview · Cloudflare Realtime docs
  head_html: <title>Overview · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Build scalable real-time applications with Cloudflare Realtime products including RealtimeKit, SFU, and TURN."><link rel="canonical" href="https://developers.cloudflare.com/realtime/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/index.md"><meta property="og:title" content="Overview · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build scalable real-time applications with Cloudflare Realtime products including RealtimeKit, SFU, and TURN."><meta property="og:url" content="https://developers.cloudflare.com/realtime/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/realtime/#page","headline":"Overview \u00b7 Cloudflare Realtime docs","description":"Build scalable real-time applications with Cloudflare Realtime products including RealtimeKit, SFU, and TURN.","url":"https://developers.cloudflare.com/realtime/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/
  schema: 1
---
<div class="nb-description">
@markup("md", "content/.markup/bodies/466.md")
</div>
<h3 id="realtimekit">RealtimeKit</h3>
<p><a href="/realtime/realtimekit/">RealtimeKit</a> is a set of SDKs and APIs that lets you add customizable live video and voice to web or mobile applications. It is fully customisable and lets you set up in just a few lines of code.</p>
<p>It sits on top of the Realtime SFU, abstracting away the heavy lifting of media routing, peer management, and other complex WebRTC operations.</p>
<h3 id="realtime-sfu">Realtime SFU</h3>
<p>The <a href="/realtime/sfu/">Realtime SFU (Selective Forwarding Unit)</a> routes WebRTC audio, video, and DataChannels between application endpoints.</p>
<p>Use Realtime SFU when your application needs custom media routing, signaling, state, permissions, or user interfaces. Common topologies include custom calls, interactive broadcasts, AI media pipelines, cloud gaming, device control, and media processing.</p>
<p>Your application backend keeps the Realtime SFU credentials and decides which sessions can publish, subscribe, or control resources.</p>
<h3 id="turn-service">TURN Service</h3>
<p>The <a href="/realtime/turn/">TURN service</a> is a managed service that acts as a relay for WebRTC traffic. It ensures connectivity for users behind restrictive firewalls or NATs by providing a public relay point for media streams.</p>
<h2 id="choose-the-right-realtime-product">Choose the right Realtime product</h2>
<p>Use this comparison table to quickly find the right Realtime product for your needs:</p>
<table>
<thead>
<tr>
<th></th>
<th><strong>RealtimeKit</strong></th>
<th><strong>Realtime SFU</strong></th>
<th><strong>TURN Service</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Choose it when</strong></td>
<td>You want meeting SDKs, participant management, and pre-built UI components.</td>
<td>You want to compose WebRTC media and data into a custom application topology.</td>
<td>You need a relay for peer-to-peer or self-hosted WebRTC connections.</td>
</tr>
<tr>
<td><strong>Provides</strong></td>
<td>Meetings, participants, presets, stage management, and UI components.</td>
<td>Sessions, media tracks, DataChannels, and programmable publish and subscribe operations.</td>
<td>TURN allocations and relayed UDP, TCP, or TLS transport.</td>
</tr>
<tr>
<td><strong>Your application manages</strong></td>
<td>Product integration, branding, and application-specific behavior.</td>
<td>Authentication, authorization, signaling, presence, state, and track discovery.</td>
<td>Peer connections, signaling, media routing, and application state.</td>
</tr>
<tr>
<td><strong>Example outcomes</strong></td>
<td>Meetings, classrooms, webinars, and social video.</td>
<td>Custom calls, interactive broadcasts, AI pipelines, cloud gaming, device control, and media processing.</td>
<td>Connectivity through restrictive firewalls and network address translation.</td>
</tr>
<tr>
<td><strong>Pricing</strong></td>
<td>Pricing by minute <a href="https://workers.cloudflare.com/pricing#media">view details</a></td>
<td>$0.05/GB egress</td>
<td>Free when used with Realtime SFU, otherwise $0.05/GB egress</td>
</tr>
<tr>
<td><strong>Free tier</strong></td>
<td>None</td>
<td>First 1,000 GB free each month</td>
<td>First 1,000 GB free each month</td>
</tr>
</tbody>
</table>
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/467.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/468.md")
</div>
<h2 id="more-resources">More resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/472.md")
</div>
