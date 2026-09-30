<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15444.md")
</aside>
<p>Custom rulesets are collections of custom rules that you can deploy at the account or <a href="/waf/custom-rules/custom-rulesets/">zone level</a>.</p>
<p>Like <a href="/waf/custom-rules/">custom rules</a> at the zone level, custom rulesets allow you to control incoming traffic by filtering requests.</p>
<p>Account-level custom rulesets allow you to define a set of custom rules once and apply them across multiple Enterprise zones in your account. Instead of configuring each zone individually, you create a ruleset at the account level and use expressions to control which zones and traffic it applies to.</p>
<p>At the zone level, all customers can create and deploy custom rulesets. Custom rulesets at the account level require an Enterprise plan. For more details, refer to <a href="/waf/custom-rules/#availability">Availability</a>.</p>
<h2 id="next-steps">Next steps</h2>
<p>Refer to the following pages for more information on working with custom rulesets:</p>
<ul>
<li><a href="/waf/account/custom-rulesets/create-dashboard/">Work with custom rulesets in the dashboard</a></li>
<li><a href="/waf/account/custom-rulesets/create-api/">Work with custom rulesets using the API</a></li>
</ul>
<p>For Terraform examples, refer to <a href="/terraform/additional-configurations/waf-custom-rules/#create-and-deploy-a-custom-ruleset">WAF custom rules configuration using Terraform</a>.</p>
