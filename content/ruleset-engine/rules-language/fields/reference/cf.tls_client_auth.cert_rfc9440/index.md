<h1 id="cf-tls-client-auth-cert-rfc9440">cf.tls_client_auth.cert_rfc9440</h1>

**Data type:** String

<p>The mTLS client certificate encoded as a Structured Fields Byte Sequence per <a href="https://datatracker.ietf.org/doc/html/rfc9440">RFC 9440</a>.</p>

<p>Contains the DER-encoded, Base64-wrapped client leaf certificate formatted as an <a href="https://datatracker.ietf.org/doc/html/rfc9440#name-client-cert-http-header-fie">RFC 9440</a> <code>Client-Cert</code> HTTP header value. The value is a Structured Fields Byte Sequence (the Base64 data prefixed and suffixed by <code>:</code>).</p>
<p>This field is populated regardless of the certificate validation result. Before using this value, verify the certificate status by checking <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_verified/"><code>cf.tls_client_auth.cert_verified</code></a> and <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_revoked/"><code>cf.tls_client_auth.cert_revoked</code></a>.</p>
<p>Returns <code>&quot;&quot;</code> if no client certificate was presented or if the encoded value exceeds the 10 KiB size limit. Refer to <a href="/ruleset-engine/rules-language/fields/reference/cf.tls_client_auth.cert_rfc9440_too_large/"><code>cf.tls_client_auth.cert_rfc9440_too_large</code></a> to distinguish between these cases.</p>
<p>This field defaults to <code>&quot;&quot;</code> if the connection does not use <a href="/ssl/client-certificates/enable-mtls/">mTLS authentication</a>.</p>

**Example value:**

```txt
":MIIBqDCCAU6g......:"
```

<h2 id="categories">Categories</h2>

- Request
- mTLS

**Keywords:** request, ssl, mtls, client, visitor, rfc9440, cert, chain

