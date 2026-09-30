<h1 id="changelog">Changelog</h1>

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


<h2 id="generate-citations-on-cloudflare-radar"><a href="/changelog/post/2026-04-14-radar-citations/">Generate citations on Cloudflare Radar</a></h2>
<p><em>2026-04-14</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> shareable widgets now include a <strong>generate citation</strong> action, making it easier to reference <a href="https://radar.cloudflare.com">Cloudflare Radar</a> data in research papers and other publications.</p>
<p><img src="/assets/upstream/images/radar/citation-action-icon.png" alt="Screenshot of the generate citation icon in the widget action bar" /></p>
<p>Select the citation icon to open a modal with five supported citation styles:</p>
<ul>
<li><strong>BibTeX</strong></li>
<li><strong>APA</strong></li>
<li><strong>MLA</strong></li>
<li><strong>Chicago</strong></li>
<li><strong>RIS</strong></li>
</ul>
<p><img src="/assets/upstream/images/radar/citation-modal.png" alt="Screenshot of the citation modal with format options" /></p>
<p>Explore the feature on any shareable widget at <a href="https://radar.cloudflare.com">Cloudflare Radar</a>.</p>


<h2 id="real-time-alerts-and-daily-digests-for-threat-events"><a href="/changelog/post/2026-04-08-threat-events-notification/">Real-time alerts and daily digests for Threat Events</a></h2>
<p><em>2026-04-08</em></p>
<p>You can now automate your threat monitoring by setting up custom alerts in your saved views. Instead of manually checking the dashboard for updates, you can subscribe to notifications that trigger whenever new data matches your specific filter sets, like new activity associated to a particular threat actor or spikes in activity within your industry.</p>
<h4 id="2026-04-08-threat-events-notification-stay-ahead-of-emerging-threats">Stay ahead of emerging threats</h4>
<p>By linking your saved views to the Cloudflare Notifications Center, you can ensure the right information reaches your team at the right time.</p>
<ul>
<li>
<p><strong>Immediate Alerts</strong>: receive real-time notifications the moment a critical event is detected that matches your saved criteria. This is essential for high-priority monitoring, such as tracking active campaigns from specific APT groups.</p>
</li>
<li>
<p><strong>Daily Digests</strong>: opt for a summarized report delivered once a day. This is ideal for maintaining situational awareness of broader trends, like regional activity shifts or industry-wide threat landscapes, without cluttering your inbox.</p>
</li>
</ul>
<p><img src="/assets/upstream/images/changelog/security-center/threat-events-notifications.png" alt="Threat Events notifications" /></p>
<h4 id="2026-04-08-threat-events-notification-how-to-get-started">How to get started</h4>
<p>To set up an alert, go to <strong>Application Security</strong> &gt; <strong>Threat Intelligence</strong> &gt; <strong>Threat Events</strong>. From there:</p>
<ol>
<li>Choose your datasets and apply your desired filters and select <strong>Save View</strong> (or select an existing one).</li>
<li>Open the <strong>Manage Saved Views</strong> menu.</li>
<li>Select <strong>Add Alert</strong> next to your chosen view to configure your notification preferences in the Cloudflare dashboard.</li>
</ol>
<p>For more technical details on configuring notifications, refer to the <a href="/security-center/cloudforce-one/">Threat Events documentation</a>.</p>


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


