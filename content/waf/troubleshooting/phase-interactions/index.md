<p>Cloudflare evaluates request processing features in <a href="/ruleset-engine/about/phases/">phases</a>. A rule that appears correct in isolation can behave differently when another product has already modified or terminated the request.</p>
<h2 id="custom-rules-are-evaluated-against-the-rewritten-url">Custom rules are evaluated against the rewritten URL</h2>
<p>Cloudflare applies <a href="/rules/transform/url-rewrite/">URL Rewrite Rules</a> before <a href="/waf/custom-rules/">custom rules</a>.</p>
<p>If a transform rule rewrites <code>/public-login</code> to <code>/internal/login</code>, later WAF phases will evaluate the rewritten path.</p>
<p>This means that:</p>
<ul>
<li>A custom rule matching <code>/public-login</code> may not fire after the rewrite.</li>
<li>A custom rule matching <code>/internal/login</code> may fire even though the visitor requested <code>/public-login</code>.</li>
</ul>
<h3 id="resolution">Resolution</h3>
<p>When troubleshooting a custom rule, check whether a rewrite rule already changed the URL before WAF evaluation. You can use <a href="/rules/trace-request/">Trace</a> to check the evaluation order of your rules based on an example request.</p>
<p>For more information, refer to the request execution order in <a href="/ruleset-engine/reference/phases-list/#application-layer">Phases list</a>.</p>
<h2 id="ip-access-rules-can-bypass-custom-rules">IP Access rules can bypass custom rules</h2>
<p><a href="/waf/tools/ip-access-rules/">IP Access rules</a> run before WAF custom rules.</p>
<p>If an IP Access rule with an <strong>Allow</strong> action matches a request, Cloudflare will not evaluate later custom rules for that request.</p>
<h3 id="what-this-means">What this means</h3>
<ul>
<li>A custom rule may appear to &quot;not fire&quot; for a specific IP address even though the expression is correct.</li>
<li>Allowlisting a source IP address too early can prevent other app security logic from running (namely custom rules).</li>
</ul>
<h3 id="resolution-1">Resolution</h3>
<p>If a request is unexpectedly bypassing a custom rule, check for matching IP Access rules first.</p>
<h2 id="skip-and-allow-do-not-behave-the-same-way">Skip and Allow do not behave the same way</h2>
<p>The <em>Allow</em> action in IP Access rules has a different behavior from the <em>Skip</em> action available in WAF custom rules.</p>
<p>The <em>Allow</em> action in IP Access rules bypasses WAF custom rules, rate limiting rules, WAF Managed Rules (except for country-level entries), and deprecated firewall rules. Any matches do not appear in <a href="/waf/analytics/security-events/">Security Events</a>. An allowed request never reaches WAF custom rules, including any logging or tracking rules.</p>
<p>The <em>Skip</em> action in WAF custom rules instructs Cloudflare to selectively skip certain application security products or components, such as WAF managed rules. Depending on the configuration of the custom rule with the <em>Skip</em> action, other security products will still evaluate the request and might block it.</p>
<p>WAF custom rules do not have an <em>Allow</em> action. To control what a matching request bypasses, you must use the <a href="/waf/custom-rules/skip/"><em>Skip</em></a> action and select the specific products or phases to skip.</p>
<h3 id="resolution-2">Resolution</h3>
<p>Review your configuration (namely IP Access rules and custom rules with the <em>Skip</em> action) to ensure the intended behavior is achieved.</p>
<p>If specific rules of <a href="/waf/managed-rules/">WAF managed rulesets</a> are blocking requests you want to allow, you can create <a href="/waf/managed-rules/waf-exceptions/">managed rules exceptions</a> to skip specific managed rules or rulesets for particular requests instead of skipping WAF Managed Rules entirely.</p>
<h2 id="page-rules-do-not-use-the-same-request-view-as-modern-rules">Page Rules do not use the same request view as modern rules</h2>
<p><a href="/rules/page-rules/">Page Rules</a> are legacy behavior and do not line up exactly with modern Rules products.</p>
<p>In mixed configurations, you may see:</p>
<ul>
<li>A rewrite affecting custom rules and Managed Rules</li>
<li>Different results between a Page Rule and a modern rule that appear to target the same path</li>
</ul>
<h3 id="resolution-3">Resolution</h3>
<p>When possible, migrate older Page Rules behavior to the current Rules products so the request is evaluated in one model.</p>
<h2 id="recommended-troubleshooting-workflow">Recommended troubleshooting workflow</h2>
<p>When a WAF decision looks incorrect:</p>
<ol>
<li>Check for earlier request rewrites.</li>
<li>Check for matching IP Access rules.</li>
<li>Confirm whether the request was expected to stop in the custom rules phase or skip later phases.</li>
<li>Review whether a managed rule still ran after a custom rule match.</li>
<li>Use <a href="/rules/trace-request/">Trace</a> when available to confirm the actual phase-by-phase result.</li>
</ol>
