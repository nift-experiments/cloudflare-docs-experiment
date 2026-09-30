<h1 id="changelog">Changelog</h1>

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


<h2 id="post-meeting-transcriptions-are-now-generally-available-in-realtimekit"><a href="/changelog/post/2026-06-08-realtimekit-post-meeting-transcription-ga/">Post-meeting transcriptions are now Generally Available in RealtimeKit</a></h2>
<p><em>2026-06-08</em></p>
<p><a href="/realtime/realtimekit/">RealtimeKit</a> lets you build products where people meet over live audio and video — such as HealthTech, EdTech, proctoring, and other real-time platforms — on Cloudflare's <a href="/realtime/sfu/calls-vs-sfus/">global WebRTC infrastructure</a>.</p>
<p><a href="/realtime/realtimekit/ai/transcription/#post-meeting-transcription">Post-meeting transcription</a> is now Generally Available, so completed RealtimeKit meetings can automatically produce full transcript files after they end. Those transcripts can also power <a href="/realtime/realtimekit/ai/summary/">AI-generated summaries</a> for meeting notes, review workflows, and follow-up tasks after the transcript is available.</p>
<p>Post-meeting transcription is a managed service powered by <a href="/workers-ai/">Workers AI</a> using <a href="/workers-ai/models/whisper-large-v3-turbo/">Whisper Large v3 Turbo</a>. RealtimeKit handles transcription processing and can return transcript and summary files through <a href="/realtime/realtimekit/webhooks/">webhooks</a> or the REST API, so you do not need to run your own transcription infrastructure.</p>
<h4 id="2026-06-08-realtimekit-post-meeting-transcription-ga-generate-transcripts-and-summaries">Generate transcripts and summaries</h4>
<p>To generate a transcript after a meeting ends, set <code>transcribe_on_end: true</code> when <a href="/api/resources/realtime_kit/subresources/meetings/methods/create/">creating a meeting</a>. To also generate an AI summary automatically after the transcript is available, set <code>summarize_on_end: true</code>:</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/meetings&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;title&quot;: &quot;Weekly product review&quot;,&#10;    &quot;transcribe_on_end&quot;: true,&#10;    &quot;summarize_on_end&quot;: true,&#10;    &quot;ai_config&quot;: {&#10;      &quot;transcription&quot;: {&#10;        &quot;language&quot;: &quot;en&quot;&#10;      },&#10;      &quot;summarization&quot;: {&#10;        &quot;word_limit&quot;: 500,&#10;        &quot;text_format&quot;: &quot;markdown&quot;,&#10;        &quot;summary_type&quot;: &quot;team_meeting&quot;&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<h4 id="2026-06-08-realtimekit-post-meeting-transcription-ga-consume-results">Consume results</h4>
<p>When RealtimeKit finishes processing a meeting, it creates download URLs for the transcript and, if <code>summarize_on_end</code> is set, the summary. You can receive those URLs automatically with <a href="/realtime/realtimekit/webhooks/">webhooks</a>, or fetch them later for a specific session with the <a href="/realtime/realtimekit/ai/summary/#rest-api">REST API</a>.</p>
<p>To receive results as soon as they are ready, configure the <code>meeting.transcript</code> and <code>meeting.summary</code> webhook events:</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/webhooks&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;name&quot;: &quot;AI results webhook&quot;,&#10;    &quot;url&quot;: &quot;https://example.com/webhook&quot;,&#10;    &quot;events&quot;: [&quot;meeting.transcript&quot;, &quot;meeting.summary&quot;],&#10;    &quot;enabled&quot;: true&#10;  }&#x27;&#10;</code></pre>
<p>To fetch results later, call the <a href="/api/resources/realtime_kit/subresources/sessions/methods/get_session_transcripts/">transcript</a> or <a href="/api/resources/realtime_kit/subresources/sessions/methods/get_session_summary/">summary</a> endpoint for the session:</p>
<pre><code class="language-bash">curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/transcript&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;&#10;curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/summary&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>Use the <a href="/api/resources/realtime_kit/subresources/sessions/methods/generate_summary_of_transcripts/">Generate summary of transcripts for the session</a> API only if <code>summarize_on_end</code> was not set and you want to generate a summary manually after the transcript is available:</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/sessions/$SESSION_ID/summary&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
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
<pre><code class="language-bash">curl --request POST \&#10;  &#45;-url https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/realtime/kit/&lt;app_id&gt;/recordings/track \&#10;  &#45;-header &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;  &quot;meeting_id&quot;: &quot;97440c6a-140b-40a9-9499-b23fd7a3868a&quot;,&#10;  &quot;user_ids&quot;: [&quot;user-123&quot;, &quot;user-456&quot;]&#10;}&#x27;&#10;</code></pre>
<p>To pass <code>user_ids</code> for selective track recording, use the following minimum SDK versions:</p>
<ul>
<li>Web Core: <code>@cloudflare/realtimekit</code> version <code>1.4.0</code> or later</li>
<li>Web UI Kit: <code>@cloudflare/realtimekit-ui</code>, <code>@cloudflare/realtimekit-react-ui</code>, or <code>@cloudflare/realtimekit-angular-ui</code> version <code>1.1.2</code> or later</li>
<li>Android Core or iOS Core: version <code>2.0.0</code> or later</li>
<li>Android UI Kit or iOS UI Kit: version <code>1.1.0</code> or later</li>
</ul>
<p><a href="/realtime/realtimekit/">RealtimeKit</a> provides SDKs and UI components so that you can build your own meeting experience on Cloudflare's <a href="/realtime/#realtime-sfu">global WebRTC infrastructure</a>. Teams today build products ranging from telehealth to education on RealtimeKit for global audiences. You can get started today with our <a href="/realtime/realtimekit/quickstart/">Quickstart</a> or take a look at our <a href="https://github.com/cloudflare/meet">Cloudflare Meet repo</a> as a reference.</p>


