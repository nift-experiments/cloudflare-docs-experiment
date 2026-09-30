---
cp9:
  canonical: https://developers.cloudflare.com/realtime/sfu/https-api/
  description: Manage Realtime SFU sessions and media tracks using the HTTPS connection API.
  full_title: Connection API · Cloudflare Realtime docs
  head_html: <title>Connection API · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Manage Realtime SFU sessions and media tracks using the HTTPS connection API."><link rel="canonical" href="https://developers.cloudflare.com/realtime/sfu/https-api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/sfu/https-api/index.md"><meta property="og:title" content="Connection API · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Manage Realtime SFU sessions and media tracks using the HTTPS connection API."><meta property="og:url" content="https://developers.cloudflare.com/realtime/sfu/https-api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/sfu/https-api/#page","headline":"Connection API \u00b7 Cloudflare Realtime docs","description":"Manage Realtime SFU sessions and media tracks using the HTTPS connection API.","url":"https://developers.cloudflare.com/realtime/sfu/https-api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/sfu/https-api/
  schema: 1
---
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
<pre tabindex="0"><code class="language-mermaid">sequenceDiagram&#10;    participant WA as WebRTC Agent&#10;    participant BS as Backend Server&#10;    participant CA as Realtime API&#10;&#10;    Note over BS: Client Joins&#10;&#10;    WA-&gt;&gt;BS: Request&#10;    BS-&gt;&gt;CA: POST /sessions/new&#10;    CA-&gt;&gt;BS: newSessionResponse&#10;    BS-&gt;&gt;WA: Response&#10;&#10;    WA-&gt;&gt;BS: Request&#10;    BS-&gt;&gt;CA: POST /sessions/&lt;ID&gt;/tracks/new (Offer)&#10;    CA-&gt;&gt;BS: newTracksResponse (Answer)&#10;    BS-&gt;&gt;WA: Response&#10;&#10;    WA--&gt;&gt;CA: ICE Connectivity Check&#10;    Note over WA: iceconnectionstatechange (connected)&#10;    WA--&gt;&gt;CA: DTLS Handshake&#10;    Note over WA: connectionstatechange (connected)&#10;&#10;    WA&lt;&lt;-&gt;&gt;CA: *Media Flow*&#10;&#10;    Note over BS: Remote Client Joins&#10;&#10;    WA-&gt;&gt;BS: Request&#10;    BS-&gt;&gt;CA: POST /sessions/&lt;ID&gt;/tracks/new&#10;    CA-&gt;&gt;BS: newTracksResponse (Offer)&#10;    BS-&gt;&gt;WA: Response&#10;&#10;    WA-&gt;&gt;BS: Request&#10;    BS-&gt;&gt;CA: PUT /sessions/&lt;ID&gt;/renegotiate (Answer)&#10;    CA-&gt;&gt;BS: OK&#10;    BS-&gt;&gt;WA: Response&#10;&#10;    Note over BS: Remote Client Leaves&#10;&#10;    WA-&gt;&gt;BS: Request&#10;    BS-&gt;&gt;CA: PUT /sessions/&lt;ID&gt;/tracks/close&#10;    CA-&gt;&gt;BS: closeTracksResponse&#10;    BS-&gt;&gt;WA: Response&#10;&#10;    Note over BS: Client Leaves&#10;&#10;    WA-&gt;&gt;BS: Request&#10;    BS-&gt;&gt;CA: PUT /sessions/&lt;ID&gt;/tracks/close&#10;    CA-&gt;&gt;BS: closeTracksResponse&#10;    BS-&gt;&gt;WA: Response&#10;</code></pre>
