<h1 id="changelog">Changelog</h1>

<h2 id="radar-search-now-includes-internet-events"><a href="/changelog/post/2026-09-08-radar-search-events/">Radar search now includes Internet events</a></h2>
<p><em>2026-09-08</em></p>
<p><a href="/radar/"><strong>Cloudflare Radar</strong></a> search now includes Internet events and outages alongside existing results. Search event descriptions or related entities, such as locations, ASes, bots, and top-level domains, to find relevant events and open the most relevant Radar view.</p>
<p><img src="/assets/upstream/images/radar/radar-search-events.png" alt="Radar search results showing Internet outage events associated with locations and autonomous systems" /></p>
<p>Event links preserve the event date range, making it easier to investigate what changed before, during, and after an event. These results are also available to browser-based AI agents through <a href="/browser-run/features/webmcp/">WebMCP</a>.</p>


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


<h2 id="radar-researcher-adds-richer-sources-and-url-scanner-explanations"><a href="/changelog/post/2026-08-26-radar-researcher-improvements/">Radar Researcher adds richer sources and URL Scanner explanations</a></h2>
<p><em>2026-08-26</em></p>
<p><a href="/radar/"><strong>Cloudflare Radar</strong></a> expands the <a href="https://radar.cloudflare.com/?prompt=">Radar Researcher</a> beta with richer sources and new ways to investigate Internet data.</p>
<h4 id="2026-08-26-radar-researcher-improvements-connected-insights">Connected insights</h4>
<p>Radar Researcher responses can now link to relevant Radar pages, reports, and Cloudflare Blog posts.</p>
<p><img src="/assets/upstream/images/radar/radar-researcher-page-links.png" alt="Radar Researcher response linking to the IP Address Information and Network Quality Test pages" /></p>
<h4 id="2026-08-26-radar-researcher-improvements-url-scanner-report-explanations">URL Scanner report explanations</h4>
<p>Select <strong>Explain with AI</strong> on a <a href="https://radar.cloudflare.com/scan">URL Scanner report</a> to have Radar Researcher explain its findings and answer follow-up questions about the scanned site.</p>
<p><img src="/assets/upstream/images/radar/radar-researcher-url-scanner-explanation.png" alt="Radar Researcher explaining findings from an example.com URL Scanner report" /></p>
<h4 id="2026-08-26-radar-researcher-improvements-improved-shared-sessions">Improved shared sessions</h4>
<p>Shared conversations now open in fullscreen, while the share URL remains available until you close the panel or start a new conversation.</p>
<p>Open <a href="https://radar.cloudflare.com/?prompt=">Radar Researcher</a> to explore these improvements.</p>


