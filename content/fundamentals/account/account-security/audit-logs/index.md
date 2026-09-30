---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/
  description: Use Cloudflare Audit Logs v2 to track user-initiated and system-initiated actions across your account via the dashboard, API, or Logpush.
  full_title: Audit Logs - version 2 · Cloudflare Fundamentals docs
  head_html: <title>Audit Logs - version 2 · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Use Cloudflare Audit Logs v2 to track user-initiated and system-initiated actions across your account via the dashboard, API, or Logpush."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/index.md"><meta property="og:title" content="Audit Logs - version 2 · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Use Cloudflare Audit Logs v2 to track user-initiated and system-initiated actions across your account via the dashboard, API, or Logpush."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Fundamentals,Audit Logs"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/#page","headline":"Audit Logs - version 2 \u00b7 Cloudflare Fundamentals docs","description":"Use Cloudflare Audit Logs v2 to track user-initiated and system-initiated actions across your account via the dashboard, API, or Logpush.","url":"https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/account/account-security/audit-logs/
  schema: 1
---
<p>Cloudflare Audit Logs are account-based. All user-initiated actions are recorded automatically across both the Cloudflare API and dashboard. System-initiated logs are also captured to reflect actions taken automatically by Cloudflare systems, such as configuration updates, background processes, or internal policy enforcement.</p>
<p>When a user-initiated action triggers additional automated behavior, corresponding system-initiated logs will be generated. In some cases, user-initiated logs include additional enrichments that provide more context about what was changed, offering deeper visibility into the full lifecycle of the action.</p>
<p>When an action occurs, it is streamed through Cloudflare's audit logging pipeline and stored. This ensures consistent visibility into activity across all products.</p>
<p>For more detailed information about how the user-initiated actions are logged automatically, refer to the <a href="https://blog.cloudflare.com/introducing-automatic-audit-logs/">Cloudflare Blog</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8954.md")
</aside>
<h2 id="key-features">Key features</h2>
<p>Audit Logs (version 2) provide a unified and standardized system for tracking and recording actions across Cloudflare products. This system enhances transparency and accountability by offering comprehensive insights into user-initiated and system-initiated activities within your Cloudflare environment.</p>
<ul>
<li><strong>Standardized logging</strong>: Audit logs are automatically generated in a consistent format across all Cloudflare services, ensuring uniformity and eliminating inconsistencies.</li>
<li><strong>Expanded product coverage</strong>: Audit Logs covers ~95% of Cloudflare products, capturing actions from key endpoints, such as <code>/accounts</code>, <code>/zones</code>, <code>/user</code>, and <code>/memberships</code> APIs.</li>
<li><strong>Granular filtering</strong>: Uniformly formatted logs allow for precise filtering by actions, actors, methods, and resources, facilitating efficient investigations.</li>
<li><strong>Enhanced context and transparency</strong>: Each log entry includes detailed context, such as the authentication method used, the interface (API or dashboard) through which the action was performed, and mappings to Cloudflare Ray IDs for improved traceability.</li>
<li><strong>Comprehensive activity capture</strong>: Audit Logs records create, update, and delete actions across all supported products. Selective logging of <code>GET</code> requests for sensitive read operations is planned for a future release.</li>
</ul>
<h2 id="retention">Retention</h2>
<ul>
<li>
<p>Audit logs are retained for 18 months before being deleted. No additional setup is required.</p>
</li>
<li>
<p>In the Audit Logs v2 UI, queries are limited to the most recent 90 days for performance reasons. To access the full 18 months of data, use the API or <a href="/logs/logpush/">Logpush</a>.</p>
</li>
<li>
<p>Enterprise customers can use <a href="/logs/logpush/">Logpush</a> to store audit logs beyond 18 months.</p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8953.md")
</aside>
<h2 id="customer-metadata-boundary">Customer Metadata Boundary</h2>
<p>Audit Logs v2 supports <a href="/data-localization/metadata-boundary/">Customer Metadata Boundary (CMB)</a>. The account-level CMB preference automatically applies to Audit Logs v2. For example, if you select <code>eu</code>, Audit Logs v2 uses the EU metadata boundary. You do not need to configure Audit Logs separately.</p>
<p>To configure CMB in the Cloudflare dashboard or via the <code>/accounts/{account_id}/logs/control/cmb/config</code> API, refer to <a href="/data-localization/metadata-boundary/get-started/">Get started with Customer Metadata Boundary</a>. CMB is part of the Data Localization Suite. Contact your account team if CMB is not enabled for your account.</p>
<h2 id="access-audit-logs">Access Audit Logs</h2>
<p>You can retrieve audit logs using the Cloudflare dashboard, the API, or Logpush.</p>
<h3 id="api">API</h3>
<p>Audit Logs are available through the Cloudflare API. To retrieve audit logs, use the following endpoint:</p>
<pre tabindex="0"><code class="language-bash">https://api.cloudflare.com/client/v4/accounts/{account_id}/logs/audit&#10;</code></pre>
<p>Below is an example request to retrieve audit logs for a certain period of time along with its corresponding response. Replace the example values in the URL with your actual values:</p>
<ul>
<li><code>account_id</code>: Your Cloudflare account identifier.</li>
<li><code>since</code> (required): Start date for the audit log retrieval. Accepts <code>yyyy-mm-dd</code> (interpreted as UTC) or RFC3339 timestamp (<code>yyyy-mm-ddTHH:MM:SSZ</code>).</li>
<li><code>before</code> (required): End date for the audit log retrieval. Same format as <code>since</code>.</li>
</ul>
<pre tabindex="0"><code class="language-bash">GET https://api.cloudflare.com/client/v4/accounts/1234567890abcdef/logs/audit?since=2025-03-01T00:00:00Z&amp;before=2025-03-26T23:59:59Z&#10;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;action&quot;: &quot;zone.settings.change&quot;,&#10;			&quot;actor&quot;: {&#10;				&quot;email&quot;: &quot;user@example.com&quot;,&#10;				&quot;id&quot;: &quot;0987654321abcdef&quot;&#10;			},&#10;			&quot;ip&quot;: &quot;192.0.2.1&quot;,&#10;			&quot;method&quot;: &quot;PUT&quot;,&#10;			&quot;interface&quot;: &quot;dashboard&quot;,&#10;			&quot;resources&quot;: [&#10;				{&#10;					&quot;resource_id&quot;: &quot;zone123&quot;,&#10;					&quot;resource_type&quot;: &quot;zone&quot;&#10;				}&#10;			],&#10;			&quot;timestamp&quot;: &quot;2025-03-15T14:25:37Z&quot;&#10;		}&#10;		// Additional log entries&#10;	],&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>For more information refer to the <a href="https://developers.cloudflare.com/api/resources/accounts/subresources/logs/subresources/audit/methods/list/#(params)%20default%20%3E%20(param)%20since%20%3E%20(schema)">API documentation</a>.</p>
<h3 id="dashboard">Dashboard</h3>
<p>To access audit logs in the Cloudflare dashboard, go to <strong>Manage Account</strong> &gt; <strong>Audit Logs</strong>.</p>
<div class="nb-dash-button"></div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8952.md")
</aside>
<h4 id="account-analytics">Account analytics</h4>
<p>The account-level Audit Logs v2 dashboard includes analytics for the selected time range. The <strong>Actions over time</strong> chart separates successful and failed actions. The summary cards show <strong>Total actions</strong>, <strong>Unique actors</strong>, <strong>Products impacted</strong>, and <strong>Failure rate</strong>.</p>
<p>Select a summary card to view more details:</p>
<ul>
<li><strong>Total actions</strong>: Action types and authentication methods</li>
<li><strong>Unique actors</strong>: Actors with the most actions</li>
<li><strong>Products impacted</strong>: Products with the most actions</li>
<li><strong>Failure rate</strong>: Failed actions and their HTTP status codes</li>
</ul>
<p>To focus the analytics and audit log table on a value, select <strong>Filter</strong> or <strong>Exclude</strong> from a detail panel. The analytics, table, filters, and time range remain synchronized.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8951.md")
</aside>
<h3 id="logpush">Logpush</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8950.md")
</aside>
<p>To create a Logpush job:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Logpush</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create a Logpush job</strong>.</li>
<li>In <strong>Select a destination</strong>, select the destination of your choice and add the destination details.</li>
<li>In the datasets section, select the <a href="/logs/logpush/logpush-job/datasets/account/audit_logs_v2/">Audit Logs v2 dataset</a>. Audit Logs v2 is an account-based dataset.</li>
<li>Once you are done configuring your logpush job, select <strong>Submit</strong>.</li>
</ol>
<h2 id="resource-history">Resource History</h2>
<p>Resource History shows what changed on every configuration modification captured in Audit Logs. For any audit log entry, you can see the sequence of previous changes to the same resource and view a side-by-side diff of what was modified.</p>
<p>Resource History is available in the Cloudflare dashboard and via the Audit Logs API. It uses the audit log entries you already have. There is no additional configuration, no backend recapture, and no changes to how audit logs are generated.</p>
<h3 id="what-resource-history-gives-you">What Resource History gives you</h3>
<p>For any audit log entry, Resource History retrieves every other audit log entry for the same resource, ordered chronologically. You can then pick an earlier entry from that history to see exactly which fields changed between the two.</p>
<h3 id="use-resource-history-in-the-dashboard">Use Resource History in the dashboard</h3>
<ol>
<li>Go to <strong>Manage Account</strong> &gt; <strong>Audit Logs</strong>.</li>
<li>Open any audit log entry.</li>
<li>Select the <strong>History</strong> tab to see the full history for the resource that entry describes.</li>
<li>In the history view, select any earlier entry to see a side-by-side diff of the fields that changed between it and the current entry.</li>
</ol>
<p>When Resource History cannot identify the underlying resource (for example, for certain system-initiated events), the dashboard shows an empty state indicating that change history is not available for that entry.</p>
<h3 id="use-resource-history-via-the-api">Use Resource History via the API</h3>
<p>You can retrieve the change history for any audit log entry using the History endpoint. Given the <code>id</code> of a source audit log entry, the endpoint derives identifying filters from that entry and returns matching audit log entries within a date window you specify.</p>
<p>For account-scoped audit logs, use:</p>
<pre tabindex="0"><code class="language-bash">GET https://api.cloudflare.com/client/v4/accounts/{account_id}/logs/audit/{id}/history&#10;</code></pre>
<p>For organization-scoped audit logs, use:</p>
<pre tabindex="0"><code class="language-bash">GET https://api.cloudflare.com/client/v4/organizations/{organization_id}/logs/audit/{id}/history&#10;</code></pre>
<p>The <code>{id}</code> path parameter is the <code>id</code> of the source audit log entry whose resource history you want to retrieve.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="required-api-token-permissions">Required API token permissions</h3>
@markup("md", "content/.markup/bodies/8949.md")
</aside>
<p>The endpoint requires three query parameters:</p>
<ul>
<li><code>action_time</code> (required): RFC3339 timestamp of the source audit log entry's action time. Provide the <code>action.time</code> value from the audit log identified by <code>{id}</code>. This narrows the source-entry lookup window.</li>
<li><code>since</code> (required): Limits returned results to entries newer than this date. Accepts a date string (<code>2024-10-30</code>, interpreted as UTC) or an RFC3339 timestamp.</li>
<li><code>before</code> (required): Limits returned results to entries older than this date. Same format as <code>since</code>.</li>
</ul>
<p>Optional query parameters:</p>
<ul>
<li><code>direction</code>: <code>desc</code> (default) or <code>asc</code>.</li>
<li><code>limit</code>: Number of entries to return per page. Default <code>100</code>.</li>
<li><code>cursor</code>: Pagination cursor from a previous response's <code>result_info.cursor</code>.</li>
</ul>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/logs/audit/{id}/history \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<p>Each entry in <code>result</code> has the same shape as an entry returned by the Audit Logs list endpoint. Results are paginated using the <code>cursor</code> value in <code>result_info</code>.</p>
<p>The <code>result_info.history_status</code> field indicates the quality of resource identification used to build the history:</p>
<ul>
<li><code>exact</code>: The source entry contained a resource URI, so the history was built from an exact resource match.</li>
<li><code>approximate</code>: The source entry did not contain a resource URI, so the history was built from an approximate match (other resources of the same product and type). The dashboard surfaces this state with a warning banner.</li>
<li><code>unavailable</code>: The source entry did not contain enough information to identify the resource. <code>result</code> is empty. This can happen for certain system-initiated events.</li>
</ul>
<p>Resource History reflects the audit log entries currently retained by Audit Logs v2 (refer to <a href="#retention">Retention</a>). Entries older than the retention window are not returned. Resource History is a query-time capability and is not exposed as additional fields in the <code>audit_logs_v2</code> Logpush dataset.</p>
<h2 id="audit-log-structure">Audit Log structure</h2>
<p>Cloudflare's audit logs offer a detailed view of activity across your environment by capturing both the source of actions and the context in which they occur. These logs are categorized by who initiated the action (user or system) and whether the activity occurred within a specific account or spanned multiple accounts under the same user profile. This structure enables flexible filtering, investigation, and compliance monitoring.</p>
<h3 id="initiation-type">Initiation type</h3>
<p>Audit logs can be initiated either by users or the system. Understanding the type of actor involved helps in identifying the source and intent of actions.</p>
<h4 id="user-initiated-audit-logs">User initiated Audit Logs</h4>
<p>Track actions initiated by users through Cloudflare interfaces, including the dashboard and API. These logs capture who or what performed the action. They also record when it occurred and which resource was affected. User-initiated actions can have four actor types:</p>
<ul>
<li><code>actor_type=&quot;user&quot;</code>: Action was performed by an individual user.</li>
<li><code>actor_type=&quot;cloudflare_admin&quot;</code>: Action was performed by Cloudflare.</li>
<li><code>actor_type=&quot;account&quot;</code>: Action was performed using an account API token. Refer to the <a href="/fundamentals/api/get-started/account-owned-tokens/">Account API tokens</a> documentation for more information.</li>
<li><code>actor_type=&quot;delegated_service&quot;</code>: Action was performed by a Cloudflare service acting on a user's behalf. The log does not identify the initiating user.</li>
</ul>
<h4 id="system-initiated-audit-logs">System initiated Audit Logs</h4>
<p>Record changes made automatically by Cloudflare systems, without direct user input. These logs provide visibility into internal processes, automated tasks, and security events. Some entries may include associated user context for traceability (<code>actor_type=&quot;system&quot;</code>).</p>
<h3 id="activity-scope">Activity Scope</h3>
<h4 id="account-activity-logs">Account Activity Logs</h4>
<p>Contain events scoped to a single Cloudflare account. These logs are filterable by <code>account ID</code> and reflect actions within that account only. You can optionally filter events further using the <code>resource_scope</code> field, which specifies whether the resource is associated with a user, an account, or a zone (<code>resource_scope =&quot;user&quot;</code>, <code>resource_scope =&quot;accounts&quot;</code>, or <code>resource_scope =&quot;zones&quot;</code>).</p>
<h4 id="user-profile-activity-logs">User Profile Activity Logs</h4>
<p>Reflect actions associated with a user's login (email) across multiple accounts. These logs enable cross-account tracking and can be filtered by <code>user ID</code> or <code>email</code>. They are visible on any account the user had access to at the time of the activity. User Profile Activity Logs can be filtered using <code>resource_scope =&quot;user&quot;</code>.</p>
<p>The <code>GET /memberships</code> endpoint supports cross-account access. To query memberships, use the parameter <code>resource_scope=memberships</code>.</p>
<h4 id="organization-activity-logs">Organization Activity Logs</h4>
<p>Contain events scoped to specific <a href="/fundamentals/organizations/">Cloudflare Organizations</a>. These logs capture user-initiated actions performed by Org Admins through organization-level APIs.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8948.md")
</aside>
<p>You can retrieve Organization audit logs using either the API or the Cloudflare dashboard.</p>
<h5 id="api-access">API access</h5>
<p>Retrievable via the Audit Logs v2 API:</p>
<pre tabindex="0"><code class="language-bash">GET https://api.cloudflare.com/client/v4/organizations/{organization_id}/logs/audit&#10;</code></pre>
<h5 id="dashboard-access">Dashboard access</h5>
<p>To access organization audit logs in the Cloudflare dashboard, go to <strong>Organizations</strong> &gt; <em>(select your organization)</em> &gt; <strong>Manage Organization</strong> &gt; <strong>Audit Logs</strong>.</p>
<p>If you are viewing account-level audit logs and the account belongs to an organization where you are an Organization Super Administrator, you can navigate to the parent organization's audit logs using the <strong>View Organization Audit Logs</strong> button.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8947.md")
</aside>
<h2 id="example-how-to-query-audit-logs">Example how to query Audit Logs</h2>
<p>Use the following example to get a list of audit logs for a Cloudflare account.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/logs/audit \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;errors&quot;: [&#10;		{&#10;			&quot;message&quot;: &quot;message&quot;&#10;		}&#10;	],&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;account&quot;: {&#10;				&quot;id&quot;: &quot;4bb334f7c94c4a29a045f03944f072e5&quot;,&#10;				&quot;name&quot;: &quot;Example Account&quot;&#10;			},&#10;			&quot;action&quot;: {&#10;				&quot;description&quot;: &quot;Add Member&quot;,&#10;				&quot;result&quot;: &quot;success&quot;,&#10;				&quot;time&quot;: &quot;2024-04-26T17:31:07Z&quot;,&#10;				&quot;type&quot;: &quot;create&quot;&#10;			},&#10;			&quot;actor&quot;: {&#10;				&quot;id&quot;: &quot;f6b5de0326bb5182b8a4840ee01ec774&quot;,&#10;				&quot;context&quot;: &quot;dash&quot;,&#10;				&quot;email&quot;: &quot;alice@example.com&quot;,&#10;				&quot;ip_address&quot;: &quot;198.41.129.166&quot;,&#10;				&quot;token_id&quot;: &quot;token_id&quot;,&#10;				&quot;token_name&quot;: &quot;token_name&quot;,&#10;				&quot;type&quot;: &quot;user&quot;&#10;			},&#10;			&quot;raw&quot;: {&#10;				&quot;cf_ray_id&quot;: &quot;8e9b1c60ef9e1c9a&quot;,&#10;				&quot;method&quot;: &quot;POST&quot;,&#10;				&quot;status_code&quot;: 200,&#10;				&quot;uri&quot;: &quot;/accounts/4bb334f7c94c4a29a045f03944f072e5/members&quot;,&#10;				&quot;user_agent&quot;: &quot;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/605.1.15&quot;&#10;			},&#10;			&quot;resource&quot;: {&#10;				&quot;id&quot;: &quot;id&quot;,&#10;				&quot;product&quot;: &quot;members&quot;,&#10;				&quot;request&quot;: {},&#10;				&quot;response&quot;: {},&#10;				&quot;scope&quot;: {},&#10;				&quot;type&quot;: &quot;type&quot;&#10;			},&#10;			&quot;zone&quot;: {&#10;				&quot;id&quot;: &quot;id&quot;,&#10;				&quot;name&quot;: &quot;example.com&quot;&#10;			}&#10;		}&#10;	],&#10;	&quot;result_info&quot;: {&#10;		&quot;count&quot;: &quot;1&quot;,&#10;		&quot;cursor&quot;: &quot;ASqdKd7dKgxh-aZ8bm0mZos1BtW4BdEqifCzNkEeGRzi_5SN_-362Y8sF-C1TRn60_6rd3z2dIajf9EAPyQ_NmIeAMkacmaJPXipqvP7PLU4t72wyqBeJfjmjdE=&quot;&#10;	},&#10;	&quot;success&quot;: true&#10;}&#10;</code></pre>
<h2 id="common-terms-and-definitions">Common terms and definitions</h2>
<h3 id="actor">Actor</h3>
<p>The actor represents who or what performed the action. Its identity attributes depend on the actor type. These attributes can include a user ID, email address, and IP address. Actor types include <code>user</code>, <code>account</code>, <code>cloudflare_admin</code>, <code>delegated_service</code>, or <code>system</code>. An actor can also include the context used to initiate the action:</p>
<ul>
<li><code>api</code>: The action was performed through the API. The specific credential type was not recorded.</li>
<li><code>api_key</code>: The action was authenticated with a Cloudflare Global API Key.</li>
<li><code>api_token</code>: The action was authenticated with an API token.</li>
<li><code>dash</code>: The action was performed through the Cloudflare dashboard.</li>
<li><code>oauth</code>: The action was authenticated with an OAuth token.</li>
<li><code>origin_ca_key</code>: The action was authenticated with an Origin CA key.</li>
</ul>
<h3 id="action">Action</h3>
<p>The action field captures the nature of the event and whether it was successful. It includes a high-level type (e.g., <code>create</code>, <code>update</code>, <code>delete</code>), a specific description (such as <code>SSO_LOGIN</code>), the timestamp of when the action occurred, and the result (<code>success</code> or <code>failure</code>).</p>
<p><code>view</code> actions correspond to <code>GET</code> requests. These are defined in the schema but not currently captured in Audit Logs. Selective <code>GET</code> logging for sensitive read operations is planned for a future release.</p>
<h3 id="account">Account</h3>
<p>This field refers to the Cloudflare account under which the action was executed. It includes a unique account ID and a human-readable account name to help associate activity with a customer environment.</p>
<h3 id="resource">Resource</h3>
<p>The resource identifies the object impacted by the action. It includes the resource type, the unique resource ID, the scope (<code>user</code>, <code>account</code>, or <code>zone</code>), and optionally the product associated with the change.</p>
<h3 id="audit-log-id">Audit Log ID</h3>
<p>This is a unique identifier for the log record itself. It can be used for deduplication, correlation, or referencing specific actions during investigations.</p>
