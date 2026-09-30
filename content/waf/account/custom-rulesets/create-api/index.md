<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15452.md")
</aside>
<h2 id="quota-limits">Quota limits</h2>
<p>Account-level custom rulesets have the following quota limits:</p>
<ul>
<li><strong>Maximum rulesets:</strong> 10</li>
<li><strong>Maximum rules per ruleset:</strong> 100</li>
<li><strong>Total rule quota:</strong> 1,000 rules across all rulesets on the request path</li>
</ul>
<p>The total rule quota of 1,000 rules is a hard limit that applies to all plans and cannot be increased. This limit applies across all rulesets that a request traverses, not just account-level custom rulesets.</p>
<h3 id="redistribute-rules-across-rulesets">Redistribute rules across rulesets</h3>
<p>If you need to change the distribution of rules across your rulesets (for example, to create fewer rulesets with more rules per ruleset), contact Cloudflare Support. Only Cloudflare Support can update account-level entitlements to change the ruleset and rule distribution.</p>
<p>Before contacting Support, consider the following optimizations:</p>
<ul>
<li><strong>Consolidate rules:</strong> Combine rules with similar conditions or actions into a single rule with broader matching criteria.</li>
<li><strong>Remove unused rules:</strong> Audit your rulesets and remove rules that are no longer triggering or are duplicating functionality.</li>
<li><strong>Use IP lists:</strong> Instead of creating multiple rules for individual IP addresses, use <a href="/waf/tools/lists/">IP lists</a> to group IPs and reference them in a single rule.</li>
</ul>
<p>To deploy custom rules at the account level:</p>
<ol>
<li>Create a custom ruleset with one or more rules. Alternatively, identify the existing custom ruleset you want to deploy using the <a href="/api/resources/rulesets/methods/list/">List account rulesets</a> API operation.</li>
<li>Deploy the custom ruleset so that it gets executed. To deploy a custom ruleset, create a rule with the <code>execute</code> action.</li>
</ol>
<p>Use the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> to work with custom rulesets using the API.</p>
<p>If you are using Terraform, refer to <a href="/terraform/additional-configurations/waf-custom-rules/#create-and-deploy-a-custom-ruleset">WAF custom rules configuration using Terraform</a>.</p>
<h2 id="procedure">Procedure</h2>
<p>To deploy a custom ruleset, follow these general steps:</p>
<ol>
<li>Create a custom ruleset in the <code>http_request_firewall_custom</code> phase with one or more rules.</li>
<li>Deploy the ruleset to the <a href="/ruleset-engine/about/rulesets/#entry-point-ruleset">entry point ruleset</a> of the <code>http_request_firewall_custom</code> phase.</li>
</ol>
<h3 id="1-create-a-custom-ruleset"><ol>
<li>Create a custom ruleset</li>
</ol></h3>
<p>The following example creates a custom ruleset at the account level with a single rule in the <code>rules</code> array.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;description&quot;: &quot;&quot;,&#10;  &quot;kind&quot;: &quot;custom&quot;,&#10;  &quot;name&quot;: &quot;My custom ruleset&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;description&quot;: &quot;Challenge web traffic (not /api)&quot;,&#10;      &quot;expression&quot;: &quot;not starts_with(http.request.uri.path, \&quot;/api/\&quot;)&quot;,&#10;      &quot;action&quot;: &quot;managed_challenge&quot;&#10;    }&#10;  ],&#10;  &quot;phase&quot;: &quot;http_request_firewall_custom&quot;&#10;}&#x27;</code></pre>
<p>Save the ruleset ID in the response for the next step.</p>
<h3 id="2-deploy-the-custom-ruleset"><ol start="2">
<li>Deploy the custom ruleset</li>
</ol></h3>
<p>To deploy the custom ruleset, add a rule with <code>&quot;action&quot;: &quot;execute&quot;</code> to the <code>http_request_firewall_custom</code> phase entry point ruleset.</p>
<ol>
<li></li>
</ol>
<p>Invoke the <a href="/api/resources/rulesets/subresources/phases/methods/get/">Get an account entry point ruleset</a> operation to obtain the definition of the entry point ruleset for the <code>http_request_firewall_custom</code> phase. You will need the <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a> for this task.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets/phases/{ruleset_phase}/entrypoint \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;description&quot;: &quot;Account-level phase entry point&quot;,&#10;		&quot;id&quot;: &quot;&lt;RULESET_ID&gt;&quot;,&#10;		&quot;kind&quot;: &quot;root&quot;,&#10;		&quot;last_updated&quot;: &quot;2024-03-16T15:40:08.202335Z&quot;,&#10;		&quot;name&quot;: &quot;root&quot;,&#10;		&quot;phase&quot;: &quot;http_request_firewall_custom&quot;,&#10;		&quot;rules&quot;: [&#10;			// ...&#10;		],&#10;		&quot;version&quot;: &quot;9&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<ol start="2">
<li></li>
</ol>
<p>If the entry point ruleset already exists (that is, if you received a <code>200 OK</code> status code and the ruleset definition), take note of the ruleset ID in the response. Then, invoke the <a href="/api/resources/rulesets/subresources/rules/methods/create/">Create an account ruleset rule</a> operation to add an <code>execute</code> rule to the existing ruleset deploying the <p>custom ruleset</p>
. By default, the rule will be added at the end of the list of rules already in the ruleset.</p>
<pre><code>The following request creates a rule that executes the custom ruleset with ID `&lt;CUSTOM_RULESET_ID&gt;` for all Enterprise zones in the account:&#10;</code></pre>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets/{ruleset_id}/rules \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;description&quot;: &quot;Execute custom ruleset&quot;,&#10;  &quot;expression&quot;: &quot;(cf.zone.plan eq \&quot;ENT\&quot;)&quot;,&#10;  &quot;action&quot;: &quot;execute&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;id&quot;: &quot;&lt;CUSTOM_RULESET_ID&gt;&quot;&#10;  },&#10;  &quot;enabled&quot;: true&#10;}&#x27;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15451.md")
</aside>
<ol start="3">
<li></li>
</ol>
<p>If the entry point ruleset does not exist (that is, if you received a <code>404 Not Found</code> status code in step 1), create it using the <a href="/api/resources/rulesets/methods/create/">Create an account ruleset</a> operation. Include a single rule in the <code>rules</code> array that executes the <p>custom ruleset</p>
for <p>all incoming requests of Enterprise zones in your account</p>
.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;description&quot;: &quot;&quot;,&#10;  &quot;kind&quot;: &quot;root&quot;,&#10;  &quot;name&quot;: &quot;Account-level phase entry point&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;expression&quot;: &quot;(cf.zone.plan eq \&quot;ENT\&quot;)&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;&lt;CUSTOM_RULESET_ID&gt;&quot;&#10;      }&#10;    }&#10;  ],&#10;  &quot;phase&quot;: &quot;http_request_firewall_custom&quot;&#10;}&#x27;</code></pre>
<h2 id="next-steps">Next steps</h2>
<p>Use the different operations in the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> to work with the custom ruleset you created and deployed. The following table has a list of common tasks for working with custom rulesets at the account level:</p>
<table>
<thead>
<tr>
<th>Task</th>
<th>Procedure</th>
</tr>
</thead>
<tbody>
<tr>
<td>Get list of custom rulesets</td>
<td><p>Use the [List account rulesets][1] operation and search for rulesets with <code>&quot;kind&quot;: &quot;custom&quot;</code> and <code>&quot;phase&quot;: &quot;http_request_firewall_custom&quot;</code>. The response will include the ruleset IDs.</p><p>For more information, refer to [List existing rulesets][2].</p></td>
</tr>
<tr>
<td>List all rules in a custom ruleset</td>
<td><p>Use the [Get an account ruleset][3] operation with the custom ruleset ID to obtain the list of configured rules and their IDs.</p><p>For more information, refer to [View a specific ruleset][4].</p></td>
</tr>
<tr>
<td>Update a custom rule</td>
<td><p>Use the [Update an account ruleset rule][5] operation. You will need to provide the custom ruleset ID and the rule ID.</p><p>For more information, refer to [Update a rule in a ruleset][6].</p></td>
</tr>
<tr>
<td>Delete a custom rule</td>
<td><p>Use the [Delete an account ruleset rule][7] operation. You will need to provide the custom ruleset ID and the rule ID.</p><p>For more information, refer to [Delete a rule in a ruleset][8].</p></td>
</tr>
</tbody>
</table>
<h2 id="more-resources">More resources</h2>
<p>For instructions on creating a custom ruleset at the zone level via API, refer to <a href="/waf/custom-rules/custom-rulesets/">Custom rulesets (zone level)</a>.</p>
<p>For more information on working with custom rulesets, refer to <a href="/ruleset-engine/custom-rulesets/">Work with custom rulesets</a> in the Ruleset Engine documentation.</p>
