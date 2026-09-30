<h2 id="406-not-acceptable">406 Not Acceptable</h2>
<p>The <code>406 Not Acceptable</code> status code indicates that the requested resource is not available in a format that adheres to the content negotiation headers specified by the client (for example, <code>Accept-Charset</code> or <code>Accept-Language</code>).</p>
<p>For more details, refer to <a href="https://tools.ietf.org/html/rfc7231">RFC 7231</a>.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>For example, if a client requests content in a specific language or character set that the server does not support, this error will be generated. To avoid returning a <code>406</code> error, the server can instead serve the less preferred method to the client's User-Agent, rather than rejecting the request.</p>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<p>Cloudflare does not generate <code>406</code> errors directly but can proxy these responses from the origin server. If content negotiation issues occur, they are typically related to configurations at the origin server, such as language or character set settings.</p>
