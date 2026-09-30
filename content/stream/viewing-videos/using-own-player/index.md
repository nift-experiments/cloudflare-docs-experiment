---
cp9:
  canonical: https://developers.cloudflare.com/stream/viewing-videos/using-own-player/
  description: Play Cloudflare Stream videos with any HLS/DASH-compatible player on web, iOS, or Android.
  full_title: Use your own player · Cloudflare Stream docs
  head_html: <title>Use your own player · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Play Cloudflare Stream videos with any HLS/DASH-compatible player on web, iOS, or Android."><link rel="canonical" href="https://developers.cloudflare.com/stream/viewing-videos/using-own-player/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/viewing-videos/using-own-player/index.md"><meta property="og:title" content="Use your own player · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Play Cloudflare Stream videos with any HLS/DASH-compatible player on web, iOS, or Android."><meta property="og:url" content="https://developers.cloudflare.com/stream/viewing-videos/using-own-player/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Stream"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/stream/viewing-videos/using-own-player/#page","headline":"Use your own player \u00b7 Cloudflare Stream docs","description":"Play Cloudflare Stream videos with any HLS/DASH-compatible player on web, iOS, or Android.","url":"https://developers.cloudflare.com/stream/viewing-videos/using-own-player/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /stream/viewing-videos/using-own-player/
  schema: 1
---
<p>Cloudflare Stream is compatible with all video players that support HLS and DASH, which are standard formats for streaming media with broad support across all web browsers, mobile operating systems and media streaming devices.</p>
<p>Platform-specific guides:</p>
<ul>
<li><a href="/stream/viewing-videos/using-own-player/web/">Web</a></li>
<li><a href="/stream/viewing-videos/using-own-player/ios/">iOS (AVPlayer)</a></li>
<li><a href="/stream/viewing-videos/using-own-player/android/">Android (ExoPlayer)</a></li>
</ul>
<h2 id="use-hls-and-dash-manifests">Use HLS and Dash manifests</h2>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14601.md")
</aside>
<h3 id="url">URL</h3>
<p>Each video and live stream has its own unique HLS and DASH manifest. You can access the manifest by replacing <code>&lt;UID&gt;</code> with the UID of your video or live input, and replacing <code>&lt;CODE&gt;</code> with your unique customer code, in the URLs below:</p>
<pre tabindex="0"><code class="language-txt">https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;UID&gt;/manifest/video.m3u8&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;UID&gt;/manifest/video.mpd&#10;</code></pre>
<h4 id="ll-hls-playback">LL-HLS playback <span class="nb-badge">Beta</span></h4>
<p>If a Live Input is enabled for the Low-Latency HLS beta, add the query string <code>?protocol=llhls</code> to the HLS manifest URL to test the low latency manifest in a custom player. Refer to <a href="/stream/stream-live/start-stream-live/#use-the-api">Start a Live Stream</a> to enable this option.</p>
<pre tabindex="0"><code class="language-txt">https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;UID&gt;/manifest/video.m3u8?protocol=llhls&#10;</code></pre>
<h3 id="dashboard">Dashboard</h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Stream</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>From the list of videos, locate your video and select it.</li>
<li>From the <strong>Settings</strong> tab, locate the <strong>HLS Manifest URL</strong> and <strong>Dash Manifest URL</strong>.</li>
<li>Select <strong>Click to copy</strong> under the option you want to use.</li>
</ol>
<h3 id="api">API</h3>
<p>Refer to the <a href="/api/resources/stream/methods/get/">Stream video details API documentation</a> to learn how to fetch the manifest URLs using the Cloudflare API.</p>
<h2 id="customize-manifests-by-specifying-available-client-bandwidth">Customize manifests by specifying available client bandwidth</h2>
<p>Each HLS and DASH manifest provides multiple resolutions of your video or live stream. Your player contains adaptive bitrate logic to estimate the viewer's available bandwidth, and select the optimal resolution to play. Each player has different logic that makes this decision, and most have configuration options to allow you to customize or override either bandwidth or resolution.</p>
<p>If your player lacks such configuration options or you need to override them, you can add the <code>clientBandwidthHint</code> query param to the request to fetch the manifest file. This should be used only as a last resort — we recommend first using customization options provided by your player. Remember that while you may be developing your website or app on a fast Internet connection, and be tempted to use this setting to force high quality playback, many of your viewers are likely connecting over slower mobile networks.</p>
<ul>
<li><code>clientBandwidthHint</code> float
<ul>
<li>Return only the video representation closest to the provided bandwidth value (in Mbps). This can be used to enforce a specific quality level. If you specify a value that would cause an invalid or empty manifest to be served, the hint is ignored.</li>
</ul>
</li>
</ul>
<p>Refer to the example below to display only the video representation with a bitrate closest to 1.8 Mbps.</p>
<pre tabindex="0"><code class="language-txt">https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/manifest/video.m3u8?clientBandwidthHint=1.8&#10;</code></pre>
<h2 id="play-live-video-in-native-apps-with-less-than-1-second-latency">Play live video in native apps with less than 1 second latency</h2>
<p>If you need ultra low latency, and your users view live video in native apps, you can stream live video with <a href="https://blog.cloudflare.com/magic-hdmi-cable/"><strong>glass-to-glass latency of less than 1 second</strong></a>, by using SRT or RTMPS for playback.</p>
<p><img src="/assets/upstream/images/stream/stream-rtmps-srt-playback-magic-hdmi-cable.png" alt="Diagram showing SRT and RTMPS playback via the Cloudflare Network" /></p>
<p>SRT and RTMPS playback is built into <a href="https://ffmpeg.org/">ffmpeg</a>. You will need to integrate ffmpeg with your own video player —  neither <a href="/stream/viewing-videos/using-own-player/ios/">AVPlayer (iOS)</a> nor <a href="/stream/viewing-videos/using-own-player/android/">ExoPlayer (Android)</a> natively support SRT or RTMPS playback.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14600.md")
</aside>
<p>We recommend using <a href="https://github.com/arthenica/ffmpeg-kit">ffmpeg-kit</a> as a cross-platform wrapper for ffmpeg.</p>
<h3 id="examples">Examples</h3>
<ul>
<li><a href="/stream/examples/rtmps_playback/">RTMPS Playback with ffplay</a></li>
<li><a href="/stream/examples/srt_playback/">SRT playback with ffplay</a></li>
</ul>
