<h2 id="411-length-required">411 Length Required</h2>
<p>The <code>411 Length Required</code> status code indicates that the client did not specify the <code>Content-Length</code> of the request body in the headers, and this information is required to obtain the resource. The client may resend the request after adding the required header field.</p>
<p>For more details, refer to <a href="https://tools.ietf.org/html/rfc7231">RFC 7231</a>.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>This status code can occur in various scenarios, such as when a client sends an API request without the required <code>Content-Length</code> header, when uploading a file where the server needs the header to allocate resources, or when proxies or legacy systems enforce strict HTTP compliance. In each case, the server or intermediary requires the <code>Content-Length</code> header to process the request properly.</p>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<p>Cloudflare does not generate <code>411</code> for customer websites, we only proxy the request from the origin server. If you encounter a <code>411</code> error on a Cloudflare-powered site, the issue lies with the origin server. In such cases, contact your hosting provider for assistance.</p>
