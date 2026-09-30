<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6043.md")
</aside>
<p>Enterprise customers who do not wish to install a <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/manual-deployment/">Cloudflare certificate</a> have the option to upload their own root certificate to Cloudflare. This feature is sometimes referred to as Bring Your Own Public Key Infrastructure (BYOPKI). Gateway will use your uploaded certificate to encrypt all sessions between the end user and Gateway, enabling all HTTPS inspection features that previously required a Cloudflare certificate. You can upload multiple certificates to your account, but only one can be active at any given time. You also need to upload a private key to intercept domains with JIT certificates and to enable the <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/">block page</a>.</p>
<p>You can upload either a root certificate or a full certificate chain (root certificate plus intermediate certificates). Uploading a certificate chain allows end-user devices to only install the root certificate, which can simplify certificate management for larger enterprises.</p>
<p>You can upload up to five custom root certificates. If your organization requires more than five certificates, contact your account team.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6042.md")
</aside>
<h2 id="generate-a-custom-root-ca">Generate a custom root CA</h2>
<ol>
<li>
<p>Open a terminal.</p>
</li>
<li>
<p>(Optional) Create a directory for the root CA and change into it.</p>
</li>
</ol>
<pre><code class="language-sh">mkdir -p /root/customca&#10;cd /root/customca&#10;</code></pre>
<p>You can generate the certificate files in any directory. This step keeps things organized. If you skip it, files will be created in your current working directory.</p>
<ol start="3">
<li>Generate a private key for the root CA.</li>
</ol>
<pre><code class="language-sh">openssl genrsa -out &lt;CUSTOM-ROOT-PRIVATE-KEY&gt;.pem 2048&#10;</code></pre>
<p>The <code>2048</code> value specifies the RSA key size in bits. You can use <code>4096</code> for stronger security at the cost of slightly slower TLS handshakes.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6041.md")
</aside>
<ol start="4">
<li>Generate a self-signed root certificate.</li>
</ol>
<pre><code class="language-sh">openssl req -x509 -sha256 -new -nodes \&#10;  &#45;key &lt;CUSTOM-ROOT-PRIVATE-KEY&gt;.pem \&#10;  &#45;days 365 \&#10;  &#45;out &lt;CUSTOM-ROOT-CERT&gt;.pem \&#10;  &#45;addext &quot;basicConstraints=critical,CA:TRUE&quot; \&#10;  &#45;addext &quot;keyUsage=critical,keyCertSign,cRLSign&quot;&#10;</code></pre>
<p>The <code>-addext</code> flags add the <code>basicConstraints</code> and <code>keyUsage</code> extensions required by <a href="https://datatracker.ietf.org/doc/html/rfc5280">RFC 5280</a> for CA certificates. Without them, some TLS clients may reject certificates signed by your custom CA. In particular, Python 3.13 and later enforce strict RFC 5280 compliance by default (<code>ssl.VERIFY_X509_STRICT</code>), causing HTTPS requests to fail for devices using the Cloudflare One Client when the uploaded CA does not include these extensions.</p>
<p>The <code>-days 365</code> value controls certificate expiry. A shorter duration reduces risk if the key is compromised, but requires more frequent rotation. Rotating a deployed BYOPKI certificate is a disruptive operation, so choose an expiry that balances security with operational overhead.</p>
   <details class="nb-details"><summary>Error: �CODE18�</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6044.md")
</div></details>
<ol start="5">
<li>Verify the required RFC 5280 extensions are present:</li>
</ol>
<pre><code class="language-sh">openssl x509 -in &lt;CUSTOM-ROOT-CERT&gt;.pem -noout -ext keyUsage,basicConstraints&#10;</code></pre>
<pre><code>The output should include:&#10;</code></pre>
<pre><code class="language-txt">X509v3 Basic Constraints: critical&#10;		CA:TRUE&#10;X509v3 Key Usage: critical&#10;		Certificate Sign, CRL Sign&#10;</code></pre>
<pre><code>If these fields are missing, regenerate the certificate using the command in step 4.&#10;</code></pre>
<ol start="6">
<li>To review the private key, run the following command:</li>
</ol>
<pre><code class="language-sh">openssl rsa -in &lt;CUSTOM-ROOT-PRIVATE-KEY&gt;.pem -text&#10;</code></pre>
<pre><code>To review the certificate, run the following command:&#10;</code></pre>
<pre><code class="language-sh">openssl x509 -in &lt;CUSTOM-ROOT-CERT&gt;.pem -text&#10;</code></pre>
<p>When preparing your certificate and private key for upload, be sure to remove any unwanted characters, such as mismatching subdomains in the certificate's common name.</p>
<h2 id="deploy-a-custom-root-certificate">Deploy a custom root certificate</h2>
<p>You can upload a single root certificate or a full certificate chain. When uploading a certificate chain via the dashboard, API, or Terraform, concatenate the root certificate and any intermediate certificates in PEM format, with the root certificate first.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6047.md")
</div></div>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="private-key-visibility">Private key visibility</h3>
@markup("md", "content/.markup/bodies/6040.md")
</aside>
<h2 id="use-a-custom-root-certificate">Use a custom root certificate</h2>
<p>To use a custom root certificate you generated and uploaded to Cloudflare, refer to <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/#activate-a-root-certificate">Activate a root certificate</a>.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="error-526-invalid-ssl-certificate">Error 526: Invalid SSL certificate</h3>
<p>If Gateway returns an <strong>HTTP Response Code: 526</strong> after deploying a custom certificate, refer to the <a href="/cloudflare-one/traffic-policies/troubleshooting/#error-526-invalid-ssl-certificate">Error 526 documentation</a>.</p>
<h3 id="python-3-13-ssl-errors-with-the-cloudflare-one-client">Python 3.13+ SSL errors with the Cloudflare One Client</h3>
<p>Python 3.13 and later enable <code>ssl.VERIFY_X509_STRICT</code> by default, which requires CA certificates to comply with <a href="https://datatracker.ietf.org/doc/html/rfc5280">RFC 5280</a>. If your BYOPKI certificate was generated without the <code>keyUsage</code> and <code>basicConstraints</code> extensions, Python HTTPS requests will fail when the Cloudflare One Client is active. To resolve the issue, <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/custom-certificate/#generate-a-custom-root-ca">generate a new custom root CA</a> and upload it to Cloudflare.</p>
