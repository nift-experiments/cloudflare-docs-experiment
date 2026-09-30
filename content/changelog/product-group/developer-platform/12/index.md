<h1 id="changelog">Changelog</h1>

<h2 id="agents-sdk-v0-6-0-rpc-transport-for-mcp-optional-oauth-hardened-schema-conversion-and-cloudflare-ai-chat-fixes"><a href="/changelog/post/2026-02-25-agents-sdk-v0.6.0/">Agents SDK v0.6.0: RPC transport for MCP, optional OAuth, hardened schema conversion, and @cloudflare/ai-chat fixes</a></h2>
<p><em>2026-02-25</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> lets you define an Agent and an McpAgent in the same Worker and connect them over RPC — no HTTP, no network overhead. It also makes OAuth opt-in for simple MCP connections, hardens the schema converter for production workloads, and ships a batch of <code>@cloudflare/ai-chat</code> reliability fixes.</p>
<h4 id="2026-02-25-agents-sdk-v0.6.0-rpc-transport-for-mcp">RPC transport for MCP</h4>
<p>You can now connect an Agent to an McpAgent in the same Worker using a Durable Object binding instead of an HTTP URL. The connection stays entirely within the Cloudflare runtime — no network round-trips, no serialization overhead.</p>
<p>Pass the Durable Object namespace directly to <code>addMcpServer</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17642.md")</div>
<p>The <code>addMcpServer</code> method now accepts <code>string | DurableObjectNamespace</code> as the second parameter with full TypeScript overloads, so HTTP and RPC paths are type-safe and cannot be mixed.</p>
<p>Key capabilities:</p>
<ul>
<li><strong>Hibernation support</strong> — RPC connections survive Durable Object hibernation automatically. The binding name and props are persisted to storage and restored on wake-up, matching the behavior of HTTP MCP connections.</li>
<li><strong>Deduplication</strong> — Calling <code>addMcpServer</code> with the same server name returns the existing connection instead of creating duplicates. Connection IDs are stable across hibernation restore.</li>
<li><strong>Smaller surface area</strong> — The RPC transport internals have been rewritten and reduced from 609 lines to 245 lines. <code>RPCServerTransport</code> now uses <code>JSONRPCMessageSchema</code> from the MCP SDK for validation instead of hand-written checks.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17641.md")</aside>
<h4 id="2026-02-25-agents-sdk-v0.6.0-optional-oauth-for-mcp-connections">Optional OAuth for MCP connections</h4>
<p><code>addMcpServer()</code> no longer eagerly creates an OAuth provider for every connection. For servers that do not require authentication, a simple call is all you need:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17643.md")</div>
<p>If the server responds with a 401, the SDK throws a clear error: <code>&quot;This MCP server requires OAuth authentication. Provide callbackHost in addMcpServer options to enable the OAuth flow.&quot;</code> The restore-from-storage flow also handles missing callback URLs gracefully, skipping auth provider creation for non-OAuth servers.</p>
<h4 id="2026-02-25-agents-sdk-v0.6.0-hardened-json-schema-to-typescript-converter">Hardened JSON Schema to TypeScript converter</h4>
<p>The schema converter used by <code>generateTypes()</code> and <code>getAITools()</code> now handles edge cases that previously caused crashes in production:</p>
<ul>
<li><strong>Depth and circular reference guards</strong> — Prevents stack overflows on recursive or deeply nested schemas</li>
<li><strong><code>$ref</code> resolution</strong> — Supports internal JSON Pointers (<code>#/definitions/...</code>, <code>#/$defs/...</code>, <code>#</code>)</li>
<li><strong>Tuple support</strong> — <code>prefixItems</code> (JSON Schema 2020-12) and array <code>items</code> (draft-07)</li>
<li><strong>OpenAPI 3.0 <code>nullable: true</code></strong> — Supported across all schema branches</li>
<li><strong>Per-tool error isolation</strong> — One malformed schema cannot crash the full pipeline in <code>generateTypes()</code> or <code>getAITools()</code></li>
<li><strong>Missing <code>inputSchema</code> fallback</strong> — <code>getAITools()</code> falls back to <code>{ type: &quot;object&quot; }</code> instead of throwing</li>
</ul>
<h4 id="2026-02-25-agents-sdk-v0.6.0-cloudflare-ai-chat-fixes"><code>@cloudflare/ai-chat</code> fixes</h4>
<ul>
<li><strong>Tool denial flow</strong> — Denied tool approvals (<code>approved: false</code>) now transition to <code>output-denied</code> with a <code>tool_result</code>, fixing Anthropic provider compatibility. Custom denial messages are supported via <code>state: &quot;output-error&quot;</code> and <code>errorText</code>.</li>
<li><strong>Abort/cancel support</strong> — Streaming responses now properly cancel the reader loop when the abort signal fires and send a done signal to the client.</li>
<li><strong>Duplicate message persistence</strong> — <code>persistMessages()</code> now reconciles assistant messages by content and order, preventing duplicate rows when clients resend full history.</li>
<li><strong><code>requestId</code> in <code>OnChatMessageOptions</code></strong> — Handlers can now send properly-tagged error responses for pre-stream failures.</li>
<li><strong><code>redacted_thinking</code> preservation</strong> — The message sanitizer no longer strips Anthropic <code>redacted_thinking</code> blocks.</li>
<li><strong><code>/get-messages</code> reliability</strong> — Endpoint handling moved from a prototype <code>onRequest()</code> override to a constructor wrapper, so it works even when users override <code>onRequest</code> without calling <code>super.onRequest()</code>.</li>
<li><strong>Client tool APIs undeprecated</strong> — <code>createToolsFromClientSchemas</code>, <code>clientTools</code>, <code>AITool</code>, <code>extractClientToolSchemas</code>, and the <code>tools</code> option on <code>useAgentChat</code> are restored for SDK use cases where tools are defined dynamically at runtime.</li>
<li><strong><code>jsonSchema</code> initialization</strong> — Fixed <code>jsonSchema not initialized</code> error when calling <code>getAITools()</code> in <code>onChatMessage</code>.</li>
</ul>
<h4 id="2026-02-25-agents-sdk-v0.6.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest&#10;</code></pre>


<h2 id="run-15x-more-containers-with-higher-resource-limits"><a href="/changelog/post/2026-02-25-higher-container-resource-limits/">Run 15x more Containers with higher resource limits</a></h2>
<p><em>2026-02-25</em></p>
<p>You can now run more <a href="/containers/">Containers</a> concurrently with significantly higher limits on memory, vCPU, and disk.</p>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Previous Limit</th>
<th>New Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Memory for concurrent live Container instances</td>
<td>400GiB</td>
<td>6TiB</td>
</tr>
<tr>
<td>vCPU for concurrent live Container instances</td>
<td>100</td>
<td>1,500</td>
</tr>
<tr>
<td>Disk for concurrent live Container instances</td>
<td>2TB</td>
<td>30TB</td>
</tr>
</tbody>
</table>
<p>This 15x increase enables larger-scale workloads on Containers. You can now run 15,000 instances of the <code>lite</code> instance type, 6,000 instances of <code>basic</code>, over 1,500 instances of <code>standard-1</code>, or over 1,000 instances of <code>standard-2</code> concurrently.</p>
<p>Refer to <a href="/containers/platform/limits/">Limits</a> for more details on the available instance types and limits.</p>


<h2 id="better-windows-support-for-python-workers"><a href="/changelog/post/2026-02-13-pywrangler-windows-support/">Better Windows support for Python Workers</a></h2>
<p><em>2026-02-25</em></p>
<p><a href="https://github.com/cloudflare/workers-py?tab=readme-ov-file#pywrangler">Pywrangler</a>, the CLI tool for managing Python Workers and packages,
now supports Windows, allowing you to develop and deploy Python Workers from Windows environments.
Previously, Pywrangler was only available on macOS and Linux.</p>
<p>You can install and use Pywrangler on Windows the same way you would on other platforms.
<a href="/workers/languages/python/packages/">Specify your Worker's Python dependencies</a> in your <code>pyproject.toml</code> file,
then use the following commands to develop and deploy:</p>
<pre><code class="language-bash">uvx --from workers-py pywrangler dev&#10;uvx --from workers-py pywrangler deploy&#10;</code></pre>
<p>All existing Pywrangler functionality, including package management, local development, and deployment, works on Windows without any additional configuration.</p>
<h4 id="2026-02-13-pywrangler-windows-support-requirements">Requirements</h4>
<p>This feature requires the following minimum versions:</p>
<ul>
<li><code>wrangler</code> &gt;= 4.64.0</li>
<li><code>workers-py</code> &gt;= 1.72.0</li>
<li><code>uv</code> &gt;= 0.29.8</li>
</ul>
<p>To upgrade <code>workers-py</code> (which includes Pywrangler) in your project, run:</p>
<pre><code class="language-bash">uv tool upgrade workers-py&#10;</code></pre>
<p>To upgrade <code>wrangler</code>, run:</p>
<pre><code class="language-bash">npm install -g wrangler@latest&#10;</code></pre>
<p>To upgrade <code>uv</code>, run:</p>
<pre><code class="language-bash">uv self update&#10;</code></pre>
<p>To get started with Python Workers on Windows, refer to the <a href="/workers/languages/python/packages/">Python packages documentation</a> for full details on Pywrangler.</p>


<h2 id="write-structured-queries-to-filter-and-search-your-workers-logs-and-traces"><a href="/changelog/post/2026-02-24-observability-query-language/">Write structured queries to filter and search your Workers logs and traces</a></h2>
<p><em>2026-02-25</em></p>
<p><a href="/workers/observability/">Workers Observability</a> now includes a query language that lets you write structured queries directly in the search bar to filter your logs and traces. The search bar doubles as a free text search box — type any term to search across all metadata and attributes, or write field-level queries for precise filtering.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2026-02-24-query-language.png" alt="Workers Observability search bar with autocomplete suggestions and Query Builder sidebar filters" /></p>
<p>Queries written in the search bar sync with the <a href="/workers/observability/">Query Builder</a> sidebar, so you can write a query by hand and then refine it visually, or build filters in the Query Builder and see the corresponding query syntax. The search bar provides autocomplete suggestions for metadata fields and operators as you type.</p>
<p>The query language supports:</p>
<ul>
<li><strong>Free text search</strong> — search everywhere with a keyword like <code>error</code>, or match an exact phrase with <code>&quot;exact phrase&quot;</code></li>
<li><strong>Field queries</strong> — filter by specific fields using comparison operators (for example, <code>status = 500</code> or <code>$workers.wallTimeMs &gt; 100</code>)</li>
<li><strong>Operators</strong> — <code>=</code>, <code>!=</code>, <code>&gt;</code>, <code>&gt;=</code>, <code>&lt;</code>, <code>&lt;=</code>, and <code>:</code> (contains)</li>
<li><strong>Functions</strong> — <code>contains(field, value)</code>, <code>startsWith(field, prefix)</code>, <code>regex(field, pattern)</code>, and <code>exists(field)</code></li>
<li><strong>Boolean logic</strong> — add conditions with <code>AND</code>, <code>OR</code>, and <code>NOT</code></li>
</ul>
<p>Select the help icon next to the search bar to view the full syntax reference, including all supported operators, functions, and keyboard shortcuts.</p>
<p>Go to the <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/">Workers Observability dashboard</a> to try the query language.</p>


<h2 id="no-config-no-problem-just-wrangler-deploy"><a href="/changelog/post/2026-02-25-wrangler-autoconfig-ga/">No config? No problem. Just `wrangler deploy`</a></h2>
<p><em>2026-02-25</em></p>
<p>You can now deploy any existing project to Cloudflare Workers — even without a Wrangler configuration file — and <code>wrangler deploy</code> will <em>just work</em>.</p>
<p>Starting with Wrangler <strong>4.68.0</strong>, running <a href="/workers/wrangler/commands/general/#deploy"><code>wrangler deploy</code></a> <a href="/workers/framework-guides/automatic-configuration/">automatically configures your project</a> by detecting your framework, installing required adapters, and deploying it to Cloudflare Workers.</p>
<h4 id="2026-02-25-wrangler-autoconfig-ga-using-wrangler-locally">Using Wrangler locally</h4>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<p>When you run <code>wrangler deploy</code> in a project without a configuration file, Wrangler:</p>
<ol>
<li>Detects your framework from <code>package.json</code></li>
<li>Prompts you to confirm the detected settings</li>
<li>Installs any required adapters</li>
<li>Generates a <code>wrangler.jsonc</code> <a href="/workers/wrangler/configuration/">configuration file</a></li>
<li>Deploys your project to Cloudflare Workers</li>
</ol>
<p>You can also use <a href="/workers/wrangler/commands/general/#setup"><code>wrangler setup</code></a> to configure without deploying, or pass <a href="/workers/wrangler/commands/general/#deploy"><code>--yes</code></a> to skip prompts.</p>
<h4 id="2026-02-25-wrangler-autoconfig-ga-using-the-cloudflare-dashboard">Using the Cloudflare dashboard</h4>
<p><img src="/assets/upstream/images/workers/ci-cd/builds/automatic-pr.png" alt="Automatic configuration pull request created by Workers Builds" /></p>
<p>When you connect a repository through the <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/create">Workers dashboard</a>, a <a href="/workers/ci-cd/builds/automatic-prs/">pull request is generated</a> for you with all necessary files, and a <a href="/workers/versions-and-deployments/preview-urls/">preview deployment</a> to check before merging.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17800.md")</aside>
<h4 id="2026-02-25-wrangler-autoconfig-ga-background">Background</h4>
<p>In December 2025, we <a href="/changelog/2025-12-16-wrangler-autoconfig/">introduced automatic configuration</a> as an experimental feature. It is now generally available and the default behavior.</p>
<p>If you have questions or run into issues, join the <a href="https://github.com/cloudflare/workers-sdk/discussions/11667">GitHub discussion</a>.</p>


