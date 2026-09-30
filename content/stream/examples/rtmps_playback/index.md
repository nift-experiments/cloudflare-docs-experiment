---
cp9:
  canonical: https://developers.cloudflare.com/stream/examples/rtmps_playback/
  description: Example of sub 1s latency video playback using RTMPS and ffplay
  full_title: RTMPS playback · Cloudflare Stream docs
  head_html: <title>RTMPS playback · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Example of sub 1s latency video playback using RTMPS and ffplay"><link rel="canonical" href="https://developers.cloudflare.com/stream/examples/rtmps_playback/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/examples/rtmps_playback/index.md"><meta property="og:title" content="RTMPS playback · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Example of sub 1s latency video playback using RTMPS and ffplay"><meta property="og:url" content="https://developers.cloudflare.com/stream/examples/rtmps_playback/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Stream"><meta name="pcx_tags" content="Playback"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/stream/examples/rtmps_playback/#page","headline":"RTMPS playback \u00b7 Cloudflare Stream docs","description":"Example of sub 1s latency video playback using RTMPS and ffplay","url":"https://developers.cloudflare.com/stream/examples/rtmps_playback/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Playback"]}</script>
  markdown: true
  noindex: false
  route: /stream/examples/rtmps_playback/
  schema: 1
---
<p class="article-summary">Example of sub 1s latency video playback using RTMPS and ffplay</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14465.md")
</aside>
<p>Copy the RTMPS <em>playback</em> key for your live input from either:</p>
<ul>
<li>The <strong>Live inputs</strong> page of the Cloudflare dashboard.</li>
</ul>
<div class="nb-dash-button"></div>
<ul>
<li>The <a href="/stream/stream-live/start-stream-live/#use-the-api">Stream API</a></li>
</ul>
<p>Paste it into the URL below, replacing <code>&lt;RTMPS_PLAYBACK_KEY&gt;</code>:</p>
<pre tabindex="0"><code class="language-sh">ffplay -analyzeduration 1 -fflags -nobuffer -sync ext &#x27;rtmps://live.cloudflare.com:443/live/&lt;RTMPS_PLAYBACK_KEY&gt;&#x27;&#10;</code></pre>
<p>For more, refer to <a href="/stream/viewing-videos/using-own-player/#play-live-video-in-native-apps-with-less-than-1-second-latency">Play live video in native apps with less than one second latency</a>.</p>
