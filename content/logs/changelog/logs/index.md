---
cp9:
  canonical: https://developers.cloudflare.com/logs/changelog/logs/
  description: View changelog entries for Cloudflare Logs.
  full_title: Logs · Cloudflare Logs docs
  head_html: <title>Logs · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="View changelog entries for Cloudflare Logs."><link rel="canonical" href="https://developers.cloudflare.com/logs/changelog/logs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/changelog/logs/index.md"><link rel="alternate" type="application/rss+xml" href="https://developers.cloudflare.com/logs/changelog/logs/index.xml"><meta property="og:title" content="Logs · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="View changelog entries for Cloudflare Logs."><meta property="og:url" content="https://developers.cloudflare.com/logs/changelog/logs/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Changelog"><meta name="algolia_content_type" content="Changelog"><meta name="pcx_additional_products" content="Logs"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/logs/changelog/logs/#page","headline":"Logs \u00b7 Cloudflare Logs docs","description":"View changelog entries for Cloudflare Logs.","url":"https://developers.cloudflare.com/logs/changelog/logs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/changelog/logs/
  schema: 1
---
<h2 id="2026-08-26">2026-08-26</h2>

<strong>Azure Functions-based Microsoft Sentinel connector deprecation</strong>

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


<h2 id="2026-08-20">2026-08-20</h2>

<strong>New Logpush datasets and updated fields across multiple Logpush datasets in Cloudflare Logs</strong>

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


<h2 id="2026-08-20-1">2026-08-20</h2>

<strong>Per-zone post-quantum visibility in Logpush and Log Explorer</strong>

<p><a href="https://radar.cloudflare.com/post-quantum">Cloudflare Radar</a> publishes global statistics on post-quantum key agreement adoption across all Cloudflare traffic, but until now customers had no way to see the same measurement scoped to their own zones. This is now possible because the <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/"><code>http_requests</code></a> Logpush dataset — also queryable in <a href="/log-explorer/">Log Explorer</a> — includes a new <code>ClientTLSKeyExchangeGroup</code> field.</p>
<p>The field reports the TLS key exchange group negotiated on the client-to-Cloudflare connection, by group name. Post-quantum connections appear as <code>X25519MLKEM768</code>, and classical connections appear as <code>X25519</code>, <code>P-256</code>, or another named group. A value of <code>UNK</code> means the group could not be determined, and <code>NONE</code> means TLS was not used.</p>
<p>With this field, you can build per-zone reports showing what percentage of your inbound HTTPS traffic is protected by post-quantum key agreement, break the number down by hostname, path, user agent, or country, and push the data into your SIEM via any <a href="/logs/logpush/logpush-job/enable-destinations/">Logpush destination</a>.</p>


<h2 id="2026-07-07">2026-07-07</h2>

<strong>New WebSocket Analytics Logpush dataset</strong>

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


<h2 id="2026-07-02">2026-07-02</h2>

<strong>Updated fields across multiple Logpush datasets in Cloudflare Logs</strong>

<p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-07-02-log-fields-updated-updated-fields-in-existing-datasets">Updated fields in existing datasets</h4>
<ul>
<li><strong>Gateway DNS</strong> (added): <code>AppliedMaxTTL</code> and <code>UpstreamRecordTTLs</code>.</li>
<li><strong>Gateway HTTP</strong> (added): <code>Warnings</code>.</li>
<li><strong>HTTP requests</strong> (added): <code>CacheLockWaitedMs</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>


<h2 id="2026-06-30">2026-06-30</h2>

<strong>Account-scoped firewall events dataset in Logpush</strong>

<p>Cloudflare Logpush now supports <a href="/logs/logpush/logpush-job/datasets/account/firewall_events/">firewall events as an account-scoped dataset</a>. Configure a single Logpush job at the account level to receive firewall events for every zone in the account, instead of creating and maintaining a separate job per zone.</p>
<p>The dataset includes a new <a href="/logs/logpush/logpush-job/datasets/account/firewall_events/#zonename"><code>ZoneName</code></a> field so you can identify which zone each event came from when consuming logs in your downstream pipeline.</p>
<h4 id="2026-06-30-account-level-firewall-events-what-s-available">What's available</h4>
<ul>
<li>A new account-scoped <code>firewall_events</code> dataset, configurable via the <a href="/api/resources/logpush/subresources/jobs/">Logpush API</a> or the Cloudflare dashboard.</li>
<li>The same fields and filter expressions supported by the existing <a href="/logs/logpush/logpush-job/datasets/zone/firewall_events/">zone-scoped firewall events dataset</a>, plus the new <code>ZoneName</code> field.</li>
<li>Support for all existing Logpush destinations.</li>
</ul>


<h2 id="2026-06-24">2026-06-24</h2>

