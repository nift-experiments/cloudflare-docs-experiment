<p>This page provides examples of creating <a href="/waf/rate-limiting-rules/">rate limiting rules</a> in a zone or account using Terraform.</p>
<p>If you are using the Cloudflare API, refer to the following resources:</p>
<ul>
<li><a href="/waf/rate-limiting-rules/create-api/">Create a rate limiting rule via API</a></li>
<li><a href="/waf/account/rate-limiting-rulesets/create-api/">Create a rate limiting ruleset via API</a></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14829.md")
</aside>
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
<h2 id="create-a-rate-limiting-rule-at-the-zone-level">Create a rate limiting rule at the zone level</h2>
<p>This example creates a rate limiting rule in zone with ID <code>&lt;ZONE_ID&gt;</code> blocking traffic that exceeds the configured rate:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14833.md")
</div></div>
<br />
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="use-a-single-ruleset-resource-per-phase">Use a single ruleset resource per phase</h3>
@markup("md", "content/.markup/bodies/14828.md")
</aside>
<h2 id="create-a-rate-limiting-rule-at-the-account-level">Create a rate limiting rule at the account level</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/14827.md")
</aside>
<p>This example defines a <a href="/ruleset-engine/custom-rulesets/">custom ruleset</a> with a single rate limiting rule in account with ID <code>&lt;ACCOUNT_ID&gt;</code> that blocks traffic for the <code>/api/</code> path exceeding the configured rate. The second <code>cloudflare_ruleset</code> resource defines an <code>execute</code> rule that deploys the custom ruleset for traffic addressed at <code>example.com</code>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14837.md")
</div></div>
<br />
<h2 id="create-an-advanced-rate-limiting-rule">Create an advanced rate limiting rule</h2>
<p>This example creates a rate limiting rule in zone with ID <code>&lt;ZONE_ID&gt;</code> with:</p>
<ul>
<li>A custom counting expression that includes a response field (<code>http.response.code</code>).</li>
<li>A custom JSON response for rate limited requests.</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14841.md")
</div></div>
<br />
