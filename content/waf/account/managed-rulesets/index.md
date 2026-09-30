<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15426.md")
</aside>
<p>Cloudflare provides pre-configured managed rulesets that protect against web application exploits such as the following:</p>
<ul>
<li>Zero-day vulnerabilities</li>
<li>Top-10 attack techniques</li>
<li>Use of stolen/leaked credentials</li>
<li>Extraction of sensitive data</li>
</ul>
<p>Managed rulesets are <a href="/waf/change-log/">regularly updated</a>. Each rule has a default action that varies according to the severity of the rule. You can adjust the behavior of specific rules, choosing from several possible actions.</p>
<p>Rules of managed rulesets have associated tags (such as <code>wordpress</code>) that allow you to search for a specific group of rules and configure them in bulk.</p>
<h2 id="account-level-deployment">Account-level deployment</h2>
<p>At the zone level, each <a href="/waf/managed-rules/#available-managed-rulesets">WAF managed ruleset</a> can only be deployed once. At the account level, you can deploy each managed ruleset more than once. This allows you to apply the same ruleset with different configurations to different subsets of incoming traffic across the Enterprise zones in your account.</p>
<p>For example, you could deploy the <a href="/waf/managed-rules/reference/owasp-core-ruleset/">Cloudflare OWASP Core Ruleset</a> multiple times with different <a href="/waf/managed-rules/reference/owasp-core-ruleset/concepts/#paranoia-level">paranoia levels</a> and a different action (<em>Managed Challenge</em> action for PL3 and <em>Log</em> action for PL4). Higher paranoia levels enable additional rules that are more likely to produce false positives.</p>
<details class="nb-details"><summary>Example: Deploy OWASP with two different configurations</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15430.md")
</div></details>
<h2 id="customize-the-behavior-of-managed-rulesets">Customize the behavior of managed rulesets</h2>
<p>To customize the behavior of managed rulesets, do one of the following:</p>
<ul>
<li><a href="/waf/managed-rules/waf-exceptions/">Create exceptions</a> to skip the execution of managed rulesets or some of their rules under certain conditions.</li>
<li><a href="/waf/account/managed-rulesets/deploy-dashboard/#configure-a-managed-ruleset">Configure overrides</a> to change the rule action
or disable one or more rules of managed rulesets. Overrides can affect an
entire managed ruleset, specific tags, or specific rules in the managed
ruleset.</li>
</ul>
<p>Exceptions have priority over overrides.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/15425.md")
</aside>
