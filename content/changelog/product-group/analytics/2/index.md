---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/analytics/2/
  description: '2026-06-01'
  full_title: Analytics changelog - page 2 | Cloudflare Docs
  head_html: <title>Analytics changelog - page 2 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-06-01"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/analytics/2/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Analytics changelog - page 2"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-06-01"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/analytics/2/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/analytics/2/#page","headline":"Analytics changelog - page 2 | Cloudflare Docs","description":"2026-06-01","url":"https://developers.cloudflare.com/changelog/product-group/analytics/2/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/analytics/2/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="new-turnstile-events-logpush-dataset-in-cloudflare-logs"><a href="/changelog/post/2026-06-01-log-fields-updated/">New Turnstile Events Logpush dataset in Cloudflare Logs</a></h2>
<p><em>2026-06-01</em></p>
<p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-06-01-log-fields-updated-new-datasets">New datasets</h4>
<ul>
<li><strong>Turnstile Events</strong>: A new dataset with fields including <code>ASN</code>, <code>Action</code>, <code>BrowserMajor</code>, <code>BrowserName</code>, <code>ClientIP</code>, <code>CountryCode</code>, <code>EventType</code>, <code>Hostname</code>, <code>OSMajor</code>, <code>OSName</code>, <code>Sitekey</code>, <code>Timestamp</code>, and <code>UserAgent</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>


<h2 id="updated-fields-across-multiple-logpush-datasets-in-cloudflare-logs"><a href="/changelog/post/2026-05-29-log-fields-updated/">Updated fields across multiple Logpush datasets in Cloudflare Logs</a></h2>
<p><em>2026-05-29</em></p>
<p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-05-29-log-fields-updated-updated-fields-in-existing-datasets">Updated fields in existing datasets</h4>
<ul>
<li><strong>DEX Device State Events</strong> (added): <code>DeviceRegistrationProfileID</code>.</li>
<li><strong>Gateway HTTP</strong> (added): <code>AddedHeaders</code>, <code>DeletedHeaders</code>, and <code>SetHeaders</code>.</li>
<li><strong>HTTP requests</strong> (added): <code>MatchedRules</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>


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


<h2 id="security-scans-more-frequent"><a href="/changelog/post/2026-05-29-security-insights-default-scans/">Security scans more frequent</a></h2>
<p><em>2026-05-29</em></p>
<p>Security Insights scans now run more often. Cloudflare scans Free accounts <strong>every 7 days</strong>, Pro and Business accounts <strong>every 3 days</strong>, and Enterprise accounts <strong>daily</strong>.</p>
<p>In addition, all accounts and zones now receive scans by default. You no longer need to enable scans before Cloudflare checks your account for misconfigurations, vulnerabilities, and other security risks.</p>
<p>Granular on-demand scans are now available on any plan. You can trigger an on-demand scan for any zone, insight, insight type from the Cloudflare dashboard in order to quickly re-check your security posture after remediating an issue.</p>
<p>To learn more, refer to the <a href="/security/security-insights/">Security Insights documentation</a>.</p>


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


<h2 id="new-logpush-datasets-and-updated-fields-across-multiple-logpush-datasets-in-cloudflare-logs"><a href="/changelog/post/2026-05-13-log-fields-updated/">New Logpush datasets and updated fields across multiple Logpush datasets in Cloudflare Logs</a></h2>
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


<h2 id="cdn-cgi-rum-endpoint-now-returns-405-for-non-post-requests"><a href="/changelog/post/2026-05-13-rum-405-method-not-allowed/">/cdn-cgi/rum endpoint now returns 405 for non-POST requests</a></h2>
<p><em>2026-05-13</em></p>
<p>The <code>/cdn-cgi/rum</code> beacon endpoint now returns <code>405 Method Not Allowed</code> for non-POST requests instead of <code>404 Not Found</code>. The response includes an <code>Allow: POST, OPTIONS</code> header per <a href="https://www.rfc-editor.org/rfc/rfc9110#section-15.5.6">RFC 9110 §15.5.6</a>.</p>
<p>Previously, sending a <code>GET</code> or other non-POST request to this endpoint returned a <code>404</code>, which was misleading because it suggested the endpoint did not exist. The new <code>405</code> response clearly indicates that the endpoint exists but only accepts <code>POST</code> requests.</p>
<p>The Web Analytics beacon (<code>beacon.min.js</code>) already uses <code>POST</code> for all metric submissions, so this change does not affect normal beacon operation. <code>OPTIONS</code> requests for CORS preflight continue to work as before.</p>
<p>For more information, refer to the <a href="/web-analytics/faq/#why-am-i-getting-a-405-method-not-allowed-error-from-cdn-cgirum">Web Analytics FAQ</a>.</p>


