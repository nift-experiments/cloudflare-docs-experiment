<aside class="nb-aside note">
<h3 class="nb-aside-title" id="user-permission">User permission</h3>
@markup("md", "content/.markup/bodies/13845.md")
</aside>
<p>Security Insights provides you with a list of insights, covering different areas of your Cloudflare environment, such as: Cloudflare account settings, DNS record configurations, SSL/TLS certificates configurations, Cloudflare Access configurations and Cloudflare WAF configurations.</p>
<p>Listed below are the specific insights currently available:</p>
<table>
<thead>
<tr>
<th>Insight Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/cloudflare-one/integrations/cloud-and-saas/troubleshooting/">CASB integration status</a></td>
<td>We detect unhealthy CASB integrations.</td>
</tr>
<tr>
<td><a href="/dns/manage-dns-records/reference/dns-record-types/#a-and-aaaa">Dangling <code>A</code> Records</a></td>
<td>A record is pointing to an IPv4 address that you might no longer control. You are at risk of a subdomain takeover.</td>
</tr>
<tr>
<td><a href="/dns/manage-dns-records/reference/dns-record-types/#a-and-aaaa">Dangling <code>AAAA</code> Records</a></td>
<td>A record is pointing to an IPv6 address that you might no longer control. You are at risk of a subdomain takeover.</td>
</tr>
<tr>
<td><a href="/dns/manage-dns-records/reference/dns-record-types/#a-and-aaaa">Dangling <code>CNAME</code> Records</a></td>
<td>A record is pointing to a resource that cannot be found. You are at risk of a subdomain takeover.</td>
</tr>
<tr>
<td><a href="/dns/manage-dns-records/reference/dns-record-types/#dmarc">DMARC Record Errors</a></td>
<td>We detect an incorrect or missing <code>DMARC</code> record.</td>
</tr>
<tr>
<td><a href="/ssl/get-started/">Domains missing TLS Encryption</a></td>
<td>We detect that there is no TLS encryption for this domain.</td>
</tr>
<tr>
<td><a href="/ssl/reference/protocols/">Domains supporting older TLS version</a></td>
<td>This domain supports older versions of the TLS protocol.</td>
</tr>
<tr>
<td><a href="/ssl/edge-certificates/additional-options/always-use-https/">Domains without 'Always Use HTTPS'</a></td>
<td>HTTP requests to this domain may not redirect to its HTTPS equivalent.</td>
</tr>
<tr>
<td><a href="/ssl/edge-certificates/additional-options/http-strict-transport-security/">Domains without HSTS</a></td>
<td>HTTP Strict Transport Security (<code>HSTS</code>), is a header which allows a website to specify and enforce security policy in client web browsers. This policy enforcement protects secure websites from downgrade attacks SSL stripping and cookie hijacking.</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/">Exposed RDP Servers</a></td>
<td>We detect an RDP server that is exposed to the public Internet.</td>
</tr>
<tr>
<td><a href="/client-side-security/alerts/">Get notified of malicious client-side scripts</a></td>
<td>We detect that client-side security alerts are not configured. You will not receive notifications when we detect potential malicious scripts executing in your client-side environment.</td>
</tr>
<tr>
<td><a href="/api-shield/management-and-monitoring/endpoint-labels/">Increased body response size detected on API endpoints</a></td>
<td>Investigate changes, abuse, or successful attacks that may have led to this increase in response body size.</td>
</tr>
<tr>
<td><a href="/api-shield/management-and-monitoring/endpoint-labels/">Increased errors detected on API endpoints</a></td>
<td>Investigate changes, abuse, or successful attacks that may have led to this increase in errors.</td>
</tr>
<tr>
<td><a href="/api-shield/management-and-monitoring/endpoint-labels/">Increased latency detected on API endpoints</a></td>
<td>Investigate changes, abuse, or successful attacks that may have led to this increase in response latency.</td>
</tr>
<tr>
<td><a href="/waf/managed-rules/">Managed Rules not deployed</a></td>
<td>No managed rules deployed on a WAF protected domain. Refer to <a href="#known-limitations">Known limitations</a>.</td>
</tr>
<tr>
<td><a href="/waf/reference/legacy/old-waf-managed-rules/upgrade/">Upgrade to new Managed Rules</a></td>
<td>Upgrade to new Managed Rules system required for optimal protection.</td>
</tr>
<tr>
<td><a href="/api-shield/management-and-monitoring/endpoint-labels/#managed-labels">Mixed-authentication API endpoints detected</a></td>
<td>Not all of the successful requests against API endpoints carried session identifiers.</td>
</tr>
<tr>
<td><a href="/api-shield/security/api-discovery/">New API endpoints detected</a></td>
<td>API Discovery detects new API endpoints in your zone's traffic.</td>
</tr>
<tr>
<td><a href="/cloudflare-one/integrations/cloud-and-saas/">New CASB integrations found</a></td>
<td>New CASB integrations have been found.</td>
</tr>
<tr>
<td><a href="/cloudflare-one/access-controls/policies/">Overprovisioned Access Policies</a></td>
<td>We detect an Access policy to allow everyone access to your application.</td>
</tr>
<tr>
<td><a href="/client-side-security/get-started/">Client-side security not enabled</a></td>
<td>Client-side security (formerly known as Page Shield) helps meet PCI DSS v4.0 compliance regarding requirement 6.4.3.</td>
</tr>
<tr>
<td><a href="/dns/manage-dns-records/reference/dns-record-types/#spf">SPF Record Errors</a></td>
<td>We detect an incorrect or missing <code>SPF</code> record.</td>
</tr>
<tr>
<td><a href="/api-shield/management-and-monitoring/#sensitive-data-detection">Sensitive data in API response</a></td>
<td>Sensitive data in API responses detected.</td>
</tr>
<tr>
<td><a href="/bots/additional-configurations/javascript-detections/">Turn on JavaScript Detection</a></td>
<td>One or more of your Bot Management enabled zones does not have JavaScript Detection enabled, which is a critical part of our bot detection suite.</td>
</tr>
<tr>
<td><a href="/cloudflare-one/">Unassigned Access seats</a></td>
<td>We detect a Zero Trust subscription that is not configured yet.</td>
</tr>
<tr>
<td><a href="/api-shield/management-and-monitoring/endpoint-labels/#managed-labels">Unauthenticated API endpoints detected</a></td>
<td>None of the successful requests against API endpoints carried session identifiers.</td>
</tr>
<tr>
<td><a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/#4-connect-your-origin-to-cloudflare">Unprotected Cloudflare Tunnels</a></td>
<td>We detect an application that is served by a Cloudflare Tunnel but not protected by a corresponding Access policy.</td>
</tr>
<tr>
<td><a href="/dns/manage-dns-records/reference/dns-record-types/#a-and-aaaa">Unproxied <code>A</code> Records</a></td>
<td>This DNS record is not proxied by Cloudflare. Cloudflare can not protect this origin because it is exposed to the public Internet.</td>
</tr>
<tr>
<td><a href="/dns/manage-dns-records/reference/dns-record-types/#a-and-aaaa">Unproxied <code>AAAA</code> Records</a></td>
<td>This DNS record is not proxied by Cloudflare. Cloudflare can not protect this origin because it is exposed to the public Internet.</td>
</tr>
<tr>
<td><a href="/dns/proxy-status/#dns-only-records">Unproxied <code>CNAME</code> Records</a></td>
<td>This DNS record is not proxied by Cloudflare. Cloudflare can not protect this origin because it is exposed to the public Internet.</td>
</tr>
<tr>
<td><a href="/fundamentals/user-profiles/2fa/">Users without MFA</a></td>
<td>We detect that a Cloudflare administrative user has not enabled multifactor authentication.</td>
</tr>
<tr>
<td><a href="/waf/managed-rules/">Zones without WAF Managed Rules</a></td>
<td>We detect that this domain does not have the WAF's Managed Rules enabled. You are at risk from zero-day and other common vulnerabilities.</td>
</tr>
<tr>
<td><a href="/turnstile/">No Turnstile enabled</a></td>
<td>We detect that there is no Turnstile widget configured on the account.</td>
</tr>
</tbody>
</table>
<h2 id="known-limitations">Known limitations</h2>
<p>Security Insights scans run periodically and use heuristics to detect potential issues. In some cases, an insight may not accurately reflect your current configuration:</p>
<ul>
<li>
<p><strong><em>Managed Rules not deployed</em> on zones with account-level managed rules</strong>: If you deploy managed rules at the account level rather than the zone level, Security Center may not detect them and may report that managed rules are not deployed. If your account-level configuration is correct, you can <a href="/security/security-insights/review-insights/#archive-insights">archive the insight</a> to dismiss it.</p>
</li>
<li>
<p><strong>Vulnerability insights for rules in log mode</strong>: If you configure a managed rule with a <em>Log</em> action (for example, to monitor traffic before enforcing), Security Center may still generate a vulnerability insight because the rule is not actively blocking traffic. This is expected behavior. You can archive the insight if you are intentionally using log mode.</p>
</li>
</ul>
<p>To remove a resolved or inaccurate insight from your dashboard, <a href="/security/security-insights/review-insights/#archive-insights">archive the insight</a> or wait for the next automatic scan.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="accounts-with-more-than-10-000-zones">Accounts with more than 10,000 zones</h3>
@markup("md", "content/.markup/bodies/13844.md")
</aside>
<h2 id="more-resources">More resources</h2>
<p>For more information on available operations for Security Insights, refer to <a href="/security/security-insights/review-insights/">Review Security Insights</a>.</p>
