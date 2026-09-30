<p>Custom rules allow you to control incoming traffic by filtering requests to a zone. They work as customized web application firewall (WAF) rules that you can use to perform actions like <em>Block</em> or <em>Managed Challenge</em> on incoming requests. You can also use the <em>Skip</em> action in a custom rule to <a href="/waf/custom-rules/skip/">skip one or more Cloudflare security features</a>.</p>
<p>In the <a href="/security/">new security dashboard</a>, custom rules are one of the available types of <a href="/security/rules/">security rules</a>. Security rules perform security-related actions on incoming requests that match specified filters.</p>
<p>Like other rules evaluated by Cloudflare's <a href="/ruleset-engine/">Ruleset Engine</a>, custom rules have the following basic parameters:</p>
<ul>
<li>An <a href="/ruleset-engine/rules-language/expressions/">expression</a> that specifies the criteria you are matching traffic on using the <a href="/ruleset-engine/rules-language/">Rules language</a>.</li>
<li>An <a href="/ruleset-engine/rules-language/actions/">action</a> that specifies what to perform when there is a match for the rule.</li>
</ul>
<p>Custom rules are evaluated in order, and some actions like <em>Block</em> will stop the evaluation of other rules. This means that if an earlier rule blocks a request, later rules will not run for that request. For more details on actions and their behavior, refer to <a href="/ruleset-engine/rules-language/actions/">Actions</a>.</p>
<h2 id="custom-rulesets">Custom rulesets</h2>
<p>To define sets of custom rules that apply to more than one zone, use <a href="/waf/account/custom-rulesets/">custom rulesets</a>. At the zone level, all customers can create and deploy custom rulesets. Custom rulesets at the account level require an Enterprise plan.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15390.md")
</aside>
<h2 id="interaction-with-other-app-security-features">Interaction with other app security features</h2>
<p>If you are using several app security features like custom rules, Managed Rules, and Super Bot Fight Mode, it is important to understand how these features interact and the order in which they execute. Refer to <a href="/waf/feature-interoperability/">Security features interoperability</a> for more information.</p>
<h2 id="availability">Availability</h2>
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
<tr>
<td>Number of custom rulesets (zone)</td>
<td>1</td>
<td>2</td>
<td>5</td>
<td>10</td>
</tr>
<tr>
<td>Account-level custom rulesets</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<p>The maximum number of custom rules applies to all rules in the <code>http_request_firewall_custom</code> <a href="/ruleset-engine/about/phases/">phase</a>, which is where custom rules run. Each scope (zone or account) has a separate maximum number of rules, counted in the following way:</p>
<ul>
<li>Zone: All custom rules plus all the rules across custom rulesets defined at the zone level.</li>
<li>Account: All the rules across custom rulesets defined at the account level.</li>
</ul>
<hr />
<h2 id="next-steps">Next steps</h2>
<p>Refer to the following pages for instructions on creating custom rules:</p>
<ul>
<li><a href="/waf/custom-rules/create-dashboard/">Create a custom rule in the dashboard</a></li>
<li><a href="/waf/custom-rules/create-api/">Create a custom rule via API</a></li>
<li><a href="/terraform/additional-configurations/waf-custom-rules/">WAF custom rules configuration using Terraform</a></li>
</ul>
<p>For examples of using custom rules to address common use cases, refer to <a href="/waf/custom-rules/use-cases/">Common use cases</a>.</p>
