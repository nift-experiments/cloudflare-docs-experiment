<p>Create an exception to skip the execution of WAF managed rulesets or some of their rules. The exception configuration includes an expression that defines the skip conditions, and the rules or rulesets to skip under those conditions.</p>
<h2 id="types-of-exceptions">Types of exceptions</h2>
<p>An exception can have one of the following behaviors (from highest to lowest priority):</p>
<ul>
<li>Skip all remaining rules (belonging to WAF managed rulesets)</li>
<li>Skip one or more WAF managed rulesets</li>
<li>Skip one or more rules of WAF managed rulesets</li>
</ul>
<p>For more information on exceptions, refer to <a href="/ruleset-engine/managed-rulesets/create-exception/">Create an exception</a> in the Ruleset Engine documentation.</p>
<h2 id="scope-and-execution-order">Scope and execution order</h2>
<p>You can define exceptions at the account level and at the zone level. The scope of an exception determines which rules it affects:</p>
<ul>
<li>An account-level exception only skips rules configured at the account level. It does not affect zone-level rules.</li>
<li>A zone-level exception only skips rules configured at the zone level. It does not affect account-level rules.</li>
</ul>
<p>Within each phase, account-level rulesets run before zone-level rulesets. This means that if you deploy managed rules at both the account level and the zone level, a request is evaluated against account-level rules first. An exception defined at the zone level will not prevent a match at the account level.</p>
<p>For more information on how WAF features run in sequence, refer to <a href="/waf/feature-interoperability/">Security features interoperability</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15586.md")
</aside>
<h2 id="next-steps">Next steps</h2>
<p>Add exceptions <a href="/waf/managed-rules/waf-exceptions/define-dashboard/">in the Cloudflare dashboard</a> or <a href="/waf/managed-rules/waf-exceptions/define-api/">via API</a>.</p>
