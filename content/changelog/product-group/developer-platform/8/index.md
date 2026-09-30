<h1 id="changelog">Changelog</h1>

<h2 id="cloudflare-tunnel-now-runs-connectivity-pre-checks-at-startup"><a href="/changelog/post/2026-05-27-cloudflared-connectivity-prechecks/">Cloudflare Tunnel now runs connectivity pre-checks at startup</a></h2>
<p><em>2026-05-27</em></p>
<p>Starting with <a href="https://github.com/cloudflare/cloudflared/releases"><code>cloudflared</code> version 2026.5.2</a>, <a href="/tunnel/">Cloudflare Tunnel</a> automates the entire <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/connectivity-prechecks/">connectivity pre-checks workflow</a> directly inside the binary. Previously, customers had to install <code>dig</code> and <code>netcat</code> and run those commands by hand to verify their environment. Now <code>cloudflared</code> does it natively at startup — and surfaces actionable remediation when something is blocked.</p>
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


<h2 id="flagship-now-in-public-beta"><a href="/changelog/post/2026-05-26-public-beta/">Flagship now in public beta</a></h2>
<p><em>2026-05-26</em></p>
<p><strong><a href="/flagship/">Flagship</a></strong> is now in public beta. Evaluate feature flags directly from Cloudflare Workers with no outbound HTTP calls, using globally distributed flag configuration backed by Workers KV and Durable Objects. Flagship supports typed flag values, targeting rules, percentage rollouts, audit history, and OpenFeature-compatible SDKs.</p>
<p>Evaluate a flag from a Worker in a few lines of code:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17724.md")</div>
<p>Start creating flags from the Cloudflare dashboard today. Refer to the <a href="/flagship/get-started/">Flagship documentation</a> to get started.</p>


<h2 id="call-any-ai-model-through-ai-gateway-s-new-rest-api"><a href="/changelog/post/2026-05-21-rest-api/">Call any AI model through AI Gateway's new REST API</a></h2>
<p><em>2026-05-21</em></p>
<p>AI Gateway now uses the AI REST API on <code>api.cloudflare.com</code>. You can call any model — whether from OpenAI, Anthropic, Google, or hosted on Workers AI — through one unified API, using the same endpoints and authentication regardless of provider. Four endpoints are available:</p>
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


<h2 id="granular-permissions-for-cloudflare-tunnel-and-cloudflare-mesh"><a href="/changelog/post/2026-05-21-tunnel-mesh-granular-permissions/">Granular permissions for Cloudflare Tunnel and Cloudflare Mesh</a></h2>
<p><em>2026-05-21</em></p>
<p>You can now scope Cloudflare permissions to individual <a href="/tunnel/">Cloudflare Tunnel</a> instances and <a href="/mesh/">Cloudflare Mesh</a> nodes. Administrators can delegate access to specific Tunnels or Mesh nodes without granting account-wide control over private networking.</p>
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


<h2 id="reach-cloudflare-wan-destinations-from-workers-vpc"><a href="/changelog/post/2026-05-21-vpc-networks-cloudflare-wan/">Reach Cloudflare WAN destinations from Workers VPC</a></h2>
<p><em>2026-05-21</em></p>
<p>You can now use <a href="/workers-vpc/configuration/vpc-networks/">VPC Network</a> bindings with <code>network_id: &quot;cf1:network&quot;</code> to reach your full private network from Workers, including:</p>
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


<h2 id="event-subscriptions-for-artifacts-lifecycle-events"><a href="/changelog/post/2026-05-19-event-subscriptions/">Event subscriptions for Artifacts lifecycle events</a></h2>
<p><em>2026-05-19</em></p>
<p>You can now receive <a href="/queues/event-subscriptions/">event notifications</a> for <a href="/artifacts/">Artifacts</a> repository changes and consume them from a Worker to build commit-driven automation.</p>
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


<h2 id="manage-artifacts-namespaces-and-repos-with-wrangler-cli"><a href="/changelog/post/2026-05-18-wrangler-support/">Manage Artifacts namespaces and repos with Wrangler CLI</a></h2>
<p><em>2026-05-18</em></p>
<p>You can now manage <a href="/artifacts/">Artifacts</a> namespaces, repos, and repo-scoped tokens directly from Wrangler CLI.</p>
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


<h2 id="share-local-dev-servers-through-cloudflare-tunnel-in-wrangler-and-vite"><a href="/changelog/post/2026-05-18-local-dev-tunnels/">Share local dev servers through Cloudflare Tunnel in Wrangler and Vite</a></h2>
<p><em>2026-05-18</em></p>
<p>You can now share local dev sessions through <a href="/tunnel/">Cloudflare Tunnel</a> and get a public URL when using either <a href="/workers/wrangler/">Wrangler</a> or the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>. This is useful when you need to share a preview, test a webhook, or access your app from another device.</p>
<p><img src="/assets/upstream/images/changelog/workers/vite-local-dev-tunnel.gif" alt="Vite local dev tunnel demo" /></p>
<p>This lets you either:</p>
<ul>
<li>start a temporary <a href="/tunnel/get-started/#quick-tunnels-development">Quick tunnel</a> with a random <code>*.trycloudflare.com</code> hostname, or</li>
<li>use an existing <a href="/tunnel/get-started/#create-a-tunnel">named tunnel</a> for a stable hostname and to restrict access with <a href="/cloudflare-one/access-controls/">Cloudflare Access</a>.</li>
</ul>
<p>To start a tunnel, press <code>t</code> in Wrangler or <code>t + Enter</code> in Vite while your dev server is running. For details on setting up a named tunnel, refer to <a href="/workers/local-development/local-dev-tunnels/">Share a local dev server</a>.</p>


<h2 id="hyperdrive-exposes-database-connection-pool-size-metrics"><a href="/changelog/post/2026-05-15-hyperdrive-pool-size-metrics/">Hyperdrive exposes database connection pool size metrics</a></h2>
<p><em>2026-05-15</em></p>
<p>You can now view the size of your Hyperdrive database connection pools, giving you the ability to self-diagnose connection issues. Using the Cloudflare dashboard or the <code>hyperdrivePoolSizesAdaptiveGroups</code> dataset in the <a href="/analytics/graphql-api/getting-started/">GraphQL Analytics API</a>, you can see <code>waitingClients</code>, <code>currentPoolSize</code>, <code>availablePoolSlots</code>, and <code>maxPoolSize</code> for each of your configurations.</p>
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


