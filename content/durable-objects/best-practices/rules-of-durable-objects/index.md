<p>Durable Objects provide a powerful primitive for building stateful, coordinated applications. Each Durable Object is a single-threaded, globally-unique instance with its own persistent storage. Understanding how to design around these properties is essential for building effective applications.</p>
<p>This is a guidebook on how to build more effective and correct Durable Object applications.</p>
<h2 id="when-to-use-durable-objects">When to use Durable Objects</h2>
<h3 id="use-durable-objects-for-stateful-coordination-not-stateless-request-handling">Use Durable Objects for stateful coordination, not stateless request handling</h3>
<p>Workers are stateless functions: each request may run on a different instance, in a different location, with no shared memory between requests. Durable Objects are stateful compute: each instance has a unique identity, runs in a single location, and maintains state across requests.</p>
<p>Use Durable Objects when you need:</p>
<ul>
<li><strong>Coordination</strong> — Multiple clients need to interact with shared state (chat rooms, multiplayer games, collaborative documents)</li>
<li><strong>Strong consistency</strong> — Operations must be serialized to avoid race conditions (inventory management, booking systems, turn-based games)</li>
<li><strong>Per-entity storage</strong> — Each user, tenant, or resource needs its own isolated database (multi-tenant SaaS, per-user data)</li>
<li><strong>Persistent connections</strong> — Long-lived WebSocket connections that survive across requests (real-time notifications, live updates)</li>
<li><strong>Scheduled work per entity</strong> — Each entity needs its own timer or scheduled task (subscription renewals, game timeouts)</li>
</ul>
<p>Use plain Workers when you need:</p>
<ul>
<li><strong>Stateless request handling</strong> — API endpoints, proxies, or transformations with no shared state</li>
<li><strong>Maximum global distribution</strong> — Requests should be handled at the nearest edge location</li>
<li><strong>High fan-out</strong> — Each request is independent and can be processed in parallel</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8262.md")
</div>
<p>A common pattern is to use Workers as the stateless entry point that routes requests to Durable Objects when coordination is needed. The Worker handles authentication, validation, and response formatting, while the Durable Object handles the stateful logic.</p>
<h2 id="design-and-sharding">Design and sharding</h2>
<h3 id="model-your-durable-objects-around-your-atom-of-coordination">Model your Durable Objects around your &quot;atom&quot; of coordination</h3>
<p>The most important design decision is choosing what each Durable Object represents. Create one Durable Object per logical unit that needs coordination: a chat room, a game session, a document, a user's data, or a tenant's workspace.</p>
<p>This is the key insight that makes Durable Objects powerful. Instead of a shared database with locks, each &quot;atom&quot; of your application gets its own single-threaded execution environment with private storage.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8263.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8261.md")
</aside>
<p>Do not create a single &quot;global&quot; Durable Object that handles all requests:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8264.md")
</div>
<h3 id="message-throughput-limits">Message throughput limits</h3>
<p>A single Durable Object can handle approximately <strong>500-1,000 requests per second</strong> for simple operations. This limit varies based on the work performed per request:</p>
<table>
<thead>
<tr>
<th>Operation type</th>
<th>Throughput</th>
</tr>
</thead>
<tbody>
<tr>
<td>Simple pass-through (minimal parsing)</td>
<td>~1,000 req/sec</td>
</tr>
<tr>
<td>Moderate processing (JSON parsing, validation)</td>
<td>~500-750 req/sec</td>
</tr>
<tr>
<td>Complex operations (transformation, storage writes)</td>
<td>~200-500 req/sec</td>
</tr>
</tbody>
</table>
<p>When modeling your &quot;atom,&quot; factor in the expected request rate. If your use case exceeds these limits, shard your workload across multiple Durable Objects.</p>
<p>For example, consider a real-time game with 50,000 concurrent players sending 10 updates per second. This generates 500,000 requests per second total. You would need 500-1,000 game session Durable Objects—not one global coordinator.</p>
<p>Calculate your sharding requirements:</p>
<pre><code>&#10;Required DOs = (Total requests/second) / (Requests per DO capacity)&#10;</code></pre>
<h3 id="use-deterministic-ids-for-predictable-routing">Use deterministic IDs for predictable routing</h3>
<p>Use <code>getByName()</code> with meaningful, deterministic strings for consistent routing. The same input always produces the same Durable Object ID, ensuring requests for the same logical entity always reach the same instance.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8265.md")
</div>
<p>Creating a stub does not instantiate or wake up the Durable Object. The Durable Object is only activated when you call a method on the stub.</p>
<p>Use <code>newUniqueId()</code> only when you need a new, random instance and will store the mapping externally:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8266.md")
</div>
<h3 id="use-parent-child-relationships-for-related-entities">Use parent-child relationships for related entities</h3>
<p>Do not put all your data in a single Durable Object. When you have hierarchical data (workspaces containing projects, game servers managing matches), create separate child Durable Objects for each entity. The parent coordinates and tracks children, while children handle their own state independently.</p>
<p>This enables parallelism: operations on different children can happen concurrently, while each child maintains its own single-threaded consistency (<a href="/reference-architecture/diagrams/storage/durable-object-control-data-plane-pattern/">read more about this pattern</a>).</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8267.md")
</div>
<p>With this pattern:</p>
<ul>
<li>Listing matches only queries the parent (children stay hibernated)</li>
<li>Different matches process player actions in parallel</li>
<li>Each match has its own SQLite database for player data</li>
</ul>
<h3 id="consider-location-hints-for-latency-sensitive-applications">Consider location hints for latency-sensitive applications</h3>
<p>By default, a Durable Object is created near the location of the first request it receives. For most applications, this works well. However, you can provide a location hint to influence where the Durable Object is created.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8268.md")
</div>
<p>Location hints are suggestions, not guarantees. Refer to <a href="/durable-objects/reference/data-location/">Data location</a> for available regions and details.</p>
<h2 id="storage-and-state">Storage and state</h2>
<h3 id="use-sqlite-backed-durable-objects">Use SQLite-backed Durable Objects</h3>
<p><a href="/durable-objects/api/sqlite-storage-api/">SQLite storage</a> is the recommended storage backend for new Durable Objects. It provides a familiar SQL API for relational queries, indexes, transactions, and better performance than the legacy key-value storage backed Durable Objects. SQLite Durable Objects also support the KV API in synchronous and asynchronous versions.</p>
<p>Configure your Durable Object class to use SQLite storage in your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8269.md")
</div>
<p>Then use the SQL API in your Durable Object:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8270.md")
</div>
<p>Refer to <a href="/durable-objects/best-practices/access-durable-objects-storage/">Access Durable Objects storage</a> for more details on the SQL API.</p>
<h3 id="initialize-storage-and-run-migrations-in-the-constructor">Initialize storage and run migrations in the constructor</h3>
<p>Use <code>blockConcurrencyWhile()</code> in the constructor to run migrations and initialize state before any requests are processed. This ensures your schema is ready and prevents race conditions during initialization.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8260.md")
</aside>
<p>For production applications, use a migration library that handles version tracking and execution automatically:</p>
<ul>
<li><a href="https://github.com/lambrospetrou/durable-utils#sqlite-schema-migrations"><code>durable-utils</code></a> — provides a <code>SQLSchemaMigrations</code> class that tracks executed migrations both in memory and in storage.</li>
<li><a href="https://github.com/cloudflare/actors/blob/main/packages/storage/src/sql-schema-migrations.ts"><code>@cloudflare/actors</code> storage utilities</a> — a reference implementation of the same pattern used by the Cloudflare Actors framework.</li>
</ul>
<p>If you prefer not to use a library, you can track schema versions manually using a <code>_sql_schema_migrations</code> table. The following example demonstrates this approach:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8271.md")
</div>
<h3 id="understand-the-difference-between-in-memory-state-and-persistent-storage">Understand the difference between in-memory state and persistent storage</h3>
<p>Durable Objects provide multiple state management layers, each with different characteristics:</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Speed</th>
<th>Persistence</th>
<th>Use Case</th>
</tr>
</thead>
<tbody>
<tr>
<td>In-memory (class properties)</td>
<td>Fastest</td>
<td>Lost on eviction or crash</td>
<td>Caching, active connections</td>
</tr>
<tr>
<td>SQLite storage</td>
<td>Fast</td>
<td>Durable across restarts</td>
<td>Primary data storage</td>
</tr>
<tr>
<td>External (R2, D1)</td>
<td>Variable</td>
<td>Durable, cross-DO accessible</td>
<td>Large files, shared data</td>
</tr>
</tbody>
</table>
<p>In-memory state is <strong>not preserved</strong> if the Durable Object is evicted from memory due to inactivity, or if it crashes from an uncaught exception. Always persist important state to SQLite storage.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8272.md")
</div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8259.md")
</aside>
<h3 id="create-indexes-for-frequently-queried-columns">Create indexes for frequently-queried columns</h3>
<p>Just like any database, indexes dramatically improve read performance for frequently-filtered columns. The cost is slightly more storage and marginally slower writes.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8273.md")
</div>
<h3 id="understand-how-input-and-output-gates-work">Understand how input and output gates work</h3>
<p>While Durable Objects are single-threaded, JavaScript's <code>async</code>/<code>await</code> can allow multiple requests to interleave execution while a request waits for the result of an asynchronous operation. Cloudflare's runtime uses <strong>input gates</strong> and <strong>output gates</strong> to prevent data races and ensure correctness by default.</p>
<p><strong>Input gates</strong> block new events (incoming requests, fetch responses) while synchronous JavaScript execution is in progress. Awaiting async operations like <code>fetch()</code> or KV storage methods opens the input gate, allowing other requests to interleave. However, storage operations provide special protection:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8274.md")
</div>
<p><strong>Output gates</strong> hold outgoing network messages (responses, fetch requests) until pending storage writes complete. This ensures clients never see confirmation of data that has not been persisted:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8275.md")
</div>
<p><strong>Write coalescing:</strong> Multiple storage writes without intervening <code>await</code> calls are automatically batched into a single atomic implicit transaction:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8276.md")
</div>
<p>For more details, see <a href="https://blog.cloudflare.com/durable-objects-easy-fast-correct-choose-three/">Durable Objects: Easy, Fast, Correct — Choose three</a> and the <a href="/durable-objects/reference/glossary/">glossary</a>.</p>
<h3 id="avoid-race-conditions-with-non-storage-i-o">Avoid race conditions with non-storage I/O</h3>
<p>Input gates only protect during storage operations. Non-storage I/O like <code>fetch()</code> or writing to R2 allows other requests to interleave, which can cause race conditions:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8277.md")
</div>
<p>To handle this, use optimistic locking (check-and-set) patterns: read a version number before the external call, then verify it has not changed before writing.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8258.md")
</aside>
<h3 id="use-blockconcurrencywhile-sparingly">Use <code>blockConcurrencyWhile()</code> sparingly</h3>
<p>The <a href="/durable-objects/api/state/#blockconcurrencywhile"><code>blockConcurrencyWhile()</code></a> method guarantees that no other events are processed until the provided callback completes, even if the callback performs asynchronous I/O. This is useful for operations that must be atomic, such as state initialization from storage in the constructor:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8278.md")
</div>
<p>Because <code>blockConcurrencyWhile()</code> blocks <em>all</em> concurrency unconditionally, it significantly reduces throughput. If each call takes ~5ms, that individual Durable Object is limited to approximately 200 requests/second. Reserve it for initialization and migrations, not regular request handling. For normal operations, rely on input/output gates and write coalescing instead.</p>
<p>For atomic read-modify-write operations during request handling, prefer <a href="/durable-objects/api/sqlite-storage-api/#transaction"><code>transaction()</code></a> over <code>blockConcurrencyWhile()</code>. Transactions provide atomicity for storage operations without blocking unrelated concurrent requests.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8257.md")
</aside>
<h2 id="communication-and-api-design">Communication and API design</h2>
<h3 id="use-rpc-methods-instead-of-the-fetch-handler">Use RPC methods instead of the <code>fetch()</code> handler</h3>
<p>Projects with a <a href="/workers/configuration/compatibility-flags/">compatibility date</a> of <code>2024-04-03</code> or later should use RPC methods. RPC is more ergonomic, provides better type safety, and eliminates manual request/response parsing.</p>
<p>Define public methods on your Durable Object class, and call them directly from stubs with full TypeScript support:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8279.md")
</div>
<p>Refer to <a href="/durable-objects/best-practices/create-durable-object-stubs-and-send-requests/">Invoke methods</a> for more details on RPC and the legacy <code>fetch()</code> handler.</p>
<h3 id="initialize-durable-objects-explicitly-with-an-init-method">Initialize Durable Objects explicitly with an <code>init()</code> method</h3>
<p>Durable Objects do not know their own name or ID from within. If your Durable Object needs to know its identity (for example, to store a reference to itself or to communicate with related objects), you must explicitly initialize it.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8280.md")
</div>
<h3 id="always-await-rpc-calls">Always <code>await</code> RPC calls</h3>
<p>When calling methods on a Durable Object stub, always use <code>await</code>. Unawaited calls create dangling promises, causing errors to be swallowed and return values to be lost.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8281.md")
</div>
<h2 id="error-handling">Error handling</h2>
<h3 id="handle-errors-and-use-exception-boundaries">Handle errors and use exception boundaries</h3>
<p>Uncaught exceptions in a Durable Object can leave it in an unknown state and may cause the runtime to terminate the instance. Wrap risky operations in <code>try...catch</code> blocks, and handle errors appropriately.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8282.md")
</div>
<p>When calling Durable Objects from a Worker, errors may include <code>.retryable</code> and <code>.overloaded</code> properties indicating whether the operation can be retried. For transient failures, implement exponential backoff to avoid overwhelming the system.</p>
<p>Refer to <a href="/durable-objects/best-practices/error-handling/">Error handling</a> for details on error properties, retry strategies, and exponential backoff patterns.</p>
<h2 id="websockets-and-real-time">WebSockets and real-time</h2>
<h3 id="use-the-hibernatable-websockets-api-for-cost-efficiency">Use the Hibernatable WebSockets API for cost efficiency</h3>
<p>The Hibernatable WebSockets API allows Durable Objects to sleep while maintaining WebSocket connections. This significantly reduces costs for applications with many idle connections.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8283.md")
</div>
<p>With the Hibernation API, your Durable Object can go to sleep when there is no active JavaScript execution, but WebSocket connections remain open. When a message arrives, the Durable Object wakes up automatically.</p>
<p>Best practices:</p>
<ul>
<li>The <a href="/durable-objects/best-practices/websockets/#durable-objects-hibernation-websocket-api">WebSocket Hibernation API</a> exposes <code>webSocketError</code>, <code>webSocketMessage</code>, and <code>webSocketClose</code> handlers for their respective WebSocket events.</li>
<li>With the <a href="/workers/configuration/compatibility-flags/#websocket-auto-reply-to-close"><code>web_socket_auto_reply_to_close</code></a> compatibility flag (enabled by default on compatibility dates on or after <code>2026-04-07</code>), the runtime automatically completes the close handshake. Calling <code>ws.close()</code> in <code>webSocketClose</code> is still safe but no longer required. On older compatibility dates, you <strong>must</strong> call <code>ws.close()</code> to avoid <code>1006</code> abnormal closure errors.</li>
</ul>
<p>Refer to <a href="/durable-objects/best-practices/websockets/">WebSockets</a> for more details.</p>
<h3 id="use-serializeattachment-to-persist-per-connection-state">Use <code>serializeAttachment()</code> to persist per-connection state</h3>
<p>WebSocket attachments let you store metadata for each connection that survives hibernation. Use this for user IDs, session tokens, or other per-connection data.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8284.md")
</div>
<h2 id="scheduling-and-lifecycle">Scheduling and lifecycle</h2>
<h3 id="use-alarms-for-per-entity-scheduled-tasks">Use alarms for per-entity scheduled tasks</h3>
<p>Each Durable Object can schedule its own future work using the <a href="/durable-objects/api/alarms/">Alarms API</a>, allowing a Durable Object to execute background tasks on any interval without an incoming request, RPC call, or WebSocket message.</p>
<p>Key points about alarms:</p>
<ul>
<li><strong><code>setAlarm(timestamp)</code></strong> schedules the <code>alarm()</code> handler to run at any time in the future (millisecond precision)</li>
<li><strong>Alarms do not repeat automatically</strong> — you must call <code>setAlarm()</code> again to schedule the next execution</li>
<li><strong>Only schedule alarms when there is work to do</strong> — avoid waking up every Durable Object on short intervals (seconds), as each alarm invocation incurs costs</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8285.md")
</div>
<h3 id="make-alarm-handlers-idempotent">Make alarm handlers idempotent</h3>
<p>In rare cases, alarms may fire more than once. Your <code>alarm()</code> handler should be safe to run multiple times without causing issues.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8286.md")
</div>
<h3 id="clean-up-storage-with-deleteall">Clean up storage with <code>deleteAll()</code></h3>
<p>To fully clear a Durable Object's storage, call <code>deleteAll()</code>. Simply deleting individual keys or dropping tables is not sufficient, as some internal metadata may remain. Workers with a compatibility date before <a href="/workers/configuration/compatibility-flags/#durable-object-deleteall-deletes-alarms">2026-02-24</a> and an alarm set should delete the alarm first with <code>deleteAlarm()</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8287.md")
</div>
<h3 id="design-for-unexpected-shutdowns">Design for unexpected shutdowns</h3>
<p>Durable Objects may shut down at any time due to deployments, inactivity, or runtime decisions. Rather than relying on shutdown hooks (which are not provided), design your application to write state incrementally.</p>
<p>Shutdown hooks or lifecycle callbacks that run before shutdown are not provided because Cloudflare cannot guarantee these hooks would execute in all cases, and external software may rely too heavily on these (unreliable) hooks.</p>
<p>Instead of relying on shutdown hooks, you can regularly write to storage to recover gracefully from shutdowns.</p>
<p>For example, if you are processing a stream of data and need to save your progress, write your position to storage as you go rather than waiting to persist it at the end:</p>
<pre><code class="language-js">// Good: Write progress as you go&#10;async processData(data) {&#10;  data.forEach(async (item, index) =&gt; {&#10;    await this.processItem(item);&#10;    // Save progress frequently&#10;    await this.ctx.storage.put(&quot;lastProcessedIndex&quot;, index);&#10;  });&#10;}&#10;</code></pre>
<p>While this may feel unintuitive, Durable Object storage writes are fast and synchronous, so you can persist state with minimal performance concerns.</p>
<p>This approach ensures your Durable Object can safely resume from any point, even if it shuts down unexpectedly.</p>
<h2 id="anti-patterns-to-avoid">Anti-patterns to avoid</h2>
<h3 id="do-not-use-a-single-durable-object-as-a-global-singleton">Do not use a single Durable Object as a global singleton</h3>
<p>A single Durable Object handling all traffic becomes a bottleneck. While async operations allow request interleaving, all synchronous JavaScript execution is single-threaded, and storage operations provide serialization guarantees that limit throughput.</p>
<p>A common mistake is using a Durable Object for global rate limiting or global counters. This funnels all traffic through a single instance:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8288.md")
</div>
<p>This pattern does not scale. As traffic increases, the single Durable Object becomes a chokepoint. Instead, identify natural coordination boundaries in your application (per user, per room, per document) and create separate Durable Objects for each.</p>
<h2 id="testing-and-class-lifecycle">Testing and class lifecycle</h2>
<h3 id="test-with-vitest-and-plan-for-class-lifecycle-changes">Test with Vitest and plan for class lifecycle changes</h3>
<p>Use <code>@cloudflare/vitest-plugin</code> for testing Durable Objects. The integration provides utilities for direct instance access.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/8289.md")
</div>
<p>Configure Vitest in your <code>vitest.config.ts</code>:</p>
<pre><code class="language-ts">import { cloudflareTest } from &quot;@cloudflare/vitest-plugin&quot;;&#10;import { defineConfig } from &quot;vitest/config&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflareTest({&#10;			wrangler: { configPath: &quot;./wrangler.jsonc&quot; },&#10;		}),&#10;	],&#10;});&#10;</code></pre>
<p>For data-schema changes, run schema migrations in the constructor using <code>blockConcurrencyWhile()</code>. For class renames or deletions, change the class entry in the <a href="/durable-objects/reference/durable-objects-migrations/"><code>exports</code></a> field of your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/8290.md")
</div>
<p>Refer to <a href="/durable-objects/reference/durable-objects-migrations/">Durable Object class exports</a> for more details on class lifecycle changes, and <a href="/durable-objects/examples/testing-with-durable-objects/">Testing with Durable Objects</a> for comprehensive testing patterns including SQLite queries and alarm testing.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/best-practices/workers-best-practices/">Workers Best Practices</a>: code patterns for request handling, observability, and security that apply to the Workers calling your Durable Objects.</li>
<li><a href="/workflows/build/rules-of-workflows/">Rules of Workflows</a>: best practices for durable, multi-step Workflows — useful when combining Workflows with Durable Objects for long-running orchestration.</li>
</ul>
