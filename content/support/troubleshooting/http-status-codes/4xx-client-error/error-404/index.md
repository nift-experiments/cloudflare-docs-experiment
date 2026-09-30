<h2 id="404-not-found">404 Not Found</h2>
<p>The <code>404 Not Found</code> status code indicates that the origin server was unable to locate the requested resource. Typically, this means the host server could not find the resource. For a more permanent version of this error, the 410 Gone status code should be used.</p>
<p>For more details, refer to <a href="https://tools.ietf.org/html/rfc7231">RFC 7231</a>.</p>
<h3 id="common-use-cases">Common use cases</h3>
<p>These errors typically occur when someone mistypes a URL on your site, when there is a broken link from another page, when a page that previously existed is moved or removed, or there is an error when a search engine indexes your site.</p>
<p>These errors typically account for approximately 3% of total page views for a typical site. However, they often go untracked by traditional analytics platforms, such as Google Analytics. To improve user experience, website owners usually implement a custom 404 page to be displayed when this error is generated.</p>
<h3 id="cloudflare-specific-information">Cloudflare-specific information</h3>
<p>Cloudflare does not generate <code>404s</code> for customer websites, we only proxy the request from the origin server. If you encounter a <code>404</code> error on a Cloudflare-powered site, the issue lies with the origin server. In such cases, contact your hosting provider for assistance.</p>
