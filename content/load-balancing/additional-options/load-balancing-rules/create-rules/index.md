<p>Create and manage <a href="/load-balancing/additional-options/load-balancing-rules/">Load Balancing rules</a> in the <strong>Custom Rules</strong> page, which is part of the Create/Edit Load Balancer workflow found in <strong>Traffic</strong> in the dashboard.</p>
<hr />
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li><strong>Understand whether Cloudflare proxies your traffic</strong>: Depending on the <a href="/load-balancing/understand-basics/proxy-modes/">proxy status</a> of your traffic, you may have access to different fields for your load balancing rules. For more details, refer to <a href="/load-balancing/additional-options/load-balancing-rules/reference/">Supported fields and expressions</a>.</li>
</ul>
<hr />
<h2 id="example-workflow">Example Workflow</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Load Balancing</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Edit an existing load balancer or <a href="/load-balancing/load-balancers/create-load-balancer/">create a new load balancer</a>.</li>
<li>From the Load Balancer workflow, select <strong>Custom Rules</strong>.</li>
<li>Select <strong>Create Custom Rule</strong>.</li>
<li>In the <strong>Field</strong> drop-down list, choose an HTTP property. For more details, refer to <a href="/load-balancing/additional-options/load-balancing-rules/reference/">Supported fields</a>.</li>
<li>In the <strong>Operator</strong> drop-down list, choose an operator. For more details, refer to <a href="/load-balancing/additional-options/load-balancing-rules/reference/#operators-and-grouping-symbols">Operators</a>.</li>
<li>Enter the value to match. When the field is an ordered list, <strong>Value</strong> is a drop-down list. Otherwise, <strong>Value</strong> is a text input.</li>
<li>(Optional) To create a compound expression using logical operators, select <strong>And</strong> or <strong>Or</strong>.</li>
<li>For an action, choose <strong>Respond with fixed response</strong> or <strong>Override</strong> and enter additional details. For a full list of actions, refer to <a href="/load-balancing/additional-options/load-balancing-rules/actions/">Actions</a>.</li>
<li>(Optional) Select <strong>Add another override</strong>.</li>
<li>After you create your rule, select <strong>Save and Deploy</strong> or <strong>Save as Draft</strong>.</li>
<li>Select <strong>Next</strong> and review your changes.</li>
<li>Select <strong>Save</strong> to confirm.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/10439.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10438.md")
</aside>
<h2 id="example-use-case">Example use case</h2>
<h3 id="url-based-routing">URL-based routing</h3>
<p>If you want to host <code>example.com/blog</code> separately from your main website, for example, use the following custom rule.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/10440.md")
</div>
