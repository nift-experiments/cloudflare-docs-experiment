<h1 id="changelog">Changelog</h1>

<h2 id="control-ai-search-similarity-cache-freshness"><a href="/changelog/post/2026-06-24-ai-search-similarity-cache-controls/">Control AI Search similarity cache freshness</a></h2>
<p><em>2026-06-24</em></p>
<p><a href="/ai-search/">AI Search</a> now gives you more control over <a href="/ai-search/configuration/retrieval/cache/">similarity cache</a> freshness. Similarity cache helps reduce latency and inference cost by reusing responses for semantically similar queries.</p>
<p>With these updates, you can choose how long responses are eligible for reuse and clear cached responses when they may be stale.</p>
<h4 id="2026-06-24-ai-search-similarity-cache-controls-cache-duration-now-defaults-to-48-hours">Cache duration now defaults to 48 hours</h4>
<p>Previously, AI Search cached responses for a fixed duration of 30 days. Cached responses now use the instance's <code>cache_ttl</code> setting, and the default is <strong>48 hours</strong>.</p>
<p>You can set <code>cache_ttl</code> when creating or updating an instance to choose a cache duration from 10 minutes to 6 days.</p>
<p>Use a shorter TTL when your source content changes frequently and freshness is more important. Use a longer TTL when your content is stable and you want more cache reuse.</p>
<p>For example, set <code>cache_ttl</code> to <code>518400</code> to retain cached responses for 6 days:</p>
<pre><code class="language-json">{&#10;	&quot;cache_ttl&quot;: 518400&#10;}&#10;</code></pre>
<h4 id="2026-06-24-ai-search-similarity-cache-controls-purge-cached-responses">Purge cached responses</h4>
<p>You can also purge all cached responses for an instance on demand. Purging cached responses does not delete indexed content or source files.</p>
<p>It prevents AI Search from reusing previous cached responses, so subsequent similar queries generate fresh answers and repopulate the cache.</p>
<pre><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai-search/instances/$INSTANCE_NAME/purge_cache&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>You can also purge cached responses from the instance settings page in the Cloudflare dashboard.</p>
<p>Refer to <a href="/ai-search/configuration/retrieval/cache/">similarity cache</a> for the full list of supported <code>cache_ttl</code> values and more details about cache behavior.</p>


<h2 id="workflows-rollback-handlers-now-include-step-context"><a href="/changelog/post/2026-06-16-rollback-options/">Workflows rollback handlers now include step context</a></h2>
<p><em>2026-06-23 12:00:00 UTC</em></p>
<p><a href="/workflows/">Workflows</a> makes it easier to build reliable multi-step applications that can recover when downstream systems fail. Rollback handlers now receive the original <a href="/workflows/build/step-context/">step context</a> via a <code>ctx</code> object for the step being rolled back. This includes <code>ctx.step.name</code>, <code>ctx.step.count</code>, <code>ctx.attempt</code>, and the step <code>config</code> with defaults applied.</p>
<p>The <a href="/workflows/build/workers-api/#workflowstepconfig">step configuration</a> includes the retry and timeout settings used for that step, so you can customize your step recovery logic according to those fields.</p>
<pre><code class="language-ts">await step.do(&#10;	&quot;create charge&quot;,&#10;	async () =&gt; {&#10;		const charge = await createCharge();&#10;		return { chargeId: charge.id };&#10;	},&#10;	{&#10;		rollback: async ({ ctx, output, error }) =&gt; {&#10;			// `output` is the value returned by the step being rolled back.&#10;			const { chargeId } = output as { chargeId: string };&#10;			await refundCharge(chargeId, {&#10;				// `ctx` is the original step context, including step name, count, attempt, and config.&#10;				reason: `${ctx.step.name}: ${error.message}`,&#10;			});&#10;		},&#10;		rollbackConfig: {&#10;			// `rollbackConfig` controls retries and timeout for the rollback handler.&#10;			retries: { limit: 3, delay: &quot;30 seconds&quot;, backoff: &quot;linear&quot; },&#10;			timeout: &quot;5 minutes&quot;,&#10;		},&#10;	},&#10;);&#10;</code></pre>
<p>Refer to <a href="/workflows/build/workers-api/#rollback-options">rollback options</a> to learn more.</p>


<h2 id="regionalized-ip-bindings-for-regional-services"><a href="/changelog/post/2026-06-23-regionalized-ip-bindings/">Regionalized IP Bindings for Regional Services</a></h2>
<p><em>2026-06-23</em></p>
<p>Regional Services now supports <strong>Regionalized IP Bindings</strong>, letting you regionalize traffic at the IP layer for prefixes you bring to Cloudflare through <a href="/byoip/">Bring Your Own IP (BYOIP)</a>.</p>
<p>Where <a href="/data-localization/regional-services/regional-hostnames/">Regional Hostnames</a> regionalize traffic by hostname, Regionalized IP Bindings let you bind a CIDR from one of your prefixes to a region — ideal for address-map deployments and any service you address by IP rather than hostname. Cloudflare then terminates TLS and processes traffic to those addresses only within the data centers in that region.</p>
<p>Regionalized IP Bindings requires the Regional Services and Regional Services for BYOIP entitlements. Contact your account team to enable them.</p>
<p>To get started, refer to <a href="/data-localization/regional-services/ip-bindings/">Regionalized IP Bindings</a>.</p>


<h2 id="r2-sql-now-supports-window-functions-distinct-and-set-operations"><a href="/changelog/post/2026-06-21-window-functions-distinct-set-operations/">R2 SQL now supports window functions, DISTINCT, and set operations</a></h2>
<p><em>2026-06-22</em></p>
<p>R2 SQL now supports window functions, <code>SELECT DISTINCT</code>, set operations, and additional aggregates, making it easier to write analytical queries without preprocessing your data elsewhere.</p>
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
<pre><code class="language-sql">SELECT customer_id, region,&#10;       ROW_NUMBER() OVER (PARTITION BY region ORDER BY total_amount DESC) AS rank_in_region&#10;FROM my_namespace.sales_data&#10;</code></pre>
<h4 id="2026-06-21-window-functions-distinct-set-operations-filter-with-qualify">Filter with QUALIFY</h4>
<pre><code class="language-sql">SELECT customer_id, region, total_amount&#10;FROM my_namespace.sales_data&#10;QUALIFY ROW_NUMBER() OVER (PARTITION BY region ORDER BY total_amount DESC) &lt;= 3&#10;</code></pre>
<h4 id="2026-06-21-window-functions-distinct-set-operations-combine-tables-with-a-set-operation">Combine tables with a set operation</h4>
<pre><code class="language-sql">SELECT customer_id FROM my_namespace.sales_data&#10;EXCEPT&#10;SELECT customer_id FROM my_namespace.archived_sales&#10;</code></pre>
<p>The named <code>WINDOW</code> clause is not supported — inline the <code>OVER (...)</code> specification at each call site. For the full syntax reference, refer to the <a href="/r2-sql/sql-reference/">SQL reference</a>. For supported features and performance guidance, refer to <a href="/r2-sql/reference/limitations-best-practices/">Limitations and best practices</a>.</p>


<h2 id="manage-all-your-routes-from-one-page-in-the-dashboard"><a href="/changelog/post/2026-06-19-unified-routes-page/">Manage all your routes from one page in the dashboard</a></h2>
<p><em>2026-06-19</em></p>
<p>The <strong>Routes</strong> page in the Cloudflare dashboard now shows the routes across all of your connectors — <a href="/mesh/">Cloudflare Mesh</a> and <a href="/tunnel/">Cloudflare Tunnel</a> routes alongside <a href="/cloudflare-wan/">Cloudflare WAN</a> and <a href="/magic-transit/">Magic Transit</a> static routes — in a single table, instead of a separate routes view per product.</p>
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


<h2 id="new-asia-pacific-location-hints-apac-ne-and-apac-se"><a href="/changelog/post/2026-06-19-apac-ne-apac-se-location-hints/">New Asia-Pacific location hints: apac-ne and apac-se</a></h2>
<p><em>2026-06-19</em></p>
<p>Durable Objects now supports two new location hints for Asia-Pacific: <code>apac-ne</code> (Northeast Asia-Pacific) and <code>apac-se</code> (Southeast Asia-Pacific). Use <code>apac-ne</code> or <code>apac-se</code> when you want finer-grained placement within Asia-Pacific rather than the broader <code>apac</code> hint.</p>
<p>Use the new hints the same way as any other <code>locationHint</code>:</p>
<pre><code class="language-js">// Northeast Asia-Pacific (Japan, Korea, etc.)&#10;const stubNE = env.MY_DURABLE_OBJECT.get(id, { locationHint: &quot;apac-ne&quot; });&#10;&#10;// Southeast Asia-Pacific (Singapore, Indonesia, etc.)&#10;const stubSE = env.MY_DURABLE_OBJECT.get(id, { locationHint: &quot;apac-se&quot; });&#10;</code></pre>
<p>If your users are spread across all of Asia-Pacific, the existing <code>apac</code> hint remains the right choice. Only reach for <code>apac-ne</code> or <code>apac-se</code> when your traffic is clearly concentrated in one sub-region and you want to minimize round-trip time to that audience. The default behavior and what we generally recommended is not adding a location hint unless absolutely needed, this will create the Durable Object as close to the initializing request as possible to reduce latency.</p>
<p>As with all location hints, these are best-effort suggestions. Cloudflare will place the Durable Object in a nearby data center, not necessarily the exact hinted location.</p>
<p>For the full list of supported hints, refer to <a href="/durable-objects/reference/data-location/#provide-a-location-hint">Data location — Provide a location hint</a>.</p>


<h2 id="outbound-connections-keep-durable-objects-alive"><a href="/changelog/post/2026-06-19-outbound-connections-keep-dos-alive/">Outbound connections keep Durable Objects alive</a></h2>
<p><em>2026-06-19</em></p>
<p>Durable Objects now remain alive for the duration of active outbound connections created via <a href="/workers/runtime-apis/tcp-sockets/"><code>connect()</code></a> or an outbound WebSocket. Previously, a Durable Object would be evicted after 70-140 seconds of no incoming traffic, even if the object had an open outbound connection, which is a common pattern when streaming responses from a large language model (LLM) over TCP or an outbound WebSocket.</p>
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


<h2 id="temporary-accounts-for-ai-agent-deployments"><a href="/changelog/post/2026-06-19-temporary-accounts-for-agents/">Temporary accounts for AI agent deployments</a></h2>
<p><em>2026-06-19</em></p>
<p>AI agents can now deploy Workers to Cloudflare without first requiring a user to sign up, open a browser-based OAuth flow, click through the dashboard, or create an API token. When an agent tries to deploy without Cloudflare credentials, Wrangler can tell it to rerun with <code>--temporary</code>, then deploy the Worker to a temporary preview account.</p>
<p>To try this with your agent, update to Wrangler 4.102.0 or later, make sure you are logged out (<code>wrangler logout</code>), and then ask your agent to build something and deploy it to Cloudflare. The agent should follow Wrangler's output and deploy using the <code>--temporary</code> flag.</p>
<p><img src="/assets/upstream/images/workers/claim-deployments-flow.png" alt="Diagram showing an AI agent deploying, verifying, and redeploying a Worker to a temporary account, then claiming it after authentication and moving it to a permanent account" /></p>
<pre><code class="language-sh">wrangler deploy --temporary&#10;</code></pre>
<p>The temporary deployment stays live for 60 minutes. During that window, the agent can verify the Worker, redeploy changes, and return both the live Worker URL and claim URL. Opening the claim URL lets you sign in to or create a Cloudflare account and make the temporary account permanent.</p>
<p>Temporary preview accounts currently support a limited set of products, including Workers, Workers Static Assets, Workers KV, D1, Durable Objects, Hyperdrive, Queues, and SSL/TLS certificates. For supported products, limits, and claim behavior, refer to <a href="/workers/platform/claim-deployments/">Claim deployments (temporary accounts)</a>.</p>
<p>For more context, refer to <a href="https://blog.cloudflare.com/temporary-accounts/">Temporary Cloudflare Accounts for Agents</a>.</p>


<h2 id="exec-is-now-available-for-containers"><a href="/changelog/post/2026-06-18-container-exec/">exec() is now available for Containers</a></h2>
<p><em>2026-06-18</em></p>
<p><code>exec()</code> is now available for <a href="/containers/">Containers</a>. Use <code>this.ctx.container.exec()</code> to start processes inside a running Container, stream standard input and output, inspect exit codes, and signal each process.</p>
<p>Call <code>exec()</code> from a class extending <code>Container</code>, or from another Durable Object through <code>this.ctx.container</code>. The associated Container must already be running.</p>
<p>This example starts the Container when needed, then reads its Node.js version:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17713.md")</div>
<p>The command array starts an executable directly, without an implicit shell. Invoke a shell explicitly for pipes, redirects, or variable expansion.</p>
<p>One RPC method can coordinate multiple <code>exec()</code> calls in one caller-to-Durable Object round trip. It can also pass byte-oriented <code>ReadableStream</code> input or return streamed output with flow control.</p>
<p>For options and streaming examples, refer to <a href="/containers/guides/execute-commands/">Execute commands</a>.</p>


<h2 id="create-planetscale-postgres-and-mysql-databases-billed-to-your-cloudflare-account"><a href="/changelog/post/2026-06-18-planetscale-databases-cloudflare-billing/">Create PlanetScale Postgres and MySQL databases, billed to your Cloudflare account</a></h2>
<p><em>2026-06-18</em></p>
<p>You can create PlanetScale Postgres and MySQL databases from Cloudflare and bill PlanetScale database usage through your Cloudflare account as a pay-as-you-go customer. Cloudflare contract customers will be able to add PlanetScale usage to their contract in July so reach out to your Cloudflare account team if interested.</p>
<p>Create a PlanetScale database from the Cloudflare dashboard to check out globally distributed Workers optimized for regional data access.</p>
<div class="nb-dash-button"></div>
<p><img src="/assets/upstream/images/hyperdrive/planetscale-request-flow.svg" alt="Request flow from a user to Workers, Hyperdrive caches, connection pools, and PlanetScale." /></p>
<p>PlanetScale databases created from Cloudflare work with <a href="/workers/">Workers</a> through <a href="/hyperdrive/">Hyperdrive</a>. Hyperdrive manages database connection pools and query caching, so you can use PlanetScale as a centralized relational database for Workers applications without changing your database drivers, object-relational mapping (ORM) libraries, or SQL tooling.</p>
<p>PlanetScale usage appears on your Cloudflare invoice each billing period as a dollar total at PlanetScale's standard <a href="https://planetscale.com/pricing">pricing</a>. You can introspect per-database billing usage via PlanetScale's <a href="https://planetscale.com/docs/billing#organization-usage-and-billing-page">dashboard</a>.</p>
<p>When you create a PlanetScale database from the Cloudflare dashboard, you receive the same PlanetScale developer experience, including development branches, query insights, and Model Context Protocol (MCP) server support for agents.</p>
<p>To get started, refer to <a href="/hyperdrive/planetscale/">PlanetScale Postgres and MySQL with Hyperdrive</a>.</p>


<h2 id="manage-artifacts-from-the-cloudflare-dashboard"><a href="/changelog/post/2026-06-17-dashboard-management/">Manage Artifacts from the Cloudflare dashboard</a></h2>
<p><em>2026-06-17T12:00:00+00:00</em></p>
<p>You can now configure <a href="/artifacts/concepts/how-artifacts-works/">Artifacts</a> namespaces, repos, and tokens directly from the Cloudflare dashboard.</p>
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


<h2 id="agents-sdk-improves-browser-automation-code-execution-and-recovery"><a href="/changelog/post/2026-06-16-agents-sdk-v0.16.1/">Agents SDK improves browser automation, code execution, and recovery</a></h2>
<p><em>2026-06-16</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> makes it easier to build agents that can safely interact with real systems and keep working through interruptions.</p>
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
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest @cloudflare/ai-chat@latest @cloudflare/voice@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Refer to the <a href="/agents/tools/codemode/">Code Mode documentation</a>, <a href="/agents/tools/browser/">Browser tools documentation</a>, <a href="/agents/harnesses/think/tools/">Think tools documentation</a>, and <a href="/agents/communication-channels/voice/">Voice documentation</a> for more information.</p>


<h2 id="new-optimization-features-in-images"><a href="/changelog/post/2026-06-16-new-optimization-features/">New optimization features in Images</a></h2>
<p><em>2026-06-16</em></p>
<p>These updates introduce new features for optimizing and manipulating with Images:</p>
<ul>
<li><strong>New <code>composite</code> option:</strong> Control how <a href="/images/optimization/draw-overlays/#composite">overlays are blended</a> with the base image.</li>
<li><strong>Percentage widths:</strong> Set the dimensions of an overlay as <a href="/images/optimization/draw-overlays/#width-and-height">a fraction of the dimensions</a> of the base image.</li>
<li><strong>New <code>fit</code> modes:</strong> Use <a href="/images/optimization/features/#aspect-crop"><code>aspect-crop</code></a> to always preserve the target aspect ratio or <a href="/images/optimization/features/#scale-up"><code>scale-up</code></a> to always enlarge images.</li>
<li><strong>New <code>upscale</code> parameter:</strong> Apply <a href="/images/optimization/features/#upscale">AI upscaling</a> to produce sharper, more detailed results when enlarging images.</li>
</ul>


<h2 id="workers-tracing-now-supports-custom-spans"><a href="/changelog/post/2026-06-16-custom-spans/">Workers tracing now supports custom spans</a></h2>
<p><em>2026-06-16</em></p>
<p>You can now create custom trace spans in your Workers code using <code>tracing.enterSpan()</code>. Custom spans appear alongside the automatic platform instrumentation (fetch calls, KV reads, D1 queries, and other platform operations) in your traces and OpenTelemetry exports, with correct parent-child nesting.</p>
<p>The API is available via <code>import { tracing } from &quot;cloudflare:workers&quot;</code> or through the handler context as <code>ctx.tracing</code>:</p>
<pre><code class="language-ts">import { tracing } from &quot;cloudflare:workers&quot;;&#10;&#10;export default {&#10;  async fetch(request, env, ctx) {&#10;    return tracing.enterSpan(&quot;handleRequest&quot;, async (span) =&gt; {&#10;      span.setAttribute(&quot;url.path&quot;, new URL(request.url).pathname);&#10;      const data = await env.MY_KV.get(&quot;key&quot;);&#10;      return new Response(data);&#10;    });&#10;  },&#10;};&#10;</code></pre>
<p>Spans nest automatically based on the JavaScript async context, and are auto-ended when the callback returns or its returned promise settles. The <code>Span</code> object provides <code>setAttribute(key, value)</code> for attaching metadata and an <code>isTraced</code> property to check whether the current request is being sampled.</p>
<p><img src="/assets/upstream/images/workers-observability/wobs_custom_spans_screenshot.png" alt="Trace waterfall showing custom spans nested alongside automatic KV and fetch instrumentation" /></p>
<p><a href="/workers/observability/traces/#how-to-enable-tracing">Tracing must be enabled</a> in your Wrangler configuration for spans to be recorded.</p>
<p>For full API details and examples, refer to <a href="/workers/observability/traces/custom-spans/">Custom spans</a>.</p>


<h2 id="introducing-glm-5-2-on-workers-ai"><a href="/changelog/post/2026-06-16-glm-5.2-workers-ai/">Introducing GLM-5.2 on Workers AI</a></h2>
<p><em>2026-06-16</em></p>
<p>We are excited to announce <strong>GLM-5.2</strong> on Workers AI, Z.ai's flagship agentic coding model.</p>
<p><a href="/workers-ai/models/glm-5.2/"><code>@cf/zai-org/glm-5.2</code></a> is a text generation model built for agentic coding workflows. With function calling and reasoning support, it can handle long codebases, multi-step planning, and tool-augmented agents.</p>
<p><strong>Key features and use cases:</strong></p>
<ul>
<li><strong>Agentic coding</strong>: Designed for autonomous coding tasks, long-horizon planning, and complex software engineering workflows</li>
<li><strong>Large context window</strong>: GLM-5.2 supports up to a 1,048,576 token context window. Workers AI is launching the model with a 262,144 token context window and plans to increase this in the future</li>
<li><strong>Function calling</strong>: Build agents that invoke tools and APIs across multiple conversation turns</li>
<li><strong>Reasoning</strong>: Tackles complex problem-solving and step-by-step reasoning tasks</li>
</ul>
<p>Use GLM-5.2 through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/run</code> or <code>/v1/chat/completions</code>, or <a href="/ai-gateway/">AI Gateway</a>.</p>
<p>Pricing is available on the <a href="/workers-ai/models/glm-5.2/">model page</a> or <a href="/workers-ai/platform/pricing/">pricing page</a>.</p>


<h2 id="tcp-connections-via-connect-over-vpc-networks"><a href="/changelog/post/2026-06-16-tcp-connect-vpc-networks/">TCP connections via connect() over VPC Networks</a></h2>
<p><em>2026-06-16</em></p>
<p><a href="/workers-vpc/configuration/vpc-networks/">VPC Network</a> bindings now support the <a href="/workers/runtime-apis/tcp-sockets/"><code>connect()</code></a> Socket API for raw TCP connections to private destinations, in addition to HTTP traffic via <code>fetch()</code>.</p>
<p>This means Workers can now open TCP sockets to any private service reachable through the bound Cloudflare Tunnel, Cloudflare Mesh, or Cloudflare WAN on-ramp — Redis, Memcached, MQTT, custom binary protocols, or any other TCP-based service.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17828.md")</div>
<p>At runtime, use <code>connect()</code> on the binding to open a TCP socket to a private destination:</p>
<pre><code class="language-ts">export default {&#10;	async fetch(request: Request, env: Env) {&#10;		// Open a TCP connection to a private Redis instance&#10;		const socket = await env.PRIVATE_NETWORK.connect(&quot;10.0.1.50:6379&quot;);&#10;&#10;		// Write a Redis PING command&#10;		const writer = socket.writable.getWriter();&#10;		await writer.write(new TextEncoder().encode(&quot;PING\r\n&quot;));&#10;		await writer.close();&#10;&#10;		return new Response(socket.readable);&#10;	},&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17827.md")</aside>
<p>For more details, refer to <a href="/workers-vpc/configuration/vpc-networks/">VPC Networks</a> and the <a href="/workers-vpc/api/">Workers Binding API</a>.</p>


<h2 id="view-the-user-agent-of-requests-in-ai-gateway-logs"><a href="/changelog/post/2026-06-12-user-agent-logging/">View the user agent of requests in AI Gateway logs</a></h2>
<p><em>2026-06-12</em></p>
<p>AI Gateway logs now capture the user agent of the client that made each request, making it easier to identify which SDK, library, or application sent the traffic flowing through your gateway. For example, you can tell apart requests coming from <code>openai-python</code> versus a custom application or a Cloudflare Worker.</p>
<p>The user agent appears alongside the other details in each log entry, and you can filter logs by user agent (equals, does not equal, or contains) in the dashboard.</p>
<p>For more information, refer to <a href="/ai-gateway/observability/logging/">Logging</a>.</p>


<h2 id="filter-durable-objects-metrics-by-object-id-or-name"><a href="/changelog/post/2026-06-12-durable-objects-metrics-filter-by-id-name/">Filter Durable Objects metrics by object ID or name</a></h2>
<p><em>2026-06-12</em></p>
<p>You can now filter the <strong>Metrics</strong> tab for a Durable Objects namespace by an individual Durable Object's <a href="/durable-objects/api/id/">ID</a> or <a href="/durable-objects/api/id/#name">name</a> in the Cloudflare dashboard. Previously, metrics charts only showed aggregate, namespace-level data, making it difficult to isolate the behavior of a specific object.</p>
<div class="nb-dash-button"></div>
<p><img src="/assets/upstream/images/changelog/durable-objects/durable-objects-metrics-dashboard.png" alt="The Durable Objects Metrics tab filtered to a single object by ID, showing per-object requests and errors by invocation status." /></p>
<p>Start typing an ID or name into the filter and select a match from the autocomplete dropdown. The autocomplete only shows objects with invocations during the selected time range, so an object that does not appear has not been invoked in that window. This does not necessarily mean the object has been deleted. Every chart on the page updates to reflect only the selected object. This makes it easier to identify and investigate a single Durable Object when debugging a high-traffic object, an error spike, or unexpected storage usage. Clear the filter to return to namespace-level metrics.</p>
<p>Metrics are powered by the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>, so standard analytics behavior such as ingestion delay and <a href="/analytics/faq/graphql-api-inconsistent-results/">sampling</a> applies.</p>
<p>For more information, refer to <a href="/durable-objects/observability/metrics-and-analytics/">Metrics and analytics</a>.</p>


<h2 id="terraform-v5-20-0-now-available"><a href="/changelog/post/2026-06-12-terraform-v5.20.0-provider/">Terraform v5.20.0 now available</a></h2>
<p><em>2026-06-12</em></p>
<p>Cloudflare's Terraform v5 Provider makes it easy for developers to manage their Cloudflare infrastructure using a configuration as code approach. It releases every <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774">2-3 weeks</a> to ensure that you can always manage the latest features in the platform. This week, we launched Terraform v5.20.0, which adds 24 new resources, bumps the underlying Go SDK to cloudflare-go v7, and includes a range of bug fixes and state upgraders based on community feedback.</p>
<h4 id="2026-06-12-terraform-v5.20.0-provider-new-resources">New resources</h4>
<ul>
<li><strong>cloudflare_ai_search_namespace:</strong> Manage AI Search namespaces</li>
<li><strong>cloudflare_custom_csr:</strong> Manage custom certificate signing requests</li>
<li><strong>cloudflare_dls_prefix_binding:</strong> Manage DLS regional service prefix bindings</li>
<li><strong>cloudflare_flagship_app:</strong> Manage Flagship feature flag apps</li>
<li><strong>cloudflare_flagship_flag:</strong> Manage Flagship feature flags</li>
<li><strong>cloudflare_google_tag_gateway:</strong> Manage Google Tag Gateway</li>
<li><strong>cloudflare_load_balancer_monitor_group:</strong> Manage load balancer monitor groups</li>
<li><strong>cloudflare_oauth_client:</strong> Manage IAM OAuth clients</li>
<li><strong>cloudflare_origin_cloud_region:</strong> Manage origin cloud regions (v2 endpoints)</li>
<li><strong>cloudflare_secrets_store:</strong> Manage Secrets Store instances</li>
<li><strong>cloudflare_secrets_store_secret:</strong> Manage Secrets Store secrets</li>
<li><strong>cloudflare_share:</strong> Manage resource shares</li>
<li><strong>cloudflare_share_recipient:</strong> Manage share recipients</li>
<li><strong>cloudflare_share_resource:</strong> Manage shared resources</li>
<li><strong>cloudflare_zero_trust_device_deployment_groups:</strong> Manage Zero Trust device deployment groups</li>
<li><strong>cloudflare_zero_trust_dlp_data_class:</strong> Manage DLP data classes</li>
<li><strong>cloudflare_zero_trust_dlp_data_tag:</strong> Manage DLP data tags</li>
<li><strong>cloudflare_zero_trust_dlp_data_tag_category:</strong> Manage DLP data tag categories</li>
<li><strong>cloudflare_zero_trust_dlp_sensitivity_group:</strong> Manage DLP sensitivity groups</li>
<li><strong>cloudflare_zero_trust_dlp_sensitivity_level:</strong> Manage DLP sensitivity levels</li>
<li><strong>cloudflare_zero_trust_dlp_sensitivity_level_order:</strong> Manage DLP sensitivity level ordering</li>
<li><strong>cloudflare_zero_trust_resource_library_application:</strong> Manage Zero Trust resource library applications</li>
<li><strong>cloudflare_zero_trust_resource_library_category:</strong> Manage Zero Trust resource library categories</li>
<li><strong>cloudflare_zero_trust_tunnel_warp_connector_config:</strong> Manage WARP connector tunnel configurations</li>
</ul>
<h4 id="2026-06-12-terraform-v5.20.0-provider-features">Features</h4>
<ul>
<li><strong>cache:</strong> add create (POST) method for smart_tiered_cache</li>
<li><strong>cache:</strong> update OPCR config to v2 endpoints</li>
<li><strong>dlp:</strong> promote classification Stainless config to main</li>
<li><strong>dlp:</strong> add custom prompt topics endpoint</li>
<li><strong>email_security_block_sender:</strong> state upgrader for v4 to v5 migration</li>
<li><strong>email_security_impersonation_registry:</strong> state upgrader for v4 to v5 migration</li>
<li><strong>email_security_trusted_domains:</strong> state upgrader for v4 to v5 migration</li>
<li><strong>snippets:</strong> add Terraform <code>id_property</code> annotations for snippet and snippet_rules</li>
<li>bump Go SDK to cloudflare-go v7</li>
</ul>
<h4 id="2026-06-12-terraform-v5.20.0-provider-bug-fixes">Bug fixes</h4>
<ul>
<li><strong>account_member:</strong> missing upgrade path from v5.0–v5.15</li>
<li><strong>authenticated_origin_pulls_settings:</strong> nil pointer panic</li>
<li><strong>bot_management:</strong> restore <code>content_bots_protection</code> handling in model.go</li>
<li><strong>dns_record:</strong> prevent FQDN normalization from swallowing name shortening changes</li>
<li><strong>list:</strong> nullify empty nested objects to prevent inconsistent result after apply</li>
<li><strong>load_balancer_pool:</strong> accept early-v5 object-shape state at schema_version=0</li>
<li><strong>load_balancer_pool:</strong> add <code>UseStateForUnknown</code> for <code>load_shedding</code> attribute to prevent drift</li>
<li><strong>r2_custom_domain:</strong> restore degraded-response handling in resource.go</li>
<li><strong>regional_hostname:</strong> update cloudflare-go imports from v6 to v7</li>
<li><strong>secrets_store:</strong> fix model/schema parity and guard acceptance tests</li>
<li><strong>spectrum_application:</strong> accept early-v5 object-shape state at schema_version=0</li>
<li><strong>worker:</strong> preserve <code>observability.traces.propagation_policy</code> across reads</li>
<li><strong>worker:</strong> add <code>propagation_policy</code> to observability defaults</li>
<li><strong>worker_version:</strong> restore handwritten D1 <code>database_id</code> handling</li>
<li><strong>workers_custom_domain:</strong> missing <code>CertId</code> field in state migration</li>
<li><strong>workers_script:</strong> restore annotations Read workaround stripped by codegen</li>
<li><strong>zero_trust_access_identity_provider:</strong> change <code>read_only</code> from computed to optional</li>
<li><strong>zero_trust_access_identity_provider:</strong> add <code>UseStateForUnknown</code> to SAML-only config fields</li>
<li><strong>zero_trust_access_identity_provider:</strong> use <code>UseNonNullStateForUnknown</code> on scim_config fields</li>
<li><strong>zero_trust_access_policy:</strong> populate <code>account_id</code> when migrating zone-scoped v4 state</li>
<li><strong>zero_trust_access_policy:</strong> missing <code>common_names</code> transform in migration</li>
<li>gracefully handle nil pointer dereference when config has <code>attributes_flat</code> during migration</li>
<li>set initial schema version to 500 for all new resources</li>
</ul>
<h4 id="2026-06-12-terraform-v5.20.0-provider-refactors">Refactors</h4>
<p>Extracted <code>MoveState</code> nil guard into shared helper</p>
<h4 id="2026-06-12-terraform-v5.20.0-provider-for-more-information">For more information</h4>
- [Terraform Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Version 5 Migration Guide](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-migration)
- [Documentation on using Terraform with Cloudflare](/terraform/)
- [List of stabilized resources](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237)


<h2 id="moonshot-ai-kimi-k2-7-code-now-available-on-workers-ai"><a href="/changelog/post/2026-06-12-kimi-k2-7-code-workers-ai/">Moonshot AI Kimi K2.7 Code now available on Workers AI</a></h2>
<p><em>2026-06-12</em></p>
<p><a href="/workers-ai/models/kimi-k2.7-code/"><code>@cf/moonshotai/kimi-k2.7-code</code></a> is now available on Workers AI. Kimi K2.7 Code is a code-optimized variant of the Kimi K2 family, built on a Mixture-of-Experts architecture with 1T total parameters and 32B active per token.</p>
<h4 id="2026-06-12-kimi-k2-7-code-workers-ai-improved-coding-and-agent-performance">Improved coding and agent performance</h4>
<p>K2.7 Code delivers meaningful gains over K2.6 on coding and agentic benchmarks:</p>
<ul>
<li><strong>+21.8%</strong> on Kimi Code Bench v2</li>
<li><strong>+11.0%</strong> on Program Bench</li>
<li><strong>+31.5%</strong> on MLS Bench Lite</li>
</ul>
<h4 id="2026-06-12-kimi-k2-7-code-workers-ai-reasoning-efficiency">Reasoning efficiency</h4>
<p>K2.7 Code uses 30% fewer reasoning tokens compared to K2.6, reducing overthinking and lowering inference cost for reasoning-heavy workloads.</p>
<h4 id="2026-06-12-kimi-k2-7-code-workers-ai-key-capabilities">Key capabilities</h4>
<ul>
<li><strong>262.1k token context window</strong> for retaining full conversation history, tool definitions, and codebases across long-running agent sessions</li>
<li><strong>Long-horizon coding</strong> with improved instruction following and higher end-to-end coding task success rates</li>
<li><strong>Vision inputs</strong> for processing images alongside text</li>
<li><strong>Thinking mode</strong> with configurable reasoning depth via <code>chat_template_kwargs.thinking</code></li>
<li><strong>Multi-turn tool calling</strong> for building agents that invoke tools across multiple conversation turns</li>
<li><strong>Structured outputs</strong> with JSON schema support</li>
</ul>
<h4 id="2026-06-12-kimi-k2-7-code-workers-ai-differences-from-kimi-k2-6">Differences from Kimi K2.6</h4>
<p>If you are migrating from Kimi K2.6, note the following:</p>
<ul>
<li>K2.7 Code is optimized for coding tasks with improved benchmark performance and reasoning efficiency</li>
<li>Cached input token pricing is $0.19 per M tokens (vs $0.16 for K2.6)</li>
<li>API usage is identical — no parameter changes required</li>
</ul>
<h4 id="2026-06-12-kimi-k2-7-code-workers-ai-get-started">Get started</h4>
<p>Use Kimi K2.7 Code through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/ai/run</code>, or the OpenAI-compatible endpoint at <code>/v1/chat/completions</code>. You can also use <a href="/ai-gateway/">AI Gateway</a> with any of these endpoints.</p>
<p>For more information, refer to the <a href="/workers-ai/models/kimi-k2.7-code/">Kimi K2.7 Code model page</a> and <a href="/workers-ai/platform/pricing/">pricing</a>.</p>


<h2 id="new-formats-parameter-for-the-browser-run-snapshot-endpoint"><a href="/changelog/post/2026-06-11-browser-run-snapshot-formats/">New formats parameter for the Browser Run /snapshot endpoint</a></h2>
<p><em>2026-06-11</em></p>
<p><a href="/browser-run/">Browser Run</a>'s <a href="/browser-run/quick-actions/snapshot/"><code>/snapshot</code> endpoint</a> now supports a <code>formats</code> parameter that lets you return multiple page formats in a single API call. Previously, <code>/snapshot</code> returned only HTML content and a screenshot. You can now also include Markdown and the accessibility tree in the same response.</p>
<p>These formats are particularly useful for AI agent workflows:</p>
<ul>
<li>Markdown provides a token-efficient representation of page content that LLMs can process directly, without parsing HTML markup.</li>
<li>The accessibility tree provides a structured representation of a page's elements, including roles, labels, and hierarchy, helping LLMs understand page structure and navigate its contents.</li>
</ul>
<p>The following example returns a screenshot, Markdown, and the accessibility tree in one call:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17699.md")
</div></div>
<p>You must request at least two formats. If you only need one, use the respective single-format endpoint such as <a href="/browser-run/quick-actions/screenshot-endpoint/"><code>/screenshot</code></a> or <a href="/browser-run/quick-actions/markdown-endpoint/"><code>/markdown</code></a>.</p>
<p>Refer to the <a href="/browser-run/quick-actions/snapshot/"><code>/snapshot</code> documentation</a> for the full list of accepted values.</p>


<h2 id="track-dynamic-workers-usage-from-the-dashboard-and-graphql-api"><a href="/changelog/post/2026-06-11-dynamic-workers-count/">Track Dynamic Workers usage from the dashboard and GraphQL API</a></h2>
<p><em>2026-06-11</em></p>
<p><img src="/assets/upstream/images/workers/changelog/dynamic-workers-count.png" alt="Dynamic Workers usage on the Workers overview page" /></p>
<p>Customers can now view the number of <a href="/dynamic-workers/">Dynamic Workers</a> invoked during their billing period from the Workers overview page in the Cloudflare dashboard.</p>
<p>This count reflects the number of Dynamic Workers that Cloudflare would bill for during the selected billing period. Dynamic Workers usage data only goes back to June 1, 2026.</p>
<p>You can also query this count through the <a href="/analytics/graphql-api/">GraphQL Analytics API</a> by using <code>workersInvocationsByOwnerAndScriptGroups</code> and selecting <code>distinctDynamicWorkerCount</code>:</p>
<pre><code class="language-graphql">query getDynamicWorkersCount(&#10;	$accountTag: string!&#10;	$filter: AccountWorkersInvocationsByOwnerAndScriptGroupsFilter_InputObject&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			workersInvocationsByOwnerAndScriptGroups(limit: 10000, filter: $filter) {&#10;				uniq {&#10;					distinctDynamicWorkerCount&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Use variables to set the account and billing-period date range:</p>
<pre><code class="language-json">{&#10;	&quot;accountTag&quot;: &quot;&lt;ACCOUNT_ID&gt;&quot;,&#10;	&quot;filter&quot;: {&#10;		&quot;date_geq&quot;: &quot;2026-06-01&quot;,&#10;		&quot;date_leq&quot;: &quot;2026-06-30&quot;&#10;	}&#10;}&#10;</code></pre>
<p>For more information, refer to <a href="/dynamic-workers/pricing/">Dynamic Workers pricing</a>.</p>


<h2 id="manage-ai-search-namespaces-with-wrangler-cli"><a href="/changelog/post/2026-06-10-ai-search-namespace-wrangler-commands/">Manage AI Search namespaces with Wrangler CLI</a></h2>
<p><em>2026-06-10</em></p>
<p><a href="/ai-search/">AI Search</a> now supports namespace-level Wrangler commands, making it easier to manage <a href="/ai-search/concepts/namespaces/">namespaces</a> from your terminal, scripts, and agent workflows.</p>
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
<td><code>wrangler ai-search namespace list</code></td>
<td>List AI Search namespaces</td>
</tr>
<tr>
<td><code>wrangler ai-search namespace create</code></td>
<td>Create a new AI Search namespace</td>
</tr>
<tr>
<td><code>wrangler ai-search namespace get</code></td>
<td>Get details for a namespace</td>
</tr>
<tr>
<td><code>wrangler ai-search namespace update</code></td>
<td>Update a namespace description</td>
</tr>
<tr>
<td><code>wrangler ai-search namespace delete</code></td>
<td>Delete an AI Search namespace</td>
</tr>
</tbody>
</table>
<p>Create a namespace for a new application or tenant directly from the CLI:</p>
<pre><code class="language-sh">wrangler ai-search namespace create docs-production --description &quot;Production documentation search&quot;&#10;</code></pre>
<p>List namespaces with pagination or filter by name or description:</p>
<pre><code class="language-sh">wrangler ai-search namespace list --search docs --page 1 --per-page 10&#10;</code></pre>
<p>Use <code>--json</code> with <code>list</code>, <code>create</code>, <code>get</code>, and <code>update</code> to return structured output that automation and AI agents can parse directly.</p>
<p>Instance-level commands also now support a <code>--namespace</code> flag, so you can interact with instances inside a specific namespace from the CLI:</p>
<pre><code class="language-sh">wrangler ai-search list --namespace docs-production&#10;</code></pre>
<p>For full usage details, refer to the <a href="/ai-search/wrangler-commands/">AI Search Wrangler commands documentation</a>.</p>


<h2 id="flagship-api-reference-now-available"><a href="/changelog/post/2026-06-10-api-reference/">Flagship API reference now available</a></h2>
<p><em>2026-06-10</em></p>
<p>The <strong><a href="/api/resources/flagship/">Flagship API reference</a></strong> is now available. You can use the Cloudflare API to create and update apps, and to create, update, delete, and list feature flags without using the dashboard.</p>
<p>For example, create a new boolean flag with the API:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/flagship/apps/$APP_ID/flags \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;key&quot;: &quot;new-checkout&quot;,&#10;    &quot;enabled&quot;: true,&#10;    &quot;default_variation&quot;: &quot;off&quot;,&#10;    &quot;variations&quot;: {&#10;      &quot;off&quot;: false,&#10;      &quot;on&quot;: true&#10;    },&#10;    &quot;rules&quot;: []&#10;  }&#x27;&#10;</code></pre>
<p>To create an API token, go to <a href="https://dash.cloudflare.com/?to=/:account/api-tokens">Account API Tokens</a> in the Cloudflare dashboard and search for Flagship.</p>
<p>The API reference includes endpoints for Flagship apps, flags, changelog entries, and flag evaluation. Agents can also use the <a href="https://github.com/cloudflare/skills/tree/main/skills/cloudflare/references/flagship">Flagship reference in the Cloudflare skill</a> to create and manage Flagship resources.</p>
<p>Refer to the <a href="/flagship/">Flagship documentation</a> to learn more about evaluating feature flags from your applications.</p>


<h2 id="manage-hosted-images-with-the-images-binding"><a href="/changelog/post/2026-06-10-hosted-images-binding/">Manage hosted images with the Images binding</a></h2>
<p><em>2026-06-10</em></p>
<p>Use the Images binding to upload, list, retrieve, update, and delete images stored in Images directly from your Worker without managing API tokens or making HTTP requests.</p>
<p>The <code>env.IMAGES.hosted</code> namespace supports the following storage and management operations:</p>
<ul>
<li><a href="/images/storage/binding/#uploadimage-options"><code>.upload(image, options)</code></a> — Upload a new image to your account.</li>
<li><a href="/images/storage/binding/#listoptions"><code>.list(options)</code></a> — List images with pagination.</li>
<li><a href="/images/storage/binding/#imageimageiddetails"><code>.image(imageId).details()</code></a> — Get image metadata.</li>
<li><a href="/images/storage/binding/#imageimageidbytes"><code>.image(imageId).bytes()</code></a> — Stream the original image bytes.</li>
<li><a href="/images/storage/binding/#imageimageidupdateoptions"><code>.image(imageId).update(options)</code></a> — Update metadata or access controls.</li>
<li><a href="/images/storage/binding/#imageimageiddelete"><code>.image(imageId).delete()</code></a> — Delete an image.</li>
</ul>
<p>For example, you can upload an image from a request body and return its metadata:</p>
<pre><code class="language-ts">const image = await env.IMAGES.hosted.upload(request.body, {&#10;	filename: &quot;upload.jpg&quot;,&#10;	metadata: { source: &quot;worker&quot; },&#10;});&#10;&#10;return Response.json(image);&#10;</code></pre>
<p>Or retrieve and serve the original bytes of a hosted image:</p>
<pre><code class="language-ts">const bytes = await env.IMAGES.hosted.image(&quot;IMAGE_ID&quot;).bytes();&#10;return new Response(bytes);&#10;</code></pre>
<p>For more information, refer to the <a href="/images/storage/binding/">Images binding</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/developer-platform/5/">Previous</a><span>Page 6 of 23</span><a class="pagination-next" rel="next" href="/changelog/product-group/developer-platform/7/">Next</a></nav>