<h2 id="deleteall-now-deletes-durable-object-alarm"><a href="/changelog/post/2026-02-24-deleteall-deletes-alarms/">deleteAll() now deletes Durable Object alarm</a></h2>
<p><em>2026-02-24</em></p>
<p><code>deleteAll()</code> now deletes a Durable Object alarm in addition to stored data for Workers with a compatibility date of <code>2026-02-24</code> or later. This change simplifies clearing a Durable Object's storage with a single API call.</p>
<p>Previously, <code>deleteAll()</code> only deleted user-stored data for an object. Alarm usage stores metadata in an object's storage, which required a separate <code>deleteAlarm()</code> call to fully clean up all storage for an object. The <code>deleteAll()</code> change applies to both KV-backed and SQLite-backed Durable Objects.</p>
<pre><code class="language-js">// Before: two API calls required to clear all storage&#10;await this.ctx.storage.deleteAlarm();&#10;await this.ctx.storage.deleteAll();&#10;&#10;// Now: a single call clears both data and the alarm&#10;await this.ctx.storage.deleteAll();&#10;</code></pre>
<p>For more information, refer to the <a href="/durable-objects/api/sqlite-storage-api/#deleteall">Storage API documentation</a>.</p>


<h2 id="dropped-event-metrics-typed-pipelines-bindings-and-improved-setup"><a href="/changelog/post/2026-02-24-typed-bindings-setup-improvements-error-metrics/">Dropped event metrics, typed Pipelines bindings, and improved setup</a></h2>
<p><em>2026-02-24</em></p>
<p><a href="/pipelines/">Cloudflare Pipelines</a> ingests streaming data via <a href="/workers/">Workers</a> or HTTP endpoints, transforms it with SQL, and writes it to <a href="/r2/">R2</a> as Apache Iceberg tables. Today we're shipping three improvements to help you understand why streaming events get dropped, catch data quality issues early, and set up Pipelines faster.</p>
<h4 id="2026-02-24-typed-bindings-setup-improvements-error-metrics-dropped-event-metrics">Dropped event metrics</h4>
<p>When <a href="/pipelines/streams/">stream</a> events don't match the expected schema, Pipelines accepts them during ingestion but drops them when attempting to deliver them to the <a href="/pipelines/sinks/">sink</a>. To help you identify the root cause of these issues, we are introducing a new dashboard and metrics that surface dropped events with detailed error messages.</p>
<p><img src="/assets/upstream/images/pipelines/pipelines-error-log-dash.png" alt="The Errors tab in the Cloudflare dashboard showing deserialization errors grouped by type with individual error details" /></p>
<p>Dropped events can also be queried programmatically via the new <code>pipelinesUserErrorsAdaptiveGroups</code> GraphQL dataset. The dataset breaks down failures by specific error type (<code>missing_field</code>, <code>type_mismatch</code>, <code>parse_failure</code>, or <code>null_value</code>) so you can trace issues back to the source.</p>
<pre><code class="language-graphql">query GetPipelineUserErrors(&#10;	$accountTag: String!&#10;	$pipelineId: String!&#10;	$datetimeStart: Time!&#10;	$datetimeEnd: Time!&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			pipelinesUserErrorsAdaptiveGroups(&#10;				limit: 100&#10;				filter: {&#10;					pipelineId: $pipelineId&#10;					datetime_geq: $datetimeStart&#10;					datetime_leq: $datetimeEnd&#10;				}&#10;				orderBy: [count_DESC]&#10;			) {&#10;				count&#10;				dimensions {&#10;					errorFamily&#10;					errorType&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>For the full list of dimensions, error types, and additional query examples, refer to <a href="/pipelines/observability/metrics/#user-error-metrics">User error metrics</a>.</p>
<h4 id="2026-02-24-typed-bindings-setup-improvements-error-metrics-typed-pipelines-bindings">Typed Pipelines bindings</h4>
<p>Sending data to a Pipeline from a Worker previously used a generic <code>Pipeline&lt;PipelineRecord&gt;</code> type, which meant schema mismatches (wrong field names, incorrect types) were only caught at runtime as dropped events.</p>
<p>Running <code>wrangler types</code> now generates schema-specific TypeScript types for your <a href="/pipelines/streams/writing-to-streams/#send-via-workers">Pipeline bindings</a>. TypeScript catches missing required fields and incorrect field types at compile time, before your code is deployed.</p>
<pre><code class="language-ts">declare namespace Cloudflare {&#10;	type EcommerceStreamRecord = {&#10;		user_id: string;&#10;		event_type: string;&#10;		product_id?: string;&#10;		amount?: number;&#10;	};&#10;	interface Env {&#10;		STREAM: import(&quot;cloudflare:pipelines&quot;).Pipeline&lt;Cloudflare.EcommerceStreamRecord&gt;;&#10;	}&#10;}&#10;</code></pre>
<p>For more information, refer to <a href="/pipelines/streams/writing-to-streams/#typed-pipeline-bindings">Typed Pipeline bindings</a>.</p>
<h4 id="2026-02-24-typed-bindings-setup-improvements-error-metrics-improved-pipelines-setup">Improved Pipelines setup</h4>
<p>Setting up a new Pipeline previously required multiple manual steps: creating an R2 bucket, enabling R2 Data Catalog, generating an API token, and configuring format, compression, and rolling policies individually.</p>
<p>The <code>wrangler pipelines setup</code> command now offers a <strong>Simple</strong> setup mode that applies recommended defaults and automatically creates the <a href="/r2/buckets/">R2 bucket</a> and enables <a href="/r2-data-catalog/">R2 Data Catalog</a> if they do not already exist. Validation errors during setup prompt you to retry inline rather than restarting the entire process.</p>
<p>For a full walkthrough, refer to the <a href="/pipelines/getting-started/">Getting started guide</a>.</p>


<h2 id="stream-live-inputs-can-now-be-disabled-and-enabled"><a href="/changelog/post/2026-02-24-disable-live-inputs/">Stream live inputs can now be disabled and enabled</a></h2>
<p><em>2026-02-24</em></p>
<p>You can now disable a live input to reject incoming RTMPS and SRT
connections. When a live input is disabled, any broadcast attempts will fail to
connect.</p>
<p>This gives you more control over your live inputs:</p>
<ul>
<li>Temporarily pause an input without deleting it</li>
<li>Programmatically end creator broadcasts</li>
<li>Prevent new broadcasts from starting on a specific input</li>
</ul>
<p>To disable a live input via the API, set the <code>enabled</code> property to <code>false</code>:</p>
<pre><code class="language-bash">curl --request PUT \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/live_inputs/{input_id} \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-data &#x27;{&quot;enabled&quot;: false}&#x27;&#10;</code></pre>
<p>You can also disable or enable a live input from the <strong>Live inputs</strong> list page
or the live input detail page in the Dashboard.</p>
<p>All existing live inputs remain enabled by default. For more information, refer
to <a href="/stream/stream-live/start-stream-live/">Start a live stream</a>.</p>


<h2 id="backup-and-restore-api-for-sandbox-sdk"><a href="/changelog/post/2026-02-23-sandbox-backup-restore-api/">Backup and restore API for Sandbox SDK</a></h2>
<p><em>2026-02-23</em></p>
<p><a href="/sandbox/">Sandboxes</a> now support <code>createBackup()</code> and <code>restoreBackup()</code> methods for creating and restoring point-in-time snapshots of directories.</p>
<p>This allows you to restore environments quickly. For instance, in order to develop in a sandbox, you may need to include a user's codebase and run a build step.
Unfortunately <code>git clone</code> and <code>npm install</code> can take minutes, and you don't want to run these steps every time the user starts their sandbox.</p>
<p>Now, after the initial setup, you can just call <code>createBackup()</code>, then <code>restoreBackup()</code> the next time this environment is needed. This makes it practical to pick up exactly
where a user left off, even after days of inactivity, without repeating expensive setup steps.</p>
<pre><code class="language-ts">const sandbox = getSandbox(env.Sandbox, &quot;my-sandbox&quot;);&#10;&#10;// Make non-trivial changes to the file system&#10;await sandbox.gitCheckout(endUserRepo, { targetDir: &quot;/workspace&quot; });&#10;await sandbox.exec(&quot;npm install&quot;, { cwd: &quot;/workspace&quot; });&#10;&#10;// Create a point-in-time backup of the directory&#10;const backup = await sandbox.createBackup({ dir: &quot;/workspace&quot; });&#10;&#10;// Store the handle for later use&#10;await env.KV.put(`backup:${userId}`, JSON.stringify(backup));&#10;&#10;// ... in a future session...&#10;&#10;// Restore instead of re-cloning and reinstalling&#10;await sandbox.restoreBackup(backup);&#10;</code></pre>
<p>Backups are stored in <a href="/r2">R2</a> and can take advantage of <a href="/sandbox/guides/backup-restore/#configure-r2-lifecycle-rules-for-automatic-cleanup">R2 object lifecycle rules</a> to ensure they do not persist forever.</p>
<p>Key capabilities:</p>
<ul>
<li><strong>Persist and reuse across sandbox sessions</strong> — Easily store backup handles in KV, D1, or Durable Object storage for use in subsequent sessions</li>
<li><strong>Usable across multiple instances</strong> — Fork a backup across many sandboxes for parallel work</li>
<li><strong>Named backups</strong> — Provide optional human-readable labels for easier management</li>
<li><strong>TTLs</strong> — Set time-to-live durations so backups are automatically removed from storage once they are no longer needed</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17640.md")</aside>
<p>To get started, refer to the <a href="/sandbox/guides/backup-restore/">backup and restore guide</a> for setup instructions and usage patterns, or the <a href="/sandbox/api/backups/">Backups API reference</a> for full method documentation.</p>


<h2 id="hyperdrive-no-longer-caches-queries-using-stable-postgresql-functions"><a href="/changelog/post/2026-02-23-hyperdrive-stable-functions-uncacheable/">Hyperdrive no longer caches queries using STABLE PostgreSQL functions</a></h2>
<p><em>2026-02-23</em></p>
<p>Hyperdrive now treats queries containing PostgreSQL <code>STABLE</code> functions as uncacheable, in addition to <code>VOLATILE</code> functions.</p>
<p>Previously, only functions <a href="https://www.postgresql.org/docs/current/xfunc-volatility.html">that PostgreSQL categorizes</a> as <code>VOLATILE</code> (for example, <code>RANDOM()</code>, <code>LASTVAL()</code>) were detected as uncacheable. <code>STABLE</code> functions (for example, <code>NOW()</code>, <code>CURRENT_TIMESTAMP</code>, <code>CURRENT_DATE</code>) were incorrectly allowed to be cached.</p>
<p>Because <code>STABLE</code> functions can return different results across different SQL statements within the same transaction, caching their results could serve stale or incorrect data. This change aligns Hyperdrive's caching behavior with PostgreSQL's function volatility semantics.</p>
<p>If your queries use <code>STABLE</code> functions, and you were relying on them being cached, move the function call to your application code and pass the result as a query parameter. For example, instead of <code>WHERE created_at &gt; NOW()</code>, compute the timestamp in your Worker and pass it as <code>WHERE created_at &gt; $1</code>.</p>
<p>Hyperdrive uses text-based pattern matching to detect uncacheable functions. References to function names like <code>NOW()</code> in SQL comments also cause the query to be marked as uncacheable.</p>
<p>For more information, refer to <a href="/hyperdrive/concepts/query-caching/">Query caching</a> and <a href="/hyperdrive/observability/troubleshooting/">Troubleshoot and debug</a>.</p>


<h2 id="cloudflare-codemode-v0-1-0-a-new-runtime-agnostic-modular-architecture"><a href="/changelog/post/2026-02-20-codemode-sdk-rewrite/">@cloudflare/codemode v0.1.0: a new runtime agnostic modular architecture</a></h2>
<p><em>2026-02-20</em></p>
<p>The <a href="https://www.npmjs.com/package/@cloudflare/codemode"><code>@cloudflare/codemode</code></a> package has been rewritten into a modular, runtime-agnostic SDK.</p>
<p><a href="https://blog.cloudflare.com/code-mode/">Code Mode</a> enables LLMs to write and execute code that orchestrates your tools, instead of calling them one at a time. This can (and does) yield significant token savings, reduces context window pressure and improves overall model performance on a task.</p>
<p>The new <code>Executor</code> interface is runtime agnostic and comes with a prebuilt <code>DynamicWorkerExecutor</code> to run generated code in a <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker Loader</a>.</p>
<h4 id="2026-02-20-codemode-sdk-rewrite-breaking-changes">Breaking changes</h4>
<ul>
<li>Removed <code>experimental_codemode()</code> and <code>CodeModeProxy</code> — the package no longer owns an LLM call or model choice</li>
<li>New import path: <code>createCodeTool()</code> is now exported from <code>@cloudflare/codemode/ai</code></li>
</ul>
<h4 id="2026-02-20-codemode-sdk-rewrite-new-features">New features</h4>
<ul>
<li><strong><code>createCodeTool()</code></strong> — Returns a standard AI SDK <code>Tool</code> to use in your AI agents.</li>
<li><strong><code>Executor</code> interface</strong> — Minimal <code>execute(code, fns)</code> contract. Implement for any code sandboxing primitive or runtime.</li>
</ul>
<h4 id="2026-02-20-codemode-sdk-rewrite-dynamicworkerexecutor"><code>DynamicWorkerExecutor</code></h4>
<p>Runs code in a <a href="/workers/runtime-apis/bindings/worker-loader/">Dynamic Worker</a>. It comes with the following features:</p>
<ul>
<li><strong>Network isolation</strong> — <code>fetch()</code> and <code>connect()</code> blocked by default (<code>globalOutbound: null</code>) when using <code>DynamicWorkerExecutor</code></li>
<li><strong>Console capture</strong> — <code>console.log/warn/error</code> captured and returned in <code>ExecuteResult.logs</code></li>
<li><strong>Execution timeout</strong> — Configurable via <code>timeout</code> option (default 30s)</li>
</ul>
<h4 id="2026-02-20-codemode-sdk-rewrite-usage">Usage</h4>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17638.md")</div>
<h4 id="2026-02-20-codemode-sdk-rewrite-wrangler-configuration">Wrangler configuration</h4>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17639.md")</div>
<p>See the <a href="/agents/tools/codemode/">Code Mode documentation</a> for full API reference and examples.</p>
<h4 id="2026-02-20-codemode-sdk-rewrite-upgrade">Upgrade</h4>
<pre><code class="language-sh">npm i @cloudflare/codemode@latest&#10;</code></pre>


<h2 id="manage-cloudflare-tunnel-directly-from-the-main-cloudflare-dashboard"><a href="/changelog/post/2026-02-20-tunnel-core-dashboard/">Manage Cloudflare Tunnel directly from the main Cloudflare Dashboard</a></h2>
<p><em>2026-02-20</em></p>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> is now available in the main Cloudflare Dashboard at <a href="https://dash.cloudflare.com/?to=/:account/tunnels">Networking &gt; Tunnels</a>, bringing first-class Tunnel management to developers using Tunnel for securing origin servers.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-tunnel/tunnel-core-dashboard.gif" alt="Manage Tunnels in the Core Dashboard" /></p>
<p>This new experience provides everything you need to manage Tunnels for <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">public applications</a>, including:</p>
<ul>
<li><strong>Full Tunnel lifecycle management</strong>: Create, configure, delete, and monitor all your Tunnels in one place.</li>
<li><strong>Native integrations</strong>: View Tunnels by name when configuring <a href="/dns/manage-dns-records/how-to/create-dns-records/">DNS records</a> and <a href="/workers-vpc/">Workers VPC</a> — no more copy-pasting UUIDs.</li>
<li><strong>Real-time visibility</strong>: Monitor <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">replicas</a> and Tunnel <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/#tunnel-status">health status</a> directly in the dashboard.</li>
<li><strong>Routing map</strong>: Manage all ingress routes for your Tunnel, including <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">public applications</a>, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/">private hostnames</a>, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/">private CIDRs</a>, and <a href="/workers-vpc/">Workers VPC services</a>, from a single interactive interface.</li>
</ul>
<h4 id="2026-02-20-tunnel-core-dashboard-choose-the-right-dashboard-for-your-use-case">Choose the right dashboard for your use case</h4>
<p><strong>Core Dashboard</strong>: Navigate to <a href="https://dash.cloudflare.com/?to=/:account/tunnels">Networking &gt; Tunnels</a> to manage Tunnels for:</p>
<ul>
<li>Securing origin servers and <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">public applications</a> with CDN, WAF, Load Balancing, and DDoS protection</li>
<li>Connecting <a href="/workers-vpc/">Workers to private services</a> via Workers VPC</li>
</ul>
<p><strong>Cloudflare One Dashboard</strong>: Navigate to <a href="https://one.dash.cloudflare.com/?to=/:account/networks/connectors">Zero Trust &gt; Networks &gt; Connectors</a> to manage Tunnels for:</p>
<ul>
<li>Securing your public applications with <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">Zero Trust access policies</a></li>
<li>Connecting users to <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">private applications</a></li>
<li>Building a <a href="/reference-architecture/architectures/sase/#connecting-networks">private mesh network</a></li>
</ul>
<p>Both dashboards provide complete Tunnel management capabilities — choose based on your primary workflow.</p>
<h4 id="2026-02-20-tunnel-core-dashboard-get-started">Get started</h4>
<p>New to Tunnel? Learn how to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/">get started with Cloudflare Tunnel</a> or explore advanced use cases like <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/">securing SSH servers</a> or <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/kubernetes/">running Tunnels in Kubernetes</a>.</p>


<h2 id="ai-dashboard-experience-improvements"><a href="/changelog/post/2026-02-19-ai-dashboard-experience-improvements/">AI dashboard experience improvements</a></h2>
<p><em>2026-02-19</em></p>
<p><a href="/workers-ai/">Workers AI</a> and <a href="/ai-gateway/">AI Gateway</a> have received a series of dashboard improvements to help you get started faster and manage your AI workloads more easily.</p>
<p><strong>Navigation and discoverability</strong></p>
<p>AI now has its own top-level section in the Cloudflare dashboard sidebar, so you can find AI features without digging through menus.</p>
<p><img src="/assets/upstream/images/ai-gateway/sidebar-navigation.png" alt="AI sidebar navigation in the Cloudflare dashboard" />
<em>The new top-level AI section in the dashboard sidebar.</em></p>
<p><strong>Onboarding and getting started</strong></p>
<p><a href="/ai-gateway/get-started/">Getting started</a> with AI Gateway is now simpler. When you create your first gateway, we now show your gateway's OpenAI-compatible endpoint and step-by-step guidance to help you configure it. The Playground also includes helpful prompts, and usage pages have clear next steps if you have not made any requests yet.</p>
<p><img src="/assets/upstream/images/ai-gateway/onboarding-flow.png" alt="AI Gateway onboarding flow" />
<em>The first-run setup experience for new gateways.</em></p>
<p>We've also combined the previously separate code example sections into one view with dropdown selectors for API type, provider, SDK, and authentication method so you can now customize the exact code snippet you need from one place.</p>
<p><strong>Dynamic Routing</strong></p>
<ul>
<li>The <a href="/ai-gateway/features/dynamic-routing/">route builder</a> is now more performant and responsive.</li>
<li>You can now copy route names to your clipboard with a single click.</li>
<li>Code examples use the <a href="/ai-gateway/usage/universal/">Universal Endpoint</a> format, making it easier to integrate routes into your application.</li>
</ul>
<p><strong>Observability and analytics</strong></p>
<ul>
<li>Small monetary values now display correctly in <a href="/ai-gateway/observability/costs/">cost analytics</a> charts, so you can accurately track spending at any scale.</li>
</ul>
<p><strong>Accessibility</strong></p>
<ul>
<li>Improvements to keyboard navigation within the AI Gateway, specifically when exploring usage by <a href="/ai-gateway/usage/providers/">provider</a>.</li>
<li>Improvements to sorting and filtering components on the <a href="/workers-ai/models/">Workers AI</a> models page.</li>
</ul>
<p>For more information, refer to the <a href="/ai-gateway/">AI Gateway documentation</a>.</p>


<h2 id="agents-sdk-v0-5-0-protocol-message-control-retry-utilities-data-parts-and-cloudflare-ai-chat-v0-1-0"><a href="/changelog/post/2026-02-17-agents-sdk-v0.5.0/">Agents SDK v0.5.0: Protocol message control, retry utilities, data parts, and @cloudflare/ai-chat v0.1.0</a></h2>
<p><em>2026-02-17</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> adds built-in retry utilities, per-connection protocol message control, and a fully rewritten <code>@cloudflare/ai-chat</code> with data parts, tool approval persistence, and zero breaking changes.</p>
<h4 id="2026-02-17-agents-sdk-v0.5.0-retry-utilities">Retry utilities</h4>
<p>A new <code>this.retry()</code> method lets you retry any async operation with exponential backoff and jitter. You can pass an optional <code>shouldRetry</code> predicate to bail early on non-retryable errors.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17635.md")</div>
<p>Retry options are also available per-task on <code>queue()</code>, <code>schedule()</code>, <code>scheduleEvery()</code>, and <code>addMcpServer()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17636.md")</div>
<p>Retry options are validated eagerly at enqueue/schedule time, and invalid values throw immediately. Internal retries have also been added for workflow operations (<code>terminateWorkflow</code>, <code>pauseWorkflow</code>, and others) with Durable Object-aware error detection.</p>
<h4 id="2026-02-17-agents-sdk-v0.5.0-per-connection-protocol-message-control">Per-connection protocol message control</h4>
<p>Agents automatically send JSON text frames (identity, state, MCP server lists) to every WebSocket connection. You can now suppress these per-connection for clients that cannot handle them — binary-only devices, MQTT clients, or lightweight embedded systems.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17637.md")</div>
<p>Connections with protocol messages disabled still fully participate in RPC and regular messaging. Use <code>isConnectionProtocolEnabled(connection)</code> to check a connection's status at any time. The flag persists across Durable Object hibernation.</p>
<p>See <a href="/agents/runtime/communication/protocol-messages/">Protocol messages</a> for full documentation.</p>
<h4 id="2026-02-17-agents-sdk-v0.5.0-cloudflare-ai-chat-v0-1-0"><code>@cloudflare/ai-chat</code> v0.1.0</h4>
<p>The first stable release of <code>@cloudflare/ai-chat</code> ships alongside this release with a major refactor of <code>AIChatAgent</code> internals — new <code>ResumableStream</code> class, WebSocket <code>ChatTransport</code>, and simplified SSE parsing — with zero breaking changes. Existing code using <code>AIChatAgent</code> and <code>useAgentChat</code> works as-is.</p>
<p>Key new features:</p>
<ul>
<li><strong>Data parts</strong> — Attach typed JSON blobs (<code>data-*</code>) to messages alongside text. Supports reconciliation (type+id updates in-place), append, and transient parts (ephemeral via <code>onData</code> callback). See <a href="/agents/communication-channels/chat/chat-agents/#data-parts">Data parts</a>.</li>
<li><strong>Tool approval persistence</strong> — The <code>needsApproval</code> approval UI now survives page refresh and DO hibernation. The streaming message is persisted to SQLite when a tool enters <code>approval-requested</code> state.</li>
<li><strong><code>maxPersistedMessages</code></strong> — Cap SQLite message storage with automatic oldest-message deletion.</li>
<li><strong><code>body</code> option on <code>useAgentChat</code></strong> — Send custom data with every request (static or dynamic).</li>
<li><strong>Incremental persistence</strong> — Hash-based cache to skip redundant SQL writes.</li>
<li><strong>Row size guard</strong> — Automatic two-pass compaction when messages approach the SQLite 2 MB limit.</li>
<li><strong><code>autoContinueAfterToolResult</code> defaults to <code>true</code></strong> — Client-side tool results and tool approvals now automatically trigger a server continuation, matching server-executed tool behavior. Set <code>autoContinueAfterToolResult: false</code> in <code>useAgentChat</code> to restore the previous behavior.</li>
</ul>
<p>Notable bug fixes:</p>
<ul>
<li>Resolved stream resumption race conditions</li>
<li>Resolved an issue where <code>setMessages</code> functional updater sent empty arrays</li>
<li>Resolved an issue where client tool schemas were lost after DO hibernation</li>
<li>Resolved <code>InvalidPromptError</code> after tool approval (<code>approval.id</code> was dropped)</li>
<li>Resolved an issue where message metadata was not propagated on broadcast/resume paths</li>
<li>Resolved an issue where <code>clearAll()</code> did not clear in-memory chunk buffers</li>
<li>Resolved an issue where <code>reasoning-delta</code> silently dropped data when <code>reasoning-start</code> was missed during stream resumption</li>
</ul>
<h4 id="2026-02-17-agents-sdk-v0.5.0-synchronous-queue-and-schedule-getters">Synchronous queue and schedule getters</h4>
<p><code>getQueue()</code>, <code>getQueues()</code>, <code>getSchedule()</code>, <code>dequeue()</code>, <code>dequeueAll()</code>, and <code>dequeueAllByCallback()</code> were unnecessarily <code>async</code> despite only performing synchronous SQL operations. They now return values directly instead of wrapping them in Promises. This is backward compatible — existing code using <code>await</code> on these methods will continue to work.</p>
<h4 id="2026-02-17-agents-sdk-v0.5.0-other-improvements">Other improvements</h4>
<ul>
<li><strong>Fix TypeScript &quot;excessively deep&quot; error</strong> — A depth counter on <code>CanSerialize</code> and <code>IsSerializableParam</code> types bails out to <code>true</code> after 10 levels of recursion, preventing the &quot;Type instantiation is excessively deep&quot; error with deeply nested types like AI SDK <code>CoreMessage[]</code>.</li>
<li><strong>POST SSE keepalive</strong> — The POST SSE handler now sends <code>event: ping</code> every 30 seconds to keep the connection alive, matching the existing GET SSE handler behavior. This prevents POST response streams from being silently dropped by proxies during long-running tool calls.</li>
<li><strong>Widened peer dependency ranges</strong> — Peer dependency ranges across packages have been widened to prevent cascading major bumps during 0.x minor releases. <code>@cloudflare/ai-chat</code> and <code>@cloudflare/codemode</code> are now marked as optional peer dependencies.</li>
</ul>
<h4 id="2026-02-17-agents-sdk-v0.5.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre><code class="language-sh">npm i agents@latest @cloudflare/ai-chat@latest&#10;</code></pre>


<h2 id="docker-in-docker-support-added-to-containers-and-sandboxes"><a href="/changelog/post/2026-02-17-docker-in-docker/">Docker-in-Docker support added to Containers and Sandboxes</a></h2>
<p><em>2026-02-17</em></p>
<p><a href="/sandbox/">Sandboxes</a> and <a href="/containers/">Containers</a> now support running Docker for &quot;Docker-in-Docker&quot; setups. This is particularly useful when your end users or <a href="/agents">agents</a> want to run a full sandboxed development environment.</p>
<p>This allows you to:</p>
<ul>
<li>Develop containerized applications with your Sandbox</li>
<li>Run isolated test environments for images</li>
<li>Build container images as part of CI/CD workflows</li>
<li>Deploy arbitrary images supplied at runtime within a container</li>
</ul>
<p>For <a href="/sandbox/">Sandbox SDK</a> users, see the <a href="/sandbox/guides/docker-in-docker/">Docker-in-Docker guide</a> for instructions on combining Docker with the SandboxSDK. For general Containers usage, see the <a href="/containers/faq/#can-i-run-docker-inside-a-container-docker-in-docker">Containers FAQ</a>.</p>


<h2 id="quick-editor-devtools-replaced-with-log-viewer"><a href="/changelog/post/2026-02-12-quick-editor-dev-tools-deprecation/">Quick Editor devtools replaced with log viewer</a></h2>
<p><em>2026-02-16</em></p>
<p>Cloudflare has deprecated the Workers Quick Editor dev tools inspector and replaced it with a lightweight log viewer.</p>
<p>This aligns our logging with <code>wrangler tail</code> and gives us the opportunity to focus our efforts on bringing benefits from the work we have invested in observability, which would not be possible otherwise.</p>
<p>We have made improvements to this logging viewer based on your feedback such that you can log object and array types, and easily clear the list of logs. This does not include class instances. Limitations are documented in the <a href="/workers/playground/">Workers Playground docs</a>.</p>
<p>If you do need to develop your Worker with a remote inspector, you can still do this using Wrangler locally. Cloning a project from your quick editor to your computer for local development can be done with the <code>wrangler init --from-dash</code> command. For more information, refer to <a href="/workers/wrangler/commands/general/#init">Wrangler commands</a>.</p>


<h2 id="new-best-practices-guide-for-workers"><a href="/changelog/post/2026-02-15-workers-best-practices/">New Best Practices guide for Workers</a></h2>
<p><em>2026-02-15</em></p>
<p>A new <a href="/workers/best-practices/workers-best-practices/">Workers Best Practices</a> guide provides opinionated recommendations for building fast, reliable, observable, and secure Workers. The guide draws on production patterns, Cloudflare internal usage, and best practices observed from developers building on Workers.</p>
<p>Key guidance includes:</p>
<ul>
<li><strong>Keep your compatibility date current and enable <code>nodejs_compat</code></strong> — Ensure you have access to the latest runtime features and Node.js built-in modules.</li>
</ul>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17799.md")</div>
- **Generate binding types with `wrangler types`** — Never hand-write your `Env` interface. Let Wrangler generate it from your actual configuration to catch mismatches at compile time.
- **Stream request and response bodies** — Avoid buffering large payloads in memory. Use `TransformStream` and `pipeTo` to stay within the 128 MB memory limit and improve time-to-first-byte.
- **Use bindings, not REST APIs** — Bindings to KV, R2, D1, Queues, and other Cloudflare services are direct, in-process references with no network hop and no authentication overhead.
- **Use Queues and Workflows for background work** — Move long-running or retriable tasks out of the critical request path. Use Queues for simple fan-out and buffering, and Workflows for multi-step durable processes.
- **Enable Workers Logs and Traces** — Configure observability before deploying to production so you have data when you need to debug.
- **Avoid global mutable state** — Workers reuse isolates across requests. Storing request-scoped data in module-level variables causes cross-request data leaks.
- **Always `await` or `waitUntil` your Promises** — Floating promises cause silent bugs and dropped work.
- **Use Web Crypto for secure token generation** — Never use `Math.random()` for security-sensitive operations.
<p>To learn more, refer to <a href="/workers/best-practices/workers-best-practices/">Workers Best Practices</a>.</p>


<h2 id="cloudflare-python-sdk-v5-0-0-beta-1-now-available"><a href="/changelog/post/2026-02-13-cloudflare-python-v5.0.0-beta.1/">Cloudflare Python SDK v5.0.0-beta.1 now available</a></h2>
<p><em>2026-02-13</em></p>
<blockquote>
<p><strong>Disclaimer:</strong> Please note that v5.0.0-beta.1 is in Beta and we are still testing it for stability.</p>
</blockquote>
<p>Full Changelog: <a href="https://github.com/cloudflare/cloudflare-python/compare/v4.3.1...v5.0.0-beta.1">v4.3.1...v5.0.0-beta.1</a></p>
<p>In this release, you'll see a large number of breaking changes. This is primarily due to a change in OpenAPI definitions,
which our libraries are based off of, and codegen updates that we rely on to read those OpenAPI definitions and produce
our SDK libraries. As the codegen is always evolving and improving, so are our code bases.</p>
<p>There may be changes that are not captured in this changelog. Feel free to open an issue to report any inaccuracies, and we will make sure it gets into the changelog before the v5.0.0 release.</p>
<p>Most of the breaking changes below are caused by improvements to the accuracy of the base OpenAPI schemas, which
sometimes translates to breaking changes in downstream clients that depend on those schemas.</p>
<p>Please ensure you read through the list of changes below and the migration guide before moving to this version - this
will help you understand any down or upstream issues it may cause to your environments.</p>
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-breaking-changes">Breaking Changes</h4>
<p><strong>The following resources have breaking changes. See the <a href="https://github.com/cloudflare/cloudflare-python/blob/main/docs/v5-migration-guide.md">v5 Migration Guide</a> for detailed migration instructions.</strong></p>
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
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-features">Features</h4>
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-new-api-resources">New API Resources</h4>
<ul>
<li><code>abusereports</code> - Abuse report management</li>
<li><code>abusereports.mitigations</code> - Abuse report mitigation actions</li>
<li><code>ai.tomarkdown</code> - AI-powered markdown conversion</li>
<li><code>aigateway.dynamicrouting</code> - AI Gateway dynamic routing configuration</li>
<li><code>aigateway.providerconfigs</code> - AI Gateway provider configurations</li>
<li><code>aisearch</code> - AI-powered search functionality</li>
<li><code>aisearch.instances</code> - AI Search instance management</li>
<li><code>aisearch.tokens</code> - AI Search authentication tokens</li>
<li><code>alerting.silences</code> - Alert silence management</li>
<li><code>brandprotection.logomatches</code> - Brand protection logo match detection</li>
<li><code>brandprotection.logos</code> - Brand protection logo management</li>
<li><code>brandprotection.matches</code> - Brand protection match results</li>
<li><code>brandprotection.queries</code> - Brand protection query management</li>
<li><code>cloudforceone.binarystorage</code> - CloudForce One binary storage</li>
<li><code>connectivity.directory</code> - Connectivity directory services</li>
<li><code>d1.database</code> - D1 database management</li>
<li><code>diagnostics.endpointhealthchecks</code> - Endpoint health check diagnostics</li>
<li><code>fraud</code> - Fraud detection and prevention</li>
<li><code>iam.sso</code> - IAM Single Sign-On configuration</li>
<li><code>loadbalancers.monitorgroups</code> - Load balancer monitor groups</li>
<li><code>organizations</code> - Organization management</li>
<li><code>organizations.organizationprofile</code> - Organization profile settings</li>
<li><code>origintlsclientauth.hostnamecertificates</code> - Origin TLS client auth hostname certificates</li>
<li><code>origintlsclientauth.hostnames</code> - Origin TLS client auth hostnames</li>
<li><code>origintlsclientauth.zonecertificates</code> - Origin TLS client auth zone certificates</li>
<li><code>pipelines</code> - Data pipeline management</li>
<li><code>pipelines.sinks</code> - Pipeline sink configurations</li>
<li><code>pipelines.streams</code> - Pipeline stream configurations</li>
<li><code>queues.subscriptions</code> - Queue subscription management</li>
<li><code>r2datacatalog</code> - R2 Data Catalog integration</li>
<li><code>r2datacatalog.credentials</code> - R2 Data Catalog credentials</li>
<li><code>r2datacatalog.maintenanceconfigs</code> - R2 Data Catalog maintenance configurations</li>
<li><code>r2datacatalog.namespaces</code> - R2 Data Catalog namespaces</li>
<li><code>radar.bots</code> - Radar bot analytics</li>
<li><code>radar.ct</code> - Radar certificate transparency data</li>
<li><code>radar.geolocations</code> - Radar geolocation data</li>
<li><code>realtimekit.activesession</code> - Real-time Kit active session management</li>
<li><code>realtimekit.analytics</code> - Real-time Kit analytics</li>
<li><code>realtimekit.apps</code> - Real-time Kit application management</li>
<li><code>realtimekit.livestreams</code> - Real-time Kit live streaming</li>
<li><code>realtimekit.meetings</code> - Real-time Kit meeting management</li>
<li><code>realtimekit.presets</code> - Real-time Kit preset configurations</li>
<li><code>realtimekit.recordings</code> - Real-time Kit recording management</li>
<li><code>realtimekit.sessions</code> - Real-time Kit session management</li>
<li><code>realtimekit.webhooks</code> - Real-time Kit webhook configurations</li>
<li><code>tokenvalidation.configuration</code> - Token validation configuration</li>
<li><code>tokenvalidation.rules</code> - Token validation rules</li>
<li><code>workers.beta</code> - Workers beta features</li>
</ul>
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-new-endpoints-existing-resources">New Endpoints (Existing Resources)</h4>
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-acm-totaltls"><code>acm.totaltls</code></h4>
- `edit()`
- `update()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-cloudforceone-threatevents"><code>cloudforceone.threatevents</code></h4>
- `list()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-contentscanning"><code>contentscanning</code></h4>
- `create()`
- `get()`
- `update()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-dns-records"><code>dns.records</code></h4>
- `scan_list()`
- `scan_review()`
- `scan_trigger()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-intel-indicatorfeeds"><code>intel.indicatorfeeds</code></h4>
- `create()`
- `delete()`
- `list()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-leakedcredentialchecks-detections"><code>leakedcredentialchecks.detections</code></h4>
- `get()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-queues-consumers"><code>queues.consumers</code></h4>
- `list()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-radar-ai"><code>radar.ai</code></h4>
- `summary()`
- `timeseries()`
- `timeseries_groups()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-radar-bgp"><code>radar.bgp</code></h4>
- `changes()`
- `snapshot()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-workers-subdomains"><code>workers.subdomains</code></h4>
- `delete()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-zerotrust-networks"><code>zerotrust.networks</code></h4>
- `create()`
- `delete()`
- `edit()`
- `get()`
- `list()`
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-general-fixes-and-improvements">General Fixes and Improvements</h4>
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-type-system-compatibility">Type System &amp; Compatibility</h4>
<ul>
<li><strong>Type inference improvements</strong>: Allow Pyright to properly infer TypedDict types within SequenceNotStr</li>
<li><strong>Type completeness</strong>: Add missing types to method arguments and response models</li>
<li><strong>Pydantic compatibility</strong>: Ensure compatibility with Pydantic versions prior to 2.8.0 when using additional fields</li>
</ul>
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-request-response-handling">Request/Response Handling</h4>
<ul>
<li><strong>Multipart form data</strong>: Correctly handle sending multipart/form-data requests with JSON data</li>
<li><strong>Header handling</strong>: Do not send headers with default values set to omit</li>
<li><strong>GET request headers</strong>: Don't send Content-Type header on GET requests</li>
<li><strong>Response body model accuracy</strong>: Broad improvements to the correctness of models</li>
</ul>
<h4 id="2026-02-13-cloudflare-python-v5.0.0-beta.1-parsing-data-processing">Parsing &amp; Data Processing</h4>
<ul>
<li><strong>Discriminated unions</strong>: Correctly handle nested discriminated unions in response parsing</li>
<li><strong>Extra field types</strong>: Parse extra field types correctly</li>
<li><strong>Empty metadata</strong>: Ignore empty metadata fields during parsing</li>
<li><strong>Singularization rules</strong>: Update resource name singularization rules for better consistency</li>
</ul>


<h2 id="introducing-glm-4-7-flash-on-workers-ai-cloudflare-tanstack-ai-and-workers-ai-provider-v3-1-1"><a href="/changelog/post/2026-02-13-glm-4.7-flash-workers-ai/">Introducing GLM-4.7-Flash on Workers AI, @cloudflare/tanstack-ai, and workers-ai-provider v3.1.1</a></h2>
<p><em>2026-02-13</em></p>
<p>We're excited to announce <strong>GLM-4.7-Flash</strong> on Workers AI, a fast and efficient text generation model optimized for multilingual dialogue and instruction-following tasks, along with the brand-new <a href="https://www.npmjs.com/package/@cloudflare/tanstack-ai"><strong>@cloudflare/tanstack-ai</strong></a> package and <a href="https://www.npmjs.com/package/workers-ai-provider"><strong>workers-ai-provider v3.1.1</strong></a>.</p>
<p>You can now run AI agents entirely on Cloudflare. With GLM-4.7-Flash's multi-turn tool calling support, plus full compatibility with TanStack AI and the Vercel AI SDK, you have everything you need to build agentic applications that run completely at the edge.</p>
<h4 id="2026-02-13-glm-4.7-flash-workers-ai-glm-4-7-flash-multilingual-text-generation-model">GLM-4.7-Flash — Multilingual Text Generation Model</h4>
<p><a href="/workers-ai/models/glm-4.7-flash/"><code>@cf/zai-org/glm-4.7-flash</code></a> is a multilingual model with a 131,072 token context window, making it ideal for long-form content generation, complex reasoning tasks, and multilingual applications.</p>
<p><strong>Key Features and Use Cases:</strong></p>
<ul>
<li><strong>Multi-turn Tool Calling for Agents</strong>: Build AI agents that can call functions and tools across multiple conversation turns</li>
<li><strong>Multilingual Support</strong>: Built to handle content generation in multiple languages effectively</li>
<li><strong>Large Context Window</strong>: 131,072 tokens for long-form writing, complex reasoning, and processing long documents</li>
<li><strong>Fast Inference</strong>: Optimized for low-latency responses in chatbots and virtual assistants</li>
<li><strong>Instruction Following</strong>: Excellent at following complex instructions for code generation and structured tasks</li>
</ul>
<p>Use GLM-4.7-Flash through the <a href="/workers-ai/configuration/bindings/">Workers AI binding</a> (<code>env.AI.run()</code>), the REST API at <code>/run</code> or <code>/v1/chat/completions</code>, <a href="/ai-gateway/">AI Gateway</a>, or via <a href="/workers-ai/configuration/ai-sdk/">workers-ai-provider</a> for the Vercel AI SDK.</p>
<p>Pricing is available on the <a href="/workers-ai/models/glm-4.7-flash/">model page</a> or <a href="/workers-ai/platform/pricing/">pricing page</a>.</p>
<h4 id="2026-02-13-glm-4.7-flash-workers-ai-cloudflare-tanstack-ai-v0-1-1-tanstack-ai-adapters-for-workers-ai-and-ai-gateway">@cloudflare/tanstack-ai v0.1.1 — TanStack AI adapters for Workers AI and AI Gateway</h4>
<p>We've released <code>@cloudflare/tanstack-ai</code>, a new package that brings Workers AI and AI Gateway support to <a href="https://tanstack.com/ai">TanStack AI</a>. This provides a framework-agnostic alternative for developers who prefer TanStack's approach to building AI applications.</p>
<p><strong>Workers AI adapters</strong> support four configuration modes — plain binding (<code>env.AI</code>), plain REST, AI Gateway binding (<code>env.AI.gateway(id)</code>), and AI Gateway REST — across all capabilities:</p>
<ul>
<li><strong>Chat</strong> (<code>createWorkersAiChat</code>) — Streaming chat completions with tool calling, structured output, and reasoning text streaming.</li>
<li><strong>Image generation</strong> (<code>createWorkersAiImage</code>) — Text-to-image models.</li>
<li><strong>Transcription</strong> (<code>createWorkersAiTranscription</code>) — Speech-to-text.</li>
<li><strong>Text-to-speech</strong> (<code>createWorkersAiTts</code>) — Audio generation.</li>
<li><strong>Summarization</strong> (<code>createWorkersAiSummarize</code>) — Text summarization.</li>
</ul>
<p><strong>AI Gateway adapters</strong> route requests from third-party providers — OpenAI, Anthropic, Gemini, Grok, and OpenRouter — through Cloudflare AI Gateway for caching, rate limiting, and unified billing.</p>
<p>To get started:</p>
<pre><code class="language-sh">npm install @cloudflare/tanstack-ai @tanstack/ai&#10;</code></pre>
<h4 id="2026-02-13-glm-4.7-flash-workers-ai-workers-ai-provider-v3-1-1-transcription-speech-reranking-and-reliability">workers-ai-provider v3.1.1 — transcription, speech, reranking, and reliability</h4>
<p>The Workers AI provider for the <a href="https://ai-sdk.dev">Vercel AI SDK</a> now supports three new capabilities beyond chat and image generation:</p>
<ul>
<li><strong>Transcription</strong> (<code>provider.transcription(model)</code>) — Speech-to-text with automatic handling of model-specific input formats across binding and REST paths.</li>
<li><strong>Text-to-speech</strong> (<code>provider.speech(model)</code>) — Audio generation with support for voice and speed options.</li>
<li><strong>Reranking</strong> (<code>provider.reranking(model)</code>) — Document reranking for RAG pipelines and search result ordering.</li>
</ul>
<pre><code class="language-typescript">import { createWorkersAI } from &quot;workers-ai-provider&quot;;&#10;import {&#10;	experimental_transcribe,&#10;	experimental_generateSpeech,&#10;	rerank,&#10;} from &quot;ai&quot;;&#10;&#10;const workersai = createWorkersAI({ binding: env.AI });&#10;&#10;const transcript = await experimental_transcribe({&#10;	model: workersai.transcription(&quot;@cf/openai/whisper-large-v3-turbo&quot;),&#10;	audio: audioData,&#10;	mediaType: &quot;audio/wav&quot;,&#10;});&#10;&#10;const speech = await experimental_generateSpeech({&#10;	model: workersai.speech(&quot;@cf/deepgram/aura-1&quot;),&#10;	text: &quot;Hello world&quot;,&#10;	voice: &quot;asteria&quot;,&#10;});&#10;&#10;const ranked = await rerank({&#10;	model: workersai.reranking(&quot;@cf/baai/bge-reranker-base&quot;),&#10;	query: &quot;What is machine learning?&quot;,&#10;	documents: [&quot;ML is a branch of AI.&quot;, &quot;The weather is sunny.&quot;],&#10;});&#10;</code></pre>
<p>This release also includes a comprehensive reliability overhaul (v3.0.5):</p>
<ul>
<li><strong>Fixed streaming</strong> — Responses now stream token-by-token instead of buffering all chunks, using a proper <code>TransformStream</code> pipeline with backpressure.</li>
<li><strong>Fixed tool calling</strong> — Resolved issues with tool call ID sanitization, conversation history preservation, and a heuristic that silently fell back to non-streaming mode when tools were defined.</li>
<li><strong>Premature stream termination detection</strong> — Streams that end unexpectedly now report <code>finishReason: &quot;error&quot;</code> instead of silently reporting <code>&quot;stop&quot;</code>.</li>
<li><strong>AI Search support</strong> — Added <code>createAISearch</code> as the canonical export (renamed from AutoRAG). <code>createAutoRAG</code> still works with a deprecation warning.</li>
</ul>
<p>To upgrade:</p>
<pre><code class="language-sh">npm install workers-ai-provider@latest ai&#10;</code></pre>
<h4 id="2026-02-13-glm-4.7-flash-workers-ai-resources">Resources</h4>
<ul>
<li><a href="https://www.npmjs.com/package/@cloudflare/tanstack-ai">@cloudflare/tanstack-ai on npm</a></li>
<li><a href="https://www.npmjs.com/package/workers-ai-provider">workers-ai-provider on npm</a></li>
<li><a href="https://github.com/cloudflare/ai">GitHub repository</a></li>
</ul>


<h2 id="origin-ca-certificate-support-for-workers-vpc"><a href="/changelog/post/2026-02-13-origin-ca-certificate-support/">Origin CA certificate support for Workers VPC</a></h2>
<p><em>2026-02-13</em></p>
<p>Workers VPC now supports <a href="/ssl/origin-configuration/origin-ca/">Cloudflare Origin CA certificates</a> when connecting to your private services over HTTPS. Previously, Workers VPC only trusted certificates issued by publicly trusted certificate authorities (for example, Let's Encrypt, DigiCert).</p>
<p>With this change, you can use free Cloudflare Origin CA certificates on your origin servers within private networks and connect to them from Workers VPC using the <code>https</code> scheme. This is useful for encrypting traffic between the tunnel and your service without needing to provision certificates from a public CA.</p>
<p>For more information, refer to <a href="/workers-vpc/configuration/vpc-services/#supported-tls-certificates">Supported TLS certificates</a>.</p>


<h2 id="terraform-v5-17-0-now-available"><a href="/changelog/post/2026-02-12-terraform-v5.17.0-provider/">Terraform v5.17.0 now available</a></h2>
<p><em>2026-02-12</em></p>
<p>In January 2025, we announced the launch of the new Terraform v5 Provider. We
greatly appreciate the proactive engagement and valuable feedback from the
Cloudflare community following the v5 release. In response, we have established
a consistent and rapid <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/5774">2-3 week cadence</a> for releasing targeted improvements,
demonstrating our commitment to stability and reliability.</p>
<p>With the help of the community, we have a growing number of resources that we
have marked as <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">stable</a>, with that list continuing to grow with every release.
The most used <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237">resources</a> are on track to be stable by the end of March 2026,
when we will also be releasing a new migration tool to help you migrate from v4
to v5 with ease.</p>
<p>This release brings new capabilities for AI Search, enhanced Workers Script
placement controls, and numerous bug fixes based on community feedback. We also
begun laying foundational work for improving the v4 to v5 migration process.
Stay tuned for more details as we approach the March 2026 release timeline.</p>
<p>Thank you for continuing to raise issues. They make our provider stronger and
help us build products that reflect your needs.</p>
<h4 id="2026-02-12-terraform-v5.17.0-provider-features">Features</h4>
<ul>
<li><strong>ai_search_instance:</strong> add data source for querying AI Search instances</li>
<li><strong>ai_search_token:</strong> add data source for querying AI Search tokens</li>
<li><strong>account:</strong> add support for tenant unit management with new <code>unit</code> field</li>
<li><strong>account:</strong> add automatic mapping from <code>managed_by.parent_org_id</code> to <code>unit.id</code></li>
<li><strong>authenticated_origin_pulls_certificate:</strong> add data source for querying authenticated origin pull certificates</li>
<li><strong>authenticated_origin_pulls_hostname_certificate:</strong> add data source for querying hostname-specific authenticated origin pull certificates</li>
<li><strong>authenticated_origin_pulls_settings:</strong> add data source for querying authenticated origin pull settings</li>
<li><strong>workers_kv:</strong> add <code>value</code> field to data source to retrieve KV values directly</li>
<li><strong>workers_script:</strong> add <code>script</code> field to data source to retrieve script content</li>
<li><strong>workers_script:</strong> add support for <code>simple</code> rate limit binding</li>
<li><strong>workers_script:</strong> add support for targeted placement mode with <code>placement.target</code> array for specifying placement targets (region, hostname, host)</li>
<li><strong>workers_script:</strong> add <code>placement_mode</code> and <code>placement_status</code> computed fields</li>
<li><strong>zero_trust_dex_test:</strong> add data source with filter support for finding specific tests</li>
<li><strong>zero_trust_dlp_predefined_profile:</strong> add <code>enabled_entries</code> field for flexible entry management</li>
</ul>
<h4 id="2026-02-12-terraform-v5.17.0-provider-bug-fixes">Bug Fixes</h4>
<ul>
<li><strong>account:</strong> map <code>managed_by.parent_org_id</code> to <code>unit.id</code> in unmarshall and add acceptance tests</li>
<li><strong>authenticated_origin_pulls_certificate:</strong> add certificate normalization to prevent drift</li>
<li><strong>authenticated_origin_pulls:</strong> handle array response and implement full lifecycle</li>
<li><strong>authenticated_origin_pulls_hostname_certificate:</strong> fix resource and tests</li>
<li><strong>cloudforce_one_request_message:</strong> use correct <code>request_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>dns_zone_transfers_incoming:</strong> use correct <code>zone_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>dns_zone_transfers_outgoing:</strong> use correct <code>zone_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>email_routing_settings:</strong> use correct <code>zone_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>hyperdrive_config:</strong> add proper handling for write-only fields to prevent state drift</li>
<li><strong>hyperdrive_config:</strong> add normalization for empty <code>mtls</code> objects to prevent unnecessary diffs</li>
<li><strong>magic_network_monitoring_rule:</strong> use correct <code>account_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>mtls_certificates:</strong> fix resource and test</li>
<li><strong>pages_project:</strong> revert build_config to computed optional</li>
<li><strong>stream_key:</strong> use correct <code>account_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>total_tls:</strong> use upsert pattern for singleton zone setting</li>
<li><strong>waiting_room_rules:</strong> use correct <code>waiting_room_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>workers_script:</strong> add support for placement mode/status</li>
<li><strong>zero_trust_access_application:</strong> update v4 version on migration tests</li>
<li><strong>zero_trust_device_posture_rule:</strong> update tests to match API</li>
<li><strong>zero_trust_dlp_integration_entry:</strong> use correct <code>entry_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>zero_trust_dlp_predefined_entry:</strong> use correct <code>entry_id</code> field instead of <code>id</code> in API calls</li>
<li><strong>zero_trust_organization:</strong> fix plan issues</li>
</ul>
<h4 id="2026-02-12-terraform-v5.17.0-provider-chores">Chores</h4>
<ul>
<li>add state upgraders to 95+ resources to lay the foundation for replacing Grit
(still under active development)</li>
<li><strong>certificate_pack:</strong> add state migration handler for SDKv2 to Framework conversion</li>
<li><strong>custom_hostname_fallback_origin:</strong> add comprehensive lifecycle test and migration support</li>
<li><strong>dns_record:</strong> add state migration handler for SDKv2 to Framework conversion</li>
<li><strong>leaked_credential_check:</strong> add import functionality and tests</li>
<li><strong>load_balancer_pool:</strong> add state migration handler with detection for v4 vs v5 format</li>
<li><strong>pages_project:</strong> add state migration handlers</li>
<li><strong>tiered_cache:</strong> add state migration handlers</li>
<li><strong>zero_trust_dlp_predefined_profile:</strong> deprecate <code>entries</code> field in favor of <code>enabled_entries</code></li>
</ul>
<h4 id="2026-02-12-terraform-v5.17.0-provider-for-more-information">For more information</h4>
- [Terraform Provider](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs)
- [Documentation on using Terraform with Cloudflare](/terraform/)
- [List of stabilized resources](https://github.com/cloudflare/terraform-provider-cloudflare/issues/6237)


<h2 id="workers-are-no-longer-limited-to-1000-subrequests"><a href="/changelog/post/2026-02-11-subrequests-limit/">Workers are no longer limited to 1000 subrequests</a></h2>
<p><em>2026-02-11</em></p>
<p>Workers no longer have a limit of 1000 subrequests per invocation, allowing you to make more <code>fetch()</code> calls or requests
to Cloudflare services on every incoming request. This is especially important for long-running Workers requests, such as
open websockets on <a href="/durable-objects">Durable Objects</a> or long-running <a href="/workflows">Workflows</a>, as these could often exceed this limit and error.</p>
<p>By default, Workers on paid plans are now limited to 10,000 subrequests per invocation, but this
limit can be increased up to 10 million by setting the new <code>subrequests</code> limit in your Wrangler configuration file.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17797.md")</div>
<p>Workers on the free plan remain limited to 50 external subrequests and 1000 subrequests to Cloudflare services per invocation.</p>
<p>To protect against runaway code or unexpected costs, you can also set a lower limit for both subrequests and CPU usage.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17798.md")</div>
<p>For more information, refer to the <a href="/workers/wrangler/configuration/#limits">Wrangler configuration documentation for limits</a> and <a href="/workers/platform/limits/#subrequests">subrequest limits</a>.</p>


<h2 id="improved-react-server-components-support-in-the-cloudflare-vite-plugin"><a href="/changelog/post/2026-02-11-vite-plugin-child-environments/">Improved React Server Components support in the Cloudflare Vite plugin</a></h2>
<p><em>2026-02-11</em></p>
<p>The Cloudflare Vite plugin now integrates seamlessly <a href="https://github.com/vitejs/vite-plugin-react/tree/main/packages/plugin-rsc">@vitejs/plugin-rsc</a>, the official Vite plugin for <a href="https://react.dev/reference/rsc/server-components">React Server Components</a>.</p>
<p>A <code>childEnvironments</code> option has been added to the plugin config to enable using multiple environments within a single Worker.
The parent environment can then import modules from a child environment in order to access a separate module graph.
For a typical RSC use case, the plugin might be configured as in the following example:</p>
<pre><code class="language-ts">export default defineConfig({&#10;	plugins: [&#10;		cloudflare({&#10;			viteEnvironment: {&#10;				name: &quot;rsc&quot;,&#10;				childEnvironments: [&quot;ssr&quot;],&#10;			},&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<p><code>@vitejs/plugin-rsc</code> provides the lower level functionality that frameworks, such as <a href="https://reactrouter.com/how-to/react-server-components">React Router</a>, build upon.
The GitHub repository includes a <a href="https://github.com/vitejs/vite-plugin-react/tree/f066114c3e6bf18f5209ff3d3ef6bf1ab46d3866/packages/plugin-rsc/examples/starter-cf-single">basic Cloudflare example</a>.</p>


<h2 id="agents-sdk-v0-4-0-readonly-connections-mcp-security-improvements-x402-v2-migration-and-custom-mcp-oauth-providers"><a href="/changelog/post/2026-02-09-agents-sdk-v0.4.0/">Agents SDK v0.4.0: Readonly connections, MCP security improvements, x402 v2 migration, and custom MCP OAuth providers</a></h2>
<p><em>2026-02-09</em></p>
<p>The latest release of the <a href="https://github.com/cloudflare/agents">Agents SDK</a> brings readonly connections, MCP protocol and security improvements, x402 payment protocol v2 migration, and the ability to customize OAuth for MCP server connections.</p>
<h4 id="2026-02-09-agents-sdk-v0.4.0-readonly-connections">Readonly connections</h4>
<p>Agents can now restrict WebSocket clients to read-only access, preventing them from modifying agent state. This is useful for dashboards, spectator views, or any scenario where clients should observe but not mutate.</p>
<p>New hooks: <code>shouldConnectionBeReadonly</code>, <code>setConnectionReadonly</code>, <code>isConnectionReadonly</code>. Readonly connections block both client-side <code>setState()</code> and mutating <code>@callable()</code> methods, and the readonly flag survives hibernation.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17630.md")</div>
<h4 id="2026-02-09-agents-sdk-v0.4.0-custom-mcp-oauth-providers">Custom MCP OAuth providers</h4>
<p>The new <code>createMcpOAuthProvider</code> method on the <code>Agent</code> class allows subclasses to override the default OAuth provider used when connecting to MCP servers. This enables custom authentication strategies such as pre-registered client credentials or mTLS, beyond the built-in dynamic client registration.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17631.md")</div>
<h4 id="2026-02-09-agents-sdk-v0.4.0-mcp-sdk-upgrade-to-1-26-0">MCP SDK upgrade to 1.26.0</h4>
<p>Upgraded the MCP SDK to 1.26.0 to prevent cross-client response leakage. Stateless MCP Servers should now create a new <code>McpServer</code> instance per request instead of sharing a single instance. A guard is added in this version of the MCP SDK which will prevent connection to a Server instance that has already been connected to a transport. Developers will need to modify their code if they declare their <code>McpServer</code> instance as a global variable.</p>
<h4 id="2026-02-09-agents-sdk-v0.4.0-mcp-oauth-callback-url-security-fix">MCP OAuth callback URL security fix</h4>
<p>Added <code>callbackPath</code> option to <code>addMcpServer</code> to prevent instance name leakage in MCP OAuth callback URLs. When <code>sendIdentityOnConnect</code> is <code>false</code>, <code>callbackPath</code> is now required — the default callback URL would expose the instance name, undermining the security intent. Also fixes callback request detection to match via the <code>state</code> parameter instead of a loose <code>/callback</code> URL substring check, enabling custom callback paths.</p>
<h4 id="2026-02-09-agents-sdk-v0.4.0-deprecate-onstateupdate-in-favor-of-onstatechanged">Deprecate <code>onStateUpdate</code> in favor of <code>onStateChanged</code></h4>
<p><code>onStateChanged</code> is a drop-in rename of <code>onStateUpdate</code> (same signature, same behavior). <code>onStateUpdate</code> still works but emits a one-time console warning per class. <code>validateStateChange</code> rejections now propagate a <code>CF_AGENT_STATE_ERROR</code> message back to the client.</p>
<h4 id="2026-02-09-agents-sdk-v0.4.0-x402-v2-migration">x402 v2 migration</h4>
<p>Migrated the x402 MCP payment integration from the legacy <code>x402</code> package to <code>@x402/core</code> and <code>@x402/evm</code> v2.</p>
<p><strong>Breaking changes for x402 users:</strong></p>
<ul>
<li>Peer dependencies changed: replace <code>x402</code> with <code>@x402/core</code> and <code>@x402/evm</code></li>
<li><code>PaymentRequirements</code> type now uses v2 fields (e.g. <code>amount</code> instead of <code>maxAmountRequired</code>)</li>
<li><code>X402ClientConfig.account</code> type changed from <code>viem.Account</code> to <code>ClientEvmSigner</code> (structurally compatible with <code>privateKeyToAccount()</code>)</li>
</ul>
<pre><code class="language-bash">npm uninstall x402&#10;npm install @x402/core @x402/evm&#10;</code></pre>
<p>Network identifiers now accept both legacy names and CAIP-2 format:</p>
<pre><code class="language-ts">// Legacy name (auto-converted)&#10;{&#10;	network: &quot;base-sepolia&quot;,&#10;}&#10;&#10;// CAIP-2 format (preferred)&#10;{&#10;	network: &quot;eip155:84532&quot;,&#10;}&#10;</code></pre>
<p><strong>Other x402 changes:</strong></p>
<ul>
<li><code>X402ClientConfig.network</code> is now optional — the client auto-selects from available payment requirements</li>
<li>Server-side lazy initialization: facilitator connection is deferred until the first paid tool invocation</li>
<li>Payment tokens support both v2 (<code>PAYMENT-SIGNATURE</code>) and v1 (<code>X-PAYMENT</code>) HTTP headers</li>
<li>Added <code>normalizeNetwork</code> export for converting legacy network names to CAIP-2 format</li>
<li>Re-exports <code>PaymentRequirements</code>, <code>PaymentRequired</code>, <code>Network</code>, <code>FacilitatorConfig</code>, and <code>ClientEvmSigner</code> from <code>agents/x402</code></li>
</ul>
<h4 id="2026-02-09-agents-sdk-v0.4.0-other-improvements">Other improvements</h4>
<ul>
<li>Fix <code>useAgent</code> and <code>AgentClient</code> crashing when using <code>basePath</code> routing</li>
<li>CORS handling delegated to partyserver's native support (simpler, more reliable)</li>
<li>Client-side <code>onStateUpdateError</code> callback for handling rejected state updates</li>
</ul>
<h4 id="2026-02-09-agents-sdk-v0.4.0-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre><code class="language-sh">npm i agents@latest&#10;</code></pre>


<h2 id="interactive-browser-terminals-in-sandboxes"><a href="/changelog/post/2026-02-09-pty-terminal-support/">Interactive browser terminals in Sandboxes</a></h2>
<p><em>2026-02-09</em></p>
<p>The <a href="https://github.com/cloudflare/sandbox-sdk">Sandbox SDK</a> now supports PTY (pseudo-terminal) passthrough, enabling browser-based terminal UIs to connect to sandbox shells via WebSocket.</p>
<h4 id="2026-02-09-pty-terminal-support-sandbox-terminal-request"><code>sandbox.terminal(request)</code></h4>
<p>The new <code>terminal()</code> method proxies a WebSocket upgrade to the container's PTY endpoint, with output buffering for replay on reconnect.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17632.md")</div>
<h4 id="2026-02-09-pty-terminal-support-multiple-terminals-per-sandbox">Multiple terminals per sandbox</h4>
<p>Each session can have its own terminal with an isolated working directory and environment, so users can run separate shells side-by-side in the same container.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17633.md")</div>
<h4 id="2026-02-09-pty-terminal-support-xterm-js-addon">xterm.js addon</h4>
<p>The new <code>@cloudflare/sandbox/xterm</code> export provides a <code>SandboxAddon</code> for <a href="https://xtermjs.org/">xterm.js</a> with automatic reconnection (exponential backoff + jitter), buffered output replay, and resize forwarding.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17634.md")</div>
<h4 id="2026-02-09-pty-terminal-support-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre><code class="language-sh">npm i @cloudflare/sandbox@latest&#10;</code></pre>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/developer-platform/11/">Previous</a><span>Page 12 of 23</span><a class="pagination-next" rel="next" href="/changelog/product-group/developer-platform/13/">Next</a></nav>
