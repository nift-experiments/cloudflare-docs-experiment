<h1 id="changelog">Changelog</h1>

<h2 id="d1-enforces-free-tier-daily-query-limits"><a href="/changelog/post/2026-09-01-d1-free-tier-limit-enforcement/">D1 enforces free tier daily query limits</a></h2>
<p><em>2026-09-01</em></p>
<p>Beginning September 1, 2026, D1 queries on the <a href="/workers/platform/pricing/#workers">Workers Free plan</a> will fail when an account exceeds the daily <a href="/d1/platform/pricing/">row read or row write limits</a>. Queries via the <a href="/d1/worker-api/">Workers Binding API</a> and the <a href="/d1/rest-api/">REST API</a> will return errors until the limit resets at midnight UTC. Stored data is not affected.</p>
<p>You will receive email alerts when the daily limit is reached. The following errors indicate that a limit has been exceeded:</p>
<table>
<thead>
<tr>
<th>Error</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Your account has exceeded D1's free tier daily row read limit. Upgrade to a paid plan or wait until tomorrow (midnight UTC) to continue.</td>
<td>The account has reached its daily row read limit.</td>
</tr>
<tr>
<td>Your account has exceeded D1's free tier daily row write limit. Upgrade to a paid plan or wait until tomorrow (midnight UTC) to continue.</td>
<td>The account has reached its daily row write limit.</td>
</tr>
</tbody>
</table>
<p>Inspect database query activity before the enforcement date to identify queries that may exceed these limits. To reduce row reads, add <a href="/d1/best-practices/use-indexes/">indexes</a> to tables and review queries that perform full table scans. If usage requires higher limits after optimization, upgrade to a <a href="/workers/platform/pricing/#workers">Workers Paid plan</a>.</p>
<p>For more information on D1 errors and how to handle them, refer to the <a href="/d1/observability/debug-d1/#error-list">D1 error list</a>.</p>


<h2 id="billable-usage-and-budget-alerts-now-in-product-sidebars"><a href="/changelog/post/2026-06-04-billable-usage-product-sidebar/">Billable usage and budget alerts now in product sidebars</a></h2>
<p><em>2026-06-04</em></p>
<p>Pay-as-you-go customers can now view billable usage and create <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">budget alerts</a> directly from the product overview pages for <a href="/workers/">Workers &amp; Pages</a>, <a href="/d1/">D1</a>, <a href="/r2/">R2</a>, <a href="/kv/">Workers KV</a>, <a href="/queues/">Queues</a>, <a href="/vectorize/">Vectorize</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/containers/">Containers</a>. A new sidebar widget shows current-period spend and the billing cycle date range, alongside a button to create a budget alert.</p>
<p>The widget pulls from the same data as the <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">Billable Usage dashboard</a> and aligns to your billing cycle (or the current day on Free plans), so the numbers match your invoice. Enterprise contract accounts are not yet supported.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-06-04-billable-usage-product-sidebar.png" alt="Billable usage widget in the Durable Objects product sidebar showing current-period spend and a breakdown by service" /></p>
<p>Selecting <strong>Create budget alert</strong> opens the budget alert flow inline so you can set a dollar threshold in the same place you are reviewing usage. Budget alerts apply to your total account-level spend across all products, not just the product page you create them from.</p>
<p>For more information, refer to the <a href="/billing/">Usage-based billing documentation</a>.</p>


