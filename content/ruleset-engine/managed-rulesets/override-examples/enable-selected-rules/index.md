<p>Use a ruleset override and a rule override in a phase entry point ruleset to execute only selected rules in a managed ruleset.</p>
<ol>
<li><a href="/ruleset-engine/basic-operations/deploy-rulesets/">Add a rule</a> to a phase entry point ruleset that executes a managed ruleset.</li>
<li><a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">Configure a ruleset override</a> that disables all rules in the managed ruleset.</li>
<li><a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">Configure a rule override</a> to set an action for the rules you want to execute.</li>
</ol>
<h2 id="zone-level-example">Zone-level example</h2>
<p>The following <code>PUT</code> request uses the <a href="/ruleset-engine/rulesets-api/update/">Update a zone entry point ruleset</a> operation to define a configuration that executes only two rules from a managed ruleset in the <code>http_request_firewall_managed</code> phase.</p>
<p>In this example:</p>
<ul>
<li><code>&quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;</code> defines the managed ruleset to execute for requests in the specified zone (<code>$ZONE_ID</code>).</li>
<li><code>&quot;enabled&quot;: false</code> defines an override at the ruleset level to disable all rules in the managed ruleset.</li>
<li><code>&quot;rules&quot;: [{&quot;id&quot;: &quot;&lt;RULE_ID_1&gt;&quot;, &quot;action&quot;: &quot;block&quot;, &quot;enabled&quot;: true}, {&quot;id&quot;: &quot;&lt;RULE_ID_2&gt;&quot;, &quot;action&quot;: &quot;log&quot;, &quot;enabled&quot;: true}]</code> defines a list of overrides at the rule level to enable two individual rules.</li>
</ul>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/{ruleset_phase}/entrypoint \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;expression&quot;: &quot;true&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;,&#10;        &quot;overrides&quot;: {&#10;          &quot;enabled&quot;: false,&#10;          &quot;rules&quot;: [&#10;            {&#10;              &quot;id&quot;: &quot;&lt;RULE_ID_1&gt;&quot;,&#10;              &quot;action&quot;: &quot;block&quot;,&#10;              &quot;enabled&quot;: true&#10;            },&#10;            {&#10;              &quot;id&quot;: &quot;&lt;RULE_ID_2&gt;&quot;,&#10;              &quot;action&quot;: &quot;log&quot;,&#10;              &quot;enabled&quot;: true&#10;            }&#10;          ]&#10;        }&#10;      }&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<h2 id="account-level-example">Account-level example</h2>
<p>The following <code>PUT</code> request uses the <a href="/ruleset-engine/rulesets-api/update/">Update an account entry point ruleset</a> operation to define a configuration that executes only two rules from a managed ruleset in the <code>http_request_firewall_managed</code> phase.</p>
<p>In this example:</p>
<ul>
<li><code>&quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;</code> defines the managed ruleset to execute for requests addressed to <code>example.com</code>.</li>
<li><code>&quot;enabled&quot;: false</code> defines an override at the ruleset level to disable all rules in the managed ruleset.</li>
<li><code>&quot;rules&quot;: [{&quot;id&quot;: &quot;&lt;RULE_ID_1&gt;&quot;, &quot;action&quot;: &quot;block&quot;, &quot;enabled&quot;: true}, {&quot;id&quot;: &quot;&lt;RULE_ID_2&gt;&quot;, &quot;action&quot;: &quot;log&quot;, &quot;enabled&quot;: true}]</code> defines a list of overrides at the rule level to enable two individual rules.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13294.md")
</aside>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets/phases/{ruleset_phase}/entrypoint \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;expression&quot;: &quot;cf.zone.name eq \&quot;example.com\&quot; and cf.zone.plan eq \&quot;ENT\&quot;&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;,&#10;        &quot;overrides&quot;: {&#10;          &quot;enabled&quot;: false,&#10;          &quot;rules&quot;: [&#10;            {&#10;              &quot;id&quot;: &quot;&lt;RULE_ID_1&gt;&quot;,&#10;              &quot;action&quot;: &quot;block&quot;,&#10;              &quot;enabled&quot;: true&#10;            },&#10;            {&#10;              &quot;id&quot;: &quot;&lt;RULE_ID_2&gt;&quot;,&#10;              &quot;action&quot;: &quot;log&quot;,&#10;              &quot;enabled&quot;: true&#10;            }&#10;          ]&#10;        }&#10;      }&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
