<p>Use the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> to create a compression rule via API.</p>
<h2 id="basic-rule-settings">Basic rule settings</h2>
<p>When creating a compression rule via API, make sure you:</p>
<ul>
<li>Set the rule action to <code>compress_response</code>.</li>
<li>Define the parameters in the <code>action_parameters</code> field according to the <a href="/rules/compression-rules/settings/#api-configuration-settings">settings</a> you wish to override for matching requests.</li>
<li>Deploy the rule to the <code>http_response_compression</code> phase at the zone level.</li>
</ul>
<h2 id="procedure">Procedure</h2>
<p>Follow this workflow to create a compression rule for a given zone via API:</p>
<ol>
<li>
<p>Use the <a href="/api/resources/rulesets/methods/list/">List zone rulesets</a> operation to check if there is already a ruleset for the <code>http_response_compression</code> phase at the zone level.</p>
</li>
<li>
<p>If the phase ruleset does not exist, create it using the <a href="/api/resources/rulesets/methods/create/">Create a zone ruleset</a> operation. In the new ruleset properties, set the following values:</p>
<ul>
<li><strong>kind</strong>: <code>zone</code></li>
<li><strong>phase</strong>: <code>http_response_compression</code></li>
</ul>
</li>
<li>
<p>Use the <a href="/api/resources/rulesets/methods/update/">Update a zone ruleset</a> operation to add a compression rule to the list of ruleset rules. Alternatively, include the rule in the <a href="/api/resources/rulesets/methods/create/">Create a zone ruleset</a> request mentioned in the previous step.</p>
</li>
</ol>
<h2 id="examples">Examples</h2>
<p>For example API requests, refer to the <a href="/rules/compression-rules/examples/">Examples gallery</a>.</p>