<h2 id="routing-section-expansion-on-cloudflare-radar"><a href="/changelog/post/2026-04-01-radar-routing-section/">Routing Section Expansion on Cloudflare Radar</a></h2>
<p><em>2026-04-01</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> now features an expanded <a href="https://radar.cloudflare.com/routing">Routing section</a> with dedicated sub-pages, providing a more organized and in-depth view of the global routing ecosystem. This restructuring lays the groundwork for additional routing features and widgets coming in the near future.</p>
<h4 id="2026-04-01-radar-routing-section-dedicated-sub-pages">Dedicated sub-pages</h4>
<p>The single Routing page has been split into three focused sub-pages:</p>
<ul>
<li><a href="https://radar.cloudflare.com/routing"><strong>Overview</strong></a> — Routing statistics, IP address space trends, BGP announcements, and the new Top 100 ASes ranking.</li>
<li><a href="https://radar.cloudflare.com/routing/rpki"><strong>RPKI</strong></a> — RPKI validation status, ASPA deployment trends, and per-ASN ASPA provider details.</li>
<li><a href="https://radar.cloudflare.com/routing/anomalies"><strong>Anomalies</strong></a> — BGP route leaks, origin hijacks, and Multi-Origin AS (MOAS) conflicts.</li>
</ul>
<p><img src="/assets/upstream/images/radar/routing-section-menu.png" alt="Screenshot of the routing section menu" /></p>
<h4 id="2026-04-01-radar-routing-section-new-widgets">New widgets</h4>
<p>The routing overview now includes a <strong>Top 100 ASes</strong> table ranking autonomous systems by customer cone size, IPv4 address space, or IPv6 address space. Users can switch between rankings using a segmented control.</p>
<p><img src="/assets/upstream/images/radar/top-100-ases-table.png" alt="Screenshot of the top-100 ASes table" /></p>
<p>The RPKI sub-page introduces a <strong>RPKI validation</strong> view for per-ASN pages, showing prefixes grouped by RPKI validation status (Valid, Invalid, Unknown) with visibility scores.</p>
<p><img src="/assets/upstream/images/radar/rpki-validation-view.png" alt="Screenshot of the RPKI validation view" /></p>
<h4 id="2026-04-01-radar-routing-section-improved-ip-address-space-chart">Improved IP address space chart</h4>
<p>The <a href="https://radar.cloudflare.com/routing">IP address space</a> chart now displays both IPv4 and IPv6 trends stacked vertically and is available on global, country, and AS views.</p>
<p><img src="/assets/upstream/images/radar/combined-ipv4-ipv6-space.png" alt="Screenshot of the IPv4 and IPv6 combined IP space chart" /></p>
<p>Check out the <a href="https://radar.cloudflare.com/routing">Radar routing section</a> to explore the data, and stay tuned for more routing insights coming soon.</p>


<h2 id="url-scanner-improvements-on-cloudflare-radar"><a href="/changelog/post/2026-03-26-url-scanner-improvements/">URL Scanner improvements on Cloudflare Radar</a></h2>
<p><em>2026-03-26</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> ships several improvements to the <a href="https://radar.cloudflare.com/scan">URL Scanner</a> that make scan reports more informative and easier to share:</p>
<ul>
<li><strong>Live screenshots</strong> — the summary card now includes an option to capture a live screenshot of the scanned URL on demand using the <a href="/browser-run/">Browser Rendering</a> API.</li>
<li><strong>Save as PDF</strong> — a new button generates a print-optimized document aggregating all tab contents (Summary, Security, Network, Behavior, and Indicators) into a single file.</li>
<li><strong>Download as JSON</strong> — raw scan data is available as a JSON download for programmatic use.</li>
<li><strong>Redesigned summary layout</strong> — page information and security details are now displayed side by side with the screenshot, with a layout that adapts to narrower viewports.</li>
<li><strong>File downloads</strong> — downloads are separated into a dedicated card with expandable rows showing each file's source URL and SHA256 hash.</li>
<li><strong>Detailed IP address data</strong> — the Network tab now includes additional detail per IP address observed during the scan.</li>
</ul>
<p><img src="/assets/upstream/images/radar/url-scanner-summary-redesign.png" alt="Screenshot of the redesigned URL Scanner summary on Radar" /></p>
<p>Explore these improvements on the <a href="https://radar.cloudflare.com/scan">Cloudflare Radar URL Scanner</a>.</p>


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


