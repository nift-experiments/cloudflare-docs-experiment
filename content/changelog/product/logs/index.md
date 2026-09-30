<h1 id="changelog">Changelog</h1>

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


<h2 id="new-websocket-analytics-logpush-dataset"><a href="/changelog/post/2026-07-07-websocket-analytics-dataset/">New WebSocket Analytics Logpush dataset</a></h2>
<p><em>2026-07-07</em></p>
<p>Enterprise customers can now push per-connection WebSocket analytics to any <a href="/logs/logpush/logpush-job/enable-destinations/">Logpush destination</a> using the new <code>websocket_analytics</code> dataset. Each log record is emitted when a WebSocket connection closes and includes fields that were previously only available to Cloudflare engineers via internal tooling.</p>
<p>Key fields include:</p>
<ul>
<li><strong><code>ConnectionCloseReason</code></strong> — why the connection ended: <code>peerReset</code>, <code>peerNoError</code>, <code>timedOut</code>, <code>upstreamReset</code>, <code>protocolViolation</code>, <code>unspecifiedError</code>, or <code>none</code>.</li>
<li><strong><code>ConnectionCloseSource</code></strong> — which side initiated the close: <code>upstream</code>, <code>downstream</code>, <code>me</code>, or <code>both</code>.</li>
<li><strong><code>ConnectionTransportCloseCode</code></strong> — the TLS alert code or TCP-level close code for additional precision.</li>
<li><strong><code>RayID</code></strong> — correlate WebSocket connection events with your existing HTTP Request logs.</li>
</ul>
<p>The dataset also includes directional byte counts (<code>BytesSentClient</code>, <code>BytesReceivedClient</code>, <code>BytesSentOrigin</code>, <code>BytesReceivedOrigin</code>), connection timestamps, client IP, colo code, and request metadata from the original WebSocket upgrade.</p>
<p>This data lets you build alerts on connection close patterns — for example, detecting spikes in TCP resets (<code>ConnectionCloseReason == &quot;peerReset&quot;</code>) grouped by host and data center — directly in your existing log analysis tools.</p>
<p>For the full list of available fields, refer to <a href="/logs/logpush/logpush-job/datasets/zone/websocket_analytics/">WebSocket Analytics</a>.</p>


<h2 id="updated-fields-across-multiple-logpush-datasets-in-cloudflare-logs"><a href="/changelog/post/2026-07-02-log-fields-updated/">Updated fields across multiple Logpush datasets in Cloudflare Logs</a></h2>
<p><em>2026-07-02</em></p>
<p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-07-02-log-fields-updated-updated-fields-in-existing-datasets">Updated fields in existing datasets</h4>
<ul>
<li><strong>Gateway DNS</strong> (added): <code>AppliedMaxTTL</code> and <code>UpstreamRecordTTLs</code>.</li>
<li><strong>Gateway HTTP</strong> (added): <code>Warnings</code>.</li>
<li><strong>HTTP requests</strong> (added): <code>CacheLockWaitedMs</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>


<h2 id="account-scoped-firewall-events-dataset-in-logpush"><a href="/changelog/post/2026-06-30-account-level-firewall-events/">Account-scoped firewall events dataset in Logpush</a></h2>
<p><em>2026-06-30</em></p>
<p>Cloudflare Logpush now supports <a href="/logs/logpush/logpush-job/datasets/account/firewall_events/">firewall events as an account-scoped dataset</a>. Configure a single Logpush job at the account level to receive firewall events for every zone in the account, instead of creating and maintaining a separate job per zone.</p>
<p>The dataset includes a new <a href="/logs/logpush/logpush-job/datasets/account/firewall_events/#zonename"><code>ZoneName</code></a> field so you can identify which zone each event came from when consuming logs in your downstream pipeline.</p>
<h4 id="2026-06-30-account-level-firewall-events-what-s-available">What's available</h4>
<ul>
<li>A new account-scoped <code>firewall_events</code> dataset, configurable via the <a href="/api/resources/logpush/subresources/jobs/">Logpush API</a> or the Cloudflare dashboard.</li>
<li>The same fields and filter expressions supported by the existing <a href="/logs/logpush/logpush-job/datasets/zone/firewall_events/">zone-scoped firewall events dataset</a>, plus the new <code>ZoneName</code> field.</li>
<li>Support for all existing Logpush destinations.</li>
</ul>


