<p>Configure the HTTP DDoS Attack Protection managed ruleset by defining overrides using the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a>.</p>
<p>Each zone has the HTTP DDoS Attack Protection managed ruleset enabled by default. This means that you do not need to deploy the managed ruleset to the <code>ddos_l7</code> phase ruleset explicitly. You only have to create a rule in the phase ruleset to deploy the managed ruleset if you need to configure overrides.</p>
<p>If you are using Terraform, refer to <a href="/terraform/additional-configurations/ddos-managed-rulesets/#example-configure-http-ddos-attack-protection">DDoS managed rulesets configuration using Terraform</a>.</p>
<h2 id="configure-an-override-for-the-http-ddos-attack-protection-managed-ruleset">Configure an override for the HTTP DDoS Attack Protection managed ruleset</h2>
<p>Use overrides to configure the HTTP DDoS Attack Protection managed ruleset. Overrides allow you to define a different action or sensitivity level from the default values. For more information on the available action and sensitivity level values, refer to <a href="/ddos-protection/managed-rulesets/http/override-parameters/">Ruleset parameters</a>.</p>
<p>Overrides can have a ruleset, tag, or rule scope. Tag and rule configurations have greater priority than ruleset configurations.</p>
<p>You can create overrides at the zone level and at the account level. Account-level overrides allow you to apply the same override to several zones in your account with a single rule. For example, you can use an account-level override to lower the sensitivity of a specific managed ruleset rule or exclude an <a href="/waf/tools/lists/custom-lists/#ip-lists">IP list</a> for multiple zones. However, if a given zone has overrides for the HTTP DDoS Attack Protection managed ruleset, the account-level overrides will not be evaluated for that zone.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/7539.md")
</aside>
<h3 id="creating-multiple-rules">Creating multiple rules</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7538.md")
</aside>
<p>Create multiple rules in the <code>ddos_l7</code> phase entry point ruleset to define different overrides for different sets of incoming requests. Set each rule expression according to the traffic whose HTTP DDoS protection you wish to customize.</p>
<p>Rules in the phase entry point ruleset, where you create overrides, are evaluated in order until there is a match for a rule expression and sensitivity level, and Cloudflare will apply the first rule that matches the request. Therefore, the rule order in the entry point ruleset is very important.</p>
<h2 id="example-api-calls">Example API calls</h2>
<h3 id="zone-level-configuration-example">Zone-level configuration example</h3>
<p>The following <code>PUT</code> example creates a new phase ruleset (or updates the existing one) for the <code>ddos_l7</code> phase at the zone level. The request includes several overrides to adjust the default behavior of the HTTP DDoS Attack Protection managed ruleset. These overrides are the following:</p>
<ul>
<li>All rules of the managed ruleset will use the <code>managed_challenge</code> action and have a sensitivity level of <code>medium</code>.</li>
<li>All rules tagged with <code>&lt;TAG_NAME&gt;</code> will have a sensitivity level of <code>low</code>.</li>
<li>The rule with ID <code>&lt;MANAGED_RULESET_RULE_ID&gt;</code> will use the <code>block</code> action.</li>
</ul>
<pre><code class="language-bash">curl --request PUT \&#10;https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/ddos_l7/entrypoint \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;description&quot;: &quot;Execute HTTP DDoS Attack Protection managed ruleset in the zone-level phase entry point ruleset&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;,&#10;        &quot;overrides&quot;: {&#10;          &quot;sensitivity_level&quot;: &quot;medium&quot;,&#10;          &quot;action&quot;: &quot;managed_challenge&quot;,&#10;          &quot;categories&quot;: [&#10;            {&#10;              &quot;category&quot;: &quot;&lt;TAG_NAME&gt;&quot;,&#10;              &quot;sensitivity_level&quot;: &quot;low&quot;&#10;            }&#10;          ],&#10;          &quot;rules&quot;: [&#10;            {&#10;              &quot;id&quot;: &quot;&lt;MANAGED_RULESET_RULE_ID&gt;&quot;,&#10;              &quot;action&quot;: &quot;block&quot;&#10;            }&#10;          ]&#10;        }&#10;      },&#10;      &quot;expression&quot;: &quot;true&quot;&#10;    }&#10;  ]&#10;}&#x27;&#10;</code></pre>
<p>The response returns the created (or updated) phase entry point ruleset.</p>
<details class="nb-details"><summary>Response</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7540.md")
</div></details>
<p>For more information on defining overrides for managed rulesets using the Rulesets API, refer to <a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">Override a managed ruleset</a> in the Ruleset Engine documentation.</p>
<h3 id="account-level-configuration-example">Account-level configuration example</h3>
<p>The following <code>PUT</code> example creates a new phase ruleset (or updates the existing one) for the <code>ddos_l7</code> phase at the account level. The example defines a single rule override for requests coming from IP addresses in the <code>allowlisted_ips</code> <a href="/waf/tools/lists/custom-lists/#ip-lists">IP list</a>, with the following configuration:</p>
<ul>
<li>The rule with ID <code>&lt;MANAGED_RULESET_RULE_ID&gt;</code>, belonging to the HTTP DDoS Attack Protection managed ruleset (with ID <code>&lt;MANAGED_RULESET_ID&gt;</code>), will have an <code>eoff</code> (<em>Essentially Off</em>) sensitivity level and it will perform a <code>log</code> action.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7537.md")
</aside>
<pre><code class="language-bash">curl --request PUT \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets/phases/ddos_l7/entrypoint \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;description&quot;: &quot;Disable a managed ruleset rule for allowlisted IP addresses&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;expression&quot;: &quot;ip.src in $allowlisted_ips&quot;,&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;,&#10;        &quot;overrides&quot;: {&#10;          &quot;rules&quot;: [&#10;            {&#10;              &quot;id&quot;: &quot;&lt;MANAGED_RULESET_RULE_ID&gt;&quot;,&#10;              &quot;action&quot;: &quot;log&quot;,&#10;              &quot;sensitivity_level&quot;: &quot;eoff&quot;&#10;            }&#10;          ]&#10;        }&#10;      }&#10;    }&#10;  ]&#10;}&#x27;&#10;</code></pre>
<p>The response returns the created (or updated) phase entry point ruleset.</p>
<details class="nb-details"><summary>Response</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7541.md")
</div></details>
<p>For more information on defining overrides for managed rulesets using the Rulesets API, refer to <a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">Override a managed ruleset</a> in the Ruleset Engine documentation.</p>
