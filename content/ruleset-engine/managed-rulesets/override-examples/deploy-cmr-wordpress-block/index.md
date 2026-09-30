<p>Follow the steps below to create a rule that executes a managed ruleset and defines an override for rules with a specific tag.</p>
<ol>
<li><a href="/ruleset-engine/basic-operations/deploy-rulesets/">Add a rule</a> to a phase entry point ruleset that executes a managed ruleset.</li>
<li><a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">Configure a tag override</a> that sets a specified action for all rules with a given tag.</li>
</ol>
<h2 id="zone-level-example">Zone-level example</h2>
<p>This example uses the <a href="/ruleset-engine/rulesets-api/update/">Update a zone entry point ruleset</a> operation to perform the following two steps in a single <code>PUT</code> request:</p>
<ul>
<li>Set the list of rules in the <code>http_request_firewall_managed</code> phase entry point ruleset to a single rule that executes the <a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/">Cloudflare Managed Ruleset</a>.</li>
<li>Override rules with the <code>wordpress</code> tag to set the action to <code>block</code>. All other rules use the default action provided by the ruleset issuer.</li>
</ul>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/{ruleset_phase}/entrypoint \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;expression&quot;: &quot;true&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;,&#10;        &quot;overrides&quot;: {&#10;          &quot;categories&quot;: [&#10;            {&#10;              &quot;category&quot;: &quot;wordpress&quot;,&#10;              &quot;action&quot;: &quot;block&quot;&#10;            }&#10;          ]&#10;        }&#10;      }&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<h2 id="account-level-example">Account-level example</h2>
<p>This example uses the <a href="/ruleset-engine/rulesets-api/update/">Update an account entry point ruleset</a> operation to perform the following two steps in a single <code>PUT</code> request:</p>
<ul>
<li>Set the list of rules in the <code>http_request_firewall_managed</code> phase entry point ruleset to a single rule that executes the <a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/">Cloudflare Managed Ruleset</a> for the zone <code>example.com</code>.</li>
<li>Override rules with the <code>wordpress</code> tag to set the action to <code>block</code>. All other rules use the default action provided by the ruleset issuer.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13295.md")
</aside>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets/phases/{ruleset_phase}/entrypoint \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;expression&quot;: &quot;cf.zone.name eq \&quot;example.com\&quot; and cf.zone.plan eq \&quot;ENT\&quot;&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;&lt;MANAGED_RULESET_ID&gt;&quot;,&#10;        &quot;overrides&quot;: {&#10;          &quot;categories&quot;: [&#10;            {&#10;              &quot;category&quot;: &quot;wordpress&quot;,&#10;              &quot;action&quot;: &quot;block&quot;&#10;            }&#10;          ]&#10;        }&#10;      }&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
