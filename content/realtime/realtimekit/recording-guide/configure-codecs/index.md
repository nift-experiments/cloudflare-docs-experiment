---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-codecs/
  description: Configure video codecs, resolution, and container formats for RealtimeKit recordings.
  full_title: Configure Video Settings · Cloudflare Realtime docs
  head_html: <title>Configure Video Settings · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure video codecs, resolution, and container formats for RealtimeKit recordings."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-codecs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-codecs/index.md"><meta property="og:title" content="Configure Video Settings · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure video codecs, resolution, and container formats for RealtimeKit recordings."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-codecs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-codecs/#page","headline":"Configure Video Settings \u00b7 Cloudflare Realtime docs","description":"Configure video codecs, resolution, and container formats for RealtimeKit recordings.","url":"https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-codecs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/recording-guide/configure-codecs/
  schema: 1
---
<p>Video codecs are software programs that compress and decompress digital video data for transmission, storage, or playback. Configuring the appropriate video codec can help reduce file size, enhance video quality, and ensure compatibility with different playback devices.</p>
<h2 id="configure-codecs">Configure Codecs</h2>
<p>You can modify the codec which is used for recording the videos. We currently
support the following codecs:</p>
<ul>
<li><strong>H264 (default)</strong>: Records video using the H.264 codec with 1280px × 720px
resolution, and 384 kbps AAC audio in MP4 container.</li>
<li><strong>VP8</strong>: Records video using the VP8 codec with 1280px × 720px
resolution, and Vorbis codec audio in WebM container.</li>
</ul>
<p>You can change the codec by specifying the codec in the <code>video_config</code> field in
the <a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start Recording API</a>, for
example:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;video_config&quot;: {&#10;    &quot;codec&quot;: &quot;H264&quot;&#10;  }&#10;}&#10;</code></pre>
<h2 id="download-video-files">Download Video Files</h2>
<p>The video file for your recording is generated only if you passed the <code>video_config</code> parameters in the <a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start Recording API</a>.</p>
<p>When the recording is completed, you can use the <code>downloadUrl</code> provided in the response body of the <a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start Recording API</a> to download and export the video file.</p>
