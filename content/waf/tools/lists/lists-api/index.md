<p>The <a href="/api/resources/rules/subresources/lists/">Lists API</a> provides an interface for programmatically managing the following types of lists:</p>
<ul>
<li>
<p><a href="/waf/tools/lists/custom-lists/">Custom lists</a>: Contain one or more strings of the same type (such as IP addresses or hostnames) that you can reference collectively, by name, in rule expressions.</p>
</li>
<li>
<p><a href="/rules/url-forwarding/bulk-redirects/concepts/#bulk-redirect-lists">Bulk Redirect Lists</a>: Contain URL redirects that you enable by creating a Bulk Redirect Rule.</p>
</li>
</ul>
<p>To use a list in a rule expression, refer to <a href="/ruleset-engine/rules-language/values/#lists">Lists</a> in the Rules language documentation.</p>
<h2 id="get-started">Get started</h2>
<p>To get started, review the Lists <a href="/waf/tools/lists/lists-api/json-object/">JSON object</a> and <a href="/waf/tools/lists/lists-api/endpoints/">Endpoints</a>.</p>
<hr />
<h2 id="rate-limiting-for-lists-api-requests">Rate limiting for Lists API requests</h2>
<p>Cloudflare may apply rate limiting to your API requests creating, modifying, or deleting list items in custom lists and Bulk Redirect Lists.</p>
<p>Each operation (create, edit, or delete) on a list item counts as a modification. The following limits apply:</p>
<ul>
<li>You can make a maximum of 1,000,000 list item modifications in API requests over 12 hours.</li>
<li>You can make a maximum of 30,000 API requests over 12 hours doing list item modifications.</li>
</ul>
<p>If a write operation is still being processed — which happens asynchronously — and you submit a new request, you will receive a <code>429</code> HTTP status code. When this happens, submit your request again later.</p>
