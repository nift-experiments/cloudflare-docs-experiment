<p>If your origin only receives traffic from <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/14280.md")
</div>, use Cloudflare origin CA certificates to encrypt traffic between Cloudflare and your origin web server and reduce bandwidth consumption. Once deployed, these certificates are compatible with [Strict SSL mode](/ssl/origin-configuration/ssl-modes/full-strict/).
<p>For more background information on origin CA certificates, refer to the <a href="https://blog.cloudflare.com/cloudflare-ca-encryption-origin/">introductory blog post</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="api-access-required">API Access required</h3>
@markup("md", "content/.markup/bodies/14279.md")
</aside>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14278.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="known-limitation">Known limitation</h3>
@markup("md", "content/.markup/bodies/14277.md")
</aside>
<hr />
<h2 id="deploy-an-origin-ca-certificate">Deploy an Origin CA certificate</h2>
<h3 id="1-create-an-origin-ca-certificate"><ol>
<li>Create an Origin CA certificate</li>
</ol></h3>
<p>To create an Origin CA certificate in the dashboard:</p>
<ol>
<li>Go to the <strong>Origin Server</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>On the <strong>Origin Certificates</strong> tab, select <strong>Create Certificate</strong>.</p>
</li>
<li>
<p>Choose either:</p>
<ul>
<li><strong>Generate private key and CSR with Cloudflare</strong>: Private key type can be RSA or ECC.</li>
<li><strong>Use my private key and CSR</strong>: Paste the Certificate Signing Request into the text field.</li>
</ul>
</li>
<li>
<p>List the <a href="#hostname-and-wildcard-coverage">hostnames (including wildcards)</a> the certificate should protect with SSL encryption. The zone apex and first level wildcard hostname are included by default.</p>
</li>
<li>
<p>Choose a <strong>Certificate Validity</strong> period.</p>
</li>
<li>
<p>Select <strong>Create</strong>.</p>
</li>
<li>
<p>Choose the <strong>Key Format</strong>:</p>
<ul>
<li>Servers using OpenSSL — like Apache and NGINX — generally expect PEM files (Base64-encoded ASCII), but also work with binary DER files.</li>
<li>Servers using Windows and Apache Tomcat require PKCS#7 (a <code>.p7b</code> file).</li>
</ul>
</li>
<li>
<p>Copy the signed <strong>Origin Certificate</strong> and <strong>Private Key</strong> into separate files. For security reasons, you cannot see the <strong>Private Key</strong> after you exit this screen.</p>
</li>
<li>
<p>Select <strong>OK</strong>.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14276.md")
</aside>
<h3 id="2-install-origin-ca-certificate-on-origin-server"><ol start="2">
<li>Install Origin CA certificate on origin server</li>
</ol></h3>
<p>To add an Origin CA certificate to your origin web server</p>
<ol>
<li>Upload the Origin CA certificate (created in <a href="#1-create-an-origin-ca-certificate">Step 1</a>) to your origin web server.</li>
<li>Update your web server configuration:</li>
</ol>
<ul>
<li><a href="https://www.digicert.com/kb/csr-ssl-installation/apache-openssl.htm">Apache httpd</a></li>
<li><a href="https://www.digitalcandy.agency/website-tips/cloudflare-origin-ca-free-ssl-installation-on-godaddy/">GoDaddy Hosting</a></li>
<li><a href="https://knowledge.digicert.com/tutorials/iis7-create-csr-install-ssl-certificate">Microsoft IIS 7</a></li>
<li><a href="https://knowledge.digicert.com/tutorials/iis-8-create-csr-install-ssl-certificate">Microsoft IIS 8 and 8.5</a></li>
<li><a href="https://www.digicert.com/kb/csr-creation-ssl-installation-iis-10.htm">Microsoft IIS 10</a></li>
<li><a href="https://www.digicert.com/kb/csr-ssl-installation/nginx-openssl.htm">NGINX</a></li>
<li><a href="https://knowledge.digicert.com/tutorials/tomcat-install-your-ssl-certificate-on-a-tomcat-server">Apache Tomcat</a></li>
<li><a href="https://knowledge.digicert.com/tutorials/amazon-aws-create-csr-install-ssl-certificate">Amazon Web Services</a></li>
<li><a href="https://www.digicert.com/kb/ssl-certificate-installation-apache-cpanel.htm">Apache cPanel</a></li>
<li><a href="https://www.digicert.com/kb/csr-ssl-installation/ubuntu-server-with-apache2-openssl.htm#ssl_certificate_install">Ubuntu Server with Apache2</a></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14275.md")
</aside>
<ol start="3">
<li>(Required for some) Upload the <a href="#cloudflare-origin-ca-root-certificate">Cloudflare CA root certificate</a> to your origin server. This can also be referred to as the certificate chain.</li>
<li>Enable SSL and port <code>443</code> at your origin web server.</li>
</ol>
<h3 id="3-change-ssl-tls-mode"><ol start="3">
<li>Change SSL/TLS mode</li>
</ol></h3>
<p>After you have installed the Origin CA certificate on your origin web server, update the SSL/TLS encryption mode for your application.</p>
<p>If all your origin hosts are protected by Origin CA certificates or publicly trusted certificates:</p>
<ol>
<li>Go to the <strong>SSL/TLS</strong> overview page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>For <strong>SSL/TLS encryption mode</strong>, select <strong>Full (strict)</strong>.</li>
</ol>
<p>If you have origin hosts that are not protected by certificates, set the <strong>SSL/TLS encryption</strong> mode for a specific application to <strong>Full (strict)</strong> by using a <a href="/rules/page-rules/">Page Rule</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14274.md")
</aside>
<h2 id="revoke-an-origin-ca-certificate">Revoke an Origin CA certificate</h2>
<p>If you misplace your key material or do not want a certificate to be trusted, you may want to revoke your certificate. You cannot undo this process.</p>
<p>To prevent visitors from seeing warnings about an insecure certificate, you may want to set your <a href="/ssl/origin-configuration/ssl-modes/">SSL/TLS encryption</a> to <strong>Full</strong> or <strong>Flexible</strong> before revoking your certificate. Do this globally via the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls">Cloudflare dashboard</a> or for a specific hostname via a <a href="/rules/page-rules/">Page Rule</a>.</p>
<p>To revoke a certificate:</p>
<ol>
<li>Go to the <strong>Origin Server</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>On the <strong>Origin Certificates</strong> tab, choose a certificate.</li>
<li>Select <strong>Revoke</strong>.</li>
</ol>
<h2 id="additional-details">Additional details</h2>
<h3 id="cloudflare-origin-ca-root-certificate">Cloudflare Origin CA root certificate</h3>
<p>Some origin web servers require upload of the Cloudflare Origin CA root certificate or certificate chain. Use the following links to download either an ECC or an RSA version and upload to your origin web server:</p>
<ul>
<li><a href="/ssl/static/origin_ca_ecc_root.pem">Cloudflare Origin ECC PEM</a> (do not use with Apache cPanel)</li>
<li><a href="/ssl/static/origin_ca_rsa_root.pem">Cloudflare Origin RSA PEM</a></li>
</ul>
<h3 id="hostname-and-wildcard-coverage">Hostname and wildcard coverage</h3>
<p>Certificates may be generated with up to 200 individual Subject Alternative Names (SANs). A SAN can take the form of a fully-qualified domain name (<code>www.example.com</code>) or a wildcard (<code>*.example.com</code>). You cannot use IP addresses as SANs on Cloudflare origin CA certificates.</p>
<p>Wildcards may only cover one level, but can be used multiple times on the same certificate for broader coverage (for example, <code>*.example.com</code> and <code>*.secure.example.com</code> may co-exist).</p>
<h2 id="api-calls">API calls</h2>
<p>To automate processes involving Origin CA certificates, use the following API calls. To authenticate, use an <a href="/fundamentals/api/get-started/create-token/">API token</a> with <strong>Permissions</strong> that include <code>Zone</code>-<code>SSL and Certificates</code>-<code>Edit</code>.</p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Method</th>
<th>Endpoint</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/api/resources/origin_ca_certificates/methods/list/">List certificates</a></td>
<td><code>GET</code></td>
<td><code>certificates?zone_id=&lt;&lt;ZONE_ID&gt;&gt;</code></td>
</tr>
<tr>
<td><a href="/api/resources/origin_ca_certificates/methods/create/">Create certificate</a></td>
<td><code>POST</code></td>
<td><code>certificates</code></td>
</tr>
<tr>
<td><a href="/api/resources/origin_ca_certificates/methods/get/">Get certificate</a></td>
<td><code>GET</code></td>
<td><code>certificates/&lt;&lt;ID&gt;&gt;</code></td>
</tr>
<tr>
<td><a href="/api/resources/origin_ca_certificates/methods/delete/">Revoke certificate</a></td>
<td><code>DELETE</code></td>
<td><code>certificates/&lt;&lt;ID&gt;&gt;</code></td>
</tr>
</tbody>
</table>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you find <code>NET::ERR_CERT_AUTHORITY_INVALID</code> or other issues after setting up Cloudflare origin CA, refer to <a href="/ssl/origin-configuration/origin-ca/troubleshooting/">troubleshooting</a>.</p>
