<p>The Cloudflare Web Application Firewall (Cloudflare WAF) checks incoming web and API requests and filters undesired traffic based on sets of rules called rulesets. The WAF uses the <a href="/ruleset-engine/rules-language/">Rules language</a>, a flexible expression syntax that lets you filter traffic by request properties such as IP address, URL path, headers, and body content.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="what-is-a-web-application-firewall">What is a Web Application Firewall?</h3>
@markup("md", "content/.markup/bodies/171.md")
</aside>
<h2 id="rules-and-rulesets">Rules and rulesets</h2>
<p>A <a href="/ruleset-engine/about/rules/">rule</a> defines a filter and an action to perform on the incoming requests that match the filter.</p>
<p>A <a href="/ruleset-engine/about/rulesets/">ruleset</a> is an ordered set of rules that you can apply to traffic on the Cloudflare global network. Rules within a ruleset are evaluated in sequence. The first matching rule with a <a href="/ruleset-engine/rules-language/actions/">terminating action</a> (such as Block, Challenge, or Redirect) stops evaluation — later rules do not run for that request.</p>
<h2 id="main-components">Main components</h2>
<p>The Cloudflare WAF includes:</p>
<ul>
<li><a href="/waf/managed-rules/">Managed Rules</a> (for example, the <a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/">Cloudflare Managed Ruleset</a>), which are signature-based rules created by Cloudflare that provide immediate protection against known attacks.</li>
<li><a href="/waf/detections/">Traffic detections</a> (for example, bot score and attack score) that enrich requests with metadata.</li>
<li>User-defined rules for your specific needs, including <a href="/waf/custom-rules/">custom rules</a> and <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/172.md")
</div>.
<h2 id="detection-versus-mitigation">Detection versus mitigation</h2>
<p>The two main roles of the Cloudflare WAF are the following:</p>
<ul>
<li>
<p><strong>Detection</strong>: Run incoming requests through one or more <a href="/waf/detections/">traffic detections</a> to find malicious or potentially malicious activity. The scores from enabled detections are available in the <a href="/waf/analytics/security-analytics/">Security Analytics</a> dashboard, where you can analyze your security posture and determine the most appropriate mitigation rules.</p>
</li>
<li>
<p><strong>Mitigation</strong>: Blocks, challenges, or throttles requests through different mitigation features such as <a href="/waf/custom-rules/">custom rules</a>, <a href="/waf/managed-rules/">Managed Rules</a>, and <a href="/waf/rate-limiting-rules/">rate limiting rules</a>. Rules that mitigate traffic can include scores from traffic scans in their expressions to better address possibly malicious requests.</p>
</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/170.md")
</aside>
<h3 id="available-traffic-detections">Available traffic detections</h3>
<p>The WAF currently provides the following detections for finding security threats in incoming requests:</p>
<ul>
<li><a href="/waf/detections/attack-score/"><strong>Attack score</strong></a>: Checks for known attack variations and malicious payloads. Scores traffic on a scale from 1 (likely to be malicious) to 99 (unlikely to be malicious).</li>
<li><a href="/waf/detections/leaked-credentials/"><strong>Leaked credentials</strong></a>: Scans incoming requests for credentials (usernames and passwords) previously leaked from data breaches.</li>
<li><a href="/waf/detections/malicious-uploads/"><strong>Malicious uploads</strong></a>: Scans content objects, such as uploaded files, for malicious signatures like malware.</li>
<li><a href="/waf/detections/ai-security-for-apps/"><strong>AI Security for Apps</strong></a>: Helps protect your services powered by large language models (LLMs) against abuse.</li>
<li><a href="/bots/concepts/bot-score/"><strong>Bot score</strong></a>: Scores traffic on a scale from 1 (likely to be a bot) to 99 (likely to be human).</li>
</ul>
<p>To enable traffic detections in the Cloudflare dashboard, go to the Security <strong>Settings</strong> page.</p>
<div class="nb-dash-button"></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/169.md")
</aside>
<hr />
<h2 id="rule-execution-order">Rule execution order</h2>
<p>Cloudflare evaluates different types of rules when processing incoming requests. The first rule with a <a href="/ruleset-engine/rules-language/actions/">terminating action</a> (such as <em>Block</em>, <em>Managed Challenge</em>, or <em>Redirect</em>) stops all further evaluation. For example, an IP Access rule that blocks a request prevents custom rules from running. The rule execution order is the following:</p>
<ol>
<li><a href="/waf/tools/ip-access-rules/">IP Access rules</a></li>
<li><a href="/firewall/cf-firewall-rules/">Firewall rules</a> (deprecated)</li>
<li><a href="/waf/custom-rules/">Custom rules</a></li>
<li><a href="/waf/rate-limiting-rules/">Rate limiting rules</a></li>
<li><a href="/waf/managed-rules/">Managed Rules</a></li>
<li><a href="/waf/reference/legacy/old-rate-limiting/">Cloudflare Rate Limiting</a> (previous version, no longer available)</li>
</ol>
<p>Rules are evaluated in order. If there is a match for a rule with a <a href="/ruleset-engine/rules-language/actions/">terminating action</a>, the rule evaluation will stop and the action will be executed immediately. Rules with a non-terminating action (such as <em>Log</em>) will not prevent subsequent rules from being evaluated and executed. For more information on how rules are evaluated, refer to <a href="/ruleset-engine/about/rules/#rule-evaluation">Rule evaluation</a> in the Ruleset Engine documentation.</p>
<p>For more information on the phases where each WAF feature will execute, refer to <a href="/waf/reference/phases/">WAF phases</a>.</p>
<p>For common interactions between rewrites, IP Access rules, custom rules, and managed rules, refer to <a href="/waf/troubleshooting/phase-interactions/">Rule phase interactions</a>.</p>