<h2 id="r2-sql-now-supports-joins-subqueries-and-multi-table-queries"><a href="/changelog/post/2026-05-14-joins-subqueries-multi-table-queries/">R2 SQL now supports JOINs, subqueries, and multi-table queries</a></h2>
<p><em>2026-05-15</em></p>
<p><a href="/r2-sql/">R2 SQL</a> is Cloudflare's serverless, distributed SQL engine for querying <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables stored in <a href="/r2-data-catalog/">R2 Data Catalog</a>. R2 SQL runs directly on Cloudflare's global network with no infrastructure to manage, so you can analyze data in R2 without exporting it to an external warehouse.</p>
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


<h2 id="new-domains-tab-in-the-workers-dashboard"><a href="/changelog/post/2026-05-14-domains-tab/">New Domains tab in the Workers dashboard</a></h2>
<p><em>2026-05-14</em></p>
<p>In your Worker's dashboard, there is now a dedicated <strong>Domains</strong> tab where you can purchase a new domain through Cloudflare Registrar and have it automatically connected, add an <a href="/workers/configuration/routing/custom-domains/">existing domain</a>, and manage all of your Worker's routing in one place.</p>
<p><img src="/assets/upstream/images/workers/changelog/domains-tab.png" alt="The new Domains tab in the Workers dashboard" /></p>
<p>You can also enable or disable your <a href="/workers/configuration/routing/workers-dev/"><code>workers.dev</code> subdomain</a> and <a href="/workers/versions-and-deployments/preview-urls/">Preview URLs</a>, put them behind <a href="/cloudflare-one/access-controls/">Cloudflare Access</a> to require sign-in, and jump directly to <a href="/analytics/">analytics</a> or domain overview for any connected domain.</p>
<p>To get started, go to <strong>Workers &amp; Pages</strong>, select a Worker, and open the <strong>Domains</strong> tab.</p>
<div class="nb-dash-button"></div>


<h2 id="agents-sdk-v0-12-4-chat-recovery-routing-retries-durable-think-submissions-and-voice-connection-control"><a href="/changelog/post/2026-05-13-agents-sdk-v0.12.4/">Agents SDK v0.12.4: chat recovery, routing retries, durable Think submissions, and Voice connection control</a></h2>
<p><em>2026-05-13</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> brings more reliable chat recovery, fixes Agent state synchronization during reconnects, adds durable submissions for Think, exposes routing retry configuration, and adds connection control for Voice agents.</p>
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


<h2 id="cdn-cgi-rum-endpoint-now-returns-405-for-non-post-requests"><a href="/changelog/post/2026-05-13-rum-405-method-not-allowed/">/cdn-cgi/rum endpoint now returns 405 for non-POST requests</a></h2>
<p><em>2026-05-13</em></p>
<p>The <code>/cdn-cgi/rum</code> beacon endpoint now returns <code>405 Method Not Allowed</code> for non-POST requests instead of <code>404 Not Found</code>. The response includes an <code>Allow: POST, OPTIONS</code> header per <a href="https://www.rfc-editor.org/rfc/rfc9110#section-15.5.6">RFC 9110 §15.5.6</a>.</p>
<p>Previously, sending a <code>GET</code> or other non-POST request to this endpoint returned a <code>404</code>, which was misleading because it suggested the endpoint did not exist. The new <code>405</code> response clearly indicates that the endpoint exists but only accepts <code>POST</code> requests.</p>
<p>The Web Analytics beacon (<code>beacon.min.js</code>) already uses <code>POST</code> for all metric submissions, so this change does not affect normal beacon operation. <code>OPTIONS</code> requests for CORS preflight continue to work as before.</p>
<p>For more information, refer to the <a href="/web-analytics/faq/#why-am-i-getting-a-405-method-not-allowed-error-from-cdn-cgirum">Web Analytics FAQ</a>.</p>


<h2 id="ssh-through-wrangler-is-now-enabled-by-default-for-containers"><a href="/changelog/post/2026-05-12-ssh-enabled-by-default/">SSH through Wrangler is now enabled by default for Containers</a></h2>
<p><em>2026-05-12</em></p>
<p>SSH through Wrangler is now enabled by default for <a href="/containers/">Containers</a>. Previously, you had to set <code>ssh.enabled</code> to <code>true</code> in your Container configuration before you could connect.</p>
<p>This change does not expose any publicly accessible ports on your Container. The SSH service is reachable only through <a href="/workers/wrangler/commands/containers/#containers-ssh"><code>wrangler containers ssh</code></a>, which authenticates against your Cloudflare account. You also need to add an <code>ssh-ed25519</code> public key to <code>authorized_keys</code> before anyone can connect, so enabling SSH alone does not grant access.</p>
<p>To connect, add a public key to your Container configuration and run <code>wrangler containers ssh &lt;INSTANCE_ID&gt;</code>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17711.md")</div>
<p>To disable SSH, set <code>ssh.enabled</code> to <code>false</code> in your Container configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17712.md")</div>
<p>For more information, refer to the <a href="/containers/guides/ssh/">SSH documentation</a>.</p>


<h2 id="r2-data-catalog-now-exposes-metrics-via-the-graphql-analytics-api"><a href="/changelog/post/2026-05-12-r2-data-catalog-graphql-analytics/">R2 Data Catalog now exposes metrics via the GraphQL Analytics API</a></h2>
<p><em>2026-05-12</em></p>
<p><a href="/r2-data-catalog/">R2 Data Catalog</a> is a managed Apache Iceberg data catalog built directly into your R2 bucket that allows you to connect query engines like <a href="/r2-sql/">R2 SQL</a>, Spark, Snowflake, and DuckDB to your data in R2.</p>
<p>You can now query analytics for your R2 Data Catalog warehouses via Cloudflare's <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. Two new datasets are available:</p>
<ul>
<li><strong><code>r2CatalogDataOperationsAdaptiveGroups</code></strong> tracks Iceberg REST API requests made to your catalog, including operation type, request duration, HTTP status, and request body bytes. Use this to monitor request volume and latency across warehouses, namespaces, and tables.</li>
<li><strong><code>r2CatalogTableMaintenanceAdaptiveGroups</code></strong> tracks table maintenance jobs such as compaction and snapshot expiration. Use this to monitor job success rates, files processed, bytes read and written, and job duration.</li>
</ul>
<p>Both datasets support filtering by warehouse name, namespace, table name, and time range. They also include percentile aggregations for duration metrics.</p>
<p>For detailed schema information and example queries, refer to the <a href="/r2-data-catalog/observability/metrics/">R2 Data Catalog metrics and analytics documentation</a>.</p>


