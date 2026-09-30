---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2026-05-29-websocket-adapter-auto-reconnect/
  description: New updates and improvements at Cloudflare.
  full_title: Cloudflare's Realtime WebSocket adapter now auto-reconnects and buffers WebRTC media · Changelog
  head_html: <title>Cloudflare&#x27;s Realtime WebSocket adapter now auto-reconnects and buffers WebRTC media · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2026-05-29-websocket-adapter-auto-reconnect/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Cloudflare&#x27;s Realtime WebSocket adapter now auto-reconnects and buffers WebRTC media · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2026-05-29-websocket-adapter-auto-reconnect/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-29-websocket-adapter-auto-reconnect/#page","headline":"Cloudflare's Realtime WebSocket adapter now auto-reconnects and buffers WebRTC media \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-05-29-websocket-adapter-auto-reconnect/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2026-05-29-websocket-adapter-auto-reconnect/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 29, 2026</time><h2 id="post-title">Cloudflare's Realtime WebSocket adapter now auto-reconnects and buffers WebRTC media</h2>
<div class="changelog-badges"><span>realtime</span></div><div class="changelog-body"><p><a href="/realtime/sfu/">Cloudflare Realtime SFU</a> is a <a href="/realtime/sfu/calls-vs-sfus/">WebRTC Selective Forwarding Unit that runs on Cloudflare's global network</a>, so you can route live audio, video, and data between WebRTC clients around the world without managing SFU infrastructure or regions.</p>
<p>When you use the <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/">WebSocket adapter</a> to stream WebRTC media to a WebSocket endpoint, the adapter now auto-reconnects and buffers audio and video after brief endpoint disconnects or restarts.</p>
<h4 id="streaming-webrtc-media-to-websocket-endpoints">Streaming WebRTC media to WebSocket endpoints</h4>
<p>Many teams also use Realtime SFU as the media layer for backend applications, such as transcription, recording, note-taking, and agentic media-processing services. These systems often need to consume live WebRTC audio or video from the SFU in backend infrastructure, including <a href="/durable-objects/">Durable Objects</a>, <a href="/workers/">Workers</a>, <a href="/containers/">Containers</a>, or external services, without running a WebRTC client themselves.</p>
<p>The <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/">WebSocket adapter</a> bridges that gap by streaming WebRTC media from the SFU to a standard WebSocket endpoint as application-consumable payloads: <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/#media-formats">PCM audio frames and JPEG video frames</a>.</p>
<h4 id="what-changed">What changed</h4>
<p>When you use the WebSocket adapter in <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/#stream-mode-egress">Stream mode (egress)</a> to send live audio or video from the SFU to your own WebSocket endpoint, the SFU now <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/#automatic-reconnection-for-streaming">automatically reconnects</a> after brief endpoint disconnects or restarts. This is especially helpful for long-running media pipelines where the WebSocket endpoint may briefly restart while a recording, transcription, or live analysis job is still in progress.</p>
<p>Previously, a brief disconnect from your WebSocket endpoint could close the adapter and require your application to recreate it before media could resume. Now, the SFU retries the same endpoint for up to 5 seconds with no API change required. If the endpoint comes back within that window, audio and video delivery resumes automatically.</p>
<p>The reconnect behavior also includes <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/#media-buffering-during-reconnect">live-first media buffering</a>, so brief interruptions reduce media loss without replaying stale video.</p>
<h4 id="reconnect-behavior">Reconnect behavior</h4>
<p>During reconnect:</p>
<ul>
<li>Audio uses a short bounded backlog to reduce audible loss. If the interruption lasts longer than the backlog can cover, older audio may be dropped.</li>
<li>Video resumes from the <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/#video-jpeg">latest available JPEG frame</a> instead of replaying stale frames.</li>
<li>Recovery is best effort and does not guarantee gapless or exactly-once delivery.</li>
</ul>
<p>If the endpoint remains unavailable after the 5-second reconnect window, the adapter closes and must be recreated.</p>
<h4 id="learn-more">Learn more</h4>
<ul>
<li><a href="/realtime/sfu/media-transport-adapters/websocket-adapter/">WebSocket adapter</a></li>
<li><a href="/realtime/sfu/media-transport-adapters/websocket-adapter/#automatic-reconnection-for-streaming">Automatic reconnection for streaming</a></li>
<li><a href="/realtime/sfu/get-started/">Get started with Realtime SFU</a></li>
<li><a href="/realtime/sfu/example-architecture/">Realtime SFU example architecture</a></li>
<li><a href="/realtime/sfu/calls-vs-sfus/">Realtime vs Regular SFUs</a></li>
<li><a href="https://realtime-sfu.dev-demos.workers.dev/">Global SFU Network Visualization</a></li>
</ul>
</div></article></div>