<h2 id="real-time-logo-match-preview"><a href="/changelog/post/2026-03-18-brand-protection-logo-match-preview/">Real-time logo match preview</a></h2>
<p><em>2026-03-18</em></p>
<p>We are introducing <strong>Logo Match Preview</strong>, bringing the same pre-save visibility to visual assets that was previously only available for string-based queries. This update allows you to fine-tune your brand detection strategy before committing to a live monitor.</p>
<h4 id="2026-03-18-brand-protection-logo-match-preview-what-s-new">What’s new:</h4>
<ul>
<li>Upload your brand logo and immediately see a sample of potential matches from recently detected sites before finalizing the query</li>
<li>Adjust your similarity score (from 75% to 100%) and watch the results refresh in real-time to find the balance between broad detection and noise reduction</li>
<li>Review the specific logos triggered by your current settings to ensure your query is capturing the right level of brand infringement</li>
</ul>
<p>If you are ready to test your brand assets, go to the <a href="https://developers.cloudflare.com/security-center/brand-protection/">Brand Protection dashboard</a> to try the new preview tool.</p>


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


<h2 id="region-filtering-as-traffic-volume-and-navigation-improvements-on-cloudflare-radar"><a href="/changelog/post/2026-03-06-radar-region-filtering-traffic-volume-navigation/">Region Filtering, AS Traffic Volume, and Navigation Improvements on Cloudflare Radar</a></h2>
<p><em>2026-03-06</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> ships several new features that improve the flexibility and usability of the platform, as well as visibility into what is happening on the Internet.</p>
<h4 id="2026-03-06-radar-region-filtering-traffic-volume-navigation-region-filtering">Region filtering</h4>
<p>All location-aware pages now support filtering by region, including continents, geographic subregions (<a href="https://radar.cloudflare.com/middle-east">Middle East</a>, <a href="https://radar.cloudflare.com/eastern-asia">Eastern Asia</a>, etc.), political regions (<a href="https://radar.cloudflare.com/european-union">EU</a>, <a href="https://radar.cloudflare.com/african-union">African Union</a>), and US Census regions/divisions (for example, <a href="https://radar.cloudflare.com/traffic/us-new-england">New England</a>, <a href="https://radar.cloudflare.com/traffic/us-northeast">US Northeast</a>).</p>
<p><img src="/assets/upstream/images/radar/region-filtering-middle-east.png" alt="Screenshot of region filtering on Radar - Middle east" /></p>
<h4 id="2026-03-06-radar-region-filtering-traffic-volume-navigation-traffic-volume-by-top-autonomous-systems-and-locations">Traffic volume by top autonomous systems and locations</h4>
<p>A new traffic volume view shows the top autonomous systems and countries/territories for a given location. This is useful for quickly determining which network providers in a location may be experiencing connectivity issues, or how traffic is distributed across a region.</p>
<p><img src="/assets/upstream/images/radar/traffic-volume-top-as-us.png" alt="Screenshot of traffic volume by top autonomous systems in US" /></p>
<p>The new AS and location dimensions have also been added to the <a href="https://radar.cloudflare.com/explorer">Data Explorer</a> for the HTTP, DNS, and NetFlows datasets. Combined with other available filters, this provides a powerful tool for generating unique insights.</p>
<p><img src="/assets/upstream/images/radar/data-explorer-top-as-pt.png" alt="Screenshot of AS and location dimensions in Data Explorer" /></p>
<p>Finally, breadcrumb navigation is now available on most pages, allowing easier navigation between parent and related pages.</p>
<p>Check out these features on <a href="https://radar.cloudflare.com">Cloudflare Radar</a>.</p>


<h2 id="dismiss-and-filter-matches-in-brand-protection"><a href="/changelog/post/2026-03-06-brand-protection-dismiss-match/">Dismiss and filter matches in Brand Protection</a></h2>
<p><em>2026-03-06</em></p>
<p>We have introduced new triage controls to help you manage your Brand Protection results more efficiently. You can now clear out the noise by dismissing matches while maintaining full visibility into your historical decisions.</p>
<h4 id="2026-03-06-brand-protection-dismiss-match-what-s-new">What's new</h4>
<ul>
<li><strong>Dismiss matches</strong>: Users can now mark specific results as dismissed if they are determined to be benign or false positives, removing them from the primary triage view.</li>
<li><strong>Show/Hide toggle</strong>: A new visibility control allows you to instantly switch between viewing only active matches and including previously dismissed ones.</li>
<li><strong>Persistent review states</strong>: Dismissed status is saved across sessions, ensuring that your workspace remains organized and focused on new or high-priority threats.</li>
</ul>
<h4 id="2026-03-06-brand-protection-dismiss-match-key-benefits-of-the-dismiss-match-functionality">Key benefits of the dismiss match functionality:</h4>
<ul>
<li>Reduce alert fatigue by hiding known-safe results, allowing your team to focus exclusively on unreviewed or high-risk infringements.</li>
<li>Auditability and recovery through the visibility toggle, ensuring that no match is ever truly &quot;lost&quot; and can be re-evaluated if a site's content changes.</li>
<li>Improved collaboration as your team members can see which matches have already been vetted and dismissed by others.</li>
</ul>
<p>Ready to clean up your match queue? Learn more in our <a href="/security-center/brand-protection/">Brand Protection documentation</a>.</p>