<h2 id="agent-readiness-scores-now-available-in-url-scanner-via-the-cloudflare-dashboard"><a href="/changelog/post/2026-05-12-URL-scanner-report-agent-readiness/">Agent Readiness scores now available in URL Scanner via the Cloudflare Dashboard</a></h2>
<p><em>2026-05-12</em></p>
<p>We’ve added a new <strong>Agent Readiness</strong> tab to URL Scanner reports accessible via the Cloudflare dashboard. This feature evaluates your site against emerging AI standards and provides six specialized scores to help you optimize for the next generation of AI agents and automated discovery.</p>
<p>The Internet is shifting from a human-read web to a machine-read web. AI agents now browse, interact with, and even perform transactions on websites. If a site isn't &quot;agent-ready,&quot; these bots may consume excessive bandwidth, fail to find critical information, or be unable to navigate your services efficiently.</p>
<p>This update provides material value by breaking down readiness into six actionable categories:</p>
<ul>
<li><strong>Basic Web Presence</strong></li>
<li><strong>Discoverability</strong></li>
<li><strong>Content Accessibility</strong></li>
<li><strong>Bot Access Control</strong></li>
<li><strong>Protocol Discovery</strong></li>
<li><strong>Commerce</strong></li>
</ul>
<h4 id="2026-05-12-URL-scanner-report-agent-readiness-accessing-the-report">Accessing the report</h4>
<p>You can view these scores for any scanned URL directly in the dashboard or via our API.</p>
<ul>
<li><strong>Dashboard:</strong> Go to <strong>Protect &amp; Connect &gt; Application Security &gt; Investigate</strong>. After running a scan, select the <strong>Agent Readiness</strong> tab in the report.</li>
<li><strong>API:</strong> Use the <a href="https://developers.cloudflare.com/radar/investigate/url-scanner/">URL Scanner API</a> to programmatically retrieve these scores for your infrastructure.</li>
</ul>
<p>To learn more about the methodology behind these scores, refer to the <a href="https://blog.cloudflare.com/agent-readiness/">blogpost</a>.</p>


<h2 id="csv-export-and-adjustable-page-density-for-rfis"><a href="/changelog/post/2026-05-07-CSV-export-for-RFIs/">CSV export and adjustable page density for RFIs</a></h2>
<p><em>2026-05-07</em></p>
<p>You can now export your Requests for Information (RFI) history to a <strong>CSV document</strong> and customize your dashboard view by choosing how many RFI records to load per page.</p>
<h4 id="2026-05-07-CSV-export-for-RFIs-why-this-matters">Why this matters</h4>
These quality-of-life updates focus on data portability and dashboard performance, allowing power users to manage high volumes of requests more efficiently:
<ul>
<li>The new <strong>CSV export</strong> allows you to move RFI data into external tools for custom reporting, internal auditing, or cross-referencing with other security projects without manual data entry</li>
<li>With <strong>adjustable page density</strong>, you can now choose to load more records at once (10, 25 or 50) to scan through history faster</li>
</ul>
<p>Cloudforce One subscribers can find these new options in <a href="https://dash.cloudflare.com/?to=/:account/application-security/threat-intelligence/requests">Cloudflare Dashboard &gt; Application Security &gt; Threat Intelligence &gt; Requests for Information</a>.</p>


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


<h2 id="taxii-support-added-to-threat-events-api"><a href="/changelog/post/2026-05-06-TAXII-support-for-threat-events-api/">TAXII support added to Threat Events API</a></h2>
<p><em>2026-05-06</em></p>
<p>The Cloudforce One Threat Events API now supports <a href="https://www.cloudflare.com/en-gb/learning/security/what-is-stix-and-taxii/"><strong>TAXII</strong></a> as an output format, enabling standardized, automated sharing of cyber threat intelligence with your existing security stack.</p>
<h4 id="2026-05-06-TAXII-support-for-threat-events-api-why-this-matters">Why this matters</h4>
<ul>
<li>You can now ingest Cloudforce One threat data directly into your SIEM, TIP or SOAR tools that prefer TAXII-formatted streams without needing custom translation scripts.</li>
<li>By supporting the TAXII format parameter in our API, security teams can automate the synchronization of indicator data, reducing the manual overhead of updating blocklists and detection rules.</li>
<li>This alignment with industry standards ensures that your threat data remains consistent across different security ecosystems and partner integrations.</li>
</ul>
<h4 id="2026-05-06-TAXII-support-for-threat-events-api-how-to-use-it">How to use it</h4>
<p>When calling the Threat Events API, you can now specify <code>taxii</code> in the <code>format</code> query parameter:</p>
<p><code>GET /accounts/{account_id}/cloudforce_one/threat_events?format=taxii</code></p>
<p>You can find the updated documentation in the <a href="https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/methods/list#%28resource%29%20cloudforce_one.threat_events%20%3E%20%28method%29%20list%20%3E%20%28params%29%20default%20%3E%20%28param%29%20format%20%3E%20%28schema%29">Cloudflare API Reference</a>.</p>


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


