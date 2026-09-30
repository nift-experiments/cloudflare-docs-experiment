---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/pricing/
  description: RealtimeKit pricing for audio, video, recording, and transcription features.
  full_title: Pricing · Cloudflare Realtime docs
  head_html: <title>Pricing · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="RealtimeKit pricing for audio, video, recording, and transcription features."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/pricing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/pricing/index.md"><meta property="og:title" content="Pricing · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="RealtimeKit pricing for audio, video, recording, and transcription features."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/pricing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Content"><meta name="algolia_content_type" content="Content"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/pricing/#page","headline":"Pricing \u00b7 Cloudflare Realtime docs","description":"RealtimeKit pricing for audio, video, recording, and transcription features.","url":"https://developers.cloudflare.com/realtime/realtimekit/pricing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/pricing/
  schema: 1
---
<p>RealtimeKit usage is charged according to the pricing model below:</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11615.md")
</aside>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Price</th>
</tr>
</thead>
<tbody>
<tr>
<td>Audio/Video Participant</td>
<td>$0.002 / minute</td>
</tr>
<tr>
<td>Audio-Only Participant</td>
<td>$0.0005 / minute</td>
</tr>
<tr>
<td>Export (recording, RTMP or HLS streaming)</td>
<td>$0.010 / minute</td>
</tr>
<tr>
<td>Export (recording, RTMP or HLS streaming, audio only)</td>
<td>$0.003 / minute</td>
</tr>
<tr>
<td>Export (Raw RTP) into R2</td>
<td>$0.0005 / minute</td>
</tr>
<tr>
<td>Transcription (Real-time)</td>
<td>Standard model pricing via Workers AI</td>
</tr>
</tbody>
</table>
<p>Whether a participant is an audio-only participant or an audio/video participant is determined by the <code>Meeting Type</code> of their <a href="/realtime/realtimekit/concepts/preset/">preset</a>.</p>
