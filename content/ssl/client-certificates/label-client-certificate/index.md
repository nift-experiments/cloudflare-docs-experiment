<p>After <a href="/ssl/client-certificates/">creating client certificates</a> at Cloudflare, it may be hard to differentiate the generated certificates.</p>
<h2 id="root-cause">Root Cause</h2>
<p>The option to generate private key and CSR with Cloudflare is meant for simpler cases and the certificates will be generated with just &quot;CN=Cloudflare, C=US&quot;.</p>
<h2 id="solution">Solution</h2>
<p>If you need to differentiate client certificates for your clients on a per-organization basis, you can generate your own private key and CSR. When you generate the private key and CSR, you can then enter information that will be incorporated into your certificate request.</p>
<p>For example, if you run the following command (with OpenSSL installed):</p>
<pre><code class="language-sh">openssl req -new -newkey rsa:2048 -nodes -keyout client1.key -out client1.csr&#10;</code></pre>
<p>You can then specify:</p>
<pre><code>Country Name (2 letter code) []:&#10;State or Province Name (full name) []:&#10;Locality Name (eg, city) []:&#10;Organization Name (eg, company) []:&#10;Organizational Unit Name (eg, section) []:&#10;Common Name (eg, fully qualified host name) []:&#10;Email Address []:&#10;</code></pre>
<p>Usually, adding <code>Country Name</code> and <code>Organization Name</code> is enough, but you can provide as much information as you need or want.</p>
<p>The additional information will be included in the <strong>Certificate Subject</strong>, allowing you to easily identify which certificate belongs to which client. This can also make it easier to revoke a specific certificate when needed.</p>
<p>The following image displays an example of how a certificate with <code>Country Name</code>, <code>Organization Name</code>, and <code>Organizational Unit Name</code> will look like on the Cloudflare dashboard:</p>
<p><img src="/assets/upstream/images/support/chrome_mQRJVOpkTQ.png" alt="" /></p>
