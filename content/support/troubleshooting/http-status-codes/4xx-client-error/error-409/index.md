<h2 id="409-conflict">409 Conflict</h2>
<p>The <code>409 Conflict</code> status code indicates that the request could not be completed due to a conflict with the current state of the target resource.</p>
<p>For more details, refer to <a href="https://tools.ietf.org/html/rfc7231">RFC 7231</a>.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>This error typically happens with a <code>PUT</code> request when multiple clients are attempting to edit the same resource. To solve this issue:</p>
<pre><code>- The server should generate a payload that includes enough information for the client to recognize the source of the conflict.&#10;- Clients should retry the request again after resolving the conflict.&#10;</code></pre>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<p>Cloudflare will return a 409 response for a <a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1001/">Error 1001: DNS Resolution Error</a>.</p>
