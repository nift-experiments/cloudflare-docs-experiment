<p>MCP servers, like any web application, need to be secured so they can be used by trusted users without abuse. The MCP specification uses OAuth 2.1 for authentication between MCP clients and servers.</p>
<p>This guide covers security best practices for MCP servers that act as OAuth proxies to third-party providers (like GitHub or Google).</p>
<h2 id="oauth-protection-with-workers-oauth-provider">OAuth protection with workers-oauth-provider</h2>
<p>Cloudflare's <a href="https://github.com/cloudflare/workers-oauth-provider"><code>workers-oauth-provider</code></a> handles token management, client registration, and access token validation:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2206.md")
</div>
<h2 id="consent-dialog-security">Consent dialog security</h2>
<p>When your MCP server proxies to third-party OAuth providers, you must implement your own consent dialog before forwarding users upstream. This prevents the &quot;confused deputy&quot; problem where attackers could exploit cached consent.</p>
<h3 id="csrf-protection">CSRF protection</h3>
<p>Without CSRF protection, attackers can trick users into approving malicious OAuth clients. Use a random token stored in a secure cookie:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2207.md")
</div>
<p>Include the token as a hidden field in your consent form:</p>
<pre><code class="language-html">&lt;input type=&quot;hidden&quot; name=&quot;csrf_token&quot; value=&quot;${csrfToken}&quot; /&gt;&#10;</code></pre>
<h3 id="input-sanitization">Input sanitization</h3>
<p>User-controlled content (client names, logos, URIs) can execute malicious scripts if not sanitized:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2208.md")
</div>
<h3 id="content-security-policy">Content Security Policy</h3>
<p>CSP headers instruct browsers to block dangerous content:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2209.md")
</div>
<h2 id="state-handling">State handling</h2>
<p>Between the consent dialog and the OAuth callback, you need to ensure it is the same user. Use a state token stored in KV with a short expiration:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2210.md")
</div>
<h2 id="cookie-security">Cookie security</h2>
<h3 id="why-use-the-host-prefix">Why use the <code>__Host-</code> prefix?</h3>
<p>The <code>__Host-</code> prefix prevents subdomain attacks, which is especially important on <code>*.workers.dev</code> domains:</p>
<ul>
<li>Must be set with <code>Secure</code> flag (HTTPS only)</li>
<li>Must have <code>Path=/</code></li>
<li>Must not have a <code>Domain</code> attribute</li>
</ul>
<p>Without <code>__Host-</code>, an attacker controlling <code>evil.workers.dev</code> could set cookies for your <code>mcp-server.workers.dev</code> domain.</p>
<h3 id="multiple-oauth-flows">Multiple OAuth flows</h3>
<p>If running multiple OAuth flows on the same domain, namespace your cookies:</p>
<pre><code class="language-txt">__Host-CSRF_TOKEN_GITHUB&#10;__Host-CSRF_TOKEN_GOOGLE&#10;__Host-APPROVED_CLIENTS_GITHUB&#10;__Host-APPROVED_CLIENTS_GOOGLE&#10;</code></pre>
<h2 id="approved-clients-registry">Approved clients registry</h2>
<p>Maintain a registry of approved client IDs per user to avoid showing the consent dialog repeatedly:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2211.md")
</div>
<p>When reading the cookie, verify the HMAC signature before trusting the data. If the client is not in the approved list, show the consent dialog.</p>
<h2 id="security-checklist">Security checklist</h2>
<table>
<thead>
<tr>
<th>Protection</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>CSRF tokens</td>
<td>Prevent forged consent approvals</td>
</tr>
<tr>
<td>Input sanitization</td>
<td>Prevent XSS in consent dialogs</td>
</tr>
<tr>
<td>CSP headers</td>
<td>Block injected scripts</td>
</tr>
<tr>
<td>State binding</td>
<td>Prevent session fixation</td>
</tr>
<tr>
<td><code>__Host-</code> cookies</td>
<td>Prevent subdomain attacks</td>
</tr>
<tr>
<td>HMAC signatures</td>
<td>Verify cookie integrity</td>
</tr>
</tbody>
</table>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/agents/model-context-protocol/protocol/authorization/"><h3 id="card-mcp-authorization-agents-model-context-protocol-protocol-authorization">MCP authorization</h3><p>OAuth and authentication for MCP servers.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/model-context-protocol/guides/remote-mcp-server/"><h3 id="card-build-a-remote-mcp-server-agents-model-context-protocol-guides-remote-mcp-server">Build a remote MCP server</h3><p>Deploy MCP servers on Cloudflare.</p></a></p>
<p><a class="nb-card nb-link-card" href="https://modelcontextprotocol.io/specification/draft/basic/security_best_practices"><h3 id="card-mcp-security-best-practices-https-modelcontextprotocol-io-specification-draft-basic-security-best-practices">MCP security best practices</h3><p>Official MCP specification security guide.</p></a></p>
