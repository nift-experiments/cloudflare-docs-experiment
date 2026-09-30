---
cp9:
  canonical: https://developers.cloudflare.com/reference-architecture/diagrams/content-delivery/distributed-web-performance-architecture/
  description: A prescriptive pattern for building a Cloudflare-based L7 performance architecture that reduces latency, raises cache efficiency, and improves Core Web Vitals.
  full_title: Designing a distributed web performance architecture · Cloudflare Reference Architecture docs
  head_html: <title>Designing a distributed web performance architecture · Cloudflare Reference Architecture docs</title><meta name="generator" content="Nift"><meta name="description" content="A prescriptive pattern for building a Cloudflare-based L7 performance architecture that reduces latency, raises cache efficiency, and improves Core Web Vitals."><link rel="canonical" href="https://developers.cloudflare.com/reference-architecture/diagrams/content-delivery/distributed-web-performance-architecture/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/reference-architecture/diagrams/content-delivery/distributed-web-performance-architecture/index.md"><meta property="og:title" content="Designing a distributed web performance architecture · Cloudflare Reference Architecture docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="A prescriptive pattern for building a Cloudflare-based L7 performance architecture that reduces latency, raises cache efficiency, and improves Core Web Vitals."><meta property="og:url" content="https://developers.cloudflare.com/reference-architecture/diagrams/content-delivery/distributed-web-performance-architecture/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Reference Architecture"><meta name="algolia_product_filter" content="Reference Architecture"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference architecture diagram"><meta name="algolia_content_type" content="Reference architecture diagram"><meta name="pcx_additional_products" content="Argo Smart Routing,Cache / CDN,DNS,Cloudflare Images,Load Balancing,R2,Smart Shield,Speed,Waiting Room,Zaraz"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/reference-architecture/diagrams/content-delivery/distributed-web-performance-architecture/#page","headline":"Designing a distributed web performance architecture \u00b7 Cloudflare Reference Architecture docs","description":"A prescriptive pattern for building a Cloudflare-based L7 performance architecture that reduces latency, raises cache efficiency, and improves Core Web Vitals.","url":"https://developers.cloudflare.com/reference-architecture/diagrams/content-delivery/distributed-web-performance-architecture/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /reference-architecture/diagrams/content-delivery/distributed-web-performance-architecture/
  schema: 1
