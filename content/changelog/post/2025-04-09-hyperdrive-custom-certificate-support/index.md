<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 9, 2025</time><h2 id="post-title">Hyperdrive now supports custom TLS/SSL certificates</h2>
<div class="changelog-badges"><span>hyperdrive</span></div><div class="changelog-body"><p>Hyperdrive now supports more SSL/TLS security options for your database connections:</p>
<ul>
<li>Configure Hyperdrive to verify server certificates with <code>verify-ca</code> or <code>verify-full</code> SSL modes and protect against man-in-the-middle attacks</li>
<li>Configure Hyperdrive to provide client certificates to the database server to authenticate itself (mTLS) for stronger security beyond username and password</li>
</ul>
<p>Use the new <code>wrangler cert</code> commands to create certificate authority (CA) certificate bundles or client certificate pairs:</p>
<pre><code class="language-bash">&#35; Create CA certificate bundle&#10;npx wrangler cert upload certificate-authority --ca-cert your-ca-cert.pem --name your-custom-ca-name&#10;&#10;&#35; Create client certificate pair&#10;npx wrangler cert upload mtls-certificate --cert client-cert.pem --key client-key.pem --name your-client-cert-name&#10;</code></pre>
<p>Then create a Hyperdrive configuration with the certificates and desired SSL mode:</p>
<pre><code class="language-bash">npx wrangler hyperdrive create your-hyperdrive-config \&#10;  &#45;-connection-string=&quot;postgres://user:password@hostname:port/database&quot; \&#10;  &#45;-ca-certificate-id &lt;CA_CERT_ID&gt; \&#10;  &#45;-mtls-certificate-id &lt;CLIENT_CERT_ID&gt;&#10;  &#45;-sslmode verify-full&#10;</code></pre>
<p>Learn more about <a href="/hyperdrive/configuration/tls-ssl-certificates-for-hyperdrive/">configuring SSL/TLS certificates for Hyperdrive</a> to enhance your database security posture.</p>
</div></article></div>
