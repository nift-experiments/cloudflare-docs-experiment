<p>Cloudflare provides pre-configured managed rulesets that protect against web application exploits such as the following:</p>
<ul>
<li>Zero-day vulnerabilities</li>
<li>Top-10 attack techniques</li>
<li>Use of stolen/leaked credentials</li>
<li>Extraction of sensitive data</li>
</ul>
<p>Managed rulesets are <a href="/waf/change-log/">regularly updated</a>. Each rule has a default action that varies according to the severity of the rule. You can adjust the behavior of specific rules, choosing from several possible actions.</p>
<p>Rules of managed rulesets have associated tags (such as <code>wordpress</code>) that allow you to search for a specific group of rules and configure them in bulk.</p>
<p><a href="/waf/detections/attack-signature-detection/#compare-attack-signature-detection-and-managed-rules">Attack Signature Detection</a> uses the same signatures as Cloudflare Managed Rules. It records match metadata without applying an action by itself.</p>
<h2 id="available-managed-rulesets">Available managed rulesets</h2>
<ul>
<li>
<p><a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/"><strong>Cloudflare Managed Ruleset</strong></a>: Created by the Cloudflare security team, this ruleset provides fast and effective protection for all of your applications. It covers known attack techniques and zero-day vulnerabilities (newly discovered flaws with no available patch). The ruleset is updated frequently to address new threats and reduce false positives (legitimate requests incorrectly flagged).<br/>Ruleset ID: <code class="nb-rule-id" title="efb7b8c949ac4650a09736fc376e9aee">376e9aee</code></p>
</li>
<li>
<p><a href="/waf/managed-rules/reference/owasp-core-ruleset/"><strong>Cloudflare OWASP Core Ruleset</strong></a>: Cloudflare's implementation of the Open Web Application Security Project (OWASP) ModSecurity Core Rule Set. This ruleset uses a scoring model — each matching rule adds its score to a cumulative <a href="/waf/managed-rules/reference/owasp-core-ruleset/concepts/#request-threat-score">threat score</a>, and the WAF executes the configured action when the score exceeds the <a href="/waf/managed-rules/reference/owasp-core-ruleset/concepts/#score-threshold">threshold</a>.<br/>Ruleset ID: <code class="nb-rule-id" title="4814384a9e5d4991b9815dcfc25d2f1f">c25d2f1f</code></p>
</li>
<li>
<p><a href="/waf/managed-rules/reference/exposed-credentials-check/"><strong>Cloudflare Exposed Credentials Check</strong></a>: Deploys an automated credentials check on your end-user authentication endpoints. For any credential pair, the Cloudflare WAF performs a lookup against a public database of stolen credentials to determine if they were previously compromised. Cloudflare recommends that you use <a href="/waf/detections/leaked-credentials/">leaked credentials detection</a> instead of this ruleset.<br/>Ruleset ID: <code class="nb-rule-id" title="c2e184081120413c86c3ab7e14069605">14069605</code></p>
</li>
<li>
<p><strong>Cloudflare Free Managed Ruleset</strong>: Available on all Cloudflare plans. Provides protection against high-impact and widely exploited vulnerabilities. The rules are safe to deploy on most applications. If you have already deployed the Cloudflare Managed Ruleset, you do not need this ruleset — the Cloudflare Managed Ruleset includes broader coverage.<br/>Ruleset ID: <code class="nb-rule-id" title="77454fe2d30c4220b5701f6fdfb893ba">dfb893ba</code></p>
</li>
</ul>
<p>The following managed rulesets run in a response phase:</p>
<ul>
<li><a href="/waf/managed-rules/reference/sensitive-data-detection/"><strong>Cloudflare Sensitive Data Detection</strong></a>: Created by Cloudflare to address common data loss threats. These rules monitor the download of specific sensitive data — for example, financial and personally identifiable information.<br/>Ruleset ID: <code class="nb-rule-id" title="e22d83c647c64a3eae91b71b499d988e">499d988e</code></li>
</ul>
<h2 id="availability">Availability</h2>
<p>The managed rulesets you can deploy depend on your Cloudflare plan.</p>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Free Managed Ruleset</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Cloudflare OWASP Core Ruleset</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Cloudflare Exposed Credentials Check (deprecated)</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Cloudflare Sensitive Data Detection</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="customize-the-behavior-of-managed-rulesets">Customize the behavior of managed rulesets</h2>
<p>To customize the behavior of managed rulesets, do one of the following:</p>
<ul>
<li><a href="/waf/managed-rules/waf-exceptions/">Create exceptions</a> to skip the execution of managed rulesets or some of their rules under certain conditions.</li>
<li><a href="/waf/managed-rules/deploy-zone-dashboard/#configure-a-managed-ruleset">Configure overrides</a> to change the rule action
or disable one or more rules of managed rulesets. Overrides can affect an
entire managed ruleset, specific tags, or specific rules in the managed
ruleset.</li>
</ul>
<p>Exceptions have priority over overrides.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/15376.md")
</aside>
<h2 id="interaction-with-other-app-security-features">Interaction with other app security features</h2>
<p>If you are using several app security features like custom rules, Managed Rules, and Super Bot Fight Mode, it is important to understand how these features interact and the order in which they execute. Refer to <a href="/waf/feature-interoperability/">Security features interoperability</a> for more information.</p>
<h2 id="important-remarks">Important remarks</h2>
<h3 id="maximum-body-size">Maximum body size</h3>
<p>Managed rules inspect the body of each incoming request up to a maximum size. This limit varies by plan:</p>
<ul>
<li>For Enterprise customers, the maximum body size is 128 KB.</li>
<li>For other paid plans, the limit is lower by default — contact your account team or Cloudflare Support to increase the limit.</li>
<li>For users in the Free plan, the limit is 1 MB.</li>
</ul>
<p>Request content beyond this limit may not be fully analyzed, which can affect how managed rules behave. For example, the <a href="/waf/managed-rules/reference/owasp-core-ruleset/">OWASP Core Ruleset</a> calculates a cumulative <a href="/waf/managed-rules/reference/owasp-core-ruleset/concepts/#request-threat-score">threat score</a> based on the scores of individual rules that match a request. Larger payloads give more content for rules to match against, which increases the score and makes it more likely to exceed the <a href="/waf/managed-rules/reference/owasp-core-ruleset/concepts/#score-threshold">score threshold</a> — resulting in a false positive.</p>
<p>If included in your plan, you can use <a href="/ruleset-engine/rules-language/fields/reference/?field-category=Body">request body fields</a> in <a href="/waf/custom-rules/">custom rules</a> to apply appropriate actions to requests that have not been fully analyzed. The <code>http.request.body.truncated</code> field indicates whether the request body was truncated, while <code>http.request.headers.truncated</code> indicates whether the request contained too many headers for all of them to be included.</p>
<h3 id="zone-level-deployment">Zone-level deployment</h3>
<p>At the zone level, you can deploy each managed ruleset once. At the <a href="/waf/account/managed-rulesets/">account level</a>, you can deploy each managed ruleset multiple times, which allows you to apply different configurations of the same ruleset to different subsets of incoming traffic.</p>
<h2 id="execution-order">Execution order</h2>
<p>WAF Managed Rules run in the <code>http_request_firewall_managed</code> phase, which executes <strong>after</strong>:</p>
<ul>
<li>HTTP DDoS Attack Protection (<code>ddos_l7</code> phase)</li>
<li>Custom Rules (<code>http_request_firewall_custom</code> phase)</li>
<li>Rate Limiting Rules (<code>http_ratelimit</code> phase)</li>
</ul>
<p>This means a rule with a terminal action (such as Block or Managed Challenge) in any of these earlier phases prevents Managed Rules from evaluating that request. For the complete security feature execution order, refer to <a href="/waf/feature-interoperability/">Security features interoperability</a>.</p>
<h3 id="waf-exceptions">WAF exceptions</h3>
<p>WAF exceptions (skip rules) are rules with a <code>skip</code> action deployed to the <code>http_request_firewall_managed</code> phase entry-point ruleset. They are evaluated in list order within the entry-point ruleset — a skip rule only bypasses <code>execute</code> rules listed after it. Place exceptions before the managed ruleset execute rules they are intended to skip. For more information, refer to <a href="/waf/managed-rules/waf-exceptions/">WAF exceptions</a>.</p>
