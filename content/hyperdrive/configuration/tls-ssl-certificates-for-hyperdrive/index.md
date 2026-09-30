<p>Hyperdrive provides additional ways to secure connectivity to your database. Hyperdrive supports:</p>
<ol>
<li><strong>Server certificates</strong> for TLS (SSL) modes such as <code>verify-ca</code>/<code>VERIFY_CA</code> and <code>verify-full</code>/<code>VERIFY_IDENTITY</code> for increased security. When configured, Hyperdrive will verify that the certificates have been signed by the expected certificate authority (CA) to avoid man-in-the-middle attacks.</li>
<li><strong>Client certificates</strong> for Hyperdrive to authenticate itself to your database with credentials beyond username/password. To properly use client certificates, your database must be configured to verify the client certificates provided by a client, such as Hyperdrive, to allow access to the database.</li>
</ol>
<p>Hyperdrive can be configured to use only server certificates, only client certificates, or both depending on your security requirements and database configurations.</p>
<h2 id="server-certificates-tls-ssl-modes">Server certificates (TLS/SSL modes)</h2>
<p>Hyperdrive supports common encryption TLS/SSL modes to connect to your database. The mode names differ between PostgreSQL and MySQL:</p>
<table>
<thead>
<tr>
<th>PostgreSQL</th>
<th>MySQL</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>require</code> (default)</td>
<td><code>REQUIRED</code> (default)</td>
<td>TLS is required for encrypted connectivity and server certificates are validated (based on WebPKI).</td>
</tr>
<tr>
<td><code>verify-ca</code></td>
<td><code>VERIFY_CA</code></td>
<td>Hyperdrive will verify that the database server is trustworthy by verifying that the certificates of the server have been signed by the expected root certificate authority or intermediate certificate authority.</td>
</tr>
<tr>
<td><code>verify-full</code></td>
<td><code>VERIFY_IDENTITY</code></td>
<td>In addition to <code>verify-ca</code>/<code>VERIFY_CA</code> checks, Hyperdrive requires the database hostname to match a Subject Alternative Name (SAN) or Common Name (CN) on the certificate.</td>
</tr>
</tbody>
</table>
<p>By default, all Hyperdrive configurations are encrypted with SSL/TLS (<code>require</code>/<code>REQUIRED</code>). This requires your database to be configured to accept encrypted connections (with SSL/TLS).</p>
<p>You can configure Hyperdrive to use <code>verify-ca</code>/<code>VERIFY_CA</code> and <code>verify-full</code>/<code>VERIFY_IDENTITY</code> for a more stringent security configuration, which provide additional verification checks of the server's certificates. This helps guard against man-in-the-middle attacks.</p>
<p>To configure Hyperdrive to verify the certificates of the server, you must provide Hyperdrive with the certificate of the root certificate authority (CA) or an intermediate certificate which has been used to sign the certificate of your database.</p>
<h3 id="step-1-upload-the-root-certificate-authority-ca-certificate">Step 1: Upload the root certificate authority (CA) certificate</h3>
<p>Using Wrangler, you can upload your root certificate authority (CA) certificate:</p>
<pre><code class="language-bash">&#35; requires Wrangler 4.9.0 or greater&#10;npx wrangler cert upload certificate-authority --ca-cert \&lt;ROUTE_TO_CA_PEM_FILE\&gt;.pem --name \&lt;CUSTOM_NAME_FOR_CA_CERT\&gt;&#10;&#10;&#45;--&#10;&#10;Uploading CA Certificate tmp-cert...&#10;Success! Uploaded CA Certificate &lt;CUSTOM_NAME_FOR_CA_CERT&gt;&#10;ID: &lt;YOUR_ID_FOR_THE_CA_CERTIFICATE&gt;&#10;...&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9037.md")
</aside>
<h3 id="step-2-create-your-hyperdrive-configuration-using-the-ca-certificate-and-the-ssl-mode">Step 2: Create your Hyperdrive configuration using the CA certificate and the SSL mode</h3>
<p>Once your CA certificate has been created, you can create a Hyperdrive configuration with the newly created certificates using either the dashboard or Wrangler. You must also specify the SSL mode to use (<code>verify-ca</code>/<code>verify-full</code> for PostgreSQL or <code>VERIFY_CA</code>/<code>VERIFY_IDENTITY</code> for MySQL).</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9040.md")
</div></div>
<p>When creating the Hyperdrive configuration, Hyperdrive will attempt to connect to the database with the provided credentials. If the command provides successful results, you have properly configured your Hyperdrive configuration to verify the certificates provided by your database server.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9036.md")
</aside>
<h2 id="client-certificates">Client certificates</h2>
<p>Your database can be configured to verify a certificate provided by the client (in this case, Hyperdrive). This serves as an additional factor to authenticate clients (in addition to the username and password). Refer to the <a href="https://www.postgresql.org/docs/current/libpq-ssl.html#LIBPQ-SSL-CLIENTCERT">PostgreSQL</a> or <a href="https://dev.mysql.com/doc/refman/8.0/en/using-encrypted-connections.html">MySQL</a> documentation for more details.</p>
<p>For the database server to be able to verify the client certificates, Hyperdrive must be configured to provide a certificate file (<code>client-cert.pem</code>) and a private key with which the certificate was generated (<code>private-key.pem</code>).</p>
<h3 id="step-1-upload-your-client-certificates-mtls-certificates">Step 1: Upload your client certificates (mTLS certificates)</h3>
<p>Upload your client certificates to be used by Hyperdrive using Wrangler:</p>
<pre><code class="language-bash">&#35; requires Wrangler 4.9.0 or greater&#10;npx wrangler cert upload mtls-certificate --cert client-cert.pem --key client-key.pem --name &lt;CUSTOM_NAME_FOR_CLIENT_CERTIFICATE&gt;&#10;&#10;&#45;--&#10;&#10;Uploading client certificate &lt;CUSTOM_NAME_FOR_CLIENT_CERTIFICATE&gt;...&#10;Success! Uploaded client certificate &lt;CUSTOM_NAME_FOR_CLIENT_CERTIFICATE&gt;&#10;ID: &lt;YOUR_ID_FOR_THE_CLIENT_CERTIFICATE_PAIR&gt;&#10;...&#10;</code></pre>
<h3 id="step-2-create-a-hyperdrive-configuration">Step 2: Create a Hyperdrive configuration</h3>
<p>You can now create a Hyperdrive configuration using the newly created client certificate bundle using the dashboard or Wrangler.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9043.md")
</div></div>
<p>When Hyperdrive connects to your database, it will provide a client certificate signed with the private key to the database server. This allows the database server to confirm that the client, in this case Hyperdrive, has both the private key and the client certificate. By using client certificates, you can add an additional authentication layer for your database to ensure that only Hyperdrive can connect to it.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9035.md")
</aside>
