<pre><code>&quot;The available actions are: _Block_, _Log_, _Non-Interactive Challenge_, _Managed Challenge_, and _Interactive Challenge_.&quot;;&#10;</code></pre>
<p>Created by the Cloudflare security team, this ruleset provides fast and effective protection for all of your applications. The ruleset is updated frequently to cover new vulnerabilities and reduce false positives.</p>
<p>Cloudflare recommends that you enable the rules whose tags correspond to your technology stack. For example, if you use WordPress, enable the rules tagged with <code>wordpress</code>.</p>
<p>Cloudflare's <a href="/waf/change-log/">WAF changelog</a> allows you to monitor ongoing changes to the WAF's managed rulesets.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15614.md")
</aside>
<h2 id="deploy-the-cloudflare-managed-ruleset-deploy-in-the-dashboard">Deploy the Cloudflare Managed Ruleset </h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15615.md")
</div>
<p>This operation deploys the managed ruleset for the current zone, creating a new rule with the <em>Execute</em> action.</p>
<h2 id="configure-in-the-dashboard">Configure in the dashboard</h2>
<p>You can configure (or override) the Cloudflare Managed Ruleset, overriding its default configuration, at several levels:</p>
<ul>
<li><a href="#ruleset-level-configuration">Ruleset level</a></li>
<li><a href="#tag-level-configuration">Tag level</a></li>
<li><a href="#rule-level-configuration">Rule level</a></li>
</ul>
<p>When you create several overrides at different levels, more specific configurations (tag and rule level) have priority over less specific configurations (ruleset level). Refer to <a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">Override a managed ruleset</a> in the Ruleset Engine documentation for more information.</p>
<h3 id="ruleset-level-configuration">Ruleset-level configuration</h3>
<p>You can configure (or override) the following Cloudflare Managed Ruleset settings in the Cloudflare dashboard:</p>
<ul>
<li><strong>Scope</strong>: When you define a custom filter expression for the scope, the Cloudflare Managed Ruleset applies only to a subset of the incoming requests. By default, a managed ruleset deployed in the dashboard applies to all incoming traffic.</li>
<li><strong>Ruleset action</strong>: When you define an action for the ruleset, you override the default action defined for each rule. <p>availableActions</p>
To remove the action override at the ruleset level, set the ruleset action to <em>Default</em>.</li>
<li><strong>Ruleset status</strong>: Enables or disables all the rules in the ruleset.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15613.md")
</aside>
<ul>
<li><strong><a href="/waf/managed-rules/payload-logging/configure/">Payload logging</a></strong>: When enabled, logs the request information (payload) that triggered a specific rule of the managed ruleset. You must configure a public key to encrypt the payload.</li>
</ul>
<p>Once you have <a href="#deploy-in-the-dashboard">deployed the Cloudflare Managed Ruleset</a>, do the following to configure it in the dashboard:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15616.md")
</div>
<h3 id="tag-level-configuration">Tag-level configuration</h3>
<p>You can configure (or override) the following Cloudflare Managed Ruleset settings in the dashboard for rules tagged with at least one of the selected tags:</p>
<ul>
<li>
<p><strong>Rule action</strong>: Sets the rule action for all the rules with the selected tags. <p>availableActions</p></p>
</li>
<li>
<p><strong>Rule status</strong>: Sets the rule status for all the rules with the selected tags.</p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15612.md")
</aside>
<p>Once you have <a href="#deploy-in-the-dashboard">deployed the Cloudflare Managed Ruleset</a>, do the following to configure rules with specific tags in the dashboard:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15617.md")
</div>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15618.md")
</div>
<h3 id="rule-level-configuration">Rule-level configuration</h3>
<p>You can configure (or override) the following Cloudflare Managed Ruleset settings in the dashboard for the selected rules:</p>
<ul>
<li><strong>Rule action</strong>: Sets the action of a single rule or, if you select multiple rules, for the selected rules. <p>availableActions</p>
Once you have changed the configuration of a rule, you have the option to reset the configuration back to the default one as defined in the Cloudflare Managed Ruleset.</li>
<li><strong>Rule status</strong>: Sets the status (enabled or disabled) of a single rule or, if you select multiple rules, for the selected rules.</li>
</ul>
<p>Once you have <a href="#deploy-in-the-dashboard">deployed the Cloudflare Managed Ruleset</a>, do the following to configure individual ruleset rules in the dashboard:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15619.md")
</div>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15620.md")
</div>
<h2 id="configure-via-api">Configure via API</h2>
<p>To deploy the Cloudflare Managed Ruleset for a given zone via API, create a rule with <code>execute</code> action in the <a href="/ruleset-engine/about/rulesets/#entry-point-ruleset">entry point ruleset</a> for the <code>http_request_firewall_managed</code> phase.</p>
<h3 id="example">Example</h3>
<p>The following example deploys the <a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/">Cloudflare Managed Ruleset</a> to the <code>http_request_firewall_managed</code> phase of a given zone (<code>$ZONE_ID</code>) by creating a rule that executes the managed ruleset.</p>
<ol>
<li></li>
</ol>
<p>Invoke the <a href="/api/resources/rulesets/subresources/phases/methods/get/">Get a zone entry point ruleset</a> operation to obtain the definition of the entry point ruleset for the <code>http_request_firewall_managed</code> phase. You will need the <a href="/fundamentals/account/find-account-and-zone-ids/">zone ID</a> for this task.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/{ruleset_phase}/entrypoint \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;description&quot;: &quot;Zone-level phase entry point&quot;,&#10;		&quot;id&quot;: &quot;&lt;RULESET_ID&gt;&quot;,&#10;		&quot;kind&quot;: &quot;zone&quot;,&#10;		&quot;last_updated&quot;: &quot;2024-03-16T15:40:08.202335Z&quot;,&#10;		&quot;name&quot;: &quot;zone&quot;,&#10;		&quot;phase&quot;: &quot;http_request_firewall_managed&quot;,&#10;		&quot;rules&quot;: [&#10;			// ...&#10;		],&#10;		&quot;source&quot;: &quot;firewall_managed&quot;,&#10;		&quot;version&quot;: &quot;10&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<ol start="2">
<li></li>
</ol>
<p>If the entry point ruleset already exists (that is, if you received a <code>200 OK</code> status code and the ruleset definition), take note of the ruleset ID in the response. Then, invoke the <a href="/api/resources/rulesets/subresources/rules/methods/create/">Create a zone ruleset rule</a> operation to add an <code>execute</code> rule to the existing ruleset deploying the <p>Cloudflare Managed Ruleset (with ID �CODE11�)</p>
. By default, the rule will be added at the end of the list of rules already in the ruleset.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/{ruleset_id}/rules \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;action&quot;: &quot;execute&quot;,&#10;  &quot;action_parameters&quot;: {&#10;    &quot;id&quot;: &quot;efb7b8c949ac4650a09736fc376e9aee&quot;&#10;  },&#10;  &quot;expression&quot;: &quot;true&quot;,&#10;  &quot;description&quot;: &quot;Execute the Cloudflare Managed Ruleset&quot;&#10;}&#x27;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;id&quot;: &quot;&lt;RULESET_ID&gt;&quot;,&#10;		&quot;name&quot;: &quot;Zone-level phase entry point&quot;,&#10;		&quot;description&quot;: &quot;&quot;,&#10;		&quot;kind&quot;: &quot;zone&quot;,&#10;		&quot;version&quot;: &quot;11&quot;,&#10;		&quot;rules&quot;: [&#10;			// ... any existing rules&#10;			{&#10;				&quot;id&quot;: &quot;&lt;RULE_ID&gt;&quot;,&#10;				&quot;version&quot;: &quot;1&quot;,&#10;				&quot;action&quot;: &quot;execute&quot;,&#10;				&quot;action_parameters&quot;: {&#10;					&quot;id&quot;: &quot;efb7b8c949ac4650a09736fc376e9aee&quot;,&#10;					&quot;version&quot;: &quot;latest&quot;&#10;				},&#10;				&quot;expression&quot;: &quot;true&quot;,&#10;				&quot;description&quot;: &quot;Execute the Cloudflare Managed Ruleset&quot;,&#10;				&quot;last_updated&quot;: &quot;2024-03-18T18:08:14.003361Z&quot;,&#10;				&quot;ref&quot;: &quot;&lt;RULE_REF&gt;&quot;,&#10;				&quot;enabled&quot;: true&#10;			}&#10;		],&#10;		&quot;last_updated&quot;: &quot;2024-03-18T18:08:14.003361Z&quot;,&#10;		&quot;phase&quot;: &quot;http_request_firewall_managed&quot;&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<ol start="3">
<li></li>
</ol>
<p>If the entry point ruleset does not exist (that is, if you received a <code>404 Not Found</code> status code in step 1), create it using the <a href="/api/resources/rulesets/methods/create/">Create a zone ruleset</a> operation. Include a single rule in the <code>rules</code> array that executes the <p>Cloudflare Managed Ruleset (with ID �CODE14�)</p>
for <p>all incoming requests in the zone</p>
.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;My ruleset&quot;,&#10;  &quot;description&quot;: &quot;Entry point ruleset for WAF managed rulesets&quot;,&#10;  &quot;kind&quot;: &quot;zone&quot;,&#10;  &quot;phase&quot;: &quot;http_request_firewall_managed&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;execute&quot;,&#10;      &quot;action_parameters&quot;: {&#10;        &quot;id&quot;: &quot;efb7b8c949ac4650a09736fc376e9aee&quot;&#10;      },&#10;      &quot;expression&quot;: &quot;true&quot;,&#10;      &quot;description&quot;: &quot;Execute the Cloudflare Managed Ruleset&quot;&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<h3 id="next-steps">Next steps</h3>
<p>To configure the Cloudflare Managed Ruleset via API, create <a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">overrides</a> using the Rulesets API. You can perform the following configurations:</p>
<ul>
<pre><code>&lt;li&gt;&#10;	Specify the action to perform for all the rules in the ruleset by creating&#10;	a ruleset override.&#10;&lt;/li&gt;&#10;&lt;li&gt;&#10;	Disable or customize the action of individual rules by creating rule&#10;	overrides.&#10;&lt;/li&gt;&#10;</code></pre>
</ul>
<p>For examples of creating overrides using the API, refer to <a href="/ruleset-engine/managed-rulesets/override-managed-ruleset/">Override a managed ruleset</a>.</p>
<h3 id="more-resources">More resources</h3>
<p>For more information on working with managed rulesets via API, refer to <a href="/ruleset-engine/managed-rulesets/">Work with managed rulesets</a> in the Ruleset Engine documentation.</p>
<h2 id="configure-using-terraform">Configure using Terraform</h2>
<p>The following example deploys the Cloudflare Managed Ruleset for a zone and overrides the action and status of a specific rule.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15624.md")
</div></div>
<p>For more information, refer to <a href="/terraform/additional-configurations/waf-managed-rulesets/">WAF Managed Rules configuration using Terraform</a>.</p>