<strong>New WebSocket Analytics Logpush dataset and updated fields</strong>

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


<h2 id="2026-06-01">2026-06-01</h2>

<strong>New Turnstile Events Logpush dataset in Cloudflare Logs</strong>

<p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-06-01-log-fields-updated-new-datasets">New datasets</h4>
<ul>
<li><strong>Turnstile Events</strong>: A new dataset with fields including <code>ASN</code>, <code>Action</code>, <code>BrowserMajor</code>, <code>BrowserName</code>, <code>ClientIP</code>, <code>CountryCode</code>, <code>EventType</code>, <code>Hostname</code>, <code>OSMajor</code>, <code>OSName</code>, <code>Sitekey</code>, <code>Timestamp</code>, and <code>UserAgent</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>


<h2 id="2026-05-29">2026-05-29</h2>

<strong>Updated fields across multiple Logpush datasets in Cloudflare Logs</strong>

<p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-05-29-log-fields-updated-updated-fields-in-existing-datasets">Updated fields in existing datasets</h4>
<ul>
<li><strong>DEX Device State Events</strong> (added): <code>DeviceRegistrationProfileID</code>.</li>
<li><strong>Gateway HTTP</strong> (added): <code>AddedHeaders</code>, <code>DeletedHeaders</code>, and <code>SetHeaders</code>.</li>
<li><strong>HTTP requests</strong> (added): <code>MatchedRules</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>


<h2 id="2026-05-13">2026-05-13</h2>

<strong>New Logpush datasets and updated fields across multiple Logpush datasets in Cloudflare Logs</strong>

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


<h2 id="2026-04-21">2026-04-21</h2>

<strong>Logpush subrequest merging for HTTP requests</strong>

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


<h2 id="2026-04-20">2026-04-20</h2>

<strong>Cloudflare Pipelines as a Logpush destination</strong>

<p>Logpush has traditionally been great at delivering Cloudflare logs to a variety of destinations in JSON format. While JSON is flexible and easily readable, it can be inefficient to store and query at scale.</p>
<p>With this release, you can now send your logs directly to <a href="/pipelines/">Pipelines</a> to ingest, transform, and store your logs in <a href="/r2/">R2</a> as Parquet files or Apache Iceberg tables managed by <a href="/r2-data-catalog/">R2 Data Catalog</a>. This makes the data footprint more compact and more efficient at querying your logs instantly with <a href="/r2-sql/">R2 SQL</a> or any other query engine that supports Apache Iceberg or Parquet.</p>
<h4 id="2026-04-20-pipelines-logpush-destination-transform-logs-before-storage">Transform logs before storage</h4>
<p>Pipelines SQL runs on each log record in-flight, so you can reshape your data before it is written. For example, you can drop noisy fields, redact sensitive values, or derive new columns:</p>
<pre tabindex="0"><code class="language-sql">INSERT INTO http_logs_sink&#10;SELECT&#10;  ClientIP,&#10;  EdgeResponseStatus,&#10;  to_timestamp_micros(EdgeStartTimestamp) AS event_time,&#10;  upper(ClientRequestMethod) AS method,&#10;  sha256(ClientIP) AS hashed_ip&#10;FROM http_logs_stream&#10;WHERE EdgeResponseStatus &gt;= 400;&#10;</code></pre>
<p>Pipelines SQL supports string functions, regex, hashing, JSON extraction, timestamp conversion, conditional expressions, and more. For the full list, refer to the <a href="/pipelines/sql-reference/">Pipelines SQL reference</a>.</p>
<h4 id="2026-04-20-pipelines-logpush-destination-get-started">Get started</h4>
<p>To configure Pipelines as a Logpush destination, refer to <a href="/logs/logpush/logpush-job/enable-destinations/pipelines/">Enable Cloudflare Pipelines</a>.</p>


<h2 id="2026-04-15">2026-04-15</h2>

<strong>New TenantID and Firewall for AI fields in Logpush datasets</strong>

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


<h2 id="2026-04-14">2026-04-14</h2>

<strong>Logpush to BigQuery — Cloudflare dashboard support</strong>

<p>You can now configure Logpush jobs to Google BigQuery directly from the Cloudflare dashboard, in addition to the existing API-based setup.</p>
<p>Previously, setting up a BigQuery Logpush destination required using the Logpush API. Now you can create and manage BigQuery Logpush jobs from the <strong>Logpush</strong> page in the Cloudflare dashboard by selecting <strong>Google BigQuery</strong> as the destination and entering your Google Cloud project ID, dataset ID, table ID, and service account credentials.</p>
<p>For more information, refer to <a href="/logs/logpush/logpush-job/enable-destinations/bigquery/">Enable Logpush to Google BigQuery</a>.</p>


<h2 id="2026-04-06">2026-04-06</h2>

