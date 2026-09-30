<h2 id="error-1041-invalid-request-rewrite-invalid-header-value">Error 1041: Invalid request rewrite (invalid header value)</h2>
<p>This error indicates that the header value is not valid.</p>
<h3 id="common-causes">Common causes</h3>
<p>The added/modified header value is too long or it contains characters that are not allowed.</p>
<h3 id="resolution">Resolution</h3>
<ul>
<li>Use a shorter value or expression to define the header value.</li>
<li>Remove the characters that are not allowed. Refet to <a href="/rules/transform/request-header-modification/reference/header-format/">Format of HTTP request header names and values</a> in Developer Docs for more information on the allowed characters.</li>
</ul>
