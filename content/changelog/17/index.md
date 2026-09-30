---
cp9:
  canonical: https://developers.cloudflare.com/changelog/17/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 17 | Cloudflare Docs
  head_html: <title>Changelog - page 17 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/17/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 17"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/17/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/17/#page","headline":"Changelog - page 17 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/17/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/17/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-04-30">Apr 30, 2026</time><div>
<h2 id="post-2026-04-30-emergency-waf-release"><a href="/changelog/post/2026-04-30-emergency-waf-release/">WAF Release - 2026-04-30 - Emergency</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This emergency release introduces a new rule to block a cPanel &amp; WHM Authentication Bypass related to CVE-2026-41940.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-41940: A critical authentication bypass vulnerability in cPanel &amp; WHM allows unauthenticated remote attackers to bypass authentication mechanisms and gain unauthorized administrative access to the web hosting control panel. This vulnerability affects the session validation logic, enabling attackers to craft malicious requests that circumvent normal authentication checks.</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation allows unauthenticated attackers to gain administrative control over affected cPanel &amp; WHM installations. This leads to complete server compromise, potential theft or manipulation of hosted data, and significant service disruption across managed environments.</p>
<p>We strongly recommend applying official vendor patches for cPanel &amp; WHM immediately to address the underlying vulnerability.</p>
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
				<code class="nb-rule-id" title="fb29b1b660864285a5ebac86eb2b9e2f">eb2b9e2f</code>
