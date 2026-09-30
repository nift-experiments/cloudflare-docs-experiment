<p>Use the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> to create configuration rules via API.</p>
<h2 id="basic-rule-settings">Basic rule settings</h2>
<p>When creating a configuration rule via API, make sure you:</p>
<ul>
<li>Set the rule action to <code>set_config</code>.</li>
<li>Define the parameters in the <code>action_parameters</code> field according to the <a href="/rules/configuration-rules/settings/">settings</a> you wish to override for matching requests.</li>
<li>Deploy the rule to the <code>http_config_settings</code> phase at the zone level.</li>
</ul>
<h2 id="procedure">Procedure</h2>
<p>Follow this workflow to create a configuration rule for a given zone via API:</p>
<ol>
<li>
<p>Use the <a href="/api/resources/rulesets/methods/list/">List zone rulesets</a> operation to check if there is already a ruleset for the <code>http_config_settings</code> phase at the zone level.</p>
</li>
<li>
<p>If the phase ruleset does not exist, create it using the <a href="/api/resources/rulesets/methods/create/">Create a zone ruleset</a> operation. In the new ruleset properties, set the following values:</p>
<ul>
<li><strong>kind</strong>: <code>zone</code></li>
<li><strong>phase</strong>: <code>http_config_settings</code></li>
</ul>
</li>
<li>
<p>Use the <a href="/api/resources/rulesets/methods/update/">Update a zone ruleset</a> operation to add a configuration rule to the list of ruleset rules. Alternatively, include the rule in the <a href="/api/resources/rulesets/methods/create/">Create a zone ruleset</a> request mentioned in the previous step.</p>
</li>
</ol>
<p>Make sure your API token has the <a href="#required-api-token-permissions">required permissions</a> to perform the API operations.</p>
<h2 id="example-requests">Example requests</h2>
<details class="nb-details"><summary>Example: Add a rule that enables Email Obfuscation and Browser Integrity Check</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13024.md")
</div></details>
<details class="nb-details"><summary>Example: Add a rule that turns on Under Attack mode for the admin area</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13025.md")
</div></details>
<hr />
<h2 id="required-api-token-permissions">Required API token permissions</h2>
<p>The API token used in API requests to manage configuration rules must have at least the following permission:</p>
<ul>
<li><em>Zone</em> &gt; <em>Config Rules</em> &gt; <em>Edit</em></li>
</ul>