<h2 id="new-websocket-analytics-logpush-dataset-and-updated-fields"><a href="/changelog/post/2026-06-24-log-fields-updated/">New WebSocket Analytics Logpush dataset and updated fields</a></h2>
<p><em>2026-06-24</em></p>
<p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-06-24-log-fields-updated-new-datasets">New datasets</h4>
<ul>
<li><strong>WebSocket Analytics</strong>: A new dataset with fields including <code>BytesReceivedClient</code>, <code>BytesReceivedOrigin</code>, <code>BytesSentClient</code>, <code>BytesSentOrigin</code>, <code>ClientASN</code>, <code>ClientIP</code>, <code>ClientRequestHost</code>, <code>ClientRequestPath</code>, <code>ClientRequestUserAgent</code>, <code>ColoCode</code>, <code>ConnectionCloseReason</code>, <code>ConnectionCloseSource</code>, <code>ConnectionID</code>, <code>ConnectionTransportCloseCode</code>, <code>EdgeEndTimestamp</code>, <code>EdgeStartTimestamp</code>, and <code>RayID</code>.</li>
</ul>
<h4 id="2026-06-24-log-fields-updated-updated-fields-in-existing-datasets">Updated fields in existing datasets</h4>
<ul>
<li><strong>Firewall events</strong> (added): <code>ZoneName</code>. The Firewall events dataset is now also available for <a href="/logs/logpush/logpush-job/datasets/account/firewall_events/">account-scope Logpush</a>, in addition to the existing zone scope.</li>
<li><strong>Email Security Alerts</strong> (added): <code>BCC</code>, <code>DKIMResult</code>, <code>DMARCPolicy</code>, <code>DMARCResult</code>, and <code>SPFResult</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>


<h2 id="new-turnstile-events-logpush-dataset-in-cloudflare-logs"><a href="/changelog/post/2026-06-01-log-fields-updated/">New Turnstile Events Logpush dataset in Cloudflare Logs</a></h2>
<p><em>2026-06-01</em></p>
<p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-06-01-log-fields-updated-new-datasets">New datasets</h4>
<ul>
<li><strong>Turnstile Events</strong>: A new dataset with fields including <code>ASN</code>, <code>Action</code>, <code>BrowserMajor</code>, <code>BrowserName</code>, <code>ClientIP</code>, <code>CountryCode</code>, <code>EventType</code>, <code>Hostname</code>, <code>OSMajor</code>, <code>OSName</code>, <code>Sitekey</code>, <code>Timestamp</code>, and <code>UserAgent</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>


<h2 id="updated-fields-across-multiple-logpush-datasets-in-cloudflare-logs-1"><a href="/changelog/post/2026-05-29-log-fields-updated/">Updated fields across multiple Logpush datasets in Cloudflare Logs</a></h2>
<p><em>2026-05-29</em></p>
<p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-05-29-log-fields-updated-updated-fields-in-existing-datasets">Updated fields in existing datasets</h4>
<ul>
<li><strong>DEX Device State Events</strong> (added): <code>DeviceRegistrationProfileID</code>.</li>
<li><strong>Gateway HTTP</strong> (added): <code>AddedHeaders</code>, <code>DeletedHeaders</code>, and <code>SetHeaders</code>.</li>
<li><strong>HTTP requests</strong> (added): <code>MatchedRules</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>


