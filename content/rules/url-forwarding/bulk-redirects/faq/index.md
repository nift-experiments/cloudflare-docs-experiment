<p>Below you will find answers to the most commonly asked questions regarding Bulk Redirects.</p>
<p>To troubleshoot errors related to Bulk Redirects:</p>
<ul>
<li>Refer to <a href="/support/troubleshooting/http-status-codes/cloudflare-10xxx-errors/">Troubleshooting Cloudflare 10XXX Errors</a> for more information on runtime errors.</li>
<li>Use <a href="/rules/trace-request/">Cloudflare Trace</a> to determine if a rule is triggering for a specific URL.</li>
</ul>
<h2 id="what-happens-if-the-same-source-url-appears-in-two-different-bulk-redirect-lists">What happens if the same source URL appears in two different Bulk Redirect Lists?</h2>
<p>In this situation, Cloudflare will use the URL redirect of the first rule that triggers. This will be determined by the order of the Bulk Redirect Rules enabling each Bulk Redirect List in the <code>http_request_redirect</code> phase entry point ruleset.</p>
<h2 id="how-can-i-solve-the-following-error-this-account-has-reached-the-limit-on-the-number-of-url-matching-items-on-the-same-hostname-path">How can I solve the following error: &quot;This account has reached the limit on the number of URL matching items on the same hostname/path&quot;?</h2>
<p>You may get this error when adding items to a Bulk Redirect List.</p>
<p>You can have any number of URL redirects with the same source hostname (with different paths) or same source path (with different hostnames). However, you can have a maximum of 16 source URLs with the same hostname and path across all lists, either enabled by a Bulk Redirect Rule or not.</p>
<p>If you receive this error, check if you have any unused Bulk Redirect Lists with the source hostname and path that caused the error, and remove such items from the list.</p>
<h2 id="how-many-url-redirects-can-i-have-in-a-single-bulk-redirect-list">How many URL redirects can I have in a single Bulk Redirect List?</h2>
<p>Each account has a maximum number of URL redirects across all lists which depends on your Cloudflare plan. If you wish, you can use all the URL redirects available in your plan in a single Bulk Redirect List, but you will not be able to create any other URL redirects in a different list. Refer to <a href="/rules/url-forwarding/#availability">Availability</a> for more information.</p>
<h2 id="how-can-i-redirect-based-on-the-non-normalized-version-of-a-url">How can I redirect based on the non-normalized version of a URL?</h2>
<p>Use the <code>raw.http.request.full_uri</code> field both in the rule expression and in the key, instead of the default field <code>http.request.full_uri</code>. This will take the raw version of the URL into account, that is, the URL received on the Cloudflare global network before applying <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/13213.md")
</div>. Refer to [Bulk Redirects concepts](/rules/url-forwarding/bulk-redirects/concepts/#bulk-redirect-rules) for more information on using a custom rule expression and a custom key.
<h2 id="do-bulk-redirects-take-precedence-over-page-rules">Do Bulk Redirects take precedence over Page Rules?</h2>
<p>Yes. Bulk Redirects take precedence over Page Rules redirects. For more information on the execution order of Rules products, refer to <a href="/rules/url-forwarding/#execution-order">Execution order</a>.</p>
<h2 id="can-i-purge-an-entire-bulk-redirect-list-in-one-api-call">Can I purge an entire Bulk Redirect List in one API call?</h2>
<p>If your <a href="/rules/url-forwarding/bulk-redirects/concepts/#bulk-redirect-lists">Bulk Redirect List</a> contains 500,001 or more items, you will not be able to purge the entire list in a single API call. Instead, you must make multiple calls to <a href="/api/resources/rules/subresources/lists/subresources/items/methods/delete/">Delete List Items</a> API end-point, deleting a maximum of 100,000 items per request.</p>
<p>For example, to delete a list with 1,000,000 items, you would need to issue at least 10 API requests.</p>
