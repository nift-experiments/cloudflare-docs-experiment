<h2 id="paranoia-level">Paranoia level</h2>
<p>The paranoia level (PL) classifies OWASP rules according to their aggressiveness. Paranoia levels vary from PL1 to PL4, where PL4 is the most strict level:</p>
<ul>
<li>PL1 (default value)</li>
<li>PL2</li>
<li>PL3</li>
<li>PL4</li>
</ul>
<p>Each rule in the OWASP managed ruleset is associated with a paranoia level. Rules associated with higher paranoia levels are considered more aggressive and provide increased protection. However, they might cause more legitimate traffic to get blocked due to false positives.</p>
<p>When you configure the paranoia level of the OWASP ruleset, you are enabling all the rules belonging to all paranoia levels up to the level you select. For example, if you configure the ruleset paranoia level to PL3, you are enabling rules belonging to paranoia levels PL1, PL2, and PL3.</p>
<p>When you set the ruleset paranoia level, the WAF enables the corresponding rules in bulk. You then can disable specific rules individually or by tag, if needed. If you use the highest paranoia level (PL4) you will probably need to disable some of its rules for applications that need to receive complex input patterns.</p>
<h2 id="request-threat-score">Request threat score</h2>
<p>Each OWASP rule that matches the current request has an associated score. The request threat score is the sum of the individual scores of all OWASP rules that matched the request.</p>
<h2 id="score-threshold">Score threshold</h2>
<p>The score threshold (or anomaly threshold) defines the minimum cumulative score — obtained from matching OWASP rules — for the WAF to apply the configured OWASP ruleset action.</p>
<p>The available score thresholds are the following:</p>
<ul>
<li><em>Low – 60 and higher</em></li>
<li><em>Medium – 40 and higher</em> (default value)</li>
<li><em>High – 25 and higher</em></li>
</ul>
<p>Each threshold (<em>Low</em>, <em>Medium</em>, and <em>High</em>) has an associated value (<em>60</em>, <em>40</em>, and <em>25</em>, respectively). Configuring a <em>Low</em> threshold means that more rules will have to match the current request for the WAF to apply the configured ruleset action.</p>
<p>When the OWASP Anomaly Score Threshold is set to <em>High</em>, file uploads may trigger the <code>949110: Inbound Anomaly Score Exceeded</code> rule due to the lower amount of scoring rules needed. Consider <a href="/waf/managed-rules/reference/owasp-core-ruleset/configure-dashboard/#ruleset-level-configuration">adjusting the score threshold</a>, <a href="/waf/managed-rules/reference/owasp-core-ruleset/configure-dashboard/#rule-level-configuration">adjusting individual rules</a> in the ruleset, or <a href="/waf/managed-rules/waf-exceptions/">creating an exception</a> if excessive false positives occur.</p>
<p>For an example, refer to <a href="/waf/managed-rules/reference/owasp-core-ruleset/example/">OWASP evaluation example</a>.</p>
