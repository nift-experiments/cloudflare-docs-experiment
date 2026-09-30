<p>This page provides examples of creating <a href="/rules/transform/">Transform Rules</a> in a zone using Terraform. The examples cover the following scenarios:</p>
<ul>
<li><a href="#create-a-url-rewrite-rule">Create a URL rewrite rule</a></li>
<li><a href="#create-a-request-header-transform-rule">Create a request header transform rule</a></li>
<li><a href="#create-a-response-header-transform-rule">Create a response header transform rule</a></li>
<li><a href="#configure-managed-transforms">Configure Managed Transforms</a></li>
</ul>
<p>If you are using the Cloudflare API, refer to the following resources:</p>
<ul>
<li><a href="/rules/transform/url-rewrite/create-api/">Create a URL rewrite rule via API</a></li>
<li><a href="/rules/transform/request-header-modification/create-api/">Create a request header transform rule via API</a></li>
<li><a href="/rules/transform/response-header-modification/create-api/">Create a response header transform rule via API</a></li>
<li><a href="/rules/transform/managed-transforms/configure/">Configure Managed Transforms</a></li>
</ul>
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
<h2 id="create-a-url-rewrite-rule">Create a URL rewrite rule</h2>
<p>The following example creates a URL rewrite rule that rewrites requests for <code>example.com/old-folder</code> to <code>example.com/new-folder</code>:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14814.md")
</div></div>
<p>Use the <code>ref</code> field to get stable rule IDs across updates when using Terraform. Adding this field prevents Terraform from recreating the rule on changes. For more information, refer to <a href="/terraform/troubleshooting/rule-id-changes/#how-to-keep-the-same-rule-id-between-modifications">Troubleshooting</a>.</p>
<br />
<p>For more information on rewriting URLs, refer to <a href="/rules/transform/url-rewrite/">URL Rewrite Rules</a>.</p>
<h2 id="create-a-request-header-transform-rule">Create a request header transform rule</h2>
<p>The following configuration example performs the following adjustments to HTTP request headers:</p>
<ul>
<li>Adds a <code>my-header-1</code> header to the request with a static value.</li>
<li>Adds a <code>my-header-2</code> header to the request with a dynamic value defined by an expression.</li>
<li>Deletes the <code>existing-header</code> header from the request, if it exists.</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14818.md")
</div></div>
<p>Use the <code>ref</code> field to get stable rule IDs across updates when using Terraform. Adding this field prevents Terraform from recreating the rule on changes. For more information, refer to <a href="/terraform/troubleshooting/rule-id-changes/#how-to-keep-the-same-rule-id-between-modifications">Troubleshooting</a>.</p>
<p>For more information on modifying request headers, refer to <a href="/rules/transform/request-header-modification/">Request Header Transform Rules</a>.</p>
<h2 id="create-a-response-header-transform-rule">Create a response header transform rule</h2>
<p>The following configuration example performs the following adjustments to HTTP response headers:</p>
<ul>
<li>Adds a <code>my-header-1</code> header to the response with a static value.</li>
<li>Adds a <code>my-header-2</code> header to the response with a dynamic value defined by an expression.</li>
<li>Deletes the <code>existing-header</code> header from the response, if it exists.</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14822.md")
</div></div>
<p>Use the <code>ref</code> field to get stable rule IDs across updates when using Terraform. Adding this field prevents Terraform from recreating the rule on changes. For more information, refer to <a href="/terraform/troubleshooting/rule-id-changes/#how-to-keep-the-same-rule-id-between-modifications">Troubleshooting</a>.</p>
<p>For more information on modifying response headers, refer to <a href="/rules/transform/response-header-modification/">Response Header Transform Rules</a>.</p>
<h2 id="configure-managed-transforms">Configure Managed Transforms</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="terraformVersion"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14826.md")
</div></div>
<p>Make sure you include the Managed Transforms you are updating in the correct object (<code>managed_request_headers</code> or <code>managed_response_headers</code>).</p>
<p>For more information on Managed Transforms, refer to <a href="/rules/transform/managed-transforms/">Managed Transforms</a>.</p>
