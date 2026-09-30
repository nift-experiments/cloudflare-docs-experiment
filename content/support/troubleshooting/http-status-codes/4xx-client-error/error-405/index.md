<h2 id="405-method-not-allowed">405 Method Not Allowed</h2>
<p>The 405 Method Not Allowed status code indicates that the origin server recognizes the requested resource but does not support the HTTP method used in the request.</p>
<p>For more details, refer to <a href="https://tools.ietf.org/html/rfc7231">RFC 7231</a>.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>This error typically occurs when the client uses an unsupported HTTP method to interact with a specific resource. The origin server must include an <code>Allow</code> header in the response, which lists the HTTP methods supported for that resource.</p>
<p>For example, attempting a <code>POST</code> request on a resource that is unchangeable and only supports <code>GET</code> requests will result in a <code>405</code> error.</p>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<p>Cloudflare does not directly generate <code>405</code> errors. These errors are returned by the origin server when it does not allow the HTTP method used in the request. If you encounter a <code>405</code> error, review the configuration of your origin server to ensure the correct methods are enabled for the resource in question.</p>