<strong>New ResponseTimeMs field in Gateway DNS Logpush dataset</strong>

<p>Cloudflare has added a new field to the <a href="/logs/logpush/logpush-job/datasets/account/gateway_dns/#responsetimems">Gateway DNS</a> Logpush dataset:</p>
<ul>
<li><strong>ResponseTimeMs</strong>: Total response time of the DNS request in milliseconds.</li>
</ul>
<p>For the complete field definitions, refer to <a href="/logs/logpush/logpush-job/datasets/account/gateway_dns/">Gateway DNS dataset</a>.</p>


<h2 id="2026-04-02">2026-04-02</h2>

<strong>BigQuery as Logpush destination</strong>

<p>Cloudflare Logpush now supports <strong>BigQuery</strong> as a native destination.</p>
<p>Logs from Cloudflare can be sent to <a href="https://cloud.google.com/bigquery">Google Cloud BigQuery</a> via <a href="/logs/logpush/">Logpush</a>. The destination can be configured through the Logpush UI in the Cloudflare dashboard or by using the <a href="/api/resources/logpush/subresources/jobs/">Logpush API</a>.</p>
<p>For more information, refer to the <a href="/logs/logpush/logpush-job/enable-destinations/bigquery/">Destination Configuration</a> documentation.</p>


<h2 id="2026-03-25">2026-03-25</h2>

<strong>Logpush — More granular timestamps</strong>

<p>Logpush now supports higher-precision timestamp formats for log output. You can configure jobs to output timestamps at millisecond or nanosecond precision. This is available in both the Logpush UI in the Cloudflare dashboard and the <a href="/api/resources/logpush/subresources/jobs/">Logpush API</a>.</p>
<p>To use the new formats, set <code>timestamp_format</code> in your Logpush job's <code>output_options</code>:</p>
<ul>
<li><code>rfc3339ms</code> — <code>2024-02-17T23:52:01.123Z</code></li>
<li><code>rfc3339ns</code> — <code>2024-02-17T23:52:01.123456789Z</code></li>
</ul>
<p>Default timestamp formats apply unless explicitly set. The dashboard defaults to <code>rfc3339</code> and the API defaults to <code>unixnano</code>.</p>
<p>For more information, refer to the <a href="/logs/logpush/logpush-job/log-output-options/">Log output options</a> documentation.</p>


<h2 id="2026-03-09">2026-03-09</h2>

<strong>New MCP Portal Logs dataset and new fields across multiple Logpush datasets in Cloudflare Logs</strong>

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


<h2 id="2025-12-11">2025-12-11</h2>

<strong>SentinelOne as Logpush destination</strong>

<p>Cloudflare Logpush now supports <strong>SentinelOne</strong> as a native destination.</p>
<p>Logs from Cloudflare can be sent to <a href="https://www.sentinelone.com/">SentinelOne AI SIEM</a> via <a href="/logs/logpush/">Logpush</a>. The destination can be configured through the Logpush UI in the Cloudflare dashboard or by using the <a href="/api/resources/logpush/subresources/jobs/">Logpush API</a>.</p>
<p>For more information, refer to the <a href="/logs/logpush/logpush-job/enable-destinations/sentinelone/">Destination Configuration</a> documentation.</p>


<h2 id="2025-11-11">2025-11-11</h2>

<strong>Logpush Health Dashboards</strong>

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


<h2 id="2025-11-05">2025-11-05</h2>

<strong>Logpush Permission Update for Zero Trust Datasets</strong>

<p><a href="/logs/logpush/permissions/">Permissions</a> for managing Logpush jobs related to <a href="/logs/logpush/logpush-job/datasets/account/">Zero Trust datasets</a> (Access, Gateway, and DEX) have been updated to improve data security and enforce appropriate access controls.</p>
<p>To view, create, update, or delete Logpush jobs for Zero Trust datasets, users must now have both of the following permissions:</p>
<ul>
<li>Logs Edit</li>
<li>Zero Trust: PII Read</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17738.md")</aside>


<h2 id="2025-10-27">2025-10-27</h2>

<strong>Azure Sentinel Connector</strong>

