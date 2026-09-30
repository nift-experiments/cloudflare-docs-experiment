---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/analytics/4/
  description: '2026-02-03'
  full_title: Analytics changelog - page 4 | Cloudflare Docs
  head_html: <title>Analytics changelog - page 4 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-02-03"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/analytics/4/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Analytics changelog - page 4"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-02-03"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/analytics/4/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/analytics/4/#page","headline":"Analytics changelog - page 4 | Cloudflare Docs","description":"2026-02-03","url":"https://developers.cloudflare.com/changelog/product-group/analytics/4/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/analytics/4/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="threat-actor-identification-with-also-known-as-aliases"><a href="/changelog/post/2026-02-03-threat-actor-name-mapping/">Threat actor identification with "also known as" aliases</a></h2>
<p><em>2026-02-03</em></p>
<p>Identifying threat actors can be challenging, because naming conventions often vary across the security industry. To simplify your research, <strong>Cloudflare Threat Events</strong> now include an <strong>Also known as</strong> field, providing a list of common aliases and industry-standard names for the groups we track.</p>
<p>This new field is available in both the Cloudflare dashboard and via the API. In the dashboard, you can view these aliases by expanding the event details side panel (under the <strong>Attacker</strong> field) or by adding it as a column in your configurable table view.</p>
<h4 id="2026-02-03-threat-actor-name-mapping-key-benefits">Key benefits</h4>
<ul>
<li>Easily map Cloudflare-tracked actors to the naming conventions used by other vendors without manual cross-referencing.</li>
<li>Quickly identify if a detected threat actor matches a group your team is already monitoring via other intelligence feeds.</li>
</ul>
<p>For more information on how to access this data, refer to the <a href="https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/">Threat Events API documentation</a>.</p>


<h2 id="network-services-navigation-update"><a href="/changelog/post/2026-01-15-networking-navigation-update/">Network Services navigation update</a></h2>
<p><em>2026-01-15</em></p>
<p>The Network Services menu structure in Cloudflare's dashboard has been updated to reflect solutions and capabilities instead of product names. This will make it easier for you to find what you need and better reflects how our services work together.</p>
<p>Your existing configurations will remain the same, and you will have access to all of the same features and functionality.</p>
<p>The changes visible in your dashboard may vary based on the products you use. Overall, changes relate to <a href="https://developers.cloudflare.com/magic-transit/">Magic Transit</a>, <a href="https://developers.cloudflare.com/magic-wan/">Magic WAN</a>, and <a href="https://developers.cloudflare.com/cloudflare-network-firewall/">Magic Firewall</a>.</p>
<p><strong>Summary of changes:</strong></p>
<ul>
<li>A new <strong>Overview</strong> page provides access to the most common tasks across Magic Transit and Magic WAN.</li>
<li>Product names have been removed from top-level navigation.</li>
<li>Magic Transit and Magic WAN configuration is now organized under <strong>Routes</strong> and <strong>Connectors</strong>. For example, you will find IP Prefixes under <strong>Routes</strong>, and your GRE/IPsec Tunnels under <strong>Connectors.</strong></li>
<li>Magic Firewall policies are now called <strong>Firewall Policies.</strong></li>
<li>Magic WAN Connectors and Connector On-Ramps are now referenced in the dashboard as <strong>Appliances</strong> and <strong>Appliance profiles.</strong> They can be found under <strong>Connectors &gt; Appliances.</strong></li>
<li>Network analytics, network health, and real-time analytics are now available under <strong>Insights.</strong></li>
<li>Packet Captures are found under <strong>Insights &gt; Diagnostics.</strong></li>
<li>You can manage your Sites from <strong>Insights &gt; Network health.</strong></li>
<li>You can find Magic Network Monitoring under <strong>Insights &gt; Network flow</strong>.</li>
</ul>
<p>If you would like to provide feedback, complete <a href="https://forms.gle/htWyjRsTjw1usdis5">this form</a>. You can also find these details in the January 7, 2026 email titled <strong>[FYI] Upcoming Network Services Dashboard Navigation Update</strong>.</p>
<p>Preview:
<img src="/assets/upstream/images/changelog/cloudflare-network-firewall/networking-overview-and-navigation.png" alt="Networking Navigation" /></p>


