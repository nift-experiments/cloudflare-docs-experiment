<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-05-28">May 28, 2026</time><div>
<h2 id="post-2026-05-28-named-email-recipients"><a href="/changelog/post/2026-05-28-named-email-recipients/">Send emails with named recipient addresses</a></h2>
<div class="changelog-badges"><span>email-service</span></div><div class="changelog-body"><p>You can now send emails with display names on recipient addresses in addition to the existing <code>from</code> support. Pass an object with <code>email</code> and an optional <code>name</code> field for <code>to</code>, <code>cc</code>, <code>bcc</code>, <code>replyTo</code>, or <code>from</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17723.md")</div>
<p>Plain strings remain fully supported for backward compatibility, and you can mix strings and named objects in the same array.</p>
<p>Refer to the <a href="/email-service/api/send-emails/workers-api/">Workers API</a> and <a href="/email-service/api/send-emails/rest-api/">REST API</a> documentation for full request examples.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-28">May 28, 2026</time><div>
<h2 id="post-2026-05-11-pipelines-pricing-announced"><a href="/changelog/post/2026-05-11-pipelines-pricing-announced/">Pipelines pricing announced</a></h2>
<div class="changelog-badges"><span>pipelines</span></div><div class="changelog-body"><p><a href="/pipelines/">Cloudflare Pipelines</a> is a streaming data platform that ingests events, transforms them with SQL, and writes to <a href="/r2/">R2</a> as JSON, Parquet, or <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables. Pipelines now has published pricing based on two usage dimensions: the volume of data processed by SQL transforms and the volume of data delivered to sinks. Ingress into a Pipeline stream is free.</p>
<p><strong>Billing is not yet enabled. We will provide at least 30 days notice before we start charging for Pipelines usage.</strong></p>
<p>Pipelines pricing model is designed to charge per GB based on what you use:</p>
<ul>
<li><strong>Streams (ingress)</strong>: Free, regardless of volume.</li>
<li><strong>SQL transforms</strong>: $0.04 / GB for stateless transforms (filter, reshape, unnest, cast, compute).</li>
<li><strong>Sinks</strong>: $0.03 / GB for JSON, $0.06 / GB for Parquet or Iceberg output.</li>
</ul>
<p>Workers Free plans include 1 GB / month for each dimension. Workers Paid plans include 50 GB / month.</p>
<p>For full pricing details and billing examples, refer to <a href="/pipelines/platform/pricing/">Pipelines pricing</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-28">May 28, 2026</time><div>
<h2 id="post-2026-05-11-r2-data-catalog-pricing-announced"><a href="/changelog/post/2026-05-11-r2-data-catalog-pricing-announced/">R2 Data Catalog pricing announced</a></h2>
<div class="changelog-badges"><span>r2</span><span>r2-data-catalog</span></div><div class="changelog-body"><p><a href="/r2-data-catalog/">R2 Data Catalog</a> is a managed <a href="https://iceberg.apache.org/">Apache Iceberg</a> data catalog built directly into R2 buckets, queryable by any Iceberg-compatible engine such as Spark, Snowflake, and DuckDB. R2 Data Catalog now has published pricing for catalog operations and table compaction, in addition to standard <a href="/r2/pricing/">R2 storage and operations</a>.</p>
<p>Billing is not yet enabled. We will provide at least 30 days notice before we start charging for R2 Data Catalog usage.</p>
<p>Pricing is based on two dimensions:</p>
<ul>
<li><strong>Catalog operations</strong>: $9.00 / million operations for metadata requests such as creating tables, reading table metadata, and updating table properties.</li>
<li><strong>Compaction</strong>: $0.005 / GB processed and $2.00 / million objects processed. These charges only apply when automatic compaction is turned on for a table.</li>
</ul>
<p>Both dimensions include a monthly free tier: 1 million catalog operations, 10 GB of compaction data processed, and 1 million compaction objects processed.</p>
<p>For full pricing details and billing examples, refer to <a href="/r2-data-catalog/platform/pricing/">R2 Data Catalog pricing</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-28">May 28, 2026</time><div>
<h2 id="post-2026-05-28-r2-data-catalog-dashboard"><a href="/changelog/post/2026-05-28-r2-data-catalog-dashboard/">R2 Data Catalog gets a dedicated dashboard experience</a></h2>
<div class="changelog-badges"><span>r2</span><span>r2-data-catalog</span></div><div class="changelog-body"><p><a href="/r2-data-catalog/">R2 Data Catalog</a> is a managed <a href="https://iceberg.apache.org/">Apache Iceberg</a> data catalog built directly into your R2 bucket. It exposes a standard Iceberg REST catalog interface so you can connect query engines like <a href="/r2-data-catalog/config-examples/spark-scala/">Spark</a>, <a href="/r2-data-catalog/config-examples/snowflake/">Snowflake</a>, <a href="/r2-data-catalog/config-examples/duckdb/">DuckDB</a>, and <a href="/r2-sql/">R2 SQL</a> to your data in R2.</p>
<p>R2 Data Catalog now has a dedicated section in the Cloudflare dashboard, replacing the previous settings panel embedded in R2 bucket configuration. The new experience includes:</p>
<p><img src="/assets/upstream/images/r2-data-catalog/data-catalog-dashboard.png" alt="R2 Data Catalog dashboard overview" /></p>
<ul>
<li><strong>Catalog overview</strong> — View all your catalogs in one place with catalog request counts, bucket sizes, and table maintenance status at a glance.</li>
<li><strong>Guided setup wizard</strong> — Create a catalog in three steps: choose or create an R2 bucket, configure table maintenance (compaction and snapshot expiration), and review. The wizard creates the bucket and generates a service credential automatically.</li>
<li><strong>Settings management</strong> — A dedicated settings page for each catalog with sections for general configuration, table maintenance, service credentials, and disabling the catalog. You can now enable and configure <a href="/r2-data-catalog/table-maintenance/">snapshot expiration</a> directly from the dashboard.</li>
<li><strong>Built-in metrics</strong> — Five charts on each catalog's metrics tab: bytes compacted, files compacted, catalog requests, storage size, and snapshots expired.</li>
</ul>
<p>To get started, go to <strong>R2 Data Catalog</strong> in the Cloudflare dashboard or refer to the <a href="/r2-data-catalog/get-started/">getting started guide</a> and <a href="/r2-data-catalog/manage-catalogs/">manage catalogs documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-28">May 28, 2026</time><div>
<h2 id="post-2026-05-11-r2-sql-pricing-announced"><a href="/changelog/post/2026-05-11-r2-sql-pricing-announced/">R2 SQL pricing announced</a></h2>
<div class="changelog-badges"><span>r2-sql</span></div><div class="changelog-body"><p><a href="/r2-sql/">R2 SQL</a> is a serverless, distributed query engine that runs SQL against <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables stored in <a href="/r2-data-catalog/">R2 Data Catalog</a>. R2 SQL now has published pricing based on a single dimension: the volume of compressed data scanned to execute your queries. At $2.50 / TB ($0.0025 / GB), R2 SQL is priced at half the cost of AWS Athena and less than half of Google BigQuery on-demand.</p>
<p>Billing is not yet enabled. We will provide at least 30 days notice before we start charging for R2 SQL usage.</p>
<p>Data scanned is measured on compressed bytes read from R2 object storage. This matches what you see in your R2 bucket — if a Parquet file is 100 MB on disk, scanning that file bills for 100 MB. Each query has a minimum billing increment of 10 MB.</p>
<p>All plans include 10 GB of data scanned per month. Standard <a href="/r2/pricing/">R2 storage and operations</a> and <a href="/r2-data-catalog/platform/pricing/">R2 Data Catalog</a> charges apply separately.</p>
<p>For full pricing details and billing examples, refer to <a href="/r2-sql/platform/pricing/">R2 SQL pricing</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-28">May 28, 2026</time><div>
<h2 id="post-2026-05-28-realtimekit-track-recording"><a href="/changelog/post/2026-05-28-realtimekit-track-recording/">Record specific participant audio tracks in RealtimeKit</a></h2>
<div class="changelog-badges"><span>realtime</span></div><div class="changelog-body"><p>You can now record specific participant audio tracks in RealtimeKit with <a href="/realtime/realtimekit/recording-guide/track-recording/">track recording</a>. Track recording creates separate WebM files for each participant instead of a single composite recording, which is useful for post-processing, transcription, and regulated or content-sensitive workflows.</p>
<p>To record specific participants, pass <code>user_ids</code> when starting a track recording:</p>
<pre><code class="language-bash">curl --request POST \&#10;  &#45;-url https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/realtime/kit/&lt;app_id&gt;/recordings/track \&#10;  &#45;-header &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;{&#10;  &quot;meeting_id&quot;: &quot;97440c6a-140b-40a9-9499-b23fd7a3868a&quot;,&#10;  &quot;user_ids&quot;: [&quot;user-123&quot;, &quot;user-456&quot;]&#10;}&#x27;&#10;</code></pre>
<p>To pass <code>user_ids</code> for selective track recording, use the following minimum SDK versions:</p>
<ul>
<li>Web Core: <code>@cloudflare/realtimekit</code> version <code>1.4.0</code> or later</li>
<li>Web UI Kit: <code>@cloudflare/realtimekit-ui</code>, <code>@cloudflare/realtimekit-react-ui</code>, or <code>@cloudflare/realtimekit-angular-ui</code> version <code>1.1.2</code> or later</li>
<li>Android Core or iOS Core: version <code>2.0.0</code> or later</li>
<li>Android UI Kit or iOS UI Kit: version <code>1.1.0</code> or later</li>
</ul>
<p><a href="/realtime/realtimekit/">RealtimeKit</a> provides SDKs and UI components so that you can build your own meeting experience on Cloudflare's <a href="/realtime/#realtime-sfu">global WebRTC infrastructure</a>. Teams today build products ranging from telehealth to education on RealtimeKit for global audiences. You can get started today with our <a href="/realtime/realtimekit/quickstart/">Quickstart</a> or take a look at our <a href="https://github.com/cloudflare/meet">Cloudflare Meet repo</a> as a reference.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-27">May 27, 2026</time><div>
<h2 id="post-2026-05-27-cloudy-regex-assistance"><a href="/changelog/post/2026-05-27-cloudy-regex-assistance/">Write regex using natural language in Cloudflare One</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span><span>gateway</span></div><div class="changelog-body"><p><a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> policy selectors which support regular expressions can now be authored in the dashboard using natural language. When building a <a href="/cloudflare-one/traffic-policies/expression-syntax/">policy</a> with a regex-based selector (like <code>matches regex</code>), you can describe what you want to match in plain English and the Cloudflare Agent will generate and validate a corresponding regular expression.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/gateway-regex-ai-generation.png" alt="Write policy regex using natural language" /></p>
<p>To get started, select a regex-compatible selector in the <a href="/cloudflare-one/traffic-policies/">Gateway policy builder</a> and select the icon. You'll see an input field for natural language, such as &quot;any URL starting with /api/v1&quot; or &quot;.com, .net, and .app hosts which contain <code>gooogle</code> in the host.&quot;</p>
<p>You can also use the tool to explain existing regular expressions. If a policy already contains a regex pattern, you can instantly generate a plain-language description.</p>
<p>A built-in feedback mechanism allows you to rate each interaction to help improve output quality over time.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/">Cloudflare One firewall policies</a> and expect to see the same functionality supported soon in <a href="/cloudflare-one/data-loss-prevention/">Data loss prevention profiles</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-27">May 27, 2026</time><div>
<h2 id="post-2026-05-27-transformation-flows"><a href="/changelog/post/2026-05-27-transformation-flows/">Transformation flows in Images</a></h2>
<div class="changelog-badges"><span>images</span></div><div class="changelog-body"><p><img src="/assets/upstream/images/images/custom-flow.png" alt="Custom flow configuration panel" /></p>
<p>Flows are automated rules that pair conditions (such as file extension, URL path, or query parameter) with parameters. Set up a flow to automatically apply image optimization to matching requests on your zone without writing code or changing URLs.</p>
<p>There are two modes for transformation flows:</p>
<ul>
<li><strong><a href="/images/optimization/transformations/flows/#set-up-a-provider-flow">Provider flows</a></strong> — Migrate from another image optimization service. Your existing URLs continue to work while Cloudflare rewrites provider-specific parameters to their Cloudflare equivalents. Currently, Cloudflare supports provider flows for Fastly Image Optimizer.</li>
<li><strong><a href="/images/optimization/transformations/flows/#set-up-a-custom-flow">Custom flows</a></strong> — Define your own conditions and actions for use cases like automatic format conversion, <a href="/images/optimization/make-responsive-images/#using-widthauto">responsive sizing</a> with <code>width=auto</code>, or directory-based optimization.</li>
</ul>
<p>To get started, go to <strong>Images</strong> &gt; <strong>Transformations</strong> &gt; <strong>Automation</strong> in the <a href="https://dash.cloudflare.com/?to=/:account/images/transformations">Cloudflare dashboard</a>.</p>
<p>Learn more about <a href="/images/optimization/transformations/flows/">transformation flows</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-27">May 27, 2026</time><div>
<h2 id="post-2026-05-27-cloudflared-connectivity-prechecks"><a href="/changelog/post/2026-05-27-cloudflared-connectivity-prechecks/">Cloudflare Tunnel now runs connectivity pre-checks at startup</a></h2>
<div class="changelog-badges"><span>tunnel</span><span>cloudflare-tunnel-sase</span></div><div class="changelog-body"><p>Starting with <a href="https://github.com/cloudflare/cloudflared/releases"><code>cloudflared</code> version 2026.5.2</a>, <a href="/tunnel/">Cloudflare Tunnel</a> automates the entire <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/">connectivity pre-checks workflow</a> directly inside the binary. Previously, customers had to install <code>dig</code> and <code>netcat</code> and run those commands by hand to verify their environment. Now <code>cloudflared</code> does it natively at startup — and surfaces actionable remediation when something is blocked.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/cloudflared-connectivity-prechecks.gif" alt="cloudflared connectivity pre-checks output" /></p>
<p>On every <code>cloudflared tunnel run</code> (and <code>cloudflared tunnel diag</code>), the binary now natively checks:</p>
<ul>
<li><strong>DNS resolution</strong> — <code>region1.v2.argotunnel.com</code> and <code>region2.v2.argotunnel.com</code> resolve to valid Cloudflare IPs.</li>
<li><strong>Transport connectivity</strong> — outbound <code>UDP (QUIC)</code> and <code>TCP (HTTP/2)</code> on port <code>7844</code>.</li>
<li><strong>Management API</strong> — outbound <code>TCP/443</code> to <code>api.cloudflare.com</code> for software updates.</li>
</ul>
<p>Results are printed in a scannable CLI table with three states:</p>
<ul>
<li>✅ <strong>Pass</strong> — the check succeeded.</li>
<li>⚠️ <strong>Warn</strong> — a non-blocking issue, for example the Management API is unreachable so automatic updates will not work, but the tunnel will still come up.</li>
<li>❌ <strong>Fail</strong> — a blocking issue, with a specific remediation hint (for example, <code>Allow outbound UDP on port 7844</code>).</li>
</ul>
<p>If DNS is unresolvable, or <strong>both</strong> UDP and TCP fail on port 7844, <code>cloudflared</code> exits early with the failure rather than looping on opaque <code>failed to dial</code> errors.</p>
<p>Pre-checks now run automatically on every start, which also catches regressions like overnight firewall policy changes — no need to remember to rerun the troubleshooting guide.</p>
<p>To get the new behavior, upgrade <code>cloudflared</code> to version <code>2026.5.2</code> or later. For more details, refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/">Connectivity pre-checks documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-27">May 27, 2026</time><div>
<h2 id="post-2026-05-26-warp-linux-ga"><a href="/changelog/post/2026-05-26-warp-linux-ga/">Cloudflare One Client for Linux (version 2026.4.1390.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Linux Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces the new Cloudflare One Client UI for Linux! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:</p>
<ul>
<li>Right click context menu to access the most common client actions quickly</li>
<li>Built-in captive portal login experience</li>
</ul>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>Added a new CLI command: warp-cli mdm refresh. This command executes an immediate refresh of the Mobile Device Management (MDM) configuration file.</li>
<li>Official support for RHEL 9 has been added for Cloudflare Mesh nodes. To install the RHEL 9 package, the Extra Packages for Enterprise Linux (EPEL) repository must be active, as it contains dependencies required for the tray icon and captive portal webview.</li>
<li>Fixed a proxy mode connection stall issue.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
<li>Split tunnel list configuration is not available in the new UI. Management of split tunnel entries is currently only possible via <code>warp-cli tunnel ip</code> and <code>warp-cli tunnel host</code>. UI support will be added in a future release.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-27">May 27, 2026</time><div>
<h2 id="post-2026-05-26-warp-macos-ga"><a href="/changelog/post/2026-05-26-warp-macos-ga/">Cloudflare One Client for macOS (version 2026.4.1390.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces the new Cloudflare One Client UI for macOS! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:</p>
<ul>
<li>Right click context menu to access the most common client actions quickly</li>
<li>Built-in captive portal login experience</li>
</ul>
<p><strong>Additional Changes and improvements</strong></p>
<ul>
<li>Added a new CLI command: warp-cli mdm refresh. This command executes an immediate refresh of the Mobile Device Management (MDM) configuration file.</li>
<li>Fixed a proxy mode connection stall issue.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
<li>Split tunnel list configuration is not available in the new UI. Management of split tunnel entries is currently only possible via <code>warp-cli tunnel ip</code> and <code>warp-cli tunnel host</code>. UI support will be added in a future release.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-27">May 27, 2026</time><div>
<h2 id="post-2026-05-26-warp-windows-ga"><a href="/changelog/post/2026-05-26-warp-windows-ga/">Cloudflare One Client for Windows (version 2026.4.1390.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces the new Cloudflare One Client UI for Windows! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:</p>
<ul>
<li>Right click context menu to access the most common client actions quickly</li>
<li>Built-in captive portal login experience</li>
</ul>
<p><strong>Additional Changes and improvements</strong></p>
<ul>
<li>Added a new CLI command: warp-cli mdm refresh. This command executes an immediate refresh of the Mobile Device Management (MDM) configuration file.</li>
<li>Fixed a proxy mode connection stall issue.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Registration authentication for devices via the integrated WebView2 browser is unavailable in this version as a temporary measure. As a result, the client will utilize the default browser on the device to complete the authentication process.</li>
<li>An error indicating that Microsoft Edge can't read and write to its data directory may be displayed during captive portal login; this error is benign and can be dismissed.</li>
<li>Registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
<li>Split tunnel list configuration is not available in the new UI. Management of Split Tunnel entries is currently only possible via <code>warp-cli tunnel ip</code> and <code>warp-cli tunnel host</code>. UI support will be added in a future release.</li>
<li>Windows ARM may prompt the user to close running applications while trying to install this version. Simply click “Ok” with the default highlighted option.</li>
<li>DNS resolution may be broken when the following conditions are all true:
<ul>
<li>The client is in Secure Web Gateway without DNS filtering (tunnel-only) mode.</li>
<li>A custom DNS server address is configured on the primary network adapter.</li>
<li>The custom DNS server address on the primary network adapter is changed while the client is connected.<br />
To work around this issue, please reconnect the client by selecting &quot;disconnect&quot; and then &quot;connect&quot; in the client user interface.</li>
</ul>
</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-26">May 26, 2026</time><div>
<h2 id="post-2026-05-26-bypass-status-for-uncacheable-responses"><a href="/changelog/post/2026-05-26-bypass-status-for-uncacheable-responses/">BYPASS status now returned for uncacheable responses</a></h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>Cloudflare now returns a <code>BYPASS</code> <a href="/cache/concepts/cache-responses/">cache status</a> whenever a response is not cacheable, instead of the previous mix of <code>BYPASS</code> and <code>MISS</code> that depended on why Cloudflare chose not to cache the response.</p>
<p>There are multiple reasons Cloudflare may refuse to cache a response — for example, the response exceeds the <a href="/cache/concepts/default-cache-behavior/#cacheable-size-limits">maximum cacheable file size</a> for your plan, the origin sends <code>Cache-Control: no-cache</code>, <code>private</code>, or <code>max-age=0</code>, the response includes a <code>Set-Cookie</code> header, or the request includes an <code>Authorization</code> header.</p>
<p>Previously, only some of these conditions returned <code>BYPASS</code>. Others — such as responses exceeding the maximum cacheable file size — returned <code>MISS</code> on every request, regardless of whether <a href="/cache/concepts/cache-control/#origin-cache-control-behavior">Origin Cache Control</a> was on or off. Because the response could never be cached, every subsequent request also returned <code>MISS</code>, which looked indistinguishable from a broken cache and made it hard to tell whether Cloudflare was trying and failing to cache the asset or had deliberately chosen not to cache it.</p>
<p><code>BYPASS</code> now consistently signals that Cloudflare refused to cache the response, regardless of the reason. <code>MISS</code> is reserved for cacheable responses that simply were not in the local cache at request time.</p>
<h4 id="2026-05-26-bypass-status-for-uncacheable-responses-what-to-expect-in-your-analytics">What to expect in your analytics</h4>
<p>After this change rolls out, you should see:</p>
<ul>
<li><strong>MISS rate decreases</strong>: Uncacheable responses no longer count as cache misses.</li>
<li><strong>BYPASS rate increases</strong>: These same responses are now reported as bypasses.</li>
<li><strong>Cache hit ratio increases</strong>: Hit ratio calculations no longer include uncacheable traffic that could never have been cached, giving you a more accurate view of cache effectiveness.</li>
</ul>
<p>Your total request volume and origin traffic are unchanged — only the cache status label is different.</p>
<h4 id="2026-05-26-bypass-status-for-uncacheable-responses-browser-cache-ttl-behavior-is-preserved">Browser cache TTL behavior is preserved</h4>
<p>The cache status label is the only thing changing — browser cache TTL handling for any given response is identical to what it was before:</p>
<ul>
<li>Responses that historically returned <code>MISS</code> because Cloudflare refused to cache them (for example, responses over the maximum cacheable file size) now return <code>BYPASS</code>, but continue to have browser cache TTL applied — exactly as they did when they were labeled <code>MISS</code>.</li>
<li>Responses that historically returned <code>BYPASS</code> and skipped browser cache TTL continue to skip browser cache TTL.</li>
</ul>
<p>In both cases, the decision to apply browser cache TTL depends on the underlying reason Cloudflare did not cache the response, not on the new <code>BYPASS</code> label.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-26">May 26, 2026</time><div>
<h2 id="post-2026-05-26-public-beta"><a href="/changelog/post/2026-05-26-public-beta/">Flagship now in public beta</a></h2>
<div class="changelog-badges"><span>flagship</span></div><div class="changelog-body"><p><strong><a href="/flagship/">Flagship</a></strong> is now in public beta. Evaluate feature flags directly from Cloudflare Workers with no outbound HTTP calls, using globally distributed flag configuration backed by Workers KV and Durable Objects. Flagship supports typed flag values, targeting rules, percentage rollouts, audit history, and OpenFeature-compatible SDKs.</p>
<p>Evaluate a flag from a Worker in a few lines of code:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17724.md")</div>
<p>Start creating flags from the Cloudflare dashboard today. Refer to the <a href="/flagship/get-started/">Flagship documentation</a> to get started.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-21">May 21, 2026</time><div>
<h2 id="post-2026-05-21-rest-api"><a href="/changelog/post/2026-05-21-rest-api/">Call any AI model through AI Gateway's new REST API</a></h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p>AI Gateway now uses the AI REST API on <code>api.cloudflare.com</code>. You can call any model — whether from OpenAI, Anthropic, Google, or hosted on Workers AI — through one unified API, using the same endpoints and authentication regardless of provider. Four endpoints are available:</p>
<ul>
<li><code>POST /ai/run</code> — universal endpoint for all models and modalities</li>
<li><code>POST /ai/v1/chat/completions</code> — OpenAI SDK compatible</li>
<li><code>POST /ai/v1/responses</code> — OpenAI Responses API compatible</li>
<li><code>POST /ai/v1/messages</code> — Anthropic SDK compatible</li>
</ul>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1/chat/completions&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;model&quot;: &quot;openai/gpt-5.5&quot;,&#10;    &quot;messages&quot;: [{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;What is Cloudflare?&quot;}]&#10;  }&#x27;&#10;</code></pre>
<p>All AI Gateway features — logging, caching, rate limiting, and guardrails — are applied automatically. Third-party models are billed through <a href="/ai-gateway/features/unified-billing/">Unified Billing</a>, so you do not need to manage separate provider API keys.</p>
<p>Third-party model requests are routed through your account's default gateway, which is created automatically on first use. To route requests through a specific gateway, add the <code>cf-aig-gateway-id</code> header.</p>
<p>If you are already calling Workers AI models through the existing REST API, that path (<code>/ai/run/@cf/{model}</code>) continues to work. To call Workers AI models through AI Gateway, use the <code>@cf/</code> model prefix (for example, <code>@cf/moonshotai/kimi-k2.6</code>) and include the <code>cf-aig-gateway-id</code> header to specify which gateway to route through.</p>
<p>For more details and examples, refer to the <a href="/ai-gateway/usage/rest-api/">REST API documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-21">May 21, 2026</time><div>
<h2 id="post-2026-05-21-modernised-billing-profile"><a href="/changelog/post/2026-05-21-modernised-billing-profile/">Modernized Billing Profile with new payment options</a></h2>
<div class="changelog-badges"><span>billing</span></div><div class="changelog-body"><p>The <a href="/billing/get-started/update-billing-info/">Billing Profile</a> now has a modern UI and a single space that unifies billing information, payment method management and an enhanced subscriptions view under a single <strong>Subscriptions</strong> tab.</p>
<h4 id="2026-05-21-modernised-billing-profile-what-changed">What changed</h4>
<p>The <strong>Subscriptions</strong> tab brings billing information, payment method management, and your subscriptions together in one place. The payment management and <strong>Pay overdue balances</strong> flows now use the latest checkout as product purchase flows, so you can pay with Apple Pay, Google Pay, Link, and <a href="/billing/payment-methods/instant-bank-payments-link/">Instant Bank Payments via Link</a> alongside cards and PayPal.</p>
<p>New cards complete 3D Secure authentication when the issuer requires it — for example, the EU under PSD2 and India under RBI.</p>
<p><img src="/assets/upstream/images/changelog/billing/2026-05-21-modernised-billing-profile.png" alt="Modernized Billing Profile with the Subscriptions tab" /></p>
<p>For details, refer to the <a href="/billing/">Billing Home</a> documentation.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-21">May 21, 2026</time><div>
<h2 id="post-2026-05-21-tunnel-mesh-granular-permissions"><a href="/changelog/post/2026-05-21-tunnel-mesh-granular-permissions/">Granular permissions for Cloudflare Tunnel and Cloudflare Mesh</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>cloudflare-one</span><span>cloudflare-tunnel-sase</span><span>tunnel</span><span>mesh</span></div><div class="changelog-body"><p>You can now scope Cloudflare permissions to individual <a href="/tunnel/">Cloudflare Tunnel</a> instances and <a href="/mesh/">Cloudflare Mesh</a> nodes. Administrators can delegate access to specific Tunnels or Mesh nodes without granting account-wide control over private networking.</p>
<h4 id="2026-05-21-tunnel-mesh-granular-permissions-what-is-new">What is new</h4>
<p>When you <a href="/fundamentals/manage-members/manage/">add a member</a> or create a <a href="/fundamentals/manage-members/policies/">permission policy</a>, the resource picker now lists <a href="/tunnel/">Cloudflare Tunnel</a> instances and <a href="/mesh/">Cloudflare Mesh</a> nodes as scopable resource types. You can:</p>
<ul>
<li>Grant a read-only role on a single Cloudflare Tunnel instance to a support operator for log streaming and diagnostics — without exposing other Tunnels or destructive actions.</li>
<li>Grant a write role on a specific Cloudflare Mesh node to an application team — without giving them access to the rest of your private network.</li>
<li>Scope a single policy to one or many Tunnels and Mesh nodes at once.</li>
</ul>
<h4 id="2026-05-21-tunnel-mesh-granular-permissions-how-it-works">How it works</h4>
<p>Granular permissions are a parallel layer to existing account-level roles — they do not replace them.</p>
<ul>
<li><strong>Existing account-level roles continue to work.</strong> A member with <code>Cloudflare Access</code> or <code>Cloudflare Zero Trust</code> retains write access to every Tunnel and Mesh node in the account. This ensures backward compatibility for existing automation and tokens.</li>
<li><strong>Granular permissions are additive.</strong> For any API request on a specific Tunnel or Mesh node, access is granted if the principal has <strong>either</strong> the account-level role <strong>or</strong> a granular permission for that resource.</li>
<li><strong>Resource enumeration is authorization-aware.</strong> Listing endpoints (<code>GET /accounts/{id}/cfd_tunnel</code>, <code>GET /accounts/{id}/warp_connector</code>) return only the resources the principal has at least read access to.</li>
</ul>
<h4 id="2026-05-21-tunnel-mesh-granular-permissions-get-started">Get started</h4>
<ul>
<li>Configure <a href="/tunnel/guides/granular-permissions/">granular permissions for Cloudflare Tunnel</a>.</li>
<li>Configure <a href="/cloudflare-one/networks/connectors/granular-permissions/">granular permissions for Cloudflare Tunnel and Cloudflare Mesh in Cloudflare One</a>.</li>
<li>Review the <a href="/fundamentals/manage-members/roles/#resource-scoped-roles">resource-scoped roles</a> on the Cloudflare role reference.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-21">May 21, 2026</time><div>
<h2 id="post-2026-05-21-vpc-networks-cloudflare-wan"><a href="/changelog/post/2026-05-21-vpc-networks-cloudflare-wan/">Reach Cloudflare WAN destinations from Workers VPC</a></h2>
<div class="changelog-badges"><span>workers-vpc</span></div><div class="changelog-body"><p>You can now use <a href="/workers-vpc/configuration/vpc-networks/">VPC Network</a> bindings with <code>network_id: &quot;cf1:network&quot;</code> to reach your full private network from Workers, including:</p>
<ul>
<li><a href="/mesh/">Cloudflare Mesh</a> nodes and client devices</li>
<li>Subnet routes and hostname routes announced through <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> or Cloudflare Mesh</li>
<li>Destinations connected through <a href="/cloudflare-wan/">Cloudflare WAN</a> on-ramps — GRE, IPsec, and CNI</li>
</ul>
<p>This means a single VPC Network binding can route Worker requests to private services regardless of how those services are connected to Cloudflare: through a Cloudflare Tunnel from a cloud VPC, a Mesh node on a private subnet, or a Cloudflare WAN on-ramp from your data center or branch site.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17824.md")</div>
<p>At runtime, the URL you pass to <code>fetch()</code> determines the destination:</p>
<pre><code class="language-js">// Reach a service behind a Cloudflare WAN IPsec on-ramp&#10;const response = await env.PRIVATE_NETWORK.fetch(&quot;http://10.50.0.100:8080/api&quot;);&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17823.md")</aside>
<p>For configuration options, refer to <a href="/workers-vpc/configuration/vpc-networks/">VPC Networks</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-20">May 20, 2026</time><div>
<h2 id="post-2026-05-20-new-dns-records-ux"><a href="/changelog/post/2026-05-20-new-dns-records-ux/">New DNS records UX is rolling out</a></h2>
<div class="changelog-badges"><span>dns</span></div><div class="changelog-body"><p>Starting today, everyone can opt in to a refreshed DNS records page in the Cloudflare dashboard. Over the coming weeks, the new experience will become the default for Free plan users first, followed by paid plans.</p>
<p><img src="/assets/upstream/images/changelog/dns/new-dns-ux.png" alt="New DNS records UX" /></p>
<h4 id="2026-05-20-new-dns-records-ux-what-is-new">What is new</h4>
<ul>
<li><strong>Better table experience</strong>: resizable and hideable columns, row pinning, advanced filters with logical operators (AND/OR), configurable pagination, and expanded input fields so long values are no longer cut off.</li>
<li><strong>First-class mobile experience</strong>: responsive layout with a touch-friendly, card-based UI and compact controls for small screens.</li>
<li><strong>DNS quick reference</strong>: bite-sized explainers for DNS, proxy status, and TTL, available directly in the product to help users configure records without leaving the page.</li>
<li><strong>Modern frontend</strong>: a refactor onto Cloudflare's new UI framework that improves performance and lays the foundation for future improvements.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/dns/new-dns-ux.gif" alt="New DNS records UX" /></p>
<h4 id="2026-05-20-new-dns-records-ux-rollout-plan">Rollout plan</h4>
<p>Dates are subject to change based on feedback received during the rollout.</p>
<ul>
<li><strong>20 May - 05 June</strong>: ramped rollout to Free, then Pro and Business plans.</li>
<li><strong>08 June - 03 July</strong>: ramped rollout to Enterprise plans.</li>
</ul>
<h4 id="2026-05-20-new-dns-records-ux-share-your-feedback">Share your feedback</h4>
<p>Once the new experience is turned on for your account, look for the feedback link at the top of the DNS records page in the Cloudflare dashboard and let us know what you think. Your input helps us prioritize the next round of improvements.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-20">May 20, 2026</time><div>
<h2 id="post-2026-05-20-radar-content-type-and-api-traffic"><a href="/changelog/post/2026-05-20-radar-content-type-and-api-traffic/">Content type distribution and API traffic share on Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now includes two new charts on the <a href="https://radar.cloudflare.com/traffic">traffic page</a> that provide deeper insights into the composition of HTTP traffic: a content type distribution chart and an API traffic share chart.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-20">May 20, 2026</time><div>
<h2 id="post-2026-05-20-waf-release"><a href="/changelog/post/2026-05-20-waf-release/">WAF Release - 2026-05-20</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p><strong>Key Findings</strong></p>
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
				<code class="nb-rule-id" title="bcdcec3ea63a480896513dc39e9c068d">9e9c068d</code>
</td>
<td>N/A</td>
<td>Sitecore - Cache Poisoning - CVE:CVE-2025-53693 Beta</td>
<td>N/A</td>
<td>Block</td>
<td>
				This rule is merged into the original rule "Sitecore - Cache Poisoning - CVE:CVE-2025-53693" (ID:{" "}
				<code class="nb-rule-id" title="d1bd7563e6254db48ce703807c5b669c">7c5b669c</code>).
</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-19">May 19, 2026</time><div>
<h2 id="post-2026-05-19-cloudflare-as-identity-provider"><a href="/changelog/post/2026-05-19-cloudflare-as-identity-provider/">Cloudflare as identity provider and account membership selector</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>Cloudflare Access now supports using Cloudflare itself as an <a href="/cloudflare-one/integrations/identity-providers/cloudflare/">identity provider</a>. If you publish an Access application and select Cloudflare as the login method, users can sign in with their existing Cloudflare account — no one-time PINs, no third-party IdP configuration, and no shared email inboxes. Authentication is backed by Cloudflare's own account security (including multi-factor authentication), making it both simpler to set up and more secure than OTP-based login for most use cases.</p>
<p>Cloudflare is now the <strong>default identity provider for all newly created Zero Trust accounts</strong>, replacing One-time PIN.</p>
<p>This also enables two new capabilities:</p>
<ul>
<li><strong>Cloudflare Account Member selector</strong> — A new <a href="/cloudflare-one/access-controls/policies/#cloudflare-access-selectors">policy selector</a> that matches users based on their membership in a Cloudflare account. You can target the current account or specify a different account ID for cross-account access scenarios.</li>
<li><strong>Restrict to account members</strong> — An identity provider configuration option that limits authentication to users who are members of your Cloudflare account.</li>
</ul>
<p>To get started, add Cloudflare as an <a href="/cloudflare-one/integrations/identity-providers/cloudflare/">identity provider</a> in your Zero Trust settings.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-19">May 19, 2026</time><div>
<h2 id="post-2026-05-19-event-subscriptions"><a href="/changelog/post/2026-05-19-event-subscriptions/">Event subscriptions for Artifacts lifecycle events</a></h2>
<div class="changelog-badges"><span>artifacts</span><span>queues</span></div><div class="changelog-body"><p>You can now receive <a href="/queues/event-subscriptions/">event notifications</a> for <a href="/artifacts/">Artifacts</a> repository changes and consume them from a Worker to build commit-driven automation.</p>
<p>This allows you to:</p>
<ul>
<li>Run custom workflows when a repository is created or imported</li>
<li>Kick off a build and deploy a change when an agent pushes to a repo</li>
<li>Trigger a review agent on every push</li>
</ul>
<p>Available events include:</p>
<ul>
<li><strong>Account-level events</strong> (<code>artifacts</code> source) — <code>repo.created</code>, <code>repo.deleted</code>, <code>repo.forked</code>, <code>repo.imported</code></li>
<li><strong>Repository-level events</strong> (<code>artifacts.repo</code> source) — <code>pushed</code>, <code>cloned</code>, <code>fetched</code></li>
</ul>
<p>To learn more, refer to <a href="/artifacts/guides/event-subscriptions/">Artifacts documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-19">May 19, 2026</time><div>
<h2 id="post-2026-05-19-casb-claude-compliance-api"><a href="/changelog/post/2026-05-19-casb-claude-compliance-api/">CASB adds support for Claude Compliance API</a></h2>
<div class="changelog-badges"><span>casb</span></div><div class="changelog-body"><p><a href="/cloudflare-one/integrations/cloud-and-saas/anthropic/">Cloudflare CASB</a> now integrates with the <a href="https://support.claude.com/en/articles/13015708-access-the-compliance-api">Claude Compliance API</a>. This enhancement gives security teams visibility into Claude usage patterns, admin activity, and compliance-relevant events across their organization.</p>
<p>The Claude Compliance API provides structured access to audit logs and administrative actions within Claude Enterprise and Claude Platform. Cloudflare CASB ingests this data to surface security findings that help organizations enhance their security posture and enforce AI governance.</p>
<h4 id="2026-05-19-casb-claude-compliance-api-key-capabilities">Key capabilities</h4>
<p>Starting today, security teams can scan for security findings across the following assets:</p>
<ul>
<li><strong>Public projects</strong> — Projects set to public visibility</li>
<li><strong>Project attachment</strong> — Files and documents added to projects that violate DLP policies</li>
<li><strong>Chat files</strong> — User-uploaded and provider-generated files that violate DLP policies</li>
<li><strong>Chat messages</strong> — User prompts and provider responses that violate DLP policies</li>
<li><strong>Artifacts</strong> — Provider-generated documents and files that violate DLP policies</li>
</ul>
<h4 id="2026-05-19-casb-claude-compliance-api-learn-more">Learn more</h4>
<p>This <a href="/cloudflare-one/integrations/cloud-and-saas/anthropic/">integration</a> is available to all Cloudflare One customers. New Cloudflare customers can sign up and start with their first two integrations for free. Existing customers can enable the integration directly in the dashboard. The integration begins scanning immediately and surfaces findings in the dashboard within minutes.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-19">May 19, 2026</time><div>
<h2 id="post-2026-05-19-radar-mrt-explorer"><a href="/changelog/post/2026-05-19-radar-mrt-explorer/">MRT Explorer on Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now includes an <a href="https://radar.cloudflare.com/routing/mrt-explorer">MRT Explorer</a> tool in the Routing section. Route collectors like RIPE RIS and RouteViews publish MRT (Multi-Threaded Routing Toolkit) dump files containing BGP announcements, withdrawals, and route attributes. The new tool parses these files entirely in the browser — nothing gets uploaded.</p>
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
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/13/">Previous</a><span>Page 14 of 50</span><a class="pagination-next" rel="next" href="/changelog/15/">Next</a></nav>
</div>
