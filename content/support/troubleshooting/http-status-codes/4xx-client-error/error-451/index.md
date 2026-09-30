<h2 id="451-unavailable-for-legal-reason">451 Unavailable For Legal Reason</h2>
<p>The <code>451</code> status code indicates that the server cannot deliver the requested resource due to legal actions or restrictions.</p>
<p>For more details, refer to <a href="https://tools.ietf.org/html/rfc7725">RFC 7725</a>.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>This occurs when access to a resource is blocked due to court orders, copyright claims, or other legal demands. Typically search engines (for example, Google) and ISP (for example, ATT) are the ones affected by this response code, rather than the origin server itself. The server should include an explanation in the response body, detailing the legal demand or reason for the restriction.</p>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<p>Cloudflare may pass through a <code>451</code> response from the origin server if the requested resource is legally restricted.</p>
