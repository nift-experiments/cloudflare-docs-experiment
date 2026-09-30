<h1 id="cf-tls-client-auth-cert-chain-rfc9440-too-large">cf.tls_client_auth.cert_chain_rfc9440_too_large</h1>

**Data type:** Boolean

<p>Returns <code>true</code> when the RFC 9440 encoded client certificate chain exceeds the 16 KiB size limit.</p>

<p>When <code>true</code>, <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_chain_rfc9440/"><code>cf.tls_client_auth.cert_chain_rfc9440</code></a> contains an empty string instead of the encoded certificate chain.</p>
<p>This field defaults to <code>false</code> if the connection does not use <a href="/ssl/client-certificates/enable-mtls/">mTLS authentication</a>.</p>

<h2 id="categories">Categories</h2>

- Request
- mTLS

**Keywords:** request, ssl, mtls, client, visitor, rfc9440, cert, chain, too large, error

