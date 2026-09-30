---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/load-balancing/
  description: '2026-08-31'
  full_title: load-balancing changelog | Cloudflare Docs
  head_html: <title>load-balancing changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-08-31"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/load-balancing/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="load-balancing changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-08-31"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/load-balancing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/load-balancing/#page","headline":"load-balancing changelog | Cloudflare Docs","description":"2026-08-31","url":"https://developers.cloudflare.com/changelog/product/load-balancing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/load-balancing/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="load-balancing-now-supports-pool-sets"><a href="/changelog/post/2026-08-31-pool-sets/">Load Balancing now supports pool sets</a></h2>
<p><em>2026-08-31</em></p>
<p>Cloudflare Load Balancing now supports pool sets through the API. Pool sets combine geographic matching with location-specific traffic steering. One load balancer can now use different routing behavior for different locations.</p>
<p>Each pool set can match a Cloudflare data center, country, or region. It then supplies the candidate pools and can apply its own steering policy, pool weights, and fallback pool. Cloudflare evaluates pool sets in array order and applies the first matching pool set.</p>
<p>For example, this pool set uses Dynamic Latency steering for traffic from Germany:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;pool_sets&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;germany-lowest-latency&quot;,&#10;			&quot;match&quot;: { &quot;topology&quot;: { &quot;countries&quot;: [&quot;DE&quot;] } },&#10;			&quot;overrides&quot;: {&#10;				&quot;pools&quot;: [&#10;					&quot;0930eec54a4c7ae6616985b79f678210&quot;,&#10;					&quot;c8b4f5a6d7e84910a2b3c4d5e6f70819&quot;&#10;				],&#10;				&quot;steering_policy&quot;: &quot;dynamic_latency&quot;&#10;			}&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>Use pool sets for active-active traffic distribution, location-specific failover, and regional routing policies. For proxied traffic, a pool set can also return a fixed HTTP response instead of selecting a pool.</p>
<p>For configuration details and more examples, refer to <a href="/load-balancing/understand-basics/traffic-steering/pool-sets/">Pool sets</a>.</p>


<h2 id="load-balancing-analytics-now-filters-by-pool-name"><a href="/changelog/post/2026-08-17-pool-name-analytics-filter/">Load balancing analytics now filters by pool name</a></h2>
<p><em>2026-08-17</em></p>
<p>Load balancing analytics now filters traffic data by pool name instead of pool ID, aligning the query behavior with the pool names displayed in the filter dropdown.</p>
<p>Previously, the analytics pool filter queried by internal pool ID while displaying pool names in the UI dropdown. This mismatch caused filtering issues when pools shared similar names or when you expected results based on the visible pool name. Because the underlying query used a different identifier than what appeared on screen, the displayed data could be confusing or incorrect.</p>
<p>The pool filter now queries by the same pool name shown in the dropdown. When you select a pool from the filter, the analytics graphs and tables display data for that specific pool as you would expect. This change affects:</p>
<ul>
<li><strong>Requests over time</strong>, filtering the chart series to the selected pool.</li>
<li><strong>Pool distribution</strong>, showing only the selected pool segment.</li>
<li><strong>Top endpoints</strong>, displaying cards for origins in the selected pool.</li>
<li><strong>Latency</strong>, showing latency data for the selected pool.</li>
</ul>
<p>The <strong>Logs</strong> view and health event filtering are unchanged.</p>
<p>To use this, go to <strong>Traffic</strong> &gt; <strong>Load Balancing Analytics</strong> for a zone. The same pool filter appears in the analytics view for an individual load balancer under <strong>Load Balancing</strong> at the account level.</p>
<p>For more information about analytics filters and metrics, refer to <a href="/load-balancing/reference/load-balancing-analytics/">Load Balancing Analytics</a>.</p>


<h2 id="load-balancing-health-notifications-now-resolve-automatically"><a href="/changelog/post/2026-08-07-stateful-health-notifications/">Load Balancing health notifications now resolve automatically</a></h2>
<p><em>2026-08-07</em></p>
<p><a href="/load-balancing/">Load Balancing</a> health notifications are now stateful. When a pool or endpoint becomes unhealthy, the notification opens an incident in your alerting tool as before. When that same pool or endpoint recovers, the follow-up notification is matched to the original alert and resolves that incident automatically, so you no longer have to close it by hand.</p>
<p>As part of this change, Load Balancing also sends a notification when a pool or endpoint returns to a healthy state, not only when it becomes unhealthy. Expect to see recovery notifications alongside the failure notifications you already receive.</p>
<p>This applies to your existing Load Balancing health alerts with no configuration change, and it matches the behavior already used by <a href="/health-checks/">Health Checks</a> notifications.</p>
<p>Two things to keep in mind:</p>
<ul>
<li>A recovery notification is matched to the earlier unhealthy notification for the <strong>same pool or endpoint</strong>. Renaming an endpoint while an incident is open prevents the match, so that incident stays open until you close it.</li>
<li>If a health change cannot be classified as either healthy or unhealthy, the notification is still delivered, but without the state needed to open or resolve an incident.</li>
</ul>
<p>Refer to <a href="/load-balancing/additional-options/pagerduty-integration/">Integrate with PagerDuty</a> to learn more about routing Load Balancing health notifications to an incident management tool.</p>


