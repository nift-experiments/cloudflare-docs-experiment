---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/media/
  description: '2026-09-02'
  full_title: Media changelog | Cloudflare Docs
  head_html: <title>Media changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-09-02"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/media/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Media changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-09-02"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/media/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/media/#page","headline":"Media changelog | Cloudflare Docs","description":"2026-09-02","url":"https://developers.cloudflare.com/changelog/product-group/media/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/media/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="new-in-images-text-rasterization-and-updates-to-the-binding"><a href="/changelog/post/2026-09-02-images-binding-updates/">New in Images: text rasterization and updates to the binding</a></h2>
<p><em>2026-09-02</em></p>
<p>We've added more ways to manage and manipulate images with the <a href="/images/optimization/binding/">Images binding</a>. Here's what's new:</p>
<p><strong>Render text into an image.</strong> Output a string of text into its own image or draw it over another image.</p>
<ul>
<li>Use the <a href="/images/optimization/binding/#textcontent-options"><code>.text()</code></a> method to rasterize text with the Images binding.</li>
<li>Style content using the <code>font</code>, <code>size</code>, and <code>color</code> options.</li>
<li>The <a href="/images/optimization/draw-overlays/#draw-with-cfimage"><code>draw</code></a> array in <code>cf.image</code> now accepts a <code>text</code> key.</li>
</ul>
<p><strong>Manage hosted images without an API token.</strong></p>
<ul>
<li><strong>Metadata filtering:</strong> Pass <code>filter.metadata</code> to <a href="/images/storage/binding/#listoptions"><code>.list()</code></a> to return images by custom metadata. Match a bounded range by setting two operators in one condition, for example, <code>priority: { gte: 2, lte: 5 }</code>.</li>
<li><strong>Server-side signing:</strong> Get a signed URL for a private image with <a href="/images/storage/binding/#imageimageidsignedurloptions"><code>.signedUrl()</code></a>.</li>
<li><strong>User uploads:</strong> Create a Direct Creator Upload link with <a href="/images/storage/binding/#createdirectuploadoptions"><code>.createDirectUpload()</code></a> so that a client can upload an image to your storage.</li>
</ul>
<p><strong>Set headers in a single call.</strong></p>
<ul>
<li>Pass a <code>headers</code> option to <a href="/images/optimization/binding/#responseoptions"><code>.response()</code></a> to set headers without rebuilding the <code>Response</code>.</li>
<li><code>Content-Type</code> is always taken from the optimized image and can't be overridden by a specified header.</li>
<li>Set <code>Cache-Control</code> with <a href="/workers/cache/">Workers Cache</a> to cache your optimized image at the edge.</li>
</ul>
<p>For more information, refer to <a href="/images/optimization/binding/">Optimize with Workers</a>, <a href="/images/optimization/draw-overlays/">Draw overlays and watermarks</a>, and <a href="/images/storage/binding/">Manage hosted images with Workers</a>.</p>


