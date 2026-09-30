<h2 id="408-request-timeout">408 Request Timeout</h2>
<p>The <code>408 Request Timeout</code> status code indicates that the origin server did not receive the complete request within a reasonable time frame and does not wish to continue waiting for the connection. This response is not commonly used, as servers often prefer to use the &quot;close&quot; connection option to terminate idle connections</p>
<p>For more details, refer to <a href="https://tools.ietf.org/html/rfc7231">RFC 7231</a>.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>This error typically occurs when a client fails to send a complete request within the server's timeout period. Common scenarios include slow network connections, server overload or client-side delays to complete the request.</p>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<p>If a <code>408</code> error occurs on a Cloudflare-powered site, it is most often being proxied from the origin. In these cases, it is essential to review the origin server's timeout settings and ensure that the server is not overloaded. Additionally, verify that the client's Internet connection is stable and that the request is being sent promptly.</p>
<p>Cloudflare may return a <code>408</code> error response if public client requests to our network exceed certain internally-defined timeouts. These timeouts are configured as a protective measure and cannot be changed.</p>
