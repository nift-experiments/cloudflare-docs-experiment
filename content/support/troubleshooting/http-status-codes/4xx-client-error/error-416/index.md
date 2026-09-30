<h2 id="416-range-not-satisfiable">416 Range Not Satisfiable</h2>
<p>The <code>416 Range Not Satisfiable</code> status code indicates that the server cannot fulfill the byte range specified in the request's <code>Range</code> header.</p>
<p>For more details, refer to <a href="https://www.rfc-editor.org/rfc/rfc9110.html#name-416-range-not-satisfiable">RFC 9110</a>.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>This error can occur when every requested byte range falls outside the selected resource. It can also occur when the server does not support the requested range unit.</p>
<p>A <code>416</code> response to a byte-range request should include a <code>Content-Range</code> header. The header uses <code>bytes */&lt;LENGTH&gt;</code>, where <code>&lt;LENGTH&gt;</code> is the current resource length.</p>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<p>Cloudflare can return a <code>416</code> response when the origin rejects a range request. Cloudflare can also generate this response when a cached resource cannot satisfy the requested range.</p>
<p>Cloudflare does not cache <code>416</code> responses returned by an origin server. This applies even when the response includes explicit cache directives or a matching Cache Rule sets a <a href="/cache/how-to/configure-cache-status-code/">Status Code TTL</a> for <code>416</code>. This behavior prevents one unsatisfiable range request from affecting later requests for the same URL.</p>
