<p>Agents can handle HTTP requests and stream responses using Server-Sent Events (SSE). This page covers the <code>onRequest</code> method and SSE patterns.</p>
<h2 id="handling-http-requests">Handling HTTP requests</h2>
<p>Define the <code>onRequest</code> method to handle HTTP requests to your agent:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2633.md")
</div>
<h2 id="server-sent-events-sse">Server-Sent Events (SSE)</h2>
<p>SSE allows you to stream data to clients over a long-running HTTP connection. This is ideal for AI model responses that generate tokens incrementally.</p>
<h3 id="manual-sse">Manual SSE</h3>
<p>Create an SSE stream manually using <code>ReadableStream</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2634.md")
</div>
<h3 id="sse-message-format">SSE message format</h3>
<p>SSE messages follow a specific format:</p>
<pre><code class="language-txt">data: your message here\n\n&#10;</code></pre>
<p>You can also include event types and IDs:</p>
<pre><code class="language-txt">event: update\n&#10;id: 123\n&#10;data: {&quot;count&quot;: 42}\n\n&#10;</code></pre>
<h3 id="with-ai-sdk">With AI SDK</h3>
<p>The <a href="https://ai-sdk.dev/">AI SDK</a> provides built-in SSE streaming:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2635.md")
</div>
<h2 id="connection-handling">Connection handling</h2>
<p>SSE connections can be long-lived. Handle client disconnects gracefully:</p>
<ul>
<li><strong>Persist progress</strong> — Write to <a href="/agents/runtime/lifecycle/state/">agent state</a> so clients can resume</li>
<li><strong>Use agent routing</strong> — Clients can <a href="/agents/runtime/communication/routing/">reconnect to the same agent instance</a> without session stores</li>
<li><strong>No timeout limits</strong> — Cloudflare Workers have no effective limit on SSE response duration</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2636.md")
</div>
<h2 id="websockets-vs-sse">WebSockets vs SSE</h2>
<table>
<thead>
<tr>
<th>Feature</th>
<th>WebSockets</th>
<th>SSE</th>
</tr>
</thead>
<tbody>
<tr>
<td>Direction</td>
<td>Bi-directional</td>
<td>Server → Client only</td>
</tr>
<tr>
<td>Protocol</td>
<td><code>ws://</code> / <code>wss://</code></td>
<td>HTTP</td>
</tr>
<tr>
<td>Binary data</td>
<td>Yes</td>
<td>No (text only)</td>
</tr>
<tr>
<td>Reconnection</td>
<td>Manual</td>
<td>Automatic (browser)</td>
</tr>
<tr>
<td>Best for</td>
<td>Interactive apps, chat</td>
<td>Streaming responses, notifications</td>
</tr>
</tbody>
</table>
<p><strong>Recommendation:</strong> Use WebSockets for interactive applications. Use SSE for streaming AI responses or server-push notifications.</p>
<p>Refer to <a href="/agents/runtime/communication/websockets/">WebSockets</a> for WebSocket documentation.</p>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/agents/runtime/communication/websockets/"><h3 id="card-websockets-agents-runtime-communication-websockets">WebSockets</h3><p>Bi-directional real-time communication.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/lifecycle/state/"><h3 id="card-state-management-agents-runtime-lifecycle-state">State management</h3><p>Persist stream progress and agent state.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/examples/chat-agent/"><h3 id="card-build-a-chat-agent-agents-examples-chat-agent">Build a chat agent</h3><p>Streaming responses with AI chat.</p></a></p>
