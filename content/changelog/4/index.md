<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-08-21">Aug 21, 2026</time><div>
<h2 id="post-2026-08-21-one-click-login"><a href="/changelog/post/2026-08-21-one-click-login/">Saved login profiles for returning users</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Cloudflare Dashboard users can now save login profiles on a device for faster sign-in on future visits.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-08-21-one-click-login.png" alt="Saved login profiles for returning users" /></p>
<p><strong>What's New</strong></p>
<p><strong>Save login profiles on a device</strong>: After a successful sign-in, users can choose to save a login profile on that device. Saved profiles store the email address, login method, and last-used profile locally in the browser.</p>
<p><strong>Faster sign-in for returning users</strong>: Saved profiles appear directly on the login page. Selecting one can prefill the email field for password logins or resume the associated SSO or social login flow.</p>
<p>Up to five login profiles can be saved per device, and saved profiles can be removed from the profile list at any time.</p>
<p>For more info:</p>
<ul>
<li><a href="/fundamentals/user-profiles/login/">Log in to Cloudflare</a></li>
<li><a href="/fundamentals/manage-members/dashboard-sso/">Set up dashboard SSO</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-21">Aug 21, 2026</time><div>
<h2 id="post-2026-08-21-scim-put-group-synchronization"><a href="/changelog/post/2026-08-21-scim-put-group-synchronization/">Improved SCIM 2.0 group synchronization</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>Dashboard SCIM now supports replacing groups using HTTP <code>PUT</code>, as defined by <a href="https://datatracker.ietf.org/doc/html/rfc7644#section-3.5.1">RFC 7644 section 3.5.1</a>. This allows identity providers to synchronize a group's full state, including its display name, external ID, and members, in a single request.</p>
<p><strong>What's New</strong></p>
<p><strong>Group replacement via <code>PUT</code></strong>: Full-state group synchronization improves compatibility with identity providers that use replacement semantics and helps keep Cloudflare groups aligned with their source identity provider.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17732.md")</aside>
<p>For more information:</p>
<ul>
<li><a href="/fundamentals/account/account-security/scim-setup/">SCIM provisioning overview</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-21">Aug 21, 2026</time><div>
<h2 id="post-2026-08-21-improved-soft-navigation-measurement-for-single-page-applications"><a href="/changelog/post/2026-08-21-improved-soft-navigation-measurement-for-single-page-applications/">Web Analytics improves soft navigation measurement for Single Page Applications (SPAs)</a></h2>
<div class="changelog-badges"><span>web-analytics</span></div><div class="changelog-body"><p>Cloudflare Web Analytics (Real User Monitoring) is rolling out accuracy improvements to client-side soft navigations. <strong>Update: this update is complete as of 2026-09-04.</strong></p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-20">Aug 20, 2026</time><div>
<h2 id="post-2026-08-20-limits-increase"><a href="/changelog/post/2026-08-20-limits-increase/">Run more headless browsers concurrently with Browser Run</a></h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p><a href="/browser-run/">Browser Run</a> lets you automate headless browsers on Cloudflare's global network. Run full browser sessions for interactive workflows, or use <a href="/browser-run/quick-actions/">Quick Actions</a> for one-request tasks such as screenshots, PDFs, and capturing page content.</p>
<p>If you are on the <a href="/workers/platform/pricing/">Workers Paid plan</a>, your default <a href="/browser-run/limits/#workers-paid">limits</a> are now higher:</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Previous</th>
<th>New</th>
</tr>
</thead>
<tbody>
<tr>
<td>Concurrent browsers</td>
<td>120</td>
<td><strong>200</strong></td>
</tr>
<tr>
<td>New browser instances / second</td>
<td>1</td>
<td><strong>3</strong></td>
</tr>
<tr>
<td>Quick Actions requests / second</td>
<td>10</td>
<td><strong>30</strong></td>
</tr>
</tbody>
</table>
<p>You can now run hundreds of browser sessions in parallel, launch new browsers faster, and process three times as many <a href="/browser-run/quick-actions/">Quick Actions</a> per second. These published limits are defaults, not maximums. If your workload needs more more concurrent browsers, <a href="https://forms.gle/CdueDKvb26mTaepa9">request higher limits</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-20">Aug 20, 2026</time><div>
<h2 id="post-2026-08-20-fuse-local-development"><a href="/changelog/post/2026-08-20-fuse-local-development/">Use FUSE in local Containers development</a></h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>Miniflare now automatically grants local Containers the Docker privileges required for Filesystem in Userspace (FUSE). This applies to <code>wrangler dev</code>, the Cloudflare Vite plugin, and direct Miniflare use.</p>
<p>Miniflare grants these privileges when the local Docker daemon runs inside a virtual machine (VM). This includes Docker engines on macOS and through Windows Subsystem for Linux (WSL). On Linux, Miniflare grants the privileges for local rootless Docker when <code>/dev/fuse</code> is available.</p>
<p>Rootful Docker on Linux does not support FUSE by default during local development. Miniflare does not grant FUSE privileges when the Docker daemon does not meet these conditions or cannot be inspected.</p>
<p>For requirements and troubleshooting, refer to <a href="/containers/guides/local-dev/#fuse-support">FUSE support during local development</a>. For a complete example, refer to <a href="/containers/examples/r2-fuse-mount/">Mount R2 buckets with FUSE</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-20">Aug 20, 2026</time><div>
<h2 id="post-2026-08-20-durable-objects-deployments-tab"><a href="/changelog/post/2026-08-20-durable-objects-deployments-tab/">View deployments for Durable Objects in the dashboard</a></h2>
<div class="changelog-badges"><span>durable-objects</span><span>workers</span></div><div class="changelog-body"><p>Durable Object namespaces now have a <strong>Deployments</strong> tab in the Cloudflare dashboard, showing the <a href="/workers/versions-and-deployments/#versions">versions</a> of the backing Worker that are currently live and the traffic split between them.</p>
<p><img src="/assets/upstream/images/changelog/durable-objects/durable-objects-deployments-tab.png" alt="The Deployments tab for a Durable Object namespace, showing two versions with their traffic %, requests/sec, error rate, and median wall time" /></p>
<div class="nb-dash-button"></div>
<p>A Durable Object namespace is backed by a Worker script, so its deployments are the same as that Worker's deployments. Previously, checking on a <a href="/workers/versions-and-deployments/gradual-deployments/">gradual deployment</a> in progress for a Durable Object meant navigating to the backing Worker. The new tab surfaces that information directly on the namespace, alongside the metrics that matter for it: requests, error rate, and wall time per version.</p>
<p>The tab is read-only — promoting, rolling back, or splitting traffic on a deployment is still managed from the backing Worker's Deployments tab.</p>
<h4 id="2026-08-20-durable-objects-deployments-tab-actual-vs-configured-traffic-split">Actual vs. configured traffic split</h4>
<p>The <strong>Traffic %</strong> column, for both Workers and Durable Objects, now shows the actual, observed traffic share for each version next to the percentage you configured. Previously, this column only showed the configured percentage. If you moved a deployment from 50/50 to 100% on a new version, the configured number updated immediately, but requests take time to catch up, and there was no way to tell how far along that shift was without checking metrics elsewhere.</p>
<p>The configured split assigns Worker versions to individual Durable Objects, not to individual requests. Because <a href="/workers/versions-and-deployments/gradual-deployments/with-durable-objects/">each Durable Object is pinned to the version it started on until you create a new deployment</a> and some objects naturally receive more traffic than others, the observed split can differ from the configured one for as long as multiple versions are active.</p>
<p>Actual traffic share is calculated from the same <a href="/analytics/graphql-api/">GraphQL Analytics API</a> data that powers other Workers and Durable Objects metrics, so standard ingestion delay and <a href="/analytics/faq/graphql-api-inconsistent-results/">sampling</a> apply. Durable Objects analytics can lag Workers analytics by several minutes, so a version's actual share may take a little longer to catch up after a change.</p>
<p>To view this, go to <strong>Workers &amp; Pages</strong> &gt; <strong>Durable Objects</strong>, select a namespace, then select the <strong>Deployments</strong> tab. For more on how gradual deployments work, refer to <a href="/workers/versions-and-deployments/gradual-deployments/">Gradual deployments</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-20">Aug 20, 2026</time><div>
<h2 id="post-2026-08-20-oauth-optional-scopes"><a href="/changelog/post/2026-08-20-oauth-optional-scopes/">Optional OAuth scopes</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>We're announcing the GA of Optional OAuth Scopes.</p>
<p>OAuth client developers can now classify configured scopes as required or optional in the Cloudflare dashboard. By default, all configured scopes remain required .</p>
<h4 id="2026-08-20-oauth-optional-scopes-what-s-new">What's New</h4>
<p><strong>Optional Scopes:</strong> OAuth clients can now mark configured scopes as optional, allowing applications to request them without requiring users to approve them.</p>
<p><strong>Scope Selection:</strong> On the consent screen, users must grant required scopes but can decline optional scopes. This helps customers apply least-privilege access to applications, CLIs, and workloads. Optional scopes are selected by default.</p>
<p><strong>Templates:</strong> The consent screen now includes <strong>Read Only</strong> and <strong>Full Access</strong> templates to make scope selection faster and easier.</p>
<p><strong>Search:</strong> Users can now search scopes in the consent screen.</p>
<p>Learn how to <a href="/fundamentals/oauth/create-an-oauth-client/#select-scopes">select client scopes</a> and <a href="/fundamentals/oauth/authorizing-an-application/#edit-optional-permissions">edit optional permissions</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-20">Aug 20, 2026</time><div>
<h2 id="post-2026-08-20-log-fields-updated"><a href="/changelog/post/2026-08-20-log-fields-updated/">New Logpush datasets and updated fields across multiple Logpush datasets in Cloudflare Logs</a></h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-20">Aug 20, 2026</time><div>
<h2 id="post-2026-08-20-pqc-key-exchange-visibility"><a href="/changelog/post/2026-08-20-pqc-key-exchange-visibility/">Per-zone post-quantum visibility in Logpush and Log Explorer</a></h2>
<div class="changelog-badges"><span>logs</span><span>log-explorer</span></div><div class="changelog-body"><p><a href="https://radar.cloudflare.com/post-quantum">Cloudflare Radar</a> publishes global statistics on post-quantum key agreement adoption across all Cloudflare traffic, but until now customers had no way to see the same measurement scoped to their own zones. This is now possible because the <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/"><code>http_requests</code></a> Logpush dataset — also queryable in <a href="/log-explorer/">Log Explorer</a> — includes a new <code>ClientTLSKeyExchangeGroup</code> field.</p>
<p>The field reports the TLS key exchange group negotiated on the client-to-Cloudflare connection, by group name. Post-quantum connections appear as <code>X25519MLKEM768</code>, and classical connections appear as <code>X25519</code>, <code>P-256</code>, or another named group. A value of <code>UNK</code> means the group could not be determined, and <code>NONE</code> means TLS was not used.</p>
<p>With this field, you can build per-zone reports showing what percentage of your inbound HTTPS traffic is protected by post-quantum key agreement, break the number down by hostname, path, user agent, or country, and push the data into your SIEM via any <a href="/logs/logpush/logpush-job/enable-destinations/">Logpush destination</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-20">Aug 20, 2026</time><div>
<h2 id="post-2026-08-20-leaked-credentials-authorization-header"><a href="/changelog/post/2026-08-20-leaked-credentials-authorization-header/">Leaked credentials detection now scans Authorization headers</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p><a href="/waf/detections/leaked-credentials/">Leaked credentials detection</a> now scans the <code>Authorization</code> request header for Basic Authentication credentials. Previously, the detection only inspected request bodies, query strings, and headers for well-known web applications or custom detection locations, which meant credentials sent through HTTP Basic Authentication were not covered by default.</p>
<p>This new default scan location decodes the <code>Authorization: Basic &lt;credentials&gt;</code> header and compares the extracted username and password against Cloudflare's database of leaked credentials, the same way as other default scan locations. Matches populate the existing <a href="/waf/detections/leaked-credentials/#leaked-credentials-fields">leaked credentials fields</a>, such as <code>cf.waf.credential_check.password_leaked</code>, and trigger the <a href="/rules/transform/managed-transforms/reference/#add-leaked-credentials-checks-header"><code>Exposed-Credential-Check</code> managed transform header</a> if configured, so you can reuse existing <a href="/waf/custom-rules/">custom rules</a> and <a href="/waf/rate-limiting-rules/">rate limiting rules</a> without changes.</p>
<p>This change was applied automatically for zones with leaked credentials detection enabled. No configuration changes are required.</p>
<p>For more information, refer to <a href="/waf/detections/leaked-credentials/">Leaked credentials detection</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-20">Aug 20, 2026</time><div>
<h2 id="post-2026-08-19-warp-macos-ga"><a href="/changelog/post/2026-08-19-warp-macos-ga/">Cloudflare One Client for macOS (version 2026.7.1343.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces multiple features from our previous beta release into stable release, including:</p>
<ul>
<li>When reauthentication is needed for any reason, the notifications are clearer and reduce the actions needed to get you back to work by redirecting to the browser for authentication instead of the app window when necessary.</li>
<li>When a network is blocking or otherwise not supportive of HTTP/3, the client will learn and adapt by switching the order of fallback for that network by starting with HTTP/2 first and then trying HTTP/3 if needed. This reduces delays in time to connectivity when joining older or heavily filtered networks.</li>
</ul>
<p><strong>Additional changes and improvements</strong></p>
<ul>
<li>Fixed the client not allowing login to another organization when currently showing &quot;Device not in organization.&quot;</li>
<li>A DNS search domain parsing failure no longer prevents connection.</li>
<li>Cloud icon now correctly reflects actual connection status instead of showing disconnected while fully connected.</li>
<li>Fixed missing certificate error display due to a race condition.</li>
<li>Fixed crash when trying to connect to captive portal on Wi-Fi.</li>
<li>Fixed empty black window after transitioning from docked dual displays to undocked/internal display.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>None</li>
</ul>
<p>For Zero Trust documentation please see: <a href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/</a><br />
For Consumer documentation please see: <a href="https://developers.cloudflare.com/warp-client/">https://developers.cloudflare.com/warp-client/</a></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-20">Aug 20, 2026</time><div>
<h2 id="post-2026-08-19-warp-windows-ga"><a href="/changelog/post/2026-08-19-warp-windows-ga/">Cloudflare One Client for Windows (version 2026.7.1343.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces multiple features from our previous beta release into stable release, including:</p>
<ul>
<li>When reauthentication is needed for any reason, the notifications are clearer and reduce the actions needed to get you back to work by redirecting to the browser for authentication instead of the app window when necessary.</li>
<li>When a network is blocking or otherwise not supportive of HTTP/3, the client will learn and adapt by switching the order of fallback for that network by starting with HTTP/2 first and then trying HTTP/3 if needed. This reduces delays in time to connectivity when joining older or heavily filtered networks.</li>
</ul>
<p><strong>Additional changes and improvements</strong></p>
<ul>
<li>Fixed a process leak in the Windows GUI that could exhaust system resources during IPC client-creation failures.</li>
<li>Fixed being unable to switch organizations when the client was stuck in the &quot;Device not in organization&quot; state.</li>
<li>Fixed an issue where Microsoft Defender would falsely flag the Cloudflare One Client installation as malicious when installing with Intune.</li>
<li>Made the Windows domain-joined posture check more reliable.</li>
<li>A DNS search domain parsing failure no longer prevents connection.</li>
<li>Cloud icon now correctly reflects actual connection status instead of showing disconnected while fully connected.</li>
<li>Fixed missing certificate error display due to a race condition.</li>
<li>Fixed empty black window after transitioning from docked dual displays to undocked/internal display.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>If a user upgrades to version 2026.7.1343.0, downgrades to an earlier version, re-registers, and then upgrades back to 2026.7.1343.0, the client might fail to connect or switch organizations. To resolve this issue, run <code>warp-cli registration delete</code> or <code>warp-cli registration delete-all</code>.</li>
</ul>
<p>For Zero Trust documentation please see: <a href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/</a><br />
For Consumer documentation please see: <a href="https://developers.cloudflare.com/warp-client/">https://developers.cloudflare.com/warp-client/</a></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-19">Aug 19, 2026</time><div>
<h2 id="post-2026-08-19-granular-permissions-resource-lists"><a href="/changelog/post/2026-08-19-granular-permissions-resource-lists/">Access resource lists now support resource-scoped roles</a></h2>
<div class="changelog-badges"><span>access</span><span>fundamentals</span></div><div class="changelog-body"><p>Members with only resource-scoped Access roles can now open Access resource list pages in the Cloudflare dashboard and call list endpoints in the API. They no longer need an additional account-scoped read-only role to list resources.</p>
<p>The dashboard and API return only resources included in the member's permission policy scopes. Filtering applies to Access applications, policies, service tokens, and identity providers. This allows administrators to delegate specific Access resources without granting account-wide visibility. Previously, the dashboard blocked these list pages and API list requests returned <code>403</code> responses.</p>
<p>For members with the Cloudflare Access App Admin role, policy lists include policies attached directly to the selected application. Reusable policies appear only when the member has the Cloudflare Access Policy Admin role for those policies.</p>
<p>For role definitions and assignment details, refer to <a href="/fundamentals/manage-members/roles/#resource-scoped-roles">Resource-scoped roles</a> and <a href="/fundamentals/manage-members/scope/">Role scopes</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-19">Aug 19, 2026</time><div>
<h2 id="post-2026-08-19-gpt-5-6-sol-discount"><a href="/changelog/post/2026-08-19-gpt-5-6-sol-discount/">Get 50% off GPT-5.6 Sol through AI Gateway</a></h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p>GPT-5.6 Sol is available through AI Gateway, and for a limited time you can use it at 50% off. If you are already using AI Gateway, point to the <code>openai/gpt-5.6-sol</code> model and the discounted pricing applies automatically — no promo code needed.</p>
<p>The promotion is available for <a href="/ai-gateway/features/unified-billing/">Unified Billing</a> users only (not <a href="/ai-gateway/configuration/bring-your-own-keys/">Bring Your Own Keys</a>). Load credits onto AI Gateway and start sending requests to <code>openai/gpt-5.6-sol</code>.</p>
<p>Discounted pricing during the promotion:</p>
<table>
<thead>
<tr>
<th>Usage</th>
<th>Promotional price</th>
<th>Standard price</th>
</tr>
</thead>
<tbody>
<tr>
<td>Input</td>
<td>$2.50 per 1M tokens</td>
<td>$5 per 1M tokens</td>
</tr>
<tr>
<td>Output</td>
<td>$15 per 1M tokens</td>
<td>$30 per 1M tokens</td>
</tr>
<tr>
<td>Cache read</td>
<td>$0.25 per 1M tokens</td>
<td>$0.50 per 1M tokens</td>
</tr>
</tbody>
</table>
<p>The promotion runs through September 18, 2026. After that date, GPT-5.6 Sol requests return to standard pricing.</p>
<p>For more details, refer to the <a href="/ai-gateway/features/unified-billing/">Unified Billing documentation</a> and the <a href="/ai/models/openai/gpt-5.6-sol/">GPT-5.6 Sol model page</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-19">Aug 19, 2026</time><div>
<h2 id="post-2026-08-19-unified-routing-threat-lists"><a href="/changelog/post/2026-08-19-unified-routing-threat-lists/">Threat Intel Lists supported in Unified Routing</a></h2>
<div class="changelog-badges"><span>cloudflare-network-firewall</span><span>magic-transit</span><span>cloudflare-wan</span></div><div class="changelog-body"><p><a href="/cloudflare-network-firewall/">Cloudflare Advanced Network Firewall</a> Threat Intel Lists are now supported for accounts using <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> mode. This feature requires a Cloudflare Advanced Network Firewall subscription.</p>
<p>Support for additional features - Rate Limiting and Managed Rulesets - is planned.</p>
<p>For the full list of current beta limitations, refer to <a href="/cloudflare-wan/reference/traffic-steering/#beta-limitations">Traffic steering beta limitations</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-19">Aug 19, 2026</time><div>
<h2 id="post-2026-08-19-vitest-plugin"><a href="/changelog/post/2026-08-19-vitest-plugin/">@cloudflare/vitest-pool-workers is now @cloudflare/vitest-plugin</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Version 1 of the Workers Vitest integration is published as <a href="https://www.npmjs.com/package/@cloudflare/vitest-plugin"><code>@cloudflare/vitest-plugin</code></a>. The package was formerly named <code>@cloudflare/vitest-pool-workers</code>.</p>
<p>The Vitest configuration API is unchanged. Existing projects must update the dependency name, package imports, and TypeScript <code>types</code> entries.</p>
<p>To migrate automatically, run:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npx @cloudflare/codemods vitest:pool-workers-to-vitest-plugin</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx @cloudflare/codemods vitest:pool-workers-to-vitest-plugin" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn @cloudflare/codemods vitest:pool-workers-to-vitest-plugin</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn @cloudflare/codemods vitest:pool-workers-to-vitest-plugin" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm @cloudflare/codemods vitest:pool-workers-to-vitest-plugin</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm @cloudflare/codemods vitest:pool-workers-to-vitest-plugin" aria-label="Copy to clipboard">Copy</button></div></div>
<p>The codemod updates your dependency, imports, and test TypeScript configuration. For manual migration steps, refer to <a href="/workers/testing/vitest-integration/migration-guides/migrate-to-vitest-plugin/">Migrate to Vitest plugin</a>.</p>
<p>For outbound request mocks in Workers tests, use the <a href="https://github.com/mswjs/cloudflare"><code>@msw/cloudflare</code></a> integration. Refer to <a href="/workers/testing/vitest-integration/mock-outbound-requests/">Mock outbound requests</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-19">Aug 19, 2026</time><div>
<h2 id="post-2026-08-19-warp-linux-ga"><a href="/changelog/post/2026-08-19-warp-linux-ga/">Cloudflare One Client for Linux (version 2026.7.1343.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Linux Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces multiple features from our previous beta release into stable release, including:</p>
<ul>
<li>When reauthentication is needed for any reason, the notifications are clearer and reduce the actions needed to get you back to work by redirecting to the browser for authentication instead of the app window when necessary.</li>
<li>When a network is blocking or otherwise not supportive of HTTP/3, the client will learn and adapt by switching the order of fallback for that network by starting with HTTP/2 first and then trying HTTP/3 if needed. This reduces delays in time to connectivity when joining older or heavily filtered networks.</li>
</ul>
<p><strong>Additional changes and improvements</strong></p>
<ul>
<li>Fixed the client not allowing login to another organization when currently showing &quot;Device not in organization.&quot;</li>
<li>A DNS search domain parsing failure no longer prevents connection.</li>
<li>Cloud icon now correctly reflects actual connection status instead of showing disconnected while fully connected.</li>
<li>Fixed missing certificate error display due to a race condition.</li>
<li>Fixed empty black window after transitioning from docked dual displays to undocked/internal display.</li>
<li>Fixed hostname routes not working for Cloudflare Mesh when the IP addresses of the hostnames are local addresses.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>When in DNS Only mode, the client may send DNS queries for names that are configured for Local Domain Fallback to the encrypted DNS server instead of falling back to the system configuration. Local Domain Fallback works as expected in other client modes.</li>
</ul>
<p>For Zero Trust documentation please see: <a href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/</a><br />
For Consumer documentation please see: <a href="https://developers.cloudflare.com/warp-client/">https://developers.cloudflare.com/warp-client/</a></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-18">Aug 18, 2026</time><div>
<h2 id="post-2026-08-18-tunnel-origin-settings-dashboard"><a href="/changelog/post/2026-08-18-tunnel-origin-settings-dashboard/">Configure origin application settings for Cloudflare Tunnel in the dashboard</a></h2>
<div class="changelog-badges"><span>tunnel</span><span>cloudflare-tunnel-sase</span></div><div class="changelog-body"><p>You can now configure origin application settings directly in the Cloudflare dashboard when adding or editing a published application route for a <a href="/tunnel/">Cloudflare Tunnel</a>. These settings control how <code>cloudflared</code> connects to your origin server and were previously only available in the Cloudflare One dashboard or via local configuration files.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/tunnel-origin-settings-dashboard.gif" alt="Configure origin application settings in the Cloudflare dashboard" /></p>
<p>When editing a published application, expand <strong>Additional application settings</strong> to configure parameters organized into three categories:</p>
<ul>
<li><strong>HTTP</strong> — Set a custom HTTP Host header or disable chunked encoding.</li>
<li><strong>TLS</strong> — Configure origin server name, CA pool, TLS timeout, disable TLS verification, match SNI to host, or enable HTTP/2 to origin.</li>
<li><strong>Connection</strong> — Tune connect timeout, keep-alive timeout, keep-alive connections, TCP keep-alive interval, proxy type, or disable Happy Eyeballs.</li>
</ul>
<div class="nb-dash-button"></div>
<p>For the full list of origin parameters, refer to <a href="/tunnel/reference/origin-parameters/">Origin parameters</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-17">Aug 17, 2026</time><div>
<h2 id="post-2026-08-17-post-quantum-key-exchange-mx"><a href="/changelog/post/2026-08-17-post-quantum-key-exchange-mx/">Post-quantum key exchange for MX deployments</a></h2>
<div class="changelog-badges"><span>email-security-cf1</span></div><div class="changelog-body"><p>Cloudflare Email Security now supports post-quantum hybrid key exchange with X25519MLKEM768 on the SMTP connections we make to receive and deliver mail. Deploying Email Security in front of a provider that supports post-quantum hybrid key agreement (like Google Workspace) will create a TLS 1.3 connection using post-quantum key agreement.</p>
<p>Inbound MX connections and outbound delivery connections now negotiate the <a href="/ssl/post-quantum-cryptography/#hybrid-key-agreement">X25519MLKEM768</a> hybrid key agreement when the peer supports it, protecting SMTP traffic against <a href="https://blog.cloudflare.com/pq-2024/">harvest-now, decrypt-later</a> attacks.</p>
<p>Support is backwards compatible and enabled automatically for all customers. Senders and receivers that do not yet advertise post-quantum key agreement continue to connect with classical key exchange.</p>
<p>This applies to all Email Security packages:</p>
<ul>
<li><strong>Advantage</strong></li>
<li><strong>Enterprise</strong></li>
<li><strong>Enterprise + PhishGuard</strong></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-17">Aug 17, 2026</time><div>
<h2 id="post-2026-08-17-pool-name-analytics-filter"><a href="/changelog/post/2026-08-17-pool-name-analytics-filter/">Load balancing analytics now filters by pool name</a></h2>
<div class="changelog-badges"><span>load-balancing</span></div><div class="changelog-body"><p>Load balancing analytics now filters traffic data by pool name instead of pool ID, aligning the query behavior with the pool names displayed in the filter dropdown.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-17">Aug 17, 2026</time><div>
<h2 id="post-2026-08-17-r2-us-jurisdiction"><a href="/changelog/post/2026-08-17-r2-us-jurisdiction/">New `us` jurisdiction for R2</a></h2>
<div class="changelog-badges"><span>r2</span></div><div class="changelog-body"><p>R2 now supports a <code>us</code> <a href="/r2/reference/data-location/#jurisdictional-restrictions">jurisdiction</a>, which guarantees that bucket data is stored and processed within the United States. Use this jurisdiction when you need explicit US data residency guarantees.</p>
<p>Use the jurisdiction-specific S3 endpoint to create and access buckets in the <code>us</code> jurisdiction:</p>
<p><code>https://&lt;ACCOUNT_ID&gt;.us.r2.cloudflarestorage.com</code></p>
<p>To access a bucket in the <code>us</code> jurisdiction from Workers, set <code>jurisdiction</code> in your R2 binding:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17741.md")</div>
<p>Once an R2 bucket is created, its jurisdiction cannot be changed.</p>
<p>For setup instructions and the full list of supported jurisdictions, refer to <a href="/r2/reference/data-location/#jurisdictional-restrictions">R2 data location</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-17">Aug 17, 2026</time><div>
<h2 id="post-2026-08-17-waf-release"><a href="/changelog/post/2026-08-17-waf-release/">WAF Release - 2026-08-17</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This release updates WordPress remote code execution rule metadata in the Cloudflare Managed Ruleset and Cloudflare Free Ruleset to identify CVE-2026-65640.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-65640: A remote code execution vulnerability affecting WordPress core and plugin components. Remote, unauthenticated attackers can execute arbitrary system commands to gain unauthorized access or establish backdoors on host servers.</li>
</ul>
<p><strong>Impact</strong></p>
<p>The WordPress changes update rule metadata only; detection behavior and actions remain unchanged.</p>
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
				<code class="nb-rule-id" title="dcf635ab2e744e1a994443973590a4ad">3590a4ad</code>
</td>
<td>N/A</td>
<td>Wordpress - Remote Code Execution - CVE:CVE-2026-65640</td>
<td>Block</td>
<td>N/A</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="6ad9f2049b094c608be0f8adcfe1a93c">cfe1a93c</code>
</td>
<td>N/A</td>
<td>Wordpress - Remote Code Execution - CVE:CVE-2026-65640</td>
<td>Block</td>
<td>N/A</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-17">Aug 17, 2026</time><div>
<h2 id="post-2026-08-17-qwen-3.8-27b-workers-ai"><a href="/changelog/post/2026-08-17-qwen-3.8-27b-workers-ai/">Qwen 3.8 27B now available on Workers AI</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p><a href="/workers-ai/models/qwen3.8-27b/"><code>@cf/qwen/qwen3.8-27b</code></a> is now available on Workers AI.</p>
<p>Qwen 3.8 27B is a 27-billion-parameter instruction-tuned vision language model from Alibaba's Qwen family. It processes images and text together, with reasoning and function calling for agentic workflows.</p>
<p><strong>Key capabilities:</strong></p>
<ul>
<li><strong>Vision</strong>: Accept image and text inputs and generate text responses.</li>
<li><strong>Reasoning</strong>: Support thinking mode for complex, step-by-step problem-solving.</li>
<li><strong>Function calling</strong>: Build agents that invoke tools and APIs across multiple conversation turns.</li>
<li><strong>262,144 token context window</strong>: Retain long conversations and multimodal inputs across extended agent sessions.</li>
</ul>
<p>Use Qwen 3.8 27B through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>) or the REST API at <code>/ai/run</code>. You can also use <a href="/ai-gateway/">AI Gateway</a> with these endpoints.</p>
<p>For more information, refer to the <a href="/workers-ai/models/qwen3.8-27b/">Qwen 3.8 27B model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-14">Aug 14, 2026</time><div>
<h2 id="post-2026-08-14-websocket-data-transfer-reporting"><a href="/changelog/post/2026-08-14-websocket-data-transfer-reporting/">WebSocket reporting now includes full connection data transfer and duration</a></h2>
<div class="changelog-badges"><span>analytics</span></div><div class="changelog-body"><p>Cloudflare has fixed an issue affecting WebSocket data transfer and session duration reporting. HTTP Traffic Analytics and HTTP request logs now correctly report data transferred throughout a WebSocket connection and the duration of the full session. During the affected period, reporting captured only the bytes and duration of the initial <code>101 Switching Protocols</code> handshake for some WebSocket connections.</p>
<p>Customers with WebSocket traffic will see the correct <strong>Data Transfer</strong> in the dashboard and <code>EdgeResponseBytes</code> in analytics and HTTP request logs. Reported session duration now reflects the full WebSocket session rather than only the handshake. These changes restore the accounting of existing WebSocket traffic and duration. They do not indicate an increase in traffic or alter WebSocket connection behavior.</p>
<p>The separate <a href="/logs/logpush/logpush-job/datasets/zone/websocket_analytics/">WebSocket Analytics Logpush dataset</a> continues to provide per-connection directional byte counts, timestamps, and close details.</p>
<p>For more information about HTTP Traffic Analytics, refer to <a href="/analytics/account-and-zone-analytics/zone-analytics/#http-traffic">Zone Analytics</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-14">Aug 14, 2026</time><div>
<h2 id="post-2026-08-14-workers-access"><a href="/changelog/post/2026-08-14-workers-access/">You can now enable Access on a Worker or all Workers at once</a></h2>
<div class="changelog-badges"><span>workers</span><span>access</span></div><div class="changelog-body"><p>You now have two new ways to protect your <a href="/workers/">Workers</a> with <a href="/workers/configuration/cloudflare-access/">Cloudflare Access</a>.</p>
<p><strong>Protect an application across all its domains at once</strong></p>
<p>Until now, if a Worker was reachable on a route, a Custom Domain, and a <code>workers.dev</code> URL, you had to manually add each one to an Access application and keep the list in sync whenever routes or domains changed.</p>
<p>Now, Access attaches the policy to the Worker itself, so every associated domain and preview URL stays protected even when its routes or domains change.</p>
<p><img src="/assets/upstream/images/changelog/workers/protect-one-worker.png" alt="Access setting for protecting a single Worker" /></p>
<p><strong>Protect all new and existing Workers by default</strong></p>
<p>Make all Workers private by default, so every existing and newly created Worker requires sign-in before anyone can reach it.</p>
<p><img src="/assets/upstream/images/changelog/workers/protect-all-workers.png" alt="Account-wide Access setting that protects all Workers" /></p>
<p>If a specific Worker should remain publicly accessible, add a Worker-level bypass to exempt it.</p>
<p><img src="/assets/upstream/images/changelog/workers/make-worker-public.png" alt="Make a Worker public when all Workers are protected" /></p>
<p>Whether you protect a single application or all Workers at once, you can choose whether to protect preview deployments only or both previews and production, and control who can sign in by Cloudflare account membership, email address, or email domain.</p>
<p>For more advanced policy options, edit the policy in <a href="https://dash.cloudflare.com/?to=/:account/one/access/apps">Zero Trust</a>.</p>
<p><img src="/assets/upstream/images/changelog/workers/choose-who-can-sign-in.png" alt="Access policy configuration for controlling who can sign in" /></p>
<p><strong>View all of your Worker Access policies</strong></p>
<p>You can view and manage all of your Access policies in the <strong>Access</strong> tab of the Workers &amp; Pages section in the dashboard.</p>
<p><img src="/assets/upstream/images/changelog/workers/access-policies.png" alt="Access tab showing all configured Access policies" /></p>
<p><strong>See who is accessing your Worker</strong></p>
<p>When Access is enabled on your Worker, every authenticated request includes <code>ctx.access</code>. Call <a href="/workers/runtime-apis/context/#access"><code>ctx.access.getIdentity()</code></a> to get the user's email, name, and groups — no manual JWT validation required.</p>
<pre><code class="language-js">export default {&#10;  async fetch(request, env, ctx) {&#10;    if (!ctx.access) {&#10;      return new Response(&quot;Access did not run&quot;, { status: 401 });&#10;    }&#10;&#10;    const identity = await ctx.access.getIdentity();&#10;    return Response.json({ aud: ctx.access.aud, email: identity?.email });&#10;  },&#10;};&#10;</code></pre>
<p><strong>Test Access locally</strong></p>
<p>You can now test Cloudflare Access locally with <code>wrangler dev</code>. Add a <code>dev</code> block to your <code>wrangler.jsonc</code>:</p>
<pre><code class="language-json">{&#10;  &quot;access&quot;: {&#10;    &quot;dev&quot;: {&#10;      &quot;aud&quot;: &quot;my-app&quot;,&#10;      &quot;identity&quot;: { &quot;email&quot;: &quot;admin@example.com&quot; }&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>Your Worker will receive this identity through <code>ctx.access</code> and <code>ctx.access.getIdentity()</code>, letting you test authenticated and unauthenticated flows without deploying. Remove the <code>dev</code> block to simulate unauthenticated requests.</p>
<p><strong>API and programmatic access</strong></p>
<p>You can also set up these policies through the <a href="/workers/configuration/cloudflare-access/">Workers API</a> instead of the dashboard.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/3/">Previous</a><span>Page 4 of 50</span><a class="pagination-next" rel="next" href="/changelog/5/">Next</a></nav>
</div>