<h2 id="url-scanner-now-supports-pdf-report-downloads"><a href="/changelog/post/2026-01-14-Download-URL-Scanner-Report-PDF/">URL Scanner now supports PDF report downloads</a></h2>
<p><em>2026-01-14</em></p>
<p>We have expanded the reporting capabilities of the Cloudflare URL Scanner. In addition to existing JSON and HAR exports, users can now generate and download a <strong>PDF report</strong> directly from the Cloudflare dashboard.
This update streamlines how security analysts can share findings with stakeholders who may not have access to the Cloudflare dashboard or specialized tools to parse JSON and HAR files.</p>
<p><strong>Key Benefits:</strong></p>
<ul>
<li>Consolidate scan results, including screenshots, security signatures, and metadata, into a single, portable document</li>
<li>Easily share professional-grade summaries with non-technical stakeholders or legal teams for faster incident response</li>
</ul>
<p><strong>What’s new:</strong></p>
<ul>
<li><strong>PDF Export Button:</strong> A new download option is available in the URL Scanner results page within the Cloudflare dashboard</li>
<li><strong>Unified Documentation:</strong> Access all scan details—from high-level summaries to specific security flags—in one offline-friendly file</li>
</ul>
<p>To get started with the URL Scanner and explore our reporting capabilities, visit the <a href="https://developers.cloudflare.com/api/resources/url_scanner/">URL Scanner API documentation</a>.</p>
<hr />


<h2 id="cloudflare-threat-events-now-support-stix2-format"><a href="/changelog/post/2026-01-12-STIX2-available-for-threat-events-api/">Cloudflare Threat Events now support STIX2 format</a></h2>
<p><em>2026-01-12</em></p>
<p>We are excited to announce that <strong>Cloudflare Threat Events</strong> now supports the <strong>STIX2 (Structured Threat Information Expression)</strong> format. This was a highly requested feature designed to streamline how security teams consume and act upon our threat intelligence.</p>
<p>By adopting this industry-standard format, you can now integrate Cloudflare's threat events data more effectively into your existing security ecosystem.</p>
<h4 id="2026-01-12-STIX2-available-for-threat-events-api-key-benefits">Key benefits</h4>
<ul>
<li>
<p>Eliminate the need for custom parsers, as STIX2 allows for &quot;out of the box&quot; ingestion into major <strong>Threat Intel Platforms (TIPs)</strong>, <strong>SIEMs</strong>, and <strong>SOAR</strong> tools.</p>
</li>
<li>
<p>STIX2 provides a standardized way to represent relationships between indicators, sightings, and threat actors, giving your analysts a clearer picture of the threat landscape.</p>
</li>
</ul>
<p>For technical details on how to query events using this format, please refer to our <a href="https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/list/">Threat Events API Documentation</a>.</p>
<hr />


