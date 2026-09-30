<p>Single Redirects allow you to create static or dynamic URL <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/13190.md")
</div>. Static redirects send users to a fixed target URL, while dynamic redirects build the target URL from components of the original request. A [wildcard-based](/ruleset-engine/rules-language/operators/#wildcard-matching) interface allows you to define source and target URL patterns without complex functions or regular expressions, efficiently handling thousands of URLs with a single rule. Dynamic URL redirects also support advanced features such as string replacement operations and [regular expressions](/ruleset-engine/rules-language/values/#string-values-and-regular-expressions) (depending on your Cloudflare plan).
<p>For more complex and customized redirect logic, consider using <a href="/rules/snippets/">Snippets</a>.</p>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/rules/url-forwarding/#availability">Availability</a>: Information on the Single Redirects quotas and features per Cloudflare plan.</li>
<li><a href="/rules/url-forwarding/#execution-order">Execution order</a>: Execution order of the different Rules products.</li>
<li><a href="/rules/trace-request/">Trace a request</a>: Use Cloudflare Trace to determine if a redirect rule is triggering for a specific URL.</li>
</ul>
