<p>Cloudflare Realtime simplifies the management of peer connections and media tracks through HTTPS API endpoints. These endpoints allow developers to efficiently manage sessions, add or remove tracks, and gather session information.</p>
<h2 id="api-endpoints">API Endpoints</h2>
<ul>
<li><strong>Create a New Session</strong>: Initiates a new session on Cloudflare Realtime, which can be modified with other endpoints below.
<ul>
<li><code>POST /apps/{appId}/sessions/new</code></li>
</ul>
</li>
<li><strong>Add a New Track</strong>: Adds a media track (audio or video) to an existing session.
<ul>
<li><code>POST /apps/{appId}/sessions/{sessionId}/tracks/new</code></li>
</ul>
</li>
<li><strong>Update Tracks</strong>: Changes tracks by reusing existing transceivers.
<ul>
<li><code>PUT /apps/{appId}/sessions/{sessionId}/tracks/update</code></li>
</ul>
</li>
<li><strong>Renegotiate a Session</strong>: Updates the session's negotiation state to accommodate new tracks or changes in the existing ones.
<ul>
<li><code>PUT /apps/{appId}/sessions/{sessionId}/renegotiate</code></li>
</ul>
</li>
<li><strong>Close a Track</strong>: Removes a specified track from the session.
<ul>
<li><code>PUT /apps/{appId}/sessions/{sessionId}/tracks/close</code></li>
</ul>
</li>
<li><strong>Establish a DataChannel Transport</strong>: Pulls the <code>server-events</code> channel to establish DataChannel transport. Call this before you add DataChannels.
<ul>
<li><code>POST /apps/{appId}/sessions/{sessionId}/datachannels/establish</code></li>
</ul>
</li>
<li><strong>Add DataChannels</strong>: Publishes a local DataChannel or pulls a remote one (optional <code>waitForAck</code>, <code>canReply</code>).
<ul>
<li><code>POST /apps/{appId}/sessions/{sessionId}/datachannels/new</code></li>
</ul>
</li>
<li><strong>Update DataChannels</strong>: Grants or revokes flags on an already pulled remote DataChannel (for example <code>canReply</code>).
<ul>
<li><code>PUT /apps/{appId}/sessions/{sessionId}/datachannels/update</code></li>
</ul>
</li>
<li><strong>Close DataChannels</strong>: Removes a specified DataChannel from the session.
<ul>
<li><code>PUT /apps/{appId}/sessions/{sessionId}/datachannels/close</code></li>
</ul>
</li>
<li><strong>Retrieve Session Information</strong>: Fetches detailed information about a specific session.
<ul>
<li><code>GET /apps/{appId}/sessions/{sessionId}</code></li>
</ul>
</li>
</ul>
<p><a href="/realtime/static/realtime-api-2024-05-21.yaml">View full API and schema (OpenAPI format)</a></p>
<h2 id="handling-secrets">Handling Secrets</h2>
<p>It is vital to manage App ID and its secret securely. While track and session IDs can be public, they should be protected to prevent misuse. An attacker could exploit these IDs to disrupt service if your backend server does not authenticate request origins properly, for example by sending requests to close tracks on sessions other than their own. Ensuring the security and authenticity of requests to your backend server is crucial for maintaining the integrity of your application.</p>
<h2 id="using-stun-and-turn-servers">Using STUN and TURN Servers</h2>
<p>Cloudflare Realtime is designed to operate efficiently without the need for TURN servers in most scenarios, as Cloudflare exposes a publicly routable IP address for Realtime. However, integrating a STUN server can be necessary for facilitating peer discovery and connectivity.</p>
<ul>
<li><strong>Cloudflare STUN Server</strong>: <code>stun.cloudflare.com:3478</code></li>
</ul>
<p>Utilizing Cloudflare's STUN server can help the connection process for Realtime applications.</p>
<h2 id="lifecycle-of-a-simple-session">Lifecycle of a Simple Session</h2>
<p>This section provides an overview of the typical lifecycle of a simple session, focusing on audio-only applications. It illustrates how clients are notified by the backend server as new remote clients join or leave, incorporating video would introduce additional tracks and considerations into the session.</p>
<pre><code class="language-mermaid">sequenceDiagram&#10;    participant WA as WebRTC Agent&#10;    participant BS as Backend Server&#10;    participant CA as Realtime API&#10;&#10;    Note over BS: Client Joins&#10;&#10;    WA-&gt;&gt;BS: Request&#10;    BS-&gt;&gt;CA: POST /sessions/new&#10;    CA-&gt;&gt;BS: newSessionResponse&#10;    BS-&gt;&gt;WA: Response&#10;&#10;    WA-&gt;&gt;BS: Request&#10;    BS-&gt;&gt;CA: POST /sessions/&lt;ID&gt;/tracks/new (Offer)&#10;    CA-&gt;&gt;BS: newTracksResponse (Answer)&#10;    BS-&gt;&gt;WA: Response&#10;&#10;    WA--&gt;&gt;CA: ICE Connectivity Check&#10;    Note over WA: iceconnectionstatechange (connected)&#10;    WA--&gt;&gt;CA: DTLS Handshake&#10;    Note over WA: connectionstatechange (connected)&#10;&#10;    WA&lt;&lt;-&gt;&gt;CA: *Media Flow*&#10;&#10;    Note over BS: Remote Client Joins&#10;&#10;    WA-&gt;&gt;BS: Request&#10;    BS-&gt;&gt;CA: POST /sessions/&lt;ID&gt;/tracks/new&#10;    CA-&gt;&gt;BS: newTracksResponse (Offer)&#10;    BS-&gt;&gt;WA: Response&#10;&#10;    WA-&gt;&gt;BS: Request&#10;    BS-&gt;&gt;CA: PUT /sessions/&lt;ID&gt;/renegotiate (Answer)&#10;    CA-&gt;&gt;BS: OK&#10;    BS-&gt;&gt;WA: Response&#10;&#10;    Note over BS: Remote Client Leaves&#10;&#10;    WA-&gt;&gt;BS: Request&#10;    BS-&gt;&gt;CA: PUT /sessions/&lt;ID&gt;/tracks/close&#10;    CA-&gt;&gt;BS: closeTracksResponse&#10;    BS-&gt;&gt;WA: Response&#10;&#10;    Note over BS: Client Leaves&#10;&#10;    WA-&gt;&gt;BS: Request&#10;    BS-&gt;&gt;CA: PUT /sessions/&lt;ID&gt;/tracks/close&#10;    CA-&gt;&gt;BS: closeTracksResponse&#10;    BS-&gt;&gt;WA: Response&#10;</code></pre>