<h2 id="real-time-transcription-in-realtimekit-now-supports-10-languages-with-regional-variants"><a href="/changelog/post/2026-03-06-realtimekit-multilingual-transcription/">Real-time transcription in RealtimeKit now supports 10 languages with regional variants</a></h2>
<p><em>2026-03-06</em></p>
<p><a href="/realtime/realtimekit/ai/transcription/">Real-time transcription</a> in RealtimeKit now supports 10 languages with regional variants, powered by <a href="/workers-ai/models/nova-3/">Deepgram Nova-3</a> running on <a href="/workers-ai/">Workers AI</a>.</p>
<p>During a meeting, participant audio is routed through <a href="/ai-gateway/">AI Gateway</a> to Nova-3 on Workers AI — so transcription runs on Cloudflare's network end-to-end, reducing latency compared to routing through external speech-to-text services.</p>
<p>Set the language when <a href="/realtime/realtimekit/concepts/meeting/">creating a meeting</a> via <code>ai_config.transcription.language</code>:</p>
<pre><code class="language-json">{&#10;	&quot;ai_config&quot;: {&#10;		&quot;transcription&quot;: {&#10;			&quot;language&quot;: &quot;fr&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Supported languages include English, Spanish, French, German, Hindi, Russian, Portuguese, Japanese, Italian, and Dutch — with regional variants like <code>en-AU</code>, <code>en-GB</code>, <code>en-IN</code>, <code>en-NZ</code>, <code>es-419</code>, <code>fr-CA</code>, <code>de-CH</code>, <code>pt-BR</code>, and <code>pt-PT</code>. Use <code>multi</code> for automatic multilingual detection.</p>
<p>If you are building voice agents or real-time translation workflows, your agent can now transcribe in the caller's language natively — no extra services or routing logic needed.</p>
<ul>
<li><a href="/realtime/realtimekit/ai/transcription/">Transcription docs</a></li>
<li><a href="/workers-ai/models/nova-3/">Nova-3 model page</a></li>
<li><a href="/workers-ai/">Workers AI</a></li>
<li><a href="/ai-gateway/">AI Gateway</a></li>
</ul>



