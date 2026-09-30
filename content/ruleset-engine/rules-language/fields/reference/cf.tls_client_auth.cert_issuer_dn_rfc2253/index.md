<h1 id="cf-tls-client-auth-cert-issuer-dn-rfc2253">cf.tls_client_auth.cert_issuer_dn_rfc2253</h1>

**Data type:** String

<p>The Distinguished Name (DN) of the Certificate Authority (CA) that issued the mTLS client certificate in <a href="https://datatracker.ietf.org/doc/html/rfc2253">RFC 2253</a> format.</p>

<p>This field defaults to <code>&quot;&quot;</code> if the connection does not use <a href="/ssl/client-certificates/enable-mtls/">mTLS authentication</a>.</p>

**Example value:**

```txt
"CN=Access Testing CA,OU=TX,O=Access Testing,L=Austin,ST=Texas,C=US"
```

<h2 id="categories">Categories</h2>

- Request
- mTLS

**Keywords:** request, ssl, mtls, client, visitor

