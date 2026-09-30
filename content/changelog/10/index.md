<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-07-02">Jul 2, 2026</time><div>
<h2 id="post-2026-07-02-vary-for-cache-rules"><a href="/changelog/post/2026-07-02-vary-for-cache-rules/">Cache multiple versions of a URL with Vary</a></h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>Your origin can serve different responses for the same URL — different languages based on <code>Accept-Language</code>, or different formats based on <code>Accept</code> — by returning a <a href="https://www.rfc-editor.org/rfc/rfc9110.html#name-vary"><code>Vary</code></a> response header. Cloudflare's cache now honors that header directly in <a href="/cache/how-to/cache-rules/">Cache Rules</a>, so the same URL can hold multiple cached versions and each request is matched to the right one. Content that previously had to bypass cache to stay correct can now be cached, following standard <a href="https://www.rfc-editor.org/rfc/rfc9111.html#name-calculating-cache-keys-with">HTTP caching behavior</a>.</p>
<h4 id="2026-07-02-vary-for-cache-rules-what-changed">What changed</h4>
<p>Your origin now decides which request headers matter by listing them in its <code>Vary</code> response, and you control how Cloudflare treats each one. When you have enabled Vary using a cache rule and a response includes a <code>Vary</code> header, the request headers listed become part of the cache key.</p>
<p>For each header your origin varies on, choose one of three actions:</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>Behavior</th>
<th>Best for</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>normalize</code></td>
<td>Converts equivalent header values to the same cache key value before matching, collapsing redundant versions.</td>
<td>Most <code>Accept</code>, <code>Accept-Language</code>, and <code>Accept-Encoding</code> use cases.</td>
</tr>
<tr>
<td><code>passthrough</code></td>
<td>Uses the raw header value to select the cached version and forwards it to the origin unchanged.</td>
<td>When byte-for-byte differences in the header value should create versions.</td>
</tr>
<tr>
<td><code>bypass</code></td>
<td>Bypasses cache whenever this header name appears in the origin's <code>Vary</code> response.</td>
<td>Per-user values, or headers with too many possible values to cache safely.</td>
</tr>
</tbody>
</table>
<h4 id="2026-07-02-vary-for-cache-rules-benefits">Benefits</h4>
<ul>
<li><strong>Higher cache hit ratios</strong>: <code>normalize</code> treats semantically equivalent headers as one version. For example, <code>Accept-Language: en-US, fr;q=0.8</code> and <code>Accept-Language: fr;q=0.8, en-GB</code> both resolve to the same cache key, so you serve more requests from cache instead of the origin.</li>
<li><strong>Correct content negotiation</strong>: Requests always receive the cached version that matches their headers, so language and format variants stay accurate.</li>
<li><strong>No origin or Worker changes required</strong>: If your origin already sends <code>Vary</code>, you configure the behavior entirely in Cache Rules.</li>
<li><strong>Standards-aligned</strong>: Cache key calculation follows RFC 9111, and <code>Vary: *</code> continues to bypass cache as required by RFC 9110.</li>
</ul>
<h4 id="2026-07-02-vary-for-cache-rules-availability">Availability</h4>
<p>Vary in Cache Rules is available on all plans (Free, Pro, Business, and Enterprise). For per-request control in Workers subrequests, use the <a href="/workers/runtime-apis/request/#the-cfvary-property"><code>cf.vary</code></a> property.</p>
<h4 id="2026-07-02-vary-for-cache-rules-get-started">Get started</h4>
<p>Configure Vary in the <a href="https://dash.cloudflare.com/?to=/:account/:zone/caching/cache-rules">Cloudflare dashboard</a> under <strong>Caching</strong> &gt; <strong>Cache Rules</strong>, or through the <a href="/ruleset-engine/rulesets-api/">Rulesets API</a>. To learn how Vary affects cache keys and how each action works, refer to <a href="/cache/concepts/vary/">Vary</a> and the <a href="/cache/how-to/cache-rules/settings/#vary">Cache Rules Vary setting</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-02">Jul 2, 2026</time><div>
<h2 id="post-2026-07-02-log-fields-updated"><a href="/changelog/post/2026-07-02-log-fields-updated/">Updated fields across multiple Logpush datasets in Cloudflare Logs</a></h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-07-02-log-fields-updated-updated-fields-in-existing-datasets">Updated fields in existing datasets</h4>
<ul>
<li><strong>Gateway DNS</strong> (added): <code>AppliedMaxTTL</code> and <code>UpstreamRecordTTLs</code>.</li>
<li><strong>Gateway HTTP</strong> (added): <code>Warnings</code>.</li>
<li><strong>HTTP requests</strong> (added): <code>CacheLockWaitedMs</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-02">Jul 2, 2026</time><div>
<h2 id="post-2026-07-02-mesh-hostname-routing"><a href="/changelog/post/2026-07-02-mesh-hostname-routing/">Hostname routing for Cloudflare Mesh</a></h2>
<div class="changelog-badges"><span>mesh</span><span>cloudflare-one</span></div><div class="changelog-body"><p>You can now add <a href="/mesh/features/routes/#hostname-routes">hostname routes</a> to a Cloudflare Mesh node, in addition to CIDR routes.</p>
<div class="nb-interactive-component" data-cf-component="MeshHostnameRoutingDiagram"></div>
<p>Instead of managing IP ranges, you can attract traffic for a hostname to a Mesh node:</p>
<ul>
<li><strong>Private hostname</strong> (for example, <code>wiki.internal.local</code>) — reach an internal application by name, which is useful when it has an unknown or ephemeral IP. On Mesh you do not need to run a DNS server; a local hosts-file entry on the node is enough, or you can use a Gateway resolver policy for split DNS.</li>
<li><strong>Public hostname</strong> (for example, <code>www.example.com</code>) — route that hostname's traffic through the node and egress via the node's public IP.</li>
</ul>
<div class="nb-dash-button"></div>
<p>For setup steps, prerequisites, and DNS options, refer to <a href="/mesh/features/routes/#hostname-routes">Hostname routes</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-02">Jul 2, 2026</time><div>
<h2 id="post-2026-07-02-wrangler-auth-profiles"><a href="/changelog/post/2026-07-02-wrangler-auth-profiles/">Work across multiple accounts with Wrangler auth profiles</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="/workers/wrangler/">Wrangler CLI</a> now supports auth profiles: named logins that you scope to specific Cloudflare accounts and switch between automatically, based on the directory you are working in.</p>
<p>A profile is a named OAuth login bound to a directory. Commands run in that directory, and its subdirectories, use the matching account — so you can move between accounts without re-running <code>wrangler login</code>.</p>
<p>Use profiles to keep a separate login for each client when working at an agency, or to separate staging and production into different accounts. Pair a profile with an <code>account_id</code> in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> so a command cannot reach the wrong account.</p>
<pre><code class="language-sh">&#35; Create a profile for each account, choosing which accounts it can reach&#10;wrangler auth create client-a&#10;wrangler auth activate client-a ~/clients/client-a&#10;&#10;wrangler auth create client-b&#10;wrangler auth activate client-b ~/clients/client-b&#10;</code></pre>
<p>Use the <code>--profile</code> flag to run a single command with a specific profile:</p>
<pre><code class="language-sh">wrangler deploy --profile personal&#10;</code></pre>
<p>In CI and other automated environments, <code>CLOUDFLARE_API_TOKEN</code> still takes precedence over all profiles.</p>
<p>For setup, the resolution order, and the full command reference, refer to <a href="/workers/wrangler/profiles/">Authentication profiles</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-02">Jul 2, 2026</time><div>
<h2 id="post-2026-07-01-warp-linux-ga"><a href="/changelog/post/2026-07-01-warp-linux-ga/">Cloudflare One Client for Linux (version 2026.6.836.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Linux Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This package is the same release as 2026.6.822.0, with a fix for our RPM package. Previously the repository served a single build to every OS version, so an install could pull a dependency that isn't available on that release. The repository now serves the correct build for each operating system version, so installs automatically pull the dependencies that version requires. Debian and Ubuntu were not affected.</p>
<p>If you installed version 2026.6.822.0 on an RPM-based distribution, we recommend refreshing your repository configuration:</p>
<pre><code class="language-bash">sudo curl -fsSL https://pkg.cloudflareclient.com/cloudflare-warp-ascii.repo | sudo tee /etc/yum.repos.d/cloudflare-warp.repo&#10;sudo dnf clean all&#10;sudo dnf install cloudflare-warp&#10;</code></pre>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-01">Jul 1, 2026</time><div>
<h2 id="post-2026-07-01-spa-redirect-fragment-fix"><a href="/changelog/post/2026-07-01-spa-redirect-fragment-fix/">Fix redirect URL fragment encoding for single-page applications</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>Access now correctly preserves URL fragment characters (<code>/</code>, <code>?</code>, <code>=</code>, <code>&amp;</code>, <code>;</code>) when redirecting users back to an application after login. Previously, these characters were encoded with <code>encodeURIComponent</code>, which mangled fragment-based routes used by single-page applications (SPAs).</p>
<p>For example, an SPA URL like <code>https://app.example.com/#/dashboard?tab=settings&amp;view=advanced</code> would previously redirect to a broken URL after login. This is now handled correctly.</p>
<p>If your SPA users were experiencing broken navigation after authenticating through Access, this fix resolves the issue without any configuration changes.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-01">Jul 1, 2026</time><div>
<h2 id="post-2026-07-01-ssh-mfa-piv-keys"><a href="/changelog/post/2026-07-01-ssh-mfa-piv-keys/">Independent MFA for infrastructure applications</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p><a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Access for Infrastructure</a> now supports independent multi-factor authentication (MFA) for SSH connections using YubiKey PIV keys. This adds a hardware-backed second factor to SSH access, ensuring that a compromised device session alone is not sufficient to reach your servers.</p>
<p>With per-application and per-policy configuration, you can enforce PIV key authentication for sensitive usernames (for example, <code>root</code>) while applying different requirements for other usernames. You can also set an MFA session duration to control how often users must re-authenticate.</p>
<h4 id="2026-07-01-ssh-mfa-piv-keys-enrollment">Enrollment</h4>
<p>Users enroll their YubiKey PIV key through the <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a>. For enrollment instructions and SSH client setup, refer to <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/#enroll-a-piv-key-for-infrastructure-apps">Enroll a PIV key for infrastructure apps</a>.</p>
<h4 id="2026-07-01-ssh-mfa-piv-keys-configuration">Configuration</h4>
<p>For setup instructions, refer to <a href="/cloudflare-one/access-controls/policies/mfa-requirements/#infrastructure-applications">Enforce MFA for infrastructure applications</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-01">Jul 1, 2026</time><div>
<h2 id="post-2026-07-01-ai-traffic-options"><a href="/changelog/post/2026-07-01-ai-traffic-options/">New options to manage AI traffic</a></h2>
<div class="changelog-badges"><span>bots</span></div><div class="changelog-body"><p>Not all AI traffic is the same. Now, all customers — including those on the Free plan — can manage AI crawlers based on what they actually do on your site. Cloudflare groups AI traffic into three behaviors you can control independently: <a href="/bots/concepts/bot/#ai-bots">Search, Agent, and Training</a>. This lets you keep the automated traffic that sends readers and revenue back to you, while blocking the traffic that only takes from your content.</p>
<p>Each behavior maps to a real use case. <strong>Search</strong> covers crawlers that index your content so they can answer questions about it later, where you should expect referral traffic or other equitable compensation in return. <strong>Agent</strong> covers automated activity acting in real time on a person's behalf, such as chat fetch bots and browser-use agents. <strong>Training</strong> covers crawlers that take your content to train or fine-tune a model. For each preset you can choose to block on all pages, block only on pages that display ads, or choose not to block.</p>
<p><img src="/assets/upstream/images/changelog/bots/ai-bot-traffic-policies.png" alt="The Configure AI bot traffic policies screen, where Search, Agent, and Training can each be set to allow, block, or block only on pages with ads" /></p>
<p>Starting <strong>September 15, 2026</strong>, new domains onboarding to Cloudflare receive updated defaults: Bots classified as Training or as Agent are blocked on pages that display ads, while <strong>Search</strong> remains allowed. On that date, multi-purpose crawlers that combine Search and Training will be affected by the new defaults to block Training. All customers can <a href="https://dash.cloudflare.com/?to=/:account/:zone/security/settings">opt out of the new defaults</a> at any time before September 15.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-01">Jul 1, 2026</time><div>
<h2 id="post-2026-07-01-botbase-attribution-business-insights"><a href="/changelog/post/2026-07-01-botbase-attribution-business-insights/">More visibility into bot traffic with BotBase and Business Insights</a></h2>
<div class="changelog-badges"><span>bots</span></div><div class="changelog-body"><p>With Content Independence Day 2026, <a href="/bots/get-started/bot-management/">Enterprise Bot Management</a> customers get two new tools that make bot traffic far easier to see and reason about: <a href="/bots/botbase/">BotBase</a>, a searchable directory of every bot Cloudflare tracks, and <a href="/bots/business-insights/">Business Insights</a>, a dashboard that shows how much value each crawler sends back to your business.</p>
<p>BotBase is Cloudflare's directory of all known bots and agents, available directly in the dashboard. It shows how Cloudflare classifies each bot by behavior — Search, Agent, Training, and other categories such as Transact, Data Collection, SEO, and Ads Verification — so you can understand why a given crawler is visiting you. You can search and filter the full catalogue, filter your own traffic down to a single bot to investigate its activity on your zone, and copy any bot's detection ID to target it precisely in <a href="/security/rules/">Security rules</a>. Every tracked bot in BotBase is also published in <a href="https://radar.cloudflare.com/bots/directory">Cloudflare Radar's bots and agents directory</a>.</p>
<p>Business Insights is built for content owners and business decision-makers who want to know which bots help or harm their business, without reading rule syntax. The dashboard reports crawl-to-referral ratios both site-wide and per bot operator — comparing how often a company crawls your content against how many visitors it actually refers back — over the last 24 hours, 7 days, or 30 days. Each operator is labeled with Cloudflare's <a href="/bots/concepts/bot/verified-bots/">updated classification</a> and an action status of Allowed, Blocked, or Partially blocked, giving stakeholders a shared, at-a-glance view of the AI traffic reaching your site.</p>
<p><img src="/assets/upstream/images/changelog/bots/attribution-business-insights.png" alt="The Business Insights dashboard, showing bot traffic, content page requests, crawl-to-referral ratio, and a per-operator bot activity table" /></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-01">Jul 1, 2026</time><div>
<h2 id="post-2026-07-01-google-artifact-registry-images"><a href="/changelog/post/2026-07-01-google-artifact-registry-images/">Use Google Artifact Registry images with Containers</a></h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>Containers now support <a href="https://cloud.google.com/artifact-registry">Google Artifact Registry</a> images. After you configure credentials, you can use a fully qualified Google Artifact Registry image reference in your <a href="/workers/wrangler/configuration/#containers">Wrangler configuration</a> instead of first pushing the image to Cloudflare Registry.</p>
<p>Provide the service account email with <code>--gar-email</code> and pipe the service account JSON key through <code>stdin</code>:</p>
<pre><code class="language-bash">cat &lt;PATH_TO_KEY&gt; | npx wrangler containers registries configure &lt;REGION&gt;-docker.pkg.dev --gar-email=&lt;SERVICE_ACCOUNT_EMAIL&gt; --secret-name=&lt;SECRET_NAME&gt;&#10;</code></pre>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17714.md")</div>
<p>Only <code>*-docker.pkg.dev</code> hosts are supported. To configure credentials, refer to <a href="/containers/guides/image-management/#use-private-google-artifact-registry-images">Use private Google Artifact Registry images</a>.</p>
<p>For more information, refer to <a href="/containers/guides/image-management/">Image management</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-01">Jul 1, 2026</time><div>
<h2 id="post-2026-07-01-binding-unique-transformations"><a href="/changelog/post/2026-07-01-binding-unique-transformations/">Images binding is now billed per unique transformation</a></h2>
<div class="changelog-badges"><span>images</span></div><div class="changelog-body"><p>The <a href="/images/optimization/binding/">Images binding</a> is now billed per unique transformation, matching the model already used for URL-based transformations. Repeat requests for the same combination of source image and parameters within the same calendar month are counted only once.</p>
<p>Previously, every call to the binding counted as a separate transformation regardless of whether the image or parameters were unique. With this change, you can call the binding on hot paths without paying for each individual request.</p>
<p>Calls to <a href="/images/optimization/binding/#infostream"><code>.info()</code></a> are no longer billed.</p>
<p>For more information, refer to <a href="/images/pricing/#images-transformed">Images pricing</a> and the <a href="/images/optimization/binding/">Images binding documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-01">Jul 1, 2026</time><div>
<h2 id="post-2026-06-30-improved-wal-throughput"><a href="/changelog/post/2026-06-30-improved-wal-throughput/">Reduced end-to-end latency for vector changes</a></h2>
<div class="changelog-badges"><span>vectorize</span></div><div class="changelog-body"><p>We have greatly improved the throughput of the Vectorize <a href="https://blog.cloudflare.com/building-vectorize-a-distributed-vector-database-on-cloudflare-developer-platform/#the-wal">write-ahead log (WAL)</a>. As a result, we have significantly reduced the end-to-end latency for a vector change to become queryable: median latency has dropped from 2 minutes to under 30 seconds, and p99 latency from 5 minutes to under 2 minutes.</p>
<p><img src="/assets/upstream/images/vectorize/vectorize-p99-wal-batch-end-to-end-latency-improvement.png" alt="Vectorize p99 WAL batch end-to-end latency improved" /></p>
<p>This means inserts, upserts, and deletes are reflected in query results faster, improving the freshness of semantic search, recommendation, and retrieval-augmented generation (RAG) workloads. You do not need to change your code or configuration to benefit from this improvement.</p>
<p>For more information, refer to the <a href="/vectorize/">Vectorize documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-01">Jul 1, 2026</time><div>
<h2 id="post-2026-07-01-waf-release"><a href="/changelog/post/2026-07-01-waf-release/">WAF Release - 2026-07-01</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This release adds targeted coverage for a path traversal flaw in Fortinet FortiSandbox (CVE-2026-39813) and transitions the Anomaly:Header:User-Agent - Fake Bing or MSN Bot rule action from Block to Disabled.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-39813: A path traversal vulnerability in Fortinet FortiSandbox allows remote, unauthenticated attackers to read arbitrary files from the underlying filesystem due to insufficient validation of user-supplied input paths.</li>
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
				<code class="nb-rule-id" title="32075e19b1494117ac5915e8d84c92c9">d84c92c9</code>
</td>
<td>N/A</td>
<td>Fortinet FortiSandbox - Path Traversal - CVE:CVE-2026-39813</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="ae20608d93b94e97988db1bbc12cf9c8">c12cf9c8</code>
</td>
<td>N/A</td>
<td>Anomaly:Header:User-Agent - Fake Bing or MSN Bot</td>
<td>Enabled</td>
<td>Disabled</td>
<td>
				We are changing the action for this rule from BLOCK to Disabled
</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-30">Jun 30, 2026</time><div>
<h2 id="post-2026-06-30-gateway-granular-permissions"><a href="/changelog/post/2026-06-30-gateway-granular-permissions/">New permissions and roles for Gateway policies and lists</a></h2>
<div class="changelog-badges"><span>gateway</span><span>cloudflare-one</span><span>fundamentals</span></div><div class="changelog-body"><p>You can now assign granular, resource-scoped roles for <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> firewall policies and <a href="/cloudflare-one/reusable-components/lists/">Zero Trust lists</a>. Administrators can delegate access to specific policy types or list management without granting account-wide or product-wide control.</p>
<h4 id="2026-06-30-gateway-granular-permissions-what-is-new">What is new</h4>
<p>When you <a href="/fundamentals/manage-members/manage/">add a member</a> or create a <a href="/fundamentals/manage-members/policies/">permission policy</a>, the following resource-scoped roles are now available:</p>
<table>
<thead>
<tr>
<th>Role</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Zero Trust Gateway Firewall Policies Admin</td>
<td>Can view and edit all Gateway firewall policies, including DNS, HTTP, and Network policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway DNS Policies Admin</td>
<td>Can view and edit Gateway DNS policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway HTTP Policies Admin</td>
<td>Can view and edit Gateway HTTP policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Network Policies Admin</td>
<td>Can view and edit Gateway Network policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Egress Policies Admin</td>
<td>Can view and edit Gateway Egress policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Resolver Policies Admin</td>
<td>Can view and edit Gateway Resolver policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Policies Admin</td>
<td>Can view and edit all Gateway policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Policies Read</td>
<td>Can view all Gateway policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Read Only</td>
<td>Can view all Gateway resources.</td>
</tr>
<tr>
<td>Zero Trust DNS Locations Admin</td>
<td>Can view and edit DNS locations.</td>
</tr>
<tr>
<td>Zero Trust Proxy Endpoints Admin</td>
<td>Can view and edit Gateway Proxy Endpoints.</td>
</tr>
<tr>
<td>Zero Trust Account Lists Admin</td>
<td>Can view and edit all Gateway and Access lists.</td>
</tr>
<tr>
<td>Zero Trust Account Lists Read</td>
<td>Can view all Gateway and Access lists.</td>
</tr>
</tbody>
</table>
<p>These roles allow you to:</p>
<ul>
<li>Grant a network engineer write access to Network policies only, without exposing DNS or HTTP policy configuration.</li>
<li>Allow a security analyst to view all Gateway policies in read-only mode for auditing purposes.</li>
<li>Delegate list management to a team that maintains block and allow lists without giving them access to policy configuration.</li>
</ul>
<p>You can also now assign <em>Resource-scoped roles</em>. These roles are complementary to existing account-level roles, and allow you to grant access to a specific resource, like an individual Gateway policy or Cloudflare One list. <strong>Existing account-level roles continue to work.</strong> A member with the <code>Cloudflare Gateway</code> or <code>Cloudflare Zero Trust</code> role retains full access to all Gateway resources. This ensures backward compatibility for existing automation and API tokens.</p>
<h4 id="2026-06-30-gateway-granular-permissions-get-started">Get started</h4>
<ul>
<li>Review the <a href="/fundamentals/manage-members/roles/#resource-scoped-roles">resource-scoped roles</a> on the Cloudflare role reference.</li>
<li>Learn how to <a href="/fundamentals/manage-members/policies/">create permission policies</a> that use these roles.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-30">Jun 30, 2026</time><div>
<h2 id="post-2026-06-30-account-level-firewall-events"><a href="/changelog/post/2026-06-30-account-level-firewall-events/">Account-scoped firewall events dataset in Logpush</a></h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>Cloudflare Logpush now supports <a href="/logs/logpush/logpush-job/datasets/account/firewall_events/">firewall events as an account-scoped dataset</a>. Configure a single Logpush job at the account level to receive firewall events for every zone in the account, instead of creating and maintaining a separate job per zone.</p>
<p>The dataset includes a new <a href="/logs/logpush/logpush-job/datasets/account/firewall_events/#zonename"><code>ZoneName</code></a> field so you can identify which zone each event came from when consuming logs in your downstream pipeline.</p>
<h4 id="2026-06-30-account-level-firewall-events-what-s-available">What's available</h4>
<ul>
<li>A new account-scoped <code>firewall_events</code> dataset, configurable via the <a href="/api/resources/logpush/subresources/jobs/">Logpush API</a> or the Cloudflare dashboard.</li>
<li>The same fields and filter expressions supported by the existing <a href="/logs/logpush/logpush-job/datasets/zone/firewall_events/">zone-scoped firewall events dataset</a>, plus the new <code>ZoneName</code> field.</li>
<li>Support for all existing Logpush destinations.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-30">Jun 30, 2026</time><div>
<h2 id="post-2026-06-30-memory-usage-metrics"><a href="/changelog/post/2026-06-30-memory-usage-metrics/">Track memory usage for Workers and Durable Objects in the dashboard</a></h2>
<div class="changelog-badges"><span>workers</span><span>durable-objects</span></div><div class="changelog-body"><p>You can now monitor how much memory your <a href="/workers/">Workers</a> and <a href="/durable-objects/">Durable Objects</a> consume across invocations with the new <strong>Memory Usage</strong> chart in the Workers Metrics tab, broken down by P50, P90, P99, and P999 percentiles.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2026-06-26-memory-usage.png" alt="Memory usage chart showing P50, P90, P99, and P999 percentiles with deployment markers" /></p>
<p>Memory usage measures the V8 <a href="/workers/reference/how-workers-works/#isolates">isolate</a> memory at the time of each invocation, subject to the <a href="/workers/platform/limits/#memory">128 MB per-isolate limit</a> — a single isolate can handle many concurrent requests and shares memory across them.</p>
<p>Use the Memory Usage chart to:</p>
<ul>
<li><strong>Track memory trends</strong> — Spot gradual increases that may indicate a memory leak before they cause <code>Exceeded Memory</code> errors.</li>
<li><strong>Correlate with deployments</strong> — Deployment markers on the chart help you identify whether a new version introduced a memory regression.</li>
<li><strong>Right-size your Worker</strong> — Understand your baseline memory footprint and how much headroom you have before hitting the 128 MB limit.</li>
</ul>
<p>For Durable Objects, memory usage reflects the in-memory state an object holds (class properties, caches, active WebSocket connections), which persists across invocations until the object is <a href="/durable-objects/concepts/durable-object-lifecycle/">hibernated or evicted</a>. This state is not preserved across eviction, hibernation, or a crash, so persist anything important to <a href="/durable-objects/best-practices/access-durable-objects-storage/">storage</a>.</p>
<p>To view memory usage, open the <strong>Metrics</strong> tab for your <a href="https://dash.cloudflare.com/?to=/:account/workers/services/view/:worker/production/metrics">Worker</a> or <a href="https://dash.cloudflare.com/?to=/:account/workers/durable-objects">Durable Object namespace</a>. For Durable Objects, you can filter by DO ID or name to drill down into memory usage for a specific object. You can also query memory usage programmatically via the <a href="/analytics/graphql-api/tutorials/querying-workers-metrics/">GraphQL Analytics API</a> using the <code>workersInvocationsAdaptive</code> dataset — the <code>quantiles.memoryUsageBytesP50</code> through <code>quantiles.memoryUsageBytesP999</code> fields return percentile values in bytes.</p>
<p>For local memory debugging, you can also <a href="/workers/observability/dev-tools/memory-usage/">profile memory with DevTools</a> to take heap snapshots and identify specific objects causing high memory usage.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-30">Jun 30, 2026</time><div>
<h2 id="post-2026-06-29-warp-linux-ga"><a href="/changelog/post/2026-06-29-warp-linux-ga/">Cloudflare One Client for Linux (version 2026.6.822.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Linux Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces multiple features from our previous beta release into stable release, including:</p>
<ul>
<li>The client now applies DNS search suffixes configured in your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles">device profile</a> / <a href="/cloudflare-one/traffic-policies/network-policies">network policy</a>. Administrators can push a list of DNS search domains that the client appends to single-label queries, alongside any system-configured suffixes. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes">DNS search suffixes</a> for details.</li>
<li>Upgraded security of device registration to be hardware-backed. Registration tokens can now be generated in the TPM (with TPM 2.0+) whenever it is available to provide stronger protection against device impersonation. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/hardware-backed-registration/">Hardware-backed registration</a> for details.</li>
<li>Added a local-file signal source for Emergency Disconnect. In addition to the existing HTTPS polling mechanism, administrators can now configure WARP to monitor for a file on disk; the presence of the file triggers an emergency disconnect even if both Cloudflare and your own infrastructure are unreachable. Either signal being asserted triggers disconnect; both must be cleared for normal operation to resume.</li>
<li>Added new warp-cli debug commands for interactive connection diagnosis. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#extra-debug-logging">Extra debug logging</a> for details.</li>
<li>The local DNS proxy now supports DNSSEC passthrough. DNSSEC-signed responses are forwarded to the application intact (including DO/AD bits and RRSIG records), so applications that validate DNSSEC locally — including resolvers and the dig/drill tooling — work correctly through the client.</li>
<li>Added a new MDM format for organization-wide settings, including a cleaner way to configure the compliance environment (e.g. FedRAMP). The previous per-configuration approach still works, but the new format is now recommended. See the updated <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#organization_configs">Cloudflare One MDM documentation</a> for details.</li>
</ul>
<p><strong>Additional changes and improvements</strong></p>
<ul>
<li>Starting with 2026.6.822.0, the client unifies all API requests under the <code>api.devices.cloudflare.com</code> SNI, where previously both <code>zero-trust-client.cloudflareclient.com</code> and <code>notifications.cloudflareclient.com</code> were used. Review <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/">Cloudflare One Client with firewall</a> to ensure systems that rely on SNI inspection do not block the API traffic. The behavior of previous client versions is unaffected.</li>
<li><a href="/mesh/">Cloudflare Mesh</a> functionality using the Cloudflare One Client is now supported on RHEL 9 and 10.</li>
<li>Cloudflare Mesh now supports <a href="/mesh/features/routes/#hostname-routes">hostname-based routing</a>.</li>
<li>Client Certificate device-posture checks now support template variables (e.g. <code>${serial_number}</code>, <code>${device_uuid}</code>) in the Subject Alternative Name field. Previously only the Common Name field accepted variables, which broke posture rules that pinned identity to a SAN entry.</li>
<li>Improved accessibility by using high contrast colors and more defined color boundaries when high contrast is enabled in the system display settings.</li>
<li>Path MTU Discovery (PMTUD) is now enabled by default.</li>
<li>Fixed the in-client captive-portal browser rendering a blank &quot;Success&quot; page on some airline Wi-Fi networks. The browser now more consistently loads the airline's real portal page so users can complete sign-in from inside the client instead of having to open a separate browser.</li>
<li>Fixed an issue in proxy mode where hostnames containing underscores (e.g. ai_app.com) were rejected, breaking apps that depend on such hostnames (notably ChatGPT sandbox apps). The local proxy now accepts underscore-containing hostnames in CONNECT requests.</li>
<li>Fixed an issue where DNS queries would fail after the connection was idle, requiring users to retry.</li>
<li>Fixed an issue where some Debian releases experienced inaccurate version reporting for posture checks.</li>
<li>Users can now register with team names in any case format without errors.</li>
<li>New UI fixes
<ul>
<li>Fixed an issue where users with invalid MDM configurations were returned to the onboarding screen after successful authentication.</li>
<li>Added a re-auth button and banner to the home screen so users don't miss it when their session expires.</li>
<li>Added clear error messaging when the Cloudflare certificate needs to be installed.</li>
<li>Brought back support for pausing the tunnel when connected to user-specified Wi-Fi networks for consumer users.</li>
<li>New client UI now surfaces Split tunnel configuration and Local Domain Fallback configuration.</li>
<li>Added ability to configure proxy mode for consumer users.</li>
<li>Added back the option to quit for consumer users.</li>
</ul>
</li>
</ul>
<p>For RHEL deployments, this release introduces a dependency on the <a href="https://docs.fedoraproject.org/en-US/epel/">Extra Packages for Enterprise Linux</a> repository (EPEL). The EPEL repository provides packages that support the captive portal detection’s in-app browser authentication and system tray icon. See <a href="https://docs.fedoraproject.org/en-US/epel/getting-started/">Getting started with EPEL</a> for instructions on enabling EPEL.</p>
<p><strong>Known issues</strong></p>
<ul>
<li>Registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-30">Jun 30, 2026</time><div>
<h2 id="post-2026-06-29-warp-macos-ga"><a href="/changelog/post/2026-06-29-warp-macos-ga/">Cloudflare One Client for macOS (version 2026.6.822.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces multiple features from our previous beta release into stable release, including:</p>
<ul>
<li>The client now applies DNS search suffixes configured in your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles">device profile</a> / <a href="/cloudflare-one/traffic-policies/network-policies">network policy</a>. Administrators can push a list of DNS search domains that the client appends to single-label queries, alongside any system-configured suffixes. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes">DNS search suffixes</a> for details.</li>
<li>Upgraded security of device registration to be hardware-backed. Registration tokens can now be generated in the Secure Enclave whenever available to provide stronger protection against device impersonation. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/hardware-backed-registration/">Hardware-backed registration</a> for details.</li>
<li>Added a local-file signal source for Emergency Disconnect. In addition to the existing HTTPS polling mechanism, administrators can now configure WARP to monitor for a file on disk; the presence of the file triggers an emergency disconnect even if both Cloudflare and your own infrastructure are unreachable. Either signal being asserted triggers disconnect; both must be cleared for normal operation to resume.</li>
<li>Added new warp-cli debug commands for interactive connection diagnosis. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#extra-debug-logging">Extra debug logging</a> for details.</li>
<li>The local DNS proxy now supports DNSSEC passthrough. DNSSEC-signed responses are forwarded to the application intact (including DO/AD bits and RRSIG records), so applications that validate DNSSEC locally — including resolvers and the dig/drill tooling — work correctly through the client.</li>
<li>Added a new MDM format for organization-wide settings, including a cleaner way to configure the compliance environment (e.g. FedRAMP). The previous per-configuration approach still works, but the new format is now recommended. See the updated <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#organization_configs">Cloudflare One MDM documentation</a> for details.</li>
<li>Added support for dashboard-managed client version deployments. Administrators can now upgrade or downgrade the client version on enrolled devices directly from the Zero Trust dashboard. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/">Client version assignments</a> for details.</li>
</ul>
<p><strong>Additional Changes and improvements</strong></p>
<ul>
<li>Starting with 2026.6.822.0, the client unifies all API requests under the <code>api.devices.cloudflare.com</code> SNI, where previously both <code>zero-trust-client.cloudflareclient.com</code> and <code>notifications.cloudflareclient.com</code> were used. Review <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/">Cloudflare One Client with firewall</a> to ensure systems that rely on SNI inspection do not block the API traffic. The behavior of previous client versions is unaffected.</li>
<li>Client Certificate device-posture checks now support template variables (e.g. <code>${serial_number}</code>, <code>${device_uuid}</code>) in the Subject Alternative Name field. Previously only the Common Name field accepted variables, which broke posture rules that pinned identity to a SAN entry.</li>
<li>Improved accessibility by using high contrast colors and more defined color boundaries when high contrast is enabled in the macOS Display settings.</li>
<li>Path MTU Discovery (PMTUD) is now enabled by default.</li>
<li>Fixed the in-client captive-portal browser rendering a blank &quot;Success&quot; page on some airline Wi-Fi networks. The browser now more consistently loads the airline's real portal page so users can complete sign-in from inside the client instead of having to open a separate browser.</li>
<li>Fixed an issue in proxy mode where hostnames containing underscores (e.g. ai_app.com) were rejected, breaking apps that depend on such hostnames (notably ChatGPT sandbox apps). The local proxy now accepts underscore-containing hostnames in CONNECT requests.</li>
<li>Fixed an issue where DNS queries would fail after the connection was idle, requiring users to retry.</li>
<li>Users can now register with team names in any case format without errors.</li>
<li>New UI fixes
<ul>
<li>Fixed an issue where users with invalid MDM configurations were returned to the onboarding screen after successful authentication.</li>
<li>Added a re-auth button and banner to the home screen so users don't miss it when their session expires.</li>
<li>Added clear error messaging when the Cloudflare certificate needs to be installed.</li>
<li>Brought back support for pausing the tunnel when connected to user-specified Wi-Fi networks for consumer users.</li>
<li>New client UI now surfaces Split tunnel configuration and Local Domain Fallback configuration.</li>
<li>Added ability to configure proxy mode for consumer users.</li>
<li>Added back the option to quit for consumer users.</li>
</ul>
</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
<li>When deploying with Microsoft Intune, the client may be repeatedly reinstalled because Intune adds the client's embedded framework bundles to its install-detection list, and those frameworks cannot be detected as installed on their own. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/known-limitations/#repeated-reinstalls-on-macos-with-microsoft-intune">Repeated reinstalls on macOS with Microsoft Intune</a> for the workaround.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-30">Jun 30, 2026</time><div>
<h2 id="post-2026-06-29-warp-windows-ga"><a href="/changelog/post/2026-06-29-warp-windows-ga/">Cloudflare One Client for Windows (version 2026.6.822.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces multiple features from our previous beta release into stable release, including:</p>
<ul>
<li>The client now applies DNS search suffixes configured in your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles">device profile</a> / <a href="/cloudflare-one/traffic-policies/network-policies">network policy</a>. Administrators can push a list of DNS search domains that the client appends to single-label queries, alongside any system-configured suffixes. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes">DNS search suffixes</a> for details.</li>
<li>Added mandatory authentication. When enabled via MDM, the Cloudflare One Client blocks all Internet traffic from the moment the machine boots until the user authenticates, closing the visibility gap on newly deployed devices and during re-authentication. See the <a href="https://blog.cloudflare.com/mandatory-authentication-mfa/">announcement blog</a> and <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/windows-no-auth-no-internet/">documentation</a> for details.</li>
<li>Upgraded security of device registration to be hardware-backed. Registration tokens can now be generated in the TPM (with TPM 2.0+) whenever it is available to provide stronger protection against device impersonation. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/hardware-backed-registration/">Hardware-backed registration</a> for details.</li>
<li>Added a local-file signal source for Emergency Disconnect. In addition to the existing HTTPS polling mechanism, administrators can now configure WARP to monitor for a file on disk; the presence of the file triggers an emergency disconnect even if both Cloudflare and your own infrastructure are unreachable. Either signal being asserted triggers disconnect; both must be cleared for normal operation to resume.</li>
<li>Added new warp-cli debug commands for interactive connection diagnosis. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/diagnostic-logs/#extra-debug-logging">Extra debug logging</a> for details.</li>
<li>The local DNS proxy now supports DNSSEC passthrough. DNSSEC-signed responses are forwarded to the application intact (including DO/AD bits and RRSIG records), so applications that validate DNSSEC locally — including resolvers and the dig/drill tooling — work correctly through the client.</li>
<li>Added a new MDM format for organization-wide settings, including a cleaner way to configure the compliance environment (e.g. FedRAMP). The previous per-configuration approach still works, but the new format is now recommended. See the updated <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#organization_configs">Cloudflare One MDM documentation</a> for details.</li>
<li>Added support for dashboard-managed client version deployments. Administrators can now upgrade or downgrade the client version on enrolled devices directly from the Zero Trust dashboard. See <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/">Client version assignments</a> for details.</li>
</ul>
<p><strong>Additional Changes and improvements</strong></p>
<ul>
<li>Starting with 2026.6.822.0, the client unifies all API requests under the <code>api.devices.cloudflare.com</code> SNI, where previously both <code>zero-trust-client.cloudflareclient.com</code> and <code>notifications.cloudflareclient.com</code> were used. Review <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/firewall/">Cloudflare One Client with firewall</a> to ensure systems that rely on SNI inspection do not block the API traffic. The behavior of previous client versions is unaffected.</li>
<li>Client Certificate device-posture checks now support template variables (e.g. <code>${serial_number}</code>, <code>${device_uuid}</code>) in the Subject Alternative Name field. Previously only the Common Name field accepted variables, which broke posture rules that pinned identity to a SAN entry.</li>
<li>Improved accessibility by using high contrast colors and more defined color boundaries when high contrast is enabled in Windows Accessibility settings.</li>
<li>Path MTU Discovery (PMTUD) is now enabled by default.</li>
<li>The UseWebView2 registry value (HKLM\SOFTWARE\Cloudflare\CloudflareWARP\UseWebView2 = y) is once again honored by the new GUI for authentication, so administrators who prefer the embedded WebView2 browser for sign-in can opt back in. This setting was effectively ignored in the previous release; the default browser was always used. This key is now also honored for re-authentications.</li>
<li>Fixed a crash in the authentication browser when navigating to a site that prompts for browser permissions (microphone, camera, notifications, etc.). The same fix had previously landed for the captive-portal browser; this extends it to the auth browser.</li>
<li>Fixed an issue in proxy mode where hostnames containing underscores (e.g. ai_app.com) were rejected, breaking apps that depend on such hostnames (notably ChatGPT sandbox apps). The local proxy now accepts underscore-containing hostnames in CONNECT requests.</li>
<li>Fixed an issue where DNS queries would fail after the connection was idle, requiring users to retry.</li>
<li>Fixed a high CPU issue when the device wakes from sleep.</li>
<li>Users can now register with team names in any case format without errors.</li>
<li>New UI fixes
<ul>
<li>Fixed an issue where users with invalid MDM configurations were returned to the onboarding screen after successful authentication.</li>
<li>Added a re-auth button and banner to the home screen so users don't miss it when their session expires.</li>
<li>Added clear error messaging when the Cloudflare certificate needs to be installed.</li>
<li>Brought back support for pausing the tunnel when connected to user-specified Wi-Fi networks for consumer users.</li>
<li>New client UI now surfaces Split tunnel configuration and Local Domain Fallback configuration.</li>
<li>Added ability to configure proxy mode for consumer users.</li>
<li>Added back the option to quit for consumer users.</li>
</ul>
</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Single sign-on in the embedded WebView2 authentication browser may fail to use the Windows primary account, prompting for an interactive sign-in.</li>
<li>An error indicating that Microsoft Edge can't read and write to its data directory may be displayed during captive portal login; this error is benign and can be dismissed.</li>
<li>In rare cases, a registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
<li>Windows ARM may prompt the user to close running applications while trying to install this version. Simply click &quot;Ok&quot; with the default highlighted option.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-28">Jun 28, 2026</time><div>
<h2 id="post-2026-06-28-cf-vary-request-option"><a href="/changelog/post/2026-06-28-cf-vary-request-option/">Workers fetch requests now support cf.vary</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Workers <code>fetch()</code> requests now support the <code>cf.vary</code> request option. Use <code>cf.vary</code> to control how Cloudflare caches origin responses with a <code>Vary</code> header for a single subrequest.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17804.md")</div>
<p>For more information, refer to <a href="/workers/runtime-apis/request/#the-cfvary-property"><code>cf.vary</code></a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-26">Jun 26, 2026</time><div>
<h2 id="post-2026-06-26-agents-sdk-v0.17.0"><a href="/changelog/post/2026-06-26-agents-sdk-v0.17.0/">Agents SDK adds background sub-agents and a unified turn entry point</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> makes it easier to run long work in the background, drive turns through one entry point, and keep chat agents working through deploys, evictions, and reconnects.</p>
<p>This release adds first-class detached (background) sub-agent runs with live progress and durable milestones, a single <code>runTurn</code> turn-admission entry point, and a large round of recovery and reliability fixes that continue converging <code>@cloudflare/think</code> and <code>@cloudflare/ai-chat</code> onto one model.</p>
<h4 id="2026-06-26-agents-sdk-v0.17.0-background-sub-agents-with-progress-and-milestones">Background sub-agents with progress and milestones</h4>
<p><code>runAgentTool</code> can now dispatch a sub-agent without blocking the calling turn. A detached run returns a handle immediately and is owned by a durable, eviction-surviving backbone instead of being abandoned when the dispatching turn ends.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17675.md")</div>
<p>Highlights:</p>
<ul>
<li><strong>Durable, exactly-once-on-the-happy-path completion</strong> via a warm fast path plus a self-scheduling reconcile backbone that survives eviction and deploys.</li>
<li><strong>Bounded.</strong> An absolute <code>maxBudgetMs</code> ceiling (default 24h) and <code>cancelAgentTool(runId)</code> keep abandoned runs from holding a concurrency slot forever.</li>
<li><strong><code>detached: { notify: true }</code></strong> lets a finished background run inject a message back into the chat so the model reacts to the result — no hand-wired <code>onFinish</code> needed.</li>
</ul>
<p>Sub-agents can also report mid-run progress that rides their own turn stream back to the parent's connected clients:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17676.md")</div>
<p>Progress surfaces on <code>AgentToolRunState.progress</code> via <code>useAgentToolEvents</code>, so a background-runs tray can render a live bar without drilling in, and the latest snapshot is persisted for inspection after eviction. Naming a <code>milestone</code> promotes a signal to a durable, replayable row, and <code>detached: { onMilestones }</code> can surface a milestone as a synthetic chat message (<code>&quot;narrate&quot;</code> for a cheap status line, or <code>&quot;react&quot;</code> to drive a model turn).</p>
<h4 id="2026-06-26-agents-sdk-v0.17.0-one-entry-point-for-turns-runturn">One entry point for turns: <code>runTurn</code></h4>
<p><code>@cloudflare/think</code> adds a public <code>runTurn(options)</code> facade that unifies turn admission behind a single <code>mode</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17677.md")</div>
<p><code>stream</code> mode accepts array and function inputs to match <code>wait</code> mode, and all entry points now route through a shared internal admission path that throws a clear error on nested blocking admissions that previously could deadlock.</p>
<h4 id="2026-06-26-agents-sdk-v0.17.0-recovery-and-reliability">Recovery and reliability</h4>
<p>A large part of this release continues hardening recovery and converging <code>@cloudflare/think</code> and <code>@cloudflare/ai-chat</code> onto one model:</p>
<ul>
<li><strong>Stream stall watchdog.</strong> <code>AIChatAgent</code> can detect and recover from a hung model/transport stream via the opt-in <code>chatStreamStallTimeoutMs</code> watchdog. With <code>chatRecovery</code> enabled the stall routes into the same bounded-recovery machinery a deploy or eviction uses; otherwise it surfaces as a terminal stream error so the spinner clears.</li>
<li><strong>Interrupted tool-call repair.</strong> <code>AIChatAgent</code> now repairs a transcript with a dead server-tool call before re-entering inference (parity with <code>@cloudflare/think</code>), so a recovered turn no longer fails with <code>AI_MissingToolResultsError</code>. An overridable <code>repairInterruptedToolPart(part)</code> hook lets apps customize the repaired shape.</li>
<li><strong>Stuck status after reconnect.</strong> Fixed AI SDK <code>status</code> getting stuck when a reconnect races a turn that has been accepted but has not started streaming yet, so the UI now renders the in-flight turn instead of settling on <code>ready</code>.</li>
<li><strong>Live &quot;recovering…&quot; on connect.</strong> <code>AIChatAgent</code> now replays the recovering status to a client that connects mid-recovery, so <code>useAgentChat</code>'s <code>isRecovering</code> reflects in-progress recovery immediately instead of appearing frozen.</li>
<li><strong>Terminal connection failures.</strong> The client stops reconnecting on terminal WebSocket close events and exposes them via <code>connectionError</code> / <code>onConnectionError</code> on <code>AgentClient</code>, <code>useAgent</code>, and <code>useAgentChat</code>.</li>
<li><strong>Agent-tool child recovery.</strong> A healthy long-running sub-agent run is no longer abandoned as <code>interrupted</code> after a deploy (both <code>@cloudflare/think</code> and <code>AIChatAgent</code>).</li>
<li><strong>Workflows from sub-agent facets.</strong> Agent Workflows can now start from sub-agent facets, with callbacks and Workflow RPC routed back to the originating facet.</li>
<li>Plus forward-progress crediting convergence, broadcast-first give-up ordering, an event-driven auto-continuation barrier, and structured row-size compaction in <code>AIChatAgent</code>.</li>
</ul>
<h4 id="2026-06-26-agents-sdk-v0.17.0-other-improvements">Other improvements</h4>
<ul>
<li><strong>Shared chat React core.</strong> A new <code>agents/chat/react</code> entry exposes <code>useAgentChat</code>, transport helpers, and shared wire types, with <code>syncMessagesToServer</code> for server-authoritative transcript storage. <code>@cloudflare/think/react</code> and <code>@cloudflare/ai-chat/react</code> are now thin wrappers over it.</li>
<li><strong>Optional <code>ai</code> peer.</strong> The root <code>agents</code> and <code>@cloudflare/codemode</code> runtimes no longer reference AI SDK types, so they bundle without <code>ai</code> / <code>zod</code> installed; AI-specific entry points still require the peer when imported. <code>just-bash</code> likewise moves to an optional peer used only by the skills bash runner.</li>
<li><strong>Code Mode.</strong> The default <code>DynamicWorkerExecutor</code> timeout increases from 30s to 60s, executions now dispose the dynamically-loaded Worker and its RPC stub after each run (fixing a flaky isolate-shutdown assertion), connector imports are cleaned up, and the outer MCP tool-call context is passed to <code>openApiMcpServer</code> request callbacks.</li>
<li><strong>Voice.</strong> Voice turns now support AI SDK <code>fullStream</code> responses (and warn when <code>textStream</code> is used).</li>
<li><strong>MCP.</strong> <code>McpAgent</code> server-to-client requests can now be sent from callbacks that do not inherit the agent's async context, including callbacks reached through Worker Loader RPC.</li>
<li><strong>Experimental: server actions and channels.</strong> This release lays groundwork for guarded server actions (<code>action()</code> / <code>getActions()</code> with a durable replay ledger and approvals) and a unified channels surface (<code>configureChannels()</code>, <code>deliverNotice()</code>). Both are experimental and their APIs may change, so we don't recommend depending on them yet.</li>
</ul>
<h4 id="2026-06-26-agents-sdk-v0.17.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest @cloudflare/think@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Refer to the <a href="/agents/harnesses/think/">Think documentation</a>, <a href="/agents/tools/codemode/">Code Mode documentation</a>, and <a href="/agents/">Agents documentation</a> for more information.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-26">Jun 26, 2026</time><div>
<h2 id="post-2026-06-26-mcp-portal-service-tokens"><a href="/changelog/post/2026-06-26-mcp-portal-service-tokens/">Service token support for MCP server portals</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span><span>access</span></div><div class="changelog-body"><p>You can now connect autonomous agents and bots to an <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portal</a> using an <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Access service token</a>. Service token sessions can reach upstream MCP servers through the portal without a browser-based OAuth flow.</p>
<p>To set this up:</p>
<ul>
<li>Add a <a href="/cloudflare-one/access-controls/policies/#service-auth">Service Auth policy</a> that matches your service token to the portal's Access application.</li>
<li>Add a Service Auth policy that matches the same token to each linked MCP server's Access application.</li>
<li>Turn <strong>Require user auth</strong> off (<code>on_behalf: false</code>) for each linked server so the portal uses the admin credential instead of a per-user OAuth grant.</li>
</ul>
<p>The bot connects with <code>CF-Access-Client-Id</code> and <code>CF-Access-Client-Secret</code> headers and sees the tools from every linked server it is authorized for. Servers that still require per-user OAuth are excluded from service token sessions because a service token cannot complete a per-user OAuth grant.</p>
<p>For step-by-step setup, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#connect-with-a-service-token">Connect with a service token</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-26">Jun 26, 2026</time><div>
<h2 id="post-2026-06-26-durable-objects-us-jurisdiction"><a href="/changelog/post/2026-06-26-durable-objects-us-jurisdiction/">New `us` jurisdiction for Durable Objects</a></h2>
<div class="changelog-badges"><span>durable-objects</span><span>workers</span></div><div class="changelog-body"><p>Durable Objects now supports a <code>us</code> <a href="/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction">jurisdiction</a>, letting you create Durable Objects that only run and store data within the United States. Use the <code>us</code> jurisdiction when you need to keep a Durable Object's compute and storage inside the United States to meet data residency requirements.</p>
<p>Create a namespace restricted to the <code>us</code> jurisdiction the same way as any other jurisdiction:</p>
<pre><code class="language-js">// Worker&#10;export default {&#10;	async fetch(request, env) {&#10;		const usSubnamespace = env.MY_DURABLE_OBJECT.jurisdiction(&quot;us&quot;);&#10;		const stub = usSubnamespace.getByName(&quot;general&quot;);&#10;		return stub.fetch(request);&#10;	},&#10;};&#10;</code></pre>
<p>Workers may still access Durable Objects constrained to the <code>us</code> jurisdiction from anywhere in the world. The jurisdiction constraint only controls where the Durable Object itself runs and persists data.</p>
<p>For the full list of supported jurisdictions, refer to <a href="/durable-objects/reference/data-location/#restrict-durable-objects-to-a-jurisdiction">Data location — Restrict Durable Objects to a jurisdiction</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-25">Jun 25, 2026</time><div>
<h2 id="post-2026-06-25-api-token-search"><a href="/changelog/post/2026-06-25-api-token-search/">Search API tokens by name</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>You can now search API tokens by name, making it easier to find specific tokens across large token lists without manually paginating.</p>
<h4 id="2026-06-25-api-token-search-what-s-new">What's new</h4>
<ul>
<li><strong>Dashboard search</strong>: Both <a href="https://dash.cloudflare.com/?to=/:account/account-api-tokens">account API tokens</a> and <a href="https://dash.cloudflare.com/profile/api-tokens">user API tokens</a> pages now include a search bar. Type a name to filter results.</li>
<li><strong>API search support</strong>: The <a href="/api/resources/user/subresources/tokens/methods/list/"><code>/user/tokens</code></a> and <a href="/api/resources/accounts/subresources/tokens/methods/list/"><code>/accounts/{account_id}/tokens</code></a> endpoints now accept a <code>name</code> query parameter to filter tokens by name.</li>
</ul>
<p>For more information, refer to <a href="/fundamentals/api/get-started/create-token/">Create an API token</a> and <a href="/fundamentals/api/get-started/account-owned-tokens/">Account API tokens</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-25">Jun 25, 2026</time><div>
<h2 id="post-2026-06-25-durable-object-eviction-test-helpers"><a href="/changelog/post/2026-06-25-durable-object-eviction-test-helpers/">Test Durable Object eviction with new cloudflare:test helpers</a></h2>
<div class="changelog-badges"><span>durable-objects</span><span>workers</span></div><div class="changelog-body"><p>The <code>@cloudflare/vitest-pool-workers</code> package now includes <code>evictDurableObject</code> and <code>evictAllDurableObjects</code> test helpers, exported from <code>cloudflare:test</code>.</p>
<p>These helpers let you test how a Durable Object behaves across evictions, simulating the production lifecycle where an idle Durable Object can be evicted from memory.</p>
<p>For more context, refer to <a href="/durable-objects/concepts/durable-object-lifecycle/">Lifecycle of a Durable Object</a>.</p>
<pre><code class="language-ts">import { evictDurableObject, evictAllDurableObjects } from &quot;cloudflare:test&quot;;&#10;import { env } from &quot;cloudflare:workers&quot;;&#10;&#10;const id = env.COUNTER.idFromName(&quot;my-counter&quot;);&#10;const stub = env.COUNTER.get(id);&#10;&#10;// Evict the Durable Object instance pointed to by a specific stub&#10;await evictDurableObject(stub);&#10;&#10;// Close WebSockets instead of hibernating them&#10;await evictDurableObject(stub, { webSockets: &quot;close&quot; });&#10;&#10;// Evict all currently-running Durable Objects in evictable namespaces&#10;await evictAllDurableObjects();&#10;</code></pre>
<p>These helpers are available in <code>@cloudflare/vitest-pool-workers@0.16.20</code> and later.</p>
<p>Learn more in the <a href="/workers/testing/vitest-integration/test-apis/#durable-objects">Test APIs reference</a> and the <a href="/durable-objects/examples/testing-with-durable-objects/#testing-eviction">Testing Durable Objects guide</a>.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/9/">Previous</a><span>Page 10 of 50</span><a class="pagination-next" rel="next" href="/changelog/11/">Next</a></nav>
</div>
