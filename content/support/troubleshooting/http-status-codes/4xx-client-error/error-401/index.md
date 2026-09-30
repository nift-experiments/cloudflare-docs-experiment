<h2 id="401-unauthorized">401 Unauthorized</h2>
<p>This error indicates that the request was not sent with the proper authentication credentials. The server requires authentication to process the request.</p>
<p>For more details, refer to <a href="https://tools.ietf.org/html/rfc7235">RFC 7235</a>.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>A <code>401 Unauthorized</code> error occurs when the client fails to provide valid authentication credentials. The server responds with at least one challenge in the form of a <code>WWW-Authenticate</code> header field, as outlined in <a href="https://datatracker.ietf.org/doc/html/rfc7235#section-4.1">section 4.1</a>.</p>
<p>If the client resends the request with the same credentials and the challenge remains unchanged, the server may return an entity to assist the client in identifying the correct credentials needed.</p>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<p>When encountering a <code>401</code> error while using the Cloudflare API, ensure that you are providing the correct authentication credentials (for example, <a href="/fundamentals/api/get-started/create-token/">API tokens</a> or <a href="/fundamentals/api/get-started/ca-keys/">keys</a>). Double-check that the credentials are active and properly formatted. If the error persists, refer to the <code>WWW-Authenticate</code> header in the response for guidance on resolving the issue.</p>
