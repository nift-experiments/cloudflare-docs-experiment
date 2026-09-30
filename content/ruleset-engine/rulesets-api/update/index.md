<p>Use one of the following API endpoints to update a ruleset:</p>
<ul>
<li><a href="/api/resources/rulesets/methods/update/">Update an account ruleset</a><br/>
<code>PUT /accounts/{account_id}/rulesets/{ruleset_id}</code></li>
<li><a href="/api/resources/rulesets/subresources/phases/methods/update/">Update an account entry point ruleset</a><br/>
<code>PUT /accounts/{account_id}/rulesets/phases/{phase_name}/entrypoint</code></li>
<li><a href="/api/resources/rulesets/methods/update/">Update a zone ruleset</a><br/>
<code>PUT /zones/{zone_id}/rulesets/{ruleset_id}</code></li>
<li><a href="/api/resources/rulesets/subresources/phases/methods/update/">Update a zone entry point ruleset</a><br/>
<code>PUT /zones/{zone_id}/rulesets/phases/{phase_name}/entrypoint</code></li>
</ul>
<p>When updating a ruleset, you can update:</p>
<ul>
<li>The basic properties of a ruleset (currently only the description)</li>
<li>The list of rules in a ruleset</li>
</ul>
<p>You cannot update the name of the ruleset or its type. Do not include these fields in the <code>data</code> field of your <code>PUT</code> request.</p>
<p>To deploy a ruleset, add a rule with <code>&quot;action&quot;: &quot;execute&quot;</code> to the list of rules of an <a href="/ruleset-engine/about/rulesets/#entry-point-ruleset">entry point ruleset</a>. Refer to <a href="#example---deploy-a-ruleset">Deploy a ruleset</a> for an example.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="risk-of-replacing-all-rules">Risk of replacing all rules</h3>
@markup("md", "content/.markup/bodies/13238.md")
</aside>
<h2 id="example-set-the-rules-of-a-ruleset">Example - Set the rules of a ruleset</h2>
<p>The following <code>PUT</code> request defines the list of rules of a ruleset, setting it to a single rule. You must include all the rules you want to associate with the ruleset in every request.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;&#10;      },&#10;      &quot;expression&quot;: &quot;true&quot;&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;RULESET_ID&gt;&quot;,&#10;		&quot;name&quot;: &quot;Zone-level phase entry point ruleset&quot;,&#10;		&quot;description&quot;: &quot;This ruleset executes a managed ruleset.&quot;,&#10;		&quot;kind&quot;: &quot;zone&quot;,&#10;		&quot;version&quot;: &quot;4&quot;,&#10;		&quot;rules&quot;: [&#10;			{&#10;				&quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;,&#10;				&quot;version&quot;: &quot;2&quot;,&#10;				&quot;action&quot;: &quot;execute&quot;,&#10;				&quot;expression&quot;: &quot;true&quot;,&#10;				&quot;action_parameters&quot;: {&#10;					&quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;&#10;				},&#10;				&quot;last_updated&quot;: &quot;2025-03-17T15:42:37.917815Z&quot;&#10;			}&#10;		],&#10;		&quot;last_updated&quot;: &quot;2025-03-17T15:42:37.917815Z&quot;,&#10;		&quot;phase&quot;: &quot;http_request_firewall_managed&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<h2 id="example-deploy-a-ruleset">Example - Deploy a ruleset</h2>
<p>To deploy a ruleset, create a rule with <code>&quot;action&quot;: &quot;execute&quot;</code> that executes the ruleset, and add the ruleset ID to the <code>action_parameters</code> field in the <code>id</code> parameter.</p>
<p>The following <code>PUT</code> request deploys a managed ruleset to the <code>http_request_firewall_managed</code> phase of a zone (<code>$ZONE_ID</code>).</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/{ruleset_phase}/entrypoint \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;&#10;      },&#10;      &quot;expression&quot;: &quot;true&quot;,&#10;      &quot;description&quot;: &quot;Execute Cloudflare Managed Ruleset on my phase entry point ruleset&quot;&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;RULESET_ID&gt;&quot;,&#10;		&quot;name&quot;: &quot;Zone-level phase entry point ruleset&quot;,&#10;		&quot;description&quot;: &quot;&quot;,&#10;		&quot;kind&quot;: &quot;zone&quot;,&#10;		&quot;version&quot;: &quot;4&quot;,&#10;		&quot;rules&quot;: [&#10;			{&#10;				&quot;id&quot;: &quot;&lt;RULE_ID_1&gt;&quot;,&#10;				&quot;version&quot;: &quot;1&quot;,&#10;				&quot;action&quot;: &quot;execute&quot;,&#10;				&quot;action_parameters&quot;: {&#10;					&quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;,&#10;					&quot;version&quot;: &quot;latest&quot;&#10;				},&#10;				&quot;expression&quot;: &quot;true&quot;,&#10;				&quot;description&quot;: &quot;Execute Cloudflare Managed Ruleset on my phase entry point ruleset&quot;,&#10;				&quot;last_updated&quot;: &quot;2025-03-21T11:02:08.769537Z&quot;,&#10;				&quot;ref&quot;: &quot;&lt;RULE_REF_1&gt;&quot;,&#10;				&quot;enabled&quot;: true&#10;			}&#10;		],&#10;		&quot;last_updated&quot;: &quot;2025-03-21T11:02:08.769537Z&quot;,&#10;		&quot;phase&quot;: &quot;http_request_firewall_managed&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>For more information on deploying rulesets, refer to <a href="/ruleset-engine/basic-operations/deploy-rulesets/">Deploy rulesets</a>.</p>
<h2 id="example-update-ruleset-description">Example - Update ruleset description</h2>
<p>The following <code>PUT</code> request updates the description of an existing ruleset or phase entry point.</p>
<p>The response will include the complete ruleset definition, including all the rules.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13237.md")
</aside>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;description&quot;: &quot;My updated phase entry point ruleset&quot;&#10;}&#x27;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;RULESET_ID&gt;&quot;,&#10;		&quot;name&quot;: &quot;Zone entry point&quot;,&#10;		&quot;description&quot;: &quot;My updated phase entry point ruleset&quot;,&#10;		&quot;kind&quot;: &quot;zone&quot;,&#10;		&quot;version&quot;: &quot;4&quot;,&#10;		&quot;rules&quot;: [&#10;			// (...)&#10;		],&#10;		&quot;last_updated&quot;: &quot;2025-03-30T10:49:11.006109Z&quot;,&#10;		&quot;phase&quot;: &quot;http_request_firewall_managed&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
