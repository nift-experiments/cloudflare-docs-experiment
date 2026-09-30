<h2 id="2026-08-13">2026-08-13</h2><strong>DataChannels reliability and ordering (ordered, maxRetransmits, maxPacketLifeTime)</strong><p>DataChannels now accept reliability settings on both publisher (<code>location: &quot;local&quot;</code>) and subscriber (<code>location: &quot;remote&quot;</code>) channels, so unreliable and unordered delivery is honored end to end.</p>
<ul>
<li><code>ordered</code> (default <code>true</code>) controls in-order delivery. When <code>false</code>, a delayed message does not block later messages.</li>
<li>Set <code>ordered: false</code> and omit both retry fields for reliable, unordered delivery.</li>
<li><code>maxRetransmits</code> or <code>maxPacketLifeTime</code> enable partial reliability; set <code>maxRetransmits: 0</code> for fully unreliable delivery.</li>
<li>Set the same fields on local and remote <code>/datachannels/new</code> calls, and mirror them on <code>createDataChannel()</code> for negotiated channels.</li>
<li>Docs: <a href="/realtime/sfu/datachannels/">DataChannels</a>, <a href="/realtime/sfu/https-api/">Connection API</a></li>
</ul><h2 id="2026-07-23">2026-07-23</h2><strong>DataChannels return-to-publisher (canReply)</strong><p>DataChannels now support opt-in reverse traffic from one subscriber back to the publisher on the same channel. When a subscriber pulls a remote DataChannel with <code>canReply: true</code> (or is granted it later via <code>datachannels/update</code>), the SFU admits that subscriber's messages to the publisher only.</p>
<ul>
<li>Opt-in per subscriber; defaults to <code>false</code>, so existing publisher-to-subscriber fan-out is unchanged.</li>
<li>Reverse traffic is not fanned out to other subscribers.</li>
<li>Exclusive: at most one subscriber holds <code>canReply</code> per publisher DataChannel; a new grant replaces the previous holder.</li>
<li>Grant or revoke without re-pulling via <code>PUT .../datachannels/update</code>.</li>
<li>Docs: <a href="/realtime/sfu/datachannels/">DataChannels</a>, <a href="/realtime/sfu/limits/">Limits, timeouts and quotas</a></li>
</ul><h2 id="2026-06-10">2026-06-10</h2><strong>DataChannels subscriber acknowledgment gate (waitForAck)</strong><p>DataChannels now support an opt-in subscriber acknowledgment gate. When a subscriber pulls a remote DataChannel with <code>waitForAck: true</code>, the SFU holds delivery to that subscriber until it sends its first message (the acknowledgment). This avoids losing the first messages before the subscriber is ready to handle them.</p>
<ul>
<li>Opt-in per subscriber; defaults to <code>false</code>, so existing behavior is unchanged.</li>
<li>The acknowledgment is consumed by the SFU and is not forwarded, so the channel stays unidirectional.</li>
<li>Send the acknowledgment within 30 seconds of creating the remote DataChannel.</li>
<li>Docs: <a href="/realtime/sfu/datachannels/">DataChannels</a>, <a href="/realtime/sfu/limits/">Limits, timeouts and quotas</a></li>
</ul><h2 id="2025-11-21">2025-11-21</h2><strong>WebSocket adapter video (JPEG) support</strong><p>Updated Media Transport Adapters (WebSocket adapter) to support video egress as JPEG frames in addition to audio.</p>
<ul>
<li>Stream audio and video between WebRTC tracks and WebSocket endpoints</li>
<li>Video egress-only as JPEG at approximately 1 FPS for snapshots, thumbnails, and computer vision pipelines</li>
<li>Clarified media formats for PCM audio and JPEG video over Protocol Buffers</li>
<li>Updated docs: <a href="/realtime/sfu/media-transport-adapters/">Adapters</a>, <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/">WebSocket adapter</a></li>
</ul><h2 id="2025-08-29">2025-08-29</h2><strong>Media Transport Adapters (WebSocket) open beta</strong><p>Open beta for Media Transport Adapters (WebSocket adapter) to bridge audio between WebRTC and WebSocket.</p>
<ul>
<li>Ingest (WebSocket → WebRTC) and Stream (WebRTC → WebSocket)</li>
<li>Opus for WebRTC tracks; PCM over WebSocket via Protocol Buffers</li>
</ul>
<p>Docs: <a href="/realtime/sfu/media-transport-adapters/">Adapters</a>, <a href="/realtime/sfu/media-transport-adapters/websocket-adapter/">WebSocket adapter</a></p><h2 id="2024-09-25">2024-09-25</h2><strong>TURN service is generally available (GA)</strong><p>Cloudflare Realtime TURN service is generally available and helps address common challenges with real-time communication. For more information, refer to the <a href="https://blog.cloudflare.com/webrtc-turn-using-anycast/">blog post</a> or <a href="/realtime/turn/">TURN documentation</a>.</p><h2 id="2024-04-04">2024-04-04</h2><strong>Orange Meets availability</strong><p>Orange Meets, Cloudflare's internal video conferencing app, is open source and available for use from <a href="https://github.com/cloudflare/orange?cf_target_id=40DF7321015C5928F9359DD01303E8C2">Github</a>.</p><h2 id="2024-04-04-1">2024-04-04</h2><strong>Cloudflare Realtime open beta</strong><p>Cloudflare Realtime is in open beta and available from the Cloudflare Dashboard.</p><h2 id="2022-09-27">2022-09-27</h2><strong>Cloudflare Realtime closed beta</strong><p>Cloudflare Realtime is available as a closed beta for users who request an invitation. Refer to the <a href="https://blog.cloudflare.com/announcing-cloudflare-calls/">blog post</a> for more information.</p>
