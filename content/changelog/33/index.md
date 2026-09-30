<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2025-10-18">Oct 18, 2025</time><div>
<h2 id="post-2025-10-16-on-demand-security-report"><a href="/changelog/post/2025-10-16-on-demand-security-report/">On-Demand Security Report</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>You can now generate on-demand security reports directly from the Cloudflare dashboard. This new feature provides a comprehensive overview of your email security posture, making it easier than ever to demonstrate the value of Cloudflare’s Email security to executives and other decision makers.</p>
<p>These reports offer several key benefits:</p>
<ul>
<li><strong>Executive Summary:</strong> Quickly view the performance of Email security with a high-level executive summary.</li>
<li><strong>Actionable Insights:</strong> Dive deep into trend data, breakdowns of threat types, and analysis of top targets to identify and address vulnerabilities.</li>
<li><strong>Configuration Transparency:</strong> Gain a clear view of your policy, submission, and domain configurations to ensure optimal setup.</li>
<li><strong>Account Takeover Risks:</strong> Get a snapshot of your M365 risky users (requires a Microsoft Entra ID P2 license and <a href="https://developers.cloudflare.com/cloudflare-one/integrations/cloud-and-saas/microsoft-365/">M365 SaaS integration</a>).</li>
</ul>
<p>To get started, refer to <a href="/cloudflare-one/email-security/monitoring/download-report/#download-a-security-report">Download a security report</a>.
<img src="/assets/upstream/images/changelog/email-security/report.png" alt="Report" /></p>
<p>This feature is available across the following Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-17">Oct 17, 2025</time><div>
<h2 id="post-2025-10-17-app-sec-reports"><a href="/changelog/post/2025-10-17-app-sec-reports/">New Application Security reports (Closed Beta)</a></h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p>Cloudflare's new <strong>Application Security report</strong>, currently in Closed Beta, is now available in the dashboard.</p>
<div class="nb-dash-button"></div>
<p>The reports are generated monthly and provide cyber security insights trends for all of the Enterprise zones in your Cloudflare account.</p>
<p>The reports also include an industry benchmark, comparing your cyber security landscape to peers in your industry.</p>
<p><img src="/assets/upstream/images/changelog/security-center/2025-10-17-application-security-report-mock-data.png" alt="Application Security report mock data" /></p>
<p>Learn more about the reports by referring to the <a href="/analytics/account-and-zone-analytics/app-security-reports/">Security Reports documentation</a>.</p>
<p>Use the feedback survey link at the top of the page to help us improve the reports.</p>
<p><img src="/assets/upstream/images/changelog/security-center/2025-10-17-report-feedback-survey.png" alt="Application Security report survey" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-17">Oct 17, 2025</time><div>
<h2 id="post-2025-10-17-emergency-waf-release"><a href="/changelog/post/2025-10-17-emergency-waf-release/">New detections released for WAF managed rulesets</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week we introduced several new detections across Cloudflare Managed Rulesets, expanding coverage for high-impact vulnerability classes such as SSRF, SQLi, SSTI, Reverse Shell attempts, and Prototype Pollution. These rules aim to improve protection against attacker-controlled payloads that exploit misconfigurations or unvalidated input in web applications.</p>
<p><strong>Key Findings</strong></p>
<p>New detections added for multiple exploit categories:</p>
<p>SSRF (Server-Side Request Forgery) — new rules targeting both local and cloud metadata abuse patterns (Beta).</p>
<p>SQL Injection (SQLi) — rules for common patterns, sleep/time-based injections, and string/wait function exploitation across headers and URIs.</p>
<p>SSTI (Server-Side Template Injection) — arithmetic-based probe detections introduced across URI, header, and body fields.</p>
<p>Reverse Shell and XXE payloads — enhanced heuristics for command execution and XML external entity misuse.</p>
<p>Prototype Pollution — new Beta rule identifying common JSON payload structures used in object prototype poisoning.</p>
<p>PHP Wrapper Injection and HTTP Parameter Pollution detections — to catch path traversal and multi-parameter manipulation attempts.</p>
<p>Anomaly Header Checks — detecting CRLF injection attempts in header names.</p>
<p><strong>Impact</strong></p>
<p>These updates help detect multi-vector payloads that blend SSRF + RCE or SQLi + SSTI attacks, especially in cloud-hosted applications with exposed metadata endpoints or unsafe template rendering.</p>
<p>Prototype Pollution and HTTP parameter pollution rules address emerging JavaScript supply-chain exploitation patterns increasingly seen in real-world incidents.</p>
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
<td><code class="nb-rule-id" title="72f0ff933fb0492eb71cda50589f2a1d">589f2a1d</code></td>
<td>N/A</td>
<td>Anomaly:Header - name - CR, LF</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="5d0377e4435f467488614170132fab7e">132fab7e</code></td>
<td>N/A</td>
<td>Generic Rules - Reverse Shell - Body</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="54e32f7f802c4a699182e8921a027008">1a027008</code></td>
<td>N/A</td>
<td>Generic Rules - Reverse Shell - Header</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="7cbda8dbafbc465d9b64a8f2958d0486">958d0486</code></td>
<td>N/A</td>
<td>Generic Rules - Reverse Shell - URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="b9f3420674cf481da32333dc8e0cf7ad">8e0cf7ad</code></td>
<td>N/A</td>
<td>Generic Rules - XXE - Body</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="ad55483512f0440b81426acdbf8aab5e">bf8aab5e</code></td>
<td>N/A</td>
<td>Generic Rules - SQLi - Common Patterns - Header URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="849c0618d1674f1c92ba6f9b2e466337">2e466337</code></td>
<td>N/A</td>
<td>Generic Rules - SQLi - Sleep Function - Header URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="1b4db4c4bd0649c095c27c6cb686ab47">b686ab47</code></td>
<td>N/A</td>
<td>Generic Rules - SQLi - String Function - Header URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="fa2055b84af94ba4b925f834b0633709">b0633709</code></td>
<td>N/A</td>
<td>Generic Rules - SQLi - WaitFor Function - Header URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="158177dec2504acdba1f2da201a076eb">01a076eb</code></td>
<td>N/A</td>
<td>SSRF - Local - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="98bfd6bb46074d5b8d1c4b39743a63ec">743a63ec</code></td>
<td>N/A</td>
<td>SSRF - Local - 2 - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="54e1733b10da4a599e06c6fbc2e84e2d">c2e84e2d</code></td>
<td>N/A</td>
<td>SSRF - Cloud - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="ecd26d61a75e46f6a4449a06ab8af26f">ab8af26f</code></td>
<td>N/A</td>
<td>SSRF - Cloud - 2 - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="c16f4e133c4541f293142d02e6e8dc5b">e6e8dc5b</code></td>
<td>N/A</td>
<td>SSTI - Arithmetic Probe - URI</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="f4fd9904e7624666b8c49cd62550d794">2550d794</code></td>
<td>N/A</td>
<td>SSTI - Arithmetic Probe - Header</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="5c0875604f774c36a4f9b69c659d12a6">659d12a6</code></td>
<td>N/A</td>
<td>SSTI - Arithmetic Probe - Body</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="fae6fa37ae9249d58628e54b1a3e521e">1a3e521e</code></td>
<td>N/A</td>
<td>PHP Wrapper Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="9c02e585db34440da620eb668f76bd74">8f76bd74</code></td>
<td>N/A</td>
<td>PHP Wrapper Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="cb67fe56a84747b8b64277dc091e296d">091e296d</code></td>
<td>N/A</td>
<td>HTTP parameter pollution</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td><code class="nb-rule-id" title="443b54d984944cd69043805ee34214ef">e34214ef</code></td>
<td>N/A</td>
<td>Prototype Pollution - Common Payloads - Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-17">Oct 17, 2025</time><div>
<h2 id="post-2025-10-16-warp-macos-beta"><a href="/changelog/post/2025-10-16-warp-macos-beta/">WARP client for macOS (version 2025.9.173.1)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new Beta release for the macOS WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This release contains minor fixes, improvements, and new features including Path Maximum Transmission Unit Discovery (PMTUD). With PMTUD enabled, the client will dynamically adjust packet sizing to optimize connection performance. There is also a new connection status message in the GUI to inform users that the local network connection may be unstable. This will make it easier to debug connectivity issues.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>The GUI now displays the health of the tunnel and DNS connections by showing a connection status message when the network may be unstable. This will make it easier to debug connectivity issues.</li>
<li>Deleting registrations no longer returns an error when succeeding.</li>
<li>Path Maximum Transmission Unit Discovery (PMTUD) is now used to discover the effective MTU of the connection. This allows the client to improve connection performance optimized for the current network.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>macOS Sequoia: Due to changes Apple introduced in macOS 15.0.x, the WARP client may not behave as expected. Cloudflare recommends the use of macOS 15.4 or later.</li>
<li>Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server">Route traffic to fallback server</a>.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-17">Oct 17, 2025</time><div>
<h2 id="post-2025-10-16-warp-windows-beta"><a href="/changelog/post/2025-10-16-warp-windows-beta/">WARP client for Windows (version 2025.9.173.1)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new Beta release for the Windows WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This release contains minor fixes, improvements, and new features including Path Maximum Transmission Unit Discovery (PMTUD). With PMTUD enabled, the client will dynamically adjust packet sizing to optimize connection performance. There is also a new connection status message in the GUI to inform users that the local network connection may be unstable. This will make it easier to debug connectivity issues.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Improvements for <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-multiuser/">Windows multi-user</a> to maintain the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#disconnect-warp-on-all-devices">Global WARP override</a> state when switching between users.</li>
<li>The GUI now displays the health of the tunnel and DNS connections by showing a connection status message when the network may be unstable. This will make it easier to debug connectivity issues.</li>
<li>Deleting registrations no longer returns an error when succeeding.</li>
<li>Path Maximum Transmission Unit Discovery (PMTUD) is now used to discover the effective MTU of the connection. This allows the client to improve connection performance optimized for the current network.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>
<p>For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum <a href="https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd">Windows 11 24H2 KB5062553</a> or higher for resolution.</p>
</li>
<li>
<p>Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server">Route traffic to fallback server</a>.</p>
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
<time datetime="2025-10-16">Oct 16, 2025</time><div>
<h2 id="post-2025-10-16-durable-objects-data-studio"><a href="/changelog/post/2025-10-16-durable-objects-data-studio/">View and edit Durable Object data in UI with Data Studio (Beta)</a></h2>
<div class="changelog-badges"><span>durable-objects</span><span>workers</span></div><div class="changelog-body"><p><img src="/assets/upstream/images/workers/changelog/do-data-studio.png" alt="Screenshot of Durable Objects Data Studio" /></p>
<p>You can now view and write to each Durable Object's storage using a UI editor on the Cloudflare dashboard. Only Durable Objects using <a href="/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class">SQLite storage</a> can use Data Studio.</p>
<div class="nb-dash-button"></div>
<p>Data Studio unlocks easier data access with Durable Objects for prototyping application data models to debugging production storage usage. Before, querying your Durable Objects data required deploying a Worker.</p>
<p>To access a Durable Object, you can provide an object's unique name or ID generated by Cloudflare. Data Studio requires you to have at least the <code>Workers Platform Admin</code> role, and all queries are captured with audit logging for your security and compliance needs. Queries executed by Data Studio send requests to your remote, deployed objects and incur normal usage billing.</p>
<p>To learn more, visit the Data Studio <a href="/durable-objects/observability/data-studio/">documentation</a>. If you have feedback or suggestions for the new Data Studio, please share your experience on <a href="https://discord.com/channels/595317990191398933/773219443911819284">Discord</a></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-16">Oct 16, 2025</time><div>
<h2 id="post-2025-10-16-header-limit-increase"><a href="/changelog/post/2025-10-16-header-limit-increase/">Increased HTTP header size limit to 128 KB</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><h4 id="2025-10-16-header-limit-increase-cdn-now-supports-128-kb-request-and-response-headers">CDN now supports 128 KB request and response headers 🚀</h4>
<p>We're excited to announce a significant increase in the maximum header size supported by Cloudflare's Content Delivery Network (CDN). Cloudflare now supports up to <strong>128 KB</strong> for both <strong>request and response headers</strong>.</p>
<p>Previously, customers were limited to a total of 32 KB for request or response headers, with a maximum of 16 KB per individual header. Larger headers could cause requests to fail with <code>HTTP 413</code> (Request Header Fields Too Large) errors.</p>
<hr />
<h4 id="2025-10-16-header-limit-increase-what-s-new">What's new?</h4>
<ul>
<li><strong>Support for large headers:</strong> You can now utilize much larger headers, whether as a single large header up to 128 KB or split over multiple headers.</li>
<li><strong>Reduces <code>413</code> and <code>520</code> HTTP errors:</strong> This change drastically reduces the likelihood of customers encountering <code>HTTP 413</code> errors from large request headers or <code>HTTP 520</code> errors caused by oversized response headers, improving the overall reliability of your web applications.</li>
<li><strong>Enhanced functionality:</strong> This is especially beneficial for applications that rely on:
<ul>
<li>A large number of cookies.</li>
<li>Large Content-Security-Policy (CSP) response headers.</li>
<li>Advanced use cases with Cloudflare Workers that generate large response headers.</li>
</ul>
</li>
</ul>
<p>This enhancement improves compatibility with Cloudflare's CDN, enabling more use cases that previously failed due to header size limits.</p>
<hr />
<p>To learn more and get started, refer to the <a href="/fundamentals/reference/connection-limits/#request-limits">Cloudflare Fundamentals documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-16">Oct 16, 2025</time><div>
<h2 id="post-2025-08-15-monitor-groups-for-load-balancing"><a href="/changelog/post/2025-08-15-monitor-groups-for-load-balancing/">Monitor Groups for Advanced Health Checking With Load Balancing</a></h2>
<div class="changelog-badges"><span>load-balancing</span></div><div class="changelog-body"><p>Cloudflare Load Balancing now supports Monitor Groups, a powerful new way to combine multiple health monitors into a single, logical group. This allows you to create sophisticated health checks that more accurately reflect the true availability of your applications by assessing multiple services at once.</p>
<p>With Monitor Groups, you can ensure that all critical components of an application are healthy before sending traffic to an origin pool, enabling smarter failover decisions and greater resilience. This feature is now available via the API for customers with an Enterprise Load Balancing subscription.</p>
<h4 id="2025-08-15-monitor-groups-for-load-balancing-what-you-can-do">What you can do:</h4>
<ul>
<li><strong>Combine Multiple Monitors</strong>: Group different health monitors (for example, HTTP, TCP) that check various application components, like a primary API gateway and a specific <code>/login</code> service.</li>
<li><strong>Isolate Monitors for Observation</strong>: Mark a monitor as &quot;monitoring only&quot; to receive alerts and data without it affecting a pool's health status or traffic steering. This is perfect for testing new checks or observing non-critical dependencies.</li>
<li><strong>Improve Steering Intelligence</strong>: Latency for Dynamic Steering is automatically averaged across all active monitors in a group, providing a more holistic view of an origin's performance.</li>
</ul>
<p>This enhancement is ideal for complex, multi-service applications where the health of one component depends on another. By aggregating health signals, Monitor Groups provide a more accurate and comprehensive assessment of your application's true status.</p>
<p>For detailed information and API configuration guides, please visit our <a href="/load-balancing/monitors/monitor-groups">developer documentation</a> for Monitor Groups.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-14">Oct 14, 2025</time><div>
<h2 id="post-2025-10-14-enhanced-metrics-drilldowns"><a href="/changelog/post/2025-10-14-enhanced-metrics-drilldowns/">Enhanced AI Crawl Control metrics with new drilldowns and filters</a></h2>
<div class="changelog-badges"><span>ai-crawl-control</span></div><div class="changelog-body"><p>AI Crawl Control now provides enhanced metrics and CSV data exports to help you better understand AI crawler activity across your sites.</p>
<h4 id="2025-10-14-enhanced-metrics-drilldowns-what-s-new">What's new</h4>
<h4 id="2025-10-14-enhanced-metrics-drilldowns-track-crawler-requests-over-time">Track crawler requests over time</h4>
<p>Visualize crawler activity patterns over time, and group data by different dimensions:</p>
<ul>
<li><strong>By Crawler</strong> — Track activity from individual AI crawlers (GPTBot, ClaudeBot, Bytespider)</li>
<li><strong>By Category</strong> — Analyze crawler purpose or type</li>
<li><strong>By Operator</strong> — Discover which companies (OpenAI, Anthropic, ByteDance) are crawling your site</li>
<li><strong>By Host</strong> — Break down activity across multiple subdomains</li>
<li><strong>By Status Code</strong> — Monitor HTTP response codes to crawlers (200s, 300s, 400s, 500s)</li>
</ul>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-requests-over-time.png" alt="AI Crawl Control requests over time chart with grouping tabs" title="Interactive chart showing crawler requests over time with filterable dimensions" /></p>
<h4 id="2025-10-14-enhanced-metrics-drilldowns-analyze-referrer-data-paid-plans">Analyze referrer data (Paid plans)</h4>
<p>Identify traffic sources with referrer analytics:</p>
<ul>
<li>View top referrers driving traffic to your site</li>
<li>Understand discovery patterns and content popularity from AI operators</li>
</ul>
<p><img src="/assets/upstream/images/ai-crawl-control/ai-crawl-control-top-referrers.png" alt="AI Crawl Control top referrers breakdown" title="Bar chart showing top referrers and their respective traffic volumes" /></p>
<h4 id="2025-10-14-enhanced-metrics-drilldowns-export-data">Export data</h4>
<p>Download your filtered view as a CSV:</p>
<ul>
<li>Includes all applied filters and groupings</li>
<li>Useful for custom reporting and deeper analysis</li>
</ul>
<h4 id="2025-10-14-enhanced-metrics-drilldowns-get-started">Get started</h4>
<ol>
<li>Log in to the Cloudflare dashboard, and select your account and domain.</li>
<li>Go to <strong>AI Crawl Control</strong> &gt; <strong>Metrics</strong>.</li>
<li>Use the grouping tabs to explore different views of your data.</li>
<li>Apply filters to focus on specific crawlers, time ranges, or response codes.</li>
<li>Select <strong>Download CSV</strong> to export your filtered data for further analysis.</li>
</ol>
<p>Learn more about <a href="/ai-crawl-control">AI Crawl Control</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-14">Oct 14, 2025</time><div>
<h2 id="post-2025-10-14-sso-self-service-ux"><a href="/changelog/post/2025-10-14-sso-self-service-ux/">Single sign-on now manageable in the user experience</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p><img src="/assets/upstream/images/changelog/fundamentals/2025-10-14-sso-configuration-ux.png" alt="Screenshot of new user experience for managing SSO" /></p>
<p>During Birthday Week, we announced that <a href="https://blog.cloudflare.com/enterprise-grade-features-for-all/">single sign-on (SSO) is available for free</a> to everyone who signs in with a custom email domain and maintains a compatible <a href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/">identity provider</a>. SSO minimizes user friction around login and provides the strongest security posture available. At the time, this could only be configured using the API.</p>
<p>Today, we are launching a new user experience which allows users to manage their SSO configuration from within the Cloudflare dashboard. You can access this by going to <strong>Manage account</strong> &gt; <strong>Members</strong> &gt; <strong>Settings</strong>.</p>
<h4 id="2025-10-14-sso-self-service-ux-for-more-information">For more information</h4>
<ul>
<li><a href="/fundamentals/manage-members/dashboard-sso/">Cloudflare dashboard SSO</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-13">Oct 13, 2025</time><div>
<h2 id="post-2025-10-13-waf-release"><a href="/changelog/post/2025-10-13-waf-release/">WAF Release - 2025-10-13</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s highlights include a new JinJava rule targeting a sandbox-bypass flaw that could allow malicious template input to escape execution controls. The rule improves detection for unsafe template rendering paths.</p>
<p><strong>Key Findings</strong></p>
<p>New WAF rule deployed for JinJava (CVE-2025-59340) to block a sandbox bypass in the template engine that permits attacker-controlled type construction and arbitrary class instantiation; in vulnerable environments this can escalate to remote code execution and full server compromise.</p>
<p><strong>Impact</strong></p>
<ul>
<li>CVE-2025-59340 — Exploitation enables attacker-supplied type descriptors / Jackson <code>ObjectMapper</code> abuse, allowing arbitrary class loading, file/URL access (LFI/SSRF primitives) and, with suitable gadget chains, potential remote code execution and system compromise.</li>
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
				<code class="nb-rule-id" title="b327d6442e2d4848b4aab3cbc04bab5f">c04bab5f</code>
