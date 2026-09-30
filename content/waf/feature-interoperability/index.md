<p>Cloudflare applies multiple security features to every incoming request. Each feature runs at a specific stage, and the order determines which feature acts first. Understanding this order helps you avoid conflicts and reduce false positives.</p>
<h2 id="execution-order">Execution order</h2>
<p>Cloudflare security features powered by the <a href="/ruleset-engine/">Ruleset Engine</a> run in a fixed sequence of phases. When a request arrives, it passes through each phase in order. If a rule takes a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/167.md")
</div> (for example, _Block_ or _Managed Challenge_), the request stops and does not reach later phases.
<p>The security-related request phases, in execution order, are:</p>
<table>
<thead>
<tr>
<th>Phase name</th>
<th>Product</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ddos_l7</code></td>
<td><a href="/ddos-protection/managed-rulesets/http/">HTTP DDoS Attack Protection</a></td>
</tr>
<tr>
<td><code>http_request_firewall_custom</code></td>
<td><a href="/waf/custom-rules/">Custom rules</a></td>
</tr>
<tr>
<td><code>http_ratelimit</code></td>
<td><a href="/waf/rate-limiting-rules/">Rate limiting rules</a></td>
</tr>
<tr>
<td><code>http_request_firewall_managed</code></td>
<td><a href="/waf/managed-rules/">Managed Rules</a></td>
</tr>
<tr>
<td><code>http_request_sbfm</code></td>
<td><a href="/bots/get-started/super-bot-fight-mode/">Super Bot Fight Mode</a></td>
</tr>
</tbody>
</table>
<p>Within each phase, account-level rulesets run before zone-level rulesets.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/166.md")
</aside>
<p>The Ruleset Engine powers many Cloudflare products beyond security. Refer to <a href="/ruleset-engine/reference/phases-list/">Phases list</a> for the complete list of request and response phases.</p>
<h3 id="features-outside-the-ruleset-engine">Features outside the Ruleset Engine</h3>
<p>The following security features are not powered by the Ruleset Engine and are evaluated independently:</p>
<ul>
<li><a href="/waf/tools/ip-access-rules/">IP Access Rules</a></li>
<li><a href="/waf/tools/zone-lockdown/">Zone Lockdown</a></li>
<li><a href="/waf/tools/user-agent-blocking/">User Agent Blocking</a></li>
<li><a href="/waf/tools/browser-integrity-check/">Browser Integrity Check</a></li>
<li><a href="/waf/tools/scrape-shield/hotlink-protection/">Hotlink Protection</a></li>
<li><a href="/waf/tools/security-level/">Security Level</a></li>
</ul>
<p>Because these features run independently, they do not follow the phase order described above.</p>
<h2 id="security-features-overview">Security features overview</h2>
<h3 id="ddos-protection">DDoS protection</h3>
<p><a href="/ddos-protection/">DDoS protection</a> is always on for all Cloudflare plans. L7 HTTP DDoS Attack Protection detects and mitigates application-layer DDoS attacks. L3/4 Network-layer DDoS Attack Protection handles network-layer attacks. You do not need to turn on or configure anything for DDoS protection to work.</p>
<h3 id="custom-rules">Custom rules</h3>
<p><a href="/waf/custom-rules/">Custom rules</a> are rules you define. They run in the <code>http_request_firewall_custom</code> phase and support actions like <em>Block</em>, <em>Managed Challenge</em>, <em>Skip</em>, and <em>Log</em>. You can reference <a href="/bots/concepts/bot-score/">bot score</a> fields, <a href="/waf/detections/attack-score/">WAF attack score</a> fields, and all standard request fields in your expressions.</p>
<h3 id="rate-limiting-rules">Rate limiting rules</h3>
<p><a href="/waf/rate-limiting-rules/">Rate limiting rules</a> throttle or block traffic that exceeds a defined request rate. They run in the <code>http_ratelimit</code> phase, after custom rules.</p>
<h3 id="managed-rules">Managed Rules</h3>
<p><a href="/waf/managed-rules/">Managed Rules</a> are pre-configured rulesets maintained by Cloudflare. These include the <a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/">Cloudflare Managed Ruleset</a> and the <a href="/waf/managed-rules/reference/owasp-core-ruleset/">OWASP Core Ruleset</a>. They run in the <code>http_request_firewall_managed</code> phase.</p>
<h3 id="bot-fight-mode">Bot Fight Mode</h3>
<p><a href="/bots/get-started/bot-fight-mode/">Bot Fight Mode</a> is available on Free plans. It is a simple on/off toggle that challenges traffic matching patterns of known bots. You cannot customize its behavior or skip it with custom rules.</p>
<h3 id="super-bot-fight-mode">Super Bot Fight Mode</h3>
<p><a href="/bots/get-started/super-bot-fight-mode/">Super Bot Fight Mode</a> (SBFM) is available on Pro, Business, and Enterprise plans (without the Bot Management add-on). It runs in the <code>http_request_sbfm</code> phase and offers more control than Bot Fight Mode. You can configure separate actions for <strong>Definitely automated</strong>, <strong>Likely automated</strong>, and <strong>Verified bots</strong> traffic. You can skip SBFM for specific requests using the <a href="/waf/custom-rules/skip/"><em>Skip</em> action</a> in custom rules.</p>
<h3 id="bot-management">Bot Management</h3>
<p><a href="/bots/get-started/bot-management/">Bot Management</a> is an Enterprise add-on. It generates a bot score from <code>1</code> to <code>99</code> for every request. Lower scores indicate more automated traffic. You write custom rules using the <code>cf.bot_management.score</code> field to take action based on this score. For more information, refer to <a href="/bots/reference/bot-management-variables/">Bot Management variables</a>.</p>
<h2 id="key-interaction-rules">Key interaction rules</h2>
<p>These rules govern how security features interact:</p>
<ul>
<li><strong>Terminating actions stop the request evaluation workflow.</strong> If a rule blocks or challenges a request, Cloudflare does not evaluate later phases for that request.</li>
<li><strong>Custom rules run before SBFM.</strong> A terminating action in custom rules prevents Super Bot Fight Mode from evaluating the request.</li>
<li><strong>Skip actions bypass later phases.</strong> You can use the <a href="/waf/custom-rules/skip/options/"><em>Skip</em> action</a> in custom rules to bypass rate limiting rules (<code>http_ratelimit</code>), Super Bot Fight Mode (<code>http_request_sbfm</code>), and Managed Rules (<code>http_request_firewall_managed</code>).</li>
<li><strong>Bot Fight Mode cannot be skipped.</strong> Because Bot Fight Mode is not part of the Ruleset Engine, custom rules cannot skip it. If you need to exempt traffic from bot protection, upgrade to Super Bot Fight Mode or Bot Management.</li>
<li><strong>Bot Management scores are available in custom rules.</strong> Enterprise customers with Bot Management can use <code>cf.bot_management.score</code> in custom rule expressions to define custom thresholds per path, user agent, or any other request property.</li>
</ul>
<h2 id="common-scenarios">Common scenarios</h2>
<h3 id="small-business-website-free-plan">Small business website (Free plan)</h3>
<p>A Free plan includes DDoS protection and Bot Fight Mode.</p>
<ul>
<li>DDoS protection runs automatically on every request.</li>
<li>Turn on <strong>Bot Fight Mode</strong> under <strong>Security</strong> &gt; <strong>Settings</strong> to challenge known bot patterns.</li>
<li>Turn on <strong>Block AI Bots</strong> to prevent AI crawlers from scraping your content.</li>
</ul>
<p>Because Bot Fight Mode cannot be skipped or customized, you cannot create exceptions for specific bots. If Bot Fight Mode causes false positives for legitimate automated traffic (for example, monitoring services or payment processors), consider upgrading to a Pro or Business plan that includes Super Bot Fight Mode.</p>
<h3 id="e-commerce-site-pro-or-business-plan">E-commerce site (Pro or Business plan)</h3>
<p>A Pro or Business plan adds Super Bot Fight Mode, custom rules, and Managed Rules.</p>
<ul>
<li>DDoS protection runs automatically.</li>
<li>Turn on <strong>Super Bot Fight Mode</strong> to block automated and likely automated traffic.</li>
<li>Deploy <strong>Managed Rules</strong> for protection against known vulnerabilities like SQL injection and cross-site scripting.</li>
<li>Create custom rules with the <em>Skip</em> action to allow legitimate automated traffic while SBFM blocks bad bots everywhere else. Use the following rule configuration:
<ul>
<li>Set the rule expression to match the IP addresses or user agents of your payment processor.</li>
<li>Set the action to <em>Skip</em>, and select <strong>Super Bot Fight Mode</strong>.</li>
</ul>
</li>
</ul>
<h3 id="enterprise-api-and-website-enterprise-plan">Enterprise API and website (Enterprise plan)</h3>
<p>An Enterprise plan with the Bot Management add-on provides the most flexibility.</p>
<ul>
<li>DDoS protection runs automatically.</li>
<li>Bot Management generates a bot score on every request.</li>
<li>Create custom rules that reference <code>cf.bot_management.score</code> to define your own thresholds. For example, block requests with a bot score below 30 for website paths, while allowing all scores on API paths that authenticated partners use.</li>
<li>Use rate limiting rules to throttle abusive traffic patterns.</li>
<li>Deploy Managed Rules to protect against known vulnerabilities.</li>
</ul>
<h2 id="troubleshoot-conflicts">Troubleshoot conflicts</h2>
<p>When security features interfere with legitimate traffic, use the following steps to identify and resolve the issue.</p>
<h3 id="identify-which-feature-blocked-a-request">Identify which feature blocked a request</h3>
<p>Use <a href="/waf/analytics/security-events/">Security Events</a> to identify the feature that blocked a request:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Analytics</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Events</strong> tab.</li>
<li>Find the blocked request in the log.</li>
<li>Check the <strong>Service</strong> field to determine which product took the action. This field tells you which feature to adjust.</li>
</ol>
<h3 id="resolve-bot-fight-mode-false-positives">Resolve Bot Fight Mode false positives</h3>
<p>Bot Fight Mode does not support exceptions. You have two options:</p>
<ul>
<li>Turn off Bot Fight Mode entirely under <strong>Security</strong> &gt; <strong>Settings</strong>.</li>
<li>Upgrade to a plan with Super Bot Fight Mode, which supports skip rules.</li>
</ul>
<p>For more information, refer to <a href="/bots/troubleshooting/false-positives/">Handle false positives from Bot Fight Mode or Super Bot Fight Mode</a>.</p>
<h3 id="resolve-super-bot-fight-mode-false-positives">Resolve Super Bot Fight Mode false positives</h3>
<p>Create a custom rule with the <em>Skip</em> action to bypass SBFM for the affected traffic:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/168.md")
</div>
<p>For more information, refer to <a href="/bots/troubleshooting/false-positives/">Handle false positives from Bot Fight Mode or Super Bot Fight Mode</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/165.md")
</aside>
<h3 id="resolve-managed-rules-false-positives">Resolve Managed Rules false positives</h3>
<p>If a managed rule blocks legitimate traffic:</p>
<ul>
<li>Create a <a href="/waf/managed-rules/waf-exceptions/">WAF exception</a> to skip specific rules or rulesets for matching requests.</li>
<li>Disable individual rules within a managed ruleset if they do not apply to your application.</li>
</ul>
<p>For detailed guidance, refer to <a href="/waf/managed-rules/troubleshooting/">Troubleshoot managed rules</a>.</p>
