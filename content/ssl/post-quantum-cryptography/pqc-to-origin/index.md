<p>This page covers post-quantum cryptography on the TLS connection between Cloudflare's edge and your origin server. Cloudflare supports both <a href="#post-quantum-key-agreement">post-quantum key agreement</a> (X25519MLKEM768) and <a href="#post-quantum-signatures">post-quantum signatures</a> (ML-DSA via Authenticated Origin Pulls and Custom Origin Trust Store) on this connection.</p>
<p>If you would prefer to connect your origin to Cloudflare without managing certificates on a publicly exposed TLS endpoint, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> is another option for post-quantum origin connections. Cloudflare Tunnel uses post-quantum key agreement on the TLS connection between <code>cloudflared</code> and Cloudflare's network. Post-quantum signatures are not yet used for authentication on that path.</p>
<h2 id="post-quantum-key-agreement">Post-quantum key agreement</h2>
<p>As explained in <a href="/ssl/post-quantum-cryptography/">About PQC</a>, Cloudflare has deployed support for hybrid key agreements, which includes both the most common key agreement for TLS 1.3, X25519, and the post-quantum secure ML-KEM.</p>
<p>With X25519, the <a href="https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/">ClientHello</a> almost always fits within one network packet. However, with the addition of ML-KEM, the ClientHello is typically split across two packets.</p>
<p>This poses a question of how the origin servers - as well as other middleboxes (routers, load balancers, etc) - will handle this change in behavior. Although allowed by the TLS 1.3 standard (<a href="https://www.rfc-editor.org/rfc/rfc8446.html">RFC 8446</a>), a split ClientHello risks not being handled well due to <a href="https://en.wikipedia.org/wiki/Protocol_ossification">protocol ossification</a> and implementation bugs. Refer to our <a href="https://blog.cloudflare.com/post-quantum-to-origins/">blog post</a> for details.</p>
<h3 id="clienthello-from-cloudflare">ClientHello from Cloudflare</h3>
<p>Cloudflare uses <a href="/ssl/origin-configuration/automatic-key-exchange/">automatic key exchange</a> to learn which key agreements a zone's origin servers prefer. Cloudflare applies one preference across the zone. When the selected preference is <a href="/ssl/post-quantum-cryptography/#hybrid-key-agreement">X25519MLKEM768</a>, Cloudflare sends that key share in the initial <code>ClientHello</code> to allow for faster connection establishment.</p>
<p>Cloudflare continues to advertise other allowed key agreements. If an origin requires another key share, it can use a <a href="https://www.rfc-editor.org/rfc/rfc8446.html#section-4.1.4">HelloRetryRequest</a> to request one. The retry adds one network round trip but does not break the connection.</p>
<h3 id="set-up">Set up</h3>
<h4 id="cloudflare-zone-settings">Cloudflare zone settings</h4>
<p><a href="/ssl/origin-configuration/automatic-key-exchange/">Automatic key exchange</a> is on for all existing zones and on by default for new zones. When an origin supports both classical and post-quantum options, Cloudflare prefers post-quantum key agreement.</p>
<p>Use <strong>Automatic key exchange</strong> to control scanning and preferred key share selection. Compliance requirements apply only to TLS 1.3 connections.</p>
<p>The <a href="/api/resources/origin_post_quantum_encryption/methods/update/">Origin Post-Quantum Encryption API</a> remains available. Requests to this API are no-ops and do not change a zone's post-quantum key agreement behavior. Cloudflare plans to deprecate this API, but a deprecation date has not been established.</p>
<h4 id="origin-server">Origin server</h4>
<p>To make sure that your origin server prefers the post-quantum key agreement, use the <code>bssl</code> tool of <a href="https://github.com/google/boringssl">BoringSSL</a>:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13990.md")
</div>
<h2 id="post-quantum-signatures">Post-quantum signatures</h2>
<p>Since mid-2026, Cloudflare supports <a href="https://csrc.nist.gov/pubs/fips/204/final">ML-DSA</a> post-quantum signatures in two origin-facing features:</p>
<ul>
<li><a href="/ssl/origin-configuration/authenticated-origin-pull/">Authenticated Origin Pulls</a> (AOP) — Cloudflare presents an ML-DSA client certificate during the mTLS handshake to the origin.</li>
<li><a href="/ssl/origin-configuration/custom-origin-trust-store/">Custom Origin Trust Store</a> (COTS) — Cloudflare trusts an ML-DSA certificate authority when validating the origin server certificate under <a href="/ssl/origin-configuration/ssl-modes/full-strict/">Full (strict) encryption mode</a>.</li>
</ul>
<p>Both can be used independently or together. Using them together lets you establish end-to-end post-quantum authentication between Cloudflare's edge and your origin server, in addition to <a href="#post-quantum-key-agreement">post-quantum key agreement</a>.</p>
<h3 id="requirements">Requirements</h3>
<ul>
<li>A TLS library on your origin that supports ML-DSA — for example, <a href="https://www.openssl.org/">OpenSSL</a> 3.5.0 or later. Refer to <a href="/ssl/post-quantum-cryptography/pqc-support/">PQC support</a> for additional options.</li>
<li><a href="https://www.openssl.org/">OpenSSL</a> 3.5.0 or later on your workstation to generate certificates.</li>
<li>An origin server that negotiates TLS 1.3 for ML-DSA signatures.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13989.md")
</aside>
<h3 id="generate-an-ml-dsa-certificate-authority-and-leaf-certificate">Generate an ML-DSA certificate authority and leaf certificate</h3>
<p>The following commands create a private certificate authority and a leaf certificate that chains to it, using ML-DSA-44. Repeat once for an AOP client certificate, and once for a COTS server-facing certificate if you manage that side too.</p>
<pre><code class="language-bash">&#35; Private ML-DSA-44 CA (30-year validity)&#10;openssl genpkey \&#10;  &#45;algorithm mldsa44 \&#10;  &#45;provparam ml-dsa.output_formats=seed-only \&#10;  &#45;out ca.key&#10;openssl req -new -x509 \&#10;  &#45;key ca.key \&#10;  &#45;out ca.crt \&#10;  &#45;days 10950 \&#10;  &#45;subj &quot;/CN=ML-DSA Origin CA&quot;&#10;&#10;&#35; Leaf certificate signed by the CA (15-year validity)&#10;openssl genpkey \&#10;  &#45;algorithm mldsa44 \&#10;  &#45;provparam ml-dsa.output_formats=seed-only \&#10;  &#45;out leaf.key&#10;openssl req -new \&#10;  &#45;key leaf.key \&#10;  &#45;out leaf.csr \&#10;  &#45;subj &quot;/CN=origin.example.com&quot; \&#10;  &#45;addext basicConstraints=CA:FALSE \&#10;  &#45;addext keyUsage=digitalSignature \&#10;  &#45;addext subjectAltName=DNS:origin.example.com&#10;openssl x509 -req \&#10;  &#45;in leaf.csr \&#10;  &#45;CA ca.crt -CAkey ca.key \&#10;  &#45;CAcreateserial \&#10;  &#45;out leaf.crt \&#10;  &#45;days 5475 \&#10;  &#45;copy_extensions copy&#10;</code></pre>
<p>The <code>-provparam ml-dsa.output_formats=seed-only</code> flag is required so that the private key is written in the FIPS 204 seed form rather than as the expanded private key. This is the only form Cloudflare currently accepts on upload.</p>
<p>Verify the generated cert:</p>
<pre><code class="language-bash">openssl x509 -in leaf.crt -noout -subject -issuer -dates -ext subjectAltName&#10;</code></pre>
<h3 id="set-up-authenticated-origin-pulls-with-an-ml-dsa-client-certificate">Set up Authenticated Origin Pulls with an ML-DSA client certificate</h3>
<p>ML-DSA client certificates are supported with both <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/zone-level/">zone-level</a> and <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/">per-hostname</a> AOP. Generate an ML-DSA CA and leaf cert as described in <a href="#generate-an-ml-dsa-certificate-authority-and-leaf-certificate">Generate an ML-DSA certificate authority and leaf certificate</a>, then follow the setup guide for the scope you are configuring. The <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/global/">global AOP</a> scope uses a Cloudflare-provided certificate and is not configurable.</p>
<p>On the origin server side, install the ML-DSA CA certificate (the <code>ca.crt</code> file generated earlier) so that your TLS server can verify the client certificate that Cloudflare presents. For nginx, this looks like:</p>
<pre><code class="language-txt">ssl_client_certificate /etc/ssl/cloudflare-aop-ca.crt;&#10;ssl_verify_client      on;&#10;</code></pre>
<p>Refer to the <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/">AOP setup guide for origin servers</a> for complete origin-side configuration.</p>
<h3 id="set-up-custom-origin-trust-store-with-an-ml-dsa-ca">Set up Custom Origin Trust Store with an ML-DSA CA</h3>
<p>Upload the ML-DSA CA certificate (the <code>ca.crt</code> file generated earlier) as a <a href="/ssl/origin-configuration/custom-origin-trust-store/">Custom Origin Trust Store</a> entry. Cloudflare will then trust any origin server certificate that chains to that CA under <a href="/ssl/origin-configuration/ssl-modes/full-strict/">Full (strict) encryption mode</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13988.md")
</aside>
<p>On the origin server side, present the ML-DSA leaf certificate and its private key as the TLS server cert:</p>
<pre><code class="language-txt">ssl_certificate     /etc/ssl/origin-mldsa.pem;&#10;ssl_certificate_key /etc/ssl/origin-mldsa.key;&#10;ssl_protocols       TLSv1.3;&#10;</code></pre>
<h3 id="verify-end-to-end">Verify end-to-end</h3>
<p>Once AOP and COTS are configured, you can verify the post-quantum origin handshake from a host that has ML-DSA support. For example, from a machine with OpenSSL 3.5.0 or later, connect directly to your origin and confirm the handshake uses ML-DSA:</p>
<pre><code class="language-bash">openssl s_client \&#10;  &#45;connect origin.example.com:443 \&#10;  &#45;servername origin.example.com \&#10;  &#45;CAfile ca.crt \&#10;  &#45;cert leaf.crt \&#10;  &#45;key leaf.key \&#10;  &#45;brief&#10;</code></pre>
<p>The output should show <code>Signature type: mldsa44</code> and <code>Negotiated TLS1.3 group: X25519MLKEM768</code>.</p>
<h3 id="avoid-downgrades">Avoid downgrades</h3>
<p>Presenting an ML-DSA certificate on the authenticating side is not enough on its own. To actually gain post-quantum authentication, the <em>verifying</em> side must reject classical (non-post-quantum) certificates. If the verifier still accepts a classical certificate, an attacker who compromises that classical key can impersonate the peer with an <a href="https://www.cloudflare.com/learning/security/threats/on-path-attack/">on-path attack</a> — a downgrade that negates the post-quantum protection.</p>
<ul>
<li><strong>Custom Origin Trust Store (COTS):</strong> Upload only ML-DSA certificate authorities. If you leave classical CAs in the trust store alongside the ML-DSA CA, Cloudflare will still accept an origin certificate that chains to a classical CA, leaving the connection open to downgrade. Uploading a COTS CA already replaces the default publicly trusted CAs for the zone (see the caution above), so make sure every CA you upload is post-quantum.</li>
<li><strong>Authenticated Origin Pulls (AOP):</strong> Configure your origin server to require the ML-DSA client certificate and to reject classical client certificates. Cloudflare presenting an ML-DSA certificate only helps if the origin refuses to authenticate connections that use a classical certificate.</li>
</ul>
