<p>The AI Gateway WebSockets API provides a persistent connection for AI interactions, eliminating repeated handshakes and reducing latency. This API is divided into two categories:</p>
<ul>
<li><strong>Realtime APIs</strong> - Designed for AI providers that offer low-latency, multimodal interactions over WebSockets.</li>
<li><strong>Non-Realtime APIs</strong> - Supports standard WebSocket communication for AI providers, including those that do not natively support WebSockets.</li>
</ul>
<h2 id="when-to-use-websockets">When to use WebSockets</h2>
<p>WebSockets are long-lived TCP connections that enable bi-directional, real-time and non realtime communication between client and server. Unlike HTTP connections, which require repeated handshakes for each request, WebSockets maintain the connection, supporting continuous data exchange with reduced overhead. WebSockets are ideal for applications needing low-latency, real-time data, such as voice assistants.</p>
<h2 id="key-benefits">Key benefits</h2>
<ul>
<li><strong>Reduced overhead</strong>: Avoid overhead of repeated handshakes and TLS negotiations by maintaining a single, persistent connection.</li>
<li><strong>Provider compatibility</strong>: Works with all AI providers in AI Gateway. Even if your chosen provider does not support WebSockets, Cloudflare handles it for you, managing the requests to your preferred AI provider.</li>
</ul>
<h2 id="key-differences">Key differences</h2>
<table>
<thead>
<tr>
<th align="left">Feature</th>
<th align="left">Realtime APIs</th>
<th align="left">Non-Realtime APIs</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><strong>Purpose</strong></td>
<td align="left">Enables real-time, multimodal AI interactions for providers that offer dedicated WebSocket endpoints.</td>
<td align="left">Supports WebSocket-based AI interactions with providers that do not natively support WebSockets.</td>
</tr>
<tr>
<td align="left"><strong>Use Case</strong></td>
<td align="left">Streaming responses for voice, video, and live interactions.</td>
<td align="left">Text-based queries and responses, such as LLM requests.</td>
</tr>
<tr>
<td align="left"><strong>AI Provider Support</strong></td>
<td align="left"><a href="/ai-gateway/usage/websockets-api/realtime-api/#supported-providers">Limited to providers offering real-time WebSocket APIs.</a></td>
<td align="left"><a href="/ai-gateway/usage/providers/">All AI providers in AI Gateway.</a></td>
</tr>
<tr>
<td align="left"><strong>Streaming Support</strong></td>
<td align="left">Providers natively support real-time data streaming.</td>
<td align="left">AI Gateway handles streaming via WebSockets.</td>
</tr>
</tbody>
</table>
<p>For details on implementation, refer to the next sections:</p>
<ul>
<li><a href="/ai-gateway/usage/websockets-api/realtime-api/">Realtime WebSockets API</a></li>
<li><a href="/ai-gateway/usage/websockets-api/non-realtime-api/">Non-Realtime WebSockets API</a></li>
</ul>
