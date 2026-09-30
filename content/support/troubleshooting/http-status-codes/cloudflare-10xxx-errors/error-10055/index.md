<h2 id="error-10055-query-string-settings-incompatible-with-redirect-target-url">Error 10055: Query string settings incompatible with redirect target URL</h2>
<p>This error indicates a conflict between the <strong>Preserve query string</strong> option and the query string in the redirect target URL.</p>
<h3 id="common-causes">Common causes</h3>
<p>This error occurs when you enable the <strong>Preserve query string</strong> option of a URL redirect, but also provide a query string in the redirect target URL. In this case, the URL redirect would have conflicting configuration on how to handle the query string of incoming requests.</p>
<h3 id="resolution">Resolution</h3>
<p>To resolve this issue, either disable the <strong>Preserve query string</strong> option in the URL redirect or remove the query string component from the redirect target URL to eliminate the conflict.</p>