<h2 id="workers-analytics-engine-sql-now-supports-filtering-using-having-and-like"><a href="/changelog/post/2026-01-07-analytics-engine-support-for-like-and-having/">Workers Analytics Engine SQL now supports filtering using HAVING and LIKE</a></h2>
<p><em>2026-01-07</em></p>
<p>You can now use the <code>HAVING</code> clause and <code>LIKE</code> pattern matching operators in <a href="https://developers.cloudflare.com/analytics/analytics-engine/">Workers Analytics Engine</a>.</p>
<p>Workers Analytics Engine allows you to ingest and store high-cardinality data at scale and query your data through a simple SQL API.</p>
<h4 id="2026-01-07-analytics-engine-support-for-like-and-having-filtering-using-having">Filtering using <code>HAVING</code></h4>
<p>The <code>HAVING</code> clause complements the <code>WHERE</code> clause by enabling you to filter groups based on aggregate values. While <code>WHERE</code> filters rows before aggregation, <code>HAVING</code> filters groups after aggregation is complete.</p>
<p>You can use <code>HAVING</code> to filter groups where the average exceeds a threshold:</p>
<pre tabindex="0"><code class="language-sql">SELECT&#10;    blob1 AS probe_name,&#10;    avg(double1) AS average_temp&#10;FROM temperature_readings&#10;GROUP BY probe_name&#10;HAVING average_temp &gt; 10&#10;</code></pre>
<p>You can also filter groups based on aggregates such as the number of items in the group:</p>
<pre tabindex="0"><code class="language-sql">SELECT&#10;    blob1 AS probe_name,&#10;    count() AS num_readings&#10;FROM temperature_readings&#10;GROUP BY probe_name&#10;HAVING num_readings &gt; 100&#10;</code></pre>
<h4 id="2026-01-07-analytics-engine-support-for-like-and-having-pattern-matching-using-like">Pattern matching using <code>LIKE</code></h4>
<p>The new pattern matching operators enable you to search for strings that match specific patterns using wildcard characters:</p>
<ul>
<li><code>LIKE</code> - case-sensitive pattern matching</li>
<li><code>NOT LIKE</code> - case-sensitive pattern exclusion</li>
<li><code>ILIKE</code> - case-insensitive pattern matching</li>
<li><code>NOT ILIKE</code> - case-insensitive pattern exclusion</li>
</ul>
<p>Pattern matching supports two wildcard characters: <code>%</code> (matches zero or more characters) and <code>_</code> (matches exactly one character).</p>
<p>You can match strings starting with a prefix:</p>
<pre tabindex="0"><code class="language-sql">SELECT *&#10;FROM logs&#10;WHERE blob1 LIKE &#x27;error%&#x27;&#10;</code></pre>
<p>You can also match file extensions (case-insensitive):</p>
<pre tabindex="0"><code class="language-sql">SELECT *&#10;FROM requests&#10;WHERE blob2 ILIKE &#x27;%.jpg&#x27;&#10;</code></pre>
<p>Another example is excluding strings containing specific text:</p>
<pre tabindex="0"><code class="language-sql">SELECT *&#10;FROM events&#10;WHERE blob3 NOT ILIKE &#x27;%debug%&#x27;&#10;</code></pre>
<h4 id="2026-01-07-analytics-engine-support-for-like-and-having-ready-to-get-started">Ready to get started?</h4>
<p>Learn more about the <a href="/analytics/analytics-engine/sql-reference/statements/#having-clause"><code>HAVING</code> clause</a> or <a href="/analytics/analytics-engine/sql-reference/operators/#pattern-matching-operators">pattern matching operators</a> in the Workers Analytics Engine SQL reference documentation.</p>


<h2 id="improved-accuracy-of-cached-request-classification-in-analytics"><a href="/changelog/post/2025-12-18-cached-request-classification/">Improved accuracy of cached request classification in analytics</a></h2>
<p><em>2025-12-18</em></p>
<p>The cached/uncached classification logic used in Zone Overview analytics has been updated to improve accuracy.</p>
<p>Previously, requests were classified as &quot;cached&quot; based on an overly broad condition that included blocked 403 responses, Snippets requests, and other non-cache request types. This caused inflated cache hit ratios — in some cases showing near-100% cached — and affected approximately 15% of requests classified as cached in rollups.</p>
<p>The condition has been removed from the Zone Overview page. Cached/uncached classification now aligns with the heuristics used in <a href="/analytics/account-and-zone-analytics/zone-analytics/">HTTP Analytics</a>, so only requests genuinely served from cache are counted as cached.</p>
<p><strong>What changed:</strong></p>
<ul>
<li><strong>Zone Overview</strong> — Cache ratios now reflect actual cache performance.</li>
<li><strong>HTTP Analytics</strong> — No change. HTTP Analytics already used the correct classification logic.</li>
<li><strong>Historical data</strong> — This fix applies to new requests only. Previously logged data is not retroactively updated.</li>
</ul>


<h2 id="sentinelone-as-logpush-destination"><a href="/changelog/post/2025-12-11-sentinelone-destination/">SentinelOne as Logpush destination</a></h2>
<p><em>2025-12-11</em></p>
<p>Cloudflare Logpush now supports <strong>SentinelOne</strong> as a native destination.</p>
<p>Logs from Cloudflare can be sent to <a href="https://www.sentinelone.com/">SentinelOne AI SIEM</a> via <a href="/logs/logpush/">Logpush</a>. The destination can be configured through the Logpush UI in the Cloudflare dashboard or by using the <a href="/api/resources/logpush/subresources/jobs/">Logpush API</a>.</p>
<p>For more information, refer to the <a href="/logs/logpush/logpush-job/enable-destinations/sentinelone/">Destination Configuration</a> documentation.</p>


