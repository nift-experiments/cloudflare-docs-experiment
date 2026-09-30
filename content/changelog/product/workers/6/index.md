<h1 id="changelog">Changelog</h1>

<h2 id="one-click-access-protection-for-workers-now-creates-reusable-cloudflare-access-policies"><a href="/changelog/post/2025-12-03-reusable-access-policies/">One-click Access protection for Workers now creates reusable Cloudflare Access policies</a></h2>
<p><em>2025-12-04</em></p>
<p>Workers applications now use reusable <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access policies</a> to reduce duplication and simplify access management across multiple Workers.</p>
<p>Previously, enabling Cloudflare Access on a Worker created per-application policies, unique to each application. Now, we create reusable policies that can be shared across applications:</p>
<ul>
<li>
<p><strong>Preview URLs</strong>: All Workers preview URLs share a single &quot;Cloudflare Workers Preview URLs&quot; policy across your account. This policy is automatically created the first time you enable Access on any preview URL. By sharing a single policy across all preview URLs, you can configure access rules once and have them apply company-wide to all Workers which protect preview URLs. This makes it much easier to manage who can access preview environments without having to update individual policies for each Worker.</p>
</li>
<li>
<p><strong>Production workers.dev URLs</strong>: When enabled, each Worker gets its own reusable policy (named <code>&lt;worker-name&gt; - Production</code>) by default. We recognize production services often have different access requirements and having individual policies here makes it easier to configure service-to-service authentication or protect internal dashboards or applications with specific user groups. Keeping these policies separate gives you the flexibility to configure exactly the right access rules for each production service. When you disable Access on a production Worker, the associated policy is automatically cleaned up if it's not being used by other applications.</p>
</li>
</ul>
<p>This change reduces policy duplication, simplifies cross-company access management for preview environments, and provides the flexibility needed for production services. You can still customize access rules by editing the reusable policies in the Zero Trust dashboard.</p>
<p>To enable Cloudflare Access on your Worker:</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Workers &amp; Pages</strong>.</li>
<li>Select your Worker.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domains &amp; Routes</strong>.</li>
<li>For <code>workers.dev</code> or Preview URLs, click <strong>Enable Cloudflare Access</strong>.</li>
<li>Optionally, click <strong>Manage Cloudflare Access</strong> to customize the policy.</li>
</ol>
<p>For more information on configuring Cloudflare Access for Workers, refer to the <a href="/workers/configuration/routing/workers-dev/#manage-access-to-workersdev">Workers Access documentation</a>.</p>


<h2 id="agents-sdk-v0-2-24-with-resumable-streaming-mcp-improvements-and-schedule-fixes"><a href="/changelog/post/2025-11-26-agents-resumable-streaming/">Agents SDK v0.2.24 with resumable streaming, MCP improvements, and schedule fixes</a></h2>
<p><em>2025-11-26</em></p>
<p>The latest release of <a href="https://github.com/cloudflare/agents">@cloudflare/agents</a> brings resumable streaming, significant MCP client improvements, and critical fixes for schedules and Durable Object lifecycle management.</p>
<h4 id="2025-11-26-agents-resumable-streaming-resumable-streaming">Resumable streaming</h4>
<p><code>AIChatAgent</code> now supports resumable streaming, allowing clients to reconnect and continue receiving streamed responses without losing data. This is useful for:</p>
<ul>
<li>Long-running AI responses</li>
<li>Users on unreliable networks</li>
<li>Users switching between devices mid-conversation</li>
<li>Background tasks where users navigate away and return</li>
<li>Real-time collaboration where multiple clients need to stay in sync</li>
</ul>
<p>Streams are maintained across page refreshes, broken connections, and syncing across open tabs and devices.</p>
<h4 id="2025-11-26-agents-resumable-streaming-other-improvements">Other improvements</h4>
<ul>
<li>Default JSON schema validator added to MCP client</li>
<li><a href="https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/">Schedules</a> can now safely destroy the agent</li>
</ul>
<h4 id="2025-11-26-agents-resumable-streaming-mcp-client-api-improvements">MCP client API improvements</h4>
<p>The <code>MCPClientManager</code> API has been redesigned for better clarity and control:</p>
<ul>
<li><strong>New <code>registerServer()</code> method</strong>: Register MCP servers without immediately connecting</li>
<li><strong>New <code>connectToServer()</code> method</strong>: Establish connections to registered servers</li>
<li><strong>Improved reconnect logic</strong>: <code>restoreConnectionsFromStorage()</code> now properly handles failed connections</li>
</ul>
<pre><code class="language-ts">// Register a server to Agent&#10;const { id } = await this.mcp.registerServer({&#10;	name: &quot;my-server&quot;,&#10;	url: &quot;https://my-mcp-server.example.com&quot;,&#10;});&#10;&#10;// Connect when ready&#10;await this.mcp.connectToServer(id);&#10;&#10;// Discover tools, prompts and resources&#10;await this.mcp.discoverIfConnected(id);&#10;</code></pre>
<p>The SDK now includes a formalized <code>MCPConnectionState</code> enum with states: <code>idle</code>, <code>connecting</code>, <code>authenticating</code>, <code>connected</code>, <code>discovering</code>, and <code>ready</code>.</p>
<h4 id="2025-11-26-agents-resumable-streaming-enhanced-mcp-discovery">Enhanced MCP discovery</h4>
<p>MCP discovery fetches the available tools, prompts, and resources from an MCP server so your agent knows what capabilities are available. The <code>MCPClientConnection</code> class now includes a dedicated <code>discover()</code> method with improved reliability:</p>
<ul>
<li>Supports cancellation via AbortController</li>
<li>Configurable timeout (default 15s)</li>
<li>Discovery failures now throw errors immediately instead of silently continuing</li>
</ul>
<h4 id="2025-11-26-agents-resumable-streaming-bug-fixes">Bug fixes</h4>
<ul>
<li>Fixed a bug where <a href="https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/">schedules</a> meant to fire immediately with this.schedule(0, ...) or <code>this.schedule(new Date(), ...)</code> would not fire</li>
<li>Fixed an issue where schedules that took longer than 30 seconds would occasionally time out</li>
<li>Fixed SSE transport now properly forwards session IDs and request headers</li>
<li>Fixed AI SDK stream events conversion to UIMessageStreamPart</li>
</ul>
<h4 id="2025-11-26-agents-resumable-streaming-upgrade">Upgrade</h4>
<p>To update to the latest version:</p>
<pre><code class="language-sh">npm i agents@latest&#10;</code></pre>


<h2 id="environment-variable-limits-increase-for-workers-builds"><a href="/changelog/post/2025-11-21-builds-env-var-increase/">Environment variable limits increase for Workers Builds</a></h2>
<p><em>2025-11-21</em></p>
<p><a href="/workers/ci-cd/builds/">Workers Builds</a> now supports up to 64 environment variables, and each environment variable can be up to 5 KB in size. The previous limit was 5 KB total across all environment variables.</p>
<p>This change enables better support for complex build configurations, larger application settings, and more flexible CI/CD workflows.</p>
<p>For more details, refer to the <a href="/workers/ci-cd/builds/limits-and-pricing/#definitions">build limits documentation</a>.</p>


