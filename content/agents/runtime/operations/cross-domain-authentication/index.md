<p>When your Agents are deployed, to keep things secure, send a token from the client, then verify it on the server. This guide covers authentication patterns for WebSocket connections to agents.</p>
<h2 id="websocket-authentication">WebSocket authentication</h2>
<p>WebSockets are not HTTP, so the handshake is limited when making cross-domain connections.</p>
<p>You cannot send:</p>
<ul>
<li>Custom headers during the upgrade</li>
<li><code>Authorization: Bearer ...</code> on connect</li>
</ul>
<p>You can:</p>
<ul>
<li>Put a signed, short-lived token in the connection URL as query parameters</li>
<li>Verify the token in your server's connect path</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2300.md")
</aside>
<h3 id="same-origin">Same origin</h3>
<p>If the client and server share the origin, the browser will send cookies during the WebSocket handshake. Session-based auth can work here. Prefer HTTP-only cookies.</p>
<h3 id="cross-origin">Cross origin</h3>
<p>Cross-origin cookie behavior depends on the cookie's domain and <code>SameSite</code> attributes, whether the two origins are same-site, and browser third-party cookie policy. If you cannot rely on a cookie, pass a short-lived credential in the URL query and verify it on the server.</p>
<h2 id="usage-examples">Usage examples</h2>
<h3 id="static-authentication">Static authentication</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2301.md")
</div>
<h3 id="async-authentication">Async authentication</h3>
<p>Build query values right before connect. Use Suspense for async setup.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2302.md")
</div>
<h3 id="jwt-refresh-pattern">JWT refresh pattern</h3>
<p><code>useAgent</code> resolves an async query before connecting and reevaluates it when reconnecting. Return a fresh, short-lived application token each time:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2303.md")
</div>
<h2 id="cross-domain-authentication">Cross-domain authentication</h2>
<p>Pass credentials in the URL when connecting to another host, then verify on the server.</p>
<h3 id="static-cross-domain-auth">Static cross-domain auth</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2304.md")
</div>
<h3 id="async-cross-domain-auth">Async cross-domain auth</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2305.md")
</div>
<h2 id="server-side-verification">Server-side verification</h2>
<p>On the server side, verify the token in the <code>onConnect</code> handler:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2306.md")
</div>
<h2 id="best-practices">Best practices</h2>
<ol>
<li>
<p><strong>Use short-lived tokens</strong> - Tokens in URLs may be logged. Keep expiration times short (minutes, not hours).</p>
</li>
<li>
<p><strong>Scope tokens appropriately</strong> - Include the agent name or instance in the token claims to prevent token reuse across agents.</p>
</li>
<li>
<p><strong>Validate on every connection</strong> - Always verify tokens in <code>onConnect</code>, not just once.</p>
</li>
<li>
<p><strong>Use HTTPS</strong> - Always use secure WebSocket connections (<code>wss://</code>) in production.</p>
</li>
<li>
<p><strong>Rotate secrets</strong> - Regularly rotate your JWT signing keys or token secrets.</p>
</li>
<li>
<p><strong>Log authentication failures</strong> - Track failed authentication attempts for security monitoring.</p>
</li>
</ol>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/agents/runtime/communication/routing/"><h3 id="card-routing-agents-runtime-communication-routing">Routing</h3><p>Routing and authentication hooks.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/communication/websockets/"><h3 id="card-websockets-agents-runtime-communication-websockets">WebSockets</h3><p>Real-time bidirectional communication.</p></a></p>
<p><a class="nb-card nb-link-card" href="https://github.com/cloudflare/agents/tree/main/examples/auth-agent"><h3 id="card-github-oauth-agent-example-https-github-com-cloudflare-agents-tree-main-examples-auth-agent">GitHub OAuth agent example</h3><p>Protect an app built with Agents using GitHub OAuth, HTTP-only cookies, and server-owned Durable Object routing.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/agents-api/"><h3 id="card-agents-api-agents-runtime-agents-api">Agents API</h3><p>Complete API reference for the Agents SDK.</p></a></p>