<h2 id="d1-migrations-support-nested-layouts-via-migrations-pattern"><a href="/changelog/post/2026-06-04-migrations-pattern/">D1 migrations support nested layouts via `migrations_pattern`</a></h2>
<p><em>2026-05-29</em></p>
<p>You can now point <code>wrangler d1 migrations apply</code> at a nested migrations layout — such as the one produced by <a href="https://orm.drizzle.team/">Drizzle</a> (<code>migrations/0001_init/migration.sql</code>) — using the new <code>migrations_pattern</code> D1 binding config:</p>
<pre><code class="language-jsonc">{&#10;	&quot;d1_databases&quot;: [&#10;		{&#10;			&quot;binding&quot;: &quot;DB&quot;,&#10;			&quot;database_name&quot;: &quot;my-database&quot;,&#10;			&quot;database_id&quot;: &quot;&lt;UUID&gt;&quot;,&#10;			&quot;migrations_dir&quot;: &quot;migrations&quot;,&#10;			&quot;migrations_pattern&quot;: &quot;migrations/*/migration.sql&quot;,&#10;		},&#10;	],&#10;}&#10;</code></pre>
<p><code>migrations_pattern</code> is a glob (relative to your Wrangler config file) used to discover migration files. It defaults to <code>${migrations_dir}/*.sql</code>, so existing projects keep working unchanged. Each migration's name is recorded in the migrations table as a path relative to <code>migrations_dir</code>.</p>
<p>To learn more, visit D1's <a href="/d1/reference/migrations/#nested-migration-layouts">migrations documentation</a>.</p>


<h2 id="d1-can-restrict-data-localization-with-jurisdictions"><a href="/changelog/post/2025-11-05-d1-jurisdiction/">D1 can restrict data localization with jurisdictions</a></h2>
<p><em>2025-11-05</em></p>
<p>You can now set a <a href="/d1/configuration/data-location/">jurisdiction</a> when creating a D1 database to guarantee where your database runs and stores data. Jurisdictions can help you comply with data localization regulations such as GDPR. Supported jurisdictions include <code>eu</code> and <code>fedramp</code>.</p>
<p>A jurisdiction can only be set at database creation time via wrangler, REST API or the UI and cannot be added/updated after the database already exists.</p>
<pre><code class="language-sh">npx wrangler@latest d1 create db-with-jurisdiction --jurisdiction eu&#10;</code></pre>
<pre><code class="language-sh">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/d1/database&quot; \&#10;     &#45;H &quot;Authorization: Bearer $TOKEN&quot; \&#10;     &#45;H &quot;Content-Type: application/json&quot; \&#10;     &#45;-data &#x27;{&quot;name&quot;: &quot;db-with-jurisdiction&quot;, &quot;jurisdiction&quot;: &quot;eu&quot; }&#x27;&#10;</code></pre>
<p>To learn more, visit D1's data location <a href="/d1/configuration/data-location/">documentation</a>.</p>


<h2 id="d1-automatically-retries-read-only-queries"><a href="/changelog/post/2025-09-11-d1-automatic-read-retries/">D1 automatically retries read-only queries</a></h2>
<p><em>2025-09-11</em></p>
<p>D1 now detects read-only queries and automatically attempts up to two retries to execute those queries in the event of failures with retryable errors. You can access the number of execution attempts in the returned <a href="/d1/worker-api/return-object/#d1result">response metadata</a> property <code>total_attempts</code>.</p>
<p>At the moment, only read-only queries are retried, that is, queries containing only the following SQLite keywords: <code>SELECT</code>, <code>EXPLAIN</code>, <code>WITH</code>. Queries containing any <a href="https://sqlite.org/lang_keywords.html">SQLite keyword</a> that leads to database writes are not retried.</p>
<p>The retry success ratio among read-only retryable errors varies from 5% all the way up to 95%, depending on the underlying error and its duration (like network errors or other internal errors).</p>
<p>The retry success ratio among all retryable errors is lower, indicating that there are write-queries that could be retried. Therefore, we recommend D1 users to continue applying <a href="/d1/best-practices/retry-queries/">retries in their own code</a> for queries that are not read-only but are idempotent according to the business logic of the application.</p>
<p><img src="/assets/upstream/images/changelog/d1/d1-auto-retry-success-ratio.png" alt="D1 automatically query retries success ratio" /></p>
<p>D1 ensures that any retry attempt does not cause database writes, making the automatic retries safe from side-effects, even if a query causing changes slips through the read-only detection. D1 achieves this by checking for modifications after every query execution, and if any write occurred due to a retry attempt, the query is rolled back.</p>
<p>The read-only query detection heuristics are simple for now, and there is room for improvement to capture more cases of queries that can be retried, so this is just the beginning.</p>


<h2 id="automate-worker-deployments-with-a-simplified-sdk-and-more-reliable-terraform-provider"><a href="/changelog/post/2025-06-17-workers-terraform-sdk-api-fixes/">Automate Worker deployments with a simplified SDK and more reliable Terraform provider</a></h2>
<p><em>2025-06-19</em></p>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-simplified-worker-deployments-with-our-sdks">Simplified Worker Deployments with our SDKs</h4>
<p>We've simplified the programmatic deployment of Workers via our <a href="/fundamentals/api/reference/sdks/">Cloudflare SDKs</a>. This update abstracts away the low-level complexities of the <code>multipart/form-data</code> upload process, allowing you to focus on your code while we handle the deployment mechanics.</p>
<p>This new interface is available in:</p>
<ul>
<li><a href="https://github.com/cloudflare/cloudflare-typescript">cloudflare-typescript</a> (4.4.1)</li>
<li><a href="https://github.com/cloudflare/cloudflare-python">cloudflare-python</a> (4.3.1)</li>
</ul>
<p>For complete examples, see our guide on <a href="/workers/platform/infrastructure-as-code">programmatic Worker deployments</a>.</p>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-the-old-way-manual-api-calls">The Old way: Manual API calls</h4>
<p>Previously, deploying a Worker programmatically required manually constructing a <code>multipart/form-data</code> HTTP request, packaging your code and a separate <code>metadata.json</code> file. This was more complicated and verbose, and prone to formatting errors.</p>
<p>For example, here's how you would upload a Worker script previously with cURL:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/workers/scripts/my-hello-world-script \&#10;  &#45;X PUT \&#10;  &#45;H &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;  &#45;F &#x27;metadata={&#10;        &quot;main_module&quot;: &quot;my-hello-world-script.mjs&quot;,&#10;        &quot;bindings&quot;: [&#10;          {&#10;            &quot;type&quot;: &quot;plain_text&quot;,&#10;            &quot;name&quot;: &quot;MESSAGE&quot;,&#10;            &quot;text&quot;: &quot;Hello World!&quot;&#10;          }&#10;        ],&#10;        &quot;compatibility_date&quot;: &quot;$today&quot;&#10;      };type=application/json&#x27; \&#10;  &#45;F &#x27;my-hello-world-script.mjs=@-;filename=my-hello-world-script.mjs;type=application/javascript+module&#x27; &lt;&lt;EOF&#10;export default {&#10;  async fetch(request, env, ctx) {&#10;    return new Response(env.MESSAGE, { status: 200 });&#10;  }&#10;};&#10;EOF&#10;</code></pre>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-after-sdk-interface">After: SDK interface</h4>
<p>With the new SDK interface, you can now define your entire Worker configuration using a single, structured object.</p>
<p>This approach allows you to specify metadata like <code>main_module</code>, <code>bindings</code>, and <code>compatibility_date</code> as clearer properties directly alongside your script content. Our SDK takes this logical object and automatically constructs the complex multipart/form-data API request behind the scenes.</p>
<p>Here's how you can now programmatically deploy a Worker via the <a href="https://github.com/cloudflare/cloudflare-typescript"><code>cloudflare-typescript</code> SDK</a></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17777.md")</div>
<p>View the complete example here: <a href="https://github.com/cloudflare/cloudflare-typescript/blob/main/examples/workers/script-upload.ts">https://github.com/cloudflare/cloudflare-typescript/blob/main/examples/workers/script-upload.ts</a></p>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-terraform-provider-improvements">Terraform provider improvements</h4>
<p>We've also made several fixes and enhancements to the <a href="https://github.com/cloudflare/terraform-provider-cloudflare">Cloudflare Terraform provider</a>:</p>
<ul>
<li>Fixed the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script"><code>cloudflare_workers_script</code></a> resource in Terraform, which previously was producing a diff even when there were no changes. Now, your <code>terraform plan</code> outputs will be cleaner and more reliable.</li>
<li>Fixed the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_for_platforms_dispatch_namespace"><code>cloudflare_workers_for_platforms_dispatch_namespace</code></a>, where the provider would attempt to recreate the namespace on a <code>terraform apply</code>. The resource now correctly reads its remote state, ensuring stability for production environments and CI/CD workflows.</li>
<li>The <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_route"><code>cloudflare_workers_route</code></a> resource now allows for the <code>script</code> property to be empty, null, or omitted to indicate that pattern should be negated for all scripts (see routes <a href="/workers/configuration/routing/routes">docs</a>). You can now reserve a pattern or temporarily disable a Worker on a route without deleting the route definition itself.</li>
<li>Using <code>primary_location_hint</code> in the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/d1_database"><code>cloudflare_d1_database</code></a> resource will no longer always try to recreate. You can now safely change the location hint for a D1 database without causing a destructive operation.</li>
</ul>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-api-improvements">API improvements</h4>
<p>We've also properly documented the <a href="/api/resources/workers/subresources/scripts/subresources/script_and_version_settings">Workers Script And Version Settings</a> in our public OpenAPI spec and SDKs.</p>


<h2 id="50-500ms-faster-d1-rest-api-requests"><a href="/changelog/post/2025-05-30-d1-rest-api-latency/">50-500ms Faster D1 REST API Requests</a></h2>
<p><em>2025-05-29</em></p>
<p>Users using Cloudflare's <a href="/api/resources/d1/">REST API</a> to query their D1 database can see lower end-to-end request latency now that D1 authentication is performed at the closest Cloudflare network data center that received the request. Previously, authentication required D1 REST API requests to proxy to Cloudflare's core, centralized data centers, which added network round trips and latency.</p>
<p>Latency improvements range from 50-500 ms depending on request location and <a href="/d1/configuration/data-location/">database location</a> and only apply to the REST API. REST API requests and databases outside the United States see a bigger benefit since Cloudflare's primary core data centers reside in the United States.</p>
<p>D1 query endpoints like <code>/query</code> and <code>/raw</code> have the most noticeable improvements since they no longer access Cloudflare's core data centers. D1 control plane endpoints such as those to create and delete databases see smaller improvements, since they still require access to Cloudflare's core data centers for other control plane metadata.</p>


<h2 id="d1-read-replication-public-beta"><a href="/changelog/post/2025-04-10-d1-read-replication-beta/">D1 Read Replication Public Beta</a></h2>
<p><em>2025-04-10</em></p>
<p>D1 read replication is available in public beta to help lower average latency and increase overall throughput for read-heavy applications like e-commerce websites or content management tools.</p>
<p>Workers can leverage read-only database copies, called read replicas, by using D1 <a href="/d1/best-practices/read-replication">Sessions API</a>. A session encapsulates all the queries from one logical session for your application. For example, a session may correspond to all queries coming from a particular web browser session. With Sessions API, D1 queries in a session are guaranteed to be <a href="/d1/best-practices/read-replication/#replica-lag-and-consistency-model">sequentially consistent</a> to avoid data consistency pitfalls. D1 <a href="/d1/reference/time-travel/#bookmarks">bookmarks</a> can be used from a previous session to ensure logical consistency between sessions.</p>
<pre><code class="language-ts">// retrieve bookmark from previous session stored in HTTP header&#10;const bookmark = request.headers.get(&quot;x-d1-bookmark&quot;) ?? &quot;first-unconstrained&quot;;&#10;&#10;const session = env.DB.withSession(bookmark);&#10;const result = await session&#10;	.prepare(`SELECT * FROM Customers WHERE CompanyName = &#x27;Bs Beverages&#x27;`)&#10;	.run();&#10;// store bookmark for a future session&#10;response.headers.set(&quot;x-d1-bookmark&quot;, session.getBookmark() ?? &quot;&quot;);&#10;</code></pre>
<p>Read replicas are automatically created by Cloudflare (currently one in each supported <a href="/d1/best-practices/read-replication/#read-replica-locations">D1 region</a>), are active/inactive based on query traffic, and are transparently routed to by Cloudflare at no additional cost.</p>
<p>To checkout D1 read replication, deploy the following Worker code using Sessions API, which will prompt you to create a D1 database and enable read replication on said database.</p>
<p><a href="https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/d1-starter-sessions-api"><img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare" /></a></p>
<p>To learn more about how read replication was implemented, go to our <a href="https://blog.cloudflare.com/d1-read-replication-beta">blog post</a>.</p>


<h2 id="40-60-faster-d1-worker-api-requests"><a href="/changelog/post/2025-01-07-d1-faster-query/">40-60% Faster D1 Worker API Requests</a></h2>
<p><em>2025-01-07</em></p>
<p>Users making <a href="/d1/">D1</a> requests via the <a href="/d1/worker-api/">Workers API</a> can see up to a 60% end-to-end latency improvement due to the removal of redundant network round trips needed for each request to a D1 database.</p>
<p><img src="/images/d1/faster-d1-worker-api.png" alt="D1 Worker API latency" /></p>
<p><em>p50, p90, and p95 request latency aggregated across entire D1 service. These latencies are a reference point and should not be viewed as your exact workload improvement.</em></p>
<p>This performance improvement benefits all D1 Worker API traffic, especially cross-region requests where network latency is an outsized latency factor. For example, a user in Europe talking to a database in North America. D1 <a href="/d1/configuration/data-location/#provide-a-location-hint">location hints</a> can be used to influence the geographic location of a database.</p>
<p>For more details on how D1 removed redundant round trips, see the D1 specific release note <a href="/d1/platform/release-notes/#2025-01-07">entry</a>.</p>



