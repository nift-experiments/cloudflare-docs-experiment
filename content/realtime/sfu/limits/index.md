<p>Understanding the limits and timeouts of Cloudflare Realtime is crucial for optimizing the performance and reliability of your applications. This section outlines the key constraints and behaviors you should be aware of when integrating Cloudflare Realtime into your app.</p>
<h2 id="free">Free</h2>
<ul>
<li>Each account gets 1,000GB/month of data transfer from Cloudflare to your client for free.</li>
<li>Data transfer from your client to Cloudflare is always free of charge.</li>
</ul>
<h2 id="limits">Limits</h2>
<ul>
<li>
<p><strong>API Realtime per Session</strong>: You can make up to 50 API calls per second for each session. There is no ratelimit on a App basis, just sessions.</p>
</li>
<li>
<p><strong>Tracks per API Call</strong>: Up to 64 tracks can be added with a single API call. If you need to add more tracks to a session, you should distribute them across multiple API calls.</p>
</li>
<li>
<p><strong>Tracks per Session</strong>: There's no upper limit to the number of tracks a session can contain, the practical limit is governed by your connection's bandwidth to and from Cloudflare.</p>
</li>
<li>
<p><strong>DataChannel canReply exclusivity</strong>: At most one subscriber may hold <code>canReply</code> for a given publisher DataChannel at a time. Granting <code>canReply</code> to another subscriber replaces the previous selection. The publisher receives reverse traffic only, and it is not fanned out to other subscribers. For more information, refer to <a href="/realtime/sfu/datachannels/#return-to-publisher-canreply">Return to publisher (canReply)</a>.</p>
</li>
</ul>
<h2 id="inactivity-timeout">Inactivity Timeout</h2>
<ul>
<li><strong>Track Timeout</strong>: Tracks will automatically timeout and be garbage collected after 30 seconds of inactivity, where inactivity is defined as no media packets being received by Cloudflare. This mechanism ensures efficient use of resources and session cleanliness across all Sessions that use a track.</li>
<li><strong>DataChannel acknowledgment timeout</strong>: When <code>waitForAck</code> is enabled on a remote DataChannel, the subscriber must send its first message (the acknowledgment) within 30 seconds of creating the channel. If it does not, the SFU tears down the gated channel and forwards no messages. Create the remote DataChannel again to retry.</li>
</ul>
<h2 id="peerconnection-requirements">PeerConnection Requirements</h2>
<ul>
<li><strong>Session State</strong>: For any operation on a session (e.g., pulling or pushing tracks), the PeerConnection state must be <code>connected</code>. Operations will block for up to 5 seconds awaiting this state before timing out. This ensures that only active and viable sessions are engaged in media transmission.</li>
</ul>
<h2 id="handling-connectivity-issues">Handling Connectivity Issues</h2>
<ul>
<li><strong>Internet Connectivity Considerations</strong>: The potential for internet connectivity loss between the client and Cloudflare is an operational reality that must be addressed. Implementing a detection and reconnection strategy is recommended to maintain session continuity. This could involve periodic 'heartbeat' signals to your backend server to monitor connectivity status. Upon detecting connectivity issues, automatically attempting to reconnect and establish a new session is advised. Sessions and tracks will remain available for reuse for 30 seconds before timing out, providing a brief window for reconnection attempts.</li>
</ul>
<p>Adhering to these limits and understanding the timeout behaviors will help ensure that your applications remain responsive and stable while providing a seamless user experience.</p>
<h2 id="supported-codecs">Supported Codecs</h2>
<p>Cloudflare Realtime supports the following codecs:</p>
<h3 id="supported-video-codecs">Supported video codecs</h3>
<ul>
<li><strong>H264</strong></li>
<li><strong>H265</strong></li>
<li><strong>VP8</strong></li>
<li><strong>VP9</strong></li>
<li><strong>AV1</strong></li>
</ul>
<h3 id="supported-audio-codecs">Supported audio codecs</h3>
<ul>
<li><strong>Opus</strong></li>
<li><strong>G.711 PCM (A-law)</strong></li>
<li><strong>G.711 PCM (µ-law)</strong></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11574.md")
</aside>