<p>Logpush now supports integration with <a href="https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-sentinel">Microsoft Sentinel</a>.The new Azure Sentinel Connector built on Microsoft’s Codeless Connector Framework (CCF), is now available. This solution replaces the previous Azure Functions-based connector, offering significant improvements in security, data control, and ease of use for customers. Logpush customers can send logs to Azure Blob Storage and configure this new Sentinel Connector to ingest those logs directly into Microsoft Sentinel.</p>
<p>This upgrade significantly streamlines log ingestion, improves security, and provides greater control:</p>
<ul>
<li>Simplified Implementation: Easier for engineering teams to set up and maintain.</li>
<li>Cost Control: New support for Data Collection Rules (DCRs) allows you to filter and transform logs at ingestion time, offering potential cost savings.</li>
<li>Enhanced Security: CCF provides a higher level of security compared to the older Azure Functions connector.</li>
<li>Data Lake Integration: Includes native integration with Data Lake.</li>
</ul>
<p>Find the new solution <a href="https://marketplace.microsoft.com/en-us/product/azure-application/cloudflare.azure-sentinel-solution-cloudflare-ccf?tab=Overview">here</a> and refer to the <a href="https://developers.cloudflare.com/analytics/analytics-integrations/sentinel/#supported-logs:~:text=WorkBook%20fields,-Analytic%20rules">Cloudflare's developer documentation</a>for more information on the connector, including setup steps, supported logs and Microsoft's resources.</p>


<h2 id="2025-08-22">2025-08-22</h2>

<strong>Dedicated Egress IP for Logpush</strong>

<p>Cloudflare Logpush can now deliver logs from using fixed, dedicated egress IPs. By routing Logpush traffic through a Cloudflare zone enabled with <a href="/smart-shield/configuration/dedicated-egress-ips/">Aegis IP</a>, your log destination only needs to allow Aegis IPs making setup more secure.</p>
<p>Highlights:</p>
<ul>
<li>Fixed egress IPs ensure your destination only accepts traffic from known addresses.</li>
<li>Works with any supported Logpush destination.</li>
<li>Recommended to use a dedicated zone as a proxy for easier management.</li>
</ul>
<p>To get started, work with your Cloudflare account team to provision Aegis IPs, then configure your Logpush job to deliver logs through the proxy zone. For full setup instructions, refer to the <a href="/logs/logpush/logpush-job/enable-destinations/egress-ip/">Logpush documentation</a>.</p>


<h2 id="2025-08-13">2025-08-13</h2>

<strong>IBM Cloud Logs as Logpush destination</strong>

<p>Cloudflare Logpush now supports IBM Cloud Logs as a native destination.</p>
<p>Logs from Cloudflare can be sent to <a href="https://www.ibm.com/products/cloud-logs">IBM Cloud Logs</a> via <a href="/logs/logpush/">Logpush</a>. The setup can be done through the Logpush UI in the Cloudflare Dashboard or by using the <a href="/api/resources/logpush/subresources/jobs/">Logpush API</a>. The integration requires IBM Cloud Logs HTTP Source Address and an IBM API Key. The feature also allows for filtering events and selecting specific log fields.</p>
<p>For more information, refer to <a href="/logs/logpush/logpush-job/enable-destinations/ibm-cloud-logs/">Destination Configuration</a> documentation.</p>


<h2 id="2025-04-18">2025-04-18</h2>

<strong>Custom fields raw and transformed values support</strong>

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


<h2 id="2025-03-06">2025-03-06</h2>

<strong>One-click Logpush Setup with R2 Object Storage</strong>

<p>We’ve streamlined the <a href="/logs/logpush/">Logpush</a> setup process by integrating R2 bucket creation directly into the Logpush workflow!</p>
<p>Now, you no longer need to navigate multiple pages to manually create an R2 bucket or copy credentials. With this update, you can seamlessly <strong>configure a Logpush job to R2 in just one click</strong>, reducing friction and making setup faster and easier.</p>
<p>This enhancement makes it easier for customers to adopt Logpush and R2.</p>
<p>For more details refer to our <a href="/logs/logpush/logpush-job/enable-destinations/r2/">Logs</a> documentation.</p>


<h2 id="2024-10-08">2024-10-08</h2>

<strong>New fields added to Gateway-related datasets in Cloudflare Logs</strong>

<p>Cloudflare has introduced new fields to two Gateway-related datasets in Cloudflare Logs:</p>
<ul>
<li>
<p><strong>Gateway HTTP</strong>: <code>ApplicationIDs</code>, <code>ApplicationNames</code>, <code>CategoryIDs</code>, <code>CategoryNames</code>, <code>DestinationIPContinentCode</code>, <code>DestinationIPCountryCode</code>, <code>ProxyEndpoint</code>, <code>SourceIPContinentCode</code>, <code>SourceIPCountryCode</code>, <code>VirtualNetworkID</code>, and <code>VirtualNetworkName</code>.</p>
</li>
<li>
<p><strong>Gateway Network</strong>: <code>ApplicationIDs</code>, <code>ApplicationNames</code>, <code>DestinationIPContinentCode</code>, <code>DestinationIPCountryCode</code>, <code>ProxyEndpoint</code>, <code>SourceIPContinentCode</code>, <code>SourceIPCountryCode</code>, <code>TransportProtocol</code>, <code>VirtualNetworkID</code>, and <code>VirtualNetworkName</code>.</p>
</li>
</ul>


