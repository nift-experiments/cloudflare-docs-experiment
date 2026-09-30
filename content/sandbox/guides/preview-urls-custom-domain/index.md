<p>Set up wildcard DNS, routes, and TLS so <code>exposePort()</code> preview URLs work on your domain. To deploy the Worker and sandbox image, refer to <a href="/sandbox/guides/deploy/">Deploy a Sandbox application</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="only-required-for-preview-urls">Only required for preview URLs</h3>
@markup("md", "content/.markup/bodies/13361.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="sandbox-sdk-1-0-preview">Sandbox SDK 1.0 preview</h3>
@markup("md", "content/.markup/bodies/13360.md")
</aside>
<p>Preview URLs need wildcard DNS because each exposed port gets a unique subdomain: <code>https://8080-abc123.yourdomain.com</code>.</p>
<p>The <code>.workers.dev</code> domain does not support wildcard subdomains, so preview URLs that must be reachable on a public hostname outside local development need a custom domain.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="subdomain-depth-matters-for-tls">Subdomain depth matters for TLS</h3>
@markup("md", "content/.markup/bodies/13359.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Active Cloudflare zone with a domain</li>
<li>Worker that uses <code>exposePort()</code></li>
<li><a href="/workers/wrangler/install-and-update/">Wrangler CLI</a> installed</li>
<li>Sandbox app already <a href="/sandbox/guides/deploy/">deployable</a> (Worker + image)</li>
</ul>
<h2 id="setup">Setup</h2>
<h3 id="create-a-wildcard-dns-record">Create a wildcard DNS record</h3>
<p>In the Cloudflare dashboard, go to your domain and create an A record:</p>
<ul>
<li><strong>Type</strong>: A</li>
<li><strong>Name</strong>: <code>*</code> (wildcard)</li>
<li><strong>IPv4 address</strong>: <code>192.0.2.0</code></li>
<li><strong>Proxy status</strong>: Proxied (orange cloud)</li>
</ul>
<p>This routes all subdomains through Cloudflare's proxy. The IP address <code>192.0.2.0</code> is a documentation address (RFC 5737) that Cloudflare recognizes when proxied.</p>
<h3 id="configure-worker-routes">Configure Worker routes</h3>
<p>Add a wildcard route to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13362.md")
</div>
<p>Replace <code>yourdomain.com</code> with your actual domain. This routes all subdomain requests to your Worker and enables Cloudflare to provision SSL certificates automatically.</p>
<h3 id="apply-the-route">Apply the route</h3>
<p>Redeploy the Worker so the route configuration takes effect:</p>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>If this deploy also changes your sandbox image or package, follow <a href="/sandbox/guides/deploy/">Deploy a Sandbox application</a> for rollout and package/image pairing. For route-only changes you can still use a normal deploy. Use <code>--containers-rollout=none</code> only when you intentionally skip container image and instance updates.</p>
<h2 id="verify">Verify</h2>
<p>Test that preview URLs work:</p>
<pre><code class="language-typescript">// Extract hostname from request&#10;const { hostname } = new URL(request.url);&#10;&#10;const sandbox = getSandbox(env.Sandbox, &quot;test-sandbox&quot;);&#10;await sandbox.startProcess(&quot;python -m http.server 8080&quot;);&#10;const exposed = await sandbox.exposePort(8080, { hostname });&#10;&#10;console.log(exposed.url);&#10;// https://8080-test-sandbox.yourdomain.com&#10;</code></pre>
<p>Visit the URL in your browser to confirm your service is accessible.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<ul>
<li><strong>CustomDomainRequiredError</strong>: Verify your Worker is not deployed only to <code>.workers.dev</code> and that the wildcard DNS record and route are configured correctly.</li>
<li><strong>SSL/TLS errors</strong>: Wait a few minutes for certificate provisioning. Verify the DNS record is proxied and SSL/TLS mode is set to &quot;Full&quot; or &quot;Full (strict)&quot; in your dashboard. If your Worker is on a subdomain (for example, <code>sandbox.yourdomain.com</code>), Universal SSL will not cover the second-level wildcard <code>*.sandbox.yourdomain.com</code>. Refer to the <a href="#subdomain-depth-matters-for-tls">TLS caution</a> at the top of this page for options.</li>
<li><strong>Preview URL not resolving</strong>: Confirm the wildcard DNS record exists and is proxied. Wait 30–60 seconds for DNS propagation.</li>
<li><strong>Port not accessible</strong>: Ensure your service binds to <code>0.0.0.0</code> (not <code>localhost</code>) and that <code>proxyToSandbox()</code> is called first in your Worker's fetch handler.</li>
</ul>
<p>For detailed troubleshooting, see the <a href="/workers/configuration/routing/">Workers routing documentation</a>.</p>
<h2 id="related">Related</h2>
<ul>
<li><a href="/sandbox/guides/deploy/">Deploy a Sandbox application</a> - Deploy Worker and image</li>
<li><a href="/sandbox/concepts/preview-urls/">Preview URLs</a> - How preview URLs work</li>
<li><a href="/sandbox/guides/expose-services/">Expose services</a> - Patterns for exposing ports</li>
<li><a href="/sandbox/api/tunnels/">Tunnels API</a> - Zero-config <code>*.trycloudflare.com</code> URLs for development</li>
<li><a href="/workers/configuration/routing/">Workers routing</a> - Advanced routing configuration</li>
<li><a href="/dns/">Cloudflare DNS</a> - DNS management</li>
</ul>
