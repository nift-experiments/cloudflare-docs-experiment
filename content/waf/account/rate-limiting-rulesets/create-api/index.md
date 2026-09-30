<p>To deploy rate limiting rules at the account level, you must create a rate limiting ruleset with one or more rules. Use the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> to create and deploy rate limiting rulesets via API.</p>
<p>For more information on rule parameters, refer to <a href="/waf/rate-limiting-rules/parameters/">Rate limiting parameters</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15424.md")
</aside>
<p>Each rate limiting rule contains a <code>ratelimit</code> object with the rate limiting configuration. Refer to <a href="/waf/rate-limiting-rules/parameters/">Rate limiting parameters</a> for more information on this object and its parameters.</p>
<p>If you are using Terraform, refer to <a href="/terraform/additional-configurations/rate-limiting-rules/#create-a-rate-limiting-rule-at-the-account-level">Rate limiting rules configuration using Terraform</a>.</p>
<h2 id="procedure">Procedure</h2>
<p>To deploy a rate limiting ruleset in your account, follow these general steps:</p>
<ol>
<li>Create a rate limiting ruleset (that is, a custom ruleset in the <code>http_ratelimit</code> phase) with one or more rate limiting rules.</li>
<li>Deploy the ruleset to the <a href="/ruleset-engine/about/rulesets/#entry-point-ruleset">entry point ruleset</a> of the <code>http_ratelimit</code> phase at the account level.</li>
</ol>
<h3 id="1-create-a-rate-limiting-ruleset"><ol>
<li>Create a rate limiting ruleset</li>
</ol></h3>
<p>The following example creates a rate limiting ruleset with a single rate limiting rule in the <code>rules</code> array.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;description&quot;: &quot;&quot;,&#10;  &quot;kind&quot;: &quot;custom&quot;,&#10;  &quot;name&quot;: &quot;My rate limiting ruleset&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;description&quot;: &quot;Rate limit API requests&quot;,&#10;      &quot;expression&quot;: &quot;(starts_with(http.request.uri.path, \&quot;/my-api/\&quot;))&quot;,&#10;      &quot;ratelimit&quot;: {&#10;        &quot;characteristics&quot;: [&#10;          &quot;ip.src&quot;,&#10;          &quot;cf.colo.id&quot;&#10;        ],&#10;        &quot;requests_to_origin&quot;: false,&#10;        &quot;requests_per_period&quot;: 30,&#10;        &quot;period&quot;: 60,&#10;        &quot;mitigation_timeout&quot;: 120&#10;      },&#10;      &quot;action&quot;: &quot;block&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;response&quot;: {&#10;          &quot;status_code&quot;: 429,&#10;          &quot;content_type&quot;: &quot;application/json&quot;,&#10;          &quot;content&quot;: &quot;{ \&quot;error\&quot;: \&quot;Your API requests have been rate limited. Wait a couple of minutes and try again.\&quot; }&quot;&#10;        }&#10;      },&#10;      &quot;enabled&quot;: true&#10;    }&#10;  ],&#10;  &quot;phase&quot;: &quot;http_ratelimit&quot;&#10;}&#x27;</code></pre>
<p>The available characteristics depend on your Cloudflare plan and product subscriptions. Refer to <a href="/waf/rate-limiting-rules/#availability">Availability</a> for more information.</p>
<p>Save the ruleset ID in the response for the next step.</p>
<h3 id="2-deploy-the-rate-limiting-ruleset"><ol start="2">
<li>Deploy the rate limiting ruleset</li>
</ol></h3>
<p>To deploy the rate limiting ruleset, add a rule with <code>&quot;action&quot;: &quot;execute&quot;</code> to the <code>http_ratelimit</code> phase entry point ruleset at the account level.</p>
<ol>
<li></li>
</ol>
<p>Invoke the <a href="/api/resources/rulesets/subresources/phases/methods/get/">Get an account entry point ruleset</a> operation to obtain the definition of the entry point ruleset for the <code>http_ratelimit</code> phase. You will need the <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a> for this task.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets/phases/{ruleset_phase}/entrypoint \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;description&quot;: &quot;Account-level phase entry point&quot;,&#10;		&quot;id&quot;: &quot;&lt;RULESET_ID&gt;&quot;,&#10;		&quot;kind&quot;: &quot;root&quot;,&#10;		&quot;last_updated&quot;: &quot;2024-03-16T15:40:08.202335Z&quot;,&#10;		&quot;name&quot;: &quot;root&quot;,&#10;		&quot;phase&quot;: &quot;http_ratelimit&quot;,&#10;		&quot;rules&quot;: [&#10;			// ...&#10;		],&#10;		&quot;source&quot;: &quot;firewall_managed&quot;,&#10;		&quot;version&quot;: &quot;10&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<ol start="2">
<li></li>
</ol>
<p>If the entry point ruleset already exists (that is, if you received a <code>200 OK</code> status code and the ruleset definition), take note of the ruleset ID in the response. Then, invoke the <a href="/api/resources/rulesets/subresources/rules/methods/create/">Create an account ruleset rule</a> operation to add an <code>execute</code> rule to the existing ruleset deploying the <p>rate limiting ruleset</p>
. By default, the rule will be added at the end of the list of rules already in the ruleset.</p>
<pre><code>The following request creates a rule that executes the rate limiting ruleset with ID `&lt;RATE_LIMITING_RULESET_ID&gt;` for all Enterprise zones in the account:&#10;</code></pre>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets/{ruleset_id}/rules \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;description&quot;: &quot;Execute rate limiting ruleset&quot;,&#10;  &quot;expression&quot;: &quot;(cf.zone.plan eq \&quot;ENT\&quot;)&quot;,&#10;  &quot;action&quot;: &quot;execute&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;id&quot;: &quot;&lt;RATE_LIMITING_RULESET_ID&gt;&quot;&#10;  },&#10;  &quot;enabled&quot;: true&#10;}&#x27;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15423.md")
</aside>
<ol start="3">
<li></li>
</ol>
<p>If the entry point ruleset does not exist (that is, if you received a <code>404 Not Found</code> status code in step 1), create it using the <a href="/api/resources/rulesets/methods/create/">Create an account ruleset</a> operation. Include a single rule in the <code>rules</code> array that executes the <p>rate limiting ruleset</p>
for <p>all incoming requests of Enterprise zones in your account</p>
.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;description&quot;: &quot;&quot;,&#10;  &quot;kind&quot;: &quot;root&quot;,&#10;  &quot;name&quot;: &quot;Account-level phase entry point&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;expression&quot;: &quot;(cf.zone.plan eq \&quot;ENT\&quot;)&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;&lt;RATE_LIMITING_RULESET_ID&gt;&quot;&#10;      }&#10;    }&#10;  ],&#10;  &quot;phase&quot;: &quot;http_ratelimit&quot;&#10;}&#x27;</code></pre>
<p>For examples of rate limiting rule definitions for the API, refer to <a href="/waf/rate-limiting-rules/create-api/">Create a rate limiting rule via API</a>.</p>
<hr />
<h2 id="next-steps">Next steps</h2>
<p>Use the different operations in the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> to work with the ruleset you just created and deployed. The following table has a list of common tasks for working with rate limiting rulesets at the account level:</p>
<table>
<thead>
<tr>
<th>Task</th>
<th>Procedure</th>
</tr>
</thead>
<tbody>
<tr>
<td>Get list of rate limiting rulesets</td>
<td><p>Use the [List account rulesets][1] operation and search for rulesets with <code>&quot;kind&quot;: &quot;custom&quot;</code> and <code>&quot;phase&quot;: &quot;http_ratelimit&quot;</code>. The response will include the ruleset IDs.</p><p>For more information, refer to [List existing rulesets][2].</p></td>
</tr>
<tr>
<td>List all rules in a rate limiting ruleset</td>
<td><p>Use the [Get an account ruleset][3] operation with the rate limiting ruleset ID to obtain the list of configured rate limiting rules and their IDs.</p><p>For more information, refer to [View a specific ruleset][4].</p></td>
</tr>
<tr>
<td>Update a rate limiting rule</td>
<td><p>Use the [Update an account ruleset rule][5] operation. You will need to provide the rate limiting ruleset ID and the rule ID.</p><p>For more information, refer to [Update a rule in a ruleset][6].</p></td>
</tr>
<tr>
<td>Delete a rate limiting rule</td>
<td><p>Use the [Delete an account ruleset rule][7] operation. You will need to provide the rate limiting ruleset ID and the rule ID.</p><p>For more information, refer to [Delete a rule in a ruleset][8].</p></td>
</tr>
</tbody>
</table>
<h2 id="more-resources">More resources</h2>
<p>For instructions on deploying a rate limiting rule at the zone level via API, refer to <a href="/waf/rate-limiting-rules/create-api/">Create a rate limiting rule via API</a>.</p>
<p>For more information on the different rate limiting parameters you can configure in your rate limiting rules, refer to <a href="/waf/rate-limiting-rules/parameters/">Rate limiting parameters</a>.</p>
