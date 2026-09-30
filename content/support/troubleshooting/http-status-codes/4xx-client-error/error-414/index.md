<h2 id="414-uri-too-long">414 URI Too Long</h2>
<p>The <code>414 URI Too Long</code> status code indicates that the server refuses to process the request because the URI provided by the client is excessively long.</p>
<p>For more details, refer to <a href="https://tools.ietf.org/html/rfc7231">RFC 7231</a>.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>For example, if a client is attempting a <code>GET</code> request with an unusually long URI, such as one containing an excessive number of query parameters, after a <code>POST</code>, this could be seen as a security risk and a <code>414</code> is generated.</p>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<p>Cloudflare will generate a <code>414</code> response if the URI length exceeds 32KB.</p>