<h2 id="better-local-deployment-flow-for-cloudflare-workers"><a href="/changelog/post/2025-11-21-wrangler-deploy-remote-config-management/">Better local deployment flow for Cloudflare Workers</a></h2>
<p><em>2025-11-21</em></p>
<p>Until now, if a Worker had been previously deployed via the <a href="https://dash.cloudflare.com">Cloudflare Dashboard</a>, a subsequent deployment done via the Cloudflare Workers CLI, <a href="/workers/wrangler/"><strong>Wrangler</strong></a>
(through the <a href="/workers/wrangler/commands/general/#deploy"><code>deploy</code> command</a>), would allow the user to override the Worker's dashboard settings without providing details on
what dashboard settings would be lost.</p>
<p>Now instead, <code>wrangler deploy</code> presents a helpful representation of the differences between the <a href="/workers/wrangler/configuration/">local configuration</a>
and the remote dashboard settings, and offers to update your local configuration file for you.</p>
<p>See example below showing a before and after for <code>wrangler deploy</code> when a local configuration is expected to override a Worker's dashboard settings:</p>
<div class="nb-example"><h3 class="nb-component-title" id="2025-11-21-wrangler-deploy-remote-config-management-before">Before</h3>
@markup("md", "content/.markup/bodies/17791.md")</div>
<div class="nb-example"><h3 class="nb-component-title" id="2025-11-21-wrangler-deploy-remote-config-management-after">After</h3>
@markup("md", "content/.markup/bodies/17792.md")</div>
<p>Also, if instead Wrangler detects that a deployment would override remote dashboard settings but in an additive way, without modifying or removing any of them, it will simply proceed with the deployment without requesting any user interaction.</p>
<p>Update to <a href="/workers/wrangler/">Wrangler</a> v4.50.0 or greater to take advantage of this improved deploy flow.</p>


<h2 id="more-sql-aggregate-date-and-time-functions-available-in-workers-analytics-engine"><a href="/changelog/post/2025-11-12-analytics-engine-further-sql-enhancements/">More SQL aggregate, date and time functions available in Workers Analytics Engine</a></h2>
<p><em>2025-11-12</em></p>
<p>You can now perform more powerful queries directly in <a href="https://developers.cloudflare.com/analytics/analytics-engine/">Workers Analytics Engine</a> with a major expansion of our SQL function library.</p>
<p>Workers Analytics Engine allows you to ingest and store high-cardinality data at scale (such as custom analytics) and query your data through a simple SQL API.</p>
<p>Today, we've expanded Workers Analytics Engine's SQL capabilities with several new functions:</p>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/aggregate-functions/"><strong>New aggregate functions:</strong></a></p>
<ul>
<li><code>countIf()</code> - count the number of rows which satisfy a provided condition</li>
<li><code>sumIf()</code> - calculate a sum from rows which satisfy a provided condition</li>
<li><code>avgIf()</code> - calculate an average from rows which satisfy a provided condition</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/date-time-functions/"><strong>New date and time functions:</strong></a></p>
<ul>
<li><code>toYear()</code></li>
<li><code>toMonth()</code></li>
<li><code>toDayOfMonth()</code></li>
<li><code>toDayOfWeek()</code></li>
<li><code>toHour()</code></li>
<li><code>toMinute()</code></li>
<li><code>toSecond()</code></li>
<li><code>toStartOfYear()</code></li>
<li><code>toStartOfMonth()</code></li>
<li><code>toStartOfWeek()</code></li>
<li><code>toStartOfDay()</code></li>
<li><code>toStartOfHour()</code></li>
<li><code>toStartOfFifteenMinutes()</code></li>
<li><code>toStartOfTenMinutes()</code></li>
<li><code>toStartOfFiveMinutes()</code></li>
<li><code>toStartOfMinute()</code></li>
<li><code>today()</code></li>
<li><code>toYYYYMM()</code></li>
</ul>
<h4 id="2025-11-12-analytics-engine-further-sql-enhancements-ready-to-get-started">Ready to get started?</h4>
Whether you're building usage-based billing systems, customer analytics dashboards, or other custom analytics, these functions let you get the most out of your data. [Get started ](/analytics/analytics-engine/get-started/) with Workers Analytics Engine and explore all available functions in our [SQL reference documentation](/analytics/analytics-engine/sql-reference/).


<h2 id="select-wrangler-environments-using-the-cloudflare-env-environment-variable"><a href="/changelog/post/2025-11-09-cloudflare-env-variable/">Select Wrangler environments using the CLOUDFLARE_ENV environment variable</a></h2>
<p><em>2025-11-09</em></p>
<p>Wrangler now supports using the <code>CLOUDFLARE_ENV</code> <a href="/workers/wrangler/system-environment-variables/#supported-environment-variables">environment variable</a> to select the active <a href="/workers/wrangler/environments/">environment</a> for your Worker commands. This provides a more flexible way to manage environments, especially when working with build tools and CI/CD pipelines.</p>
<h4 id="2025-11-09-cloudflare-env-variable-what-s-new">What's new</h4>
<p><strong>Environment selection via environment variable:</strong></p>
<ul>
<li>Set <code>CLOUDFLARE_ENV</code> to specify which environment to use for Wrangler commands</li>
<li>Works with all Wrangler commands that support the <code>--env</code> flag</li>
<li>The <code>--env</code> command line argument takes precedence over the <code>CLOUDFLARE_ENV</code> environment variable</li>
</ul>
<h4 id="2025-11-09-cloudflare-env-variable-example-usage">Example usage</h4>
<pre><code class="language-bash">&#35; Deploy to the production environment using CLOUDFLARE_ENV&#10;CLOUDFLARE_ENV=production wrangler deploy&#10;&#10;&#35; Upload a version to the staging environment&#10;CLOUDFLARE_ENV=staging wrangler versions upload&#10;&#10;&#35; The --env flag takes precedence over CLOUDFLARE_ENV&#10;CLOUDFLARE_ENV=dev wrangler deploy --env production&#10;&#35; This will deploy to production, not dev&#10;</code></pre>
<h4 id="2025-11-09-cloudflare-env-variable-use-with-build-tools">Use with build tools</h4>
<p>The <code>CLOUDFLARE_ENV</code> environment variable is particularly useful when working with build tools like Vite. You can set the environment once during the build process, and it will be used for both building and deploying your Worker:</p>
<pre><code class="language-bash">&#35; Set the environment for both build and deploy&#10;CLOUDFLARE_ENV=production npm run build &amp; wrangler deploy&#10;</code></pre>
<p>When using <code>@cloudflare/vite-plugin</code>, the build process generates a <a href="/workers/wrangler/configuration/#generated-wrangler-configuration">&quot;redirected deploy config&quot;</a> that is flattened to only contain the active environment. Wrangler will validate that the environment specified matches the environment used during the build to prevent accidentally deploying a Worker built for one environment to a different environment.</p>
<h4 id="2025-11-09-cloudflare-env-variable-learn-more">Learn more</h4>
<ul>
<li><a href="/workers/wrangler/system-environment-variables/">System environment variables</a></li>
<li><a href="/workers/wrangler/environments/">Environments</a></li>
</ul>


