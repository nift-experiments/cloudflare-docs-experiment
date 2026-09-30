<h2 id="error-10050-invalid-redirect-source-url-with-user-info">Error 10050: Invalid redirect source URL with user info</h2>
<p>This error indicates that the source URL includes unsupported user information.</p>
<h3 id="common-causes">Common causes</h3>
<p>This error occurs when the source URL of a URL redirect includes a user info component (for example, <code>https://user:password@example.com</code>), which is not supported.</p>
<h3 id="resolution">Resolution</h3>
<p>You need to remove the user information component from the redirect source URL. Refer to <a href="/rules/url-forwarding/bulk-redirects/reference/url-components/">Supported URL components in Bulk Redirects</a> for details on the supported URL components for redirect source URLs.</p>
