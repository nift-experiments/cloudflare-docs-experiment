<p>MoQ (Media over QUIC) is a protocol for delivering live media content using QUIC transport. It provides efficient, low-latency media streaming by leveraging QUIC's multiplexing and connection management capabilities.</p>
<p>MoQ is designed to be an Internet infrastructure level service that provides media delivery to applications, similar to how HTTP provides content delivery and WebRTC provides real-time communication.</p>
<p>Cloudflare currently supports <a href="https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-14">draft-14</a> and <a href="https://www.ietf.org/archive/id/draft-ietf-moq-transport-16.html">draft-16</a> of the MoQ Transport specification. For a full breakdown of supported messages per draft, refer to <a href="/moq/feature-matrix/">MoQ Feature Matrix</a>.</p>
<p>For the most up-to-date documentation on the protocol, please visit the IETF working group documentation.</p>
<h2 id="get-started">Get started</h2>
<p>Cloudflare MoQ relays are available through the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and the <a href="/api/resources/moq">API</a>. They are free to use during the beta period.</p>
<h3 id="provision-a-relay">Provision a relay</h3>
<p>Each relay provides an isolated scope — your namespaces, tracks, and objects are separated from those belonging to other relays. You control who can publish and who can subscribe by issuing tokens scoped to the operations each client needs.</p>
<p>To create a relay via the API:</p>
<pre><code class="language-sh">curl -X POST \&#10;  &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/moq/relays&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&quot;name&quot;: &quot;My Relay&quot;}&#x27;&#10;</code></pre>
<p>Cloudflare returns a relay ID and two default tokens: one that can publish and subscribe, and one that can only subscribe. Token secrets are shown once in the response and never stored.</p>
<p>You can also create and manage relays in the Cloudflare dashboard under <strong>Media</strong> &gt; <strong>Realtime</strong> &gt; <strong>MoQ Relay</strong>.</p>
<h3 id="connect-a-publisher-and-subscriber-draft-16">Connect a publisher and subscriber (draft-16)</h3>
<p>Draft-16 requires authentication. Clients send a token in the URL path when opening a MoQ session. Using the open-source <a href="https://github.com/cloudflare/moq-rs">moq-rs</a> tools:</p>
<p><strong>Publisher:</strong></p>
<pre><code class="language-sh">ffmpeg -stream_loop -1 -re -i input.mp4 \&#10;  &#45;f mp4 -movflags empty_moov+frag_every_frame+separate_moof+omit_tfhd_offset - \&#10;  | moq-pub --name my-namespace \&#10;    &quot;https://draft-16.cloudflare.mediaoverquic.com/&lt;publish_subscribe_token&gt;&quot;&#10;</code></pre>
<p><strong>Subscriber:</strong></p>
<pre><code class="language-sh">moq-sub --name my-namespace \&#10;  &quot;https://draft-16.cloudflare.mediaoverquic.com/&lt;subscribe_token&gt;&quot; \&#10;  | ffplay -hide_banner -&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="token-security">Token security</h3>
@markup("md", "content/.markup/bodies/742.md")
</aside>
<h3 id="connect-a-publisher-and-subscriber-draft-14">Connect a publisher and subscriber (draft-14)</h3>
<p>Draft-14 clients connect to:</p>
<pre><code class="language-txt">https://draft-14.cloudflare.mediaoverquic.com/&#10;</code></pre>
<h3 id="test-draft-18">Test draft-18</h3>
<p>Cloudflare is working on draft-18 support ahead of a global deployment. To test against a draft-18 relay in the meantime, refer to <a href="https://github.com/englishm/moq-interop-runner">moq-interop-runner</a>.</p>