<h2 id="new-logpush-datasets-and-updated-fields-across-multiple-logpush-datasets-in-cloudflare-logs-1"><a href="/changelog/post/2026-05-13-log-fields-updated/">New Logpush datasets and updated fields across multiple Logpush datasets in Cloudflare Logs</a></h2>
<p><em>2026-05-13</em></p>
<p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-05-13-log-fields-updated-new-datasets">New datasets</h4>
<ul>
<li><strong>Email Security Post-Delivery Events</strong>: A new dataset with fields including <code>AlertID</code>, <code>CompletedAt</code>, <code>Destination</code>, <code>FinalDisposition</code>, <code>Folder</code>, <code>From</code>, <code>FromName</code>, <code>MessageID</code>, <code>MessageTimestamp</code>, <code>MicrosoftTenantID</code>, <code>Operation</code>, <code>PostfixID</code>, <code>Reasons</code>, <code>Recipient</code>, <code>RequestedAt</code>, <code>RequestedBy</code>, <code>RequestedDisposition</code>, <code>Status</code>, <code>Subject</code>, <code>Success</code>, and <code>To</code>.</li>
<li><strong>Magic Network Monitoring Flow Logs</strong>: A new dataset with fields including <code>AWSVPCFlowJSON</code>, <code>Bits</code>, <code>DestinationAS</code>, <code>DestinationAddress</code>, <code>DestinationPort</code>, <code>DeviceID</code>, <code>EgressBits</code>, <code>EgressPackets</code>, <code>Ethertype</code>, <code>FlowProtocol</code>, <code>FlowTimestamp</code>, <code>NumFlows</code>, <code>PacketID</code>, <code>Packets</code>, <code>Protocol</code>, <code>RuleIDs</code>, <code>SampleRate</code>, <code>SampleRateType</code>, <code>SamplerAddress</code>, <code>SourceAS</code>, <code>SourceAddress</code>, <code>SourcePort</code>, <code>TcpFlags</code>, and <code>Timestamp</code>.</li>
</ul>
<h4 id="2026-05-13-log-fields-updated-updated-fields-in-existing-datasets">Updated fields in existing datasets</h4>
<ul>
<li><strong>Firewall events</strong> (added): <code>AISecurityInjectionScore</code>, <code>AISecurityPIICategories</code>, <code>AISecurityTokenCount</code>, and <code>AISecurityUnsafeTopicCategories</code>.</li>
<li><strong>HTTP requests</strong> (added): <code>AISecurityInjectionScore</code>, <code>AISecurityPIICategories</code>, <code>AISecurityTokenCount</code>, <code>AISecurityUnsafeTopicCategories</code>, and <code>Subrequests</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>


<h2 id="logpush-subrequest-merging-for-http-requests"><a href="/changelog/post/2026-04-21-logpush-subrequests-merging/">Logpush subrequest merging for HTTP requests</a></h2>
<p><em>2026-04-21</em></p>
<p>When a Cloudflare Worker intercepts a visitor request, it can dispatch additional outbound fetch calls called subrequests. By default, each subrequest generates its own log entry in Logpush, resulting in multiple log lines per visitor request. With subrequest merging enabled, subrequest data is embedded as a nested array field on the parent log record instead.</p>
<h4 id="2026-04-21-logpush-subrequests-merging-what-s-new">What's new</h4>
- New subrequest_merging field on Logpush jobs — Set "merge_subrequests": true when creating or updating an http_requests Logpush job to enable the feature.
- New Subrequests log field — When subrequest merging is enabled, a Subrequests field (`array\<object\>`) is added to each parent request log record. Each element in the array contains the standard http_requests fields for that subrequest.
<h4 id="2026-04-21-logpush-subrequests-merging-limitations">Limitations</h4>
- Applies to the http_requests (zone-scoped) dataset only.
- A maximum of 50 subrequests are merged per parent request. Subrequests beyond this limit are passed through unmodified as individual log entries.
- Subrequests must complete within 5 minutes of the visitor request. Subrequests that exceed this window are passed through unmodified.
- Subrequests that do not qualify appear as separate log entries — no data is lost.
- Subrequest merging is being gradually rolled out and is not yet available on all zones. Contact your account team for concerns or to ensure it is enabled for your zone.
- For more information, refer to [Subrequests](/logs/logpush/logpush-job/subrequests/).


