<h2 id="error-10060-missing-scheme-in-redirect-target-url">Error 10060: Missing scheme in redirect target URL</h2>
<p>This error indicates that the target URL is missing a scheme.</p>
<h3 id="common-causes">Common causes</h3>
<p>This error occurs when the target URL of a URL redirect does not include a scheme, which is mandatory. This could have happened due to a typo or the URL was copied from a source that did not include the scheme.</p>
<h3 id="resolution">Resolution</h3>
<p>Review the target URL of the URL redirect and ensure that it contains a scheme (for example, <code>https</code>). Refer to <a href="/rules/url-forwarding/bulk-redirects/reference/url-components/">Supported URL components in Bulk Redirects</a> for details on the required URL components for redirect target URLs.</p>
