<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 13, 2026</time><h2 id="post-title">Control Realtime SFU DataChannel delivery</h2>
<div class="changelog-badges"><span>realtime</span></div><div class="changelog-body"><p><a href="/realtime/sfu/">Cloudflare Realtime SFU</a> is a <a href="/realtime/sfu/calls-vs-sfus/">WebRTC selective forwarding unit</a> that runs on Cloudflare's global network. It forwards audio, video, and application data between WebRTC clients without requiring you to manage SFU infrastructure or regions.</p>
<p><a href="/realtime/sfu/datachannels/">DataChannels</a> are WebRTC channels for application messages. A client publishes a named DataChannel to Realtime SFU, and the SFU forwards its messages to every client that subscribes to that channel. Use DataChannels for low-latency payloads such as chat messages, game state, sensor updates, and control events.</p>
<h4 id="what-changed">What changed</h4>
<p>Realtime SFU DataChannels now support unordered and partially reliable delivery. DataChannels remain reliable and ordered by default, so existing channels keep their current behavior.</p>
<p>With ordered delivery, a delayed message can block later messages. For game state or sensor updates, recent data may be more useful than recovering an older message. Unordered delivery lets later messages proceed, while partial reliability limits retransmission attempts or delivery time.</p>
<h4 id="choose-delivery-behavior">Choose delivery behavior</h4>
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
<h4 id="apply-the-policy-end-to-end">Apply the policy end to end</h4>
<p>Realtime DataChannels use negotiated IDs, so browsers do not receive delivery settings from the remote peer. Apply the same settings when the publisher creates the local channel, each subscriber pulls the remote channel, and each client calls <code>createDataChannel()</code>.</p>
<p>The following example configures unordered delivery with no retransmissions. It begins after you <a href="/realtime/sfu/datachannels/#set-up-a-datachannel">establish a DataChannel transport on both sessions and complete any required SDP exchange</a>. Run the API requests from your backend with <code>APP_ID</code>, <code>APP_TOKEN</code>, <code>PUBLISHER_SESSION_ID</code>, and <code>SUBSCRIBER_SESSION_ID</code> set in your environment.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17744.md")</div>
<h4 id="related-documentation">Related documentation</h4>
<ul>
<li><a href="/realtime/sfu/">Realtime SFU overview</a></li>
<li><a href="/realtime/sfu/datachannels/">DataChannels</a></li>
<li><a href="/realtime/sfu/https-api/">Connection API</a></li>
</ul>
</div></article></div>
