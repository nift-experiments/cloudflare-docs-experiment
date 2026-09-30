<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3273.md")
</aside>
<div class="nb-glossary-definition"><p><a href="https://www.cloudflare.com/learning/access-management/what-is-mutual-tls/">Mutual TLS (mTLS)</a> authentication is a common security practice that uses client certificates to ensure traffic between client and server is bidirectionally secure and trusted. mTLS also allows requests that do not authenticate via an identity provider — such as Internet-of-things (IoT) devices — to demonstrate they can reach a given resource.</p></div>
<p>Use mTLS when you need to verify the identity of API clients, such as mobile applications, IoT devices, or services that connect to your API.</p>
<p><img src="/assets/upstream/images/api-shield/api-shield-call-sequence.png" alt="mTLS sequence diagram" /></p>
<p>mTLS also supports <a href="https://grpc.io/docs/what-is-grpc/introduction/">gRPC</a>-based APIs, which use binary formats such as protocol buffers rather than JSON.</p>
<h2 id="setup">Setup</h2>
<p>To set up mTLS for one or more hosts using the dashboard, refer to <a href="/api-shield/security/mtls/configure/">Configure mTLS</a>.</p>
<h2 id="availability">Availability</h2>
<p>All Cloudflare plans can set up mTLS with a Cloudflare-managed certificate authority (CA). Enterprise customers can <a href="/ssl/client-certificates/byo-ca/">upload up to five non-Cloudflare CAs</a>. For higher limits, contact your account team.</p>
<h2 id="limitations">Limitations</h2>
<p>When using Yubikeys, the browser may prompt for unlocking the key due to a problem in Yubikey's PKCS#11 library.</p>
