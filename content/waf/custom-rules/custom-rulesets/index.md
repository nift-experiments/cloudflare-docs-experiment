<p>Custom rulesets are collections of custom rules that you can deploy at the zone or <a href="/waf/account/custom-rulesets/">account level</a>.</p>
<p>Like <a href="/waf/custom-rules/">custom rules</a>, custom rulesets allow you to control incoming traffic by filtering requests.</p>
<p>For example, you can apply a custom ruleset to all incoming requests of your zone or to a subset of incoming requests.</p>
<p>At the zone level, all customers can create and deploy custom rulesets. Custom rulesets at the account level require an Enterprise plan. For more details, refer to <a href="/waf/custom-rules/#availability">Availability</a>.</p>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="use-case-different-teams-managing-different-sets-of-custom-rules">Use case: Different teams managing different sets of custom rules</h3>
@markup("md", "content/.markup/bodies/15393.md")
</aside>
<h2 id="deploy-a-custom-ruleset-via-api">Deploy a custom ruleset via API</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15392.md")
</aside>
<p>Creating a custom ruleset does not activate it. Custom rulesets only run when a rule with the <code>execute</code> action references them from a <a href="/ruleset-engine/about/rulesets/#entry-point-ruleset">phase entry point ruleset</a> — the top-level ruleset that Cloudflare evaluates for each request in a given <a href="/ruleset-engine/about/phases/">phase</a>.</p>
<p>To deploy a custom ruleset for a zone:</p>
<ol>
<li>Create a custom ruleset at the zone level with one or more rules. Alternatively, identify the existing custom ruleset you want to deploy using the <a href="/api/resources/rulesets/methods/list/">List zone rulesets</a> API operation.</li>
<li>Add a rule with the <code>execute</code> action to the <code>http_request_firewall_custom</code> phase entry point ruleset, referencing the custom ruleset ID. This rule tells Cloudflare to run the custom ruleset when the rule expression matches.</li>
</ol>
<h3 id="1-create-custom-ruleset"><ol>
<li>Create custom ruleset</li>
</ol></h3>
<p>The following request creates a new custom ruleset at the zone level with two rules. The response will include the ID of the new custom ruleset in the <code>id</code> field.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;Custom Ruleset 1&quot;,&#10;  &quot;description&quot;: &quot;My First Custom Ruleset (zone)&quot;,&#10;  &quot;kind&quot;: &quot;custom&quot;,&#10;  &quot;phase&quot;: &quot;http_request_firewall_custom&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;expression&quot;: &quot;(ip.src.country in {\&quot;GB\&quot; \&quot;FR\&quot;} and cf.bot_management.score &lt; 20 and not cf.bot_management.verified_bot)&quot;,&#10;      &quot;action&quot;: &quot;challenge&quot;,&#10;      &quot;description&quot;: &quot;challenge GB and FR based on bot score&quot;&#10;    },&#10;    {&#10;      &quot;expression&quot;: &quot;not http.request.uri.path wildcard \&quot;/api/*\&quot;&quot;,&#10;      &quot;action&quot;: &quot;challenge&quot;,&#10;      &quot;description&quot;: &quot;challenge not /api&quot;&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;f82ccda3d21f4a02825d3fe45b5e1c10&quot;,&#10;		&quot;name&quot;: &quot;Custom Ruleset 1&quot;,&#10;		&quot;description&quot;: &quot;My First Custom Ruleset (zone)&quot;,&#10;		&quot;kind&quot;: &quot;custom&quot;,&#10;		&quot;version&quot;: &quot;1&quot;,&#10;		&quot;rules&quot;: [&#10;			{&#10;				&quot;expression&quot;: &quot;(ip.src.country in {\&quot;GB\&quot; \&quot;FR\&quot;} and cf.bot_management.score &lt; 20 and not cf.bot_management.verified_bot)&quot;,&#10;				&quot;action&quot;: &quot;challenge&quot;,&#10;				&quot;description&quot;: &quot;challenge GB and FR based on bot score&quot;&#10;			},&#10;			{&#10;				&quot;expression&quot;: &quot;not http.request.uri.path wildcard \&quot;/api/*\&quot;&quot;,&#10;				&quot;action&quot;: &quot;challenge&quot;,&#10;				&quot;description&quot;: &quot;challenge not /api&quot;&#10;			}&#10;		],&#10;		&quot;last_updated&quot;: &quot;2025-11-09T10:27:30.636197Z&quot;,&#10;		&quot;phase&quot;: &quot;http_request_firewall_custom&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15391.md")
</aside>
<h3 id="2-deploy-custom-ruleset"><ol start="2">
<li>Deploy custom ruleset</li>
</ol></h3>
<p>Deploy the custom ruleset by adding a rule with <code>&quot;action&quot;: &quot;execute&quot;</code> to the <code>http_request_firewall_custom</code> phase entry point ruleset.</p>
<ol>
<li></li>
</ol>
<p>Invoke the <a href="/api/resources/rulesets/subresources/phases/methods/get/">Get a zone entry point ruleset</a> operation to obtain the definition of the entry point ruleset for the <code>http_request_firewall_custom</code> phase. You will need the <a href="/fundamentals/account/find-account-and-zone-ids/">zone ID</a> for this task.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/{ruleset_phase}/entrypoint \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;description&quot;: &quot;Zone-level phase entry point&quot;,&#10;		&quot;id&quot;: &quot;&lt;ENTRY_POINT_RULESET_ID&gt;&quot;,&#10;		&quot;kind&quot;: &quot;zone&quot;,&#10;		&quot;last_updated&quot;: &quot;2025-11-16T15:40:08.202335Z&quot;,&#10;		&quot;name&quot;: &quot;zone&quot;,&#10;		&quot;phase&quot;: &quot;http_request_firewall_custom&quot;,&#10;		&quot;rules&quot;: [&#10;			// ...&#10;		],&#10;		&quot;version&quot;: &quot;10&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<ol start="2">
<li></li>
</ol>
<p>If the entry point ruleset already exists (that is, if you received a <code>200 OK</code> status code and the ruleset definition), take note of the ruleset ID in the response. Then, invoke the <a href="/api/resources/rulesets/subresources/rules/methods/create/">Create a zone ruleset rule</a> operation to add an <code>execute</code> rule to the existing ruleset deploying the <p>custom ruleset you created in Step 1 (replace �CODE12� with your custom ruleset ID).&amp;lt;br/&amp;gt;Since the expression is �CODE13�, the custom ruleset will run for all incoming requests</p>
. By default, the rule will be added at the end of the list of rules already in the ruleset.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id}/rules \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;action&quot;: &quot;execute&quot;,&#10;  &quot;expression&quot;: &quot;true&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;id&quot;: &quot;f82ccda3d21f4a02825d3fe45b5e1c10&quot;&#10;  },&#10;  &quot;description&quot;: &quot;Execute custom ruleset&quot;&#10;}&#x27;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;ENTRY_POINT_RULESET_ID&gt;&quot;,&#10;		&quot;name&quot;: &quot;zone&quot;,&#10;		&quot;description&quot;: &quot;Zone-level phase entry point&quot;,&#10;		&quot;kind&quot;: &quot;zone&quot;,&#10;		&quot;version&quot;: &quot;11&quot;,&#10;		&quot;rules&quot;: [&#10;			// ... any existing rules&#10;			{&#10;				&quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;,&#10;				&quot;version&quot;: &quot;1&quot;,&#10;				&quot;action&quot;: &quot;execute&quot;,&#10;				&quot;action_parameters&quot;: {&#10;					&quot;id&quot;: &quot;f82ccda3d21f4a02825d3fe45b5e1c10&quot;&#10;				},&#10;				&quot;expression&quot;: &quot;true&quot;,&#10;				&quot;description&quot;: &quot;Execute custom ruleset&quot;,&#10;				&quot;last_updated&quot;: &quot;2025-11-18T18:08:14.003361Z&quot;,&#10;				&quot;ref&quot;: &quot;&lt;RULE_REF&gt;&quot;,&#10;				&quot;enabled&quot;: true&#10;			}&#10;		],&#10;		&quot;last_updated&quot;: &quot;2025-11-18T18:08:14.003361Z&quot;,&#10;		&quot;phase&quot;: &quot;http_request_firewall_custom&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<ol start="3">
<li></li>
</ol>
<p>If the entry point ruleset does not exist (that is, if you received a <code>404 Not Found</code> status code in step 1), create it using the <a href="/api/resources/rulesets/methods/create/">Create a zone ruleset</a> operation. Include a single rule in the <code>rules</code> array that executes the <p>custom ruleset</p>
for <p>all incoming requests in the zone</p>
. <p>Replace �CODE16� with your custom ruleset ID.</p></p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;zone&quot;,&#10;  &quot;description&quot;: &quot;Zone-level phase entry point&quot;,&#10;  &quot;kind&quot;: &quot;zone&quot;,&#10;  &quot;phase&quot;: &quot;http_request_firewall_custom&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;f82ccda3d21f4a02825d3fe45b5e1c10&quot;&#10;      },&#10;      &quot;expression&quot;: &quot;true&quot;,&#10;      &quot;description&quot;: &quot;Execute custom ruleset&quot;&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<h2 id="next-steps">Next steps</h2>
<p>Use the different operations in the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> to work with the custom ruleset you created and deployed. The following table has a list of common tasks for working with custom rulesets at the zone level:</p>
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
<td><p>Use the [List zone rulesets][1] operation and search for rulesets with <code>&quot;kind&quot;: &quot;custom&quot;</code> and <code>&quot;phase&quot;: &quot;http_request_firewall_custom&quot;</code>. The response will include the ruleset IDs.</p><p>For more information, refer to [List existing rulesets][2].</p></td>
</tr>
<tr>
<td>List all rules in a custom ruleset</td>
<td><p>Use the [Get a zone ruleset][3] operation with the custom ruleset ID to obtain the list of configured rules and their IDs.</p><p>For more information, refer to [View a specific ruleset][4].</p></td>
</tr>
<tr>
<td>Update a custom rule</td>
<td><p>Use the [Update a zone ruleset rule][5] operation. You will need to provide the custom ruleset ID and the rule ID.</p><p>For more information, refer to [Update a rule in a ruleset][6].</p></td>
</tr>
<tr>
<td>Delete a custom rule</td>
<td><p>Use the [Delete a zone ruleset rule][7] operation. You will need to provide the custom ruleset ID and the rule ID.</p><p>For more information, refer to [Delete a rule in a ruleset][8].</p></td>
</tr>
</tbody>
</table>
<h2 id="more-resources">More resources</h2>
<p>For more information on working with custom rulesets via Cloudflare API, refer to <a href="/ruleset-engine/custom-rulesets/">Work with custom rulesets</a> in the Ruleset Engine documentation.</p>