<h2 id="rpki-aspa-path-validation-on-cloudflare-radar"><a href="/changelog/post/2026-08-24-radar-aspa-validation/">RPKI ASPA path validation on Cloudflare Radar</a></h2>
<p><em>2026-08-24</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> adds an <a href="https://radar.cloudflare.com/routing/aspa-validation">ASPA validation tool</a> to its <a href="https://radar.cloudflare.com/routing">Routing section</a>. Enter a BGP <code>AS_PATH</code> and the tool checks it against the <a href="https://blog.cloudflare.com/aspa-secure-internet/">Autonomous System Provider Authorization (ASPA)</a> records currently published in the RPKI, returning a verdict of <code>Valid</code>, <code>Invalid</code>, or <code>Unknown</code>. An <code>Invalid</code> verdict means no chain of provider authorizations covers the whole path, which is the signature of a route leak.</p>
<p>Validation follows <a href="https://datatracker.ietf.org/doc/draft-ietf-sidrops-aspa-verification/">draft-ietf-sidrops-aspa-verification</a>, so verdicts match those produced by validators implementing the same draft. The draft is still a work in progress and not yet an RFC.</p>
<h4 id="2026-08-24-radar-aspa-validation-enter-a-path">Enter a path</h4>
<p>Paths are read in BGP wire order: the rightmost AS is the origin, and the leftmost AS is the one closest to the collector or router that observed the route. AS numbers can be separated by spaces, commas, or hyphens, with or without an <code>AS</code> prefix. The full ASPA snapshot is loaded into the browser once, so the verdict, graph, and trace update as the path is edited, with no further requests. A set of example paths covers the interesting cases, including a route leak with an AS0 ASPA, where an AS declares that it has no providers at all.</p>
<h4 id="2026-08-24-radar-aspa-validation-choose-an-algorithm">Choose an algorithm</h4>
<p>The draft defines two verification algorithms that differ only in whether a down-ramp is permitted:</p>
<ul>
<li><strong>Upstream</strong> (<a href="https://datatracker.ietf.org/doc/html/draft-ietf-sidrops-aspa-verification#section-5.4">section 5.4</a>) — for routes received from a customer, peer, route server client, or route server. Only an up-ramp is permitted.</li>
<li><strong>Downstream</strong> (<a href="https://datatracker.ietf.org/doc/html/draft-ietf-sidrops-aspa-verification#section-5.5">section 5.5</a>) — for routes received from a provider. Both an up-ramp and a down-ramp are permitted.</li>
</ul>
<p>An <strong>up-ramp</strong> is the run of consecutive customer-to-provider hops from the origin to the apex of the path, and a <strong>down-ramp</strong> is the equivalent run from the announcing neighbor back to that apex. The tool evaluates both algorithms at once and labels each with its verdict, so a path that is legitimate when received from one session type and a leak when received from another is visible without switching modes. Selecting an algorithm drives the graph and the trace.</p>
<h4 id="2026-08-24-radar-aspa-validation-read-the-result">Read the result</h4>
<p>The <strong>ASPA validation graph</strong> draws the path hop by hop, labeling each AS with its role, whether it publishes an ASPA, and how many providers that ASPA authorizes. Every hop is marked <code>Provider+</code>, <code>Not Provider+</code>, or <code>No attestation</code>, and the maximum and minimum bounds of each ramp are drawn against the length of the path. Hops that no ramp reaches are highlighted, because a path the ramps cannot cover end to end is <code>Invalid</code>. The accompanying <strong>ASPA records</strong> table lists every AS in the path with its ASPA status and its authorized providers, each linked to its Radar AS page.</p>
<p><img src="/assets/upstream/images/radar/aspa-validation-graph.png" alt="ASPA validation graph for the path 1003 6939 1299 553, showing a Valid verdict under the downstream algorithm, the Provider+, Not Provider+, and No attestation outcome on each hop, and the up-ramp and down-ramp bounds that together cover the path" /></p>
<h4 id="2026-08-24-radar-aspa-validation-follow-the-algorithm">Follow the algorithm</h4>
<p>The <strong>Algorithm step by step</strong> section shows the derivation rather than just the answer. Two columns run the same scans under different stopping rules: the upper bounds, which test for <code>Invalid</code> and stop only on <code>Not Provider+</code>, and the lower bounds, which test for <code>Unknown</code> and also stop on <code>No Attestation</code>. A hop is <code>Not Provider+</code> when the AS publishes an ASPA that does not list the next AS as a provider, and <code>No Attestation</code> when the AS publishes no ASPA at all. Each column lists the outcome for every hop scanned, marks where the scan stopped, gives the resulting ramp length, and then evaluates the verdict rule with the numbers filled in.</p>
<p><img src="/assets/upstream/images/radar/aspa-validation-algorithm-trace.png" alt="Step-by-step trace for the same path, with the upper-bound and lower-bound columns each listing the up-ramp and down-ramp scans, the ramp lengths they produce, and the verdict rule that neither Invalid nor Unknown satisfies, leaving a Valid verdict" /></p>
<h4 id="2026-08-24-radar-aspa-validation-share-a-validation">Share a validation</h4>
<p>The path and the selected algorithm are kept in the URL, so a link reproduces a result exactly — for example, this <a href="https://radar.cloudflare.com/routing/aspa-validation?path=22652-1299-9498-149765-14789">route leak with an AS0 ASPA</a>. Appending <code>&amp;mode=upstream</code> pins the link to the upstream algorithm. The graph is a standard Radar widget, so it can also be embedded or shared as an image.</p>
<p>The records behind the tool are the same ones served by the <a href="/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/methods/snapshot/"><code>/bgp/rpki/aspa/snapshot</code></a> endpoint of the <a href="/api/resources/radar/subresources/bgp/subresources/rpki/subresources/aspa/"><code>ASPA</code></a> API, and the number of records loaded and the snapshot timestamp are shown alongside the input.</p>
<p>Try the <a href="https://radar.cloudflare.com/routing/aspa-validation">ASPA validation tool</a> with a path of your own.</p>


