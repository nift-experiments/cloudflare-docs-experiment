---
cp9:
  canonical: https://developers.cloudflare.com/stream/stream-live/start-stream-live/
  description: Create live inputs and broadcast live video to Cloudflare Stream using RTMPS or SRT.
  full_title: Start a live stream · Cloudflare Stream docs
  head_html: <title>Start a live stream · Cloudflare Stream docs</title><meta name="generator" content="Nift"><meta name="description" content="Create live inputs and broadcast live video to Cloudflare Stream using RTMPS or SRT."><link rel="canonical" href="https://developers.cloudflare.com/stream/stream-live/start-stream-live/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/stream/stream-live/start-stream-live/index.md"><meta property="og:title" content="Start a live stream · Cloudflare Stream docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create live inputs and broadcast live video to Cloudflare Stream using RTMPS or SRT."><meta property="og:url" content="https://developers.cloudflare.com/stream/stream-live/start-stream-live/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Stream"><meta name="algolia_product_filter" content="Stream"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Stream"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/stream/stream-live/start-stream-live/#page","headline":"Start a live stream \u00b7 Cloudflare Stream docs","description":"Create live inputs and broadcast live video to Cloudflare Stream using RTMPS or SRT.","url":"https://developers.cloudflare.com/stream/stream-live/start-stream-live/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /stream/stream-live/start-stream-live/
  schema: 1
