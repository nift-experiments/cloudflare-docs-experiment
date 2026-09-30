<p>This page describes the security settings available in the new security dashboard for a given domain.</p>
<p>To access security settings in the new security dashboard, go to the <strong>Settings</strong> page.</p>
<div class="nb-dash-button"></div>
<h2 id="security-setting-categories">Security setting categories</h2>
<p>Security settings and detection tools are categorized by the type of threat that they detect and mitigate.</p>
<h3 id="web-application-exploits">Web application exploits</h3>
<p>In the <strong>Web application exploits</strong> security category you can manage the following settings:</p>
<ul>
<li>Detection tools:
<ul>
<li><a href="/waf/detections/leaked-credentials/">Leaked credentials detection</a></li>
<li><a href="/waf/detections/malicious-uploads/">Malicious uploads detection</a></li>
<li><a href="/waf/managed-rules/reference/sensitive-data-detection/">Sensitive data detection</a></li>
<li><a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/">Cloudflare managed ruleset</a></li>
<li><a href="/waf/managed-rules/reference/owasp-core-ruleset/">OWASP Core</a> ruleset</li>
<li><a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a></li>
</ul>
</li>
<li><a href="/fundamentals/reference/under-attack-mode/">Under Attack mode</a> in Security Level</li>
<li>Managed <a href="/security-center/infrastructure/security-file/">security.txt</a></li>
</ul>
<p>Refer to each linked page for details.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/357.md")
</aside>
<h3 id="ddos-attacks">DDoS attacks</h3>
<p>The <strong>DDoS attacks</strong> security category shows the multiple mitigation services against DDoS attacks provided by Cloudflare.</p>
<p>You can create rules to override DDoS attack protection tools. DDoS attack protection overrides are only available to Enterprise customers with the Advanced DDoS Protection subscription.</p>
<p>To learn more about DDoS protection overrides, refer to the following resources:</p>
<ul>
<li><a href="/ddos-protection/managed-rulesets/http/http-overrides/">HTTP DDoS attack protection overrides</a></li>
<li><a href="/ddos-protection/managed-rulesets/network/network-overrides/">Network-layer DDoS attack protection overrides</a></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/356.md")
</aside>
<p>Additionally, you can manage the following settings:</p>
<ul>
<li><a href="/bots/concepts/bot/#ai-bots">Block AI Bots</a></li>
<li><a href="/bots/get-started/bot-management/">Bot Management</a> (depending on your Enterprise subscriptions)</li>
<li><a href="/waf/tools/browser-integrity-check/">Browser Integrity Check</a></li>
<li><a href="/cloudflare-challenges/challenge-types/challenge-pages/challenge-passage/">Challenge Passage</a></li>
<li><a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/">Cloudflare managed ruleset</a></li>
<li><a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a></li>
<li><a href="/api-shield/management-and-monitoring/endpoint-management/schema-learning/">Schema learning</a></li>
<li><a href="/api-shield/security/schema-validation/">Schema validation</a> (requires an uploaded schema)</li>
<li><a href="/fundamentals/reference/under-attack-mode/">Under Attack mode</a> (under Security Level)</li>
<li>SSL/TLS DDoS attack protection</li>
</ul>
<h3 id="bot-traffic">Bot traffic</h3>
<p>In the <strong>Bot traffic</strong> security category you can manage the following settings:</p>
<ul>
<li><a href="/bots/additional-configurations/ai-labyrinth/">AI Labyrinth</a></li>
<li><a href="/bots/concepts/bot/#ai-bots">Block AI Bots</a></li>
<li><a href="/bots/get-started/bot-fight-mode/">Bot fight mode</a> (depending on your Cloudflare plan)</li>
<li><a href="/bots/get-started/super-bot-fight-mode/">Super Bot fight mode</a> (depending on your Cloudflare plan)</li>
<li><a href="/bots/get-started/bot-management/">Bot Management</a> (depending on your Enterprise subscriptions)</li>
<li>AI bot traffic management with <a href="/bots/additional-configurations/managed-robots-txt/">robots.txt</a></li>
<li>API <a href="/api-shield/security/sequence-analytics/">sequence detection</a> (requires you to configure a session identifier)</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/355.md")
</aside>
<h3 id="api-abuse">API abuse</h3>
<p>In the <strong>API abuse</strong> security category you can manage the following settings:</p>
<ul>
<li><a href="/api-shield/management-and-monitoring/developer-portal/">Developer portal</a> creation</li>
<li>Web asset discovery (always enabled if included in your Enterprise subscriptions. For Enterprise subscriptions, <a href="/api-shield/security/api-discovery/">API endpoint discovery</a> is also included, which requires you to configure a <a href="/api-shield/management-and-monitoring/session-identifiers/">session identifier</a>)</li>
<li><a href="/api-shield/management-and-monitoring/endpoint-labels/">Endpoint labels</a></li>
<li><a href="/api-shield/security/jwt-validation/">JWT validation</a> (requires you to add a <a href="/api-shield/security/jwt-validation/api/#token-configurations">JWT configuration</a>)</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/354.md")
</aside>
<h3 id="client-side-abuse">Client-side abuse</h3>
<p>In the <strong>Client-side abuse</strong> security category you can manage the following settings:</p>
<ul>
<li><a href="/client-side-security/how-it-works/">Continuous script monitoring</a>:
<ul>
<li><a href="/client-side-security/reference/settings/#reporting-endpoint">Reporting endpoint</a> to use your hostname instead of a Cloudflare-owned endpoint (only for Enterprise customers with a paid add-on)</li>
<li><a href="/client-side-security/reference/settings/#connection-target-details">Data logged in client-side abuse reports</a> (only the hostname or the full URI)</li>
</ul>
</li>
<li><a href="/waf/tools/scrape-shield/email-address-obfuscation/">Email Address Obfuscation</a></li>
<li><a href="/waf/tools/scrape-shield/hotlink-protection/">Hotlink Protection</a></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/353.md")
</aside>
<h2 id="all-settings">All settings</h2>
<p>The following table links to additional information about each available setting:</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Location in previous dashboard navigation</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/bots/additional-configurations/ai-labyrinth/">AI Labyrinth</a></td>
<td><strong>Security</strong> &gt; <strong>Bots</strong> &gt; <strong>Configure Bot Fight Mode<br/>Security</strong> &gt; <strong>Bots</strong> &gt; <strong>Configure Super Bot Fight Mode<br/>Security</strong> &gt; <strong>Bots</strong> &gt; <strong>Configure Bot Management</strong></td>
</tr>
<tr>
<td><a href="/waf/detections/ai-security-for-apps/">AI Security for Apps</a></td>
<td><em>N/A</em></td>
</tr>
<tr>
<td><a href="/bots/concepts/bot/#ai-bots">Block AI Bots</a></td>
<td><strong>Security</strong> &gt; <strong>Bots</strong> &gt; <strong>Configure Bot Fight Mode<br/>Security</strong> &gt; <strong>Bots</strong> &gt; <strong>Configure Super Bot Fight Mode<br/>Security</strong> &gt; <strong>Bots</strong> &gt; <strong>Configure Bot Management</strong></td>
</tr>
<tr>
<td><a href="/bots/get-started/bot-management/">Bot Management</a>:</td>
<td><strong>Security</strong> &gt; <strong>Bots</strong></td>
</tr>
<tr>
<td>— <a href="/bots/additional-configurations/javascript-detections/">JS detections</a></td>
<td><strong>Security</strong> &gt; <strong>Bots</strong> &gt; <strong>Configure Super Bot Fight Mode<br/>Security</strong> &gt; <strong>Bots</strong> &gt; <strong>Configure Bot Management</strong></td>
</tr>
<tr>
<td>— <a href="/bots/reference/machine-learning-models/">Auto-update machine learning</a></td>
<td><strong>Security</strong> &gt; <strong>Bots</strong> &gt; <strong>Configure Bot Management</strong></td>
</tr>
<tr>
<td><a href="/waf/tools/browser-integrity-check/">Browser integrity check</a></td>
<td><strong>Security</strong> &gt; <strong>Settings</strong></td>
</tr>
<tr>
<td>Challenge Passage: <a href="/cloudflare-challenges/challenge-types/challenge-pages/challenge-passage/">Timeout</a></td>
<td><strong>Security</strong> &gt; <strong>Settings</strong></td>
</tr>
<tr>
<td><a href="/ssl/client-certificates/">Client certificates</a></td>
<td><strong>SSL</strong> &gt; <strong>Client Certificates</strong></td>
</tr>
<tr>
<td><a href="/waf/managed-rules/reference/cloudflare-managed-ruleset/">Cloudflare managed ruleset</a></td>
<td><strong>Security</strong> &gt; <strong>WAF</strong> &gt; <strong>Managed rules</strong> tab</td>
</tr>
<tr>
<td><a href="/client-side-security/how-it-works/">Continuous script monitoring</a>:</td>
<td><strong>Security</strong> &gt; <strong>Client-side security</strong></td>
</tr>
<tr>
<td>— <a href="/client-side-security/reference/settings/#reporting-endpoint">Reporting endpoint</a></td>
<td><strong>Security</strong> &gt; <strong>Client-side security</strong> &gt; <strong>Settings</strong></td>
</tr>
<tr>
<td>— <a href="/client-side-security/reference/settings/#connection-target-details">Data processing</a></td>
<td><strong>Security</strong> &gt; <strong>Client-side security</strong> &gt; <strong>Settings</strong></td>
</tr>
<tr>
<td>— <a href="/client-side-security/alerts/configure/">Alerts</a></td>
<td><strong>Security</strong> &gt; <strong>Client-side security</strong> &gt; <strong>Settings</strong><br/>Account Home &gt; <strong>Notifications</strong></td>
</tr>
<tr>
<td><a href="/api-shield/management-and-monitoring/developer-portal/">Create a developer portal</a></td>
<td><strong>Security</strong> &gt; <strong>API Shield</strong> &gt; <strong>Settings</strong></td>
</tr>
<tr>
<td><a href="/api-shield/security/schema-validation/#add-validation-by-adding-a-fallthrough-rule">Custom fallthrough rules</a></td>
<td><strong>Security</strong> &gt; <strong>API Shield</strong> &gt; <strong>Settings</strong></td>
</tr>
<tr>
<td><a href="/waf/tools/scrape-shield/email-address-obfuscation/">Email Address Obfuscation</a></td>
<td><strong>Scrape Shield</strong></td>
</tr>
<tr>
<td><a href="/api-shield/security/api-discovery/">API endpoint discovery</a>:</td>
<td><strong>API Shield</strong> &gt; <strong>Discovery</strong></td>
</tr>
<tr>
<td>— <a href="/api-shield/management-and-monitoring/session-identifiers/">Session identifiers</a></td>
<td><strong>Security</strong> &gt; <strong>API Shield</strong> &gt; <strong>Settings</strong></td>
</tr>
<tr>
<td><a href="/api-shield/management-and-monitoring/endpoint-labels/">Endpoint labels</a></td>
<td><strong>Security</strong> &gt; <strong>Settings</strong> &gt; <strong>Labels</strong></td>
</tr>
<tr>
<td><a href="/waf/tools/scrape-shield/hotlink-protection/">Hotlink Protection</a></td>
<td><strong>Scrape Shield</strong></td>
</tr>
<tr>
<td><a href="/ddos-protection/managed-rulesets/http/">HTTP DDoS attack protection</a>:</td>
<td><strong>Security</strong> &gt; <strong>DDoS</strong></td>
</tr>
<tr>
<td>— <a href="/ddos-protection/managed-rulesets/http/http-overrides/configure-dashboard/">Configure overrides</a></td>
<td><strong>Security</strong> &gt; <strong>DDoS</strong></td>
</tr>
<tr>
<td><a href="/bots/additional-configurations/managed-robots-txt/">Instruct AI bot traffic with robots.txt</a></td>
<td><strong>Security</strong> &gt; <strong>Bots</strong> &gt; <strong>Configure Bot Fight Mode<br/>Security</strong> &gt; <strong>Bots</strong> &gt; <strong>Configure Super Bot Fight Mode<br/>Security</strong> &gt; <strong>Bots</strong> &gt; <strong>Configure Bot Management</strong></td>
</tr>
<tr>
<td><a href="/waf/tools/ip-access-rules/">IP access rules</a></td>
<td><strong>Security</strong> &gt; <strong>WAF</strong> &gt; <strong>Tools</strong> tab<br/><strong>Security</strong> &gt; <strong>WAF</strong> &gt; <strong>Custom rules</strong> tab</td>
</tr>
<tr>
<td><a href="/waf/tools/lists/custom-lists/#ip-lists">IP lists</a></td>
<td>Account Home &gt; <strong>Manage Account</strong> &gt; <strong>Configurations</strong></td>
</tr>
<tr>
<td><a href="/api-shield/security/jwt-validation/">JWT validation</a>:</td>
<td><strong>Security</strong> &gt; <strong>API Shield</strong> &gt; <strong>Settings</strong></td>
</tr>
<tr>
<td>— <a href="/api-shield/security/jwt-validation/#add-a-jwt-validation-rule">JWT validation rules</a></td>
<td><strong>Security</strong> &gt; <strong>API Shield</strong> &gt; <strong>API Rules</strong></td>
</tr>
<tr>
<td>— <a href="/api-shield/security/jwt-validation/#add-a-token-validation-configuration">Token configurations</a></td>
<td><strong>Security</strong> &gt; <strong>API Shield</strong> &gt; <strong>Settings</strong></td>
</tr>
<tr>
<td><a href="/waf/detections/leaked-credentials/">Leaked credentials detection</a>:</td>
<td><strong>Security</strong> &gt; <strong>Settings</strong></td>
</tr>
<tr>
<td>— <a href="/waf/detections/leaked-credentials/#custom-detection-locations">Custom username and password location</a></td>
<td><strong>Security</strong> &gt; <strong>Settings</strong></td>
</tr>
<tr>
<td><a href="/waf/detections/malicious-uploads/">Malicious uploads detection</a>:</td>
<td><strong>Security</strong> &gt; <strong>Settings</strong></td>
</tr>
<tr>
<td>— <a href="/waf/detections/malicious-uploads/#custom-scan-expressions">Custom content location</a></td>
<td><strong>Security</strong> &gt; <strong>Settings</strong></td>
</tr>
<tr>
<td><a href="/api-shield/security/mtls/configure/">mTLS rules</a></td>
<td><strong>SSL/TLS</strong> &gt; <strong>Client Certificates</strong></td>
</tr>
<tr>
<td><a href="/ddos-protection/managed-rulesets/network/">Network-layer DDoS attack protection</a></td>
<td>Account Home &gt; <strong>L3/4 DDoS</strong> &gt; <strong>Network-layer DDoS Protection</strong></td>
</tr>
<tr>
<td><a href="/waf/managed-rules/reference/owasp-core-ruleset/">OWASP Core</a> ruleset</td>
<td><strong>Security</strong> &gt; <strong>WAF</strong> &gt; <strong>Managed rules</strong> tab</td>
</tr>
<tr>
<td>Rate limit authentication requests</td>
<td><strong>Security</strong> &gt; <strong>WAF</strong> &gt; <strong>Rate limiting rules</strong> tab</td>
</tr>
<tr>
<td><a href="/waf/tools/replace-insecure-js-libraries/">Replace insecure JavaScript libraries</a></td>
<td><strong>Security</strong> &gt; <strong>Settings</strong></td>
</tr>
<tr>
<td><a href="/api-shield/management-and-monitoring/endpoint-management/schema-learning/">Schema learning</a>:</td>
<td><strong>Security</strong> &gt; <strong>Web Assets</strong> &gt; <strong>Operations</strong></td>
</tr>
<tr>
<td>— <a href="/api-shield/management-and-monitoring/session-identifiers/">Session identifiers</a></td>
<td><strong>Security</strong> &gt; <strong>API Shield</strong> &gt; <strong>Settings</strong></td>
</tr>
<tr>
<td><a href="/api-shield/security/schema-validation/">Schema validation</a></td>
<td><strong>Security</strong> &gt; <strong>API Shield</strong> &gt; <strong>Schema Validation</strong></td>
</tr>
<tr>
<td>— <a href="/api-shield/management-and-monitoring/endpoint-management/">Operations</a></td>
<td><strong>Security</strong> &gt; <strong>Web Assets</strong> &gt; <strong>Operations</strong></td>
</tr>
<tr>
<td>— <a href="/api-shield/security/schema-validation/#view-active-schemas">Active schemas</a></td>
<td><strong>Security</strong> &gt; <strong>API Shield</strong> &gt; <strong>Schema Validation</strong></td>
</tr>
<tr>
<td><a href="/fundamentals/reference/under-attack-mode/">Security level: I'm under attack mode</a></td>
<td><strong>Security</strong> &gt; <strong>Settings</strong></td>
</tr>
<tr>
<td><a href="/security-center/infrastructure/security-file/">Security.txt</a></td>
<td><strong>Security</strong> &gt; <strong>Settings</strong></td>
</tr>
<tr>
<td><a href="/waf/managed-rules/reference/sensitive-data-detection/#configure-in-the-dashboard">Sensitive data detection</a> ruleset</td>
<td><strong>Security</strong> &gt; <strong>Sensitive Data</strong></td>
</tr>
<tr>
<td><a href="/api-shield/security/sequence-analytics/">Sequence detection</a>:</td>
<td><strong>Security</strong> &gt; <strong>API Shield</strong> &gt; <strong>API Rules</strong></td>
</tr>
<tr>
<td>— <a href="/api-shield/management-and-monitoring/endpoint-management/">Endpoints</a></td>
<td><strong>Security</strong> &gt; <strong>API Shield</strong></td>
</tr>
<tr>
<td>— <a href="/api-shield/management-and-monitoring/session-identifiers/">Session identifiers</a></td>
<td><strong>Security</strong> &gt; <strong>API Shield</strong> &gt; <strong>Settings</strong></td>
</tr>
<tr>
<td><a href="/api-shield/management-and-monitoring/session-identifiers/">Session identifiers</a></td>
<td><strong>Security</strong> &gt; <strong>API Shield</strong> &gt; <strong>Settings</strong></td>
</tr>
<tr>
<td><a href="/ddos-protection/managed-rulesets/">SSL/TLS DDoS attack protection</a></td>
<td><strong>Security</strong> &gt; <strong>DDoS</strong></td>
</tr>
<tr>
<td><a href="/api-shield/security/jwt-validation/">Token configurations</a></td>
<td><strong>Security</strong> &gt; <strong>API Shield</strong> &gt; <strong>Settings</strong></td>
</tr>
<tr>
<td><a href="/waf/tools/user-agent-blocking/">User agent blocking</a></td>
<td><strong>Security</strong> &gt; <strong>WAF</strong> &gt; <strong>Tools</strong> tab<br/><strong>Security</strong> &gt; <strong>WAF</strong> &gt; <strong>Custom rules</strong> tab</td>
</tr>
<tr>
<td><a href="/waf/tools/zone-lockdown/">Zone lockdown</a></td>
<td><strong>Security</strong> &gt; <strong>WAF</strong> &gt; <strong>Tools</strong> tab<br/><strong>Security</strong> &gt; <strong>WAF</strong> &gt; <strong>Custom rules</strong> tab</td>
</tr>
</tbody>
</table>