<h2 id="see-fallback-pool-traffic-separately-in-load-balancing-analytics"><a href="/changelog/post/2026-08-03-fallback-pool-analytics/">See fallback pool traffic separately in load balancing analytics</a></h2>
<p><em>2026-08-03</em></p>
<p>Load balancing analytics now shows traffic served by your <a href="/load-balancing/understand-basics/health-details/#fallback-pools">fallback pool</a> separately from traffic routed to the same pool by normal steering.</p>
<p>Previously, requests were grouped by pool name alone. If the pool acting as your fallback also received traffic through your steering policy, both appeared as a single series, so it was not obvious from the graph whether Cloudflare was still making health-based routing decisions or had fallen back to the pool of last resort. Because the fallback pool ignores health, that distinction matters when you are diagnosing an outage or reviewing how much traffic was shed.</p>
<p>Fallback traffic is now labeled with the pool name followed by <code>(Fallback)</code>. A pool named <code>eu-west</code>, for example, is shown as <code>eu-west (Fallback)</code>. This label appears as its own entry in:</p>
<ul>
<li><strong>Requests over time</strong>, as a separate series in the chart.</li>
<li><strong>Pool distribution</strong>, as a separate segment.</li>
<li><strong>Top endpoints</strong>, as a separate card for the pool.</li>
</ul>
<p>The <strong>Latency</strong> view and the health event <strong>Logs</strong> are unchanged.</p>
<p>To see this, go to <strong>Traffic</strong> &gt; <strong>Load Balancing Analytics</strong> for a zone. The same breakdown appears in the analytics view for an individual load balancer under <strong>Load Balancing</strong> at the account level.</p>
<p>Refer to <a href="/load-balancing/reference/load-balancing-analytics/">load balancing analytics</a> to learn more.</p>


<h2 id="monitor-groups-for-advanced-health-checking-with-load-balancing"><a href="/changelog/post/2025-08-15-monitor-groups-for-load-balancing/">Monitor Groups for Advanced Health Checking With Load Balancing</a></h2>
<p><em>2025-10-16</em></p>
<p>Cloudflare Load Balancing now supports Monitor Groups, a powerful new way to combine multiple health monitors into a single, logical group. This allows you to create sophisticated health checks that more accurately reflect the true availability of your applications by assessing multiple services at once.</p>
<p>With Monitor Groups, you can ensure that all critical components of an application are healthy before sending traffic to an origin pool, enabling smarter failover decisions and greater resilience. This feature is now available via the API for customers with an Enterprise Load Balancing subscription.</p>
<h4 id="2025-08-15-monitor-groups-for-load-balancing-what-you-can-do">What you can do:</h4>
<ul>
<li><strong>Combine Multiple Monitors</strong>: Group different health monitors (for example, HTTP, TCP) that check various application components, like a primary API gateway and a specific <code>/login</code> service.</li>
<li><strong>Isolate Monitors for Observation</strong>: Mark a monitor as &quot;monitoring only&quot; to receive alerts and data without it affecting a pool's health status or traffic steering. This is perfect for testing new checks or observing non-critical dependencies.</li>
<li><strong>Improve Steering Intelligence</strong>: Latency for Dynamic Steering is automatically averaged across all active monitors in a group, providing a more holistic view of an origin's performance.</li>
</ul>
<p>This enhancement is ideal for complex, multi-service applications where the health of one component depends on another. By aggregating health signals, Monitor Groups provide a more accurate and comprehensive assessment of your application's true status.</p>
<p>For detailed information and API configuration guides, please visit our <a href="/load-balancing/monitors/monitor-groups">developer documentation</a> for Monitor Groups.</p>


<h2 id="steer-traffic-by-as-number-in-load-balancing-custom-rules"><a href="/changelog/post/2025-08-15-asnum-support-in-custom-rules/">Steer Traffic by AS Number in Load Balancing Custom Rules</a></h2>
<p><em>2025-08-15</em></p>
<p>You can now create more granular, network-aware Custom Rules in Cloudflare Load Balancing using the Autonomous System Number (ASN) of an incoming request.</p>
<p>This allows you to steer traffic with greater precision based on the network source of a request. For example, you can route traffic from specific Internet Service Providers (ISPs) or enterprise customers to dedicated infrastructure, optimize performance, or enforce compliance by directing certain networks to preferred data centers.</p>
<p><img src="/assets/upstream/images/changelog/load-balancing/asnum-custom-rule.png" alt="Create a Load Balancing Custom Rule using AS Num" /></p>
<p>To get started, create a <a href="https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/">Custom Rule</a> in your Load Balancer and select <strong>AS Num</strong> from the <strong>Field</strong> dropdown.</p>


