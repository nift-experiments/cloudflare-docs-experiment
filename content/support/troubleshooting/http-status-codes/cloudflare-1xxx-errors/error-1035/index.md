<h2 id="error-1035-invalid-request-rewrite-invalid-uri-path">Error 1035: Invalid request rewrite (invalid URI path)</h2>
<p>This error indicates an invalid URI path in a request rewrite.</p>
<h3 id="common-cause">Common cause</h3>
<p>The value or expression of your rewritten URI path is not valid.</p>
<p>This error also occurs when the destination of the URL rewrite is a path under <code>/cdn-cgi/</code>.</p>
<h3 id="resolution">Resolution</h3>
<p>Make sure that the rewritten URI path is not empty and it starts with a <code>/</code> (slash) character.</p>
<p>For example, the following URI path rewrite expression is not valid:</p>
<p><code>concat(lower(ip.src.country), http.request.uri.path)</code></p>
<p>To fix the expression above, add a <code>/</code> prefix:</p>
<p><code>concat(&quot;/&quot;, lower(ip.src.country), http.request.uri.path)</code></p>
