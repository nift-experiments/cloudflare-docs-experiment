<h2 id="407-authentication-required">407 Authentication Required</h2>
<p>The <code>407 Proxy Authentication Required</code> status code indicates that the client did not provide the necessary authentication credentials to access the requested resource through a proxy server.
For more details, refer to <a href="https://tools.ietf.org/html/rfc7235">RFC 7235</a>.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>This error typically occurs in environments where a proxy server is used as an intermediary between the client and the target server. To resolve this, the client must include the appropriate <code>Proxy-Authorization</code> header in the request with valid credentials.</p>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<p>Cloudflare does not generate <code>407</code> errors but proxies them from the origin server or an upstream proxy. If a <code>407</code> error occurs on a Cloudflare-powered site, review the origin server's proxy configuration to ensure authentication requirements are properly set, and verify that the client is providing the required credentials.</p>
