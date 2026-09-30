<h1 id="cf-tls-client-random">cf.tls_client_random</h1>

**Data type:** String

<p>The value of the 32-byte random value provided by the client in a <a href="https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake">TLS handshake</a>, encoded in Base64.</p>

<p>For more details, refer to <a href="https://datatracker.ietf.org/doc/html/rfc8446#section-4.1.2">RFC 8446</a>.</p>

**Example value:**

```txt
"YWJjZA=="
```

<h2 id="categories">Categories</h2>

- Request
- SSL/TLS

**Keywords:** request, ssl, tls, client, visitor