---
<h2 id="introduction">Introduction</h2>
<p>This guide describes a comprehensive layer 7 (L7) Application Performance strategy for architects and developers. In today's competitive digital landscape, <strong>application performance is a critical business differentiator</strong>. However, the ultimate objective is finding the performance-security equilibrium point.</p>
<p>While this guide focuses on maximizing speed and user experience (UX), performance cannot come at the expense of security. Architects must balance latency reduction against the necessary processing overhead of rigorous security controls, such as DDoS protection, WAF and Bot Management.</p>
<p>In high-risk scenarios, security must take precedence, where the &quot;latency budget&quot; gained from these performance optimizations is strategically reinvested to power essential protections, ensuring the application remains both fast enough to convert users and secure enough to protect the business.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12729.md")
</aside>
<table>
<thead>
<tr>
<th align="left">Key business metrics</th>
<th align="left">Why it matters</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><strong>User Engagement &amp; Retention</strong></td>
<td align="left"><strong>First Impressions &amp; Abandonment:</strong> A fast-loading website is fundamental to a positive user experience. Users today expect instant access to information, and research highlights this, showing that a significant portion of users will abandon a website if it <a href="https://support.google.com/adsense/answer/7450973?hl=en">takes too long to load</a>, directly increasing the bounce rate.</td>
</tr>
<tr>
<td align="left"><strong>Revenue Generation &amp; Conversion</strong></td>
<td align="left"><strong>Direct Business Impact:</strong> Web performance directly impacts a website's conversion rate, which is the percentage of visitors who complete a desired action, such as making a purchase or signing up for a newsletter. A faster site leads to higher conversion rates; for example, one <a href="https://www.cloudflare.com/en-gb/learning/performance/more/website-performance-conversion-rates/">study</a> found that even a 100-millisecond reduction in homepage load time resulted in a 1.11% increase in conversions.</td>
</tr>
<tr>
<td align="left"><strong>Organic Visibility &amp; Search Ranking</strong></td>
<td align="left"><strong>Traffic Acquisition &amp; Authority:</strong> Search Engine Optimization (SEO) is how search engines like Google use page speed as a ranking factor. Faster-loading websites tend to rank higher in search results, which leads to more organic traffic. Google's <strong>Core Web Vitals (CWVs)</strong> are a set of metrics that measure a page's loading speed, interactivity, and visual stability, all of which are directly tied to performance and can significantly boost a site's search engine ranking.</td>
</tr>
<tr>
<td align="left"><strong>High-Speed Delivery &amp; Reliability</strong></td>
<td align="left"><strong>User Experience &amp; Trust:</strong> This metric combines a high <strong>Download Success Rate</strong> (Availability/Resiliency) with maximum <strong>Download Throughput</strong> (Speed). For mission-critical assets like software, video, or AI models, it ensures users get the file fast and reliably, directly impacting product usability and customer trust, especially during traffic spikes.</td>
</tr>
<tr>
<td align="left"><strong>Edge Efficiency &amp; Cost Control</strong></td>
<td align="left"><strong>Operational Cost Reduction:</strong> This metric is primarily measured by the <strong>Cache Hit Ratio (CHR)</strong> for large files. Maximizing the CHR offloads traffic from the origin server, which is the key driver for minimizing infrastructure load and achieving significant <strong>Data Egress Cost Reduction</strong> (for example, through the <a href="https://www.cloudflare.com/bandwidth-alliance/">Bandwidth Alliance</a>), directly translating to lower operational costs and greater profitability for the business.</td>
</tr>
</tbody>
</table>
<p>Measuring the Impact: While marketing dashboards (for example, <a href="/fundamentals/reference/google-analytics/">Google Analytics</a>) track business outcomes, Cloudflare <a href="/web-analytics/">Web Analytics</a> and <a href="/speed/observatory/">Observatory</a> measure the performance drivers. Use them to correlate real-time Core Web Vitals (CWV) and Real User Monitoring (RUM) improvements directly with reduced bounce rates and higher conversions, without compromising privacy or relying on heavy client-side scripts.</p>
<p>By following this architecture, organizations can expect:</p>
<ul>
<li><strong>Improving Core Web Vitals (CWV)</strong> like LCP and INP, which can help reduce bounce rates and drive sales.</li>
<li>Maximizing Cache Hit Ratio, which offloads traffic from the origin, reducing infrastructure spend, and overall <strong>lowering operational costs</strong>.</li>
<li>Ensuring high uptime/availability and <strong>business resiliency</strong> even during traffic spikes.</li>
</ul>
<h2 id="performance-goals-and-metrics">Performance goals and metrics</h2>
<p><a href="https://blog.cloudflare.com/loving-performance-measurements/">Measuring performance is tricky</a>, and it serves a broader business context where Security and <a href="https://www.cloudflare.com/trust-hub/">Compliance</a> are often non-negotiable prerequisites. Organizations frequently validate that their architecture meets regulatory standards (such as <a href="https://www.cloudflare.com/learning/privacy/what-is-data-localization/">data residency</a> or <a href="/ssl/reference/protocols/">encryption protocols</a>, including <a href="/ssl/post-quantum-cryptography/">Post-Quantum Cryptography (PQC)</a>) before unlocking performance capabilities.</p>
<p>Once these security and compliance baselines are secured, effective optimization starts with measuring the “right” things - which interestingly is slightly different for everyone. Nonetheless, most people would agree to focus on user-centric metrics for website performance, using <a href="https://blog.cloudflare.com/ttfb-is-not-what-it-used-to-be/">TTFB as a diagnostic tool</a> for server responsiveness, but prioritizing <a href="https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/">Core Web Vitals (CWV)</a> for measuring user experience.</p>
<p>Successful implementation is measured by these metrics:</p>
<table>
<thead>
<tr>
<th align="left">Metric</th>
<th align="left">Target (75th percentile)</th>
<th align="left">What it measures</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><strong>Largest Contentful Paint (LCP)</strong></td>
<td align="left">&lt; 2.5 s</td>
<td align="left">Loading performance (hero image/text visibility).</td>
</tr>
<tr>
<td align="left"><strong>Interaction to Next Paint (INP)</strong></td>
<td align="left">&lt; 200 ms</td>
<td align="left">Interactivity and responsiveness to inputs.</td>
</tr>
<tr>
<td align="left"><strong>Cumulative Layout Shift (CLS)</strong></td>
<td align="left">&lt; 0.1</td>
<td align="left">Visual stability (unexpected layout shifts).</td>
</tr>
<tr>
<td align="left"><strong>Time to First Byte (TTFB)</strong></td>
<td align="left">&lt; 800 ms</td>
<td align="left">Server responsiveness (network + processing time). Gain deep visibility into connection performance by leveraging fields like <a href="/ruleset-engine/rules-language/fields/reference/cf.timings.origin_ttfb_msec/"><em>cf.timings.origin_ttfb_msec</em></a> to isolate origin latency from network overhead.</td>
</tr>
</tbody>
</table>
<p>The 75th percentile target is <a href="https://web.dev/articles/defining-core-web-vitals-thresholds">based on previous analysis</a> for reasonable balance.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12728.md")
</aside>
<h2 id="data-flow">Data flow</h2>
<p>This diagram illustrates the request lifecycle, highlighting how Cloudflare's layers/<a href="/ruleset-engine/reference/phases-list/">phases</a> - Network, Optimization, Caching, and Origin connectivity - work together to minimize latency.</p>
<p><img src="/assets/upstream/images/reference-architecture/distributed-web-performance-architecture/data-flow-overview.jpg" alt="Figure 1: Data flow overview showing the request lifecycle across User, Cloudflare Edge, Tiered Edge, and Origin layers." title="Figure 1: Data flow overview" /></p>
<p>For demonstration purposes, the architecture is organized into four logical layers and follows specific <a href="/ruleset-engine/reference/phases-list/">phases</a>. Optimizing every step in this chain is required to achieve the best aggregate performance.</p>
<h3 id="1-user-eyeball-client"><ol>
<li>User (eyeball client)</li>
</ol></h3>
<p>The performance journey begins at the client's device. Device hardware, <a href="https://caniuse.com/">browser</a>, network quality and topology determine initial responsiveness. The goal here is to establish the fastest possible connection to the Cloudflare network.</p>
<ul>
<li><strong>DNS Resolution:</strong> The client device queries the domain, going through both a public DNS resolver and, ultimately, to an authoritative DNS server. Cloudflare's <a href="https://www.cloudflare.com/network/">global anycast network</a> routes requests to the nearest Point of Presence (PoP), with <a href="https://www.dnsperf.com/">global DNS</a> resolution ensuring minimal lookup latency, including the possibility to expand to <a href="/china-network/">mainland China</a>.</li>
<li><strong>Connection Establishment:</strong> The client establishes a connection via IPv4/<a href="/network/ipv6-compatibility/">IPv6</a> using <a href="/speed/optimization/protocol/http3/">HTTP/3 (QUIC)</a> and <a href="/ssl/edge-certificates/additional-options/tls-13/">TLS 1.3</a> - this also allows for <a href="/ssl/post-quantum-cryptography/">Post-Quantum Cryptography (PQC)</a>. If the client has visited before, <a href="/speed/optimization/protocol/0-rtt-connection-resumption/">0-RTT Connection Resumption</a> eliminates round-trips during the handshake. Additionally, <a href="/ssl/edge-certificates/additional-options/http-strict-transport-security/">HTTP Strict Transport Security (HSTS)</a> enforces browser-side redirects to HTTPS, removing unnecessary server round-trips. It is generally recommended to <a href="/ssl/edge-certificates/encrypt-visitor-traffic/">enforce HTTPS connections</a>. Furthermore, by leveraging relevant <a href="/changelog/2025-10-30-tcp-rtt-and-tcp-fields/">TCP fields</a>, you can implement adaptive performance strategies.</li>
<li><strong>Browser Optimization:</strong> Features like <a href="/speed/optimization/content/speed-brain/">Speed Brain</a> (Speculation Rules API) proactively prefetch resources, while <a href="/cache/advanced-configuration/early-hints/">Early Hints</a> send link headers to the browser during &quot;server think time&quot;, speeding up page rendering.</li>
<li><strong>Third-Party Offloading:</strong> <a href="/zaraz/">Zaraz</a> offloads third-party tools (like Google Analytics 4 or Mixpanel) to the cloud. This reduces main thread blocking on the device, significantly improving INP.</li>
<li><strong>Web Analytics (RUM):</strong> Leverage Cloudflare <a href="/web-analytics/">Web Analytics</a> to collect privacy-first, cookie-less performance data directly from the user's browser. This lightweight JavaScript beacon provides real-world insights into Core Web Vitals (LCP, INP, CLS) without tracking users or storing client-side state.</li>
</ul>
<p><img src="/assets/upstream/images/smart-shield/network-diagram.png" alt="Figure 2: Smart Shield Advanced network diagram showing Argo Smart Routing, Tiered Cache, Cache Reserve, Connection Reuse, Dedicated Egress IPs, and Load Balancing across multiple Points of Presence." title="Figure 2: Smart Shield Advanced network diagram" /></p>
<h3 id="2-network-and-optimization-cloudflare-edge"><ol start="2">
<li>Network and optimization (Cloudflare edge)</li>
</ol></h3>
<p>Once the request reaches the network edge, Cloudflare processes and optimizes the content before it is served or fetched from the cache.</p>
<ul>
<li><strong>Traffic Management:</strong> The request is inspected. <a href="/rules/normalization/">URL Normalization</a> ensures consistency, while <a href="/rules/url-forwarding/">Redirect Rules</a> or <a href="/rules/transform/">Transform Rules</a> handle path modifications efficiently. <a href="/waiting-room/">Waiting Room</a> protects the backend during <a href="/learning-paths/surge-readiness/concepts/">massive traffic surges</a>, maintaining availability.</li>
<li><strong>Programmatic Customization:</strong> For advanced use cases where standard rules are insufficient, <a href="/rules/snippets/when-to-use/">Snippets and Workers</a> allow for programmatic customization. This enables executing custom code logic to modify headers, rewrite URLs, <a href="/images/optimization/transformations/transform-via-workers/">image optimizations</a>, or implement unique caching logic directly at the edge. Utilize <a href="/workers/runtime-apis/bindings/service-bindings/">Service Bindings</a> to facilitate low-latency, zero-overhead communication between these Workers.</li>
<li><strong>Content Optimization:</strong> Text assets are compressed using <a href="/rules/compression-rules/">Compression Rules</a> (Brotli/Gzip). Images are processed on-the-fly via <a href="/images/optimization/transformations/overview/">Image Transformations</a> or <a href="/images/polish/">Polish</a> to ensure they are served in the optimal format (AVIF/WebP) and size for the device, significantly improving LCP and CLS.</li>
<li><strong>Font &amp; Tag Optimization:</strong> <a href="/speed/optimization/content/fonts/">Cloudflare Fonts</a> eliminates DNS lookups and TLS connections to Google Fonts by serving them inline from the domain. <a href="/google-tag-gateway/">Google Tag Gateway</a> improves ad signal measurement and privacy.</li>
<li><strong>Routing, Availability &amp; Protocol Intelligence:</strong> Cloudflare operates one of the most <a href="https://blog.cloudflare.com/network-performance-update-birthday-week-2025/">interconnected networks</a> in the world, peering with over 13,000 networks, operating a <a href="https://blog.cloudflare.com/backbone2024/">global backbone</a>, and participating in a leading number of <a href="https://bgp.he.net/report/exchanges#_participants">Internet Exchange Points (IXPs)</a> globally. We leverage the <a href="https://blog.cloudflare.com/how-cloudflare-uses-the-worlds-greatest-collection-of-performance-data/">unique intelligence</a> derived from this massive dataset to dynamically optimize Congestion Control (CC) at the protocol level - automatically selecting the optimal algorithm and tuning adequate parameters for every connection based on real-time network conditions. For dynamic requests that cannot be cached, <a href="/argo-smart-routing/">Argo Smart Routing</a> finds the fastest path through the network to the origin. <a href="/rules/custom-errors/">Custom Errors</a> provide a consistent brand experience during failures.</li>
</ul>
<p><img src="/assets/upstream/images/reference-architecture/distributed-web-performance-architecture/data-flow-network-content-optimization.jpg" alt="Figure 3: Data flow for network and content optimization showing Traffic Handling, Programmatic Customization, Content Optimization, and Font and Tag Optimization." title="Figure 3: Data flow - network and content optimization" /></p>
<h3 id="3-tiered-cache-and-storage-cloudflare-edge"><ol start="3">
<li>Tiered Cache and Storage (Cloudflare edge)</li>
</ol></h3>
<p>Cloudflare can be organized into a specific topology. This layer handles content retention and retrieval. It acts as a shield for the origin and a high-speed store for the client.</p>
<ul>
<li><strong>Cache Logic:</strong> <a href="/cache/concepts/cache-control/">Origin Cache Control Headers</a>, <a href="/cache/how-to/cache-rules/">Cache Rules</a> and <a href="/cache/how-to/set-caching-levels/">Caching Levels</a> allow precise control over TTL and query string handling. Implement Cache Normalization strategies to consolidate requests with variable URLs - such as those with distinct marketing or SEO parameters - into a single <a href="/cache/how-to/cache-keys/">Cache Key</a>, significantly improving cache hit ratios. <a href="/speed/optimization/content/prefetch-urls/">Prefetch URLs</a> can pre-populate the cache with critical assets via manifest files to further reduce latency. Note the <a href="/cache/concepts/default-cache-behavior/#default-cached-file-extensions">default caching behavior and limits</a>.</li>
<li><strong>Tiered Caching:</strong> If the content is not on the local PoP, Cloudflare checks an upper-tier cache topology. <a href="/cache/how-to/tiered-cache/">Smart Tiered Caching</a> and <a href="/cache/how-to/tiered-cache/#regional-tiered-cache">Regional Tiered Cache</a> centralize connections, increasing cache hit ratios and reducing global origin load. For a more customized approach, Enterprise customers can opt for a <a href="/cache/how-to/tiered-cache/#custom-tiered-cache">Custom Tiered Cache</a> topology.</li>
<li><strong>Dedicated long-term Cache:</strong> <a href="/cache/advanced-configuration/cache-reserve/">Cache Reserve</a> extends the life of large, infrequently accessed assets (for example, images, archived video, software updates, or static AI models) by moving infrequently accessed content to persistent object storage backend (powered by R2). This prevents eviction due to <a href="/cache/concepts/retention-vs-freshness/">Least Recently Used (LRU)</a> algorithms and avoids latency-inducing origin fetches, while simultaneously supporting storage redundancy and resilience requirements.</li>
<li><strong>Instant Purge:</strong> Leverage Cloudflare's <a href="https://blog.cloudflare.com/instant-purge-for-all/">decentralized purging architecture</a> to invalidate content globally in approximately 150ms. This <a href="/cache/how-to/purge-cache/">Instant Purge</a> capability supports various granular approaches - including Purge by URL, Tag, Prefix, or Hostname - ensuring users receive fresh content immediately without waiting for TTL expiration.</li>
<li><strong>Cloud Connectivity:</strong> <a href="/rules/cloud-connector/">Cloud Connector Rules</a> simplify routing traffic to public cloud providers (AWS, Azure, GCP) for specific object storage or origin requirements. For private infrastructure, <a href="/workers-vpc/">Workers VPC</a> enables direct connectivity to private storage endpoints or databases on public clouds (for example, AWS, Azure) without exposing them to the public Internet.</li>
<li><strong>Static Asset Hosting:</strong> Entire parts of an application (frontend assets, images, including large media files, software packages) can be stored directly in <a href="/r2/">R2 Object Storage</a> or <a href="/workers/static-assets/">Workers Static Assets</a>, serving them from the edge without ever hitting a traditional origin server. Additional <a href="/workers/platform/storage-options/">storage options</a> are available.</li>
</ul>
<p><img src="/assets/upstream/images/reference-architecture/distributed-web-performance-architecture/data-flow-caching.jpg" alt="Figure 4: Data flow for caching showing Local Edge, Tiered Cache, and Long-Term Cache or Storage layers with cache miss and fill paths." title="Figure 4: Data flow - caching" /></p>
<h3 id="4-origin-server"><ol start="4">
<li>Origin server</li>
</ol></h3>
<p>For requests that must traverse the full path (that is, dynamic content or cache misses), the origin configuration determines the final latency impact. Architects have two primary paths here: adopting the performant, resilient serverless model (also known as originless), or optimizing connectivity and security for a traditional Origin Server.</p>
<p><strong>Serverless:</strong> Cloudflare's <a href="/learning-paths/workers/devplat/intro-to-devplat/">Developer Platform</a> achieves the optimal performance tier by enabling an &quot;originless&quot; model. <a href="/reference-architecture/diagrams/serverless/fullstack-application/">Fullstack applications</a> are built and deployed directly on the global edge network worldwide, eliminating the full path traversal to a distant origin. Dynamic requests execute at the nearest Cloudflare PoP and provide seamless access to integrated <a href="/workers/platform/storage-options/">edge storage solutions</a> like R2 Object Storage and D1 Serverless SQLite Database. This drastically reduces TTFB and contributes significantly to aggressive CWV targets. Furthermore, this Originless model, leveraging Workers and R2, is the optimal design for high-performance file distribution, eliminating the need for a traditional backend server to deliver large datasets and media.</p>
<p><strong>Traditional Origin Optimization:</strong> For applications that cannot be <a href="https://www.cloudflare.com/modernize-applications/">refactored or modernized</a> to an originless model, the following optimizations are required to minimize the resulting latency impact of traditional infrastructure:</p>
<ul>
<li><strong>Connectivity:</strong> Cloudflare connects using <a href="/speed/optimization/protocol/http2-to-origin/">HTTP/2 to Origin</a>, utilizing <a href="/smart-shield/concepts/connection-reuse/">Connection Reuse</a> to multiplex requests over a single persistent connection, reducing TCP/TLS overhead. For enhanced reliability and security, <a href="/network-interconnect/">Cloudflare Network Interconnect (CNI)</a> allows you to connect your network infrastructure directly to Cloudflare - bypassing the public Internet - for a more performant and secure experience. Additionally, leveraging the <a href="https://www.cloudflare.com/bandwidth-alliance/">Bandwidth Alliance</a> (including partners like <a href="https://www.cloudflare.com/en-gb/partners/technology-partners/microsoft/azure-routing-preference/">Microsoft Azure Routing Preference</a>) can significantly reduce or waive data egress fees.</li>
<li><strong>Private Infrastructure:</strong> <a href="/workers-vpc/">Workers VPC</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> enable direct connectivity to private storage endpoints or databases on public clouds without necessarily exposing them to the public Internet.</li>
<li><strong>Load Balancing:</strong> Traffic is distributed across healthy servers using <a href="/load-balancing/understand-basics/proxy-modes/">Cloudflare Load Balancing</a>. If an origin fails, traffic is instantly rerouted to healthy server pools. Alternatively, <a href="/dns/manage-dns-records/how-to/round-robin-dns/">Round-Robin DNS</a> can be used for simpler distribution strategies.</li>
</ul>
<p><img src="/assets/upstream/images/reference-architecture/distributed-web-performance-architecture/deployment-models.jpg" alt="Figure 5: Deployment models comparing Serverful (DNS, CDN, Images, Zaraz, Waiting Room, Load Balancing, Network Interconnect) and Serverless (Workers, Workers KV, AI, Queues, R2, D1, Hyperdrive) architectures." title="Figure 5: Deployment models" /></p>
<h2 id="tools-and-resources">Tools and resources</h2>
<p>Continuous monitoring and testing verify each optimization. Measurement and logging confirm real gains, surface regressions early, and reveal edge cases long before they affect clients.</p>
<p>When analyzing this data, it is important to take into account <a href="/fundamentals/reference/connection-limits/">connection limits</a> and <a href="/fundamentals/reference/tcp-connections/">TCP connection behavior</a>, while also accounting for <a href="/fundamentals/reference/cloudflare-site-crawling/">Cloudflare crawlers</a> and the <a href="/fundamentals/reference/cdn-cgi-endpoint/">/cdn-cgi/ endpoint</a>, as well as potential <a href="/fundamentals/reference/google-analytics/">data discrepancies between Cloudflare and Google Analytics</a>.</p>
<h3 id="cloudflare-platform-tools">Cloudflare platform tools</h3>
<ul>
<li><a href="https://dash.cloudflare.com/?to=/:account/:zone/speed/">Cloudflare Observatory</a>: The primary dashboard for performance. It combines Synthetic tests (Google Lighthouse) for standardized baselines with Real User Monitoring (RUM) to capture actual user experiences across different devices and regions.</li>
<li><a href="/analytics/graphql-api/">GraphQL Analytics API</a>: Use this for Trends and <a href="https://blog.cloudflare.com/introducing-timing-insights/">Timing Insights</a>. Query specific metrics like <code>edgeDnsResponseTimeMs</code> versus <code>originResponseDurationMs</code> to pinpoint exactly where latency is introduced.</li>
<li><a href="/web-analytics/">Web Analytics</a>: Specific for privacy-first, edge-based RUM analytics.</li>
<li><a href="/cache/performance-review/cache-analytics/">Cache Analytics</a>: Critical for analyzing Cache Hit Ratio (CHR) and &quot;Requests by Cache Status&quot; to find uncached content that causes origin load.</li>
<li><a href="/ruleset-engine/">Ruleset Engine</a>: Review and leverage the extensive library of <a href="/ruleset-engine/rules-language/fields/reference/">fields</a>, including network metrics like <a href="/changelog/2025-10-30-tcp-rtt-and-tcp-fields/">TCP RTT and TCP fields</a>, to implement precise custom logic for routing, caching, and security based on real-time connection properties.</li>
<li>Logging &amp; Forensics:
<ul>
<li><a href="/log-explorer/">Log Explorer</a>: For ad-hoc querying of request logs directly in the dashboard. Use <a href="/logs/logpush/logpush-job/custom-fields/">Custom Log Fields</a> to log additional request headers, response headers and cookies.</li>
<li><a href="/logs/logpush/">Logpush</a>: For exporting logs to third-party SIEMs with optional <a href="/logs/logpush/logpush-job/log-output-options/">Log Output Options</a>, supporting formats such as CSV or JSON. Essential for analyzing custom fields and long-term trends, as well as calculating the Download Success Rate and analyzing Download Throughput for large files.</li>
<li><a href="/logs/instant-logs/">Instant Logs</a>: Real-time traffic inspection for immediate debugging.</li>
<li><a href="/network-error-logging/">Network Error Logging (NEL)</a>: Captures client-side connectivity issues that the server might never see.</li>
</ul>
</li>
</ul>
<h3 id="open-source-and-automation">Open source and automation</h3>
<ul>
<li><a href="https://github.com/cloudflare/telescope">Cloudflare Telescope</a>: An open-source, cross-browser front-end testing agent capable of running tests in all major browsers. Use this to automate performance regression testing in your CI/CD pipeline.</li>
<li><a href="https://blog.cloudflare.com/how-does-cloudflares-speed-test-really-work/">Cloudflare Speed Test</a>: Measures realistic Internet connection quality - including loaded latency, jitter, and packet loss - by simulating real-world usage on Cloudflare's global network using predefined data blocks, rather than simply testing for peak throughput saturation.</li>
<li><a href="https://github.com/cloudflare/cloudflare-prometheus-exporter">Cloudflare Prometheus Exporter</a>: Scrapes metrics from the <a href="/analytics/graphql-api/">GraphQL Analytics API</a> and exposes them in a Prometheus-compatible format, allowing you to visualize Cloudflare performance data alongside your infrastructure metrics in Grafana or similar tools.</li>
</ul>
<h3 id="external-validation-and-benchmarking-tools">External validation and benchmarking tools</h3>
<p>While Cloudflare provides internal metrics, external (third-party) tools are vital for independent validation and deep-dive analysis of the critical rendering path.</p>
<ul>
<li><a href="https://www.webpagetest.org/">WebPageTest</a>: Detailed waterfall charts and deep analysis of loading behavior.</li>
<li><a href="https://pagespeed.web.dev/">Google PageSpeed Insights</a>: The standard for Core Web Vitals assessment (Field &amp; Lab data).</li>
<li><a href="https://www.debugbear.com/tools">DebugBear</a>: Excellent for continuous monitoring and tracking speed history.</li>
<li><a href="https://tools.pingdom.com/">Pingdom</a>: Useful for simple, geographic-based availability and speed testing.</li>
<li><a href="https://treo.sh/sitespeed">Treo.sh</a>: Fast, historical visualization of Chrome User Experience Report (CrUX) data.</li>
</ul>
