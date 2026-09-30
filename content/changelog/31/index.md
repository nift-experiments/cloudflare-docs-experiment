---
cp9:
  canonical: https://developers.cloudflare.com/changelog/31/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 31 | Cloudflare Docs
  head_html: <title>Changelog - page 31 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/31/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 31"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/31/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/31/#page","headline":"Changelog - page 31 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/31/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/31/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2025-11-13">Nov 13, 2025</time><div>
<h2 id="post-2025-11-13-new-datasets"><a href="/changelog/post/2025-11-13-new-datasets/">Log Explorer adds 14 new datasets</a></h2>
<div class="changelog-badges"><span>log-explorer</span></div><div class="changelog-body"><p>We've significantly enhanced Log Explorer by adding support for 14 additional Cloudflare product datasets.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-12">Nov 12, 2025</time><div>
<h2 id="post-2025-11-12-bola-attack-detection"><a href="/changelog/post/2025-11-12-bola-attack-detection/">New BOLA Vulnerability Detection for API Shield</a></h2>
<div class="changelog-badges"><span>api-shield</span></div><div class="changelog-body"><p>Now, API Shield automatically searches for and highlights <strong>Broken Object Level Authorization (BOLA) attacks</strong> on managed API endpoints. API Shield will highlight both BOLA enumeration attacks and BOLA pollution attacks, telling you what was attacked, by who, and for how long.</p>
<p>You can find these attacks three different ways: Security Overview, Endpoint details, or Security Analytics. If these attacks are not found on your managed API endpoints, there will not be an overview card or security analytics suspicious activity card.</p>
<p>On the Security Overview card, select the suggestion &gt; <strong>View details</strong> to review the top attacked API endpoints, endpoint details, and the attack summary:
<img src="/assets/upstream/images/changelog/api-shield/bola-overview-card.png" alt="BOLA attack Overview card" />
<img src="/assets/upstream/images/changelog/api-shield/bola-overview-drawer.png" alt="BOLA attack Overview drawer" /></p>
<p>From the endpoint details, you can select <strong>View attack</strong> to find details about the BOLA attacker’s sessions.</p>
<p><img src="/assets/upstream/images/changelog/api-shield/bola-endpoint-attack.png" alt="BOLA attack endpoint details" /></p>
<p>From here, select <strong>View in Analytics</strong> to observe attacker traffic over time for the last seven days.</p>
<p><img src="/assets/upstream/images/changelog/api-shield/bola-analytics-drawer.png" alt="BOLA attack analytics drawer" /></p>
<p>Your search will filter to traffic on that endpoint in the last seven days, along with the malicious session IDs found in the attack. Session IDs are hashed for privacy and will not be found in your origin logs. Refer to IP and JA4 fingerprint to cross-reference behavior at the origin.</p>
<p>At any time, you can also start your investigation into attack traffic from Security Analytics by selecting the suspicious activity card.</p>
<p><img src="/assets/upstream/images/changelog/api-shield/bola-suspicious-card.png" alt="Suspicious Activity card" /></p>
<p>We urge you to take all of this client information to your developer team to research the attacker behavior and ensure any broken authorization policies in your API are fixed at the source in your application, preventing further abuse.</p>
<p>In addition, this release marks the end of the beta period for these scans. All Enterprise customers with API Shield subscriptions will see these new attacks if found on their zone.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-12">Nov 12, 2025</time><div>
<h2 id="post-2025-11-12-dex-logpush-jobs"><a href="/changelog/post/2025-11-12-dex-logpush-jobs/">DEX Logpush jobs</a></h2>
<div class="changelog-badges"><span>dex</span></div><div class="changelog-body"><p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into WARP device metrics, connectivity, and network performance across your Cloudflare SASE deployment.</p>
<p>We've released four new WARP and DEX device data sets that can be exported via <a href="/cloudflare-one/insights/logs/logpush/">Cloudflare Logpush</a>. These Logpush data sets can be exported to R2, a cloud bucket, or a SIEM to build a customized logging and analytics experience.</p>
<ol>
<li><a href="/logs/logpush/logpush-job/datasets/account/dex_application_tests/">DEX Application Tests</a></li>
<li><a href="/logs/logpush/logpush-job/datasets/account/dex_device_state_events/">DEX Device State Events</a></li>
<li><a href="/logs/logpush/logpush-job/datasets/account/warp_config_changes/">WARP Config Changes</a></li>
<li><a href="/logs/logpush/logpush-job/datasets/account/warp_toggle_changes/">WARP Toggle Changes</a></li>
</ol>
<p>To create a new DEX or WARP Logpush job, customers can go to the account level of the Cloudflare dashboard &gt; Analytics &amp; Logs &gt; Logpush to get started.</p>
<p><img src="/assets/upstream/images/changelog/dex/dex_logpush_datasets.png" alt="DEX logpush job creation dashboard" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-12">Nov 12, 2025</time><div>
<h2 id="post-2025-11-12-analytics-engine-further-sql-enhancements"><a href="/changelog/post/2025-11-12-analytics-engine-further-sql-enhancements/">More SQL aggregate, date and time functions available in Workers Analytics Engine</a></h2>
<div class="changelog-badges"><span>workers-analytics-engine</span><span>workers</span></div><div class="changelog-body"><p>You can now perform more powerful queries directly in <a href="https://developers.cloudflare.com/analytics/analytics-engine/">Workers Analytics Engine</a> with a major expansion of our SQL function library.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-12">Nov 12, 2025</time><div>
<h2 id="post-2025-11-11-warp-linux-ga"><a href="/changelog/post/2025-11-11-warp-linux-ga/">WARP client for Linux (version 2025.9.558.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Linux WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes, improvements, and new features including <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery">Path Maximum Transmission Unit Discovery (PMTUD)</a>. When PMTUD is enabled, the client will dynamically adjust packet sizing to optimize connection performance. There is also a new connection status message in the GUI to inform users that the local network connection may be unstable. This will make it easier to diagnose connectivity issues.</p>
<p>WARP client version 2025.8.779.0 introduced an updated public key for Linux packages. The public key must be updated if it was installed before September 12, 2025 to ensure the repository remains functional after December 4, 2025. Instructions to make this update are available at <a href="https://pkg.cloudflareclient.com/">pkg.cloudflareclient.com</a>.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>The GUI now displays the health of the tunnel and DNS connections by showing a connection status message when the network may be unstable. This will make it easier to diagnose connectivity issues.</li>
<li>Fixed an issue where deleting a registration was erroneously reported as having failed.</li>
<li>Path Maximum Transmission Unit Discovery (PMTUD) may now be used to discover the effective MTU of the connection. This allows the WARP client to improve connectivity optimized for each network. PMTUD is disabled by default. To enable it, refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery">PMTUD documentation</a>.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-12">Nov 12, 2025</time><div>
<h2 id="post-2025-11-11-warp-macos-ga"><a href="/changelog/post/2025-11-11-warp-macos-ga/">WARP client for macOS (version 2025.9.558.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the macOS WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes, improvements, and new features including <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery">Path Maximum Transmission Unit Discovery (PMTUD)</a>. When PMTUD is enabled, the client will dynamically adjust packet sizing to optimize connection performance. There is also a new connection status message in the GUI to inform users that the local network connection may be unstable. This will make it easier to diagnose connectivity issues.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>The GUI now displays the health of the tunnel and DNS connections by showing a connection status message when the network may be unstable. This will make it easier to diagnose connectivity issues.</li>
<li>Fixed an issue where deleting a registration was erroneously reported as having failed.</li>
<li>Path Maximum Transmission Unit Discovery (PMTUD) may now be used to discover the effective MTU of the connection. This allows the WARP client to improve connectivity optimized for each network. PMTUD is disabled by default. To enable it, refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery">PMTUD documentation</a>.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to <a href="https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server">Route traffic to fallback server</a>.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-12">Nov 12, 2025</time><div>
<h2 id="post-2025-11-11-warp-windows-ga"><a href="/changelog/post/2025-11-11-warp-windows-ga/">WARP client for Windows (version 2025.9.558.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Windows WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes, improvements, and new features including <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery">Path Maximum Transmission Unit Discovery (PMTUD)</a>. When PMTUD is enabled, the client will dynamically adjust packet sizing to optimize connection performance. There is also a new connection status message in the GUI to inform users that the local network connection may be unstable. This will make it easier to diagnose connectivity issues.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Fixed an inconsistency with <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#disconnect-warp-on-all-devices">Global WARP override</a> settings in multi-user environments when switching between users.</li>
<li>The GUI now displays the health of the tunnel and DNS connections by showing a connection status message when the network may be unstable. This will make it easier to diagnose connectivity issues.</li>
<li>Fixed an issue where deleting a registration was erroneously reported as having failed.</li>
<li>Path Maximum Transmission Unit Discovery (PMTUD) may now be used to discover the effective MTU of the connection. This allows the WARP client to improve connectivity optimized for each network. PMTUD is disabled by default. To enable it, refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery">PMTUD documentation</a>.</li>
<li>Improvements for the <a href="/cloudflare-one/reusable-components/posture-checks/warp-client-checks/os-version/">OS version</a> WARP client check. Windows Updated Build Revision (UBR) numbers can now be checked by the client to ensure devices have required security patches and features installed.</li>
<li>The WARP client now supports Windows 11 ARM-based machines. For information on known limitations, refer to the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/known-limitations/#cloudflare-one-client-disconnected-on-windows-arm">Known limitations page</a>.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>
<p>For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum <a href="https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd">Windows 11 24H2 KB5062553</a> or higher for resolution.</p>
</li>
<li>
<p>Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to <a href="https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server">Route traffic to fallback server</a>.</p>
</li>
<li>
<p>Devices with KB5055523 installed may receive a warning about <code>Win32/ClickFix.ABA</code> being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to <a href="https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0">version 1.429.19.0</a> or later.</p>
</li>
<li>
<p>DNS resolution may be broken when the following conditions are all true:</p>
<ul>
<li>WARP is in Secure Web Gateway without DNS filtering (tunnel-only) mode.</li>
<li>A custom DNS server address is configured on the primary network adapter.</li>
<li>The custom DNS server address on the primary network adapter is changed while WARP is connected.</li>
</ul>
<p>To work around this issue, reconnect the WARP client by toggling off and back on.</p>
</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-11">Nov 11, 2025</time><div>
<h2 id="post-2025-11-11-resize-sql-window"><a href="/changelog/post/2025-11-11-resize-sql-window/">Resize your custom SQL window in Log Explorer</a></h2>
<div class="changelog-badges"><span>log-explorer</span></div><div class="changelog-body"><p>We're excited to announce a quality-of-life improvement for Log Explorer users. You can now resize the custom SQL query window to accommodate longer and more complex queries.</p>
<p>Previously, if you were writing a long custom SQL query, the fixed-size window required excessive scrolling to view the full query. This update allows you to easily drag the bottom edge of the query window to make it taller. This means you can view your entire custom query at once, improving the efficiency and experience of writing and debugging complex queries.</p>
<p>To learn more and get started, refer to the <a href="/log-explorer/">Log Explorer documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-11">Nov 11, 2025</time><div>
<h2 id="post-2025-11-11-health-dashboards"><a href="/changelog/post/2025-11-11-health-dashboards/">Logpush Health Dashboards</a></h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>We’re excited to introduce <strong>Logpush Health Dashboards</strong>, giving customers real-time visibility into the status, reliability, and performance of their <a href="/logs/logpush/">Logpush</a> jobs. Health dashboards make it easier to detect delivery issues, monitor job stability, and track performance across destinations. The dashboards are divided into two sections:</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-11">Nov 11, 2025</time><div>
<h2 id="post-2025-11-11-cloudflared-proxy-dns"><a href="/changelog/post/2025-11-11-cloudflared-proxy-dns/">cloudflared proxy-dns command will be removed starting February 2, 2026</a></h2>
<div class="changelog-badges"><span>tunnel</span><span>cloudflare-tunnel-sase</span></div><div class="changelog-body"><p>Starting February 2, 2026, the <code>cloudflared proxy-dns</code> command will be removed from all new <code>cloudflared</code> <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/">releases</a>.</p>
<p>This change is being made to enhance security and address a potential vulnerability in an underlying DNS library. This vulnerability is specific to the <code>proxy-dns</code> command and does not affect any other <code>cloudflared</code> features, such as the core <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> service.</p>
<p>The <code>proxy-dns</code> command, which runs a client-side <a href="/1.1.1.1/encryption/dns-over-https/">DNS-over-HTTPS (DoH)</a> proxy, has been an officially undocumented feature for several years. This functionality is fully and securely supported by our actively developed products.</p>
<p>Versions of <code>cloudflared</code> released before this date will not be affected and will continue to operate. However, note that our <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/#deprecated-releases">official support policy</a> for any <code>cloudflared</code> release is one year from its release date.</p>
<h4 id="2025-11-11-cloudflared-proxy-dns-migration-paths">Migration paths</h4>
<p>We strongly advise users of this undocumented feature to migrate to one of the following officially supported solutions before February 2, 2026, to continue benefiting from secure <a href="/1.1.1.1/encryption/dns-over-https/">DNS-over-HTTPS</a>.</p>
<h4 id="2025-11-11-cloudflared-proxy-dns-end-user-devices">End-user devices</h4>
<p>The preferred method for enabling DNS-over-HTTPS on user devices is the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare WARP client</a>. The WARP client automatically secures and proxies all DNS traffic from your device, integrating it with your organization's <a href="/cloudflare-one/traffic-policies/">Zero Trust policies</a> and <a href="/cloudflare-one/reusable-components/posture-checks/">posture checks</a>.</p>
<h4 id="2025-11-11-cloudflared-proxy-dns-servers-routers-and-iot-devices">Servers, routers, and IoT devices</h4>
<p>For scenarios where installing a client on every device is not possible (such as servers, routers, or IoT devices), we recommend using the <a href="/mesh/">WARP Connector</a>.</p>
<p>Instead of running <code>cloudflared proxy-dns</code> on a machine, you can install the WARP Connector on a single Linux host within your private network. This connector will act as a gateway, securely routing all DNS and network traffic from your <a href="/mesh/features/routes/">entire subnet</a> to Cloudflare for <a href="/cloudflare-one/traffic-policies/">filtering and logging</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-10">Nov 10, 2025</time><div>
<h2 id="post-2025-11-10-ai-crawl-control-crawler-info"><a href="/changelog/post/2025-11-10-ai-crawl-control-crawler-info/">Crawler drilldowns with extended actions menu</a></h2>
<div class="changelog-badges"><span>ai-crawl-control</span></div><div class="changelog-body"><p>AI Crawl Control now supports per-crawler drilldowns with an extended actions menu and status code analytics. Drill down into Metrics, Cloudflare Radar, and Security Analytics, or export crawler data for use in <a href="/waf/custom-rules/">WAF custom rules</a>, <a href="/rules/url-forwarding/">Redirect Rules</a>, and robots.txt files.</p>
<h4 id="2025-11-10-ai-crawl-control-crawler-info-what-s-new">What's new</h4>
<h4 id="2025-11-10-ai-crawl-control-crawler-info-status-code-distribution-chart">Status code distribution chart</h4>
<p>The <strong>Metrics</strong> tab includes a status code distribution chart showing HTTP response codes (2xx, 3xx, 4xx, 5xx) over time. Filter by individual crawler, category, operator, or time range to analyze how specific crawlers interact with your site.</p>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-status-codes.png" alt="AI Crawl Control status code distribution chart" /></p>
<h4 id="2025-11-10-ai-crawl-control-crawler-info-extended-actions-menu">Extended actions menu</h4>
<p>Each crawler row includes a three-dot menu with per-crawler actions:</p>
<ul>
<li><strong>View Metrics</strong> — Filter the AI Crawl Control Metrics page to the selected crawler.</li>
<li><strong>View on Cloudflare Radar</strong> — Access verified crawler details on Cloudflare Radar.</li>
<li><strong>Copy User Agent</strong> — Copy user agent strings for use in WAF custom rules, Redirect Rules, or robots.txt files.</li>
<li><strong>View in Security Analytics</strong> — Filter Security Analytics by detection IDs (Bot Management customers).</li>
<li><strong>Copy Detection ID</strong> — Copy detection IDs for use in WAF custom rules (Bot Management customers).</li>
</ul>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-crawler-info.png" alt="AI Crawl Control crawler actions menu" /></p>
<h4 id="2025-11-10-ai-crawl-control-crawler-info-get-started">Get started</h4>
<ol>
<li>Log in to the Cloudflare dashboard, and select your account and domain.</li>
<li>Go to <strong>AI Crawl Control</strong> &gt; <strong>Metrics</strong> to access the status code distribution chart.</li>
<li>Go to <strong>AI Crawl Control</strong> &gt; <strong>Crawlers</strong> and select the three-dot menu for any crawler to access per-crawler actions.</li>
<li>Select multiple crawlers to use bulk copy buttons for user agents or detection IDs.</li>
</ol>
<p>Learn more about <a href="/ai-crawl-control/">AI Crawl Control</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-10">Nov 10, 2025</time><div>
<h2 id="post-2025-11-10-waf-release"><a href="/changelog/post/2025-11-10-waf-release/">WAF Release - 2025-11-10</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s release introduces new detections for Prototype Pollution across three common vectors: URI, Body, and Header/Form.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>These attacks can affect both API and web applications by altering normal behavior or bypassing security controls.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Exploitation may allow attackers to change internal logic or cause unexpected behavior in applications using JavaScript or Node.js frameworks. Developers should sanitize input keys and avoid merging untrusted data structures.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="32405a50728746dd8caa057b606285e6">606285e6</code>
</td>
<td>N/A</td>
<td>Generic Rules - Prototype Pollution - URI</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection</td>
</tr>    
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a7da00c63c4243d2a72456fe4f59ff26">4f59ff26</code>
</td>
<td>N/A</td>
<td>Generic Rules - Prototype Pollution - Body</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="833078bdcfa04bb7aa7b8fb67efbeb39">7efbeb39</code>
</td>
<td>N/A</td>
<td>Generic Rules - Prototype Pollution - Header - Form</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection</td>
</tr>        
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-09">Nov 9, 2025</time><div>
<h2 id="post-2025-11-09-cloudflare-env-variable"><a href="/changelog/post/2025-11-09-cloudflare-env-variable/">Select Wrangler environments using the CLOUDFLARE_ENV environment variable</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Wrangler now supports using the <code>CLOUDFLARE_ENV</code> <a href="/workers/wrangler/system-environment-variables/#supported-environment-variables">environment variable</a> to select the active <a href="/workers/wrangler/environments/">environment</a> for your Worker commands. This provides a more flexible way to manage environments, especially when working with build tools and CI/CD pipelines.</p>
<h4 id="2025-11-09-cloudflare-env-variable-what-s-new">What's new</h4>
<p><strong>Environment selection via environment variable:</strong></p>
<ul>
<li>Set <code>CLOUDFLARE_ENV</code> to specify which environment to use for Wrangler commands</li>
<li>Works with all Wrangler commands that support the <code>--env</code> flag</li>
<li>The <code>--env</code> command line argument takes precedence over the <code>CLOUDFLARE_ENV</code> environment variable</li>
</ul>
<h4 id="2025-11-09-cloudflare-env-variable-example-usage">Example usage</h4>
<pre tabindex="0"><code class="language-bash">&#35; Deploy to the production environment using CLOUDFLARE_ENV&#10;CLOUDFLARE_ENV=production wrangler deploy&#10;&#10;&#35; Upload a version to the staging environment&#10;CLOUDFLARE_ENV=staging wrangler versions upload&#10;&#10;&#35; The --env flag takes precedence over CLOUDFLARE_ENV&#10;CLOUDFLARE_ENV=dev wrangler deploy --env production&#10;&#35; This will deploy to production, not dev&#10;</code></pre>
<h4 id="2025-11-09-cloudflare-env-variable-use-with-build-tools">Use with build tools</h4>
<p>The <code>CLOUDFLARE_ENV</code> environment variable is particularly useful when working with build tools like Vite. You can set the environment once during the build process, and it will be used for both building and deploying your Worker:</p>
<pre tabindex="0"><code class="language-bash">&#35; Set the environment for both build and deploy&#10;CLOUDFLARE_ENV=production npm run build &amp; wrangler deploy&#10;</code></pre>
<p>When using <code>@cloudflare/vite-plugin</code>, the build process generates a <a href="/workers/wrangler/configuration/#generated-wrangler-configuration">&quot;redirected deploy config&quot;</a> that is flattened to only contain the active environment. Wrangler will validate that the environment specified matches the environment used during the build to prevent accidentally deploying a Worker built for one environment to a different environment.</p>
<h4 id="2025-11-09-cloudflare-env-variable-learn-more">Learn more</h4>
<ul>
<li><a href="/workers/wrangler/system-environment-variables/">System environment variables</a></li>
<li><a href="/workers/wrangler/environments/">Environments</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-07">Nov 7, 2025</time><div>
<h2 id="post-2025-11-07-cache-keys-for-cloudflare-trace"><a href="/changelog/post/2025-11-07-cache-keys-for-cloudflare-trace/">Inspect Cache Keys with Cloudflare Trace</a></h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now see the exact cache key generated for any request directly in Cloudflare Trace. This visibility helps you troubleshoot cache hits and misses, and verify that your Custom Cache Keys — configured via Cache Rules or Page Rules — are working as intended.</p>
<p>Previously, diagnosing caching behavior required inferring the key from configuration settings. Now, you can confirm that your custom logic for headers, query strings, and device types is correctly applied.</p>
<p>Access Trace via the <a href="/rules/trace-request/how-to/#use-trace-in-the-dashboard">dashboard</a> or <a href="/api/resources/request_tracer/methods/trace/">API</a>, either manually for ad-hoc debugging or automated as part of your quality-of-service monitoring.</p>
<h4 id="2025-11-07-cache-keys-for-cloudflare-trace-example-scenario">Example scenario</h4>
<p>If you have a Cache Rule that segments content based on a specific cookie (for example, <code>user_region</code>), run a Trace with that cookie present to confirm the <code>user_region</code> value appears in the resulting cache key.</p>
<p>The Trace response includes the cache key in the <code>cache</code> object:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;step_name&quot;: &quot;request&quot;,&#10;  &quot;type&quot;: &quot;cache&quot;,&#10;  &quot;matched&quot;: true,&#10;  &quot;public_name&quot;: &quot;Cache Parameters&quot;,&#10;  &quot;cache&quot;: {&#10;    &quot;key&quot;: {&#10;      &quot;zone_id&quot;: &quot;023e105f4ecef8ad9ca31a8372d0c353&quot;,&#10;      &quot;scheme&quot;: &quot;https&quot;,&#10;      &quot;host&quot;: &quot;example.com&quot;,&#10;      &quot;uri&quot;: &quot;/images/hero.jpg&quot;&#10;    },&#10;    &quot;key_string&quot;: &quot;023e105f4ecef8ad9ca31a8372d0c353::::https://example.com/images/hero.jpg:::::&quot;&#10;  }&#10;}&#10;</code></pre>
<h4 id="2025-11-07-cache-keys-for-cloudflare-trace-get-started">Get started</h4>
<p>To learn more, refer to the <a href="/rules/trace-request/">Trace documentation</a> and our guide on <a href="/cache/how-to/cache-keys/">Custom Cache Keys</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-07">Nov 7, 2025</time><div>
<h2 id="post-2025-11-07-automatic-tracing"><a href="/changelog/post/2025-11-07-automatic-tracing/">Workers automatic tracing, now in open beta</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Enable automatic tracing on your Workers, giving you detailed metadata and timing information for every operation your Worker performs.</p>
<p><img src="/assets/upstream/images/workers-observability/R2_Screenshot.png" alt="Tracing example" /></p>
<p>Tracing helps you identify performance bottlenecks, resolve errors, and understand how your Worker interacts with other services on the Workers platform. You can now answer questions like:</p>
<ul>
<li>Which calls are slowing down my application?</li>
<li>Which queries to my database take the longest?</li>
<li>What happened within a request that resulted in an error?</li>
</ul>
<p><strong>You can now:</strong></p>
<ul>
<li>View traces alongside your logs in the Workers Observability dashboard</li>
<li>Export traces (and correlated logs) to any <a href="https://opentelemetry.io/docs/specs/otel/protocol/">OTLP-compatible destination</a>, such as <a href="/workers/observability/exporting-opentelemetry-data/honeycomb/">Honeycomb</a>, <a href="/workers/observability/exporting-opentelemetry-data/sentry/">Sentry</a> or <a href="/workers/observability/exporting-opentelemetry-data/grafana-cloud/">Grafana</a>, by configuring a tracing destination in the <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/destinations">Cloudflare dashboard</a></li>
<li>Analyze and query across span attributes (operation type, status, duration, errors)</li>
</ul>
<h4 id="2025-11-07-automatic-tracing-to-get-started-set">To get started, set:</h4>
<pre tabindex="0"><code class="language-jsonc">{&#10;	&quot;observability&quot;: {&#10;		&quot;traces&quot;: {&#10;			&quot;enabled&quot;: true,&#10;		},&#10;	},&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17790.md")</aside>
<h4 id="2025-11-07-automatic-tracing-want-to-learn-more">Want to learn more?</h4>
<ul>
<li><a href="https://blog.cloudflare.com/workers-tracing-now-in-open-beta/">Read the announcement</a></li>
<li><a href="/workers/observability/traces/">Check out the documentation</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-06">Nov 6, 2025</time><div>
<h2 id="post-2025-11-06-automatic-return-routing-beta"><a href="/changelog/post/2025-11-06-automatic-return-routing-beta/">Automatic Return Routing (Beta)</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span><span>cloudflare-wan</span></div><div class="changelog-body"><p>Magic WAN now supports Automatic Return Routing (ARR), allowing customers to configure Magic on-ramps (IPsec/GRE/CNI) to learn the return path for traffic flows without requiring static routes.</p>
<p>Key benefits:</p>
<ul>
<li><strong>Route-less mode</strong>: Static or dynamic routes are optional when using ARR.</li>
<li><strong>Overlapping IP space support</strong>: Traffic originating from customer sites can use overlapping private IP ranges.</li>
<li><strong>Symmetric routing</strong>: Return traffic is guaranteed to use the same connection as the original on-ramp.</li>
</ul>
<p>This feature is currently in beta and requires the new Unified Routing mode (beta).</p>
<p>For configuration details, refer to <a href="/cloudflare-wan/configuration/how-to/configure-routes/#configure-automatic-return-routing-beta">Configure Automatic Return Routing</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-06">Nov 6, 2025</time><div>
<h2 id="post-2025-11-06-connector-designate-wan-link-breakout"><a href="/changelog/post/2025-11-06-connector-designate-wan-link-breakout/">Designate WAN link for breakout traffic</a></h2>
<div class="changelog-badges"><span>cloudflare-one-appliance</span><span>cloudflare-one</span><span>cloudflare-wan</span></div><div class="changelog-body"><p>Magic WAN Connector now allows you to designate a specific WAN port for breakout traffic, giving you deterministic control over the egress path for latency-sensitive applications.</p>
<p>With this feature, you can:</p>
<ul>
<li>Pin breakout traffic for specific applications to a preferred WAN port.</li>
<li>Ensure critical traffic (such as Zoom or Teams) always uses your fastest or most reliable connection.</li>
<li>Benefit from automatic failover to standard WAN port priority if the preferred port goes down.</li>
</ul>
<p>This is useful for organizations with multiple ISP uplinks who need predictable egress behavior for performance-sensitive traffic.</p>
<p>For configuration details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#designate-wan-ports-for-breakout-apps">Designate WAN ports for breakout apps</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-06">Nov 6, 2025</time><div>
<h2 id="post-2025-11-06-Applications-recategorised-plan"><a href="/changelog/post/2025-11-06-Applications-recategorised-plan/">Applications to be remapped to the new categories</a></h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>We have previously added new application categories to better reflect their content and improve HTTP traffic management: refer to <a href="/cloudflare-one/changelog/gateway/#2025-10-28">Changelog</a>.
While the new categories are live now, we want to ensure you have ample time to review and adjust any existing rules you have configured against old categories.
The remapping of existing applications into these new categories will be completed by January 30, 2026.
This timeline allows you a dedicated period to:</p>
<ul>
<li>Review the new category structure.</li>
<li>Identify any policies you have that target the older categories.</li>
<li>Adjust your rules to reference the new, more precise categories before the old mappings change.
Once the applications have been fully remapped by January 30, 2026, you might observe some changes in the traffic being mitigated or allowed by your existing policies. We encourage you to use the intervening time to prepare for a smooth transition.</li>
</ul>
<p><strong>Applications being remappedd</strong></p>
<table>
<thead>
<tr>
<th>Application Name</th>
<th>Existing Category</th>
<th>New Category</th>
</tr>
</thead>
<tbody>
<tr>
<td>Google Photos</td>
<td>File Sharing</td>
<td>Photography &amp; Graphic Design</td>
</tr>
<tr>
<td>Flickr</td>
<td>File Sharing</td>
<td>Photography &amp; Graphic Design</td>
</tr>
<tr>
<td>ADP</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>Greenhouse</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>myCigna</td>
<td>Human Resources</td>
<td>Health &amp; Fitness</td>
</tr>
<tr>
<td>UnitedHealthcare</td>
<td>Human Resources</td>
<td>Health &amp; Fitness</td>
</tr>
<tr>
<td>ZipRecruiter</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>Amazon Business</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>Jobcenter</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>Jobsuche</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>Zenjob</td>
<td>Human Resources</td>
<td>Business</td>
</tr>
<tr>
<td>DocuSign</td>
<td>Legal</td>
<td>Business</td>
</tr>
<tr>
<td>Postident</td>
<td>Legal</td>
<td>Business</td>
</tr>
<tr>
<td>Adobe Creative Cloud</td>
<td>Productivity</td>
<td>Photography &amp; Graphic Design</td>
</tr>
<tr>
<td>Airtable</td>
<td>Productivity</td>
<td>Development</td>
</tr>
<tr>
<td>Autodesk Fusion360</td>
<td>Productivity</td>
<td>IT Management</td>
</tr>
<tr>
<td>Coursera</td>
<td>Productivity</td>
<td>Education</td>
</tr>
<tr>
<td>Microsoft Power BI</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Tableau</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Duolingo</td>
<td>Productivity</td>
<td>Education</td>
</tr>
<tr>
<td>Adobe Reader</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>AnpiReport</td>
<td>Productivity</td>
<td>Travel</td>
</tr>
<tr>
<td>ビズリーチ</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>doda (デューダ)</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>求人ボックス</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>マイナビ2026</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Power Apps</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>RECRUIT AGENT</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>シフトボード</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>スタンバイ</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Doctolib</td>
<td>Productivity</td>
<td>Health &amp; Fitness</td>
</tr>
<tr>
<td>Miro</td>
<td>Productivity</td>
<td>Photography &amp; Graphic Design</td>
</tr>
<tr>
<td>MyFitnessPal</td>
<td>Productivity</td>
<td>Health &amp; Fitness</td>
</tr>
<tr>
<td>Sentry Mobile</td>
<td>Productivity</td>
<td>Travel</td>
</tr>
<tr>
<td>Slido</td>
<td>Productivity</td>
<td>Photography &amp; Graphic Design</td>
</tr>
<tr>
<td>Arista Networks</td>
<td>Productivity</td>
<td>IT Management</td>
</tr>
<tr>
<td>Atlassian</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>CoderPad</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>eAgreements</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Vmware</td>
<td>Productivity</td>
<td>IT Management</td>
</tr>
<tr>
<td>Vmware Vcenter</td>
<td>Productivity</td>
<td>IT Management</td>
</tr>
<tr>
<td>AWS Skill Builder</td>
<td>Productivity</td>
<td>Education</td>
</tr>
<tr>
<td>Microsoft Office 365 (GCC)</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Microsoft Exchange Online (GCC)</td>
<td>Productivity</td>
<td>Business</td>
</tr>
<tr>
<td>Canva</td>
<td>Sales &amp; Marketing</td>
<td>Photography &amp; Graphic Design</td>
</tr>
<tr>
<td>Instacart</td>
<td>Shopping</td>
<td>Food &amp; Drink</td>
</tr>
<tr>
<td>Wawa</td>
<td>Shopping</td>
<td>Food &amp; Drink</td>
</tr>
<tr>
<td>McDonald's</td>
<td>Shopping</td>
<td>Food &amp; Drink</td>
</tr>
<tr>
<td>Vrbo</td>
<td>Shopping</td>
<td>Travel</td>
</tr>
<tr>
<td>American Airlines</td>
<td>Shopping</td>
<td>Travel</td>
</tr>
<tr>
<td>Booking.com</td>
<td>Shopping</td>
<td>Travel</td>
</tr>
<tr>
<td>Ticketmaster</td>
<td>Shopping</td>
<td>Entertainment &amp; Events</td>
</tr>
<tr>
<td>Airbnb</td>
<td>Shopping</td>
<td>Travel</td>
</tr>
<tr>
<td>DoorDash</td>
<td>Shopping</td>
<td>Food &amp; Drink</td>
</tr>
<tr>
<td>Expedia</td>
<td>Shopping</td>
<td>Travel</td>
</tr>
<tr>
<td>EasyPark</td>
<td>Shopping</td>
<td>Travel</td>
</tr>
<tr>
<td>UEFA Tickets</td>
<td>Shopping</td>
<td>Entertainment &amp; Events</td>
</tr>
<tr>
<td>DHL Express</td>
<td>Shopping</td>
<td>Business</td>
</tr>
<tr>
<td>UPS</td>
<td>Shopping</td>
<td>Business</td>
</tr>
</tbody>
</table>
<p>For more information on creating HTTP policies, refer to <a href="/cloudflare-one/traffic-policies/application-app-types/">Applications and app types</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-05">Nov 5, 2025</time><div>
<h2 id="post-2025-11-05-d1-jurisdiction"><a href="/changelog/post/2025-11-05-d1-jurisdiction/">D1 can restrict data localization with jurisdictions</a></h2>
<div class="changelog-badges"><span>d1</span><span>workers</span></div><div class="changelog-body"><p>You can now set a <a href="/d1/configuration/data-location/">jurisdiction</a> when creating a D1 database to guarantee where your database runs and stores data. Jurisdictions can help you comply with data localization regulations such as GDPR. Supported jurisdictions include <code>eu</code> and <code>fedramp</code>.</p>
<p>A jurisdiction can only be set at database creation time via wrangler, REST API or the UI and cannot be added/updated after the database already exists.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler@latest d1 create db-with-jurisdiction --jurisdiction eu&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/d1/database&quot; \&#10;     &#45;H &quot;Authorization: Bearer $TOKEN&quot; \&#10;     &#45;H &quot;Content-Type: application/json&quot; \&#10;     &#45;-data &#x27;{&quot;name&quot;: &quot;db-with-jurisdiction&quot;, &quot;jurisdiction&quot;: &quot;eu&quot; }&#x27;&#10;</code></pre>
<p>To learn more, visit D1's data location <a href="/d1/configuration/data-location/">documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-05">Nov 5, 2025</time><div>
<h2 id="post-2025-11-05-logpush-permissions-update"><a href="/changelog/post/2025-11-05-logpush-permissions-update/">Logpush Permission Update for Zero Trust Datasets</a></h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p><a href="/logs/logpush/permissions/">Permissions</a> for managing Logpush jobs related to <a href="/logs/logpush/logpush-job/datasets/account/">Zero Trust datasets</a> (Access, Gateway, and DEX) have been updated to improve data security and enforce appropriate access controls.</p>
<p>To view, create, update, or delete Logpush jobs for Zero Trust datasets, users must now have both of the following permissions:</p>
<ul>
<li>Logs Edit</li>
<li>Zero Trust: PII Read</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17738.md")</aside>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-05">Nov 5, 2025</time><div>
<h2 id="post-2025-11-05-emergency-waf-release"><a href="/changelog/post/2025-11-05-emergency-waf-release/">WAF Release - 2025-11-05 - Emergency</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s emergency release introduces a new detection signature that enhances coverage for a critical vulnerability in the React Native Metro Development Server, tracked as CVE-2025-11953.</p>
<p><strong>Key Findings</strong></p>
<p>The Metro Development Server exposes an HTTP endpoint that is vulnerable to OS command injection (CWE-78). An unauthenticated network attacker can send a crafted request to this endpoint and execute arbitrary commands on the host running Metro. The vulnerability affects Metro/cli-server-api builds used by React Native Community CLI in pre-patch development releases.</p>
<p><strong>Impact</strong></p>
<p>Successful exploitation of CVE-2025-11953 may result in remote command execution on developer workstations or CI/build agents, leading to credential and secret exposure, source tampering, and potential lateral movement into internal networks. Administrators and developers are strongly advised to apply the vendor's patches and restrict Metro’s network exposure to reduce this risk.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="db6b9e1ac1494971ae8c70aac8e30c5b">c8e30c5b</code>
</td>
<td>N/A</td>
<td>React Native Metro - Command Injection - CVE:CVE-2025-11953</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-05">Nov 5, 2025</time><div>
<h2 id="post-2025-09-25-workers-vpc"><a href="/changelog/post/2025-09-25-workers-vpc/">Announcing Workers VPC Services (Beta)</a></h2>
<div class="changelog-badges"><span>workers-vpc</span></div><div class="changelog-body"><p><strong>Workers VPC Services</strong> is now available, enabling your Workers to securely access resources in your private networks, without having to expose them on the public Internet.</p>
<h4 id="2025-09-25-workers-vpc-what-s-new">What's new</h4>
<ul>
<li><strong>VPC Services</strong>: Create secure connections to internal APIs, databases, and services using familiar Worker binding syntax</li>
<li><strong>Multi-cloud Support</strong>: Connect to resources in private networks in any external cloud (AWS, Azure, GCP, etc.) or on-premise using Cloudflare Tunnels</li>
</ul>
<pre tabindex="0"><code class="language-js">export default {&#10;	async fetch(request, env, ctx) {&#10;		// Perform application logic in Workers here&#10;&#10;		// Sample call to an internal API running on ECS in AWS using the binding&#10;		const response = await env.AWS_VPC_ECS_API.fetch(&quot;https://internal-host.example.com&quot;);&#10;&#10;		// Additional application logic in Workers&#10;		return new Response();&#10;	},&#10;};&#10;</code></pre>
<h4 id="2025-09-25-workers-vpc-getting-started">Getting started</h4>
<p>Set up a Cloudflare Tunnel, create a VPC Service, add service bindings to your Worker, and access private resources securely. <a href="/workers-vpc/">Refer to the documentation</a> to get started.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-04">Nov 4, 2025</time><div>
<h2 id="post-2025-11-04-query-cancellation"><a href="/changelog/post/2025-11-04-query-cancellation/">Log Explorer now supports query cancellation</a></h2>
<div class="changelog-badges"><span>log-explorer</span></div><div class="changelog-body"><p>We're excited to announce that Log Explorer users can now cancel queries that are currently running.</p>
<p>This new feature addresses a common pain point: waiting for a long, unintended, or misconfigured query to complete before you can submit a new, correct one. With query cancellation, you can immediately stop the execution of any undesirable query, allowing you to quickly craft and submit a new query, significantly improving your investigative workflow and productivity within Log Explorer.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-04">Nov 4, 2025</time><div>
<h2 id="post-2025-11-13-query-result-distribution"><a href="/changelog/post/2025-11-13-query-result-distribution/">Log Explorer now shows query result distribution</a></h2>
<div class="changelog-badges"><span>log-explorer</span></div><div class="changelog-body"><p>We're excited to announce a new feature in Log Explorer that significantly enhances how you analyze query results: the Query results distribution chart.</p>
<p>This new chart provides a graphical distribution of your results over the time window of the query. Immediately after running a query, you will see the distribution chart above your result table. This visualization allows Log Explorer users to quickly spot trends, identify anomalies, and understand the temporal concentration of log events that match their criteria. For example, you can visually confirm if a spike in traffic or errors occurred at a specific time, allowing you to focus your investigation efforts more effectively. This feature makes it faster and easier to extract meaningful insights from your vast log data.</p>
<p>The chart will dynamically update to reflect the logs matching your current query.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-11-03">Nov 3, 2025</time><div>
<h2 id="post-2025-11-03-waf-release"><a href="/changelog/post/2025-11-03-waf-release/">WAF Release - 2025-11-03</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week highlights enhancements to detection signatures improving coverage for vulnerabilities in Adobe Commerce and Magento Open Source, linked to CVE-2025-54236.</p>
<p><strong>Key Findings</strong></p>
<p>This vulnerability allows unauthenticated attackers to take over customer accounts through the Commerce REST API and, in certain configurations, may lead to remote code execution. The latest update provides enhanced detection logic for resilient protection against exploitation attempts.</p>
<p><strong>Impact</strong></p>
<ul>
<li>Adobe Commerce (CVE-2025-54236): Exploitation may allow attackers to hijack sessions, execute arbitrary commands, steal data, and disrupt storefronts, resulting in confidentiality and integrity risks for merchants. Administrators are strongly encouraged to apply vendor patches without delay.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="f5295d8333b7428c816654d8cb6d5fe5">cb6d5fe5</code>
</td>
<td>100774C</td>
<td>Adobe Commerce - Remote Code Execution - CVE:CVE-2025-54236</td>
<td>Log</td>
<td>Block</td>
<td>This is an improved detection.</td>
</tr>
</tbody>
</table>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/30/">Previous</a><span>Page 31 of 50</span><a class="pagination-next" rel="next" href="/changelog/32/">Next</a></nav>
</div>
