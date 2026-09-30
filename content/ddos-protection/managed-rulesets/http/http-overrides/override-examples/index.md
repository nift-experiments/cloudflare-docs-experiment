<h2 id="use-cases">Use cases</h2>
<p>The following scenarios detail how you can make use of override rules as a solution to common HTTP DDoS Protection issues.</p>
<h3 id="traffic-from-your-mobile-application-is-blocked-by-a-ddos-managed-rule">Traffic from your mobile application is blocked by a DDoS Managed Rule</h3>
<p>The traffic from your mobile application may have appeared suspicious, causing a DDoS Managed Rule to block it.</p>
<p>You should identify the Managed Rule blocking the traffic and change the sensitivity level to <code>Medium</code>. If traffic continues to be blocked by the managed rule, set the sensitivity level to <code>Low</code> or <code>Essentially off</code>.</p>
<p>If you have access to filter expressions, you can create an override to target the specific affected traffic.</p>
<h3 id="traffic-is-flagged-by-an-adaptive-rule-based-on-the-location-and-may-be-an-attack">Traffic is flagged by an adaptive rule based on the location and may be an attack</h3>
<p>If you recognize that the traffic flagged by an adaptive rule may be considered an attack, you can create an override rule to enable the adaptive rule in mitigation mode to <code>challenge</code> (if it is browser traffic) or <code>block</code> (for other suspicious traffic).</p>
<h3 id="legitimate-traffic-is-incorrectly-identified-as-an-attack-and-causes-a-false-positive">Legitimate traffic is incorrectly identified as an attack and causes a false positive</h3>
<p>A false positive is an incorrect identification. In the case of DDoS protection, there is a false positive when legitimate traffic is mistakenly classified as attack traffic. This can occur when legacy applications, Internet services, or faulty client applications generate legitimate traffic that appears suspicious, has odd traffic patterns, deviates from best practices, or violates protocols.</p>
<p>In these cases, Cloudflare's DDoS Protection systems may flag that traffic as malicious and apply mitigation actions. If the traffic is in fact legitimate and not part of an attack, the mitigation actions can cause service disruptions and outages to your Internet properties.</p>
<p>To remedy a false positive:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7524.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7521.md")
</aside>
<p>Once saved, the rule takes effect within one or two minutes. The rule adjustment should provide immediate remedy, which you can view in the <a href="/ddos-protection/reference/analytics/">analytics dashboard</a>.</p>
<h4 id="update-the-adjusted-rules-later">Update the adjusted rules later</h4>
<p>Later, you can change the <a href="/ddos-protection/managed-rulesets/network/override-parameters/#sensitivity-level">sensitivity level</a> of the rule causing the false positives to avoid future issues, and change the rule action back to its default value.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="recommendation-enable-ddos-alerts">Recommendation: Enable DDoS alerts</h3>
@markup("md", "content/.markup/bodies/7520.md")
</aside>
<h4 id="avoid-false-positives-while-retaining-protection-and-visibility">Avoid false positives while retaining protection and visibility</h4>
<p>To see what DDoS Managed Rules do in a high sensitivity level while remaining protected by blocking attacks at a low sensitivity level, Advanced DDoS protection customers can <a href="/ddos-protection/managed-rulesets/network/network-overrides/configure-dashboard/#create-a-ddos-override">create a first override</a> that blocks attacks at a low sensitivity and a second override to log at a high sensitivity.</p>
<p>The overrides must be set in that order. Otherwise, it will not work. This is because overrides are evaluated in order and will stop at the first override that matches both expression and sensitivity. Setting the overrides in the wrong order would cause the <code>Log</code> override at a high sensitivity to match all instances. As a result, Cloudflare will never evaluate the <code>Block</code> override that would be placed behind it, causing all rules to be set in <code>Log</code> mode.</p>
<p>If an override without an expression matches, Cloudflare will not evaluate the expressions that follow it.</p>
<h3 id="an-attack-is-incorrectly-identified-as-legitimate-traffic-and-causes-a-false-negative">An attack is incorrectly identified as legitimate traffic and causes a false negative</h3>
<p>A false negative is a lack of identification. In the case of DDoS protection, there is a false negative when attack traffic is mistakenly classified as legitimate traffic and is not mitigated. This can occur when the attack traffic is not sufficiently high to trigger mitigation actions or if there are no rules matching the attack.</p>
<p>To address a false negative:</p>
<ul>
<li>If you are a WAF/CDN customer, follow the steps in the <a href="/ddos-protection/best-practices/proactive-defense/">Proactive DDoS defense</a> page, which guides you on enabling the <em>Under Attack</em> mode and creating <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/7525.md")
</div> rules and WAF custom rules as needed.
- If you are a Magic Transit customer, [use Cloudflare Network Firewall rules](/cloudflare-one/traffic-policies/packet-filtering/add-policies/) to help mitigate the attack.
<h3 id="incomplete-mitigations">Incomplete mitigations</h3>
<p>An incomplete mitigation is a case when the DDoS protection systems have applied mitigation, but not all the attack was mitigated. This can happen when Cloudflare's systems apply a mitigation action that is less strict than what the attack requires.</p>
<p>The system chooses the mitigation action based on the logic and the DDoS protection system's confidence that the traffic is indeed part of an attack:</p>
<ul>
<li>For high-confidence rules, the system will apply a strict mitigation action such as the <em>Block</em> action.</li>
<li>For low-confidence rules, the system will apply a less strict mitigation rule such as <em>Challenge</em> or <em>Force Connection Close</em>.</li>
</ul>
<p>If you are experiencing a DDoS attack detected by Cloudflare and the applied mitigation action is not sufficiently strict, change the rule action to <em>Block</em>:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7528.md")
</div>
<p>Once saved, the rule takes effect within one or two minutes. The rule adjustment should provide immediate remedy, which you can view in the <a href="/ddos-protection/reference/analytics/">analytics dashboard</a>.</p>
<h4 id="alternate-procedure">Alternate procedure</h4>
<p>If you cannot stop an attack from overloading your origin web server using the above steps, <a href="/support/contacting-cloudflare-support/">contact Cloudflare Support</a> for assistance, providing the following details:</p>
<ul>
<li>Time period of the attack (UTC timestamp)</li>
<li>Domain/path being targeted (zone name/ID)</li>
<li>Attack frequency</li>
<li>Steps to reproduce the issue, with actual results versus expected results</li>
<li>Any relevant additional information such as site URLs, error messages, screenshots, or relevant logs from your origin web server</li>
</ul>
