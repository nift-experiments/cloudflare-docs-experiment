<h2 id="add-client-cert-and-client-cert-chain-headers-rfc-9440">Add Client-Cert and Client-Cert-Chain headers (RFC 9440)</h2>
<p><a href="https://datatracker.ietf.org/doc/html/rfc9440">RFC 9440</a> defines the <code>Client-Cert</code> and <code>Client-Cert-Chain</code> HTTP header fields for passing client certificate information to origin servers. You can construct these headers using <a href="/rules/transform/request-header-modification/">request header modification rules</a> with the following Ruleset Engine fields:</p>
<ul>
<li><a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_rfc9440/"><code>cf.tls_client_auth.cert_rfc9440</code></a> — The client leaf certificate encoded in RFC 9440 formatting (see reference).</li>
<li><a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_chain_rfc9440/"><code>cf.tls_client_auth.cert_chain_rfc9440</code></a> — The certificate chain (excluding the leaf certificate) encoded in RFC 9440 formatting (see reference).</li>
</ul>
<p>As indicated in field definitions, the fields may be set to either an empty string or a valid RFC 9440 encoding. Proper usage depends on a couple of factors discussed in the following sections.</p>
<h3 id="security-considerations">Security considerations</h3>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/14019.md")
</aside>
<p>The <code>cert_rfc9440</code> and <code>cert_chain_rfc9440</code> fields are populated <strong>regardless of the certificate validation result</strong>. This means a client can present an invalid, expired, or self-signed certificate, and the fields will still contain the encoded certificate data. Always check the following fields before trusting the values:</p>
<ul>
<li><a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_verified/"><code>cf.tls_client_auth.cert_verified</code></a> — Returns <code>true</code> when the client certificate is valid.</li>
<li><a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_revoked/"><code>cf.tls_client_auth.cert_revoked</code></a> — Returns <code>true</code> when the client certificate has been revoked.</li>
</ul>
<p>A client can also include its own <code>Client-Cert</code> or <code>Client-Cert-Chain</code> headers on a request to inject arbitrary values. As described in the <a href="https://datatracker.ietf.org/doc/html/rfc9440#name-security-considerations">RFC 9440 security considerations</a>, you must unconditionally remove any existing <code>Client-Cert</code> and <code>Client-Cert-Chain</code> headers from incoming requests, regardless of certificate validity. This prevents a client from injecting forged certificate data that your origin would trust.</p>
<p>See <a href="/ssl/client-certificates/enable-mtls/">Enable mTLS</a> for details on how to configure mTLS and certificate validation.</p>
<h3 id="size-limits">Size limits</h3>
<p>The encoded leaf certificate is limited to 10 KiB and the encoded chain is limited to 16 KiB. If the encoded value exceeds the limit, the corresponding field contains an empty string. Use the following fields to check for this condition:</p>
<ul>
<li><a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_rfc9440_too_large/"><code>cf.tls_client_auth.cert_rfc9440_too_large</code></a> — Returns <code>true</code> when the encoded certificate exceeds 10 KiB.</li>
<li><a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_chain_rfc9440_too_large/"><code>cf.tls_client_auth.cert_chain_rfc9440_too_large</code></a> — Returns <code>true</code> when the encoded chain exceeds 16 KiB.</li>
</ul>
<h3 id="example-transform-rules">Example Transform Rules</h3>
<p>Here we provide an example on how to securely use these fields to construct trusted <code>Client-Cert</code> and <code>Client-Cert-Chain</code> headers to be forwarded to your origin.
The origin can then rely on the presence of the headers to be certain the client presented a valid certificate.
Note: the <code>Client-Cert-Chain</code> header may be omitted when the client did not present any intermediates (only a leaf certificate).</p>
<p>You need to create the following request header modification rules.
The <strong>Remove</strong> rules must be placed before the <strong>Set dynamic</strong> rules
so that client-injected headers are stripped on every request before the validated values are set.</p>
<h4 id="rule-1-remove-client-cert-header">Rule 1 — Remove Client-Cert header</h4>
<p>This rule unconditionally removes any <code>Client-Cert</code> header sent by the client.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/14020.md")
</div>
<h4 id="rule-2-remove-client-cert-chain-header">Rule 2 — Remove Client-Cert-Chain header</h4>
<p>This rule unconditionally removes any <code>Client-Cert-Chain</code> header sent by the client.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@markup("md", "content/.markup/bodies/14021.md")
</div>
<h4 id="rule-3-set-client-cert-header">Rule 3 — Set Client-Cert header</h4>
<p>This rule sets the <code>Client-Cert</code> header only when the client presented a valid, non-revoked certificate that is within the size limit.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-2">Example</h3>
@markup("md", "content/.markup/bodies/14022.md")
</div>
<h4 id="rule-4-set-client-cert-chain-header">Rule 4 — Set Client-Cert-Chain header</h4>
<p>This rule sets the <code>Client-Cert-Chain</code> header only when the client presented a valid, non-revoked certificate
and the chain is non-empty and within the size limit.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example-3">Example</h3>
@markup("md", "content/.markup/bodies/14023.md")
</div>
<h3 id="cloudflare-workers">Cloudflare Workers</h3>
<p>You can also construct RFC 9440 headers in a <a href="/workers/">Cloudflare Worker</a>
using the <a href="/ssl/client-certificates/client-certificate-variables/#workers-variables"><code>tlsClientAuth</code></a>
properties on the incoming request.</p>
<p>The same security considerations mentioned above apply.</p>
<h2 id="forward-a-client-certificate-legacy">Forward a client certificate (legacy)</h2>
<p>In addition to enforcing mTLS authentication for your host, you can also forward a client certificate to your origin server as an HTTP header. This setup is often helpful for server logging.</p>
<p>To avoid adding the certificate to every single request, the certificate is only forwarded on the first request of an mTLS connection.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14018.md")
</aside>
<h3 id="cloudflare-api">Cloudflare API</h3>
<p>The most common approach to forwarding a certificate is to use the Cloudflare API to <a href="/api/resources/zero_trust/subresources/access/subresources/certificates/subresources/settings/methods/update/">update an mTLS certificate's hostname settings</a>.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/access/certificates/settings \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;settings&quot;: [&#10;    {&#10;      &quot;hostname&quot;: &quot;&lt;HOSTNAME&gt;&quot;,&#10;      &quot;china_network&quot;: false,&#10;      &quot;client_certificate_forwarding&quot;: true&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<p>Once <code>client_certificate_forwarding</code> is set to <code>true</code>, every request within an mTLS connection will now include the following headers:</p>
<ul>
<li><code>Cf-Client-Cert-Der-Base64</code></li>
<li><code>Cf-Client-Cert-Sha256</code></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14017.md")
</aside>
<h3 id="managed-transforms">Managed Transforms</h3>
<p>You can also <a href="/rules/transform/response-header-modification/">modify HTTP response headers</a> using Managed Transforms to pass along <strong>TLS client auth headers</strong>.</p>
<h3 id="cloudflare-workers-1">Cloudflare Workers</h3>
<p>Additionally, Workers can provide details around the <a href="/workers/runtime-apis/bindings/mtls/">client certificate</a>.</p>
<pre><code class="language-js">const tlsHeaders = {&#10;	&quot;X-CERT-ISSUER-DN&quot;: request.cf.tlsClientAuth.certIssuerDN,&#10;	&quot;X-CERT-SUBJECT-DN&quot;: request.cf.tlsClientAuth.certSubjectDN,&#10;	&quot;X-CERT-ISSUER-DN-L&quot;: request.cf.tlsClientAuth.certIssuerDNLegacy,&#10;	&quot;X-CERT-SUBJECT-DN-L&quot;: request.cf.tlsClientAuth.certSubjectDNLegacy,&#10;	&quot;X-CERT-SERIAL&quot;: request.cf.tlsClientAuth.certSerial,&#10;	&quot;X-CERT-FINGER&quot;: request.cf.tlsClientAuth.certFingerprintSHA1,&#10;	&quot;X-CERT-VERIFY&quot;: request.cf.tlsClientAuth.certVerify,&#10;	&quot;X-CERT-NOTBE&quot;: request.cf.tlsClientAuth.certNotBefore,&#10;	&quot;X-CERT-NOTAF&quot;: request.cf.tlsClientAuth.certNotAfter,&#10;};&#10;</code></pre>