<h2 id="cloud-services-observability-in-cloudflare-radar"><a href="/changelog/post/2025-11-24-radar-cloud-observability/">Cloud Services Observability in Cloudflare Radar</a></h2>
<p><em>2025-11-24</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> introduces HTTP Origins insights, providing visibility into the status of traffic between Cloudflare's global network and cloud-based origin infrastructure.</p>
<p>The new <a href="/api/resources/radar/subresources/origins/"><code>Origins</code></a> API provides provides the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/origins/methods/list/"><code>/origins</code></a> - Lists all origins (cloud providers and associated regions).</li>
<li><a href="/api/resources/radar/subresources/origins/methods/get/"><code>/origins/{origin}</code></a> - Retrieves information about a specific origin (cloud provider).</li>
<li><a href="/api/resources/radar/subresources/origins/methods/timeseries/"><code>/origins/timeseries</code></a> - Retrieves normalized time series data for a specific origin, including the following metrics:
<ul>
<li><code>REQUESTS</code>: Number of requests</li>
<li><code>CONNECTION_FAILURES</code>: Number of connection failures</li>
<li><code>RESPONSE_HEADER_RECEIVE_DURATION</code>: Duration of the response header receive</li>
<li><code>TCP_HANDSHAKE_DURATION</code>: Duration of the TCP handshake</li>
<li><code>TCP_RTT</code>: TCP round trip time</li>
<li><code>TLS_HANDSHAKE_DURATION</code>: Duration of the TLS handshake</li>
</ul>
</li>
<li><a href="/api/resources/radar/subresources/origins/methods/summary/"><code>/origins/summary</code></a> - Retrieves HTTP requests to origins summarized by a dimension.</li>
<li><a href="/api/resources/radar/subresources/origins/methods/timeseries_groups/"><code>/origins/timeseries_groups</code></a> - Retrieves timeseries data for HTTP requests to origins grouped by a dimension.</li>
</ul>
<p>The following dimensions are available for the <code>summary</code> and <code>timeseries_groups</code> endpoints:</p>
<ul>
<li><code>region</code>: Origin region</li>
<li><code>success_rate</code>: Success rate of requests (2XX versus 5XX response codes)</li>
<li><code>percentile</code>: Percentiles of metrics listed above</li>
</ul>
<p>Additionally, the <a href="/api/resources/radar/subresources/annotations/"><code>Annotations</code></a> and <a href="/api/resources/radar/subresources/traffic_anomalies/"><code>Traffic Anomalies</code></a> APIs have been extended to support origin outages and anomalies, enabling automated detection and alerting for origin infrastructure issues.</p>
<p><img src="/assets/upstream/images/radar/cloud-service-status.png" alt="Screenshot of the cloud service status heatmap" /></p>
<p>Check out the <a href="https://radar.cloudflare.com/cloud-observatory">new Radar page</a>.</p>


<h2 id="threat-insights-are-now-available-in-the-threat-events-platform"><a href="/changelog/post/2025-11-21-Threat-Events-now-show-events-insights/">Threat insights are now available in the Threat Events platform</a></h2>
<p><em>2025-11-21</em></p>
<p>The threat events platform now has threat insights available for some relevant parent events. Threat intelligence analyst users can access these insights for their threat hunting activity.
Insights are also highlighted in the Cloudflare dashboard by a small <code>lightning icon</code> and the insights can refer to multiple, connected events, potentially part of the same attack or campaign and associated with the same threat actor.</p>
<p>For more information, refer to <a href="/security-center/cloudforce-one/#analyze-threat-events">Analyze threat events</a>.</p>


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


<h2 id="dex-logpush-jobs"><a href="/changelog/post/2025-11-12-dex-logpush-jobs/">DEX Logpush jobs</a></h2>
<p><em>2025-11-12</em></p>
<p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into WARP device metrics, connectivity, and network performance across your Cloudflare SASE deployment.</p>
<p>We've released four new WARP and DEX device data sets that can be exported via <a href="/cloudflare-one/insights/logs/logpush/">Cloudflare Logpush</a>. These Logpush data sets can be exported to R2, a cloud bucket, or a SIEM to build a customized logging and analytics experience.</p>
<ol>
<li><a href="/logs/logpush/logpush-job/datasets/account/dex_application_tests/">DEX Application Tests</a></li>
<li><a href="/logs/logpush/logpush-job/datasets/account/dex_device_state_events/">DEX Device State Events</a></li>
<li><a href="/logs/logpush/logpush-job/datasets/account/warp_config_changes/">WARP Config Changes</a></li>
<li><a href="/logs/logpush/logpush-job/datasets/account/warp_toggle_changes/">WARP Toggle Changes</a></li>
</ol>
<p>To create a new DEX or WARP Logpush job, customers can go to the account level of the Cloudflare dashboard &gt; Analytics &amp; Logs &gt; Logpush to get started.</p>
<p><img src="/assets/upstream/images/changelog/dex/dex_logpush_datasets.png" alt="DEX logpush job creation dashboard" /></p>


