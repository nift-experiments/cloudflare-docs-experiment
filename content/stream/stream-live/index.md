---
cp9:
  canonical: https://developers.cloudflare.com/stream/stream-live/
  description: Ingest, encode, and deliver live video to viewers worldwide using Cloudflare Stream.
  full_title: Stream live video · Cloudflare Stream docs
  head_html: <title>Stream live video · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Ingest, encode, and deliver live video to viewers worldwide using Cloudflare Stream."><link rel="canonical" href="https://developers.cloudflare.com/stream/stream-live/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/stream-live/index.md"><meta property="og:title" content="Stream live video · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Ingest, encode, and deliver live video to viewers worldwide using Cloudflare Stream."><meta property="og:url" content="https://developers.cloudflare.com/stream/stream-live/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Stream"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/stream/stream-live/#page","headline":"Stream live video \u00b7 Cloudflare Stream docs","description":"Ingest, encode, and deliver live video to viewers worldwide using Cloudflare Stream.","url":"https://developers.cloudflare.com/stream/stream-live/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /stream/stream-live/
  schema: 1
---
<p>Cloudflare Stream lets you or your users <a href="https://www.cloudflare.com/learning/video/what-is-live-streaming/">stream live video</a>, and play live video in your website or app, without managing and configuring any of your own infrastructure.</p>
<h2 id="how-stream-works">How Stream works</h2>
<p>Stream handles video streaming end-to-end, from ingestion through delivery.</p>
<ol>
<li>For each live stream, you create a unique live input, either using the Stream Dashboard or API.</li>
<li>Each live input has a unique Stream Key, that you provide to the creator who is streaming live video.</li>
<li>Creators use this Stream Key to broadcast live video to Cloudflare Stream, over either RTMPS or SRT.</li>
<li>Cloudflare Stream encodes this live video at multiple resolutions and delivers it to viewers, using Cloudflare's Global Network. You can play video on your website using the <a href="/stream/viewing-videos/using-the-stream-player/">Stream Player</a> or using <a href="/stream/viewing-videos/using-own-player/">any video player that supports HLS or DASH</a>.</li>
</ol>
<p><img src="/assets/upstream/images/stream/live-stream-workflow.png" alt="Diagram the explains the live stream workflow" /></p>
<h2 id="rtmp-reconnections">RTMP reconnections</h2>
<p>As long as your streaming software reconnects, Stream Live will continue to ingest and stream your live video. Make sure the streaming software you use to push RTMP feeds automatically reconnects if the connection breaks. Some apps like OBS reconnect automatically while other apps like FFmpeg require custom configuration.</p>
<h2 id="bitrate-estimates-at-each-quality-level-bitrate-ladder">Bitrate estimates at each quality level (bitrate ladder)</h2>
<p>Cloudflare Stream transcodes and makes live streams available to viewers at multiple quality levels. This is commonly referred to as <a href="https://www.cloudflare.com/learning/video/what-is-adaptive-bitrate-streaming">Adaptive Bitrate Streaming (ABR)</a>.</p>
<p>With ABR, client video players need to be provided with estimates of how much bandwidth will be needed to play each quality level (ex: 1080p). Stream creates and updates these estimates dynamically by analyzing the bitrate of your users' live streams. This ensures that live video plays at the highest quality a viewer has adequate bandwidth to play, even in cases where the broadcaster's software or hardware provides incomplete or inaccurate information about the bitrate of their live content.</p>
<h3 id="how-it-works">How it works</h3>
<p>If a live stream contains content with low visual complexity, like a slideshow presentation, the bandwidth estimates provided in the HLS and DASH manifests will be lower —  a stream like this has a low bitrate and requires relatively little bandwidth, even at high resolution.  This ensures that as many viewers as possible view the highest quality level.</p>
<p>Conversely, if a live stream contains content with high visual complexity, like live sports with motion and camera panning, the bandwidth estimates provided in the manifest will be higher — a stream like this has a high bitrate and requires more bandwidth. This ensures that viewers with inadequate bandwidth switch down to a lower quality level, and their playback does not buffer.</p>
<h3 id="how-you-benefit">How you benefit</h3>
<p>If you're building a creator platform or any application where your end users create their own live streams, your end users likely use streaming software or hardware that you cannot control. In practice, these live streaming setups often send inaccurate or incomplete information about the bitrate of a given live stream, or are misconfigured by end users.</p>
<p>Stream adapts based on the live video that we actually receive, rather than blindly trusting the advertised bitrate. This means that even in cases where your end users' settings are less than ideal, client video players will still receive the most accurate bitrate estimates possible, ensuring the highest quality video playback for your viewers, while avoiding pushing configuration complexity back onto your users.</p>
<h2 id="transition-from-live-playback-to-a-recording">Transition from live playback to a recording</h2>
<p>Recordings are available for live streams within 60 seconds after a live stream ends.</p>
<p>You can check a video's status to determine if it's ready to view by making a <a href="/stream/stream-live/watch-live-stream/#use-the-api"><code>GET</code> request to the <code>stream</code> endpoint</a> and viewing the <code>state</code> or by <a href="/stream/stream-live/watch-live-stream/#use-the-dashboard">using the Cloudflare dashboard</a>.</p>
<p>After the live stream ends, you can <a href="/stream/stream-live/replay-recordings/">replay live stream recordings</a> in the <code>ready</code> state by using one of the playback URLs.</p>
<h2 id="billing">Billing</h2>
<p>Stream Live is billed identically to the rest of Cloudflare Stream.</p>
<ul>
<li>You pay $5 per 1000 minutes of recorded video.</li>
<li>You pay $1 per 1000 minutes of delivered video.</li>
</ul>
<p>All Stream Live videos are automatically recorded. There is no additional cost for encoding and packaging live videos.</p>
