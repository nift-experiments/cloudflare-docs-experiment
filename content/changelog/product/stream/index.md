---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/stream/
  description: '2026-07-31'
  full_title: stream changelog | Cloudflare Docs
  head_html: <title>stream changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-07-31"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/stream/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="stream changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-07-31"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/stream/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/stream/#page","headline":"stream changelog | Cloudflare Docs","description":"2026-07-31","url":"https://developers.cloudflare.com/changelog/product/stream/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/stream/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="rotate-stream-broadcast-keys-for-live-inputs"><a href="/changelog/post/2026-07-30-rotate-stream-broadcast-keys/">Rotate Stream broadcast keys for live inputs</a></h2>
<p><em>2026-07-31</em></p>
<p>You can now rotate the broadcast credentials for a Stream live input without changing the live input identifier.</p>
<p>Use key rotation when live input credentials may have been shared with the wrong audience, exposed in client code or a screenshare, or need to be refreshed as part of your security process. Rotating keys revokes the old credentials, disconnects broadcasts using stale credentials, and returns refreshed credentials in the API response.</p>
<p>To rotate keys for a live input, make a <code>POST</code> request to the <code>rotate_keys</code> endpoint:</p>
<pre tabindex="0"><code class="language-bash">curl --request POST \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/rotate_keys \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>Live input responses now also include <code>keysRotatedAt</code>, which indicates when the live input keys were last rotated. This field is omitted for live inputs whose keys have never been rotated.</p>
<p>For endpoint details, refer to <a href="/api/resources/stream/subresources/live_inputs/methods/rotate_keys/">Rotate keys for a live input</a>. For usage guidance, refer to <a href="/stream/stream-live/start-stream-live/#manage-live-inputs">Manage live inputs</a>.</p>


<h2 id="introducing-stream-bindings-for-workers"><a href="/changelog/post/2026-05-07-stream-workers-binding/">Introducing Stream Bindings for Workers</a></h2>
<p><em>2026-05-07</em></p>
<p>You can now interact with your Stream video library using new bindings for Workers! This allows customers to upload content to Stream, provision direct uploads, manage videos, and generate signed URLs from a Worker without making authenticated API calls. We're excited to bring Stream and Workers closer together to empower more programmatic pipelines, tighter integrations, and support generative AI and inference workloads.</p>
<p>Use the Stream binding when you want to:</p>
<ul>
<li>Upload videos from URLs or create basic direct upload links for end users</li>
<li>Generate signed playback tokens without managing signing keys</li>
<li>Manage video metadata, captions, downloads, and watermarks</li>
<li>Build video pipelines entirely within Workers</li>
</ul>
<p>To get started, add the Stream binding to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17756.md")</div>
<p><strong>Generate a video with AI and upload directly to Stream</strong> or send a URL of a file you already have:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17757.md")</div>
<p><strong>Generate a signed URL without using a signing key</strong> or an API call:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17758.md")</div>
<p><strong>Get and set video properties</strong> easily:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17759.md")</div>
<p>For setup instructions and the full API reference, refer to <a href="/stream/manage-video-library/bindings/">Bind to Workers API</a>.</p>
<h4 id="2026-05-07-stream-workers-binding-get-started-with-your-agent">Get started with your Agent</h4>
<blockquote>
<p>Add a binding for Cloudflare Stream (env.STREAM). On the watch page, use the
Stream binding to get info based on the ID, and leverage video.meta.name as
the page title.</p>
</blockquote>


<h2 id="media-transformations-binding-for-workers"><a href="/changelog/post/2026-03-18-media-transformations-workers-binding/">Media Transformations binding for Workers</a></h2>
<p><em>2026-03-18</em></p>
<p>You can now use a Workers binding to transform videos with Media Transformations. This allows you to resize, crop, extract frames, and extract audio from videos stored anywhere, even in private locations like R2 buckets.</p>
<p>The Media Transformations binding is useful when you want to:</p>
<ul>
<li>Transform videos stored in private or protected sources</li>
<li>Optimize videos and store the output directly back to R2 for re-use</li>
<li>Extract still frames for classification or description with Workers AI</li>
<li>Extract audio tracks for transcription using Workers AI</li>
</ul>
<p>To get started, add the Media binding to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17754.md")</div>
<p>Then use the binding in your Worker to transform videos:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17755.md")</div>
<p>Output modes include <code>video</code> for optimized MP4 clips, <code>frame</code> for still images, <code>spritesheet</code> for multiple frames, and <code>audio</code> for M4A extraction.</p>
<p>For more information, refer to the <a href="/stream/transform-videos/bindings/">Media Transformations binding documentation</a>.</p>