<h2 id="more-sql-aggregate-date-and-time-functions-available-in-workers-analytics-engine"><a href="/changelog/post/2025-11-12-analytics-engine-further-sql-enhancements/">More SQL aggregate, date and time functions available in Workers Analytics Engine</a></h2>
<p><em>2025-11-12</em></p>
<p>You can now perform more powerful queries directly in <a href="https://developers.cloudflare.com/analytics/analytics-engine/">Workers Analytics Engine</a> with a major expansion of our SQL function library.</p>
<p>Workers Analytics Engine allows you to ingest and store high-cardinality data at scale (such as custom analytics) and query your data through a simple SQL API.</p>
<p>Today, we've expanded Workers Analytics Engine's SQL capabilities with several new functions:</p>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/aggregate-functions/"><strong>New aggregate functions:</strong></a></p>
<ul>
<li><code>countIf()</code> - count the number of rows which satisfy a provided condition</li>
<li><code>sumIf()</code> - calculate a sum from rows which satisfy a provided condition</li>
<li><code>avgIf()</code> - calculate an average from rows which satisfy a provided condition</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/date-time-functions/"><strong>New date and time functions:</strong></a></p>
<ul>
<li><code>toYear()</code></li>
<li><code>toMonth()</code></li>
<li><code>toDayOfMonth()</code></li>
<li><code>toDayOfWeek()</code></li>
<li><code>toHour()</code></li>
<li><code>toMinute()</code></li>
<li><code>toSecond()</code></li>
<li><code>toStartOfYear()</code></li>
<li><code>toStartOfMonth()</code></li>
<li><code>toStartOfWeek()</code></li>
<li><code>toStartOfDay()</code></li>
<li><code>toStartOfHour()</code></li>
<li><code>toStartOfFifteenMinutes()</code></li>
<li><code>toStartOfTenMinutes()</code></li>
<li><code>toStartOfFiveMinutes()</code></li>
<li><code>toStartOfMinute()</code></li>
<li><code>today()</code></li>
<li><code>toYYYYMM()</code></li>
</ul>
<h4 id="2025-11-12-analytics-engine-further-sql-enhancements-ready-to-get-started">Ready to get started?</h4>
Whether you're building usage-based billing systems, customer analytics dashboards, or other custom analytics, these functions let you get the most out of your data. [Get started ](/analytics/analytics-engine/get-started/) with Workers Analytics Engine and explore all available functions in our [SQL reference documentation](/analytics/analytics-engine/sql-reference/).


<h2 id="resize-your-custom-sql-window-in-log-explorer"><a href="/changelog/post/2025-11-11-resize-sql-window/">Resize your custom SQL window in Log Explorer</a></h2>
<p><em>2025-11-11</em></p>
<p>We're excited to announce a quality-of-life improvement for Log Explorer users. You can now resize the custom SQL query window to accommodate longer and more complex queries.</p>
<p>Previously, if you were writing a long custom SQL query, the fixed-size window required excessive scrolling to view the full query. This update allows you to easily drag the bottom edge of the query window to make it taller. This means you can view your entire custom query at once, improving the efficiency and experience of writing and debugging complex queries.</p>
<p>To learn more and get started, refer to the <a href="/log-explorer/">Log Explorer documentation</a>.</p>


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


<h2 id="log-explorer-now-supports-query-cancellation"><a href="/changelog/post/2025-11-04-query-cancellation/">Log Explorer now supports query cancellation</a></h2>
<p><em>2025-11-04</em></p>
<p>We're excited to announce that Log Explorer users can now cancel queries that are currently running.</p>
<p>This new feature addresses a common pain point: waiting for a long, unintended, or misconfigured query to complete before you can submit a new, correct one. With query cancellation, you can immediately stop the execution of any undesirable query, allowing you to quickly craft and submit a new query, significantly improving your investigative workflow and productivity within Log Explorer.</p>