<h2 id="web-analytics-improves-soft-navigation-measurement-for-single-page-applications-spas"><a href="/changelog/post/2026-08-21-improved-soft-navigation-measurement-for-single-page-applications/">Web Analytics improves soft navigation measurement for Single Page Applications (SPAs)</a></h2>
<p><em>2026-08-21</em></p>
<p>Cloudflare Web Analytics (Real User Monitoring) is rolling out accuracy improvements to client-side soft navigations. <strong>Update: this update is complete as of 2026-09-04.</strong></p>
<p><strong>This change may alter the volume of reported pageviews and visits in the dashboard and GraphQL API. The reported Largest Contentful Paint (LCP) metric may also fluctuate.</strong> The extent of these variances depend on your front-end architecture and visitor traffic patterns.</p>
<p>Single Page Applications (SPAs)—such as websites built with React, Angular, Vue, or Svelte—predominantly use soft navigations. Soft navigations avoid fully unloading the current page and rendering the next one from scratch as visitors navigate.</p>
<p>Any client-side navigation counts as a soft navigation, including navigations intercepted by <a href="https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API">the Navigation API</a> or triggered by <a href="https://developer.mozilla.org/en-US/docs/Web/API/History_API">the History API</a>. This means a non-SPA website can have soft navigation activity if its implementation uses these APIs.</p>
<p>The main improvement comes from <a href="https://developer.chrome.com/docs/web-platform/soft-navigations">Google Chrome's new Soft Navigation API</a>. It natively measures <a href="/web-analytics/data-metrics/core-web-vitals/#core-web-vitals-metrics">Largest Contentful Paint (LCP)</a> on soft navigations, removing a blind spot in perceived loading speed across pageviews.</p>
<p>We've extended our <code>navigationType</code> values to segment these different types of navigations:</p>
<table>
<thead>
<tr>
<th><code>navigationType</code></th>
<th>New?</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>navigate</code></td>
<td>❌</td>
<td>Hard navigations that traditional websites (or &quot;Multi Page Applications&quot;) perform when clicking links or submitting forms</td>
</tr>
<tr>
<td><code>soft-navigation</code></td>
<td>✅</td>
<td>Where <a href="https://developer.chrome.com/docs/web-platform/soft-navigations">the new Soft Navigation API</a> is available and a visitor makes a client-side navigation, we record these events</td>
</tr>
<tr>
<td><code>routing-apis</code></td>
<td>✅</td>
<td>Where the native Soft Navigation API is unavailable (e.g. Safari, Firefox, older Chromium-based browsers), we fallback to measuring soft navigations using <a href="https://developer.mozilla.org/en-US/docs/Web/API/Navigation_API">the Navigation API</a> or <a href="https://developer.mozilla.org/en-US/docs/Web/API/History_API">History API</a>. We cannot collect LCP for these, but the other Core Web Vitals are present.</td>
</tr>
</tbody>
</table>
<p>Prior to this change, we only used History API and all navigations were bucketed into <code>navigate</code>.</p>
<p>For more information, refer to the <a href="/web-analytics/data-metrics/dimensions/#navigation-types">Navigation Types</a> and <a href="/web-analytics/get-started/web-analytics-spa/">Web Analytics SPA</a> documentation pages.</p>


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


<h2 id="websocket-reporting-now-includes-full-connection-data-transfer-and-duration"><a href="/changelog/post/2026-08-14-websocket-data-transfer-reporting/">WebSocket reporting now includes full connection data transfer and duration</a></h2>
<p><em>2026-08-14</em></p>
<p>Cloudflare has fixed an issue affecting WebSocket data transfer and session duration reporting. HTTP Traffic Analytics and HTTP request logs now correctly report data transferred throughout a WebSocket connection and the duration of the full session. During the affected period, reporting captured only the bytes and duration of the initial <code>101 Switching Protocols</code> handshake for some WebSocket connections.</p>
<p>Customers with WebSocket traffic will see the correct <strong>Data Transfer</strong> in the dashboard and <code>EdgeResponseBytes</code> in analytics and HTTP request logs. Reported session duration now reflects the full WebSocket session rather than only the handshake. These changes restore the accounting of existing WebSocket traffic and duration. They do not indicate an increase in traffic or alter WebSocket connection behavior.</p>
<p>The separate <a href="/logs/logpush/logpush-job/datasets/zone/websocket_analytics/">WebSocket Analytics Logpush dataset</a> continues to provide per-connection directional byte counts, timestamps, and close details.</p>
<p>For more information about HTTP Traffic Analytics, refer to <a href="/analytics/account-and-zone-analytics/zone-analytics/#http-traffic">Zone Analytics</a>.</p>


