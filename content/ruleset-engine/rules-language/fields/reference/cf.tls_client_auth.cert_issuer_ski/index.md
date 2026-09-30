<h1 id="cf-tls-client-auth-cert-issuer-ski">cf.tls_client_auth.cert_issuer_ski</h1>

**Data type:** String

<p>The Subject Key Identifier (SKI) of the direct issuer of the mTLS client certificate.</p>

<p>This field defaults to <code>&quot;&quot;</code> if the connection does not use <a href="/ssl/client-certificates/enable-mtls/">mTLS authentication</a>.</p>

**Example value:**

```txt
"8204924CF49D471E855862706D889F58F6B784D3"
```

<h2 id="categories">Categories</h2>

- Request
- mTLS

**Keywords:** request, ssl, mtls, client, visitor

