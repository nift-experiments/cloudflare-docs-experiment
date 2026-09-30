<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9841.md")
</aside>
<h2 id="1-enable-mtls"><ol>
<li>Enable mTLS</li>
</ol></h2>
<ol>
<li>
<p>Go to your Cloudflare dashboard and select your account and domain.</p>
</li>
<li>
<p>Go to <strong>SSL/TLS</strong> &gt; <strong><a href="/ssl/client-certificates/">Client Certificates</a></strong> and, on the <strong>Hosts</strong> section, select <strong>Edit</strong> to add the hostnames you want to <a href="/ssl/client-certificates/enable-mtls/">enable mTLS</a> for.</p>
<p>Example host: <code>mtls-test.example.com</code></p>
</li>
<li>
<p>Select <strong>Add Certificate</strong>. The Cloudflare-managed CA is the default <strong>Certificate Authority</strong>.</p>
</li>
<li>
<p>Fill in the required fields. You can choose one of the following options:</p>
</li>
</ol>
<ul>
<li>Generate a private key (usually referred to as Private Certificate) and Certificate Signing Request (CSR) with Cloudflare (which includes the Public Certificate).</li>
<li>Use your own private key and CSR which allows you to also <a href="/ssl/client-certificates/label-client-certificate/">label client certificates</a>.</li>
</ul>
<p>To generate and use your own CSR, you can run a command like the following:</p>
<pre><code class="language-sh">openssl req -new -newkey rsa:2048 -nodes -keyout client1.key -out client1.csr -subj &#x27;/C=GB/ST=London/L=London/O=Organization/CN=CommonName&#x27;&#10;</code></pre>
<p>Or use a script like this one from <a href="https://github.com/erfianugrah/rootcatest/blob/main/fullgenerator.py">GitHub</a>.</p>
<p>Do not forget to copy the values shown when creating the certificate as they become unavailable after creation.</p>
<h2 id="2-install-the-client-certificate"><ol start="2">
<li>Install the client certificate</li>
</ol></h2>
<p>In order for a client to utilize the Client Certificate you created, it must be on the devices that you want to use them on. You will want to place them in the same directory as your process / script that targets your APIs / hostnames.</p>
<p>We generally recommended using one Client Certificate per device. Configuring your system to actually use the Public and Private Certificates is especially important.</p>
<p>An example is to <a href="https://support.apple.com/en-gb/guide/keychain-access/kyca2431/mac">add both certificates to the Keychain</a> on a MacBook laptop.</p>
<p>Another example is to generate a <a href="https://en.wikipedia.org/wiki/PKCS_12">PKCS12 (P12) certificate</a> file and then <a href="https://www.ibm.com/docs/en/engineering-lifecycle-management-suite/lifecycle-management/7.0.2?topic=dashboards-importing-certificates-configuring-browsers">add it to your browser</a>:</p>
<pre><code class="language-sh">openssl pkcs12 -export -out certificate.p12 -inkey private-cert.pem -in cert.pem&#10;</code></pre>
<p>Use the values from the previous step.</p>
<p>Example using cURL command:</p>
<pre><code class="language-sh">curl -v --cert cert.pem --key private-cert.pem &lt;HOSTNAME&gt;&#10;</code></pre>
<p>Use the values from the previous step.</p>
<h2 id="3-validate-the-client-certificate-in-the-waf"><ol start="3">
<li>Validate the client certificate in the WAF</li>
</ol></h2>
<p>mTLS is verified and checked in the <a href="/waf/reference/phases/">Cloudflare WAF phase</a>. This is done by creating WAF <a href="/waf/custom-rules/">Custom Rules</a> using the dynamic fields.</p>
<p>All Client Certificate details can be found in the <a href="/ruleset-engine/rules-language/fields/reference/?field-category=mTLS&amp;field-category=SSL/TLS"><code>cf.tls_*</code></a> fields in the <a href="/ruleset-engine/">Cloudflare Ruleset Engine</a>.</p>
<p>Example WAF Custom Rule with action block:</p>
<p><img src="/assets/upstream/images/learning-paths/mtls/waf-custom-rule-action-block.png" alt="Example of a WAF custom rule with an action block in the Cloudflare dashboard during the validate client certificate step" /></p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9840.md")
</aside>
<h2 id="demo">Demo</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9839.md")
</aside>
<p>With the Public and Private Certificates in the same directory, with this cURL command, we will gain access:</p>
<pre><code class="language-sh">curl -I --cert cert.pem --key private-cert.pem https://mtls-test.example.com/mtls-test&#10;</code></pre>
<pre><code class="language-txt">HTTP/2 200&#10;server: cloudflare&#10;</code></pre>
<p>Without the certificates, the terminal will display the following:</p>
<pre><code class="language-sh">curl -I https://mtls-test.example.com/mtls-test&#10;</code></pre>
<pre><code class="language-txt">HTTP/2 403&#10;server: cloudflare&#10;</code></pre>