<h2 id="network-quality-test-on-cloudflare-radar"><a href="/changelog/post/2026-03-03-radar-network-quality-test/">Network Quality Test on Cloudflare Radar</a></h2>
<p><em>2026-03-03</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> now includes a <a href="https://radar.cloudflare.com/speedtest">Network Quality Test</a> page. The tool measures Internet connection quality and performance, showing connection details such as IP address, server location, network (ASN), and IP version. For more detailed speed test results, the page links to <a href="https://speed.cloudflare.com/">speed.cloudflare.com</a>.</p>
<p><img src="/assets/upstream/images/radar/network-quality-test.png" alt="Screenshot of the Network Quality Test page on Radar" /></p>


<h2 id="post-quantum-encryption-and-key-transparency-on-cloudflare-radar"><a href="/changelog/post/2026-02-27-radar-pq-key-transparency/">Post-Quantum Encryption and Key Transparency on Cloudflare Radar</a></h2>
<p><em>2026-02-27</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> now tracks post-quantum encryption support on origin servers, provides a tool to test any host for post-quantum compatibility, and introduces a Key Transparency dashboard for monitoring end-to-end encrypted messaging audit logs.</p>
<h4 id="2026-02-27-radar-pq-key-transparency-post-quantum-origin-support">Post-quantum origin support</h4>
<p>The new <a href="/api/resources/radar/subresources/post_quantum/"><code>Post-Quantum</code></a> API provides the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/post_quantum/subresources/tls/methods/support/"><code>/post_quantum/tls/support</code></a> - Tests whether a host supports post-quantum TLS key exchange.</li>
<li><a href="/api/resources/radar/subresources/post_quantum/methods/summary/"><code>/post_quantum/origin/summary/{dimension}</code></a> - Returns origin post-quantum data summarized by key agreement algorithm.</li>
<li><a href="/api/resources/radar/subresources/post_quantum/methods/timeseries_groups/"><code>/post_quantum/origin/timeseries_groups/{dimension}</code></a> - Returns origin post-quantum timeseries data grouped by key agreement algorithm.</li>
</ul>
<p>The new <a href="https://radar.cloudflare.com/post-quantum">Post-Quantum Encryption</a> page shows the share of customer origins supporting <a href="/ssl/post-quantum-cryptography/pqc-support/#x25519mlkem768">X25519MLKEM768</a>, derived from daily automated TLS scans of TLS 1.3-compatible origins. The scanner tests for algorithm support rather than the origin server's configured preference.</p>
<p><img src="/assets/upstream/images/radar/pq-origin-support.png" alt="Screenshot of the origin post-quantum support graph on Radar" /></p>
<p>A host test tool allows checking any publicly accessible website for post-quantum encryption compatibility. Enter a hostname and optional port to see whether the server negotiates a post-quantum key exchange algorithm.</p>
<p><img src="/assets/upstream/images/radar/pq-host-test.png" alt="Screenshot of the post-quantum host test tool on Radar" /></p>
<h4 id="2026-02-27-radar-pq-key-transparency-key-transparency">Key Transparency</h4>
<p>A new <a href="https://radar.cloudflare.com/key-transparency">Key Transparency</a> section displays the audit status of Key Transparency logs for end-to-end encrypted messaging services. The page launches with two monitored logs: WhatsApp and Facebook Messenger Transport.</p>
<p>Each log card shows the current status, last signed epoch, last verified epoch, and the root hash of the Auditable Key Directory tree. The data is also available through the <a href="/key-transparency/api/">Key Transparency Auditor API</a>.</p>
<p><img src="/assets/upstream/images/radar/key-transparency-dashboard.png" alt="Screenshot of the Key Transparency dashboard on Radar" /></p>
<p>Learn more about these features in our <a href="https://blog.cloudflare.com/radar-origin-pq-key-transparency-aspa">blog post</a> and check out the <a href="https://radar.cloudflare.com/post-quantum">Post-Quantum Encryption</a> and <a href="https://radar.cloudflare.com/key-transparency">Key Transparency</a> pages to explore the data.</p>


