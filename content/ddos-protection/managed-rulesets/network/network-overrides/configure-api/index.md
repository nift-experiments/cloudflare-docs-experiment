<p>Configure the Cloudflare Network-layer DDoS Attack Protection managed ruleset by defining overrides at the account level using the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a>.</p>
<p>Each account has the Network-layer DDoS Attack Protection managed ruleset enabled by default. This means that you do not need to deploy the managed ruleset to the <code>ddos_l4</code> phase entry point ruleset explicitly. You only have to create a rule in the phase entry point to deploy the managed ruleset if you need to configure overrides.</p>
<p>If you are using Terraform, refer to <a href="/terraform/additional-configurations/ddos-managed-rulesets/#example-configure-network-layer-ddos-attack-protection">DDoS managed rulesets configuration using Terraform</a>.</p>
<h2 id="configure-an-override-for-the-network-layer-ddos-attack-protection-managed-ruleset">Configure an override for the Network-layer DDoS Attack Protection managed ruleset</h2>
<p>You can define overrides at the ruleset, tag, and rule level for all managed rulesets.</p>
<p>When configuring the Network-layer DDoS Attack Protection managed ruleset, use overrides to define a different <strong>action</strong> or <strong>sensitivity</strong> from the default values. For more information on these rule parameters and the allowed values, refer to <a href="/ddos-protection/managed-rulesets/network/override-parameters/">Managed ruleset parameters</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/7549.md")
</aside>
<h2 id="example">Example</h2>
<p>The following <code>PUT</code> example creates a new phase ruleset (or updates the existing one) for the <code>ddos_l4</code> phase at the account level. The request includes several overrides to adjust the default behavior of the Network-layer DDoS Attack Protection managed ruleset. These overrides are the following:</p>
<ul>
<li>All rules of the Network-layer DDoS Attack Protection managed ruleset will have their sensitivity set to <code>medium</code>.</li>
<li>All rules tagged with <code>&lt;TAG_NAME&gt;</code> will have their sensitivity set to <code>low</code>.</li>
<li>The rule with ID <code>&lt;MANAGED_RULESET_RULE_ID&gt;</code> will use the <code>block</code> action.</li>
</ul>
<p>The overrides apply to all packets matching the rule expression: <code>ip.dst in { 1.1.1.0/24 }</code>.</p>
<pre><code class="language-bash">curl --request PUT \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets/phases/ddos_l4/entrypoint \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;description&quot;: &quot;Define overrides for the Network-layer DDoS Attack Protection managed ruleset&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;expression&quot;: &quot;ip.dst in { 1.1.1.0/24 }&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;,&#10;        &quot;overrides&quot;: {&#10;          &quot;sensitivity_level&quot;: &quot;medium&quot;,&#10;          &quot;categories&quot;: [&#10;            {&#10;              &quot;category&quot;: &quot;&lt;TAG_NAME&gt;&quot;,&#10;              &quot;sensitivity_level&quot;: &quot;low&quot;&#10;            }&#10;          ],&#10;          &quot;rules&quot;: [&#10;            {&#10;              &quot;id&quot;: &quot;&lt;MANAGED_RULESET_RULE_ID&gt;&quot;,&#10;              &quot;action&quot;: &quot;block&quot;&#10;            }&#10;          ]&#10;        }&#10;      }&#10;    }&#10;  ]&#10;}&#x27;&#10;</code></pre>
<p>The response returns the created (or updated) phase entry point ruleset.</p>
<details class="nb-details"><summary>Response</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7550.md")
</div></details>
<p>For more information on defining overrides for managed rulesets using the Rulesets API, refer to <a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">Override a managed ruleset</a>.</p>
