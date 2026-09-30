<p>To customize the behavior of a managed ruleset via API, override the ruleset at deployment. When you override a ruleset you specify changes to be executed on top of the default configuration. These changes take precedence over the ruleset's default behavior.</p>
<p>For example, to test a managed ruleset before enforcing it, consider executing the ruleset with all rules set to <code>log</code> instead of their default actions. To do this, override the configured behavior of the managed ruleset at the ruleset level, so that each rule uses the <code>log</code> action.</p>
<p>If you are using Terraform, refer to the following pages:</p>
<ul>
<li><a href="/terraform/additional-configurations/waf-managed-rulesets/#configure-overrides">WAF Managed Rules configuration using Terraform</a></li>
<li><a href="/terraform/additional-configurations/ddos-managed-rulesets/">DDoS managed rulesets configuration using Terraform</a></li>
</ul>
<p>To define overrides in the Cloudflare dashboard, refer to the following resources:</p>
<ul>
<li><a href="/waf/managed-rules/deploy-zone-dashboard/#configure-a-managed-ruleset">Configure a WAF managed ruleset in the dashboard</a></li>
<li><a href="/ddos-protection/managed-rulesets/http/http-overrides/configure-dashboard/">Configure HTTP DDoS Attack Protection in the dashboard</a></li>
<li><a href="/ddos-protection/managed-rulesets/network/network-overrides/configure-dashboard/">Configure Network-layer DDoS Attack Protection in the dashboard</a></li>
</ul>
<h2 id="work-with-overrides">Work with overrides</h2>
<p>You can override a ruleset at three levels:</p>
<ul>
<li><strong>Ruleset overrides</strong> apply to all rules in the executed ruleset.</li>
<li><strong>Tag overrides</strong> apply to all rules with a specific tag. For example, use a tag override to customize the Cloudflare Managed Ruleset so all rules with the <code>wordpress</code> tag are set to <em>Block</em>. If multiple tags have overrides and if a given rule has more than one of these tags, the tag overrides order determines the behavior. For rules tagged with multiple overridden tags, the last tag's overrides apply.</li>
<li><strong>Rule overrides</strong> apply to specific rules in a managed ruleset, referenced by their Rule ID.</li>
</ul>
<p>Specific overrides take precedence over more general ones, and rule overrides take precedence over tag overrides, which take precedence over ruleset overrides.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/13273.md")
</aside>
<p>To apply an override for a managed ruleset:</p>
<ol>
<li>Use one of the <a href="/ruleset-engine/rulesets-api/update/">update ruleset operations</a> to update your phase entry point ruleset.</li>
<li>Specify the <code>overrides</code> in the <code>action_parameters</code> of the rule that executes your managed ruleset.</li>
</ol>
<pre><code class="language-json">&quot;action_parameters&quot;: {&#10;  &quot;id&quot;: &quot;&lt;RULESET_ID&gt;&quot;,&#10;  &quot;overrides&quot;: {&#10;    // ruleset overrides&#10;    &quot;property-to-modify&quot;: &quot;value&quot;,&#10;    &quot;property-to-modify&quot;: &quot;value&quot;,&#10;    // tag overrides&#10;    &quot;categories&quot;: [&#10;      {&#10;        &quot;category&quot;: &quot;&lt;TAG_NAME&gt;&quot;,&#10;        &quot;property-to-modify&quot;: &quot;value&quot;,&#10;        &quot;property-to-modify&quot;: &quot;value&quot;&#10;      }&#10;    ],&#10;    // rule overrides&#10;    &quot;rules&quot;: [&#10;      {&#10;        &quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;,&#10;        &quot;property-to-modify&quot;: &quot;value&quot;,&#10;        &quot;property-to-modify&quot;: &quot;value&quot;&#10;      }&#10;    ]&#10;  }&#10;}&#10;</code></pre>
<p>You can override the following rule properties:</p>
<ul>
<li><code>&quot;action&quot;</code></li>
<li><code>&quot;enabled&quot;</code></li>
</ul>
<p>Some managed rulesets may have additional override requirements, or they may allow you to override other rule properties. Check each Cloudflare product’s documentation for details.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important-1">Important</h3>
@markup("md", "content/.markup/bodies/13272.md")
</aside>
<h2 id="examples">Examples</h2>
<h3 id="rule-override-example">Rule override example</h3>
<p>The following <code>PUT</code> request adds a rule that executes a managed ruleset in the <code>http_request_firewall_managed</code> phase at the zone level, and defines a rule override to enable rule <code>&lt;RULE_ID&gt;</code> and set its action to <code>log</code>.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/{ruleset_phase}/entrypoint \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;description&quot;: &quot;Deploy managed ruleset, enabling a specific rule with log action&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;expression&quot;: &quot;true&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;,&#10;        &quot;overrides&quot;: {&#10;          &quot;rules&quot;: [&#10;            {&#10;              &quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;,&#10;              &quot;enabled&quot;: true,&#10;              &quot;action&quot;: &quot;log&quot;&#10;            }&#10;          ]&#10;        }&#10;      }&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<h3 id="ruleset-override-example">Ruleset override example</h3>
<p>The following <code>PUT</code> request adds a rule that executes a managed ruleset in the <code>http_request_firewall_managed</code> phase at the account level, and defines a ruleset override that sets the action to <code>log</code> for all (enabled) rules.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets/phases/{ruleset_phase}/entrypoint \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;description&quot;: &quot;Deploy managed ruleset for example.com, overriding the rules action to log&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;expression&quot;: &quot;(cf.zone.name eq \&quot;example.com\&quot;) and cf.zone.plan eq \&quot;ENT\&quot;&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;,&#10;        &quot;overrides&quot;: {&#10;          &quot;action&quot;: &quot;log&quot;&#10;        }&#10;      }&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<h2 id="more-resources">More resources</h2>
<p>For additional examples of configuring overrides via API, refer to <a href="/ruleset-engine/managed-rulesets/override-examples/">Override examples</a>.</p>