<h2 id="as-level-connectivity-and-upstream-providers-on-cloudflare-radar"><a href="/changelog/post/2026-08-07-radar-as-connectivity-upstreams/">AS-level connectivity and upstream providers on Cloudflare Radar</a></h2>
<p><em>2026-08-07</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> expands its <a href="https://radar.cloudflare.com/routing">Routing section</a> with two widgets on AS pages, such as <a href="https://radar.cloudflare.com/routing/as13335">AS13335</a>, that describe how a network reaches the rest of the Internet: the paths it takes toward the <a href="https://en.wikipedia.org/wiki/Tier_1_network">Tier-1</a> networks, and the mix of direct upstreams carrying its routes. Both are derived from <a href="https://www.routeviews.org/">RouteViews</a> RIB snapshots, unioned across selected collectors.</p>
<h4 id="2026-08-07-radar-as-connectivity-upstreams-as-level-connectivity">AS-level connectivity</h4>
<p>The <strong>AS-level connectivity</strong> graph aggregates the BGP paths an AS uses to reach the Tier-1 networks, unioned across all the prefixes it announces, as observed by selected RouteViews collectors. It reads from left to right, starting at the queried AS and ending at the Tier-1 networks, and each node is labeled with its AS number, country, and organization name. Tier-1 nodes are marked so they stand apart from the intermediate networks that lead to them.</p>
<p>By default, the graph shows the network's direct connections to Tier-1 networks plus the indirect paths, which keeps the view readable. A <strong>Show full paths</strong> toggle expands it to every observed path, including transit through Tier-1 networks the AS already connects to. An IP version selector switches between IPv4 and IPv6, because the paths reaching Tier-1 networks may differ between the two address families.</p>
<p><img src="/assets/upstream/images/radar/as-level-connectivity-graph.png" alt="AS-level connectivity graph for AS13335, showing Tier-1 networks it reaches directly alongside paths that reach others through intermediate networks" /></p>
<p>This is the AS-level counterpart to the <strong>Real-time connectivity</strong> graph on prefix pages, such as the one for <a href="https://radar.cloudflare.com/routing/prefix/1.1.1.0/24">1.1.1.0/24</a>. Instead of covering a single prefix, it covers the union of paths for all prefixes an AS announces, which makes it a fast way to read a network's transit hierarchy: which providers it depends on, how many hops separate it from the core, and whether its paths to the core are diverse or concentrated. For more information on the prefix-level graph, refer to <a href="/radar/glossary/#bgp-real-time-routes">BGP real-time routes</a>.</p>
<h4 id="2026-08-07-radar-as-connectivity-upstreams-upstream-providers">Upstream providers</h4>
<p>The <strong>Upstream providers</strong> widget tracks the share of an AS's observed paths carried by each of its direct upstream networks over time, drawn as a stacked area chart. Up to 10 upstreams appear as their own series and the remaining ones are grouped into <strong>Other</strong>. Transit changes such as adding a provider, dropping one, or moving traffic between them appear as movement between bands rather than as a single aggregate number. As with the connectivity graph, an IP version selector switches between IPv4 and IPv6.</p>
<p><img src="/assets/upstream/images/radar/as-upstream-providers-timeseries.png" alt="Stacked area chart of the share of AS13335's observed paths carried by each of its top 10 direct upstreams, with the remainder grouped into Other" /></p>
<h4 id="2026-08-07-radar-as-connectivity-upstreams-api-endpoints">API endpoints</h4>
<p>The data behind both widgets is also available through two new endpoints on the <a href="/api/resources/radar/subresources/bgp/"><code>BGP</code></a> API:</p>
<ul>
<li><a href="/api/resources/radar/subresources/bgp/subresources/routes/subresources/paths/methods/list/"><code>/bgp/routes/paths/{asn}</code></a> — Returns the ordered AS path segments an AS uses to reach the Tier-1 networks, each with its observed path count, peer count, and contributing collectors, alongside the name and country of every ASN in the response. Pass <code>collector</code> to scope the result to a single RouteViews collector.</li>
<li><a href="/api/resources/radar/subresources/bgp/subresources/routes/subresources/upstreams/methods/timeseries/"><code>/bgp/routes/upstreams/{asn}/timeseries</code></a> — Returns the share of an AS's observed paths carried by each direct upstream over time. Use <code>limit</code> to control how many upstreams come back as separate series before the rest are grouped into an <code>OTHER</code> series, and <code>ipVersion</code> to select the address family.</li>
</ul>
<p>Visit the <a href="https://radar.cloudflare.com/routing/as13335">AS13335 routing page</a> to explore both widgets, or swap in any other AS number.</p>


