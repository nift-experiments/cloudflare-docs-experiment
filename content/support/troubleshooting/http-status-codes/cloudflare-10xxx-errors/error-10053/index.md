<h2 id="error-10053-invalid-redirect-source-url-with-query-string">Error 10053: Invalid redirect source URL with query string</h2>
<p>This error indicates that the source URL contains an unsupported query string component.</p>
<h3 id="common-causes">Common causes</h3>
<p>This error occurs when the source URL of a URL redirect includes a query string component, which is not supported. Possible causes include copying a URL with query parameters, misconfiguration during setup, or attempting to redirect based on query parameters instead of the path.</p>
<h3 id="resolution">Resolution</h3>
<p>Remove the query string from the redirect source URL. Refer to <a href="/rules/url-forwarding/bulk-redirects/reference/url-components/">Supported URL components in Bulk Redirects</a> for details on the supported URL components for redirect source URLs.</p>
