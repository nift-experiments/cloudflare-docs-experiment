---
cp9:
  canonical: https://developers.cloudflare.com/realtime/sfu/datachannels/
  description: Send low-latency application data between clients with Realtime SFU DataChannels.
  full_title: DataChannels · Cloudflare Realtime docs
  head_html: <title>DataChannels · Cloudflare Realtime docs</title><meta name="generator" content="Nift"><meta name="description" content="Send low-latency application data between clients with Realtime SFU DataChannels."><link rel="canonical" href="https://developers.cloudflare.com/realtime/sfu/datachannels/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/realtime/sfu/datachannels/index.md"><meta property="og:title" content="DataChannels · Cloudflare Realtime docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Send low-latency application data between clients with Realtime SFU DataChannels."><meta property="og:url" content="https://developers.cloudflare.com/realtime/sfu/datachannels/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Realtime"><meta name="algolia_product_filter" content="Realtime"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Realtime"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/realtime/sfu/datachannels/#page","headline":"DataChannels \u00b7 Cloudflare Realtime docs","description":"Send low-latency application data between clients with Realtime SFU DataChannels.","url":"https://developers.cloudflare.com/realtime/sfu/datachannels/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /realtime/sfu/datachannels/
  schema: 1
---
<p>Use Realtime SFU DataChannels to send low-latency application data over WebRTC. Common payloads include chat messages, game state, sensor updates, and control events.</p>
<p>Use Realtime SFU media tracks, rather than DataChannels, to send audio and video.</p>
<pre tabindex="0"><code class="language-mermaid">graph LR&#10;    A[Publisher] --&gt;|Application data| B[Cloudflare Realtime SFU]&#10;    B --&gt;|Application data| C@{ shape: procs, label: &quot;Subscribers&quot;}&#10;</code></pre>
<p>Each publisher can send a named DataChannel to multiple subscribers. By default, messages flow from the publisher to subscribers.</p>
<h2 id="set-up-a-datachannel">Set up a DataChannel</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11586.md")
</div>
<h2 id="configure-message-delivery">Configure message delivery</h2>
<p>DataChannels use reliable, ordered delivery by default. Choose partial reliability or unordered delivery when recent data matters more than delayed data, such as game state or live sensor updates.</p>
<p>Set these optional fields when you create a DataChannel with the <a href="/realtime/sfu/https-api/">HTTPS API</a>:</p>
<ul>
<li><code>ordered</code> (<code>boolean</code>, default <code>true</code>): Set to <code>false</code> to allow messages to arrive out of order. A delayed message will not block later messages.</li>
<li><code>maxRetransmits</code> (<code>integer</code>): Limits retransmission attempts after the first send. Set to <code>0</code> for no retransmissions, or omit for no retransmission limit.</li>
<li><code>maxPacketLifeTime</code> (<code>integer</code>): Limits how long, in milliseconds, the transport attempts delivery. Omit for no lifetime limit.</li>
</ul>
<p><code>maxRetransmits</code> and <code>maxPacketLifeTime</code> are mutually exclusive. Do not set both on the same channel.</p>
<p>Ordering and retry behavior are independent. For reliable, unordered delivery, set <code>ordered: false</code> and omit both <code>maxRetransmits</code> and <code>maxPacketLifeTime</code>. Messages may arrive out of order, but the transport continues to retry failed deliveries.</p>
<p>Use the same values on the publisher (<code>location: &quot;local&quot;</code>), each subscriber (<code>location: &quot;remote&quot;</code>), and each client's <code>createDataChannel()</code> call. Realtime DataChannels use negotiated IDs, so the browser does not receive these settings from the remote peer.</p>
<p>Create an unreliable, unordered publisher channel:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;dataChannels&quot;: [&#10;		{&#10;			&quot;location&quot;: &quot;local&quot;,&#10;			&quot;dataChannelName&quot;: &quot;player-state&quot;,&#10;			&quot;ordered&quot;: false,&#10;			&quot;maxRetransmits&quot;: 0&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>Then create the matching remote channel on the subscriber with the same reliability fields:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;dataChannels&quot;: [&#10;		{&#10;			&quot;location&quot;: &quot;remote&quot;,&#10;			&quot;sessionId&quot;: &quot;&lt;PUBLISHER_SESSION_ID&gt;&quot;,&#10;			&quot;dataChannelName&quot;: &quot;player-state&quot;,&#10;			&quot;ordered&quot;: false,&#10;			&quot;maxRetransmits&quot;: 0&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>Create the matching browser DataChannel with the same settings. In this example, <code>pc</code> is the active <code>RTCPeerConnection</code>, and <code>resp</code> is the API response for the channel.</p>
<pre tabindex="0"><code class="language-ts">const dc = pc.createDataChannel(&quot;player-state&quot;, {&#10;	negotiated: true,&#10;	id: resp.dataChannels[0].id,&#10;	ordered: false,&#10;	maxRetransmits: 0,&#10;});&#10;</code></pre>
<p>For partial reliability, choose a retransmission limit or packet lifetime based on how long the payload remains useful.</p>
<h2 id="wait-for-subscriber-readiness-waitforack">Wait for subscriber readiness (<code>waitForAck</code>)</h2>
<p>Set <code>waitForAck: true</code> on a remote DataChannel to delay delivery until the subscriber signals that it is ready.</p>
<ul>
<li><code>waitForAck</code> applies only to <code>location: &quot;remote&quot;</code> DataChannels and defaults to <code>false</code>.</li>
<li>While the gate is closed, the SFU holds delivery to that subscriber.</li>
<li>After the DataChannel opens, the subscriber sends any message, such as <code>&quot;ack&quot;</code>. The SFU consumes this first message, opens the gate, and starts forwarding publisher messages.</li>
<li>The acknowledgment must reach the SFU within 30 seconds after creating the remote DataChannel. Otherwise, the SFU tears down the gated channel. Create the remote DataChannel again to retry.</li>
</ul>
<p>Without <a href="#return-to-publisher-canreply"><code>canReply</code></a>, later subscriber messages are not forwarded to the publisher.</p>
<p>Create a remote DataChannel with the gate enabled by calling <code>POST /apps/{appId}/sessions/{sessionId}/datachannels/new</code> on the subscriber session:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;dataChannels&quot;: [&#10;		{&#10;			&quot;location&quot;: &quot;remote&quot;,&#10;			&quot;sessionId&quot;: &quot;&lt;PUBLISHER_SESSION_ID&gt;&quot;,&#10;			&quot;dataChannelName&quot;: &quot;my-channel&quot;,&#10;			&quot;waitForAck&quot;: true&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>Then, on the subscriber, send the acknowledgment once the DataChannel is open. This example assumes you have initialized <code>API_BASE</code>, <code>headers</code>, and <code>pc</code>, and defined a <code>waitForOpen()</code> helper.</p>
<pre tabindex="0"><code class="language-ts">const response = await fetch(&#10;	`${API_BASE}/sessions/${subscriberId}/datachannels/new`,&#10;	{&#10;		method: &quot;POST&quot;,&#10;		headers,&#10;		body: JSON.stringify({&#10;			dataChannels: [&#10;				{&#10;					location: &quot;remote&quot;,&#10;					sessionId: publisherId,&#10;					dataChannelName: &quot;my-channel&quot;,&#10;					waitForAck: true,&#10;				},&#10;			],&#10;		}),&#10;	},&#10;);&#10;&#10;if (!response.ok) {&#10;	throw new Error(`Failed to create DataChannel: ${response.status}`);&#10;}&#10;&#10;const resp = await response.json();&#10;const channelId = resp.dataChannels?.[0]?.id;&#10;if (channelId === undefined) {&#10;	throw new Error(&quot;DataChannel response did not include an id&quot;);&#10;}&#10;&#10;const dc = pc.createDataChannel(&quot;my-channel-subscribed&quot;, {&#10;	negotiated: true,&#10;	id: channelId,&#10;});&#10;&#10;await waitForOpen(dc);&#10;dc.send(&quot;ack&quot;); // The first message opens the gate.&#10;</code></pre>
<h2 id="return-to-publisher-canreply">Return to publisher (canReply)</h2>
<p>Messages travel from the publisher to subscribers by default. Set <code>canReply: true</code> when one subscriber needs to respond on the same channel, such as an operator responding to a device that publishes telemetry.</p>
<pre tabindex="0"><code class="language-mermaid">graph LR&#10;    P[Publisher] --&gt;|Publisher messages| SFU[Cloudflare Realtime SFU]&#10;    SFU --&gt;|Publisher messages| S1[Subscriber with canReply]&#10;    SFU --&gt;|Publisher messages| S2[Other subscribers]&#10;    S1 --&gt;|Reply| SFU&#10;    SFU --&gt;|Reply| P&#10;</code></pre>
<p><code>canReply</code> controls reply access as follows:</p>
<ul>
<li><code>canReply</code> applies only to <code>location: &quot;remote&quot;</code> DataChannels and defaults to <code>false</code>.</li>
<li>At most one subscriber can have reply access for each publisher DataChannel. Granting access to another subscriber replaces the previous subscriber.</li>
<li>The SFU forwards replies only from the subscriber with access.</li>
<li>The publisher receives the replies. Other subscribers do not.</li>
</ul>
<h3 id="allow-replies-when-subscribing">Allow replies when subscribing</h3>
<p>Create the remote DataChannel on the subscriber session with <code>canReply: true</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;dataChannels&quot;: [&#10;		{&#10;			&quot;location&quot;: &quot;remote&quot;,&#10;			&quot;sessionId&quot;: &quot;&lt;PUBLISHER_SESSION_ID&gt;&quot;,&#10;			&quot;dataChannelName&quot;: &quot;my-channel&quot;,&#10;			&quot;canReply&quot;: true&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>Example flow:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11587.md")
</div>
<h3 id="change-reply-access">Change reply access</h3>
<p>To change reply access without recreating the remote DataChannel, call <code>PUT /apps/{appId}/sessions/{subscriberSessionId}/datachannels/update</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;dataChannels&quot;: [&#10;		{&#10;			&quot;location&quot;: &quot;remote&quot;,&#10;			&quot;sessionId&quot;: &quot;&lt;PUBLISHER_SESSION_ID&gt;&quot;,&#10;			&quot;dataChannelName&quot;: &quot;my-channel&quot;,&#10;			&quot;canReply&quot;: true&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>Use the same body with <code>&quot;canReply&quot;: false</code> to revoke. The following table lists common patterns:</p>
<table>
<thead>
<tr>
<th>Goal</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Allow replies after subscribing</td>
<td>Create the remote DataChannel without <code>canReply</code>, then update it with <code>canReply: true</code>.</td>
</tr>
<tr>
<td>Move access to another subscriber</td>
<td>On the new subscriber, update the DataChannel with <code>canReply: true</code>. The previous subscriber loses reply access.</td>
</tr>
<tr>
<td>Stop replies</td>
<td>On the subscriber with reply access, update the DataChannel with <code>canReply: false</code>.</td>
</tr>
</tbody>
</table>
<pre tabindex="0"><code class="language-ts">// The subscriber already pulled &quot;my-channel&quot; without canReply.&#10;// Allow replies later.&#10;const response = await fetch(&#10;	`${API_BASE}/sessions/${subscriberId}/datachannels/update`,&#10;	{&#10;		method: &quot;PUT&quot;,&#10;		headers,&#10;		body: JSON.stringify({&#10;			dataChannels: [&#10;				{&#10;					location: &quot;remote&quot;,&#10;					sessionId: publisherId,&#10;					dataChannelName: &quot;my-channel&quot;,&#10;					canReply: true,&#10;				},&#10;			],&#10;		}),&#10;	},&#10;);&#10;&#10;if (!response.ok) {&#10;	throw new Error(`Failed to update DataChannel: ${response.status}`);&#10;}&#10;&#10;// The same negotiated DataChannel can now send replies to the publisher.&#10;dc.send(JSON.stringify({ type: &quot;reply&quot;, body: &quot;pong&quot; }));&#10;</code></pre>
<h3 id="combine-acknowledgment-and-replies">Combine acknowledgment and replies</h3>
<p>You can set both <code>canReply</code> and <code>waitForAck</code> on the same remote DataChannel. The subscriber's first message opens the acknowledgment gate and is not forwarded. Later subscriber messages are forwarded to the publisher while that subscriber has reply access.</p>
<h2 id="example">Example</h2>
<p>Review the <a href="https://github.com/cloudflare/realtime-examples/tree/main/echo-datachannels">DataChannel echo example</a> for complete transport, publishing, and subscription setup.</p>
<p>The example places an app token in browser code for local testing. In production, keep the token on your backend.</p>
