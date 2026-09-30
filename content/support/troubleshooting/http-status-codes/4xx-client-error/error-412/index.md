<h2 id="412-precondition-failed">412 Precondition Failed</h2>
<p>The <code>412 Precondition Failed</code> status code indicates that the server denies the request because the resource does not meet the conditions specified by the client.</p>
<p>For more details, refer to <a href="https://tools.ietf.org/html/rfc7232">RFC 7232</a>.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>One common use case for the <code>412 Precondition Failed</code> status code is version control. For example, a client modifying an existing resource may set the <code>If-Unmodified-Since</code> header to ensure the resource has not been changed since the client downloaded it for editing. If another client edits the resource after the specified date but before the original client uploads their changes, the server will return a <code>412</code> response to prevent overwriting the newer updates.</p>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<p>Cloudflare may serve this response: for more information please refer to <a href="/cache/reference/etag-headers/">ETag Headers</a>.</p>
