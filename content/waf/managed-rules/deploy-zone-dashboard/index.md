<p>The instructions in this page provide general guidance for deploying and configuring a managed ruleset for a zone.</p>
<p>For more specific instructions, refer to the following pages:</p>
<ul>
<li><a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/#deploy-in-the-dashboard">Deploy the Cloudflare Managed Ruleset</a></li>
<li><a href="/waf/managed-rules/reference/owasp-core-ruleset/configure-dashboard/#deploy-in-the-dashboard">Deploy the Cloudflare OWASP Core Ruleset</a></li>
<li><a href="/waf/managed-rules/reference/sensitive-data-detection/#deploy-in-the-dashboard">Deploy the Cloudflare Sensitive Data Detection ruleset</a></li>
</ul>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/15378.md")
</aside>
<h2 id="deploy-a-managed-ruleset">Deploy a managed ruleset</h2>
<p>To deploy a managed ruleset for a zone:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15379.md")
</div>
<p>This operation deploys the managed ruleset for the current zone, creating a new rule with the <em>Execute</em> action.</p>
<p>To temporarily turn off a managed ruleset without deleting its deployment configuration, use the toggle next to the rule that deploys the managed ruleset.</p>
<h2 id="configure-a-managed-ruleset">Configure a managed ruleset</h2>
<p>Configure a managed ruleset to:</p>
<ul>
<li>Specify a custom filter expression to apply the rules in the ruleset to a subset of incoming requests.</li>
<li>Configure (or override) specific settings for one or more rules (for example, configure a rule with an action different from the default action configured by Cloudflare), or turn off those rules.</li>
</ul>
<p>To skip one or more rules — or even entire managed rulesets — for specific incoming requests, <a href="/waf/managed-rules/waf-exceptions/">add an exception</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15377.md")
</aside>
<h3 id="configure-all-the-rules-in-a-managed-ruleset">Configure all the rules in a managed ruleset</h3>
<p>To configure (or override) settings for all the rules in a managed ruleset:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15380.md")
</div>
<h3 id="configure-rules-of-a-managed-ruleset-with-specific-tags">Configure rules of a managed ruleset with specific tags</h3>
<p>To configure (or override) settings of rules tagged with specific tags:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15381.md")
</div>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15382.md")
</div>
<h3 id="configure-individual-rules-of-a-managed-ruleset">Configure individual rules of a managed ruleset</h3>
<p>To configure (or override) settings of individual rules of a managed ruleset:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15383.md")
</div>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15384.md")
</div>
<h3 id="browse-the-rules-of-a-managed-ruleset">Browse the rules of a managed ruleset</h3>
<p>You can browse the available rules in a managed ruleset and search for individual rules or tags.</p>
<ol>
<li>In the Cloudflare dashboard, go to the Security <strong>Settings</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>(Optional) Filter by <strong>Web application exploits</strong>.</li>
<li>Find the managed ruleset you want to browse, and select <strong>View ruleset</strong>.</li>
<li>Review the rules and their tags in the side panel.</li>
</ol>
<h3 id="delete-a-managed-ruleset-deployment-rule-or-an-exception">Delete a managed ruleset deployment rule or an exception</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15385.md")
</div>