<h2 id="cloudflare-pipelines-as-a-logpush-destination"><a href="/changelog/post/2026-04-20-pipelines-logpush-destination/">Cloudflare Pipelines as a Logpush destination</a></h2>
<p><em>2026-04-20</em></p>
<p>Logpush has traditionally been great at delivering Cloudflare logs to a variety of destinations in JSON format. While JSON is flexible and easily readable, it can be inefficient to store and query at scale.</p>
<p>With this release, you can now send your logs directly to <a href="/pipelines/">Pipelines</a> to ingest, transform, and store your logs in <a href="/r2/">R2</a> as Parquet files or Apache Iceberg tables managed by <a href="/r2-data-catalog/">R2 Data Catalog</a>. This makes the data footprint more compact and more efficient at querying your logs instantly with <a href="/r2-sql/">R2 SQL</a> or any other query engine that supports Apache Iceberg or Parquet.</p>
<h4 id="2026-04-20-pipelines-logpush-destination-transform-logs-before-storage">Transform logs before storage</h4>
<p>Pipelines SQL runs on each log record in-flight, so you can reshape your data before it is written. For example, you can drop noisy fields, redact sensitive values, or derive new columns:</p>
<pre><code class="language-sql">INSERT INTO http_logs_sink&#10;SELECT&#10;  ClientIP,&#10;  EdgeResponseStatus,&#10;  to_timestamp_micros(EdgeStartTimestamp) AS event_time,&#10;  upper(ClientRequestMethod) AS method,&#10;  sha256(ClientIP) AS hashed_ip&#10;FROM http_logs_stream&#10;WHERE EdgeResponseStatus &gt;= 400;&#10;</code></pre>
<p>Pipelines SQL supports string functions, regex, hashing, JSON extraction, timestamp conversion, conditional expressions, and more. For the full list, refer to the <a href="/pipelines/sql-reference/">Pipelines SQL reference</a>.</p>
<h4 id="2026-04-20-pipelines-logpush-destination-get-started">Get started</h4>
<p>To configure Pipelines as a Logpush destination, refer to <a href="/logs/logpush/logpush-job/enable-destinations/pipelines/">Enable Cloudflare Pipelines</a>.</p>


