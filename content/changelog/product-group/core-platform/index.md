<h1 id="changelog">Changelog</h1>

<h2 id="create-additional-free-accounts-through-the-dashboard-and-api"><a href="/changelog/post/2026-09-15-free-account-creation/">Create additional Free accounts through the dashboard and API</a></h2>
<p><em>2026-09-17</em></p>
<p>We're expanding how customers create accounts across Cloudflare, making it easier to self-serve account creation in the dashboard, automate standalone account creation with user-owned API tokens or OAuth access tokens, and create Free accounts directly within Enterprise Organizations.</p>
<h4 id="2026-09-15-free-account-creation-what-s-new">What's New</h4>
<p><strong>Dashboard account creation:</strong> All cloudflare customers can create additional Free accounts directly through self-serve flows in the Cloudflare dashboard.</p>
<p><strong>Enterprise Organization account creation:</strong> Super Administrators can now create up to five Free accounts directly within an Enterprise Organization. This makes it easier to provision and manage additional accounts and directly associate them with your Organization.</p>
<p><strong>API and OAuth account creation:</strong> Customers can now create standalone Free accounts programmatically via User-owned API tokens or OAuth access tokens.</p>
<p>For more information:</p>
<ul>
<li><a href="/fundamentals/account/create-account/">Create a Free account in the dashboard</a></li>
<li><a href="/api/resources/accounts/methods/create/">Create an account via the API</a></li>
<li><a href="/fundamentals/organizations/for-enterprise/#create-new-accounts">Create Free accounts in an Enterprise Organization</a></li>
</ul>


<h2 id="enterprise-customers-can-self-serve-cdn-upload-limits-up-to-5-gb"><a href="/changelog/post/2026-09-04-enterprise-self-serve-upload-limits/">Enterprise customers can self-serve CDN upload limits up to 5 GB</a></h2>
<p><em>2026-09-04</em></p>
<p>Enterprise customers can now configure a zone's CDN <strong>Maximum Upload Size</strong> up to 5 GB directly from the <strong>Network</strong> page in the Cloudflare dashboard. This removes the need to contact your account team or Cloudflare Support when applications need to accept request bodies larger than 500 MB and no greater than 5 GB.</p>
<p>The default maximum upload size remains 500 MB. Upload limits above 5 GB still require additional configuration through your account team or <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a>.</p>
<p>Very large uploads may reach connection or read timeouts before reaching the configured size limit. Make sure clients and origins allow enough time to complete the transfer when increasing this setting.</p>
<p>Refer to <a href="/cache/concepts/default-cache-behavior/#upload-limits">Cache upload limits</a> and <a href="/workers/platform/limits/#request-and-response-limits">Workers request body size limits</a> for details.</p>


<h2 id="create-multiple-cloudflare-tunnel-and-cloudflare-mesh-routes-at-once"><a href="/changelog/post/2026-09-02-tunnel-mesh-bulk-route-creation/">Create multiple Cloudflare Tunnel and Cloudflare Mesh routes at once</a></h2>
<p><em>2026-09-02</em></p>
<p>You can now create multiple <a href="/tunnel/">Cloudflare Tunnel</a> and <a href="/mesh/">Cloudflare Mesh</a> routes from the Routes page in a single action, instead of submitting one route at a time.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/2026-09-01-tunnel-mesh-bulk.gif" alt="Creating multiple Cloudflare Tunnel and Cloudflare Mesh routes at once from the Routes page" /></p>
<p>When creating a route, you can now:</p>
<ul>
<li><strong>Add multiple destinations at once</strong> — Enter a comma-separated list of CIDR ranges or hostnames to create several routes of the same type and connector together.</li>
<li><strong>Queue up multiple routes</strong> — Select <strong>Add another</strong> to stage additional routes, including different types or connectors, before creating them all in one action.</li>
<li><strong>Retry only what failed</strong> — If some routes in a batch fail (for example, an invalid CIDR), the routes that were created successfully are removed from the form automatically, so you only need to fix and resubmit the ones that failed.</li>
</ul>
<p>The same Routes UI already supports bulk creation for <a href="/cloudflare-wan/">Cloudflare WAN</a> static routes, so you can add multiple WAN destinations or queue up several WAN routes before creating them together as well.</p>
<div class="nb-dash-button"></div>
<p>For setup steps, refer to <a href="/cloudflare-one/networks/routes/add-routes/">Add routes</a>.</p>


<h2 id="improved-dataset-configuration-in-log-explorer"><a href="/changelog/post/2026-08-28-dataset-configuration/">Improved dataset configuration in Log Explorer</a></h2>
<p><em>2026-08-28</em></p>
<p>Log Explorer has a refreshed dataset configuration experience in the Cloudflare dashboard. The new controls make it easier to choose which fields and events Log Explorer ingests.</p>
<ul>
<li><strong>Grouped field selection</strong> organizes fields by category and shows the number selected in each group.</li>
<li><strong>Field details</strong> identify each field's data type and mark required or deprecated fields.</li>
<li><strong>Bulk controls</strong> let you select all fields or reset the selection to the dataset defaults.</li>
<li><strong>Ingestion filters</strong> let you ingest all events or only events that match your conditions.</li>
</ul>
<p>These controls are available when you add a dataset or select <strong>Actions</strong> &gt; <strong>Edit</strong> for an enabled dataset.</p>
<p>For more information, refer to <a href="/log-explorer/manage-datasets/#configure-fields-and-filters">Configure fields and filters</a>.</p>