<h2 id="control-realtime-sfu-datachannel-delivery"><a href="/changelog/post/2026-08-13-datachannels-reliability-ordering/">Control Realtime SFU DataChannel delivery</a></h2>
<p><em>2026-08-13</em></p>
<p><a href="/realtime/sfu/">Cloudflare Realtime SFU</a> is a <a href="/realtime/sfu/calls-vs-sfus/">WebRTC selective forwarding unit</a> that runs on Cloudflare's global network. It forwards audio, video, and application data between WebRTC clients without requiring you to manage SFU infrastructure or regions.</p>
<p><a href="/realtime/sfu/datachannels/">DataChannels</a> are WebRTC channels for application messages. A client publishes a named DataChannel to Realtime SFU, and the SFU forwards its messages to every client that subscribes to that channel. Use DataChannels for low-latency payloads such as chat messages, game state, sensor updates, and control events.</p>
<h4 id="2026-08-13-datachannels-reliability-ordering-what-changed">What changed</h4>
<p>Realtime SFU DataChannels now support unordered and partially reliable delivery. DataChannels remain reliable and ordered by default, so existing channels keep their current behavior.</p>
<p>With ordered delivery, a delayed message can block later messages. For game state or sensor updates, recent data may be more useful than recovering an older message. Unordered delivery lets later messages proceed, while partial reliability limits retransmission attempts or delivery time.</p>
<h4 id="2026-08-13-datachannels-reliability-ordering-choose-delivery-behavior">Choose delivery behavior</h4>
<p>Delivery settings answer two questions: whether newer messages can bypass a delayed message, and when the transport should stop retrying delivery.</p>
<p>Choose the policy that matches how long your payload remains useful:</p>
<table>
<thead>
<tr>
<th>Goal</th>
<th>Settings</th>
<th>Use when</th>
</tr>
</thead>
<tbody>
<tr>
<td>Reliable, ordered delivery (default)</td>
<td>Omit <code>ordered</code>, <code>maxRetransmits</code>, and <code>maxPacketLifeTime</code></td>
<td>Messages remain useful and must arrive in order</td>
</tr>
<tr>
<td>Reliable, unordered delivery</td>
<td>Set <code>ordered: false</code>; omit both retry fields</td>
<td>Messages remain useful, but later messages should not wait for earlier messages</td>
</tr>
<tr>
<td>No retries or ordering</td>
<td>Set <code>ordered: false</code> and <code>maxRetransmits: 0</code></td>
<td>The application tolerates message loss and discards out-of-date updates</td>
</tr>
<tr>
<td>Limited retries</td>
<td>Set <code>maxRetransmits: &lt;COUNT&gt;</code></td>
<td>Brief recovery is useful, but repeated retries are not</td>
</tr>
<tr>
<td>Time-bounded delivery</td>
<td>Set <code>maxPacketLifeTime: &lt;MILLISECONDS&gt;</code></td>
<td>A message loses value after a known time window</td>
</tr>
</tbody>
</table>
<p><code>ordered</code> controls ordering independently from retries. <code>maxRetransmits</code> and <code>maxPacketLifeTime</code> are alternative retry budgets, so set at most one for each channel. Omit both for reliable delivery, whether ordered or unordered.</p>
<h4 id="2026-08-13-datachannels-reliability-ordering-apply-the-policy-end-to-end">Apply the policy end to end</h4>
<p>Realtime DataChannels use negotiated IDs, so browsers do not receive delivery settings from the remote peer. Apply the same settings when the publisher creates the local channel, each subscriber pulls the remote channel, and each client calls <code>createDataChannel()</code>.</p>
<p>The following example configures unordered delivery with no retransmissions. It begins after you <a href="/realtime/sfu/datachannels/#set-up-a-datachannel">establish a DataChannel transport on both sessions and complete any required SDP exchange</a>. Run the API requests from your backend with <code>APP_ID</code>, <code>APP_TOKEN</code>, <code>PUBLISHER_SESSION_ID</code>, and <code>SUBSCRIBER_SESSION_ID</code> set in your environment.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17744.md")</div>
<h4 id="2026-08-13-datachannels-reliability-ordering-related-documentation">Related documentation</h4>
<ul>
<li><a href="/realtime/sfu/">Realtime SFU overview</a></li>
<li><a href="/realtime/sfu/datachannels/">DataChannels</a></li>
<li><a href="/realtime/sfu/https-api/">Connection API</a></li>
</ul>


<h2 id="rotate-stream-broadcast-keys-for-live-inputs"><a href="/changelog/post/2026-07-30-rotate-stream-broadcast-keys/">Rotate Stream broadcast keys for live inputs</a></h2>
<p><em>2026-07-31</em></p>
<p>You can now rotate the broadcast credentials for a Stream live input without changing the live input identifier.</p>
<p>Use key rotation when live input credentials may have been shared with the wrong audience, exposed in client code or a screenshare, or need to be refreshed as part of your security process. Rotating keys revokes the old credentials, disconnects broadcasts using stale credentials, and returns refreshed credentials in the API response.</p>
<p>To rotate keys for a live input, make a <code>POST</code> request to the <code>rotate_keys</code> endpoint:</p>
<pre tabindex="0"><code class="language-bash">curl --request POST \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/rotate_keys \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>Live input responses now also include <code>keysRotatedAt</code>, which indicates when the live input keys were last rotated. This field is omitted for live inputs whose keys have never been rotated.</p>
<p>For endpoint details, refer to <a href="/api/resources/stream/subresources/live_inputs/methods/rotate_keys/">Rotate keys for a live input</a>. For usage guidance, refer to <a href="/stream/stream-live/start-stream-live/#manage-live-inputs">Manage live inputs</a>.</p>


