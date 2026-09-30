<h2 id="error-10054-invalid-redirect-source-url-with-fragment">Error 10054: Invalid redirect source URL with fragment</h2>
<p>This error indicates that the source URL includes an unsupported fragment component.</p>
<h3 id="common-causes">Common causes</h3>
<p>This error occurs when the source URL of a URL redirect includes a fragment component (for example, <code>https://example.com/search/#fragment</code>). Fragment components are not part of an HTTP request; they are an indication for the browser to scroll to a specific location once the page has loaded. Possible causes of this error include copying a URL with a fragment from a browser or external source, or inadvertently adding a fragment during URL configuration or editing.</p>
<h3 id="resolution">Resolution</h3>
<p>Remove the fragment from the redirect source URL. Refer to <a href="/rules/url-forwarding/bulk-redirects/reference/url-components/">Supported URL components in Bulk Redirects</a> for details on the supported URL components for redirect source URLs.</p>