---
<p>After you subscribe to Stream, you can create Live Inputs in Dash or via the API. Broadcast to your new Live Input using RTMPS or SRT. SRT supports newer video codecs and makes using accessibility features, such as captions and multiple audio tracks, easier.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14401.md")
</aside>
<p><strong>First time live streaming?</strong> You will need software to send your video to Cloudflare. <a href="/stream/examples/obs-from-scratch/">Learn how to go live on Stream using OBS Studio</a>.</p>
<h2 id="use-the-dashboard">Use the dashboard</h2>
<p><strong>Step 1:</strong> In the Cloudflare dashboard, go to the <strong>Live inputs</strong> page and create a live input.</p>
<div class="nb-dash-button"></div>
<p><img src="/assets/upstream/images/stream/create-live-input-from-stream-dashboard.png" alt="Create live input field from dashboard" /></p>
<p><strong>Step 2:</strong> Copy the RTMPS URL and key, and use them with your live streaming application. We recommend using <a href="https://obsproject.com/">Open Broadcaster Software (OBS)</a> to get started.</p>
<p><img src="/assets/upstream/images/stream/copy-rtmps-url-from-stream-dashboard.png" alt="Example of RTMPS URL field" /></p>
<p><strong>Step 3:</strong> Go live and preview your live stream in the Stream Dashboard</p>
<p>In the Stream Dashboard, within seconds of going live, you will see a preview of what your viewers will see. To add live video playback to your website or app, refer to <a href="/stream/viewing-videos">Play videos</a>.</p>
<h2 id="use-the-api">Use the API</h2>
<p>To start a live stream programmatically, make a <code>POST</code> request to the <code>/live_inputs</code> endpoint:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-data &#x27;{&quot;meta&quot;: {&quot;name&quot;:&quot;test stream&quot;},&quot;recording&quot;: { &quot;mode&quot;: &quot;automatic&quot; }}&#x27; \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/live_inputs&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;uid&quot;: &quot;f256e6ea9341d51eea64c9454659e576&quot;,&#10;	&quot;rtmps&quot;: {&#10;		&quot;url&quot;: &quot;rtmps://live.cloudflare.com:443/live/&quot;,&#10;		&quot;streamKey&quot;: &quot;MTQ0MTcjM3MjI1NDE3ODIyNTI1MjYyMjE4NTI2ODI1NDcxMzUyMzcf256e6ea9351d51eea64c9454659e576&quot;&#10;	},&#10;	&quot;created&quot;: &quot;2021-09-23T05:05:53.451415Z&quot;,&#10;	&quot;modified&quot;: &quot;2021-09-23T05:05:53.451415Z&quot;,&#10;	&quot;meta&quot;: {&#10;		&quot;name&quot;: &quot;test stream&quot;&#10;	},&#10;	&quot;status&quot;: null,&#10;	&quot;recording&quot;: {&#10;		&quot;mode&quot;: &quot;automatic&quot;,&#10;		&quot;requireSignedURLs&quot;: false,&#10;		&quot;allowedOrigins&quot;: null,&#10;		&quot;hideLiveViewerCount&quot;: false&#10;	},&#10;	&quot;enabled&quot;: true,&#10;	&quot;deleteRecordingAfterDays&quot;: null,&#10;	&quot;preferLowLatency&quot;: false&#10;}&#10;</code></pre>
<h4 id="optional-api-parameters">Optional API parameters</h4>
<p><a href="/api/resources/stream/subresources/live_inputs/methods/create/">API Reference Docs for <code>/live_inputs</code></a></p>
<ul>
<li>
<p><code>enabled</code> boolean default: <code>true</code></p>
<ul>
<li>Controls whether the live input accepts incoming broadcasts. When set to <code>false</code>, the live input will reject any incoming RTMPS or SRT connections. Use this property to programmatically end creator broadcasts or prevent new broadcasts from starting on a specific input.</li>
</ul>
</li>
<li>
<p><code>preferLowLatency</code> boolean default: <code>false</code> <span class="nb-badge">Beta</span></p>
<ul>
<li>When set to true, this live input will be enabled for the beta Low-Latency HLS pipeline. The Stream built-in player will automatically use LL-HLS when possible. (Recording <code>mode</code> property must also be set to <code>automatic</code>.)</li>
</ul>
</li>
<li>
<p><code>deleteRecordingAfterDays</code> integer default: <code>null</code> (any)</p>
<ul>
<li>
<p>Specifies a date and time when the recording, not the input, will be deleted. This property applies from the time the recording is made available and ready to stream. After the recording is deleted, it is no longer viewable and no longer counts towards storage for billing. Minimum value is <code>30</code>, maximum value is <code>1096</code>.</p>
<p>When the stream ends, a <code>scheduledDeletion</code> timestamp is calculated using the <code>deleteRecordingAfterDays</code> value if present.</p>
<p>Note that if the value is added to a live input while a stream is live, the property will only apply to future streams.</p>
</li>
</ul>
</li>
<li>
<p><code>timeoutSeconds</code> integer default: <code>0</code></p>
<ul>
<li>The <code>timeoutSeconds</code> property specifies how long a live feed can be disconnected before it results in a new video being created.</li>
</ul>
</li>
</ul>
<p>The following four properties are nested under the <code>recording</code> object.</p>
<ul>
<li>
<p><code>mode</code> string default: <code>off</code></p>
<ul>
<li>When the mode property is set to <code>automatic</code>, the live stream will be automatically available for viewing using HLS/DASH. In addition, the live stream will be automatically recorded for later replays. By default, recording mode is set to <code>off</code>, and the input will not be recorded or available for playback.</li>
</ul>
</li>
<li>
<p><code>requireSignedURLs</code> boolean default: <code>false</code></p>
<ul>
<li>The <code>requireSignedURLs</code> property indicates if signed URLs are required to view the video. This setting is applied by default to all videos recorded from the input. In addition, if viewing a video via the live input ID, this field takes effect over any video-level settings.</li>
</ul>
</li>
<li>
<p><code>allowedOrigins</code> integer default: <code>null</code> (any)</p>
<ul>
<li>The <code>allowedOrigins</code> property can optionally be invoked to provide a list of allowed origins. This setting is applied by default to all videos recorded from the input. In addition, if viewing a video via the live input ID, this field takes effect over any video-level settings.</li>
</ul>
</li>
<li>
<p><code>hideLiveViewerCount</code> boolean default: <code>false</code></p>
<ul>
<li>Restrict access to the live viewer count and remove the value from the player.</li>
</ul>
</li>
</ul>
<h2 id="manage-live-inputs">Manage live inputs</h2>
<h3 id="update-a-live-input">Update a live input</h3>
<p>Update a live input by making a <code>PUT</code> request:</p>
<pre tabindex="0"><code class="language-bash">curl --request PUT \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/live_inputs/{input_id} \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-data &#x27;{&quot;meta&quot;: {&quot;name&quot;:&quot;test stream 1&quot;},&quot;recording&quot;: { &quot;mode&quot;: &quot;automatic&quot;, &quot;timeoutSeconds&quot;: 10 }}&#x27;&#10;</code></pre>
<h3 id="enable-or-disable-a-live-input">Enable or disable a live input</h3>
<p>Live inputs are enabled by default. When a live input is disabled, it rejects incoming RTMPS and SRT connections. Use this to temporarily pause a live input without deleting it, terminate active broadcasts, and prevent new broadcasts from starting on a specific input.</p>
<p>To disable a live input, set <code>enabled</code> to <code>false</code>:</p>
<pre tabindex="0"><code class="language-bash">curl --request PUT \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/live_inputs/{input_id} \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-data &#x27;{&quot;enabled&quot;: false}&#x27;&#10;</code></pre>
<p>To enable the live input again, set <code>enabled</code> to <code>true</code>:</p>
<pre tabindex="0"><code class="language-bash">curl --request PUT \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/live_inputs/{input_id} \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-data &#x27;{&quot;enabled&quot;: true}&#x27;&#10;</code></pre>
<h3 id="rotate-broadcast-keys">Rotate broadcast keys</h3>
<p>Rotate the broadcast credentials for a live input when credentials may have been shared with the wrong audience, exposed in client code or a screenshare, or need to be refreshed as part of your security process. Rotating keys does not change the live input ID or its other configuration.</p>
<p>When keys are rotated, old credentials are revoked, broadcasts using stale credentials are disconnected, and refreshed credentials are returned in the API response.</p>
<pre tabindex="0"><code class="language-bash">curl --request POST \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/live_inputs/{input_id}/rotate_keys \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>Live input responses include <code>keysRotatedAt</code>, which indicates when the live input keys were last rotated. This field is omitted for live inputs whose keys have never been rotated.</p>
<h3 id="delete-a-live-input">Delete a live input</h3>
<p>Delete a live input by making a <code>DELETE</code> request:</p>
<pre tabindex="0"><code class="language-bash">curl --request DELETE \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/live_inputs/{input_id} \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<h2 id="recommendations-requirements-and-limitations">Recommendations, requirements and limitations</h2>
<p>If you are experiencing buffering, freezing, experiencing latency, or having other similar issues, visit <a href="/stream/stream-live/troubleshooting/">live stream troubleshooting</a>.</p>
<h3 id="recommendations">Recommendations</h3>
<ul>
<li>Your creators should use an appropriate bitrate for their live streams, typically well under 12Mbps (12000Kbps). High motion, high frame rate content typically should use a higher bitrate, while low motion content like slide presentations should use a lower bitrate.</li>
<li>Your creators should use a <a href="https://en.wikipedia.org/wiki/Group_of_pictures">GOP duration</a> (keyframe interval) of between 2 to 8 seconds. The default in most encoding software and hardware, including Open Broadcaster Software (OBS), is within this range. Setting a lower GOP duration will reduce latency for viewers, while also reducing encoding efficiency. Setting a higher GOP duration will improve encoding efficiency, while increasing latency for viewers. This is a tradeoff inherent to video encoding, and not a limitation of Cloudflare Stream.</li>
<li>When possible, select CBR (constant bitrate) instead of VBR (variable bitrate) as CBR helps to ensure a stable streaming experience while preventing buffering and interruptions.</li>
</ul>
<h4 id="low-latency-hls-broadcast-recommendations">Low-Latency HLS broadcast recommendations <span class="nb-badge">Beta</span></h4>
<ul>
<li>Turn off B Frames or set them to 0. B Frames are incompatible with LL-HLS and will result in jitter and sporadic buffering delays.</li>
<li>For lowest latency, use a GOP size (or &quot;keyframe interval&quot;) of 2 - 4 seconds.</li>
<li>Broadcast to the RTMP endpoint if possible, SRT otherwise.</li>
<li>If using OBS, select the &quot;ultra low&quot; latency profile.</li>
</ul>
<h3 id="requirements">Requirements</h3>
<ul>
<li>Closed GOPs are required. This means that if there are any B frames in the video, they should always refer to frames within the same GOP. This setting is the default in most encoding software and hardware, including <a href="https://obsproject.com/">OBS Studio</a>.</li>
<li>Stream Live only supports H.264 video and AAC audio codecs as inputs. This requirement does not apply to inputs that are relayed to Stream Connect outputs. Stream Live supports ADTS but does not presently support LATM.</li>
<li>Clients must be configured to reconnect when a disconnection occurs. Stream Live is designed to handle reconnection gracefully by continuing the live stream.</li>
</ul>
<h3 id="limitations">Limitations</h3>
<ul>
<li>Watermarks cannot yet be used with live videos.</li>
<li>If a live video exceeds seven days in length, the recording will be truncated to seven days. Only the first seven days of live video content will be recorded.</li>
</ul>