<h2 id="images-binding-is-now-billed-per-unique-transformation"><a href="/changelog/post/2026-07-01-binding-unique-transformations/">Images binding is now billed per unique transformation</a></h2>
<p><em>2026-07-01</em></p>
<p>The <a href="/images/optimization/binding/">Images binding</a> is now billed per unique transformation, matching the model already used for URL-based transformations. Repeat requests for the same combination of source image and parameters within the same calendar month are counted only once.</p>
<p>Previously, every call to the binding counted as a separate transformation regardless of whether the image or parameters were unique. With this change, you can call the binding on hot paths without paying for each individual request.</p>
<p>Calls to <a href="/images/optimization/binding/#infostream"><code>.info()</code></a> are no longer billed.</p>
<p>For more information, refer to <a href="/images/pricing/#images-transformed">Images pricing</a> and the <a href="/images/optimization/binding/">Images binding documentation</a>.</p>


<h2 id="new-optimization-features-in-images"><a href="/changelog/post/2026-06-16-new-optimization-features/">New optimization features in Images</a></h2>
<p><em>2026-06-16</em></p>
<p>These updates introduce new features for optimizing and manipulating with Images:</p>
<ul>
<li><strong>New <code>composite</code> option:</strong> Control how <a href="/images/optimization/draw-overlays/#composite">overlays are blended</a> with the base image.</li>
<li><strong>Percentage widths:</strong> Set the dimensions of an overlay as <a href="/images/optimization/draw-overlays/#width-and-height">a fraction of the dimensions</a> of the base image.</li>
<li><strong>New <code>fit</code> modes:</strong> Use <a href="/images/optimization/features/#aspect-crop"><code>aspect-crop</code></a> to always preserve the target aspect ratio or <a href="/images/optimization/features/#scale-up"><code>scale-up</code></a> to always enlarge images.</li>
<li><strong>New <code>upscale</code> parameter:</strong> Apply <a href="/images/optimization/features/#upscale">AI upscaling</a> to produce sharper, more detailed results when enlarging images.</li>
</ul>


