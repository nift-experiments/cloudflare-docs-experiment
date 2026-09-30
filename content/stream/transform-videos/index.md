---
cp9:
  canonical: https://developers.cloudflare.com/stream/transform-videos/
  description: Optimize and manipulate videos stored outside Cloudflare Stream with Media Transformations.
  full_title: Transform videos · Cloudflare Stream docs
  head_html: <title>Transform videos · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Optimize and manipulate videos stored outside Cloudflare Stream with Media Transformations."><link rel="canonical" href="https://developers.cloudflare.com/stream/transform-videos/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/transform-videos/index.md"><meta property="og:title" content="Transform videos · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Optimize and manipulate videos stored outside Cloudflare Stream with Media Transformations."><meta property="og:url" content="https://developers.cloudflare.com/stream/transform-videos/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Stream"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/stream/transform-videos/#page","headline":"Transform videos \u00b7 Cloudflare Stream docs","description":"Optimize and manipulate videos stored outside Cloudflare Stream with Media Transformations.","url":"https://developers.cloudflare.com/stream/transform-videos/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /stream/transform-videos/
  schema: 1
---
<p>You can optimize and manipulate videos stored <em>outside</em> of Cloudflare Stream with Media Transformations. Transformed videos and images are served from one of your zones on Cloudflare.</p>
<p>To transform a video or image, you must <a href="/stream/transform-videos/#getting-started">enable transformations</a> for your zone. If your zone already has Image Transformations enabled, you can also optimize videos with Media Transformations.</p>
<h2 id="getting-started">Getting started</h2>
<p>You can dynamically optimize and generate still images from videos that are stored <em>outside</em> of Cloudflare Stream with Media Transformations.</p>
<p>Cloudflare will automatically cache every transformed video or image on our global network so that you store only the original image at your origin.</p>
<p>To enable transformations on your zone:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Transformations</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Locate the specific zone where you want to enable transformations.</li>
<li>Select <strong>Enable</strong> for the zone.</li>
</ol>
<h2 id="transform-a-video-by-url">Transform a video by URL</h2>
<p>You can convert and resize videos by requesting them via a specially-formatted URL, without writing any code. The URL format is:</p>
<pre tabindex="0"><code>https://example.com/cdn-cgi/media/&lt;OPTIONS&gt;/&lt;SOURCE-VIDEO&gt;&#10;</code></pre>
<ul>
<li><code>example.com</code>: Your website or zone on Cloudflare, with Transformations enabled.</li>
<li><code>/cdn-cgi/media/</code>: A prefix that identifies a special path handled by Cloudflare's built-in media transformation service.</li>
<li><code>&lt;OPTIONS&gt;</code>: A comma-separated list of options. Refer to the available options below.</li>
<li><code>&lt;SOURCE-VIDEO&gt;</code>: A full URL (starting with <code>https://</code> or <code>http://</code>) of the original asset to resize.</li>
</ul>
<p>For example, this URL will source an HD video from an R2 bucket, shorten it, crop and resize it as a square, and remove the audio.</p>
<pre tabindex="0"><code>https://example.com/cdn-cgi/media/mode=video,time=5s,duration=5s,width=500,height=500,fit=crop,audio=false/https://pub-8613b7f94d6146408add8fefb52c52e8.r2.dev/aus-mobile-demo.mp4&#10;</code></pre>
<p>The result is an MP4 that can be used in an HTML video element without a player library.</p>
<h2 id="options">Options</h2>
<h3 id="mode"><code>mode</code></h3>
<p>Specifies the kind of output to generate.</p>
<ul>
<li><code>video</code>: Outputs an H.264/AAC optimized MP4 file.</li>
<li><code>frame</code>: Outputs a still image.</li>
<li><code>spritesheet</code>: Outputs a JPEG with multiple frames.</li>
<li><code>audio</code>: Outputs an AAC encoded M4A file.</li>
</ul>
<h3 id="time"><code>time</code></h3>
<p>Specifies when to start extracting the output in the input file. Depends on <code>mode</code>:</p>
<ul>
<li>When <code>mode</code> is <code>spritesheet</code>, <code>video</code>, or <code>audio</code>, specifies the timestamp where the output will start.</li>
<li>When <code>mode</code> is <code>frame</code>, specifies the timestamp from which to extract the still image.</li>
<li>Formats as a time string, for example: 5s, 2m</li>
<li>Acceptable range: 0 – 10m</li>
<li>Default: 0</li>
</ul>
<h3 id="duration"><code>duration</code></h3>
<p>The duration of the output video or spritesheet. Depends on <code>mode</code>:</p>
<ul>
<li>When <code>mode</code> is <code>video</code> or <code>audio</code>, specifies the duration of the output.</li>
<li>When <code>mode</code> is <code>spritesheet</code>, specifies the time range from which to select frames.</li>
<li>Acceptable range: 1s - 60s (or 1m)</li>
<li>Default: input duration or 60 seconds, whichever is shorter</li>
</ul>
<h3 id="fit"><code>fit</code></h3>
<p>In combination with <code>width</code> and <code>height</code>, specifies how to resize and crop the output. If the output is resized, it will always resize proportionally so content is not stretched.</p>
<ul>
<li><code>contain</code>: Respecting aspect ratio, scales a video up or down to be entirely contained within output dimensions.</li>
<li><code>scale-down</code>: Same as contain, but downscales to fit only. Do not upscale.</li>
<li><code>cover</code>: Respecting aspect ratio, scales a video up or down to entirely cover the output dimensions, with a center-weighted crop of the remainder.</li>
</ul>
<h3 id="height"><code>height</code></h3>
<p>Specifies maximum height of the output in pixels. Exact behavior depends on <code>fit</code>.</p>
<ul>
<li>Acceptable range: 10-2000 pixels</li>
</ul>
<h3 id="width"><code>width</code></h3>
<p>Specifies the maximum width of the image in pixels. Exact behavior depends on <code>fit</code>.</p>
<ul>
<li>Acceptable range: 10-2000 pixels</li>
</ul>
<h3 id="audio"><code>audio</code></h3>
<p>When <code>mode</code> is <code>video</code>, specifies whether or not to include the source audio in the output.</p>
<ul>
<li><code>true</code>: Includes source audio.</li>
<li><code>false</code>: Output will be silent.</li>
<li>Default: <code>true</code></li>
</ul>
<p>When <code>mode</code> is <code>audio</code>, audio cannot be false.</p>
<h3 id="format"><code>format</code></h3>
<p>If <code>mode</code> is <code>frame</code>, specifies the image output format.</p>
<ul>
<li>Acceptable options: <code>jpg</code>, <code>png</code></li>
</ul>
<p>If <code>mode</code> is <code>audio</code>, specifies the audio output format.</p>
<ul>
<li>Acceptable options: <code>m4a</code> (default)</li>
</ul>
<h3 id="filename"><code>filename</code></h3>
<p>Specifies the filename to use in the returned Content-Disposition header. If not specified, the filename will be derived from the source URL.</p>
<ul>
<li>Acceptable values:
<ul>
<li>Maximum of 120 characters in length.</li>
<li>Can only contain lowercase letters (a-z), numbers (0-9), hyphens (-), underscores (_), and an optional extension. A valid name satisfies this regular expression: <code>^[a-zA-Z0-9-_]+.?[a-zA-Z0-9-_]+$</code>.</li>
</ul>
</li>
<li>Examples: <code>default.mp4</code>, <code>shortened-clip_5s</code></li>
</ul>
<h2 id="source-video-requirements">Source video requirements</h2>
<ul>
<li>Input video must be less than 100MB.</li>
<li>Input video should be an MP4 with H.264 encoded video and AAC or MP3 encoded audio. Other formats may work but are untested.</li>
<li>Origin must support either HTTP HEAD and range requests, and must return a Content-Range header.</li>
</ul>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Maximum input file size is 100 MB. Maximum duration of input video is 10 minutes.</li>
<li>Media Transformations are not compatible with <a href="/byoip/">Bring Your Own IP (BYOIP)</a>.</li>
<li>Input video should be an MP4 with H.264 encoded video and AAC or MP3 encoded audio, or animated GIF. Other formats may work but are untested.</li>
</ul>
<p>When using Media Transformations from a Cloudflare Worker, we recommend using the <a href="/stream/transform-videos/bindings/">bindings</a>. Otherwise, if the Worker is calling Media Transformations on the same zone used as its trigger, apply the <code>global_fetch_strictly_public</code> compatibility flag to avoid 404 errors on <code>/cdn-cgi/media</code> paths.</p>
<h2 id="pricing">Pricing</h2>
<p>After November 1st, 2025, Media Transformations and Image Transformations will use the same subscriptions and usage metrics.</p>
<ul>
<li>Generating a still frame (single image) from a video counts as 1 transformation.</li>
<li>Generating an optimized video or extracting audio counts as 1 transformation <em>per second of the output</em> content.</li>
<li>Each unique transformation, as determined by input and unique combination of flags, is only billed once per calendar month.</li>
<li>All Media and Image Transformations cost $0.50 per 1,000 monthly unique transformation operations, with a free monthly allocation of 5,000.</li>
</ul>
