<h1 id="changelog">Changelog</h1>

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


<h2 id="per-zone-post-quantum-visibility-in-logpush-and-log-explorer"><a href="/changelog/post/2026-08-20-pqc-key-exchange-visibility/">Per-zone post-quantum visibility in Logpush and Log Explorer</a></h2>
<p><em>2026-08-20</em></p>
<p><a href="https://radar.cloudflare.com/post-quantum">Cloudflare Radar</a> publishes global statistics on post-quantum key agreement adoption across all Cloudflare traffic, but until now customers had no way to see the same measurement scoped to their own zones. This is now possible because the <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/"><code>http_requests</code></a> Logpush dataset — also queryable in <a href="/log-explorer/">Log Explorer</a> — includes a new <code>ClientTLSKeyExchangeGroup</code> field.</p>
<p>The field reports the TLS key exchange group negotiated on the client-to-Cloudflare connection, by group name. Post-quantum connections appear as <code>X25519MLKEM768</code>, and classical connections appear as <code>X25519</code>, <code>P-256</code>, or another named group. A value of <code>UNK</code> means the group could not be determined, and <code>NONE</code> means TLS was not used.</p>
<p>With this field, you can build per-zone reports showing what percentage of your inbound HTTPS traffic is protected by post-quantum key agreement, break the number down by hostname, path, user agent, or country, and push the data into your SIEM via any <a href="/logs/logpush/logpush-job/enable-destinations/">Logpush destination</a>.</p>


<h2 id="custom-dashboards-available-to-all-customers"><a href="/changelog/post/2026-04-22-custom-dashboards-ga/">Custom dashboards available to all customers</a></h2>
<p><em>2026-04-22</em></p>
<p>Custom Dashboards are now available to all Cloudflare customers. Build personalized views that highlight the metrics most critical to your infrastructure and security posture, moving beyond standard product dashboards.</p>
<p>This update significantly expands the data available for visualization. Build charts based on any of the <strong>100+ datasets</strong> available via the Cloudflare GraphQL API, covering everything from WAF events and Workers metrics to Load Balancing and Zero Trust logs.</p>
<h4 id="2026-04-22-custom-dashboards-ga-log-explorer-integration">Log Explorer integration</h4>
<p>Log Explorer customers can select Log Explorer datasets to create charts from raw, unsampled log data.</p>
<h4 id="2026-04-22-custom-dashboards-ga-key-benefits">Key benefits</h4>
<ul>
<li><strong>Unified visibility</strong>: Consolidate signals from different Cloudflare products (for example, HTTP Traffic and R2 Storage) into a single view.</li>
<li><strong>Flexible monitoring</strong>: Create charts that focus on specific status codes, ASN regions, or security actions that matter to your business.</li>
<li><strong>Expanded limits</strong>: Log Explorer customers can create up to <strong>100 dashboards</strong> (up from 25 for standard customers).</li>
</ul>
<p><img src="/assets/upstream/images/analytics/customdashboardshome.jpg" alt="Custom Dashboards home page showing dashboard list and chart previews" /></p>
<p>To get started, refer to the <a href="/analytics/custom-dashboards/">Custom Dashboards documentation</a>.</p>