<h2 id="log-explorer-now-shows-query-result-distribution"><a href="/changelog/post/2025-11-13-query-result-distribution/">Log Explorer now shows query result distribution</a></h2>
<p><em>2025-11-04</em></p>
<p>We're excited to announce a new feature in Log Explorer that significantly enhances how you analyze query results: the Query results distribution chart.</p>
<p>This new chart provides a graphical distribution of your results over the time window of the query. Immediately after running a query, you will see the distribution chart above your result table. This visualization allows Log Explorer users to quickly spot trends, identify anomalies, and understand the temporal concentration of log events that match their criteria. For example, you can visually confirm if a spike in traffic or errors occurred at a specific time, allowing you to focus your investigation efforts more effectively. This feature makes it faster and easier to extract meaningful insights from your vast log data.</p>
<p>The chart will dynamically update to reflect the logs matching your current query.</p>


<h2 id="report-logo-misuse-to-cloudflare-directly-from-the-brand-protection-dashboard"><a href="/changelog/post/2025-10-31-brand-protection-logo-dashboard-report-abuse/">Report logo misuse to Cloudflare directly from the Brand Protection dashboard</a></h2>
<p><em>2025-10-31</em></p>
<p>The Brand Protection logo query dashboard now allows you to use the <strong>Report to Cloudflare</strong> button to submit an Abuse report directly from the Brand Protection logo queries dashboard. While you could previously report new domains that were impersonating your brand before, now you can do the same for websites found to be using your logo without your permission. The abuse reports will be prefilled and you will only need to validate a few fields before you can click the submit button, after which our team process your request.</p>
<p>Ready to start? Check out the <a href="/security-center/brand-protection/">Brand Protection docs</a>.</p>


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


<h2 id="tld-insights-in-cloudflare-radar"><a href="/changelog/post/2025-10-27-radar-tld-insights/">TLD Insights in Cloudflare Radar</a></h2>
<p><em>2025-10-27</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> now introduces Top-Level Domain (TLD) insights, providing visibility into popularity based on the DNS magnitude metric, detailed TLD information including its type, manager, DNSSEC support, RDAP support, and WHOIS data, and trends such as DNS query volume and geographic distribution observed by the <a href="/1.1.1.1/">1.1.1.1</a> DNS resolver.</p>
<p>The following dimensions were added to the Radar DNS API, specifically, to the <a href="/api/resources/radar/subresources/dns/methods/summary_v2/"><code>/dns/summary/{dimension}</code></a> and <a href="/api/resources/radar/subresources/dns/methods/timeseries_groups_v2/"><code>/dns/timeseries_groups/{dimension}</code></a> endpoints:</p>
<ul>
<li><code>tld</code>: Top-level domain extracted from DNS queries; can also be used as a filter.</li>
<li><code>tld_dns_magnitude</code>: Top-level domain ranking by <a href="/radar/glossary#dns-magnitude">DNS magnitude</a>.</li>
</ul>
<p>And the following endpoints were added:</p>
<ul>
<li><a href="/api/resources/radar/subresources/tlds/methods/list/"><code>/tlds</code></a> - Lists all TLDs.</li>
<li><a href="/api/resources/radar/subresources/tlds/methods/get/"><code>/tlds/{tld}</code></a> - Retrieves information about a specific TLD.</li>
</ul>
<p><img src="/assets/upstream/images/radar/tld-ranking-by-dns-magnitude.png" alt="Screenshot of the TLD ranking by DNS magnitude" /></p>
<p>Learn more about the new Radar DNS insights in our <a href="https://blog.cloudflare.com/introducing-tld-insights-on-cloudflare-radar/">blog post</a>, and check out the <a href="https://radar.cloudflare.com/tlds">new Radar page</a>.</p>