<h2 id="new-tenantid-and-firewall-for-ai-fields-in-logpush-datasets"><a href="/changelog/post/2026-04-15-logpush-new-fields/">New TenantID and Firewall for AI fields in Logpush datasets</a></h2>
<p><em>2026-04-15</em></p>
<p>Cloudflare has added new fields to multiple <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-04-15-logpush-new-fields-tenantid-field">TenantID field</h4>
<p>The following Gateway and Zero Trust datasets now include a <code>TenantID</code> field:</p>
<ul>
<li><strong><a href="/logs/logpush/logpush-job/datasets/account/gateway_dns/#tenantid">Gateway DNS</a></strong>: Identifies the tenant ID of the DNS request, if it exists.</li>
<li><strong><a href="/logs/logpush/logpush-job/datasets/account/gateway_http/#tenantid">Gateway HTTP</a></strong>: Identifies the tenant ID of the HTTP request, if it exists.</li>
<li><strong><a href="/logs/logpush/logpush-job/datasets/account/gateway_network/#tenantid">Gateway Network</a></strong>: Identifies the tenant ID of the network session, if it exists.</li>
<li><strong><a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/#tenantid">Zero Trust Network Sessions</a></strong>: Identifies the tenant ID of the network session, if it exists.</li>
</ul>
<h4 id="2026-04-15-logpush-new-fields-firewall-for-ai-fields">Firewall for AI fields</h4>
<p>The following datasets now include <a href="/api-shield/security/volumetric-abuse-detection/#firewall-for-ai">Firewall for AI</a> fields:</p>
<ul>
<li>
<p><strong><a href="/logs/logpush/logpush-job/datasets/zone/firewall_events/">Firewall Events</a></strong>:</p>
<ul>
<li><code>FirewallForAIInjectionScore</code>: The score indicating the likelihood of a prompt injection attack in the request.</li>
<li><code>FirewallForAIPIICategories</code>: List of PII categories detected in the request.</li>
<li><code>FirewallForAITokenCount</code>: The number of tokens in the request.</li>
<li><code>FirewallForAIUnsafeTopicCategories</code>: List of unsafe topic categories detected in the request.</li>
</ul>
</li>
<li>
<p><strong><a href="/logs/logpush/logpush-job/datasets/zone/http_requests/">HTTP Requests</a></strong>:</p>
<ul>
<li><code>FirewallForAIInjectionScore</code>: The score indicating the likelihood of a prompt injection attack in the request.</li>
<li><code>FirewallForAIPIICategories</code>: List of PII categories detected in the request.</li>
<li><code>FirewallForAITokenCount</code>: The number of tokens in the request.</li>
<li><code>FirewallForAIUnsafeTopicCategories</code>: List of unsafe topic categories detected in the request.</li>
</ul>
</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>


<h2 id="logpush-to-bigquery-cloudflare-dashboard-support"><a href="/changelog/post/2026-04-14-bigquery-dashboard-support/">Logpush to BigQuery — Cloudflare dashboard support</a></h2>
<p><em>2026-04-14</em></p>
<p>You can now configure Logpush jobs to Google BigQuery directly from the Cloudflare dashboard, in addition to the existing API-based setup.</p>
<p>Previously, setting up a BigQuery Logpush destination required using the Logpush API. Now you can create and manage BigQuery Logpush jobs from the <strong>Logpush</strong> page in the Cloudflare dashboard by selecting <strong>Google BigQuery</strong> as the destination and entering your Google Cloud project ID, dataset ID, table ID, and service account credentials.</p>
<p>For more information, refer to <a href="/logs/logpush/logpush-job/enable-destinations/bigquery/">Enable Logpush to Google BigQuery</a>.</p>


<h2 id="new-responsetimems-field-in-gateway-dns-logpush-dataset"><a href="/changelog/post/2026-04-06-gateway-dns-response-time-ms/">New ResponseTimeMs field in Gateway DNS Logpush dataset</a></h2>
<p><em>2026-04-06</em></p>
<p>Cloudflare has added a new field to the <a href="/logs/logpush/logpush-job/datasets/account/gateway_dns/#responsetimems">Gateway DNS</a> Logpush dataset:</p>
<ul>
<li><strong>ResponseTimeMs</strong>: Total response time of the DNS request in milliseconds.</li>
</ul>
<p>For the complete field definitions, refer to <a href="/logs/logpush/logpush-job/datasets/account/gateway_dns/">Gateway DNS dataset</a>.</p>


<h2 id="bigquery-as-logpush-destination"><a href="/changelog/post/2026-04-02-bigquery-destination/">BigQuery as Logpush destination</a></h2>
<p><em>2026-04-02</em></p>
<p>Cloudflare Logpush now supports <strong>BigQuery</strong> as a native destination.</p>
<p>Logs from Cloudflare can be sent to <a href="https://cloud.google.com/bigquery">Google Cloud BigQuery</a> via <a href="/logs/logpush/">Logpush</a>. The destination can be configured through the Logpush UI in the Cloudflare dashboard or by using the <a href="/api/resources/logpush/subresources/jobs/">Logpush API</a>.</p>
<p>For more information, refer to the <a href="/logs/logpush/logpush-job/enable-destinations/bigquery/">Destination Configuration</a> documentation.</p>


