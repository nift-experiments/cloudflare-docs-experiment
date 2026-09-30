<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-05-18">May 18, 2026</time><div>
<h2 id="post-2026-05-18-wrangler-support"><a href="/changelog/post/2026-05-18-wrangler-support/">Manage Artifacts namespaces and repos with Wrangler CLI</a></h2>
<div class="changelog-badges"><span>artifacts</span></div><div class="changelog-body"><p>You can now manage <a href="/artifacts/">Artifacts</a> namespaces, repos, and repo-scoped tokens directly from Wrangler CLI.</p>
<p>Available commands:</p>
<ul>
<li><code>wrangler artifacts namespaces list</code> — List Artifacts namespaces in your account.</li>
<li><code>wrangler artifacts namespaces get</code> — Get metadata for a namespace.</li>
<li><code>wrangler artifacts repos create</code> — Create a repo in a namespace.</li>
<li><code>wrangler artifacts repos list</code> — List repos in a namespace.</li>
<li><code>wrangler artifacts repos get</code> — Get metadata for a repo.</li>
<li><code>wrangler artifacts repos delete</code> — Delete a repo.</li>
<li><code>wrangler artifacts repos issue-token</code> — Issue a repo-scoped token for Git access.</li>
</ul>
<p>To get started, refer to the <a href="/workers/wrangler/commands/artifacts/">Wrangler Artifacts commands documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-18">May 18, 2026</time><div>
<h2 id="post-2026-05-18-unified-routing-network-analytics"><a href="/changelog/post/2026-05-18-unified-routing-network-analytics/">Network Analytics support for Unified Routing</a></h2>
<div class="changelog-badges"><span>cloudflare-wan</span><span>magic-transit</span></div><div class="changelog-body"><p><a href="/analytics/network-analytics/">Network Analytics</a> is now fully supported for accounts using <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing</a> mode. Traffic that traverses Unified Routing onramps and offramps is now visible in Network Analytics with the same dimensions and filters as traffic on the standard data plane.</p>
<p>This closes a parity gap for customers who had moved tunnels onto Unified Routing and lost visibility into their dataplane traffic in the Network Analytics dashboard. No configuration change is required — analytics data is collected automatically for all accounts with Unified Routing enabled.</p>
<p>For the remaining beta limitations, refer to <a href="/cloudflare-wan/reference/traffic-steering/#beta-limitations">Traffic steering beta limitations</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-18">May 18, 2026</time><div>
<h2 id="post-2026-05-18-local-dev-tunnels"><a href="/changelog/post/2026-05-18-local-dev-tunnels/">Share local dev servers through Cloudflare Tunnel in Wrangler and Vite</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now share local dev sessions through <a href="/tunnel/">Cloudflare Tunnel</a> and get a public URL when using either <a href="/workers/wrangler/">Wrangler</a> or the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>. This is useful when you need to share a preview, test a webhook, or access your app from another device.</p>
<p><img src="/assets/upstream/images/changelog/workers/vite-local-dev-tunnel.gif" alt="Vite local dev tunnel demo" /></p>
<p>This lets you either:</p>
<ul>
<li>start a temporary <a href="/tunnel/get-started/#quick-tunnels-development">Quick tunnel</a> with a random <code>*.trycloudflare.com</code> hostname, or</li>
<li>use an existing <a href="/tunnel/get-started/#create-a-tunnel">named tunnel</a> for a stable hostname and to restrict access with <a href="/cloudflare-one/access-controls/">Cloudflare Access</a>.</li>
</ul>
<p>To start a tunnel, press <code>t</code> in Wrangler or <code>t + Enter</code> in Vite while your dev server is running. For details on setting up a named tunnel, refer to <a href="/workers/local-development/local-dev-tunnels/">Share a local dev server</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-15">May 15, 2026</time><div>
<h2 id="post-2026-05-15-hyperdrive-pool-size-metrics"><a href="/changelog/post/2026-05-15-hyperdrive-pool-size-metrics/">Hyperdrive exposes database connection pool size metrics</a></h2>
<div class="changelog-badges"><span>hyperdrive</span><span>workers</span></div><div class="changelog-body"><p>You can now view the size of your Hyperdrive database connection pools, giving you the ability to self-diagnose connection issues. Using the Cloudflare dashboard or the <code>hyperdrivePoolSizesAdaptiveGroups</code> dataset in the <a href="/analytics/graphql-api/getting-started/">GraphQL Analytics API</a>, you can see <code>waitingClients</code>, <code>currentPoolSize</code>, <code>availablePoolSlots</code>, and <code>maxPoolSize</code> for each of your configurations.</p>
<p>A new <strong>Pool connections</strong> chart has been added to the <strong>Metrics</strong> tab of each Hyperdrive configuration in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>. You can use the location selector to drill down into specific locations hosting your connection pool by airport code.</p>
<p><img src="/assets/upstream/images/hyperdrive/changelog/hyperdrive-pool-size-metrics-chart.png" alt="Hyperdrive pool size metrics chart" /></p>
<p>The chart shows:</p>
<ul>
<li><strong>Waiting clients</strong>: Client requests waiting for an available connection.</li>
<li><strong>Open connections</strong>: Active connections to your database.</li>
<li><strong>Pool size maximum</strong>: Your configured origin connection limit.</li>
</ul>
<p>Connection contention appears as a spike in waiting clients, or when open connections consistently approach the pool size maximum. If your open connections regularly approach this limit, consider contacting Cloudflare to <a href="/hyperdrive/platform/limits/#request-a-limit-increase">increase your Hyperdrive connection limit</a>.</p>
<h4 id="2026-05-15-hyperdrive-pool-size-metrics-pool-size-metrics">Pool size metrics</h4>
<p>The <code>hyperdrivePoolSizesAdaptiveGroups</code> dataset in the <a href="/analytics/graphql-api/getting-started/">GraphQL Analytics API</a> exposes the following key connection pool metrics for each Hyperdrive configuration:</p>
<p>Under <code>avg</code>:</p>
<ul>
<li><strong><code>currentPoolSize</code></strong> — Average number of connections currently open in the pool.</li>
<li><strong><code>availablePoolSlots</code></strong> — Average number of pool connections available for checkout.</li>
<li><strong><code>waitingClients</code></strong> — Average number of clients waiting for a connection from the pool.</li>
</ul>
<p>Under <code>max</code>:</p>
<ul>
<li><strong><code>maxPoolSize</code></strong> — Configured maximum size of the connection pool.</li>
<li><strong><code>currentPoolSize</code></strong> — Peak number of connections open in the pool.</li>
<li><strong><code>waitingClients</code></strong> — Peak number of clients waiting for a connection from the pool.</li>
</ul>
<p>For more information, refer to <a href="/hyperdrive/observability/metrics/">Metrics and analytics</a> and <a href="/hyperdrive/concepts/connection-pooling/">Connection pooling</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-15">May 15, 2026</time><div>
<h2 id="post-2026-05-14-joins-subqueries-multi-table-queries"><a href="/changelog/post/2026-05-14-joins-subqueries-multi-table-queries/">R2 SQL now supports JOINs, subqueries, and multi-table queries</a></h2>
<div class="changelog-badges"><span>r2-sql</span></div><div class="changelog-body"><p><a href="/r2-sql/">R2 SQL</a> is Cloudflare's serverless, distributed SQL engine for querying <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables stored in <a href="/r2-data-catalog/">R2 Data Catalog</a>. R2 SQL runs directly on Cloudflare's global network with no infrastructure to manage, so you can analyze data in R2 without exporting it to an external warehouse.</p>
<p>R2 SQL now supports joining multiple Iceberg tables in a single query. You can combine tables with JOINs, filter with subqueries, and define multi-table CTEs to build complex analytical queries.</p>
<h4 id="2026-05-14-joins-subqueries-multi-table-queries-new-capabilities">New capabilities</h4>
<ul>
<li><strong>JOINs</strong> — <code>INNER JOIN</code>, <code>LEFT JOIN</code>, <code>RIGHT JOIN</code>, <code>FULL OUTER JOIN</code>, <code>CROSS JOIN</code>, and implicit joins (comma-separated <code>FROM</code> with conditions in <code>WHERE</code>)</li>
<li><strong>Subqueries</strong> — <code>IN</code> / <code>NOT IN</code>, <code>EXISTS</code> / <code>NOT EXISTS</code>, scalar subqueries in <code>SELECT</code> / <code>WHERE</code> / <code>HAVING</code>, and derived tables (subqueries in <code>FROM</code>)</li>
<li><strong>Multi-table CTEs</strong> — <code>WITH</code> clauses can reference different tables and include JOINs</li>
<li><strong>Self-joins</strong> — join a table with itself using different aliases</li>
<li><strong>Multi-way joins</strong> — join three or more tables in a single query</li>
</ul>
<h4 id="2026-05-14-joins-subqueries-multi-table-queries-examples">Examples</h4>
<h4 id="2026-05-14-joins-subqueries-multi-table-queries-two-table-join-with-aggregation">Two-table JOIN with aggregation</h4>
<pre><code class="language-sql">SELECT z.domain, z.plan, COUNT(*) AS request_count&#10;FROM my_namespace.zones z&#10;INNER JOIN my_namespace.http_requests h ON z.zone_id = h.zone_id&#10;WHERE z.plan = &#x27;enterprise&#x27;&#10;GROUP BY z.domain, z.plan&#10;ORDER BY request_count DESC&#10;LIMIT 20&#10;</code></pre>
<h4 id="2026-05-14-joins-subqueries-multi-table-queries-exists-subquery"><code>EXISTS</code> subquery</h4>
<pre><code class="language-sql">SELECT z.domain, z.plan&#10;FROM my_namespace.zones z&#10;WHERE EXISTS (&#10;    SELECT 1 FROM my_namespace.firewall_events f&#10;    WHERE f.zone_id = z.zone_id AND f.action = &#x27;block&#x27;&#10;)&#10;ORDER BY z.domain&#10;LIMIT 20&#10;</code></pre>
<h4 id="2026-05-14-joins-subqueries-multi-table-queries-multi-table-cte-with-join">Multi-table CTE with JOIN</h4>
<pre><code class="language-sql">WITH top_zones AS (&#10;    SELECT zone_id, COUNT(*) AS req_count&#10;    FROM my_namespace.http_requests&#10;    GROUP BY zone_id&#10;    ORDER BY req_count DESC&#10;    LIMIT 50&#10;),&#10;zone_threats AS (&#10;    SELECT zone_id, COUNT(*) AS threat_count&#10;    FROM my_namespace.firewall_events&#10;    WHERE risk_score &gt; 0.5&#10;    GROUP BY zone_id&#10;)&#10;SELECT tz.zone_id, tz.req_count, COALESCE(zt.threat_count, 0) AS threat_count&#10;FROM top_zones tz&#10;LEFT JOIN zone_threats zt ON tz.zone_id = zt.zone_id&#10;ORDER BY tz.req_count DESC&#10;LIMIT 20&#10;</code></pre>
<p>For the full syntax reference, refer to the <a href="/r2-sql/sql-reference/">SQL reference</a>. For performance guidance with joins, refer to <a href="/r2-sql/reference/limitations-best-practices/">Limitations and best practices</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-15">May 15, 2026</time><div>
<h2 id="post-2026-05-15-emergency-waf-release"><a href="/changelog/post/2026-05-15-emergency-waf-release/">WAF Release - 2026-05-15 - Emergency</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This emergency release introduces two new rules to detect nginx heap buffer overflow and heap spray exploitation attempts targeting the rewrite module's <code>is_args</code> stale-state bug (CVE-2026-42945).</p>
<p><strong>Key Findings</strong></p>
<p>CVE-2026-42945: nginx Heap Buffer Overflow via Stale <code>is_args</code> in Rewrite Module</p>
<p>Successful exploitation allows remote attackers to trigger a heap buffer overflow in nginx's rewrite module by sending crafted URIs containing escapable characters. A length/copy pass mismatch in <code>ngx_http_script_copy_capture_code()</code> causes the copy pass to write escaped data into an undersized buffer, leading to heap corruption. This enables denial of service (worker process crash) and, with heap feng shui techniques, potential remote code execution.</p>
<p>We strongly recommend upgrading to nginx 1.30.1 (or later) immediately to address the underlying vulnerability. If you cannot upgrade immediately, avoid <code>rewrite</code> directives with <code>?</code> in the replacement string followed by <code>set</code> or <code>if</code> referencing capture groups.</p>
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
				<code class="nb-rule-id" title="2013e3e58efe4b79a26e214f7e52be73">7e52be73</code>
</td>
<td>N/A</td>
<td>nginx - Remote Code Execution - Buffer Overread - CVE:CVE-2026-42945</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="68226e83a4d14ee9a9c878469df0ee6c">9df0ee6c</code>
</td>
<td>N/A</td>
<td>nginx - Remote Code Execution - Heap Spray - CVE:CVE-2026-42945</td>
<td>N/A</td>
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
<time datetime="2026-05-14">May 14, 2026</time><div>
<h2 id="post-2026-05-14-domains-tab"><a href="/changelog/post/2026-05-14-domains-tab/">New Domains tab in the Workers dashboard</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>In your Worker's dashboard, there is now a dedicated <strong>Domains</strong> tab where you can purchase a new domain through Cloudflare Registrar and have it automatically connected, add an <a href="/workers/configuration/routing/custom-domains/">existing domain</a>, and manage all of your Worker's routing in one place.</p>
<p><img src="/assets/upstream/images/workers/changelog/domains-tab.png" alt="The new Domains tab in the Workers dashboard" /></p>
<p>You can also enable or disable your <a href="/workers/configuration/routing/workers-dev/"><code>workers.dev</code> subdomain</a> and <a href="/workers/versions-and-deployments/preview-urls/">Preview URLs</a>, put them behind <a href="/cloudflare-one/access-controls/">Cloudflare Access</a> to require sign-in, and jump directly to <a href="/analytics/">analytics</a> or domain overview for any connected domain.</p>
<p>To get started, go to <strong>Workers &amp; Pages</strong>, select a Worker, and open the <strong>Domains</strong> tab.</p>
<div class="nb-dash-button"></div>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-13">May 13, 2026</time><div>
<h2 id="post-2026-05-13-agents-sdk-v0.12.4"><a href="/changelog/post/2026-05-13-agents-sdk-v0.12.4/">Agents SDK v0.12.4: chat recovery, routing retries, durable Think submissions, and Voice connection control</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> brings more reliable chat recovery, fixes Agent state synchronization during reconnects, adds durable submissions for Think, exposes routing retry configuration, and adds connection control for Voice agents.</p>
<h4 id="2026-05-13-agents-sdk-v0.12.4-chat-recovery-improvements">Chat recovery improvements</h4>
<p><code>@cloudflare/ai-chat</code> now keeps server turns running when a browser or client stream is interrupted. This is useful for long-running AI responses where users refresh the page, close a tab, or temporarily lose connection. Calling <code>stop()</code> still cancels the server turn.</p>
<p>Set <code>cancelOnClientAbort: true</code> if browser or client aborts should also cancel the server turn:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17661.md")</div>
<p>Notable bug fixes:</p>
<ul>
<li>Chat stream resume negotiation no longer throws when replay races with a closed WebSocket connection.</li>
<li>Recovered chat continuations no longer leave <code>useAgentChat</code> stuck in a streaming state when the original socket disconnects before a terminal response.</li>
<li>Approval auto-continuation preserves reasoning parts and persists continuation reasoning in the final message.</li>
<li><code>isServerStreaming</code> now resets correctly when a resumed stream moves from the fallback observer path to a transport-owned stream.</li>
</ul>
<h4 id="2026-05-13-agents-sdk-v0.12.4-agent-state-and-routing-fixes">Agent state and routing fixes</h4>
<p><code>agents@0.12.4</code> prevents duplicate initial state frames during WebSocket connection setup. This avoids stale initial state messages overwriting state updates already sent by the client.</p>
<p>Agent recovery is also more reliable when tool calls span a Durable Object restart. Recovery now defers user finish hooks until after agent startup and isolates hook failures, so one failed hook does not block other recovered runs from finalizing.</p>
<p><code>getAgentByName()</code> now supports <code>routingRetry</code> for transient Durable Object routing failures:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17662.md")</div>
<h4 id="2026-05-13-agents-sdk-v0.12.4-durable-think-submissions">Durable Think submissions</h4>
<p><code>@cloudflare/think</code> now supports durable programmatic submissions. <code>submitMessages()</code> provides durable acceptance, idempotent retries, status inspection, cancellation, and cleanup for server-driven turns that should continue after the caller returns.</p>
<p><code>Think.chat()</code> RPC turns now run inside chat recovery fibers and persist their stream chunks. Interrupted sub-agent turns can recover partial output instead of starting over.</p>
<p><code>ChatOptions.tools</code> has been removed from the TypeScript API. Define durable tools on the child agent or use agent tools for orchestration. Runtime <code>options.tools</code> values passed by legacy callers are ignored with a warning.</p>
<h4 id="2026-05-13-agents-sdk-v0.12.4-think-message-pruning-behavior-change">Think message pruning behavior change</h4>
<p><code>@cloudflare/think</code> no longer applies <code>pruneMessages({ toolCalls: &quot;before-last-2-messages&quot; })</code> to model context by default. The previous default could strip client-side tool results from longer multi-turn flows.</p>
<p><code>truncateOlderMessages</code> still runs as before, so context cost remains bounded. Subclasses that relied on the old aggressive pruning can opt back in from <code>beforeTurn</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17663.md")</div>
<h4 id="2026-05-13-agents-sdk-v0.12.4-voice-agent-connection-control">Voice agent connection control</h4>
<p><code>@cloudflare/voice</code> adds an <code>enabled</code> option to <code>useVoiceAgent</code>. React apps can now delay creating and connecting a <code>VoiceClient</code> until prerequisites such as capability tokens are ready.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17664.md")</div>
<p>This release also fixes Workers AI speech-to-text session edge cases and <code>withVoice</code> text streaming from AI SDK <code>textStream</code> responses.</p>
<h4 id="2026-05-13-agents-sdk-v0.12.4-other-improvements">Other improvements</h4>
<ul>
<li><strong>Streamable HTTP routing</strong> — Server-to-client requests now route through the originating POST stream when no standalone SSE stream is available.</li>
<li><strong>Structured tool output</strong> — Tool output shapes are preserved when truncating older messages or oversized persisted rows.</li>
<li><strong>Non-chat Think tool steps</strong> — Think agent-tool children can complete without emitting assistant text and can return structured output through <code>getAgentToolOutput</code>.</li>
<li><strong>Sub-agent schedules</strong> — Stale sub-agent schedule rows are pruned when their owning facet registry entry no longer exists.</li>
<li><strong><code>@cloudflare/codemode</code></strong> — Adds a browser-safe export with an iframe sandbox executor and resolves OpenAPI specs inside the sandbox to avoid Worker Loader RPC size limits.</li>
</ul>
<h4 id="2026-05-13-agents-sdk-v0.12.4-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest @cloudflare/think@latest @cloudflare/voice@latest&#10;</code></pre>
<p>Refer to the <a href="/agents/runtime/">Agents API reference</a> and <a href="/agents/communication-channels/chat/chat-agents/">Chat agents documentation</a> for more information.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-13">May 13, 2026</time><div>
<h2 id="post-2026-05-13-log-fields-updated"><a href="/changelog/post/2026-05-13-log-fields-updated/">New Logpush datasets and updated fields across multiple Logpush datasets in Cloudflare Logs</a></h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>Cloudflare has updated <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>:</p>
<h4 id="2026-05-13-log-fields-updated-new-datasets">New datasets</h4>
<ul>
<li><strong>Email Security Post-Delivery Events</strong>: A new dataset with fields including <code>AlertID</code>, <code>CompletedAt</code>, <code>Destination</code>, <code>FinalDisposition</code>, <code>Folder</code>, <code>From</code>, <code>FromName</code>, <code>MessageID</code>, <code>MessageTimestamp</code>, <code>MicrosoftTenantID</code>, <code>Operation</code>, <code>PostfixID</code>, <code>Reasons</code>, <code>Recipient</code>, <code>RequestedAt</code>, <code>RequestedBy</code>, <code>RequestedDisposition</code>, <code>Status</code>, <code>Subject</code>, <code>Success</code>, and <code>To</code>.</li>
<li><strong>Magic Network Monitoring Flow Logs</strong>: A new dataset with fields including <code>AWSVPCFlowJSON</code>, <code>Bits</code>, <code>DestinationAS</code>, <code>DestinationAddress</code>, <code>DestinationPort</code>, <code>DeviceID</code>, <code>EgressBits</code>, <code>EgressPackets</code>, <code>Ethertype</code>, <code>FlowProtocol</code>, <code>FlowTimestamp</code>, <code>NumFlows</code>, <code>PacketID</code>, <code>Packets</code>, <code>Protocol</code>, <code>RuleIDs</code>, <code>SampleRate</code>, <code>SampleRateType</code>, <code>SamplerAddress</code>, <code>SourceAS</code>, <code>SourceAddress</code>, <code>SourcePort</code>, <code>TcpFlags</code>, and <code>Timestamp</code>.</li>
</ul>
<h4 id="2026-05-13-log-fields-updated-updated-fields-in-existing-datasets">Updated fields in existing datasets</h4>
<ul>
<li><strong>Firewall events</strong> (added): <code>AISecurityInjectionScore</code>, <code>AISecurityPIICategories</code>, <code>AISecurityTokenCount</code>, and <code>AISecurityUnsafeTopicCategories</code>.</li>
<li><strong>HTTP requests</strong> (added): <code>AISecurityInjectionScore</code>, <code>AISecurityPIICategories</code>, <code>AISecurityTokenCount</code>, <code>AISecurityUnsafeTopicCategories</code>, and <code>Subrequests</code>.</li>
</ul>
<p>For the complete field definitions for each dataset, refer to <a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-13">May 13, 2026</time><div>
<h2 id="post-2026-05-13-rum-405-method-not-allowed"><a href="/changelog/post/2026-05-13-rum-405-method-not-allowed/">/cdn-cgi/rum endpoint now returns 405 for non-POST requests</a></h2>
<div class="changelog-badges"><span>web-analytics</span></div><div class="changelog-body"><p>The <code>/cdn-cgi/rum</code> beacon endpoint now returns <code>405 Method Not Allowed</code> for non-POST requests instead of <code>404 Not Found</code>. The response includes an <code>Allow: POST, OPTIONS</code> header per <a href="https://www.rfc-editor.org/rfc/rfc9110#section-15.5.6">RFC 9110 §15.5.6</a>.</p>
<p>Previously, sending a <code>GET</code> or other non-POST request to this endpoint returned a <code>404</code>, which was misleading because it suggested the endpoint did not exist. The new <code>405</code> response clearly indicates that the endpoint exists but only accepts <code>POST</code> requests.</p>
<p>The Web Analytics beacon (<code>beacon.min.js</code>) already uses <code>POST</code> for all metric submissions, so this change does not affect normal beacon operation. <code>OPTIONS</code> requests for CORS preflight continue to work as before.</p>
<p>For more information, refer to the <a href="/web-analytics/faq/#why-am-i-getting-a-405-method-not-allowed-error-from-cdn-cgirum">Web Analytics FAQ</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-12">May 12, 2026</time><div>
<h2 id="post-2026-05-12-access-login-page-refresh"><a href="/changelog/post/2026-05-12-access-login-page-refresh/">Refreshed Access login page</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span><span>access</span></div><div class="changelog-body"><p>The <a href="/cloudflare-one/reusable-components/custom-pages/access-login-page/">Access login page</a> and <a href="/cloudflare-one/integrations/identity-providers/one-time-pin/">one-time password (OTP)</a> page now feature a refreshed design that improves visual consistency, user trust, and mobile responsiveness.</p>
<p><strong>Before:</strong></p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/access-login-old.png" alt="Screenshot of the previous Access login page" /></p>
<p><strong>After:</strong></p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/access-login-new.png" alt="Screenshot of the updated Access login page" /></p>
<p>The updated login experience includes:</p>
<ul>
<li><strong>Unified authentication card</strong> - All sign-in options (identity provider buttons, email input, OTP) now appear in a single card with consistent styling, replacing the previous multi-section layout.</li>
<li><strong>Consistent button styling</strong> - Identity provider buttons use a uniform size and layout for easier scanning and selection.</li>
<li><strong>Better mobile experience</strong> - Responsive layout improvements ensure the login page renders correctly on phones and tablets.</li>
<li><strong>Dark mode support</strong> - The login page now supports dark mode.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-12">May 12, 2026</time><div>
<h2 id="post-2026-05-12-single-anycast-ip-default"><a href="/changelog/post/2026-05-12-single-anycast-ip-default/">New accounts assigned a single IPv4 anycast address</a></h2>
<div class="changelog-badges"><span>cloudflare-wan</span><span>magic-transit</span><span>cloudflare-one</span></div><div class="changelog-body"><p>New Magic Transit and Cloudflare WAN accounts are now assigned a single IPv4 anycast address by default.</p>
<p>Cloudflare handles failures on its network automatically by advertising your endpoint IP from multiple nodes across many globally distributed data centers. To handle failures on your network, configure two tunnels from separate routers.</p>
<p>To request additional anycast IP addresses for your account, contact your account team.</p>
<p>For tunnel configuration guidance, refer to <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">Configure tunnel endpoints</a> for Cloudflare WAN or <a href="/magic-transit/how-to/configure-tunnel-endpoints/">Configure tunnel endpoints</a> for Magic Transit.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-12">May 12, 2026</time><div>
<h2 id="post-2026-05-12-ssh-enabled-by-default"><a href="/changelog/post/2026-05-12-ssh-enabled-by-default/">SSH through Wrangler is now enabled by default for Containers</a></h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>SSH through Wrangler is now enabled by default for <a href="/containers/">Containers</a>. Previously, you had to set <code>ssh.enabled</code> to <code>true</code> in your Container configuration before you could connect.</p>
<p>This change does not expose any publicly accessible ports on your Container. The SSH service is reachable only through <a href="/workers/wrangler/commands/containers/#containers-ssh"><code>wrangler containers ssh</code></a>, which authenticates against your Cloudflare account. You also need to add an <code>ssh-ed25519</code> public key to <code>authorized_keys</code> before anyone can connect, so enabling SSH alone does not grant access.</p>
<p>To connect, add a public key to your Container configuration and run <code>wrangler containers ssh &lt;INSTANCE_ID&gt;</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17711.md")</div>
<p>To disable SSH, set <code>ssh.enabled</code> to <code>false</code> in your Container configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17712.md")</div>
<p>For more information, refer to the <a href="/containers/guides/ssh/">SSH documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-12">May 12, 2026</time><div>
<h2 id="post-2026-05-12-natural-language-policy-creation"><a href="/changelog/post/2026-05-12-natural-language-policy-creation/">Create Gateway firewall policies with natural language</a></h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>Cloudflare Gateway now supports natural language policy creation for <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS</a>, <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP</a>, and <a href="/cloudflare-one/traffic-policies/network-policies/">Network</a> firewall policies. Administrators can describe the outcome they want in plain language, and Cloudflare will generate a complete policy rule that populates the policy builder form.</p>
<p><img src="/assets/upstream/images/changelog/gateway/gateway-create-with-ai.png" alt="Create with AI button on the Gateway firewall policies page" /></p>
<p>To create a policy with natural language, select <strong>Create with AI</strong> on any Gateway firewall policy tab. Choose a policy type, describe what the policy should do, and a fully configured rule will appear in the policy builder for review. You can edit any field before saving, or re-generate with a different prompt.</p>
<p>The generated policy incorporates your account context - including lists, DLP profiles, applications, and device posture checks - so that references to your existing resources resolve automatically.</p>
<p>A built-in feedback mechanism allows you to rate each generated policy and provide optional comments, which Cloudflare uses to improve output quality over time.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/">Gateway firewall policies</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-12">May 12, 2026</time><div>
<h2 id="post-2026-05-12-r2-data-catalog-graphql-analytics"><a href="/changelog/post/2026-05-12-r2-data-catalog-graphql-analytics/">R2 Data Catalog now exposes metrics via the GraphQL Analytics API</a></h2>
<div class="changelog-badges"><span>r2</span><span>r2-data-catalog</span></div><div class="changelog-body"><p><a href="/r2-data-catalog/">R2 Data Catalog</a> is a managed Apache Iceberg data catalog built directly into your R2 bucket that allows you to connect query engines like <a href="/r2-sql/">R2 SQL</a>, Spark, Snowflake, and DuckDB to your data in R2.</p>
<p>You can now query analytics for your R2 Data Catalog warehouses via Cloudflare's <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. Two new datasets are available:</p>
<ul>
<li><strong><code>r2CatalogDataOperationsAdaptiveGroups</code></strong> tracks Iceberg REST API requests made to your catalog, including operation type, request duration, HTTP status, and request body bytes. Use this to monitor request volume and latency across warehouses, namespaces, and tables.</li>
<li><strong><code>r2CatalogTableMaintenanceAdaptiveGroups</code></strong> tracks table maintenance jobs such as compaction and snapshot expiration. Use this to monitor job success rates, files processed, bytes read and written, and job duration.</li>
</ul>
<p>Both datasets support filtering by warehouse name, namespace, table name, and time range. They also include percentile aggregations for duration metrics.</p>
<p>For detailed schema information and example queries, refer to the <a href="/r2-data-catalog/observability/metrics/">R2 Data Catalog metrics and analytics documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-12">May 12, 2026</time><div>
<h2 id="post-2026-05-12-URL-scanner-report-agent-readiness"><a href="/changelog/post/2026-05-12-URL-scanner-report-agent-readiness/">Agent Readiness scores now available in URL Scanner via the Cloudflare Dashboard</a></h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p>We’ve added a new <strong>Agent Readiness</strong> tab to URL Scanner reports accessible via the Cloudflare dashboard. This feature evaluates your site against emerging AI standards and provides six specialized scores to help you optimize for the next generation of AI agents and automated discovery.</p>
<p>The Internet is shifting from a human-read web to a machine-read web. AI agents now browse, interact with, and even perform transactions on websites. If a site isn't &quot;agent-ready,&quot; these bots may consume excessive bandwidth, fail to find critical information, or be unable to navigate your services efficiently.</p>
<p>This update provides material value by breaking down readiness into six actionable categories:</p>
<ul>
<li><strong>Basic Web Presence</strong></li>
<li><strong>Discoverability</strong></li>
<li><strong>Content Accessibility</strong></li>
<li><strong>Bot Access Control</strong></li>
<li><strong>Protocol Discovery</strong></li>
<li><strong>Commerce</strong></li>
</ul>
<h4 id="2026-05-12-URL-scanner-report-agent-readiness-accessing-the-report">Accessing the report</h4>
<p>You can view these scores for any scanned URL directly in the dashboard or via our API.</p>
<ul>
<li><strong>Dashboard:</strong> Go to <strong>Protect &amp; Connect &gt; Application Security &gt; Investigate</strong>. After running a scan, select the <strong>Agent Readiness</strong> tab in the report.</li>
<li><strong>API:</strong> Use the <a href="https://developers.cloudflare.com/radar/investigate/url-scanner/">URL Scanner API</a> to programmatically retrieve these scores for your infrastructure.</li>
</ul>
<p>To learn more about the methodology behind these scores, refer to the <a href="https://blog.cloudflare.com/agent-readiness/">blogpost</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-12">May 12, 2026</time><div>
<h2 id="post-2026-05-11-warp-linux-ga"><a href="/changelog/post/2026-05-11-warp-linux-ga/">Cloudflare One Client for Linux (version 2026.4.1350.0)</a></h2>
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
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
<li>Split tunnel list configuration is not available in the new UI. Management of split tunnel entries is currently only possible via <code>warp-cli tunnel ip</code> and <code>warp-cli tunnel host</code>. UI support will be added in a future release.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-12">May 12, 2026</time><div>
<h2 id="post-2026-05-11-warp-macos-ga"><a href="/changelog/post/2026-05-11-warp-macos-ga/">Cloudflare One Client for macOS (version 2026.4.1350.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces the new Cloudflare One Client UI for macOS! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:</p>
<ul>
<li>Right click context menu to access the most common client actions quickly</li>
<li>Built-in captive portal login experience</li>
</ul>
<p><strong>Additional Changes and improvements</strong></p>
<ul>
<li>Added a new CLI command: warp-cli mdm refresh. This command executes an immediate refresh of the Mobile Device Management (MDM) configuration file.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>Registration may hang at &quot;Checking your organization configuration&quot; due to IPC errors. A system reboot should resolve the error, allowing registration to proceed.</li>
<li>Split tunnel list configuration is not available in the new UI. Management of split tunnel entries is currently only possible via <code>warp-cli tunnel ip</code> and <code>warp-cli tunnel host</code>. UI support will be added in a future release.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-12">May 12, 2026</time><div>
<h2 id="post-2026-05-11-warp-windows-ga"><a href="/changelog/post/2026-05-11-warp-windows-ga/">Cloudflare One Client for Windows (version 2026.4.1350.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This release introduces the new Cloudflare One Client UI for Windows! You can expect a cleaner and more intuitive design as well as easier access to common actions and information. Here are some of the many things we have found our users appreciate:</p>
<ul>
<li>Right click context menu to access the most common client actions quickly</li>
<li>Built-in captive portal login experience</li>
</ul>
<p><strong>Additional Changes and improvements</strong></p>
<ul>
<li>Added a new CLI command: warp-cli mdm refresh. This command executes an immediate refresh of the Mobile Device Management (MDM) configuration file.</li>
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
<time datetime="2026-05-11">May 11, 2026</time><div>
<h2 id="post-2026-05-11-nat-t-port-500"><a href="/changelog/post/2026-05-11-nat-t-port-500/">NAT-T support for IKE on UDP port 500</a></h2>
<div class="changelog-badges"><span>cloudflare-wan</span><span>magic-transit</span></div><div class="changelog-body"><p>Cloudflare IPsec now supports the standard NAT traversal (NAT-T) flow, where IKE begins on UDP port <code>500</code> and switches to UDP port <code>4500</code> after NAT is detected.</p>
<p>Previously, devices behind NAT had to be configured to initiate IKE on UDP port <code>4500</code> directly. Devices that started on UDP port <code>500</code> could not complete the IKE handshake when NAT was in the path. This required custom configuration on devices such as VeloCloud SD-WAN edges, Cisco IOS-XE routers, and Juniper SRX firewalls, and was not possible on every platform.</p>
<p>What changed:</p>
<ul>
<li>Devices behind NAT can now initiate IKE on either UDP port <code>500</code> or UDP port <code>4500</code>.</li>
<li>Devices that start IKE on UDP port <code>500</code> and switch to UDP port <code>4500</code> after NAT detection now complete the handshake successfully.</li>
<li>No configuration change is required on Cloudflare. The change is available for all IPsec tunnels on Cloudflare WAN and Magic Transit.</li>
</ul>
<p>This change does not affect existing tunnels:</p>
<ul>
<li>Tunnels using UDP port <code>500</code> with no NAT detected continue to operate as before.</li>
<li>Tunnels configured to start IKE on UDP port <code>4500</code> continue to operate as before.</li>
<li>NAT detection logic is unchanged.</li>
</ul>
<p>For configuration details, refer to <a href="/cloudflare-wan/reference/gre-ipsec-tunnels/">GRE and IPsec tunnels</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-11">May 11, 2026</time><div>
<h2 id="post-2026-05-11-waf-release"><a href="/changelog/post/2026-05-11-waf-release/">WAF Release - 2026-05-11</a></h2>
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
				<code class="nb-rule-id" title="23ac4a9e53f94467ba470c9468b3c389">68b3c389</code>
</td>
<td>N/A</td>
<td>Remote Code Execution - Java Deserialization - Body - Beta</td>
<td>Block</td>
<td>Disabled</td>
<td>
				This is a new detection. This rule is merged into the original rule
				"Remote Code Execution - Java Deserialization" (ID:{" "}
				<code class="nb-rule-id" title="36b0532eb3c941449afed2d3744305c4">744305c4</code>).
</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-08">May 8, 2026</time><div>
<h2 id="post-2026-05-08-planned-model-deprecations"><a href="/changelog/post/2026-05-08-planned-model-deprecations/">Planned model deprecations on Workers AI</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>We are refreshing the Workers AI model catalog to make room for newer releases. Please update your apps to remove references to the models listed below before the deprecation date.</p>
<h4 id="2026-05-08-planned-model-deprecations-recommended-replacements">Recommended replacements</h4>
<ul>
<li><a href="/workers-ai/models/glm-4.7-flash/"><code>@cf/zai-org/glm-4.7-flash</code></a> — fast multilingual model with multi-turn tool calling and coding capabilities.</li>
<li><a href="/workers-ai/models/gemma-4-26b-a4b-it/"><code>@cf/google/gemma-4-26b-a4b-it</code></a> — efficient open model with vision and tool calling.</li>
<li><a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a> — capable tool-calling and vision model for agentic workloads and coding.</li>
</ul>
<p>For pricing, refer to the <a href="/workers-ai/platform/pricing/">Workers AI pricing page</a>.</p>
<h4 id="2026-05-08-planned-model-deprecations-kimi-k2-5">Kimi K2.5</h4>
<p>We originally stated Kimi K2.5 would be deprecated on May 10, 2026, however we have extended the deprecation date to May 30, 2026. Requests will be automatically aliased to Kimi K2.6 on May 30, 2026, which has a higher price. Please review the <a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a> pricing and model capabilities prior to May 30, 2026 to ensure that the model suits your needs.</p>
<h4 id="2026-05-08-planned-model-deprecations-models-deprecated-on-may-30-2026">Models deprecated on May 30, 2026</h4>
<ul>
<li><code>@cf/moonshotai/kimi-k2.5</code> --&gt; <code>@cf/moonshotai/kimi-k2.6</code></li>
<li><code>@hf/meta-llama/meta-llama-3-8b-instruct</code></li>
<li><code>@cf/meta/llama-3-8b-instruct</code></li>
<li><code>@cf/meta/llama-3-8b-instruct-awq</code></li>
<li><code>@cf/meta/llama-3.1-8b-instruct</code></li>
<li><code>@cf/meta/llama-3.1-8b-instruct-awq</code></li>
<li><code>@cf/meta/llama-3.1-70b-instruct</code></li>
<li><code>@cf/meta/llama-2-7b-chat-int8</code></li>
<li><code>@cf/meta/llama-2-7b-chat-fp16</code></li>
<li><code>@cf/mistral/mistral-7b-instruct-v0.1</code></li>
<li><code>@hf/mistral/mistral-7b-instruct-v0.2</code></li>
<li><code>@hf/google/gemma-7b-it</code></li>
<li><code>@cf/google/gemma-3-12b-it</code></li>
<li><code>@hf/nousresearch/hermes-2-pro-mistral-7b</code></li>
<li><code>@cf/microsoft/phi-2</code></li>
<li><code>@cf/defog/sqlcoder-7b-2</code></li>
<li><code>@cf/unum/uform-gen2-qwen-500m</code></li>
<li><code>@cf/facebook/bart-large-cnn</code></li>
</ul>
<h4 id="2026-05-08-planned-model-deprecations-variants-that-remain-active">Variants that remain active</h4>
<p>The <code>-fast</code> and <code>-lora</code> variants of models will remain active, including:</p>
<ul>
<li><code>@cf/meta/llama-3.3-70b-instruct-fp8-fast</code></li>
<li><code>@cf/meta/llama-3.1-8b-instruct-fast</code></li>
<li><code>@cf/google/gemma-7b-it-lora</code></li>
<li><code>@cf/google/gemma-2b-it-lora</code></li>
<li><code>@cf/mistral/mistral-7b-instruct-v0.2-lora</code></li>
<li><code>@cf/meta-llama/llama-2-7b-chat-hf-lora</code></li>
</ul>
<p>LoRA models may be deprecated in the future. We will be adding more LoRA capabilities to the catalog, and will communicate when new LoRA models come online to give users time to train new LoRAs before we deprecate old ones.</p>
<p>For the full list of available models, refer to the <a href="/workers-ai/models/">Workers AI model catalog</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-07">May 7, 2026</time><div>
<h2 id="post-2026-05-06-react-nextjs-vulnerabilities"><a href="/changelog/post/2026-05-06-react-nextjs-vulnerabilities/">WAF and framework adapter mitigations for React and Next.js vulnerabilities</a></h2>
<div class="changelog-badges"><span>workers</span><span>waf</span></div><div class="changelog-body"><p>Multiple security vulnerabilities were disclosed by the React team and Vercel affecting React Server Components and Next.js. These include denial of service, middleware and proxy bypass, server-side request forgery, cross-site scripting, and cache poisoning issues across a range of severity levels.</p>
<p><strong>We strongly recommend updating your application and its dependencies immediately.</strong> Patched versions are available for React (<code>react-server-dom-webpack</code>, <code>react-server-dom-parcel</code>, and <code>react-server-dom-turbopack</code> <code>19.0.6</code>, <code>19.1.7</code>, and <code>19.2.6</code>) and Next.js (<code>15.5.16</code> and <code>16.2.5</code>).</p>
<h4 id="2026-05-06-react-nextjs-vulnerabilities-waf-protections">WAF protections</h4>
<p>Cloudflare WAF rules deployed in response to prior React Server Component CVEs (<a href="https://github.com/facebook/react/security/advisories/GHSA-2m3v-v2m8-q956"><code>CVE-2025-55184</code></a> and <a href="https://github.com/facebook/react/security/advisories/GHSA-83fc-fqcc-2hmg"><code>CVE-2026-23864</code></a>) already provide coverage for the newly disclosed denial-of-service vulnerabilities. These rules are enabled by default with a Block action for all customers using the Cloudflare Managed Ruleset, including Free plan customers using the Free Managed Ruleset.</p>
<table>
<thead>
<tr>
<th>Ruleset</th>
<th>Rule description</th>
<th>Rule ID</th>
<th>Default action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>React - DoS - <a href="https://github.com/facebook/react/security/advisories/GHSA-2m3v-v2m8-q956"><code>CVE-2025-55184</code></a></td>
<td><code>2694f1610c0b471393b21aef102ec699</code></td>
<td>Block</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>React - DoS - <a href="https://github.com/facebook/react/security/advisories/GHSA-83fc-fqcc-2hmg"><code>CVE-2026-23864</code></a></td>
<td><code>aaede80b4d414dc89c443cea61680354</code></td>
<td>Block</td>
</tr>
</tbody>
</table>
<p>The existing rules detect the underlying attack patterns generically. As a result, they apply to the new <a href="https://github.com/facebook/react/security/advisories/GHSA-rv78-f8rc-xrxh"><code>CVE-2026-23870</code></a> denial-of-service vulnerability in Server Components and the corresponding Next.js advisory <a href="https://github.com/vercel/next.js/security/advisories/GHSA-8h8q-6873-q5fj"><code>GHSA-8h8q-6873-q5fj</code></a>.</p>
<p>Cloudflare is investigating whether WAF rules can be safely and effectively deployed for three of the high-severity advisories: <a href="https://github.com/facebook/react/security/advisories/GHSA-rv78-f8rc-xrxh"><code>CVE-2026-23870</code></a> / <a href="https://github.com/vercel/next.js/security/advisories/GHSA-8h8q-6873-q5fj"><code>GHSA-8h8q-6873-q5fj</code></a>, <a href="https://github.com/vercel/next.js/security/advisories/GHSA-267c-6grr-h53f"><code>GHSA-267c-6grr-h53f</code></a>, and <a href="https://github.com/vercel/next.js/security/advisories/GHSA-mg66-mrh9-m8jx"><code>GHSA-mg66-mrh9-m8jx</code></a>. If it is possible to create a managed WAF rule that mitigates these CVEs and does not potentially break application behavior, Cloudflare will add additional managed WAF rules. These rules will be announced through the <a href="/waf/change-log/changelog/">WAF changelog</a>. Because these vulnerabilities were shared with Cloudflare with minimal advance notice, we are still investigating what WAF mitigations are possible.</p>
<p>Several of the disclosed vulnerabilities are not possible to block in WAF. We strongly recommend updating your applications so they are not purely reliant on WAF mitigations.</p>
<p>Customers on Pro, Business, or Enterprise plans should ensure that <a href="/waf/get-started/#1-deploy-the-cloudflare-managed-ruleset">Managed Rules are enabled</a>.</p>
<h4 id="2026-05-06-react-nextjs-vulnerabilities-next-js-adapters">Next.js adapters</h4>
<p><strong>Vinext:</strong> <a href="https://github.com/cloudflare/vinext">Vinext</a> is a Vite plugin that reimplements the Next.js API surface. Vinext's latest release is not vulnerable to any of the disclosed CVEs. Vinext's architecture differs from stock Next.js in ways that sidestep the affected code paths. For example, it does not implement the PPR resume protocol, does not expose Pages Router data-route endpoints, and strips internal headers such as <code>x-nextjs-data</code> at request boundaries. As an extra layer of defense, we added a React <code>19.2.6</code> or later requirement when running <code>vinext init</code> (<a href="https://github.com/cloudflare/vinext/pull/1118">PR #1118</a>, <a href="https://github.com/cloudflare/vinext/pull/1112">PR #1112</a>) to prevent accidentally running a vulnerable version of React with Vinext.</p>
<p><strong>OpenNext on Cloudflare:</strong> OpenNext is an adapter that lets you deploy Next.js apps to the Cloudflare Workers platform. OpenNext itself is not directly vulnerable to the React denial-of-service CVE, but users must update the Next.js version in their application. The OpenNext team has updated the adapter to further harden against these vectors and released a new version of the Cloudflare adapter. Test fixtures and examples have been updated to use patched versions (<a href="https://github.com/opennextjs/opennextjs-cloudflare/pull/1255">PR #1255</a>).</p>
<h4 id="2026-05-06-react-nextjs-vulnerabilities-summary-of-disclosed-vulnerabilities">Summary of disclosed vulnerabilities</h4>
<table>
<thead>
<tr>
<th>Advisory</th>
<th>Severity</th>
<th>Issue</th>
<th>WAF status</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/facebook/react/security/advisories/GHSA-rv78-f8rc-xrxh"><code>CVE-2026-23870</code></a> / <a href="https://github.com/vercel/next.js/security/advisories/GHSA-8h8q-6873-q5fj"><code>GHSA-8h8q-6873-q5fj</code></a></td>
<td>High</td>
<td>Denial of service in Server Components</td>
<td><strong>WAF rules in place:</strong> <code>2694f1610c0b471393b21aef102ec699</code>, <code>aaede80b4d414dc89c443cea61680354</code><br/>Cloudflare is investigating additional managed WAF coverage</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-267c-6grr-h53f"><code>GHSA-267c-6grr-h53f</code></a></td>
<td>High</td>
<td>Middleware bypass via segment-prefetch routes</td>
<td>Cloudflare is investigating if this can be safely and effectively mitigated by a managed WAF rule</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-mg66-mrh9-m8jx"><code>GHSA-mg66-mrh9-m8jx</code></a></td>
<td>High</td>
<td>Denial of service via connection exhaustion in Cache Components</td>
<td>Cloudflare is investigating if this can be safely and effectively mitigated by a managed WAF rule</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-492v-c6pp-mqqv"><code>GHSA-492v-c6pp-mqqv</code></a></td>
<td>High</td>
<td>Middleware bypass via dynamic route parameter injection</td>
<td>Not possible to safely enable a managed WAF rule without potentially breaking application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-c4j6-fc7j-m34r"><code>GHSA-c4j6-fc7j-m34r</code></a></td>
<td>High</td>
<td>SSRF via WebSocket upgrades</td>
<td>Not possible to safely enable a managed WAF rule without potentially breaking application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-36qx-fr4f-26g5"><code>GHSA-36qx-fr4f-26g5</code></a></td>
<td>High</td>
<td>Middleware bypass in Pages Router i18n</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-ffhc-5mcf-pf4q"><code>GHSA-ffhc-5mcf-pf4q</code></a></td>
<td>Moderate</td>
<td>XSS via CSP nonces</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-gx5p-jg67-6x7h"><code>GHSA-gx5p-jg67-6x7h</code></a></td>
<td>Moderate</td>
<td>XSS in <code>beforeInteractive</code> scripts</td>
<td>Not possible to safely enable a managed WAF rule without potentially breaking application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-h64f-5h5j-jqjh"><code>GHSA-h64f-5h5j-jqjh</code></a></td>
<td>Moderate</td>
<td>Denial of service in Image Optimization API</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-wfc6-r584-vfw7"><code>GHSA-wfc6-r584-vfw7</code></a></td>
<td>Moderate</td>
<td>Cache poisoning in RSC responses</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-vfv6-92ff-j949"><code>GHSA-vfv6-92ff-j949</code></a></td>
<td>Low</td>
<td>Cache poisoning via RSC cache-busting collisions</td>
<td>Not possible to safely enable a managed WAF rule without potentially breaking application behavior</td>
</tr>
<tr>
<td><a href="https://github.com/vercel/next.js/security/advisories/GHSA-3g8h-86w9-wvmq"><code>GHSA-3g8h-86w9-wvmq</code></a></td>
<td>Low</td>
<td>Middleware redirect cache poisoning</td>
<td>Custom WAF rule possible; global managed rule could potentially break application behavior</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-07">May 7, 2026</time><div>
<h2 id="post-2026-05-07-appliance-dhcp-options"><a href="/changelog/post/2026-05-07-appliance-dhcp-options/">Custom DHCP options on Cloudflare One Appliance</a></h2>
<div class="changelog-badges"><span>cloudflare-one-appliance</span><span>cloudflare-one</span><span>cloudflare-wan</span></div><div class="changelog-body"><p>When the Cloudflare One Appliance is acting as the DHCP server for a LAN, you can now configure custom DHCP options on the leases it issues. This unlocks workflows such as PXE / iPXE boot, VoIP phone provisioning, and vendor-specific client configuration.</p>
<p>Each option is defined by <code>option_number</code>, <code>value</code>, and one of four value types: <code>text</code>, <code>integer</code>, <code>hex</code>, or <code>ip</code>. Configurations are validated on the appliance before being applied — invalid configurations are rejected and the underlying error is returned to the API caller, so a bad option will not disrupt the live DHCP service.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-options/">DHCP server options</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-05-07">May 7, 2026</time><div>
<h2 id="post-2026-05-07-appliance-source-based-breakout"><a href="/changelog/post/2026-05-07-appliance-source-based-breakout/">Source-based breakout and prioritization on Cloudflare One Appliance</a></h2>
<div class="changelog-badges"><span>cloudflare-one-appliance</span><span>cloudflare-one</span><span>cloudflare-wan</span></div><div class="changelog-body"><p>Breakout and traffic prioritization rules on the Cloudflare One Appliance can now match by <strong>source</strong> in addition to destination application. You can pin breakout or priority behavior to:</p>
<ul>
<li>A source LAN interface — VLANs attached to that LAN are included automatically.</li>
<li>A source IP address, range, or CIDR block.</li>
</ul>
<p>This is the natural way to break out a guest VLAN to the local Internet, or to prioritize traffic from a specific subnet, without enumerating destination applications.</p>
<p>For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#breakout-by-source">Breakout traffic</a>.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/14/">Previous</a><span>Page 15 of 50</span><a class="pagination-next" rel="next" href="/changelog/16/">Next</a></nav>
</div>