<h2 id="rpki-aspa-deployment-insights-on-cloudflare-radar"><a href="/changelog/post/2026-02-25-radar-aspa-insights/">RPKI ASPA Deployment Insights on Cloudflare Radar</a></h2>
<p><em>2026-02-25</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> now includes <a href="https://datatracker.ietf.org/doc/draft-ietf-sidrops-aspa-verification/">Autonomous System Provider Authorization (ASPA)</a> deployment insights, providing visibility into the adoption and verification of ASPA objects across the global routing ecosystem.</p>
<h4 id="2026-02-25-radar-aspa-insights-new-api-endpoints">New API endpoints</h4>
<p>The new <a href="/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/"><code>ASPA</code></a> API provides the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/snapshot/"><code>/bgp/rpki/aspa/snapshot</code></a> - Retrieves current or historical ASPA objects.</li>
<li><a href="/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/changes/"><code>/bgp/rpki/aspa/changes</code></a> - Retrieves changes to ASPA objects over time.</li>
<li><a href="/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/timeseries/"><code>/bgp/rpki/aspa/timeseries</code></a> - Retrieves ASPA object counts over time as a timeseries.</li>
</ul>
<h4 id="2026-02-25-radar-aspa-insights-new-radar-widgets">New Radar widgets</h4>
<p>The <a href="https://radar.cloudflare.com/routing">global routing page</a> now shows the ASPA deployment trend over time by counting daily ASPA objects.</p>
<p><img src="/assets/upstream/images/radar/aspa-global-trend.png" alt="Screenshot of the ASPA deployment trend chart" /></p>
<p>The global routing page also displays the most recent ASPA objects, searchable by ASN or AS name.</p>
<p><img src="/assets/upstream/images/radar/aspa-global-table.png" alt="Screenshot of the ASPA objects table" /></p>
<p>On country and region routing pages, a new widget shows the ASPA deployment rate for ASNs registered in the selected country or region.</p>
<p><img src="/assets/upstream/images/radar/aspa-germany-trend.png" alt="Screenshot of the ASPA deployment trent chart for Germany" /></p>
<p>On AS routing pages, the connectivity table now includes checkmarks for ASPA-verified upstreams. All ASPA upstreams are listed in a dedicated table, and a timeline shows ASPA changes at daily granularity.</p>
<p><img src="/assets/upstream/images/radar/aspa-asn-timeline.png" alt="Screenshot of the ASPA changes timeline on an AS routing page" /></p>
<p>Check out the <a href="https://radar.cloudflare.com/routing">Radar routing page</a> to explore the data.</p>


<h2 id="saved-views-for-threat-events"><a href="/changelog/post/2026-02-23-Saved-views-in-threat-events/">Saved views for Threat Events</a></h2>
<p><em>2026-02-23</em></p>
<p><strong>TL;DR:</strong> You can now create and save custom configurations of the Threat Events dashboard, allowing you to instantly return to specific filtered views — such as industry-specific attacks or regional Sankey flows — without manual reconfiguration.</p>
<h4 id="2026-02-23-Saved-views-in-threat-events-why-this-matters">Why this matters</h4>
<p>Threat intelligence is most effective when it is personalized. Previously, analysts had to manually re-apply complex filters (like combining specific industry datasets with geographic origins) every time they logged in. This update provides material value by:</p>
<ul>
<li>Analysts can now jump straight into &quot;Known Ransomware Infrastructure&quot; or &quot;Retail Sector Targets&quot; views with a single click, eliminating repetitive setup tasks</li>
<li>Teams can ensure everyone is looking at the same data subsets by using standardized saved views, reducing the risk of missing critical patterns due to inconsistent filtering.</li>
</ul>
<p>Cloudforce One subscribers can start saving their custom views now in <a href="https://dash.cloudflare.com/?to=/:account/security-center/threat-intelligence/threat-events">Application Security &gt; Threat Intelligence &gt; Threat Events</a>.</p>


