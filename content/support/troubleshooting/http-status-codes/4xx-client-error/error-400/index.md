<h2 id="400-bad-request">400 Bad Request</h2>
<p>This error indicates that the client sent a request to the server that could not be understood or processed due to issues with the request itself.</p>
<p>For more information, refer to <a href="https://tools.ietf.org/html/rfc7231">RFC 7231</a>.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>A <code>400 Bad Request</code> error occurs due to client-side issues, such as malformed request syntax, invalid request content, message framing problems, or deceptive request routing.
For example:</p>
<ul>
<li>If the request contains a special character that is not properly <a href="https://en.wikipedia.org/wiki/Percent-encoding">URL Encoded (or percent-encoded)</a>, an <code>HTTP Error 400</code> will be returned.</li>
<li>If the request contains both <code>Content Length</code> and <code>Transfer Encoding</code> chunked, these two framing methods contradict each other. <code>Content Length</code> declares a fixed size body, while chunked encoding declares a streamed body with no known size. <a href="https://datatracker.ietf.org/doc/html/rfc7230#section-3.3.3">RFC 7230 section 3.3.3</a> states that when <code>Transfer Encoding</code> is present, the <code>Content Length</code> header must be ignored and a request that includes both is considered malformed. This creates ambiguity in body framing and can enable request smuggling if different systems parse the boundary differently. Cloudflare follows the RFC and an <code>HTTP Error 400</code> will be returned.</li>
</ul>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<p>If you encounter an HTTP error while using the <a href="/api/">Cloudflare API</a>, make sure that you are using the correct syntax, parameters, and body for your API call.</p>
