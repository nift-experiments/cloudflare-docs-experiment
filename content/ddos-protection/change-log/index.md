<p>Cloudflare has a regular cadence of releasing updates and new rules to the DDoS managed rulesets. The updates either improve a rule's accuracy, lower false positives rates, or increase the protection due to a change in the threat landscape.</p>
<p>The release cycle for a new rule within the regular cadence follows this process:</p>
<ul>
<li>Cloudflare adds a new rule configured with the <em>Log</em> action, and announces the rule in the &quot;Scheduled changes&quot; section of each managed ruleset.</li>
<li>From that point on, if this rule matches any traffic, the matched traffic will be visible in one of the <a href="/ddos-protection/reference/analytics/">analytics dashboards</a>. If you suspect this might be a false positive, you can lower the sensitivity for that rule. Refer to <a href="/ddos-protection/managed-rulesets/http/http-overrides/override-examples/#legitimate-traffic-is-incorrectly-identified-as-an-attack-and-causes-a-false-positive">override examples</a> for details.</li>
<li>Cloudflare updates the rule action to mitigate traffic (for example, using the <em>Block</em> action) after a period of at least seven days, usually on a Monday. The exact date is shown in the scheduled changes list.</li>
</ul>
<p>Changes to existing rules follow the same process, except that Cloudflare will create a temporary updated rule (denoted as <code>BETA</code> in rule description) before updating the original rule on the next release cycle.</p>
<p>Cloudflare is very proactive in responding to new attack vectors, which may need to be released outside of the 7-day cycle, defined as an Emergency Release. This emergency release is only used to respond to new high priority threats with a low false positive probability.</p>
<h2 id="rss-feeds">RSS feeds</h2>
<ul>
<li><a href="/ddos-protection/change-log/general-updates/">General updates</a> - <div class="nb-r-s-s-button"></div></li>
<li><a href="/ddos-protection/change-log/network/">Network-layer DDoS managed ruleset</a> - <div class="nb-r-s-s-button"></div></li>
<li><a href="/ddos-protection/change-log/http/">HTTP DDoS managed ruleset</a> - <div class="nb-r-s-s-button"></div></li>
</ul>