<h2 id="radar-researcher-beta-and-webmcp-support-now-available"><a href="/changelog/post/2026-08-07-radar-researcher-and-webmcp/">Radar Researcher beta and WebMCP support now available</a></h2>
<p><em>2026-08-07</em></p>
<p><a href="/radar/"><strong>Cloudflare Radar</strong></a> now includes <a href="https://radar.cloudflare.com/?prompt=">Radar Researcher</a>, a beta AI-powered assistant for exploring Internet trends and traffic data in plain language. Open Researcher from the header on any Radar page to ask questions by voice or text, receive explanations, and view interactive charts based on Radar API data.</p>
<p><img src="/assets/upstream/images/radar/radar-researcher-panel.webp" alt="Screenshot of the Radar Researcher panel alongside the Radar overview page" /></p>
<p>To ask about a specific chart, select <strong>Explain with AI</strong> to start a conversation with its underlying data and context.</p>
<p><img src="/assets/upstream/images/radar/radar-explain-with-ai.webp" alt="Screenshot of the Explain with AI option in a Radar chart menu" /></p>
<p>You can explore further with suggested follow-up questions, find earlier conversations through searchable history, and share conversations through shareable links.</p>
<p>Alongside the user-facing Researcher experience, Radar now supports <a href="/browser-run/features/webmcp/">WebMCP</a>, allowing browser-based AI agents to navigate Radar, search data, and use tools such as URL scanning and domain lookup.</p>
<p>To get started, visit <a href="https://radar.cloudflare.com/">Cloudflare Radar</a>.</p>


<h2 id="improved-reliability-for-account-wide-web-analytics-dashboards"><a href="/changelog/post/2026-06-10-improved-reliability-for-web-analytics-dash/">Improved reliability for account-wide Web Analytics dashboards</a></h2>
<p><em>2026-07-14</em></p>
<p>Cloudflare Web Analytics (Real User Monitoring) has rolled out performance optimizations to significantly improve the stability and loading speed of account-wide dashboards.</p>
<p>For larger accounts (with &gt;100 Web Analytics sites), loading the aggregate account-wide view would often fail, running into timeouts or unexpected interface errors due to the massive scale of parallel query processing. This update optimizes how high-volume multi-site data is queried to reduce errors and provide a snappier dashboard experience.</p>
<p>Accounts with up to 1,000 sites will now be able to load this account-wide aggregate view without experiencing misleading errors.</p>
<p>If you have an account with over 1,000 sites, we cannot currently aggregate over this volume due to processing constraints but you will now be presented with a clear error and instruction to filter to the relevant site(s) you wish to see the data for.</p>


<h2 id="wi-fi-signal-and-network-performance-analytics-for-cloudflare-one-client-devices"><a href="/changelog/post/2026-07-09-warp-wifi-network-performance-analytics/">Wi-Fi signal and network performance analytics for Cloudflare One Client devices</a></h2>
<p><em>2026-07-09</em></p>
<p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into device, network, and application performance across your Cloudflare SASE deployment.</p>
<p>The <strong>Device Monitoring</strong> page now analyzes hardware and network data between a Cloudflare One Client device and Cloudflare's edge, so you can diagnose connectivity and performance issues. Previously, this data was only available in raw DEX Device State Event logs, which required you to build your own analytics to interpret it.</p>
<p><img src="/assets/upstream/images/changelog/dex/dex-device-monitoring-summary.png" alt="Device Monitoring summary with connection status, connection mode, Wi-Fi signal strength, traffic performance, and device health" /></p>
<p>A summary at the top of the page shows the health of each category at a glance, using <strong>Good</strong>, <strong>Fair</strong>, and <strong>Poor</strong> labels:</p>
<ul>
<li><strong>Connection</strong> — connection status, Cloudflare One Client mode, and tunnel type over time</li>
<li><strong>Wi-Fi signal strength</strong> — signal measured in dBm over time, with thresholds that flag a weak signal</li>
<li><strong>Traffic performance</strong> — upstream and downstream performance, including network throughput on the active interface</li>
<li><strong>Device health</strong> — hardware metrics such as CPU, memory, and disk</li>
</ul>
<p><img src="/assets/upstream/images/changelog/dex/dex-device-monitoring-wifi-network.png" alt="Wi-Fi signal strength and network throughput charts on the Device Monitoring page" /></p>
<p>You can filter by category and adjust the time range to correlate a device's metrics with a user's reported issue.</p>
<p>These analytics are available to all Cloudflare One customers at no additional cost.</p>
<p>To learn more, refer to the <a href="/cloudflare-one/insights/dex/monitoring/">DEX monitoring documentation</a>.</p>


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