<h2 id="dex-supports-eu-customer-metadata-boundary"><a href="/changelog/post/2026-02-19-dex-supports-cmb-eu/">DEX Supports EU Customer Metadata Boundary</a></h2>
<p><em>2026-02-19</em></p>
<p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into <a href="/warp-client/">WARP</a> device connectivity and performance to any internal or external application.</p>
<p>Now, all DEX logs are fully compatible with Cloudflare's <a href="/data-localization/metadata-boundary/">Customer Metadata Boundary</a> (CMB) setting for the 'EU' (European Union), which ensures that DEX logs will not be stored outside the 'EU' when the option is configured.</p>
<p>If a Cloudflare One customer using DEX enables CMB 'EU', they will not see any DEX data in the Cloudflare One dashboard. Customers can ingest DEX data via <a href="/logs/logpush/">LogPush</a>, and build their own analytics and dashboards.</p>
<p>If a customer enables CMB in their account, they will see the following message in the Digital Experience dashboard: &quot;DEX data is unavailable because Customer Metadata Boundary configuration is on. Use Cloudflare LogPush to export DEX datasets.&quot;</p>
<p><img src="/assets/upstream/images/changelog/dex/dex_supports_cmb.png" alt="Digital Experience Monitoring message when Customer Metadata Boundary for the EU is enabled" /></p>


<h2 id="cloudforce-one-threat-events-graphs-are-now-visible-in-the-dashboard"><a href="/changelog/post/2026-02-19-threat-events-graphs/">Cloudforce One Threat events graphs are now visible in the dashboard</a></h2>
<p><em>2026-02-19</em></p>
<p>We have introduced dynamic visualizations to the Threat Events dashboard to help you better understand the threat landscape and identify emerging patterns at a glance.</p>
<p>What's new:</p>
<ul>
<li><strong>Sankey Diagrams</strong>: Trace the flow of attacks from country of origin to target country to identify which regions are being hit hardest and where the threat infrastructure resides.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/security-center/2026-02-19-sankey-diagram.png" alt="Sankey Diagram" /></p>
<ul>
<li><strong>Dataset Distribution over time</strong>: Instantly pivot your view to understand if a specific campaign is targeting your sector or if it is a broad-spectrum commodity attack.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/security-center/2026-02-19-events-over-time.png" alt="Events over time" /></p>
<ul>
<li><strong>Enhanced Filtering</strong>: Use these visual tools to filter and drill down into specific attack vectors directly from the charts.</li>
</ul>
<p>Cloudforce One subscribers can explore these new views now in <a href="https://dash.cloudflare.com/?to=/:account/security-center/threat-intelligence/threat-events">Application Security &gt; Threat Intelligence &gt; Threat Events</a>.</p>


