---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/api/reference/deprecations/
  description: Track Cloudflare API deprecations, removal timelines, and replacement endpoints.
  full_title: API deprecations · Cloudflare Fundamentals docs
  head_html: <title>API deprecations · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Track Cloudflare API deprecations, removal timelines, and replacement endpoints."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/api/reference/deprecations/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/api/reference/deprecations/index.md"><link rel="alternate" type="application/rss+xml" href="https://developers.cloudflare.com/fundamentals/api/reference/deprecations/index.xml"><meta property="og:title" content="API deprecations · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Track Cloudflare API deprecations, removal timelines, and replacement endpoints."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/api/reference/deprecations/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Changelog"><meta name="algolia_content_type" content="Changelog"><meta name="pcx_additional_products" content="Cloudflare Fundamentals,API documentation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/fundamentals/api/reference/deprecations/#page","headline":"API deprecations \u00b7 Cloudflare Fundamentals docs","description":"Track Cloudflare API deprecations, removal timelines, and replacement endpoints.","url":"https://developers.cloudflare.com/fundamentals/api/reference/deprecations/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/api/reference/deprecations/
  schema: 1
---
<p>Cloudflare occasionally makes updates to our APIs that result in behavior changes or deprecations. When this happens, we will communicate when the API will no longer be available and whether there will be a replacement.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8976.md")
</aside>
<h2 id="2026-07-27">2026-07-27</h2><strong>Zone Settings Batch API</strong><p>Deprecation date: April 23, 2025</p>
<p>End of life date: March 31, 2027</p>
<p><strong>Update:</strong> This deprecation's end of life date has been extended to March 31, 2027 (previously September 15, 2026).</p>
<p>The Zone Settings Batch API endpoints, which read and edit multiple zone settings in a single request, are deprecated and will reach their end of life on March 31, 2027. Use the per-setting endpoints to read and edit individual zone settings instead.</p>
<p>Deprecated APIs:</p>
<ul>
<li><code>GET /zones/{zone_id}/settings</code></li>
<li><code>PATCH /zones/{zone_id}/settings</code></li>
</ul>
<p>Replacements:</p>
<ul>
<li><a href="/api/resources/zones/subresources/settings/methods/get/">Get zone setting</a> — <code>GET /zones/{zone_id}/settings/{setting_id}</code></li>
<li><a href="/api/resources/zones/subresources/settings/methods/edit/">Edit zone setting</a> — <code>PATCH /zones/{zone_id}/settings/{setting_id}</code></li>
</ul>
<p>Integrations that read or edit multiple settings in a single call must migrate to per-setting requests before March 31, 2027 to ensure uninterrupted service. After this date, the batch endpoints will no longer be available.</p><h2 id="2026-07-27-1">2026-07-27</h2><strong>Foundation DNS boolean setting</strong><p>Deprecation date: July 27, 2026</p>
<p>End of life date: November 23, 2026</p>
<p>The <code>foundation_dns</code> boolean is deprecated in the <a href="/api/resources/dns/subresources/settings/">DNS settings endpoints</a> for zone settings and account defaults. Use <code>nameservers.type: &quot;cloudflare.advanced&quot;</code> to configure Advanced Nameservers instead.</p>
<p>Affected endpoints:</p>
<ul>
<li><a href="/api/resources/dns/subresources/settings/subresources/zone/"><code>/zones/{zone_id}/dns_settings</code></a></li>
<li><a href="/api/resources/dns/subresources/settings/subresources/account/"><code>/accounts/{account_id}/dns_settings</code></a></li>
</ul>
<p>Beginning October 26, 2026, the DNS settings API will gradually represent Advanced Nameservers with <code>nameservers.type: &quot;cloudflare.advanced&quot;</code>. This rollout is expected to take seven days. Before the rollout reaches an account, the API will continue to return <code>nameservers.type: &quot;cloudflare.standard&quot;</code> for Advanced Nameservers. The API will accept <code>nameservers.type: &quot;cloudflare.advanced&quot;</code> in <code>PATCH</code> requests for entitled accounts throughout the rollout.</p>
<p>The <code>foundation_dns</code> boolean remains available as a compatibility alias during this transition. You can continue to read and write it. If a <code>PATCH</code> request includes both values, they must match. The API will reject conflicting values.</p>
<p>Beginning November 23, 2026, the DNS settings API will no longer return or accept <code>foundation_dns</code>. This rollout is expected to take seven days. <code>PATCH</code> requests that include <code>foundation_dns</code> will be rejected. Update clients that treat <code>nameservers.type</code> as a closed enum to recognize the <code>&quot;cloudflare.advanced&quot;</code> value, and update clients that read or write <code>foundation_dns</code> before the end-of-life date. This API change does not change your Foundation DNS subscription or whether Advanced Nameservers are enabled on your zones. It does not require a zone migration.</p><h2 id="2026-07-22">2026-07-22</h2><strong>Account name 65-character limit</strong><p>Enforcement date: September 27, 2026</p>
<p>Account names will be limited to a maximum of 65 characters across all account creation and update APIs. This limit applies to all accounts, including organization accounts. Currently, the account update API (<code>PUT /accounts/{account_id}</code>) already enforces this limit, while the account create API (<code>POST /accounts</code>) silently truncates names up to 120 bytes. This mismatch can result in accounts that are created successfully but cannot later be renamed. After September 27, 2026, the create API will reject names longer than 65 characters with an HTTP <code>400</code> error.</p>
<p>Affected APIs:</p>
<ul>
<li><code>POST /accounts</code> — Create account</li>
<li><code>PUT /accounts/{account_id}</code> — Update account (already enforced)</li>
</ul>
<p>After the enforcement date, integrations that create accounts with names longer than 65 characters must truncate or shorten the name before sending the request to ensure uninterrupted service.</p><h2 id="2026-07-21">2026-07-21</h2><strong>Account Roles API</strong><p>Deprecation date: July 21, 2026</p>
<p>The <a href="/api/resources/accounts/subresources/roles/">Account Roles API</a> only returns account-level roles today, and is deprecated in favor of the <a href="/api/resources/iam/subresources/permission_groups/">Permission Groups API</a>. The Permission Groups API is the supported way to enumerate account, zone, and resource-level roles that can be granted to account members.</p>
<p>Deprecated APIs:</p>
<ul>
<li><code>GET /accounts/{account_id}/roles</code> — List roles</li>
<li><code>GET /accounts/{account_id}/roles/{role_id}</code> — Role details</li>
</ul>
<p>Replacements:</p>
<ul>
<li><code>GET /accounts/{account_id}/iam/permission_groups</code> — List account permission groups</li>
<li><code>GET /accounts/{account_id}/iam/permission_groups/{permission_group_id}</code> — Permission group details</li>
</ul>
<p>The response schema differs from the legacy Roles response:</p>
<ul>
<li>The legacy <code>Role</code> response includes a top-level <code>description</code> and a <code>permissions</code> object keyed by resource type with edit/read flags.</li>
<li>The <code>PermissionGroup</code> response replaces those with a <code>meta</code> object containing <code>label</code> and <code>scopes</code>. Individual permissions are not returned as part of the permission group.</li>
</ul>
<p>Additional notes:</p>
<ul>
<li>Integrations migrating to the Permission Groups API must obtain Permission Group IDs from that API and use them in the Account Members API policies request shape. Integrations that persist legacy Role IDs will need to remap their assignments.</li>
<li>Both endpoints use the standard Cloudflare response envelope, so pagination and error-handling do not change.</li>
<li>The new API supports the <a href="/fundamentals/api/get-started/create-token/">API Token</a> authorization scheme. The legacy Email + API Key authorization scheme is provided for backwards compatibility.</li>
<li>The affected terraform resource is the <code>cloudflare_account_role</code> data source. You will need to migrate to the <code>cloudflare_account_permission_group</code> data source.</li>
</ul><h2 id="2026-07-15">2026-07-15</h2><strong>Workers KV: Legacy Namespace Routes</strong><p>Deprecation date: July 15, 2026</p>
<p>End of life date: October 15, 2026</p>
<p>The legacy Workers KV API routes under <code>/accounts/{account_id}/workers/namespaces/*</code> are deprecated in favor of the <a href="/api/resources/kv/">Workers KV API</a> routes under <code>/accounts/{account_id}/storage/kv/namespaces/*</code>.</p>
<p>The legacy and replacement routes are interchangeable. They accept the same request parameters and return the same response payloads. To migrate, update the URL path from <code>/workers/namespaces/</code> to <code>/storage/kv/namespaces/</code>.</p>
<p>Deprecated APIs:</p>
<ul>
<li><code>GET</code> and <code>POST /accounts/{account_id}/workers/namespaces</code> (list and create namespaces)</li>
<li><code>GET</code>, <code>PUT</code>, and <code>DELETE /accounts/{account_id}/workers/namespaces/{namespace_id}</code> (get, rename, and remove a namespace)</li>
<li><code>GET /accounts/{account_id}/workers/namespaces/{namespace_id}/keys</code> (list keys)</li>
<li><code>GET /accounts/{account_id}/workers/namespaces/{namespace_id}/metadata/{key_name}</code> (read key metadata)</li>
<li><code>GET</code>, <code>PUT</code>, and <code>DELETE /accounts/{account_id}/workers/namespaces/{namespace_id}/values/{key_name}</code> (read, write, and delete key-value pairs)</li>
</ul>
<p>Replacements:</p>
<p>Update the URL path from <code>/workers/namespaces/</code> to <code>/storage/kv/namespaces/</code> in each endpoint.</p>
<ul>
<li><code>GET</code> and <code>POST /accounts/{account_id}/storage/kv/namespaces</code> (list and create namespaces)</li>
<li><code>GET</code>, <code>PUT</code>, and <code>DELETE /accounts/{account_id}/storage/kv/namespaces/{namespace_id}</code> (get, rename, and remove a namespace)</li>
<li><code>GET /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/keys</code> (list keys)</li>
<li><code>GET /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/metadata/{key_name}</code> (read key metadata)</li>
<li><code>GET</code>, <code>PUT</code>, and <code>DELETE /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}</code> (read, write, and delete key-value pairs)</li>
</ul>
<p>After October 15, 2026, requests to the legacy <code>/accounts/{account_id}/workers/namespaces/*</code> routes will no longer be supported. Update integrations to use the documented Workers KV API endpoints before that date to ensure uninterrupted service.</p><h2 id="2026-07-09">2026-07-09</h2><strong>Zero Trust Networks Route Endpoints and Cloudflare Tunnel Connections Field</strong><p>Deprecation date: July 9, 2026</p>
<p>End of life date: October 5, 2026</p>
<p>Two related changes to the <a href="/api/resources/zero_trust/subresources/networks/">Zero Trust Networks API</a> and <a href="/api/resources/zero_trust/subresources/tunnels/">Cloudflare Tunnel API</a> take effect on October 5, 2026.</p>
<p><strong>Route endpoints</strong></p>
<p>The CIDR-encoded route endpoints are deprecated in favor of the standard, <code>route_id</code>-based endpoints that already exist today.</p>
<p>Deprecated APIs:</p>
<ul>
<li><code>POST /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}</code></li>
<li><code>PATCH /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}</code></li>
<li><code>DELETE /accounts/{account_id}/teamnet/routes/network/{ip_network_encoded}</code></li>
</ul>
<p>Replacements:</p>
<ul>
<li><code>POST /accounts/{account_id}/teamnet/routes</code></li>
<li><code>PATCH /accounts/{account_id}/teamnet/routes/{route_id}</code></li>
<li><code>DELETE /accounts/{account_id}/teamnet/routes/{route_id}</code></li>
</ul>
<p><strong>Cloudflare Tunnel and Cloudflare Mesh connections</strong></p>
<p>The <code>connections</code> array is removed from list and get responses for Cloudflare Tunnel and Cloudflare Mesh nodes (the <code>cfd_tunnel</code> and <code>warp_connector</code> API resources). Query the dedicated connections endpoint instead of reading the field off the tunnel or node object.</p>
<p>Affected APIs:</p>
<ul>
<li><code>GET /accounts/{account_id}/cfd_tunnel</code></li>
<li><code>GET /accounts/{account_id}/cfd_tunnel/{tunnel_id}</code></li>
<li><code>GET /accounts/{account_id}/warp_connector</code></li>
<li><code>GET /accounts/{account_id}/warp_connector/{tunnel_id}</code></li>
</ul>
<p>Replacements:</p>
<ul>
<li><code>GET /accounts/{account_id}/cfd_tunnel/{tunnel_id}/connections</code></li>
<li><code>GET /accounts/{account_id}/warp_connector/{tunnel_id}/connections</code></li>
</ul>
<p>For full migration guidance, including <code>curl</code> examples and <code>cloudflared</code> and Terraform notes, refer to the <a href="/changelog/2026-07-09-tunnel-routes-and-connections-api-changes/">Cloudflare Tunnel changelog</a>.</p><h2 id="2026-07-08">2026-07-08</h2><strong>AMP/SXG API and Rules</strong><p>Deprecation date: September 18, 2025</p>
<p>End of life date: June 23, 2026</p>
<p>The AMP/SXG features have reached end of life. There will be no replacement functionality. The zone settings API endpoints and sxg <a href="https://developers.cloudflare.com/rules/configuration-rules/settings/">Configuration Rule setting</a> should no longer be used.</p>
<p>Deprecated APIs:</p>
<ul>
<li><code>GET /zones/{zone_id}/amp/sxg</code></li>
<li><code>PUT /zones/{zone_id}/amp/sxg</code></li>
</ul>
<p>Deprecated Configuration Rule setting:</p>
<ul>
<li><code>sxg</code></li>
</ul>
<p>The Dashboard UI will no longer show references to AMP or the sxg setting. Users can remove the sxg parameter from their rulesets by using the <a href="https://developers.cloudflare.com/ruleset-engine/rulesets-api/update-rule/">rulesets API</a>. Terraform deprecation will follow later, and users should remove references to the <code>sxg</code> parameter from their <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/ruleset#sxg-1">terraform</a>.</p><h2 id="2026-06-29">2026-06-29</h2><strong>Legacy Registrar Domain Management API</strong><p>Deprecation date: April 10, 2026</p>
<p>End of life date: September 27, 2026</p>
<p>The legacy Registrar domain management endpoints are deprecated and will reach their end of life on September 27, 2026. These endpoints have been replaced by the new <a href="/api/resources/registrar/">Registrar API</a>, which provides domain search, availability checking, and registration capabilities.</p>
<p>Deprecated APIs:</p>
<ul>
<li><code>GET /accounts/{account_id}/registrar/domains</code> — List domains</li>
<li><code>GET /accounts/{account_id}/registrar/domains/{domain_name}</code> — Get domain</li>
<li><code>PUT /accounts/{account_id}/registrar/domains/{domain_name}</code> — Update domain</li>
</ul>
<p>Replacement: <a href="/api/resources/registrar/">Registrar API</a></p>
<ul>
<li><a href="/api/resources/registrar/methods/search/">Search for available domains</a> — <code>GET /accounts/{account_id}/registrar/domain-search</code></li>
<li><a href="/api/resources/registrar/methods/check/">Check domain availability</a> — <code>POST /accounts/{account_id}/registrar/domain-check</code></li>
<li><a href="/api/resources/registrar/subresources/registrations/methods/list/">List registrations</a> — <code>GET /accounts/{account_id}/registrar/registrations</code></li>
<li><a href="/api/resources/registrar/subresources/registrations/methods/create/">Create registration</a> — <code>POST /accounts/{account_id}/registrar/registrations</code></li>
</ul>
<p>Customers and integrations using the legacy domain management endpoints must migrate to the new Registrar API before September 27, 2026 to ensure uninterrupted service. After this date, the legacy endpoints will no longer be available.</p><h2 id="2026-05-13">2026-05-13</h2><strong>Gateway Audit SSH rules</strong><p>Deprecation date: November 3, 2025</p>
<p>End of life date: July 15, 2026</p>
<p>The Gateway Audit SSH action for <a href="/cloudflare-one/traffic-policies/network-policies/">network policies</a> is deprecated and will be fully removed on July 15, 2026. <a href="/cloudflare-one/connections/connect-networks/use-cases/ssh/ssh-infrastructure-access/">SSH with Access for Infrastructure</a> is the replacement for managing and auditing SSH access.</p>
<p>Creating new Gateway rules with <code>action: &quot;audit_ssh&quot;</code> via the dashboard was disabled in December 2024. Creating new rules via the API and Terraform was disabled on November 3, 2025. Editing existing rules via the dashboard, API, and Terraform was disabled on January 15, 2026. On July 15, 2026, all remaining Audit SSH rules will stop working.</p>
<p>Deprecated APIs:</p>
<ul>
<li><code>POST /accounts/{account_id}/gateway/rules</code> — creating rules with <code>action: &quot;audit_ssh&quot;</code> is no longer accepted</li>
<li><code>PUT /accounts/{account_id}/gateway/rules/{rule_id}</code> — editing rules with <code>action: &quot;audit_ssh&quot;</code> is no longer accepted</li>
</ul>
<p>Replacement: <a href="/cloudflare-one/connections/connect-networks/use-cases/ssh/ssh-infrastructure-access/">SSH with Access for Infrastructure</a></p><h2 id="2026-03-19">2026-03-19</h2><strong>Service Key Authentication</strong><p>Deprecation date: March 19, 2026</p>
<p>End of life date: September 30, 2026</p>
<p>Service Key authentication for the Cloudflare API is deprecated and will be removed on September 30, 2026. <a href="/fundamentals/api/get-started/create-token/">API Tokens</a> are capable of providing all functionality of Service Keys, with additional support for fine-grained permission scoping, expiration, and IP address restrictions.</p>
<p>Deprecated behavior:</p>
<ul>
<li>Authenticating API requests using the <code>X-Auth-User-Service-Key</code> header.</li>
<li>Generating new Service Keys via the Cloudflare dashboard or API. The ability to generate new Service Keys from the Dashboard will be removed soon.</li>
</ul>
<p>Replacement:</p>
<ul>
<li><a href="/fundamentals/api/get-started/create-token/">Create an API Token</a> with the appropriate permissions for your use case. API Tokens support fine-grained scoping, expiration, and revocation.</li>
</ul>
<p>Users of <code>cloudflared</code> should ensure they are running a version from November 2022 or later, which uses API Tokens instead of Service Keys. Users of <a href="https://github.com/cloudflare/origin-ca-issuer">origin-ca-issuer</a> should update to a version that supports API Token authentication.</p><h2 id="2026-01-23">2026-01-23</h2><strong>DNS Record Type Updates via API</strong><p>Deprecation date: January 23, 2026</p>
<p>End of life date: June 30, 2026</p>
<p>Changing the type of an existing DNS record via the API is deprecated and will no longer be supported after June 30, 2026.</p>
<p>Changing a DNS record's type is not a natural update operation and typically also requires changing the record's content. Updates to attributes such as name, TTL, or content are common and safe, but changing the record type introduces additional validation complexity and consistency risks.</p>
<p>To align with correct DNS semantics and reduce operational risk, Cloudflare is deprecating support for in-place DNS record type changes. This behavior already exists in the Terraform v5 provider, where record type changes result in a delete and recreate operation rather than an update.</p>
<p>Deprecated behavior:</p>
<ul>
<li>Using the <a href="/api/resources/dns/subresources/records/">DNS Records API</a> to change the type of an existing record.</li>
</ul>
<p>Replacement behavior:</p>
<ul>
<li>
<p><a href="/api/resources/dns/subresources/records/methods/delete/">Delete the existing DNS record</a> and <a href="/api/resources/dns/subresources/records/methods/create/">Create a new DNS record</a> with the desired type and content.</p>
<p><code>DELETE /zones/{zone_id}/dns_records/{dns_record_id}</code></p>
<p><code>POST /zones/{zone_id}/dns_records</code></p>
</li>
<li>
<p>Use the <a href="/api/resources/dns/subresources/records/methods/batch/">Batch DNS records</a> API to perform both operations in a single request.</p>
<p><code>POST /zones/{zone_id}/dns_records/batch</code></p>
</li>
</ul>
<p>Customers and integrations that rely on in-place record type updates must migrate to a delete-and-recreate workflow before June 30, 2026 to ensure uninterrupted service. After this date, attempts to change a record's type via update operations will no longer be supported.</p><h2 id="2025-12-09">2025-12-09</h2><strong>Authoritative DNS and DNS Firewall Legacy Analytics</strong><p>Deprecation date: December 9, 2025</p>
<p>End of life date: December 1, 2026</p>
<p>The following REST APIs are deprecated and will reach their end of life on December 1, 2026.</p>
<ul>
<li><a href="https://developers.cloudflare.com/api/resources/dns/subresources/analytics/">DNS Analytics API</a></li>
<li><a href="https://developers.cloudflare.com/api/resources/dns_firewall/subresources/analytics/">DNS Firewall Analytics API</a></li>
</ul>
<p>All existing functionality is fully supported by Cloudflare's GraphQL Analytics API, which provides improved performance, flexibility, and long-term support. Integrations using the REST API need to be migrated to the new GraphQL API before December 1, 2026 in order to ensure uninterrupted service.</p>
<p>Deprecated APIs:</p>
<ul>
<li><code>GET/zones/{zone_id}/dns_analytics/</code> (DNS Analytics API)</li>
<li><code>GET/accounts/{account_id}/dns_firewall/{dns_firewall_id}/dns_analytics/report</code> (DNS Firewall Analytics API)</li>
</ul>
<p>Replacements:</p>
<ul>
<li><a href="/dns/additional-options/analytics/#explore-with-the-api">GraphQL API for DNS Analytics</a></li>
<li><a href="/dns/dns-firewall/analytics/#graphql">GraphQL API for DNS Firewall Analytics</a></li>
</ul><h2 id="2025-11-11">2025-11-11</h2><strong>Zero Trust Devices</strong><p>End of life date: November 11, 2025</p>
<p>We are changing the definition of Devices. Devices are going to represent the real-world machines while
the relation between Users and Devices will be represented by a new concept - Registrations.</p>
<p>As a result multiple fields are moving from Devices to Registrations and we are deprecating the endpoints listed below.</p>
<p>The deprecated endpoints are not supported on accounts with <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-multiuser/">multi-user mode</a> enabled.</p>
<p>Deprecated API:</p>
<ul>
<li><code>GET /accounts/{account_id}/devices</code></li>
<li><code>GET /accounts/{account_id}/devices/{device_id}</code></li>
<li><code>GET /accounts/{account_id}/devices/{device_id}/override_codes</code></li>
<li><code>POST /accounts/{account_id}/devices/revoke</code></li>
<li><code>POST /accounts/{account_id}/devices/unrevoke</code></li>
</ul>
<p>Replacement:</p>
<ul>
<li><code>GET /accounts/{account_id}/devices/physical-devices</code></li>
<li><code>GET /accounts/{account_id}/devices/physical-devices/{device_id}</code></li>
<li><code>GET /accounts/{account_id}/devices/registrations</code></li>
<li><code>GET /accounts/{account_id}/devices/registrations/{registration_id}</code></li>
<li><code>GET /accounts/{account_id}/devices/registrations/{registration_id}/override_codes</code></li>
<li><code>POST /accounts/{account_id}/devices/registrations/revoke</code></li>
<li><code>POST /accounts/{account_id}/devices/registrations/unrevoke</code></li>
</ul><h2 id="2025-11-03">2025-11-03</h2><strong>Cloudflare Mirage</strong><p>Deprecation date: November 2025</p>
<p>End of life date: January 2026</p>
<p>Following on from the <a href="/speed/optimization/images/mirage/">deprecation of Cloudflare Mirage</a>, the following API endpoints that manage Mirage settings are now deprecated and will be sunsetted in January 2026.</p>
<p>Deprecated APIs:</p>
<ul>
<li><code>GET /zones/{zone_id}/settings/mirage</code></li>
<li><code>PATCH /zones/{zone_id}/settings/mirage</code></li>
</ul>
<p>Affected APIs:</p>
<ul>
<li><code>GET /zones/{zone_id}/pagerules/settings</code> - Mirage will be removed from available settings.</li>
<li><code>POST /zones/{zone_id}/pagerules</code> - Mirage parameter will be removed.</li>
<li><code>PATCH /zones/{zone_id}/pagerules/{rule_id}</code> - Mirage parameter will be removed.</li>
<li><code>PUT /zones/{zone_id}/pagerules/{rule_id}</code> - Mirage parameter will be removed.</li>
<li><code>GET /zones/{zone_id}/rulesets/{ruleset_id}</code> - Mirage parameter in <code>set_config</code> action will be removed.</li>
<li><code>GET /zones/{zone_id}/rulesets/{ruleset_id}/versions/{version_id}</code> - Mirage parameter in <code>set_config</code> action will be removed.</li>
<li><code>POST /zones/{zone_id}/rulesets</code> - Mirage parameter in <code>set_config</code> action will be removed.</li>
<li><code>PUT /zones/{zone_id}/rulesets/{ruleset_id}</code> - Mirage parameter in <code>set_config</code> action will be removed.</li>
<li><code>POST /zones/{zone_id}/rulesets/{ruleset_id}/rules</code> - Mirage parameter in <code>set_config</code> action will be removed.</li>
<li><code>PATCH /zones/{zone_id}/rulesets/{ruleset_id}/rules/{rule_id}</code> - Mirage parameter in <code>set_config</code> action will be removed.</li>
<li><code>GET /accounts/{account_id}/rulesets/{ruleset_id}</code> - Mirage parameter in <code>set_config</code> action will be removed.</li>
<li><code>GET /accounts/{account_id}/rulesets/{ruleset_id}/versions/{version_id}</code> - Mirage parameter in <code>set_config</code> action will be removed.</li>
<li><code>POST /accounts/{account_id}/rulesets</code> - Mirage parameter in <code>set_config</code> action will be removed.</li>
<li><code>PUT /accounts/{account_id}/rulesets/{ruleset_id}</code> - Mirage parameter in <code>set_config</code> action will be removed.</li>
<li><code>POST /accounts/{account_id}/rulesets/{ruleset_id}/rules</code> - Mirage parameter in <code>set_config</code> action will be removed.</li>
<li><code>PATCH /accounts/{account_id}/rulesets/{ruleset_id}/rules/{rule_id}</code> - Mirage parameter in <code>set_config</code> action will be removed.</li>
</ul><h2 id="2025-10-15">2025-10-15</h2><strong>Cloudflare Radar: Summary and Timeseries Groups Endpoints</strong><p>Deprecation date: October 15, 2025</p>
<p>End of life date: April 15, 2026</p>
<p>The Radar API currently has multiple summary and timeseries groups endpoints per dataset (for example, <code>/radar/http/summary/device_type</code> and <code>/radar/http/timeseries_groups/device_type</code>), which share nearly identical parameters and schema.
To simplify the API and improve maintainability, these endpoints will be replaced with parameterized endpoints using a <code>{dimension}</code> path parameter.</p>
<p>Deprecated APIs:</p>
<ul>
<li><code>GET /radar/http/summary/device_type</code></li>
<li><code>GET /radar/http/summary/bot_class</code></li>
<li><code>GET /radar/http/timeseries_groups/device_type</code></li>
<li><code>GET /radar/http/timeseries_groups/bot_class</code></li>
<li>Other similar summary and timeseries groups endpoints for the following datasets: AI Bots, AI Inference, AS112, DNS, Email Routing, Email security, HTTP, Layer 3 Attacks, Layer 7 Attacks, Leaked Credential Checks</li>
</ul>
<p>Replacements:</p>
<ul>
<li><code>GET /radar/http/summary/{dimension}</code></li>
<li><code>GET /radar/http/timeseries_groups/{dimension}</code></li>
<li>...</li>
</ul>
<p>Here, <code>{dimension}</code> is a required path parameter listing all available dimensions for the dataset.</p>
<p>For users calling the API directly (not via the Cloudflare SDK), no action is required.
For users using the SDK, we recommend updating to the new operations to ensure compatibility after the operations are removed.</p><h2 id="2025-07-01">2025-07-01</h2><strong>Cloudflare Radar: Verified Bots APIs</strong><p>Deprecation date: July 1, 2025</p>
<p>End of life date: January 1, 2026</p>
<p>The Radar Verified Bots API is now deprecated and will be replaced by the new Bots API.</p>
<p>Deprecated APIs:</p>
<ul>
<li><code>GET /radar/verified_bots/top/bots</code></li>
<li><code>GET /radar/verified_bots/top/categories</code></li>
</ul>
<p>Replacements:</p>
<ul>
<li><code>GET /radar/bots/summary/bot</code></li>
<li><code>GET /radar/bots/summary/category</code></li>
</ul><h2 id="2025-07-01-1">2025-07-01</h2><strong>Cloudflare DWeb Resolver</strong><p>Deprecation date: July 1, 2025</p>
<p>The Cloudflare DWeb Resolver experiment is ending.</p>
<p>Deprecated APIs:</p>
<ul>
<li>DoH resolver on resolver.cloudflare-eth.com</li>
</ul><h2 id="2025-06-15">2025-06-15</h2><strong>Firewall Rules API and Filters API</strong><p>Deprecation date: June 15, 2025</p>
<p>The Firewall Rules API and the Filters API are deprecated, since Firewall Rules was deprecated in favor of <a href="/waf/custom-rules/">WAF custom rules</a>. Refer to <a href="/waf/reference/legacy/firewall-rules-upgrade/">Firewall Rules upgrade</a> for more information about this change.</p>
<p>Deprecated APIs:</p>
<ul>
<li><code>GET /zones/:zone_id/firewall/rules</code></li>
<li><code>POST /zones/:zone_id/firewall/rules</code></li>
<li><code>PATCH /zones/:zone_id/firewall/rules</code></li>
<li><code>PUT /zones/:zone_id/firewall/rules</code></li>
<li><code>DELETE /zones/:zone_id/firewall/rules</code></li>
<li><code>GET /zones/:zone_id/firewall/rules/:rule_id</code></li>
<li><code>PATCH /zones/:zone_id/firewall/rules/:rule_id</code></li>
<li><code>PUT /zones/:zone_id/firewall/rules/:rule_id</code></li>
<li><code>DELETE /zones/:zone_id/firewall/rules/:rule_id</code></li>
<li><code>GET /zones/:zone_id/filters</code></li>
<li><code>POST /zones/:zone_id/filters</code></li>
<li><code>PUT /zones/:zone_id/filters</code></li>
<li><code>DELETE /zones/:zone_id/filters</code></li>
<li><code>GET /zones/:zone_id/filters/:filter_id</code></li>
<li><code>PUT /zones/:zone_id/filters/:filter_id</code></li>
<li><code>DELETE /zones/:zone_id/filters/:filter_id</code></li>
</ul>
<p>Replacement: <a href="/waf/custom-rules/">WAF custom rules</a></p><h2 id="2025-06-15-1">2025-06-15</h2><strong>WAF managed rules APIs (previous version)</strong><p>Deprecation date: June 15, 2025</p>
<p>The APIs for managing WAF managed rules (previous version) — namely for managing packages, rule groups, rules, and overrides — are deprecated in favor of using the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> for managing the new version of <a href="/waf/managed-rules/">WAF Managed Rules</a>. Refer to <a href="/waf/reference/legacy/old-waf-managed-rules/upgrade/">WAF Managed Rules upgrade</a> for more information about this change.</p>
<p>Deprecated APIs:</p>
<ul>
<li><code>GET /zones/:zone_id/firewall/waf/packages</code></li>
<li><code>GET /zones/:zone_id/firewall/waf/packages/:package_id</code></li>
<li><code>PATCH /zones/:zone_id/firewall/waf/packages/:package_id</code></li>
<li><code>GET /zones/:zone_id/firewall/waf/packages/:package_id/groups</code></li>
<li><code>GET /zones/:zone_id/firewall/waf/packages/:package_id/groups/:group_id</code></li>
<li><code>PATCH /zones/:zone_id/firewall/waf/packages/:package_id/groups/:group_id</code></li>
<li><code>GET /zones/:zone_id/firewall/waf/packages/:package_id/rules</code></li>
<li><code>GET /zones/:zone_id/firewall/waf/packages/:package_id/rules/:rule_id</code></li>
<li><code>PATCH /zones/:zone_id/firewall/waf/packages/:package_id/rules/:rule_id</code></li>
<li><code>GET /zones/:zone_id/firewall/waf/overrides</code></li>
<li><code>POST /zones/:zone_id/firewall/waf/overrides</code></li>
<li><code>GET /zones/:zone_id/firewall/waf/overrides/:override_id</code></li>
<li><code>PUT /zones/:zone_id/firewall/waf/overrides/:override_id</code></li>
<li><code>DELETE /zones/:zone_id/firewall/waf/overrides/:override_id</code></li>
</ul>
<p>Replacement: <a href="/waf/managed-rules/">WAF Managed Rules</a> (new version)</p><h2 id="2025-06-15-2">2025-06-15</h2><strong>Rate Limiting API (previous version)</strong><p>Deprecation date: June 15, 2025</p>
<p>The Rate Limiting API is deprecated, in favor of using the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a> for managing the new <a href="/waf/rate-limiting-rules/">rate limiting rules</a>. Refer to <a href="/waf/reference/legacy/old-rate-limiting/upgrade/">Rate limiting (previous version) upgrade</a> for more information about this change.</p>
<p>Deprecated API:</p>
<ul>
<li><code>GET /zones/:zone_id/rate_limits</code></li>
<li><code>POST /zones/:zone_id/rate_limits</code></li>
<li><code>GET /zones/:zone_id/rate_limits/:rate_limit_id</code></li>
<li><code>PUT /zones/:zone_id/rate_limits/:rate_limit_id</code></li>
<li><code>DELETE /zones/:zone_id/rate_limits/:rate_limit_id</code></li>
</ul>
<p>Replacement: <a href="/waf/rate-limiting-rules/">Rate limiting rules</a> (new version)</p><h2 id="2025-06-08">2025-06-08</h2><strong>Zone Setting: cname_flattening</strong><p>Deprecation date: June 8, 2025</p>
<p>The Zone Settings API endpoints for managing zone-level CNAME flattening are deprecated. Instead, use the <a href="/api/resources/dns/subresources/settings/subresources/zone/methods/get/">Show DNS Settings</a> and <a href="/api/resources/dns/subresources/settings/subresources/zone/methods/edit/">Update DNS Settings</a> endpoints to manage this setting.</p>
<p>Changes via the old endpoints will be reflected in the new ones, and vice versa, so there is no need to migrate existing zones. However, future API calls must use DNS Settings instead of the Zone Settings endpoints.</p>
<p>Note that, with the deprecated zone setting, values <code>&quot;off&quot;</code> and <code>&quot;apex&quot;</code> have the same behavior. These are represented as <code>{&quot;flatten_all_cnames&quot;: false}</code> in the new API.
The zone setting <code>&quot;on&quot;</code> corresponds to <code>{&quot;flatten_all_cnames&quot;: true}</code> in the new API.</p>
<p>Affected APIs:</p>
<ul>
<li><code>GET /zones/:zone_id/settings</code></li>
<li><code>PATCH /zones/:zone_id/settings</code></li>
</ul>
<p>Deprecated APIs:</p>
<ul>
<li><code>GET /zones/:zone_id/settings/cname_flattening</code></li>
<li><code>PATCH /zones/:zone_id/settings/cname_flattening</code></li>
</ul><h2 id="2025-03-23">2025-03-23</h2><strong>Eligible Zones For Account Custom Nameservers</strong><p>Deprecation date: March 23, 2025</p>
<p>Users can now add custom nameservers that are not part of a zone managed within their account. As a result, any zone is eligible for custom nameservers, regardless of whether it is managed by Cloudflare. Given this change, an endpoint to check for eligible zones is no longer relevant and is therefore being deprecated.</p>
<p>Deprecated APIs:</p>
<ul>
<li><code>GET /accounts/:account_id/custom_ns/availability</code></li>
</ul><h2 id="2025-03-20">2025-03-20</h2><strong>Cloudflare Radar: Attack top industry and vertical endpoints</strong><p>Deprecation date: March 20, 2025</p>
<p>End of life date: September 20, 2025</p>
<p>The <code>/top/industry</code> and <code>/top/vertical</code> attack endpoints are now deprecated and will be replaced by the corresponding summary endpoints.</p>
<p>Affected APIs:</p>
<ul>
<li><code>GET /radar/attacks/layer3/top/industry</code></li>
<li><code>GET /radar/attacks/layer3/top/vertical</code></li>
<li><code>GET /radar/attacks/layer7/top/industry</code></li>
<li><code>GET /radar/attacks/layer7/top/vertical</code></li>
</ul>
<p>Replacements:</p>
<ul>
<li><code>GET /radar/attacks/layer3/summary/industry</code></li>
<li><code>GET /radar/attacks/layer3/summary/vertical</code></li>
<li><code>GET /radar/attacks/layer7/summary/industry</code></li>
<li><code>GET /radar/attacks/layer7/summary/vertical</code></li>
</ul><h2 id="2025-03-17">2025-03-17</h2><strong>Security Center: Security level and Threat Score are now automated</strong><p>Change date: March 17, 2025</p>
<p>Cloudflare now combines the IP address threat signal with threshold and botnet data, no longer requiring you to set a sensitivity level. Users will no longer be able to set Security level via the  Cloudflare dashboard. However, users can still rely on the existing API or Terraform configuration to set a Security level.</p>
<p>If you are using threat score in rule expressions, you should review those expressions to make sure the rule still triggers when appropriate. Cloudflare will audit and migrate your configuration in the future to update any references to threat score. If you are using the Rulesets API or Terraform to push your configuration, you should review your scripts and pipelines before the end of Q1 2026 to prevent issues.</p><h2 id="2025-03-14">2025-03-14</h2><strong>Account Settings: default_nameservers and use_account_custom_ns_by_default</strong><p>Deprecation date: March 14, 2025</p>
<p>The fields <code>&quot;default_nameservers&quot;</code> and <code>&quot;use_account_custom_ns_by_default&quot;</code> within the <code>&quot;settings&quot;</code> object of accounts are deprecated.
Instead, use the <a href="/api/resources/dns/subresources/settings/subresources/account/methods/get/">Show DNS Settings</a> and <a href="/api/resources/dns/subresources/settings/subresources/account/methods/edit/">Update DNS Settings</a> endpoints to manage this setting.
This setting is available in the new API as <code>.zone_defaults.nameservers.type</code>, with allowed values <code>&quot;cloudflare.standard&quot;</code>, <code>&quot;cloudflare.standard.random&quot;</code>, <code>&quot;custom.account&quot;</code> and <code>&quot;custom.tenant&quot;</code>.</p>
<p>Changes via the old endpoints will be reflected in the new ones, and vice versa, so there is no need to migrate existing zones. However, future API calls must use DNS Settings instead of the Accounts endpoints.</p>
<p>Affected APIs:</p>
<ul>
<li><code>GET /accounts</code></li>
<li><code>POST /accounts</code></li>
<li><code>GET /accounts/:account_id</code></li>
<li><code>PUT /accounts/:account_id</code></li>
</ul><h2 id="2025-03-11">2025-03-11</h2><strong>Cloudflare Radar: Layer 7 attack magnitude parameter</strong><p>Deprecation date: March 11, 2025</p>
<p>End of life date: June 11, 2025</p>
<p>The layer 7 attack <code>magnitude</code> query parameter, which allows you to define attack magnitude by total requests mitigated (<code>MITIGATED_REQUESTS</code>) or total zones attacked (<code>AFFECTED_ZONES</code>), is deprecated.
Moving forward, Cloudflare Radar will only support defining layer 7 attack magnitude based on the total number of mitigated requests.</p>
<p>Affected API:</p>
<p><code>GET /radar/attacks/layer7/top/attacks</code></p>
<p>Replacement:</p>
<p>Users should stop using the <code>magnitude</code> parameter, as the default behavior already uses <code>MITIGATED_REQUESTS</code>.</p><h2 id="2025-02-21">2025-02-21</h2><strong>DNS Records API: Changes to Filter Parameters</strong><p>Deprecation date: February 21, 2025</p>
<p>The following URL parameters for filtering DNS records are deprecated:</p>
<ul>
<li><code>name=contains:value</code>
Instead, use the supported <code>name.contains=value</code> syntax.</li>
<li><code>name=starts_with:value</code>
Instead, use the supported <code>name.startswith=value</code> syntax.</li>
<li><code>name=ends_with:value</code>
Instead, use the supported <code>name.endswith=value</code> syntax.</li>
<li><code>name=one,two,three</code> (searching for one of multiple possible names, separated by commas)
Instead, make multiple requests, one for each possible <code>name</code>.
Alternatively, if only querying the <code>name</code> field, the <code>?match=any&amp;name=one&amp;name=two&amp;name=three</code> syntax can be used instead.
This syntax has an extended deprecation date of May 23, 2025.</li>
<li><code>content=contains:value</code>
Instead, use the supported <code>content.contains=value</code> syntax.</li>
<li><code>content=starts_with:value</code>
Instead, use the supported <code>content.startswith=value</code> syntax.</li>
<li><code>content=ends_with:value</code>
Instead, use the supported <code>content.endswith=value</code> syntax.</li>
<li><code>content=one,two,three</code> (searching for one of multiple possible contents, separated by commas)
Instead, make multiple requests, one for each possible <code>content</code>.
Alternatively, if only querying the <code>content</code> field, the <code>?match=any&amp;content=one&amp;content=two&amp;content=three</code> syntax can be used instead.
This syntax has an extended deprecation date of May 23, 2025.</li>
<li><code>type=contains:value</code>
Searching for substrings of a type name will no longer be supported.
Instead, please search for an exact type name, such as <code>type=CNAME</code>.
If the input value is a free-text search from a human user, consider using the <code>search</code> parameter instead.</li>
</ul>
<p>None of the parameters being deprecated were ever officially supported per our API documentation.</p>
<p>Affected APIs:</p>
<ul>
<li><code>GET /zones/:zone_id/dns_records</code></li>
</ul><h2 id="2024-12-09">2024-12-09</h2><strong>Access applications: self_hosted_domains</strong><p>Deprecation date: November 21, 2025</p>
<p>The <code>self_hosted_domains</code> field for <a href="https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/applications/methods/update/">Access applications</a> is deprecated in favor of <code>destinations</code> to allow for more flexibility in defining different types of domains.</p>
<p>Before:</p>
<pre tabindex="0"><code class="language-json">{&#10;  // ...&#10;  &quot;self_hosted_domains&quot;: [&quot;foo.example.com&quot;, &quot;bar.example.com&quot;]&#10;}&#10;</code></pre>
<p>After:</p>
<pre tabindex="0"><code class="language-json">{&#10;  // ...&#10;  &quot;destinations&quot;: [&#10;    {&#10;      &quot;type&quot;: &quot;public&quot;,&#10;      &quot;uri&quot;: &quot;foo.example.com&quot;&#10;    },&#10;    {&#10;      &quot;type&quot;: &quot;public&quot;,&#10;      &quot;uri&quot;: &quot;bar.example.com&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<p>The API will accept both fields until the deprecation date. If <code>self_hosted_domains</code> are provided, then they will be interpreted as <code>public</code> destinations. However, if <code>destinations</code> are provided, then <code>self_hosted_domains</code> will be ignored even if provided.</p>
<p>Additionally, the API will continue to return <code>self_hosted_domains</code> until the deprecation date. The field will contain the URIs of the subset of destinations that have type <code>public</code>.</p>
<p>Affected APIs:</p>
<ul>
<li><code>GET /accounts/:account_id/access/apps</code></li>
<li><code>POST /accounts/:account_id/access/apps</code></li>
<li><code>GET /accounts/:account_id/access/apps/:app_id</code></li>
<li><code>PUT /accounts/:account_id/access/apps/:app_id</code></li>
<li><code>GET /zones/:zone_id/access/apps</code></li>
<li><code>POST /zones/:zone_id/access/apps</code></li>
<li><code>GET /zones/:zone_id/access/apps/:app_id</code></li>
<li><code>PUT /zones/:zone_id/access/apps/:app_id</code></li>
</ul><h2 id="2024-11-30">2024-11-30</h2><strong>Zone information in individual DNS records</strong><p>Deprecation date: November 30, 2024</p>
<p>Currently, each individual DNS record returned by the API contains information about the zone it is on, specifically the zone ID and name.</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;result&quot;: [&#10;    {&#10;      // ...&#10;      &quot;zone_id&quot;: &quot;ab922473c42f4e50819d7c1c9b81b16b&quot;,&#10;      &quot;zone_name&quot;: &quot;example.com&quot;&#10;    }&#10;  ],&#10;  // ...&#10;}&#10;</code></pre>
<p>This information is redundant because both affected API routes are already within the zone scope. In particular, the zone ID will already be known to any user of these routes because it appears in the URL. The zone name can be retrieved by making a <code>GET</code> request to <code>/zones/:zone_id</code> if it is necessary.</p>
<p>After November 30th, 2024, Cloudflare will stop including the <code>zone_id</code> and <code>zone_name</code> fields on individual DNS records in API responses. These fields are currently ignored when sent to the API as part of a request body, so no changes to request bodies are required.</p>
<p>Modified API:</p>
<ul>
<li><code>GET /zones/:zone_id/dns_records</code></li>
<li><code>POST /zones/:zone_id/dns_records</code></li>
<li><code>GET /zones/:zone_id/dns_records/:dns_record_id</code></li>
<li><code>PATCH /zones/:zone_id/dns_records/:dns_record_id</code></li>
<li><code>PUT /zones/:zone_id/dns_records/:dns_record_id</code></li>
</ul><h2 id="2024-10-01">2024-10-01</h2><strong>DNS Records: Error chains for DNS validation errors</strong><p>Deprecation date: October 1, 2024</p>
<p>Cloudflare is making a minor change to the representation of certain errors when creating DNS records. Currently, when the DNS record to be created is invalid, an error similar to the following may be returned:</p>
<pre tabindex="0"><code class="language-txt">{&#10;  &quot;result&quot;: null,&#10;  &quot;success&quot;: false,&#10;  &quot;errors&quot;: [&#10;    {&#10;      &quot;code&quot;: 1004,&#10;      &quot;message&quot;: &quot;DNS Validation Error&quot;,&#10;      &quot;error_chain&quot;: [&#10;        {&#10;          &quot;code&quot;: 9999,&#10;          &quot;message&quot;: &quot;This is an example.&quot;&#10;        }&#10;      ]&#10;    }&#10;  ],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>After October 1st, 2024, the <code>error_chain</code> will be omitted, returning the root cause directly without wrapping it in another &quot;DNS Validation Error&quot; error:</p>
<pre tabindex="0"><code class="language-txt">{&#10;  &quot;result&quot;: null,&#10;  &quot;success&quot;: false,&#10;  &quot;errors&quot;: [&#10;    {&#10;      &quot;code&quot;: 9999,&#10;      &quot;message&quot;: &quot;This is an example.&quot;&#10;    }&#10;  ],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre><h2 id="2024-09-13">2024-09-13</h2><strong>Legacy DNS Settings Endpoints</strong><p>Deprecation date: September 13, 2024</p>
<p>The dedicated endpoints for DNS settings <code>use_apex_ns</code> and <code>secondary_overrides</code> are being deprecated.</p>
<p>Instead, use the <a href="/api/resources/dns/subresources/settings/subresources/zone/methods/get/">Show DNS Settings</a> and <a href="/api/resources/dns/subresources/settings/subresources/zone/methods/edit/">Update DNS Settings</a> endpoints to manage these settings.</p>
<ul>
<li>Instead of the <code>.../use_apex_ns</code> endpoint, use the <code>multi_provider</code> field.</li>
<li>Instead of the <code>.../secondary_overrides</code> endpoint, use the <code>secondary_overrides</code> field.</li>
</ul>
<p>Deprecated APIs:</p>
<ul>
<li><code>GET /zones/:zone_id/dns_settings/use_apex_ns</code></li>
<li><code>PATCH /zones/:zone_id/dns_settings/use_apex_ns</code></li>
<li><code>GET /zones/:zone_id/dns_settings/secondary_overrides</code></li>
<li><code>PATCH /zones/:zone_id/dns_settings/secondary_overrides</code></li>
</ul><h2 id="2024-08-15">2024-08-15</h2><strong>Brotli</strong><p>Deprecation date: August 15, 2024</p>
<p>The Brotli setting and its API endpoints are deprecated. Brotli compression is available for all non-Enterprise zones, and it will be extended to Enterprise zones in the coming year.</p>
<p>Deprecated APIs:</p>
<ul>
<li><code>GET /zones/:zone_id/settings/brotli</code></li>
<li><code>PATCH /zones/:zone_id/settings/brotli</code></li>
</ul>
<p>Enterprise customers can override Cloudflare's default compression behavior using <a href="/rules/compression-rules/">Compression Rules</a>.</p><h2 id="2024-08-05">2024-08-05</h2><strong>Auto Minify</strong><p>Deprecation date: August 5, 2024</p>
<p>The Auto Minify API endpoints are deprecated since the Auto Minify feature was deprecated.</p>
<p>Deprecated APIs:</p>
<ul>
<li><code>GET /zones/:zone_id/settings/minify</code></li>
<li><code>PATCH /zones/:zone_id/settings/minify</code></li>
</ul><h2 id="2024-07-14">2024-07-14</h2><strong>DNS Records: &#x27;locked&#x27; Field</strong><p>Deprecation date: July 14, 2024</p>
<p>The <code>&quot;locked&quot;</code> field of DNS records in API responses is unused and has been guaranteed to always be <code>false</code> for more than a year. This deprecation means that the field will be omitted from API responses entirely. If received from a client, the field will continue to be ignored, just as it is today.</p>
<p>Modified API:</p>
<ul>
<li><code>GET /zones/:zone_id/dns_records</code></li>
<li><code>POST /zones/:zone_id/dns_records</code></li>
<li><code>GET /zones/:zone_id/dns_records/:dns_record_id</code></li>
<li><code>PATCH /zones/:zone_id/dns_records/:dns_record_id</code></li>
<li><code>PUT /zones/:zone_id/dns_records/:dns_record_id</code></li>
</ul><h2 id="2024-06-30">2024-06-30</h2><strong>Mobile redirect</strong><p>Deprecation date: June 30, 2024</p>
<p>This endpoint and its related APIs are deprecated in favor of <a href="/rules/url-forwarding/single-redirects/">Single Redirects</a>. Refer to <a href="/rules/url-forwarding/examples/perform-mobile-redirects/">Perform mobile redirects</a> to migrate Mobile Redirect to Redirect Rules.</p>
<p>Deprecated API:</p>
<ul>
<li><code>GET /zones/:zone_identifier/settings/mobile_redirect</code></li>
<li><code>PATCH /zones/:zone_identifier/settings/mobile_redirect</code></li>
</ul>
<p>Replacement: <a href="/rules/url-forwarding/single-redirects/">Single Redirects</a></p><h2 id="2024-06-14">2024-06-14</h2><strong>Server-side Excludes</strong><p>Deprecation date: June 14, 2024</p>
<p>The Server-side Excludes feature and its API endpoints are deprecated.</p>
<p>Deprecated APIs:</p>
<ul>
<li><code>GET /zones/:zone_id/settings/server_side_exclude</code></li>
<li><code>PATCH /zones/:zone_id/settings/server_side_exclude</code></li>
</ul><h2 id="2024-05-31">2024-05-31</h2><strong>Name-Related Data Fields on SRV (DNS) Records</strong><p>Deprecation date: May 31, 2024</p>
<p>The name of an SRV record normally consists of three parts: the service (e.g., <code>_xmpp</code>), the protocol (e.g., <code>_tcp</code>), and the base name (<code>example.com</code>).</p>
<p>The complete name would then be, e.g., <code>_xmpp._tcp.example.com</code>.</p>
<p>When interacting with DNS records through the <a href="/api/resources/dns/subresources/records/methods/create/">API</a>, SRV records contain both a full <code>name</code> as well as a <code>data</code> map containing the individual components of the name:</p>
<pre tabindex="0"><code class="language-txt">{&#10;  &quot;name&quot;: &quot;_xmpp._tcp.example.com&quot;,&#10;  &quot;data&quot;: {&#10;    &quot;service&quot;: &quot;_xmpp&quot;,&#10;    &quot;proto&quot;: &quot;_tcp&quot;,&#10;    &quot;name&quot;: &quot;example.com&quot;,&#10;    ...&#10;  },&#10;  ...&#10;}&#10;</code></pre>
<p>We are deprecating the <code>service</code>, <code>proto</code> and <code>name</code> fields <em>within</em> the <code>data</code> map in favor of the <code>name</code> field <em>outside</em> the data map, which is the same name field that's used by all other record types.</p>
<p>Before the end of life date, please ensure that:</p>
<ul>
<li>when reading SRV records, you use only the <code>name</code> outside of the data map and ignore <code>service</code>, <code>proto</code> and <code>name</code> within the data map if they exist; and</li>
<li>when writing SRV records, you set the <code>name</code> outside of the data map and <strong>do not set</strong> <code>service</code>, <code>proto</code> or <code>name</code> within the data map.</li>
</ul>
<p>After the end of life date, the API will stop producing the <code>service</code>, <code>proto</code> and <code>name</code> data fields, and if any of them are received from a client, an error will be returned.</p>
<p>This deprecation does not affect other SRV data fields not mentioned above (<code>priority</code>, <code>weight</code>, <code>port</code>, <code>target</code>) or data fields for any other record type other than SRV.</p>
<p>Modified API:</p>
<ul>
<li><code>GET /zones/:zone_id/dns_records</code></li>
<li><code>POST /zones/:zone_id/dns_records</code></li>
<li><code>GET /zones/:zone_id/dns_records/:dns_record_id</code></li>
<li><code>PATCH /zones/:zone_id/dns_records/:dns_record_id</code></li>
<li><code>PUT /zones/:zone_id/dns_records/:dns_record_id</code></li>
</ul><h2 id="2024-03-31">2024-03-31</h2><strong>Privacy Pass API Removal</strong><p>Deprecation date: March 31, 2024</p>
<p>In 2017, Cloudflare <a href="https://blog.cloudflare.com/cloudflare-supports-privacy-pass/">announced support</a> for Privacy Pass, a recent protocol to let users prove their identity across multiple sites anonymously without enabling tracking. The initial use case was to provide untraceable tokens to sites to vouch for users who might otherwise have been presented with a CAPTCHA challenge. In the time since this release, Privacy Pass has evolved both at the <a href="https://datatracker.ietf.org/wg/privacypass/documents/">IETF</a> and within Cloudflare. The version announced in 2017 is now considered legacy, and these legacy Privacy Pass tokens are no longer supported as an alternative to Cloudflare challenges. As has been discussed on our blog <a href="https://blog.cloudflare.com/end-cloudflare-captcha/">The end road for CAPTCHA</a>, Cloudflare uses a variety of signals to infer if incoming traffic is likely automated. The (legacy) Privacy Pass zone setting is no longer meaningful to Cloudflare customers as Cloudflare now operates <a href="https://blog.cloudflare.com/turnstile-ga/">CAPTCHA free</a>, and supports the latest <a href="https://blog.cloudflare.com/eliminating-captchas-on-iphones-and-macs-using-new-standard/">Privacy Pass draft</a>.</p>
<p>In September 2023, support for legacy Privacy Pass tokens as an alternative to Cloudflare Managed Challenge was removed. By the end of March 2024, the current public-facing API will be removed as well.</p>
<p>Deprecated API:</p>
<ul>
<li><code>GET zones/:zone_identifier/settings/privacy_pass</code></li>
<li><code>POST zones/:zone_identifier/settings/privacy_pass</code></li>
</ul><h2 id="2024-02-04">2024-02-04</h2><strong>Argo Tunnel</strong><p>Deprecation date: February 4, 2024</p>
<p>This endpoint and its related APIs are deprecated in favor of the Cloudflare Tunnels equivalent APIs.</p>
<p>Deprecated API:</p>
<ul>
<li><code>GET accounts/:account_identifier/tunnels</code></li>
<li><code>POST accounts/:account_identifier/tunnels</code></li>
<li><code>GET accounts/:account_identifier/tunnels/:tunnel_id</code></li>
<li><code>DELETE accounts/:account_identifier/tunnels/:tunnel_id</code></li>
</ul>
<p>Replacement:
Cloudflare Tunnel API</p><h2 id="2023-07-01">2023-07-01</h2><strong>ChaCha20 TLS Cipher Removal</strong><p>Deprecation date: July 1, 2023</p>
<p>Back in 2016, Cloudflare <a href="https://blog.cloudflare.com/it-takes-two-to-chacha-poly/">introduced support</a> for <code>ChaCha20-Poly1305</code> cipher suites for TLS 1.2. At the time, we introduced two variants of these new suites, the &quot;standard&quot; suites as defined by the IETF RFC 7905, and &quot;draft&quot; suites that followed an earlier draft of said specification. The draft suites were added for compatibility with some older Android devices that at the time did not yet support the proper <code>ChaCha20-Poly1305</code> standard versions. This was in 2016, and in the meantime the standard <code>ChaCha20-Poly1305</code> cipher suites have gained much wider adoption, to the point were traffic using the old suites has dropped significantly. Due to the current low usage and the non-standard nature of these cipher suites, we are now deprecating their support on the Cloudflare network.</p>
<p>This should not affect customer zones in any way, as clients that might currently use these cipher suites will be able to fallback to different ones. In addition, unlike the standard variants, these legacy cipher suites are not exposed directly through our API (e.g. through the TLS cipher suites preferences endpoint), and their deprecation will not affect customer configurations in any way.</p>
<p>As of July 1st, 2023, the ChaCha20-Poly1305 ciphers have been deprecated and are deemed End of Life by Cloudflare. If you have clients that currently rely on these ciphers, it is strongly recommended to upgrade them to newer, more secure ciphers. Be aware that these deprecated ciphers will be completely removed in the first quarter of 2024, and requests using them will start to fail. Take proactive measures to ensure a smooth transition and maintain the security of your systems.</p><h2 id="2023-07-01-1">2023-07-01</h2><strong>Transfer-Encoding and Content-Length headers</strong><p>Deprecation date: July 1, 2023</p>
<p>Previously, RFC 2616 allowed the use of <code>Transfer-Encoding</code> and <code>Content-Length</code> HTTP headers in the same request. RFC 7230 supersedes RFC 2616 and prohibits the use of <code>Transfer-Encoding</code> and <code>Content-Length</code> headers in the same request because they can cause HTTP request smuggling vulnerabilities.</p>
<p>Starting on July 1st, 2023, Cloudflare will decline requests with both <code>Transfer-Encoding</code> and <code>Content-Length</code> HTTP headers.</p><h2 id="2023-06-06">2023-06-06</h2><strong>Account Billing Profile, User Billing Profile, and User Billing History</strong><p>Deprecation date: June 6, 2023</p>
<p>There is no API replacement for these endpoints. As an alternative, please log in to your Cloudflare account to view your:</p>
<ul>
<li><a href="https://dash.cloudflare.com/?to=/:account/billing">Invoices &amp; Billing Email</a></li>
<li><a href="https://dash.cloudflare.com/?to=/:account/billing/subscriptions">Billing subscriptions</a></li>
<li><a href="https://dash.cloudflare.com/?to=/:account/billing/payment-info">Billing profile payment info</a></li>
</ul>
<p>Deprecated API:</p>
<ul>
<li><code>GET accounts/{account_identifier}/billing/profile</code></li>
<li><code>GET user/billing/profile</code></li>
<li><code>GET user/billing/history</code></li>
</ul><h2 id="2023-04-03">2023-04-03</h2><strong>Load Balancing - notification_email</strong><p>Deprecation date: April 3, 2023</p>
<p>This field is deprecated and has been moved to <a href="/notifications/">Cloudflare centralized notification service</a>.</p>
<p><code>notification_email</code> is the email address to send health status notifications to. This can be an individual mailbox or a mailing list. Multiple emails can be supplied as a comma delimited list.</p><h2 id="2023-03-19">2023-03-19</h2><strong>Access Bookmark applications</strong><p>Deprecation date: March 19, 2023</p>
<p>This endpoint is deprecated in favor of using a specialized Access Application App Type API.</p>
<p>Deprecated API:</p>
<ul>
<li><code>GET accounts/:identifier/access/bookmarks</code></li>
<li><code>GET accounts/:identifier/access/bookmarks/:uuid</code></li>
<li><code>POST accounts/:identifier/access/bookmarks/:uuid</code></li>
<li><code>PUT accounts/:identifier/access/bookmarks/:uuid</code></li>
<li><code>DELETE accounts/:identifier/access/bookmarks/:uuid</code></li>
</ul>
<p>Replacement:
Access applications app type API</p><h2 id="2022-10-11">2022-10-11</h2><strong>Page Shield</strong><p>Deprecation date: October 11, 2022</p>
<p>Replace <code>script_monitor</code> in Page Shield API routes with <code>page_shield</code>.</p><h2 id="2022-07-01">2022-07-01</h2><strong>Cloudflare Images - Create authenticated direct upload URL v1</strong><p>Deprecation date: July 1, 2022</p>
<p>This endpoint is deprecated in favor of using v2, which allows you to control metadata, define an access policy, and get the image ID.</p>
<p>Deprecated API:
<code>POST accounts/:account_identifier/images/v1/direct_upload</code></p>
<p>Replacement:
<code>POST accounts/:account_identifier/images/v2/direct_upload</code></p><h2 id="2021-03-01">2021-03-01</h2><strong>Zone Analytics API</strong><p>Deprecation date: March 1, 2021</p>
<p>This API is deprecated in favor of the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>, which provides equivalent data and more features, including the ability to select only the metrics that you need. For more information, refer to the <a href="/analytics/graphql-api/migration-guides/zone-analytics/">Zone analytics to GraphQL analytics migration guide</a>.</p>
<p>Deprecated API:</p>
<ul>
<li><code>GET zones/:zone_identifier/analytics/dashboard</code></li>
<li><code>GET zones/:zone_identifier/analytics/colos</code></li>
</ul>
<p>Replacement:
GraphQL Analytics API</p><h2 id="2020-04-02">2020-04-02</h2><strong>Organizations</strong><p>Deprecation date: April 2, 2020</p>
<p>This endpoint and its related APIs are deprecated in favor of the <code>/accounts</code> equivalent API, which has a broader range of features and is backwards compatible with the <code>/organizations</code> API.</p>
<p>Deprecated API:</p>
<ul>
<li><code>GET organizations/:identifier</code></li>
<li><code>PATCH organizations/:identifier</code></li>
<li><code>GET organizations/:organization_identifier/invites</code></li>
<li><code>POST organizations/:organization_identifier/invites</code></li>
<li><code>GET organizations/:organization_identifier/invites/:identifier</code></li>
<li><code>PATCH organizations/:organization_identifier/invites/:identifier</code></li>
<li><code>DELETE organizations/:organization_identifier/invites/:identifier</code></li>
<li><code>GET organizations/:organization_identifier/members</code></li>
<li><code>GET organizations/:organization_identifier/members/:identifier</code></li>
<li><code>PATCH organizations/:organization_identifier/members/:identifier</code></li>
<li><code>DELETE organizations/:organization_identifier/members/:identifier</code></li>
<li><code>GET organizations/:organization_identifier/roles</code></li>
<li><code>GET organizations/:organization_identifier/roles/:identifier</code></li>
<li><code>GET organizations/:organization_identifier/audit_logs</code></li>
<li><code>GET organizations/:organization_identifier/railguns</code></li>
<li><code>POST organizations/:organization_identifier/railguns</code></li>
<li><code>GET organizations/:organization_identifier/railguns/:identifier</code></li>
<li><code>PATCH organizations/:organization_identifier/railguns/:identifier</code></li>
<li><code>DELETE organizations/:organization_identifier/railguns/:identifier</code></li>
<li><code>GET organizations/:organization_identifier/railguns/:identifier/zones</code></li>
</ul>
<p>Replacement:
Accounts API</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/fundamentals/new-features/available-rss-feeds/">Available RSS feeds</a> (for the <a href="/changelog/">Cloudflare changelog</a>)</li>
<li><a href="/support/cloudflare-status/">Subscribe to Cloudflare Status</a></li>
<li><a href="/support/disruptive-maintenance/">Planned maintenance windows</a></li>
</ul>
