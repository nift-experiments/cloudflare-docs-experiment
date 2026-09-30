<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-07-21">Jul 21, 2026</time><div>
<h2 id="post-2026-07-21-automatic-origin-key-exchange"><a href="/changelog/post/2026-07-21-automatic-origin-key-exchange/">Faster and more secure TLS handshakes to your origins, automatically</a></h2>
<div class="changelog-badges"><span>ssl</span></div><div class="changelog-body"><p>Cloudflare now takes the guesswork out of TLS 1.3 key agreement with your origins. Automatic key exchange predicts the preferred algorithm and sends its key share in the first <code>ClientHello</code>, helping avoid a <code>HelloRetryRequest</code> and one extra network round trip.</p>
<p>Automatic key exchange is on for all existing zones and on by default for new zones. When an origin supports both classical and post-quantum key agreements, Cloudflare prefers the post-quantum <code>X25519MLKEM768</code> hybrid key agreement.</p>
<p>To change this behavior, go to <strong>SSL/TLS</strong> &gt; <strong>Overview</strong> &gt; <strong>Origin connection &amp; post-quantum encryption</strong>. Turn off <strong>Automatic key exchange</strong> to stop automatic scans and preference updates. Turning it off does not change your compliance requirements.</p>
<p><strong>Compliance requirements</strong> apply only to TLS 1.3 connections. The <strong>Post-quantum hybrid</strong> option requires hybrid post-quantum key agreements support on your origin server. The <strong>Federal Information Processing Standards (FIPS)</strong> option requires FIPS-compliant key agreements. Select both to require key agreements that satisfy both, or leave both unselected to allow all supported key agreements.</p>
<p>For requirements, configuration options, and rollout details, refer to <a href="/ssl/origin-configuration/automatic-key-exchange/">Automatic key exchange to origins</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-21">Jul 21, 2026</time><div>
<h2 id="post-2026-07-21-waf-release"><a href="/changelog/post/2026-07-21-waf-release/">WAF Release - 2026-07-21</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This release introduces new rules for vulnerabilities in Adobe ColdFusion, Next.js, WordPress alongside updates to existing rules thereby providing enhanced generic protections against Server-Side Request Forgery (SSRF), Local File Inclusion (LFI), and Cross-Site Scripting (XSS).</p>
<p><strong>WAF and framework adapter mitigations for Next.js vulnerabilities</strong></p>
<p>Multiple <a href="https://nextjs.org/blog/july-2026-security-release">security vulnerabilities</a> were disclosed and patched by the Next.js team through July 2026 security release. These include denial of service, middleware and proxy bypass, server-side request forgery, information disclosure, and cache poisoning across a range of severities.</p>
<p>Several of the disclosed vulnerabilities are not possible to block at WAF layer,we strongly recommend updating your application and its dependencies immediately. Patched versions are available through v16.2.11 (Active LTS) and v15.5.21 (Maintenance LTS) to address these issues.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Advisory</th>
<th>CVE</th>
<th>Severity</th>
<th>Issue</th>
<th>WAF Coverage</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-m99w-x7hq-7vfj">Denial of Service in App Router using Server Actions</a></td>
<td>CVE-2026-64641</td>
<td>High</td>
<td>
				Crafted requests targeting Next.js applications using App Router with at least one Server Action can lead to excessive CPU usage. The CPU usage blocks processing of further requests in the same process, leading to Denial of Service.
</td>
<td>
				WAF rule Next.js - DoS - CVE-2026-64641 (<code class="nb-rule-id" title="b013b67c357547b4b866234390dcdb0a">90dcdb0a</code>) has been deployed to provide coverage.
</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-6gpp-xcg3-4w24">Middleware / Proxy bypass in App Router applications using Turbopack and single locale</a></td>
<td>CVE-2026-64642</td>
<td>High</td>
<td>
				Next.js applications using App Router built with Turbopack and a single entry in config.i18n.locales are vulnerable to a middleware/proxy bypass. Accordingly, any authentication or security checks that a middleware/proxy may perform are bypassed.
</td>
<td>
				This is a middleware bypass that unfortunately cannot be covered through Cloudflare WAF signature engine.
</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-p9j2-gv94-2wf4">Server-Side Request Forgery in rewrites via attacker-controlled destination hostname</a></td>
<td>CVE-2026-64645</td>
<td>High</td>
<td>
				A rewrites() or redirects() rule that builds its external destination hostname from request-controlled input can be pointed at an arbitrary hostname, regardless of the rule's hostname suffix. For rewrites, this behavior enables Server-Side Request Forgery (SSRF); for redirects, Open Redirect can be achieved.
</td>
<td>
				Existing SSRF rules provide adequate coverage for this vulnerability, no tailored WAF rule was developed.
</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-89xv-2m56-2m9x">Server-Side Request Forgery in Server Actions on custom servers</a></td>
<td>CVE-2026-64649</td>
<td>High</td>
<td>
				When a Server Action forwards or redirects a request, an attacker can cause the server to send that outbound request to a malicious host (Server-Side Request Forgery). This requires the attacker’s request to control Host-associated headers.
</td>
<td>
				WAF rule Next.js - SSRF - CVE-2026-64649 (<code class="nb-rule-id" title="7fe6d6f3df774ae2a0011f20930091a3">930091a3</code>) has been deployed to provide coverage.
</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-q8wf-6r8g-63ch">Denial of Service in the Image Optimization API using SVGs</a></td>
<td>CVE-2026-64644</td>
<td>Medium</td>
<td>
				When self-hosting Next.js with the default image loader, the Image Optimization API can optimize remotely hosted images if configured (not enabled by default). If those images contain malicious content, the images can cause CPU exhaustion in the /_next/image endpoint.
</td>
<td>
				Malicious request is unfortunately indistinguishable from a legitimate image optimization request, so no WAF rule has been created to address this vulnerability.
</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-4c39-4ccg-62r3">Unbounded Server Action payload in Edge runtime</a></td>
<td>CVE-2026-64646</td>
<td>Medium</td>
<td>
				A crafted request can lead to memory consumption on Server Actions in the Edge runtime. Next.js applications which use App Router and have at least one Server Action are affected.
</td>
<td>
				Unfortunately there is no one size fits all rule that can be deployed through WAF in lieu of custom bodySizeLimit configurations, so no WAF rule has been created to address this vulnerability.
</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-955p-x3mx-jcvp">Unauthenticated disclosure of internal Server Function endpoints</a></td>
<td>CVE-2026-64643</td>
<td>Medium</td>
<td>
				In Next.js applications using App Router, Server Actions (use server) or use cache endpoint IDs can be globally disclosed. An attacker can use this for reconnaissance and as part of a broader attack chain.
</td>
<td>
				WAF rule Next.js - Information Disclosure - CVE-2026-64643 (<code class="nb-rule-id" title="6c4135d4d9d745e4866ad83672952826">72952826</code>) has been deployed to provide coverage.
