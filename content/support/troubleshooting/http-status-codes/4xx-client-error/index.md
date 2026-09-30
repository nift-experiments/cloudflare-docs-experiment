<p><code>4xx</code> codes are error responses that indicate an issue on the client's end, potentially due to a network problem.</p>
<ul>
<li><code>4xx</code> codes can be used as a response to any request method.</li>
<li>The origin server should include an explanation, which should be displayed by the User-Agent, except in the case of a <code>HEAD</code> request.</li>
<li><a href="/waf/custom-rules/">Custom rules</a> can return any response code in the range of <code>400–499</code> on your HTML page if the site owner has created a rule with the <em>Block</em> action and configured a custom response code. For more details, refer to <a href="/waf/custom-rules/create-dashboard/#configure-a-custom-response-for-blocked-requests">custom response</a>.</li>
</ul>
<h2 id="log-explorer">Log Explorer</h2>
<p><a href="/log-explorer/">Log Explorer</a> provides access to Cloudflare logs with all the context available within the Cloudflare platform.
You can monitor security and performance issues with custom dashboards or investigate and troubleshoot issues with log search.
Log explorer <a href="/log-explorer/log-search/">allows you to build queries</a> filtering for a specific <a href="/fundamentals/reference/cloudflare-ray-id/">Ray ID</a>, which can be useful to investigate HTTP Errors.</p>
<h2 id="400-bad-request">400 Bad Request</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-400/">Error 400</a> page.</p>
<h2 id="401-unauthorized">401 Unauthorized</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-401/">Error 401</a> page.</p>
<h2 id="402-payment-required">402 Payment Required</h2>
<p>The <code>402 Payment Required</code> status code is reserved for future use and is not yet implemented according to the standards outlined in <a href="https://tools.ietf.org/html/rfc7231">RFC 7231</a>.</p>
<h2 id="403-forbidden">403 Forbidden</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-403/">Error 403</a> page.</p>
<h2 id="404-not-found">404 Not Found</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-404/">Error 404</a> page.</p>
<h2 id="405-method-not-allowed">405 Method Not Allowed</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-405/">Error 405</a> page.</p>
<h2 id="406-not-acceptable">406 Not Acceptable</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-406/">Error 406</a> page.</p>
<h2 id="407-authentication-required">407 Authentication Required</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-407/">Error 407</a> page.</p>
<h2 id="408-request-timeout">408 Request Timeout</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-408/">Error 408</a> page.</p>
<h2 id="409-conflict">409 Conflict</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-409/">Error 409</a> page.</p>
<h2 id="410-gone">410 Gone</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-410/">Error 410</a> page.</p>
<h2 id="411-length-required">411 Length Required</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-411/">Error 411</a> page.</p>
<h2 id="412-precondition-failed">412 Precondition Failed</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-412/">Error 412</a> page.</p>
<h2 id="413-payload-too-large">413 Payload Too Large</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-413/">Error 413</a> page.</p>
<h2 id="414-uri-too-long">414 URI Too Long</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-414/">Error 414</a> page.</p>
<h2 id="415-unsupported-media-type">415 Unsupported Media Type</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-415/">Error 415</a> page.</p>
<h2 id="416-range-not-satisfiable">416 Range Not Satisfiable</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-416/">Error 416</a> page.</p>
<h2 id="417-expectation-failed">417 Expectation Failed</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-417/">Error 417</a> page.</p>
<h2 id="429-too-many-requests">429 Too Many Requests</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-429/">Error 429</a> page.</p>
<h2 id="451-unavailable-for-legal-reason">451 Unavailable For Legal Reason</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-451/">Error 451</a> page.</p>
<h2 id="499-client-close-request">499 Client Close Request</h2>
<p>For a complete description of this error refer to the <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-499/">Error 499</a> page.</p>
