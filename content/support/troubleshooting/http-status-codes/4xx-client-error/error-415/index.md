<h2 id="415-unsupported-media-type">415 Unsupported Media Type</h2>
<p>The <code>415 Unsupported Media Type</code> status code indicates that the server refuses to process the request because the format of the payload is not supported. One way to identify and fix this issue would be to look at the <code>Content-Type</code> or <code>Content-Encoding</code> headers sent in the client's request.</p>
<p>For more details, refer to <a href="https://tools.ietf.org/html/rfc7231">RFC 7231</a>.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>This may be triggered by submitting a file type or format that the server is not configured to handle, such as uploading an unsupported image or document format, may also trigger this error.</p>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<p>Cloudflare typically passes this response from the origin server if it encounters an unsupported media type in the client's request payload.</p>