</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-68g3-v927-f742">Cache confusion of response bodies for requests with bodies</a></td>
<td>CVE-2026-64648</td>
<td>Medium</td>
<td>
				A server-side fetch with a request body may return a cached response body from a different request to the same URL but different body. This only applies for fetch calls of the shape fetch(new Request(init), aDifferentInit)
</td>
<td>
				This is an application logic bug that unfortunately cannot be covered through Cloudflare WAF signature engine.
</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-4633-3j49-mh5q">Cache confusion of response bodies for requests with bodies containing invalid UTF-8 byte sequences</a></td>
<td>CVE-2026-64647</td>
<td>Medium</td>
<td>
				A server-side fetch with a request body may return a cached response body from a different request to the same URL but different body. This only applies when receiving request bodies which contain invalid UTF-8 characters.
</td>
<td>
				This is an application logic bug that unfortunately cannot be covered through Cloudflare WAF signature engine.
</td>
</tr>
</tbody>
</table>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>CVE-2026-48276: A path traversal vulnerability in Adobe ColdFusion file upload mechanisms allows unauthenticated attackers to write or upload files to arbitrary locations outside designated directories on the origin server.</p>
</li>
<li>
<p>CVE-2026-48282: A path traversal vulnerability in Adobe ColdFusion enables unauthenticated attackers to manipulate directory sequences and access restricted system files on the host filesystem.</p>
</li>
<li>
<p>CVE-2026-60137: An unauthenticated SQL injection vulnerability affecting WordPress. Threat actors exploit unsanitized input parameters to execute arbitrary SQL queries, leading to unauthorized database access, record manipulation, or data exfiltration.</p>
</li>
<li>
<p>CVE-2026-63030: A remote code execution vulnerability affecting WordPress core and plugin components. Remote, unauthenticated attackers can execute arbitrary system commands to gain unauthorized access or establish backdoors on host servers.</p>
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
				<code class="nb-rule-id" title="7fbdc9407bdb4a4eae2b3d91215e7d31">215e7d31</code>
</td>
<td>N/A</td>
<td>SSRF - Restricted Protocol</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6ca512d240d848d6a0c7ef42a935ee5d">a935ee5d</code>
</td>
<td>N/A</td>
<td>SSRF - Obfuscated Host</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a3fb0870c38440d8a9a0eba81b0230ac">1b0230ac</code>
</td>
<td>N/A</td>
<td>LFI - Path Traversal</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="452a04be3f73458c863d8dae61349c8b">61349c8b</code>
</td>
<td>N/A</td>
<td>Adobe ColdFusion - File Upload Path Traversal - CVE:CVE-2026-48276</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a53a3fb491c64d74908081ee9cb61eac">9cb61eac</code>
</td>
<td>N/A</td>
<td>Adobe ColdFusion - Path Traversal - CVE:CVE-2026-48282</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d8b63828c2344d919b94d2594ac5e21f">4ac5e21f</code>
</td>
<td>N/A</td>
<td>XSS — JS Bracket Concat Obfuscation - Body</td>
<td>Log</td>
<td>Disabled</td>
<td>
				This is a new detection.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="264a83a764be428ca41d516ff31f5559">f31f5559</code>
</td>
<td>N/A</td>
<td>XSS — JS Bracket Concat Obfuscation - Headers</td>
<td>Log</td>
<td>Disabled</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="4ba21a60837244029183b782987984fd">987984fd</code>
</td>
<td>N/A</td>
<td>XSS — JS Bracket Concat Obfuscation - URI</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1c060d3a371549219ee290d7ed933fcc">ed933fcc</code>
</td>
<td>N/A</td>
<td>Wordpress - SQL Injection - CVE:CVE-2026-60137</td>
<td>N/A</td>
<td>Block</td>
<td>
				This was labeled as Generic Rules - SQLi.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7dfb2bd4708d4b88b9911dc0550664b6">550664b6</code>
</td>
<td>N/A</td>
<td>Wordpress - Remote Code Execution - CVE:CVE-2026-63030</td>
<td>N/A</td>
<td>Block</td>
<td>
				This was labeled as Generic Rules - Unauthenticated RCE.
</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="db003b39b7774859a8d588ce33697a1a">33697a1a</code>
</td>
<td>N/A</td>
<td>Wordpress - SQL Injection - CVE:CVE-2026-60137</td>
<td>N/A</td>
<td>Block</td>
<td>
				This was labeled as Generic Rules - SQLi.
</td>
</tr>	
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="ebd3f2df15c74ddcbf6220c9b5ec246a">b5ec246a</code>
</td>
<td>N/A</td>
<td>Wordpress - Remote Code Execution - CVE:CVE-2026-63030</td>
<td>N/A</td>
<td>Block</td>
<td>
				This was labeled as Generic Rules - Unauthenticated RCE.
</td>
</tr>		
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6c4135d4d9d745e4866ad83672952826">72952826</code>
</td>
<td>N/A</td>
<td>Next.js - Information Disclosure - CVE-2026-64643</td>
<td>N/A</td>
<td>Block</td>
<td>
				This was labeled as Generic Rules - Information Disclosure.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="7fe6d6f3df774ae2a0011f20930091a3">930091a3</code>
</td>
<td>N/A</td>
<td>Next.js - SSRF - CVE-2026-64649</td>
<td>N/A</td>
<td>Block</td>
<td>
				This was labeled as Generic Rules - Auth Bypass - 2.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="c4ca56c0a6a348299d5a93e663167195">63167195</code>
</td>
<td>N/A</td>
<td>Next.js - Remote Code Execution - Cache Components</td>
<td>N/A</td>
<td>Block</td>
<td>
				This was labeled as Generic Rules - RCE.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="b013b67c357547b4b866234390dcdb0a">90dcdb0a</code>
</td>
<td>N/A</td>
<td>Next.js - DoS - CVE-2026-64641</td>
<td>N/A</td>
<td>Block</td>
<td>
				This was labeled as Generic Rules - DoS.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="aa21c9b8b97743bfb217748b2049a60c">2049a60c</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - Body - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="e7ee67e824844754b513cdf3836855a4">836855a4</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - Header - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5f2a6681a2b94442b23816286d060a0d">6d060a0d</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - URI - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-20">Jul 20, 2026</time><div>
