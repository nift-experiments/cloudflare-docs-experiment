<h2 id="410-gone">410 Gone</h2>
<p>When a resource is intentionally and permanently removed, servers use the <code>410 Gone</code> status code to inform clients that the resource is no longer available.
In this case:</p>
<pre><code>- The server suggests that links referencing the resource should be removed.&#10;- The server is not obligated to use this status code instead of a `404` response, nor is it required to maintain this response for any specific period of time.&#10;</code></pre>
<p>For more details, refer to <a href="https://tools.ietf.org/html/rfc7231">RFC 7231</a>.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>This status is commonly applied to deprecated content, such as outdated pages or discontinued products.</p>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<p>Cloudflare does not generate <code>410</code> for customer websites, we only proxy the request from the origin server. If you encounter a <code>410</code> error on a Cloudflare-powered site, the issue lies with the origin server. In such cases, contact your hosting provider for assistance.</p>