<h2 id="new-cfworker-metric-in-server-timing-header"><a href="/changelog/post/2026-02-18-cfworker-server-timing/">New cfWorker metric in Server-Timing header</a></h2>
<p><em>2026-02-18</em></p>
<p>The Server-Timing header now includes a new <code>cfWorker</code> metric that measures time spent executing Cloudflare Workers, including any subrequests performed by the Worker. This helps developers accurately identify whether high Time to First Byte (TTFB) is caused by Worker processing or slow upstream dependencies.</p>
<p>Previously, Worker execution time was included in the <code>edge</code> metric, making it harder to identify true edge performance. The new <code>cfWorker</code> metric provides this visibility:</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>edge</code></td>
<td>Total time spent on the Cloudflare edge, including Worker execution</td>
</tr>
<tr>
<td><code>origin</code></td>
<td>Time spent fetching from the origin server</td>
</tr>
<tr>
<td><code>cfWorker</code></td>
<td>Time spent in Worker execution, including subrequests but excluding origin fetch time</td>
</tr>
</tbody>
</table>
<h4 id="2026-02-18-cfworker-server-timing-example-response">Example response</h4>
<pre><code class="language-txt">Server-Timing: cdn-cache; desc=DYNAMIC, edge; dur=20, origin; dur=100, cfWorker; dur=7&#10;</code></pre>
<p>In this example, the edge took 20ms, the origin took 100ms, and the Worker added just 7ms of processing time.</p>
<h4 id="2026-02-18-cfworker-server-timing-availability">Availability</h4>
<p>The <code>cfWorker</code> metric is enabled by default if you have <a href="/web-analytics/">Real User Monitoring (RUM)</a> enabled. Otherwise, you can enable it using <a href="/rules/">Rules</a>.</p>
<p>This metric is particularly useful for:</p>
<ul>
<li><strong>Performance debugging</strong>: Quickly determine if latency is caused by Worker code, external API calls within Workers, or slow origins.</li>
<li><strong>Optimization targeting</strong>: Identify which component of your request path needs optimization.</li>
<li><strong>Real User Monitoring (RUM)</strong>: Access detailed timing breakdowns directly from response headers for client-side analytics.</li>
</ul>
<p>For more information about Server-Timing headers, refer to the <a href="https://www.w3.org/TR/server-timing/">W3C Server Timing specification</a>.</p>


<h2 id="cloudflare-one-product-name-updates"><a href="/changelog/post/2026-02-17-product-name-updates/">Cloudflare One Product Name Updates</a></h2>
<p><em>2026-02-17</em></p>
<p>We are updating naming related to some of our Networking products to better clarify their place in the Zero Trust and Secure Access Service Edge (SASE) journey.</p>
<p>We are retiring some older brand names in favor of names that describe exactly what the products do within your network. We are doing this to help customers build better, clearer mental models for comprehensive SASE architecture delivered on Cloudflare.</p>
<h4 id="2026-02-17-product-name-updates-what-s-changing">What's changing</h4>
<ul>
<li><strong>Magic WAN</strong> → <strong>Cloudflare WAN</strong></li>
<li><strong>Magic WAN IPsec</strong> → <strong>Cloudflare IPsec</strong></li>
<li><strong>Magic WAN GRE</strong> → <strong>Cloudflare GRE</strong></li>
<li><strong>Magic WAN Connector</strong> → <strong>Cloudflare One Appliance</strong></li>
<li><strong>Magic Firewall</strong> → <strong>Cloudflare Network Firewall</strong></li>
<li><strong>Magic Network Monitoring</strong> → <strong>Network Flow</strong></li>
<li><strong>Magic Cloud Networking</strong> → <strong>Cloudflare One Multi-cloud Networking</strong></li>
</ul>
<p><strong>No action is required by you</strong> — all functionality, existing configurations, and billing will remain exactly the same.</p>
<p>For more information, visit the <a href="/cloudflare-one/">Cloudflare One documentation</a>.</p>


