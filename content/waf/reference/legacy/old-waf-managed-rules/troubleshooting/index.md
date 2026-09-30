<p>By default, WAF managed rules are fully managed via the Cloudflare dashboard and are compatible with most websites and web applications. However, false positives and false negatives may occur:</p>
<ul>
<li><strong>False positives</strong>: Legitimate requests detected and filtered as malicious.</li>
<li><strong>False negatives</strong>: Malicious requests not filtered.</li>
</ul>
<h2 id="troubleshoot-false-positives">Troubleshoot false positives</h2>
<p>The definition of suspicious content is subjective for each website. For example, PHP code posted to your website is normally suspicious. However, your website may be teaching how to code and it may require PHP code submissions from visitors. In this situation, you should disable related managed rules for this website, since they would interfere with normal website operation.</p>
<p>To test for false positives, set WAF managed rules to <em>Simulate</em> mode. This mode allows you to record the response to possible attacks without challenging or blocking incoming requests. Also, review the Security Events' <a href="/waf/analytics/security-events/#sampled-logs">sampled logs</a> to determine which managed rules caused false positives.</p>
<p>If you find a false positive, there are several potential resolutions:</p>
<ul>
<li><strong>Add the client’s IP addresses to the <a href="/waf/tools/ip-access-rules/">IP Access Rules</a> allowlist:</strong> If the browser or client visits from the same IP addresses, allowing is recommended.</li>
<li><strong>Disable the corresponding managed rule(s)</strong>: Stops blocking or challenging false positives, but reduces overall site security. A request blocked by Rule ID <code>981176</code> refers to OWASP rules. Decrease OWASP sensitivity to resolve the issue.</li>
<li><strong>Bypass WAF managed rules with a firewall rule (deprecated):</strong> <a href="/firewall/cf-dashboard/create-edit-delete-rules/#create-a-firewall-rule">Create a firewall rule</a> with the <em>Bypass</em> action to deactivate WAF managed rules for a specific combination of parameters. For example, <a href="/firewall/cf-firewall-rules/actions/">bypass managed rules</a> for a specific URL and a specific IP address or user agent.</li>
<li><strong>(Not recommended) Disable WAF managed rules for traffic to a URL:</strong> Lowers security on the particular URL endpoint. Configured via <a href="/rules/page-rules/">Page Rules</a>.</li>
</ul>
<p>Additional guidelines are as follows:</p>
<ul>
<li>If one specific rule causes false positives, set rule’s <strong>Mode</strong> to <em>Disable</em> rather than turning <em>Off</em> the entire rule <strong>Group</strong>.</li>
<li>For false positives with the administrator section of your website, create a <a href="/rules/page-rules/">page rule</a> to <strong>Disable Security</strong> for the admin section of your site resources — for example, <code>example.com/admin</code>.</li>
</ul>
<h2 id="troubleshoot-false-negatives">Troubleshoot false negatives</h2>
<p>To identify false negatives, review the HTTP logs on your origin web server. To reduce false negatives, use the following checklist:</p>
<ul>
<li>
<p>Are WAF managed rules enabled in <strong>Security</strong> &gt; <strong>WAF</strong> &gt; <strong>Managed rules</strong>?</p>
</li>
<li>
<p>Are WAF managed rules being disabled via <a href="/rules/page-rules/">Page Rules</a>?</p>
</li>
<li>
<p>Not all managed rules are enabled by default, so review individual managed rule default actions.</p>
<ul>
<li>For example, Cloudflare allows requests with empty user agents by default. To block requests with an empty user agent, change the rule <strong>Mode</strong> to <em>Block</em>.</li>
<li>Another example: if you are looking to block unmitigated SQL injection attacks, make sure the relevant SQLi rules are enabled and set to <em>Block</em> under the <strong>Cloudflare Specials</strong> group.</li>
</ul>
</li>
<li>
<p>Are DNS records that serve HTTP traffic proxied through Cloudflare?</p>
</li>
<li>
<p>Is a firewall rule <a href="/firewall/cf-firewall-rules/actions/#supported-actions">bypassing</a> managed rules?</p>
</li>
<li>
<p>Does an allowed country, ASN, IP range, or IP address in <a href="/waf/tools/ip-access-rules/">IP Access rules</a> or <a href="/firewall/cf-firewall-rules/">firewall rules</a> match the attack traffic?</p>
</li>
<li>
<p>Is the malicious traffic reaching your origin IP addresses directly to bypass Cloudflare protection? Block all traffic except from <a href="/fundamentals/concepts/cloudflare-ip-addresses/">Cloudflare's IP addresses</a> at your origin web server.</p>
</li>
</ul>
