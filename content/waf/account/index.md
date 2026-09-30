<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15416.md")
</aside>
<p>The account-level Web Application Firewall (WAF) configuration allows you to define a configuration once and apply it to multiple Enterprise zones in your account. Instead of configuring each zone individually, you create rulesets at the account level and use expressions to control which zones and traffic they apply to.</p>
<p>For example, you can deploy a single ruleset that applies to <code>/admin/*</code> URI paths across both <code>example.com</code> and <code>example.net</code>. Rulesets can target all incoming traffic or a specific subset.</p>
<p>At the account level, WAF rules are grouped into rulesets. You can perform the following operations:</p>
<ul>
<li>Create and deploy <a href="/waf/account/custom-rulesets/">custom rulesets</a></li>
<li>Create and deploy <a href="/waf/account/rate-limiting-rulesets/">rate limiting rulesets</a></li>
<li>Deploy <a href="/waf/account/managed-rulesets/">managed rulesets</a></li>
</ul>