<h2 id="precise-ip-location-and-richer-as-details-on-the-cloudflare-radar-ip-page"><a href="/changelog/post/2026-06-24-radar-ip-page-improvements/">Precise IP location and richer AS details on the Cloudflare Radar IP page</a></h2>
<p><em>2026-06-24</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> now plots your IPv4 and IPv6 locations on the <a href="https://radar.cloudflare.com/ip">IP page</a>, shows the Cloudflare data centers serving your connection, and includes more detail about the autonomous system (AS) your primary IP belongs to.</p>
<h4 id="2026-06-24-radar-ip-page-improvements-your-ip-location-on-the-map">Your IP location on the map</h4>
<p>The map of your connection now shows:</p>
<ul>
<li><strong>IP location markers</strong> — The primary IP will show as a red marker. When both IP addresses do not geolocate to the same place, a second marker will appear in blue with a note explaining why IPv4 and IPv6 can resolve to different locations.</li>
<li><strong>Cloudflare data center markers</strong> — Cloudflare data centers now show as orange dots on the map and the one you are connected to is highlighted.</li>
<li><strong>Data center connectors</strong> — Each line connects your IP markers to their respective data centers.</li>
</ul>
<p><img src="/assets/upstream/images/radar/ip-page-geolocation.png" alt="Map showing Cloudflare data centers and a marker representing the IP location with a line connected to a data center" /></p>
<p>Due to the data policies of our geolocation provider, this detailed location is only available for your own IP. Other IP addresses keep the current country-level view.</p>
<h4 id="2026-06-24-radar-ip-page-improvements-extended-as-information">Extended AS information</h4>
<p>The AS card on the IP page now shows additional detail about the network an IP belongs to — including alternate names, the operator website, and an estimate of the AS user population — alongside the AS number and country.</p>
<p>Visit the <a href="https://radar.cloudflare.com/ip">Cloudflare Radar IP page</a> to explore more details about your IP.</p>


<h2 id="regionalized-ip-bindings-for-regional-services"><a href="/changelog/post/2026-06-23-regionalized-ip-bindings/">Regionalized IP Bindings for Regional Services</a></h2>
<p><em>2026-06-23</em></p>
<p>Regional Services now supports <strong>Regionalized IP Bindings</strong>, letting you regionalize traffic at the IP layer for prefixes you bring to Cloudflare through <a href="/byoip/">Bring Your Own IP (BYOIP)</a>.</p>
<p>Where <a href="/data-localization/regional-services/regional-hostnames/">Regional Hostnames</a> regionalize traffic by hostname, Regionalized IP Bindings let you bind a CIDR from one of your prefixes to a region — ideal for address-map deployments and any service you address by IP rather than hostname. Cloudflare then terminates TLS and processes traffic to those addresses only within the data centers in that region.</p>
<p>Regionalized IP Bindings requires the Regional Services and Regional Services for BYOIP entitlements. Contact your account team to enable them.</p>
<p>To get started, refer to <a href="/data-localization/regional-services/ip-bindings/">Regionalized IP Bindings</a>.</p>


<h2 id="updated-workers-ai-popularity-metric-in-cloudflare-radar"><a href="/changelog/post/2026-06-18-radar-workers-ai-inference-metric/">Updated Workers AI popularity metric in Cloudflare Radar</a></h2>
<p><em>2026-06-18</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> has changed how it measures <a href="/workers-ai/">Workers AI</a> model and task popularity.</p>
<p>Previously, popularity was based on the number of unique accounts running inferences against each model or task. It is now based on the <strong>number of inferences</strong>, giving a more representative view of actual usage volume. This change will affect all new measurements as well as historical data. As a result, the model and task distributions shown on Radar may differ from what you saw previously, and historical trends may shift accordingly.</p>
<p>The <a href="https://radar.cloudflare.com/ai-insights#workers-ai-model-popularity">Workers AI model popularity</a> chart shows the distribution of inferences across models.</p>
<p><img src="/assets/upstream/images/radar/workers-ai-model-popularity.png" alt="Screenshot of the Workers AI model popularity chart on the AI Insights page" /></p>
<p>The <a href="https://radar.cloudflare.com/ai-insights#workers-ai-task-popularity">Workers AI task popularity</a> chart shows the distribution of inferences across tasks.</p>
<p><img src="/assets/upstream/images/radar/workers-ai-task-popularity.png" alt="Screenshot of the Workers AI task popularity chart on the AI Insights page" /></p>
<p>The same data is available via the following API endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/ai/subresources/inference/methods/summary_v2/"><code>/ai/inference/summary/{dimension}</code></a></li>
<li><a href="/api/resources/radar/subresources/ai/subresources/inference/methods/timeseries_groups_v2/"><code>/ai/inference/timeseries_groups/{dimension}</code></a></li>
</ul>
<p>Explore the data on the <a href="https://radar.cloudflare.com/ai-insights">AI Insights page</a>.</p>


