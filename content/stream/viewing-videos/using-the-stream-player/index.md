---
cp9:
  canonical: https://developers.cloudflare.com/stream/viewing-videos/using-the-stream-player/
  description: Embed and customize the Cloudflare Stream Player for on-demand and live video playback.
  full_title: Use the Stream Player · Cloudflare Stream docs
  head_html: <title>Use the Stream Player · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Embed and customize the Cloudflare Stream Player for on-demand and live video playback."><link rel="canonical" href="https://developers.cloudflare.com/stream/viewing-videos/using-the-stream-player/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/viewing-videos/using-the-stream-player/index.md"><meta property="og:title" content="Use the Stream Player · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Embed and customize the Cloudflare Stream Player for on-demand and live video playback."><meta property="og:url" content="https://developers.cloudflare.com/stream/viewing-videos/using-the-stream-player/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Stream"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/stream/viewing-videos/using-the-stream-player/#page","headline":"Use the Stream Player \u00b7 Cloudflare Stream docs","description":"Embed and customize the Cloudflare Stream Player for on-demand and live video playback.","url":"https://developers.cloudflare.com/stream/viewing-videos/using-the-stream-player/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /stream/viewing-videos/using-the-stream-player/
  schema: 1
---
<p>Cloudflare provides a customizable web player that can play both on-demand and live video, and requires zero additional engineering work.</p>
<figure data-type="stream">
<div class="AspectRatio" style="--aspect-ratio: calc(16 / 9)">
<iframe title="Embedded media" class="AspectRatio--content" src="https://iframe.videodelivery.net/5d5bc37ffcf54c9b82e996823bffbb81?mute=true" style="border: none" frame-border="0" allow="accelerometer; gyroscope; autoplay; encrypted-media; picture-in-picture;" allow-full-screen></iframe>
</div>
</figure>
<p>To add the Stream Player to a web page, you can either:</p>
<ul>
<li>Generate an embed code on the <strong>Stream</strong> page of the Cloudflare dashboard for a specific video or live input.</li>
</ul>
<div class="nb-dash-button"></div>
<ul>
<li>Use the code example below, replacing <code>&lt;VIDEO_UID&gt;</code> with the video UID (or <a href="/stream/viewing-videos/securing-your-stream/">signed token</a>) and <code>&lt;CODE&gt;</code> with the your unique customer code, which can be found in the Stream Dashboard.</li>
</ul>
<pre tabindex="0"><code class="language-html">&lt;iframe&#10;	src=&quot;https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;VIDEO_UID&gt;/iframe&quot;&#10;	style=&quot;border: none&quot;&#10;	height=&quot;720&quot;&#10;	width=&quot;1280&quot;&#10;	allow=&quot;accelerometer; gyroscope; autoplay; encrypted-media; picture-in-picture;&quot;&#10;	allowfullscreen=&quot;true&quot;&#10;&gt;&lt;/iframe&gt;&#10;</code></pre>
<p>Stream player is also available as a <a href="https://www.npmjs.com/package/@cloudflare/stream-react">React</a> or <a href="https://www.npmjs.com/package/@cloudflare/stream-angular">Angular</a> component.</p>
<h2 id="browser-compatibility">Browser compatibility</h2>
<h3 id="desktop">Desktop</h3>
<ul>
<li>Chrome: version 88 or higher</li>
<li>Firefox: version 87 or higher</li>
<li>Edge: version 89 or higher</li>
<li>Safari: version 14 or higher</li>
<li>Opera: version 75 or higher</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14597.md")
</aside>
<h3 id="mobile">Mobile</h3>
<ul>
<li>Chrome on Android: version 90</li>
<li>UC Browser on Android: version 12.12 or higher</li>
<li>Samsung Internet: version 13 or higher</li>
<li>Safari on iOS: version 13.4 or higher (speed selector supported when not in fullscreen)</li>
</ul>
<h2 id="player-size">Player Size</h2>
<h3 id="fixed-dimensions">Fixed Dimensions</h3>
<p>Changing the <code>height</code> and <code>width</code> attributes on the <code>iframe</code> will change the pixel value dimensions of the iframe displayed on the host page.</p>
<pre tabindex="0"><code class="language-html">&lt;iframe&#10;	src=&quot;https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;VIDEO_UID&gt;/iframe&quot;&#10;	style=&quot;border: none&quot;&#10;	height=&quot;400&quot;&#10;	width=&quot;400&quot;&#10;	allow=&quot;accelerometer; gyroscope; autoplay; encrypted-media; picture-in-picture;&quot;&#10;	allowfullscreen=&quot;true&quot;&#10;&gt;&lt;/iframe&gt;&#10;</code></pre>
<h3 id="responsive">Responsive</h3>
<p>To make an iframe responsive, it needs styles to enforce an aspect ratio by setting the <code>iframe</code> to <code>position: absolute;</code> and having it fill a container that uses a calculated <code>padding-top</code> percentage.</p>
<pre tabindex="0"><code class="language-html">&lt;!-- padding-top calculation is height / width (assuming 16:9 aspect ratio) --&gt;&#10;&lt;div style=&quot;position: relative; padding-top: 56.25%&quot;&gt;&#10;	&lt;iframe&#10;		src=&quot;https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;VIDEO_UID&gt;/iframe&quot;&#10;		style=&quot;border: none; position: absolute; top: 0; height: 100%; width: 100%&quot;&#10;		allow=&quot;accelerometer; gyroscope; autoplay; encrypted-media; picture-in-picture;&quot;&#10;		allowfullscreen=&quot;true&quot;&#10;	&gt;&lt;/iframe&gt;&#10;&lt;/div&gt;&#10;</code></pre>
<h2 id="basic-options">Basic Options</h2>
<p>Player options are configured with querystring parameters in the iframe's <code>src</code> attribute. For example:</p>
<p><code>https://customer-&lt;CODE&gt;.cloudflarestream.com/&lt;VIDEO_UID&gt;/iframe?autoplay=true&amp;muted=true</code></p>
<ul>
<li><code>autoplay</code> default: <code>false</code>
<ul>
<li>If the autoplay flag is included as a querystring parameter, the player will attempt to autoplay the video. If you don't want the video to autoplay, don't include the autoplay flag at all (instead of setting it to <code>autoplay=false</code>.) Note that mobile browsers generally do not support this attribute, the user must tap the screen to begin video playback. Please consider mobile users or users with Internet usage limits as some users don't have unlimited Internet access before using this attribute.</li>
</ul>
</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14596.md")
</aside>
<ul>
<li>
<p><code>controls</code> default: <code>true</code></p>
<ul>
<li>Shows video controls such as buttons for play/pause, volume controls.</li>
</ul>
</li>
<li>
<p><code>defaultTextTrack</code></p>
<ul>
<li>Will initialize the player with the specified language code's text track enabled. The value should be the BCP-47 language code that was used to <a href="/stream/edit-videos/adding-captions/">upload the text track</a>. If the specified language code has no captions available, the player will behave as though no language code had been provided.</li>
</ul>
</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14595.md")
</aside>
<ul>
<li><code>letterboxColor</code>
<ul>
<li>Any valid <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/color_value">CSS color value</a> provided will be applied to the letterboxing/pillarboxing of the player's UI. This can be set to <code>transparent</code> to avoid letterboxing/pillarboxing when not in fullscreen mode.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14594.md")
</aside>
<ul>
<li>
<p><code>loop</code> default: <code>false</code></p>
<ul>
<li>If enabled the player will automatically seek back to the start upon reaching the end of the video.</li>
</ul>
</li>
<li>
<p><code>muted</code> default: <code>false</code></p>
<ul>
<li>If set, the audio will be initially silenced.</li>
</ul>
</li>
<li>
<p><code>preload</code> default: <code>none</code></p>
<ul>
<li>This enumerated option is intended to provide a hint to the browser about what the author thinks will lead to the best user experience. You may specify the value <code>preload=&quot;auto&quot;</code> to preload the beginning of the video. Not including the option or using <code>preload=&quot;metadata&quot;</code> will just load the metadata needed to start video playback when requested.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14593.md")
</aside>
<ul>
<li><code>poster</code> defaults to the first frame of the video
<ul>
<li>A URL for an image to be shown before the video is started or while the video is downloading. If this attribute isn't specified, a thumbnail image of the video is shown.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14592.md")
</aside>
<ul>
<li><code>primaryColor</code>
<ul>
<li>Any valid <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/color_value">CSS color value</a> provided will be applied to certain elements of the player's UI.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14591.md")
</aside>
<ul>
<li>
<p><code>src</code></p>
<ul>
<li>The video id from the video you've uploaded to Cloudflare Stream should be included here.</li>
</ul>
</li>
<li>
<p><code>startTime</code></p>
<ul>
<li>A timestamp that specifies the time when playback begins. If a plain number is used such as <code>?startTime=123</code>, it will be interpreted as <code>123</code> seconds. More human readable timestamps can also be used, such as <code>?startTime=1h12m27s</code> for <code>1 hour, 12 minutes, and 27 seconds</code>.</li>
</ul>
</li>
<li>
<p><code>ad-url</code></p>
<ul>
<li>The Stream Player supports VAST Tags to insert ads such as prerolls. If you have a VAST tag URI, you can pass it to the Stream Player by setting the <code>ad-url</code> parameter. The URI must be encoded using a function like JavaScript's <code>encodeURIComponent()</code>.</li>
</ul>
</li>
</ul>
<h2 id="debug-info">Debug Info</h2>
<p>The Stream player Debug menu can be shown and hidden using the key combination <code>Shift-D</code> while the video is playing.</p>
<h2 id="live-stream-recording-playback">Live stream recording playback</h2>
<p>After a live stream ends, a recording is automatically generated and available within 60 seconds. To ensure successful video viewing and playback, keep the following in mind:</p>
<ul>
<li>If a live stream ends while a viewer is watching, viewers should wait 60 seconds and then reload the player to view the recording of the live stream.</li>
<li>After a live stream ends, you can check the status of the recording via the API. When the video state is <code>ready</code>, you can use one of the manifest URLs to stream the recording.</li>
</ul>
<p>While the recording of the live stream is generating, the video may report as <code>not-found</code> or <code>not-started</code>.</p>
<h2 id="low-latency-hls-playback">Low-Latency HLS playback <span class="nb-badge">Beta</span></h2>
<p>If a Live Input is enabled for the Low-Latency HLS beta, the Stream player will automatically play in low-latency mode if possible. Refer to <a href="/stream/stream-live/start-stream-live/#use-the-api">Start a Live Stream</a> to enable this option.</p>