<h2 id="ingest-field-selection-for-log-explorer"><a href="/changelog/post/2026-03-11-ingest-field-selection/">Ingest field selection for Log Explorer</a></h2>
<p><em>2026-03-11</em></p>
<p>Cloudflare Log Explorer now allows you to customize exactly which data fields are ingested and stored when enabling or managing log datasets.</p>
<p>Previously, ingesting logs often meant taking an &quot;all or nothing&quot; approach to data fields. With <strong>Ingest Field Selection</strong>, you can now choose from a list of available and recommended fields for each dataset. This allows you to reduce noise, focus on the metrics that matter most to your security and performance analysis, and manage your data footprint more effectively.</p>
<h4 id="2026-03-11-ingest-field-selection-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Granular control:</strong> Select only the specific fields you need when enabling a new dataset.</li>
<li><strong>Dynamic updates:</strong> Update fields for existing, already enabled logstreams at any time.</li>
<li><strong>Historical consistency:</strong> Even if you disable a field later, you can still query and receive results for that field for the period it was captured.</li>
<li><strong>Data integrity:</strong> Core fields, such as <code>Timestamp</code>, are automatically retained to ensure your logs remain searchable and chronologically accurate.</li>
</ul>
<h4 id="2026-03-11-ingest-field-selection-example-configuration">Example configuration</h4>
<p>When configuring a dataset via the dashboard or API, you can define a specific set of fields. The <code>Timestamp</code> field remains mandatory to ensure data indexability.</p>
<pre><code class="language-json">{&#10;  &quot;dataset&quot;: &quot;firewall_events&quot;,&#10;  &quot;enabled&quot;: true,&#10;  &quot;fields&quot;: [&#10;    &quot;Timestamp&quot;,&#10;    &quot;ClientRequestHost&quot;,&#10;    &quot;ClientIP&quot;,&#10;    &quot;Action&quot;,&#10;    &quot;EdgeResponseStatus&quot;,&#10;    &quot;OriginResponseStatus&quot;&#10;  ]&#10;}&#10;</code></pre>
<p>For more information, refer to the <a href="/log-explorer/">Log Explorer documentation</a>.</p>


<h2 id="tabs-and-pivots"><a href="/changelog/post/2026-02-09-tabs-and-pivots/">Tabs and pivots</a></h2>
<p><em>2026-02-09</em></p>
<p>Log Explorer now supports multiple concurrent queries with the new Tabs feature. Work with multiple queries simultaneously and pivot between datasets to investigate malicious activity more effectively.</p>
<h4 id="2026-02-09-tabs-and-pivots-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Multiple tabs:</strong> Open and switch between multiple query tabs to compare results across different datasets.</li>
<li><strong>Quick filtering:</strong> Select the filter button from query results to add a value as a filter to your current query.</li>
<li><strong>Pivot to new tab:</strong> Use Cmd + click on the filter button to start a new query tab with that filter applied.</li>
<li><strong>Preserved progress:</strong> Your query progress is preserved on each tab if you navigate away and return.</li>
</ul>
<p>For more information, refer to the <a href="/log-explorer/">Log Explorer documentation</a>.</p>


<h2 id="fixed-custom-sql-date-picker-inconsistencies"><a href="/changelog/post/2025-11-13-fixed-custom-date/">Fixed custom SQL date picker inconsistencies</a></h2>
<p><em>2025-11-13</em></p>
<p>We've resolved a bug in Log Explorer that caused inconsistencies between the custom SQL date field filters and the date picker dropdown. Previously, users attempting to filter logs based on a custom date field via a SQL query sometimes encountered unexpected results or mismatching dates when using the interactive date picker.</p>
<p>This fix ensures that the custom SQL date field filters now align correctly with the selection made in the date picker dropdown, providing a reliable and predictable filtering experience for your log data. This is particularly important for users creating custom log views based on time-sensitive fields.</p>


<h2 id="log-explorer-adds-14-new-datasets"><a href="/changelog/post/2025-11-13-new-datasets/">Log Explorer adds 14 new datasets</a></h2>
<p><em>2025-11-13</em></p>
<p>We've significantly enhanced Log Explorer by adding support for 14 additional Cloudflare product datasets.</p>
<p>This expansion enables Operations and Security Engineers to gain deeper visibility and telemetry across a wider range of Cloudflare services. By integrating these new datasets, users can now access full context to efficiently investigate security incidents, troubleshoot application performance issues, and correlate logged events across different layers (like application and network) within a single interface. This capability is crucial for a complete and cohesive understanding of event flows across your Cloudflare environment.</p>
<p>The newly supported datasets include:</p>
<h4 id="2025-11-13-new-datasets-zone-level">Zone Level</h4>
<ul>
<li><code>Dns_logs</code></li>
<li><code>Nel_reports</code></li>
<li><code>Page_shield_events</code></li>
<li><code>Spectrum_events</code></li>
<li><code>Zaraz_events</code></li>
</ul>
<h4 id="2025-11-13-new-datasets-account-level">Account Level</h4>
<ul>
<li><code>Audit Logs</code></li>
<li><code>Audit_logs_v2</code></li>
<li><code>Biso_user_actions</code></li>
<li><code>DNS firewall logs</code></li>
<li><code>Email_security_alerts</code></li>
<li><code>Magic Firewall IDS</code></li>
<li><code>Network Analytics</code></li>
<li><code>Sinkhole HTTP</code></li>
<li><code>ipsec_logs</code></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17736.md")</aside>
<h4 id="2025-11-13-new-datasets-example-correlating-logs">Example: Correlating logs</h4>
<p>You can now use Log Explorer to query and filter with each of these datasets. For example, you can identify an IP address exhibiting suspicious behavior in the <code>FW_event</code> logs, and then instantly pivot to the <code>Network Analytics</code> logs or <code>Access</code> logs to see its network-level traffic profile or if it bypassed a corporate policy.</p>
<p>To learn more and get started, refer to the <a href="/log-explorer/">Log Explorer documentation</a> and the <a href="/logs/">Cloudflare Logs documentation</a>.</p>


<h2 id="resize-your-custom-sql-window-in-log-explorer"><a href="/changelog/post/2025-11-11-resize-sql-window/">Resize your custom SQL window in Log Explorer</a></h2>
<p><em>2025-11-11</em></p>
<p>We're excited to announce a quality-of-life improvement for Log Explorer users. You can now resize the custom SQL query window to accommodate longer and more complex queries.</p>
<p>Previously, if you were writing a long custom SQL query, the fixed-size window required excessive scrolling to view the full query. This update allows you to easily drag the bottom edge of the query window to make it taller. This means you can view your entire custom query at once, improving the efficiency and experience of writing and debugging complex queries.</p>
<p>To learn more and get started, refer to the <a href="/log-explorer/">Log Explorer documentation</a>.</p>


<h2 id="log-explorer-now-supports-query-cancellation"><a href="/changelog/post/2025-11-04-query-cancellation/">Log Explorer now supports query cancellation</a></h2>
<p><em>2025-11-04</em></p>
<p>We're excited to announce that Log Explorer users can now cancel queries that are currently running.</p>
<p>This new feature addresses a common pain point: waiting for a long, unintended, or misconfigured query to complete before you can submit a new, correct one. With query cancellation, you can immediately stop the execution of any undesirable query, allowing you to quickly craft and submit a new query, significantly improving your investigative workflow and productivity within Log Explorer.</p>


<h2 id="log-explorer-now-shows-query-result-distribution"><a href="/changelog/post/2025-11-13-query-result-distribution/">Log Explorer now shows query result distribution</a></h2>
<p><em>2025-11-04</em></p>
<p>We're excited to announce a new feature in Log Explorer that significantly enhances how you analyze query results: the Query results distribution chart.</p>
<p>This new chart provides a graphical distribution of your results over the time window of the query. Immediately after running a query, you will see the distribution chart above your result table. This visualization allows Log Explorer users to quickly spot trends, identify anomalies, and understand the temporal concentration of log events that match their criteria. For example, you can visually confirm if a spike in traffic or errors occurred at a specific time, allowing you to focus your investigation efforts more effectively. This feature makes it faster and easier to extract meaningful insights from your vast log data.</p>
<p>The chart will dynamically update to reflect the logs matching your current query.</p>


<h2 id="contextual-pivots"><a href="/changelog/post/2025-09-11-contextual-pivots/">Contextual pivots</a></h2>
<p><em>2025-09-11</em></p>
<p>Directly from <a href="/log-explorer/log-search/">Log Search</a> results, customers can pivot to other parts of the Cloudflare dashboard to immediately take action as a result of their investigation.</p>
<p>From the <code>http_requests</code> or <code>fw_events</code> dataset results, right click on an IP Address or JA3 Fingerprint to pivot to the Investigate portal to lookup the reputation of an IP address or JA3 fingerprint.</p>
<p><img src="/assets/upstream/images/changelog/log-explorer/investigate-ip-address.png" alt="Investigate IP address" /></p>
<p>Easily learn about error codes by linking directly to our documentation from the <strong>EdgeResponseStatus</strong> or <strong>OriginResponseStatus</strong> fields.</p>
<p><img src="/assets/upstream/images/changelog/log-explorer/view-documentation.png" alt="View documentation" /></p>
<p>From the <code>gateway_http</code> dataset, click on a <strong>policyid</strong> to link directly to the Zero Trust dashboard to review or make changes to a specific Gateway policy.</p>
<p><img src="/assets/upstream/images/changelog/log-explorer/policyid.png" alt="View policy" /></p>


<h2 id="new-results-table-view"><a href="/changelog/post/2025-09-11-new-results-table-view/">New results table view</a></h2>
<p><em>2025-09-11</em></p>
<p>The results table view of <strong>Log Search</strong> has been updated with additional functionality and a more streamlined user experience. Users can now easily:</p>
<ul>
<li>Remove/add columns.</li>
<li>Resize columns.</li>
<li>Sort columns.</li>
<li>Copy values from any field.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/log-explorer/new-table.png" alt="New results table view" /></p>


<h2 id="logging-headers-and-cookies-using-custom-fields"><a href="/changelog/post/2025-09-03-log-headers-and-cookies/">Logging headers and cookies using custom fields</a></h2>
<p><em>2025-09-03</em></p>
<p><a href="/log-explorer/">Log Explorer</a> now supports logging and filtering on header or cookie fields in the <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/"><code>http_requests</code> dataset</a>.</p>
<p>Create a custom field to log desired header or cookie values into the <code>http_requests</code> dataset and Log Explorer will import these as searchable fields. Once configured, use the custom SQL editor in Log Explorer to view or filter on these requests.</p>
<p><img src="/assets/upstream/images/changelog/log-explorer/edit-custom-fields.png" alt="Edit Custom fields" /></p>
<p>For more details, refer to <a href="/log-explorer/log-search/#headers-and-cookies">Headers and cookies</a>.</p>


<h2 id="extended-retention"><a href="/changelog/post/2025-08-15-extended-retention/">Extended retention</a></h2>
<p><em>2025-08-15</em></p>
<p>Customers can now rely on Log Explorer to meet their log retention compliance requirements.</p>
<p>Contract customers can choose to store their logs in Log Explorer for up to two years, at an additional cost of $0.10 per GB per month. Customers interested in this feature can contact their account team to have it added to their contract.</p>


<h2 id="usage-tracking"><a href="/changelog/post/2025-07-09-usage-tracking/">Usage tracking</a></h2>
<p><em>2025-07-09</em></p>
<p><a href="/log-explorer/">Log Explorer</a> customers can now monitor their data ingestion volume to keep track of their billing. Monthly usage is displayed at the top of the <a href="/log-explorer/log-search/">Log Search</a> and <a href="/log-explorer/manage-datasets/">Manage Datasets</a> screens in Log Explorer.</p>
<p><img src="/assets/upstream/images/changelog/log-explorer/ingested-data.png" alt="Ingested data" /></p>


<h2 id="log-explorer-is-ga"><a href="/changelog/post/2025-06-18-log-explorer-ga/">Log Explorer is GA</a></h2>
<p><em>2025-06-18</em></p>
<p><a href="/log-explorer/">Log Explorer</a> is now GA, providing native observability and forensics for traffic flowing through Cloudflare.</p>
<p>Search and analyze your logs, natively in the Cloudflare dashboard. These logs are also stored in Cloudflare's network, eliminating many of the costs associated with other log providers.</p>
<p><img src="/assets/upstream/images/changelog/log-explorer/log-explorer-dash.png" alt="Log Explorer dashboard" /></p>
<p>With Log Explorer, you can now:</p>
<ul>
<li><strong>Monitor security and performance issues with custom dashboards</strong> – use natural language to define charts for measuring response time, error rates, top statistics and more.</li>
<li><strong>Investigate and troubleshoot issues with Log Search</strong> – use data type-aware search filters or custom sql to investigate detailed logs.</li>
<li><strong>Save time and collaborate with saved queries</strong> – save Log Search queries for repeated use or sharing with other users in your account.</li>
<li><strong>Access Log Explorer at the account and zone level</strong> – easily find Log Explorer at the account and zone level for querying any dataset.</li>
</ul>
<p>For help getting started, refer to <a href="/log-explorer/">our documentation</a>.</p>



