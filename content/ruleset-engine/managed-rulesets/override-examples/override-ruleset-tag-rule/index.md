<p>Customize the execution of managed rulesets with a combination of ruleset overrides, tag overrides, and rule overrides in your phase entry point ruleset.</p>
<ol>
<li><a href="/ruleset-engine/basic-operations/deploy-rulesets/">Add a rule</a> to a phase entry point ruleset to execute a managed ruleset.</li>
<li><a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">Configure a ruleset override</a> that disables all rules in the managed ruleset.</li>
<li><a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">Configure a tag override</a> that sets an action for rules with a given tag.</li>
<li><a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">Configure a rule override</a> that sets an action for the rules you want to execute.</li>
</ol>
<h2 id="zone-level-example">Zone-level example</h2>
<p>This example uses the <a href="/ruleset-engine/rulesets-api/update/">Update a zone entry point ruleset</a> operation to execute the following in a single <code>PUT</code> request:</p>
<ul>
<li>Add a rule to the <code>http_request_firewall_managed</code> phase entry point ruleset that executes a managed ruleset.</li>
<li>Use category overrides to enable rules with <code>wordpress</code> and <code>drupal</code> tags and set their actions to <code>log</code>.</li>
<li>Add a rule override that enables a single rule.</li>
</ul>
<p>In this example:</p>
<ul>
<li><code>&quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;</code> defines the managed ruleset to execute for requests addressed to a zone (<code>$ZONE_ID</code>).</li>
<li><code>&quot;enabled&quot;: false</code> defines an override at the ruleset level to disable all rules in the managed ruleset.</li>
<li><code>&quot;categories&quot;: [{&quot;category&quot;: &quot;wordpress&quot;, &quot;action&quot;: &quot;log&quot;, &quot;enabled&quot;: true}, {&quot;category&quot;: &quot;drupal&quot;, &quot;action&quot;: &quot;log&quot;, &quot;enabled&quot;: true}]</code> defines an override at the tag level to enable rules tagged with <code>wordpress</code> or <code>drupal</code> and sets their action to <code>log</code>.</li>
<li><code>&quot;rules&quot;: [{&quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;, &quot;action&quot;: &quot;block&quot;, &quot;enabled&quot;: true}]</code> defines an override at the rule level that enables one individual rule and sets the action to <code>block</code>.</li>
</ul>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/{ruleset_phase}/entrypoint \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;expression&quot;: &quot;true&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;,&#10;        &quot;overrides&quot;: {&#10;          &quot;enabled&quot;: false,&#10;          &quot;categories&quot;: [&#10;            {&#10;              &quot;category&quot;: &quot;wordpress&quot;,&#10;              &quot;action&quot;: &quot;log&quot;,&#10;              &quot;enabled&quot;: true&#10;            },&#10;            {&#10;              &quot;category&quot;: &quot;drupal&quot;,&#10;              &quot;action&quot;: &quot;log&quot;,&#10;              &quot;enabled&quot;: true&#10;            }&#10;          ],&#10;          &quot;rules&quot;: [&#10;            {&#10;              &quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;,&#10;              &quot;action&quot;: &quot;block&quot;,&#10;              &quot;enabled&quot;: true&#10;            }&#10;          ]&#10;        }&#10;      }&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<h2 id="account-level-example">Account-level example</h2>
<p>This example uses the <a href="/ruleset-engine/rulesets-api/update/">Update an account entry point ruleset</a> operation to execute the following in a single <code>PUT</code> request:</p>
<ul>
<li>Add a rule to the <code>http_request_firewall_managed</code> phase entry point ruleset that executes a managed ruleset for the zone <code>example.com</code>.</li>
<li>Use category overrides to enable rules with <code>wordpress</code> and <code>drupal</code> tags and set their actions to <code>log</code>.</li>
<li>Add a rule override that enables a single rule.</li>
</ul>
<p>In this example:</p>
<ul>
<li><code>&quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;</code> defines the managed ruleset to execute for requests addressed to <code>example.com</code>.</li>
<li><code>&quot;enabled&quot;: false</code> defines an override at the ruleset level to disable all rules in the managed ruleset.</li>
<li><code>&quot;categories&quot;: [{&quot;category&quot;: &quot;wordpress&quot;, &quot;action&quot;: &quot;log&quot;, &quot;enabled&quot;: true}, {&quot;category&quot;: &quot;drupal&quot;, &quot;action&quot;: &quot;log&quot;, &quot;enabled&quot;: true}]</code> defines an override at the tag level to enable rules tagged with <code>wordpress</code> or <code>drupal</code> and sets their action to <code>log</code>.</li>
<li><code>&quot;rules&quot;: [{&quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;, &quot;action&quot;: &quot;block&quot;, &quot;enabled&quot;: true}]</code> defines an override at the rule level that enables one individual rule and sets the action to <code>block</code>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13293.md")
</aside>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets/phases/{ruleset_phase}/entrypoint \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;expression&quot;: &quot;cf.zone.name eq \&quot;example.com\&quot; and cf.zone.plan eq \&quot;ENT\&quot;&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;,&#10;        &quot;overrides&quot;: {&#10;          &quot;enabled&quot;: false,&#10;          &quot;categories&quot;: [&#10;            {&#10;              &quot;category&quot;: &quot;wordpress&quot;,&#10;              &quot;action&quot;: &quot;log&quot;,&#10;              &quot;enabled&quot;: true&#10;            },&#10;            {&#10;              &quot;category&quot;: &quot;drupal&quot;,&#10;              &quot;action&quot;: &quot;log&quot;,&#10;              &quot;enabled&quot;: true&#10;            }&#10;          ],&#10;          &quot;rules&quot;: [&#10;            {&#10;              &quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;,&#10;              &quot;action&quot;: &quot;block&quot;,&#10;              &quot;enabled&quot;: true&#10;            }&#10;          ]&#10;        }&#10;      }&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
