<h2 id="error-10052-invalid-redirect-source-url-with-port">Error 10052: Invalid redirect source URL with port</h2>
<p>This error indicates that the source URL includes an unsupported port.</p>
<h3 id="common-causes">Common causes</h3>
<p>This error occurs when the source URL of a URL redirect includes a port (for example, <code>https://example.com:8081</code>), which is not supported. Possible causes include using a custom or non-standard port, copying a URL from another environment that includes a port, or mistakenly using a development or testing URL.</p>
<h3 id="resolution">Resolution</h3>
<p>Remove the port from the redirect source URL. Refer to <a href="/rules/url-forwarding/bulk-redirects/reference/url-components/">Supported URL components in Bulk Redirects</a> for details on the supported URL components for redirect source URLs.</p>