<h2 id="content-type-dimension-for-ai-bots-in-cloudflare-radar"><a href="/changelog/post/2026-02-12-radar-ai-bots-content-type/">Content Type Dimension for AI Bots in Cloudflare Radar</a></h2>
<p><em>2026-02-12</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> now includes content type insights for AI bot and crawler traffic. The new <code>content_type</code> dimension and filter shows the distribution of content types returned to AI crawlers, grouped by MIME type category.</p>
<p>The content type dimension and filter are available via the following API endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/ai/subresources/bots/methods/summary_v2/"><code>/ai/bots/summary/content_type</code></a></li>
<li><a href="/api/resources/radar/subresources/ai/subresources/bots/methods/timeseries_groups/"><code>/ai/bots/timeseries_groups/content_type</code></a></li>
</ul>
<p>Content type categories:</p>
<ul>
<li><strong>HTML</strong> - Web pages (<code>text/html</code>)</li>
<li><strong>Images</strong> - All image formats (<code>image/*</code>)</li>
<li><strong>JSON</strong> - JSON data and API responses (<code>application/json</code>, <code>*+json</code>)</li>
<li><strong>JavaScript</strong> - Scripts (<code>application/javascript</code>, <code>text/javascript</code>)</li>
<li><strong>CSS</strong> - Stylesheets (<code>text/css</code>)</li>
<li><strong>Plain Text</strong> - Unformatted text (<code>text/plain</code>)</li>
<li><strong>Fonts</strong> - Web fonts (<code>font/*</code>, <code>application/font-*</code>)</li>
<li><strong>XML</strong> - XML documents and feeds (<code>text/xml</code>, <code>application/xml</code>, <code>application/rss+xml</code>, <code>application/atom+xml</code>)</li>
<li><strong>YAML</strong> - Configuration files (<code>text/yaml</code>, <code>application/yaml</code>)</li>
<li><strong>Video</strong> - Video content and streaming (<code>video/*</code>, <code>application/ogg</code>, <code>*mpegurl</code>)</li>
<li><strong>Audio</strong> - Audio content (<code>audio/*</code>)</li>
<li><strong>Markdown</strong> - Markdown documents (<code>text/markdown</code>)</li>
<li><strong>Documents</strong> - PDFs, Office documents, ePub, CSV (<code>application/pdf</code>, <code>application/msword</code>, <code>text/csv</code>)</li>
<li><strong>Binary</strong> - Executables, archives, WebAssembly (<code>application/octet-stream</code>, <code>application/zip</code>, <code>application/wasm</code>)</li>
<li><strong>Serialization</strong> - Binary API formats (<code>application/protobuf</code>, <code>application/grpc</code>, <code>application/msgpack</code>)</li>
<li><strong>Other</strong> - All other content types</li>
</ul>
<p>Additionally, individual <a href="https://radar.cloudflare.com/bots/directory/gptbot">bot information pages</a> now display content type distribution for AI crawlers that exist in both the Verified Bots and AI Bots datasets.</p>
<p><img src="/assets/upstream/images/radar/ai-bots-content-type.png" alt="Screenshot of the Content Type Distribution chart on the AI Insights page" /></p>
<p>Check out the <a href="https://radar.cloudflare.com/ai-insights#content-type">AI Insights page</a> to explore the data.</p>


<h2 id="enhanced-logo-matching-for-brand-protection"><a href="/changelog/post/2026-02-12-brand-protection-logo-matching-percentage-selector/">Enhanced Logo Matching for Brand Protection</a></h2>
<p><em>2026-02-12</em></p>
<p>We have significantly upgraded our Logo Matching capabilities within Brand Protection. While previously limited to approximately 100% matches, users can now detect a wider range of brand assets through a redesigned matching model and UI.</p>
<h4 id="2026-02-12-brand-protection-logo-matching-percentage-selector-what-s-new">What's new</h4>
<ul>
<li><strong>Configurable match thresholds</strong>: Users can set a minimum match score (starting at 75%) when creating a logo query to capture subtle variations or high-quality impersonations.</li>
<li><strong>Visual match scores</strong>: Allow users to see the exact percentage of the match directly in the results table, highlighted with color-coded lozenges to indicate severity.</li>
<li><strong>Direct logo previews</strong>: Available in the Cloudflare dashboard — similar to string matches — to verify infringements at a glance.</li>
</ul>
<h4 id="2026-02-12-brand-protection-logo-matching-percentage-selector-key-benefits">Key benefits</h4>
<ul>
<li><strong>Expose sophisticated impersonators</strong> who use slightly altered logos to bypass basic detection filters.</li>
<li><strong>Faster triage</strong> of the most relevant threats immediately using visual indicators, reducing the time spent manually reviewing matches.</li>
</ul>
<p>Ready to protect your visual identity? Learn more in our <a href="/security-center/brand-protection/">Brand Protection documentation</a>.</p>


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


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/analytics/2/">Previous</a><span>Page 3 of 6</span><a class="pagination-next" rel="next" href="/changelog/product-group/analytics/4/">Next</a></nav>