<h2 id="manage-hosted-images-with-the-images-binding"><a href="/changelog/post/2026-06-10-hosted-images-binding/">Manage hosted images with the Images binding</a></h2>
<p><em>2026-06-10</em></p>
<p>Use the Images binding to upload, list, retrieve, update, and delete images stored in Images directly from your Worker without managing API tokens or making HTTP requests.</p>
<p>The <code>env.IMAGES.hosted</code> namespace supports the following storage and management operations:</p>
<ul>
<li><a href="/images/storage/binding/#uploadimage-options"><code>.upload(image, options)</code></a> — Upload a new image to your account.</li>
<li><a href="/images/storage/binding/#listoptions"><code>.list(options)</code></a> — List images with pagination.</li>
<li><a href="/images/storage/binding/#imageimageiddetails"><code>.image(imageId).details()</code></a> — Get image metadata.</li>
<li><a href="/images/storage/binding/#imageimageidbytes"><code>.image(imageId).bytes()</code></a> — Stream the original image bytes.</li>
<li><a href="/images/storage/binding/#imageimageidupdateoptions"><code>.image(imageId).update(options)</code></a> — Update metadata or access controls.</li>
<li><a href="/images/storage/binding/#imageimageiddelete"><code>.image(imageId).delete()</code></a> — Delete an image.</li>
</ul>
<p>For example, you can upload an image from a request body and return its metadata:</p>
<pre tabindex="0"><code class="language-ts">const image = await env.IMAGES.hosted.upload(request.body, {&#10;	filename: &quot;upload.jpg&quot;,&#10;	metadata: { source: &quot;worker&quot; },&#10;});&#10;&#10;return Response.json(image);&#10;</code></pre>
<p>Or retrieve and serve the original bytes of a hosted image:</p>
<pre tabindex="0"><code class="language-ts">const bytes = await env.IMAGES.hosted.image(&quot;IMAGE_ID&quot;).bytes();&#10;return new Response(bytes);&#10;</code></pre>
<p>For more information, refer to the <a href="/images/storage/binding/">Images binding</a>.</p>


<h2 id="post-meeting-transcriptions-are-now-generally-available-in-realtimekit"><a href="/changelog/post/2026-06-08-realtimekit-post-meeting-transcription-ga/">Post-meeting transcriptions are now Generally Available in RealtimeKit</a></h2>
<p><em>2026-06-08</em></p>
<p><a href="/realtime/realtimekit/">RealtimeKit</a> lets you build products where people meet over live audio and video — such as HealthTech, EdTech, proctoring, and other real-time platforms — on Cloudflare's <a href="/realtime/sfu/calls-vs-sfus/">global WebRTC infrastructure</a>.</p>
<p><a href="/realtime/realtimekit/ai/transcription/#post-meeting-transcription">Post-meeting transcription</a> is now Generally Available, so completed RealtimeKit meetings can automatically produce full transcript files after they end. Those transcripts can also power <a href="/realtime/realtimekit/ai/summary/">AI-generated summaries</a> for meeting notes, review workflows, and follow-up tasks after the transcript is available.</p>
<p>Post-meeting transcription is a managed service powered by <a href="/workers-ai/">Workers AI</a> using <a href="/workers-ai/models/whisper-large-v3-turbo/">Whisper Large v3 Turbo</a>. RealtimeKit handles transcription processing and can return transcript and summary files through <a href="/realtime/realtimekit/webhooks/">webhooks</a> or the REST API, so you do not need to run your own transcription infrastructure.</p>
<h4 id="2026-06-08-realtimekit-post-meeting-transcription-ga-generate-transcripts-and-summaries">Generate transcripts and summaries</h4>
<p>To generate a transcript after a meeting ends, set <code>transcribe_on_end: true</code> when <a href="/api/resources/realtime_kit/subresources/meetings/methods/create/">creating a meeting</a>. To also generate an AI summary automatically after the transcript is available, set <code>summarize_on_end: true</code>:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/meetings&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;title&quot;: &quot;Weekly product review&quot;,&#10;    &quot;transcribe_on_end&quot;: true,&#10;    &quot;summarize_on_end&quot;: true,&#10;    &quot;ai_config&quot;: {&#10;      &quot;transcription&quot;: {&#10;        &quot;language&quot;: &quot;en&quot;&#10;      },&#10;      &quot;summarization&quot;: {&#10;        &quot;word_limit&quot;: 500,&#10;        &quot;text_format&quot;: &quot;markdown&quot;,&#10;        &quot;summary_type&quot;: &quot;team_meeting&quot;&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<h4 id="2026-06-08-realtimekit-post-meeting-transcription-ga-consume-results">Consume results</h4>
<p>When RealtimeKit finishes processing a meeting, it creates download URLs for the transcript and, if <code>summarize_on_end</code> is set, the summary. You can receive those URLs automatically with <a href="/realtime/realtimekit/webhooks/">webhooks</a>, or fetch them later for a specific session with the <a href="/realtime/realtimekit/ai/summary/#rest-api">REST API</a>.</p>
<p>To receive results as soon as they are ready, configure the <code>meeting.transcript</code> and <code>meeting.summary</code> webhook events:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/webhooks&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;name&quot;: &quot;AI results webhook&quot;,&#10;    &quot;url&quot;: &quot;https://example.com/webhook&quot;,&#10;    &quot;events&quot;: [&quot;meeting.transcript&quot;, &quot;meeting.summary&quot;],&#10;    &quot;enabled&quot;: true&#10;  }&#x27;&#10;</code></pre>
<p>To fetch results later, call the <a href="/api/resources/realtime_kit/subresources/sessions/methods/get_session_transcripts/">transcript</a> or <a href="/api/resources/realtime_kit/subresources/sessions/methods/get_session_summary/">summary</a> endpoint for the session:</p>
<pre tabindex="0"><code class="language-bash">curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/transcript&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;&#10;curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/summary&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>Use the <a href="/api/resources/realtime_kit/subresources/sessions/methods/generate_summary_of_transcripts/">Generate summary of transcripts for the session</a> API only if <code>summarize_on_end</code> was not set and you want to generate a summary manually after the transcript is available:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/summary&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>Post-meeting transcription supports <a href="/realtime/realtimekit/ai/transcription/#output-formats">CSV, JSON, SRT, and VTT transcript outputs</a>, <a href="/realtime/realtimekit/ai/transcription/#post-meeting-supported-languages">automatic language detection and Whisper language codes</a>. RealtimeKit also supports <a href="/realtime/realtimekit/ai/transcription/#real-time-transcription">real-time transcription</a> with <a href="/workers-ai/models/nova-3/">Deepgram Nova-3</a> for live captions, in-meeting accessibility, and real-time note-taking.</p>
<p>Learn more in the <a href="/realtime/realtimekit/ai/transcription/">RealtimeKit transcription docs</a> and <a href="/realtime/realtimekit/ai/summary/">summary docs</a>.</p>


<h2 id="cloudflare-s-realtime-websocket-adapter-now-auto-reconnects-and-buffers-webrtc-media"><a href="/changelog/post/2026-05-29-websocket-adapter-auto-reconnect/">Cloudflare's Realtime WebSocket adapter now auto-reconnects and buffers WebRTC media</a></h2>
<p><em>2026-05-29</em></p>
<p><a href="/realtime/sfu/">Cloudflare Realtime SFU</a> is a <a href="/realtime/sfu/calls-vs-sfus/">WebRTC Selective Forwarding Unit that runs on Cloudflare's global network</a>, so you can route live audio, video, and data between WebRTC clients around the world without managing SFU infrastructure or regions.</p>
<p>When you use the <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/">WebSocket adapter</a> to stream WebRTC media to a WebSocket endpoint, the adapter now auto-reconnects and buffers audio and video after brief endpoint disconnects or restarts.</p>
<h4 id="2026-05-29-websocket-adapter-auto-reconnect-streaming-webrtc-media-to-websocket-endpoints">Streaming WebRTC media to WebSocket endpoints</h4>
<p>Many teams also use Realtime SFU as the media layer for backend applications, such as transcription, recording, note-taking, and agentic media-processing services. These systems often need to consume live WebRTC audio or video from the SFU in backend infrastructure, including <a href="/durable-objects/">Durable Objects</a>, <a href="/workers/">Workers</a>, <a href="/containers/">Containers</a>, or external services, without running a WebRTC client themselves.</p>
<p>The <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/">WebSocket adapter</a> bridges that gap by streaming WebRTC media from the SFU to a standard WebSocket endpoint as application-consumable payloads: <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/#media-formats">PCM audio frames and JPEG video frames</a>.</p>
<h4 id="2026-05-29-websocket-adapter-auto-reconnect-what-changed">What changed</h4>
<p>When you use the WebSocket adapter in <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/#stream-mode-egress">Stream mode (egress)</a> to send live audio or video from the SFU to your own WebSocket endpoint, the SFU now <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/#automatic-reconnection-for-streaming">automatically reconnects</a> after brief endpoint disconnects or restarts. This is especially helpful for long-running media pipelines where the WebSocket endpoint may briefly restart while a recording, transcription, or live analysis job is still in progress.</p>
<p>Previously, a brief disconnect from your WebSocket endpoint could close the adapter and require your application to recreate it before media could resume. Now, the SFU retries the same endpoint for up to 5 seconds with no API change required. If the endpoint comes back within that window, audio and video delivery resumes automatically.</p>
<p>The reconnect behavior also includes <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/#media-buffering-during-reconnect">live-first media buffering</a>, so brief interruptions reduce media loss without replaying stale video.</p>
<h4 id="2026-05-29-websocket-adapter-auto-reconnect-reconnect-behavior">Reconnect behavior</h4>
<p>During reconnect:</p>
<ul>
<li>Audio uses a short bounded backlog to reduce audible loss. If the interruption lasts longer than the backlog can cover, older audio may be dropped.</li>
<li>Video resumes from the <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/#video-jpeg">latest available JPEG frame</a> instead of replaying stale frames.</li>
<li>Recovery is best effort and does not guarantee gapless or exactly-once delivery.</li>
</ul>
<p>If the endpoint remains unavailable after the 5-second reconnect window, the adapter closes and must be recreated.</p>
<h4 id="2026-05-29-websocket-adapter-auto-reconnect-learn-more">Learn more</h4>
<ul>
<li><a href="/realtime/sfu/media-transport-adapters/websocket-adapter/">WebSocket adapter</a></li>
<li><a href="/realtime/sfu/media-transport-adapters/websocket-adapter/#automatic-reconnection-for-streaming">Automatic reconnection for streaming</a></li>
<li><a href="/realtime/sfu/get-started/">Get started with Realtime SFU</a></li>
<li><a href="/realtime/sfu/example-architecture/">Realtime SFU example architecture</a></li>
<li><a href="/realtime/sfu/calls-vs-sfus/">Realtime vs Regular SFUs</a></li>
<li><a href="https://realtime-sfu.dev-demos.workers.dev/">Global SFU Network Visualization</a></li>
</ul>


<h2 id="record-specific-participant-audio-tracks-in-realtimekit"><a href="/changelog/post/2026-05-28-realtimekit-track-recording/">Record specific participant audio tracks in RealtimeKit</a></h2>
<p><em>2026-05-28</em></p>
<p>You can now record specific participant audio tracks in RealtimeKit with <a href="/realtime/realtimekit/recording-guide/track-recording/">track recording</a>. Track recording creates separate WebM files for each participant instead of a single composite recording, which is useful for post-processing, transcription, and regulated or content-sensitive workflows.</p>
<p>To record specific participants, pass <code>user_ids</code> when starting a track recording:</p>
<pre tabindex="0"><code class="language-bash">curl --request POST \&#10;  &#45;-url https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/realtime/kit/&lt;app_id&gt;/recordings/track \&#10;  &#45;-header &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;  &quot;meeting_id&quot;: &quot;97440c6a-140b-40a9-9499-b23fd7a3868a&quot;,&#10;  &quot;user_ids&quot;: [&quot;user-123&quot;, &quot;user-456&quot;]&#10;}&#x27;&#10;</code></pre>
<p>To pass <code>user_ids</code> for selective track recording, use the following minimum SDK versions:</p>
<ul>
<li>Web Core: <code>@cloudflare/realtimekit</code> version <code>1.4.0</code> or later</li>
<li>Web UI Kit: <code>@cloudflare/realtimekit-ui</code>, <code>@cloudflare/realtimekit-react-ui</code>, or <code>@cloudflare/realtimekit-angular-ui</code> version <code>1.1.2</code> or later</li>
<li>Android Core or iOS Core: version <code>2.0.0</code> or later</li>
<li>Android UI Kit or iOS UI Kit: version <code>1.1.0</code> or later</li>
</ul>
<p><a href="/realtime/realtimekit/">RealtimeKit</a> provides SDKs and UI components so that you can build your own meeting experience on Cloudflare's <a href="/realtime/#realtime-sfu">global WebRTC infrastructure</a>. Teams today build products ranging from telehealth to education on RealtimeKit for global audiences. You can get started today with our <a href="/realtime/realtimekit/quickstart/">Quickstart</a> or take a look at our <a href="https://github.com/cloudflare/meet">Cloudflare Meet repo</a> as a reference.</p>


<h2 id="transformation-flows-in-images"><a href="/changelog/post/2026-05-27-transformation-flows/">Transformation flows in Images</a></h2>
<p><em>2026-05-27</em></p>
<p><img src="/assets/upstream/images/images/custom-flow.png" alt="Custom flow configuration panel" /></p>
<p>Flows are automated rules that pair conditions (such as file extension, URL path, or query parameter) with parameters. Set up a flow to automatically apply image optimization to matching requests on your zone without writing code or changing URLs.</p>
<p>There are two modes for transformation flows:</p>
<ul>
<li><strong><a href="/images/optimization/transformations/flows/#set-up-a-provider-flow">Provider flows</a></strong> — Migrate from another image optimization service. Your existing URLs continue to work while Cloudflare rewrites provider-specific parameters to their Cloudflare equivalents. Currently, Cloudflare supports provider flows for Fastly Image Optimizer.</li>
<li><strong><a href="/images/optimization/transformations/flows/#set-up-a-custom-flow">Custom flows</a></strong> — Define your own conditions and actions for use cases like automatic format conversion, <a href="/images/optimization/make-responsive-images/#using-widthauto">responsive sizing</a> with <code>width=auto</code>, or directory-based optimization.</li>
</ul>
<p>To get started, go to <strong>Images</strong> &gt; <strong>Transformations</strong> &gt; <strong>Automation</strong> in the <a href="https://dash.cloudflare.com/?to=/:account/images/transformations">Cloudflare dashboard</a>.</p>
<p>Learn more about <a href="/images/optimization/transformations/flows/">transformation flows</a>.</p>


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


<h2 id="real-time-transcription-in-realtimekit-now-supports-10-languages-with-regional-variants"><a href="/changelog/post/2026-03-06-realtimekit-multilingual-transcription/">Real-time transcription in RealtimeKit now supports 10 languages with regional variants</a></h2>
<p><em>2026-03-06</em></p>
<p><a href="/realtime/realtimekit/ai/transcription/">Real-time transcription</a> in RealtimeKit now supports 10 languages with regional variants, powered by <a href="/workers-ai/models/nova-3/">Deepgram Nova-3</a> running on <a href="/workers-ai/">Workers AI</a>.</p>
<p>During a meeting, participant audio is routed through <a href="/ai-gateway/">AI Gateway</a> to Nova-3 on Workers AI — so transcription runs on Cloudflare's network end-to-end, reducing latency compared to routing through external speech-to-text services.</p>
<p>Set the language when <a href="/realtime/realtimekit/concepts/meeting/">creating a meeting</a> via <code>ai_config.transcription.language</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;ai_config&quot;: {&#10;		&quot;transcription&quot;: {&#10;			&quot;language&quot;: &quot;fr&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Supported languages include English, Spanish, French, German, Hindi, Russian, Portuguese, Japanese, Italian, and Dutch — with regional variants like <code>en-AU</code>, <code>en-GB</code>, <code>en-IN</code>, <code>en-NZ</code>, <code>es-419</code>, <code>fr-CA</code>, <code>de-CH</code>, <code>pt-BR</code>, and <code>pt-PT</code>. Use <code>multi</code> for automatic multilingual detection.</p>
<p>If you are building voice agents or real-time translation workflows, your agent can now transcribe in the caller's language natively — no extra services or routing logic needed.</p>
<ul>
<li><a href="/realtime/realtimekit/ai/transcription/">Transcription docs</a></li>
<li><a href="/workers-ai/models/nova-3/">Nova-3 model page</a></li>
<li><a href="/workers-ai/">Workers AI</a></li>
<li><a href="/ai-gateway/">AI Gateway</a></li>
</ul>


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


<h2 id="heic-support-in-cloudflare-images"><a href="/changelog/post/heic-support/">HEIC support in Cloudflare Images</a></h2>
<p><em>2025-07-08</em></p>
<p>You can use Images to ingest HEIC images and serve them in supported output formats like AVIF, WebP, JPEG, and PNG.</p>
<p>When inputting a HEIC image, dimension and sizing limits may still apply. Refer to our documentation to see limits for <a href="/images/storage/upload-images/methods/">uploading to Images</a> or <a href="/images/optimization/transformations/overview/">transforming a remote image</a>.</p>


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


<h2 id="bind-the-images-api-to-your-worker"><a href="/changelog/post/2025-02-21-images-bindings-in-workers/">Bind the Images API to your Worker</a></h2>
<p><em>2025-02-24</em></p>
<p>You can now <a href="/images/optimization/binding/">interact with the Images API</a> directly in your Worker.</p>
<p>This allows more fine-grained control over transformation request flows and cache behavior. For example, you can resize, manipulate, and overlay images without requiring them to be accessible through a URL.</p>
<p>The Images binding can be configured in the Cloudflare dashboard for your Worker or in the Wrangler configuration file in your project's directory:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17735.md")</div>
<p>Within your Worker code, you can interact with this binding by using <code>env.IMAGES</code>.</p>
<p>Here's how you can rotate, resize, and blur an image, then output the image as AVIF:</p>
<pre tabindex="0"><code class="language-ts">const info = await env.IMAGES.info(stream);&#10;// stream contains a valid image, and width/height is available on the info object&#10;&#10;const response = (&#10;	await env.IMAGES.input(stream)&#10;		.transform({ rotate: 90 })&#10;		.transform({ width: 128 })&#10;		.transform({ blur: 20 })&#10;		.output({ format: &quot;image/avif&quot; })&#10;).response();&#10;&#10;return response;&#10;</code></pre>
<p>For more information, refer to <a href="/images/optimization/binding/">Images Bindings</a>.</p>


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



