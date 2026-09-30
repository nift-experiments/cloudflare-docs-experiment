<p>When using <a href="https://www.cloudflare.com/learning/ssl/what-is-https/">HTTPS</a>, a server presents a certificate for the client to authenticate in order to prove their identity. For even tighter security, some services require that the client also present a certificate.</p>
<p>This process - known as <a href="https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/">mTLS</a> - moves authentication to the protocol of TLS, rather than managing it in application code. Connections from unauthorized clients are rejected during the TLS handshake instead.</p>
<p>To present a client certificate when communicating with a service, create a mTLS certificate <a href="/workers/runtime-apis/bindings/">binding</a> in your Worker project's Wrangler file. This will allow your Worker to present a client certificate to a service on your behalf.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17197.md")
</aside>
<p>First, upload a certificate and its private key to your account using the <a href="/workers/wrangler/commands/certificates/#mtls-certificate"><code>wrangler mtls-certificate</code></a> command:</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17196.md")
</aside>
<pre><code class="language-sh">npx wrangler mtls-certificate upload --cert cert.pem --key key.pem --name my-client-cert&#10;</code></pre>
<p>Then, update your Worker project's Wrangler file to create an mTLS certificate binding:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17198.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17195.md")
</aside>
<p>Adding an mTLS certificate binding includes a variable in the Worker's environment on which the <code>fetch()</code> method is available. This <code>fetch()</code> method uses the standard <a href="/workers/runtime-apis/fetch/">Fetch</a> API and has the exact same signature as the global <code>fetch</code>, but always presents the client certificate when establishing the TLS connection.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17194.md")
</aside>
<h3 id="interface">Interface</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17201.md")
</div></div>
