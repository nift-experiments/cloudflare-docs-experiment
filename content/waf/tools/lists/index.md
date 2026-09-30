<p>Lists allow you to group items such as IP addresses, hostnames, or autonomous system numbers (ASNs), and reference them by name in Cloudflare <a href="/ruleset-engine/rules-language/expressions/">rule expressions</a>. Instead of adding each item individually to every rule that needs it, you define the group once and reuse it across rules and zones.</p>
<p>You can create your own <a href="/waf/tools/lists/custom-lists/">custom lists</a> or use <a href="/waf/tools/lists/managed-lists/">Managed Lists</a> maintained by Cloudflare, such as Managed IP Lists that provide threat intelligence data.</p>
<p>Lists have the following advantages:</p>
<ul>
<li>When creating a rule, using a list is easier and less error-prone than adding a long list of items such as IP addresses to a rule expression.</li>
<li>When updating a set of rules that target the same group of IP addresses (or hostnames), using an IP list (or a hostname list) is easier and less error prone than editing multiple rules.</li>
<li>Lists are easier to read and more informative, particularly when you use descriptive names for your lists.</li>
</ul>
<p>When you update the content of a list, any rules that use the list are automatically updated, so you can make a single change to your list rather than modify rules individually.</p>
<p>Cloudflare stores your lists at the account level. You can use the same list in rules of different zones in your Cloudflare account.</p>
<h2 id="supported-lists">Supported lists</h2>
<p>Cloudflare supports the following lists:</p>
<ul>
<li><a href="/waf/tools/lists/custom-lists/">Custom lists</a>: Includes custom IP lists, hostname lists, and ASN lists.</li>
<li><a href="/waf/tools/lists/managed-lists/">Managed Lists</a>: Lists managed and updated by Cloudflare, such as Managed IP Lists.</li>
</ul>
<p>Refer to each page for details.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/15713.md")
</aside>
<p>You can also use <a href="/ruleset-engine/rules-language/values/#inline-lists">inline lists</a> in rule expressions. Inline lists allow you to include values directly in an expression without creating a separate list first. However, any changes to the values require editing the rule itself.</p>
<h2 id="list-names">List names</h2>
<p>The name of a list must comply with the following requirements:</p>
<ul>
<li>The name uses only lowercase letters, numbers, and the underscore (<code>_</code>) character in the name. A valid name satisfies this regular expression: <code>^[a-z0-9_]+$</code>.</li>
<li>The maximum length of a list name is 50 characters.</li>
</ul>
<h2 id="work-with-lists">Work with lists</h2>
<h3 id="create-and-edit-lists">Create and edit lists</h3>
<p>You can <a href="/waf/tools/lists/create-dashboard/">create lists in the Cloudflare dashboard</a> or using the <a href="/waf/tools/lists/lists-api/">Lists API</a>.</p>
<p>After creating a list, you can add and remove items from the list, but you cannot change the list name or type.</p>
<h3 id="use-lists-in-expressions">Use lists in expressions</h3>
<p>Both the Cloudflare dashboard and the Cloudflare API support lists:</p>
<ul>
<li>To use lists in an expression from the Cloudflare dashboard, refer to <a href="/waf/tools/lists/use-in-expressions/">Use lists in expressions</a>.</li>
<li>To reference a list in an API expression, refer to <a href="/ruleset-engine/rules-language/values/#lists">Lists</a> in the Rules language reference.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15712.md")
</aside>
<h3 id="search-list-items">Search list items</h3>
<p>You can search for list items in the dashboard or <a href="/api/resources/rules/subresources/lists/subresources/items/methods/list/">via API</a>.</p>
<p>For IP lists, Cloudflare returns IP addresses or ranges that start with your search query. For example, searching <code>192.0.2</code> matches <code>192.0.2.1</code> and <code>192.0.2.0/24</code>, but searching for <code>192.0.2.100</code> does not match a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/15714.md")
</div> like `192.0.2.0/24` that contains that address.
<p>For Bulk Redirect Lists, Cloudflare returns entries where the source URL or target URL contains your search query.</p>
<h2 id="availability">Availability</h2>
<p>List availability varies according to the list type and your Cloudflare plan and subscriptions.</p>
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
<td>Number of custom lists (any type)</td>
<td>1</td>
<td>10</td>
<td>10</td>
<td>1,000</td>
</tr>
<tr>
<td>Max. number of list items (across all custom lists)</td>
<td>10,000</td>
<td>10,000</td>
<td>10,000</td>
<td>500,000</td>
</tr>
<tr>
<td>IP lists</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Other custom lists (hostnames, ASNs)</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Managed IP Lists</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<p>Notes:</p>
<ul>
<li>
<p>The number of available custom lists depends on the highest plan in your account. Any account with at least one paid plan will get the highest quota.</p>
</li>
<li>
<p>Customers on Enterprise plans can create a maximum of 1,000 custom lists in total across different list types. The following additional limits apply:</p>
<ul>
<li>Up to 40 hostname lists, with a maximum of 10,000 list items across all hostname lists.</li>
<li>Up to 40 ASN lists, with a maximum of 30,000 list items across all ASN lists.</li>
</ul>
</li>
<li>
<p>Customers on Enterprise plans may contact their account team if they need more custom lists or a larger maximum number of items across lists.</p>
</li>
<li>
<p>For details on the availability of Bulk Redirect Lists, refer to the <a href="/rules/url-forwarding/#availability">Rules</a> documentation.</p>
</li>
</ul>
<hr />
<h2 id="user-role-requirements">User role requirements</h2>
<p>The following user roles have access to the list management functionality:</p>
<ul>
<li>Super Administrator</li>
<li>Administrator</li>
<li>Firewall</li>
</ul>
<h2 id="final-remarks">Final remarks</h2>
<p>You can only delete a list when no rules (enabled or disabled) reference it.</p>
<p>Cloudflare will apply the following rules when you add items to an existing list (either manually or via CSV file):</p>
<ul>
<li>Do not remove any existing list items before updating/adding items.</li>
<li>Update items that were already in the list.</li>
<li>Add items that were not present in the list.</li>
</ul>
<p>To replace the entire contents of a list at once, format the data as an array and use the <a href="/api/resources/rules/subresources/lists/subresources/items/methods/update/">Update all list items</a> operation in the <a href="/waf/tools/lists/lists-api/endpoints/">Lists API</a>.</p>
<p>The Cloudflare dashboard does not support downloading a list as a CSV file. To export list contents, use the <a href="/api/resources/rules/subresources/lists/subresources/items/methods/list/">Get list items</a> API operation.</p>
