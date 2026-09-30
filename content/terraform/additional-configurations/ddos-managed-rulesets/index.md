<p>This page provides examples of configuring <a href="/ddos-protection/managed-rulesets/">DDoS managed rulesets</a> in your zone or account using Terraform. It covers the following configurations:</p>
<ul>
<li><a href="#example-configure-http-ddos-attack-protection">Example: Configure HTTP DDoS Attack Protection</a></li>
<li><a href="#example-configure-network-layer-ddos-attack-protection">Example: Configure Network-layer DDoS Attack Protection</a></li>
<li><a href="#use-case-mitigate-large-http-ddos-attacks-and-monitor-flagged-traffic">Use case: Mitigate large HTTP DDoS attacks and monitor flagged traffic</a></li>
</ul>
<p>DDoS managed rulesets are always enabled. Depending on your Cloudflare services, you may be able to adjust their behavior.</p>
<p>If you are using the Cloudflare API, refer to the following resources:</p>
<ul>
<li><a href="/ddos-protection/managed-rulesets/http/http-overrides/configure-api/">Configure HTTP DDoS Attack Protection via API</a></li>
<li><a href="/ddos-protection/managed-rulesets/network/network-overrides/configure-api/">Configure Network-layer DDoS Attack Protection via API</a></li>
</ul>
<p>For more information on deploying and configuring rulesets using the Rulesets API, refer to <a href="/ruleset-engine/managed-rulesets/">Work with managed rulesets</a> in the Ruleset Engine documentation.</p>
<h2 id="before-you-start">Before you start</h2>
<h3 id="obtain-the-necessary-account-zone-and-managed-ruleset-ids">Obtain the necessary account, zone, and managed ruleset IDs</h3>
<p>The Terraform configurations provided in this page need the zone ID (or account ID) of the zone/account where you will deploy the managed rulesets.</p>
<ul>
<li>To retrieve the list of accounts you have access to, including their IDs, use the <a href="/api/resources/accounts/methods/list/">List accounts</a> operation.</li>
<li>To retrieve the list of zones you have access to, including their IDs, use the <a href="/api/resources/zones/methods/list/">List zones</a> operation.</li>
</ul>
<p>The deployment of managed rulesets via Terraform requires that you use the ruleset IDs. To find the IDs of managed rulesets, use the <a href="/api/resources/rulesets/methods/list/">List account rulesets</a> operation. The response will include the description and IDs of existing managed rulesets.</p>
<h3 id="optional-delete-existing-rulesets-to-start-from-scratch">(Optional) Delete existing rulesets to start from scratch</h3>
<p>Terraform assumes that it has complete control over account and zone rulesets. If you already have rulesets configured in your account or zone, do one of the following:</p>
<ul>
<li><a href="/terraform/advanced-topics/import-cloudflare-resources/">Import existing rulesets to Terraform</a> using the <code>cf-terraforming</code> tool. Recent versions of the tool can generate resource definitions for existing rulesets and import their configuration to Terraform state.</li>
<li>Start from scratch by <a href="/ruleset-engine/rulesets-api/delete/#delete-ruleset">deleting existing rulesets</a> (account and zone rulesets with <code>&quot;kind&quot;: &quot;root&quot;</code> and <code>&quot;kind&quot;: &quot;zone&quot;</code>, respectively) and then defining your rulesets configuration in Terraform.</li>
</ul>
<hr />
<h2 id="example-configure-http-ddos-attack-protection">Example: Configure HTTP DDoS Attack Protection</h2>
<p>This example configures the <a href="/ddos-protection/managed-rulesets/http/">HTTP DDoS Attack Protection</a> managed ruleset for a zone using Terraform.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14847.md")
</div></div>
<p>For more information about HTTP DDoS Attack Protection, refer to <a href="/ddos-protection/managed-rulesets/http/">HTTP DDoS Attack Protection managed ruleset</a>.</p>
<h2 id="example-configure-network-layer-ddos-attack-protection">Example: Configure Network-layer DDoS Attack Protection</h2>
<p>This example configures the <a href="/ddos-protection/managed-rulesets/network/">Network-layer DDoS Attack Protection</a> managed ruleset for an account using Terraform, changing the sensitivity level of rule with ID <code class="nb-rule-id" title="599dab0942ff4898ac1b7797e954e98b">e954e98b</code> to <code>low</code> using an override.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/14843.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14851.md")
</div></div>
<p>For more information about Network-layer DDoS Attack Protection, refer to <a href="/ddos-protection/managed-rulesets/network/">Network-layer DDoS Attack Protection managed ruleset</a>.</p>
<hr />
<h2 id="use-case-mitigate-large-http-ddos-attacks-and-monitor-flagged-traffic">Use case: Mitigate large HTTP DDoS attacks and monitor flagged traffic</h2>
<p>In the following example, a customer is concerned about false positives, but wants to get protection against large HTTP DDoS attacks. The two rules, containing two overrides each, in their <a href="/ddos-protection/managed-rulesets/http/">HTTP DDoS protection</a> configuration will have the following behavior:</p>
<ol>
<li>Mitigate any large HTTP DDoS attacks by configuring a rule with a <em>Low</em> <a href="/ddos-protection/managed-rulesets/http/override-parameters/#sensitivity-level">sensitivity level</a> and a <em>Block</em> action.</li>
<li>Monitor traffic being flagged by the DDoS protection system by configuring a rule with the default sensitivity level (<em>High</em>) and a <em>Log</em> action.</li>
</ol>
<p>The order of the rules is important: the rule with the highest sensitivity level must come after the rule with the lowest sensitivity level, otherwise it will never be evaluated.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important-considerations">Important considerations</h3>
@markup("md", "content/.markup/bodies/14842.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14855.md")
</div></div>
