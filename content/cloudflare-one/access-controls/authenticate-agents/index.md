<p>Coding agents such as Claude Code, OpenCode, and Windsurf often need to reach resources protected by <a href="/cloudflare-one/access-controls/">Cloudflare Access</a>. When a resource is behind Access, unauthenticated requests receive a redirect or <code>403</code> error instead of the expected response. Your agent needs a way to authenticate before it can reach the resource.</p>
<p>This page covers two authentication methods:</p>
<ul>
<li><a href="#use-cloudflared"><strong>cloudflared</strong></a> — authenticates under your user identity. Use for interactive development where you can complete a browser login.</li>
<li><a href="#use-service-tokens"><strong>Service tokens</strong></a> — authenticates with a static credential pair. Use for headless or automated workflows where no browser is available.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4536.md")
</aside>
<h2 id="use-cloudflared">Use cloudflared</h2>
<p>With <code>cloudflared</code>, your agent authenticates under your user identity. On first use, <code>cloudflared</code> opens a browser window for an interactive login. After that, the session persists for the <a href="/cloudflare-one/access-controls/access-settings/session-management/">session duration</a> configured for the application. After the session expires, the next request requires a new browser login.</p>
<h3 id="prerequisites">Prerequisites</h3>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/">Download and install cloudflared</a>.</p>
<h3 id="make-requests-with-cloudflared-access-curl">Make requests with cloudflared access curl</h3>
<p>For direct requests to a protected resource, use <code>cloudflared access curl</code>. This handles authentication automatically and does not require token management.</p>
<pre><code class="language-sh">cloudflared access curl https://example.com/api/endpoint&#10;</code></pre>
<p>If this is the first request in a session, <code>cloudflared</code> opens a browser for the user to authenticate. Prompt the user to complete the login if needed.</p>
<h3 id="use-a-reusable-token">Use a reusable token</h3>
<p>Some agents make HTTP requests using their own client libraries instead of calling <code>cloudflared</code> directly. In this case, log in to get a token and pass it as a header:</p>
<pre><code class="language-sh">CF_TOKEN=$(cloudflared access login https://example.com)&#10;curl --header &quot;cf-access-token: $CF_TOKEN&quot; https://example.com/api/endpoint&#10;</code></pre>
<p>The token is valid for the session duration configured for the application.</p>
<p>For more information, refer to <a href="/cloudflare-one/tutorials/cli/">Connect through Access using a CLI</a> and <a href="/cloudflare-one/access-controls/applications/non-http/cloudflared-authentication/">Client-side cloudflared</a>.</p>
<h2 id="use-service-tokens">Use service tokens</h2>
<p>Service tokens are static credential pairs that authenticate requests without a browser login. Use them for automated workflows where no user is present.</p>
<ol>
<li>
<p><a href="/cloudflare-one/access-controls/service-credentials/service-tokens/#create-a-service-token">Create a service token</a> and save the <strong>Client ID</strong> and <strong>Client Secret</strong>.</p>
</li>
<li>
<p>In the Access application's policy configuration, add a <a href="/cloudflare-one/access-controls/policies/#service-auth">Service Auth policy</a>. This policy type accepts service token credentials instead of requiring an identity provider login. Use the <strong>Service Token</strong> selector and select the token you created.</p>
</li>
</ol>
<table>
<thead>
<tr>
<th>Action</th>
<th>Rule type</th>
<th>Selector</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Service Auth</td>
<td>Include</td>
<td>Service Token</td>
<td>Your agent token</td>
</tr>
</tbody>
</table>
<ol start="3">
<li>
<p>Store the Client ID and Client Secret in a secure location on your machine that your agent can read.</p>
</li>
<li>
<p>Include both values as headers in requests to the protected resource:</p>
</li>
</ol>
<pre><code class="language-sh">curl --header &quot;CF-Access-Client-Id: $CF_ACCESS_CLIENT_ID&quot; \&#10;     &#45;-header &quot;CF-Access-Client-Secret: $CF_ACCESS_CLIENT_SECRET&quot; \&#10;     https://example.com/api/endpoint&#10;</code></pre>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Service tokens</a>.</p>
<h2 id="configure-your-agent">Configure your agent</h2>
<p>Add an <code>AGENTS.md</code> file to your project root with the following skill definition. This instructs coding agents to automatically detect Cloudflare Access-protected resources and authenticate using the standard OAuth 2.0 flow with PKCE (RFC 9728).</p>
<pre><code class="language-markdown">&#45;--&#10;name: access-oauth&#10;description: &quot;Detect Cloudflare Access-protected websites and authenticate via the standard OAuth 2.0 flow (RFC 9728 resource metadata, dynamic client registration, authorization code + PKCE)&quot;&#10;license: MIT&#10;compatibility: opencode&#10;metadata:&#10;  category: authentication&#10;  audience: developers&#10;&#45;--&#10;&#10;&#35; Access OAuth Authentication&#10;&#10;Authenticate to Cloudflare Access-protected resources using standard OAuth 2.0&#10;(resource metadata discovery, dynamic client registration, authorization code with PKCE).&#10;&#10;&#35;# When to Use&#10;&#10;Use this skill when:&#10;&#10;&#45; You need to access a URL that returns HTTP 401&#10;&#45; The response contains a `www-authenticate: Bearer` header with a `resource_metadata` URL&#10;&#45; The resource metadata indicates it is a Cloudflare Access-protected resource&#10;&#45; You want to authenticate interactively through the user&#x27;s IdP&#10;&#10;&#35;# Step 1: Detect a Protected Resource&#10;&#10;Make a request and inspect the response headers:&#10;</code></pre>
<p>curl -sI -L <URL> 2&gt;&amp;1</p>
<pre><code>&#10;Look for a **401** response with a `www-authenticate` header like:&#10;</code></pre>
<p>www-authenticate: Bearer realm=&quot;OAuth&quot;, error=&quot;invalid_token&quot;,
error_description=&quot;Missing or invalid access token&quot;,
resource_metadata=&quot;https://<hostname>/.well-known/cloudflare-access-protected-resource/&quot;</p>
<pre><code>&#10;If you see this header, the site supports the OAuth flow. Proceed to Step 2.&#10;&#10;The JSON body of the 401 will also contain:&#10;</code></pre>
<p>{
&quot;error&quot;: &quot;invalid_token&quot;,
&quot;error_description&quot;: &quot;Missing or invalid access token&quot;,
&quot;resource_metadata&quot;: &quot;https://<hostname>/.well-known/cloudflare-access-protected-resource/&quot;
}</p>
<pre><code>&#10;&#35;## If No `www-authenticate` Header&#10;&#10;If the 401 does not include `www-authenticate` with `resource_metadata`, the site may&#10;not support this OAuth flow. Fall back to `cloudflared access curl` or browser-based&#10;authentication.&#10;&#10;&#35;# Step 2: Fetch Resource Metadata&#10;&#10;Fetch the resource metadata URL from the `www-authenticate` header:&#10;</code></pre>
<p>curl -s https://<hostname>/.well-known/cloudflare-access-protected-resource/</p>
<pre><code>&#10;Expected response:&#10;</code></pre>
<p>{
&quot;resource&quot;: &quot;https://<hostname>&quot;,
&quot;protected&quot;: true,
&quot;team_domain&quot;: &quot;<team>.cloudflareaccess.com&quot;,
&quot;authorization_servers&quot;: [&quot;https://<team>.cloudflareaccess.com&quot;],
&quot;authentication_method&quot;: &quot;cloudflared&quot;,
&quot;authentication_method_description&quot;: &quot;Use <code>cloudflared access curl</code>...&quot;,
&quot;authentication_method_documentation&quot;: &quot;<a href="https://developers.cloudflare.com/cloudflare-one/tutorials/cli/">https://developers.cloudflare.com/cloudflare-one/tutorials/cli/</a>&quot;
}</p>
<pre><code>&#10;Extract the **authorization server** URL from `authorization_servers[0]` (e.g. `https://&lt;team&gt;.cloudflareaccess.com`).&#10;&#10;&#35;# Step 3: Fetch OAuth Authorization Server Metadata&#10;</code></pre>
<p>curl -s https://<team>.cloudflareaccess.com/.well-known/oauth-authorization-server</p>
<pre><code>&#10;Expected response:&#10;</code></pre>
<p>{
&quot;issuer&quot;: &quot;<team>.cloudflareaccess.com&quot;,
&quot;authorization_endpoint&quot;: &quot;https://<team>.cloudflareaccess.com/cdn-cgi/access/oauth/authorization&quot;,
&quot;token_endpoint&quot;: &quot;https://<team>.cloudflareaccess.com/cdn-cgi/access/oauth/token&quot;,
&quot;response_types_supported&quot;: [&quot;code&quot;],
&quot;response_modes_supported&quot;: [&quot;query&quot;],
&quot;grant_types_supported&quot;: [&quot;authorization_code&quot;, &quot;refresh_token&quot;],
&quot;token_endpoint_auth_methods_supported&quot;: [
&quot;client_secret_basic&quot;,
&quot;client_secret_post&quot;,
&quot;none&quot;
],
&quot;revocation_endpoint&quot;: &quot;https://<team>.cloudflareaccess.com/cdn-cgi/access/oauth/revoke&quot;,
&quot;registration_endpoint&quot;: &quot;https://<team>.cloudflareaccess.com/cdn-cgi/access/oauth/registration&quot;,
&quot;code_challenge_methods_supported&quot;: [&quot;S256&quot;]
}</p>
<pre><code>&#10;Verify that:&#10;&#10;&#45; `&quot;none&quot;` is in `token_endpoint_auth_methods_supported` (allows public clients)&#10;&#45; `&quot;authorization_code&quot;` is in `grant_types_supported`&#10;&#45; `&quot;S256&quot;` is in `code_challenge_methods_supported`&#10;&#45; A `registration_endpoint` is present&#10;&#10;Extract the **registration_endpoint**, **authorization_endpoint**, and **token_endpoint**.&#10;&#10;&#35;# Step 4: Dynamic Client Registration&#10;&#10;Register a public OAuth client:&#10;</code></pre>
<p>curl -s -X POST &lt;registration_endpoint&gt; <br />
-H &quot;Content-Type: application/json&quot; <br />
-d '{
&quot;redirect_uris&quot;: [&quot;http://localhost:8400/callback&quot;],
&quot;token_endpoint_auth_method&quot;: &quot;none&quot;,
&quot;grant_types&quot;: [&quot;authorization_code&quot;],
&quot;response_types&quot;: [&quot;code&quot;],
&quot;resource&quot;: &quot;https://<hostname>&quot;
}'</p>
<pre><code>&#10;Expected response:&#10;</code></pre>
<p>{
&quot;client_id&quot;: &quot;<uuid>&quot;,
&quot;redirect_uris&quot;: [&quot;http://localhost:8400/callback&quot;],
&quot;grant_types&quot;: [&quot;authorization_code&quot;],
&quot;response_types&quot;: [&quot;code&quot;],
&quot;token_endpoint_auth_method&quot;: &quot;none&quot;,
&quot;registration_client_uri&quot;: &quot;...&quot;,
&quot;client_id_issued_at&quot;: 1234567890
}</p>
<pre><code>&#10;Save the **client_id**.&#10;&#10;&#35;# Step 5: Generate PKCE Challenge&#10;&#10;Generate a code verifier and S256 challenge. Ensure the challenge starts with an&#10;alphanumeric character to avoid URL parsing issues:&#10;</code></pre>
<p>while true; do
CODE_VERIFIER=$(openssl rand -base64 32 | tr -d '=' | tr '/+' '<em>-')
CODE_CHALLENGE=$(printf '%s' &quot;$CODE_VERIFIER&quot; | openssl dgst -sha256 -binary | base64 | tr -d '=' | tr '/+' '</em>-')
if [[ &quot;$CODE_CHALLENGE&quot; =~ ^[a-zA-Z0-9] ]]; then
break
fi
done</p>
<pre><code>&#10;&#42;*Important**: The code challenge MUST start with `[a-zA-Z0-9]`. A leading `-` or `_`&#10;can cause URL parameter parsing failures on the authorization server.&#10;&#10;&#35;# Step 6: Authorization Code Flow with Local Callback&#10;&#10;Start a local HTTP server to catch the callback, then direct the user to the&#10;authorization URL.&#10;&#10;&#35;## Build the Authorization URL&#10;</code></pre>
<p>&lt;authorization_endpoint&gt;?
client_id=&lt;client_id&gt;&amp;
redirect_uri=http%3A%2F%2Flocalhost%3A8400%2Fcallback&amp;
response_type=code&amp;
code_challenge=&lt;CODE_CHALLENGE&gt;&amp;
code_challenge_method=S256&amp;
resource=<URL-encoded target resource></p>
<pre><code>&#10;&#35;## Start the Callback Listener and Prompt the User&#10;&#10;Run a Python HTTP server on port 8400 that captures the authorization code:&#10;</code></pre>
<p>python3 -c '</p>
<p>class Handler(http.server.BaseHTTPRequestHandler):
def do_GET(self):
parsed = urllib.parse.urlparse(self.path)
params = urllib.parse.parse_qs(parsed.query)
if &quot;code&quot; in params:
code = params[&quot;code&quot;][0]
with open(&quot;/tmp/oauth_code.txt&quot;, &quot;w&quot;) as f:
f.write(code)
self.send_response(200)
self.send_header(&quot;Content-Type&quot;, &quot;text/html&quot;)
self.end_headers()
self.wfile.write(b&quot;<h2 id="got-it">Got it!</h2><p>Authorization code received. You can close this tab.</p>&quot;)
print(f&quot;CODE={code}&quot;, flush=True)
elif &quot;error&quot; in params:
err = params.get(&quot;error&quot;, [&quot;&quot;])[0]
desc = params.get(&quot;error_description&quot;, [&quot;&quot;])[0]
self.send_response(200)
self.send_header(&quot;Content-Type&quot;, &quot;text/html&quot;)
self.end_headers()
self.wfile.write(f&quot;<h2 id="error">Error</h2><p>{err}: {desc}</p>&quot;.encode())
print(f&quot;ERROR: {err} - {desc}&quot;, flush=True)
else:
self.send_response(400)
self.end_headers()
self.wfile.write(b&quot;Unexpected request&quot;)
print(f&quot;Unexpected: {self.path}&quot;, flush=True)</p>
<pre><code>    threading.Thread(target=self.server.shutdown).start()&#10;def log_message(self, format, *args):&#10;    pass&#10;</code></pre>
<p>print(&quot;Listening on <a href="http://localhost:8400">http://localhost:8400</a> ...&quot;, flush=True)
print(&quot;Open the authorization URL in your browser.&quot;, flush=True)
http.server.HTTPServer((&quot;&quot;, 8400), Handler).serve_forever()
'</p>
<pre><code>&#10;&#42;*Important**: Use a timeout of at least 120000ms for this bash command since the user&#10;needs time to authenticate in the browser.&#10;&#10;Tell the user to open the authorization URL in their browser. After they authenticate&#10;with their IdP, the browser will redirect to `http://localhost:8400/callback?code=&lt;code&gt;`,&#10;the server will capture it and shut down.&#10;&#10;&#35;# Step 7: Exchange Code for Token&#10;</code></pre>
<p>curl -s -X POST &lt;token_endpoint&gt; <br />
-H &quot;Content-Type: application/x-www-form-urlencoded&quot; <br />
-d &quot;grant_type=authorization_code&quot; <br />
-d &quot;code=&lt;AUTH_CODE&gt;&quot; <br />
-d &quot;client_id=&lt;CLIENT_ID&gt;&quot; <br />
-d &quot;redirect_uri=<a href="http://localhost:8400/callback">http://localhost:8400/callback</a>&quot; <br />
-d &quot;code_verifier=&lt;CODE_VERIFIER&gt;&quot;</p>
<pre><code>&#10;Expected response:&#10;</code></pre>
<p>{
&quot;access_token&quot;: &quot;oauth:<token>&quot;,
&quot;token_type&quot;: &quot;bearer&quot;,
&quot;expires_in&quot;: 900,
&quot;scope&quot;: &quot;&quot;,
&quot;resource&quot;: &quot;https://<hostname>/&quot;,
&quot;refresh_token&quot;: &quot;oauth:&lt;refresh_token&gt;&quot;
}</p>
<pre><code>&#10;Save the **access_token** and **refresh_token**.&#10;&#10;&#35;# Step 8: Access the Protected Resource&#10;</code></pre>
<p>curl -s https://<hostname>/ <br />
-H &quot;Authorization: Bearer &lt;access_token&gt;&quot;</p>
<pre><code>&#10;This should now return the actual content behind Cloudflare Access.&#10;&#10;&#35;# Step 9: Refresh the Token (if needed)&#10;&#10;If the access token expires (default 900 seconds), use the refresh token:&#10;</code></pre>
<p>curl -s -X POST &lt;token_endpoint&gt; <br />
-H &quot;Content-Type: application/x-www-form-urlencoded&quot; <br />
-d &quot;grant_type=refresh_token&quot; <br />
-d &quot;refresh_token=&lt;REFRESH_TOKEN&gt;&quot; <br />
-d &quot;client_id=&lt;CLIENT_ID&gt;&quot;</p>
<pre><code>&#10;&#35;# Quick Reference: Full Flow Summary&#10;</code></pre>
<ol>
<li>curl -sI <URL>                          # Detect 401 + www-authenticate header</li>
<li>curl -s &lt;resource_metadata_url&gt;         # Get authorization server</li>
<li>curl -s <as>/.well-known/oauth-authorization-server  # Get endpoints</li>
<li>POST &lt;registration_endpoint&gt;            # Register public client</li>
<li>Generate PKCE code_verifier + challenge # S256, alphanumeric start</li>
<li>Start localhost:8400 listener           # Catch callback</li>
<li>User opens authorization URL            # Browser-based IdP auth</li>
<li>POST &lt;token_endpoint&gt;                   # Exchange code for token</li>
<li>curl -H &quot;Authorization: Bearer <token>&quot; # Access resource</li>
</ol>
<pre><code>&#10;&#35;# Troubleshooting&#10;&#10;<table>&#10;&#10;<thead>&#10;<tr>&#10;<th>Problem</th>&#10;<th>Cause</th>&#10;<th>Fix</th>&#10;</tr>&#10;</thead>&#10;<tbody>&#10;<tr>&#10;<td><code>code_challenge_method must be S256 for public clients</code></td>&#10;<td>Code challenge starts with <code>-</code> or <code>_</code>, corrupting the URL parameter</td>&#10;<td>Regenerate until challenge starts with <code>[a-zA-Z0-9]</code></td>&#10;</tr>&#10;<tr>&#10;<td><code>invalid_grant</code> on token exchange</td>&#10;<td>Code expired or verifier mismatch</td>&#10;<td>Redo the auth flow; codes are single-use and short-lived</td>&#10;</tr>&#10;<tr>&#10;<td>401 after using token</td>&#10;<td>Token expired (default 15 min)</td>&#10;<td>Use refresh token to get a new access token</td>&#10;</tr>&#10;<tr>&#10;<td>No <code>www-authenticate</code> header</td>&#10;<td>Site doesn't support OAuth resource metadata</td>&#10;<td>Fall back to <code>cloudflared access curl</code> or browser auth</td>&#10;</tr>&#10;<tr>&#10;<td>No <code>registration_endpoint</code> in AS metadata</td>&#10;<td>Dynamic registration not enabled</td>&#10;<td>Must use a pre-registered client or different auth method</td>&#10;</tr>&#10;<tr>&#10;<td>Port 8400 already in use</td>&#10;<td>Previous listener didn't shut down</td>&#10;<td>Kill the process or use a different port (update redirect_uri accordingly)</td>&#10;</tr>&#10;</tbody>&#10;&#10;</table>&#10;</code></pre>
