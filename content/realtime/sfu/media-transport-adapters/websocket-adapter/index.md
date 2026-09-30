<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12692.md")
</aside>
<p>Stream audio and video between WebRTC tracks and WebSocket endpoints. Supports ingesting audio from WebSocket sources and sending WebRTC audio and video to WebSocket consumers. Video egress is supported as JPEG at approximately 1 FPS.</p>
<h2 id="what-you-can-build">What you can build</h2>
<ul>
<li>AI services with WebSocket APIs for audio processing</li>
<li>Custom audio processing pipelines</li>
<li>Legacy system bridges</li>
<li>Server-side audio generation and consumption</li>
<li>Video snapshotting and thumbnails</li>
<li>Computer vision ingestion (low FPS)</li>
</ul>
<h2 id="how-it-works">How it works</h2>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12695.md")
</div></div>
<h2 id="api-reference">API reference</h2>
<h3 id="create-adapter">Create adapter</h3>
<pre><code>POST /v1/apps/{appId}/adapters/websocket/new&#10;</code></pre>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/12698.md")
</div></div>
<h3 id="close-adapter">Close adapter</h3>
<pre><code>POST /v1/apps/{appId}/adapters/websocket/close&#10;</code></pre>
<h4 id="request-body-2">Request body</h4>
<pre><code class="language-json">{&#10;	&quot;tracks&quot;: [&#10;		{&#10;			&quot;adapterId&quot;: &quot;string&quot;&#10;		}&#10;	]&#10;}&#10;</code></pre>
<h2 id="media-formats">Media formats</h2>
<h3 id="webrtc-tracks">WebRTC tracks</h3>
<ul>
<li><strong>Codec</strong>: Opus</li>
<li><strong>Sample rate</strong>: 48 kHz</li>
<li><strong>Channels</strong>: Stereo</li>
</ul>
<h3 id="websocket-binary-format">WebSocket binary format</h3>
<p>Media uses Protocol Buffers. Audio uses PCM payloads; video uses JPEG payloads:</p>
<ul>
<li>16-bit signed little-endian PCM</li>
<li>48 kHz sample rate</li>
<li>Stereo (left/right interleaved)</li>
<li>Video: JPEG image payload (one frame per message)</li>
</ul>
<pre><code class="language-proto">message Packet {&#10;    uint32 sequenceNumber = 1;  // Used in Stream mode only&#10;    uint32 timestamp = 2;       // Used in Stream mode only&#10;    bytes payload = 5;          // Media data&#10;}&#10;</code></pre>
<p><strong>Ingest mode (buffer)</strong>: Only the <code>payload</code> field is used, containing chunks of audio data.</p>
<p><strong>Stream mode (egress)</strong>:</p>
<ul>
<li>For audio frames:
<ul>
<li><code>sequenceNumber</code>: Incremental packet counter</li>
<li><code>timestamp</code>: Timestamp for synchronization</li>
<li><code>payload</code>: Individual PCM audio frame data</li>
</ul>
</li>
<li>For video frames (JPEG):
<ul>
<li><code>timestamp</code>: Timestamp for synchronization</li>
<li><code>payload</code>: JPEG image data (one frame per message)</li>
<li>Note: <code>sequenceNumber</code> may be unset for video frames</li>
</ul>
</li>
</ul>
<h3 id="video-jpeg">Video (JPEG)</h3>
<ul>
<li>Supported WebRTC input codecs: H264, H265, VP8, VP9</li>
<li>Output over WebSocket: JPEG images at approximately 1 FPS</li>
</ul>
<h2 id="connection-protocol">Connection protocol</h2>
<p>Connects to your WebSocket endpoint:</p>
<ol>
<li>WebSocket upgrade handshake</li>
<li>Secure connection for <code>wss://</code> URLs</li>
<li>Media streaming begins</li>
</ol>
<h3 id="message-format">Message format</h3>
<h4 id="buffer-mode-ingest">Buffer mode (ingest)</h4>
<ul>
<li><strong>Binary messages</strong>: PCM audio data in chunks</li>
<li><strong>Maximum message size</strong>: 32 KB per WebSocket message</li>
<li><strong>Important</strong>: Account for serialization overhead when chunking audio buffers</li>
<li>Send audio in small, frequent chunks rather than large batches</li>
</ul>
<h4 id="stream-mode-egress">Stream mode (egress)</h4>
<ul>
<li><strong>Binary messages</strong>: Individual frames with metadata (audio or video)</li>
<li>Audio frames include:
<ul>
<li>Timestamp information</li>
<li>Sequence number</li>
<li>PCM audio frame data</li>
</ul>
</li>
<li>Video frames include:
<ul>
<li>Timestamp information</li>
<li>JPEG image data</li>
<li>Note: Sequence number may be unset for video frames</li>
</ul>
</li>
<li>Frames are sent individually as they arrive from the WebRTC track</li>
<li>Video frames are emitted at approximately 1 FPS</li>
</ul>
<h3 id="connection-lifecycle">Connection lifecycle</h3>
<ol>
<li>Connects to the WebSocket endpoint</li>
<li>Audio streaming begins</li>
<li>Video streaming begins (if configured)</li>
<li>For WebRTC to WebSocket streaming, briefly retries the same endpoint after disconnects</li>
<li>Connection closes when closed, on error, or after the automatic reconnect window is exhausted</li>
</ol>
<h2 id="automatic-reconnection-for-streaming">Automatic reconnection for streaming</h2>
<p>When you use the WebSocket adapter in <a href="#stream-mode-egress">Stream mode (egress)</a> to send live audio or video from the SFU to your own WebSocket endpoint (<code>WebRTC → WebSocket</code>), the SFU automatically reconnects after brief endpoint disconnects or restarts.</p>
<p>The SFU retries the same WebSocket endpoint for up to 5 seconds. No API changes are required. If the endpoint remains unavailable after the reconnect window, the adapter closes and your application must create a new adapter to resume streaming.</p>
<h3 id="media-buffering-during-reconnect">Media buffering during reconnect</h3>
<p>Automatic reconnection uses live-first buffering while the WebSocket endpoint is temporarily unavailable:</p>
<ul>
<li><strong>Audio buffering</strong>: The SFU keeps a short, bounded backlog of audio frames. If the interruption lasts longer than the backlog can cover, older audio may be dropped so reconnect recovery stays bounded.</li>
<li><strong>Video buffering</strong>: The SFU keeps only the latest available JPEG frame. Newer frames replace older frames while reconnecting, so video resumes near-live instead of replaying stale frames.</li>
<li><strong>Delivery behavior</strong>: Buffering reduces media loss during brief interruptions, but it is not a replay mechanism and does not guarantee gapless or exactly-once delivery.</li>
</ul>
<p>Automatic reconnection applies only when using <a href="#stream-mode-egress">Stream mode (egress)</a>. It retries the same endpoint only and does not provide multi-endpoint failover.</p>
<h2 id="pricing">Pricing</h2>
<p>Currently in beta and free to use.</p>
<p>Once generally available, billing will follow standard Cloudflare Realtime pricing at $0.05 per GB egress. Only traffic originating from Cloudflare towards WebSocket endpoints incurs charges. Traffic ingested from WebSocket endpoints into Cloudflare incurs no charge.</p>
<p>Usage counts towards your Cloudflare Realtime free tier of 1,000 GB.</p>
<h2 id="best-practices">Best practices</h2>
<h3 id="connection-management">Connection management</h3>
<ul>
<li>Closing an already-closed instance returns success</li>
<li>Close when sessions end</li>
<li>When using <a href="#stream-mode-egress">Stream mode (egress)</a>, handle adapter closure after the 5-second <a href="#automatic-reconnection-for-streaming">automatic reconnect window</a> is exhausted.</li>
<li>When ingesting from WebSocket to WebRTC, implement reconnection logic in your WebSocket client if the connection drops.</li>
<li>Make your WebSocket endpoint restart-safe so it can accept reconnects to the same URL during brief restarts.</li>
</ul>
<h3 id="performance">Performance</h3>
<ul>
<li>Deploy WebSocket endpoints close to Cloudflare edge</li>
<li>Use appropriate buffer sizes</li>
<li>Monitor connection quality</li>
</ul>
<h3 id="security">Security</h3>
<ul>
<li>Secure WebSocket endpoints with authentication</li>
<li>Use <code>wss://</code> for production</li>
<li>Implement rate limiting</li>
</ul>
<h2 id="limitations">Limitations</h2>
<ul>
<li><strong>WebSocket payloads</strong>: PCM (audio) for ingest and stream; JPEG (video) for stream</li>
<li><strong>Beta status</strong>: API may change in future releases</li>
<li><strong>Video support</strong>: Egress only (JPEG)</li>
<li><strong>Video frame rate</strong>: Approximately 1 FPS (beta; not configurable)</li>
<li><strong>Streaming reconnects</strong>: When using <a href="#stream-mode-egress">Stream mode (egress)</a>, the SFU automatically retries the same WebSocket endpoint for short disconnects only. It does not fail over to alternate endpoints.</li>
<li><strong>Best-effort recovery</strong>: Brief reconnects reduce media loss, but do not guarantee gapless or exactly-once delivery.</li>
<li><strong>Video reconnect behavior</strong>: Video resumes from the latest available JPEG frame rather than replaying older frames.</li>
<li><strong>Unidirectional flow</strong>: Each instance handles one direction</li>
</ul>
<h2 id="error-handling">Error handling</h2>
<table>
<thead>
<tr>
<th>Error Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>400</code></td>
<td>Invalid request parameters</td>
</tr>
<tr>
<td><code>404</code></td>
<td>Session or track not found</td>
</tr>
<tr>
<td><code>503</code></td>
<td>Adapter not found (for close operations)</td>
</tr>
</tbody>
</table>
<h2 id="reference-implementations">Reference implementations</h2>
<ul>
<li>Audio (PCM over WebSocket): <a href="https://github.com/cloudflare/realtime-examples/tree/main/ai-tts-stt">Cloudflare Realtime Examples – ai-tts-stt</a></li>
<li>Video (JPEG egress): <a href="https://github.com/cloudflare/realtime-examples/tree/main/video-to-jpeg">Cloudflare Realtime Examples – video-to-jpeg</a></li>
</ul>
<h2 id="migration-from-custom-bridges">Migration from custom bridges</h2>
<ol>
<li>Replace custom signaling with adapter API calls</li>
<li>Update WebSocket endpoints to handle PCM format</li>
<li>Implement adapter lifecycle management</li>
<li>Remove custom STUN/TURN configuration</li>
</ol>
<h2 id="faq">FAQ</h2>
<p><strong>Q: Can I use the same adapter for bidirectional audio?</strong>
A: No, each instance is unidirectional. Create separate adapters for send and receive.</p>
<p><strong>Q: What happens if the WebSocket connection drops?</strong></p>
<p>A: When using <a href="#stream-mode-egress">Stream mode (egress)</a>, the SFU automatically retries the same WebSocket endpoint for up to 5 seconds. If the endpoint comes back within that window, streaming resumes automatically.</p>
<p>Audio uses a short bounded backlog to reduce audible loss during brief interruptions. Video resumes from the latest available JPEG frame instead of replaying older frames.</p>
<p>If the endpoint remains unavailable after the 5-second <a href="#automatic-reconnection-for-streaming">automatic reconnect window</a>, the adapter closes and must be recreated.</p>
<p>When ingesting from WebSocket to WebRTC, your WebSocket client should reconnect and recreate the adapter as needed.</p>
<p><strong>Q: Is there a limit on concurrent adapters?</strong>
A: Limits follow standard Cloudflare Realtime quotas. Contact support for specific requirements.</p>
<p><strong>Q: Can I change the audio format after creating an adapter?</strong>
A: No, audio format is fixed at creation time. Create a new adapter for different formats.</p>
