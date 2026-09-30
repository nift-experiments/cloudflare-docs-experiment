<h2 id="error-10051-missing-authority-in-redirect-source-url">Error 10051: Missing authority in redirect source URL</h2>
<p>This error indicates that the source URL is missing a required authority component.</p>
<h3 id="common-causes">Common causes</h3>
<p>This error occurs when the source URL of a URL redirect does not include an authority component (for example, <code>http:///path</code>, without a hostname), which is mandatory.</p>
<h3 id="resolution">Resolution</h3>
<p>Add an authority component to the redirect source URL (for example, include a hostname). Refer to <a href="/rules/url-forwarding/bulk-redirects/reference/url-components/">Supported URL components in Bulk Redirects</a> for details on the required URL components for redirect source URLs.</p>
