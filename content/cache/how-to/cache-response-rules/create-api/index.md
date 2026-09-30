<p>Use the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> to create a Cache Response Rule via API. To configure the Cloudflare API, refer to the <a href="/fundamentals/api/get-started/">API documentation</a>.</p>
<h2 id="basic-rule-settings">Basic rule settings</h2>
<p>When creating a Cache Response Rule via API, make sure you:</p>
<ul>
<li>Set the rule action to one of the <a href="/cache/how-to/cache-response-rules/settings/#available-actions">available actions</a>.</li>
<li>Define the parameters in the <code>action_parameters</code> field according to the <a href="/cache/how-to/cache-response-rules/settings/">settings</a> you wish to configure for matching responses.</li>
<li>Deploy the rule to the <code>http_response_cache_settings</code> phase entry point ruleset.</li>
</ul>
<h2 id="procedure">Procedure</h2>
<ol>
<li>Use the <a href="/api/resources/rulesets/methods/list/">List zone rulesets</a> method to check if a ruleset already exists for the <code>http_response_cache_settings</code> phase.</li>
<li>If the phase ruleset does not exist, create it using the <a href="/api/resources/rulesets/methods/create/">Create a zone ruleset</a> operation. In the new ruleset properties, set the following values:
<ul>
<li>kind: <code>zone</code></li>
<li>phase: <code>http_response_cache_settings</code></li>
</ul>
</li>
<li>Use the <a href="/api/resources/rulesets/methods/update/">Update a zone ruleset</a> operation to add rules to the ruleset. Alternatively, include the rules in the <a href="/api/resources/rulesets/methods/create/">Create a zone ruleset</a> request mentioned in the previous step.</li>
</ol>
<h2 id="example-requests">Example requests</h2>
<p>These examples demonstrate all the available actions in Cache Response Rules using request and response matching criteria. Using these examples directly will cause any existing rules in the phase to be replaced.</p>
<details class="nb-details"><summary>Example: Strip response headers from JS files before caching</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3924.md")
</div></details>
<details class="nb-details"><summary>Example: Set static cache tags on API responses</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3925.md")
</div></details>
<details class="nb-details"><summary>Example: Add cache tags from a response header using an expression</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3926.md")
</div></details>
<details class="nb-details"><summary>Example: Override cache-control with max-age</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3927.md")
</div></details>
<details class="nb-details"><summary>Example: Set private directive with qualifiers</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3928.md")
</div></details>
<details class="nb-details"><summary>Example: Set immutable for static font assets</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3929.md")
</div></details>
<details class="nb-details"><summary>Example: Multiple rules with strip headers, tag responses, and set cache control</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3930.md")
</div></details>
<h2 id="required-api-token-permissions">Required API token permissions</h2>
<p>The API token used in API requests to manage Cache Response Rules must have the following permissions:</p>
<ul>
<li><em>Zone</em> &gt; <em>Cache Rules</em> &gt; <em>Edit</em></li>
<li><em>Account Rulesets</em> &gt; <em>Edit</em></li>
<li><em>Account Filter Lists</em> &gt; <em>Edit</em></li>
</ul>
