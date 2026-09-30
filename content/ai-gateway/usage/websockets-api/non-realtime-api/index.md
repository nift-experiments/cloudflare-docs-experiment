<p>The Non-realtime WebSockets API allows you to establish persistent connections for AI requests without requiring repeated handshakes. This approach is ideal for applications that do not require real-time interactions but still benefit from reduced latency and continuous communication.</p>
<h2 id="set-up-websockets-api">Set up WebSockets API</h2>
<ol>
<li>Generate an AI Gateway token with appropriate AI Gateway Run and opt in to using an authenticated gateway.</li>
<li>Use the <code>wss://</code> protocol to initiate a WebSocket connection:</li>
</ol>
<pre><code>wss://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}&#10;</code></pre>
<ol start="3">
<li>Open a WebSocket connection authenticated with a Cloudflare token with the AI Gateway Run permission.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2948.md")
</aside>
<h2 id="example-request">Example request</h2>
<pre><code class="language-javascript">import WebSocket from &quot;ws&quot;;&#10;&#10;const ws = new WebSocket(&#10;	&quot;wss://gateway.ai.cloudflare.com/v1/my-account-id/my-gateway/&quot;,&#10;	{&#10;		headers: {&#10;			&quot;cf-aig-authorization&quot;: &quot;Bearer AI_GATEWAY_TOKEN&quot;,&#10;		},&#10;	},&#10;);&#10;&#10;ws.on(&quot;open&quot;, () =&gt; {&#10;	ws.send(&#10;		JSON.stringify({&#10;			type: &quot;universal.create&quot;,&#10;			request: {&#10;				eventId: &quot;my-request&quot;,&#10;				provider: &quot;workers-ai&quot;,&#10;				endpoint: &quot;@cf/meta/llama-3.1-8b-instruct&quot;,&#10;				headers: {&#10;					Authorization: &quot;Bearer WORKERS_AI_TOKEN&quot;,&#10;					&quot;Content-Type&quot;: &quot;application/json&quot;,&#10;				},&#10;				query: {&#10;					prompt: &quot;tell me a joke&quot;,&#10;				},&#10;			},&#10;		}),&#10;	);&#10;})&#10;&#10;ws.on(&quot;message&quot;, (message) =&gt; {&#10;	console.log(message.toString());&#10;});&#10;</code></pre>
<h2 id="example-response">Example response</h2>
<pre><code class="language-json">{&#10;	&quot;type&quot;: &quot;universal.created&quot;,&#10;	&quot;metadata&quot;: {&#10;		&quot;cacheStatus&quot;: &quot;MISS&quot;,&#10;		&quot;eventId&quot;: &quot;my-request&quot;,&#10;		&quot;logId&quot;: &quot;01JC3R94FRD97JBCBX3S0ZAXKW&quot;,&#10;		&quot;step&quot;: &quot;0&quot;,&#10;		&quot;contentType&quot;: &quot;application/json&quot;&#10;	},&#10;	&quot;response&quot;: {&#10;		&quot;result&quot;: {&#10;			&quot;response&quot;: &quot;Why was the math book sad? Because it had too many problems. Would you like to hear another one?&quot;&#10;		},&#10;		&quot;success&quot;: true,&#10;		&quot;errors&quot;: [],&#10;		&quot;messages&quot;: []&#10;	}&#10;}&#10;</code></pre>
<h2 id="example-streaming-request">Example streaming request</h2>
<p>For streaming requests, AI Gateway sends an initial message with request metadata indicating the stream is starting:</p>
<pre><code class="language-json">{&#10;	&quot;type&quot;: &quot;universal.created&quot;,&#10;	&quot;metadata&quot;: {&#10;		&quot;cacheStatus&quot;: &quot;MISS&quot;,&#10;		&quot;eventId&quot;: &quot;my-request&quot;,&#10;		&quot;logId&quot;: &quot;01JC40RB3NGBE5XFRZGBN07572&quot;,&#10;		&quot;step&quot;: &quot;0&quot;,&#10;		&quot;contentType&quot;: &quot;text/event-stream&quot;&#10;	}&#10;}&#10;</code></pre>
<p>After this initial message, all streaming chunks are relayed in real-time to the WebSocket connection as they arrive from the inference provider. Only the <code>eventId</code> field is included in the metadata for these streaming chunks. The <code>eventId</code> allows AI Gateway to include a client-defined ID with each message, even in a streaming WebSocket environment.</p>
<pre><code class="language-json">{&#10;	&quot;type&quot;: &quot;universal.stream&quot;,&#10;	&quot;metadata&quot;: {&#10;		&quot;eventId&quot;: &quot;my-request&quot;&#10;	},&#10;	&quot;response&quot;: {&#10;		&quot;response&quot;: &quot;would&quot;&#10;	}&#10;}&#10;</code></pre>
<p>Once all chunks for a request have been streamed, AI Gateway sends a final message to signal the completion of the request. For added flexibility, this message includes all the metadata again, even though it was initially provided at the start of the streaming process.</p>
<pre><code class="language-json">{&#10;	&quot;type&quot;: &quot;universal.done&quot;,&#10;	&quot;metadata&quot;: {&#10;		&quot;cacheStatus&quot;: &quot;MISS&quot;,&#10;		&quot;eventId&quot;: &quot;my-request&quot;,&#10;		&quot;logId&quot;: &quot;01JC40RB3NGBE5XFRZGBN07572&quot;,&#10;		&quot;step&quot;: &quot;0&quot;,&#10;		&quot;contentType&quot;: &quot;text/event-stream&quot;&#10;	}&#10;}&#10;</code></pre>