</td>
<td>100892</td>
<td>JinJava - SSTI - CVE:CVE-2025-59340</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-10">Oct 10, 2025</time><div>
<h2 id="post-2025-10-10-new-domain-categories"><a href="/changelog/post/2025-10-10-new-domain-categories/">New domain categories added</a></h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>We have added three new domain categories under the Technology parent category, to better reflect online content and improve DNS filtering.</p>
<p><strong>New categories added</strong></p>
<table>
<thead>
<tr>
<th>Parent ID</th>
<th>Parent Name</th>
<th>Category ID</th>
<th>Category Name</th>
</tr>
</thead>
<tbody>
<tr>
<td>26</td>
<td>Technology</td>
<td>194</td>
<td>Keep Awake Software</td>
</tr>
<tr>
<td>26</td>
<td>Technology</td>
<td>192</td>
<td>Remote Access</td>
</tr>
<tr>
<td>26</td>
<td>Technology</td>
<td>193</td>
<td>Shareware/Freeware</td>
</tr>
</tbody>
</table>
<p>Refer to <a href="/cloudflare-one/traffic-policies/domain-categories/">Gateway domain categories</a> to learn more.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-10">Oct 10, 2025</time><div>
<h2 id="post-2025-10-10-increased-startup-time"><a href="/changelog/post/2025-10-10-increased-startup-time/">Worker startup time limit increased to 1 second</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now upload a Worker that takes up 1 second to parse and execute its global scope. Previously, startup time was limited to 400 ms.</p>
<p>This allows you to run Workers that import more complex packages and execute more code prior to requests being handled.</p>
<p>For more information, see the documentation on <a href="/workers/platform/limits/#worker-startup-time">Workers startup limits</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-09">Oct 9, 2025</time><div>
<h2 id="post-2025-10-09-radar-ct-log-activity-insights"><a href="/changelog/post/2025-10-09-radar-ct-log-activity-insights/">Expanded CT log activity insights on Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> has expanded its Certificate Transparency (CT) log insights with new stats that provide greater visibility into log activity:</p>
<ul>
<li><strong>Log growth rate</strong>: The average throughput of the CT log over the past 7 days, measured in certificates per hour.</li>
<li><strong>Included certificate count</strong>: The total number of certificates already included in this CT log.</li>
<li><strong>Eligible-for-inclusion certificate count</strong>: The number of certificates eligible for inclusion in this log but not yet included. This metric is based on certificates signed by trusted root CAs within the log’s accepted date range.</li>
<li><strong>Last update</strong>: The timestamp of the most recent update to the CT log.</li>
</ul>
<p>These new statistics have been added to the response of the <a href="/api/resources/radar/subresources/ct/subresources/logs/methods/get/">Get Certificate Log Details</a> API endpoint, and are displayed on the <a href="https://radar.cloudflare.com/certificate-transparency/log/nimbus2025#log-activity">CT log information page</a>.</p>
<p><img src="/assets/upstream/images/radar/ct-log-activity.png" alt="Screenshot of the CT log activity card on the CT log information page" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-09">Oct 9, 2025</time><div>
<h2 id="post-2025-10-09-assets-terraform"><a href="/changelog/post/2025-10-09-assets-terraform/">You can now deploy full-stack apps on Workers using Terraform</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now upload Workers with <a href="/workers/static-assets/">static assets</a> (like HTML, CSS, JavaScript, images) with the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs">Cloudflare Terraform provider v5.11.0</a>, making it even easier to deploy and manage full-stack apps with IaC.</p>
<p><strong>Previously</strong>, you couldn't use Terraform to upload static assets without writing custom scripts to handle generating an <a href="/workers/static-assets/direct-upload/#upload-manifest">asset manifest</a>, calling the <a href="/workers/static-assets/direct-upload/#upload-static-assets">Cloudflare API to upload assets in chunks</a>, and handling change detection.</p>
<p><strong>Now</strong>, you simply define the directory where your assets are built, and we handle the rest. Check out the <a href="/changelog/#examples">examples</a> for what this looks like in Terraform configuration.</p>
<p>You can get started today with <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs">the Cloudflare Terraform provider (v5.11.0)</a>, using either the existing <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script"><code>cloudflare_workers_script</code> resource</a>, or the beta <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker_version"><code>cloudflare_worker_version</code> resource</a>.</p>
<h4 id="2025-10-09-assets-terraform-examples">Examples</h4>
<h4 id="2025-10-09-assets-terraform-with-cloudflare-workers-script">With <code>cloudflare_workers_script</code></h4>
<p>Here's how you can use the existing <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/workers_script"><code>cloudflare_workers_script</code></a> resource to upload your Worker code and assets in one shot.</p>
<pre><code class="language-hcl">resource &quot;cloudflare_workers_script&quot; &quot;my_app&quot; {&#10;  account_id  = var.account_id&#10;  script_name = &quot;my-app&quot;&#10;&#10;  content_file   = &quot;./dist/worker/index.js&quot;&#10;  content_sha256 = filesha256(&quot;./dist/worker/index.js&quot;)&#10;  main_module    = &quot;index.js&quot;&#10;&#10;  &#35; Just point to your assets directory - that&#x27;s it!&#10;  assets = {&#10;    directory = &quot;./dist/static&quot;&#10;  }&#10;}&#10;</code></pre>
<h4 id="2025-10-09-assets-terraform-with-cloudflare-worker-cloudflare-worker-version-and-cloudflare-workers-deployment">With <code>cloudflare_worker</code>, <code>cloudflare_worker_version</code>, and <code>cloudflare_workers_deployment</code></h4>
<p>And here's an example using the beta <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/worker_version"><code>cloudflare_worker_version</code></a> resource, alongside the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker"><code>cloudflare_worker</code></a> and <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/workers_deployment"><code>cloudflare_workers_deployment</code></a> resources:</p>
<pre><code class="language-hcl">&#10;&#35; This tracks the existence of your Worker, so that you&#10;&#35; can upload code and assets separately from tracking Worker state.&#10;&#10;resource &quot;cloudflare_worker&quot; &quot;my_app&quot; {&#10;  account_id = var.account_id&#10;  name       = &quot;my-app&quot;&#10;}&#10;&#10;resource &quot;cloudflare_worker_version&quot; &quot;my_app_version&quot; {&#10;  account_id = var.account_id&#10;  worker_id  = cloudflare_worker.my_app.id&#10;&#10;  &#35; Just point to your assets directory - that&#x27;s it!&#10;  assets = {&#10;    directory = &quot;./dist/static&quot;&#10;  }&#10;&#10;  modules = [{&#10;    name         = &quot;index.js&quot;&#10;    content_file = &quot;./dist/worker/index.js&quot;&#10;    content_type = &quot;application/javascript+module&quot;&#10;  }]&#10;}&#10;&#10;resource &quot;cloudflare_workers_deployment&quot; &quot;my_app_deployment&quot; {&#10;  account_id  = var.account_id&#10;  script_name = cloudflare_worker.my_app.name&#10;&#10;  strategy = &quot;percentage&quot;&#10;  versions = [{&#10;    version_id = cloudflare_worker_version.my_app_version.id&#10;    percentage = 100&#10;  }]&#10;}&#10;</code></pre>
<h4 id="2025-10-09-assets-terraform-what-s-changed">What's changed</h4>
Under the hood, the Cloudflare Terraform provider now handles the same logic that Wrangler uses for static asset uploads. This includes scanning your assets directory, computing hashes for each file, generating a manifest with file metadata, and calling the Cloudflare API to upload any missing files in chunks. We support large directories with parallel uploads and chunking, and when the asset manifest hash changes, we detect what's changed and trigger an upload for *only* those changed files.
<h4 id="2025-10-09-assets-terraform-try-it-out">Try it out</h4>
-  Get started with [the Cloudflare Terraform provider (v5.11.0)](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs)
- You can use either the existing [`cloudflare_workers_script` resource](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script) to upload your Worker code and assets in one resource.
- Or you can use the new beta [`cloudflare_worker_version` resource](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker_version) (along with the [`cloudflare_worker`](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker) and [`cloudflare_workers_deployment`](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/workers_deployment)) resources to more granularly control the lifecycle of each Worker resource.
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-09">Oct 9, 2025</time><div>
<h2 id="post-2025-10-09-workflows-terraform"><a href="/changelog/post/2025-10-09-workflows-terraform/">You can now deploy and manage Workflows in Terraform</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now create and manage <a href="/workflows/">Workflows</a> using Terraform, now supported in the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workflow">Cloudflare Terraform provider v5.11.0</a>. Workflows allow you to build durable, multi-step applications -- without needing to worry about retrying failed tasks or managing infrastructure.</p>
<p>Now, you can deploy and manage Workflows through Terraform using the new <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workflow"><code>cloudflare_workflow</code> resource</a>:</p>
<pre><code class="language-hcl">resource &quot;cloudflare_workflow&quot; &quot;my_workflow&quot; {&#10;  account_id    = var.account_id&#10;  workflow_name = &quot;my-workflow&quot;&#10;  class_name    = &quot;MyWorkflow&quot;&#10;  script_name   = &quot;my-worker&quot;&#10;}&#10;</code></pre>
<h4 id="2025-10-09-workflows-terraform-examples">Examples</h4>
Here are full examples of how to configure `cloudflare_workflow` in Terraform, using the existing [`cloudflare_workers_script` resource](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script), and the beta [`cloudflare_worker_version` resource](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker_version).
<h4 id="2025-10-09-workflows-terraform-with-cloudflare-workflow-and-cloudflare-workers-script">With <code>cloudflare_workflow</code> and <code>cloudflare_workers_script</code></h4>
<pre><code class="language-hcl">resource &quot;cloudflare_workers_script&quot; &quot;workflow_worker&quot; {&#10;  account_id  = var.cloudflare_account_id&#10;  script_name = &quot;my-workflow-worker&quot;&#10;&#10;  content_file   = &quot;${path.module}/../dist/worker/index.js&quot;&#10;  content_sha256 = filesha256(&quot;${path.module}/../dist/worker/index.js&quot;)&#10;  main_module    = &quot;index.js&quot;&#10;}&#10;&#10;resource &quot;cloudflare_workflow&quot; &quot;workflow&quot; {&#10;  account_id    = var.cloudflare_account_id&#10;  workflow_name = &quot;my-workflow&quot;&#10;  class_name    = &quot;MyWorkflow&quot;&#10;  script_name   = cloudflare_workers_script.workflow_worker.script_name&#10;}&#10;</code></pre>
<h4 id="2025-10-09-workflows-terraform-with-cloudflare-workflow-and-the-new-beta-resources">With <code>cloudflare_workflow</code>, and the new beta resources</h4>
You can more granularly control the lifecycle of each Worker resource using the beta [`cloudflare_worker_version`](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/worker_version) resource, alongside the [`cloudflare_worker`](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker) and [`cloudflare_workers_deployment`](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/workers_deployment) resources.
<pre><code class="language-hcl">&#10;resource &quot;cloudflare_worker&quot; &quot;workflow_worker&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  name       = &quot;my-workflow-worker&quot;&#10;}&#10;&#10;resource &quot;cloudflare_worker_version&quot; &quot;workflow_worker_version&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  worker_id  = cloudflare_worker.workflow_worker.id&#10;&#10;  main_module         = &quot;index.js&quot;&#10;&#10;  modules = [{&#10;    name         = &quot;index.js&quot;&#10;    content_file = &quot;${path.module}/../dist/worker/index.js&quot;&#10;    content_type = &quot;application/javascript+module&quot;&#10;  }]&#10;}&#10;&#10;resource &quot;cloudflare_workers_deployment&quot; &quot;workflow_deployment&quot; {&#10;  account_id  = var.cloudflare_account_id&#10;  script_name = cloudflare_worker.workflow_worker.name&#10;&#10;  strategy = &quot;percentage&quot;&#10;  versions = [{&#10;    version_id = cloudflare_worker_version.workflow_worker_version.id&#10;    percentage = 100&#10;  }]&#10;}&#10;&#10;resource &quot;cloudflare_workflow&quot; &quot;my_workflow&quot; {&#10;  account_id    = var.cloudflare_account_id&#10;  workflow_name = &quot;my-workflow&quot;&#10;  class_name    = &quot;MyWorkflow&quot;&#10;  script_name   = cloudflare_worker.workflow_worker.name&#10;}&#10;</code></pre>
<h4 id="2025-10-09-workflows-terraform-try-it-out">Try it out</h4>
-  Get started with [the Cloudflare Terraform provider (v5.11.0)](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs) and the new [`cloudflare_workflow` resource](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workflow).
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-08">Oct 8, 2025</time><div>
<h2 id="post-2025-10-07-warp-linux-ga"><a href="/changelog/post/2025-10-07-warp-linux-ga/">WARP client for Linux (version 2025.8.779.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Linux WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains significant fixes and improvements including an updated public key for Linux packages. The public key must be updated if it was installed before September 12, 2025 to ensure the repository remains functional after December 4, 2025. Instructions to make this update are available at <a href="https://pkg.cloudflareclient.com/">pkg.cloudflareclient.com</a>.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>
<p><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Proxy mode</a> has been enhanced for even faster resolution. Proxy mode now supports SOCKS4, SOCK5, and HTTP CONNECT over an L4 tunnel with custom congestion control optimizations instead of the previous L3 tunnel to Cloudflare's network. This has more than doubled Proxy mode throughput in lab speed testing, by an order of magnitude in some cases.</p>
</li>
<li>
<p>The MASQUE protocol is now the only protocol that can use <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Proxy mode</a>. If you previously configured a device profile to use Proxy mode with Wireguard, you will need to select a new WARP mode or switch to the MASQUE protocol. Otherwise, all devices matching the profile will lose connectivity.</p>
</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server">Route traffic to fallback server</a>.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-08">Oct 8, 2025</time><div>
<h2 id="post-2025-10-07-warp-macos-ga"><a href="/changelog/post/2025-10-07-warp-macos-ga/">WARP client for macOS (version 2025.8.779.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the macOS WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains significant fixes and improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>
<p><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Proxy mode</a> has been enhanced for even faster resolution. Proxy mode now supports SOCKS4, SOCK5, and HTTP CONNECT over an L4 tunnel with custom congestion control optimizations instead of the previous L3 tunnel to Cloudflare's network. This has more than doubled Proxy mode throughput in lab speed testing, by an order of magnitude in some cases.</p>
</li>
<li>
<p>The MASQUE protocol is now the only protocol that can use <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Proxy mode</a>. If you previously configured a device profile to use Proxy mode with Wireguard, you will need to select a new WARP mode or switch to the MASQUE protocol. Otherwise, all devices matching the profile will lose connectivity.</p>
</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>
<p>macOS Sequoia: Due to changes Apple introduced in macOS 15.0.x, the WARP client may not behave as expected. Cloudflare recommends the use of macOS 15.4 or later.</p>
</li>
<li>
<p>Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server">Route traffic to fallback server</a>.</p>
</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-08">Oct 8, 2025</time><div>
<h2 id="post-2025-10-07-warp-windows-ga"><a href="/changelog/post/2025-10-07-warp-windows-ga/">WARP client for Windows (version 2025.8.779.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Windows WARP client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains significant fixes and improvements.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>
<p><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Proxy mode</a> has been enhanced for even faster resolution. Proxy mode now supports SOCKS4, SOCK5, and HTTP CONNECT over an L4 tunnel with custom congestion control optimizations instead of the previous L3 tunnel to Cloudflare's network. This has more than doubled Proxy mode throughput in lab speed testing, by an order of magnitude in some cases.</p>
</li>
<li>
<p>The MASQUE protocol is now the only protocol that can use <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode">Proxy mode</a>. If you previously configured a device profile to use Proxy mode with Wireguard, you will need to select a new WARP mode or switch to the MASQUE protocol. Otherwise, all devices matching the profile will lose connectivity.</p>
</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>
<p>For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum <a href="https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd">Windows 11 24H2 KB5062553</a> or higher for resolution.</p>
</li>
<li>
<p>Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to <a href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server">Route traffic to fallback server</a>.</p>
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
<time datetime="2025-10-07">Oct 7, 2025</time><div>
<h2 id="post-2025-10-07-recovery-codes"><a href="/changelog/post/2025-10-07-recovery-codes/">Automated reminders for backup codes</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>The most common reason users contact Cloudflare support is lost two-factor authentication (2FA) credentials. Cloudflare supports both app-based and hardware keys for 2FA, but you could lose access to your account if you lose these. Over the past few weeks, we have been rolling out email and in-product reminders that remind you to also download backup codes (sometimes called recovery keys) that can get you back into your account in the event you lose your 2FA credentials. Download your backup codes now by logging into Cloudflare, then navigating to <strong>Profile</strong> &gt; <strong>Security &amp; Authentication</strong> &gt; <strong>Backup codes</strong>.</p>
<h4 id="2025-10-07-recovery-codes-sign-in-security-best-practices">Sign-in security best practices</h4>
<p>Cloudflare is critical infrastructure, and you should protect it as such. Please review the following best practices and make sure you are doing your part to secure your account.</p>
<ul>
<li>Use a unique password for every website, including Cloudflare, and store it in a password manager like 1Password or Keeper. These services are cross-platform and simplify the process of managing secure passwords.</li>
<li>Use 2FA to make it harder for an attacker to get into your account in the event your password is leaked</li>
<li>Store your backup codes securely. A password manager is the best place since it keeps the backup codes encrypted, but you can also print them and put them somewhere safe in your home.</li>
<li>If you use an app to manage your 2FA keys, enable cloud backup, so that you don't lose your keys in the event you lose your phone.</li>
<li>If you use a custom email domain to sign in, <a href="https://developers.cloudflare.com/fundamentals/manage-members/dashboard-sso/">configure SSO</a>.</li>
<li>If you use a public email domain like Gmail or Hotmail, you can also use social login with Apple, GitHub, or Google to sign in.</li>
<li>If you manage a Cloudflare account for work:
<ul>
<li>Have at least two administrators in case one of them unexpectedly leaves your company</li>
<li>Use SCIM to automate permissions management for members in your Cloudflare account</li>
</ul>
</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-07">Oct 7, 2025</time><div>
<h2 id="post-2025-10-07-emergency-waf-release"><a href="/changelog/post/2025-10-07-emergency-waf-release/">WAF Release - 2025-10-07 - Emergency</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week highlights multiple critical Cisco vulnerabilities (CVE-2025-20363, CVE-2025-20333, CVE-2025-20362). This flaw stems from improper input validation in HTTP(S) requests. An authenticated VPN user could send crafted requests to execute code as root, potentially compromising the device.
The initial two rules were made available on September 28, with a third rule added today, October 7, for more robust protection.</p>
<ul>
<li>Cisco (CVE-2025-20333, CVE-2025-20362, CVE-2025-20363): Multiple vulnerabilities that could allow attackers to exploit unsafe deserialization and input validation flaws. Successful exploitation may result in arbitrary code execution, privilege escalation, or command injection on affected systems.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Cisco (CVE-2025-20333, CVE-2025-20362, CVE-2025-20363): Exploitation enables attackers to escalate privileges or achieve remote code execution via command injection.
Administrators are strongly advised to apply vendor updates immediately.</p>
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
        <code class="nb-rule-id" title="12f808a5315441688f3b7c8a3a4d1bd6">3a4d1bd6</code>
</td>
<td>100788B</td>
<td>Cisco Secure Firewall Adaptive Security Appliance - Remote Code Execution - CVE:CVE-2025-20333, CVE:CVE-2025-20362, CVE:CVE-2025-20363</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-07">Oct 7, 2025</time><div>
<h2 id="post-2025-10-06-new-worker-overview-page"><a href="/changelog/post/2025-10-06-new-worker-overview-page/">New Overview Page for Cloudflare Workers</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><img src="/assets/upstream/images/workers/changelog/workers-overview.png" alt="Screenshot of the Workers overview page in the Cloudflare dashboard" /></p>
<p>Each of your Workers now has a new overview page in the Cloudflare dashboard.</p>
<p>The goal is to make it easier to understand your Worker without digging through multiple tabs. Think of it as a new home base, a place to get a high-level overview on what's going on.</p>
<p>It's the first place you land when you open a Worker in the dashboard, and it gives you an immediate view of what’s going on. You can see requests, errors, and CPU time at a glance. You can view and add bindings, and see recent versions of your app, including who published them.</p>
<p>Navigation is also simpler, with visually distinct tabs at the top of the page. At the bottom right you'll find guided steps for what to do next that are based on the state of your Worker, such as adding a <a href="/workers/runtime-apis/bindings/">binding</a> or connecting a custom domain.</p>
<p>We plan to add more here over time. Better insights, more controls, and ways to manage your Worker from one page.</p>
<p>If you have feedback or suggestions for the new Overview page or your Cloudflare Workers experience in general, we'd love to hear from you. Join the Cloudflare developer community on <a href="https://discord.com/channels/595317990191398933/1064502845061210152">Discord</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-06">Oct 6, 2025</time><div>
<h2 id="post-2025-10-06-data-catalog-table-compaction"><a href="/changelog/post/2025-10-06-data-catalog-table-compaction/">R2 Data Catalog table-level compaction</a></h2>
<div class="changelog-badges"><span>r2</span><span>r2-data-catalog</span></div><div class="changelog-body"><p>You can now enable compaction for individual <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables in <a href="/r2-data-catalog/">R2 Data Catalog</a>, giving you fine-grained control over different workloads.</p>
<pre><code class="language-bash">&#35; Enable compaction for a specific table (no token required)&#10;npx wrangler r2 bucket catalog compaction enable &lt;BUCKET&gt; &lt;NAMESPACE&gt; &lt;TABLE&gt; --target-size 256&#10;</code></pre>
<p>This allows you to:</p>
<ul>
<li>Apply different target file sizes per table</li>
<li>Disable compaction for specific tables</li>
<li>Optimize based on table-specific access patterns</li>
</ul>
<p>Learn more at <a href="/r2-data-catalog/manage-catalogs/">Manage catalogs</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-06">Oct 6, 2025</time><div>
<h2 id="post-2025-10-06-radar-pq-encryption-test"><a href="/changelog/post/2025-10-06-radar-pq-encryption-test/">Browser Support Detection for PQ Encryption on Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now includes browser detection for Post-quantum (PQ) encryption.
The <a href="https://radar.cloudflare.com/adoption-and-usage#post-quantum-encryption">Post-quantum encryption card</a> now checks whether a user’s browser supports post-quantum encryption.
If support is detected, information about the key agreement in use is displayed.</p>
<p><img src="/assets/upstream/images/radar/pq-encryption-test.png" alt="Screenshot of the PQ encryption browser support test on the Adoption &amp; Usage page" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-10-06">Oct 6, 2025</time><div>
<h2 id="post-2025-10-06-waf-release"><a href="/changelog/post/2025-10-06-waf-release/">WAF Release - 2025-10-06</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week’s highlights prioritise an emergency Oracle E-Business Suite RCE rule deployed to block active, high-impact exploitation. Also addressed are high-severity Chaos Mesh controller command-injection flaws that enable unauthenticated in-cluster RCE and potential cluster compromise, plus a form-data multipart boundary issue that permits HTTP Parameter Pollution (HPP). Two new generic SQLi detections were added to catch inline-comment obfuscation and information disclosure techniques.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>New emergency rule released for Oracle E-Business Suite (CVE-2025-61882) addressing an actively exploited remote code execution vulnerability in core business application modules. Immediate mitigation deployed to protect enterprise workloads.</p>
</li>
<li>
<p>Chaos Mesh (CVE-2025-59358,CVE-2025-59359,CVE-2025-59360,CVE-2025-59361): A GraphQL debug endpoint on the Chaos Controller Manager is exposed without authentication; several controller mutations (<code>cleanTcs</code>, <code>killProcesses</code>, <code>cleanIptables</code>) are vulnerable to OS command injection.</p>
</li>
<li>
<p>Form-Data (CVE-2025-7783): Attackers who can observe <code>Math.random()</code> outputs and control request fields in form-data may exploit this flaw to perform HTTP parameter pollution, leading to request tampering or data manipulation.</p>
</li>
<li>
<p>Two new generic SQLi detections added to enhance baseline coverage against inline-comment obfuscation and information disclosure attempts.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<ul>
<li>
<p>CVE-2025-61882 — Oracle E-Business Suite remote code execution (emergency detection): attacker-controlled input can yield full system compromise, data exfiltration, and operational outage; immediate blocking enforced.</p>
</li>
<li>
<p>CVE-2025-59358 / CVE-2025-59359 / CVE-2025-59360 / CVE-2025-59361 — Unauthenticated command-injection in Chaos Mesh controllers allowing remote code execution, cluster compromise, and service disruption (high availability risk).</p>
</li>
<li>
<p>CVE-2025-7783 — Predictable multipart boundaries in form-data enabling HTTP Parameter Pollution; results include request tampering, parameter overwrite, and downstream data integrity loss.</p>
</li>
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
        <code class="nb-rule-id" title="0c9bf31ab6fa41fc8f12daaf8650f52f">8650f52f</code>
</td>
<td>100882</td>
<td>Chaos Mesh - Missing Authentication - CVE:CVE-2025-59358</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="5d459ed434ed446c9580c73c2b8c3680">2b8c3680</code>
</td>
<td>100883</td>
<td>Chaos Mesh - Command Injection - CVE:CVE-2025-59359</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="a2591ba5befa4815a6861aefef859a04">ef859a04</code>
</td>
<td>100884</td>
<td>Chaos Mesh - Command Injection - CVE:CVE-2025-59361</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="05eea4fabf6f4cf3aac1094b961f26a7">961f26a7</code>
</td>
<td>100886</td>
<td>Form-Data - Parameter Pollution - CVE:CVE-2025-7783</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="90514c7810694b188f56979826a4074c">26a4074c</code>
</td>
<td>100888</td>
<td>Chaos Mesh - Command Injection - CVE:CVE-2025-59360</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr> 
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="42fbc8c09ec84578b9633ffc31101b2f">31101b2f</code>
</td>
<td>100916</td>
<td>Oracle E-Business Suite - Remote Code Execution - CVE:CVE-2025-61882</td>
<td>N/A</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="badc687a3ba3420a844220b129aa43c3">29aa43c3</code>
</td>
<td>100917</td>
<td>Generic Rules - SQLi - Inline Comment Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="28fa27511f29428899ceb5a273c10b6f">73c10b6f</code>
</td>
<td>100918</td>
<td>Generic Rules - SQLi - Information Disclosure</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>                    
</tbody>
</table>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/32/">Previous</a><span>Page 33 of 50</span><a class="pagination-next" rel="next" href="/changelog/34/">Next</a></nav>
</div>
