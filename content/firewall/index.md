<p>Cloudflare Firewall Rules allows you to create rules that inspect incoming traffic and block, challenge, log, or allow specific requests.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/1022.md")
</aside>
<h2 id="main-features">Main features</h2>
<ul>
<li><strong>Rule-based protection</strong>: Use pre-defined rulesets provided by Cloudflare, or define your own firewall rules. Create rules in the Cloudflare dashboard or via API.</li>
<li><strong>Complex custom rules</strong>: Each rule's expression can reference multiple fields from all the available HTTP request parameters and fields, allowing you to create complex rules.</li>
</ul>
<h2 id="availability">Availability</h2>
<p>This table outlines the Firewall Rules features and entitlements available with each customer plan:</p>
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
<td>Number of rules</td>
<td>5</td>
<td>20</td>
<td>100</td>
<td>1,000</td>
</tr>
<tr>
<td>Supported actions</td>
<td>All except Log</td>
<td>All except Log</td>
<td>All except Log</td>
<td>All</td>
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
<h2 id="next-steps">Next steps</h2>
<ul>
<li>
<p>Unless you are already an advanced user, refer to <a href="/ruleset-engine/rules-language/expressions/">Expressions</a> and <a href="/firewall/cf-firewall-rules/actions/">Actions</a> to learn more about the basic elements of firewall rules.</p>
</li>
<li>
<p>To start building your own firewall rules, refer to one of the following pages:</p>
<ul>
<li><a href="/firewall/cf-dashboard/create-edit-delete-rules/">Manage firewall rules in the dashboard</a></li>
<li><a href="/firewall/api/">Manage firewall rules via the APIs</a></li>
</ul>
</li>
<li>
<p>You can also manage firewall rules through Terraform. For more information, refer to <a href="https://blog.cloudflare.com/getting-started-with-terraform-and-cloudflare-part-1/">Getting Started with Terraform</a>.</p>
</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/ruleset-engine/rules-language/">Cloudflare Rules language</a></li>
</ul>
