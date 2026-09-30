<p>Bulk Redirects allow you to define a large number of URL redirects at the account level, which can apply across domains in your account. These redirects navigate the user from a source URL to a target URL using a given HTTP status code. URL redirection is also known as URL forwarding.</p>
<p>Unlike dynamic URL redirects created in <a href="/rules/url-forwarding/single-redirects/">Single Redirects</a>, Bulk Redirects are essentially static. They do not support string replacement operations or regular expressions. However, you can configure URL redirect parameters that affect how source URLs are matched and how the redirect is performed.</p>
<p>For more complex and customized redirect logic, consider using <a href="/rules/snippets/">Snippets</a>.</p>
<hr />
<h2 id="bulk-redirects-and-the-waf">Bulk Redirects and the WAF</h2>
<p>Bulk Redirects run after the WAF in the request processing pipeline. This means that:</p>
<ul>
<li>If a <a href="/waf/custom-rules/">WAF custom rule</a> or <a href="/waf/rate-limiting-rules/">rate limiting rule</a> blocks a request, the Bulk Redirect will not execute.</li>
<li>If a WAF rule logs or challenges a request that subsequently passes, the firewall event will still appear in <a href="/waf/analytics/security-events/">Security Events</a> and <a href="/logs/">Logpush</a> — even though the request is later redirected. This is expected behavior.</li>
</ul>
<p>For the complete request processing order, refer to <a href="/rules/url-forwarding/#execution-order">Rules execution order</a>.</p>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/rules/url-forwarding/#availability">Availability</a>: Information on the Bulk Redirects quotas and features per Cloudflare plan.</li>
<li><a href="/rules/url-forwarding/#execution-order">Execution order</a>: Execution order of the different Rules products.</li>
<li><a href="/rules/trace-request/">Trace a request</a>: Use Cloudflare Trace to determine if a bulk redirect rule is triggering for a specific URL.</li>
</ul>
