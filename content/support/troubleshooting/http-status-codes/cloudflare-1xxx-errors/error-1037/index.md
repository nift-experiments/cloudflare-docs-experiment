<h2 id="error-1037-invalid-rewrite-rule-failed-to-evaluate-expression">Error 1037: Invalid rewrite rule (failed to evaluate expression)</h2>
<p>This error indicates that the rewrite rule expression could not be evaluated.</p>
<h3 id="common-cause">Common cause</h3>
<p>There are several causes for this error, but it can mean that one expression element contained an undefined value when it was evaluated.</p>
<p>For example, you get a 1037 error when using the following URL rewrite dynamic expression and the <code>X-Source</code> header is not included in the request:</p>
<p><code>http.request.headers[&quot;x-source&quot;][0]</code></p>
<h3 id="resolution">Resolution</h3>
<p>Make sure that all the elements of your rewrite expression are defined. For example, if you are referring to a header value, ensure the header is set.</p>