<h2 id="planned-model-deprecations-on-workers-ai"><a href="/changelog/post/2026-05-08-planned-model-deprecations/">Planned model deprecations on Workers AI</a></h2>
<p><em>2026-05-08</em></p>
<p>We are refreshing the Workers AI model catalog to make room for newer releases. Please update your apps to remove references to the models listed below before the deprecation date.</p>
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


<h2 id="waf-and-framework-adapter-mitigations-for-react-and-next-js-vulnerabilities"><a href="/changelog/post/2026-05-06-react-nextjs-vulnerabilities/">WAF and framework adapter mitigations for React and Next.js vulnerabilities</a></h2>
<p><em>2026-05-07 12:00:00 UTC</em></p>
<p>Multiple security vulnerabilities were disclosed by the React team and Vercel affecting React Server Components and Next.js. These include denial of service, middleware and proxy bypass, server-side request forgery, cross-site scripting, and cache poisoning issues across a range of severity levels.</p>
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


<h2 id="introducing-stream-bindings-for-workers"><a href="/changelog/post/2026-05-07-stream-workers-binding/">Introducing Stream Bindings for Workers</a></h2>
<p><em>2026-05-07</em></p>
<p>You can now interact with your Stream video library using new bindings for Workers! This allows customers to upload content to Stream, provision direct uploads, manage videos, and generate signed URLs from a Worker without making authenticated API calls. We're excited to bring Stream and Workers closer together to empower more programmatic pipelines, tighter integrations, and support generative AI and inference workloads.</p>
<p>Use the Stream binding when you want to:</p>
<ul>
<li>Upload videos from URLs or create basic direct upload links for end users</li>
<li>Generate signed playback tokens without managing signing keys</li>
<li>Manage video metadata, captions, downloads, and watermarks</li>
<li>Build video pipelines entirely within Workers</li>
</ul>
<p>To get started, add the Stream binding to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17756.md")</div>
<p><strong>Generate a video with AI and upload directly to Stream</strong> or send a URL of a file you already have:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17757.md")</div>
<p><strong>Generate a signed URL without using a signing key</strong> or an API call:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17758.md")</div>
<p><strong>Get and set video properties</strong> easily:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17759.md")</div>
<p>For setup instructions and the full API reference, refer to <a href="/stream/manage-video-library/bindings/">Bind to Workers API</a>.</p>
<h4 id="2026-05-07-stream-workers-binding-get-started-with-your-agent">Get started with your Agent</h4>
<blockquote>
<p>Add a binding for Cloudflare Stream (env.STREAM). On the watch page, use the
Stream binding to get info based on the ID, and leverage video.meta.name as
the page title.</p>
</blockquote>


<h2 id="automatic-tracing-across-durable-object-and-worker-subrequests"><a href="/changelog/post/2026-05-07-automatic-tracing-across-do-and-worker-subrequests/">Automatic tracing across Durable Object and Worker subrequests</a></h2>
<p><em>2026-05-07</em></p>
<p>You can now get a single unified trace across Worker-to-Worker subrequests, with trace context propagating automatically. Previously, <a href="/workers/observability/traces/">automatic tracing</a> produced disconnected traces when a Worker called another Worker through a <a href="/workers/runtime-apis/bindings/service-bindings/">service binding</a> or <a href="/durable-objects/">Durable Object</a>.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2026-04-28-worker-to-worker-context-prop.png" alt="Unified trace showing nested spans across a Durable Object subrequest and a service binding call" /></p>
<p>This means you can:</p>
<ul>
<li>Follow a request through your entire Worker architecture in one trace view</li>
<li>See service binding and Durable Object calls as nested child spans instead of separate traces</li>
<li>Debug cross-Worker request flows in the Cloudflare dashboard or in an external observability platform via <a href="/workers/observability/exporting-opentelemetry-data/">OpenTelemetry</a></li>
</ul>
<p><a href="/workers/observability/traces/#how-to-enable-tracing">Tracing must be enabled</a> in your Wrangler configuration for traces to be recorded. Checkout <a href="/workers/observability/traces/">Workers tracing</a> to get started.</p>
<p>Up next, we are working on external trace context propagation using <a href="https://www.w3.org/TR/trace-context/">W3C Trace Context standards</a>, which will allow traces from your Workers to link with traces from services outside of Cloudflare.</p>


<h2 id="pipelines-and-r2-data-catalog-now-supported-in-terraform"><a href="/changelog/post/2026-04-27-terraform-support/">Pipelines and R2 Data Catalog now supported in Terraform</a></h2>
<p><em>2026-05-04</em></p>
<p><a href="/pipelines/">Cloudflare Pipelines</a> ingests streaming data via <a href="/workers/">Workers</a> or HTTP endpoints, transforms it with SQL, and writes it to <a href="/r2/">R2</a> as Apache Iceberg tables. <a href="/r2-data-catalog/">R2 Data Catalog</a> manages those Iceberg tables, compaction, and compatibility with query engines like <a href="/r2-sql/">R2 SQL</a>, <a href="/r2-data-catalog/config-examples/spark-scala/">Spark</a>, and <a href="/r2-data-catalog/config-examples/duckdb/">DuckDB</a>.</p>
<p>You can now create and manage both products using Terraform, supported in the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Terraform provider v5.19.0</a>.</p>
<p>This adds four new resources that let you define your entire data pipeline as infrastructure-as-code: a data catalog, a stream for ingestion, a sink that writes to R2 Data Catalog or R2, and a pipeline that connects them with SQL.</p>
<p>The new Terraform resources are:</p>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/r2_data_catalog"><code>cloudflare_r2_data_catalog</code></a> — enable the data catalog on an R2 bucket</li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/pipeline_stream"><code>cloudflare_pipeline_stream</code></a> — create a stream that receives events via HTTP or Worker bindings</li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/pipeline_sink"><code>cloudflare_pipeline_sink</code></a> — create a sink that writes to R2 Data Catalog or R2</li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/pipeline"><code>cloudflare_pipeline</code></a> — create a pipeline with SQL connecting a stream to a sink</li>
</ul>
<p>Here is a minimal example that creates a stream, an R2 Data Catalog sink, and a pipeline:</p>
<pre><code class="language-hcl">resource &quot;cloudflare_pipeline_stream&quot; &quot;my_stream&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  name       = &quot;my_stream&quot;&#10;  format     = { type = &quot;json&quot; }&#10;  schema = {&#10;    fields = [{&#10;      name     = &quot;value&quot;&#10;      type     = &quot;json&quot;&#10;      required = true&#10;    }]&#10;  }&#10;  http           = { enabled = true, authentication = false, cors = {} }&#10;  worker_binding = { enabled = false }&#10;}&#10;&#10;resource &quot;cloudflare_pipeline_sink&quot; &quot;my_sink&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  name       = &quot;my_sink&quot;&#10;  type       = &quot;r2_data_catalog&quot;&#10;  format     = { type = &quot;parquet&quot; }&#10;  schema     = { fields = [] }&#10;  config = {&#10;    account_id = var.cloudflare_account_id&#10;    bucket     = &quot;my-pipeline-bucket&quot;&#10;    table_name = &quot;my_table&quot;&#10;    token      = var.catalog_token&#10;  }&#10;}&#10;&#10;resource &quot;cloudflare_pipeline&quot; &quot;my_pipeline&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  name       = &quot;my_pipeline&quot;&#10;  sql        = &quot;INSERT INTO ${cloudflare_pipeline_sink.my_sink.name} SELECT * FROM ${cloudflare_pipeline_stream.my_stream.name}&quot;&#10;}&#10;</code></pre>
<p>For a full end-to-end example that includes R2 bucket creation, data catalog setup, and scoped API token provisioning, refer to the <a href="/pipelines/reference/terraform/">Pipelines Terraform documentation</a>.</p>


