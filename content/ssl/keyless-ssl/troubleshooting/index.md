<h2 id="check-the-logs">Check the logs</h2>
<p>To check logs, use a command similar to the following.</p>
<ul>
<li>systemd: <code>sudo journalctl -f -u gokeyless</code></li>
<li>upstart/sysvinit: <code>sudo tail -f /var/log/gokeyless.log</code></li>
</ul>
<h2 id="enable-debug-logging">Enable debug logging</h2>
<p>To enable debug logging, use a command similar to the following.</p>
<pre><code class="language-sh">cd /etc/keyless&#10;sudo -u keyless gokeyless --loglevel 0&#10;</code></pre>
<p>When running in a container, <code>gokeyless</code> is the container's main process (PID 1), so the host/systemd command above does not apply. Instead, set the log level when you start the container and read logs from the container runtime:</p>
<pre><code class="language-sh">&#35; Set verbosity via environment variable&#10;docker run ... -e KEYLESS_LOGLEVEL=0 ghcr.io/cloudflare/gokeyless:latest&#10;&#10;&#35; Read logs&#10;docker logs -f &lt;CONTAINER&gt;   # or: kubectl logs -f &lt;POD&gt;&#10;</code></pre>
<h2 id="browsers-are-seeing-a-tls-connection-failure-after-trying-to-connect">Browsers are seeing a TLS connection failure after trying to connect</h2>
<ol>
<li>Make sure your key server is accessible from outside your network (tcp/2407).</li>
<li>Provide a packet capture:
<code>sudo tcpdump -nni &lt;interface&gt; -s 0 -w keyless-$(date +%s).pcap port 2407</code></li>
</ol>
<h2 id="clients-are-connecting-but-immediately-aborting">Clients are connecting, but immediately aborting</h2>
<p>If you run <code>gokeyless</code> with debug logging enabled, and you see logs like this:</p>
<pre><code class="language-txt">[DEBUG] connection 162.158.57.220:37490: reading half closed by client&#10;[DEBUG] connection 162.158.57.220:37490: server closing connection&#10;[DEBUG] connection 162.158.57.220:37490 removed&#10;[DEBUG] spawning new connection: 162.158.57.220:37862&#10;[DEBUG] connection 162.158.57.220:37862: reading half closed by client&#10;[DEBUG] connection 162.158.57.220:37862: server closing connection&#10;[DEBUG] connection 162.158.57.220:37862 removed&#10;</code></pre>
<p>These logs likely indicate that the key server is not using an appropriate server or .<code>PEM</code> file and the client is aborting the connection after the certificate exchange. The certificate must be signed by the keyless CA and the SANs must include the hostname of the keyless server. Here is a valid example for a keyless server located at <code>11aa40b4a5db06d4889e48e2f.example.com</code> (note the Subject Alternative Name and Authority Key Identifier):</p>
<pre><code class="language-bash">openssl x509 -in server.pem -noout -text -certopt no_subject,no_header,no_version,no_serial,no_signame,no_validity,no_subject,no_issuer,no_pubkey,no_sigdump,no_aux | sed -e &#x27;s/^        //&#x27;&#10;</code></pre>
<pre><code class="language-bash">X509v3 extensions:&#10;    X509v3 Key Usage: critical&#10;        Digital Signature, Key Encipherment&#10;    X509v3 Extended Key Usage:&#10;        TLS Web Server Authentication&#10;    X509v3 Basic Constraints: critical&#10;        CA:FALSE&#10;    X509v3 Subject Key Identifier:&#10;        DD:24:97:F1:A9:F1:4C:73:D9:1B:44:EC:A1:C3:10:E9:F0:41:98:BB&#10;    X509v3 Authority Key Identifier:&#10;        keyid:29:CE:8F:F1:9D:4C:BA:DE:55:78:D7:A6:29:E9:C5:FD:1D:9D:21:48&#10;&#10;    X509v3 Subject Alternative Name:&#10;        DNS:11aa40b4a5db06d4889e48e2f.example.com&#10;    X509v3 CRL Distribution Points:&#10;&#10;        Full Name:&#10;          URI:http://ca.cfdata.org/api/v1/crl/key_server&#10;</code></pre>
<h2 id="the-gokeyless-binary-cannot-load-the-ca-file">The gokeyless binary cannot load the CA file</h2>
<p>Ensure permissions are correct on all keys and certificates installed on the server.</p>
<h2 id="keyless-is-affecting-to-unanticipated-hosts">Keyless is affecting to unanticipated hosts</h2>
<p>You will need to either provide a certificate for only those hosts or change the priority of the certificate in the <strong>SSL/TLS</strong> app of your Cloudflare dashboard.</p>
<h2 id="key-servers-on-windows">Key servers on Windows</h2>
<p>Cloudflare currently only provide packages for the supported GNU/Linux distributions as per the <a href="https://pkg.cloudflare.com/">Cloudflare package repository</a>.</p>
<p>However, the key server is open source so you may attempt to build and deploy a binary, but running on Windows is not a supported configuration so you may experience problems that Cloudflare will not be able to help with.</p>
<h2 id="key-server-multi-domain-support">Key server multi-domain support</h2>
<p>A single key server can serve multiple domains. Add each certificate's private key to the <code>private_key_stores</code> block in <code>gokeyless.yaml</code>, or pass them with <code>--private-key-dirs</code> / <code>--private-key-files</code>. Refer to <a href="/ssl/keyless-ssl/configuration/run-with-docker/#serve-multiple-private-keys">Serve multiple private keys</a> for details.</p>
<p>The <code>hostname</code> and <code>zone_id</code> fields are single string values used only during enrollment. You do not need to update them for additional domains.</p>
<h2 id="additional-questions">Additional questions</h2>
<p>Contact your account team or <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a>.</p>
