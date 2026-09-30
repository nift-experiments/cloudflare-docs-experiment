<h1 id="cf-tls-client-auth-cert-revoked">cf.tls_client_auth.cert_revoked</h1>

**Data type:** Boolean

<p>Indicates whether the mTLS client presented a valid but revoked client certificate.</p>

<p>When <code>true</code>, the <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_verified/"><code>cf.tls_client_auth.cert_verified</code></a> field is also <code>true</code>.</p>
<p>This field defaults to <code>false</code> if the connection does not use <a href="/ssl/client-certificates/enable-mtls/">mTLS authentication</a>.</p>

<h2 id="categories">Categories</h2>

- Request
- mTLS

**Keywords:** request, ssl, mtls, client, visitor