<h2 id="delete-log-explorer-datasets"><a href="/changelog/post/2026-08-26-dataset-deletion/">Delete Log Explorer datasets</a></h2>
<p><em>2026-08-26</em></p>
<p>Cloudflare Log Explorer customers can now permanently delete account and zone datasets from the Cloudflare dashboard or API.</p>
<p>Deletion protection is enabled by default to prevent accidental data loss. In the dashboard, go to <a href="/log-explorer/manage-datasets/">Manage datasets</a>, disable deletion protection for the dataset, select <strong>Delete</strong>, and enter the dataset name to confirm.</p>
<p>To delete a dataset through the API, first set <code>deletion_protection</code> to <code>false</code> with the <a href="/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/update/">Update an account or zone dataset</a> method. Then use the <a href="/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/delete/">Delete an account or zone dataset</a> method.</p>
<p>Dataset deletion is irreversible and runs asynchronously. You cannot recreate the same dataset while deletion is in progress.</p>


<h2 id="azure-functions-based-microsoft-sentinel-connector-deprecation"><a href="/changelog/post/2026-08-26-sentinel-functions-connector-deprecation/">Azure Functions-based Microsoft Sentinel connector deprecation</a></h2>
<p><em>2026-08-26</em></p>
<p>Cloudflare Enterprise customers using the <a href="https://marketplace.microsoft.com/en-us/product/cloudflare.cloudflare_sentinel?tab=Overview">Azure Functions-based Microsoft Sentinel connector</a> must migrate to the <a href="https://marketplace.microsoft.com/en-us/product/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview">Cloudflare for Microsoft Sentinel Codeless Connector Framework (CCF) connector</a> by 2026-09-14.</p>
<p>Microsoft is deprecating the Azure Monitor HTTP Data Collector API. Support for the API ends on 2026-09-14. As a result, Cloudflare will no longer maintain the Azure Functions-based connector after that date.</p>
<p>To migrate, follow the <a href="/analytics/analytics-integrations/sentinel/">Microsoft Sentinel integration setup guide</a>.</p>
<h4 id="2026-08-26-sentinel-functions-connector-deprecation-additional-resources">Additional resources</h4>
<ul>
<li><a href="https://marketplace.microsoft.com/en-us/product/azure-application/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview">Download Cloudflare's CCF Sentinel Solution</a></li>
<li><a href="https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-overview">Microsoft Sentinel data lake overview</a></li>
<li><a href="https://learn.microsoft.com/en-us/azure/sentinel/create-codeless-connector">About the CCF platform</a></li>
</ul>
<p>For more information, refer to Microsoft's <a href="https://learn.microsoft.com/en-us/previous-versions/azure/azure-monitor/logs/data-collector-api?tabs=powershell">Azure Monitor HTTP Data Collector API deprecation notice</a>.</p>


