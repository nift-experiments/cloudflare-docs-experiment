<p>The Sandbox SDK is built on <a href="/containers/">Containers</a>, which run each sandbox in its own VM for strong isolation.</p>
<h2 id="container-isolation">Container isolation</h2>
<p>Each sandbox runs in a separate VM, providing complete isolation:</p>
<ul>
<li><strong>Filesystem isolation</strong> - Sandboxes cannot access other sandboxes' files</li>
<li><strong>Process isolation</strong> - Processes in one sandbox cannot see or affect others</li>
<li><strong>Network isolation</strong> - Sandboxes have separate network stacks</li>
<li><strong>Resource limits</strong> - CPU, memory, and disk quotas are enforced per sandbox</li>
</ul>
<p>For complete security details about the underlying container platform, see <a href="/containers/concepts/architecture/">Containers architecture</a>.</p>
<h2 id="within-a-sandbox">Within a sandbox</h2>
<p>All code within a single sandbox shares resources:</p>
<ul>
<li><strong>Filesystem</strong> - All processes see the same files</li>
<li><strong>Processes</strong> - All sessions can see all processes</li>
<li><strong>Network</strong> - Processes can communicate via localhost</li>
</ul>
<p>For complete isolation, use separate sandboxes per user:</p>
<pre><code class="language-typescript">// Good - Each user in separate sandbox&#10;const userSandbox = getSandbox(env.Sandbox, `user-${userId}`);&#10;&#10;// Bad - Users sharing one sandbox&#10;const shared = getSandbox(env.Sandbox, &#x27;shared&#x27;);&#10;// Users can read each other&#x27;s files!&#10;</code></pre>
<h2 id="input-validation">Input validation</h2>
<h3 id="command-injection">Command injection</h3>
<p>Always validate user input before using it in commands:</p>
<pre><code class="language-typescript">// Dangerous - user input directly in command&#10;const filename = userInput;&#10;await sandbox.exec(`cat ${filename}`);&#10;// User could input: &quot;file.txt; rm -rf /&quot;&#10;&#10;// Safe - validate input&#10;const filename = userInput.replace(/[^a-zA-Z0-9._-]/g, &#x27;&#x27;);&#10;await sandbox.exec(`cat ${filename}`);&#10;&#10;// Better - use file API&#10;await sandbox.writeFile(&#x27;/tmp/input&#x27;, userInput);&#10;await sandbox.exec(&#x27;cat /tmp/input&#x27;);&#10;</code></pre>
<h2 id="authentication">Authentication</h2>
<h3 id="sandbox-access">Sandbox access</h3>
<p>Sandbox IDs provide basic access control but aren't cryptographically secure. Add application-level authentication:</p>
<pre><code class="language-typescript">export default {&#10;  async fetch(request: Request, env: Env): Promise&lt;Response&gt; {&#10;    const userId = await authenticate(request);&#10;    if (!userId) {&#10;      return new Response(&#x27;Unauthorized&#x27;, { status: 401 });&#10;    }&#10;&#10;    // User can only access their sandbox&#10;    const sandbox = getSandbox(env.Sandbox, userId);&#10;    return Response.json({ authorized: true });&#10;  }&#10;};&#10;</code></pre>
<h3 id="preview-urls">Preview URLs</h3>
<p>Preview URLs include randomly generated tokens. Anyone with the URL can access the service.</p>
<p>To revoke access, unexpose the port:</p>
<pre><code class="language-typescript">await sandbox.unexposePort(8080);&#10;</code></pre>
<h3 id="quick-tunnel-urls">Quick tunnel URLs</h3>
<p>Quick tunnels (<code>sandbox.tunnels.get(port)</code>) return a <code>*.trycloudflare.com</code> URL with a random hostname assigned by Cloudflare — there is no separate access token. The hostname itself is the access control: anyone who knows the URL can reach the service. To revoke access, destroy the tunnel:</p>
<pre><code class="language-typescript">await sandbox.tunnels.destroy(8080);&#10;</code></pre>
<p>URLs do not survive a container restart, so a restart effectively rotates the hostname. As with preview URLs, add application-level authentication for any sensitive service. See the <a href="/sandbox/api/tunnels/">Tunnels API</a> for details.</p>
<pre><code class="language-python">from flask import Flask, request, abort&#10;import os&#10;&#10;app = Flask(__name__)&#10;&#10;def check_auth():&#10;    token = request.headers.get(&#x27;Authorization&#x27;)&#10;    if token != f&quot;Bearer {os.environ[&#x27;AUTH_TOKEN&#x27;]}&quot;:&#10;        abort(401)&#10;&#10;@app.route(&#x27;/api/data&#x27;)&#10;def get_data():&#10;    check_auth()&#10;    return {&#x27;data&#x27;: &#x27;protected&#x27;}&#10;</code></pre>
<h2 id="secrets-management">Secrets management</h2>
<p>Use environment variables, not hardcoded secrets, for values the sandbox process must consume directly:</p>
<pre><code class="language-typescript">// Bad - hardcoded in file&#10;await sandbox.writeFile(&#x27;/workspace/config.js&#x27;, `&#10;  const API_KEY = &#x27;sk_live_abc123&#x27;;&#10;`);&#10;&#10;// Good - use environment variables for values the sandbox process needs&#10;await sandbox.startProcess(&#x27;node app.js&#x27;, {&#10;  env: {&#10;    API_KEY: env.API_KEY,  // From Worker environment binding&#10;  }&#10;});&#10;</code></pre>
<p>For external API credentials that the sandbox does not need to read directly, keep the credential in the Worker and inject it with an outbound handler.</p>
<p>Clean up temporary sensitive data:</p>
<pre><code class="language-typescript">try {&#10;  await sandbox.writeFile(&#x27;/tmp/sensitive.txt&#x27;, secretData);&#10;  await sandbox.exec(&#x27;python process.py /tmp/sensitive.txt&#x27;);&#10;} finally {&#10;  await sandbox.deleteFile(&#x27;/tmp/sensitive.txt&#x27;);&#10;}&#10;</code></pre>
<h2 id="handle-outbound-traffic">Handle outbound traffic</h2>
<p>Passing external API credentials directly to a sandbox — via environment variables or files — means the sandbox process holds a live credential that any code running inside it can read. Outbound handlers remove that exposure by keeping credentials in the Worker and injecting them into outbound requests.</p>
<p>The flow works as follows:</p>
<pre><code class="language-txt">Sandbox request → Outbound handler (injects real credentials) → External API&#10;</code></pre>
<p>The sandbox never sees the real credential. Rotate the secret in your Worker's environment and every request uses the updated value.</p>
<p>This pattern is useful when accessing GitHub for private repository operations, AI services, or object storage where you want to keep credentials out of the container entirely. For implementation details, refer to <a href="/sandbox/guides/outbound-traffic/">Handle outbound traffic</a>.</p>
<h2 id="what-the-sdk-protects-against">What the SDK protects against</h2>
<ul>
<li>Sandbox-to-sandbox access (VM isolation)</li>
<li>Resource exhaustion (enforced quotas)</li>
<li>Container escapes (VM-based isolation)</li>
</ul>
<h2 id="what-you-must-implement">What you must implement</h2>
<ul>
<li>Authentication and authorization</li>
<li>Input validation and sanitization</li>
<li>Rate limiting</li>
<li>Application-level security (SQL injection, XSS, etc.)</li>
</ul>
<h2 id="best-practices">Best practices</h2>
<p><strong>Use separate sandboxes for isolation</strong>:</p>
<pre><code class="language-typescript">const sandbox = getSandbox(env.Sandbox, `user-${userId}`);&#10;</code></pre>
<p><strong>Validate all inputs</strong>:</p>
<pre><code class="language-typescript">const safe = input.replace(/[^a-zA-Z0-9._-]/g, &#x27;&#x27;);&#10;await sandbox.exec(`command ${safe}`);&#10;</code></pre>
<p><strong>Use environment variables for secrets</strong>:</p>
<pre><code class="language-typescript">await sandbox.startProcess(&#x27;node app.js&#x27;, {&#10;  env: { API_KEY: env.API_KEY }&#10;});&#10;</code></pre>
<p><strong>Clean up temporary resources</strong>:</p>
<pre><code class="language-typescript">try {&#10;  const sandbox = getSandbox(env.Sandbox, sessionId);&#10;  await sandbox.exec(&#x27;npm test&#x27;);&#10;} finally {&#10;  await sandbox.destroy();&#10;}&#10;</code></pre>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/containers/concepts/architecture/">Containers architecture</a> - Underlying platform security</li>
<li><a href="/sandbox/concepts/sandboxes/">Sandbox lifecycle</a> - Resource management</li>
</ul>