<h2 id="logpush-more-granular-timestamps"><a href="/changelog/post/2026-03-25-logpush-granular-timestamps/">Logpush — More granular timestamps</a></h2>
<p><em>2026-03-25</em></p>
<p>Logpush now supports higher-precision timestamp formats for log output. You can configure jobs to output timestamps at millisecond or nanosecond precision. This is available in both the Logpush UI in the Cloudflare dashboard and the <a href="/api/resources/logpush/subresources/jobs/">Logpush API</a>.</p>
<p>To use the new formats, set <code>timestamp_format</code> in your Logpush job's <code>output_options</code>:</p>
<ul>
<li><code>rfc3339ms</code> — <code>2024-02-17T23:52:01.123Z</code></li>
<li><code>rfc3339ns</code> — <code>2024-02-17T23:52:01.123456789Z</code></li>
</ul>
<p>Default timestamp formats apply unless explicitly set. The dashboard defaults to <code>rfc3339</code> and the API defaults to <code>unixnano</code>.</p>
<p>For more information, refer to the <a href="/logs/logpush/logpush-job/log-output-options/">Log output options</a> documentation.</p>


<h2 id="new-mcp-portal-logs-dataset-and-new-fields-across-multiple-logpush-datasets-in-cloudflare-logs"><a href="/changelog/post/2026-03-09-log-fields-updated/">New MCP Portal Logs dataset and new fields across multiple Logpush datasets in Cloudflare Logs</a></h2>
<p><em>2026-03-09</em></p>
<p>Cloudflare has added new fields across multiple <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-03-09-log-fields-updated-new-dataset">New dataset</h4>
<ul>
<li><strong>MCP Portal Logs</strong>: A new dataset with fields including <code>ClientCountry</code>, <code>ClientIP</code>, <code>ColoCode</code>, <code>Datetime</code>, <code>Error</code>, <code>Method</code>, <code>PortalAUD</code>, <code>PortalID</code>, <code>PromptGetName</code>, <code>ResourceReadURI</code>, <code>ServerAUD</code>, <code>ServerID</code>, <code>ServerResponseDurationMs</code>, <code>ServerURL</code>, <code>SessionID</code>, <code>Success</code>, <code>ToolCallName</code>, <code>UserEmail</code>, and <code>UserID</code>.</li>
</ul>
<h4 id="2026-03-09-log-fields-updated-new-fields-in-existing-datasets">New fields in existing datasets</h4>
<ul>
<li><strong>DEX Application Tests</strong>: <code>HTTPRedirectEndMs</code>, <code>HTTPRedirectStartMs</code>, <code>HTTPResponseBody</code>, and <code>HTTPResponseHeaders</code>.</li>
<li><strong>DEX Device State Events</strong>: <code>ExperimentalExtra</code>.</li>
<li><strong>Firewall Events</strong>: <code>FraudUserID</code>.</li>
<li><strong>Gateway HTTP</strong>: <code>AppControlInfo</code> and <code>ApplicationStatuses</code>.</li>
<li><strong>Gateway DNS</strong>: <code>InternalDNSDurationMs</code>.</li>
<li><strong>HTTP Requests</strong>: <code>FraudEmailRisk</code>, <code>FraudUserID</code>, and <code>PayPerCrawlStatus</code>.</li>
<li><strong>Network Analytics Logs</strong>: <code>DNSQueryName</code>, <code>DNSQueryType</code>, and <code>PFPCustomTag</code>.</li>
<li><strong>WARP Toggle Changes</strong>: <code>UserEmail</code>.</li>
<li><strong>WARP Config Changes</strong>: <code>UserEmail</code>.</li>
<li><strong>Zero Trust Network Session Logs</strong>: <code>SNI</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>


