<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 19, 2026</time><h2 id="post-title">Hyperdrive now supports custom TLS/SSL certificates for MySQL</h2>
<div class="changelog-badges"><span>hyperdrive</span></div><div class="changelog-body"><p>Hyperdrive now supports custom TLS/SSL certificates for MySQL databases, bringing the same certificate options previously available for PostgreSQL to MySQL connections.</p>
<p>You can now configure:</p>
<ul>
<li><strong>Server certificate verification</strong> with <code>VERIFY_CA</code> or <code>VERIFY_IDENTITY</code> SSL modes to verify that your MySQL database server's certificate is signed by the expected certificate authority (CA).</li>
<li><strong>Client certificates</strong> (mTLS) for Hyperdrive to authenticate itself to your MySQL database with credentials beyond username and password.</li>
</ul>
<p>Create a Hyperdrive configuration with custom certificates for MySQL:</p>
<pre><code class="language-bash">&#35; Upload a CA certificate&#10;npx wrangler cert upload certificate-authority --ca-cert your-ca-cert.pem --name your-custom-ca-name&#10;&#10;&#35; Create a Hyperdrive with VERIFY_IDENTITY mode&#10;npx wrangler hyperdrive create your-hyperdrive-config \&#10;  &#45;-connection-string=&quot;mysql://user:password@hostname:port/database&quot; \&#10;  &#45;-ca-certificate-id &lt;CA_CERT_ID&gt; \&#10;  &#45;-sslmode VERIFY_IDENTITY&#10;</code></pre>
<p>For more information, refer to <a href="/hyperdrive/configuration/tls-ssl-certificates-for-hyperdrive/">SSL/TLS certificates for Hyperdrive</a> and <a href="/hyperdrive/examples/connect-to-mysql/">MySQL TLS/SSL modes</a>.</p>
</div></article></div>