</td>
<td>N/A</td>
<td>cPanel - Auth Bypass - CVE:CVE-2026-41940</td>
<td>N/A</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-30">Apr 30, 2026</time><div>
<h2 id="post-2026-04-30-rum-navigation-types"><a href="/changelog/post/2026-04-30-rum-navigation-types/">Web Analytics adds Navigation Type filtering and reporting</a></h2>
<div class="changelog-badges"><span>web-analytics</span></div><div class="changelog-body"><p>Cloudflare Web Analytics now supports <strong>Navigation Type</strong> reporting and filtering.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-29">Apr 29, 2026</time><div>
<h2 id="post-2026-04-29-dex-tests-to-auth"><a href="/changelog/post/2026-04-29-dex-tests-to-auth/">Digital experience tests to authenticated resources and enhanced configuration</a></h2>
<div class="changelog-badges"><span>dex</span></div><div class="changelog-body"><p><a href="/cloudflare-one/insights/dex/tests/">Digital experience tests</a> now support testing applications protected by Cloudflare Access or third-party authentication. All authentication secrets are managed via <a href="/secrets-store/">Cloudflare Secret Store</a>.</p>
<p>Digital experience tests also have enhanced configuration options including:</p>
<ul>
<li>New HTTP methods (DELETE, PATCH, POST, PUT)</li>
<li>Secret Store headers, custom plain text headers, and custom request bodies</li>
<li>Advanced settings: follow redirects, response bodies, response headers, and allow untrusted certificates</li>
</ul>
<p><img src="/assets/upstream/images/changelog/dex/dex_test_auth_config.png" alt="Digital experience test configuration for Cloudflare Access applications" />
<img src="/assets/upstream/images/changelog/dex/dex_test_enhanced_config.png" alt="Digital experience enhanced test configuration" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-29">Apr 29, 2026</time><div>
<h2 id="post-2026-04-29-instant-bank-payments-via-link"><a href="/changelog/post/2026-04-29-instant-bank-payments-via-link/">Instant Bank Payments via Link</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>You can now pay for Cloudflare services directly from your bank account using <a href="/billing/payment-methods/instant-bank-payments-link/">Instant Bank Payments via Link</a>.</p>
<h4 id="2026-04-29-instant-bank-payments-via-link-what-changed">What changed</h4>
<p><a href="https://link.co/">Link</a> now supports bank account payments in addition to cards. If you have a bank account saved in Link, it appears as a payment option at checkout. If not, you can connect one during the checkout flow.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-04-29-instant-bank-payments-link.png" alt="Instant Bank Payments via Link at checkout" /></p>
<h4 id="2026-04-29-instant-bank-payments-via-link-how-to-use-it">How to use it</h4>
<ol>
<li>During checkout, select your bank account from your saved Link payment methods.</li>
<li>Confirm the payment.</li>
</ol>
<p>After your first Link authentication, your bank account is available for future purchases without re-entering details.</p>
<h4 id="2026-04-29-instant-bank-payments-via-link-who-is-eligible">Who is eligible</h4>
<p>Instant Bank Payments via Link is available to US-based self-serve accounts across all Cloudflare products. Your existing cards remain available at checkout.</p>
<p>Bank-based Link payments appear in your billing history with the payment method shown as <code>link</code> and last four digits as <code>0000</code>. For details, refer to the <a href="/billing/payment-methods/instant-bank-payments-link/">Instant Bank Payments via Link documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-29">Apr 29, 2026</time><div>
<h2 id="post-2026-04-29-gateway-authorization-proxy-pac-files-ga"><a href="/changelog/post/2026-04-29-gateway-authorization-proxy-pac-files-ga/">Gateway Authorization Proxy and hosted PAC files are now generally available</a></h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>The <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#authorization-endpoint">Gateway Authorization Proxy</a> and <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#create-a-hosted-pac-file">hosted PAC files</a> are now generally available for all plan types.</p>
<p>Authorization proxy endpoints add an identity-aware option alongside the existing <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/#source-ip-endpoint">source IP proxy endpoints</a>, using <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> authentication to verify who a user is before applying Gateway filtering — without installing the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a>. Cloudflare-hosted PAC files let you create and distribute PAC files directly from Cloudflare One on Cloudflare's global network.</p>
<p>These features are ideal for environments where deploying a device client is not an option, such as virtual desktops (VDI) or compliance-restricted endpoints.</p>
<p>To get started, refer to the <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">proxy endpoints documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-29">Apr 29, 2026</time><div>
<h2 id="post-2026-04-29-hyperdrive-vpc-private-databases"><a href="/changelog/post/2026-04-29-hyperdrive-vpc-private-databases/">Hyperdrive support for private databases with Workers VPC</a></h2>
<div class="changelog-badges"><span>hyperdrive</span></div><div class="changelog-body"><p>You can now connect Hyperdrive to a private database through a <a href="/workers-vpc/">Workers VPC service</a>. This is the recommended way to connect Hyperdrive to a private database that is not exposed to the public Internet.</p>
<p>When creating a Hyperdrive configuration in the Cloudflare dashboard, choose <strong>Connect to private database</strong> and then <strong>Workers VPC</strong>. From there, you can select an existing VPC service or create a new one inline by picking a Cloudflare Tunnel and entering your origin host and TCP port.</p>
<p>You can also create a Hyperdrive configuration backed by a Workers VPC service from the command line:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler hyperdrive create my-vpc-database \&#10;  &#45;-service-id &lt;YOUR_VPC_SERVICE_ID&gt; \&#10;  &#45;-database &lt;DATABASE_NAME&gt; \&#10;  &#45;-user &lt;DATABASE_USER&gt; \&#10;  &#45;-password &lt;DATABASE_PASSWORD&gt; \&#10;  &#45;-scheme postgresql&#10;</code></pre>
<p>Workers VPC services are reusable across Hyperdrive configurations and can also be bound directly to Workers, so you can share the same private connection across multiple products.</p>
<p>To get started, refer to <a href="/hyperdrive/configuration/connect-to-private-database-vpc/">Connect Hyperdrive to a private database using Workers VPC</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-28">Apr 28, 2026</time><div>
<h2 id="post-2026-04-28-dex-internet-outage-notification"><a href="/changelog/post/2026-04-28-dex-internet-outage-notification/">Internet outage notifications for devices</a></h2>
<div class="changelog-badges"><span>dex</span></div><div class="changelog-body"><p><a href="/cloudflare-one/insights/dex/">Digital Experience</a> will display a dashboard notification when an Internet outage or traffic anomaly may impact a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> device based on its geographic location or network connection.</p>
<p>This Internet outage and traffic anomaly data is pulled from <a href="https://radar.cloudflare.com/">Cloudflare Radar</a>. All Internet outage and traffic anomaly observations can be viewed in the <a href="https://radar.cloudflare.com/outage-center">Radar Outage Center</a>.</p>
<p><img src="/assets/upstream/images/changelog/dex/dex_radar_ux_notification.png" alt="Digital Experience Monitoring dashboard notification for Internet outage impacting Cloudflare One Client devices" />
<img src="/assets/upstream/images/changelog/dex/dex_radar_analytics.png" alt="Digital Experience Monitoring dashboard analytics for Internet outage impacting Cloudflare One Client devices" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-28">Apr 28, 2026</time><div>
<h2 id="post-2026-04-28-dex-speed-test"><a href="/changelog/post/2026-04-28-dex-speed-test/">Cloudflare One Client speed tests</a></h2>
<div class="changelog-badges"><span>dex</span></div><div class="changelog-body"><p>IT teams can now remotely run speed tests from the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> to Cloudflare's network edge.</p>
<p>Each speed test includes the following metrics:</p>
<ul>
<li>Internet speed: download and upload throughput</li>
<li>Latency: download, upload, unloaded latency, and jitter</li>
<li>Network quality score: video streaming, webchat/real-time communication (RTC)</li>
</ul>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Digital experience</strong> &gt; <strong>Diagnostics</strong> and select <strong>Run diagnostics</strong> to use the feature today.</p>
<p><img src="/assets/upstream/images/changelog/dex/dex_speed_test.png" alt="Cloudflare One client speed test result" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-28">Apr 28, 2026</time><div>
<h2 id="post-2026-04-28-detection-entries-outside-profiles"><a href="/changelog/post/2026-04-28-detection-entries-outside-profiles/">Create and manage DLP detection entries outside of profiles</a></h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p>You can now create, view, and manage DLP detection entries outside of profiles.</p>
<p>Detection entries are no longer hidden inside individual profiles. Administrators can manage detection entries directly from the <strong>Detection entries</strong> section and use them in custom DLP profiles.</p>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/">Configure detection entries</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-28">Apr 28, 2026</time><div>
<h2 id="post-2026-04-28-pii-record-profile"><a href="/changelog/post/2026-04-28-pii-record-profile/">Detect PII records with a new predefined DLP profile</a></h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p>Cloudflare DLP now includes a new predefined profile designed to detect PII records that contain multiple types of personal data: <strong>Personally Identifiable Information (PII) Record</strong>.</p>
<p>Most predefined and custom DLP profiles match when any enabled detection entry matches. The <strong>Personally Identifiable Information (PII) Record</strong> profile is different. It only matches when at least three unique detection entries are found in close proximity, which reduces false positives from standalone values that may not represent a real PII record.</p>
<p>Detection entries included in the profile:</p>
<ul>
<li>AU Passport Number</li>
<li>American Express Card Number</li>
<li>Diners Club Card Number</li>
<li>US Driver's License Number</li>
<li>Email Address</li>
<li>Full Name</li>
<li>US Mailing Address</li>
<li>Mastercard Card Number</li>
<li>US Individual Tax Identification Number (ITIN)</li>
<li>US Passport Number</li>
<li>US Phone Number</li>
<li>Union Pay Card Number</li>
<li>United States SSN Numeric Detection</li>
<li>Visa Card Number</li>
</ul>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">predefined DLP profiles</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-28">Apr 28, 2026</time><div>
<h2 id="post-2026-04-28-enforce-dns-only"><a href="/changelog/post/2026-04-28-enforce-dns-only/">Account-level enforce DNS-only</a></h2>
<div class="changelog-badges"><span>dns</span></div><div class="changelog-body"><p>You can now disable Cloudflare's reverse proxy across all zones in your account simultaneously using the new <code>enforce_dns_only</code> setting. When enabled, Cloudflare responds to DNS queries for all proxied records with your origin IP addresses instead of Cloudflare's anycast IPs.
This account-level kill switch is designed for incident response scenarios where you need to quickly route traffic directly to your origin servers.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17717.md")</aside>
<h4 id="2026-04-28-enforce-dns-only-key-characteristics">Key characteristics</h4>
<ul>
<li><strong>Account-level</strong> — Affects all zones in the account simultaneously with a single API call.</li>
<li><strong>Non-destructive</strong> — Does not modify your DNS records. Disabling the setting restores normal proxy behavior.</li>
<li><strong>API-only</strong> — Available through the API only, not in the Cloudflare dashboard.</li>
</ul>
<h4 id="2026-04-28-enforce-dns-only-what-s-affected">What's affected</h4>
<p><strong>Included:</strong> Standard proxied A, AAAA, and CNAME records, Load Balancing records, and records matching Worker routes.</p>
<p><strong>Excluded:</strong> Spectrum applications, Cloudflare Tunnel CNAMEs, R2 custom domains, Web3 gateways, and Workers custom domains continue to operate normally.</p>
<h4 id="2026-04-28-enforce-dns-only-before-you-enable">Before you enable</h4>
<ul>
<li>Verify your origin servers can handle direct traffic without Cloudflare's caching and filtering.</li>
<li>Review which origin IPs will become publicly visible through DNS queries.</li>
<li>Test the API in a staging account before relying on it for incident response.</li>
</ul>
<h4 id="2026-04-28-enforce-dns-only-availability">Availability</h4>
<p>Available via API to all Cloudflare customers.</p>
<p>For information on how to use it, refer to <a href="/dns/proxy-status/enforce-dns-only/">Enforce DNS-only developer documentation</a> .</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-28">Apr 28, 2026</time><div>
<h2 id="post-2026-04-28-improved-queues-metrics"><a href="/changelog/post/2026-04-28-improved-queues-metrics/">Realtime backlog metrics now available for Queues</a></h2>
<div class="changelog-badges"><span>queues</span></div><div class="changelog-body"><p><a href="/queues/">Queues</a>, Cloudflare's managed message queue, now exposes realtime backlog metrics via the dashboard, REST API, and JavaScript API. Three new fields are available:</p>
<ul>
<li><strong><code>backlog_count</code></strong> — the number of unacknowledged messages in the queue</li>
<li><strong><code>backlog_bytes</code></strong> — the total size of those messages in bytes</li>
<li><strong><code>oldest_message_timestamp_ms</code></strong> — the timestamp of the oldest unacknowledged message</li>
</ul>
<p>The following endpoints also now include a <code>metadata.metrics</code> object on the result field after successful message consumption:</p>
<ul>
<li><code>/accounts/{account_id}/queues/{queue_id}/messages/pull</code></li>
<li><code>/accounts/{account_id}/queues/{queue_id}/messages</code></li>
<li><code>/accounts/{account_id}/queues/{queue_id}/messages/batch</code></li>
</ul>
<h4 id="2026-04-28-improved-queues-metrics-javascript-apis">Javascript APIs</h4>
<p>Call <code>env.QUEUE.metrics()</code> to get realtime backlog metrics:</p>
<pre tabindex="0"><code class="language-ts">const {&#10;	backlogCount, // number&#10;	backlogBytes, // number&#10;	oldestMessageTimestamp, // Date | undefined&#10;} = await env.QUEUE.metrics();&#10;</code></pre>
<p><code>env.QUEUE.send()</code> and <code>env.QUEUE.sendBatch()</code> also now return a metrics object on the response.</p>
<p>You can also query these fields via the <a href="/analytics/graphql-api/">GraphQL Analytics API</a> or view realtime backlog on the <a href="https://dash.cloudflare.com/?to=/:account/workers/queues">dashboard</a>.</p>
<p><img src="/assets/upstream/images/changelog/queues/2026-04-28-queues-metrics.png" alt="Queues realtime backlog" /></p>
<p>For more information, refer to <a href="/queues/observability/metrics/">Queues metrics</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-28">Apr 28, 2026</time><div>
<h2 id="post-2026-04-28-direct-support-navigation"><a href="/changelog/post/2026-04-28-direct-support-navigation/">Direct access to Support from the dashboard</a></h2>
<div class="changelog-badges"><span>support</span></div><div class="changelog-body"><h4 id="2026-04-28-direct-support-navigation-direct-access-to-support-from-the-dashboard">Direct access to Support from the dashboard</h4>
<p>The <strong>Support</strong> button in the dashboard global navigation header now takes you directly to the <a href="https://support.cloudflare.com">Cloudflare Support Portal</a>, eliminating the previous dropdown menu.</p>
<p>This change ensures that when you need help, you spend less time navigating the UI and more time getting the answers you need.</p>
<h4 id="2026-04-28-direct-support-navigation-what-changed">What changed?</h4>
<ul>
<li><strong>Previous behavior</strong>: Selecting <strong>? Support</strong> opened a dropdown menu with various links (Help Center, Cloudflare Community, etc.).</li>
<li><strong>New behavior</strong>: Selecting <strong>Support</strong> immediately redirects your current tab to the Support Portal.</li>
</ul>
<p>To learn more about the resources available to you, refer to the <a href="https://developers.cloudflare.com/support/contacting-cloudflare-support/">Cloudflare Support documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-27">Apr 27, 2026</time><div>
<h2 id="post-2026-04-27-cache-response-rules-zone-versioning"><a href="/changelog/post/2026-04-27-cache-response-rules-zone-versioning/">Cache Response Rules now support zone versioning</a></h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>Cache Response Rules now work with <a href="/version-management/">Version Management</a>. You can version response-phase cache settings and promote them through environments, just like Cache Rules and other supported configurations.</p>
<h4 id="2026-04-27-cache-response-rules-zone-versioning-what-changed">What changed</h4>
<p>Previously, Cache Response Rules were excluded from zone versioning. Any response-phase rule you created applied globally across all environments with no way to test changes in staging first. Cache Rules already supported versioning, but the response phase, where you modify <code>Cache-Control</code> directives, manage cache tags, and strip headers, did not.</p>
<p>Cache Response Rules are now fully integrated with Version Management. You can create or modify response-phase rules within a version, and those changes stay scoped to that version until promoted.</p>
<h4 id="2026-04-27-cache-response-rules-zone-versioning-benefits">Benefits</h4>
<ul>
<li><strong>Safe rollout of cache behavior changes</strong>: Test response-phase rules in a staging environment before promoting to production. Catch unintended caching side effects early.</li>
<li><strong>Parity with Cache Rules</strong>: Cache Response Rules now follow the same versioning workflow as Cache Rules, so you can manage all cache configuration through a single promotion pipeline.</li>
<li><strong>Independent environment control</strong>: Run different response-phase cache settings per environment. For example, strip <code>Set-Cookie</code> headers in staging to validate cacheability without affecting production traffic.</li>
</ul>
<h4 id="2026-04-27-cache-response-rules-zone-versioning-get-started">Get started</h4>
<p>Configure Cache Response Rules in the <a href="https://dash.cloudflare.com/?to=/:account/:zone/caching/cache-rules">Cloudflare dashboard</a> under <strong>Caching</strong> &gt; <strong>Cache Rules</strong>, or via the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a>. For more details, refer to the <a href="/cache/how-to/cache-response-rules/">Cache Response Rules documentation</a> and the <a href="/version-management/">Version Management documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-27">Apr 27, 2026</time><div>
<h2 id="post-2026-04-27-structured-responses-for-5xx-errors"><a href="/changelog/post/2026-04-27-structured-responses-for-5xx-errors/">Structured error responses for Cloudflare 5xx errors</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Cloudflare-generated 5xx error responses now return structured JSON and Markdown when agents request them, matching the format already available for 1xxx errors. Responses follow <a href="https://www.rfc-editor.org/rfc/rfc9457">RFC 9457 (Problem Details for HTTP APIs)</a> and include a <code>Retry-After</code> HTTP header on retryable codes.</p>
<h4 id="2026-04-27-structured-responses-for-5xx-errors-changes">Changes</h4>
<p><strong>5xx coverage.</strong> Ten Cloudflare-generated error codes (500, 502, 504, 520-526) now serve structured responses. These are errors Cloudflare itself generates when it cannot reach or understand the origin server. Origin-generated 5xx responses that Cloudflare passes through are not affected.</p>
<p><strong>Fault attribution.</strong> The <code>error_category</code> field tells agents where the fault lies:</p>
<ul>
<li><code>origin</code> (502, 504, 520-524) — the origin server is responsible. Transient; retry with the backoff in <code>retry_after</code>.</li>
<li><code>cloudflare</code> (500) — Cloudflare's fault, not the website or the request. Short retry.</li>
<li><code>ssl</code> (525, 526) — the origin's TLS configuration is broken. Do not retry.</li>
</ul>
<p><strong>Retry-After header.</strong> Retryable codes (500, 502, 504, 520-524) include a <code>Retry-After</code> HTTP header matching the <code>retry_after</code> body field. Non-retryable codes (525, 526) do not include the header.</p>
<h4 id="2026-04-27-structured-responses-for-5xx-errors-negotiation-behavior">Negotiation behavior</h4>
<table>
<thead>
<tr>
<th>Request header sent</th>
<th>Response format</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Accept: application/json</code></td>
<td>JSON (<code>application/json</code> content type)</td>
</tr>
<tr>
<td><code>Accept: application/problem+json</code></td>
<td>JSON (<code>application/problem+json</code> content type)</td>
</tr>
<tr>
<td><code>Accept: application/json, text/markdown;q=0.9</code></td>
<td>JSON</td>
</tr>
<tr>
<td><code>Accept: text/markdown</code></td>
<td>Markdown</td>
</tr>
<tr>
<td><code>Accept: text/markdown, application/json</code></td>
<td>Markdown (equal <code>q</code>, first-listed wins)</td>
</tr>
<tr>
<td><code>Accept: */*</code></td>
<td>HTML (default)</td>
</tr>
</tbody>
</table>
<h4 id="2026-04-27-structured-responses-for-5xx-errors-availability">Availability</h4>
<p>Available now for all zones on all plans.</p>
<h4 id="2026-04-27-structured-responses-for-5xx-errors-get-started">Get started</h4>
<p>Get JSON response for error 522:</p>
<pre tabindex="0"><code class="language-bash">curl -s --compressed -H &quot;Accept: application/json&quot; -A &quot;TestAgent/1.0&quot; -H &quot;Accept-Encoding: gzip, deflate&quot; &quot;&lt;YOUR_DOMAIN&gt;/cdn-cgi/error/522&quot; | jq .&#10;</code></pre>
<p>Check presence of the <code>Retry-After</code> HTTP header associated with the JSON response for error 521:</p>
<pre tabindex="0"><code class="language-bash">curl -s --compressed -D - -o /dev/null -H &quot;Accept: application/json&quot; -A &quot;TestAgent/1.0&quot; -H &quot;Accept-Encoding: gzip, deflate&quot; &quot;&lt;YOUR_DOMAIN&gt;/cdn-cgi/error/521&quot; | grep -i retry-after&#10;</code></pre>
<p>References:</p>
<ul>
<li><a href="https://www.rfc-editor.org/rfc/rfc9457">RFC 9457 — Problem Details for HTTP APIs</a></li>
<li><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/">Cloudflare 5xx error documentation</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-27">Apr 27, 2026</time><div>
<h2 id="post-2026-04-27-resource-tagging-public-beta"><a href="/changelog/post/2026-04-27-resource-tagging-public-beta/">Resource Tagging enters public beta</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>resource-tagging</span></div><div class="changelog-body"><p>Resource Tagging is now in public beta and rolling out to all Cloudflare accounts over the coming days. You can attach custom key-value metadata to your Cloudflare resources and query across your entire account to find what you need.</p>
<h4 id="2026-04-27-resource-tagging-public-beta-what-s-included">What's included</h4>
<ul>
<li><strong>Broad resource type support</strong> — Tag zones, custom hostnames, Cloudflare Tunnels, Workers, D1 databases, R2 buckets, KV namespaces, Durable Object namespaces, Queues, Stream videos, Images, Access applications, Gateway rules, AI Gateways, and more. Refer to the <a href="/resource-tagging/reference/resource-types/">full list of supported resource types</a>.</li>
<li><strong>Powerful filtering</strong> — Query tagged resources using AND/OR logic, negation, and key-only matching. Combine up to 20 filters per query to build precise resource views.</li>
<li><strong>Account and zone-level endpoints</strong> — Full CRUD operations across both scopes.</li>
<li><strong>Token-based authentication</strong> — Tagging supports <a href="/fundamentals/api/get-started/account-owned-tokens/">Account Owned Tokens</a> that persist independently of individual users, so your automation keeps running through credential rotations and team changes.</li>
<li><strong>Flexible role support</strong> — Super Administrators, Workers Admins, and Tag Admins can all manage tags.</li>
</ul>
<h4 id="2026-04-27-resource-tagging-public-beta-api-first-by-design">API-first by design</h4>
<p>The API is the primary interface for Resource Tagging and the recommended path for all workflows — scripting tag assignments, building CI/CD pipelines, or integrating with your infrastructure-as-code toolchain.</p>
<h4 id="2026-04-27-resource-tagging-public-beta-dashboard-ui">Dashboard UI</h4>
<p>You can also view and manage tagged resources directly in the Cloudflare dashboard. Navigate to <strong>Manage Account</strong> &gt; <strong>Resource Tagging</strong> to see all tagged resources across your account, filter by resource name or tag, and add or edit tags inline.</p>
<p><img src="/assets/upstream/images/changelog/resource-tagging/tagged-resources-dashboard.png" alt="Tagged Resources dashboard" /></p>
<h4 id="2026-04-27-resource-tagging-public-beta-what-s-coming-next">What's coming next</h4>
<p>In future releases, expect support for additional resource types across the Cloudflare platform, tag-based access control policies for scoping user permissions to tagged resources, billing and usage attribution by tag for breaking down costs by team, project, or environment, and Terraform provider support for managing tags declaratively.</p>
<h4 id="2026-04-27-resource-tagging-public-beta-current-limitations">Current limitations</h4>
<ul>
<li><code>PUT</code> replaces all tags on a resource (no partial update). Use the <a href="/resource-tagging/how-to/manage-tags/#add-a-single-tag">GET, merge, PUT workflow</a> to modify individual tags safely.</li>
<li><code>DELETE</code> removes all tags from a resource. To remove a single tag, PUT the remaining tags back.</li>
<li>Querying tags for a resource that has never been tagged returns <code>500</code> instead of <code>404</code>. This is a known beta limitation.</li>
</ul>
<p>To get started, refer to the <a href="/resource-tagging/">Resource Tagging documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-27">Apr 27, 2026</time><div>
<h2 id="post-2026-04-27-unified-workspace-brand-protection"><a href="/changelog/post/2026-04-27-unified-workspace-brand-protection/">Unified workspace for Brand Protection</a></h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p>We have introduced a unified investigation workspace within Brand Protection to help analysts manage complex brand portfolios. Instead of jumping between individual queries, you can now consolidate your workflow into a single, cohesive view.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-27">Apr 27, 2026</time><div>
<h2 id="post-2026-04-27-waf-release"><a href="/changelog/post/2026-04-27-waf-release/">WAF Release - 2026-04-27</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's release focuses on new improvements to enhance coverage.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Existing rule enhancements have been deployed to improve detection resilience against broad classes of web attacks and strengthen behavioral coverage.</li>
</ul>
<p><strong>Continuous Rule Improvements</strong></p>
<p>We are continuously refining our managed rules to provide more resilient protection and deeper insights into attack patterns. To ensure an optimal security posture, we recommend consistently monitoring the Security Events dashboard and adjusting rule actions as these enhancements are deployed.</p>
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
				<code class="nb-rule-id" title="d866f980582748568385b94480cec1dd">80cec1dd</code>
</td>
<td>N/A</td>
<td>PostgreSQL - SQLi - COPY - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.  This rule is merged into the original rule
				"PostgreSQL - SQLi - COPY - Body (ID:{" "}
				<code class="nb-rule-id" title="705a6b5569d5472596910e3ce7265a4e">e7265a4e</code>). The rule previously known as "PostgreSQL - SQLi - COPY" is now renamed to "PostgreSQL - SQLi - COPY - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="71d133c374d94559aa9fdf042903de89">2903de89</code>
</td>
<td>N/A</td>
<td>PostgreSQL - SQLi - COPY - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>		
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="9f1b1b7fd28a401b9d5c172d1036cfa6">1036cfa6</code>
</td>
<td>N/A</td>
<td>PostgreSQL - SQLi - COPY - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>  
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="8e40416659334b8ba789365755ff389e">55ff389e</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR MAKE_SET/ELT - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - AND/OR MAKE_SET/ELT - Body" (ID:{" "}
				<code class="nb-rule-id" title="0f41a593c8fe42c38a26f709252d3934">252d3934</code>). The rule previously known as "SQLi - AND/OR MAKE_SET/ELT" is now renamed to "SQLi - AND/OR MAKE_SET/ELT - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1e0d4372ee1e41b9804b2d5c346487f9">346487f9</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR MAKE_SET/ELT - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>		
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d2c961a164a64cf6b871c9511ac6ceca">1ac6ceca</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR MAKE_SET/ELT - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="4dacc0e6f32d4c5da3c2293edd471337">dd471337</code>
</td>
<td>N/A</td>
<td>SQLi - Common Patterns - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - Common Patterns - Body" (ID:{" "}
				<code class="nb-rule-id" title="98f746d07a6d48ab9dae669acb5d0b9b">cb5d0b9b</code>). The rule previously known as "SQLi - Common Patterns" is now renamed to "SQLi - Common Patterns - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="53a374379f2e41e9934791c1975c07b7">975c07b7</code>
</td>
<td>N/A</td>
<td>SQLi - Common Patterns - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>		
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="9efedebfc371443f9fe7308605b1b06b">05b1b06b</code>
</td>
<td>N/A</td>
<td>SQLi - Common Patterns - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d53a791496d64700870334f4dd0ba3c7">dd0ba3c7</code>
</td>
<td>N/A</td>
<td>SQLi - Equation - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - Equation - Body" (ID:{" "}
				<code class="nb-rule-id" title="e7691e1e4f4d4769909f3df6c2eb3e7f">c2eb3e7f</code>). The rule previously known as "SQLi - Equation" is now renamed to "SQLi - Equation - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="46efbd3496e64c3f902ad33d3d1c2384">3d1c2384</code>
</td>
<td>N/A</td>
<td>SQLi - Equation - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>		
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="46b937649a424b7ead90f6d0e1149ea6">e1149ea6</code>
</td>
<td>N/A</td>
<td>SQLi - Equation - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="04d9182545f54ba8a4fa29fe205adbb0">205adbb0</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR Digit Operator Digit - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - AND/OR Digit Operator Digit - Body" (ID:{" "}
				<code class="nb-rule-id" title="762dd334ed0b4273816e3ff13893c564">3893c564</code>). The rule previously known as "SQLi - AND/OR Digit Operator Digit" is now renamed to "SQLi - AND/OR Digit Operator Digit - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="a24e7c15503948bc8766481aad2abbaa">ad2abbaa</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR Digit Operator Digit - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="0c55eb362df64f92a85aa46753acbc0d">53acbc0d</code>
</td>
<td>N/A</td>
<td>SQLi - AND/OR Digit Operator Digit - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="18c9879b7e184c559d23c1652b45a97d">2b45a97d</code>
</td>
<td>N/A</td>
<td>SQLi - Benchmark Function - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - Benchmark Function - Body" (ID:{" "}
				<code class="nb-rule-id" title="ac4e9ebfb43a4f3998f6072d2ebc44ad">2ebc44ad</code>). The rule previously known as "SQLi - Benchmark Function" is now renamed to "SQLi - Benchmark Function - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="2adbc36c52324efcb4681b829889aadc">9889aadc</code>
</td>
<td>N/A</td>
<td>SQLi - Benchmark Function - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>		
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="69564af3bc54406080deed72491b28e9">491b28e9</code>
</td>
<td>N/A</td>
<td>SQLi - Benchmark Function - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="94b1646f0b0b46ec9b96f7742aa649de">2aa649de</code>
</td>
<td>N/A</td>
<td>SQLi - Comparison - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - Comparison - Body" (ID:{" "}
				<code class="nb-rule-id" title="8166da327a614849bfa29317e7907480">e7907480</code>). The rule previously known as "SQLi - Comparison" is now renamed to "SQLi - Comparison - Body".
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="455ce87681bd4200bf53456c39e3e013">39e3e013</code>
</td>
<td>N/A</td>
<td>SQLi - Comparison - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="8152816062ed47f69be0f907f4bdb492">f4bdb492</code>
</td>
<td>N/A</td>
<td>SQLi - Comparison - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="d5afd403a0544248b829fe5da1ff3b34">a1ff3b34</code>
</td>
<td>N/A</td>
<td>SQLi - String Concatenation - Body - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection. This rule is merged into the original rule "SQLi - String Concatenation - Headers" (ID:{" "}
				<code class="nb-rule-id" title="3b0c61407d0b4f7d87e516472116d2fe">2116d2fe</code>).The rule previously known as "SQLi - String Concatenation - Headers" is now renamed to "SQLi - String Concatenation - Body". </td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="cb0ec290ee454138abe18b750d0e6c3b">0d0e6c3b</code>
</td>
<td>N/A</td>
<td>SQLi - String Concatenation - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.(Former Id was{" "}
				<code class="nb-rule-id" title="380099df2bb2469c91ebbb7b846d1940">846d1940</code>)</td>
</tr>		
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="c46d9097c9ef419aa4d9f10626cc211f">26cc211f</code>
</td>
<td>N/A</td>
<td>SQLi - String Concatenation - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection. (Former Id was{" "}
				<code class="nb-rule-id" title="bd19397228404b85aa3797238fae8c84">8fae8c84</code>)</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="6542d36980cf4018b4d5e2bfeacc78ab">eacc78ab</code>
</td>
<td>N/A</td>
<td>SQLi - SELECT Expression - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - SELECT Expression - Body" (ID:{" "}
				<code class="nb-rule-id" title="00da180570d34b5bae2121acd0023a36">d0023a36</code>). The rule previously known as "SQLi - SELECT Expression" is now renamed to "SQLi - SELECT Expression - Body".
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="4073f7b575ff45dfb7621b43630bb223">630bb223</code>
</td>
<td>N/A</td>
<td>SQLi - SELECT Expression - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="2721e3184d50466ea637e9afdcd6efb5">dcd6efb5</code>
</td>
<td>N/A</td>
<td>SQLi - SELECT Expression - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="7ecca84c08aa4aad9b5a7bda18c47cea">18c47cea</code>
</td>
<td>N/A</td>
<td>SQLi - ORD and ASCII - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"SQLi - ORD and ASCII- Body" (ID:{" "}
				<code class="nb-rule-id" title="2fc38b34a9d744d2a3cbcc41d0d207f9">d0d207f9</code>). The rule previously known as "SQLi - ORD and ASCII" is now renamed to "SQLi - ORD and ASCII- Body".
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="f6d10e10c9514eb49dcc2122bdb1618f">bdb1618f</code>
</td>
<td>N/A</td>
<td>SQLi - ORD and ASCII - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
                <code class="nb-rule-id" title="60704f5c5513425c94cf77031d0906b6">1d0906b6</code>
</td>
<td>N/A</td>
<td>SQLi - ORD and ASCII - Headers</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="700613b191d3479ea2782b4e9fe4eff5">9fe4eff5</code>
</td>
<td>N/A</td>
<td>SQLi - Destructive Operations</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>					
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-24">Apr 24, 2026</time><div>
<h2 id="post-2026-04-24-nsl-all-onramps"><a href="/changelog/post/2026-04-24-nsl-all-onramps/">Network Session Logs now available for all on-ramps</a></h2>
<div class="changelog-badges"><span>gateway</span><span>cloudflare-one</span></div><div class="changelog-body"><p><a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/">Zero Trust Network Session Logs</a> are now generated for all traffic proxied through Cloudflare Gateway, regardless of on-ramp type. This includes traffic from <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">proxy endpoints (PAC files)</a> and <a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a> egress — on-ramps that previously did not generate session logs.</p>
<p>Customers who already consume the <code>zero_trust_network_sessions</code> dataset via <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a> or <a href="/log-explorer/">Log Explorer</a> may see increased log volume if they use these on-ramps.</p>
<p>For field definitions, refer to <a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/">Zero Trust Network Session Logs</a>. For traffic analysis, refer to <a href="/cloudflare-one/insights/analytics/network-sessions/">Network session analytics</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-24">Apr 24, 2026</time><div>
<h2 id="post-2026-04-24-terraform-v5.19.0-provider"><a href="/changelog/post/2026-04-24-terraform-v5.19.0-provider/">Terraform v5.19.0 now available</a></h2>
<div class="changelog-badges"><span>terraform</span></div><div class="changelog-body"><p>Terraform Provider v5.19.0 introduces 14 new resources spanning AI Gateway, Pipelines, R2 Data Catalog, User Groups, Vulnerability Scanner, Workers Observability, and Zero Trust capabilities. This release significantly improves the v4 to v5 migration experience with automatic state upgraders for 26 resources, working seamlessly with the new <a href="https://github.com/cloudflare/tf-migrate">tf-migrate CLI tool</a> to automate resource renames, attribute updates, and <code>moved</code> block generation. Together, these enhancements reduce manual migration effort and minimize risk when upgrading from v4 to v5.</p>
<p><strong>Note:</strong> <code>cmd/migrate</code> is deprecated in favor of <code>tf-migrate</code> and will be removed in a future release (<a href="https://github.com/cloudflare/terraform-provider-cloudflare/pull/7062">#7062</a>)</p>
<h4 id="2026-04-24-terraform-v5.19.0-provider-new-resources">New Resources</h4>
<ul>
<li><strong>cloudflare_ai_gateway</strong>: Manage AI Gateway instances</li>
<li><strong>cloudflare_certificate_authorities_hostname_associations</strong>: Manage mTLS certificate hostname associations</li>
<li><strong>cloudflare_custom_page_asset</strong>: Manage custom page assets</li>
<li><strong>cloudflare_pipeline</strong>: Manage Cloudflare Pipelines</li>
<li><strong>cloudflare_r2_data_catalog</strong>: Manage R2 Data Catalog</li>
<li><strong>cloudflare_user_group</strong>: Manage user groups</li>
<li><strong>cloudflare_user_group_members</strong>: Manage user group memberships</li>
<li><strong>cloudflare_vulnerability_scanner_credential</strong>: Manage vulnerability scanner credentials</li>
<li><strong>cloudflare_vulnerability_scanner_credential_set</strong>: Manage vulnerability scanner credential sets</li>
<li><strong>cloudflare_vulnerability_scanner_target_environment</strong>: Manage vulnerability scanner target environments</li>
<li><strong>cloudflare_workers_observability_destination</strong>: Manage Workers Observability destinations</li>
<li><strong>cloudflare_zero_trust_device_ip_profile</strong>: Manage Zero Trust device IP profiles</li>
<li><strong>cloudflare_zero_trust_device_subnet</strong>: Manage Zero Trust device subnets</li>
<li><strong>cloudflare_zero_trust_dlp_settings</strong>: Manage Zero Trust DLP settings</li>
</ul>
<h4 id="2026-04-24-terraform-v5.19.0-provider-features">Features</h4>
<h4 id="2026-04-24-terraform-v5.19.0-provider-v4-to-v5-migration-state-upgraders">V4 to V5 Migration State Upgraders</h4>
<p>State upgraders added for seamless migration from v4 to v5 for the following resources:</p>
<ul>
<li>account</li>
<li>account_member</li>
<li>account_token</li>
<li>authenticated_origin_pulls</li>
<li>authenticated_origin_pulls_hostname_certificate</li>
<li>byo_ip_prefix</li>
<li>custom_hostname</li>
<li>custom_ssl</li>
<li>leaked_credential_check</li>
<li>leaked_credential_check_rule</li>
<li>logpush_ownership_challenge</li>
<li>mtls_certificate</li>
<li>observatory_scheduled_test</li>
<li>pages_domain</li>
<li>regional_tiered_cache</li>
<li>turnstile_widget</li>
<li>workers_custom_domain</li>
<li>zero_trust_device_custom_profile</li>
<li>zero_trust_device_default_profile</li>
<li>zero_trust_device_posture_integration</li>
<li>zero_trust_gateway_certificate</li>
<li>zero_trust_gateway_settings</li>
<li>zero_trust_organization</li>
<li>zero_trust_tunnel_cloudflared_virtual_network</li>
<li>zone_setting</li>
</ul>
<h4 id="2026-04-24-terraform-v5.19.0-provider-other-features">Other Features</h4>
<ul>
<li><strong>ruleset</strong>: Add <code>content_converter</code> and <code>redirects_for_ai_training</code> support to configuration rules</li>
<li><strong>zero_trust_gateway_logging</strong>: Make importable</li>
</ul>
<h4 id="2026-04-24-terraform-v5.19.0-provider-bug-fixes">Bug Fixes</h4>
<h4 id="2026-04-24-terraform-v5.19.0-provider-migration-state-management">Migration &amp; State Management</h4>
<ul>
<li><strong>account_member</strong>: Add UseStateForUnknown to status field to prevent drift</li>
<li><strong>authenticated_origin_pulls_settings</strong>: Fix no prior schema and no-op upgrade</li>
<li><strong>certificate_pack</strong>: Initialize empty lists instead of null in state upgrader to prevent drift</li>
<li><strong>migrations</strong>: Handle ambiguous schema_version state for v4/v5 coexistence</li>
<li><strong>zero_trust_access_policy</strong>: Fix nil pointer panic in state upgrader; set PriorSchema nil for v4 state upgrade</li>
</ul>
<h4 id="2026-04-24-terraform-v5.19.0-provider-resource-specific-fixes">Resource-Specific Fixes</h4>
<ul>
<li><strong>ai_search_instance</strong>: Restore original defaults for cache and cache_threshold; conflict resolution</li>
<li><strong>apijson</strong>: Return empty object from MarshalForPatch when no fields are serializable</li>
<li><strong>dlp_predefined_profile</strong>: Eliminate perpetual entries and enabled_entries drift</li>
<li><strong>dns_record</strong>: Avoid unnecessary drift for ipv4_only and ipv6_only attributes; remove private_routing default value</li>
<li><strong>drift</strong>: Preserve prior state values for optional fields not returned by API</li>
<li><strong>healthcheck</strong>: Use buildHealthcheckPlanChecks helper for correct plan checks per migration source; update assertions</li>
<li><strong>leaked_credential_check_rule</strong>: Handle empty ID from v4 provider state migration</li>
<li><strong>list_item</strong>: Remove context</li>
<li><strong>logpush_job</strong>: Update model for migration</li>
<li><strong>ruleset</strong>: Fix migration; add redirects_for_ai_training to SourceV4ActionParametersModel; fix duplicate model attribute</li>
<li><strong>worker</strong>: Add UseStateForUnknown() plan modifiers and update tests for observability.traces</li>
<li><strong>workers_custom_domain</strong>: Handle HTTP 200 no content header; update assertions</li>
<li><strong>workers_script</strong>: Fix model drift</li>
<li><strong>zero_trust_access_identity_provider</strong>: Fix boolean drifts</li>
<li><strong>zero_trust_device_managed_networks</strong>: Upgrade resource state</li>
<li><strong>zero_trust_gateway_policy</strong>: Make filters Computed+Optional to prevent drift</li>
<li><strong>zero_trust_gateway_settings</strong>: Fix breaking changes; implement sweeper to reset account to clean defaults</li>
<li><strong>zone_setting</strong>: Migration test improvements and fixes</li>
</ul>
<h4 id="2026-04-24-terraform-v5.19.0-provider-documentation">Documentation</h4>
<ul>
<li><strong>healthcheck</strong>: Update port description to clarify defaults</li>
<li>Add application-scoped access policy migration guidance</li>
<li>Update zone_settings_override migration guide for tf-migrate v2 workflow</li>
</ul>
<h4 id="2026-04-24-terraform-v5.19.0-provider-for-more-information">For more information</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform Provider</a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-migration">Version 5 Migration Guide</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-24">Apr 24, 2026</time><div>
<h2 id="post-2026-04-24-tf-migrate-tool-released"><a href="/changelog/post/2026-04-24-tf-migrate-tool-released/">Automate migration from Cloudflare's Terraform v4 to v5 provider</a></h2>
<div class="changelog-badges"><span>terraform</span></div><div class="changelog-body"><p>We're excited to announce <strong>tf-migrate</strong>, a purpose-built CLI tool that simplifies migrating from Cloudflare Terraform Provider v4 to v5.</p>
<h4 id="2026-04-24-tf-migrate-tool-released-v5-is-stable-and-ready-for-production">v5 is stable and ready for production</h4>
<p><strong>Terraform Provider v5 is stable and actively receiving updates.</strong>  We encourage all users to migrate to v5 to take advantage of ongoing enhancements and new capabilities.</p>
<p>Cloudflare uses tf-migrate to migrate our own infrastructure — the same tool we're providing to the community — ensuring the best possible migration experience.</p>
<h4 id="2026-04-24-tf-migrate-tool-released-what-tf-migrate-does">What tf-migrate does</h4>
<p><strong>tf-migrate</strong> automates the tedious and error-prone parts of the v4 to v5 migration process:</p>
<ul>
<li><strong>Resource type renames</strong> – Automatically updates <code>cloudflare_record</code> → <code>cloudflare_dns_record</code>, <code>cloudflare_access_application</code> → <code>cloudflare_zero_trust_access_application</code>, and 40+ other renamed resources</li>
<li><strong>Attribute transformations</strong> – Updates field names (e.g., <code>value</code> → <code>content</code> for DNS records) and restructures nested blocks</li>
<li><strong>Moved block generation</strong> – Creates Terraform 1.8+ <code>moved</code> blocks to prevent resource replacements and ensure zero-downtime migrations</li>
<li><strong>Cross-file reference updates</strong> – Automatically finds and updates all references to renamed resources across your entire configuration</li>
<li><strong>Dry-run mode</strong> – Preview all changes before applying them to ensure safety</li>
</ul>
<p>Combined with the automatic state upgraders introduced in v5.19+, tf-migrate eliminates the manual work and risk that previously made v5 migrations challenging. Tf-migrate operates directly on the config, and the built-in state upgraders handle the rest.</p>
<h4 id="2026-04-24-tf-migrate-tool-released-supported-resources">Supported resources</h4>
<p>Tf-migrate currently supports the most common Terraform resources our customers use. We are actively working to expand coverage, with the most commonly used resources prioritized first.</p>
<p>For the complete list of supported resources and their migration status, refer to the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">v5 Stabilization Tracker</a>. This list is updated regularly as additional resources are stabilized and migration support is added.</p>
<p>Resources not yet supported by tf-migrate will need to be migrated manually using the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">version 5 upgrade guide</a>. The upgrade guide provides step-by-step instructions for handling resource renames, attribute changes, and state migrations.</p>
<h4 id="2026-04-24-tf-migrate-tool-released-get-started">Get started</h4>
<ul>
<li><a href="https://github.com/cloudflare/tf-migrate/releases">Download tf-migrate</a></li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-migration">Version 5 Migration Guide</a></li>
<li><a href="https://developers.cloudflare.com/terraform/">Terraform Provider documentation</a></li>
<li><a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">v5 Stabilization Tracker</a></li>
</ul>
<p>We have been releasing Betas over the past month and a half while testing this tool. See the full changelog of those Betas here: <a href="https://github.com/cloudflare/tf-migrate/releases">tf-migrate releases</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-23">Apr 23, 2026</time><div>
<h2 id="post-2026-04-23-independent-mfa-aaguid-amr"><a href="/changelog/post/2026-04-23-independent-mfa-aaguid-amr/">AAGUID restrictions and AMR matching for Access independent MFA</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p><a href="/cloudflare-one/access-controls/access-settings/independent-mfa/">Independent MFA</a> in Cloudflare Access now supports two additional organization-level controls:</p>
<ul>
<li><strong><a href="/cloudflare-one/access-controls/access-settings/independent-mfa/#restrict-authenticators-by-aaguid">Restrict authenticators by AAGUID</a></strong> — Limit enrollment to a specific set of WebAuthn authenticators using their <a href="https://fidoalliance.org/specs/fido-v2.0-id-20180227/fido-registry-v2.0-id-20180227.html#authenticator-attestation-guid">AAGUID</a>. This is useful for organizations that require FIPS-validated security keys or company-issued hardware. AAGUIDs are managed through a new <a href="/cloudflare-one/reusable-components/lists/">List</a> type.</li>
<li><strong><a href="/cloudflare-one/access-controls/access-settings/independent-mfa/#use-identity-provider-mfa">AMR matching</a></strong> — Skip the independent MFA prompt when the identity provider has already performed an equivalent MFA. Access reads the <code>amr</code> claim defined in <a href="https://datatracker.ietf.org/doc/html/rfc8176">RFC 8176</a> and matches supported values such as <code>hwk</code>, <code>otp</code>, and <code>fpt</code> to the authenticator types allowed on the application or policy. This prevents users from having to complete MFA twice when their identity provider already enforces it.</li>
</ul>
<p>To get started, refer to <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/">Independent MFA</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-23">Apr 23, 2026</time><div>
<h2 id="post-2026-04-23-audit-logs-v2-organization-level"><a href="/changelog/post/2026-04-23-audit-logs-v2-organization-level/">Audit Logs v2 — Organization-level support</a></h2>
<div class="changelog-badges"><span>audit-logs</span></div><div class="changelog-body"><p>Audit Logs v2 now supports organization-level audit logs. Org Admins can retrieve audit events for actions performed at the organization level via the Audit Logs v2 API.</p>
<p>To retrieve organization-level audit logs, use the following endpoint:</p>
<pre tabindex="0"><code class="language-bash">GET https://api.cloudflare.com/client/v4/organizations/{organization_id}/logs/audit&#10;</code></pre>
<p>This release covers user-initiated actions performed through organization-level APIs. Audit logs for system-initiated actions, a dashboard UI, and Logpush support for organizations will be added in future releases.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17692.md")</aside>
<p>For more information, refer to the <a href="/fundamentals/account/account-security/audit-logs/">Audit Logs documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-23">Apr 23, 2026</time><div>
<h2 id="post-2026-04-23-go-sdk-v6.10.0"><a href="/changelog/post/2026-04-23-go-sdk-v6.10.0/">Go SDK v6.10.0 Released</a></h2>
<div class="changelog-badges"><span>sdk</span><span>go-sdk</span></div><div class="changelog-body"><h4 id="2026-04-23-go-sdk-v6.10.0-v6-10-0">v6.10.0</h4>
<p>In this release, you'll see a number of breaking changes. This is primarily due to changes in OpenAPI definitions, which our libraries are based off of, and codegen updates that we rely on to read those OpenAPI definitions and produce our SDK libraries.</p>
<p><strong>Please ensure you read through the list of changes below before moving to this version</strong> - this will help you understand any down or upstream issues it may cause to your environments.</p>
<h4 id="2026-04-23-go-sdk-v6.10.0-breaking-changes">Breaking Changes</h4>
<p>See the <a href="https://github.com/cloudflare/cloudflare-go/blob/main/MIGRATION_GUIDE.md">v6.10.0 Migration Guide</a> for before/after code examples and actions needed for each change.</p>
<h4 id="2026-04-23-go-sdk-v6.10.0-abuse-reports-registrar-whois-report-field-removals">Abuse Reports - Registrar WHOIS Report Field Removals</h4>
<p>Several fields have been removed from <code>AbuseReportNewParamsBodyAbuseReportsRegistrarWhoisReportRegWhoRequest</code>:</p>
<ul>
<li><code>RegWhoGoodFaithAffirmation</code></li>
<li><code>RegWhoLawfulProcessingAgreement</code></li>
<li><code>RegWhoLegalBasis</code></li>
<li><code>RegWhoRequestType</code></li>
<li><code>RegWhoRequestedDataElements</code></li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-ai-search-instance-params-restructured">AI Search - Instance Params Restructured</h4>
<p>The <code>InstanceNewParams</code> and <code>InstanceUpdateParams</code> types have been significantly restructured. Many fields have been moved or removed:</p>
<ul>
<li><code>InstanceNewParams.TokenID</code>, <code>Type</code>, <code>CreatedFromAISearchWizard</code>, <code>WorkerDomain</code> removed</li>
<li><code>InstanceUpdateParams</code> — most configuration fields removed (including <code>IndexMethod</code>, <code>IndexingOptions</code>, <code>MaxNumResults</code>, <code>Metadata</code>, <code>Paused</code>, <code>PublicEndpointParams</code>, <code>Reranking</code>, <code>RerankingModel</code>, <code>RetrievalOptions</code>, <code>RewriteModel</code>, <code>RewriteQuery</code>, <code>ScoreThreshold</code>, <code>SourceParams</code>, <code>Summarization</code>, <code>SummarizationModel</code>, <code>SystemPromptAISearch</code>, <code>SystemPromptIndexSummarization</code>, <code>SystemPromptRewriteQuery</code>, <code>TokenID</code>, <code>CreatedFromAISearchWizard</code>, <code>WorkerDomain</code>)</li>
<li><code>InstanceSearchParams.Messages</code> field removed along with <code>InstanceSearchParamsMessage</code> and <code>InstanceSearchParamsMessagesRole</code> types</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-ai-search-instanceitem-service-removed">AI Search - InstanceItem Service Removed</h4>
<p>The <code>InstanceItemService</code> type has been removed. The items sub-resource at <code>client.AISearch.Instances.Items</code> no longer exists in the non-namespace path. Use <code>client.AISearch.Namespaces.Instances.Items</code> instead.</p>
<h4 id="2026-04-23-go-sdk-v6.10.0-ai-search-token-types-removed">AI Search - Token Types Removed</h4>
<p>The following types have been removed from the <code>ai_search</code> package:</p>
<ul>
<li><code>TokenDeleteResponse</code></li>
<li><code>TokenListParams</code> (and associated <code>TokenListParamsOrderBy</code>, <code>TokenListParamsOrderByDirection</code>)</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-email-security-investigate-move-return-type-change">Email Security - Investigate Move Return Type Change</h4>
<p>The <code>Investigate.Move.New()</code> method now returns a raw slice instead of a paginated wrapper:</p>
<ul>
<li><code>New()</code> returns <code>*[]InvestigateMoveNewResponse</code> instead of <code>*pagination.SinglePage[InvestigateMoveNewResponse]</code></li>
<li><code>NewAutoPaging()</code> method removed</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-hyperdrive-config-params-restructured">Hyperdrive - Config Params Restructured</h4>
<p>The <code>ConfigEditParams</code> type lost its <code>MTLS</code> and <code>Name</code> fields. The <code>HyperdriveMTLSParam</code> type lost <code>MTLS</code> and <code>Host</code> fields. The <code>Host</code> field on origin config changed from <code>param.Field[string]</code> to a plain <code>string</code>.</p>
<h4 id="2026-04-23-go-sdk-v6.10.0-iam-usergroupmember-params-and-return-types-changed">IAM - UserGroupMember Params and Return Types Changed</h4>
<p>The <code>UserGroupMemberNewParams</code> struct has been restructured and the <code>New()</code> method now returns a paginated response:</p>
<ul>
<li><code>UserGroupMemberNewParams.Body</code> renamed to <code>UserGroupMemberNewParams.Members</code></li>
<li><code>UserGroupMemberNewParamsBody</code> renamed to <code>UserGroupMemberNewParamsMember</code></li>
<li><code>UserGroupMemberUpdateParams.Body</code> renamed to <code>UserGroupMemberUpdateParams.Members</code></li>
<li><code>UserGroupMemberUpdateParamsBody</code> renamed to <code>UserGroupMemberUpdateParamsMember</code></li>
<li><code>UserGroups.Members.New()</code> returns <code>*pagination.SinglePage[UserGroupMemberNewResponse]</code> instead of <code>*UserGroupMemberNewResponse</code></li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-iam-usergroup-list-direction-type-changed">IAM - UserGroup List Direction Type Changed</h4>
<p>The <code>UserGroupListParams.Direction</code> field changed from <code>param.Field[string]</code> to <code>param.Field[UserGroupListParamsDirection]</code> (typed enum with <code>asc</code>/<code>desc</code> values).</p>
<h4 id="2026-04-23-go-sdk-v6.10.0-pipelines-delete-methods-now-return-typed-responses">Pipelines - Delete Methods Now Return Typed Responses</h4>
<p>Several delete methods across Pipelines now return typed responses instead of bare error:</p>
<ul>
<li><code>Pipelines.DeleteV1()</code> returns <code>(*PipelineDeleteV1Response, error)</code> instead of <code>error</code></li>
<li><code>Pipelines.Sinks.Delete()</code> returns <code>(*SinkDeleteResponse, error)</code> instead of <code>error</code></li>
<li><code>Pipelines.Streams.Delete()</code> returns <code>(*StreamDeleteResponse, error)</code> instead of <code>error</code></li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-queues-message-response-types-removed">Queues - Message Response Types Removed</h4>
<p>The following response envelope types have been removed:</p>
<ul>
<li><code>MessageBulkPushResponseSuccess</code></li>
<li><code>MessagePushResponseSuccess</code></li>
<li><code>MessageAckResponse</code> fields <code>RetryCount</code> and <code>Warnings</code> removed</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-secrets-store-pagination-wrapper-removal-and-type-changes">Secrets Store - Pagination Wrapper Removal and Type Changes</h4>
<p>Methods now return direct types instead of <code>SinglePage</code> wrappers, and several internal types have been removed. Associated <code>AutoPaging</code> methods have also been removed:</p>
<ul>
<li><code>Stores.New()</code> returns <code>*StoreNewResponse</code> instead of <code>*pagination.SinglePage[StoreNewResponse]</code></li>
<li><code>Stores.NewAutoPaging()</code> method removed</li>
<li><code>Stores.Secrets.BulkDelete()</code> returns <code>*StoreSecretBulkDeleteResponse</code> instead of <code>*pagination.SinglePage[StoreSecretBulkDeleteResponse]</code></li>
<li><code>Stores.Secrets.BulkDeleteAutoPaging()</code> method removed</li>
<li>Removed types: <code>StoreDeleteResponse</code>, <code>StoreDeleteResponseEnvelopeResultInfo</code>, <code>StoreSecretDeleteResponse</code>, <code>StoreSecretDeleteResponseStatus</code>, <code>StoreSecretBulkDeleteResponse</code> (old shape), <code>StoreSecretBulkDeleteResponseStatus</code>, <code>StoreSecretDeleteResponseEnvelopeResultInfo</code></li>
<li><code>StoreNewParams</code> restructured (old <code>StoreNewParamsBody</code> removed)</li>
<li><code>StoreSecretBulkDeleteParams</code> restructured</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-stream-audiotracks-return-type-change">Stream - AudioTracks Return Type Change</h4>
<p>The <code>AudioTracks.Get()</code> method now returns a dedicated response type instead of a paginated list. The <code>GetAutoPaging()</code> method has been removed:</p>
<ul>
<li><code>Get()</code> returns <code>*AudioTrackGetResponse</code> instead of <code>*pagination.SinglePage[Audio]</code></li>
<li><code>GetAutoPaging()</code> method removed</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-stream-clip-type-removal-and-return-type-change">Stream - Clip Type Removal and Return Type Change</h4>
<p>The <code>Clip.New()</code> method now returns the shared <code>Video</code> type. The following types have been entirely removed:</p>
<ul>
<li><code>Clip</code>, <code>ClipPlayback</code>, <code>ClipStatus</code>, <code>ClipWatermark</code></li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-stream-copy-and-clip-params-field-removals">Stream - Copy and Clip Params Field Removals</h4>
<ul>
<li><code>ClipNewParams.MaxDurationSeconds</code>, <code>ThumbnailTimestampPct</code>, <code>Watermark</code> removed</li>
<li><code>CopyNewParams.ThumbnailTimestampPct</code>, <code>Watermark</code> removed</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-stream-download-and-webhook-changes">Stream - Download and Webhook Changes</h4>
<ul>
<li><code>DownloadNewResponseStatus</code> type removed</li>
<li><code>WebhookUpdateResponse</code> and <code>WebhookGetResponse</code> changed from <code>interface{}</code> type aliases to full struct types</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-zero-trust-access-ai-control-mcp-portal-union-types-removed">Zero Trust - Access AI Control MCP Portal Union Types Removed</h4>
<p>The following union interface types have been removed:</p>
<ul>
<li><code>AccessAIControlMcpPortalListResponseServersUpdatedPromptsUnion</code></li>
<li><code>AccessAIControlMcpPortalListResponseServersUpdatedToolsUnion</code></li>
<li><code>AccessAIControlMcpPortalReadResponseServersUpdatedPromptsUnion</code></li>
<li><code>AccessAIControlMcpPortalReadResponseServersUpdatedToolsUnion</code></li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-features">Features</h4>
<h4 id="2026-04-23-go-sdk-v6.10.0-vulnerability-scanner-client-vulnerabilityscanner">Vulnerability Scanner (<code>client.VulnerabilityScanner</code>)</h4>
<p><strong>NEW SERVICE:</strong> Full vulnerability scanning management</p>
<ul>
<li><strong>CredentialSets</strong> - CRUD for credential sets (<code>New</code>, <code>Update</code>, <code>List</code>, <code>Delete</code>, <code>Edit</code>, <code>Get</code>)</li>
<li><strong>Credentials</strong> - Manage credentials within sets (<code>New</code>, <code>Update</code>, <code>List</code>, <code>Delete</code>, <code>Edit</code>, <code>Get</code>)</li>
<li><strong>Scans</strong> - Create and manage vulnerability scans (<code>New</code>, <code>List</code>, <code>Get</code>)</li>
<li><strong>TargetEnvironments</strong> - Manage scan target environments (<code>New</code>, <code>Update</code>, <code>List</code>, <code>Delete</code>, <code>Edit</code>, <code>Get</code>)</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-ai-search-namespaces-client-aisearch-namespaces">AI Search - Namespaces (<code>client.AISearch.Namespaces</code>)</h4>
<p><strong>NEW SERVICE:</strong> Namespace-scoped AI Search management</p>
<ul>
<li><code>New()</code>, <code>Update()</code>, <code>List()</code>, <code>Delete()</code>, <code>ChatCompletions()</code>, <code>Read()</code>, <code>Search()</code></li>
<li><strong>Instances</strong> - Namespace-scoped instances (<code>New</code>, <code>Update</code>, <code>List</code>, <code>Delete</code>, <code>ChatCompletions</code>, <code>Read</code>, <code>Search</code>, <code>Stats</code>)</li>
<li><strong>Jobs</strong> - Instance job management (<code>New</code>, <code>Update</code>, <code>List</code>, <code>Get</code>, <code>Logs</code>)</li>
<li><strong>Items</strong> - Instance item management (<code>List</code>, <code>Delete</code>, <code>Chunks</code>, <code>NewOrUpdate</code>, <code>Download</code>, <code>Get</code>, <code>Logs</code>, <code>Sync</code>, <code>Upload</code>)</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-browser-rendering-devtools-client-browserrendering-devtools">Browser Rendering - Devtools (<code>client.BrowserRendering.Devtools</code>)</h4>
<p><strong>NEW SERVICE:</strong> DevTools protocol browser control</p>
<ul>
<li><strong>Session</strong> - List and get devtools sessions</li>
<li><strong>Browser</strong> - Browser lifecycle management (<code>New</code>, <code>Delete</code>, <code>Connect</code>, <code>Launch</code>, <code>Protocol</code>, <code>Version</code>)</li>
<li><strong>Page</strong> - Get page by target ID</li>
<li><strong>Targets</strong> - Manage browser targets (<code>New</code>, <code>List</code>, <code>Activate</code>, <code>Get</code>)</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-registrar-client-registrar">Registrar (<code>client.Registrar</code>)</h4>
<p><strong>NEW:</strong> Domain check and search endpoints</p>
<ul>
<li><code>Check()</code> - <code>POST /accounts/{account_id}/registrar/domain-check</code></li>
<li><code>Search()</code> - <code>GET /accounts/{account_id}/registrar/domain-search</code></li>
</ul>
<p><strong>NEW:</strong> Registration management (<code>client.Registrar.Registrations</code>)</p>
<ul>
<li><code>New()</code>, <code>List()</code>, <code>Edit()</code>, <code>Get()</code></li>
<li><code>RegistrationStatus.Get()</code> - Get registration workflow status</li>
<li><code>UpdateStatus.Get()</code> - Get update workflow status</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-cache-origin-cloud-regions-client-cache-origincloudregions">Cache - Origin Cloud Regions (<code>client.Cache.OriginCloudRegions</code>)</h4>
<p><strong>NEW SERVICE:</strong> Manage origin cloud region configurations</p>
<ul>
<li><code>New()</code>, <code>List()</code>, <code>Delete()</code>, <code>BulkDelete()</code>, <code>BulkEdit()</code>, <code>Edit()</code>, <code>Get()</code>, <code>SupportedRegions()</code></li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-zero-trust-dlp-settings-client-zerotrust-dlp-settings">Zero Trust - DLP Settings (<code>client.ZeroTrust.DLP.Settings</code>)</h4>
<p><strong>NEW SERVICE:</strong> DLP settings management</p>
<ul>
<li><code>Update()</code>, <code>Delete()</code>, <code>Edit()</code>, <code>Get()</code></li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-radar">Radar</h4>
<ul>
<li><code>AgentReadiness.Summary()</code> - Agent readiness summary by dimension</li>
<li><code>AI.MarkdownForAgents.Summary()</code> - Markdown-for-agents summary</li>
<li><code>AI.MarkdownForAgents.Timeseries()</code> - Markdown-for-agents timeseries</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-iam-client-iam">IAM (<code>client.IAM</code>)</h4>
<ul>
<li><code>UserGroups.Members.Get()</code> - Get details of a specific member in a user group</li>
<li><code>UserGroups.Members.NewAutoPaging()</code> - Auto-paging variant for adding members</li>
<li><code>UserGroups.NewParams.Policies</code> changed from required to optional</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-bot-management">Bot Management</h4>
<ul>
<li><code>ContentBotsProtection</code> field added to <code>BotFightModeConfiguration</code> and <code>SubscriptionConfiguration</code> (<code>block</code>/<code>disabled</code>)</li>
</ul>
<h4 id="2026-04-23-go-sdk-v6.10.0-deprecations">Deprecations</h4>
<p>None in this release.</p>
<h4 id="2026-04-23-go-sdk-v6.10.0-get-started">Get started</h4>
<ul>
<li><a href="https://github.com/cloudflare/cloudflare-go/releases/tag/v6.10.0">Download Go SDK v6.10.0</a></li>
<li><a href="https://developers.cloudflare.com/api/sdks/go/">Go SDK documentation</a></li>
<li><a href="https://github.com/cloudflare/cloudflare-go/blob/main/MIGRATION_GUIDE.md">Migration Guide</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-22">Apr 22, 2026</time><div>
<h2 id="post-2026-04-22-custom-dashboards-ga"><a href="/changelog/post/2026-04-22-custom-dashboards-ga/">Custom dashboards available to all customers</a></h2>
<div class="changelog-badges"><span>analytics</span><span>log-explorer</span></div><div class="changelog-body"><p>Custom Dashboards are now available to all Cloudflare customers. Build personalized views that highlight the metrics most critical to your infrastructure and security posture, moving beyond standard product dashboards.</p>
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
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/16/">Previous</a><span>Page 17 of 50</span><a class="pagination-next" rel="next" href="/changelog/18/">Next</a></nav>
</div>
