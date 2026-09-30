<p>Transform Rules allow you to adjust the URI path, query string, and HTTP headers of requests and responses on the Cloudflare global network.</p>
<p>There are several types of Transform Rules:</p>
<ul>
<li><a href="/rules/transform/url-rewrite/"><strong>URL Rewrite Rules</strong></a>: Rewrite the URL path and query string of an HTTP request.</li>
<li><a href="/rules/transform/request-header-modification/"><strong>Request Header Transform Rules</strong></a>: Set the value of an HTTP request header or remove a request header.</li>
<li><a href="/rules/transform/response-header-modification/"><strong>Response Header Transform Rules</strong></a>: Set the value of an HTTP response header or remove a response header.</li>
<li><a href="/rules/transform/managed-transforms/"><strong>Managed Transforms</strong></a>: Perform common adjustments to HTTP request and response headers with pre-built, one-step configurations.</li>
</ul>
<p>For more complex header modifications and rewrite logic, consider using <a href="/rules/snippets/">Snippets</a>.</p>
<br />
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12773.md")
</aside>
<h2 id="get-started">Get started</h2>
<p>Cloudflare provides you with rules templates for common use cases.</p>
<ol>
<li>In the Cloudflare dashboard, go to the Rules <strong>Overview</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Templates</strong>, and then select one of the available templates.</li>
</ol>
<p>You can also refer to the <a href="/rules/examples/">Examples gallery</a> in the developer docs.</p>
<p>Alternatively, create a transform rule from scratch in the dashboard or via Cloudflare API. Refer to the following sections for detailed instructions:</p>
<ul>
<li><a href="/rules/transform/url-rewrite/">URL Rewrite Rules</a></li>
<li><a href="/rules/transform/request-header-modification/">Request Header Transform Rules</a></li>
<li><a href="/rules/transform/response-header-modification/">Response Header Transform Rules</a></li>
<li><a href="/rules/transform/managed-transforms/">Managed Transforms</a></li>
</ul>
<p>For Terraform examples, refer to <a href="/terraform/additional-configurations/transform-rules/">Transform Rules configuration using Terraform</a>.</p>
<p>Refer to <a href="/ruleset-engine/rules-language/">Rules language</a> for more information on building expressions for Transform Rules.</p>
<h2 id="availability">Availability</h2>
<p>Cloudflare Transform Rules are available to all customers. Support for regular expressions depends on your Cloudflare plan.</p>
<p>This table outlines the Transform Rules features available with each customer plan:</p>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Active Transform Rules</td>
<td>10</td>
<td>25</td>
<td>50</td>
<td>300</td>
</tr>
<tr>
<td>Regex support</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<p>A Cloudflare user must have the <a href="/fundamentals/manage-members/roles/">Firewall role</a> or one of the Administrator roles to access Transform Rules.</p>
<h2 id="transform-rules-evaluation">Transform Rules evaluation</h2>
<p>Managed Transforms run before other types of Transform Rules that modify HTTP headers:</p>
<ul>
<li>Managed Transforms that adjust HTTP request headers run before Request Header Transform Rules.</li>
<li>Managed Transforms that adjust HTTP response headers run before Response Header Transform Rules.</li>
</ul>
<p>Transform Rules run in order. Rules that appear later in the list of Transform Rules can overwrite changes done by previous rules. You can define the rule order in the dashboard or via API.</p>
<p>Request and response fields are immutable within each <a href="/ruleset-engine/about/phases/">phase</a> while evaluating Transform Rules for a request/response. This means that later rules in the same phase cannot match on changes made by earlier rules (they always use the original field values). For more information, refer to <a href="/ruleset-engine/about/rules/#field-values-during-rule-evaluation">Field values during rule evaluation</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/12772.md")
</aside>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>When troubleshooting Transform Rules, use <a href="/rules/trace-request/">Cloudflare Trace</a> to determine if a rule is triggering for a specific URL.</p>