<h2 id="sentinelone-as-logpush-destination"><a href="/changelog/post/2025-12-11-sentinelone-destination/">SentinelOne as Logpush destination</a></h2>
<p><em>2025-12-11</em></p>
<p>Cloudflare Logpush now supports <strong>SentinelOne</strong> as a native destination.</p>
<p>Logs from Cloudflare can be sent to <a href="https://www.sentinelone.com/">SentinelOne AI SIEM</a> via <a href="/logs/logpush/">Logpush</a>. The destination can be configured through the Logpush UI in the Cloudflare dashboard or by using the <a href="/api/resources/logpush/subresources/jobs/">Logpush API</a>.</p>
<p>For more information, refer to the <a href="/logs/logpush/logpush-job/enable-destinations/sentinelone/">Destination Configuration</a> documentation.</p>


<h2 id="logpush-health-dashboards"><a href="/changelog/post/2025-11-11-health-dashboards/">Logpush Health Dashboards</a></h2>
<p><em>2025-11-11</em></p>
<p>We’re excited to introduce <strong>Logpush Health Dashboards</strong>, giving customers real-time visibility into the status, reliability, and performance of their <a href="/logs/logpush/">Logpush</a> jobs. Health dashboards make it easier to detect delivery issues, monitor job stability, and track performance across destinations. The dashboards are divided into two sections:</p>
<ul>
<li>
<p><strong>Upload Health</strong>: See how much data was successfully uploaded, where drops occurred, and how your jobs are performing overall. This includes data completeness, success rate, and upload volume.</p>
</li>
<li>
<p><strong>Upload Reliability</strong> – Diagnose issues impacting stability, retries, or latency, and monitor key metrics such as retry counts, upload duration, and destination availability.</p>
</li>
</ul>
<p><img src="/assets/upstream/images/logs/Health-Dashboard.gif" alt="Health Dashboard" /></p>
<p>Health Dashboards can be accessed from the Logpush page in the Cloudflare dashboard at the account or zone level, under the Health tab. For more details, refer to our <a href="/logs/logpush/logpush-health"><strong>Logpush Health Dashboards</strong></a> documentation, which includes a comprehensive troubleshooting guide to help interpret and resolve common issues.</p>


<h2 id="logpush-permission-update-for-zero-trust-datasets"><a href="/changelog/post/2025-11-05-logpush-permissions-update/">Logpush Permission Update for Zero Trust Datasets</a></h2>
<p><em>2025-11-05</em></p>
<p><a href="/logs/logpush/permissions/">Permissions</a> for managing Logpush jobs related to <a href="/logs/logpush/logpush-job/datasets/account/">Zero Trust datasets</a> (Access, Gateway, and DEX) have been updated to improve data security and enforce appropriate access controls.</p>
<p>To view, create, update, or delete Logpush jobs for Zero Trust datasets, users must now have both of the following permissions:</p>
<ul>
<li>Logs Edit</li>
<li>Zero Trust: PII Read</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17738.md")</aside>


<h2 id="azure-sentinel-connector"><a href="/changelog/post/2025-10-27-Sentinel-connector/">Azure Sentinel Connector</a></h2>
<p><em>2025-10-27</em></p>
<p>Logpush now supports integration with <a href="https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-sentinel">Microsoft Sentinel</a>.The new Azure Sentinel Connector built on Microsoft’s Codeless Connector Framework (CCF), is now available. This solution replaces the previous Azure Functions-based connector, offering significant improvements in security, data control, and ease of use for customers. Logpush customers can send logs to Azure Blob Storage and configure this new Sentinel Connector to ingest those logs directly into Microsoft Sentinel.</p>
<p>This upgrade significantly streamlines log ingestion, improves security, and provides greater control:</p>
<ul>
<li>Simplified Implementation: Easier for engineering teams to set up and maintain.</li>
<li>Cost Control: New support for Data Collection Rules (DCRs) allows you to filter and transform logs at ingestion time, offering potential cost savings.</li>
<li>Enhanced Security: CCF provides a higher level of security compared to the older Azure Functions connector.</li>
<li>Data Lake Integration: Includes native integration with Data Lake.</li>
</ul>
<p>Find the new solution <a href="https://marketplace.microsoft.com/en-us/product/azure-application/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview">here</a> and refer to the <a href="https://developers.cloudflare.com/analytics/analytics-integrations/sentinel/#supported-logs:~:text=WorkBook%20fields,-Analytic%20rules">Cloudflare's developer documentation</a>for more information on the connector, including setup steps, supported logs and Microsoft's resources.</p>


