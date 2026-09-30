---
cp9:
  canonical: https://developers.cloudflare.com/stream/stream-live/dvr-for-live/
  description: Enable DVR mode in Cloudflare Stream to let viewers rewind, resume, and fast-forward live broadcasts.
  full_title: DVR for Live · Cloudflare Stream docs
  head_html: <title>DVR for Live · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Enable DVR mode in Cloudflare Stream to let viewers rewind, resume, and fast-forward live broadcasts."><link rel="canonical" href="https://developers.cloudflare.com/stream/stream-live/dvr-for-live/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/stream-live/dvr-for-live/index.md"><meta property="og:title" content="DVR for Live · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enable DVR mode in Cloudflare Stream to let viewers rewind, resume, and fast-forward live broadcasts."><meta property="og:url" content="https://developers.cloudflare.com/stream/stream-live/dvr-for-live/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Stream"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/stream/stream-live/dvr-for-live/#page","headline":"DVR for Live \u00b7 Cloudflare Stream docs","description":"Enable DVR mode in Cloudflare Stream to let viewers rewind, resume, and fast-forward live broadcasts.","url":"https://developers.cloudflare.com/stream/stream-live/dvr-for-live/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /stream/stream-live/dvr-for-live/
  schema: 1
---
<p>Stream Live supports &quot;DVR mode&quot; on an opt-in basis to allow viewers to rewind,
resume, and fast-forward a live broadcast. To enable DVR mode, add the
<code>dvrEnabled=true</code> query parameter to the Stream Player embed source or the HLS
manifest URL.</p>
<h2 id="stream-player">Stream Player</h2>
<pre tabindex="0"><code class="language-html">&lt;div style=&quot;position: relative; padding-top: 56.25%;&quot;&gt;&#10;  &lt;iframe&#10;    src=&quot;https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;INPUT_ID|VIDEO_ID&gt;/iframe?dvrEnabled=true&quot;&#10;    style=&quot;border: none; position: absolute; top: 0; left: 0; height: 100%; width: 100%;&quot;&#10;    allow=&quot;accelerometer; gyroscope; autoplay; encrypted-media; picture-in-picture;&quot;&#10;    allowfullscreen=&quot;true&quot;&#10;  &gt;&lt;/iframe&gt;&#10;&lt;/div&gt;&#10;</code></pre>
<p>When DVR mode is enabled the Stream Player will:</p>
<ul>
<li>Show a timeline the viewer can scrub/seek, similar to watching an on-demand
video. The timeline will automatically scale to show the growing duration of
the broadcast while it is live.</li>
<li>The &quot;LIVE&quot; indicator will show grey if the viewer is behind the live edge or
red if they are watching the latest content. Clicking that indicator will jump
forward to the live edge.</li>
<li>If the viewer pauses the player, it will resume playback from that time instead
of jumping forward to the live edge.</li>
</ul>
<h2 id="hls-manifest-for-custom-players">HLS manifest for custom players</h2>
<pre tabindex="0"><code class="language-text">https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;INPUT_ID|VIDEO_ID&gt;/manifest/video.m3u8?dvrEnabled=true&#10;</code></pre>
<p>Custom players using a DVR-capable HLS manifest may need additional
configuration to surface helpful controls or information. Refer to your player
library for additional information.</p>
<h2 id="video-id-or-input-id">Video ID or Input ID</h2>
<p>Stream Live allows loading the Player or HLS manifest by Video ID or Live Input
ID. Refer to <a href="/stream/stream-live/watch-live-stream/">Watch a live stream</a> for how to
retrieve these URLs and compare these options. There are additional
considerations when using DVR mode:</p>
<p><strong>Recommended:</strong> Use DVR Mode on a Video ID URL:</p>
<ul>
<li>When the player loads, it will start playing the active broadcast if it is
still live or play the recording if the broadcast has concluded.</li>
</ul>
<p>DVR Mode on a Live Input ID URL:</p>
<ul>
<li>When the player loads, it will start playing the currently live broadcast if
there is one (refer to <a href="/stream/stream-live/watch-live-stream/#live-input-status">Live Input Status</a>).</li>
<li>If the viewer is still watching <em>after the broadcast ends,</em> they can continue
to watch. However, if the player or manifest is then reloaded, it will show the
latest broadcast or &quot;Stream has not yet started&quot; (<code>HTTP 204</code>). Past broadcasts
are not available by Live Input ID.</li>
</ul>
<h2 id="known-limitations">Known Limitations</h2>
<ul>
<li>When using DVR Mode and a player/manifest created using a Live Input ID, the
player may stall when trying to switch quality levels if a viewer is still
watching after a broadcast has concluded.</li>
<li>Performance may be degraded for DVR-enabled broadcasts longer than three hours.
Manifests are limited to a maximum of 7,200 segments. Segment length is
determined by the keyframe interval, also called GOP size.</li>
<li>DVR Mode relies on Version 8 of the HLS manifest specification. Stream uses
HLS Version 6 in all other contexts. HLS v8 offers extremely broad compatibility
but may not work with certain old player libraries or older devices.</li>
<li>DVR Mode is not available for DASH manifests.</li>
</ul>
