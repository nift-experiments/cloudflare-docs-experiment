<h1 id="cf-tls-client-auth-cert-not-before">cf.tls_client_auth.cert_not_before</h1>

**Data type:** String

<p>The mTLS client certificate is not valid before this date.</p>

<p>This field defaults to <code>&quot;&quot;</code> if the connection does not use <a href="/ssl/client-certificates/enable-mtls/">mTLS authentication</a>.</p>

**Example value:**

```txt
"Mar 21 13:35:00 2022 GMT"
```

<h2 id="categories">Categories</h2>

- Request
- mTLS

**Keywords:** request, ssl, mtls, client, visitor