<h2 id="dedicated-egress-ip-for-logpush"><a href="/changelog/post/2025-08-22-dedicated-egress-ip-logpush/">Dedicated Egress IP for Logpush</a></h2>
<p><em>2025-08-22</em></p>
<p>Cloudflare Logpush can now deliver logs from using fixed, dedicated egress IPs. By routing Logpush traffic through a Cloudflare zone enabled with <a href="/smart-shield/configuration/dedicated-egress-ips/">Aegis IP</a>, your log destination only needs to allow Aegis IPs making setup more secure.</p>
<p>Highlights:</p>
<ul>
<li>Fixed egress IPs ensure your destination only accepts traffic from known addresses.</li>
<li>Works with any supported Logpush destination.</li>
<li>Recommended to use a dedicated zone as a proxy for easier management.</li>
</ul>
<p>To get started, work with your Cloudflare account team to provision Aegis IPs, then configure your Logpush job to deliver logs through the proxy zone. For full setup instructions, refer to the <a href="/logs/logpush/logpush-job/enable-destinations/egress-ip/">Logpush documentation</a>.</p>


<h2 id="ibm-cloud-logs-as-logpush-destination"><a href="/changelog/post/2025-08-13-ibm-cloud-logs-destination/">IBM Cloud Logs as Logpush destination</a></h2>
<p><em>2025-08-13</em></p>
<p>Cloudflare Logpush now supports IBM Cloud Logs as a native destination.</p>
<p>Logs from Cloudflare can be sent to <a href="https://www.ibm.com/products/cloud-logs">IBM Cloud Logs</a> via <a href="/logs/logpush/">Logpush</a>. The setup can be done through the Logpush UI in the Cloudflare Dashboard or by using the <a href="/api/resources/logpush/subresources/jobs/">Logpush API</a>. The integration requires IBM Cloud Logs HTTP Source Address and an IBM API Key. The feature also allows for filtering events and selecting specific log fields.</p>
<p>For more information, refer to <a href="/logs/logpush/logpush-job/enable-destinations/ibm-cloud-logs/">Destination Configuration</a> documentation.</p>


<h2 id="custom-fields-raw-and-transformed-values-support"><a href="/changelog/post/2025-04-18-custom-fields-raw-transformed-values/">Custom fields raw and transformed values support</a></h2>
<p><em>2025-04-18</em></p>
<p>Custom Fields now support logging both <strong>raw and transformed values</strong> for request and response headers in the HTTP requests dataset.</p>
<p>These fields are configured per zone and apply to all Logpush jobs in that zone that include request headers, response headers. Each header can be logged in only one format—either raw or transformed—not both.</p>
<p>By default:</p>
<ul>
<li>Request headers are logged as raw values</li>
<li>Response headers are logged as transformed values</li>
</ul>
<p>These defaults can be overridden to suit your logging needs.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17737.md")</aside>
<p>For more information refer to <a href="/logs/logpush/logpush-job/custom-fields/">Custom fields</a> documentation</p>


<nav class="pagination" aria-label="Changelog pages"><span>Page 1 of 2</span><a class="pagination-next" rel="next" href="/changelog/product/logs/2/">Next</a></nav>