<h2 id="web-analytics-adds-navigation-type-filtering-and-reporting"><a href="/changelog/post/2026-04-30-rum-navigation-types/">Web Analytics adds Navigation Type filtering and reporting</a></h2>
<p><em>2026-04-30</em></p>
<p>Cloudflare Web Analytics now supports <strong>Navigation Type</strong> reporting and filtering.</p>
<p>This update allows developers and performance analysts to see how users are navigating between pages — whether through a link click or form submission, a page reload, or using the browser's back/forward buttons — and whether a browser cache hit occurred for these behaviors.</p>
<p>Understanding navigation types is critical for optimizing user experience. For example, if a high volume of your traffic consists of &quot;Back-forward&quot; navigations versus &quot;Back-forward Cache&quot;, those visitors are not benefiting from the Back/Forward Cache (bfcache) and therefore are experiencing higher load times due to potentially unnecessary network requests.</p>
<p>The same applies for regular &quot;Navigate&quot; entries — where &quot;Navigate Cache&quot;, &quot;Navigate Prefetch Cache&quot; and &quot;Prerender&quot; would provide instant document retrieval — and &quot;Reload&quot;, where &quot;Reload cache&quot; would be more optimal.</p>
<p>A high volume of &quot;Reload&quot; entries can also indicate a potential stability problem with your website.</p>
<p>By identifying these patterns, you can tune your browser caching strategies to ensure HTML documents are served instantaneously from local caches rather than requiring a roundtrip to the network.</p>
<p>For more information, refer to <a href="/web-analytics/data-metrics/dimensions/#navigation-types">Navigation Types</a>.</p>
<h4 id="2026-04-30-rum-navigation-types-key-benefits">Key benefits</h4>
<ul>
<li><strong>Monitor Cache Effectiveness:</strong> See how often your site is served from the HTTP cache or bfcache.</li>
<li><strong>Identify Performance Bottlenecks:</strong> Filter by the different types to understand performance opportunity of improving browser cache hit ratio.</li>
</ul>
<h4 id="2026-04-30-rum-navigation-types-analyze-navigation-types-in-the-cloudflare-dashboard">Analyze navigation types in the Cloudflare dashboard</h4>
<p>You can now find the <strong>Navigation Type</strong> dimension in the Web Analytics dashboard. You can filter to include/exclude one or more specific types using &quot;equals&quot;, &quot;does not equal&quot;, &quot;in&quot;, or &quot;not in&quot; matchers.</p>
<p><img src="/assets/upstream/images/web-analytics/dash-web_analytics-navigation-type-filter.png" alt="Navigation Type filter" /></p>
<p>To check the list of popular navigation types, select <strong>Page views</strong> on the Web Analytics sidebar and scroll down to the bottom:</p>
<p><img src="/assets/upstream/images/web-analytics/dash-web_analytics-navigation-types-list.png" alt="Navigation Types list in Page Views tab" /></p>


<h2 id="digital-experience-tests-to-authenticated-resources-and-enhanced-configuration"><a href="/changelog/post/2026-04-29-dex-tests-to-auth/">Digital experience tests to authenticated resources and enhanced configuration</a></h2>
<p><em>2026-04-29</em></p>
<p><a href="/cloudflare-one/insights/dex/tests/">Digital experience tests</a> now support testing applications protected by Cloudflare Access or third-party authentication. All authentication secrets are managed via <a href="/secrets-store/">Cloudflare Secret Store</a>.</p>
<p>Digital experience tests also have enhanced configuration options including:</p>
<ul>
<li>New HTTP methods (DELETE, PATCH, POST, PUT)</li>
<li>Secret Store headers, custom plain text headers, and custom request bodies</li>
<li>Advanced settings: follow redirects, response bodies, response headers, and allow untrusted certificates</li>
</ul>
<p><img src="/assets/upstream/images/changelog/dex/dex_test_auth_config.png" alt="Digital experience test configuration for Cloudflare Access applications" />
<img src="/assets/upstream/images/changelog/dex/dex_test_enhanced_config.png" alt="Digital experience enhanced test configuration" /></p>