<h2 id="post-2026-07-20-http-private-apps-l7-auth"><a href="/changelog/post/2026-07-20-http-private-apps-l7-auth/">Browser-based login for plaintext HTTP private applications</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>Cloudflare Access now uses the standard browser-based login flow for <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">private applications</a> served over plaintext HTTP on port <code>80</code>.</p>
<p>Previously, plaintext HTTP private apps fell back to the same session flow used for SSH, RDP, and other non-HTTP protocols: users got an <code>Authentication required</code> pop-up from the Cloudflare One Client, then had to select the notification to open a browser and log in. Now, users hitting an HTTP private app see the Access login page directly in the browser and receive a standard Access <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/">application token</a> on success.</p>
<p>This brings the HTTP experience in line with HTTPS apps (with <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">Gateway TLS decryption</a> turned on). No configuration change is required. The Cloudflare One Client is still required to route traffic to the private network, but it no longer manages the Access session for HTTP apps.</p>
<p>Other non-HTTP protocols (SSH, RDP, arbitrary TCP/UDP) continue to use the Cloudflare One Client notification flow.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-20">Jul 20, 2026</time><div>
<h2 id="post-2026-06-15-budget-alerts-default-on"><a href="/changelog/post/2026-06-15-budget-alerts-default-on/">Budget alerts now on by default for Pay-as-you-go accounts</a></h2>
<div class="changelog-badges"><span>billing</span><span>workers</span></div><div class="changelog-body"><p>We are turning on budget alerts by default for eligible Pay-as-you-go accounts. If your account does not already have a budget alert, Cloudflare will create one for you with a $10 account-level threshold. Your default alert will enable at the turn of your next billing cycle, so it will not fire based on usage you have already incurred.</p>
<p>We are rolling this out in cohorts over the coming weeks, so eligible accounts may see their default alert appear at different times.</p>
<p>The default alert behaves exactly like an alert you would create yourself. When your cumulative usage-based spend this cycle reaches the threshold, you receive an email notification. The alert is informational only. It does not cap your usage or impact your account in any way.</p>
<p>Usage is processed once per day for the prior day's activity, so budget alerts fire the day after the threshold is reached rather than in real time.</p>
<p>Budget alerts only consider spend on usage-based products. Recurring subscription fees, such as the Workers Paid plan fee or other monthly plan charges, are not included in the threshold calculation.</p>
<p>You can change the threshold, add additional alerts, or remove the default alert entirely from <strong>Manage Account</strong> &gt; <strong>Billing</strong> &gt; <strong>Billable Usage</strong>, or from your Notifications settings. If you already configured your own budget alert, nothing changes.</p>
<p>Enterprise contract accounts are not in scope.</p>
<p>For more information, refer to the <a href="/billing/manage/budget-alerts/">Budget alerts documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-20">Jul 20, 2026</time><div>
<h2 id="post-2026-07-20-durable-objects-total-storage-metrics"><a href="/changelog/post/2026-07-20-durable-objects-total-storage-metrics/">View total SQLite storage for Durable Object namespaces</a></h2>
<div class="changelog-badges"><span>durable-objects</span><span>workers</span></div><div class="changelog-body"><p>You can now monitor the total SQLite storage used by a Durable Object namespace over time in the Cloudflare dashboard. The new <strong>Total storage</strong> chart shows the maximum storage reported during each hour. This helps you identify storage growth, validate data cleanup, and investigate unexpected usage.</p>
<p><img src="/assets/upstream/images/changelog/durable-objects/durable-objects-total-storage.png" alt="The Total storage chart showing a Durable Object namespace growing to 260.1 MB of storage over time." /></p>
<div class="nb-dash-button"></div>
<p>The chart appears only for SQLite-backed Durable Object namespaces. It does not appear for namespaces that use the legacy key-value storage backend. Viewing storage for individual Durable Objects by ID or name is not supported.</p>
<p>For more information, refer to <a href="/durable-objects/observability/metrics-and-analytics/#total-storage">Metrics and analytics</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-17">Jul 17, 2026</time><div>
<h2 id="post-2026-07-17-appliance-restart-reboot-shutdown"><a href="/changelog/post/2026-07-17-appliance-restart-reboot-shutdown/">Restart, reboot, or shut down a Cloudflare One Appliance from the dashboard</a></h2>
<div class="changelog-badges"><span>cloudflare-one-appliance</span><span>cloudflare-one</span><span>cloudflare-wan</span></div><div class="changelog-body"><p>You can now restart, reboot, or shut down a <a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a> directly from the dashboard or via API.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-wan/2026-07-17-appliance-restart-reboot-shutdown.gif" alt="Restarting a Cloudflare One Appliance from the Operations section of the Edit Appliance page" /></p>
<ul>
<li><strong>Restart</strong> — Restart managed services. Purges temporary and (optionally) persistent state.</li>
<li><strong>Reboot</strong> — Power cycle the appliance. Optionally, purge persistent state. Re-applies configuration starting from scratch.</li>
<li><strong>Shutdown</strong> — Power off the appliance. Optionally, purge persistent state. The machine will be offline until manually powered on again.</li>
</ul>
<p>In the dashboard, go to <strong>Networking</strong> &gt; <strong>Connectors</strong> &gt; <strong>Appliances</strong>, select an appliance, then <strong>Edit</strong> &gt; <strong>Operations</strong> to send an operation. Via API, <code>POST</code> to the <code>/accounts/{account_id}/magic/connectors/{connector_id}/interrupts</code> endpoint.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/maintenance/appliance-operations/">Appliance operations</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-17">Jul 17, 2026</time><div>
<h2 id="post-2026-07-17-email-message-preview"><a href="/changelog/post/2026-07-17-email-message-preview/">Preview sent emails in the Activity log</a></h2>
<div class="changelog-badges"><span>email-service</span></div><div class="changelog-body"><p>You can now preview the content of sent emails directly from the Email Service Activity log. Expand a sent email and open the new <strong>Preview</strong> section to inspect the message as it was sent, across tabs for the rendered <strong>HTML</strong> body, the <strong>Text</strong> body, the <strong>Headers</strong>, the <strong>Attachments</strong>, and the full <strong>Raw</strong> <a href="https://datatracker.ietf.org/doc/html/rfc5322">RFC 5322</a> source.</p>
<p><img src="/assets/upstream/images/changelog/email-service/email-message-preview.png" alt="The rendered HTML preview of a sent email in the Email Service Activity log" /></p>
<p>Previously, the Activity log surfaced delivery and authentication metadata but not the message content, making rendering and content issues harder to debug. Message preview closes that gap.</p>
<p>To make messages previewable, turn on <strong>Email preview</strong> in your sending domain's settings. Previews cover messages sent while the setting is turned on and are retained for about seven days. Sending domains onboarded on or after 2026-07-02 have <strong>Email preview</strong> turned on automatically.</p>
<p><img src="/assets/upstream/images/changelog/email-service/email-preview-setting.png" alt="The Email preview setting in a sending domain's settings" /></p>
<p>Refer to <a href="/email-service/observability/logs/#message-preview">Email logs</a> for more information.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-17">Jul 17, 2026</time><div>
<h2 id="post-2026-07-17-http-request-header-manipulation"><a href="/changelog/post/2026-07-17-http-request-header-manipulation/">New header control options for Gateway HTTP policies</a></h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>Cloudflare Gateway now supports advanced header control on <a href="/cloudflare-one/traffic-policies/http-policies/#allow">Allow policies</a>. Administrators can add, overwrite, or delete headers on matching requests using static values or dynamic variables.</p>
<h4 id="2026-07-17-http-request-header-manipulation-header-operations">Header operations</h4>
<p>Gateway HTTP policies using the Allow action support three operations in <code>rule_settings</code>:</p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>API field</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Add</td>
<td><code>add_headers</code></td>
<td>Appends a value to the header. Existing values are preserved.</td>
</tr>
<tr>
<td>Overwrite</td>
<td><code>set_headers</code></td>
<td>Replaces the header value. Creates the header if it does not exist.</td>
</tr>
<tr>
<td>Delete</td>
<td><code>delete_headers</code></td>
<td>Removes the header from the request.</td>
</tr>
</tbody>
</table>
<p>Gateway applies operations in order: delete, then overwrite, then add.</p>
<h4 id="2026-07-17-http-request-header-manipulation-dynamic-variables">Dynamic variables</h4>
<p>Header values can include dynamic variables using the <code>@{...}</code> syntax. Gateway resolves variables at request time from identity, device, and network context.</p>
<table>
<thead>
<tr>
<th>Variable</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@{identity.email}</code></td>
<td>User email from the identity provider</td>
</tr>
<tr>
<td><code>@{identity.name}</code></td>
<td>User display name from the identity provider</td>
</tr>
<tr>
<td><code>@{identity.id}</code></td>
<td>Cloudflare identity UUID</td>
</tr>
<tr>
<td><code>@{identity.groups}</code></td>
<td>Identity provider group memberships</td>
</tr>
<tr>
<td><code>@{identity.SAML}</code></td>
<td>SAML attributes (if configured)</td>
</tr>
<tr>
<td><code>@{identity.OIDC}</code></td>
<td>OIDC claims (if configured)</td>
</tr>
<tr>
<td><code>@{source.ip}</code></td>
<td>Source IP of the connection</td>
</tr>
<tr>
<td><code>@{destination.ip}</code></td>
<td>Destination IP of the request</td>
</tr>
<tr>
<td><code>@{device.id}</code></td>
<td>Cloudflare One Client device UUID</td>
</tr>
<tr>
<td><code>@{device.posture}</code></td>
<td>Device posture check results (JSON string)</td>
</tr>
</tbody>
</table>
<p>You can mix static text and dynamic variables in a single header value. For example, <code>user-@{identity.email}</code> resolves to <code>user-jdoe@example.com</code>.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/http-policies/tenant-control/">Custom headers</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-17">Jul 17, 2026</time><div>
<h2 id="post-2026-07-17-distributor-mssp-self-serve-members"><a href="/changelog/post/2026-07-17-distributor-mssp-self-serve-members/">Distributor, MSSP, and Agency partners can manage Organization members directly</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>organizations</span></div><div class="changelog-body"><p>Distributor, MSSP, and Agency partners on Cloudflare <a href="/fundamentals/organizations/">Organizations</a> can now add and manage Organization Members directly from the Cloudflare dashboard, without help from Cloudflare.</p>
<p>Previously, adding a member to a Distributor, MSSP, or Agency Organization was a manual, Cloudflare-assisted process that required a request to Cloudflare and enrollment in a closed beta, and the dashboard <strong>Add member</strong> flow was blocked for these Organizations.</p>
<p>Now, Organization admins can add members themselves from <strong>Organization</strong> &gt; <strong>Members</strong> &gt; <strong>Add member</strong>, with no beta enrollment required.</p>
<p>New members receive access to the Organization's accounts through the same implicit-access model already used for enterprise Organizations. The <strong>Accounts</strong> list and the account switcher classify Distributor, MSSP, and Agency Organizations consistently with enterprise Organizations, so their accounts are labeled and grouped correctly in the dashboard.</p>
<p>Agency partners also gain access to the Organizations dashboard, while retaining access to their existing Tenant management dashboard.</p>
<p>Distributor, MSSP, and Agency Organizations are currently in beta.</p>
<p>For more information, refer to <a href="/fundamentals/organizations/manage-members/">Manage Organization members</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-17">Jul 17, 2026</time><div>
<h2 id="post-2026-07-17-emergency-waf-release"><a href="/changelog/post/2026-07-17-emergency-waf-release/">WAF Release - 2026-07-17 - Emergency</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This emergency release adds a new managed rule to block active exploitation of a critical remote code execution (RCE) and SQL injection (SQLi) vulnerability found in popular web frameworks.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Generic Frameworks - Unauthenticated RCE: Attackers can execute arbitrary system commands with web server privileges by sending malicious input containing invalid path sequences during request processing.</p>
</li>
<li>
<p>Generic Frameworks - SQLi: Attackers can execute unauthorized database queries due to a failure to sanitize input values within request parameters.</p>
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
				<code class="nb-rule-id" title="7dfb2bd4708d4b88b9911dc0550664b6">550664b6</code>
</td>
<td>N/A</td>
<td>Generic Rules - Unauthenticated RCE</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1c060d3a371549219ee290d7ed933fcc">ed933fcc</code>
</td>
<td>N/A</td>
<td>Generic Rules - SQLi </td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="ebd3f2df15c74ddcbf6220c9b5ec246a">b5ec246a</code>
</td>
<td>N/A</td>
<td>Generic Rules - Unauthenticated RCE </td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="db003b39b7774859a8d588ce33697a1a">33697a1a</code>
</td>
<td>N/A</td>
<td>Generic Rules - SQLi </td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>        
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-16">Jul 16, 2026</time><div>
<h2 id="post-2026-07-16-rdp-bulk-print"><a href="/changelog/post/2026-07-16-rdp-bulk-print/">Bulk print PDFs for browser-based RDP</a></h2>
<div class="changelog-badges"><span>access</span><span>cloudflare-one</span></div><div class="changelog-body"><p>Users in browser-based RDP sessions can now print multiple PDF files as a single print job. Copy the files to your clipboard on the remote machine, then select <strong>Print all PDFs</strong> in the clipboard panel. The files are combined into one PDF and sent to your local printer.</p>
<p><img src="/assets/upstream/images/changelog/access/rdp-bulk-print.png" alt="The clipboard panel showing the Print all PDFs option for multiple selected PDF files." /></p>
<p>Bulk print is available in Chromium-based browsers and Firefox. For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#print-pdfs">Print PDFs for browser-based RDP</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-16">Jul 16, 2026</time><div>
<h2 id="post-2026-07-16-wrangler-commands"><a href="/changelog/post/2026-07-16-wrangler-commands/">Manage Flagship from the command line with Wrangler</a></h2>
<div class="changelog-badges"><span>flagship</span></div><div class="changelog-body"><p><strong><a href="/workers/wrangler/">Wrangler</a></strong> now includes <code>wrangler flagship</code>, a command suite for managing <a href="/flagship/">Flagship</a> apps and feature flags from your terminal.</p>
<p>Create an app and, if you use it from a Worker, add it to your <code>wrangler.json</code> or <code>wrangler.jsonc</code> file as a binding:</p>
<pre><code class="language-bash">wrangler flagship apps create &quot;My Worker App&quot; \&#10;  &#45;-binding FLAGS \&#10;  &#45;-update-config&#10;</code></pre>
<p>Then create flags for the behavior you want to control. Flags can be booleans, strings, numbers, or JSON values:</p>
<pre><code class="language-bash">wrangler flagship flags create &lt;APP_ID&gt; new-checkout&#10;&#10;wrangler flagship flags create &lt;APP_ID&gt; checkout-flow \&#10;  &#45;-variation control=old-checkout \&#10;  &#45;-variation treatment=new-checkout \&#10;  &#45;-default control \&#10;  &#45;-type string&#10;</code></pre>
<p>After a flag exists, change its default variation or use enable and disable commands as kill switches. Existing targeting rules continue to apply unless you change or clear them explicitly:</p>
<pre><code class="language-bash">wrangler flagship flags update &lt;APP_ID&gt; checkout-flow --default treatment&#10;wrangler flagship flags disable &lt;APP_ID&gt; checkout-flow&#10;wrangler flagship flags enable &lt;APP_ID&gt; checkout-flow&#10;</code></pre>
<p>For release workflows, use <code>rollout</code>, <code>split</code>, and <code>rules</code> to change exposure without redeploying your Worker:</p>
<pre><code class="language-bash">wrangler flagship flags rollout &lt;APP_ID&gt; new-checkout \&#10;  &#45;-to on \&#10;  &#45;-percentage 25 \&#10;  &#45;-by user_id&#10;&#10;wrangler flagship flags split &lt;APP_ID&gt; checkout-flow \&#10;  &#45;-weight control=80 \&#10;  &#45;-weight treatment=20 \&#10;  &#45;-by user_id&#10;&#10;wrangler flagship flags rules update &lt;APP_ID&gt; checkout-flow \&#10;  &#45;-priority 1 \&#10;  &#45;-when &quot;country equals US&quot;&#10;</code></pre>
<p>These commands can also be used from CI/CD pipelines, scripts, and AI agents to inspect Flagship state, update flag behavior, or roll back changes through Wrangler.</p>
<p>Refer to the <a href="/flagship/reference/wrangler-commands/"><code>wrangler flagship</code> command reference</a> for the full command guide.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-16">Jul 16, 2026</time><div>
<h2 id="post-2026-07-16-cache-rules-bot-fields-asn"><a href="/changelog/post/2026-07-16-cache-rules-bot-fields-asn/">Bot management fields and ASN support in Cache Rules</a></h2>
<div class="changelog-badges"><span>rules</span></div><div class="changelog-body"><h4 id="2026-07-16-cache-rules-bot-fields-asn-bot-management-fields-and-asn-support-in-cache-rules">Bot management fields and ASN support in Cache Rules</h4>
<p>Cache Rules now supports bot management fields and the <code>ip.src.asnum</code> field in expression filters. You can now build cache policies that differentiate between automated and human traffic, or segment caching behavior by autonomous system number (ASN).</p>
<p>This allows you to apply different caching strategies for verified bots, high-risk traffic, or specific network operators without affecting legitimate user requests. For example, you can set shorter cache TTLs for suspected bot traffic or bypass cache entirely for requests from specific ASNs.</p>
<h4 id="2026-07-16-cache-rules-bot-fields-asn-new-fields">New fields</h4>
<p>The following fields are now available in Cache Rules expressions:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cf.bot_management.score</code></td>
<td>Number</td>
<td>Bot score from <code>1</code> to <code>99</code>, where a lower value indicates a higher likelihood that the request originates from a bot.</td>
</tr>
<tr>
<td><code>cf.bot_management.ja3_hash</code></td>
<td>String</td>
<td>JA3 fingerprint of the request, which helps identify the client making the connection.</td>
</tr>
<tr>
<td><code>cf.bot_management.ja4</code></td>
<td>String</td>
<td>JA4 fingerprint of the request, which provides a more detailed client identification than JA3.</td>
</tr>
<tr>
<td><code>cf.bot_management.verified_bot</code></td>
<td>Boolean</td>
<td>Whether the request originates from a verified bot, such as a search engine crawler.</td>
</tr>
<tr>
<td><code>cf.bot_management.static_resource</code></td>
<td>Boolean</td>
<td>Whether the request is for a static resource and therefore exempt from bot detection.</td>
</tr>
<tr>
<td><code>cf.bot_management.js_detection.passed</code></td>
<td>Boolean</td>
<td>Whether the browser passed JavaScript detection when the feature is enabled.</td>
</tr>
<tr>
<td><code>cf.bot_management.detection_ids</code></td>
<td>Array&lt;Number&gt;</td>
<td>List of IDs that correspond to Bot Management heuristic detections made on the request.</td>
</tr>
<tr>
<td><code>cf.bot_management.tags</code></td>
<td>Array&lt;String&gt;</td>
<td>List of tags associated with the bot traffic, such as <code>API</code>, <code>GOOGLE</code>, or <code>BING</code>. Match a tag with an expression such as <code>any(cf.bot_management.tags[*] eq &quot;API&quot;)</code>.</td>
</tr>
<tr>
<td><code>cf.bot_management.signed_agent</code></td>
<td>Boolean</td>
<td>Whether the request originates from a known agent that identifies itself with Web Bot Auth.</td>
</tr>
<tr>
<td><code>cf.bot_management.corporate_proxy</code></td>
<td>Boolean</td>
<td>Whether the request originates from a known corporate proxy.</td>
</tr>
<tr>
<td><code>ip.src.asnum</code></td>
<td>Number</td>
<td>The autonomous system number (ASN) of the incoming request's IP address.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17750.md")</aside>
<h4 id="2026-07-16-cache-rules-bot-fields-asn-example">Example</h4>
<p>Cache Rules expressions support combining these fields with other criteria. The following example sets a shorter cache TTL for API requests that originate from a high-risk bot or an unexpected ASN:</p>
<pre><code class="language-txt">(http.request.uri.path contains &quot;/api/&quot; and cf.bot_management.score lt 30)&#10;or&#10;(http.request.uri.path contains &quot;/api/&quot; and not ip.src.asnum in {12345 67890})&#10;</code></pre>
<p>To learn more, refer to the <a href="/cache/how-to/cache-rules/">Cache Rules documentation</a> and the <a href="/ruleset-engine/rules-language/fields/">Fields reference</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-15">Jul 15, 2026</time><div>
<h2 id="post-2026-07-15-internal-dns-ga"><a href="/changelog/post/2026-07-15-internal-dns-ga/">Internal DNS is now generally available</a></h2>
<div class="changelog-badges"><span>gateway</span><span>dns</span></div><div class="changelog-body"><p><a href="/dns/internal-dns/">Internal DNS</a> is now generally available. Internal DNS provides authoritative and recursive DNS for private networks on the same global network and control plane you already use for public DNS, Zero Trust, and application services.</p>
<h4 id="2026-07-15-internal-dns-ga-why-it-matters">Why it matters</h4>
<ul>
<li><strong>Consolidate DNS operations.</strong> Public and private DNS run on one platform, with one API, one audit trail, and one place to set policy.</li>
<li><strong>Simplify split-horizon DNS.</strong> Internal and external resolution are defined as separate <a href="/dns/internal-dns/dns-views/">views</a> over shared zones, managed from a single control plane — so there is no drift to chase down.</li>
<li><strong>Extend Zero Trust to DNS.</strong> Resolver policies decide which users and devices resolve against which view, enforced by the same <a href="/cloudflare-one/traffic-policies/">Gateway</a> that already governs the rest of your traffic.</li>
</ul>
<p>Setting up Internal DNS takes three steps: create a zone, create a view, and define a resolver policy.</p>
<pre><code class="language-json">POST /zones&#10;{&#10;  &quot;account&quot;: {&#10;    &quot;id&quot;: &quot;&lt;ACCOUNT_ID&gt;&quot;&#10;  },&#10;  &quot;name&quot;: &quot;corp.internal&quot;,&#10;  &quot;type&quot;: &quot;internal&quot;&#10;}&#10;</code></pre>
<p>Internal DNS is included with <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> for Enterprise customers. To get started, refer to the <a href="/dns/internal-dns/">Internal DNS documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-15">Jul 15, 2026</time><div>
<h2 id="post-2026-07-15-event-subscriptions"><a href="/changelog/post/2026-07-15-event-subscriptions/">Subscribe to Email Sending events with Queues</a></h2>
<div class="changelog-badges"><span>email-service</span><span>queues</span></div><div class="changelog-body"><p>You can now subscribe to <strong><a href="/email-service/api/send-emails/">Email Sending</a> events</strong> through <a href="/queues/event-subscriptions/">Queues event subscriptions</a> and receive outbound transactional email lifecycle events on a queue. Each subscription is scoped to one sending domain — either the zone apex, such as <code>example.com</code>, or a verified sending subdomain, such as <code>send.example.com</code>.</p>
<p>Six event types are published: <code>message.delivered</code>, <code>message.deferred</code>, <code>message.bounced</code>, <code>message.failed</code>, <code>message.rejected</code>, and <code>message.complained</code>. Use them to track deliverability, react to bounces and complaints, and drive suppression or retry logic. Email Routing events are not published on this source.</p>
<p>Each event includes the message details, delivery status, and SMTP response:</p>
<pre><code class="language-json">{&#10;	&quot;type&quot;: &quot;cf.email.sending.message.delivered&quot;,&#10;	&quot;source&quot;: {&#10;		&quot;type&quot;: &quot;email.sending&quot;,&#10;		&quot;zoneId&quot;: &quot;023e105f4ecef8ad9ca31a8372d0c353&quot;,&#10;		&quot;domain&quot;: &quot;example.com&quot;&#10;	},&#10;	&quot;payload&quot;: {&#10;		&quot;messageId&quot;: &quot;0101018f7d0c4d9a-msg-deadbeef&quot;,&#10;		&quot;recipient&quot;: &quot;user@example.net&quot;,&#10;		&quot;terminal&quot;: true,&#10;		&quot;delivery&quot;: {&#10;			&quot;status&quot;: &quot;delivered&quot;,&#10;			&quot;smtpStatusCode&quot;: &quot;250&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Refer to <a href="/email-service/platform/event-subscriptions/">Event subscriptions</a> to see all event types and example payloads.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-15">Jul 15, 2026</time><div>
<h2 id="post-2026-07-15-kv-legacy-namespace-routes-deprecation"><a href="/changelog/post/2026-07-15-kv-legacy-namespace-routes-deprecation/">Deprecate legacy Workers KV namespace API routes</a></h2>
<div class="changelog-badges"><span>kv</span></div><div class="changelog-body"><p>The legacy Workers KV API routes under <code>/accounts/{account_id}/workers/namespaces/*</code> are deprecated as of July 15, 2026, and will stop working on October 15, 2026. Migrate to the documented <a href="/api/resources/kv/">Workers KV API</a> routes under <code>/accounts/{account_id}/storage/kv/namespaces/*</code> before that date.</p>
<p>The legacy and replacement routes are interchangeable. They accept the same request parameters and return the same response payloads. To migrate, update the URL path from <code>/workers/namespaces/</code> to <code>/storage/kv/namespaces/</code>.</p>
<h4 id="2026-07-15-kv-legacy-namespace-routes-deprecation-what-you-need-to-do">What you need to do</h4>
<p>Update any integration that calls a route under <code>/accounts/{account_id}/workers/namespaces/</code> to use the equivalent route under <code>/accounts/{account_id}/storage/kv/namespaces/</code>. The migration is a direct URL path substitution — request parameters and response payloads are identical:</p>
<ul>
<li><code>GET</code> and <code>POST /accounts/{account_id}/workers/namespaces</code> → <code>GET</code> and <code>POST /accounts/{account_id}/storage/kv/namespaces</code></li>
<li><code>GET</code>, <code>PUT</code>, and <code>DELETE /accounts/{account_id}/workers/namespaces/{namespace_id}</code> → <code>GET</code>, <code>PUT</code>, and <code>DELETE /accounts/{account_id}/storage/kv/namespaces/{namespace_id}</code></li>
<li><code>GET /accounts/{account_id}/workers/namespaces/{namespace_id}/keys</code> → <code>GET /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/keys</code></li>
<li><code>GET /accounts/{account_id}/workers/namespaces/{namespace_id}/metadata/{key_name}</code> → <code>GET /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/metadata/{key_name}</code></li>
<li><code>GET</code>, <code>PUT</code>, and <code>DELETE /accounts/{account_id}/workers/namespaces/{namespace_id}/values/{key_name}</code> → <code>GET</code>, <code>PUT</code>, and <code>DELETE /accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key_name}</code></li>
</ul>
<p>For more information about the deprecation timeline, refer to <a href="/fundamentals/api/reference/deprecations/">API deprecations</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-14">Jul 14, 2026</time><div>
<h2 id="post-2026-07-14-waf-release"><a href="/changelog/post/2026-07-14-waf-release/">WAF Release - 2026-07-14</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This release introduces new rules targeting critical infrastructure vulnerabilities. These include an unauthenticated memory disclosure flaw in Citrix NetScaler ADC and Gateway (CVE-2026-8451) and a high-severity pre-authentication remote code execution (RCE) vulnerability in Progress Kemp LoadMaster (CVE-2026-8037).</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>CVE-2026-8451: An insufficient input validation vulnerability affects Citrix NetScaler ADC and NetScaler Gateway appliances configured as a SAML Identity Provider (IdP). Remote, unauthenticated attackers can exploit this flaw by sending malformed requests to trigger a memory overread, allowing them to leak chunks of sensitive data from adjacent appliance memory.</p>
</li>
<li>
<p>CVE-2026-8037: A critical OS command injection vulnerability in Progress Kemp LoadMaster load balancers allows unauthenticated remote attackers to achieve remote code execution (RCE).</p>
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
				<code class="nb-rule-id" title="78826e3223b94da493a2ade876973ac4">76973ac4</code>
</td>
<td>N/A</td>
<td>Citrix Netscaler ADC - Insufficient Input Validation - CVE:CVE-2026-8451</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6b64d216620449fbb273d07910233f36">10233f36</code>
</td>
<td>N/A</td>
<td>Progress Kemp LoadMaster - Remote Code Execution - CVE:CVE-2026-8037</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>		
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-14">Jul 14, 2026</time><div>
<h2 id="post-2026-06-10-improved-reliability-for-web-analytics-dash"><a href="/changelog/post/2026-06-10-improved-reliability-for-web-analytics-dash/">Improved reliability for account-wide Web Analytics dashboards</a></h2>
<div class="changelog-badges"><span>web-analytics</span></div><div class="changelog-body"><p>Cloudflare Web Analytics (Real User Monitoring) has rolled out performance optimizations to significantly improve the stability and loading speed of account-wide dashboards.</p>
<p>For larger accounts (with &gt;100 Web Analytics sites), loading the aggregate account-wide view would often fail, running into timeouts or unexpected interface errors due to the massive scale of parallel query processing. This update optimizes how high-volume multi-site data is queried to reduce errors and provide a snappier dashboard experience.</p>
<p>Accounts with up to 1,000 sites will now be able to load this account-wide aggregate view without experiencing misleading errors.</p>
<p>If you have an account with over 1,000 sites, we cannot currently aggregate over this volume due to processing constraints but you will now be presented with a clear error and instruction to filter to the relevant site(s) you wish to see the data for.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-14">Jul 14, 2026</time><div>
<h2 id="post-2026-07-14-temporary-accounts-api"><a href="/changelog/post/2026-07-14-temporary-accounts-api/">Platforms can now create Temporary Accounts via the Cloudflare API</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Platforms can now create temporary preview accounts through the Cloudflare REST API. This lets your platform deploy a live Worker before the user signs in to Cloudflare.</p>
<p>With the Temporary Accounts API, coding agents, AI app builders, and other platforms can build a similar flow for generated Workers and supported resources.</p>
<p>Your platform can keep users in its onboarding flow while they generate, deploy, and test an application. Users do not need an existing Cloudflare account, and your platform does not need write access to one.</p>
<p><img src="/assets/upstream/images/workers/claim-deployments-flow.png" alt="Diagram showing an AI agent deploying, verifying, and redeploying a Worker in a temporary account, then a user authenticating and claiming the account to keep its resources" /></p>
<p>The API returns a claim URL that lets the user make the temporary account and its resources permanent.</p>
<p><a href="https://www.cloudflare.com/drop/">Cloudflare Drop</a> demonstrates this preview-and-claim pattern for static sites. Someone can upload a site, test and share it for one hour, then sign in or create an account only when they want to keep it.</p>
<p>This API expands the flow first introduced with <a href="/changelog/post/2026-06-19-temporary-accounts-for-agents/"><code>wrangler deploy --temporary</code></a>. Your backend now controls the provisioning and deployment experience directly:</p>
<ol>
<li>Show Cloudflare's Terms of Service and Privacy Policy in your product, and require the user to accept them.</li>
<li>Request and solve a proof-of-work challenge.</li>
<li>Create a temporary preview account.</li>
<li>Deploy with the returned temporary account ID and API token.</li>
<li>Show the deployed Worker URL and claim URL to the user.</li>
</ol>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/provisioning/previews/challenge&quot; \&#10;  &#45;X POST \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{}&#x27;&#10;&#10;curl &quot;https://api.cloudflare.com/client/v4/provisioning/previews&quot; \&#10;  &#45;X POST \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;termsOfService&quot;: &quot;https://www.cloudflare.com/terms/&quot;,&#10;    &quot;privacyPolicy&quot;: &quot;https://www.cloudflare.com/privacypolicy/&quot;,&#10;    &quot;acceptTermsOfService&quot;: &quot;yes&quot;,&#10;    &quot;challengeToken&quot;: &quot;&lt;CHALLENGE_TOKEN&gt;&quot;,&#10;    &quot;solution&quot;: {&#10;      &quot;checkpoints&quot;: &quot;&lt;BASE64_CHECKPOINTS&gt;&quot;&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>For the complete API flow, proof-of-work requirements, supported products, and limits, refer to <a href="/workers/platform/claim-deployments/#integrate-with-the-rest-api">Claim deployments (temporary accounts)</a>. For the background and design goals behind this flow, refer to <a href="https://blog.cloudflare.com/temporary-accounts/">Temporary Cloudflare Accounts for AI agents</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-13">Jul 13, 2026</time><div>
<h2 id="post-2026-07-13-mcp-client-elicitation"><a href="/changelog/post/2026-07-13-mcp-client-elicitation/">Agents can respond to MCP elicitation requests</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>Agents connected to Model Context Protocol (MCP) servers with <a href="/agents/model-context-protocol/apis/client-api/"><code>addMcpServer</code></a> can now handle <a href="https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation">elicitation</a> requests.</p>
<p>Elicitation lets an MCP server request user input while it handles a tool call. Form mode collects structured, non-sensitive data. URL mode asks for consent before opening an out-of-band flow, such as third-party authorization or payment.</p>
<pre><code class="language-mermaid">sequenceDiagram&#10;    participant User&#10;    participant Agent as Agent (MCP client)&#10;    participant Server as MCP server&#10;    participant Browser&#10;&#10;    Server-&gt;&gt;Agent: elicitation/create&#10;    Agent-&gt;&gt;User: Show server, reason, and input or URL&#10;    User-&gt;&gt;Agent: Submit, open, decline, or cancel&#10;    Agent-&gt;&gt;Browser: Open URL after consent (URL mode)&#10;    Agent-&gt;&gt;Server: accept, decline, or cancel&#10;    Server--&gt;&gt;Agent: Optional URL completion notification&#10;</code></pre>
<p>Register a handler for each mode your Agent supports in <code>onStart()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17678.md")</div>
<p>Connections advertise only the modes with configured handlers. An Agent without handlers advertises no elicitation capability, which lets the server use its fallback. The SDK stores the advertised modes with each MCP server registration so they survive Durable Object hibernation. Callback functions remain in memory and reattach when <code>onStart()</code> runs.</p>
<p>For implementation details and a browser forwarding pattern, refer to <a href="/agents/model-context-protocol/apis/client-api/#elicitation">MCP client elicitation</a>. The <a href="https://github.com/cloudflare/agents/tree/main/examples/mcp-client"><code>mcp-client</code></a> and <a href="https://github.com/cloudflare/agents/tree/main/examples/mcp-elicitation"><code>mcp-elicitation</code></a> examples implement both sides.</p>
<h4 id="2026-07-13-mcp-client-elicitation-upgrade">Upgrade</h4>
<p>To update to this release:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest" aria-label="Copy to clipboard">Copy</button></div></div>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-13">Jul 13, 2026</time><div>
<h2 id="post-2026-07-13-precursor-session-based-detection"><a href="/changelog/post/2026-07-13-precursor-session-based-detection/">Precursor introduces session-based bot detection</a></h2>
<div class="changelog-badges"><span>bots</span></div><div class="changelog-body"><p>Precursor is rolling out to all customers starting today. Precursor is client-side JavaScript that enables session-based bot detection.</p>
<p>You can <a href="https://blog.cloudflare.com/introducing-precursor">read the announcement blog</a> for background on why we built Precursor and how session-level behavioral detection works.</p>
<p>With Precursor enabled, Cloudflare can:</p>
<ul>
<li>Continuously evaluate behavioral signals across a session</li>
<li>Re-validate challenge clearance as behavior changes</li>
<li>Update bot scores with session context</li>
<li>Provide client-side visibility where none previously existed</li>
</ul>
<p>It integrates with existing protections, including Security Rules, and can be enabled directly from the Cloudflare dashboard with configurable modes to balance security and user experience.</p>
<img src="/images/precursor/enabling_precursor.gif" alt="Animated walkthrough of enabling Precursor in the Cloudflare dashboard" style="border:1px solid #e5e7eb;border-radius:6px;display:block;margin:16px 0;" />
<p>To learn more, refer to the <a href="/cloudflare-challenges/precursor/">Precursor documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-13">Jul 13, 2026</time><div>
<h2 id="post-2026-07-13-markdown-for-agents-header-preservation"><a href="/changelog/post/2026-07-13-markdown-for-agents-header-preservation/">Origin Content Signals for Markdown for Agents</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p><a href="/fundamentals/reference/markdown-for-agents/">Markdown for Agents</a> now preserves security- and cache-relevant response headers from your origin when converting HTML to Markdown:</p>
<ul>
<li>Markdown for Agents preserves security headers such as <code>Strict-Transport-Security</code> (HSTS), <code>Content-Security-Policy</code> (CSP), <code>X-Frame-Options</code>, <code>Set-Cookie</code>, and CORS headers (for example, <code>Access-Control-Allow-Origin</code>) on the converted response.</li>
<li>Caching headers (<code>Cache-Control</code>, <code>Expires</code>, <code>Age</code>) continue to pass through.</li>
</ul>
<p>Your origin's <a href="https://contentsignals.org/">Content Signals</a> policy is now authoritative. If your origin sets a <code>content-signal</code> header, Markdown for Agents preserves it. When the origin does not send one, Cloudflare adds the default <code>Content-Signal: ai-train=yes, search=yes, ai-input=yes</code>.</p>
<p>This release also fixes relative link resolution for directory-style base URLs (those ending in a trailing slash). Previously, relative links such as <code>../page/</code> could resolve one path segment too high and return a <code>404</code>. Links are now resolved correctly per <a href="https://www.rfc-editor.org/rfc/rfc3986#section-5.2.3">RFC 3986</a>.</p>
<p>Refer to our <a href="/fundamentals/reference/markdown-for-agents/">developer documentation</a> for more details.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-13">Jul 13, 2026</time><div>
<h2 id="post-2026-07-09-r2-data-catalog-read-only-tokens"><a href="/changelog/post/2026-07-09-r2-data-catalog-read-only-tokens/">R2 Data Catalog now supports read-only API tokens</a></h2>
<div class="changelog-badges"><span>r2</span><span>r2-data-catalog</span></div><div class="changelog-body"><p><a href="/r2-data-catalog/">R2 Data Catalog</a> now accepts read-only API tokens, so query engines and clients that only read data no longer need a read-write token. Previously, every catalog operation required an <strong>Admin Read &amp; Write</strong> token, which granted read-only clients more access than they needed.</p>
<p>You can now authenticate your Iceberg engine based on your workload:</p>
<ul>
<li><strong>Read-only</strong> operations (such as listing namespaces, loading tables, and querying data) work with an <strong>Admin Read only</strong> token (R2 Data Catalog read and R2 storage read).</li>
<li><strong>Write</strong> operations (such as creating or dropping tables and committing transactions) continue to require an <strong>Admin Read &amp; Write</strong> token.</li>
</ul>
<p>This lets you follow the principle of least privilege — for example, using a read-write token for the pipeline that writes to your tables and read-only tokens for engines like <a href="/r2-sql/">R2 SQL</a>, <a href="/r2-data-catalog/config-examples/duckdb/">DuckDB</a>, or <a href="/r2-data-catalog/config-examples/pyiceberg/">PyIceberg</a> that query them.</p>
<p>Note that credentials vended by the catalog inherit the R2 storage permissions of the token used to authenticate. To ensure read-only access to your underlying data, scope the R2 storage permission to read-only as well.</p>
<p>For details on choosing and creating the right token, refer to <a href="/r2-data-catalog/manage-catalogs/#authenticate-your-iceberg-engine">Authenticate your Iceberg engine</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-13">Jul 13, 2026</time><div>
<h2 id="post-2026-07-13-r2-data-catalog-manifest-optimization"><a href="/changelog/post/2026-07-13-r2-data-catalog-manifest-optimization/">R2 Data Catalog compaction now optimizes manifest files</a></h2>
<div class="changelog-badges"><span>r2-data-catalog</span></div><div class="changelog-body"><p><a href="/r2-data-catalog/">R2 Data Catalog</a>, a managed <a href="https://iceberg.apache.org/">Apache Iceberg</a> catalog built into R2, now automatically optimizes manifest files as part of <a href="/r2-data-catalog/table-maintenance/">compaction</a>.</p>
<p>Manifest files track the data files that make up an Iceberg table. As a table accumulates many small or fragmented manifests, query engines must read more metadata during query planning, which slows down queries even before any data is scanned.</p>
<p>When compaction runs, R2 Data Catalog now rewrites and clusters manifest files by partition as a best-effort pre-step. This consolidates fragmented manifests, reduces the number of manifests a query engine must open, and lowers metadata I/O overhead. Tables that are already well-clustered are skipped, so the operation only runs when it provides a benefit.</p>
<p>This happens automatically for tables with compaction enabled — no configuration changes are required.</p>
<p>For more information, refer to <a href="/r2-data-catalog/table-maintenance/">Table maintenance</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-10">Jul 10, 2026</time><div>
<h2 id="post-2026-07-10-source-code-detection-improvements"><a href="/changelog/post/2026-07-10-source-code-detection-improvements/">Source code detection improvements</a></h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p>Data Loss Prevention (DLP) source code detection now focuses on identifying whole source code file uploads and downloads. Previously, source code detection performed partial scans resulting in a higher rate of false positives. Since only whole source code files are evaluated, code embedded in other content — such as chat messages, documentation, or code samples — is no longer flagged as source code, removing a common source of false positives.</p>
<p>Source code detection requires a minimum of 500 characters to evaluate a file. Files below this threshold are not flagged to reduce noise. This threshold filters out small fragments that lack enough context for reliable classification.</p>
<p>Enable and set <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/advanced-settings/#confidence-thresholds">confidence levels</a> to tune match sensitivity. A higher confidence level reduces false positives by requiring stronger signals that the content is truly source code. A lower confidence level catches more files at the cost of additional noise.</p>
<p>Source code detection applies to standalone source code files in <a href="/cloudflare-one/traffic-policies/http-policies/">Gateway HTTP policies</a>. It does not detect source code embedded within other file types or payloads, such as <code>.docx</code> files or chat messages.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#source-code">Source Code predefined profiles</a>.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/7/">Previous</a><span>Page 8 of 50</span><a class="pagination-next" rel="next" href="/changelog/9/">Next</a></nav>
</div>