<h2 id="workers-automatic-tracing-now-in-open-beta"><a href="/changelog/post/2025-11-07-automatic-tracing/">Workers automatic tracing, now in open beta</a></h2>
<p><em>2025-11-07</em></p>
<p>Enable automatic tracing on your Workers, giving you detailed metadata and timing information for every operation your Worker performs.</p>
<p><img src="/assets/upstream/images/workers-observability/R2_Screenshot.png" alt="Tracing example" /></p>
<p>Tracing helps you identify performance bottlenecks, resolve errors, and understand how your Worker interacts with other services on the Workers platform. You can now answer questions like:</p>
<ul>
<li>Which calls are slowing down my application?</li>
<li>Which queries to my database take the longest?</li>
<li>What happened within a request that resulted in an error?</li>
</ul>
<p><strong>You can now:</strong></p>
<ul>
<li>View traces alongside your logs in the Workers Observability dashboard</li>
<li>Export traces (and correlated logs) to any <a href="https://opentelemetry.io/docs/specs/otel/protocol/">OTLP-compatible destination</a>, such as <a href="/workers/observability/exporting-opentelemetry-data/honeycomb/">Honeycomb</a>, <a href="/workers/observability/exporting-opentelemetry-data/sentry/">Sentry</a> or <a href="/workers/observability/exporting-opentelemetry-data/grafana-cloud/">Grafana</a>, by configuring a tracing destination in the <a href="https://dash.cloudflare.com/?to=/:account/workers-and-pages/observability/destinations">Cloudflare dashboard</a></li>
<li>Analyze and query across span attributes (operation type, status, duration, errors)</li>
</ul>
<h4 id="2025-11-07-automatic-tracing-to-get-started-set">To get started, set:</h4>
<pre><code class="language-jsonc">{&#10;	&quot;observability&quot;: {&#10;		&quot;traces&quot;: {&#10;			&quot;enabled&quot;: true,&#10;		},&#10;	},&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17790.md")</aside>
<h4 id="2025-11-07-automatic-tracing-want-to-learn-more">Want to learn more?</h4>
<ul>
<li><a href="https://blog.cloudflare.com/workers-tracing-now-in-open-beta/">Read the announcement</a></li>
<li><a href="/workers/observability/traces/">Check out the documentation</a></li>
</ul>


<h2 id="d1-can-restrict-data-localization-with-jurisdictions"><a href="/changelog/post/2025-11-05-d1-jurisdiction/">D1 can restrict data localization with jurisdictions</a></h2>
<p><em>2025-11-05</em></p>
<p>You can now set a <a href="/d1/configuration/data-location/">jurisdiction</a> when creating a D1 database to guarantee where your database runs and stores data. Jurisdictions can help you comply with data localization regulations such as GDPR. Supported jurisdictions include <code>eu</code> and <code>fedramp</code>.</p>
<p>A jurisdiction can only be set at database creation time via wrangler, REST API or the UI and cannot be added/updated after the database already exists.</p>
<pre><code class="language-sh">npx wrangler@latest d1 create db-with-jurisdiction --jurisdiction eu&#10;</code></pre>
<pre><code class="language-sh">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/d1/database&quot; \&#10;     &#45;H &quot;Authorization: Bearer $TOKEN&quot; \&#10;     &#45;H &quot;Content-Type: application/json&quot; \&#10;     &#45;-data &#x27;{&quot;name&quot;: &quot;db-with-jurisdiction&quot;, &quot;jurisdiction&quot;: &quot;eu&quot; }&#x27;&#10;</code></pre>
<p>To learn more, visit D1's data location <a href="/d1/configuration/data-location/">documentation</a>.</p>


<h2 id="capture-wrangler-command-output-in-structured-format"><a href="/changelog/post/2025-11-03-wrangler-output-file/">Capture Wrangler command output in structured format</a></h2>
<p><em>2025-11-03</em></p>
<p>You can now capture Wrangler command output in a structured <a href="https://github.com/ndjson/ndjson-spec">ND-JSON</a> format by setting the <a href="/workers/wrangler/system-environment-variables/#supported-environment-variables"><code>WRANGLER_OUTPUT_FILE_PATH</code></a> or <a href="/workers/wrangler/system-environment-variables/#supported-environment-variables"><code>WRANGLER_OUTPUT_FILE_DIRECTORY</code></a> environment variables. This feature is particularly useful for CI/CD pipelines and automation tools that need programmatic access to deployment information such as worker names, version IDs, deployment URLs, and error details. Commands that support this feature include <a href="/workers/wrangler/commands/#deploy"><code>wrangler deploy</code></a>, <a href="/workers/wrangler/commands/#versions"><code>wrangler versions upload</code></a>, <a href="/workers/wrangler/commands/#versions"><code>wrangler versions deploy</code></a>, and <a href="/workers/wrangler/commands/#deploy-1"><code>wrangler pages deploy</code></a>.</p>


<h2 id="workers-websocket-message-size-limit-increased-from-1-mib-to-32-mib"><a href="/changelog/post/2025-10-31-increased-websocket-message-size-limit/">Workers WebSocket message size limit increased from 1 MiB to 32 MiB</a></h2>
<p><em>2025-10-31</em></p>
<p>Workers, including those using <a href="/durable-objects/">Durable Objects</a> and <a href="/browser-run/">Browser Rendering</a>, may now process WebSocket messages up to 32 MiB in size. Previously, this limit was 1 MiB.</p>
<p>This change allows Workers to handle use cases requiring large message sizes, such as processing Chrome Devtools Protocol messages.</p>
<p>For more information, please see the <a href="/durable-objects/platform/limits/#sqlite-backed-durable-objects-general-limits">Durable Objects startup limits</a>.</p>


<h2 id="increased-workflows-instance-and-concurrency-limits"><a href="/changelog/post/2025-10-28-raising-limits/">Increased Workflows instance and concurrency limits</a></h2>
<p><em>2025-10-31</em></p>
<p>We've raised the <a href="/workflows/">Cloudflare Workflows</a> account-level limits for all accounts on the <a href="/workers/platform/pricing/">Workers paid plan</a>:</p>
<ul>
<li><strong>Instance creation rate</strong> increased from 100 workflow instances per 10 seconds to 100 instances per second</li>
<li><strong>Concurrency limit</strong> increased from 4,500 to 10,000 workflow instances per account</li>
</ul>
<p>These increases mean you can create new instances up to 10x faster, and have more workflow instances concurrently executing. To learn more and get started with Workflows, refer to <a href="/workflows/get-started/guide/">the getting started guide</a>.</p>
<p>If your application requires a higher limit, fill out the <a href="/workers/platform/limits/">Limit Increase Request Form</a> or contact your account team. Please refer to <a href="/workflows/reference/pricing/">Workflows pricing</a> for more information.</p>


<h2 id="access-workers-preview-urls-from-the-build-details-page"><a href="/changelog/post/2025-10-30-builds-preview/">Access Workers preview URLs from the Build details page</a></h2>
<p><em>2025-10-30</em></p>
<p>You can now access <a href="/workers/versions-and-deployments/preview-urls/">preview URLs</a> directly from the build details page, making it easier to test your changes when reviewing builds in the dashboard.</p>
<p><img src="/assets/upstream/images/changelog/workers/builds-preview-button.png" alt="preview button" /></p>
<p><strong>What's new</strong></p>
<ul>
<li>A <strong>Preview</strong> button now appears in the top-right corner of the build details page for successful builds</li>
<li>Click it to instantly open the latest preview URL</li>
<li>Matches the same experience you're familiar with from Pages</li>
</ul>


<h2 id="automatic-resource-provisioning-for-kv-r2-and-d1"><a href="/changelog/post/2025-10-24-automatic-resource-provisioning/">Automatic resource provisioning for KV, R2, and D1</a></h2>
<p><em>2025-10-24</em></p>
<p>Previously, if you wanted to develop or deploy a worker with attached resources, you'd have to first manually create the desired resources. Now, if your Wrangler configuration file includes a KV namespace, D1 database, or R2 bucket that does not yet exist on your account, you can develop locally and deploy your application seamlessly, without having to run additional commands.</p>
<p>Automatic provisioning is launching as an open beta, and we'd love to hear your feedback to help us make improvements! It currently works for KV, R2, and D1 bindings. You can disable the feature using the <code>--no-x-provision</code> flag.</p>
<p>To use this feature, update to wrangler@4.45.0 and add bindings to your config file <em>without</em> resource IDs e.g.:</p>
<pre><code class="language-jsonc">{&#10;	&quot;kv_namespaces&quot;: [{ &quot;binding&quot;: &quot;MY_KV&quot; }],&#10;	&quot;d1_databases&quot;: [{ &quot;binding&quot;: &quot;MY_DB&quot; }],&#10;	&quot;r2_buckets&quot;: [{ &quot;binding&quot;: &quot;MY_R2&quot; }],&#10;}&#10;</code></pre>
<p><code>wrangler dev</code> will then automatically create these resources for you locally, and on your next run of <code>wrangler deploy</code>, Wrangler will call the Cloudflare API to create the requested resources and link them to your Worker.</p>
<p>Though resource IDs will be automatically written back to your Wrangler config file after resource creation, resources will stay linked across future deploys even without adding the resource IDs to the config file. This is especially useful for shared templates, which now no longer need to include account-specific resource IDs when adding a binding.</p>


<h2 id="build-tanstack-start-apps-with-the-cloudflare-vite-plugin"><a href="/changelog/post/2025-10-24-tanstack-start/">Build TanStack Start apps with the Cloudflare Vite plugin</a></h2>
<p><em>2025-10-24</em></p>
<p>The <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a> now supports <a href="https://tanstack.com/start/">TanStack Start</a> apps.
Get started with new or existing projects.</p>
<h4 id="2025-10-24-tanstack-start-new-projects">New projects</h4>
<p>Create a new TanStack Start project that uses the Cloudflare Vite plugin via the <code>create-cloudflare</code> CLI:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- my-tanstack-start-app --framework=tanstack-start</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- my-tanstack-start-app --framework=tanstack-start" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare my-tanstack-start-app --framework=tanstack-start</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare my-tanstack-start-app --framework=tanstack-start" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest my-tanstack-start-app --framework=tanstack-start</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest my-tanstack-start-app --framework=tanstack-start" aria-label="Copy to clipboard">Copy</button></div></div>
<h4 id="2025-10-24-tanstack-start-existing-projects">Existing projects</h4>
<p>Migrate an existing TanStack Start project to use the Cloudflare Vite plugin:</p>
<ol>
<li>Install <code>@cloudflare/vite-plugin</code> and <code>wrangler</code></li>
</ol>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/vite-plugin wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/vite-plugin wrangler" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/vite-plugin wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/vite-plugin wrangler" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/vite-plugin wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/vite-plugin wrangler" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/vite-plugin wrangler</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/vite-plugin wrangler" aria-label="Copy to clipboard">Copy</button></div></div>
<ol start="2">
<li>Add the Cloudflare plugin to your Vite config</li>
</ol>
<pre><code class="language-ts">import { defineConfig } from &quot;vite&quot;;&#10;import { tanstackStart } from &quot;@tanstack/react-start/plugin/vite&quot;;&#10;import viteReact from &quot;@vitejs/plugin-react&quot;;&#10;import { cloudflare } from &quot;@cloudflare/vite-plugin&quot;;&#10;&#10;export default defineConfig({&#10;	plugins: [&#10;		cloudflare({ viteEnvironment: { name: &quot;ssr&quot; } }),&#10;		tanstackStart(),&#10;		viteReact(),&#10;	],&#10;});&#10;</code></pre>
<ol start="3">
<li>Add your Worker config file</li>
</ol>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17789.md")</div>
<ol start="4">
<li>Modify the scripts in your <code>package.json</code></li>
</ol>
<pre><code class="language-json">{&#10;	&quot;scripts&quot;: {&#10;		&quot;dev&quot;: &quot;vite dev&quot;,&#10;		&quot;build&quot;: &quot;vite build &amp;&amp; tsc --noEmit&quot;,&#10;		&quot;start&quot;: &quot;node .output/server/index.mjs&quot;,&#10;		&quot;preview&quot;: &quot;vite preview&quot;,&#10;		&quot;deploy&quot;: &quot;npm run build &amp;&amp; wrangler deploy&quot;,&#10;		&quot;cf-typegen&quot;: &quot;wrangler types&quot;&#10;	}&#10;}&#10;</code></pre>
<p>See the <a href="/workers/framework-guides/web-apps/tanstack-start/">TanStack Start framework guide</a> for more info.</p>


<h2 id="workers-preview-url-default-behavior-now-matches-your-workers-dev-setting"><a href="/changelog/post/2025-10-23-preview-url-default-behavior/">Workers Preview URL default behavior now matches your workers.dev setting</a></h2>
<p><em>2025-10-23</em></p>
<p>We have updated the default behavior for Cloudflare Workers <a href="/workers/versions-and-deployments/preview-urls/">Preview URLs</a>. <strong>Going forward, if a preview URL setting is not <a href="/workers/versions-and-deployments/preview-urls/#toggle-preview-urls-enable-or-disable">explicitly configured</a> during deployment, its default behavior will automatically match the setting of your <a href="/workers/configuration/routing/workers-dev/"><code>workers.dev</code> subdomain</a>.</strong></p>
<p>This change is intended to provide a more intuitive and secure experience by aligning your preview URL's default state with your <code>workers.dev</code> configuration to prevent cases where a preview URL might remain public even after you disabled your <code>workers.dev</code> route.</p>
<p><strong>What this means for you:</strong></p>
<ul>
<li><strong>If neither setting is configured:</strong> both the workers.dev route and the preview URL will default to enabled</li>
<li><strong>If your workers.dev route is enabled and you do not explicitly set Preview URLs to enabled or disabled:</strong> Preview URLs will default to enabled</li>
<li><strong>If your workers.dev route is disabled and you do not explicitly set Preview URLs to enabled or disabled:</strong> Preview URLs will default to disabled</li>
</ul>
<p>You can override the default setting by explicitly enabling or disabling the preview URL in your Worker's configuration through the <a href="/api/resources/workers/subresources/scripts/subresources/subdomain/">API</a>, <a href="/workers/versions-and-deployments/preview-urls/#from-the-dashboard">Dashboard</a>, or <a href="/workers/versions-and-deployments/preview-urls/#from-the-wrangler-configuration-file">Wrangler</a>.</p>
<p><strong>Wrangler Version Behavior</strong></p>
<p>The default behavior depends on the version of Wrangler you are using. This new logic applies to the latest version. Here is a summary of the behavior across different versions:</p>
<ul>
<li><strong>Before v4.34.0:</strong> Preview URLs defaulted to enabled, regardless of the workers.dev setting.</li>
<li><strong>v4.34.0 up to (but not including) v4.44.0:</strong> Preview URLs defaulted to disabled, regardless of the workers.dev setting.</li>
<li><strong>v4.44.0 or later:</strong> Preview URLs now default to matching your workers.dev setting.</li>
</ul>
<p><strong>Why we’re making this change</strong></p>
<p>In July, <a href="/changelog/2025-07-23-workers-preview-urls/">we introduced preview URLs to Workers</a>, which let you preview code changes before deploying to production. This made disabling your Worker’s workers.dev URL an ambiguous action — the preview URL, served as a subdomain of <code>workers.dev</code> (ex: <code>preview-id-worker-name.account-name.workers.dev</code>) would still be live even if you had disabled your Worker’s <code>workers.dev</code> route. If you misinterpreted what it meant to disable your <code>workers.dev</code> route, you might unintentionally leave preview URLs enabled when you didn’t mean to, and expose them to the public Internet.</p>
<p>To address this, we made a <a href="/changelog/2025-09-17-update-preview-url-setting/">one-time update</a> to disable preview URLs on existing Workers that had their workers.dev route disabled and changed the default behavior to be disabled for all new deployments where a preview URL setting was not explicitly configured.</p>
<p>While this change helped secure many customers, it was disruptive for customers who keep their <code>workers.dev</code> route enabled and actively use the preview functionality, as it now required them to explicitly enable preview URLs on every redeployment.This new, more intuitive behavior ensures that your preview URL settings align with your <code>workers.dev</code> configuration by default, providing a more secure and predictable experience.</p>
<p><strong>Securing access to <code>workers.dev</code> and preview URL endpoints</strong></p>
<p>To further secure your <code>workers.dev</code> subdomain and preview URL, you can <a href="/changelog/2025-10-03-one-click-access-for-workers/">enable Cloudflare Access with a single click</a> in your Worker's settings to limit access to specific users or groups.</p>


<h2 id="view-and-edit-durable-object-data-in-ui-with-data-studio-beta"><a href="/changelog/post/2025-10-16-durable-objects-data-studio/">View and edit Durable Object data in UI with Data Studio (Beta)</a></h2>
<p><em>2025-10-16</em></p>
<p><img src="/assets/upstream/images/workers/changelog/do-data-studio.png" alt="Screenshot of Durable Objects Data Studio" /></p>
<p>You can now view and write to each Durable Object's storage using a UI editor on the Cloudflare dashboard. Only Durable Objects using <a href="/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class">SQLite storage</a> can use Data Studio.</p>
<div class="nb-dash-button"></div>
<p>Data Studio unlocks easier data access with Durable Objects for prototyping application data models to debugging production storage usage. Before, querying your Durable Objects data required deploying a Worker.</p>
<p>To access a Durable Object, you can provide an object's unique name or ID generated by Cloudflare. Data Studio requires you to have at least the <code>Workers Platform Admin</code> role, and all queries are captured with audit logging for your security and compliance needs. Queries executed by Data Studio send requests to your remote, deployed objects and incur normal usage billing.</p>
<p>To learn more, visit the Data Studio <a href="/durable-objects/observability/data-studio/">documentation</a>. If you have feedback or suggestions for the new Data Studio, please share your experience on <a href="https://discord.com/channels/595317990191398933/773219443911819284">Discord</a></p>


<h2 id="worker-startup-time-limit-increased-to-1-second"><a href="/changelog/post/2025-10-10-increased-startup-time/">Worker startup time limit increased to 1 second</a></h2>
<p><em>2025-10-10</em></p>
<p>You can now upload a Worker that takes up 1 second to parse and execute its global scope. Previously, startup time was limited to 400 ms.</p>
<p>This allows you to run Workers that import more complex packages and execute more code prior to requests being handled.</p>
<p>For more information, see the documentation on <a href="/workers/platform/limits/#worker-startup-time">Workers startup limits</a>.</p>


<h2 id="you-can-now-deploy-full-stack-apps-on-workers-using-terraform"><a href="/changelog/post/2025-10-09-assets-terraform/">You can now deploy full-stack apps on Workers using Terraform</a></h2>
<p><em>2025-10-09</em></p>
<p>You can now upload Workers with <a href="/workers/static-assets/">static assets</a> (like HTML, CSS, JavaScript, images) with the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs">Cloudflare Terraform provider v5.11.0</a>, making it even easier to deploy and manage full-stack apps with IaC.</p>
<p><strong>Previously</strong>, you couldn't use Terraform to upload static assets without writing custom scripts to handle generating an <a href="/workers/static-assets/direct-upload/#upload-manifest">asset manifest</a>, calling the <a href="/workers/static-assets/direct-upload/#upload-static-assets">Cloudflare API to upload assets in chunks</a>, and handling change detection.</p>
<p><strong>Now</strong>, you simply define the directory where your assets are built, and we handle the rest. Check out the <a href="/changelog/#examples">examples</a> for what this looks like in Terraform configuration.</p>
<p>You can get started today with <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs">the Cloudflare Terraform provider (v5.11.0)</a>, using either the existing <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script"><code>cloudflare_workers_script</code> resource</a>, or the beta <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker_version"><code>cloudflare_worker_version</code> resource</a>.</p>
<h4 id="2025-10-09-assets-terraform-examples">Examples</h4>
<h4 id="2025-10-09-assets-terraform-with-cloudflare-workers-script">With <code>cloudflare_workers_script</code></h4>
<p>Here's how you can use the existing <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/workers_script"><code>cloudflare_workers_script</code></a> resource to upload your Worker code and assets in one shot.</p>
<pre><code class="language-hcl">resource &quot;cloudflare_workers_script&quot; &quot;my_app&quot; {&#10;  account_id  = var.account_id&#10;  script_name = &quot;my-app&quot;&#10;&#10;  content_file   = &quot;./dist/worker/index.js&quot;&#10;  content_sha256 = filesha256(&quot;./dist/worker/index.js&quot;)&#10;  main_module    = &quot;index.js&quot;&#10;&#10;  &#35; Just point to your assets directory - that&#x27;s it!&#10;  assets = {&#10;    directory = &quot;./dist/static&quot;&#10;  }&#10;}&#10;</code></pre>
<h4 id="2025-10-09-assets-terraform-with-cloudflare-worker-cloudflare-worker-version-and-cloudflare-workers-deployment">With <code>cloudflare_worker</code>, <code>cloudflare_worker_version</code>, and <code>cloudflare_workers_deployment</code></h4>
<p>And here's an example using the beta <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/worker_version"><code>cloudflare_worker_version</code></a> resource, alongside the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker"><code>cloudflare_worker</code></a> and <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/workers_deployment"><code>cloudflare_workers_deployment</code></a> resources:</p>
<pre><code class="language-hcl">&#10;&#35; This tracks the existence of your Worker, so that you&#10;&#35; can upload code and assets separately from tracking Worker state.&#10;&#10;resource &quot;cloudflare_worker&quot; &quot;my_app&quot; {&#10;  account_id = var.account_id&#10;  name       = &quot;my-app&quot;&#10;}&#10;&#10;resource &quot;cloudflare_worker_version&quot; &quot;my_app_version&quot; {&#10;  account_id = var.account_id&#10;  worker_id  = cloudflare_worker.my_app.id&#10;&#10;  &#35; Just point to your assets directory - that&#x27;s it!&#10;  assets = {&#10;    directory = &quot;./dist/static&quot;&#10;  }&#10;&#10;  modules = [{&#10;    name         = &quot;index.js&quot;&#10;    content_file = &quot;./dist/worker/index.js&quot;&#10;    content_type = &quot;application/javascript+module&quot;&#10;  }]&#10;}&#10;&#10;resource &quot;cloudflare_workers_deployment&quot; &quot;my_app_deployment&quot; {&#10;  account_id  = var.account_id&#10;  script_name = cloudflare_worker.my_app.name&#10;&#10;  strategy = &quot;percentage&quot;&#10;  versions = [{&#10;    version_id = cloudflare_worker_version.my_app_version.id&#10;    percentage = 100&#10;  }]&#10;}&#10;</code></pre>
<h4 id="2025-10-09-assets-terraform-what-s-changed">What's changed</h4>
Under the hood, the Cloudflare Terraform provider now handles the same logic that Wrangler uses for static asset uploads. This includes scanning your assets directory, computing hashes for each file, generating a manifest with file metadata, and calling the Cloudflare API to upload any missing files in chunks. We support large directories with parallel uploads and chunking, and when the asset manifest hash changes, we detect what's changed and trigger an upload for *only* those changed files.
<h4 id="2025-10-09-assets-terraform-try-it-out">Try it out</h4>
-  Get started with [the Cloudflare Terraform provider (v5.11.0)](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs)
- You can use either the existing [`cloudflare_workers_script` resource](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script) to upload your Worker code and assets in one resource.
- Or you can use the new beta [`cloudflare_worker_version` resource](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker_version) (along with the [`cloudflare_worker`](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker) and [`cloudflare_workers_deployment`](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/workers_deployment)) resources to more granularly control the lifecycle of each Worker resource.


<h2 id="you-can-now-deploy-and-manage-workflows-in-terraform"><a href="/changelog/post/2025-10-09-workflows-terraform/">You can now deploy and manage Workflows in Terraform</a></h2>
<p><em>2025-10-09</em></p>
<p>You can now create and manage <a href="/workflows/">Workflows</a> using Terraform, now supported in the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workflow">Cloudflare Terraform provider v5.11.0</a>. Workflows allow you to build durable, multi-step applications -- without needing to worry about retrying failed tasks or managing infrastructure.</p>
<p>Now, you can deploy and manage Workflows through Terraform using the new <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workflow"><code>cloudflare_workflow</code> resource</a>:</p>
<pre><code class="language-hcl">resource &quot;cloudflare_workflow&quot; &quot;my_workflow&quot; {&#10;  account_id    = var.account_id&#10;  workflow_name = &quot;my-workflow&quot;&#10;  class_name    = &quot;MyWorkflow&quot;&#10;  script_name   = &quot;my-worker&quot;&#10;}&#10;</code></pre>
<h4 id="2025-10-09-workflows-terraform-examples">Examples</h4>
Here are full examples of how to configure `cloudflare_workflow` in Terraform, using the existing [`cloudflare_workers_script` resource](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script), and the beta [`cloudflare_worker_version` resource](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker_version).
<h4 id="2025-10-09-workflows-terraform-with-cloudflare-workflow-and-cloudflare-workers-script">With <code>cloudflare_workflow</code> and <code>cloudflare_workers_script</code></h4>
<pre><code class="language-hcl">resource &quot;cloudflare_workers_script&quot; &quot;workflow_worker&quot; {&#10;  account_id  = var.cloudflare_account_id&#10;  script_name = &quot;my-workflow-worker&quot;&#10;&#10;  content_file   = &quot;${path.module}/../dist/worker/index.js&quot;&#10;  content_sha256 = filesha256(&quot;${path.module}/../dist/worker/index.js&quot;)&#10;  main_module    = &quot;index.js&quot;&#10;}&#10;&#10;resource &quot;cloudflare_workflow&quot; &quot;workflow&quot; {&#10;  account_id    = var.cloudflare_account_id&#10;  workflow_name = &quot;my-workflow&quot;&#10;  class_name    = &quot;MyWorkflow&quot;&#10;  script_name   = cloudflare_workers_script.workflow_worker.script_name&#10;}&#10;</code></pre>
<h4 id="2025-10-09-workflows-terraform-with-cloudflare-workflow-and-the-new-beta-resources">With <code>cloudflare_workflow</code>, and the new beta resources</h4>
You can more granularly control the lifecycle of each Worker resource using the beta [`cloudflare_worker_version`](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/worker_version) resource, alongside the [`cloudflare_worker`](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/worker) and [`cloudflare_workers_deployment`](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs/resources/workers_deployment) resources.
<pre><code class="language-hcl">&#10;resource &quot;cloudflare_worker&quot; &quot;workflow_worker&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  name       = &quot;my-workflow-worker&quot;&#10;}&#10;&#10;resource &quot;cloudflare_worker_version&quot; &quot;workflow_worker_version&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  worker_id  = cloudflare_worker.workflow_worker.id&#10;&#10;  main_module         = &quot;index.js&quot;&#10;&#10;  modules = [{&#10;    name         = &quot;index.js&quot;&#10;    content_file = &quot;${path.module}/../dist/worker/index.js&quot;&#10;    content_type = &quot;application/javascript+module&quot;&#10;  }]&#10;}&#10;&#10;resource &quot;cloudflare_workers_deployment&quot; &quot;workflow_deployment&quot; {&#10;  account_id  = var.cloudflare_account_id&#10;  script_name = cloudflare_worker.workflow_worker.name&#10;&#10;  strategy = &quot;percentage&quot;&#10;  versions = [{&#10;    version_id = cloudflare_worker_version.workflow_worker_version.id&#10;    percentage = 100&#10;  }]&#10;}&#10;&#10;resource &quot;cloudflare_workflow&quot; &quot;my_workflow&quot; {&#10;  account_id    = var.cloudflare_account_id&#10;  workflow_name = &quot;my-workflow&quot;&#10;  class_name    = &quot;MyWorkflow&quot;&#10;  script_name   = cloudflare_worker.workflow_worker.name&#10;}&#10;</code></pre>
<h4 id="2025-10-09-workflows-terraform-try-it-out">Try it out</h4>
-  Get started with [the Cloudflare Terraform provider (v5.11.0)](https://registry.terraform.io/providers/cloudflare/cloudflare/5.11.0/docs) and the new [`cloudflare_workflow` resource](https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workflow).


<h2 id="new-overview-page-for-cloudflare-workers"><a href="/changelog/post/2025-10-06-new-worker-overview-page/">New Overview Page for Cloudflare Workers</a></h2>
<p><em>2025-10-07</em></p>
<p><img src="/assets/upstream/images/workers/changelog/workers-overview.png" alt="Screenshot of the Workers overview page in the Cloudflare dashboard" /></p>
<p>Each of your Workers now has a new overview page in the Cloudflare dashboard.</p>
<p>The goal is to make it easier to understand your Worker without digging through multiple tabs. Think of it as a new home base, a place to get a high-level overview on what's going on.</p>
<p>It's the first place you land when you open a Worker in the dashboard, and it gives you an immediate view of what’s going on. You can see requests, errors, and CPU time at a glance. You can view and add bindings, and see recent versions of your app, including who published them.</p>
<p>Navigation is also simpler, with visually distinct tabs at the top of the page. At the bottom right you'll find guided steps for what to do next that are based on the state of your Worker, such as adding a <a href="/workers/runtime-apis/bindings/">binding</a> or connecting a custom domain.</p>
<p>We plan to add more here over time. Better insights, more controls, and ways to manage your Worker from one page.</p>
<p>If you have feedback or suggestions for the new Overview page or your Cloudflare Workers experience in general, we'd love to hear from you. Join the Cloudflare developer community on <a href="https://discord.com/channels/595317990191398933/1064502845061210152">Discord</a>.</p>


<h2 id="one-click-cloudflare-access-for-workers"><a href="/changelog/post/2025-10-03-one-click-access-for-workers/">One-click Cloudflare Access for Workers</a></h2>
<p><em>2025-10-03</em></p>
<p>You can now enable <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> for your <a href="/workers/configuration/routing/workers-dev/"><code>workers.dev</code></a> and <a href="/workers/versions-and-deployments/preview-urls/">Preview URLs</a> in a single click.</p>
<p><img src="/assets/upstream/images/workers/changelog/workers-access.png" alt="Screenshot of the Enable/Disable Cloudflare Access button on the workers.dev route settings page" /></p>
<p>Access allows you to limit access to your Workers to specific users or groups. You can limit access to yourself, your teammates, your organization, or anyone else you specify in your <a href="/cloudflare-one/access-controls/policies/">Access policy</a>.</p>
<p>To enable Cloudflare Access:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>Overview</strong>, select your Worker.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domains &amp; Routes</strong>.</li>
<li>For <code>workers.dev</code> or Preview URLs, click <strong>Enable Cloudflare Access</strong>.</li>
<li>Optionally, to configure the Access application, click <strong>Manage Cloudflare Access</strong>. There, you can change the email addresses you want to authorize. View <a href="/cloudflare-one/access-controls/policies/#selectors">Access policies</a> to learn about configuring alternate rules.</li>
</ol>
<p>To fully secure your application, it is important that you validate the JWT that Cloudflare Access adds to the <code>Cf-Access-Jwt-Assertion</code> header on the incoming request.</p>
<p>The following code will validate the JWT using the <a href="https://www.npmjs.com/package/jose">jose NPM package</a>:</p>
<pre><code class="language-javascript">import { jwtVerify, createRemoteJWKSet } from &quot;jose&quot;;&#10;&#10;export default {&#10;	async fetch(request, env, ctx) {&#10;		// Verify the POLICY_AUD environment variable is set&#10;		if (!env.POLICY_AUD) {&#10;			return new Response(&quot;Missing required audience&quot;, {&#10;				status: 403,&#10;				headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; },&#10;			});&#10;		}&#10;&#10;		// Get the JWT from the request headers&#10;		const token = request.headers.get(&quot;cf-access-jwt-assertion&quot;);&#10;&#10;		// Check if token exists&#10;		if (!token) {&#10;			return new Response(&quot;Missing required CF Access JWT&quot;, {&#10;				status: 403,&#10;				headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; },&#10;			});&#10;		}&#10;&#10;		try {&#10;			// Create JWKS from your team domain&#10;			const JWKS = createRemoteJWKSet(&#10;				new URL(`${env.TEAM_DOMAIN}/cdn-cgi/access/certs`),&#10;			);&#10;&#10;			// Verify the JWT&#10;			const { payload } = await jwtVerify(token, JWKS, {&#10;				issuer: env.TEAM_DOMAIN,&#10;				audience: env.POLICY_AUD,&#10;			});&#10;&#10;			// Token is valid, proceed with your application logic&#10;			return new Response(`Hello ${payload.email || &quot;authenticated user&quot;}!`, {&#10;				headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; },&#10;			});&#10;		} catch (error) {&#10;			// Token verification failed&#10;			return new Response(`Invalid token: ${error.message}`, {&#10;				status: 403,&#10;				headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; },&#10;			});&#10;		}&#10;	},&#10;};&#10;</code></pre>
<h4 id="2025-10-03-one-click-access-for-workers-required-environment-variables">Required environment variables</h4>
<p>Add these <a href="/workers/configuration/environment-variables/">environment variables</a> to your Worker:</p>
<ul>
<li><code>POLICY_AUD</code>: Your application's AUD tag</li>
<li><code>TEAM_DOMAIN</code>: <code>https://&lt;your-team-name&gt;.cloudflareaccess.com</code></li>
</ul>
<p>Both of these appear in the modal that appears when you enable Cloudflare Access.</p>
<p>You can set these variables by adding them to your Worker's <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>, or via the Cloudflare dashboard under <strong>Workers &amp; Pages</strong> &gt; <strong>your-worker</strong> &gt; <strong>Settings</strong> &gt; <strong>Environment Variables</strong>.</p>


<h2 id="workers-analytics-engine-adds-supports-for-new-sql-functions"><a href="/changelog/post/2025-09-26-analytics-engine-sql-enhancements/">Workers Analytics Engine adds supports for new SQL functions</a></h2>
<p><em>2025-10-02</em></p>
<p>You can now perform more powerful queries directly in <a href="https://developers.cloudflare.com/analytics/analytics-engine/">Workers Analytics Engine</a> with a major expansion of our SQL function library.</p>
<p>Workers Analytics Engine allows you to ingest and store high-cardinality data at scale (such as custom analytics) and query your data through a simple SQL API.</p>
<p>Today, we've expanded Workers Analytics Engine's SQL capabilities with several new functions:</p>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/aggregate-functions/"><strong>New aggregate functions:</strong></a></p>
<ul>
<li><code>argMin()</code> - Returns the value associated with the minimum in a group</li>
<li><code>argMax()</code> - Returns the value associated with the maximum in a group</li>
<li><code>topK()</code> - Returns an array of the most frequent values in a group</li>
<li><code>topKWeighted()</code> - Returns an array of the most frequent values in a group using weights</li>
<li><code>first_value()</code> - Returns the first value in an ordered set of values within a partition</li>
<li><code>last_value()</code> - Returns the last value in an ordered set of values within a partition</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/bit-functions/"><strong>New bit functions:</strong></a></p>
<ul>
<li><code>bitAnd()</code> - Returns the bitwise AND of two expressions</li>
<li><code>bitCount()</code> - Returns the number of bits set to one in the binary representation of a number</li>
<li><code>bitHammingDistance()</code> - Returns the number of bits that differ between two numbers</li>
<li><code>bitNot()</code> - Returns a number with all bits flipped</li>
<li><code>bitOr()</code> - Returns the inclusive bitwise OR of two expressions</li>
<li><code>bitRotateLeft()</code> - Rotates all bits in a number left by specified positions</li>
<li><code>bitRotateRight()</code> - Rotates all bits in a number right by specified positions</li>
<li><code>bitShiftLeft()</code> - Shifts all bits in a number left by specified positions</li>
<li><code>bitShiftRight()</code> - Shifts all bits in a number right by specified positions</li>
<li><code>bitTest()</code> - Returns the value of a specific bit in a number</li>
<li><code>bitXor()</code> - Returns the bitwise exclusive-or of two expressions</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/mathematical-functions/"><strong>New mathematical functions:</strong></a></p>
<ul>
<li><code>abs()</code> - Returns the absolute value of a number</li>
<li><code>log()</code> - Computes the natural logarithm of a number</li>
<li><code>round()</code> - Rounds a number to a specified number of decimal places</li>
<li><code>ceil()</code> - Rounds a number up to the nearest integer</li>
<li><code>floor()</code> - Rounds a number down to the nearest integer</li>
<li><code>pow()</code> - Returns a number raised to the power of another number</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/string-functions/"><strong>New string functions:</strong></a></p>
<ul>
<li><code>lowerUTF8()</code> - Converts a string to lowercase using UTF-8 encoding</li>
<li><code>upperUTF8()</code> - Converts a string to uppercase using UTF-8 encoding</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/encoding-functions/"><strong>New encoding functions:</strong></a></p>
<ul>
<li><code>hex()</code> - Converts a number to its hexadecimal representation</li>
<li><code>bin()</code> - Converts a string to its binary representation</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/type-conversion-functions/"><strong>New type conversion functions:</strong></a></p>
<ul>
<li><code>toUInt8()</code> - Converts any numeric expression, or expression resulting in a string representation of a decimal, into an unsigned 8 bit integer</li>
</ul>
<h4 id="2025-09-26-analytics-engine-sql-enhancements-ready-to-get-started">Ready to get started?</h4>
Whether you're building usage-based billing systems, customer analytics dashboards, or other custom analytics, these functions let you get the most out of your data. [Get started ](/analytics/analytics-engine/get-started/) with Workers Analytics Engine and explore all available functions in our [SQL reference documentation](/analytics/analytics-engine/sql-reference/).


<h2 id="automatic-loopback-bindings-via-ctx-exports"><a href="/changelog/post/2025-09-26-ctx-exports/">Automatic loopback bindings via ctx.exports</a></h2>
<p><em>2025-09-26</em></p>
<p>The <a href="/workers/runtime-apis/context/#exports"><code>ctx.exports</code> API</a> contains automatically-configured bindings corresponding to your Worker's top-level exports. For each top-level export extending <code>WorkerEntrypoint</code>, <code>ctx.exports</code> will contain a <a href="/workers/runtime-apis/bindings/service-bindings">Service Binding</a> by the same name, and for each export extending <code>DurableObject</code> (and for which storage has been configured via a <a href="/durable-objects/reference/durable-objects-migrations/">migration</a>), <code>ctx.exports</code> will contain a <a href="/durable-objects/api/namespace/">Durable Object namespace binding</a>. This means you no longer have to configure these bindings explicitly in <code>wrangler.jsonc</code>/<code>wrangler.toml</code>.</p>
<p>Example:</p>
<pre><code class="language-js">import { WorkerEntrypoint } from &quot;cloudflare:workers&quot;;&#10;&#10;export class Greeter extends WorkerEntrypoint {&#10;  greet(name) {&#10;    return `Hello, ${name}!`;&#10;  }&#10;}&#10;&#10;export default {&#10;  async fetch(request, env, ctx) {&#10;    let greeting = await ctx.exports.Greeter.greet(&quot;World&quot;)&#10;    return new Response(greeting);&#10;  }&#10;}&#10;</code></pre>
<p>At present, you must use <a href="/workers/configuration/compatibility-flags#enable-ctxexports">the <code>enable_ctx_exports</code> compatibility flag</a> to enable this API, though it will be on by default in the future.</p>
<p><a href="/workers/runtime-apis/context/#exports">See the API reference for more information.</a></p>


<h2 id="improved-support-for-running-multiple-workers-with-wrangler-dev"><a href="/changelog/post/2025-09-23-wrangler-dev-multi-config-cross-command-support/">Improved support for running multiple Workers with `wrangler dev`</a></h2>
<p><em>2025-09-23</em></p>
<p>You can run multiple Workers in a single dev command by passing multiple config files to <code>wrangler dev</code>:</p>
<pre><code class="language-sh">wrangler dev --config ./web/wrangler.jsonc --config ./api/wrangler.jsonc&#10;</code></pre>
<p>Previously, if you ran the command above and then also ran wrangler dev for a different Worker, the Workers running in separate wrangler dev sessions could not communicate with each other. This prevented you from being able to use <a href="https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/">Service Bindings</a> and <a href="https://developers.cloudflare.com/workers/observability/logs/tail-workers/">Tail Workers</a> in local development, when running separate wrangler dev sessions.</p>
<p>Now, the following works as expected:</p>
<pre><code class="language-sh">&#35; Terminal 1: Run your application that includes both Web and API workers&#10;wrangler dev --config ./web/wrangler.jsonc --config ./api/wrangler.jsonc&#10;&#10;&#35; Terminal 2: Run your auth worker separately&#10;wrangler dev --config ./auth/wrangler.jsonc&#10;</code></pre>
<p>These Workers can now communicate with each other across separate dev commands, regardless of your development setup.</p>
<pre><code class="language-js">export default {&#10;	async fetch(request, env) {&#10;		// This service binding call now works across dev commands&#10;		const authorized = await env.AUTH.isAuthorized(request);&#10;&#10;		if (!authorized) {&#10;			return new Response(&quot;Unauthorized&quot;, { status: 401 });&#10;		}&#10;&#10;		return new Response(&quot;Hello from API Worker!&quot;, { status: 200 });&#10;	},&#10;};&#10;</code></pre>
<p>Check out the <a href="/workers/local-development/multi-workers">Developing with multiple Workers</a> guide to learn more about the different approaches and when to use each one.</p>


<h2 id="rate-limiting-in-workers-is-now-ga"><a href="/changelog/post/2025-09-19-ratelimit-workers-ga/">Rate Limiting in Workers is now GA</a></h2>
<p><em>2025-09-19</em></p>
<p><a href="/workers/runtime-apis/bindings/rate-limit/">Rate Limiting within Cloudflare Workers</a> is now Generally Available (GA).</p>
<p>The <code>ratelimit</code> binding is now stable and recommended for all production workloads. Existing deployments using the unsafe binding will continue to function to allow for a smooth transition.</p>
<p>For more details, refer to <a href="/workers/runtime-apis/bindings/rate-limit/">Workers Rate Limiting</a> documentation.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product/workers/5/">Previous</a><span>Page 6 of 10</span><a class="pagination-next" rel="next" href="/changelog/product/workers/7/">Next</a></nav>
