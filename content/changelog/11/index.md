---
cp9:
  canonical: https://developers.cloudflare.com/changelog/11/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 11 | Cloudflare Docs
  head_html: <title>Changelog - page 11 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/11/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 11"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/11/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/11/#page","headline":"Changelog - page 11 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/11/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/11/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-06-25">Jun 25, 2026</time><div>
<h2 id="post-2026-06-24-warp-macos-beta"><a href="/changelog/post/2026-06-24-warp-macos-beta/">Cloudflare One Client for macOS (version 2026.6.782.1)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new Beta release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This beta release introduces upgraded security of device registration to be hardware-backed. Registration tokens can now be generated in the Secure Enclave whenever available to provide stronger protection against device impersonation.</p>
<p><strong>Additional changes and improvements</strong></p>
<p>This release also introduces multiple fixes and improvements including:</p>
<ul>
<li>Improved accessibility by using high contrast colors and more defined color boundaries when high contrast is enabled in the macOS Display settings.</li>
<li>Path MTU Discovery (PMTUD) is now enabled by default.</li>
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
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-24">Jun 24, 2026</time><div>
<h2 id="post-2026-06-24-ai-search-similarity-cache-controls"><a href="/changelog/post/2026-06-24-ai-search-similarity-cache-controls/">Control AI Search similarity cache freshness</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> now gives you more control over <a href="/ai-search/configuration/retrieval/cache/">similarity cache</a> freshness. Similarity cache helps reduce latency and inference cost by reusing responses for semantically similar queries.</p>
<p>With these updates, you can choose how long responses are eligible for reuse and clear cached responses when they may be stale.</p>
<h4 id="2026-06-24-ai-search-similarity-cache-controls-cache-duration-now-defaults-to-48-hours">Cache duration now defaults to 48 hours</h4>
<p>Previously, AI Search cached responses for a fixed duration of 30 days. Cached responses now use the instance's <code>cache_ttl</code> setting, and the default is <strong>48 hours</strong>.</p>
<p>You can set <code>cache_ttl</code> when creating or updating an instance to choose a cache duration from 10 minutes to 6 days.</p>
<p>Use a shorter TTL when your source content changes frequently and freshness is more important. Use a longer TTL when your content is stable and you want more cache reuse.</p>
<p>For example, set <code>cache_ttl</code> to <code>518400</code> to retain cached responses for 6 days:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;cache_ttl&quot;: 518400&#10;}&#10;</code></pre>
<h4 id="2026-06-24-ai-search-similarity-cache-controls-purge-cached-responses">Purge cached responses</h4>
<p>You can also purge all cached responses for an instance on demand. Purging cached responses does not delete indexed content or source files.</p>
<p>It prevents AI Search from reusing previous cached responses, so subsequent similar queries generate fresh answers and repopulate the cache.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai-search/instances/$INSTANCE_NAME/purge_cache&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>You can also purge cached responses from the instance settings page in the Cloudflare dashboard.</p>
<p>Refer to <a href="/ai-search/configuration/retrieval/cache/">similarity cache</a> for the full list of supported <code>cache_ttl</code> values and more details about cache behavior.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-24">Jun 24, 2026</time><div>
<h2 id="post-2026-06-24-audit-logs-v2-organization-dashboard-ui"><a href="/changelog/post/2026-06-24-audit-logs-v2-organization-dashboard-ui/">Audit Logs v2 — Organization-level audit logs in Cloudflare dashboard</a></h2>
<div class="changelog-badges"><span>audit-logs</span></div><div class="changelog-body"><p>You can now, as an <a href="/fundamentals/organizations/">Organization</a> Super Administrator, view organization-level <a href="/fundamentals/account/account-security/audit-logs/">audit logs</a> in the Cloudflare dashboard, in addition to the existing <a href="/fundamentals/account/account-security/audit-logs/#organization-activity-logs">API access</a>.</p>
<p>Organization audit logs help you monitor activity across your organization. You can see who performed an action, what changed, when it happened, how it was performed, and whether it succeeded or failed.</p>
<p>You can filter and search logs by actor, action, result, resource, request details, and timestamp. Use these logs to troubleshoot changes, investigate unexpected access, and support security or compliance workflows.</p>
<p><img src="/assets/upstream/images/changelog/audit-logs/Audit_logs_v2_organization_dashboard.png" alt="Organization audit logs in the Cloudflare dashboard" /></p>
<p>If you are viewing account-level audit logs and the account belongs to an organization where you are an Organization Super Administrator, select <strong>View Organization Audit Logs</strong> to open the parent organization's audit logs.</p>
<p><img src="/assets/upstream/images/changelog/audit-logs/Audit_logs_v2_view_organization_button.png" alt="View Organization Audit Logs button" /></p>
<p>To get started, go to <strong>Organizations</strong>, select your organization, then go to <strong>Manage Organization</strong> &gt; <strong>Audit Logs</strong>.</p>
<p>For more information, refer to the <a href="/fundamentals/account/account-security/audit-logs/">Audit Logs documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-24">Jun 24, 2026</time><div>
<h2 id="post-2026-06-24-log-fields-updated"><a href="/changelog/post/2026-06-24-log-fields-updated/">New WebSocket Analytics Logpush dataset and updated fields</a></h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-06-24-log-fields-updated-new-datasets">New datasets</h4>
<ul>
<li><strong>WebSocket Analytics</strong>: A new dataset with fields including <code>BytesReceivedClient</code>, <code>BytesReceivedOrigin</code>, <code>BytesSentClient</code>, <code>BytesSentOrigin</code>, <code>ClientASN</code>, <code>ClientIP</code>, <code>ClientRequestHost</code>, <code>ClientRequestPath</code>, <code>ClientRequestUserAgent</code>, <code>ColoCode</code>, <code>ConnectionCloseReason</code>, <code>ConnectionCloseSource</code>, <code>ConnectionID</code>, <code>ConnectionTransportCloseCode</code>, <code>EdgeEndTimestamp</code>, <code>EdgeStartTimestamp</code>, and <code>RayID</code>.</li>
</ul>
<h4 id="2026-06-24-log-fields-updated-updated-fields-in-existing-datasets">Updated fields in existing datasets</h4>
<ul>
<li><strong>Firewall events</strong> (added): <code>ZoneName</code>. The Firewall events dataset is now also available for <a href="/logs/logpush/logpush-job/datasets/account/firewall_events/">account-scope Logpush</a>, in addition to the existing zone scope.</li>
<li><strong>Email Security Alerts</strong> (added): <code>BCC</code>, <code>DKIMResult</code>, <code>DMARCPolicy</code>, <code>DMARCResult</code>, and <code>SPFResult</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-24">Jun 24, 2026</time><div>
<h2 id="post-2026-06-24-radar-ip-page-improvements"><a href="/changelog/post/2026-06-24-radar-ip-page-improvements/">Precise IP location and richer AS details on the Cloudflare Radar IP page</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now plots your IPv4 and IPv6 locations on the <a href="https://radar.cloudflare.com/ip">IP page</a>, shows the Cloudflare data centers serving your connection, and includes more detail about the autonomous system (AS) your primary IP belongs to.</p>
<h4 id="2026-06-24-radar-ip-page-improvements-your-ip-location-on-the-map">Your IP location on the map</h4>
<p>The map of your connection now shows:</p>
<ul>
<li><strong>IP location markers</strong> — The primary IP will show as a red marker. When both IP addresses do not geolocate to the same place, a second marker will appear in blue with a note explaining why IPv4 and IPv6 can resolve to different locations.</li>
<li><strong>Cloudflare data center markers</strong> — Cloudflare data centers now show as orange dots on the map and the one you are connected to is highlighted.</li>
<li><strong>Data center connectors</strong> — Each line connects your IP markers to their respective data centers.</li>
</ul>
<p><img src="/assets/upstream/images/radar/ip-page-geolocation.png" alt="Map showing Cloudflare data centers and a marker representing the IP location with a line connected to a data center" /></p>
<p>Due to the data policies of our geolocation provider, this detailed location is only available for your own IP. Other IP addresses keep the current country-level view.</p>
<h4 id="2026-06-24-radar-ip-page-improvements-extended-as-information">Extended AS information</h4>
<p>The AS card on the IP page now shows additional detail about the network an IP belongs to — including alternate names, the operator website, and an estimate of the AS user population — alongside the AS number and country.</p>
<p>Visit the <a href="https://radar.cloudflare.com/ip">Cloudflare Radar IP page</a> to explore more details about your IP.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-23">Jun 23, 2026</time><div>
<h2 id="post-2026-06-16-rollback-options"><a href="/changelog/post/2026-06-16-rollback-options/">Workflows rollback handlers now include step context</a></h2>
<div class="changelog-badges"><span>workflows</span></div><div class="changelog-body"><p><a href="/workflows/">Workflows</a> makes it easier to build reliable multi-step applications that can recover when downstream systems fail. Rollback handlers now receive the original <a href="/workflows/build/step-context/">step context</a> via a <code>ctx</code> object for the step being rolled back. This includes <code>ctx.step.name</code>, <code>ctx.step.count</code>, <code>ctx.attempt</code>, and the step <code>config</code> with defaults applied.</p>
<p>The <a href="/workflows/build/workers-api/#workflowstepconfig">step configuration</a> includes the retry and timeout settings used for that step, so you can customize your step recovery logic according to those fields.</p>
<pre tabindex="0"><code class="language-ts">await step.do(&#10;	&quot;create charge&quot;,&#10;	async () =&gt; {&#10;		const charge = await createCharge();&#10;		return { chargeId: charge.id };&#10;	},&#10;	{&#10;		rollback: async ({ ctx, output, error }) =&gt; {&#10;			// `output` is the value returned by the step being rolled back.&#10;			const { chargeId } = output as { chargeId: string };&#10;			await refundCharge(chargeId, {&#10;				// `ctx` is the original step context, including step name, count, attempt, and config.&#10;				reason: `${ctx.step.name}: ${error.message}`,&#10;			});&#10;		},&#10;		rollbackConfig: {&#10;			// `rollbackConfig` controls retries and timeout for the rollback handler.&#10;			retries: { limit: 3, delay: &quot;30 seconds&quot;, backoff: &quot;linear&quot; },&#10;			timeout: &quot;5 minutes&quot;,&#10;		},&#10;	},&#10;);&#10;</code></pre>
<p>Refer to <a href="/workflows/build/workers-api/#rollback-options">rollback options</a> to learn more.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-23">Jun 23, 2026</time><div>
<h2 id="post-2026-06-23-regionalized-ip-bindings"><a href="/changelog/post/2026-06-23-regionalized-ip-bindings/">Regionalized IP Bindings for Regional Services</a></h2>
<div class="changelog-badges"><span>data-localization</span></div><div class="changelog-body"><p>Regional Services now supports <strong>Regionalized IP Bindings</strong>, letting you regionalize traffic at the IP layer for prefixes you bring to Cloudflare through <a href="/byoip/">Bring Your Own IP (BYOIP)</a>.</p>
<p>Where <a href="/data-localization/regional-services/regional-hostnames/">Regional Hostnames</a> regionalize traffic by hostname, Regionalized IP Bindings let you bind a CIDR from one of your prefixes to a region — ideal for address-map deployments and any service you address by IP rather than hostname. Cloudflare then terminates TLS and processes traffic to those addresses only within the data centers in that region.</p>
<p>Regionalized IP Bindings requires the Regional Services and Regional Services for BYOIP entitlements. Contact your account team to enable them.</p>
<p>To get started, refer to <a href="/data-localization/regional-services/ip-bindings/">Regionalized IP Bindings</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-23">Jun 23, 2026</time><div>
<h2 id="post-2026-06-23-amp-sxg-end-of-life"><a href="/changelog/post/2026-06-23-amp-sxg-end-of-life/">Cloudflare AMP/SXG is now end of life.</a></h2>
<div class="changelog-badges"><span>speed</span></div><div class="changelog-body"><p>Cloudflare Accelerated Mobile Pages (AMP) and Signed Exchanges (SXG) support has reached end of life. The features have been disabled since October 2025, so customers who had them configured should see no change to their traffic.</p>
<p>Customers will no longer be able to configure AMP/SXG through API or rulesets. The Zone API will start throwing errors. Rulesets with the SXG configuration will fail to save until SXG has been removed.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-23">Jun 23, 2026</time><div>
<h2 id="post-2026-06-23-waf-release"><a href="/changelog/post/2026-06-23-waf-release/">WAF Release - 2026-06-23</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This week's release introduces new managed protection to address a critical pre-authentication OS command injection vulnerability in Ivanti Sentry (CVE-2026-10520).</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-10520: An OS command injection vulnerability in Ivanti Sentry allows remote, unauthenticated attackers to execute arbitrary system commands with root privileges. The flaw stems from improper sanitization of input strings parsed during internal configuration handling.</li>
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
				<code class="nb-rule-id" title="500a90789f874345b60b0de7242fdf83">242fdf83</code>
</td>
<td>N/A</td>
<td>Ivanti Sentry - Command Injection - CVE:CVE-2026-10520</td>
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
<time datetime="2026-06-22">Jun 22, 2026</time><div>
<h2 id="post-2026-06-21-window-functions-distinct-set-operations"><a href="/changelog/post/2026-06-21-window-functions-distinct-set-operations/">R2 SQL now supports window functions, DISTINCT, and set operations</a></h2>
<div class="changelog-badges"><span>r2-sql</span></div><div class="changelog-body"><p>R2 SQL now supports window functions, <code>SELECT DISTINCT</code>, set operations, and additional aggregates, making it easier to write analytical queries without preprocessing your data elsewhere.</p>
<p><a href="/r2-sql/">R2 SQL</a> is Cloudflare's serverless, distributed SQL engine for querying <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables stored in <a href="/r2-data-catalog/">R2 Data Catalog</a>.</p>
<h4 id="2026-06-21-window-functions-distinct-set-operations-new-capabilities">New capabilities</h4>
<ul>
<li><strong>Window functions</strong> — <code>ROW_NUMBER</code>, <code>RANK</code>, <code>DENSE_RANK</code>, <code>PERCENT_RANK</code>, <code>CUME_DIST</code>, <code>NTILE</code>, <code>LAG</code>, <code>LEAD</code>, <code>FIRST_VALUE</code>, <code>LAST_VALUE</code>, <code>NTH_VALUE</code>, and aggregates with an <code>OVER (...)</code> clause, including <code>PARTITION BY</code> and explicit frames</li>
<li><strong>QUALIFY</strong> — filter rows based on a window function result</li>
<li><strong>DISTINCT</strong> — <code>SELECT DISTINCT</code>, <code>DISTINCT ON (...)</code>, and the <code>DISTINCT</code> modifier on aggregates such as <code>COUNT(DISTINCT ...)</code></li>
<li><strong>Set operations</strong> — <code>UNION</code>, <code>UNION ALL</code>, <code>INTERSECT</code>, and <code>EXCEPT</code></li>
<li><strong>Grouping extensions</strong> — <code>GROUPING SETS</code>, <code>ROLLUP</code>, and <code>CUBE</code></li>
<li><strong>Exact aggregates</strong> — <code>MEDIAN</code>, <code>PERCENTILE_CONT</code>, <code>ARRAY_AGG</code>, and <code>STRING_AGG</code></li>
</ul>
<h4 id="2026-06-21-window-functions-distinct-set-operations-examples">Examples</h4>
<h4 id="2026-06-21-window-functions-distinct-set-operations-rank-rows-with-a-window-function">Rank rows with a window function</h4>
<pre tabindex="0"><code class="language-sql">SELECT customer_id, region,&#10;       ROW_NUMBER() OVER (PARTITION BY region ORDER BY total_amount DESC) AS rank_in_region&#10;FROM my_namespace.sales_data&#10;</code></pre>
<h4 id="2026-06-21-window-functions-distinct-set-operations-filter-with-qualify">Filter with QUALIFY</h4>
<pre tabindex="0"><code class="language-sql">SELECT customer_id, region, total_amount&#10;FROM my_namespace.sales_data&#10;QUALIFY ROW_NUMBER() OVER (PARTITION BY region ORDER BY total_amount DESC) &lt;= 3&#10;</code></pre>
<h4 id="2026-06-21-window-functions-distinct-set-operations-combine-tables-with-a-set-operation">Combine tables with a set operation</h4>
<pre tabindex="0"><code class="language-sql">SELECT customer_id FROM my_namespace.sales_data&#10;EXCEPT&#10;SELECT customer_id FROM my_namespace.archived_sales&#10;</code></pre>
<p>The named <code>WINDOW</code> clause is not supported — inline the <code>OVER (...)</code> specification at each call site. For the full syntax reference, refer to the <a href="/r2-sql/sql-reference/">SQL reference</a>. For supported features and performance guidance, refer to <a href="/r2-sql/reference/limitations-best-practices/">Limitations and best practices</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-19">Jun 19, 2026</time><div>
<h2 id="post-2026-06-19-unified-routes-page"><a href="/changelog/post/2026-06-19-unified-routes-page/">Manage all your routes from one page in the dashboard</a></h2>
<div class="changelog-badges"><span>mesh</span><span>tunnel</span><span>cloudflare-wan</span><span>cloudflare-one</span></div><div class="changelog-body"><p>The <strong>Routes</strong> page in the Cloudflare dashboard now shows the routes across all of your connectors — <a href="/mesh/">Cloudflare Mesh</a> and <a href="/tunnel/">Cloudflare Tunnel</a> routes alongside <a href="/cloudflare-wan/">Cloudflare WAN</a> and <a href="/magic-transit/">Magic Transit</a> static routes — in a single table, instead of a separate routes view per product.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/2026-06-19-unified-routes.gif" alt="The unified Routes page in the Cloudflare dashboard, showing routes across connectors in a single table" /></p>
<p>From the unified Routes page you can:</p>
<ul>
<li><strong>Visualize your network with an interactive map</strong> that shows how your destinations flow through to your connectors — including equal-cost multi-path (ECMP) routes where the same prefix is served by several connectors. Select a node to filter the table down to the routes behind it.</li>
<li><strong>See every route in one table</strong>, with its destination, type, connector, priority, and source, and filter or sort to find what you need.</li>
<li><strong>Create, edit, and delete routes</strong> of any supported type without leaving the page. When adding a Cloudflare WAN or Magic Transit static route, you now pick the next hop by <strong>connector name</strong> instead of typing its IP.</li>
<li><strong>Manage <a href="/cloudflare-one/networks/virtual-networks/">virtual networks</a></strong> from a dedicated tab.</li>
<li><strong>Test a route</strong> to see which connector and next hop a destination resolves to before you commit a change.</li>
</ul>
<p>To find it, go to <strong>Networking</strong> &gt; <strong>Routes</strong> in the dashboard sidebar.</p>
<div class="nb-dash-button"></div>
<p>Your existing routes, APIs, and configurations are unchanged — this is a dashboard experience that brings them together in one place. Learn how to <a href="/cloudflare-one/networks/routes/add-routes/">add routes</a> and <a href="/cloudflare-one/networks/virtual-networks/">manage virtual networks</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-19">Jun 19, 2026</time><div>
<h2 id="post-2026-06-19-apac-ne-apac-se-location-hints"><a href="/changelog/post/2026-06-19-apac-ne-apac-se-location-hints/">New Asia-Pacific location hints: apac-ne and apac-se</a></h2>
<div class="changelog-badges"><span>durable-objects</span><span>workers</span></div><div class="changelog-body"><p>Durable Objects now supports two new location hints for Asia-Pacific: <code>apac-ne</code> (Northeast Asia-Pacific) and <code>apac-se</code> (Southeast Asia-Pacific). Use <code>apac-ne</code> or <code>apac-se</code> when you want finer-grained placement within Asia-Pacific rather than the broader <code>apac</code> hint.</p>
<p>Use the new hints the same way as any other <code>locationHint</code>:</p>
<pre tabindex="0"><code class="language-js">// Northeast Asia-Pacific (Japan, Korea, etc.)&#10;const stubNE = env.MY_DURABLE_OBJECT.get(id, { locationHint: &quot;apac-ne&quot; });&#10;&#10;// Southeast Asia-Pacific (Singapore, Indonesia, etc.)&#10;const stubSE = env.MY_DURABLE_OBJECT.get(id, { locationHint: &quot;apac-se&quot; });&#10;</code></pre>
<p>If your users are spread across all of Asia-Pacific, the existing <code>apac</code> hint remains the right choice. Only reach for <code>apac-ne</code> or <code>apac-se</code> when your traffic is clearly concentrated in one sub-region and you want to minimize round-trip time to that audience. The default behavior and what we generally recommended is not adding a location hint unless absolutely needed, this will create the Durable Object as close to the initializing request as possible to reduce latency.</p>
<p>As with all location hints, these are best-effort suggestions. Cloudflare will place the Durable Object in a nearby data center, not necessarily the exact hinted location.</p>
<p>For the full list of supported hints, refer to <a href="/durable-objects/reference/data-location/#provide-a-location-hint">Data location — Provide a location hint</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-19">Jun 19, 2026</time><div>
<h2 id="post-2026-06-19-outbound-connections-keep-dos-alive"><a href="/changelog/post/2026-06-19-outbound-connections-keep-dos-alive/">Outbound connections keep Durable Objects alive</a></h2>
<div class="changelog-badges"><span>durable-objects</span></div><div class="changelog-body"><p>Durable Objects now remain alive for the duration of active outbound connections created via <a href="/workers/runtime-apis/tcp-sockets/"><code>connect()</code></a> or an outbound WebSocket. Previously, a Durable Object would be evicted after 70-140 seconds of no incoming traffic, even if the object had an open outbound connection, which is a common pattern when streaming responses from a large language model (LLM) over TCP or an outbound WebSocket.</p>
<p>With this change, each active outbound connection prevents eviction. Once all outbound connections close, the standard 70-140 second inactivity window applies before the Durable Object is evicted.</p>
<h4 id="2026-06-19-outbound-connections-keep-dos-alive-before-streaming-connections-were-cut-off-by-eviction">Before: streaming connections were cut off by eviction</h4>
<p><img src="/assets/upstream/images/durable-objects/outbound-connection-before.svg" alt="Timeline showing a Durable Object evicted 70-140 seconds after the last incoming request, cutting off an in-flight LLM stream while the outbound connection is still open" /></p>
<h4 id="2026-06-19-outbound-connections-keep-dos-alive-after-active-outbound-connections-keep-the-durable-object-alive">After: active outbound connections keep the Durable Object alive</h4>
<p><img src="/assets/upstream/images/durable-objects/outbound-connection-after.svg" alt="Timeline showing the same outbound stream completing because the active connection keeps the Durable Object alive, with the inactivity window starting only after the connection closes" /></p>
<p>If you are <a href="/agents/">building agents on Cloudflare</a>, this is especially relevant. An agent that streams tokens from an LLM while <a href="/agents/concepts/calling-llms/">calling models</a>, or that performs <a href="/agents/concepts/agentic-patterns/long-running-agents/">long-running tasks</a> over an outbound connection, now stays alive for the duration of that connection instead of being evicted mid-stream.</p>
<p><strong>Limits:</strong></p>
<ul>
<li>Each outbound connection keeps the Durable Object alive for a maximum of <strong>15 minutes</strong>. After 15 minutes, the connection stops preventing eviction (the connection itself continues operating), and the <a href="/durable-objects/concepts/durable-object-lifecycle/">standard eviction rules</a> resume.</li>
<li>The Durable Object's existing <a href="/durable-objects/platform/limits/">per-account instance limits</a> still apply.</li>
</ul>
<p>For more information, refer to <a href="/durable-objects/concepts/durable-object-lifecycle/">Lifecycle of a Durable Object</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-19">Jun 19, 2026</time><div>
<h2 id="post-2026-06-19-temporary-accounts-for-agents"><a href="/changelog/post/2026-06-19-temporary-accounts-for-agents/">Temporary accounts for AI agent deployments</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>AI agents can now deploy Workers to Cloudflare without first requiring a user to sign up, open a browser-based OAuth flow, click through the dashboard, or create an API token. When an agent tries to deploy without Cloudflare credentials, Wrangler can tell it to rerun with <code>--temporary</code>, then deploy the Worker to a temporary preview account.</p>
<p>To try this with your agent, update to Wrangler 4.102.0 or later, make sure you are logged out (<code>wrangler logout</code>), and then ask your agent to build something and deploy it to Cloudflare. The agent should follow Wrangler's output and deploy using the <code>--temporary</code> flag.</p>
<p><img src="/assets/upstream/images/workers/claim-deployments-flow.png" alt="Diagram showing an AI agent deploying, verifying, and redeploying a Worker to a temporary account, then claiming it after authentication and moving it to a permanent account" /></p>
<pre tabindex="0"><code class="language-sh">wrangler deploy --temporary&#10;</code></pre>
<p>The temporary deployment stays live for 60 minutes. During that window, the agent can verify the Worker, redeploy changes, and return both the live Worker URL and claim URL. Opening the claim URL lets you sign in to or create a Cloudflare account and make the temporary account permanent.</p>
<p>Temporary preview accounts currently support a limited set of products, including Workers, Workers Static Assets, Workers KV, D1, Durable Objects, Hyperdrive, Queues, and SSL/TLS certificates. For supported products, limits, and claim behavior, refer to <a href="/workers/platform/claim-deployments/">Claim deployments (temporary accounts)</a>.</p>
<p>For more context, refer to <a href="https://blog.cloudflare.com/temporary-accounts/">Temporary Cloudflare Accounts for Agents</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-18">Jun 18, 2026</time><div>
<h2 id="post-2026-06-18-cloudflare-idp-default"><a href="/changelog/post/2026-06-18-cloudflare-idp-default/">Cloudflare identity provider is now the default for new accounts</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span><span>access</span></div><div class="changelog-body"><p>When you create a new Zero Trust organization, Cloudflare now adds the <a href="/cloudflare-one/integrations/identity-providers/cloudflare/">Cloudflare identity provider</a> as your default login method. Previously, new organizations started with <a href="/cloudflare-one/integrations/identity-providers/one-time-pin/">one-time PIN (OTP)</a>.</p>
<p>With the Cloudflare identity provider, your users authenticate using their existing Cloudflare account credentials, and authentication is restricted to members of your account. You can still add OTP or connect any <a href="/cloudflare-one/integrations/identity-providers/">third-party identity provider</a> whenever you need to.</p>
<p>This change only applies to newly created accounts. Existing organizations keep the login methods they already have configured. If you would like to use the Cloudflare Identity Provider in an existing account, you must enable it.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-18">Jun 18, 2026</time><div>
<h2 id="post-2026-06-18-container-exec"><a href="/changelog/post/2026-06-18-container-exec/">exec() is now available for Containers</a></h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p><code>exec()</code> is now available for <a href="/containers/">Containers</a>. Use <code>this.ctx.container.exec()</code> to start processes inside a running Container, stream standard input and output, inspect exit codes, and signal each process.</p>
<p>Call <code>exec()</code> from a class extending <code>Container</code>, or from another Durable Object through <code>this.ctx.container</code>. The associated Container must already be running.</p>
<p>This example starts the Container when needed, then reads its Node.js version:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17713.md")</div>
<p>The command array starts an executable directly, without an implicit shell. Invoke a shell explicitly for pipes, redirects, or variable expansion.</p>
<p>One RPC method can coordinate multiple <code>exec()</code> calls in one caller-to-Durable Object round trip. It can also pass byte-oriented <code>ReadableStream</code> input or return streamed output with flow control.</p>
<p>For options and streaming examples, refer to <a href="/containers/guides/execute-commands/">Execute commands</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-18">Jun 18, 2026</time><div>
<h2 id="post-2026-06-18-planetscale-databases-cloudflare-billing"><a href="/changelog/post/2026-06-18-planetscale-databases-cloudflare-billing/">Create PlanetScale Postgres and MySQL databases, billed to your Cloudflare account</a></h2>
<div class="changelog-badges"><span>hyperdrive</span><span>workers</span></div><div class="changelog-body"><p>You can create PlanetScale Postgres and MySQL databases from Cloudflare and bill PlanetScale database usage through your Cloudflare account as a pay-as-you-go customer. Cloudflare contract customers will be able to add PlanetScale usage to their contract in July so reach out to your Cloudflare account team if interested.</p>
<p>Create a PlanetScale database from the Cloudflare dashboard to check out globally distributed Workers optimized for regional data access.</p>
<div class="nb-dash-button"></div>
<p><img src="/assets/upstream/images/hyperdrive/planetscale-request-flow.svg" alt="Request flow from a user to Workers, Hyperdrive caches, connection pools, and PlanetScale." /></p>
<p>PlanetScale databases created from Cloudflare work with <a href="/workers/">Workers</a> through <a href="/hyperdrive/">Hyperdrive</a>. Hyperdrive manages database connection pools and query caching, so you can use PlanetScale as a centralized relational database for Workers applications without changing your database drivers, object-relational mapping (ORM) libraries, or SQL tooling.</p>
<p>PlanetScale usage appears on your Cloudflare invoice each billing period as a dollar total at PlanetScale's standard <a href="https://planetscale.com/pricing">pricing</a>. You can introspect per-database billing usage via PlanetScale's <a href="https://planetscale.com/docs/billing#organization-usage-and-billing-page">dashboard</a>.</p>
<p>When you create a PlanetScale database from the Cloudflare dashboard, you receive the same PlanetScale developer experience, including development branches, query insights, and Model Context Protocol (MCP) server support for agents.</p>
<p>To get started, refer to <a href="/hyperdrive/planetscale/">PlanetScale Postgres and MySQL with Hyperdrive</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-18">Jun 18, 2026</time><div>
<h2 id="post-2026-06-18-radar-workers-ai-inference-metric"><a href="/changelog/post/2026-06-18-radar-workers-ai-inference-metric/">Updated Workers AI popularity metric in Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> has changed how it measures <a href="/workers-ai/">Workers AI</a> model and task popularity.</p>
<p>Previously, popularity was based on the number of unique accounts running inferences against each model or task. It is now based on the <strong>number of inferences</strong>, giving a more representative view of actual usage volume. This change will affect all new measurements as well as historical data. As a result, the model and task distributions shown on Radar may differ from what you saw previously, and historical trends may shift accordingly.</p>
<p>The <a href="https://radar.cloudflare.com/ai-insights#workers-ai-model-popularity">Workers AI model popularity</a> chart shows the distribution of inferences across models.</p>
<p><img src="/assets/upstream/images/radar/workers-ai-model-popularity.png" alt="Screenshot of the Workers AI model popularity chart on the AI Insights page" /></p>
<p>The <a href="https://radar.cloudflare.com/ai-insights#workers-ai-task-popularity">Workers AI task popularity</a> chart shows the distribution of inferences across tasks.</p>
<p><img src="/assets/upstream/images/radar/workers-ai-task-popularity.png" alt="Screenshot of the Workers AI task popularity chart on the AI Insights page" /></p>
<p>The same data is available via the following API endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/ai/subresources/inference/methods/summary_v2/"><code>/ai/inference/summary/{dimension}</code></a></li>
<li><a href="/api/resources/radar/subresources/ai/subresources/inference/methods/timeseries_groups_v2/"><code>/ai/inference/timeseries_groups/{dimension}</code></a></li>
</ul>
<p>Explore the data on the <a href="https://radar.cloudflare.com/ai-insights">AI Insights page</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-18">Jun 18, 2026</time><div>
<h2 id="post-2026-06-18-cloudflare-fonts-error-handling-security"><a href="/changelog/post/2026-06-18-cloudflare-fonts-error-handling-security/">Cloudflare Fonts error handling and security improvements</a></h2>
<div class="changelog-badges"><span>speed</span></div><div class="changelog-body"><p>Cloudflare Fonts now forwards <code>/cf-fonts</code> requests to your origin server when it encounters invalid paths or unexpected runtime errors, instead of returning 4xx or 5xx responses directly. This update also adds additional input validation to enhance security.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-17">Jun 17, 2026</time><div>
<h2 id="post-2026-06-17-dashboard-management"><a href="/changelog/post/2026-06-17-dashboard-management/">Manage Artifacts from the Cloudflare dashboard</a></h2>
<div class="changelog-badges"><span>artifacts</span></div><div class="changelog-body"><p>You can now configure <a href="/artifacts/concepts/how-artifacts-works/">Artifacts</a> namespaces, repos, and tokens directly from the Cloudflare dashboard.</p>
<p>Artifacts is Git-compatible storage that lets you store repos on Cloudflare and interact with them using standard Git workflows.</p>
<p>You can view and create <a href="/artifacts/concepts/namespaces/#use-namespaces-as-containers">namespaces</a>, which are top-level containers for repos:</p>
<p><img src="/assets/upstream/images/changelog/artifacts/dashboard-namespaces.png" alt="Artifacts namespaces dashboard showing namespace search and create namespace controls" /></p>
<p>You can view, create, fork, and search repos within a namespace:</p>
<p><img src="/assets/upstream/images/changelog/artifacts/dashboard-repositories.png" alt="Artifacts repositories dashboard showing repo source, access, and created columns" /></p>
<p>You can open a repo to view its files and copy its Git remote URL.</p>
<p><img src="/assets/upstream/images/changelog/artifacts/dashboard-repo-overview.png" alt="Artifacts repository overview showing files, commits, token management, and quick actions" /></p>
<p>You can also provision tokens directly from the dashboard to scope Git access to a single repo, with read tokens for clone, fetch, and pull workflows, or write tokens when a client needs to push changes.</p>
<p>To get started, go to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and select <strong>Storage &amp; databases</strong> &gt; <strong>Artifacts</strong>.</p>
<p>If you are enrolled in the Artifacts beta, you can use the dashboard to set up Artifacts. If you would like to join the beta, complete the <a href="https://forms.gle/DwBoPRa3CWQ8ajFp7">request form</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-17">Jun 17, 2026</time><div>
<h2 id="post-2026-06-17-pqc-mldsa-aop-cots"><a href="/changelog/post/2026-06-17-pqc-mldsa-aop-cots/">Post-quantum ML-DSA certificates for Authenticated Origin Pulls and Custom Origin Trust Store</a></h2>
<div class="changelog-badges"><span>ssl</span></div><div class="changelog-body"><p>Cloudflare now accepts <a href="https://csrc.nist.gov/pubs/fips/204/final">ML-DSA</a> (FIPS 204) post-quantum certificates on the connection between Cloudflare's edge and your origin server. Combined with our existing <a href="/ssl/post-quantum-cryptography/#hybrid-key-agreement">X25519MLKEM768</a> key agreement, this lets you establish end-to-end post-quantum authentication on the Cloudflare-to-origin connection.</p>
<p>ML-DSA is supported in two origin-facing features:</p>
<ul>
<li><a href="/ssl/origin-configuration/authenticated-origin-pull/">Authenticated Origin Pulls</a> (AOP) — upload an ML-DSA client certificate that Cloudflare will present during the mTLS handshake to your origin. Available at both zone-level and per-hostname scopes.</li>
<li><a href="/ssl/origin-configuration/custom-origin-trust-store/">Custom Origin Trust Store</a> (COTS) — upload an ML-DSA certificate authority that Cloudflare will trust when validating your origin server certificate under <a href="/ssl/origin-configuration/ssl-modes/full-strict/">Full (strict) encryption mode</a>.</li>
</ul>
<p>Refer to <a href="/ssl/post-quantum-cryptography/pqc-to-origin/#post-quantum-signatures">Post-quantum signatures</a> for certificate generation and setup guidance, and to <a href="/ssl/post-quantum-cryptography/pqc-cloudflare-products/">PQC in Cloudflare products</a> for the current post-quantum deployment status across Cloudflare.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-16">Jun 16, 2026</time><div>
<h2 id="post-2026-06-16-agents-sdk-v0.16.1"><a href="/changelog/post/2026-06-16-agents-sdk-v0.16.1/">Agents SDK improves browser automation, code execution, and recovery</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> makes it easier to build agents that can safely interact with real systems and keep working through interruptions.</p>
<p>Agents can now browse websites through Browser Run, write code against external tools through Code Mode, use client-provided tools when delegating to Think sub-agents, and recover more reliably from deploys, Durable Object evictions, and connection churn.</p>
<h4 id="2026-06-16-agents-sdk-v0.16.1-safer-browser-automation">Safer browser automation</h4>
<p>Agents can now use <a href="/browser-run/">Browser Run</a> through a single durable <code>browser_execute</code> tool. Instead of choosing from a fixed list of actions, the model writes code against the Chrome DevTools Protocol (CDP) and can inspect pages, capture screenshots, read rendered content, debug frontend behavior, and interact with live browser sessions.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17671.md")</div>
<p>Browser sessions can be one-time, reused, or promoted from one-time to persistent during a run. This is useful when an agent needs a human to log in, complete MFA, or approve a sensitive action. The run can pause, keep the same tabs and cookies, and resume after approval.</p>
<p>The browser tools also add Live View URLs, optional session recording, and quick actions such as <code>browser_markdown</code>, <code>browser_extract</code>, <code>browser_links</code>, and <code>browser_scrape</code> for one-shot browsing tasks.</p>
<h4 id="2026-06-16-agents-sdk-v0.16.1-resumable-code-execution-with-approvals">Resumable code execution with approvals</h4>
<p>Code Mode now uses <code>createCodemodeRuntime</code>, connectors, and a durable execution log. This lets you give a model one <code>codemode</code> tool instead of a large prompt full of tool definitions. The model can discover the capabilities it needs, write code against typed globals, and reuse saved snippets.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17672.md")</div>
<p>When the code reaches an approval-gated action, the runtime pauses execution and returns a pending approval. After approval, completed calls replay from the durable log, the approved action runs, and the same code continues. This makes it practical to build agents that create issues, update external systems, or perform other side effects without custom pause-and-resume logic for every tool.</p>
<h4 id="2026-06-16-agents-sdk-v0.16.1-better-think-delegation">Better Think delegation</h4>
<p>Think sub-agents can now use client-defined tools over the RPC <code>chat()</code> path. A parent agent can pass tool schemas with <code>clientTools</code> and resolve tool calls through <code>onClientToolCall</code>. This lets delegated agents use caller-provided capabilities without requiring a browser WebSocket.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17673.md")</div>
<p>Think Workflows also improve <code>step.prompt()</code>. A prompt step now runs a full agentic turn before returning structured output, so the agent can call tools before producing the typed result. This makes Workflow steps more useful for durable triage, research, and approval flows.</p>
<p>The unified Think execute tool can also include <code>cdp.*</code> browser capabilities alongside <code>state.*</code> and <code>tools.*</code> when Browser Run is bound.</p>
<h4 id="2026-06-16-agents-sdk-v0.16.1-voice-output-device-selection">Voice output device selection</h4>
<p>Voice clients can route assistant audio to a specific output device. Use <code>outputDeviceId</code> with <code>useVoiceAgent</code>, or call <code>client.setOutputDevice()</code> from the framework-agnostic client.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17674.md")</div>
<p>Browsers without speaker-selection support continue playing through the default output device and report a non-fatal <code>outputDeviceError</code>.</p>
<h4 id="2026-06-16-agents-sdk-v0.16.1-reliability-fixes">Reliability fixes</h4>
<p>This release includes several fixes for production agents:</p>
<ul>
<li><code>useAgent</code> and <code>AgentClient</code> handle WebSocket replacement more reliably during reconnects and configuration changes.</li>
<li>Chat stream replay is more reliable after reconnects, deploys, and provider errors.</li>
<li>Fiber recovery continues across multi-pass scans and backs off when recovery hooks keep failing.</li>
<li>Agent teardown continues even when the request that started teardown is canceled.</li>
<li>Large session histories use byte-budgeted reads to reduce memory pressure during startup.</li>
</ul>
<h4 id="2026-06-16-agents-sdk-v0.16.1-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Refer to the <a href="/agents/tools/codemode/">Code Mode documentation</a>, <a href="/agents/tools/browser/">Browser tools documentation</a>, <a href="/agents/harnesses/think/tools/">Think tools documentation</a>, and <a href="/agents/communication-channels/voice/">Voice documentation</a> for more information.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-16">Jun 16, 2026</time><div>
<h2 id="post-2026-06-16-pay-per-crawl-advanced-configuration"><a href="/changelog/post/2026-06-16-pay-per-crawl-advanced-configuration/">Pay Per Crawl advanced configuration</a></h2>
<div class="changelog-badges"><span>ai-crawl-control</span></div><div class="changelog-body"><p>You can now configure advanced Pay Per Crawl settings for your zone, including:</p>
<ul>
<li><strong>Disable Pay Per Crawl by URI pattern</strong> using <a href="/rules/configuration-rules/">Configuration Rules</a> to offer free access to specific pages while charging for others.</li>
<li><strong>Dynamic pricing</strong> by having your origin return a <code>crawler-price</code> response header, or by using a <a href="/workers/">Cloudflare Worker</a> to set prices based on request properties.</li>
</ul>
<p>When dynamic pricing is enabled, Pay Per Crawl adds a <code>cf-pay-per-crawl</code> request header to origin requests so your origin or Worker can determine the appropriate price.</p>
<p>Refer to the <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/advanced-configuration/">Advanced configuration documentation</a> for details.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-16">Jun 16, 2026</time><div>
<h2 id="post-2026-06-16-new-optimization-features"><a href="/changelog/post/2026-06-16-new-optimization-features/">New optimization features in Images</a></h2>
<div class="changelog-badges"><span>images</span></div><div class="changelog-body"><p>These updates introduce new features for optimizing and manipulating with Images:</p>
<ul>
<li><strong>New <code>composite</code> option:</strong> Control how <a href="/images/optimization/draw-overlays/#composite">overlays are blended</a> with the base image.</li>
<li><strong>Percentage widths:</strong> Set the dimensions of an overlay as <a href="/images/optimization/draw-overlays/#width-and-height">a fraction of the dimensions</a> of the base image.</li>
<li><strong>New <code>fit</code> modes:</strong> Use <a href="/images/optimization/features/#aspect-crop"><code>aspect-crop</code></a> to always preserve the target aspect ratio or <a href="/images/optimization/features/#scale-up"><code>scale-up</code></a> to always enlarge images.</li>
<li><strong>New <code>upscale</code> parameter:</strong> Apply <a href="/images/optimization/features/#upscale">AI upscaling</a> to produce sharper, more detailed results when enlarging images.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-06-16">Jun 16, 2026</time><div>
<h2 id="post-2026-06-16-custom-spans"><a href="/changelog/post/2026-06-16-custom-spans/">Workers tracing now supports custom spans</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now create custom trace spans in your Workers code using <code>tracing.enterSpan()</code>. Custom spans appear alongside the automatic platform instrumentation (fetch calls, KV reads, D1 queries, and other platform operations) in your traces and OpenTelemetry exports, with correct parent-child nesting.</p>
<p>The API is available via <code>import { tracing } from &quot;cloudflare:workers&quot;</code> or through the handler context as <code>ctx.tracing</code>:</p>
<pre tabindex="0"><code class="language-ts">import { tracing } from &quot;cloudflare:workers&quot;;&#10;&#10;export default {&#10;  async fetch(request, env, ctx) {&#10;    return tracing.enterSpan(&quot;handleRequest&quot;, async (span) =&gt; {&#10;      span.setAttribute(&quot;url.path&quot;, new URL(request.url).pathname);&#10;      const data = await env.MY_KV.get(&quot;key&quot;);&#10;      return new Response(data);&#10;    });&#10;  },&#10;};&#10;</code></pre>
<p>Spans nest automatically based on the JavaScript async context, and are auto-ended when the callback returns or its returned promise settles. The <code>Span</code> object provides <code>setAttribute(key, value)</code> for attaching metadata and an <code>isTraced</code> property to check whether the current request is being sampled.</p>
<p><img src="/assets/upstream/images/workers-observability/wobs_custom_spans_screenshot.png" alt="Trace waterfall showing custom spans nested alongside automatic KV and fetch instrumentation" /></p>
<p><a href="/workers/observability/traces/#how-to-enable-tracing">Tracing must be enabled</a> in your Wrangler configuration for spans to be recorded.</p>
<p>For full API details and examples, refer to <a href="/workers/observability/traces/custom-spans/">Custom spans</a>.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/10/">Previous</a><span>Page 11 of 50</span><a class="pagination-next" rel="next" href="/changelog/12/">Next</a></nav>
</div>
