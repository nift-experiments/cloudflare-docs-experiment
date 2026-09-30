<h2 id="417-expectation-failed">417 Expectation Failed</h2>
<p>The <code>417 Expectation Failed</code> status code indicates that the server could not meet the requirements specified in the <code>Expect</code> header of the client's request.</p>
<p>For more details, refer to <a href="https://tools.ietf.org/html/rfc7231">RFC 7231</a>.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>Some clients use the <code>Expect</code> header, such as <code>Expect: 100-continue</code>, to verify if the server is ready to receive a large payload, and if the server cannot fulfill this expectation, it returns a 417 response. Similarly, a server may reject a request with this error if the client includes an <code>Expect</code> header with unsupported or invalid values.</p>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<p>Cloudflare typically forwards this response from the origin server if it encounters an issue related to unsupported or unfulfilled <code>Expect</code> headers in the client's request.</p>
