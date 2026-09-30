<p>The Cloudflare OWASP Core Ruleset is Cloudflare's implementation of the <a href="https://owasp.org/www-project-modsecurity-core-rule-set/">OWASP ModSecurity Core Rule Set</a> (CRS). It is designed to work as a single entity to calculate a <a href="/waf/managed-rules/reference/owasp-core-ruleset/concepts/#request-threat-score">threat score</a> and execute an action based on that score.</p>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/15666.md")
</aside>
<h2 id="deploy-the-cloudflare-owasp-core-ruleset-deploy-in-the-dashboard">Deploy the Cloudflare OWASP Core Ruleset </h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15667.md")
</div>
<p>This operation deploys the managed ruleset for the current zone, creating a new rule with the <em>Execute</em> action.</p>
<h2 id="configure-in-the-dashboard">Configure in the dashboard</h2>
<p>You can configure (or override) the Cloudflare OWASP Core Ruleset, overriding its default configuration, at several levels:</p>
<ul>
<li><a href="#ruleset-level-configuration">Ruleset level</a></li>
<li><a href="#tag-level-configuration">Tag level</a></li>
<li><a href="#rule-level-configuration">Rule level</a></li>
</ul>
<p>More specific configurations (rule and tag level) have greater priority than less specific configurations (ruleset level).</p>
<h3 id="ruleset-level-configuration">Ruleset-level configuration</h3>
<p>You can configure (or override) the following Cloudflare OWASP Core Ruleset settings in the Cloudflare dashboard:</p>
<ul>
<li><strong>Scope</strong>: When you specify a custom filter expression, the Cloudflare OWASP Core Ruleset applies only to a subset of the incoming requests. By default, a managed ruleset deployed in the dashboard applies to all incoming traffic.</li>
<li><strong><a href="/waf/managed-rules/reference/owasp-core-ruleset/concepts/#paranoia-level">Paranoia level</a></strong>: The paranoia level (PL) classifies OWASP rules according to their aggressiveness, varying from <em>PL1</em> to <em>PL4</em>, where <em>PL4</em> is the most strict level. The available levels are:
<ul>
<li><em>PL1</em> (default)</li>
<li><em>PL2</em></li>
<li><em>PL3</em></li>
<li><em>PL4</em></li>
</ul>
</li>
<li><strong><a href="/waf/managed-rules/reference/owasp-core-ruleset/concepts/#score-threshold">Score threshold</a></strong>: The score threshold (or anomaly threshold) defines the minimum cumulative score — obtained from matching OWASP rules — for the WAF to apply the configured OWASP ruleset action. The available thresholds are:
<ul>
<li><em>Low - 60 and higher</em></li>
<li><em>Medium - 40 and higher</em> (default)</li>
<li><em>High - 25 and higher</em></li>
</ul>
</li>
<li><strong>OWASP action</strong>: The action to perform when the calculated <a href="/waf/managed-rules/reference/owasp-core-ruleset/concepts/#request-threat-score">request threat score</a> is greater than the <a href="/waf/managed-rules/reference/owasp-core-ruleset/concepts/#score-threshold">score threshold</a>. The available actions are: <em>Block</em>, <em>Log</em>, <em>Non-Interactive Challenge</em>, <em>Managed Challenge</em>, and <em>Interactive Challenge</em>.</li>
<li><strong><a href="/waf/managed-rules/payload-logging/configure/">Payload logging</a></strong>: When enabled, logs the request information (payload) that triggered a specific rule of the managed ruleset. You must configure a public key to encrypt the payload.</li>
</ul>
<p>Once you have <a href="#deploy-in-the-dashboard">deployed the Cloudflare OWASP Core Ruleset</a>, do the following to configure it in the dashboard:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15668.md")
</div>
<h3 id="tag-level-configuration">Tag-level configuration</h3>
<p>You can configure (or override) the following setting in the dashboard for OWASP Core Ruleset rules tagged with at least one of the selected tags:</p>
<ul>
<li><strong>Rule status</strong>: Sets the rule status (enabled or disabled) for all the rules with the selected tags. To remove the action override at the tag level, set the action to <em>Default</em>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15665.md")
</aside>
<p>Once you have <a href="#deploy-in-the-dashboard">deployed the Cloudflare OWASP Core Ruleset</a>, do the following to configure rules with specific tags in the dashboard:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15669.md")
</div>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15670.md")
</div>
<h3 id="rule-level-configuration">Rule-level configuration</h3>
<p>You can configure (or override) the following setting in the dashboard for the selected OWASP Core Ruleset rules:</p>
<ul>
<li><strong>Rule status</strong>: Sets the status (enabled or disabled) of a single rule or, if you select multiple rules, for the selected rules.</li>
</ul>
<p>Once you have <a href="#deploy-in-the-dashboard">deployed the Cloudflare OWASP Core Ruleset</a>, do the following to configure individual ruleset rules in the dashboard:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15671.md")
</div>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15672.md")
</div>