<h2 id="run-workflows-inside-dynamic-workers-with-the-cloudflare-dynamic-workflows-library"><a href="/changelog/post/2026-05-01-dynamic-workflows/">Run Workflows inside Dynamic Workers with the @cloudflare/dynamic-workflows library</a></h2>
<p><em>2026-05-01</em></p>
<p>You can now use <a href="https://github.com/cloudflare/dynamic-workflows"><code>@cloudflare/dynamic-workflows</code></a> to run a <a href="/workflows/">Workflow</a> inside a <a href="/dynamic-workers/">Dynamic Worker</a>, ensuring durable execution for code that is loaded at runtime.</p>
<p>The Worker Loader loads Dynamic Workers on demand, which previously made durability challenging. Even within a Dynamic Worker, a Workflow might sleep for hours or days between steps, and by the time it resumes, the original Dynamic Worker code would no longer be in memory.</p>
<p>The library solves this by tagging each Workflow instance with metadata that identifies which Dynamic Worker to load — for example, a tenant ID — then reloading the matching Dynamic Worker through the Worker Loader whenever a Workflow awakens.</p>
<p>Because Dynamic Workers are created on-demand, you do not have to register each Workflow up front or manage them individually. Load the Workflow code in the Dynamic Worker when it is needed, and the Workflows engine handles persistence and retries behind the scenes. Your Workflow code itself is unaffected by the routing and behaves as normal.</p>
<p>This unlocks patterns where the Workflow code itself is dynamic. For example, this is useful with:</p>
<ul>
<li><strong>SaaS platforms</strong> where each tenant defines their own automation, such as onboarding sequences, approval chains, or billing retry logic.</li>
<li><strong>AI agent frameworks</strong> where agents generate and execute multi-step plans at runtime, surviving restarts and waiting for human approval between tool calls.</li>
<li><strong>Multi-tenant job systems</strong> where each customer submits their own processing logic and every step persists progress and retries on failure.</li>
</ul>
<pre><code class="language-ts">import {&#10;	createDynamicWorkflowEntrypoint,&#10;	DynamicWorkflowBinding,&#10;	wrapWorkflowBinding,&#10;	type WorkflowRunner,&#10;} from &quot;@cloudflare/dynamic-workflows&quot;;&#10;&#10;export { DynamicWorkflowBinding };&#10;&#10;interface Env {&#10;	WORKFLOWS: Workflow;&#10;	LOADER: WorkerLoader;&#10;}&#10;&#10;function loadTenant(env: Env, tenantId: string) {&#10;	return env.LOADER.get(tenantId, async () =&gt; ({&#10;		compatibilityDate: &quot;2026-01-01&quot;,&#10;		mainModule: &quot;index.js&quot;,&#10;		modules: { &quot;index.js&quot;: await fetchTenantCode(tenantId) },&#10;		// The Dynamic Worker uses this exactly like a real Workflow binding;&#10;		// every create() is tagged with { tenantId } automatically.&#10;		env: { WORKFLOWS: wrapWorkflowBinding({ tenantId }) },&#10;	}));&#10;}&#10;&#10;// The entrypoint name must match `class_name` in the workflows binding of your Wrangler config file.&#10;export const DynamicWorkflow = createDynamicWorkflowEntrypoint&lt;Env&gt;(&#10;	async ({ env, metadata }) =&gt; {&#10;		const stub = loadTenant(env, metadata.tenantId as string);&#10;		return stub.getEntrypoint(&quot;TenantWorkflow&quot;) as unknown as WorkflowRunner;&#10;	},&#10;);&#10;&#10;export default {&#10;	fetch(request: Request, env: Env) {&#10;		const tenantId = request.headers.get(&quot;x-tenant-id&quot;)!;&#10;		return loadTenant(env, tenantId).getEntrypoint().fetch(request);&#10;	},&#10;};&#10;</code></pre>
<p>For a full walkthrough, refer to the <a href="/dynamic-workers/usage/dynamic-workflows/">Dynamic Workflows guide</a>.</p>


<h2 id="go-sdk-v7-0-0-released"><a href="/changelog/post/2026-04-30-go-sdk-v7.0.0/">Go SDK v7.0.0 Released</a></h2>
<p><em>2026-04-30</em></p>
<p>Full Changelog: <a href="https://github.com/cloudflare/cloudflare-go/compare/v6.10.0...v7.0.0">v6.10.0...v7.0.0</a></p>
<p>This is a major version release that includes breaking changes to three packages: <code>ai_search</code>, <code>email_security</code>, and <code>workers</code>. These changes reflect upstream API specification updates that improve type correctness and consistency.</p>
<p><strong>Please ensure you read through the list of changes below before moving to this version</strong> - this will help you understand any down or upstream issues it may cause to your environments.</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-breaking-changes">Breaking Changes</h4>
<p>See the <a href="https://github.com/cloudflare/cloudflare-go/blob/main/docs/migration-guides/v7.0.0-migration-guide.md">v7.0.0 Migration Guide</a> for before/after code examples and actions needed for each change.</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-ai-search-searchforagents-metadata-removed">AI Search - SearchForAgents Metadata Removed</h4>
<p>The <code>SearchForAgents</code> nested type has been removed from all instance metadata structs. This field is no longer part of the API specification.</p>
<p><strong>Removed Types:</strong></p>
<ul>
<li><code>InstanceNewResponseMetadataSearchForAgents</code></li>
<li><code>InstanceUpdateResponseMetadataSearchForAgents</code></li>
<li><code>InstanceListResponseMetadataSearchForAgents</code></li>
<li><code>InstanceDeleteResponseMetadataSearchForAgents</code></li>
<li><code>InstanceReadResponseMetadataSearchForAgents</code></li>
<li><code>InstanceNewParamsMetadataSearchForAgents</code></li>
<li><code>InstanceUpdateParamsMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceNewResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceUpdateResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceListResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceDeleteResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceReadResponseMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceNewParamsMetadataSearchForAgents</code></li>
<li><code>NamespaceInstanceUpdateParamsMetadataSearchForAgents</code></li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-email-security-path-parameter-type-changes">Email Security - Path Parameter Type Changes</h4>
<p>Multiple Email Security settings sub-resources have changed their path parameter types from <code>int64</code> to <code>string</code>:</p>
<ul>
<li><code>AllowPolicies</code> (<code>policyID int64</code> -&gt; <code>policyID string</code>)</li>
<li><code>BlockSenders</code> (<code>patternID int64</code> -&gt; <code>patternID string</code>)</li>
<li><code>Domains</code> (<code>domainID int64</code> -&gt; <code>domainID string</code>)</li>
<li><code>ImpersonationRegistry</code> (<code>displayNameID int64</code> -&gt; <code>impersonationRegistryID string</code>)</li>
<li><code>TrustedDomains</code> (<code>trustedDomainID int64</code> -&gt; <code>trustedDomainID string</code>)</li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-email-security-investigate-parameter-rename">Email Security - Investigate Parameter Rename</h4>
<p>The <code>Investigate.Get</code>, <code>Investigate.Move.New</code>, and <code>Investigate.Reclassify.New</code> methods now use <code>investigateID</code> instead of <code>postfixID</code> as the path parameter name.</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-email-security-domains-bulkdelete-method-removed">Email Security - Domains BulkDelete Method Removed</h4>
<p>The <code>SettingDomainService.BulkDelete</code> method and its associated types have been removed:</p>
<ul>
<li><code>SettingDomainBulkDeleteResponse</code></li>
<li><code>SettingDomainBulkDeleteParams</code></li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-email-security-trusteddomains-return-type-change">Email Security - TrustedDomains Return Type Change</h4>
<p><code>SettingTrustedDomainService.New</code> now returns <code>*SettingTrustedDomainNewResponse</code> instead of <code>*SettingTrustedDomainNewResponseUnion</code>.</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-email-security-investigate-move-return-type-change">Email Security - Investigate.Move Return Type Change</h4>
<p><code>InvestigateMoveService.New</code> now returns <code>*pagination.SinglePage[InvestigateMoveNewResponse]</code> instead of <code>*[]InvestigateMoveNewResponse</code>.</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-workers-observability-telemetry-filter-restructuring">Workers - Observability Telemetry Filter Restructuring</h4>
<p>The observability telemetry filter parameter types have been restructured to support nested filter groups. New discriminated union types replace the previous flat filter arrays:</p>
<ul>
<li><code>ObservabilityTelemetryKeysParams.Filters</code> now accepts <code>FiltersObjectFilterUnion</code> (was <code>[]interface\{\}</code>)</li>
<li><code>ObservabilityTelemetryQueryParams.Parameters.Filters</code> now accepts <code>FiltersObjectFilterUnion</code></li>
<li><code>ObservabilityTelemetryValuesParams.Filters</code> now accepts <code>FiltersObjectFilterUnion</code></li>
</ul>
<p>New types include <code>FiltersObjectFiltersObject</code> (for group filters with <code>FilterCombination</code>) and <code>FiltersWorkersObservabilityFilterLeaf</code> (for leaf filters with typed <code>Operation</code>, <code>Type</code>, and <code>Value</code> fields).</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-features">Features</h4>
<h4 id="2026-04-30-go-sdk-v7.0.0-organizations-audit-logs-client-organizations-logs-audit">Organizations - Audit Logs (<code>client.Organizations.Logs.Audit</code>)</h4>
<p><strong>NEW SERVICE:</strong> Query organization audit logs with cursor-based pagination.</p>
<ul>
<li><code>List()</code> - Retrieve audit logs</li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-browser-rendering-client-browserrendering">Browser Rendering (<code>client.BrowserRendering</code>)</h4>
<ul>
<li><code>client.BrowserRendering.Devtools.Browser.Targets.Close()</code> - Close a specific browser target (tab, page) by ID</li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-queues-client-queues">Queues (<code>client.Queues</code>)</h4>
<ul>
<li><code>client.Queues.GetMetrics()</code> - Retrieve queue metrics for a specific queue</li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-ai-search-client-aisearch">AI Search (<code>client.AISearch</code>)</h4>
<ul>
<li>Added <code>WaitForCompletion</code> parameter to <code>NamespaceInstanceItemNewOrUpdateParams</code> and <code>NamespaceInstanceItemSyncParams</code> for synchronous indexing confirmation</li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-bug-fixes">Bug Fixes</h4>
<ul>
<li><strong>Magic Transit</strong>: <code>ConnectorService.List</code> parameter name corrected from <code>query</code> to <code>params</code> (non-functional, affects generated documentation only)</li>
</ul>
<h4 id="2026-04-30-go-sdk-v7.0.0-deprecations">Deprecations</h4>
<p>None in this release.</p>
<h4 id="2026-04-30-go-sdk-v7.0.0-get-started">Get started</h4>
<ul>
<li><a href="https://github.com/cloudflare/cloudflare-go/releases/tag/v7.0.0">Download Go SDK v7.0.0</a></li>
<li><a href="https://developers.cloudflare.com/api/sdks/go/">Go SDK documentation</a></li>
<li><a href="https://github.com/cloudflare/cloudflare-go/blob/main/docs/migration-guides/v7.0.0-migration-guide.md">Migration Guide</a></li>
</ul>


<h2 id="empty-buckets-and-delete-folders-from-the-r2-dashboard"><a href="/changelog/post/2026-04-30-r2-empty-bucket-folder-delete/">Empty buckets and delete folders from the R2 dashboard</a></h2>
<p><em>2026-04-30</em></p>
<p>You can now empty an entire <a href="/r2/">R2</a> bucket or delete folders directly from the dashboard. Emptying a bucket is required before you can delete it. Previously, this required scripting or configuring <a href="/r2/buckets/object-lifecycles/">lifecycle rules</a>. Now, the dashboard can handle it in a single action.</p>
<h4 id="2026-04-30-r2-empty-bucket-folder-delete-empty-a-bucket">Empty a bucket</h4>
<p>Go to your bucket's <strong>Settings</strong> tab and select <strong>Empty</strong> under the <strong>Empty Bucket</strong> section. This deletes all objects in the bucket while preserving the bucket and its configuration. For large buckets, the operation runs in the background and the dashboard displays progress.</p>
<p>Emptying a bucket is also a prerequisite for deleting it. The dashboard now guides you through both steps in one place.</p>
<p><img src="/assets/upstream/images/r2/empty-bucket-changelog.png" alt="Empty Bucket and Delete Bucket sections in the R2 dashboard Settings tab" /></p>
<h4 id="2026-04-30-r2-empty-bucket-folder-delete-delete-folders">Delete folders</h4>
<p>R2 uses a flat object structure. The dashboard groups objects that share a common prefix into folders when the <strong>View prefixes as directories</strong> checkbox is selected. Deleting a folder removes every object under that prefix.</p>
<p>From the <strong>Objects</strong> tab, you can select one or more folders and delete them alongside individual objects.</p>
<p>For step-by-step instructions, refer to <a href="/r2/buckets/delete-buckets/">Delete buckets</a> and <a href="/r2/objects/delete-objects/">Delete objects</a>.</p>


<h2 id="cloudflare-python-sdk-v5-0-0-released"><a href="/changelog/post/2026-04-30-cloudflare-python-v5.0.0/">Cloudflare Python SDK v5.0.0 Released</a></h2>
<p><em>2026-04-30</em></p>
<p>Full Changelog: <a href="https://github.com/cloudflare/cloudflare-python/compare/v4.3.1...v5.0.0">v4.3.1...v5.0.0</a></p>
<p>This is a major release of the Cloudflare Python SDK. It drops support for Python 3.8, adds 11 new API services, introduces optional aiohttp backend support for improved async concurrency, and includes hundreds of type and method updates across the entire API surface.</p>
<p><strong>Please review the breaking changes below before upgrading.</strong> A migration guide is available at <a href="https://github.com/cloudflare/cloudflare-python/blob/main/docs/migration-guides/v5.0.0-migration-guide.md">v5.0.0 Migration Guide</a>.</p>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-breaking-changes">Breaking Changes</h4>
<ul>
<li><strong>Python 3.8 is no longer supported.</strong> The minimum required version is now Python 3.9.</li>
<li><strong><code>typing-extensions</code> minimum version bumped</strong> from <code>&gt;=4.10</code> to <code>&gt;=4.14</code>.</li>
</ul>
<p>The following resources have breaking changes. See the <a href="https://github.com/cloudflare/cloudflare-python/blob/main/docs/migration-guides/v5.0.0-migration-guide.md">v5.0.0 Migration Guide</a> for detailed migration instructions.</p>
<ul>
<li><code>abusereports</code></li>
<li><code>acm.totaltls</code></li>
<li><code>apigateway.configurations</code></li>
<li><code>cloudforceone.threatevents</code></li>
<li><code>d1.database</code></li>
<li><code>intel.indicatorfeeds</code></li>
<li><code>logpush.edge</code></li>
<li><code>origintlsclientauth.hostnames</code></li>
<li><code>queues.consumers</code></li>
<li><code>radar.bgp</code></li>
<li><code>rulesets.rules</code></li>
<li><code>schemavalidation.schemas</code></li>
<li><code>snippets</code></li>
<li><code>zerotrust.dlp</code></li>
<li><code>zerotrust.networks</code></li>
</ul>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-features">Features</h4>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-aiohttp-backend-support">aiohttp Backend Support</h4>
<p>The async client now supports an optional <code>aiohttp</code> HTTP backend for improved concurrency performance. Install with <code>pip install cloudflare[aiohttp]</code> and use <code>DefaultAioHttpClient()</code> as the <code>http_client</code> parameter.</p>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-python-3-13-and-3-14-support">Python 3.13 and 3.14 Support</h4>
<p>Python 3.13 and 3.14 are now tested and supported.</p>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-new-services">New Services</h4>
<p>The following top-level resources are new in this release:</p>
<table>
<thead>
<tr>
<th>Resource</th>
<th>Client Path</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>AI Search</td>
<td><code>aisearch</code></td>
<td>AI-powered search capabilities</td>
</tr>
<tr>
<td>Connectivity</td>
<td><code>connectivity</code></td>
<td>Connectivity testing and diagnostics</td>
</tr>
<tr>
<td>Email Sending</td>
<td><code>email_sending</code></td>
<td>Email send and send_raw endpoints</td>
</tr>
<tr>
<td>Fraud</td>
<td><code>fraud</code></td>
<td>Fraud detection and prevention</td>
</tr>
<tr>
<td>Google Tag Gateway</td>
<td><code>google_tag_gateway</code></td>
<td>Google Tag Gateway management</td>
</tr>
<tr>
<td>Organizations</td>
<td><code>organizations</code></td>
<td>Organization audit logs and management</td>
</tr>
<tr>
<td>R2 Data Catalog</td>
<td><code>r2_data_catalog</code></td>
<td>R2 Data Catalog operations</td>
</tr>
<tr>
<td>Realtime Kit</td>
<td><code>realtime_kit</code></td>
<td>Realtime communication (Calls/TURN)</td>
</tr>
<tr>
<td>Resource Tagging</td>
<td><code>resource_tagging</code></td>
<td>Resource tagging and labeling</td>
</tr>
<tr>
<td>Token Validation</td>
<td><code>token_validation</code></td>
<td>Token validation configuration and rules</td>
</tr>
<tr>
<td>Vulnerability Scanner</td>
<td><code>vulnerability_scanner</code></td>
<td>Vulnerability scanning, credential sets, and target environments</td>
</tr>
</tbody>
</table>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-new-endpoints-on-existing-services">New Endpoints on Existing Services</h4>
<ul>
<li><strong>api_gateway</strong>: Labels endpoints</li>
<li><strong>billing</strong>: Billable usage PayGo endpoint</li>
<li><strong>brand_protection</strong>: v2 endpoints</li>
<li><strong>browser_rendering</strong>: DevTools methods</li>
<li><strong>cache</strong>: Origin cloud regions resource</li>
<li><strong>custom_origin_trust_store</strong>: Custom origin trust store</li>
<li><strong>dns</strong>: <code>dns_records/usage</code> endpoints</li>
<li><strong>email_security</strong>: Phishguard reports endpoint</li>
<li><strong>iam</strong>: User groups and user group members resources</li>
<li><strong>radar</strong>: Botnet Threat Feed and Post-Quantum endpoints</li>
<li><strong>workers</strong>: Observability Destinations resources</li>
<li><strong>zero_trust</strong>: Access Users, DEX rules, Device IP Profile, Device Subnet, WARP Connector connections and failover, WARP Subnet, Gateway PAC files</li>
<li><strong>zones</strong>: Zone environments endpoints</li>
</ul>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-bug-fixes">Bug Fixes</h4>
<ul>
<li>Fixed <code>polymorphic_serialization</code> parameter in <code>model_dump</code> overrides</li>
<li>Added <code>BaseModel</code> base to response <code>SchemaFieldStruct</code>/<code>SchemaFieldList</code> stubs in Pipelines</li>
<li>Added missing <code>model_rebuild</code>/<code>update_forward_refs</code> for <code>SharedEntryCustomEntry</code> classes in DLP</li>
<li>Made <code>RunQueryParametersNeedleValue</code> a <code>BaseModel</code> with <code>arbitrary_types_allowed</code> in Workers</li>
<li>Removed duplicate <code>notification_url</code> field in webhook response types for Stream</li>
<li>Resolved pre-existing codegen type errors</li>
<li>Fixed <code>type: ignore[call-arg]</code> placement for mypy compatibility in Radar</li>
</ul>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-deprecations">Deprecations</h4>
<p>Resources with <code>@deprecated</code> annotations on some methods include: <code>accounts</code>, <code>addressing</code>, <code>ai-gateway</code>, <code>aisearch</code>, <code>api-gateway</code>, <code>billing</code>, <code>cloudforce-one</code>, <code>dns</code>, <code>email-routing</code>, <code>email-security</code>, <code>filters</code>, <code>firewall</code>, <code>images</code>, <code>intel</code>, <code>kv</code>, <code>logpush</code>, <code>origin-tls-client-auth</code>, <code>pages</code>, <code>pipelines</code>, <code>radar</code>, <code>rate-limits</code>, <code>registrar</code>, <code>rulesets</code>, <code>ssl</code>, <code>user</code>, <code>workers</code>, <code>workers-for-platforms</code>, <code>zero-trust</code>, <code>zones</code></p>
<h4 id="2026-04-30-cloudflare-python-v5.0.0-get-started">Get started</h4>
<ul>
<li><a href="https://github.com/cloudflare/cloudflare-python/releases/tag/v5.0.0">Download Python SDK v5.0.0</a></li>
<li><a href="https://developers.cloudflare.com/api/sdks/python/">Python SDK documentation</a></li>
<li><a href="https://github.com/cloudflare/cloudflare-python/blob/main/docs/migration-guides/v5.0.0-migration-guide.md">Migration Guide</a></li>
</ul>


<h2 id="cloudflare-typescript-sdk-v6-0-0-released"><a href="/changelog/post/2026-04-30-cloudflare-typescript-v6.0.0/">Cloudflare TypeScript SDK v6.0.0 Released</a></h2>
<p><em>2026-04-30</em></p>
<p>Full Changelog: <a href="https://github.com/cloudflare/cloudflare-typescript/compare/v6.0.0-beta.2...v6.0.0">v6.0.0-beta.2...v6.0.0</a></p>
<p>This is a major version release of the Cloudflare TypeScript SDK. It includes 11 entirely new top-level API resources, new sub-resources and methods across 50+ existing resources, SDK infrastructure improvements, and breaking changes to the generated API surface from the v5.x line.</p>
<p><strong>Please ensure you read through the list of changes below before moving to this version</strong> - this will help you understand any down or upstream issues it may cause to your environments.</p>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-breaking-changes">Breaking Changes</h4>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-sdk-infrastructure">SDK Infrastructure</h4>
<ul>
<li><strong>Retry-After handling changed</strong>: The SDK now respects any server-specified <code>Retry-After</code> value for rate-limited requests. Previously, values over 60 seconds were ignored and a default backoff was used instead.</li>
<li><strong>Empty response handling</strong>: Responses with <code>content-length: 0</code> now return <code>undefined</code> instead of attempting to parse the body.</li>
<li><strong>Environment variable reading</strong>: Empty string env vars (for example, <code>CLOUDFLARE_API_TOKEN=&quot;&quot;</code>) are now treated as unset.</li>
<li><strong>Path query parameter merging</strong>: URL search params embedded in endpoint paths are now extracted and merged into the query object.</li>
</ul>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-removed-endpoints-17">Removed Endpoints (17)</h4>
<p>17 HTTP endpoints were removed from the SDK, affecting <code>abuse-reports</code>, <code>cloudforce-one</code>, <code>dlp/profiles/predefined</code>, <code>email-security/investigate</code>, <code>email-security/settings</code>, and <code>intel/ip-list</code>.</p>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-method-signature-changes">Method Signature Changes</h4>
<ul>
<li><code>client.ai.toMarkdown.transform(file, \{ ...params \})</code> -&gt; <code>client.ai.toMarkdown.transform(\{ ...params \})</code> -- <code>file</code> moved from positional arg into params body</li>
<li><code>client.radar.ai.toMarkdown.create(body, \{ ...params \})</code> -&gt; <code>client.radar.ai.toMarkdown.create(\{ ...params \})</code> -- <code>body</code> moved from positional arg into params</li>
<li><code>client.abuseReports.create(reportType, \{ ...params \})</code> -&gt; <code>client.abuseReports.create(reportParam, \{ ...params \})</code> -- positional arg renamed</li>
<li><code>client.iam.userGroups.members.create(userGroupId, [ ...body ])</code> -&gt; <code>client.iam.userGroups.members.create(userGroupId, [ ...members ])</code> -- body array param renamed</li>
</ul>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-renamed-client-paths">Renamed Client Paths</h4>
<ul>
<li><code>client.originTLSClientAuth.hostnames.certificates</code> -&gt; <code>client.originTLSClientAuth.zoneCertificates</code></li>
<li><code>client.radar.netflows</code> -&gt; <code>client.radar.netFlows</code> (casing change)</li>
</ul>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-return-type-changes-179">Return Type Changes (179)</h4>
<ul>
<li><strong>133 methods now return <code>null</code></strong> instead of a typed response object. This primarily affects delete operations across <code>accounts</code>, <code>cache</code>, <code>d1</code>, <code>filters</code>, <code>firewall</code>, <code>hyperdrive</code>, <code>iam</code>, <code>kv</code>, <code>logpush</code>, <code>logs</code>, <code>r2</code>, <code>stream</code>, <code>workers</code>, <code>zero-trust</code>, <code>zones</code>, and others.</li>
<li><strong>17 methods changed pagination type</strong> (for example, <code>KeysCursorPaginationAfter</code> -&gt; <code>KeysCursorLimitPagination</code>).</li>
<li><strong>29 methods changed to a different named type</strong> (for example, <code>CloudflaredCreateResponse</code> -&gt; <code>CloudflareTunnel</code>).</li>
</ul>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-removed-types-43">Removed Types (43)</h4>
<p>24 shared types removed from root namespace (<code>ASN</code>, <code>AuditLog</code>, <code>Member</code>, <code>Permission</code>, <code>Role</code>, <code>Subscription</code>, <code>Token</code>, etc.). 19 response types consolidated or renamed.</p>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-resource-restructuring">Resource Restructuring</h4>
<p>19 resources were restructured from single files to directories. Public API client paths are unchanged, but deep imports may break.</p>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-new-top-level-resources">New Top-Level Resources</h4>
<p>11 entirely new resources added to the client:</p>
<table>
<thead>
<tr>
<th>Resource</th>
<th>Client Path</th>
<th>Methods</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>AI Search</td>
<td><code>client.aiSearch</code></td>
<td>46</td>
<td>Instances, namespaces, tokens, and items</td>
</tr>
<tr>
<td>Connectivity</td>
<td><code>client.connectivity</code></td>
<td>5</td>
<td>Directory service APIs</td>
</tr>
<tr>
<td>Email Sending</td>
<td><code>client.emailSending</code></td>
<td>7</td>
<td>Send and send_raw endpoints</td>
</tr>
<tr>
<td>Fraud</td>
<td><code>client.fraud</code></td>
<td>2</td>
<td>Fraud detection API</td>
</tr>
<tr>
<td>Google Tag Gateway</td>
<td><code>client.googleTagGateway</code></td>
<td>2</td>
<td>Google Tag Gateway management</td>
</tr>
<tr>
<td>Organizations</td>
<td><code>client.organizations</code></td>
<td>8</td>
<td>Organization profiles and audit logs</td>
</tr>
<tr>
<td>R2 Data Catalog</td>
<td><code>client.r2DataCatalog</code></td>
<td>11</td>
<td>R2 Data Catalog routes</td>
</tr>
<tr>
<td>Realtime Kit</td>
<td><code>client.realtimeKit</code></td>
<td>54</td>
<td>Realtime Kit APIs</td>
</tr>
<tr>
<td>Resource Tagging</td>
<td><code>client.resourceTagging</code></td>
<td>9</td>
<td>Resource tagging routes</td>
</tr>
<tr>
<td>Token Validation</td>
<td><code>client.tokenValidation</code></td>
<td>13</td>
<td>Token validation rules</td>
</tr>
<tr>
<td>Vulnerability Scanner</td>
<td><code>client.vulnerabilityScanner</code></td>
<td>21</td>
<td>Vulnerability scanning</td>
</tr>
</tbody>
</table>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-new-sub-resources-on-existing-resources">New Sub-Resources on Existing Resources</h4>
<ul>
<li><strong>browser-rendering</strong>: <code>crawl</code>, <code>devtools</code> - Crawl endpoints and DevTools methods</li>
<li><strong>cache</strong>: <code>origin-cloud-regions</code> - Origin cloud regions resource</li>
<li><strong>dns</strong>: <code>usage</code> - DNS records usage endpoints</li>
<li><strong>d1</strong>: <code>time-travel</code> - Time travel get_bookmark and restore</li>
<li><strong>email-security</strong>: <code>phishguard</code> - Phishguard reports endpoint</li>
<li><strong>pipelines</strong>: <code>sinks</code>, <code>streams</code> - Pipelines restructure</li>
<li><strong>radar</strong>: <code>agent-readiness</code>, <code>geolocations</code>, <code>post-quantum</code> - New analytics endpoints</li>
<li><strong>workers</strong>: <code>observability</code> - Observability destinations</li>
<li><strong>zones</strong>: <code>environments</code> - Zone environments endpoints</li>
<li><strong>api-gateway</strong>: <code>labels</code> - Labels endpoints</li>
<li><strong>brand-protection</strong>: <code>v2</code> - V2 endpoints</li>
<li><strong>alerting</strong>: <code>silences</code> - Alert silencing API</li>
<li><strong>billing</strong>: <code>usage</code> - Billable usage PayGo endpoint</li>
<li><strong>iam</strong>: <code>sso</code> - SSO Connectors resource</li>
<li><strong>queues</strong>: <code>getMetrics</code> method - Queues metrics endpoint</li>
<li><strong>registrar</strong>: <code>registration-status</code>, <code>update-status</code> - Registrar API convergence</li>
<li><strong>zero-trust</strong>: DLP settings, DEX rules, Access Users, WARP Connector, WARP Subnets, Gateway PAC files, Gateway tenants</li>
</ul>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-bug-fixes">Bug Fixes</h4>
<ul>
<li>Resolved type errors from codegen overwriting manual fixes</li>
<li>Fixed <code>post()</code> usage for to-markdown endpoints to resolve async type error</li>
<li>Added least-privilege permissions to all workflow jobs</li>
<li>Reverted erroneous removal of rulesets resource methods and types</li>
<li>Resolved prettier formatting errors in codegen output</li>
</ul>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-deprecations">Deprecations</h4>
<p>The following resources now include <code>@deprecated</code> annotations on some methods:</p>
<p><code>accounts</code>, <code>addressing</code>, <code>ai-gateway</code>, <code>aisearch</code>, <code>api-gateway</code>, <code>billing</code>, <code>cloudforce-one</code>, <code>custom-nameservers</code>, <code>dns</code>, <code>email-routing</code>, <code>email-security</code>, <code>filters</code>, <code>firewall</code>, <code>images</code>, <code>intel</code>, <code>keyless-certificates</code>, <code>kv</code>, <code>logpush</code>, <code>origin-tls-client-auth</code>, <code>page-shield</code>, <code>pages</code>, <code>pipelines</code>, <code>radar</code>, <code>rate-limits</code>, <code>registrar</code>, <code>rulesets</code>, <code>ssl</code>, <code>user</code>, <code>workers</code>, <code>workers-for-platforms</code>, <code>zero-trust</code>, <code>zones</code></p>
<h4 id="2026-04-30-cloudflare-typescript-v6.0.0-get-started">Get started</h4>
<ul>
<li><a href="https://github.com/cloudflare/cloudflare-typescript/releases/tag/v6.0.0">Download TypeScript SDK v6.0.0</a></li>
<li><a href="https://developers.cloudflare.com/api/sdks/typescript/">TypeScript SDK documentation</a></li>
<li><a href="https://github.com/cloudflare/cloudflare-typescript/blob/main/CHANGELOG.md">Full Changelog</a></li>
</ul>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/developer-platform/7/">Previous</a><span>Page 8 of 23</span><a class="pagination-next" rel="next" href="/changelog/product-group/developer-platform/9/">Next</a></nav>
