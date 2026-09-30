<p>This page provides examples of creating <a href="/waf/custom-rules/">WAF custom rules</a> in a zone or account using Terraform. The examples cover the following scenarios:</p>
<ul>
<li><a href="#add-a-custom-rule-to-a-zone">Add a custom rule to a zone</a></li>
<li><a href="#create-and-deploy-a-custom-ruleset">Create and deploy a custom ruleset</a></li>
</ul>
<p>The WAF documentation includes additional Terraform examples — refer to <a href="#more-resources">More resources</a>.</p>
<p>If you are using the Cloudflare API, refer to the following resources in the WAF documentation:</p>
<ul>
<li><a href="/waf/custom-rules/create-api/">Create a custom rule via API</a></li>
<li><a href="/waf/account/custom-rulesets/create-api/">Create a custom ruleset using the API</a></li>
</ul>
<p>For more information on deploying and configuring custom rulesets using the Rulesets API, refer to <a href="/ruleset-engine/custom-rulesets/">Work with custom rulesets</a> in the Ruleset Engine documentation.</p>
<h2 id="before-you-start">Before you start</h2>
<h3 id="obtain-the-necessary-account-or-zone-ids">Obtain the necessary account or zone IDs</h3>
<p>The Terraform configurations provided in this page need the zone ID (or account ID) of the zone/account where you will deploy rulesets.</p>
<ul>
<li>To retrieve the list of accounts you have access to, including their IDs, use the <a href="/api/resources/accounts/methods/list/">List accounts</a> operation.</li>
<li>To retrieve the list of zones you have access to, including their IDs, use the <a href="/api/resources/zones/methods/list/">List zones</a> operation.</li>
</ul>
<h3 id="import-or-delete-existing-rulesets">Import or delete existing rulesets</h3>
<p>Terraform assumes that it has complete control over account and zone rulesets. If you already have rulesets configured in your account or zone, do one of the following:</p>
<ul>
<li><a href="/terraform/advanced-topics/import-cloudflare-resources/">Import existing rulesets to Terraform</a> using the <code>cf-terraforming</code> tool. Recent versions of the tool can generate resource definitions for existing rulesets and import their configuration to Terraform state.</li>
<li>Start from scratch by <a href="/ruleset-engine/rulesets-api/delete/#delete-ruleset">deleting existing rulesets</a> (account and zone rulesets with <code>&quot;kind&quot;: &quot;root&quot;</code> and <code>&quot;kind&quot;: &quot;zone&quot;</code>, respectively) and then defining your rulesets configuration in Terraform.</li>
</ul>
<hr />
<h2 id="add-a-custom-rule-to-a-zone">Add a custom rule to a zone</h2>
<p>The following example configures a custom rule in the zone entry point ruleset for the <code>http_request_firewall_custom</code> phase for zone with ID <code>&lt;ZONE_ID&gt;</code>. The rule will block all traffic on non-standard HTTP(S) ports:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14802.md")
</div></div>
<br />
<h2 id="create-and-deploy-a-custom-ruleset">Create and deploy a custom ruleset</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14798.md")
</aside>
<p>The following example creates a <a href="/ruleset-engine/custom-rulesets/">custom ruleset</a> in the account with ID <code>&lt;ACCOUNT_ID&gt;</code> containing a single custom rule. This custom ruleset is then deployed using a separate <code>cloudflare_ruleset</code> Terraform resource. If you do not deploy a custom ruleset, it will not execute.</p>
<p>The following configuration creates a custom ruleset with a single rule:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14806.md")
</div></div>
<br />
<p>The following configuration deploys the custom ruleset at the account level. It defines a dependency on the <code>account_firewall_custom_ruleset</code> resource and uses the ID of the created custom ruleset in <code>action_parameters</code>:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14810.md")
</div></div>
<p>For more information on configuring and deploying custom rulesets, refer to <a href="/ruleset-engine/custom-rulesets/">Work with custom rulesets</a> in the Ruleset Engine documentation.</p>
<h2 id="more-resources">More resources</h2>
<ul>
<li><a href="/waf/detections/malicious-uploads/terraform-examples/#add-a-custom-rule-to-block-malicious-uploads">Malicious uploads detection: Add a custom rule to block malicious uploads</a></li>
<li><a href="/waf/detections/leaked-credentials/terraform-examples/#add-a-custom-rule-to-challenge-requests-with-leaked-credentials">Leaked credentials detection: Add a custom rule to challenge requests with leaked credentials</a></li>
</ul>
