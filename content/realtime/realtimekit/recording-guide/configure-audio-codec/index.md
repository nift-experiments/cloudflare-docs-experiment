---
cp9:
  canonical: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-audio-codec/
  description: Configure audio codec format and channel settings for RealtimeKit recordings.
  full_title: Set Audio Configurations · Cloudflare Realtime docs
  head_html: <title>Set Audio Configurations · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure audio codec format and channel settings for RealtimeKit recordings."><link rel="canonical" href="https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-audio-codec/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-audio-codec/index.md"><meta property="og:title" content="Set Audio Configurations · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure audio codec format and channel settings for RealtimeKit recordings."><meta property="og:url" content="https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-audio-codec/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-audio-codec/#page","headline":"Set Audio Configurations \u00b7 Cloudflare Realtime docs","description":"Configure audio codec format and channel settings for RealtimeKit recordings.","url":"https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-audio-codec/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/realtimekit/recording-guide/configure-audio-codec/
  schema: 1
---
<p>Recording audio requires configuring the <strong>codec</strong> and <strong>channel</strong> parameters to guarantee optimal quality and compatibility with your application's demands.
The codec determines the encoding format for the audio, and the channel specifies the number of audio channels for the recording.
You can modify the following <code>audio_config</code> used for recording the audio:</p>
<h2 id="codec">Codec</h2>
<p>Codec determines the audio encoding format for recording, with MP3 and AAC being the supported formats.</p>
<ul>
<li>AAC (default)</li>
<li>MP3</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11815.md")
</aside>
<h2 id="channel">Channel</h2>
<p>Audio signal pathway within an audio file that carries a specific sound source. The following channels are supported:</p>
<ul>
<li>stereo (default)</li>
<li>mono</li>
</ul>
<p>You can modify the configs by specifying it in the <code>audio_config</code> field in the <a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start Recording API</a>, for example:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;audio_config&quot;: {&#10;    &quot;codec&quot;: &quot;AAC&quot;&#10;    &quot;channel&quot;: &quot;stereo&quot;&#10;  }&#10;}&#10;</code></pre>
<h2 id="download-audio-files">Download Audio Files</h2>
<p>The audio file for your recording is generated only if you passed the <code>audio_config</code> parameters in the <a href="/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/">Start Recording API</a>.</p>
<p>When the recording is completed, you can use the <code>audio_download_url</code> provided in the response body of the <a href="/api/resources/realtime_kit/subresources/recordings/methods/get_one_recording/">Fetch details of a recording API</a> to download and export the audio file.</p>
