<h2 id="error-1040-invalid-request-rewrite-header-modification-not-allowed">Error 1040: Invalid request rewrite (header modification not allowed)</h2>
<p>This error indicates that an attempt was made to modify a restricted HTTP header.</p>
<h3 id="common-cause">Common cause</h3>
<p>You are trying to modify an HTTP header that Request Header Transform Rules cannot change.</p>
<h3 id="resolution">Resolution</h3>
<p>Make sure you are not trying to modify one of the <a href="/rules/transform/request-header-modification/#important-remarks">reserved HTTP request headers</a>.</p>