<h2 id="automated-cease-and-desist-templates-for-brand-protection"><a href="/changelog/post/2026-06-08-brand-protection-cease-and-desist-letters/">Automated Cease and Desist templates for Brand Protection</a></h2>
<p><em>2026-06-10</em></p>
<p><strong>TL;DR:</strong> Brand Protection now features an <strong>Automated Cease &amp; Desist (C&amp;D)</strong> workflow. When you discover an infringing domain hosted outside of Cloudflare, you can instantly generate, review, and download a custom-branded, pre-filled legal notice in seconds.</p>
<h4 id="2026-06-08-brand-protection-cease-and-desist-letters-why-this-matters">Why this matters</h4>
This update introduces a major shift from pure detection to actionable enforcement, eliminating the manual burden for your Trust & Safety and Legal teams:
<ul>
<li><strong>Instant WHOIS and Recipient Lookup:</strong> We automatically scrape registrar data and WHOIS contact information (such as the registrant or registrar abuse email) behind the scenes, highlighting exactly where your notice needs to be sent</li>
<li><strong>Smart Template Automation:</strong> We pre-fill your custom-branded templates with essential metadata, including the infringing domain, registrar name, and discovery date.</li>
<li><strong>Tailored Enforcement Tones:</strong> Choose from three default layout strategies depending on the severity of the infrastructure match:
<ul>
<li><em>Exact Match:</em> A formal demand for identical trademark infringements</li>
<li><em>Similar Match:</em> A standard notice optimized for typosquatting (one-character distance matches)</li>
<li><em>Friendly Tone:</em> An amicable initial outreach for potential unintentional or accidental infringements</li>
</ul>
</li>
<li><strong>Full Editing Control:</strong> Before creating the final PDF, a real-time review screen allows you to fine-tune the messaging, modify placeholders, and ensure your text aligns perfectly with internal legal standards</li>
</ul>
<h4 id="2026-06-08-brand-protection-cease-and-desist-letters-how-it-works">How it works</h4>
When reviewing a malicious domain match inside your dashboard, your enforcement path splits depending on where the attacker is located:
<ol>
<li><strong>On the Cloudflare Network:</strong> If the domain uses Cloudflare’s network or registrar, trigger our existing integrated abuse reporting flow with one click.</li>
<li><strong>Hosted Elsewhere:</strong> If the domain is hosted on an external provider, click the <strong>Generate C&amp;D Letter</strong> option to launch the new document builder, pick your template, verify the auto-populated recipient data, and download your finalized PDF.</li>
</ol>
<p>You can manage your templates and enforce matches by going to the <strong>Cloudflare Dashboard &gt; Application Security &gt; Brand Protection</strong> and selecting your detected Brand Protection matches.
For more information, read the <a href="/security-center/brand-protection/">Brand Protection documentation</a>.</p>
<blockquote>
<p><strong>Note:</strong> Cloudflare does not represent you and cannot provide you with legal advice. Only you can decide whether your rights have been infringed, whether a cease and desist letter is appropriate, and what that letter should say.</p>
</blockquote>


<h2 id="create-waf-rules-directly-from-threat-events-saved-views"><a href="/changelog/post/2026-06-08-create-waf-rules-from-threat-events/">Create WAF rules directly from Threat Events saved views</a></h2>
<p><em>2026-06-08</em></p>
<p>Cloudforce One users can now turn <a href="/security-center/cloudforce-one/#analyze-threat-events">Threat Events indicators</a> into active defense. With this update, users can instantly generate a WAF rule that matches the dynamic list of IP addresses returned by any of their <strong>Saved Views</strong>.</p>
<h4 id="2026-06-08-create-waf-rules-from-threat-events-why-this-matters">Why this matters</h4>
<p>Threat intelligence is most effective when it is immediately actionable. Previously, blocking threat actors required manually extracting indicators from threat events and copying them into your firewall rules.
This new integration bridges the gap between threat discovery and threat mitigation:</p>
<ul>
<li>When you identify an active threat pattern - such as an ongoing campaign targeting a specific industry, or using a known indicator type - you can pivot from investigation to mitigation in a single click.</li>
<li>Instead of writing complex, static IP rules, this functionality allows you to leverage the specific filtering logic you have already defined and saved within your Threat Events ecosystem.</li>
<li>Automating the generation of the WAF rule expression from your threat views eliminates manual copying errors, ensuring that the right malicious infrastructure is blocked instantly.</li>
</ul>
<h4 id="2026-06-08-create-waf-rules-from-threat-events-how-to-use-it">How to use it</h4>
<p>You can implement these rules through both the dashboard UI and via the API / Terraform.</p>
<p>Go to <strong>Cloudflare Dashboard</strong> &gt; <strong>Application Security</strong> &gt; <strong>Threat Intelligence</strong> &gt; <strong>Manage Views</strong>, select your desired view, and select <strong>Create WAF Rule</strong>.</p>
<p>This will automatically pre-populate the <a href="/firewall/cf-dashboard/create-edit-delete-rules/">WAF rule builder</a> with the matching threat event IP indicators.</p>
<p>You can also automate this workflow by utilizing the <a href="/firewall/api/cf-firewall-rules/"><strong>WAF Rule Builder API</strong></a> alongside your <a href="/firewall/api/cf-firewall-rules/">Threat Events saved views endpoints</a>.</p>


