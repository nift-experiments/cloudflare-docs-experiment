<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="deprecation-notice">Deprecation notice</h3>
@markup("md", "content/.markup/bodies/15646.md")
</aside>
<p><strong>Sampled logs</strong> in <a href="/waf/analytics/security-events/">Security Events</a> shows entries for requests with exposed credentials identified by rules with the <em>Log</em> action.</p>
<p>Check for exposed credentials events in the Security Events dashboard, filtering by a specific rule ID. For more information on filtering events, refer to <a href="/waf/analytics/security-events/#adjust-displayed-data">Adjust displayed data</a>.</p>
<h2 id="important-notes">Important notes</h2>
<p>Exposed credentials events are only logged after you activate the Exposed Credentials Check Managed Ruleset or create a custom rule checking for exposed credentials.</p>
<p>The log entries will not contain the values of the exposed credentials (username, email, or password). However, if <a href="/waf/managed-rules/payload-logging/">matched payload logging</a> is enabled, the log entries will contain the values of the fields in the rule expression that triggered the rule. These values might be the values of credential fields, depending on your rule configuration.</p>