<h2 id="stream-live-inputs-can-now-be-disabled-and-enabled"><a href="/changelog/post/2026-02-24-disable-live-inputs/">Stream live inputs can now be disabled and enabled</a></h2>
<p><em>2026-02-24</em></p>
<p>You can now disable a live input to reject incoming RTMPS and SRT
connections. When a live input is disabled, any broadcast attempts will fail to
connect.</p>
<p>This gives you more control over your live inputs:</p>
<ul>
<li>Temporarily pause an input without deleting it</li>
<li>Programmatically end creator broadcasts</li>
<li>Prevent new broadcasts from starting on a specific input</li>
</ul>
<p>To disable a live input via the API, set the <code>enabled</code> property to <code>false</code>:</p>
<pre tabindex="0"><code class="language-bash">curl --request PUT \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/live_inputs/{input_id} \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-data &#x27;{&quot;enabled&quot;: false}&#x27;&#10;</code></pre>
<p>You can also disable or enable a live input from the <strong>Live inputs</strong> list page
or the live input detail page in the Dashboard.</p>
<p>All existing live inputs remain enabled by default. For more information, refer
to <a href="/stream/stream-live/start-stream-live/">Start a live stream</a>.</p>


<h2 id="introducing-observability-and-metrics-for-stream-live-inputs"><a href="/changelog/post/2025-08-08-stream-live-observability/">Introducing observability and metrics for Stream Live Inputs</a></h2>
<p><em>2025-08-08</em></p>
<p>New information about broadcast metrics and events is now available in
<a href="/stream/">Cloudflare Stream</a> in the Live Input details of the Dashboard.</p>
<p><img src="/assets/upstream/images/changelog/stream/2025-08-05-live-input-metrics.png" alt="Live Input details showing metrics" /></p>
<p>You can now easily understand broadcast-side health and performance with new
observability, which can help when troubleshooting common issues, particularly
for new customers who are just getting started, and platform customers who may
have limited visibility into how their end-users configure their encoders.</p>
<p>To get started, start a live stream (<a href="/stream/examples/obs-from-scratch/">just getting started?</a>), then visit the Live Input details page in Dash.</p>
<p>See our new live <a href="/stream/stream-live/troubleshooting/">Troubleshooting</a> guide
to learn what these metrics mean and how to use them to address common broadcast
issues.</p>


<h2 id="audio-mode-for-media-transformations"><a href="/changelog/post/2025-07-22-media-transformations-audio-mode/">Audio mode for Media Transformations</a></h2>
<p><em>2025-07-22</em></p>
<p>We now support <code>audio</code> mode! Use this feature to extract audio from a source video, outputting
an M4A file to use in downstream workflows like <a href="/workers-ai/">AI inference</a>, content moderation, or transcription.</p>
<p>For example,</p>
<pre tabindex="0"><code class="language-text">https://example.com/cdn-cgi/media/&lt;OPTIONS&gt;/&lt;SOURCE-VIDEO&gt;&#10;https://example.com/cdn-cgi/media/mode=audio,time=3s,duration=60s/&lt;input video with diction&gt;&#10;</code></pre>
<p>For more information, learn about <a href="/stream/transform-videos/">Transforming Videos</a>.</p>


<h2 id="increased-limits-for-media-transformations"><a href="/changelog/post/2025-06-10-media-transformations-limits-increase/">Increased limits for Media Transformations</a></h2>
<p><em>2025-06-10</em></p>
<p>We have increased the limits for <a href="/stream/transform-videos/">Media Transformations</a>:</p>
<ul>
<li>Input file size limit is now 100MB (was 40MB)</li>
<li>Output video duration limit is now 1 minute (was 30 seconds)</li>
</ul>
<p>Additionally, we have improved caching of the input asset, resulting in fewer
requests to origin storage even when transformation options may differ.</p>
<p>For more information, learn about <a href="/stream/transform-videos/">Transforming Videos</a>.</p>


<h2 id="introducing-origin-restrictions-for-media-transformations"><a href="/changelog/post/2025-05-14-media-transformations-origin-restrictions/">Introducing Origin Restrictions for Media Transformations</a></h2>
<p><em>2025-05-14</em></p>
<p>We are adding <a href="/stream/transform-videos/sources/">source origin restrictions</a> to
the Media Transformations beta. This allows customers to restrict what sources
can be used to fetch images and video for transformations. This feature is the
same as --- and uses the same settings as ---
<a href="/images/optimization/transformations/sources/">Image Transformations sources</a>.</p>
<p>When transformations is first enabled, the default setting only allows
transformations on images and media from the same website or domain being used to make
the transformation request. In other words, by default, requests to
<code>example.com/cdn-cgi/media</code> can only reference originals on <code>example.com</code>.</p>
<p><img src="/assets/upstream/images/images/allowed-origins.png" alt="Enable allowed origins from the Cloudflare dashboard" /></p>
<p>Adding access to other sources, or allowing any source,
<a href="/images/optimization/transformations/sources/">is easy to do</a>
in the <strong>Transformations</strong> tab under <strong>Stream</strong>. Click each domain enabled for
Transformations and set its sources list to match the needs of your content. The
user making this change will need permission to edit zone settings.</p>
<p>For more information, learn about <a href="/stream/transform-videos/">Transforming Videos</a>.</p>


