<p>Cloudflare will issue TURN keys, but these keys cannot be used as credentials with <code>turn.cloudflare.com</code>. To use TURN, you need to create credentials with a expiring TTL value.</p>
<h2 id="create-a-turn-key">Create a TURN key</h2>
<p>To create a TURN credential, you first need to create a TURN key using <a href="https://dash.cloudflare.com/?to=/:account/calls">Dashboard</a>, or the <a href="/api/resources/calls/subresources/turn/methods/create/">API</a>.</p>
<p>You should keep your TURN key on the server side (don't share it with the browser/app). A TURN key is a long-term secret that allows you to generate unlimited, shorter lived TURN credentials for TURN clients.</p>
<p>With a TURN key you can:</p>
<ul>
<li>Generate TURN credentials that expire</li>
<li>Revoke previously issued TURN credentials</li>
</ul>
<h2 id="create-credentials">Create credentials</h2>
<p>You should generate short-lived credentials for each TURN user. In order to create credentials, you should have a back-end service that uses your TURN Token ID and API token to generate credentials. It will make an API call like this:</p>
<pre><code class="language-bash">curl https://rtc.live.cloudflare.com/v1/turn/keys/$TURN_KEY_ID/credentials/generate-ice-servers \&#10;&#45;-header &quot;Authorization: Bearer $TURN_KEY_API_TOKEN&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&quot;ttl&quot;: 86400}&#x27;&#10;</code></pre>
<p>The <strong>201 (Created)</strong> response below can then be passed on to your front-end application:</p>
<pre><code class="language-json">{&#10;  &quot;iceServers&quot;: [&#10;		{&#10;			&quot;urls&quot;: [&#10;				&quot;stun:stun.cloudflare.com:3478&quot;&#10;			]&#10;		},&#10;		{&#10;			&quot;urls&quot;: [&#10;				&quot;turn:turn.cloudflare.com:3478?transport=udp&quot;,&#10;				&quot;turn:turn.cloudflare.com:3478?transport=tcp&quot;,&#10;				&quot;turn:turn.cloudflare.com:80?transport=tcp&quot;,&#10;				&quot;turns:turn.cloudflare.com:5349?transport=tcp&quot;,&#10;				&quot;turns:turn.cloudflare.com:443?transport=tcp&quot;&#10;			],&#10;			&quot;username&quot;: &quot;bc91b63e2b5d759f8eb9f3b58062439e0a0e15893d76317d833265ad08d6631099ce7c7087caabb31ad3e1c386424e3e&quot;,&#10;			&quot;credential&quot;: &quot;ebd71f1d3edbc2b0edae3cd5a6d82284aeb5c3b8fdaa9b8e3bf9cec683e0d45fe9f5b44e5145db3300f06c250a15b4a0&quot;&#10;		}&#10;	]&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11567.md")
</aside>
<p>Use <code>iceServers</code> as follows when instantiating the <code>RTCPeerConnection</code>:</p>
<pre><code class="language-js">const myPeerConnection = new RTCPeerConnection({&#10;  iceServers: [&#10;    {&#10;      urls: [&#10;				&quot;stun:stun.cloudflare.com:3478&quot;&#10;			]&#10;		},&#10;		{&#10;			urls: [&#10;				&quot;turn:turn.cloudflare.com:3478?transport=udp&quot;,&#10;				&quot;turn:turn.cloudflare.com:3478?transport=tcp&quot;,&#10;				&quot;turn:turn.cloudflare.com:80?transport=tcp&quot;,&#10;				&quot;turns:turn.cloudflare.com:5349?transport=tcp&quot;,&#10;				&quot;turns:turn.cloudflare.com:443?transport=tcp&quot;&#10;      ],&#10;			&quot;username&quot;: &quot;bc91b63e2b5d759f8eb9f3b58062439e0a0e15893d76317d833265ad08d6631099ce7c7087caabb31ad3e1c386424e3e&quot;,&#10;			&quot;credential&quot;: &quot;ebd71f1d3edbc2b0edae3cd5a6d82284aeb5c3b8fdaa9b8e3bf9cec683e0d45fe9f5b44e5145db3300f06c250a15b4a0&quot;&#10;    },&#10;  ],&#10;});&#10;</code></pre>
<p>The <code>ttl</code> value can be adjusted to expire the short lived key in a certain amount of time. This value should be larger than the time you'd expect the users to use the TURN service. For example, if you're using TURN for a video conferencing app, the value should be set to the longest video call you'd expect to happen in the app.</p>
<p>When using short-lived TURN credentials with WebRTC, credentials can be refreshed during a WebRTC session using the <code>RTCPeerConnection</code> <a href="https://developer.mozilla.org/en-US/docs/Web/API/RTCPeerConnection/setConfiguration"><code>setConfiguration()</code></a> API.</p>
<h2 id="revoke-credentials">Revoke credentials</h2>
<p>Short lived credentials can also be revoked before their TTL expires with a API call like this:</p>
<pre><code class="language-bash">curl --request POST \&#10;https://rtc.live.cloudflare.com/v1/turn/keys/$TURN_KEY_ID/credentials/$USERNAME/revoke \&#10;&#45;-header &quot;Authorization: Bearer $TURN_KEY_API_TOKEN&quot;&#10;</code></pre>
<p>A <strong>204 (No Content)</strong> response is returned if the credential is successfully revoked.</p>
