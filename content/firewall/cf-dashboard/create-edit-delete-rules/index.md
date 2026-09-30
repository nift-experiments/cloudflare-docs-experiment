<p>A firewall rule has two main attributes: an <a href="/ruleset-engine/rules-language/expressions/">expression</a> and an <a href="/firewall/cf-firewall-rules/actions/">action</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/8699.md")
</aside>
<p>When an incoming HTTP request matches a firewall rule expression, Cloudflare performs the specified action. For more information, refer to <a href="/ruleset-engine/rules-language/expressions/">Expressions</a> and <a href="/firewall/cf-firewall-rules/actions/">Actions</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8698.md")
</aside>
<h2 id="create-a-firewall-rule">Create a firewall rule</h2>
<ol>
<li>
<p>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and select your account and website.</p>
</li>
<li>
<p>Go to <strong>Security</strong> &gt; <strong>WAF</strong> &gt; <strong>Firewall rules</strong>.</p>
</li>
<li>
<p>Select <strong>Create a firewall rule</strong>.</p>
</li>
<li>
<p>In the <strong>Create firewall rule</strong> page that displays, use the <strong>Rule name</strong> input to supply a descriptive name.</p>
</li>
<li>
<p>Under <strong>When incoming requests match</strong>, use the <strong>Field</strong> drop-down list to choose an HTTP property (refer to the <a href="/ruleset-engine/rules-language/fields/reference/">Fields reference</a> for details). For each request, the value of the property you choose for <strong>Field</strong> is compared to the value you specify for <strong>Value</strong>.</p>
<p>Alternatively, use the <a href="/ruleset-engine/rules-language/expressions/edit-expressions/#expression-editor">Expression Editor</a> to define the rule expression.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/firewall/firewall-rules-expression-builder-value.png" alt="Example firewall rule expression with a selected field, operator, and value" /></p>
<ol start="6">
<li>
<p>Use the <strong>Operator</strong> drop-down list to choose a comparison operator. For an expression to match, the value of the request <strong>Field</strong> and the value specified in the <strong>Value</strong> input must satisfy the comparison operator.</p>
</li>
<li>
<p>Next, specify the value to match. If the value is an enumeration, then the <strong>Value</strong> control will be a drop-down list. Otherwise, it will be a text input.</p>
</li>
<li>
<p>To add a new sub-expression to the rule expression, select <strong>And</strong> or <strong>Or</strong> next to <strong>Value</strong>.</p>
</li>
<li>
<p>Select an action for your rule in the <strong>Action</strong> drop-down list.</p>
</li>
<li>
<p>To save and deploy your rule, select <strong>Deploy</strong>. If you are not ready to deploy your rule, select <strong>Save as draft</strong>.</p>
</li>
</ol>
<p>After you choose an option, you return to the rules list, which displays your new rule.</p>
<h2 id="manage-rules">Manage rules</h2>
<p>Use the available options in the rules list to manage firewall rules.</p>
<p><img src="/assets/upstream/images/firewall/cf-firewall-rules-list.png" alt="The rules list interface in the dashboard where you can manage firewall rules" /></p>
<h3 id="edit-rule">Edit rule</h3>
<p>Select <strong>Edit</strong> (wrench icon) located on the right of your rule in the rules list to open the <strong>Edit firewall rule</strong> panel and make the changes you want.</p>
<h3 id="enable-or-disable-rule">Enable or disable rule</h3>
<p>Use the toggle switch associated with a firewall rule to enable or disable it.</p>
<h3 id="delete-rule">Delete rule</h3>
<ol>
<li>Next to the rule you want to delete, select <strong>Delete</strong> (<strong>X</strong> icon).</li>
<li>In the confirmation dialog, select <strong>Delete</strong> to complete the operation.</li>
</ol>
<h3 id="order-rules">Order rules</h3>
<p>By default, Cloudflare evaluates firewall rules in <strong>list order</strong>, where rules are evaluated in the order they appear in the rules list. When list ordering is enabled, the rules list allows you to drag and drop firewall rules into position, as shown below.</p>
<p><img src="/images/firewall/firewall-rules-expression-builder-10.gif" alt="Animation of a user dragging and dropping a rule in the rules list to reorder it" /></p>
<p>Once there are more than 200 total rules (including inactive rules), you must manage evaluation using <strong>priority ordering</strong>, in which Cloudflare evaluates firewall rules in order of their <strong>priority number</strong>, starting with the lowest. When you cross this threshold, the firewall rules interface automatically switches to priority ordering. For more on working with priority ordering, refer to <a href="/firewall/cf-firewall-rules/order-priority/">Order and priority</a>.</p>
<h2 id="test-firewall-rules-with-rule-preview">Test firewall rules with Rule Preview</h2>
<p>Rule Preview allows customers on an Enterprise plan to understand the potential impact of a new firewall rule, by testing it against a sample of requests drawn from the last 72 hours of traffic.</p>
<p>Rule Preview is built into the <strong>Create firewall rule</strong> and <strong>Edit firewall rule</strong> panels so that you can test a rule as you edit it. For more information, refer to <a href="/firewall/cf-dashboard/rule-preview/">Preview rules</a>.</p>