<h2 id="cloudforce-one-rfi-tokens-are-now-visible-in-the-dashboard"><a href="/changelog/post/2025-10-27-RFI-Tokens-in-Dash/">Cloudforce One RFI tokens are now visible in the dashboard</a></h2>
<p><em>2025-10-27</em></p>
<p>The Requests for Information (RFI) dashboard now shows users the number of tokens used by each submitted RFI to better understand usage of tokens and how they relate to each request submitted.</p>
<p><img src="/assets/upstream/images/changelog/security-center/2025-10-24RFITokens.png" alt="Cloudforce One RFI tokens" /></p>
<p>What’s new:</p>
<ul>
<li>Users can now see the number of tokens used for a submitted request for information.</li>
<li>Users can see the remaining tokens allocated to their account for the quarter.</li>
<li>Users can only select the Routine priority for the <code>Strategic Threat Research</code> request type.</li>
</ul>
<p>Cloudforce One subscribers can try it now in <a href="https://dash.cloudflare.com/?to=/:account/security-center/threat-intelligence/requests">Application Security &gt; Threat Intelligence &gt; Requests for Information</a>.</p>


<h2 id="new-application-security-reports-closed-beta"><a href="/changelog/post/2025-10-17-app-sec-reports/">New Application Security reports (Closed Beta)</a></h2>
<p><em>2025-10-17</em></p>
<p>Cloudflare's new <strong>Application Security report</strong>, currently in Closed Beta, is now available in the dashboard.</p>
<div class="nb-dash-button"></div>
<p>The reports are generated monthly and provide cyber security insights trends for all of the Enterprise zones in your Cloudflare account.</p>
<p>The reports also include an industry benchmark, comparing your cyber security landscape to peers in your industry.</p>
<p><img src="/assets/upstream/images/changelog/security-center/2025-10-17-application-security-report-mock-data.png" alt="Application Security report mock data" /></p>
<p>Learn more about the reports by referring to the <a href="/analytics/account-and-zone-analytics/app-security-reports/">Security Reports documentation</a>.</p>
<p>Use the feedback survey link at the top of the page to help us improve the reports.</p>
<p><img src="/assets/upstream/images/changelog/security-center/2025-10-17-report-feedback-survey.png" alt="Application Security report survey" /></p>


<h2 id="expanded-ct-log-activity-insights-on-cloudflare-radar"><a href="/changelog/post/2025-10-09-radar-ct-log-activity-insights/">Expanded CT log activity insights on Cloudflare Radar</a></h2>
<p><em>2025-10-09</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> has expanded its Certificate Transparency (CT) log insights with new stats that provide greater visibility into log activity:</p>
<ul>
<li><strong>Log growth rate</strong>: The average throughput of the CT log over the past 7 days, measured in certificates per hour.</li>
<li><strong>Included certificate count</strong>: The total number of certificates already included in this CT log.</li>
<li><strong>Eligible-for-inclusion certificate count</strong>: The number of certificates eligible for inclusion in this log but not yet included. This metric is based on certificates signed by trusted root CAs within the log’s accepted date range.</li>
<li><strong>Last update</strong>: The timestamp of the most recent update to the CT log.</li>
</ul>
<p>These new statistics have been added to the response of the <a href="/api/resources/radar/subresources/ct/subresources/logs/methods/get/">Get Certificate Log Details</a> API endpoint, and are displayed on the <a href="https://radar.cloudflare.com/certificate-transparency/log/nimbus2025#log-activity">CT log information page</a>.</p>
<p><img src="/assets/upstream/images/radar/ct-log-activity.png" alt="Screenshot of the CT log activity card on the CT log information page" /></p>


<h2 id="browser-support-detection-for-pq-encryption-on-cloudflare-radar"><a href="/changelog/post/2025-10-06-radar-pq-encryption-test/">Browser Support Detection for PQ Encryption on Cloudflare Radar</a></h2>
<p><em>2025-10-06</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> now includes browser detection for Post-quantum (PQ) encryption.
The <a href="https://radar.cloudflare.com/adoption-and-usage#post-quantum-encryption">Post-quantum encryption card</a> now checks whether a user’s browser supports post-quantum encryption.
If support is detected, information about the key agreement in use is displayed.</p>
<p><img src="/assets/upstream/images/radar/pq-encryption-test.png" alt="Screenshot of the PQ encryption browser support test on the Adoption &amp; Usage page" /></p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/analytics/3/">Previous</a><span>Page 4 of 6</span><a class="pagination-next" rel="next" href="/changelog/product-group/analytics/5/">Next</a></nav>
