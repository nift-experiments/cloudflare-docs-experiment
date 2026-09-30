---
cp9:
  canonical: https://developers.cloudflare.com/changelog/20/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 20 | Cloudflare Docs
  head_html: <title>Changelog - page 20 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/20/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 20"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/20/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/20/#page","headline":"Changelog - page 20 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/20/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/20/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-04-09">Apr 9, 2026</time><div>
<h2 id="post-2026-04-09-casb-webhooks"><a href="/changelog/post/2026-04-09-casb-webhooks/">Send CASB posture finding instances with webhooks</a></h2>
<div class="changelog-badges"><span>casb</span></div><div class="changelog-body"><p>You can now use <strong>CASB webhooks</strong> in Cloudflare One to send posture finding instances to external systems such as chat platforms, ticketing systems, SIEMs, SOAR tools, and custom automation services.</p>
<p>This gives security teams a simple way to route CASB posture findings into the tools and workflows they already use for triage and response.</p>
<p>To get started, go to <strong>Integrations</strong> &gt; <strong>Webhooks</strong> in the Cloudflare One dashboard to create a webhook destination. After you configure a webhook, open a posture finding instance and select <strong>Send webhook</strong> to send it.</p>
<h4 id="2026-04-09-casb-webhooks-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Flexible authentication</strong> — Configure destinations using <strong>None</strong>, <strong>Basic Auth</strong>, <strong>Bearer Auth</strong>, <strong>Static Headers</strong>, or <strong>HMAC-Signing</strong>.</li>
<li><strong>Built-in testing</strong> — Use <strong>Test delivery</strong> to send a test request before sending a live finding instance.</li>
<li><strong>Posture finding workflows</strong> — Send posture finding instances directly from the finding details workflow in <strong>Cloud &amp; SaaS findings</strong>.</li>
<li><strong>HTTPS destinations</strong> — Configure webhook destinations with public <code>https://</code> URLs.</li>
</ul>
<h4 id="2026-04-09-casb-webhooks-learn-more">Learn more</h4>
<ul>
<li>Configure <a href="/cloudflare-one/integrations/cloud-and-saas/webhooks/">CASB webhooks</a> in Cloudflare.</li>
<li>Learn how to <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/">manage findings</a> in Cloudflare.</li>
</ul>
<p>CASB webhooks are now available in Cloudflare One.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-09">Apr 9, 2026</time><div>
<h2 id="post-2026-04-09-relaxed-connection-limiting"><a href="/changelog/post/2026-04-09-relaxed-connection-limiting/">Relaxed simultaneous connection limiting for Workers</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The <a href="/workers/platform/limits/#simultaneous-open-connections">simultaneous open connections limit</a> has been relaxed. Previously, each Worker invocation was limited to six open connections at a time for the entire lifetime of each connection, including while reading the response body. Now, a connection is freed as soon as response headers arrive, so the six-connection limit only constrains how many connections can be in the initial &quot;waiting for headers&quot; phase simultaneously.</p>
<h4 id="2026-04-09-relaxed-connection-limiting-before-new-connections-are-blocked-until-an-earlier-connection-fully-completes">Before: New connections are blocked until an earlier connection fully completes</h4>
<p><img src="/assets/upstream/images/workers/platform/limits/connection-limit-before.svg" alt="A 7th fetch is queued until an earlier connection fully completes, including reading its entire response body" /></p>
<h4 id="2026-04-09-relaxed-connection-limiting-after-new-connections-can-start-as-soon-as-response-headers-arrive">After: New connections can start as soon as response headers arrive</h4>
<p><img src="/assets/upstream/images/workers/platform/limits/connection-limit-after.svg" alt="A 7th fetch starts as soon as any earlier connection receives its response headers" /></p>
<p>This means Workers can now have many more connections open at the same time without queueing, as long as no more than six are waiting for their initial response. This eliminates the <code>Response closed due to connection limit</code> exception that could previously occur when the runtime canceled stalled connections to prevent deadlocks.</p>
<p>Previously, the runtime used a deadlock avoidance algorithm that watched each open connection for I/O activity. If all six connections appeared idle — even momentarily — the runtime would cancel the least-recently-used connection to make room for new requests. In practice, this heuristic was fragile. For example, when a response used <code>Content-Encoding: gzip</code>, the runtime's internal decompression created brief gaps between read and write operations. During these gaps, the connection appeared stalled despite being actively read by the Worker. If multiple connections hit these gaps at the same time, the runtime could spuriously cancel a connection that was working correctly. By only counting connections during the waiting-for-headers phase — where the runtime is fully in control and there is no ambiguity about whether the connection is active — this class of bug is eliminated entirely.</p>
<h4 id="2026-04-09-relaxed-connection-limiting-before-connections-could-be-canceled-during-brief-internal-pauses">Before: Connections could be canceled during brief internal pauses</h4>
<p><img src="/assets/upstream/images/workers/platform/limits/connection-cancel-before.svg" alt="A connection with gaps from gzip decompression appears idle and is canceled by the runtime" /></p>
<h4 id="2026-04-09-relaxed-connection-limiting-after-connections-complete-normally-regardless-of-internal-pauses">After: Connections complete normally regardless of internal pauses</h4>
<p><img src="/assets/upstream/images/workers/platform/limits/connection-cancel-after.svg" alt="The same connection completes normally because the body phase is no longer counted against the limit" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-08">Apr 8, 2026</time><div>
<h2 id="post-2026-04-09-ai-search-content-selectors"><a href="/changelog/post/2026-04-09-ai-search-content-selectors/">Website Source CSS content selectors for precise content extraction in AI Search</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now supports <a href="/ai-search/configuration/data-source/website/content-selectors/">CSS content selectors</a> for website data sources. You can now define which parts of a crawled page are extracted and indexed by specifying CSS selectors paired with URL glob patterns.</p>
<p>Content selectors solve the problem of indexing only relevant content while ignoring navigation, sidebars, footers, and other boilerplate. When a page URL matches a glob pattern, only elements matching the corresponding CSS selector are extracted and converted to Markdown for indexing.</p>
<p>Configure content selectors via the dashboard or API:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/ai-search/instances&quot; \&#10;  &#45;H &quot;Authorization: Bearer {api_token}&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;id&quot;: &quot;my-ai-search&quot;,&#10;    &quot;source&quot;: &quot;https://example.com&quot;,&#10;    &quot;type&quot;: &quot;web-crawler&quot;,&#10;    &quot;source_params&quot;: {&#10;      &quot;web_crawler&quot;: {&#10;        &quot;parse_options&quot;: {&#10;          &quot;content_selector&quot;: [&#10;            {&#10;              &quot;path&quot;: &quot;**/blog/**&quot;,&#10;              &quot;selector&quot;: &quot;article .post-body&quot;&#10;            }&#10;          ]&#10;        }&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>Selectors are evaluated in order, and the first matching pattern wins. You can define up to 10 content selector entries per instance.</p>
<p>For configuration details and examples, refer to the <a href="/ai-search/configuration/data-source/website/content-selectors/">content selectors documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-08">Apr 8, 2026</time><div>
<h2 id="post-2026-04-09-new-workers-ai-models"><a href="/changelog/post/2026-04-09-new-workers-ai-models/">New Workers AI models for text generation and embedding in AI Search</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now supports four additional <a href="/workers-ai/">Workers AI</a> models across text generation and embedding.</p>
<h4 id="2026-04-09-new-workers-ai-models-text-generation">Text generation</h4>
<table>
<thead>
<tr>
<th>Model</th>
<th>Context window (tokens)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@cf/zai-org/glm-4.7-flash</code></td>
<td>131,072</td>
</tr>
<tr>
<td><code>@cf/qwen/qwen3-30b-a3b-fp8</code></td>
<td>32,000</td>
</tr>
</tbody>
</table>
<p>GLM-4.7-Flash is a lightweight model from Zhipu AI with a 131,072 token context window, suitable for long-document summarization and retrieval tasks. Qwen3-30B-A3B is a mixture-of-experts model from Alibaba that activates only 3 billion parameters per forward pass, keeping inference fast while maintaining strong response quality.</p>
<h4 id="2026-04-09-new-workers-ai-models-embedding">Embedding</h4>
<table>
<thead>
<tr>
<th>Model</th>
<th>Vector dims</th>
<th>Input tokens</th>
<th>Metric</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@cf/qwen/qwen3-embedding-0.6b</code></td>
<td>1,024</td>
<td>4,096</td>
<td>cosine</td>
</tr>
<tr>
<td><code>@cf/google/embeddinggemma-300m</code></td>
<td>768</td>
<td>512</td>
<td>cosine</td>
</tr>
</tbody>
</table>
<p>Qwen3-Embedding-0.6B supports up to 4,096 input tokens, making it a good fit for indexing longer text chunks. EmbeddingGemma-300M from Google produces 768-dimension vectors and is optimized for low-latency embedding workloads.</p>
<p>All four models are available without additional provider keys since they run on Workers AI. Select them when creating or updating an AI Search instance in the dashboard or through the API.</p>
<p>For the full list of supported models, refer to <a href="/ai-search/configuration/models/supported-models/">Supported models</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-08">Apr 8, 2026</time><div>
<h2 id="post-2026-04-08-high-risk-browsing"><a href="/changelog/post/2026-04-08-high-risk-browsing/">User risk scoring for high risk browsing activity</a></h2>
<div class="changelog-badges"><span>risk-score</span></div><div class="changelog-body"><p>Cloudflare One's <strong>User Risk Scoring</strong> now incorporates direct signals from <strong>Gateway DNS traffic patterns</strong>. This update allows security teams to automatically elevate a user's risk score when they visit high-risk or malicious domains, providing a more holistic view of internal threats.</p>
<h4 id="2026-04-08-high-risk-browsing-why-this-matters">Why this matters</h4>
<p>Browsing activity is a primary indicator of potential compromise. By tying Gateway DNS logs to specific users, administrators can now flag individuals interacting with:</p>
<ul>
<li><strong>Security threats</strong>: Domains associated with malware, phishing, or command-and-control (C2) centers.</li>
<li><strong>High-risk content</strong>: Categories such as questionable content or violence that may violate corporate compliance.</li>
</ul>
<p>Even if a Gateway policy is set to <strong>Block</strong> the traffic, the interaction is still captured as a &quot;hit&quot; to ensure the user's risk profile reflects the attempted activity.</p>
<h4 id="2026-04-08-high-risk-browsing-new-risk-behaviors">New risk behaviors</h4>
<p>Two new behaviors are now available in the dashboard:</p>
<ul>
<li><strong>Suspicious Security Domain Visited</strong>: Triggers when a user visits a domain in the security threats or security risk categories.</li>
<li><strong>High risk domain visited</strong>: Triggers when a user visits domains categorized as questionable content, violence, or CIPA.</li>
</ul>
<p>To learn more and get started, refer to the <a href="/cloudflare-one/team-and-resources/users/risk-score/">User Risk Scoring documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-08">Apr 8, 2026</time><div>
<h2 id="post-2026-04-08-threat-events-notification"><a href="/changelog/post/2026-04-08-threat-events-notification/">Real-time alerts and daily digests for Threat Events</a></h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p>You can now automate your threat monitoring by setting up custom alerts in your saved views. Instead of manually checking the dashboard for updates, you can subscribe to notifications that trigger whenever new data matches your specific filter sets, like new activity associated to a particular threat actor or spikes in activity within your industry.</p>
<h4 id="2026-04-08-threat-events-notification-stay-ahead-of-emerging-threats">Stay ahead of emerging threats</h4>
<p>By linking your saved views to the Cloudflare Notifications Center, you can ensure the right information reaches your team at the right time.</p>
<ul>
<li>
<p><strong>Immediate Alerts</strong>: receive real-time notifications the moment a critical event is detected that matches your saved criteria. This is essential for high-priority monitoring, such as tracking active campaigns from specific APT groups.</p>
</li>
<li>
<p><strong>Daily Digests</strong>: opt for a summarized report delivered once a day. This is ideal for maintaining situational awareness of broader trends, like regional activity shifts or industry-wide threat landscapes, without cluttering your inbox.</p>
</li>
</ul>
<p><img src="/assets/upstream/images/changelog/security-center/threat-events-notifications.png" alt="Threat Events notifications" /></p>
<h4 id="2026-04-08-threat-events-notification-how-to-get-started">How to get started</h4>
<p>To set up an alert, go to <strong>Application Security</strong> &gt; <strong>Threat Intelligence</strong> &gt; <strong>Threat Events</strong>. From there:</p>
<ol>
<li>Choose your datasets and apply your desired filters and select <strong>Save View</strong> (or select an existing one).</li>
<li>Open the <strong>Manage Saved Views</strong> menu.</li>
<li>Select <strong>Add Alert</strong> next to your chosen view to configure your notification preferences in the Cloudflare dashboard.</li>
</ol>
<p>For more technical details on configuring notifications, refer to the <a href="/security-center/cloudforce-one/">Threat Events documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-08">Apr 8, 2026</time><div>
<h2 id="post-2026-04-07-warp-windows-ga"><a href="/changelog/post/2026-04-07-warp-windows-ga/">Cloudflare One Client for Windows (version 2026.3.851.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes and improvements.</p>
<p>The next stable release for Windows will introduce the new Cloudflare One Client UI, providing a cleaner and more intuitive design as well as easier access to common actions and information.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Fixed an issue causing Windows client tunnel interface initialization failure which prevented clients from establishing a tunnel for connection.</li>
<li>Consumer-only CLI commands are now clearly distinguished from Zero Trust commands.</li>
<li>Added detailed QUIC connection metrics to diagnostic logs for better troubleshooting.</li>
<li>Added monitoring for tunnel statistics collection timeouts.</li>
<li>Switched tunnel congestion control algorithm for local proxy mode to Cubic for improved reliability across platforms.</li>
<li>Fixed packet capture failing on tunnel interface when the tunnel interface is renamed by SCCM VPN boundary support.</li>
<li>Fixed unnecessary registration deletion caused by RDP connections in multi-user mode.</li>
<li>Fixed increased tunnel interface start-up time due to a race between duplicate address detection (DAD) and disabling NetBT.</li>
<li>Fixed tunnel failing to connect when the system DNS search list contains unexpected characters.</li>
<li>Empty MDM files are now rejected instead of being incorrectly accepted as a single MDM config.</li>
<li>Fixed an issue in local proxy mode where the client could become unresponsive due to upstream connection timeouts.</li>
<li>Fixed an issue where the emergency disconnect status of a prior organization persisted after a switch to a different organization.</li>
<li>Fixed initiating managed network detections checks when no network is available, which caused device profile flapping.</li>
<li>Fixed an issue where degraded Windows Management Instrumentation (WMI) state could put the client in a failed connection state loop during initialization.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>
<p>For Windows 11 24H2 users, Microsoft has confirmed a regression that may lead to performance issues like mouse lag, audio cracking, or other slowdowns. Cloudflare recommends users experiencing these issues upgrade to a minimum <a href="https://support.microsoft.com/en-us/topic/july-8-2025-kb5062553-os-build-26100-4652-523e69cb-051b-43c6-8376-6a76d6caeefd">Windows 11 24H2 version KB5062553</a> or higher for resolution. This warning will be omitted from future release notes. This Windows update was released in July 2025.</p>
</li>
<li>
<p>Devices with KB5055523 installed may receive a warning about <code>Win32/ClickFix.ABA</code> being present in the installer. To resolve this false positive, update Microsoft Security Intelligence to <a href="https://www.microsoft.com/en-us/wdsi/definitions/antimalware-definition-release-notes?requestVersion=1.429.19.0">version 1.429.19.0</a> or later. This warning will be omitted from future release notes. This Microsoft Security Intelligence update was released in May 2025.</p>
</li>
<li>
<p>DNS resolution may be broken when the following conditions are all true:</p>
<ul>
<li>The client is in Secure Web Gateway without DNS filtering (tunnel-only) mode.</li>
<li>A custom DNS server address is configured on the primary network adapter.</li>
<li>The custom DNS server address on the primary network adapter is changed while the client is connected.</li>
</ul>
<p>To work around this issue, reconnect the client by selecting <strong>Disconnect</strong> and then <strong>Connect</strong> in the client user interface.</p>
</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-07">Apr 7, 2026</time><div>
<h2 id="post-2026-04-07-triage-status-tracking"><a href="/changelog/post/2026-04-07-triage-status-tracking/">User Submission Triage Status Tracking</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>Cloudflare Email security now supports <strong>Triage Status Tracking for User Submissions</strong>. This enhancement gives SOC teams a streamlined way to track, manage, and prioritize user-submitted emails directly within the Cloudflare One dashboard.</p>
<ul>
<li>The User Submissions table now includes a <strong>Status</strong> column with three states: <strong>Unreviewed</strong> (new submissions awaiting triage), <strong>Reviewed</strong> (submissions assessed by the SOC team), and <strong>Escalated</strong> (submissions escalated to team submissions for further investigation). Analysts can quickly update statuses and filter the table to focus on what needs attention.</li>
<li>SOC teams can now organize their triage workflows, avoid duplicate reviews, and make sure critical threats get escalated for deeper investigation—bringing order to the chaos of high-volume submission management.</li>
</ul>
<p>Triage Status Tracking is <strong>automatically available</strong> for all Email security customers using the user submissions feature. No additional configuration is required; customers just need to make sure user submissions are being sent to their user submission aliases.</p>
<p>This applies to all Email security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-07">Apr 7, 2026</time><div>
<h2 id="post-2026-04-07-link-aggregation-lacp-appliance"><a href="/changelog/post/2026-04-07-link-aggregation-lacp-appliance/">Link aggregation (LACP) support for Cloudflare One Appliance</a></h2>
<div class="changelog-badges"><span>cloudflare-one-appliance</span><span>cloudflare-one</span><span>cloudflare-wan</span></div><div class="changelog-body"><p>Cloudflare One Appliance now supports Link Aggregation Control Protocol (LACP), allowing you to bundle up to six physical LAN ports into a single logical interface. Link aggregation increases available bandwidth and eliminates single points of failure on the LAN side of the appliance.</p>
<p>This feature is available in beta on physical appliance hardware with the latest OS. No entitlement is required.</p>
<p>To configure a Link Aggregation Group, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/link-aggregation/">Configure link aggregation groups</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-07">Apr 7, 2026</time><div>
<h2 id="post-2026-04-07-mtls-byoca-dashboard"><a href="/changelog/post/2026-04-07-mtls-byoca-dashboard/">Manage mTLS and BYO CA certificates from the Cloudflare dashboard</a></h2>
<div class="changelog-badges"><span>ssl</span></div><div class="changelog-body"><p>You can now manage mutual TLS (mTLS) and Bring Your Own Certificate Authority
(BYO CA) configurations directly from the Cloudflare dashboard — no API required.</p>
<p>Previously, these advanced workflows required the Cloudflare API. The following
are now available in the dashboard:</p>
<ul>
<li><strong>AOP certificate management</strong> — Upload and manage your own
certificate authorities for <a href="/ssl/origin-configuration/authenticated-origin-pull/">Authenticated Origin Pulls (AOP)</a>
directly from the dashboard.</li>
<li><strong>BYO Client mTLS certificate management</strong> — Upload and manage your own CA
certificates for <a href="/ssl/client-certificates/byo-ca/">client mTLS enforcement</a>
without needing API access.</li>
<li><strong>CDN hostname to client mTLS certificate mapping</strong> — Associate client mTLS
certificates with specific hostnames directly from the dashboard.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-07">Apr 7, 2026</time><div>
<h2 id="post-2026-04-06-redesigned-support-portal"><a href="/changelog/post/2026-04-06-redesigned-support-portal/">Redesigned Support Portal for faster, personalized help</a></h2>
<div class="changelog-badges"><span>support</span></div><div class="changelog-body"><h4 id="2026-04-06-redesigned-support-portal-redesigned-get-help-portal-for-faster-personalized-help">Redesigned &quot;Get Help&quot; Portal for faster, personalized help</h4>
<p>Cloudflare has officially launched a redesigned &quot;Get Help&quot; Support Portal to eliminate friction and get you to a resolution faster. Previously, navigating support meant clicking through multiple tiles, categorizing your own technical issues across 50+ conditional fields, and translating your problem into Cloudflare's internal taxonomy.</p>
<p>The new experience replaces that complexity with a personalized front door built around your specific account plan. Whether you are under a DDoS attack or have a simple billing question, the portal now presents a single, clean page that surfaces the direct paths available to you — such as &quot;Ask AI&quot;, &quot;Chat with a human&quot;, or &quot;Community&quot; — without the manual triage.</p>
<h4 id="2026-04-06-redesigned-support-portal-what-s-new">What's New</h4>
<ul>
<li><strong>One Page, Clear Choices</strong>: No more navigating a grid of overlapping categories. The portal now uses action cards tailored to your plan (Free, Pro, Business, or Enterprise), ensuring you only see the support channels you can actually use.</li>
<li><strong>A Radically Simpler Support Form</strong>: We've reduced the ticket submission process from four+ screens and 50+ fields to a single screen with five critical inputs. You describe the issue in your own words, and our backend handles the categorization.</li>
<li><strong>AI-Driven Triage</strong>: Using <a href="https://developers.cloudflare.com/workers-ai/">Cloudflare Workers AI</a> and <a href="https://developers.cloudflare.com/vectorize/">Vectorize</a>, the portal now automatically generates case subjects and predicts product categories.</li>
</ul>
<h4 id="2026-04-06-redesigned-support-portal-moving-complexity-to-the-backend">Moving complexity to the backend</h4>
<p>Behind the scenes, we've moved the complexity from the user to our own developer stack. When you describe an issue, we use semantic embeddings to capture intent rather than just keywords.</p>
<p>By leveraging case-based reasoning, our system compares your request against millions of resolved cases to route your inquiry to the specialist best equipped to help. This ensures that while the front-end experience is simpler for you, the back-end routing is more accurate than ever.</p>
<p>To learn more, refer to the <a href="/support/contacting-cloudflare-support/">Support documentation</a> or select <strong>Get Help</strong> directly in the <a href="https://dash.cloudflare.com/">Cloudflare Dashboard</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-07">Apr 7, 2026</time><div>
<h2 id="post-2026-04-07-waf-release"><a href="/changelog/post/2026-04-07-waf-release/">WAF Release - 2026-04-07</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's release introduces new detections for a critical Remote Code Execution (RCE) vulnerability in MCP Server (CVE-2026-23744), alongside targeted protection for an authentication bypass vulnerability in SolarWinds products (CVE-2025-40552). Additionally, this release includes a new generic detection rule designed to identify and block Cross-Site Scripting (XSS) injection attempts leveraging &quot;OnEvent&quot; handlers within HTTP cookies.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>MCP Server (CVE-2026-23744): A vulnerability in the Model Context Protocol (MCP) server implementation where malformed input payloads can trigger a memory corruption state, allowing for arbitrary code execution.</p>
</li>
<li>
<p>SolarWinds (CVE-2025-40552): A critical flaw in the authentication module allows unauthenticated attackers to bypass security filters and gain unauthorized access to the management console due to improper identity token validation.</p>
</li>
<li>
<p>XSS OnEvents Cookies: This generic rule identifies malicious event handlers (such as onload or onerror) embedded within HTTP cookie values.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>Successful exploitation of the MCP Server and SolarWinds vulnerabilities could allow unauthenticated attackers to execute arbitrary code or gain administrative control, leading to a full system takeover. Additionally, the new generic XSS detection prevents attackers from leveraging browser event handlers in cookies to hijack user sessions or execute malicious scripts.</p>
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
				<code class="nb-rule-id" title="73ae1cf103da4bacaa2e1a610aa410af">0aa410af</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - 5 - Body</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="a88a85b0cc5a4bc2abead6289131ec2f">9131ec2f</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - 5 - Header</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="28518cdc40544979bbd86720551eb9e5">551eb9e5</code>
</td>
<td>N/A</td>
<td>Generic Rules - Command Execution - 5 - URI</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="1177993d53a1467997002b44d46229eb">d46229eb</code>
</td>
<td>N/A</td>
<td>MCP Server - Remote Code Execution - CVE:CVE-2026-23744</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="3d43cdfbc3c14584942f8bc4a864b9c2">a864b9c2</code>
</td>
<td>N/A</td>
<td>XSS - OnEvents - Cookies</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="c9dbce2c1da94b24916e37559712a863">9712a863</code>
</td>
<td>N/A</td>
<td>SQLi - Evasion - Body</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="64d812e6d5844d7c9d7a44a440732d48">40732d48</code>
</td>
<td>N/A</td>
<td>SQLi - Evasion - Headers</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="50de9369ef7c45928a5dfb34e68a99b5">e68a99b5</code>
</td>
<td>N/A</td>
<td>SQLi - Evasion - URI</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="765ffb5c67b94c9589106c843e8143d2">3e8143d2</code>
</td>
<td>N/A</td>
<td>SQLi - LIKE 3 - Body</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="5c3dbd4f115e47c781491fcd70e7fb97">70e7fb97</code>
</td>
<td>N/A</td>
<td>SQLi - LIKE 3 - URI</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="89fa6027a0334949b1cb2e654c538bd9">4c538bd9</code>
</td>
<td>N/A</td>
<td>SQLi - UNION - 2 - Body</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="05946b3458364f1b9d4819d561c439c9">61c439c9</code>
</td>
<td>N/A</td>
<td>SQLi - UNION - 2 - URI</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="b2fe5c2a39df4609b6d39908cf33ea10">cf33ea10</code>
</td>
<td>N/A</td>
<td>SolarWinds - Auth Bypass - CVE:CVE-2025-40552</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-07">Apr 7, 2026</time><div>
<h2 id="post-2026-04-07-websocket-auto-reply-to-close"><a href="/changelog/post/2026-04-07-websocket-auto-reply-to-close/">WebSockets now automatically reply to Close frames</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The Workers runtime now automatically sends a reciprocal Close frame when it receives a Close frame from the peer. The <code>readyState</code> transitions to <code>CLOSED</code> before the <code>close</code> event fires. This matches the <a href="https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/close_event">WebSocket specification</a> and standard browser behavior.</p>
<p>This change is enabled by default for Workers using compatibility dates on or after <code>2026-04-07</code> (via the <a href="/workers/configuration/compatibility-flags/#websocket-auto-reply-to-close"><code>web_socket_auto_reply_to_close</code></a> compatibility flag). Existing code that manually calls <code>close()</code> inside the <code>close</code> event handler will continue to work — the call is silently ignored when the WebSocket is already closed.</p>
<pre tabindex="0"><code class="language-js">const [client, server] = Object.values(new WebSocketPair());&#10;server.accept();&#10;&#10;server.addEventListener(&quot;close&quot;, (event) =&gt; {&#10;	// readyState is already CLOSED — no need to call server.close().&#10;	console.log(server.readyState); // WebSocket.CLOSED&#10;	console.log(event.code); // 1000&#10;	console.log(event.wasClean); // true&#10;});&#10;</code></pre>
<h4 id="2026-04-07-websocket-auto-reply-to-close-half-open-mode-for-websocket-proxying">Half-open mode for WebSocket proxying</h4>
<p>The automatic close behavior can interfere with WebSocket proxying, where a Worker sits between a client and a backend and needs to coordinate the close on both sides independently. To support this use case, pass <code>{ allowHalfOpen: true }</code> to <code>accept()</code>:</p>
<pre tabindex="0"><code class="language-js">const [client, server] = Object.values(new WebSocketPair());&#10;&#10;server.accept({ allowHalfOpen: true });&#10;&#10;server.addEventListener(&quot;close&quot;, (event) =&gt; {&#10;	// readyState is still CLOSING here, giving you time&#10;	// to coordinate the close on the other side.&#10;	console.log(server.readyState); // WebSocket.CLOSING&#10;&#10;	// Manually close when ready.&#10;	server.close(event.code, &quot;done&quot;);&#10;});&#10;</code></pre>
<p>For more information, refer to <a href="/workers/runtime-apis/websockets/#close-behavior">WebSockets Close behavior</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-06">Apr 6, 2026</time><div>
<h2 id="post-2026-04-06-dane-support-mx-deployments"><a href="/changelog/post/2026-04-06-dane-support-mx-deployments/">DANE Support for MX Deployments</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>Cloudflare Email Security now supports DANE (DNS-based Authentication of Named Entities) for MX deployments. This enhancement strengthens email transport security by enabling DNSSEC-backed certificate verification for our regional MX records.</p>
<ul>
<li>Regional MX hostnames now publish DANE TLSA records backed by DNSSEC, enabling DANE-capable SMTP senders to cryptographically validate certificate identities before establishing TLS connections—moving beyond opportunistic encryption to verified encrypted delivery.</li>
<li>DANE support is automatically available for all customers using regional MX deployments. No additional configuration is required; DANE-capable mail infrastructure will automatically validate MX certificates using the published records.</li>
</ul>
<p>This applies to all Email Security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-06">Apr 6, 2026</time><div>
<h2 id="post-2026-04-06-organizations-public-beta"><a href="/changelog/post/2026-04-06-organizations-public-beta/">Organizations is now in public beta for enterprises</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>cloudflare-one</span><span>gateway</span><span>organizations</span></div><div class="changelog-body"><p>We're announcing the public beta of <strong>Organizations</strong> for enterprise customers, a new top-level Cloudflare container that lets Cloudflare customers manage multiple accounts, members, analytics, and shared policies from one centralized location.</p>
<p><strong>What's New</strong></p>
<p><strong>Organizations [BETA]</strong>: <a href="/fundamentals/organizations/">Organizations</a> are a new top-level container for centrally managing multiple accounts. Each Organization supports up to 500 accounts and 5000 zones, giving larger teams a single place to administer resources at scale.</p>
<p><strong>Self-serve onboarding</strong>: Enterprise customers can <a href="/fundamentals/organizations/setup/">create an Organization</a> in the dashboard and assign accounts where they are already Super Administrators.</p>
<p><strong>Centralized Account Management</strong>: At launch, every Organization member has the Organization Super Admin role. Organization Super Admins can invite other users and manage any child account under the Organization implicitly.
<strong>Shared policies</strong>: Share <a href="/waf/custom-rules/">WAF</a> or <a href="/cloudflare-one/traffic-policies/tiered-policies/organizations/">Gateway</a> policies across multiple accounts within your Organization to simplify centralized policy management.
<strong>Implicit access</strong>: Members of an Organization automatically receive Super Administrator permissions across child accounts, removing the need for explicit membership on each account. Additional Org-level roles will be available over the course of the year.</p>
<p><strong>Unified analytics</strong>: View, filter, and download aggregate HTTP analytics across all Organization child accounts from a single dashboard for centralized visibility into traffic patterns and security events.</p>
<p><strong>Terraform provider support</strong>: Manage Organizations with infrastructure as code from day one. Provision organizations, assign accounts, and configure settings programmatically with the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/organization">Cloudflare Terraform provider</a>.</p>
<p><strong>Shared policies</strong>: Share <a href="/waf/custom-rules/">WAF</a> or <a href="/cloudflare-one/traffic-policies/">Gateway</a> policies across multiple accounts within your Organization to simplify centralized policy management.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17731.md")</aside>
<p>For more info:</p>
<ul>
<li><a href="/fundamentals/organizations/">Get started with Organizations</a></li>
<li><a href="/fundamentals/organizations/setup/">Set up your Organization</a></li>
<li><a href="/fundamentals/organizations/limitations/">Review limitations</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-06">Apr 6, 2026</time><div>
<h2 id="post-2026-04-06-gateway-dns-response-time-ms"><a href="/changelog/post/2026-04-06-gateway-dns-response-time-ms/">New ResponseTimeMs field in Gateway DNS Logpush dataset</a></h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>Cloudflare has added a new field to the <a href="/logs/logpush/logpush-job/datasets/account/gateway_dns/#responsetimems">Gateway DNS</a> Logpush dataset:</p>
<ul>
<li><strong>ResponseTimeMs</strong>: Total response time of the DNS request in milliseconds.</li>
</ul>
<p>For the complete field definitions, refer to <a href="/logs/logpush/logpush-job/datasets/account/gateway_dns/">Gateway DNS dataset</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-05">Apr 5, 2026</time><div>
<h2 id="post-2026-04-05-regional-placement"><a href="/changelog/post/2026-04-05-regional-placement/">Control where your Containers run with regional and jurisdictional placement</a></h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>You can now specify placement constraints to control where your <a href="/containers/">Containers</a> run.</p>
<table>
<thead>
<tr>
<th>Constraint</th>
<th>Values</th>
<th>Use case</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>regions</code></td>
<td><code>ENAM</code>, <code>WNAM</code>, <code>EEUR</code>, <code>WEUR</code></td>
<td>Geographic placement</td>
</tr>
<tr>
<td><code>jurisdiction</code></td>
<td><code>eu</code>, <code>fedramp</code></td>
<td>Compliance boundaries</td>
</tr>
</tbody>
</table>
<p>Use <code>regions</code> to limit placement to specific geographic areas. Use <code>jurisdiction</code> to restrict containers to compliance boundaries — <code>eu</code> maps to European regions (EEUR, WEUR) and <code>fedramp</code> maps to North American regions (ENAM, WNAM).</p>
<p>Refer to <a href="/containers/concepts/placement/">Containers placement</a> for more details.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-04">Apr 4, 2026</time><div>
<h2 id="post-2026-04-04-gemma-4-26b-a4b-workers-ai"><a href="/changelog/post/2026-04-04-gemma-4-26b-a4b-workers-ai/">Google Gemma 4 26B A4B now available on Workers AI</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>We are partnering with Google to bring <a href="/workers-ai/models/gemma-4-26b-a4b-it/"><code>@cf/google/gemma-4-26b-a4b-it</code></a> to Workers AI. Gemma 4 26B A4B is a Mixture-of-Experts (MoE) model built from Gemini 3 research, with 26B total parameters and only 4B active per forward pass. By activating a small subset of parameters during inference, the model runs almost as fast as a 4B-parameter model while delivering the quality of a much larger one.</p>
<p>Gemma 4 is Google's most capable family of open models, designed to maximize intelligence-per-parameter.</p>
<h4 id="2026-04-04-gemma-4-26b-a4b-workers-ai-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>Mixture-of-Experts architecture</strong> with 8 active experts out of 128 total (plus 1 shared expert), delivering frontier-level performance at a fraction of the compute cost of dense models</li>
<li><strong>256,000 token context window</strong> for retaining full conversation history, tool definitions, and long documents across extended sessions</li>
<li><strong>Built-in thinking mode</strong> that lets the model reason step-by-step before answering, improving accuracy on complex tasks</li>
<li><strong>Vision understanding</strong> for object detection, document and PDF parsing, screen and UI understanding, chart comprehension, OCR (including multilingual), and handwriting recognition, with support for variable aspect ratios and resolutions</li>
<li><strong>Function calling</strong> with native support for structured tool use, enabling agentic workflows and multi-step planning</li>
<li><strong>Multilingual</strong> with out-of-the-box support for 35+ languages, pre-trained on 140+ languages</li>
<li><strong>Coding</strong> for code generation, completion, and correction</li>
</ul>
<p>Use Gemma 4 26B A4B through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/run</code> or <code>/v1/chat/completions</code>, or the <a href="/workers-ai/configuration/open-ai-compatibility/">OpenAI-compatible endpoint</a>.</p>
<p>For more information, refer to the <a href="/workers-ai/models/gemma-4-26b-a4b-it/">Gemma 4 26B A4B model page</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-03">Apr 3, 2026</time><div>
<h2 id="post-2026-04-02-warp-linux-ga"><a href="/changelog/post/2026-04-02-warp-linux-ga/">Cloudflare One Client for Linux (version 2026.3.846.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Linux Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes and improvements.</p>
<p>The next stable release for Linux will introduce the new Cloudflare One Client UI, providing a cleaner and more intuitive design as well as easier access to common actions and information.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Empty MDM files are now rejected instead of being incorrectly accepted as a single MDM config.</li>
<li>Fixed an issue in local proxy mode where the client could become unresponsive due to upstream connection timeouts.</li>
<li>Fixed an issue where the emergency disconnect status of a prior organization persisted after a switch to a different organization.</li>
<li>Consumer-only CLI commands are now clearly distinguished from Zero Trust commands.</li>
<li>Added detailed QUIC connection metrics to diagnostic logs for better troubleshooting.</li>
<li>Added monitoring for tunnel statistics collection timeouts.</li>
<li>Switched tunnel congestion control algorithm for local proxy mode to Cubic for improved reliability across platforms.</li>
<li>Fixed initiating managed network detections checks when no network is available, which caused device profile flapping.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-03">Apr 3, 2026</time><div>
<h2 id="post-2026-04-02-warp-macos-ga"><a href="/changelog/post/2026-04-02-warp-macos-ga/">Cloudflare One Client for macOS (version 2026.3.846.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release contains minor fixes and improvements.</p>
<p>The next stable release for macOS will introduce the new Cloudflare One Client UI, providing a cleaner and more intuitive design as well as easier access to common actions and information.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Empty MDM files are now rejected instead of being incorrectly accepted as a single MDM config.</li>
<li>Fixed an issue in local proxy mode where the client could become unresponsive due to upstream connection timeouts.</li>
<li>Fixed an issue where the emergency disconnect status of a prior organization persisted after a switch to a different organization.</li>
<li>Consumer-only CLI commands are now clearly distinguished from Zero Trust commands.</li>
<li>Added detailed QUIC connection metrics to diagnostic logs for better troubleshooting.</li>
<li>Added monitoring for tunnel statistics collection timeouts.</li>
<li>Switched tunnel congestion control algorithm for local proxy mode to Cubic for improved reliability across platforms.</li>
<li>Fixed initiating managed network detections checks when no network is available, which caused device profile flapping.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-02">Apr 2, 2026</time><div>
<h2 id="post-2026-04-02-mcp-portal-session-management"><a href="/changelog/post/2026-04-02-mcp-portal-session-management/">Session management for MCP server portals</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> support in-session management of upstream MCP server connections. Users can return to the server selection page at any time to enable or disable servers, reauthenticate, or change which data a server has access to — all without leaving their MCP client.</p>
<p>To return to the server selection page, ask your AI agent with a prompt like &quot;take me back to the server selection page.&quot; The portal responds with an authorization URL via <a href="https://modelcontextprotocol.io/specification/2025-03-26/server/elicitation">MCP elicitation</a> that you open in your browser:</p>
<pre tabindex="0"><code class="language-txt">https://&lt;subdomain&gt;.&lt;domain&gt;/authorize?elicitationId=&lt;ELICITATION_ID&gt;&#10;</code></pre>
<p>From the server selection page you can:</p>
<ul>
<li><strong>Enable or disable servers</strong> — Toggle individual upstream MCP servers on or off. Disabling a server removes its tools from the active session, which reduces context window usage.</li>
<li><strong>Log out and reauthenticate</strong> — Log out of a server and log back in to change which data the server has access to, or to reauthenticate with different permissions.</li>
</ul>
<p>Users can also enable or disable a server inline by asking their AI agent directly, for example &quot;enable the wiki server&quot; or &quot;disable my Jira server.&quot;</p>
<p>The portal also automatically prompts connected users to authorize new servers when an admin adds them to the portal. This requires the use of <a href="/cloudflare-one/access-controls/applications/http-apps/managed-oauth/#enable-managed-oauth-on-an-mcp-server-portal">managed OAuth</a>.</p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#manage-portal-sessions">Manage portal sessions</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-02">Apr 2, 2026</time><div>
<h2 id="post-2026-04-02-auto-retry-upstream-failures"><a href="/changelog/post/2026-04-02-auto-retry-upstream-failures/">Automatically retry on upstream provider failures on AI Gateway</a></h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p>AI Gateway now supports automatic retries at the gateway level. When an upstream provider returns an error, your gateway retries the request based on the retry policy you configure, without requiring any client-side changes.</p>
<p>You can configure the retry count (up to 5 attempts), the delay between retries (from 100ms to 5 seconds), and the backoff strategy (Constant, Linear, or Exponential). These defaults apply to all requests through the gateway, and per-request headers can override them.</p>
<p><img src="/assets/upstream/images/ai-gateway/auto-retry-changelog.png" alt="Retry Requests settings in the AI Gateway dashboard" /></p>
<p>This is particularly useful when you do not control the client making the request and cannot implement retry logic on the caller side. For more complex failover scenarios — such as failing across different providers — use <a href="/ai-gateway/features/dynamic-routing/">Dynamic Routing</a>.</p>
<p>For more information, refer to <a href="/ai-gateway/configuration/manage-gateway/#retry-requests">Manage gateways</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-02">Apr 2, 2026</time><div>
<h2 id="post-2026-04-02-bigquery-destination"><a href="/changelog/post/2026-04-02-bigquery-destination/">BigQuery as Logpush destination</a></h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>Cloudflare Logpush now supports <strong>BigQuery</strong> as a native destination.</p>
<p>Logs from Cloudflare can be sent to <a href="https://cloud.google.com/bigquery">Google Cloud BigQuery</a> via <a href="/logs/logpush/">Logpush</a>. The destination can be configured through the Logpush UI in the Cloudflare dashboard or by using the <a href="/api/resources/logpush/subresources/jobs/">Logpush API</a>.</p>
<p>For more information, refer to the <a href="/logs/logpush/logpush-job/enable-destinations/bigquery/">Destination Configuration</a> documentation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-01">Apr 1, 2026</time><div>
<h2 id="post-2026-04-01-wrangler-workflows-local"><a href="/changelog/post/2026-04-01-wrangler-workflows-local/">All Wrangler commands for Workflows now support local development</a></h2>
<div class="changelog-badges"><span>workflows</span><span>workers</span></div><div class="changelog-body"><p>All <code>wrangler workflows</code> commands now accept a <code>--local</code> flag to target a Workflow running in a local <code>wrangler dev</code> session instead of the production API.</p>
<p>You can now manage the full Workflow lifecycle locally, including triggering Workflows, listing instances, pausing, resuming, restarting, terminating, and sending events:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler workflows list --local&#10;npx wrangler workflows trigger my-workflow --local&#10;npx wrangler workflows instances list my-workflow --local&#10;npx wrangler workflows instances pause my-workflow &lt;INSTANCE_ID&gt; --local&#10;npx wrangler workflows instances send-event my-workflow &lt;INSTANCE_ID&gt; --type my-event --local&#10;</code></pre>
<p>All commands also accept <code>--port</code> to target a specific <code>wrangler dev</code> session (defaults to <code>8787</code>).</p>
<p>For more information, refer to <a href="/workflows/build/local-development/">Workflows local development</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-04-01">Apr 1, 2026</time><div>
<h2 id="post-2026-04-01-ai-search-wrangler-commands"><a href="/changelog/post/2026-04-01-ai-search-wrangler-commands/">Create, manage, search AI Search instances with Wrangler CLI</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> supports a <code>wrangler ai-search</code> command namespace. Use it to manage instances from the command line.</p>
<p>The following commands are available:</p>
<table>
<thead>
<tr>
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>wrangler ai-search create</code></td>
<td>Create a new instance with an interactive wizard</td>
</tr>
<tr>
<td><code>wrangler ai-search list</code></td>
<td>List all instances in your account</td>
</tr>
<tr>
<td><code>wrangler ai-search get</code></td>
<td>Get details of a specific instance</td>
</tr>
<tr>
<td><code>wrangler ai-search update</code></td>
<td>Update the configuration of an instance</td>
</tr>
<tr>
<td><code>wrangler ai-search delete</code></td>
<td>Delete an instance</td>
</tr>
<tr>
<td><code>wrangler ai-search search</code></td>
<td>Run a search query against an instance</td>
</tr>
<tr>
<td><code>wrangler ai-search stats</code></td>
<td>Get usage statistics for an instance</td>
</tr>
</tbody>
</table>
<p>The <code>create</code> command guides you through setup, choosing a name, source type (<code>r2</code> or <code>web</code>), and data source. You can also pass all options as flags for non-interactive use:</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search create my-instance --type r2 --source my-bucket&#10;</code></pre>
<p>Use <code>wrangler ai-search search</code> to query an instance directly from the CLI:</p>
<pre tabindex="0"><code class="language-sh">wrangler ai-search search my-instance --query &quot;how do I configure caching?&quot;&#10;</code></pre>
<p>All commands support <code>--json</code> for structured output that scripts and AI agents can parse directly.</p>
<p>For full usage details, refer to the <a href="/ai-search/wrangler-commands/">Wrangler commands documentation</a>.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/19/">Previous</a><span>Page 20 of 50</span><a class="pagination-next" rel="next" href="/changelog/21/">Next</a></nav>
</div>
