<p><a href="/waf/rate-limiting-rules/">Rate limiting rules</a> allow you to define a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/15418.md")
</div> for requests matching an [expression](/ruleset-engine/rules-language/expressions/), and the action to perform when that rate limit is reached. You can configure rate limiting rules for a single zone or at the account level.
<p>Account-level rate limiting rulesets allow you to define rate limiting rules once and deploy them to multiple Enterprise zones. Instead of configuring the same rules in each zone, you create a ruleset at the account level and control which zones it applies to.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15417.md")
</aside>
<p>To apply a rate limiting ruleset at the account level:</p>
<ol>
<li>Create a rate limiting ruleset with one or more rate limiting rules.</li>
<li>Deploy the ruleset to one or more zones on an Enterprise plan.</li>
</ol>
<p>For more information on how Cloudflare calculates request rates, refer to <a href="/waf/rate-limiting-rules/request-rate/">Request rate calculation</a>.</p>
<h2 id="next-steps">Next steps</h2>
<p>For instructions on creating and deploying a rate limiting ruleset, refer to the following pages:</p>
<ul>
<li><a href="/waf/account/rate-limiting-rulesets/create-dashboard/">Create a rate limiting ruleset in the dashboard</a></li>
<li><a href="/waf/account/rate-limiting-rulesets/create-api/">Create a rate limiting ruleset using the API</a></li>
</ul>
<p>For Terraform examples, refer to <a href="/terraform/additional-configurations/rate-limiting-rules/">Rate limiting rules configuration using Terraform</a>.</p>
