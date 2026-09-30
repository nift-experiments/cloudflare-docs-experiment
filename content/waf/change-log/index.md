<p>The <a href="/waf/change-log/changelog/">WAF changelog</a> provides information about changes to <a href="/waf/managed-rules/">managed rulesets</a> and general updates to WAF protection.</p>
<p><a class="nb-link-button" href="/waf/change-log/changelog/">View changelog</a>
<a class="nb-link-button" href="/waf/change-log/scheduled-changes/">View scheduled changes</a></p>
<div class="nb-r-s-s-button"></div>
<h2 id="changelog-for-managed-rulesets">Changelog for managed rulesets</h2>
<p>Cloudflare regularly releases updates and adds new rules to WAF <a href="/waf/managed-rules/">managed rulesets</a>. Updates improve rule accuracy, reduce false positives, or increase protection in response to changes in the threat landscape.</p>
<h3 id="release-cycle">Release cycle</h3>
<p>New and updated rules follow a seven-day release cycle, typically on Monday or Tuesday (adjusted for public holidays).</p>
<p><strong>Week 1 — Logging only:</strong> Cloudflare deploys new or updated rules in logging-only mode with the <em>Log</em> action. Rules in this mode record matching requests but do not block traffic. Most newly created rules carry both the <code>beta</code> and <code>new</code> tags. Use this period to review your security events for unexpected matches that could be false positives.</p>
<p><strong>Week 2 — Default action:</strong> On the following release day, the rules change from the <em>Log</em> action to their intended default action (shown in the <strong>New Action</strong> column of the changelog table). The <code>beta</code> and <code>new</code> tags are removed.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15398.md")
</aside>
<p>For updates to existing rules, Cloudflare first deploys the updated version as a separate <code>BETA</code> rule (noted in the rule description) with a <code>beta</code> tag, before updating the original rule on the next release cycle.</p>
<h3 id="disabled-rules">Disabled rules</h3>
<p>Cloudflare may also add rules in disabled mode on the same release cycle. These rules make remediation logic available without affecting traffic, and allow Cloudflare to perform impact testing and performance checks. You can activate a disabled rule at any time if you need its protection. Disabled rules do not carry the <code>beta</code> or <code>new</code> tags.</p>
<h3 id="emergency-releases">Emergency releases</h3>
<p>For new vulnerabilities, Cloudflare may release rules outside the regular seven-day cycle. These are emergency releases.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15397.md")
</aside>
<p>If you notice a new or updated rule generating an increased volume of security events, you can disable it or change its action from the default. Once you change a rule to use an action other than the default one, Cloudflare will not be able to override the rule action.</p>
<h2 id="general-updates">General updates</h2>
<p>The <a href="/waf/change-log/changelog/">changelog</a> also includes general updates to WAF protection that are not specific to managed rulesets.</p>
