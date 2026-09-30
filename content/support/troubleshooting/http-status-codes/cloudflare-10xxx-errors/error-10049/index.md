<h2 id="error-10049-invalid-scheme-in-redirect-source-url">Error 10049: Invalid scheme in redirect source URL</h2>
<p>This error indicates that the source URL's scheme is invalid.</p>
<h3 id="common-causes">Common causes</h3>
<p>This error occurs when the source URL of a URL redirect has an invalid scheme, which may be due to a misspelled or unsupported scheme or because the scheme is missing or improperly formatted.</p>
<h3 id="resolution">Resolution</h3>
<p>Review the source URL and ensure that it uses one of the supported schemes: <code>http</code>, <code>https</code>, or empty (no scheme information, which means that it applies to both schemes). Refer to <a href="/rules/url-forwarding/bulk-redirects/reference/url-components/">Supported URL components in Bulk Redirects</a> for details on the supported URL components for redirect source URLs.</p>
