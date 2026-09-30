<p>Many external services provide libraries and SDKs to interact with their APIs. While many Node-compatible libraries work on Workers right out of the box, some, which implement <code>fs</code>, <code>http/net</code>, or access the browser <code>window</code> do not directly translate to the Workers runtime, which is v8-based.</p>
<h2 id="authentication">Authentication</h2>
<p>If your service requires authentication, use Wrangler secrets to securely store your credentials. To do this, create a secret in your Cloudflare Workers project using the following <a href="/workers/wrangler/commands/general/#secret"><code>wrangler secret</code></a> command:</p>
<pre><code class="language-sh">wrangler secret put SECRET_NAME&#10;</code></pre>
<p>Then, retrieve the secret value in your code using the following code snippet:</p>
<pre><code class="language-js">const secretValue = env.SECRET_NAME;&#10;</code></pre>
<p>Then use the secret value to authenticate with the external service. For example, if the external service requires an API key for authentication, include the secret in your library's configuration.</p>
<p>For services that require mTLS authentication, use <a href="/workers/runtime-apis/bindings/mtls">mTLS certificates</a> to present a client certificate.</p>
<p>Use <a href="/workers/configuration/routing/custom-domains/">Custom Domains</a> when communicating with external APIs, which treat your Worker as your core application.</p>
