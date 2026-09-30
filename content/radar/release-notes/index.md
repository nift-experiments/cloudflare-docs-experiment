<h2 id="2026-08-07">2026-08-07</h2><strong>Add AS-level connectivity and upstream providers widgets to Cloudflare Radar</strong><ul>
<li>Added an <strong>AS-level connectivity</strong> graph to AS <a href="https://radar.cloudflare.com/routing/as13335">routing pages</a>, aggregating the BGP paths an AS uses to reach the Tier-1 networks across every prefix it announces, as observed by selected RouteViews collectors. A <strong>Show full paths</strong> toggle switches between the simplified view and all observed paths, and an IP version selector switches between IPv4 and IPv6.</li>
<li>Added an <strong>Upstream providers</strong> timeseries widget to AS routing pages, tracking the share of an AS's observed paths carried by each direct upstream network over time. Up to 10 upstreams appear as their own series, with the remainder grouped into <strong>Other</strong>.</li>
<li>Added two new endpoints to the <a href="/api/resources/radar/subresources/bgp/"><code>BGP</code></a> API:
<ul>
<li><a href="/api/resources/radar/subresources/bgp/subresources/routes/subresources/paths/methods/list/"><code>/bgp/routes/paths/{asn}</code></a> - Returns the ordered AS path segments an AS uses to reach the Tier-1 networks, each with its observed path count, peer count, and contributing collectors.</li>
<li><a href="/api/resources/radar/subresources/bgp/subresources/routes/subresources/upstreams/methods/timeseries/"><code>/bgp/routes/upstreams/{asn}/timeseries</code></a> - Returns the share of an AS's observed paths carried by each direct upstream over time, split by IP version.</li>
</ul>
</li>
</ul><h2 id="2026-05-29">2026-05-29</h2><strong>Add TLS bug detection to the Radar post-quantum TLS support checker</strong><ul>
<li>The <a href="https://radar.cloudflare.com/post-quantum">post-quantum TLS support checker</a> now reports TLS bugs detected during the handshake test (Split ClientHello, HRR Failure, Unknown Keyshare) with user-facing descriptions and remediation guidance. The bugs section only appears for hosts where issues are detected.</li>
<li>Bug detection data is returned by the existing <a href="/api/resources/radar/subresources/post_quantum/subresources/tls/methods/support/"><code>/post_quantum/tls/support</code></a> endpoint.</li>
</ul><h2 id="2026-05-04">2026-05-04</h2><strong>Add new routing widgets to Cloudflare Radar</strong><ul>
<li>Added a <strong>Top ASes by announced IP space</strong> chart to country <a href="https://radar.cloudflare.com/routing">routing pages</a>, breaking down the IPv4 and IPv6 address space announced from a country across the top originating autonomous systems.</li>
<li>Added an <strong>RPKI ROA deployment</strong> timeseries widget to the <a href="https://radar.cloudflare.com/routing/rpki">RPKI sub-page</a>, tracking the share of announced BGP space covered by a valid Route Origin Authorization (ROA) over time, with a toggle between covered prefixes and covered IP address space. Available on global, country, and AS views.</li>
<li>Added two new endpoints to the <a href="/api/resources/radar/subresources/bgp/"><code>BGP</code></a> API:
<ul>
<li><a href="/api/resources/radar/subresources/bgp/subresources/ips/subresources/top/methods/ases/"><code>/bgp/ips/top/ases</code></a> - Returns the top autonomous systems by announced IPv4 or IPv6 address space, globally or filtered by country.</li>
<li><a href="/api/resources/radar/subresources/bgp/subresources/rpki/subresources/roas/methods/timeseries/"><code>/bgp/rpki/roas/timeseries</code></a> - Returns RPKI ROA validation coverage over time, by share of prefixes or share of IP address space, split by IP version, with optional ASN or location filters.</li>
</ul>
</li>
</ul><h2 id="2026-04-24">2026-04-24</h2><strong>Add signature agent URL to bot details</strong><ul>
<li>Added <code>signatureAgentUrl</code> field to the <a href="/api/resources/radar/subresources/bots/methods/get/">bot details</a> API endpoint. For agents verified via <a href="/bots/reference/bot-verification/web-bot-auth/">Web Bot Auth</a>, this field contains the URL to the agent's HTTP Message Signatures key directory. It is <code>null</code> for bots not verified via request signature.</li>
<li>Added signature agent URL to the <a href="https://radar.cloudflare.com/bots/directory">bot detail page</a> on Radar, with a modal to inspect the key directory JSON content.</li>
</ul><h2 id="2026-04-01">2026-04-01</h2><strong>Promote Routing to a dedicated section with sub-pages</strong><ul>
<li>Expanded the Routing page into a full section with dedicated <a href="https://radar.cloudflare.com/routing">Overview</a>, <a href="https://radar.cloudflare.com/routing/rpki">RPKI</a>, and <a href="https://radar.cloudflare.com/routing/anomalies">Anomalies</a> sub-pages.</li>
<li>Added new <strong>Top 100 ASes</strong> widget to the routing overview, with rankings by customer cone, IPv4 address space, and IPv6 address space.</li>
<li>Added new <strong>RPKI prefix validation</strong> widget showing per-ASN prefixes grouped by validation status (Valid, Invalid, Unknown).</li>
<li>Improved the IP address space chart to display both IPv4 and IPv6 trends on all views including global.</li>
</ul><h2 id="2026-03-06">2026-03-06</h2><strong>Add region filtering and AS/location dimensions to API</strong><ul>
<li>Added region filtering across all location-aware pages, including continents, geographic subregions, political regions (EU, ASEAN, African Union), and US Census regions/divisions.</li>
<li>Added traffic volume insights by top autonomous systems and countries/territories.</li>
<li>Added AS and location dimensions to the <a href="/api/resources/radar/subresources/http/"><code>HTTP</code></a>, <a href="/api/resources/radar/subresources/dns/"><code>DNS</code></a>, and <a href="/api/resources/radar/subresources/netflows/"><code>NetFlows</code></a> APIs.</li>
<li>Added breadcrumb navigation.</li>
</ul><h2 id="2026-02-27">2026-02-27</h2><strong>Add Post-Quantum and Key Transparency insights</strong><ul>
<li>Added new <a href="/api/resources/radar/subresources/post_quantum/"><code>Post-Quantum</code></a> API:
<ul>
<li><a href="/api/resources/radar/subresources/post_quantum/subresources/tls/methods/support/"><code>/post_quantum/tls/support</code></a> - Tests whether a host supports post-quantum TLS key exchange.</li>
<li><a href="/api/resources/radar/subresources/post_quantum/methods/summary/"><code>/post_quantum/origin/summary/{dimension}</code></a> - Returns origin post-quantum data summarized by key agreement algorithm.</li>
<li><a href="/api/resources/radar/subresources/post_quantum/methods/timeseries_groups/"><code>/post_quantum/origin/timeseries_groups/{dimension}</code></a> - Returns origin post-quantum timeseries data grouped by key agreement algorithm.</li>
</ul>
</li>
<li>Launched <a href="https://radar.cloudflare.com/post-quantum">Post-Quantum Encryption</a> page.</li>
<li>Launched <a href="https://radar.cloudflare.com/key-transparency">Key Transparency</a> page.</li>
</ul><h2 id="2026-02-25">2026-02-25</h2><strong>Add RPKI ASPA deployment insights</strong><ul>
<li>Added new <a href="/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/"><code>ASPA</code></a> API endpoints:
<ul>
<li><a href="/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/snapshot/"><code>/bgp/rpki/aspa/snapshot</code></a> - Retrieves current or historical ASPA objects.</li>
<li><a href="/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/changes/"><code>/bgp/rpki/aspa/changes</code></a> - Retrieves changes to ASPA objects over time.</li>
<li><a href="/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/timeseries/"><code>/bgp/rpki/aspa/timeseries</code></a> - Retrieves ASPA object counts over time as a timeseries.</li>
</ul>
</li>
<li>Added ASPA deployment trend and objects count widgets to the <a href="https://radar.cloudflare.com/routing">global routing page</a>.</li>
<li>Added ASPA deployment rate widget to country and region routing pages.</li>
<li>Added ASPA-verified upstreams and change timeline to AS routing pages.</li>
</ul><h2 id="2026-02-12">2026-02-12</h2><strong>Add content type dimension to AI Bots</strong><ul>
<li>Added new <code>content_type</code> dimension and filter to the AI Bots API:
<ul>
<li><a href="/api/resources/radar/subresources/ai/subresources/bots/methods/summary_v2/"><code>/ai/bots/summary/{dimension}</code></a></li>
<li><a href="/api/resources/radar/subresources/ai/subresources/bots/methods/timeseries_groups/"><code>/ai/bots/timeseries_groups/{dimension}</code></a></li>
</ul>
</li>
<li>Added new <strong>Content Type Distribution</strong> chart to the <a href="https://radar.cloudflare.com/ai-insights#content-type">AI Insights page</a>.</li>
<li>Added content type chart to individual <a href="https://radar.cloudflare.com/bots/directory">bot information pages</a> for AI crawlers.</li>
</ul><h2 id="2025-12-16">2025-12-16</h2><strong>New client type dimension in Web Crawlers and Mixed Purpose entry</strong><ul>
<li>Added new Mixed Purpose entry to the <code>crawl_purpose</code> dimension of the <a href="/api/resources/radar/subresources/bots/subresources/web_crawlers/">Web Crawlers</a> API, which as of this release includes Googlebot and Bingbot.</li>
<li>Added new dimension <code>client_type</code> to the <a href="/api/resources/radar/subresources/bots/subresources/web_crawlers/">Web Crawlers</a> API.
<ul>
<li>Added new <strong>HTML page requests by client type graph</strong> to the <a href="https://radar.cloudflare.com/ai-insights#html-page-requests-by-client-type">AI Insights page</a>.</li>
</ul>
</li>
</ul><h2 id="2025-11-24">2025-11-24</h2><strong>Add HTTP origins insights</strong><ul>
<li>Added new <a href="/api/resources/radar/subresources/origins/"><code>Origins</code></a> API.</li>
<li>Extended <a href="/api/resources/radar/subresources/annotations/"><code>Annotations</code></a> and <a href="/api/resources/radar/subresources/traffic_anomalies/"><code>Traffic Anomalies</code></a> APIs to support origin outages and anomalies.</li>
</ul><h2 id="2025-10-27">2025-10-27</h2><strong>Add TLD insights</strong><ul>
<li>Added new dimensions <code>tld</code> and <code>tld_dns_magnitude</code> to the <a href="/api/resources/radar/subresources/dns/">DNS</a> API.</li>
<li>Added new endpoints <a href="/api/resources/radar/subresources/tlds/methods/list/"><code>/tlds</code></a> and <a href="/api/resources/radar/subresources/tlds/methods/get/"><code>/tlds/{tld}</code></a>.</li>
</ul><h2 id="2025-10-09">2025-10-09</h2><strong>Add CT log activity statistics</strong><ul>
<li>Added new CT log activity stats to the <a href="/api/resources/radar/subresources/ct/subresources/logs/methods/get/">Get Certificate Log Details</a> API response.</li>
</ul><h2 id="2025-10-06">2025-10-06</h2><strong>Add PQ encryption browser support check</strong><ul>
<li>Added a <a href="https://radar.cloudflare.com/adoption-and-usage#browser-support">post-quantum encryption browser support check</a> to the PQ encryption card in the Adoption &amp; Usage section.</li>
</ul><h2 id="2025-09-29">2025-09-29</h2><strong>Add geolocation, ADM1 dimension to HTTP endpoints, and NetFlows endpoints</strong><ul>
<li>Added new <a href="/api/resources/radar/subresources/geolocations/">geolocation endpoints</a>.</li>
<li>Added new ADM1 dimension to <a href="/api/resources/radar/subresources/http/"><code>HTTP</code></a> <code>summary</code> and <code>timeseries_groups</code> endpoints.</li>
<li>Added new <a href="/api/resources/radar/subresources/netflows/"><code>NetFlows</code></a> summary by dimension endpoint <a href="/api/resources/radar/subresources/netflows/methods/summary_v2/">summary_v2</a>.</li>
<li>Added new <code>geoId</code> filter to all <a href="/api/resources/radar/subresources/http/"><code>HTTP</code></a> and <a href="/api/resources/radar/subresources/netflows/"><code>NetFlows</code></a> endpoints.</li>
</ul><h2 id="2025-09-22">2025-09-22</h2><strong>Add IRR AS-SET membership lookup endpoint</strong><ul>
<li>Added IRR AS-SET membership lookup endpoint
<ul>
<li><a href="/api/resources/radar/subresources/entities/subresources/asns/methods/as_set/"> <code>/entities/asns/{asn}/as_set</code> </a></li>
</ul>
</li>
</ul><h2 id="2025-08-27">2025-08-27</h2><strong>Add industry and vertical to AI Bots and Web Crawlers, and bot kind to Bots</strong><ul>
<li>Added vertical and industry dimensions/filters to:
<ul>
<li><a href="/api/resources/radar/subresources/ai/subresources/timeseries_groups/methods/summary/"><code>/ai/bots/summary/{dimension}</code></a></li>
<li><a href="/api/resources/radar/subresources/ai/subresources/timeseries_groups/methods/timeseries_groups/"><code>/ai/bots/timeseries_groups/{dimension}</code></a></li>
<li><a href="/api/resources/radar/subresources/bots/subresources/web_crawlers/methods/summary/"><code>/bots/crawlers/summary/{dimension}</code></a></li>
<li><a href="/api/resources/radar/subresources/bots/subresources/web_crawlers/methods/timeseries_groups/"><code>/bots/crawlers/timeseries_groups/{dimension}</code></a></li>
</ul>
</li>
<li>Added bot kind dimension/filter to:
<ul>
<li><a href="/api/resources/radar/subresources/bots/methods/summary/"><code>/bots/summary/{dimension}</code></a></li>
<li><a href="/api/resources/radar/subresources/bots/methods/timeseries_groups/"><code>/bots/timeseries_groups/{dimension}</code></a></li>
</ul>
</li>
<li>Added new <code>botKind</code> filter to:
<ul>
<li><a href="/api/resources/radar/subresources/bots/methods/timeseries/"><code>/bots/timeseries</code></a></li>
</ul>
</li>
<li>Added new <code>kind</code> property/filter to:
<ul>
<li><a href="/api/resources/radar/subresources/bots/methods/list/"><code>/bots</code></a></li>
<li><a href="/api/resources/radar/subresources/bots/methods/get/"><code>/bots/{bot_slug}</code></a></li>
</ul>
</li>
</ul><h2 id="2025-08-14">2025-08-14</h2><strong>Add AI Bots crawl purpose</strong><ul>
<li>Added AI Bots crawl purpose dimension and filter to <a href="/api/resources/radar/subresources/ai/subresources/timeseries_groups/methods/summary/">summary</a> and <a href="/api/resources/radar/subresources/ai/subresources/timeseries_groups/methods/timeseries_groups/">timeseries_groups</a> endpoints.</li>
</ul><h2 id="2025-08-06">2025-08-06</h2><strong>Add Certificate Transparency (CT) endpoints</strong><ul>
<li>Added <a href="/api/resources/radar/subresources/ct/">CT endpoints</a>.</li>
</ul><h2 id="2025-07-01">2025-07-01</h2><strong>Add Bots and Web Crawlers endpoints</strong><ul>
<li>Added new <a href="/api/resources/radar/subresources/bots/">bots endpoints</a>, replacing the deprecated verified bots
endpoints. Use the following replacements:
<ul>
<li><code>/verified_bots/top/bots</code> → <code>/bots/summary/bot</code></li>
<li><code>/verified_bots/top/categories</code> → <code>/bots/summary/bot_category</code></li>
</ul>
</li>
<li>Added <a href="/api/resources/radar/subresources/bots/subresources/web_crawlers/">web crawlers endpoints</a>.</li>
</ul><h2 id="2025-03-20">2025-03-20</h2><strong>Endpoint deprecations and new BGP real-time routes endpoint</strong><ul>
<li>Deprecated endpoints for improved consistency (switch to the following):
<ul>
<li><code>/attacks/layer3/top/industry</code> → <a href="/api/resources/radar/subresources/attacks/subresources/layer3/subresources/summary/methods/industry/"><code>/attacks/layer3/summary/industry</code></a></li>
<li><code>/attacks/layer3/top/vertical</code> → <a href="/api/resources/radar/subresources/attacks/subresources/layer3/subresources/summary/methods/vertical/"><code>/attacks/layer3/summary/vertical</code></a></li>
<li><code>/attacks/layer7/top/industry</code> → <a href="/api/resources/radar/subresources/attacks/subresources/layer7/subresources/summary/methods/industry/"><code>/attacks/layer7/summary/industry</code></a></li>
<li><code>/attacks/layer7/top/vertical</code> → <a href="/api/resources/radar/subresources/attacks/subresources/layer7/subresources/summary/methods/vertical/"><code>/attacks/layer7/summary/vertical</code></a></li>
</ul>
</li>
<li>Added the <a href="/api/resources/radar/subresources/bgp/subresources/routes/methods/realtime/">BGP real-time routes endpoint</a>.</li>
</ul><h2 id="2025-03-18">2025-03-18</h2><strong>Add leaked credential checks endpoints</strong><ul>
<li>Added <a href="/api/resources/radar/subresources/leaked_credentials/">leaked credential checks endpoints</a>.</li>
</ul><h2 id="2025-02-27">2025-02-27</h2><strong>Add DNS endpoints</strong><ul>
<li>Added <a href="/api/resources/radar/subresources/dns/">DNS endpoints</a>.</li>
</ul><h2 id="2025-02-04">2025-02-04</h2><strong>Add Internet services ranking, robots.txt, and AI inference endpoints</strong><ul>
<li>Added <a href="/api/resources/radar/subresources/ranking/subresources/internet_services/">Internet services ranking endpoints</a>.</li>
<li>Added <a href="/api/resources/radar/subresources/robots_txt/">robots.txt endpoints</a>.</li>
<li>Added <a href="/api/resources/radar/subresources/ai/subresources/inference/">AI inference endpoints</a>.</li>
</ul><h2 id="2024-06-27">2024-06-27</h2><strong>Change TCP connection tampering API endpoints to TCP Resets Timeouts</strong><ul>
<li>Changed the connection tampering summary and timeseries API endpoints to
TCP resets timeouts <a href="/api/resources/radar/subresources/tcp_resets_timeouts/methods/summary/">summary</a>
and <a href="/api/resources/radar/subresources/tcp_resets_timeouts/methods/timeseries_groups/">timeseries</a>,
respectively.</li>
</ul><h2 id="2023-11-27">2023-11-27</h2><strong>Add more meta information&#x27;s</strong><ul>
<li>Added meta.lastUpdated to all summaries and top endpoints (timeseries and timeseriesGroups already had this).</li>
<li>Fixed meta.dateRange to return date ranges for all requested series.</li>
</ul><h2 id="2023-11-16">2023-11-16</h2><strong>Add new layer 3 endpoints and layer 7 dimensions</strong><ul>
<li>Added layer 3 <a href="/api/resources/radar/subresources/attacks/subresources/layer3/subresources/top/subresources/locations/methods/origin/">top origin locations</a>
and <a href="/api/resources/radar/subresources/attacks/subresources/layer3/subresources/top/subresources/locations/methods/target/">top target location</a>.</li>
<li>Added layer 7 Summaries by <code>http_method</code>, <code>http_version</code>, <code>ip_version</code>, <code>managed_rules</code>, <code>mitigation_product</code>.</li>
<li>Added layer 7 Timeseries Groups by <code>http_method</code>, <code>http_version</code>, <code>ip_version</code>, <code>managed_rules</code>, <code>mitigation_product</code>, <code>industry</code>, <code>vertical</code>.</li>
<li>Added layer 7 Top by <code>industry</code>, <code>vertical</code>.</li>
<li>Deprecated layer 7 timeseries groups without dimension.
<ul>
<li>To continue getting this data, switch to the new
<a href="/api/resources/radar/subresources/attacks/subresources/layer7/subresources/timeseries_groups/methods/mitigation_product/">timeseries group by mitigation_product</a>
endpoint.</li>
</ul>
</li>
<li>Deprecated layer 7 summary without dimension.
<ul>
<li>To continue getting this data, switch to the new
<a href="/api/resources/radar/subresources/attacks/subresources/layer7/subresources/summary/methods/mitigation_product/">summary by mitigation_product</a>
endpoint.</li>
</ul>
</li>
<li>Added new <a href="/radar/get-started/error-codes/">Error codes</a>.</li>
</ul><h2 id="2023-10-31">2023-10-31</h2><strong>Add new layer 3 direction parameter</strong><ul>
<li>Added a <code>direction</code> parameter to all layer 3 endpoints. Use together with <code>location</code> parameter to filter by origin or
target location <a href="/api/resources/radar/subresources/attacks/subresources/layer3/subresources/timeseries_groups/methods/vector/">timeseries groups</a>.</li>
</ul><h2 id="2023-09-08">2023-09-08</h2><strong>Add Connection Tampering endpoints</strong><ul>
<li>Added Connection Tampering <a href="/api/resources/radar/subresources/tcp_resets_timeouts/methods/summary/">summary</a>
and <a href="/api/resources/radar/subresources/tcp_resets_timeouts/methods/timeseries_groups/">timeseries</a> endpoints.</li>
</ul><h2 id="2023-08-14">2023-08-14</h2><strong>Deprecate old layer 3 dataset</strong><ul>
<li>Added Regional Internet Registry (see field <code>source</code> in response)
to <a href="/api/resources/radar/subresources/entities/subresources/asns/methods/get/">get asn by id</a>
and <a href="/api/resources/radar/subresources/entities/subresources/asns/methods/ip/">get asn by ip</a> endpoints.</li>
<li>Stopped collecting data in the old layer 3 data source.</li>
<li>Updated layer 3
<a href="/api/resources/radar/subresources/attacks/subresources/layer3/methods/timeseries/">timeseries</a> endpoint
to start using the new layer 3 data source by default, fetching the old data source now requires sending the parameter
<code>metric=bytes_old</code>.</li>
<li>Deprecated layer 3 summary endpoint, this will stop receiving data after 2023-08-14.
<ul>
<li>To continue getting this data, switch to the
new <a href="/api/resources/radar/subresources/attacks/subresources/layer3/subresources/summary/methods/protocol/">timeseries group protocol</a>
endpoint.</li>
</ul>
</li>
<li>Deprecated layer 3 timeseries groups endpoint, this will stop receiving data after 2023-08-14.
<ul>
<li>To continue getting this data, switch to the
new <a href="/api/resources/radar/subresources/attacks/subresources/layer3/subresources/timeseries_groups/methods/protocol/">timeseries group protocol</a>
endpoint.</li>
</ul>
</li>
</ul><h2 id="2023-07-31">2023-07-31</h2><strong>Fix HTTP timeseries endpoint URLs</strong><ul>
<li>Updated HTTP <code>timeseries</code> endpoints URLs
to <a href="/api/resources/radar/subresources/http/subresources/timeseries_groups/"><code>timeseries_groups</code></a>
due to consistency. Old timeseries endpoints are still available, but will soon be removed.</li>
</ul><h2 id="2023-07-20">2023-07-20</h2><strong>Add URL Scanner endpoints</strong><ul>
<li>Added <a href="/api/resources/url_scanner/">URL Scanner endpoints</a>. For more information, refer to <a href="/radar/investigate/url-scanner/">URL Scanner</a>.</li>
</ul><h2 id="2023-06-20">2023-06-20</h2><strong>Add Internet quality endpoints</strong><ul>
<li>Added <a href="/api/resources/radar/subresources/quality/">Internet quality endpoints</a>.</li>
</ul><h2 id="2023-06-07">2023-06-07</h2><strong>Add BGP stats, pfx2as and moas endpoints</strong><ul>
<li>Added BGP <a href="/api/resources/radar/subresources/bgp/subresources/routes/methods/stats/">stats</a>,
<a href="/api/resources/radar/subresources/bgp/subresources/routes/methods/pfx2as/">pfx2as</a>
and <a href="/api/resources/radar/subresources/bgp/subresources/routes/methods/moas/">moas</a> endpoints.</li>
</ul><h2 id="2023-05-10">2023-05-10</h2><strong>Added `IOS` as an option for the OS parameter in all HTTP</strong><ul>
<li>Added <code>IOS</code> as an option for the OS parameter in all HTTP
endpoints (<a href="/api/resources/radar/subresources/http/subresources/summary/methods/bot_class/">example</a>).</li>
</ul><h2 id="2023-03-20">2023-03-20</h2><strong>Add AS112 and email endpoints</strong><ul>
<li>Added <a href="/api/resources/radar/subresources/as112/">AS112 endpoints</a>.</li>
<li>Added <a href="/api/resources/radar/subresources/email/">email endpoints</a>.</li>
</ul><h2 id="2023-01-23">2023-01-23</h2><strong>Updated IPv6 calculation method</strong><ul>
<li>IPv6 percentage started to be calculated as (IPv6 requests / requests for dual-stacked content), where as before it
was calculated as (IPv6 requests / IPv4+IPv6 requests).</li>
</ul><h2 id="2023-01-11">2023-01-11</h2><strong>Add new layer 3 dataset</strong><ul>
<li>Added new layer 3 data source and related endpoints.</li>
<li>Updated layer 3
<a href="/api/resources/radar/subresources/attacks/subresources/layer3/methods/timeseries/">timeseries</a> endpoint
to support fetching both current and new data sources. For retro-compatibility
reasons, fetching the new data source requires sending the parameter <code>metric=bytes</code> else the current data
source will be returned.</li>
<li>Deprecated old layer 3 endpoints timeseries_groups and summary.
Users should upgrade to newer endpoints.</li>
</ul>
