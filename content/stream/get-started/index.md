---
cp9:
  canonical: https://developers.cloudflare.com/stream/get-started/
  description: Upload your first video or start your first live stream with Cloudflare Stream.
  full_title: Get started · Cloudflare Stream docs
  head_html: <title>Get started · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Upload your first video or start your first live stream with Cloudflare Stream."><link rel="canonical" href="https://developers.cloudflare.com/stream/get-started/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/get-started/index.md"><meta property="og:title" content="Get started · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Upload your first video or start your first live stream with Cloudflare Stream."><meta property="og:url" content="https://developers.cloudflare.com/stream/get-started/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Stream"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/stream/get-started/#page","headline":"Get started \u00b7 Cloudflare Stream docs","description":"Upload your first video or start your first live stream with Cloudflare Stream.","url":"https://developers.cloudflare.com/stream/get-started/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /stream/get-started/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="stream-live-webrtc-is-going-ga">Stream Live WebRTC is going GA:</h3>
@markup("md", "content/.markup/bodies/290.md")
</aside>
<ul>
<li><a href="/stream/get-started#upload-your-first-video">Upload your first video</a></li>
<li><a href="/stream/get-started#start-your-first-live-stream">Start your first live stream</a></li>
</ul>
<h2 id="upload-your-first-video">Upload your first video</h2>
<h3 id="step-1-upload-an-example-video-from-a-public-url">Step 1: Upload an example video from a public URL</h3>
<p>You can upload videos using the API or directly on the <strong>Stream</strong> page of the Cloudflare dashboard.</p>
<div class="nb-dash-button"></div>
<p>For a list of accepted file types, refer to <a href="/stream/uploading-videos/#supported-video-formats">Supported video formats</a>.</p>
<p>To use the API, replace the <code>API_TOKEN</code> and <code>ACCOUNT_ID</code> values with your credentials in the example below.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/299.md")
</div></div>
<h3 id="step-2-wait-until-the-video-is-ready-to-stream">Step 2: Wait until the video is ready to stream</h3>
<p>Because Stream must download and process the video, the video might not be available for a few seconds depending on the length of your video. You should poll the Stream API until <code>readyToStream</code> is <code>true</code>, or use <a href="/stream/manage-video-library/using-webhooks/">webhooks</a> to be notified when a video is ready for streaming.</p>
<p>Use the video UID from the first step to poll the video:</p>
<pre tabindex="0"><code class="language-bash">curl \&#10;&#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/stream/&lt;VIDEO_UID&gt;&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;uid&quot;: &quot;6b9e68b07dfee8cc2d116e4c51d6a957&quot;,&#10;		&quot;preview&quot;: &quot;https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/watch&quot;,&#10;		&quot;thumbnail&quot;: &quot;https://customer-f33zs165nr7gyfy4.cloudflarestream.com/6b9e68b07dfee8cc2d116e4c51d6a957/thumbnails/thumbnail.jpg&quot;,&#10;		&quot;readyToStream&quot;: true,&#10;		&quot;status&quot;: {&#10;			&quot;state&quot;: &quot;ready&quot;&#10;		},&#10;		&quot;meta&quot;: {&#10;			&quot;downloaded-from&quot;: &quot;https://storage.googleapis.com/stream-example-bucket/video.mp4&quot;,&#10;			&quot;name&quot;: &quot;My First Stream Video&quot;&#10;		},&#10;		&quot;created&quot;: &quot;2020-10-16T20:20:17.872170843Z&quot;,&#10;		&quot;size&quot;: 9032701&#10;		//...&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h3 id="step-3-play-the-video-in-your-website-or-app">Step 3: Play the video in your website or app</h3>
<p>Videos uploaded to Stream can be played on any device and platform, from websites to native apps. See <a href="/stream/viewing-videos">Play videos</a> for details and examples of video playback across platforms.</p>
<p>To play video on your website with the <a href="/stream/viewing-videos/using-the-stream-player/">Stream Player</a>, copy the <code>uid</code> of the video from the request above, along with your unique customer code, and replace <code>&lt;CODE&gt;</code> and <code>&lt;VIDEO_UID&gt;</code> in the embed code below:</p>
<pre tabindex="0"><code class="language-html">&lt;iframe&#10;	src=&quot;https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;VIDEO_UID&gt;/iframe&quot;&#10;	title=&quot;Example Stream video&quot;&#10;	frameborder=&quot;0&quot;&#10;	allow=&quot;accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture&quot;&#10;	allowfullscreen&#10;&gt;&#10;&lt;/iframe&gt;&#10;</code></pre>
<p>The embed code above can also be found on the <strong>Stream</strong> page of the Cloudflare dashboard.</p>
<div class="nb-dash-button"></div>
<figure data-type="stream">
<div class="AspectRatio" style="--aspect-ratio: calc(16 / 9)">
<iframe class="AspectRatio--content" src="https://iframe.videodelivery.net/5d5bc37ffcf54c9b82e996823bffbb81?muted=true" title="Example Stream video" frame-border="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; fullscreen"></iframe>
</div>
</figure>
<h3 id="next-steps">Next steps</h3>
<ul>
<li><a href="/stream/edit-videos/">Edit your video</a> and add captions or watermarks</li>
<li><a href="/stream/viewing-videos/using-the-stream-player/">Customize the Stream player</a></li>
</ul>
<h2 id="start-your-first-live-stream">Start your first live stream</h2>
<h3 id="step-1-create-a-live-input">Step 1: Create a live input</h3>
<p>You can create a live input using the API or the <strong>Live inputs</strong> page of the Cloudflare dashboard.</p>
<div class="nb-dash-button"></div>
<p>To use the API, replace the <code>API_TOKEN</code> and <code>ACCOUNT_ID</code> values with your credentials in the example below.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/304.md")
</div></div>
<h3 id="step-2-copy-the-rtmps-url-and-key-and-use-them-with-your-live-streaming-application">Step 2: Copy the RTMPS URL and key, and use them with your live streaming application.</h3>
<p>We recommend using <a href="https://obsproject.com/">Open Broadcaster Software (OBS)</a> to get started.</p>
<h3 id="step-3-play-the-live-stream-in-your-website-or-app">Step 3: Play the live stream in your website or app</h3>
<p>Live streams can be played on any device and platform, from websites to native apps, using the same video players as videos uploaded to Stream. See <a href="/stream/viewing-videos">Play videos</a> for details and examples of video playback across platforms.</p>
<p>To play the live stream you just started on your website with the <a href="/stream/viewing-videos/using-the-stream-player/">Stream Player</a>, copy the <code>uid</code> of the live input from the request above, along with your unique customer code, and replace <code>&lt;CODE&gt;</code> and <code>&lt;VIDEO_UID&gt;</code> in the embed code below:</p>
<pre tabindex="0"><code class="language-html">&lt;iframe&#10;	src=&quot;https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;VIDEO_UID&gt;/iframe&quot;&#10;	title=&quot;Example Stream video&quot;&#10;	frameborder=&quot;0&quot;&#10;	allow=&quot;accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture&quot;&#10;	allowfullscreen&#10;&gt;&#10;&lt;/iframe&gt;&#10;</code></pre>
<p>The embed code above can also be found on the <strong>Stream</strong> page of the Cloudflare dashboard.</p>
<div class="nb-dash-button"></div>
<h3 id="next-steps-1">Next steps</h3>
<ul>
<li><a href="/stream/viewing-videos/securing-your-stream/">Secure your stream</a></li>
<li><a href="/stream/getting-analytics/live-viewer-count/">View live viewer counts</a></li>
</ul>
<h2 id="accessibility-considerations">Accessibility considerations</h2>
<p>To make your video content more accessible, include <a href="/stream/edit-videos/adding-captions/">captions</a> and <a href="https://www.w3.org/WAI/media/av/av-content/">high-quality audio recording</a>.</p>
