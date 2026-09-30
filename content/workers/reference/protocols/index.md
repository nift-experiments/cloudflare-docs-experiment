<p>Cloudflare Workers support the following protocols and interfaces:</p>
<table>
<thead>
<tr>
<th>Protocol</th>
<th>Inbound</th>
<th>Outbound</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>HTTP / HTTPS</strong></td>
<td>Handle incoming HTTP requests using the <a href="/workers/runtime-apis/handlers/fetch/"><code>fetch()</code> handler</a></td>
<td>Make HTTP subrequests using the <a href="/workers/runtime-apis/fetch/"><code>fetch()</code> API</a></td>
</tr>
<tr>
<td><strong>Direct TCP sockets</strong></td>
<td>Support for handling inbound TCP connections is <a href="https://blog.cloudflare.com/workers-tcp-socket-api-connect-databases/">coming soon</a></td>
<td>Create outbound TCP connections using the <a href="/workers/runtime-apis/tcp-sockets/"><code>connect()</code> API</a></td>
</tr>
<tr>
<td><strong>WebSockets</strong></td>
<td>Accept incoming WebSocket connections using the <a href="/workers/runtime-apis/websockets/"><code>WebSocket</code> API</a></td>
<td></td>
</tr>
<tr>
<td><strong>HTTP/3 (QUIC)</strong></td>
<td>Accept inbound requests over <a href="https://www.cloudflare.com/learning/performance/what-is-http3/">HTTP/3</a> by enabling it on your <a href="/fundamentals/concepts/accounts-and-zones/#zones">zone</a> in <strong>Speed</strong> &gt; <strong>Settings</strong> &gt; <strong>Protocol Optimization</strong> area of the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>.</td>
<td></td>
</tr>
<tr>
<td><strong>SMTP</strong></td>
<td>Use <a href="/email-service/api/route-emails/email-handler/">Email Workers</a> to process and forward email, without having to manage TCP connections to SMTP email servers</td>
<td><a href="/email-service/api/route-emails/email-handler/">Email Workers</a></td>
</tr>
</tbody>
</table>
