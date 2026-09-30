---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/faq/
  description: Frequently asked questions about RealtimeKit meetings, recordings, and SDK usage.
  full_title: FAQ · Cloudflare Realtime docs
  head_html: <title>FAQ · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Frequently asked questions about RealtimeKit meetings, recordings, and SDK usage."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/faq/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/faq/index.md"><meta property="og:title" content="FAQ · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Frequently asked questions about RealtimeKit meetings, recordings, and SDK usage."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/faq/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/realtime/realtimekit/faq/#page","headline":"FAQ \u00b7 Cloudflare Realtime docs","description":"Frequently asked questions about RealtimeKit meetings, recordings, and SDK usage.","url":"https://developers.cloudflare.com/realtime/realtimekit/faq/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/faq/
  schema: 1
---
<h3 id="api-token">API token</h3>
<details class="nb-details"><summary>How can I generate a Cloudflare API token?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11631.md")
</div></details>
<h3 id="auth-tokens">Auth tokens</h3>
<details class="nb-details"><summary>How do I generate an auth token for a participant?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11632.md")
</div></details>
<details class="nb-details"><summary>How long is an auth token valid?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11633.md")
</div></details>
<details class="nb-details"><summary>Can I refresh an auth token before it expires?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11634.md")
</div></details>
<details class="nb-details"><summary>Can the auth token lifespan be configured?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11635.md")
</div></details>
<details class="nb-details"><summary>Does generating a new auth token invalidate the previous token?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11636.md")
</div></details>
<details class="nb-details"><summary>Does deleting a participant revoke all previously issued tokens?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11637.md")
</div></details>
<details class="nb-details"><summary>What happens if a participant uses an expired or invalidated auth token?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11638.md")
</div></details>
<details class="nb-details"><summary>Can a participant with a valid auth token join an inactive meeting?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11639.md")
</div></details>
<details class="nb-details"><summary>Does the SDK cache participant auth tokens?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11640.md")
</div></details>
<h3 id="meetings">Meetings</h3>
<details class="nb-details"><summary>Can I schedule meetings in advance with RealtimeKit?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11641.md")
</div></details>
<details class="nb-details"><summary>How do I prevent participants from joining a meeting after a specific date or time?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11642.md")
</div></details>
<h3 id="participants">Participants</h3>
<details class="nb-details"><summary>Can the same user join from multiple devices or browser tabs?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11643.md")
</div></details>
<details class="nb-details"><summary>How can I prevent a user from joining a meeting again?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11644.md")
</div></details>
<details class="nb-details"><summary>Can the same participant join multiple sessions of a meeting?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11645.md")
</div></details>
<details class="nb-details"><summary>Do I need to create a new participant for every session?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11646.md")
</div></details>
<details class="nb-details"><summary>What should I use for custom_participant_id?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11647.md")
</div></details>
<h3 id="presets">Presets</h3>
<details class="nb-details"><summary>Do I need a new preset for every meeting or participant?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11648.md")
</div></details>
<h3 id="client-side-sdks">Client Side SDKs</h3>
<details class="nb-details"><summary>How do I decide which SDK to select?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11649.md")
</div></details>
<h3 id="camera">Camera</h3>
<details class="nb-details"><summary>How can I set an end user's camera quality to 1080p?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11650.md")
</div></details>
<details class="nb-details"><summary>How can I set a custom frame rate for an end user's camera feed?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11651.md")
</div></details>
<h3 id="microphone">Microphone</h3>
<details class="nb-details"><summary>Why is my microphone not auto-selected when plugged in?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11652.md")
</div></details>
<h3 id="screen-share">Screen Share</h3>
<details class="nb-details"><summary>How can I set a custom frame rate for screen share?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11653.md")
</div></details>
<h3 id="chat">Chat</h3>
<details class="nb-details"><summary>I cannot send a chat message</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11654.md")
</div></details>
<h3 id="recording">Recording</h3>
<details class="nb-details"><summary>Watermark images appear broken in recordings</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11655.md")
</div></details>
<h3 id="network-access">Network access</h3>
<details class="nb-details"><summary>Which domains and ports must I allowlist when my network restricts outbound traffic?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11656.md")
</div></details>
<details class="nb-details"><summary>How can I check if my network and devices are ready for a RealtimeKit meeting?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11657.md")
</div></details>
<h3 id="demo-app">Demo App</h3>
<details class="nb-details"><summary>Can I use the Cloudflare hosted demo app or examples in my website as an iframe?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11658.md")
</div></details>
<h3 id="billing">Billing</h3>
<details class="nb-details"><summary>How are Audio/Video Participant and Audio-Only Participant minutes charged?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11659.md")
</div></details>
<details class="nb-details"><summary>How is composite recording export charged?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/11660.md")
</div></details>
