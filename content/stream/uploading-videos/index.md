---
cp9:
  canonical: https://developers.cloudflare.com/stream/uploading-videos/
  description: Review upload methods, supported formats, and recommendations for Cloudflare Stream.
  full_title: Upload videos · Cloudflare Stream docs
  head_html: <title>Upload videos · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Review upload methods, supported formats, and recommendations for Cloudflare Stream."><link rel="canonical" href="https://developers.cloudflare.com/stream/uploading-videos/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/uploading-videos/index.md"><meta property="og:title" content="Upload videos · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review upload methods, supported formats, and recommendations for Cloudflare Stream."><meta property="og:url" content="https://developers.cloudflare.com/stream/uploading-videos/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Stream"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/stream/uploading-videos/#page","headline":"Upload videos \u00b7 Cloudflare Stream docs","description":"Review upload methods, supported formats, and recommendations for Cloudflare Stream.","url":"https://developers.cloudflare.com/stream/uploading-videos/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /stream/uploading-videos/
  schema: 1
---
<p>Before you upload your video, review the options for uploading a video, supported formats, and recommendations.</p>
<h2 id="upload-options">Upload options</h2>
<table>
<thead>
<tr>
<th>Upload method</th>
<th>When to use</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://dash.cloudflare.com/?to=/:account/stream">Stream Dashboard</a></td>
<td>Upload videos from the Stream Dashboard without writing any code.</td>
</tr>
<tr>
<td><a href="/stream/uploading-videos/upload-via-link/">Upload with a link</a></td>
<td>Upload videos using a link, such as an S3 bucket or content management system.</td>
</tr>
<tr>
<td><a href="/stream/uploading-videos/upload-video-file/">Upload video file</a></td>
<td>Upload videos stored on a computer.</td>
</tr>
<tr>
<td><a href="/stream/uploading-videos/direct-creator-uploads/">Direct creator uploads</a></td>
<td>Allows end users of your website or app to upload videos directly to Cloudflare Stream.</td>
</tr>
</tbody>
</table>
<h2 id="supported-video-formats">Supported video formats</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14382.md")
</aside>
<ul>
<li>MP4</li>
<li>MKV</li>
<li>MOV</li>
<li>AVI</li>
<li>FLV</li>
<li>MPEG-2 TS</li>
<li>MPEG-2 PS</li>
<li>MXF</li>
<li>LXF</li>
<li>GXF</li>
<li>3GP</li>
<li>WebM</li>
<li>MPG</li>
<li>Quicktime</li>
</ul>
<h2 id="recommendations-for-on-demand-videos">Recommendations for on-demand videos</h2>
<ul>
<li>Optional but ideal settings:
<ul>
<li>MP4 containers</li>
<li>AAC audio codec</li>
<li>H264 video codec</li>
<li>60 or fewer frames per second</li>
</ul>
</li>
<li>Closed GOP (<em>Only required for live streaming.</em>)</li>
<li>Mono or Stereo audio. Stream will mix audio tracks with more than two channels down to stereo.</li>
</ul>
<h2 id="frame-rates">Frame rates</h2>
<p>Stream accepts video uploads at any frame rate. During encoding, Stream re-encodes videos for a maximum of 90 FPS playback. If the original video has a frame rate lower than 90 FPS, Stream re-encodes at the original frame rate.</p>
<p>For variable frame rate content, Stream drops extra frames. For example, if there is more than one frame within a 1/30 second window, Stream drops the extra frames within that period.</p>
