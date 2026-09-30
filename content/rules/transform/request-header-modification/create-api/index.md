<p>Use the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> to create Request Header Transform Rules via API. Refer to the <a href="/rules/transform/examples/?operation=Request+modification">Rules examples gallery</a> for common use cases.</p>
<p>If you are using Terraform, refer to <a href="/terraform/additional-configurations/transform-rules/#create-a-request-header-transform-rule">Transform Rules configuration using Terraform</a>.</p>
<h2 id="basic-rule-settings">Basic rule settings</h2>
<p>When creating a request header transform rule via API, make sure you:</p>
<ul>
<li>Set the rule action to <code>rewrite</code>.</li>
<li>Define the <a href="/rules/transform/request-header-modification/reference/parameters/">header modification parameters</a> in the <code>action_parameters</code> field according to the operation to perform (set or remove header).</li>
<li>Deploy the rule to the <code>http_request_late_transform</code> phase at the zone level.</li>
</ul>
<h2 id="procedure">Procedure</h2>
<p>Follow this workflow to create a request header transform rule for a given zone via API:</p>
<ol>
<li>
<p>Use the <a href="/api/resources/rulesets/methods/list/">List zone rulesets</a> operation to check if there is already a ruleset for the <code>http_request_late_transform</code> phase at the zone level.</p>
</li>
<li>
<p>If the phase ruleset does not exist, create it using the <a href="/api/resources/rulesets/methods/create/">Create a zone ruleset</a> operation. In the new ruleset properties, set the following values:</p>
<ul>
<li><strong>kind</strong>: <code>zone</code></li>
<li><strong>phase</strong>: <code>http_request_late_transform</code></li>
</ul>
</li>
<li>
<p>Use the <a href="/api/resources/rulesets/methods/update/">Update a zone ruleset</a> operation to add a request header transform rule to the list of ruleset rules. Alternatively, include the rule in the <a href="/api/resources/rulesets/methods/create/">Create a zone ruleset</a> request mentioned in the previous step.</p>
</li>
</ol>
<p>Make sure your API token has the <a href="#required-api-token-permissions">required permissions</a> to perform the API operations.</p>
<h2 id="example-requests">Example requests</h2>
<details class="nb-details"><summary>Example: Add an HTTP request header with a static value</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13141.md")
</div></details>
<details class="nb-details"><summary>Example: Add an HTTP request header with a dynamic value</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13142.md")
</div></details>
<details class="nb-details"><summary>Example: Remove an HTTP request header</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13143.md")
</div></details>
<hr />
<h2 id="required-api-token-permissions">Required API token permissions</h2>
<p>The API token used in API requests to manage Request Header Transform Rules must have at least the following permissions:</p>
<ul>
<li><em>Transform Rules</em> &gt; <em>Edit</em></li>
<li><em>Account Rulesets</em> &gt; <em>Read</em></li>
</ul>
