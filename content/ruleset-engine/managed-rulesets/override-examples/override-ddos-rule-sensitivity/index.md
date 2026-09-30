<p>Follow the steps below to override the sensitivity of a specific rule of the Cloudflare HTTP DDoS Attack Protection managed ruleset.</p>
<ol>
<li><a href="/ruleset-engine/basic-operations/deploy-rulesets/">Add a rule</a> to a phase to deploy the Cloudflare HTTP DDoS Attack Protection managed ruleset. You only need to deploy this specific ruleset when you wish to define one or more overrides, since it is enabled by default.</li>
<li><a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">Configure a rule override</a> that sets the <code>sensitivity_level</code> of a specific rule.</li>
</ol>
<h2 id="example">Example</h2>
<p>The following example uses the <a href="/ruleset-engine/rulesets-api/update/">Update a zone entry point ruleset</a> operation to execute the two steps in a single <code>PUT</code> request.</p>
<ul>
<li>Set the rules in the <code>ddos_l7</code> phase entry point ruleset to a single rule that executes the Cloudflare HTTP DDoS Attack Protection managed ruleset (with ID <code>&lt;HTTP_DDOS_RULESET_ID&gt;</code>).</li>
<li>Create an override for the rule with ID <code>&lt;RULE_ID&gt;</code> and set the rule sensitivity to <code>low</code>. All other rules use the default sensitivity defined by Cloudflare.</li>
</ul>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/{ruleset_phase}/entrypoint \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;expression&quot;: &quot;true&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;&lt;HTTP_DDOS_RULESET_ID&gt;&quot;,&#10;        &quot;overrides&quot;: {&#10;          &quot;rules&quot;: [&#10;            {&#10;              &quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;,&#10;              &quot;sensitivity_level&quot;: &quot;low&quot;&#10;            }&#10;          ]&#10;        }&#10;      }&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