<h2 id="internet-outage-notifications-for-devices"><a href="/changelog/post/2026-04-28-dex-internet-outage-notification/">Internet outage notifications for devices</a></h2>
<p><em>2026-04-28</em></p>
<p><a href="/cloudflare-one/insights/dex/">Digital Experience</a> will display a dashboard notification when an Internet outage or traffic anomaly may impact a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> device based on its geographic location or network connection.</p>
<p>This Internet outage and traffic anomaly data is pulled from <a href="https://radar.cloudflare.com/">Cloudflare Radar</a>. All Internet outage and traffic anomaly observations can be viewed in the <a href="https://radar.cloudflare.com/outage-center">Radar Outage Center</a>.</p>
<p><img src="/assets/upstream/images/changelog/dex/dex_radar_ux_notification.png" alt="Digital Experience Monitoring dashboard notification for Internet outage impacting Cloudflare One Client devices" />
<img src="/assets/upstream/images/changelog/dex/dex_radar_analytics.png" alt="Digital Experience Monitoring dashboard analytics for Internet outage impacting Cloudflare One Client devices" /></p>


<h2 id="cloudflare-one-client-speed-tests"><a href="/changelog/post/2026-04-28-dex-speed-test/">Cloudflare One Client speed tests</a></h2>
<p><em>2026-04-28</em></p>
<p>IT teams can now remotely run speed tests from the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> to Cloudflare's network edge.</p>
<p>Each speed test includes the following metrics:</p>
<ul>
<li>Internet speed: download and upload throughput</li>
<li>Latency: download, upload, unloaded latency, and jitter</li>
<li>Network quality score: video streaming, webchat/real-time communication (RTC)</li>
</ul>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Digital experience</strong> &gt; <strong>Diagnostics</strong> and select <strong>Run diagnostics</strong> to use the feature today.</p>
<p><img src="/assets/upstream/images/changelog/dex/dex_speed_test.png" alt="Cloudflare One client speed test result" /></p>


<h2 id="unified-workspace-for-brand-protection"><a href="/changelog/post/2026-04-27-unified-workspace-brand-protection/">Unified workspace for Brand Protection</a></h2>
<p><em>2026-04-27</em></p>
<p>We have introduced a unified investigation workspace within Brand Protection to help analysts manage complex brand portfolios. Instead of jumping between individual queries, you can now consolidate your workflow into a single, cohesive view.</p>
<h4 id="2026-04-27-unified-workspace-brand-protection-what-s-new">What's new</h4>
<ul>
<li>You can now elect multiple saved queries from your dashboard to generate a consolidated &quot;Combined Matches&quot; view. This allows you to triage results from different brand queries in one unified table</li>
<li>You can open query extended views in distinct tabs within the Brand Protection dashboard. This enables you to maintain multiple investigation contexts simultaneously and switch between them without losing your place.</li>
<li>You can reset your workspace using the new &quot;Clear Selection&quot; action, making it easier to pivot between different investigation sets.</li>
</ul>
<h4 id="2026-04-27-unified-workspace-brand-protection-key-benefits">Key benefits</h4>
<ul>
<li>Eliminate fragmented workflows by viewing all matches across different query buckets in a single table, reducing the need to click through dozens of individual query pages</li>
<li>Correlate related campaigns by seeing similar domains or infrastructure patterns that appear across multiple saved queries</li>
</ul>
<p>Learn more in our <a href="/security-center/brand-protection/">Brand Protection documentation</a>.</p>


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
<pre tabindex="0"><code class="language-sql">INSERT INTO http_logs_sink&#10;SELECT&#10;  ClientIP,&#10;  EdgeResponseStatus,&#10;  to_timestamp_micros(EdgeStartTimestamp) AS event_time,&#10;  upper(ClientRequestMethod) AS method,&#10;  sha256(ClientIP) AS hashed_ip&#10;FROM http_logs_stream&#10;WHERE EdgeResponseStatus &gt;= 400;&#10;</code></pre>
<p>Pipelines SQL supports string functions, regex, hashing, JSON extraction, timestamp conversion, conditional expressions, and more. For the full list, refer to the <a href="/pipelines/sql-reference/">Pipelines SQL reference</a>.</p>
<h4 id="2026-04-20-pipelines-logpush-destination-get-started">Get started</h4>
<p>To configure Pipelines as a Logpush destination, refer to <a href="/logs/logpush/logpush-job/enable-destinations/pipelines/">Enable Cloudflare Pipelines</a>.</p>


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


<h2 id="last-seen-timestamp-for-cloudflare-one-client-devices-is-more-consistent"><a href="/changelog/post/2026-04-15-dex-consistent-last-seen-timestamps/">Last seen timestamp for Cloudflare One Client devices is more consistent</a></h2>
<p><em>2026-04-15</em></p>
<p>The last seen timestamp for <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> devices is now more consistent across the dashboard. IT teams will see more consistent information about the most recent client event between a device and Cloudflare's network.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/analytics/">Previous</a><span>Page 2 of 6</span><a class="pagination-next" rel="next" href="/changelog/product-group/analytics/3/">Next</a></nav>