<h2 id="improvements-to-monitoring-using-zone-settings"><a href="/changelog/post/2025-08-06-zone-monitoring-improvements/">Improvements to Monitoring Using Zone Settings</a></h2>
<p><em>2025-08-06</em></p>
<p>Cloudflare Load Balancing Monitors support loading and applying settings for a specific zone to monitoring requests to origin endpoints. This feature has been migrated to new infrastructure to improve reliability, performance, and accuracy.</p>
<p>All zone monitors have been tested against the new infrastructure. There should be no change to health monitoring results of currently healthy and active pools. Newly created or re-enabled pools may need validation of their monitor zone settings before being introduced to service, especially regarding correct application of mTLS.</p>
<h4 id="2025-08-06-zone-monitoring-improvements-what-you-can-expect">What you can expect:</h4>
<ul>
<li>More reliable application of zone settings to monitoring requests, including
<ul>
<li>Authenticated Origin Pulls</li>
<li>Aegis Egress IP Pools</li>
<li>Argo Smart Routing</li>
<li>HTTP/2 to Origin</li>
</ul>
</li>
<li>Improved support and bug fixes for retries, redirects, and proxied origin resolution</li>
<li>Improved performance and reliability of monitoring requests within the Cloudflare network</li>
<li>Unrelated CDN or WAF configuration changes should have no risk of impact to pool health</li>
</ul>


<h2 id="new-account-level-load-balancing-ui-and-private-load-balancers"><a href="/changelog/post/2025-06-04-account-load-balancing-ui/">New Account-Level Load Balancing UI and Private Load Balancers</a></h2>
<p><em>2025-06-04</em></p>
<p>We've made two large changes to load balancing:</p>
<ul>
<li>Redesigned the user interface, now centralized at the <strong>account level</strong>.</li>
<li>Introduced <a href="/load-balancing/private-network/"><strong>Private Load Balancers</strong></a> to the UI, enabling you to manage traffic for all of your external and internal applications in a single spot.</li>
</ul>
<p>This update streamlines how you manage load balancers across multiple zones and extends robust traffic management to your private network infrastructure.</p>
<p><img src="/assets/upstream/images/changelog/load-balancing/account-load-balancing-ui.png" alt="Load Balancing UI" /></p>
<p><strong>Key Enhancements:</strong></p>
<ul>
<li>
<p><strong>Account-Level UI Consolidation:</strong></p>
<ul>
<li>
<p><strong>Unified Management:</strong> Say goodbye to navigating individual zones for load balancing tasks. You can now view, configure, and monitor all your load balancers across every zone in your account from a single, intuitive interface at the account level.</p>
</li>
<li>
<p><strong>Improved Efficiency:</strong> This centralized approach provides a more streamlined workflow, making it faster and easier to manage both your public-facing and internal traffic distribution.</p>
</li>
</ul>
</li>
<li>
<p><strong>Private Network Load Balancing:</strong></p>
<ul>
<li>
<p><strong>Secure Internal Application Access:</strong> Create <a href="/load-balancing/private-network/"><strong>Private Load Balancers</strong></a> to distribute traffic to applications hosted within your private network, ensuring they are not exposed to the public Internet.</p>
</li>
<li>
<p><strong>WARP &amp; Magic WAN Integration:</strong> Effortlessly direct internal traffic from users connected via Cloudflare WARP or through your Magic WAN infrastructure to the appropriate internal endpoint pools.</p>
</li>
<li>
<p><strong>Enhanced Security for Internal Resources:</strong> Combine reliable Load Balancing with Zero Trust access controls to ensure your internal services are both performant and only accessible by verified users.</p>
</li>
</ul>
</li>
</ul>
<p><img src="/assets/upstream/images/changelog/load-balancing/private-load-balancer.png" alt="Private Load Balancers" /></p>


<h2 id="udp-and-icmp-monitor-support-for-private-load-balancing-endpoints"><a href="/changelog/post/2025-05-06-private-health-monitoring-methods/">UDP and ICMP Monitor Support for Private Load Balancing Endpoints</a></h2>
<p><em>2025-05-06</em></p>
<p>Cloudflare Load Balancing now supports <strong>UDP (Layer 4)</strong> and <strong>ICMP (Layer 3)</strong> health monitors for <strong>private endpoints</strong>. This makes it simple to track the health and availability of internal services that don’t respond to HTTP, TCP, or other protocol probes.</p>
<h4 id="2025-05-06-private-health-monitoring-methods-what-you-can-do">What you can do:</h4>
<ul>
<li>Set up <strong>ICMP ping monitors</strong> to check if your private endpoints are reachable.</li>
<li>Use <strong>UDP monitors</strong> for lightweight health checks on non-TCP workloads, such as DNS, VoIP, or custom UDP-based services.</li>
<li>Gain better visibility and uptime guarantees for services running behind <strong>Private Network Load Balancing</strong>, without requiring public IP addresses.</li>
</ul>
<p>This enhancement is ideal for internal applications that rely on low-level protocols, especially when used in conjunction with <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/"><strong>Cloudflare Tunnel</strong></a>, <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/"><strong>WARP</strong></a>, and <a href="/cloudflare-wan/"><strong>Magic WAN</strong></a> to create a secure and observable private network.</p>
<p>Learn more about <a href="/load-balancing/private-network/">Private Network Load Balancing</a> or view the full list of <a href="/load-balancing/monitors/#supported-protocols">supported health monitor protocols</a>.</p>