<h2 id="signed-urls-and-infrastructure-improvements-on-stream-live-webrtc-beta"><a href="/changelog/post/2025-04-14-webrtc-beta-signed-urls/">Signed URLs and Infrastructure Improvements on Stream Live WebRTC Beta</a></h2>
<p><em>2025-04-11</em></p>
<p>Cloudflare <a href="/stream/">Stream</a> has completed an infrastructure upgrade for our <a href="/stream/webrtc-beta/">Live WebRTC beta</a> support which brings increased scalability and improved playback performance to all customers. WebRTC allows broadcasting directly from a browser (or supported WHIP client) with ultra-low latency to tens of thousands of concurrent viewers across the globe.</p>
<p>Additionally, as part of this upgrade, the WebRTC beta now supports Signed URLs to protect playback, just like our standard live stream options (HLS/DASH).</p>
<p>For more information, learn about the <a href="/stream/webrtc-beta/">Stream Live WebRTC beta</a>.</p>


<h2 id="introducing-media-transformations-from-cloudflare-stream"><a href="/changelog/post/2025-03-06-media-transformations/">Introducing Media Transformations from Cloudflare Stream</a></h2>
<p><em>2025-03-06</em></p>
<p>Today, we are thrilled to announce Media Transformations, a new service that
brings the magic of <a href="/images/optimization/transformations/overview/">Image Transformations</a> to
<em>short-form video files,</em> wherever they are stored!</p>
<p>For customers with a huge volume of short video — generative AI output,
e-commerce product videos, social media clips, or short marketing content —
uploading those assets to Stream is not always practical. Sometimes, the
greatest friction to getting started was the thought of all that migrating.
Customers want a simpler solution that retains their current storage strategy to
deliver small, optimized MP4 files. Now you can do that with Media
Transformations.</p>
<p>To transform a video or image,
<a href="/stream/transform-videos/#getting-started">enable transformations</a> for your
zone, then make a simple request with a specially formatted URL. The result is
an MP4 that can be used in an HTML video element without a player library.
If your zone already has Image Transformations enabled, then it is ready to
optimize videos with Media Transformations, too.</p>
<pre tabindex="0"><code class="language-text">https://example.com/cdn-cgi/media/&lt;OPTIONS&gt;/&lt;SOURCE-VIDEO&gt;&#10;</code></pre>
<p>For example, we have a short video of the mobile in Austin's office. The
original is nearly 30 megabytes and wider than necessary for this layout.
Consider a simple width adjustment:</p>
<video controls>
	<source src="https://developers.cloudflare.com/cdn-cgi/media/width=640/https://middlecache.ced.cloudflare.com/v1/aus-mobile/aus-mobile.mp4" />
</video>
<pre tabindex="0"><code class="language-text">https://example.com/cdn-cgi/media/width=640/&lt;SOURCE-VIDEO&gt;&#10;https://developers.cloudflare.com/cdn-cgi/media/width=640/https://middlecache.ced.cloudflare.com/v1/aus-mobile/aus-mobile.mp4&#10;</code></pre>
<p>The result is less than 3 megabytes, properly sized, and delivered dynamically
so that customers do not have to manage the creation and storage of these
transformed assets.</p>
<p>For more information, learn about <a href="/stream/transform-videos/">Transforming Videos</a>.</p>


<h2 id="rewind-replay-resume-introducing-dvr-for-stream-live"><a href="/changelog/post/2025-02-14-introducing-dvr-for-stream-live/">Rewind, Replay, Resume: Introducing DVR for Stream Live</a></h2>
<p><em>2025-02-14</em></p>
<p>Previously, all viewers watched &quot;the live edge,&quot; or the latest content of the
broadcast, synchronously. If a viewer paused for more than a few seconds,
the player would automatically &quot;catch up&quot; when playback started again. Seeking
through the broadcast was only available once the recording was available after
it concluded.</p>
<p>Starting today, customers can make a small adjustment to the player
embed or manifest URL to enable the DVR experience for their viewers. By
offering this feature as an opt-in adjustment, our customers are empowered to
pick the best experiences for their applications.</p>
<p>When building a player embed code or manifest URL, just add <code>dvrEnabled=true</code> as
a query parameter. There are some things to be aware of when using this option.
For more information, refer to <a href="/stream/stream-live/dvr-for-live/">DVR for Live</a>.</p>


<h2 id="expanded-language-support-for-stream-ai-generated-captions"><a href="/changelog/post/2025-01-30-stream-generated-captions-new-languages/">Expanded language support for Stream AI Generated Captions</a></h2>
<p><em>2025-01-30</em></p>
<p>Stream's <a href="/stream/edit-videos/adding-captions/#generate-a-caption">generated captions</a>
leverage Workers AI to automatically transcribe audio and provide captions to
the player experience. We have added support for these languages:</p>
<ul>
<li><code>cs</code> - Czech</li>
<li><code>nl</code> - Dutch</li>
<li><code>fr</code> - French</li>
<li><code>de</code> - German</li>
<li><code>it</code> - Italian</li>
<li><code>ja</code> - Japanese</li>
<li><code>ko</code> - Korean</li>
<li><code>pl</code> - Polish</li>
<li><code>pt</code> - Portuguese</li>
<li><code>ru</code> - Russian</li>
<li><code>es</code> - Spanish</li>
</ul>
<p>For more information, learn about <a href="/stream/edit-videos/adding-captions/">adding captions to videos</a>.</p>



