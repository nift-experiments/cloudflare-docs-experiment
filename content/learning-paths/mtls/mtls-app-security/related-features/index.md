<h2 id="label-client-certificates">Label Client Certificates</h2>
<p>To make it easier to differentiate between Client Certificates, you can generate your own private key and CSR, and enter information that will be incorporated into your certificate request, essentially <a href="/ssl/client-certificates/label-client-certificate/">labeling your Client Certificates</a>.</p>
<h2 id="certificate-revocation">Certificate Revocation</h2>
<p>In cases of noticing excessive traffic, anomalous traffic (strange sequences of requests), or generally too many attack attempts registered from specific devices using your Client Certificates, it is best to <a href="/ssl/client-certificates/revoke-client-certificate/">revoke</a> those.</p>
<p>Additionally, ensure to have a WAF <a href="/waf/custom-rules/">Custom Rule</a> in place to block <a href="/api-shield/security/mtls/configure/#check-for-revoked-certificates">revoked</a> Client Certificates. Review the available <a href="/ruleset-engine/rules-language/fields/reference/?field-category=mTLS&amp;field-category=SSL/TLS"><code>cf.tls_*</code></a> fields.</p>
<p>Example WAF Custom Rule with action block:</p>
<p><img src="/assets/upstream/images/learning-paths/mtls/certification-revocation-custom-rule.png" alt="Example expression for certification revocation using a WAF custom rule in the Cloudflare dashboard" /></p>
<pre><code class="language-text">(cf.tls_client_auth.cert_revoked)&#10;</code></pre>
<p>A better approach may be to check for unverified or revoked client certificates:</p>
<pre><code class="language-txt">(not cf.tls_client_auth.cert_verified) or cf.tls_client_auth.cert_revoked&#10;</code></pre>
<p>Generally, ensure client certificates are rotated regularly and safely to reduce the risk of compromise.</p>
<h2 id="forward-a-client-certificate">Forward a client certificate</h2>
<p>There are multiple ways to <a href="/ssl/client-certificates/forward-a-client-certificate/">forward a client certificate</a> to your origin server.</p>
<h2 id="bring-your-own-ca-for-mtls">Bring your own CA for mTLS</h2>
<p>If you already have mTLS implemented, client certificates are already installed on devices, and therefore you would like to use your own Certificate Authority (CA), this is possible by <a href="/ssl/client-certificates/byo-ca/">bringing your own CA for mTLS</a>.</p>
<p>You can associate your uploaded CAs with specific hostnames via the dashboard or the <a href="/api/resources/certificate_authorities/subresources/hostname_associations/methods/update/">Replace Hostname Associations API endpoint</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9838.md")
</aside>
<h2 id="client-certificate-deployment">Client Certificate Deployment</h2>
<p>There are different ways to safely and securely deploy Client Certificates across devices.</p>
<p>Some of the most used methods are <a href="/ssl/client-certificates/configure-your-mobile-app-or-iot-device/#3-embed-the-client-certificate-in-your-mobile-app">embedding</a> the Client Certificate into an application and allowing user devices to download and install that app, or use mobile device management (MDM) to distribute certificates across devices, or to allow user devices to directly download and install the Client Certificate into a device's Certificate Store.</p>
<p>Issuing a certificate is an important step, so if possible, perform thorough client verification.</p>
<p>In complex microservices environments, you can leverage Service Mesh to automate and enforce mTLS at scale. For example, Cloudflare services can handle external traffic security, while Service Mesh technologies enforce mTLS for east-west traffic within your network. This ensures that external traffic is secured by Cloudflare, while internal microservice communication is protected using mTLS via the Service Mesh.</p>
<h2 id="customize-cipher-suites">Customize Cipher Suites</h2>
<p>It is generally recommended to <a href="/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/">customize the cipher suites</a> of your Cloudflare <a href="/ssl/edge-certificates/">Edge Certificates</a>. This only applies to the Edge Certificates, not Client Certificates.</p>
<p>The recommended TLS versions for mTLS are:</p>
<ul>
<li>TLS 1.2: still broadly compatible and secure.</li>
<li>TLS 1.3: preferred for new implementations due to its enhanced security and efficiency.</li>
</ul>
<p>Using outdated versions like TLS 1.0 or 1.1 is not recommended due to known vulnerabilities.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9837.md")
</aside>
<h2 id="tls-session-resumption">TLS Session Resumption</h2>
<p>Browsers connecting to a domain with a <a href="/dns/manage-dns-records/reference/wildcard-dns-records/">wildcard</a> <a href="/ssl/edge-certificates/">Edge Certificate</a> in place, connecting to the same domain's mTLS subdomain could cause a non-authentication event, due to TLS Session Resumption, or also called <a href="/speed/optimization/protocol/0-rtt-connection-resumption/">Connection Resumption</a>.</p>
<p>It is generally not recommended to use wildcard certificates.</p>
<p>Review the <a href="/ssl/client-certificates/troubleshooting/">troubleshooting documentation</a> for more info.</p>
<h2 id="tls-session-renegotiation">TLS Session Renegotiation</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9836.md")
</aside>
<p>If you need to use Client Certificates after the TLS handshake via renegotiation, you will need to use a prior TLS version than 1.3. This is because TLS 1.3 does not support renegotiation.</p>
<p>For example, if you are using mTLS and you are restricting requests to certain folders, based on a URL path in the request, rather than all content on your origin server, a TLS renegotiation may be triggered. Connections using TLS 1.3 do not support renegotiation.</p>
<h2 id="chain-of-trust">Chain of Trust</h2>
<p>Customers create Client Certificates and select the option to <em>use my private key and CSR</em>. The customer provides the CSR supplied by end-customers to generate the client certificates shared with end-customers. However, if your end-customers request the Certificate Chain, this can potentially be shared by the Cloudflare account team.</p>
<p>Contact your account team for more information.</p>
<h2 id="waf-for-client-certificates">WAF for Client Certificates</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9835.md")
</aside>
<p>In order to effectively implement mTLS with Cloudflare, it is strongly recommended to properly configure the <a href="/waf/">Cloudflare WAF</a>. Review the available <a href="/ruleset-engine/rules-language/fields/reference/?field-category=mTLS&amp;field-category=SSL/TLS"><code>cf.tls_*</code></a> fields.</p>
<p>Example WAF Custom Rule with action block:</p>
<p><img src="/assets/upstream/images/learning-paths/mtls/configure-waf-custom-rule.png" alt="Example expression for configure a WAF Custom Rule with action block " /></p>
<pre><code class="language-txt">(http.host in {&quot;mtls.example.com&quot; &quot;mtls2.example.com&quot;} and (not cf.tls_client_auth.cert_verified or cf.tls_client_auth.cert_revoked))&#10;</code></pre>
<p>This expression will check if the request is coming from one of the hostnames and will block the request if the Client Certificate is either not verified or revoked.</p>
<p>Another example WAF Custom Rule with action block, using the <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_fingerprint_sha256/"><code>cf.tls_client_auth.cert_fingerprint_sha256</code></a> field, for a specific Client Certificate (replace <code>ADD_STRING_OF_CLIENT_CERT_SHA256_FINGERPRINT</code>):</p>
<p><img src="/assets/upstream/images/learning-paths/mtls/waf-client-certificates-fingerprint.png" alt="Example expression of a WAF Custom Rule with action block using the cf.tls_client_auth.cert_fingerprint_sha256 field" /></p>
<pre><code class="language-txt">(http.request.uri.path in {&quot;/headers&quot;} and http.host in {&quot;mtls.example.com&quot; &quot;mtls2.example.com&quot;} and not cf.tls_client_auth.cert_verified and cf.tls_client_auth.cert_fingerprint_sha256 ne &quot;ADD_STRING_OF_CLIENT_CERT_SHA256_FINGERPRINT&quot;)&#10;</code></pre>
<p>Here is another example of a WAF custom rule to associate a serial number with a hostname:</p>
<p><img src="/assets/upstream/images/learning-paths/mtls/waf-custom-rule.png" alt="Example expression of a WAF Custom Rule to associate a serial number with a hostname" /></p>
<pre><code class="language-txt">(http.host in {&quot;mtls.example.com&quot; &quot;mtls2.example.com&quot;} and cf.tls_client_auth.cert_serial ne &quot;ADD_STRING_OF_CLIENT_CERT_SERIAL&quot;)&#10;</code></pre>
<p>This expression will check for a specific <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_serial/">Client Certificate serial number</a> linked to specific hostnames, allowing for more granular control.</p>
<h2 id="rate-limiting-by-client-certificates">Rate Limiting by Client Certificates</h2>
<p>By enabling <a href="/ssl/client-certificates/forward-a-client-certificate/#cloudflare-api">forwarding a certificate</a> via the Cloudflare API, every request of an mTLS connection will include the following headers:</p>
<ul>
<li><code>Cf-Client-Cert-Der-Base64</code> (raw certificate in DER format, encoded as base64)</li>
<li><code>Cf-Client-Cert-Sha256</code> (SHA256 fingerprint of the certificate)</li>
</ul>
<p>The header <code>Cf-Client-Cert-Sha256</code> can be used within the <a href="/waf/rate-limiting-rules/parameters/#with-the-same-characteristics">Rate Limiting characteristics</a> &quot;Header value of&quot;.</p>
<p>Example <a href="/waf/rate-limiting-rules/">Rate Limiting Rule</a>:</p>
<p><img src="/assets/upstream/images/learning-paths/mtls/rate-limiting-rule.png" alt="Example exmpression of a rate limiting rule from the Cloudflare dashboard" /></p>
<pre><code class="language-txt">(http.host in {&quot;mtls.example.com&quot; &quot;mtls2.example.com&quot;} and cf.tls_client_auth.cert_verified)&#10;&#10;With the same characteristics...&#10;&quot;Header value of&quot;: &quot;Cf-Client-Cert-Sha256&quot;&#10;</code></pre>
<h2 id="cloudflare-api-shield">Cloudflare API Shield</h2>
<p>In addition to mTLS, customers can purchase <a href="/api-shield/">API Shield</a> features, such as API Discovery, API Routing, Volumetric Abuse Detection, Sequence Mitigation, JWT Validation, Schema Validation, and more.</p>
<h2 id="cloudflare-workers">Cloudflare Workers</h2>
<p>Cloudflare Workers can provide details around the Client Certificate, such as returning information via headers to the client or to the origin server. Learn more in the <a href="/learning-paths/mtls/mtls-workers/">mTLS with Workers section</a> below.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9834.md")
</aside>
