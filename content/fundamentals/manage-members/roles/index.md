<p>Whenever you <a href="/fundamentals/manage-members/manage/">add a new member</a> to your account, you can assign policies to those users and make use of the available roles. Roles can only ever be assigned to their given scope and multiple roles can be assigned to a given policy.</p>
<h2 id="account-scoped-roles">Account-scoped roles</h2>
<p>Account-scoped roles apply across an entire Cloudflare account, and through all domains in that account.</p>
<table>
<thead>
<tr>
<th>Role</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Administrator</td>
<td>Can access the full account and edit subscriptions. Cannot manage members nor billing profile.</td>
</tr>
<tr>
<td>Super Administrator - All Privileges</td>
<td>Can edit any Cloudflare setting, make purchases, update billing, manage members, and create account-owned API tokens. Super Administrators can revoke the access of other Super Administrators.</td>
</tr>
<tr>
<td>Administrator Read Only</td>
<td>Can access the full account in read-only mode.</td>
</tr>
<tr>
<td>Analytics</td>
<td>Can read Analytics.</td>
</tr>
<tr>
<td>API Gateway</td>
<td>Grants full access to <a href="/api-shield/">API Gateway (including API Shield)</a> for all domains in an account.</td>
</tr>
<tr>
<td>API Gateway Read</td>
<td>Grants read access to <a href="/api-shield/">API Gateway (including API Shield)</a> for all domains in an account.</td>
</tr>
<tr>
<td>Application Security Reports Read</td>
<td>Can read Application Security Reports.</td>
</tr>
<tr>
<td>Audit Logs Viewer</td>
<td>Can view <a href="/fundamentals/account/account-security/review-audit-logs/">Audit Logs</a>.</td>
</tr>
<tr>
<td>Bot Management (Account-Wide)</td>
<td>Can edit <a href="/bots/plans/bm-subscription/">Bot Management</a> (including <a href="/bots/get-started/super-bot-fight-mode/">Super Bot Fight Mode</a>) configurations for all domains in account.</td>
</tr>
<tr>
<td>Billing</td>
<td>Can edit the account's <a href="/billing/get-started/create-billing-profile/">billing profile</a> and subscriptions</td>
</tr>
<tr>
<td>Cache Purge</td>
<td>Can purge the edge cache and allows the reading of zone settings.</td>
</tr>
<tr>
<td>Cloudflare Access</td>
<td>Can edit <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a>.</td>
</tr>
<tr>
<td>Cloudflare CASB</td>
<td>Can edit <a href="/cloudflare-one/cloud-and-saas-findings/">Cloudflare CASB</a>.</td>
</tr>
<tr>
<td>Cloudflare CASB Read</td>
<td>Can read <a href="/cloudflare-one/cloud-and-saas-findings/">Cloudflare CASB</a>.</td>
</tr>
<tr>
<td>Cloudchamber Admin</td>
<td>Can manage Cloudchamber deployments.</td>
</tr>
<tr>
<td>Cloudchamber Admin Read Only</td>
<td>Can manage Cloudchamber deployments in read-only mode.</td>
</tr>
<tr>
<td>Cloudflare DEX</td>
<td>Can edit <a href="/cloudflare-one/insights/dex/">Cloudflare DEX</a>.</td>
</tr>
<tr>
<td>Cloudflare Gateway</td>
<td>Can edit <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> and read <a href="/cloudflare-one/integrations/identity-providers/">Access</a>.</td>
</tr>
<tr>
<td>Cloudflare Images</td>
<td>Can access <a href="/images/">Cloudflare Images</a> data.</td>
</tr>
<tr>
<td>Cloudflare R2 Admin</td>
<td>Can edit Cloudflare <a href="/r2/">R2</a> buckets, objects, and associated configurations.</td>
</tr>
<tr>
<td>Cloudflare R2 Read</td>
<td>Can read Cloudflare <a href="/r2/">R2</a> buckets, objects, and associated configurations.</td>
</tr>
<tr>
<td>Cloudflare Stream</td>
<td>Can edit <a href="/stream/">Cloudflare Stream</a> media.</td>
</tr>
<tr>
<td>Cloudflare Zero Trust</td>
<td>Can edit <a href="/cloudflare-one/">Cloudflare Zero Trust</a>. Grants administrator access to all Zero Trust products including Access, Gateway, the Cloudflare One Client, Tunnel, Browser Isolation, CASB, DLP, DEX, and Email security.</td>
</tr>
<tr>
<td>Cloudflare Zero Trust Secure DNS Locations Write</td>
<td>Can view <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/#secure-dns-locations">Gateway DNS locations</a> and create and edit <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/#secure-dns-locations">secure DNS locations</a>.</td>
</tr>
<tr>
<td>Cloudflare Zero Trust PII</td>
<td>Can access <a href="/cloudflare-one/">Cloudflare Zero Trust</a> PII.</td>
</tr>
<tr>
<td>Cloudflare Zero Trust Read Only</td>
<td>Can access <a href="/cloudflare-one/">Cloudflare Zero Trust</a> read only mode.</td>
</tr>
<tr>
<td>Cloudflare Zero Trust Reporting</td>
<td>Can access <a href="/cloudflare-one/">Cloudflare Zero Trust</a> reporting data.</td>
</tr>
<tr>
<td>Connectivity Directory Admin</td>
<td>Can view, edit, create, and delete <a href="/workers-vpc/">Workers VPC Services</a> and bind to <a href="/workers-vpc/configuration/tunnel/">Cloudflare Tunnel</a>.</td>
</tr>
<tr>
<td>Connectivity Directory Bind</td>
<td>Can read, list, and bind to <a href="/workers-vpc/">Workers VPC Services</a>, as well as read and list <a href="/workers-vpc/configuration/tunnel/">Cloudflare Tunnels</a>.</td>
</tr>
<tr>
<td>Connectivity Directory Read</td>
<td>Can view <a href="/workers-vpc/">Workers VPC Services</a> and <a href="/workers-vpc/configuration/tunnel/">Cloudflare Tunnels</a>.</td>
</tr>
<tr>
<td>DNS</td>
<td>Can edit <a href="/dns/manage-dns-records/">DNS records</a>.</td>
</tr>
<tr>
<td>Email Configuration Admin</td>
<td>Grants administrator access to Email security. Cannot take actions on emails, or read emails.</td>
</tr>
<tr>
<td>Email Integration Admin</td>
<td>Grants read and write access to integrations only.</td>
</tr>
<tr>
<td>Email Security Analyst</td>
<td>Grants analyst access. Can take action on emails and read emails.</td>
</tr>
<tr>
<td>Email Security Read only</td>
<td>Grants read only access to all of Email security.</td>
</tr>
<tr>
<td>Email Security Reporting</td>
<td>Grants read access to Email security metrics.</td>
</tr>
<tr>
<td>Email Security Policy Admin</td>
<td>Grants read access to all settings, and write access to <a href="/cloudflare-one/email-security/settings/detection-settings/allow-policies/">allow policies</a>, <a href="/cloudflare-one/email-security/settings/detection-settings/trusted-domains/">trusted domains</a>, and <a href="/cloudflare-one/email-security/settings/detection-settings/blocked-senders/">blocked senders</a></td>
</tr>
<tr>
<td>Firewall</td>
<td>Can edit <a href="/waf/">WAF</a>, <a href="/waf/tools/ip-access-rules/">IP Access rules</a>, <a href="/waf/tools/zone-lockdown/">Zone Lockdown</a> settings, <a href="/cache/how-to/cache-rules/">Cache Rules</a>, and <a href="/cache/how-to/cache-response-rules/">Cache Response Rules</a>.</td>
</tr>
<tr>
<td>HTTP Applications</td>
<td>Grants full access to HTTP Applications.</td>
</tr>
<tr>
<td>HTTP Applications Read</td>
<td>Grants read-only access to HTTP Applications.</td>
</tr>
<tr>
<td>Load Balancer</td>
<td>Can edit <a href="/load-balancing/">Load Balancers</a>, Pools, Origins, and Health Checks.</td>
</tr>
<tr>
<td>Load Balancing Account Read</td>
<td>Can read <a href="/load-balancing/">Load Balancing</a> resources such as Load Balancers, Monitors, Monitor Groups, Pools, and Health Checks.</td>
</tr>
<tr>
<td>Log Share</td>
<td>Can edit <a href="/logs/">Log Share</a> configuration.</td>
</tr>
<tr>
<td>Log Share Reader</td>
<td>Can read Enterprise <a href="/logs/">Log Share</a>.</td>
</tr>
<tr>
<td>Magic Network Monitoring</td>
<td>Can view and edit <a href="/network-flow/">Network Flow configuration</a>.</td>
</tr>
<tr>
<td>Magic Network Monitoring Admin</td>
<td>Can view, edit, create, and delete <a href="/network-flow/">Network Flow configuration</a>.</td>
</tr>
<tr>
<td>Magic Network Monitoring Read-Only</td>
<td>Can view <a href="/network-flow/">Network Flow configuration</a>.</td>
</tr>
<tr>
<td>Network Services Write (Magic)</td>
<td>Grants write access to network configurations for Magic services. Magic Tunnel health checks require the Analytics role for non-admin users.</td>
</tr>
<tr>
<td>Network Services Read (Magic)</td>
<td>Grants read access to network configurations for Magic services. Magic Tunnel health checks require the Analytics role for non-admin users.</td>
</tr>
<tr>
<td>Minimal Account Access</td>
<td>Can view account, and nothing else.</td>
</tr>
<tr>
<td>Page Shield</td>
<td>Grants write access to <a href="/client-side-security/">client-side security</a> (formerly Page Shield) across the whole account.</td>
</tr>
<tr>
<td>Page Shield Read</td>
<td>Grants read access to <a href="/client-side-security/">client-side security</a> (formerly Page Shield) across the whole account.</td>
</tr>
<tr>
<td>Realtime</td>
<td>Grants access to Realtime configuration excluding sensitive data.</td>
</tr>
<tr>
<td>Realtime Admin</td>
<td>Grants administrator access to Realtime configuration.</td>
</tr>
<tr>
<td>Hyperdrive Read only</td>
<td>Grants read access to <a href="/hyperdrive/">Hyperdrive</a> database configuration.</td>
</tr>
<tr>
<td>Hyperdrive Admin</td>
<td>Grants write access to <a href="/hyperdrive/">Hyperdrive</a> database configuration.</td>
</tr>
<tr>
<td>SSL/TLS, Caching, Performance, Page Rules, and Customization</td>
<td>Can edit most Cloudflare settings except for <a href="/dns/">DNS</a> and <a href="/waf/">Firewall</a>.</td>
</tr>
<tr>
<td>Secrets Store Admin</td>
<td>Can create, edit, duplicate, delete, and view secrets metadata. Can also <a href="/secrets-store/integrations/workers/">add a Secrets Store binding to a Worker</a>.</td>
</tr>
<tr>
<td>Secrets Store Deployer</td>
<td>Can view secrets metadata but cannot create, edit, duplicate, nor delete secrets. Can also <a href="/secrets-store/integrations/workers/">add a Secrets Store binding to a Worker</a>.</td>
</tr>
<tr>
<td>Secrets Store Reporter</td>
<td>Can view secrets metadata. Cannot perform any actions (create, edit, duplicate, delete secrets), nor add a Secrets Store binding to a Worker.</td>
</tr>
<tr>
<td>Brand Protection</td>
<td>Can access the Brand Protection feature on the API and Cloudflare dashboard. Brand Protection role also gives you access to the Investigate platform.</td>
</tr>
<tr>
<td>Cloudforce One Admin</td>
<td>Grants write access to <a href="/security-center/cloudforce-one/">Cloudforce One</a>.</td>
</tr>
<tr>
<td>Cloudforce One Read</td>
<td>Grants read access to <a href="/security-center/cloudforce-one/">Cloudforce One</a>, and cannot create and/or edit RFIs or PIRs.</td>
</tr>
<tr>
<td>Trust and Safety</td>
<td>Can access trust and safety related services.</td>
</tr>
<tr>
<td>Turnstile</td>
<td>Grants full access to <a href="/turnstile/">Turnstile</a>.</td>
</tr>
<tr>
<td>Turnstile Read</td>
<td>Grants read access to <a href="/turnstile/">Turnstile</a>.</td>
</tr>
<tr>
<td>Vectorize Admin</td>
<td>Can edit <a href="/vectorize/">Vectorize</a> configurations.</td>
</tr>
<tr>
<td>Vectorize Read only</td>
<td>Can read <a href="/vectorize/">Vectorize</a> configurations.</td>
</tr>
<tr>
<td>Waiting Room Admin</td>
<td>Can edit <a href="/waiting-room/">Waiting Room</a> configuration.</td>
</tr>
<tr>
<td>Waiting Room Read</td>
<td>Can read <a href="/waiting-room/">Waiting Room</a> configuration.</td>
</tr>
<tr>
<td>Workers Editor</td>
<td>Can use the <a href="/workers/playground/">Workers Playground</a>.</td>
</tr>
<tr>
<td>Workers Platform Admin</td>
<td>Grants edit and read access to all products typically used as part of Cloudflare's Developer Platform, including <a href="/workers/">Workers</a>, <a href="/pages/">Pages</a>, <a href="/durable-objects/">Durable Objects</a>, <a href="/kv/">KV</a>, <a href="/r2/">R2</a>, Zones, <a href="/analytics/account-and-zone-analytics/zone-analytics/">Zone Analytics</a> and <a href="/rules/">Page Rules</a>. Cloudflare may add additional read-only permissions to this role as new products are introduced.</td>
</tr>
<tr>
<td>Workers Platform (Read-only)</td>
<td>Grants read-only access to all products typically used as part of Cloudflare's Developer Platform, including <a href="/workers/">Workers</a>, <a href="/pages/">Pages</a>, <a href="/durable-objects/">Durable Objects</a>, <a href="/kv/">KV</a>, <a href="/r2/">R2</a>, Zones, <a href="/analytics/account-and-zone-analytics/zone-analytics/">Zone Analytics</a> and <a href="/rules/">Page Rules</a>. Cloudflare may add additional read-only permissions to this role as new products are introduced.</td>
</tr>
<tr>
<td>Connectivity Directory Read</td>
<td>Can view <a href="/workers-vpc/">Workers VPC Services</a> and <a href="/workers-vpc/configuration/tunnel/">Cloudflare Tunnels</a>.</td>
</tr>
<tr>
<td>Connectivity Directory Bind</td>
<td>Can read, list, and bind to <a href="/workers-vpc/">Workers VPC Services</a>, as well as read and list <a href="/workers-vpc/configuration/tunnel/">Cloudflare Tunnels</a>.</td>
</tr>
<tr>
<td>Connectivity Directory Admin</td>
<td>Can view, edit, create, and delete <a href="/workers-vpc/">Workers VPC Services</a>, including the ability to create VPC Services that bind to <a href="/workers-vpc/configuration/tunnel/">Cloudflare Tunnel</a>.</td>
</tr>
<tr>
<td>Zaraz Admin</td>
<td>Can edit and publish <a href="/zaraz/">Zaraz</a> configuration.</td>
</tr>
<tr>
<td>Zaraz Edit</td>
<td>Can edit <a href="/zaraz/">Zaraz</a> configuration.</td>
</tr>
<tr>
<td>Zaraz Read only</td>
<td>Can read <a href="/zaraz/">Zaraz</a> configuration.</td>
</tr>
<tr>
<td>Zone Versioning (Account-Wide)</td>
<td>Can view and edit <a href="/version-management/">Zone Versioning</a> for all domains in account.</td>
</tr>
<tr>
<td>Zone Versioning Read (Account-Wide)</td>
<td>Can view <a href="/version-management/">Zone Versioning</a> for all domains in account.</td>
</tr>
</tbody>
</table>
<h2 id="domain-scoped-roles">Domain-scoped roles</h2>
<p>Domain-scoped roles apply for a given domain within an account.</p>
<table>
<thead>
<tr>
<th>Role</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>AI Crawl Control Read Only</td>
<td>Can read <a href="/ai-crawl-control/">AI Crawl Control</a> and metrics.</td>
</tr>
<tr>
<td>Bot Management</td>
<td>Can edit <a href="/bots/plans/bm-subscription/">Bot Management</a> (including <a href="/bots/get-started/super-bot-fight-mode/">Super Bot Fight Mode</a>) configurations.</td>
</tr>
<tr>
<td>Cache Domain Purge</td>
<td>Grants access to <a href="/cache/how-to/purge-cache/">purge the edge cache</a> for a specific domain and allows the reading of zone settings.</td>
</tr>
<tr>
<td>Domain Administrator</td>
<td>Grants full access to domains in an account (including <a href="/data-localization/regional-services/">Regional Services</a> configurations), and read-only access to account-wide <a href="/waf/account/managed-rulesets/deploy-dashboard/">Firewall</a>, <a href="/cloudflare-one/access-controls/policies/">Access</a>, and <a href="/workers/">Worker</a> resources.</td>
</tr>
<tr>
<td>Domain Administrator Read Only</td>
<td>Grants read-only access to domains in an account, as well as account-wide <a href="/waf/account/managed-rulesets/deploy-dashboard/">Firewall</a>, <a href="/cloudflare-one/access-controls/policies/">Access</a>, and <a href="/workers/">Worker</a> resources. This role does not currently include read access to <a href="/data-localization/regional-services/">Regional Services</a> configurations.</td>
</tr>
<tr>
<td>Domain API Gateway</td>
<td>Grants full access to API Gateway (including <a href="/api-shield/">API Shield</a>).</td>
</tr>
<tr>
<td>Domain API Gateway Read</td>
<td>Grants read access to API Gateway (including <a href="/api-shield/">API Shield</a>).</td>
</tr>
<tr>
<td>Domain DNS</td>
<td>Grants access to edit <a href="/dns/">DNS settings</a> for domains in an account.</td>
</tr>
<tr>
<td>Domain Page Shield</td>
<td>Grants write access to <a href="/client-side-security/">client-side security</a> for domains in an account.</td>
</tr>
<tr>
<td>Domain Page Shield Read</td>
<td>Grants read access to <a href="/client-side-security/">client-side security</a> for domains in an account.</td>
</tr>
<tr>
<td>Domain Waiting Room Admin</td>
<td>Can edit <a href="/waiting-room/">waiting rooms</a> configuration.</td>
</tr>
<tr>
<td>Domain Waiting Room Read</td>
<td>Can read <a href="/waiting-room/">waiting rooms</a> configuration.</td>
</tr>
<tr>
<td>Zone Versioning</td>
<td>Grants full access to <a href="/version-management/">Zone Versioning</a>.</td>
</tr>
<tr>
<td>Zone Versioning Read</td>
<td>Grants read-only access to <a href="/version-management/">Zone Versioning</a>.</td>
</tr>
</tbody>
</table>
<h2 id="resource-scoped-roles">Resource-scoped roles</h2>
<p>Resource-scoped roles apply for a specific resource within an account.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8862.md")
</aside>
<table>
<thead>
<tr>
<th>Role</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Access App Admin</td>
<td>Can edit a specific <a href="/cloudflare-one/access-controls/applications/">Access application</a> in an account.</td>
</tr>
<tr>
<td>Cloudflare Access Identity Provider Admin</td>
<td>Can edit a specific <a href="/cloudflare-one/integrations/identity-providers/">Cloudflare One identity provider (IdP)</a> in an account.</td>
</tr>
<tr>
<td>Cloudflare Access Policy Admin</td>
<td>Can edit a specific <a href="/cloudflare-one/access-controls/policies/">Access policy</a> in an account.</td>
</tr>
<tr>
<td>Cloudflare Access Service Token Admin</td>
<td>Can edit a specific <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Access service token</a> in an account.</td>
</tr>
<tr>
<td>Access for Infrastructure Target Admin</td>
<td>Can edit a specific <a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Access for Infrastructure target</a> in an account.</td>
</tr>
<tr>
<td>Individual Cloudflare Tunnel instances</td>
<td>Scopes permissions to a specific <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> instance. Refer to <a href="/cloudflare-one/networks/connectors/granular-permissions/">Granular permissions for Cloudflare Tunnel</a> for details.</td>
</tr>
<tr>
<td>Individual Cloudflare Mesh nodes</td>
<td>Scopes permissions to a specific <a href="/mesh/">Cloudflare Mesh</a> node. Refer to <a href="/cloudflare-one/networks/connectors/granular-permissions/">Granular permissions for Cloudflare Tunnel and Cloudflare Mesh</a> for details.</td>
</tr>
</tbody>
</table>
