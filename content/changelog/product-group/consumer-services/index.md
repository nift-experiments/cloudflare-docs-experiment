<h1 id="changelog">Changelog</h1>

<h2 id="radar-search-now-includes-internet-events"><a href="/changelog/post/2026-09-08-radar-search-events/">Radar search now includes Internet events</a></h2>
<p><em>2026-09-08</em></p>
<p><a href="/radar/"><strong>Cloudflare Radar</strong></a> search now includes Internet events and outages alongside existing results. Search event descriptions or related entities, such as locations, ASes, bots, and top-level domains, to find relevant events and open the most relevant Radar view.</p>
<p><img src="/assets/upstream/images/radar/radar-search-events.png" alt="Radar search results showing Internet outage events associated with locations and autonomous systems" /></p>
<p>Event links preserve the event date range, making it easier to investigate what changed before, during, and after an event. These results are also available to browser-based AI agents through <a href="/browser-run/features/webmcp/">WebMCP</a>.</p>


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


<h2 id="improved-doh-json-formatting-for-additional-record-types"><a href="/changelog/post/2026-07-28-improved-record-display-format/">Improved DoH JSON formatting for additional record types</a></h2>
<p><em>2026-07-28</em></p>
<p>Cloudflare is rolling out updated formatting for the <code>data</code> field in the 1.1.1.1 <a href="/1.1.1.1/encryption/dns-over-https/make-api-requests/dns-json/">DoH JSON API</a> (<code>application/dns-json</code>). During the roll out responses may use either the old or new format.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17613.md")</aside>
<h4 id="2026-07-28-improved-record-display-format-human-readable-display-for-additional-record-types">Human-readable display for additional record types</h4>
<p>Several record types previously returned their <code>data</code> field in <a href="https://datatracker.ietf.org/doc/html/rfc3597">RFC 3597</a> generic hex encoding (<code>\# &lt;length&gt; &lt;hex&gt;</code>). These now use standard presentation format:</p>
<pre><code class="language-txt">CAA:        0 issue &quot;letsencrypt.org&quot;&#10;NAPTR:      100 10 &quot;s&quot; &quot;SIP+D2U&quot; &quot;&quot; _sip._udp.example.com.&#10;RP:         admin.example.com. txt.example.com.&#10;IPSECKEY:   10 1 2 192.0.2.1 AwEA...&#10;SVCB:       1 target.example.com. alpn=h2&#10;HTTPS:      1 . alpn=h3,h2 ipv4hint=192.0.2.1&#10;TLSA:       3 1 1 aabbccdd...&#10;SSHFP:      1 2 aabbccdd...&#10;OPENPGPKEY: AwEA...&#10;</code></pre>
<h4 id="2026-07-28-improved-record-display-format-numeric-dnssec-algorithm-identifiers">Numeric DNSSEC algorithm identifiers</h4>
<p>DNSSEC-related records now use numeric algorithm identifiers as defined in <a href="https://datatracker.ietf.org/doc/html/rfc4034">RFC 4034</a> instead of mnemonic names. This affects <code>RRSIG</code>, <code>DS</code>, <code>CDS</code>, <code>DNSKEY</code>, and <code>CDNSKEY</code> records. For example, <code>RSASHA256</code> becomes <code>8</code>, <code>ECDSAP256SHA256</code> becomes <code>13</code>, and <code>ED25519</code> becomes <code>15</code>. DS digest types also change from mnemonic to numeric: <code>SHA-256</code> becomes <code>2</code>.</p>
<pre><code class="language-txt">RRSIG:  A RSASHA256 2 300 ...&#10;DS:     12345 RSASHA256 SHA-256 aabb...&#10;DNSKEY: 257 3 RSASHA256 AwEA...&#10;</code></pre>
<pre><code class="language-txt">RRSIG:  A 8 2 300 ...&#10;DS:     12345 8 2 aabb...&#10;DNSKEY: 257 3 8 AwEA...&#10;</code></pre>
<h4 id="2026-07-28-improved-record-display-format-other-formatting-changes">Other formatting changes</h4>
<p><code>HINFO</code> character-strings are now individually quoted to remove ambiguity when values contain spaces:</p>
<pre><code class="language-txt">&quot;data&quot;: &quot;Intel Xeon Linux&quot;&#10;</code></pre>
<pre><code class="language-txt">&quot;data&quot;: &quot;\&quot;Intel Xeon\&quot; \&quot;Linux\&quot;&quot;&#10;</code></pre>


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


<h2 id="tls-bug-detection-in-the-cloudflare-radar-post-quantum-checker"><a href="/changelog/post/2026-05-29-radar-pq-tls-bug-detection/">TLS bug detection in the Cloudflare Radar post-quantum checker</a></h2>
<p><em>2026-05-29</em></p>
<p>The <a href="/radar/"><strong>Radar</strong></a> <a href="https://radar.cloudflare.com/post-quantum#website-support">post-quantum TLS support checker</a> now also reports TLS bugs detected during the handshake test. When a scanned host exhibits compatibility issues, the results include details on the specific bugs detected, along with guidance on how to investigate and remediate each issue. The bugs section only appears for hosts where issues are found.</p>
<p>The following TLS bugs are detected:</p>
<ul>
<li><strong>Split ClientHello</strong> — The connection fails with a fragmented post-quantum <code>ClientHello</code> but succeeds with classical handshakes. Typically caused by middleboxes or firewalls that cannot reassemble split TLS messages.</li>
<li><strong>HRR Failure</strong> — The server sends a <code>HelloRetryRequest</code> but fails to complete the handshake afterward.</li>
<li><strong>Unknown Keyshare</strong> — The server cannot handle unknown key exchange algorithms and fails instead of responding with a <code>HelloRetryRequest</code> as required by the TLS 1.3 specification.</li>
</ul>
<p><img src="/assets/upstream/images/radar/pq-tls-bug-detection.png" alt="TLS bug detection results in the Radar post-quantum checker" /></p>
<p>Bug detection data is available through the existing <a href="/api/resources/radar/subresources/post_quantum/subresources/tls/methods/support/"><code>/post_quantum/tls/support</code></a> endpoint.</p>
<p>Visit the <a href="https://radar.cloudflare.com/post-quantum#website-support">Post-Quantum Encryption</a> page to test a host.</p>


<h2 id="content-type-distribution-and-api-traffic-share-on-cloudflare-radar"><a href="/changelog/post/2026-05-20-radar-content-type-and-api-traffic/">Content type distribution and API traffic share on Cloudflare Radar</a></h2>
<p><em>2026-05-20</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> now includes two new charts on the <a href="https://radar.cloudflare.com/traffic">traffic page</a> that provide deeper insights into the composition of HTTP traffic: a content type distribution chart and an API traffic share chart.</p>
<h4 id="2026-05-20-radar-content-type-and-api-traffic-content-type-distribution">Content type distribution</h4>
<p>The new <a href="https://radar.cloudflare.com/traffic#content-type"><strong>Content type</strong></a> chart displays the distribution of HTTP response content types, grouped into high-level categories. A traffic type selector allows filtering by human, bot, or all traffic. The existing <a href="https://radar.cloudflare.com/traffic#bot-vs-human"><strong>Bot vs. Human</strong></a> chart also gained a content type category filter, allowing users to see the bot/human split for specific content categories.</p>
<p><img src="/assets/upstream/images/radar/content-type-distribution.png" alt="Screenshot of the content type distribution chart on the Radar traffic page" /></p>
<p>Content type categories:</p>
<ul>
<li><strong>HTML</strong> — Web pages (<code>text/html</code>)</li>
<li><strong>Images</strong> — All image formats (<code>image/*</code>)</li>
<li><strong>JSON</strong> — JSON data and API responses (<code>application/json</code>, <code>*+json</code>)</li>
<li><strong>JavaScript</strong> — Scripts (<code>application/javascript</code>, <code>text/javascript</code>)</li>
<li><strong>CSS</strong> — Stylesheets (<code>text/css</code>)</li>
<li><strong>Plain Text</strong> — Unformatted text (<code>text/plain</code>)</li>
<li><strong>Fonts</strong> — Web fonts (<code>font/*</code>, <code>application/font-*</code>)</li>
<li><strong>XML</strong> — XML documents and feeds (<code>text/xml</code>, <code>application/xml</code>, <code>application/rss+xml</code>, <code>application/atom+xml</code>)</li>
<li><strong>YAML</strong> — Configuration files (<code>text/yaml</code>, <code>application/yaml</code>)</li>
<li><strong>Video</strong> — Video content and streaming (<code>video/*</code>, <code>application/ogg</code>, <code>*mpegurl</code>)</li>
<li><strong>Audio</strong> — Audio content (<code>audio/*</code>)</li>
<li><strong>Markdown</strong> — Markdown documents (<code>text/markdown</code>)</li>
<li><strong>Documents</strong> — PDFs, Office documents, ePub, CSV (<code>application/pdf</code>, <code>application/msword</code>, <code>text/csv</code>)</li>
<li><strong>Binary</strong> — Executables, archives, WebAssembly (<code>application/octet-stream</code>, <code>application/zip</code>, <code>application/wasm</code>)</li>
<li><strong>Serialization</strong> — Binary API formats (<code>application/protobuf</code>, <code>application/grpc</code>, <code>application/msgpack</code>)</li>
<li><strong>Other</strong> — All other content types</li>
</ul>
<p>The <code>CONTENT_TYPE</code> dimension and <code>contentType</code> filter are available on the HTTP <a href="/api/resources/radar/subresources/http/methods/summary_v2/">summary</a>, <a href="/api/resources/radar/subresources/http/methods/timeseries_groups_v2/">timeseries groups</a>, and <a href="/api/resources/radar/subresources/http/methods/timeseries/">timeseries</a> endpoints.</p>
<h4 id="2026-05-20-radar-content-type-and-api-traffic-api-traffic-share">API traffic share</h4>
<p>The new <a href="https://radar.cloudflare.com/traffic#api-traffic"><strong>API traffic</strong></a> chart shows the percentage of dynamic (non-cacheable) HTTP request traffic that is API-related. API traffic is identified by JSON or XML response content types (<code>application/json</code>, <code>application/xml</code>, <code>text/xml</code>) on HTTP requests that returned a 200 status code. A traffic type selector allows switching between human traffic, bot traffic, or all traffic.</p>
<p><img src="/assets/upstream/images/radar/api-traffic-share.png" alt="Screenshot of the API traffic share chart on the Radar traffic page" /></p>
<p>The <code>API_TRAFFIC</code> dimension is available on the existing HTTP <a href="/api/resources/radar/subresources/http/methods/summary_v2/">summary</a> and <a href="/api/resources/radar/subresources/http/methods/timeseries_groups_v2/">timeseries groups</a> endpoints. An <code>apiTraffic</code> filter (<code>API</code> or <code>NON_API</code>) can also be applied to <a href="/api/resources/radar/subresources/http/methods/timeseries/">HTTP timeseries</a> requests to retrieve raw request counts for API-only or non-API traffic.</p>
<p>Visit the <a href="https://radar.cloudflare.com/traffic">Radar traffic page</a> to explore these new charts.</p>


<h2 id="mrt-explorer-on-cloudflare-radar"><a href="/changelog/post/2026-05-19-radar-mrt-explorer/">MRT Explorer on Cloudflare Radar</a></h2>
<p><em>2026-05-19</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> now includes an <a href="https://radar.cloudflare.com/routing/mrt-explorer">MRT Explorer</a> tool in the Routing section. Route collectors like RIPE RIS and RouteViews publish MRT (Multi-Threaded Routing Toolkit) dump files containing BGP announcements, withdrawals, and route attributes. The new tool parses these files entirely in the browser — nothing gets uploaded.</p>
<h4 id="2026-05-19-radar-mrt-explorer-loading-a-file">Loading a file</h4>
<p>Paste a URL to fetch an MRT file remotely, drag and drop one onto the page, or browse for a local file. Gzip and bzip2 compressed files are supported. A sample file is also available to get started right away.</p>
<p><img src="/assets/upstream/images/radar/mrt-explorer-form.png" alt="Screenshot of the MRT Explorer file input form" /></p>
<h4 id="2026-05-19-radar-mrt-explorer-inspecting-events">Inspecting events</h4>
<p>Once parsed, the tool lists every BGP event with its timestamp, prefix, AS path, OTC (Only to Customer), and community attributes.</p>
<p><img src="/assets/upstream/images/radar/mrt-explorer-list.png" alt="Screenshot of the MRT Explorer event list" /></p>
<h4 id="2026-05-19-radar-mrt-explorer-event-details">Event details</h4>
<p>Clicking on the &quot;View details&quot; action opens a modal with additional properties and the full event JSON.</p>
<p><img src="/assets/upstream/images/radar/mrt-explorer-details.png" alt="Screenshot of the MRT Explorer event details modal" /></p>
<h4 id="2026-05-19-radar-mrt-explorer-shareable-urls">Shareable URLs</h4>
<p>When loading a file by URL, the query string captures the source so the link can be shared directly — the recipient's browser immediately fetches and parses the same file.</p>
<p>Try the <a href="https://radar.cloudflare.com/routing/mrt-explorer">MRT Explorer on Cloudflare Radar</a>.</p>


<h2 id="tld-nameserver-performance-in-cloudflare-radar"><a href="/changelog/post/2026-05-06-radar-tld-nameserver-performance/">TLD Nameserver Performance in Cloudflare Radar</a></h2>
<p><em>2026-05-06</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> now provides TLD authoritative nameserver performance insights, measuring response time (latency) as observed from Cloudflare's <a href="/1.1.1.1/">1.1.1.1</a> resolver infrastructure when forwarding queries upstream to TLD nameservers.</p>
<p>New widgets on <a href="https://radar.cloudflare.com/tlds/com">TLD detail pages</a>:</p>
<ul>
<li><a href="https://radar.cloudflare.com/tlds/com#tld-ns-latency"><strong>Aggregate nameserver latency</strong></a>: Response time percentiles (p25/p50/p75) for all authoritative nameservers of the selected TLD.</li>
<li><a href="https://radar.cloudflare.com/tlds/com#tld-ns-latency-by-ns"><strong>Latency per nameserver</strong></a>: Median response time (p50) broken down by each authoritative nameserver over time.</li>
</ul>
<p><img src="/assets/upstream/images/radar/tld-nameserver-latency-by-ns.png" alt="Latency per nameserver chart" /></p>
<ul>
<li><a href="https://radar.cloudflare.com/tlds/com#geographical-distribution"><strong>Median latency geographic distribution</strong></a>: p50 response time by Cloudflare data center country, displayed on a choropleth map.</li>
<li><a href="https://radar.cloudflare.com/tlds/com#tld-ranking"><strong>TLD ranking over time</strong></a>: Daily DNS magnitude rank and magnitude value with a Rank/Magnitude toggle.</li>
<li><a href="https://radar.cloudflare.com/tlds"><strong>Rank change deltas</strong></a>: 1 week, 4 weeks, and 3 months rank changes added to the TLD magnitude table and the TLD detail info panel.</li>
</ul>
<p><img src="/assets/upstream/images/radar/tld-magnitude-rank-deltas.webp" alt="TLD Rankings by DNS Magnitude table with rank change deltas" /></p>
<p>The new <a href="/api/resources/radar/subresources/tlds/subresources/performance/"><code>TLD Performance</code></a> API provides the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/tlds/subresources/performance/methods/summary/"><code>/tlds/performance/summary/{dimension}</code></a> — TLD nameserver performance summarized by dimension.</li>
<li><a href="/api/resources/radar/subresources/tlds/subresources/performance/methods/timeseries_groups/"><code>/tlds/performance/timeseries_groups/{dimension}</code></a> — TLD nameserver performance over time grouped by dimension.</li>
</ul>
<p>Available dimensions: <code>LATENCY</code> (aggregate p25/p50/p75), <code>NAMESERVER_LATENCY</code> (per-nameserver p50), <code>LOCATION_LATENCY</code> (per-data-center-country p50).</p>
<p>TLD Performance is also available as a dataset in the <a href="https://radar.cloudflare.com/explorer?dataSet=tlds.performance">Data Explorer</a>.</p>
<p>Check out the updated <a href="https://radar.cloudflare.com/tlds/com">TLD detail page</a>.</p>


<h2 id="new-routing-widgets-on-cloudflare-radar"><a href="/changelog/post/2026-05-04-radar-routing-widgets/">New routing widgets on Cloudflare Radar</a></h2>
<p><em>2026-05-04</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> is expanding its <a href="https://radar.cloudflare.com/routing">Routing section</a> with two new widgets that give a deeper view into how networks announce address space and how RPKI ROA coverage evolves over time.</p>
<h4 id="2026-05-04-radar-routing-widgets-top-ases-by-announced-ip-space-on-country-pages">Top ASes by announced IP space on country pages</h4>
<p>Country routing pages now include a <strong>Top ASes by announced IP space</strong> chart, breaking down the IPv4 and IPv6 address space announced from a country across the autonomous systems that originate it. The chart stacks the IPv4 and IPv6 views vertically, with the top contributing ASes called out by color and the remaining networks aggregated as <strong>Other</strong>.</p>
<p><img src="/assets/upstream/images/radar/country-top-ases-ip-space.png" alt="Screenshot of the top ASes by announced IP space chart on a country routing page" /></p>
<h4 id="2026-05-04-radar-routing-widgets-rpki-roa-deployment-timeseries">RPKI ROA deployment timeseries</h4>
<p>The <a href="https://radar.cloudflare.com/routing/rpki">RPKI sub-page</a> adds an <strong>RPKI ROA deployment</strong> timeseries widget that tracks the share of announced BGP space covered by a valid Route Origin Authorization (ROA) over time, with separate IPv4 and IPv6 lines. A toggle switches the view between the share of covered <strong>prefixes</strong> and the share of covered <strong>IP address space</strong>. The widget is available on global, country, and AS views, so operators can monitor RPKI adoption progress and compare deployment trends across different scopes.</p>
<p><img src="/assets/upstream/images/radar/rpki-roa-deployment-timeseries.png" alt="Screenshot of the RPKI ROA deployment timeseries widget" /></p>
<h4 id="2026-05-04-radar-routing-widgets-api-endpoints">API endpoints</h4>
<p>The data behind these widgets is also available through two new endpoints on the <a href="/api/resources/radar/subresources/bgp/"><code>BGP</code></a> API:</p>
<ul>
<li><a href="/api/resources/radar/subresources/bgp/subresources/ips/subresources/top/methods/ases/"><code>/bgp/ips/top/ases</code></a> - Returns the top autonomous systems by announced IP space (IPv4 <code>/24</code>s or IPv6 <code>/48</code>s), globally or filtered by country, snapped to the nearest 8-hour RIB boundary.</li>
<li><a href="/api/resources/radar/subresources/bgp/subresources/rpki/subresources/roas/methods/timeseries/"><code>/bgp/rpki/roas/timeseries</code></a> - Returns RPKI ROA validation coverage over time, by share of prefixes or share of IP address space, split by IP version, with optional ASN or location filters.</li>
</ul>
<p>Visit the <a href="https://radar.cloudflare.com/routing">Radar routing section</a> to explore both widgets.</p>


<h2 id="cloud-observatory-connection-metrics-improvements"><a href="/changelog/post/2026-04-30-radar-cloud-observatory-connection-metrics/">Cloud Observatory connection metrics improvements</a></h2>
<p><em>2026-04-30</em></p>
<p>The <a href="https://radar.cloudflare.com/cloud-observatory">Cloud Observatory</a> on <a href="/radar/"><strong>Radar</strong></a> now provides improved connection metric insights, offering new ways to explore TCP round-trip time, TCP handshake duration, TLS handshake duration, and response header receive duration across cloud provider origin servers.</p>
<p>The <a href="https://radar.cloudflare.com/cloud-observatory#connection-metrics">Cloud Observatory overview</a> now shows connection metrics broken down by cloud provider, making it easy to compare connection performance across Amazon Web Services, Google Cloud, Microsoft Azure, and Oracle Cloud.</p>
<p><img src="/assets/upstream/images/radar/cloud-observatory-connection-metrics-by-provider.png" alt="Screenshot of Cloud Observatory connection metrics broken down by cloud provider" /></p>
<p>Each <a href="https://radar.cloudflare.com/cloud-observatory/amazon#connection-metrics">provider page</a> now shows connection metrics for the top five regions, with a selector to rank by lowest or highest values.</p>
<p><img src="/assets/upstream/images/radar/cloud-observatory-connection-metrics-by-region.png" alt="Screenshot of Cloud Observatory connection metrics broken down by region for a provider" /></p>
<p>Each <a href="https://radar.cloudflare.com/cloud-observatory/amazon/us-east-1#connection-metrics">region page</a> now displays connection metrics as percentile distributions (25th percentile, median, and 75th percentile), providing insight into the range and variability of connection times.</p>
<p><img src="/assets/upstream/images/radar/cloud-observatory-connection-metrics-percentiles.png" alt="Screenshot of Cloud Observatory connection metrics with percentile distribution for a region" /></p>
<p>These views are also available through the <a href="/api/resources/radar/subresources/origins/"><code>Origins</code> API</a>, using the <code>timeseries_groups</code> endpoint with the <code>ORIGIN</code>, <code>REGION</code>, or <code>PERCENTILE</code> dimension.</p>


<h2 id="dark-mode-support-on-cloudflare-radar"><a href="/changelog/post/2026-04-30-radar-dark-mode/">Dark mode support on Cloudflare Radar</a></h2>
<p><em>2026-04-30</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> now supports <strong>dark mode</strong>. A theme selector in the upper right corner of the page lets users explicitly choose between three display options:</p>
<ul>
<li><strong>Light</strong> — standard light theme</li>
<li><strong>Dark</strong> — full dark theme</li>
<li><strong>System</strong> — follows the operating system preference</li>
</ul>
<p><img src="/assets/upstream/images/radar/dark-mode-theme-selector.png" alt="Screenshot of the theme selector showing Light, Dark, and System options" /></p>
<p>The selected theme applies consistently across all Radar pages and widgets.</p>
<p><img src="/assets/upstream/images/radar/dark-mode-overview.png" alt="Screenshot of the Cloudflare Radar overview page in dark mode" /></p>
<p>The theme choice also applies to shared and embedded graphs.</p>
<p>Try it out at <a href="https://radar.cloudflare.com">Cloudflare Radar</a>.</p>


<h2 id="ai-insights-updates-on-cloudflare-radar"><a href="/changelog/post/2026-04-17-radar-ai-insights-updates/">AI Insights updates on Cloudflare Radar</a></h2>
<p><em>2026-04-17</em></p>
<p><a href="/radar/"><strong>Radar</strong></a> adds three new features to the <a href="https://radar.cloudflare.com/ai-insights">AI Insights</a> page, expanding visibility into how AI bots, crawlers, and agents interact with the web.</p>
<h4 id="2026-04-17-radar-ai-insights-updates-adoption-of-ai-agent-standards">Adoption of AI agent standards</h4>
<p>The AI Insights page now includes an <a href="https://radar.cloudflare.com/ai-insights#adoption-of-ai-agent-standards">adoption of AI agent standards</a> widget that tracks how websites adopt agent-facing standards. The data is filterable by domain category and updated weekly on Mondays.
This data is also available through the <a href="/api/resources/radar/subresources/agent_readiness/methods/summary/">Agent Readiness API reference</a>.</p>
<p><img src="/assets/upstream/images/radar/agent-readiness-adoption-chart.png" alt="Screenshot of the adoption of AI agent standards chart" /></p>
<p><a href="https://radar.cloudflare.com/scan">URL Scanner</a> reports now include an <strong>Agent readiness</strong> tab that evaluates a scanned URL against the criteria used by the <a href="https://isitagentready.com/">Agent Readiness score tool</a>.</p>
<p><img src="/assets/upstream/images/radar/agent-readiness-url-scanner.png" alt="Screenshot of the URL Scanner agent readiness tab" /></p>
<p>For more details, refer to the <a href="https://blog.cloudflare.com/agent-readiness/">Agent Readiness blog post</a>.</p>
<h4 id="2026-04-17-radar-ai-insights-updates-markdown-for-agents-savings">Markdown for Agents savings</h4>
<p>A new <a href="https://radar.cloudflare.com/ai-insights#markdown-for-agents-savings">savings gauge</a> shows the median response-size reduction when serving Markdown instead of HTML to AI bots and crawlers. This highlights the bandwidth and token savings that <a href="/fundamentals/reference/markdown-for-agents/">Markdown for Agents</a> provides.</p>
<div style="max-width: 300px;">
<p><img src="/assets/upstream/images/radar/markdown-for-agents-savings.png" alt="Screenshot of the Markdown for Agents savings gauge" /></p>
</div>
<p>For more details, refer to the <a href="/api/resources/radar/subresources/ai/subresources/markdown_for_agents/methods/summary">Markdown for Agents API reference</a>.</p>
<h4 id="2026-04-17-radar-ai-insights-updates-response-status">Response status</h4>
<p>The new <a href="https://radar.cloudflare.com/ai-insights#response-status">response status widget</a> displays the distribution of HTTP response status codes returned to AI bots and crawlers. Results are groupable by individual status code (200, 403, 404) or by category (2xx, 3xx, 4xx, 5xx).</p>
<p>The same widget is available on each verified bot's detail page (only available for AI bots), for example <a href="https://radar.cloudflare.com/bots/directory/google#response-status">Google</a>.</p>
<p><img src="/assets/upstream/images/radar/ai-response-status.png" alt="Screenshot of the response status distribution widget" /></p>
<p>Explore all three features on the <a href="https://radar.cloudflare.com/ai-insights">Cloudflare Radar AI Insights</a> page.</p>


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


<nav class="pagination" aria-label="Changelog pages"><span>Page 1 of 2</span><a class="pagination-next" rel="next" href="/changelog/product-group/consumer-services/2/">Next</a></nav>
