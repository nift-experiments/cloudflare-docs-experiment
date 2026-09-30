<p>The Cloudflare Web Application Firewall (Cloudflare WAF) checks incoming web and API requests and filters undesired traffic based on sets of rules called rulesets.</p>
<p>This page will guide you through the recommended initial steps for configuring the WAF to get immediate protection against the most common attacks.</p>
<p>Refer to <a href="/waf/concepts/">Concepts</a> for more information on WAF concepts, main components, and roles.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/154.md")
</aside>
<div class="video-frame"><img class="video-poster" src="https://imagedelivery.net/xDOJvHcv1KwTQn6S-BGFIw/b8137b46-e0dd-45ab-b24f-4edab0fa0b00/public" alt="Application Security: Get started guide"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/1a426a3ae597ae3935eb97b5f97f106f/iframe?preload=true&amp;letterboxColor=transparent" title="Application Security: Get started guide" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<h2 id="before-you-begin">Before you begin</h2>
<ul>
<li>Make sure that you have <a href="/fundamentals/account/">set up a Cloudflare account</a> and <a href="/fundamentals/manage-domains/add-site/">added your domain</a> to Cloudflare.</li>
<li>Users on the Free plan have access to the Cloudflare Free Managed Ruleset, a subset of the Cloudflare Managed Ruleset. The Free Managed Ruleset is deployed by default on Free plans and is not specifically covered in this guide.<br/>If you are on a Free plan, you may skip to <a href="#5-review-traffic-in-security-dashboards">5. Review traffic in security dashboards</a>.</li>
</ul>
<h2 id="1-deploy-the-cloudflare-managed-ruleset"><ol>
<li>Deploy the Cloudflare Managed Ruleset</li>
</ol></h2>
<p>The <a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/">Cloudflare Managed Ruleset</a> protects against Common Vulnerabilities and Exposures (CVEs) and known attack vectors. This ruleset is designed to identify common attacks using signatures, while generating low false positives. Rule changes are published on a weekly basis in the <a href="/waf/change-log/">WAF changelog</a>. Cloudflare may also add rules at any time during emergency releases for high profile zero-day protection.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/155.md")
</div>
<details class="nb-details"><summary>Default settings and ruleset customization</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/156.md")
</div></details>
<h2 id="2-create-custom-rule-based-on-waf-attack-score"><ol start="2">
<li>Create custom rule based on WAF attack score</li>
</ol></h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/152.md")
</aside>
<p><a href="/waf/detections/attack-score/">WAF attack score</a> is a machine-learning layer that complements Cloudflare's managed rulesets, providing additional protection against <a href="https://www.cloudflare.com/learning/security/threats/sql-injection/">SQL injection</a> (SQLi), <a href="https://www.cloudflare.com/learning/security/threats/cross-site-scripting/">cross-site scripting</a> (XSS), and many <a href="https://www.cloudflare.com/learning/security/what-is-remote-code-execution/">remote code execution</a> (RCE) attacks. It helps identify rule bypasses and potentially new, undiscovered attacks.</p>
<p>If you are an Enterprise customer, do the following:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/158.md")
</div>
<p>If you are on a Business plan, create a custom rule as mentioned above but use the <a href="/waf/detections/attack-score/#available-scores">WAF Attack Score Class</a> field instead. For example, you could use the following rule expression: <code>WAF Attack Score Class equals Attack</code>.</p>
<h2 id="3-configure-bot-protection"><ol start="3">
<li>Configure bot protection</li>
</ol></h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/151.md")
</aside>
<p>Enterprise customers with Bot Management should first configure bot protection using <strong>Security Settings</strong>, which provide baseline protection without creating custom rules:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/159.md")
</div>
<p>These built-in settings auto-update with new bot signatures and do not count toward your custom rule limits. For more details, refer to <a href="/bots/get-started/bot-management/">Bot Management</a>.</p>
<h3 id="create-a-custom-rule-for-additional-control">Create a custom rule for additional control</h3>
<p>Optionally, if you need more granular control — for example, a different score threshold or rules that combine bot score with other fields — <a href="/waf/custom-rules/create-dashboard/">create a custom rule</a> using the <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/160.md")
</div> and <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/161.md")
</div> fields:
<ul>
<li><strong>When incoming requests match</strong>:</li>
</ul>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
</tr>
</thead>
<tbody>
<tr>
<td>Bot Score</td>
<td>less than</td>
<td><code>20</code></td>
<td>And</td>
</tr>
<tr>
<td>Verified Bot</td>
<td>equals</td>
<td>Off</td>
<td></td>
</tr>
</tbody>
</table>
<ul>
<li><strong>Choose action</strong>: Managed Challenge</li>
</ul>
<p>This rule uses a threshold of 20 (instead of the default threshold of 30 used by the settings), providing stricter protection for traffic in the 20-29 score range.</p>
<p>For a more comprehensive example of baseline protection against malicious bots, refer to <a href="/waf/custom-rules/use-cases/challenge-bad-bots/#general-protection">Challenge bad bots</a>.</p>
<p>For more information about the bot-related fields you can use in expressions, refer to <a href="/bots/reference/bot-management-variables/">Bot Management variables</a>.</p>
<p>Once you have deployed the Cloudflare Managed Ruleset and rules based on attack score and bot score, you will have achieved substantial protection, limiting the chance of false positives.</p>
<h2 id="4-optional-deploy-the-cloudflare-owasp-core-ruleset"><ol start="4">
<li>(Optional) Deploy the Cloudflare OWASP Core Ruleset</li>
</ol></h2>
<p>After configuring the Cloudflare Managed Ruleset and attack score, you can also deploy the <a href="/waf/managed-rules/reference/owasp-core-ruleset/">Cloudflare OWASP Core Ruleset</a>. This managed ruleset is Cloudflare's implementation of the OWASP ModSecurity Core Rule Set. Its attack coverage significantly overlaps with Cloudflare Managed Ruleset by detecting common attack vectors such as SQLi and XSS.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/150.md")
</aside>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/162.md")
</div>
<details class="nb-details"><summary>Ruleset configuration</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/163.md")
</div></details>
<h2 id="5-review-traffic-in-security-dashboards"><ol start="5">
<li>Review traffic in security dashboards</li>
</ol></h2>
<p>After setting up your WAF configuration, review how incoming traffic is being affected by your current settings using the following dashboards:</p>
<ul>
<li>Use <a href="/waf/analytics/security-analytics/">Security Analytics</a> to explore all traffic, including traffic not affected by WAF mitigation measures. All data provided by <a href="/waf/concepts/#available-traffic-detections">traffic detections</a> is available in this dashboard.</li>
<li>Use <a href="/waf/analytics/security-events/">Security Events</a> to get more information about requests that are being mitigated by Cloudflare security products.</li>
</ul>
<p>Enterprise customers can also obtain data about HTTP requests and security events using <a href="/logs/">Cloudflare Logs</a>.</p>
<h2 id="6-optional-next-steps"><ol start="6">
<li>(Optional) Next steps</li>
</ol></h2>
<p>After configuring the WAF based on the information in the previous sections, you should have a strong base protection against possible threats to your applications.</p>
<p>You can explore the following recommendations to get additional protection for specific use cases.</p>
<h3 id="allowlist-certain-ip-addresses">Allowlist certain IP addresses</h3>
<p>Create a custom rule to <a href="/waf/custom-rules/use-cases/allow-traffic-from-ips-in-allowlist/">allow traffic from IP addresses in allowlist only</a>.</p>
<h3 id="block-specific-countries">Block specific countries</h3>
<p>Create a custom rule to <a href="/waf/custom-rules/use-cases/block-traffic-from-specific-countries/">block traffic from specific countries</a>.</p>
<h3 id="define-rate-limits">Define rate limits</h3>
<p>Create a rate limiting rule to <a href="/waf/rate-limiting-rules/use-cases/#example-1">apply rate limiting on a login endpoint</a>.</p>
<h3 id="prevent-credential-stuffing-attacks">Prevent credential stuffing attacks</h3>
<p>Use <a href="/waf/detections/leaked-credentials/">leaked credentials detection</a> to prevent <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/164.md")
</div> attacks on your applications.
<h3 id="prevent-users-from-uploading-malware-into-your-applications">Prevent users from uploading malware into your applications</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/149.md")
</aside>
<p><a href="/waf/detections/malicious-uploads/get-started/">Use WAF content scanning</a> to scan content being uploaded to your application, searching for malicious content.</p>
<h3 id="get-additional-security-for-your-apis">Get additional security for your APIs</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/148.md")
</aside>
<p>Cloudflare protects your APIs from new and known application attacks and exploits such as SQL injection attacks. API-specific security products extend those protections to the unique risks in APIs such as API discovery and authentication management.</p>
<p>For more information on Cloudflare's API security features, refer to <a href="/api-shield/">Cloudflare API Shield</a>.</p>
<h3 id="protect-your-origin-server">Protect your origin server</h3>
<p>For information on how to prevent attackers from discovering or overloading your origin server, refer to <a href="/fundamentals/security/protect-your-origin-server/">Protect your origin server</a> for a layered approach including proxied DNS, IP allowlisting, and authenticated origin pulls.</p>