<h2 id="enriched-403-responses-for-the-cloudflare-api"><a href="/changelog/post/2026-08-20-contextual-403s/">Enriched 403 responses for the Cloudflare API</a></h2>
<p><em>2026-08-21</em></p>
<p>Cloudflare API <code>403 Forbidden</code> responses now include a <code>documentation_url</code> field that links directly to the API documentation for the endpoint that was denied. This gives developers, administrators, and agents an immediate path to the relevant docs with role information instead of guessing at which role or permission they are missing for that endpoint.</p>
<p><strong>What's New</strong></p>
<p><strong>Enriched 403 error responses</strong>: When a Cloudflare API request is denied, the error response now includes a <code>documentation_url</code> field that points to the documentation for that specific endpoint. Contextual 403 responses are now available across nearly all Cloudflare product APIs.</p>
<p><strong>Faster troubleshooting</strong>: The linked API docs surface the roles required for each endpoint, making it easier to self-serve access issues.</p>
<p><strong>Better support for tools and agents</strong>: Agents can use the \documentation_url` field to immediately fetch the endpoint's documentation from the 403 error response, identify the accepted permissions for the denied action, and use that context to drive third-party approval workflows.`</p>
<p>Example 403 response:</p>
<pre><code class="language-json">{&#10;  &quot;success&quot;: false,&#10;  &quot;errors&quot;: [&#10;    {&#10;      &quot;code&quot;: 10000,&#10;      &quot;message&quot;: &quot;Forbidden&quot;,&#10;      &quot;documentation_url&quot;: &quot;https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/methods/list&quot;&#10;    }&#10;  ],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: null&#10;}&#10;</code></pre>
<p>For more info:</p>
<ul>
<li><a href="/api/">Browse the Cloudflare API documentation</a></li>
<li><a href="/fundamentals/manage-members/roles/">Review Cloudflare roles</a></li>
<li><a href="/fundamentals/api/reference/permissions/">Review API token permissions</a></li>
</ul>


<h2 id="saved-login-profiles-for-returning-users"><a href="/changelog/post/2026-08-21-one-click-login/">Saved login profiles for returning users</a></h2>
<p><em>2026-08-21</em></p>
<p>Cloudflare Dashboard users can now save login profiles on a device for faster sign-in on future visits.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-08-21-one-click-login.png" alt="Saved login profiles for returning users" /></p>
<p><strong>What's New</strong></p>
<p><strong>Save login profiles on a device</strong>: After a successful sign-in, users can choose to save a login profile on that device. Saved profiles store the email address, login method, and last-used profile locally in the browser.</p>
<p><strong>Faster sign-in for returning users</strong>: Saved profiles appear directly on the login page. Selecting one can prefill the email field for password logins or resume the associated SSO or social login flow.</p>
<p>Up to five login profiles can be saved per device, and saved profiles can be removed from the profile list at any time.</p>
<p>For more info:</p>
<ul>
<li><a href="/fundamentals/user-profiles/login/">Log in to Cloudflare</a></li>
<li><a href="/fundamentals/manage-members/dashboard-sso/">Set up dashboard SSO</a></li>
</ul>


<h2 id="improved-scim-2-0-group-synchronization"><a href="/changelog/post/2026-08-21-scim-put-group-synchronization/">Improved SCIM 2.0 group synchronization</a></h2>
<p><em>2026-08-21</em></p>
<p>Dashboard SCIM now supports replacing groups using HTTP <code>PUT</code>, as defined by <a href="https://datatracker.ietf.org/doc/html/rfc7644#section-3.5.1">RFC 7644 section 3.5.1</a>. This allows identity providers to synchronize a group's full state, including its display name, external ID, and members, in a single request.</p>
<p><strong>What's New</strong></p>
<p><strong>Group replacement via <code>PUT</code></strong>: Full-state group synchronization improves compatibility with identity providers that use replacement semantics and helps keep Cloudflare groups aligned with their source identity provider.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17732.md")</aside>
<p>For more information:</p>
<ul>
<li><a href="/fundamentals/account/account-security/scim-setup/">SCIM provisioning overview</a></li>
</ul>


<h2 id="optional-oauth-scopes"><a href="/changelog/post/2026-08-20-oauth-optional-scopes/">Optional OAuth scopes</a></h2>
<p><em>2026-08-20</em></p>
<p>We're announcing the GA of Optional OAuth Scopes.</p>
<p>OAuth client developers can now classify configured scopes as required or optional in the Cloudflare dashboard. By default, all configured scopes remain required .</p>
<h4 id="2026-08-20-oauth-optional-scopes-what-s-new">What's New</h4>
<p><strong>Optional Scopes:</strong> OAuth clients can now mark configured scopes as optional, allowing applications to request them without requiring users to approve them.</p>
<p><strong>Scope Selection:</strong> On the consent screen, users must grant required scopes but can decline optional scopes. This helps customers apply least-privilege access to applications, CLIs, and workloads. Optional scopes are selected by default.</p>
<p><strong>Templates:</strong> The consent screen now includes <strong>Read Only</strong> and <strong>Full Access</strong> templates to make scope selection faster and easier.</p>
<p><strong>Search:</strong> Users can now search scopes in the consent screen.</p>
<p>Learn how to <a href="/fundamentals/oauth/create-an-oauth-client/#select-scopes">select client scopes</a> and <a href="/fundamentals/oauth/authorizing-an-application/#edit-optional-permissions">edit optional permissions</a>.</p>


<h2 id="new-logpush-datasets-and-updated-fields-across-multiple-logpush-datasets-in-cloudflare-logs"><a href="/changelog/post/2026-08-20-log-fields-updated/">New Logpush datasets and updated fields across multiple Logpush datasets in Cloudflare Logs</a></h2>
<p><em>2026-08-20</em></p>
<p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-08-20-log-fields-updated-new-datasets">New datasets</h4>
<ul>
<li><strong>Account Abuse Protection Events</strong>: A new dataset with fields including <code>AuthenticationIdentityProvider</code>, <code>AuthenticationMethod</code>, <code>AuthenticationStatus</code>, <code>BotScore</code>, <code>ClientASN</code>, <code>ClientCity</code>, <code>ClientCountry</code>, <code>ClientIP</code>, <code>Email</code>, <code>EphemeralID</code>, <code>EventSource</code>, <code>EventType</code>, <code>FraudEmailRisk</code>, <code>Host</code>, <code>JA4</code>, <code>RayID</code>, <code>Timestamp</code>, <code>UserAgent</code>, and <code>UserID</code>.</li>
<li><strong>Magic BGP Logs</strong>: A new dataset with fields including <code>Direction</code>, <code>EventData</code>, <code>EventKind</code>, <code>EventTimestamp</code>, <code>TunnelID</code>, and <code>TunnelName</code>.</li>
</ul>
<h4 id="2026-08-20-log-fields-updated-updated-fields-in-existing-datasets">Updated fields in existing datasets</h4>
<ul>
<li><strong>Firewall events</strong> (added): <code>AISecurityCustomTopicCategories</code>, <code>WAFRequestSignatureCategories</code>, and <code>WAFRequestSignatureRefs</code>.</li>
<li><strong>Gateway HTTP</strong> (added): <code>ExperimentalFeatures</code> and <code>PackageInfo</code>.</li>
<li><strong>HTTP requests</strong> (added): <code>AISecurityCustomTopicCategories</code>, <code>ClientTLSKeyExchangeGroup</code>, <code>WAFRequestSignatureCategories</code>, and <code>WAFRequestSignatureRefs</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>


<h2 id="per-zone-post-quantum-visibility-in-logpush-and-log-explorer"><a href="/changelog/post/2026-08-20-pqc-key-exchange-visibility/">Per-zone post-quantum visibility in Logpush and Log Explorer</a></h2>
<p><em>2026-08-20</em></p>
<p><a href="https://radar.cloudflare.com/post-quantum">Cloudflare Radar</a> publishes global statistics on post-quantum key agreement adoption across all Cloudflare traffic, but until now customers had no way to see the same measurement scoped to their own zones. This is now possible because the <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/"><code>http_requests</code></a> Logpush dataset — also queryable in <a href="/log-explorer/">Log Explorer</a> — includes a new <code>ClientTLSKeyExchangeGroup</code> field.</p>
<p>The field reports the TLS key exchange group negotiated on the client-to-Cloudflare connection, by group name. Post-quantum connections appear as <code>X25519MLKEM768</code>, and classical connections appear as <code>X25519</code>, <code>P-256</code>, or another named group. A value of <code>UNK</code> means the group could not be determined, and <code>NONE</code> means TLS was not used.</p>
<p>With this field, you can build per-zone reports showing what percentage of your inbound HTTPS traffic is protected by post-quantum key agreement, break the number down by hostname, path, user agent, or country, and push the data into your SIEM via any <a href="/logs/logpush/logpush-job/enable-destinations/">Logpush destination</a>.</p>


<h2 id="access-resource-lists-now-support-resource-scoped-roles"><a href="/changelog/post/2026-08-19-granular-permissions-resource-lists/">Access resource lists now support resource-scoped roles</a></h2>
<p><em>2026-08-19</em></p>
<p>Members with only resource-scoped Access roles can now open Access resource list pages in the Cloudflare dashboard and call list endpoints in the API. They no longer need an additional account-scoped read-only role to list resources.</p>
<p>The dashboard and API return only resources included in the member's permission policy scopes. Filtering applies to Access applications, policies, service tokens, and identity providers. This allows administrators to delegate specific Access resources without granting account-wide visibility. Previously, the dashboard blocked these list pages and API list requests returned <code>403</code> responses.</p>
<p>For members with the Cloudflare Access App Admin role, policy lists include policies attached directly to the selected application. Reusable policies appear only when the member has the Cloudflare Access Policy Admin role for those policies.</p>
<p>For role definitions and assignment details, refer to <a href="/fundamentals/manage-members/roles/#resource-scoped-roles">Resource-scoped roles</a> and <a href="/fundamentals/manage-members/scope/">Role scopes</a>.</p>


<h2 id="configure-origin-application-settings-for-cloudflare-tunnel-in-the-dashboard"><a href="/changelog/post/2026-08-18-tunnel-origin-settings-dashboard/">Configure origin application settings for Cloudflare Tunnel in the dashboard</a></h2>
<p><em>2026-08-18</em></p>
<p>You can now configure origin application settings directly in the Cloudflare dashboard when adding or editing a published application route for a <a href="/tunnel/">Cloudflare Tunnel</a>. These settings control how <code>cloudflared</code> connects to your origin server and were previously only available in the Cloudflare One dashboard or via local configuration files.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/tunnel-origin-settings-dashboard.gif" alt="Configure origin application settings in the Cloudflare dashboard" /></p>
<p>When editing a published application, expand <strong>Additional application settings</strong> to configure parameters organized into three categories:</p>
<ul>
<li><strong>HTTP</strong> — Set a custom HTTP Host header or disable chunked encoding.</li>
<li><strong>TLS</strong> — Configure origin server name, CA pool, TLS timeout, disable TLS verification, match SNI to host, or enable HTTP/2 to origin.</li>
<li><strong>Connection</strong> — Tune connect timeout, keep-alive timeout, keep-alive connections, TCP keep-alive interval, proxy type, or disable Happy Eyeballs.</li>
</ul>
<div class="nb-dash-button"></div>
<p>For the full list of origin parameters, refer to <a href="/tunnel/reference/origin-parameters/">Origin parameters</a>.</p>


<h2 id="websocket-reporting-now-includes-full-connection-data-transfer-and-duration"><a href="/changelog/post/2026-08-14-websocket-data-transfer-reporting/">WebSocket reporting now includes full connection data transfer and duration</a></h2>
<p><em>2026-08-14</em></p>
<p>Cloudflare has fixed an issue affecting WebSocket data transfer and session duration reporting. HTTP Traffic Analytics and HTTP request logs now correctly report data transferred throughout a WebSocket connection and the duration of the full session. During the affected period, reporting captured only the bytes and duration of the initial <code>101 Switching Protocols</code> handshake for some WebSocket connections.</p>
<p>Customers with WebSocket traffic will see the correct <strong>Data Transfer</strong> in the dashboard and <code>EdgeResponseBytes</code> in analytics and HTTP request logs. Reported session duration now reflects the full WebSocket session rather than only the handshake. These changes restore the accounting of existing WebSocket traffic and duration. They do not indicate an increase in traffic or alter WebSocket connection behavior.</p>
<p>The separate <a href="/logs/logpush/logpush-job/datasets/zone/websocket_analytics/">WebSocket Analytics Logpush dataset</a> continues to provide per-connection directional byte counts, timestamps, and close details.</p>
<p>For more information about HTTP Traffic Analytics, refer to <a href="/analytics/account-and-zone-analytics/zone-analytics/#http-traffic">Zone Analytics</a>.</p>


<h2 id="oracle-cloud-infrastructure-object-storage-support-in-cloud-connector"><a href="/changelog/post/2026-08-13-oci-object-storage-cloud-connector/">Oracle Cloud Infrastructure Object Storage support in Cloud Connector</a></h2>
<p><em>2026-08-13</em></p>
<p>Cloud Connector now supports public Oracle Cloud Infrastructure (OCI) Object Storage buckets. You can route matching requests to OCI without managing a separate origin-routing configuration.</p>
<p>OCI support uses the Amazon S3 Compatibility API. Both path-style and virtual-hosted endpoint formats are supported, including traditional <code>oraclecloud.com</code> and dedicated <code>customer-oci.com</code> path-style endpoints.</p>
<aside class="nb-aside caution">
<h4 class="nb-aside-title" id="2026-08-13-oci-object-storage-cloud-connector-public-buckets-only">Public buckets only</h4>
@markup("md", "content/.markup/bodies/17751.md")</aside>
<h4 id="2026-08-13-oci-object-storage-cloud-connector-api-example">API example</h4>
<p>Set <code>provider</code> to <code>oci_storage</code> and provide a supported OCI hostname. The following rule uses a virtual-hosted endpoint:</p>
<pre><code class="language-json">{&#10;	&quot;expression&quot;: &quot;http.request.uri.path wildcard \&quot;/assets/*\&quot;&quot;,&#10;	&quot;provider&quot;: &quot;oci_storage&quot;,&#10;	&quot;description&quot;: &quot;Route assets to OCI Object Storage&quot;,&#10;	&quot;enabled&quot;: true,&#10;	&quot;parameters&quot;: {&#10;		&quot;host&quot;: &quot;&lt;BUCKET_NAME&gt;.vhcompat.objectstorage.&lt;REGION&gt;.oci.customer-oci.com&quot;&#10;	}&#10;}&#10;</code></pre>
<p>For endpoint formats and bucket requirements, refer to <a href="/rules/cloud-connector/providers/#oracle-cloud-infrastructure-object-storage">Supported cloud providers in Cloud Connector</a>.</p>


<h2 id="new-cloudflare-status-page"><a href="/changelog/post/2026-08-11-new-status-page/">New Cloudflare Status page</a></h2>
<p><em>2026-08-11</em></p>
<p>The Cloudflare Status page at <a href="https://www.cloudflarestatus.com/">www.cloudflarestatus.com</a> has been rebuilt. It is available at the same address, and every previously documented <a href="https://www.cloudflarestatus.com/api">Status API</a> endpoint remains supported, so existing bookmarks, integrations, and monitoring continue to work.</p>
<h4 id="2026-08-11-new-status-page-notifications-that-fire-even-when-cloudflare-is-down">Notifications that fire even when Cloudflare is down</h4>
<p>The status page now has its own notification system, delivered independently of Cloudflare infrastructure. You can subscribe by email, webhook, Slack, Discord, or Google Chat.</p>
<p>The <strong>Maintenance Notification</strong> and <strong>Incident Alerts</strong> in <a href="/notifications/">Cloudflare Notifications</a> remain supported, and deliver to the destinations already configured on your account.</p>
<h4 id="2026-08-11-new-status-page-markdown-for-ai-agents">Markdown for AI agents</h4>
<p>Every page on the status page returns Markdown when requested with an <code>Accept: text/markdown</code> header, so agents can read the current status without parsing HTML:</p>
<pre><code class="language-sh">curl -H &quot;Accept: text/markdown&quot; https://www.cloudflarestatus.com/locations&#10;</code></pre>
<h4 id="2026-08-11-new-status-page-separate-feeds-for-incidents-and-maintenance">Separate feeds for incidents and maintenance</h4>
<p>Incidents and maintenance are published as separate feeds, each available in RSS and Atom, so you can subscribe to one without the other:</p>
<pre><code class="language-txt">https://www.cloudflarestatus.com/api/v3/incidents.rss&#10;https://www.cloudflarestatus.com/api/v3/incidents.atom&#10;https://www.cloudflarestatus.com/api/v3/maintenance.rss&#10;https://www.cloudflarestatus.com/api/v3/maintenance.atom&#10;</code></pre>
<p>For more information, refer to <a href="/support/cloudflare-status/">Cloudflare Status</a>.</p>


<h2 id="hostname-routing-is-now-generally-available-with-a-new-public-ip-range-for-initial-resolved-ips"><a href="/changelog/post/2026-08-11-hostname-routing-ga-public-initial-resolved-ips/">Hostname routing is now generally available, with a new public IP range for initial resolved IPs</a></h2>
<p><em>2026-08-11</em></p>
<p><a href="https://blog.cloudflare.com/tunnel-hostname-routing/">Hostname routing</a> is now generally available. Instead of managing static IP lists and routes, you can route traffic by hostname across multiple Cloudflare One connectors:</p>
<ul>
<li><strong>Cloudflare Tunnel</strong>: route a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">private hostname</a> (for example, <code>wiki.internal.local</code>) to a private application behind your tunnel, or a <a href="/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/">public hostname</a> (for example, <code>bank.example.com</code>) to egress through a specific tunnel and anchor traffic to a dedicated exit node.</li>
<li><strong>Cloudflare Mesh</strong>: attract a <a href="/mesh/features/routes/#hostname-routes">private or public hostname's traffic</a> to a Mesh node.</li>
</ul>
<p>Alongside GA, the default IPv4 range used for <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/17760.md")</div> (also called token IPs) is changing from a Carrier-Grade NAT (CGNAT) range to a public Cloudflare-owned range:
<ul>
<li><strong>IPv4</strong>: <code>172.64.128.0/20</code></li>
<li><strong>IPv6</strong>: <code>2606:4700:0cf1:4000::/64</code></li>
</ul>
<p>This is the default range. You can <a href="/cloudflare-one/networks/routes/configure-initial-resolved-ips/">configure a custom initial resolved IP range</a> for IPv4 if it conflicts with your existing network.</p>
<p><strong>Why this is changing:</strong> Starting with <a href="https://developer.chrome.com/release-notes/142">Chrome 142</a>, Local Network Access (LNA) restrictions block background requests to CGNAT addresses (<code>100.64.0.0/10</code>), which included the previous initial resolved IP default (<code>100.80.0.0/16</code>). LNA is implemented at the Chromium engine level, so it affects all Chromium-based browsers (for example, Microsoft Edge, Brave, and Opera), not only Google Chrome. This could silently break hostname-based Gateway features for users of these browsers, and required Chrome Enterprise policy workarounds. The new default range is public Cloudflare address space, so it is not affected by this restriction.</p>
<p><strong>What is affected:</strong> Initial resolved IPs are used by several features that associate a DNS query with the network connection that follows it:</p>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">Private</a> and <a href="/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/">public</a> hostname routing for Cloudflare Tunnel</li>
<li><a href="/mesh/features/routes/#hostname-routes">Hostname routes</a> for Cloudflare Mesh</li>
<li><a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">Access private applications</a> on non-HTTPS ports</li>
<li><a href="/cloudflare-one/traffic-policies/egress-policies/host-selectors/">Egress policy host selectors</a> (Domain, Host, Application, and Content Categories)</li>
</ul>
<p>You can check your account's current range, or configure a custom range, at any time from <strong>Networking</strong> &gt; <strong>IP addresses</strong> &gt; <strong>Address space</strong> &gt; <strong>Custom IPs</strong>, or using the <a href="/api/resources/zero_trust/subresources/networks/subresources/subnets/#(resource)%20zero_trust.networks.subnets.initial_resolved_ip">Initial Resolved IP Subnet API</a>.</p>
<div class="nb-dash-button"></div>
<p>For full instructions, refer to <a href="/cloudflare-one/networks/routes/configure-initial-resolved-ips/">Configure initial resolved IPs</a>. The IPv6 range (<code>2606:4700:0cf1:4000::/64</code>) is unchanged and is not affected by this restriction.</p>
<p>The default IPv4 range, and all Cloudflare One IPv6 ranges, are automatically routed through the Cloudflare One Client and do not require any Split Tunnel configuration. Refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#automatically-managed-ranges">Automatically managed ranges</a> for details.</p>
<p>If you were relying on a Chrome Enterprise policy workaround (such as <code>LocalNetworkAccessRestrictionsTemporaryOptOut</code>) while your account was still on the legacy CGNAT-based range, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/#google-chrome-restricts-access-to-private-hostnames">Google Chrome restricts access to private hostnames</a> for next steps.</p>


<h2 id="stream-live-logs-from-cloudflare-tunnel-in-the-dashboard"><a href="/changelog/post/2026-08-10-tunnel-live-logs-core-dashboard/">Stream live logs from Cloudflare Tunnel in the dashboard</a></h2>
<p><em>2026-08-10</em></p>
<p>Real-time Tunnel log streaming is now available in the Cloudflare dashboard under <strong>Networking</strong> &gt; <strong>Tunnels</strong>. This brings the same live debugging capability previously only available in the Cloudflare One dashboard, including multi-connector aggregated streaming for high-availability deployments.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/tunnel-live-logs-core-dashboard.gif" alt="Stream live logs from a tunnel in the Cloudflare dashboard" /></p>
<p>In the tunnel detail view, a new <strong>Live logs</strong> tab lets you:</p>
<ul>
<li><strong>Stream logs from single or multiple connectors</strong> — In <a href="/tunnel/configuration/#replicas-and-high-availability">highly available</a> deployments with multiple <code>cloudflared</code> replicas, logs from all connectors are merged into a single stream grouped by hostname, making it easy to identify which host machine produced each log entry.</li>
<li><strong>Filter by log level, event type, and HTTP method</strong> — Narrow the stream to only the events you care about (HTTP, TCP, UDP, or <code>cloudflared</code> internal), at any log level.</li>
</ul>
<div class="nb-dash-button"></div>
<p>For more information, refer to <a href="/tunnel/observability/#remote-log-streaming">Tunnel observability</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">Tunnel log streams</a>.</p>


<h2 id="improved-publisher-verification-details-on-oauth-consent-screens"><a href="/changelog/post/2026-08-04-oauth-consent-shields/">Improved publisher verification details on OAuth consent screens</a></h2>
<p><em>2026-08-05</em></p>
<p>OAuth consent screens now display a shield icon with explanatory text beneath the consent screen title. Each shield icon indicates who owns the application and whether its domain ownership is verified.</p>
<ul>
<li><strong>Green filled shield</strong>: Cloudflare owns and manages the application.</li>
<li><strong>Blue outlined shield</strong>: A third-party application with verified ownership of its domain.</li>
<li><strong>Amber filled shield</strong>: A third-party application without verified ownership of a domain.</li>
</ul>
<p>Domain verification only confirms that the application owner controls the displayed domain.</p>
<p>For more information, refer to <a href="/fundamentals/oauth/authorizing-an-application/">Authorizing an application</a>.</p>


<h2 id="create-free-accounts-from-the-dashboard"><a href="/changelog/post/2026-08-04-free-dashboard-button/">Create Free accounts from the dashboard</a></h2>
<p><em>2026-08-04</em></p>
<p>You can now create standalone Free accounts directly from the Cloudflare dashboard using the new <strong>Create Account</strong> button. This feature is currently available to all users.</p>
<p>When creating a Free account:</p>
<ul>
<li>You can create up to <strong>5 Free accounts</strong>.</li>
<li>Your user account must have at least <strong>7 days of tenure</strong> to be eligible.</li>
<li>The account is created immediately and ready to use.</li>
</ul>
<p>To create a Free account, go to the <a href="https://dash.cloudflare.com/"><strong>Cloudflare dashboard</strong></a> and select <strong>Create Account</strong> from either the account switcher in the top left (where your account name appears) or from the <strong>Accounts</strong> page.</p>
<h4 id="2026-08-04-free-dashboard-button-limitations">Limitations</h4>
* This feature can only be used to create a Cloudflare Free account. To create an Enterprise Account under your existing contract, please contact Cloudflare Support. 
* All users can create a Cloudflare Free account, however, Enterprises wish to restrict this action to only Super Administrators. We will deliver this improvement in a future release. 
<h4 id="2026-08-04-free-dashboard-button-next-steps">Next steps</h4>
<p>After creating your Free account, you can:</p>
<ul>
<li><a href="/billing/get-started/create-billing-profile/">Add a payment method</a> to enable additional Cloudflare products and services.</li>
<li><a href="/billing/get-started/update-billing-info/">Update billing information</a> to manage payment methods, billing address, or tax IDs.</li>
<li><a href="/billing/understand/how-billing-works/">Review how Cloudflare billing works</a> to understand the billing lifecycle and charge types.</li>
<li><a href="/fundamentals/organizations/for-enterprise/">Assign accounts to an Enterprise Organization</a> to centrally manage multiple accounts from a single dashboard.</li>
</ul>


<h2 id="audit-logs-v2-resource-history"><a href="/changelog/post/2026-07-27-audit-logs-v2-resource-history/">Audit Logs v2 — Resource History</a></h2>
<p><em>2026-07-27</em></p>
<p>Audit Logs v2 now includes <strong>Resource History</strong>. For any audit log entry, you can see the sequence of previous changes to the same resource and view a side-by-side diff of what was modified.</p>
<p>Resource History uses the audit log entries you already have. There is no additional configuration, no backend recapture, and no changes to how audit logs are generated.</p>
<p><img src="/assets/upstream/images/changelog/audit-logs/Audit_logs_v2_resource_history.png" alt="Resource History in Audit Logs v2" /></p>
<p><strong>Dashboard:</strong></p>
<ol>
<li>Go to <strong>Manage Account</strong> &gt; <strong>Audit Logs</strong>.</li>
<li>Open any audit log entry.</li>
<li>Select the <strong>History</strong> tab to see the full history for that resource.</li>
<li>Select any earlier entry to see a side-by-side diff of the fields that changed between it and the current entry.</li>
</ol>
<p><strong>API:</strong></p>
<p>Use the History endpoint to retrieve the change history for any audit log entry:</p>
<pre><code class="language-txt">GET https://api.cloudflare.com/client/v4/accounts/{account_id}/logs/audit/{id}/history&#10;</code></pre>
<p>The endpoint is also available for organization-scoped audit logs at <code>/organizations/{organization_id}/logs/audit/{id}/history</code>.</p>
<p>For more information, refer to the <a href="/fundamentals/account/account-security/audit-logs/#resource-history">Resource History documentation</a>.</p>


<h2 id="account-role-api-deprecated"><a href="/changelog/post/2026-07-21-account-role-api-deprecated/">Account Role API deprecated</a></h2>
<p><em>2026-07-21</em></p>
<p>The <a href="/api/resources/accounts/subresources/roles/">Account Roles API</a> is deprecated and is being replaced by the <a href="/api/resources/iam/subresources/permission_groups/">Permission Groups API</a>. An end of life date has not yet been established.</p>
<h4 id="2026-07-21-account-role-api-deprecated-what-you-need-to-do">What you need to do</h4>
<p>Review the <a href="/api/resources/iam/subresources/permission_groups/">Permission Groups API</a> documentation; the response schema differs from the legacy Roles response.</p>
<h4 id="2026-07-21-account-role-api-deprecated-highlights">Highlights</h4>
<ul>
<li>Integrations migrating to the Permission Groups API must obtain Permission Group IDs from that API and use them in the Account Members API policies request shape. Integrations that persist legacy Role IDs will need to remap their assignments.</li>
<li>The legacy <code>Role</code> response includes a top-level <code>description</code> and a <code>permissions</code> object keyed by resource type with edit/read flags.</li>
<li>The <code>PermissionGroup</code> response replaces those with a <code>meta</code> object containing <code>label</code> and <code>scopes</code>. Individual permissions are not returned as part of the permission group.</li>
<li>The new API supports the <a href="/fundamentals/api/get-started/create-token/">API Token</a> authorization scheme. The legacy Email + API Key authorization schema is provided for backwards compatibility.</li>
</ul>
<p>For more information, refer to <a href="/fundamentals/api/reference/deprecations/">API deprecations</a>.</p>


<h2 id="budget-alerts-now-on-by-default-for-pay-as-you-go-accounts"><a href="/changelog/post/2026-06-15-budget-alerts-default-on/">Budget alerts now on by default for Pay-as-you-go accounts</a></h2>
<p><em>2026-07-20</em></p>
<p>We are turning on budget alerts by default for eligible Pay-as-you-go accounts. If your account does not already have a budget alert, Cloudflare will create one for you with a $10 account-level threshold. Your default alert will enable at the turn of your next billing cycle, so it will not fire based on usage you have already incurred.</p>
<p>We are rolling this out in cohorts over the coming weeks, so eligible accounts may see their default alert appear at different times.</p>
<p>The default alert behaves exactly like an alert you would create yourself. When your cumulative usage-based spend this cycle reaches the threshold, you receive an email notification. The alert is informational only. It does not cap your usage or impact your account in any way.</p>
<p>Usage is processed once per day for the prior day's activity, so budget alerts fire the day after the threshold is reached rather than in real time.</p>
<p>Budget alerts only consider spend on usage-based products. Recurring subscription fees, such as the Workers Paid plan fee or other monthly plan charges, are not included in the threshold calculation.</p>
<p>You can change the threshold, add additional alerts, or remove the default alert entirely from <strong>Manage Account</strong> &gt; <strong>Billing</strong> &gt; <strong>Billable Usage</strong>, or from your Notifications settings. If you already configured your own budget alert, nothing changes.</p>
<p>Enterprise contract accounts are not in scope.</p>
<p>For more information, refer to the <a href="/billing/manage/budget-alerts/">Budget alerts documentation</a>.</p>


<h2 id="distributor-mssp-and-agency-partners-can-manage-organization-members-directly"><a href="/changelog/post/2026-07-17-distributor-mssp-self-serve-members/">Distributor, MSSP, and Agency partners can manage Organization members directly</a></h2>
<p><em>2026-07-17</em></p>
<p>Distributor, MSSP, and Agency partners on Cloudflare <a href="/fundamentals/organizations/">Organizations</a> can now add and manage Organization Members directly from the Cloudflare dashboard, without help from Cloudflare.</p>
<p>Previously, adding a member to a Distributor, MSSP, or Agency Organization was a manual, Cloudflare-assisted process that required a request to Cloudflare and enrollment in a closed beta, and the dashboard <strong>Add member</strong> flow was blocked for these Organizations.</p>
<p>Now, Organization admins can add members themselves from <strong>Organization</strong> &gt; <strong>Members</strong> &gt; <strong>Add member</strong>, with no beta enrollment required.</p>
<p>New members receive access to the Organization's accounts through the same implicit-access model already used for enterprise Organizations. The <strong>Accounts</strong> list and the account switcher classify Distributor, MSSP, and Agency Organizations consistently with enterprise Organizations, so their accounts are labeled and grouped correctly in the dashboard.</p>
<p>Agency partners also gain access to the Organizations dashboard, while retaining access to their existing Tenant management dashboard.</p>
<p>Distributor, MSSP, and Agency Organizations are currently in beta.</p>
<p>For more information, refer to <a href="/fundamentals/organizations/manage-members/">Manage Organization members</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><span>Page 1 of 8</span><a class="pagination-next" rel="next" href="/changelog/product-group/core-platform/2/">Next</a></nav>
