<h1 id="cf-tls-client-auth-cert-verified">cf.tls_client_auth.cert_verified</h1>

**Data type:** Boolean

<p>Returns <code>true</code> when an mTLS client presents a valid client certificate.</p>

<p>Also returns <code>true</code> when a client presents a valid certificate that was revoked (refer to <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_revoked/"><code>cf.tls_client_auth.cert_revoked</code></a>).</p>
<p>This field defaults to <code>false</code> if the connection does not use <a href="/ssl/client-certificates/enable-mtls/">mTLS authentication</a>.</p>

<h2 id="categories">Categories</h2>

- Request
- mTLS

**Keywords:** request, ssl, mtls, client, visitor