<h2 id="introducing-threat-actor-profiles-in-threat-events"><a href="/changelog/post/2026-06-08-threat-actor-profiles/">Introducing Threat Actor Profiles in Threat Events</a></h2>
<p><em>2026-06-08</em></p>
<p><strong>TL;DR:</strong> We’ve launched <strong>Threat Actor Profiles</strong> directly inside the Threat Events dashboard. You can now immediately pivot from a generic alert or blocked event to a profile that unmasks the &quot;Who, Why, and How&quot; behind a threat event.</p>
<h4 id="2026-06-08-threat-actor-profiles-why-this-matters">Why this matters</h4>
Security teams often suffer from a visibility gap. When an attack is blocked, it's difficult to know if it was a random automated bot or a sophisticated advanced persistent threat (APT) campaign specifically targeting your industry. Finding out usually means leaving your security dashboard to hunt through external OSINT feeds or static, out-of-date threat reports.
Threat Actor Profiles solve this by sharing Cloudforce One’s deep adversary research directly inside your workflow:
* Cloudflare sees the traffic in real-time across approximately 20% of the web. This means actor profiles display active malicious infrastructure the moment it touches our global edge.
* Every profile provides clear strategic and tactical modules including alternative aliases, origin tracking, historical threat event volume, and MITRE ATT&CK mapping detailing the adversary's technical methods.
* You can search the dedicated threat actor directory or click an actor's name inside any threat event to view all details and related events to the specific threat actor.
<h4 id="2026-06-08-threat-actor-profiles-how-to-use-it">How to use it</h4>
Adversary tracking is now available in the Cloudflare Dashbboard and ready to be included in your daily investigation workflow:
* Click on the **Threat Actor** name in the Threat Events table to open their full identity profile and review their aliases and attack stats.
* Navigate to **Cloudflare Dashboard > Application Security > Threat Intelligence** to explore the new **Threat Actors** tab. Here, you can browse a card-based directory of all established entities tracked by Cloudforce One.
<p>Learn more in the <a href="https://developers.cloudflare.com/security-center/cloudforce-one/#identify-the-adversary">Cloudforce One documentation</a>.</p>


<h2 id="finer-grained-chart-granularity-on-cloudflare-radar-for-longer-time-ranges"><a href="/changelog/post/2026-06-05-radar-traffic-chart-granularity/">Finer-grained chart granularity on Cloudflare Radar for longer time ranges</a></h2>
<p><em>2026-06-05</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> now provides finer-grained traffic charts for longer time ranges. Previously, selecting a 1-3 month view on HTTP and NetFlows charts defaulted to weekly aggregation, which was too coarse to surface meaningful trends. Views longer than 3 months defaulted to monthly aggregation, returning as few as 7 data points for a 6-month range.</p>
<p>The new defaults are:</p>
<ul>
<li><strong>1-3 months</strong>: daily granularity (7x more data points)</li>
<li><strong>Longer than 3 months</strong> (HTTP and NetFlows): weekly granularity (4x more data points)</li>
</ul>
<p>For example, a 12-week traffic view previously showed weekly data:</p>
<p><img src="/assets/upstream/images/radar/traffic-granularity-12w-before.png" alt="Traffic trends chart with weekly granularity for a 12-week view" /></p>
<p>The same view now shows daily data:</p>
<p><img src="/assets/upstream/images/radar/traffic-granularity-12w-after.png" alt="Traffic trends chart with daily granularity for a 12-week view" /></p>
<p>Similarly, a 1-year HTTP traffic view that previously showed just 12 monthly data points now provides 52 weekly data points.</p>
<p>Visit <a href="https://radar.cloudflare.com/?dateRange=12w#traffic-trends">Cloudflare Radar</a> to explore the new granular views.</p>


<nav class="pagination" aria-label="Changelog pages"><span>Page 1 of 6</span><a class="pagination-next" rel="next" href="/changelog/product-group/analytics/2/">Next</a></nav>
