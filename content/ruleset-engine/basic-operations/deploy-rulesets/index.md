<p>Use the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> to deploy a ruleset. To deploy a ruleset, add a rule with <code>&quot;action&quot;: &quot;execute&quot;</code> to a <a href="/ruleset-engine/about/rulesets/#entry-point-ruleset">phase entry point ruleset</a>, specifying the ruleset ID to execute as an action parameter. Use a separate rule for each ruleset you want to deploy.</p>
<p>A rule that executes a ruleset consists of:</p>
<ul>
<li>The ID of the ruleset you want to execute, included in <code>action_parameters.id</code>.</li>
<li>An expression.</li>
<li>The <code>execute</code> action.</li>
</ul>
<p>The rules in the ruleset execute when a request satisfies the expression.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13286.md")
</aside>
<h2 id="example">Example</h2>
<p>The following example deploys the <a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/">Cloudflare Managed Ruleset</a> (with ID <code class="nb-rule-id" title="efb7b8c949ac4650a09736fc376e9aee">376e9aee</code>) to the <code>http_request_firewall_managed</code> phase of a given zone (<code>$ZONE_ID</code>) by adding a rule that executes the managed ruleset.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/{ruleset_phase}/entrypoint \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;efb7b8c949ac4650a09736fc376e9aee&quot;&#10;      },&#10;      &quot;expression&quot;: &quot;true&quot;,&#10;      &quot;description&quot;: &quot;Execute Cloudflare Managed Ruleset on my zone ruleset&quot;&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;ZONE_PHASE_RULESET_ID&gt;&quot;,&#10;		&quot;name&quot;: &quot;Zone-level Ruleset 1&quot;,&#10;		&quot;description&quot;: &quot;&quot;,&#10;		&quot;kind&quot;: &quot;zone&quot;,&#10;		&quot;version&quot;: &quot;latest&quot;,&#10;		&quot;rules&quot;: [&#10;			{&#10;				&quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;,&#10;				&quot;version&quot;: &quot;1&quot;,&#10;				&quot;action&quot;: &quot;execute&quot;,&#10;				&quot;action_parameters&quot;: {&#10;					&quot;id&quot;: &quot;efb7b8c949ac4650a09736fc376e9aee&quot;,&#10;					&quot;version&quot;: &quot;3&quot;&#10;				},&#10;				&quot;expression&quot;: &quot;true&quot;,&#10;				&quot;description&quot;: &quot;Execute Cloudflare Managed Ruleset on my zone ruleset&quot;,&#10;				&quot;last_updated&quot;: &quot;2021-03-18T18:08:14.003361Z&quot;,&#10;				&quot;ref&quot;: &quot;&lt;RULE_REF&gt;&quot;,&#10;				&quot;enabled&quot;: true&#10;			}&#10;		],&#10;		&quot;last_updated&quot;: &quot;2021-03-18T18:08:14.003361Z&quot;,&#10;		&quot;phase&quot;: &quot;http_request_firewall_managed&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13285.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<p>For more examples of deploying rulesets, refer to the following pages:</p>
<ul>
<li><a href="/ruleset-engine/managed-rulesets/deploy-managed-ruleset/">Deploy a managed ruleset</a></li>
<li><a href="/ruleset-engine/managed-rulesets/override-examples/">Managed ruleset override examples</a>.</li>
<li><a href="/ruleset-engine/custom-rulesets/deploy-custom-ruleset/">Deploy a custom ruleset</a></li>
</ul>
<p>Refer to <a href="/ruleset-engine/managed-rulesets/">Work with managed rulesets</a> and <a href="/ruleset-engine/custom-rulesets/">Work with custom rulesets</a> for more information.</p>
<p>For more information on the available API endpoints for editing and deploying rulesets, refer to <a href="/ruleset-engine/rulesets-api/update/">Update or deploy a ruleset</a>.</p>
