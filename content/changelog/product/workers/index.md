---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/workers/
  description: 2026-09-17 12:00:00 UTC
  full_title: workers changelog | Cloudflare Docs
  head_html: <title>workers changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-09-17 12:00:00 UTC"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/workers/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="workers changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-09-17 12:00:00 UTC"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/workers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/workers/#page","headline":"workers changelog | Cloudflare Docs","description":"2026-09-17 12:00:00 UTC","url":"https://developers.cloudflare.com/changelog/product/workers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/workers/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="delete-workflow-instances-individually-or-in-batches"><a href="/changelog/post/2026-09-17-instance-delete/">Delete Workflow instances individually or in batches</a></h2>
<p><em>2026-09-17 12:00:00 UTC</em></p>
<p>You can now delete one or up to 100 Workflow instances and their stored state via the <a href="/workflows/build/workers-api/">Workflows API</a> or Wrangler 4.125.0 and later. Deleting an instance frees its stored state and stops its current execution. <a href="/workflows/reference/pricing/#storage-usage">Storage billing</a> is based on the average daily peak.</p>
<p>Delete one instance by calling <a href="/workflows/build/workers-api/#delete"><code>delete()</code></a> on its handle:</p>
<pre tabindex="0"><code class="language-ts">const instance = await env.MY_WORKFLOW.get(&quot;instance-abc&quot;);&#10;await instance.delete();&#10;</code></pre>
<p>If a Workflow deletes its own instance, execution stops during <code>await instance.delete()</code>. Code after the call does not run.</p>
<p>Delete multiple instances by calling <a href="/workflows/build/workers-api/#deletebatch"><code>deleteBatch()</code></a> on the Workflow binding:</p>
<pre tabindex="0"><code class="language-ts">const result = await env.MY_WORKFLOW.deleteBatch([&#10;	&quot;instance-abc&quot;,&#10;	&quot;instance-def&quot;,&#10;]);&#10;&#10;console.log(result.deleted);&#10;console.log(result.errors);&#10;</code></pre>
<p>The batch result contains <code>{ id }</code> entries for successful deletions and per-instance errors. IDs that do not exist are returned as errors. Duplicate IDs count toward the limit and are deleted once, with the result repeated for each input position.</p>
<p>Wrangler accepts positional instance IDs, a file containing a top-level JSON array of strings, or both, up to 100 IDs total. Use <code>latest</code> to delete the most recently created instance. Use <code>--local</code> against a local <code>wrangler dev</code> session:</p>
<pre tabindex="0"><code class="language-json">[&quot;instance-abc&quot;, &quot;instance-def&quot;]&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">npx wrangler workflows instances delete my-workflow &lt;INSTANCE_ID&gt;&#10;npx wrangler workflows instances delete my-workflow &lt;INSTANCE_ID&gt; &lt;INSTANCE_ID&gt;&#10;npx wrangler workflows instances delete my-workflow latest&#10;npx wrangler workflows instances delete my-workflow --filename ./instance-ids.json&#10;npx wrangler workflows instances delete my-workflow &lt;INSTANCE_ID&gt; --local&#10;</code></pre>
<p>For more information, refer to <a href="/workflows/build/trigger-workflows/#delete-workflow-instances">Delete Workflow instances</a>, <a href="/workflows/build/workers-api/#delete"><code>delete</code></a>, and <a href="/workflows/build/workers-api/#deletebatch"><code>deleteBatch</code></a>.</p>


<h2 id="workers-traces-now-automatically-include-javascript-rpc-session-spans"><a href="/changelog/post/2026-09-17-javascript-rpc-session-spans/">Workers traces now automatically include JavaScript RPC session spans</a></h2>
<p><em>2026-09-17</em></p>
<p>Workers traces can now follow JavaScript RPC calls across Worker boundaries and into Durable Objects. Previously, a trace stopped at the caller's RPC boundary. The dashboard now shows the caller-side session and method calls alongside the callee invocation, nested calls, and callbacks into another Worker.</p>
<p>A session span covers the lifetime of a caller-side session and groups calls that reuse it. Individual call spans show each method invocation. Execution colors distinguish the Workers or Durable Object entrypoints involved, while arrows mark outgoing and incoming calls. Together, these details show where time was spent, which calls reused a session, and how returned stubs and callbacks fit into the request.</p>
<p><img src="/assets/upstream/images/workers/changelog/jsrpc-session-spans.png" alt="A Workers trace of a Worker-to-Worker RPC session, showing the session span, the caller's getCounter and increment call spans, and the callee's invocation and matching call spans" /></p>
<p>Enable tracing with one setting in your <a href="/workers/wrangler/configuration/#observability">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17815.md")</div>
<p>Cloudflare records these spans automatically. You do not need to change your application code or add an observability SDK.</p>
<p>For supported spans and attributes, refer to <a href="/workers/observability/traces/spans-and-attributes/">Spans and attributes</a>.</p>


<h2 id="hyperdrive-support-for-python-workers"><a href="/changelog/post/2026-09-16-hyperdrive-python-workers/">Hyperdrive support for Python Workers</a></h2>
<p><em>2026-09-16</em></p>
<p><a href="/workers/languages/python/">Python Workers</a> can now connect to PostgreSQL and MySQL through Hyperdrive.</p>
<p>For setup, code examples, and limitations, refer to <a href="/hyperdrive/examples/python-workers/">Use Hyperdrive from Python Workers</a>.</p>


<h2 id="stream-workflow-instance-events-in-your-worker-or-via-the-api-with-subscribe"><a href="/changelog/post/2026-09-15-instance-event-subscriptions/">Stream Workflow instance events in your Worker or via the API with .subscribe()</a></h2>
<p><em>2026-09-15 12:00:00 UTC</em></p>
<p>You can now stream Workflow instance events via <code>WorkflowInstance.subscribe()</code> and the <code>GET /subscribe</code> API endpoint. Workers and HTTP clients can react to <a href="/workflows/build/events-and-parameters/">workflow</a> and <a href="/workflows/build/step-context/#workflowstepcontext">step</a> events, including attempts, sleeps, waits, and rollbacks, without polling for instance status.</p>
<p>A subscription first streams the entire event history of the Workflow instance. After streaming past events, the subscription waits for new events as the instance runs. You can use <code>filter</code> to receive only specific event types or <code>cursor</code> to start a subscription at a specific event.</p>
<p>Use <code>.subscribe()</code> to update Workflow status in user-facing dashboards, send notifications when steps complete, or trigger follow-up work for specific events.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17835.md")</div>
<p>For event types, available fields, and subscription options, refer to <a href="/workflows/build/subscribe-to-instance-events/">Subscribe to events</a>.</p>


<h2 id="grant-teammates-and-agents-access-to-specific-workers"><a href="/changelog/post/2026-09-15-granular-worker-permissions/">Grant teammates and agents access to specific Workers</a></h2>
<p><em>2026-09-15</em></p>
<p>You can now grant access to specific Workers and choose from four roles to control the level of access you give teammates, agents, and CI/CD workflows.</p>
<p>Choose from four roles to control the level of access:</p>
<ul>
<li><strong>Metadata Read-Only</strong>: View settings, metrics, logs, and traces without access to Worker code or the ability to make changes.</li>
<li><strong>Content Read-Only</strong>: Read Worker code, settings, and observability data without the ability to modify or deploy changes.</li>
<li><strong>Editor</strong>: Update and deploy a Worker without the ability to delete it.</li>
<li><strong>Admin</strong>: Everything in Editor, plus the ability to delete the Worker.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/workers/individual-worker-permission-roles.png" alt="Permission policy form showing four roles scoped to an individual Worker" /></p>
<p>Worker-level access controls are available today for all customers. You can configure them in the Cloudflare dashboard, through the API, or with Terraform.</p>
<h4 id="2026-09-15-granular-worker-permissions-roles-designed-for-how-teams-build">Roles designed for how teams build</h4>
<p>Give <strong>Metadata Read-Only</strong> to a debugging agent so it can inspect settings and observability data without seeing Worker code. Give <strong>Content Read-Only</strong> to a code review agent so it can read code without changing it. Give <strong>Editor</strong> to a CI/CD workflow so it can deploy without deleting the Worker or accessing other Workers. <strong>Admin</strong> gives a teammate or agent full control over the Worker, including the ability to delete it.</p>
<p>Apply these roles across all Developer Platform products, across all Workers, or to an individual Worker.</p>
<h4 id="2026-09-15-granular-worker-permissions-durable-objects">Durable Objects</h4>
<p>You can use granular permissions to control access to Durable Objects. Durable Objects do not have their own roles or scopes. Instead, they inherit the permissions assigned to the Worker that implements them.</p>
<p>Learn more about granular permissions in the <a href="/workers/authorization/durable-objects/">Durable Objects documentation</a>.</p>
<h4 id="2026-09-15-granular-worker-permissions-grant-access-to-members-and-user-groups">Grant access to members and User Groups</h4>
<p>In the Cloudflare dashboard, go to <strong>Manage Account</strong> &gt; <strong>Members</strong> and select a <a href="/fundamentals/manage-members/manage/">member</a>. Create a <a href="/fundamentals/manage-members/policies/">permission policy</a>, set the scope to <strong>Individual Workers</strong>, select the Workers they need, and choose a role to grant the right level of access.</p>
<p>If several people on the same team or project need the same access, assign the permission policy to a <a href="/fundamentals/manage-members/user-groups/">User Group</a> instead of each member individually. Everyone added to the group automatically inherits the policy.</p>
<h4 id="2026-09-15-granular-worker-permissions-create-a-scoped-api-token">Create a scoped API token</h4>
<p>For an agent or CI/CD workflow, go to <strong>Manage Account</strong> &gt; <strong>Account API Tokens</strong> and create an <a href="/fundamentals/api/get-started/account-owned-tokens/">account-owned API token</a>. Set the scope to <strong>Specified Workers</strong>, select the Workers the token can access, and choose a role to grant the right level of access.</p>
<p><img src="/assets/upstream/images/changelog/workers/scoped-worker-api-token-permissions.png" alt="Account API token policy with Metadata Read-Only access scoped to a specific Worker" /></p>
<p>For more information, refer to the <a href="/workers/authorization/workers/">Workers roles and permissions documentation</a>.</p>


<h2 id="miniflare-v5-prepares-local-development-for-the-cf-cli"><a href="/changelog/post/2026-09-08-miniflare-v5/">Miniflare v5 prepares local development for the cf CLI</a></h2>
<p><em>2026-09-08</em></p>
<p>Miniflare v5 prepares Cloudflare local development tooling for the upcoming <code>cf</code> CLI.</p>
<p>Miniflare powers local Workers development behind <code>wrangler dev</code>, the Cloudflare Vite plugin, and <code>@cloudflare/vitest-plugin</code>.
Most projects should use those tools instead of depending on Miniflare directly, and Miniflare v5 will not require any action.</p>
<p>The most significant change is a new configuration shape which aligns Miniflare with <code>cloudflare.config.ts</code>, the programmatic Cloudflare configuration format now available for testing.</p>
<p>Other breaking changes include:</p>
<ul>
<li>Removed deprecated APIs and options, such as legacy alpha D1 bindings.</li>
<li>Removed now-unused, internal APIs like <code>wrappedBindings</code></li>
<li>Removed Miniflare's built-in module discovery; higher-level tools like Wrangler and the Vite plugin should be providing the module graph.</li>
<li>Moved local-only /cdn-cgi routes under /cdn-cgi/local.</li>
<li>Replaced per-resource persistence options with shared persistence root options.</li>
</ul>
<p>For a more comprehensive list, refer to <a href="https://github.com/cloudflare/workers-sdk/blob/main/packages/miniflare/CHANGELOG.md#5202607300-alpha">Miniflare's changelog</a></p>
<p>This work sets up a cleaner foundation for the next generation of local development tooling, including the new <code>cf</code> CLI.</p>


<h2 id="python-3-14-for-python-workers"><a href="/changelog/post/2026-09-08-python-workers-314/">Python 3.14 for Python Workers</a></h2>
<p><em>2026-09-08</em></p>
<p>Python workers now use Python 3.14 by default.</p>
<p>This change applies to all new Python workers using compatibility date <code>2026-09-08</code> or later.</p>
<p>Internally, this change updates the Pyodide runtime to 314.0.6.</p>


<h2 id="enterprise-customers-can-self-serve-cdn-upload-limits-up-to-5-gb"><a href="/changelog/post/2026-09-04-enterprise-self-serve-upload-limits/">Enterprise customers can self-serve CDN upload limits up to 5 GB</a></h2>
<p><em>2026-09-04</em></p>
<p>Enterprise customers can now configure a zone's CDN <strong>Maximum Upload Size</strong> up to 5 GB directly from the <strong>Network</strong> page in the Cloudflare dashboard. This removes the need to contact your account team or Cloudflare Support when applications need to accept request bodies larger than 500 MB and no greater than 5 GB.</p>
<p>The default maximum upload size remains 500 MB. Upload limits above 5 GB still require additional configuration through your account team or <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a>.</p>
<p>Very large uploads may reach connection or read timeouts before reaching the configured size limit. Make sure clients and origins allow enough time to complete the transfer when increasing this setting.</p>
<p>Refer to <a href="/cache/concepts/default-cache-behavior/#upload-limits">Cache upload limits</a> and <a href="/workers/platform/limits/#request-and-response-limits">Workers request body size limits</a> for details.</p>


<h2 id="deploy-larger-workers-up-to-64-mib-for-both-free-and-paid-plans"><a href="/changelog/post/2026-09-04-increased-worker-size-limit/">Deploy larger Workers — up to 64 MiB for both free and paid plans</a></h2>
<p><em>2026-09-04</em></p>
<p>You can now deploy Workers with larger dependencies, heavier frameworks, and more code without hitting size limits.</p>
<p>When you deploy a Worker, Wrangler bundles your code and compresses it before uploading. Previously, Cloudflare checked that compressed size and rejected deploys over 3 MB (Free) or 10 MB (Paid). That limit has been removed. Cloudflare now only checks the uncompressed size of your bundle, which is 64 MiB across all plans.</p>
<p>To check your Worker's bundle size before deploying:</p>
<pre tabindex="0"><code class="language-sh">wrangler deploy --outdir bundled/ --dry-run&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">Total Upload: 259.61 KiB / gzip: 47.23 KiB&#10;</code></pre>
<p>The <code>Total Upload</code> value is your uncompressed bundle size. This is what counts against the 64 MiB limit. The <code>gzip</code> value is shown for reference but is no longer a limit.</p>
<p>For more information, refer to the <a href="/workers/platform/limits/#worker-size">Worker size limits documentation</a>.</p>


<h2 id="python-workers-now-support-wsgi-web-frameworks-like-django-and-flask"><a href="/changelog/post/2026-09-02-python-workers-web-framework-support/">Python Workers now support WSGI web frameworks like Django and Flask</a></h2>
<p><em>2026-09-02</em></p>
<p>Python web frameworks following the <a href="https://peps.python.org/pep-3333/">Web Server Gateway Interface (WSGI)</a> or <a href="https://asgi.readthedocs.io/">Asynchronous Server Gateway Interface (ASGI)</a> specification can now be used in Python Workers.</p>
<h4 id="2026-09-02-python-workers-web-framework-support-using-web-frameworks-with-python-workers">Using web frameworks with Python Workers</h4>
<p>Based on the web framework you are using, you can use either <code>wsgi</code> or <code>asgi</code> from the <code>workers</code> module.</p>
<h4 id="2026-09-02-python-workers-web-framework-support-wsgi-frameworks">WSGI frameworks</h4>
<p>For WSGI frameworks like Django or Flask:</p>
<pre tabindex="0"><code class="language-python">from workers import wsgi&#10;&#10;from django.core.wsgi import get_wsgi_application&#10;&#10;app = get_wsgi_application()&#10;Default = wsgi.entrypoint(app)&#10;</code></pre>
<p>The <code>wsgi.entrypoint</code> is equivalent to creating a <code>WorkerEntrypoint</code> class and using the <code>wsgi.fetch</code> method. If you want more control over the <code>WorkerEntrypoint</code> class, you can do so:</p>
<pre tabindex="0"><code class="language-python">from workers import wsgi, WorkerEntrypoint&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        return await wsgi.fetch(app, request, self.env)&#10;</code></pre>
<h4 id="2026-09-02-python-workers-web-framework-support-asgi-frameworks">ASGI frameworks</h4>
<p>For ASGI frameworks like FastAPI or Starlette:</p>
<pre tabindex="0"><code class="language-python">from workers import asgi&#10;&#10;from fastapi import FastAPI&#10;&#10;app = FastAPI()&#10;Default = asgi.entrypoint(app)&#10;</code></pre>
<p>For more information about using individual web frameworks, refer to the <a href="/workers/languages/python/packages/">packages documentation in Python Workers</a>.</p>


<h2 id="durable-objects-can-use-up-to-ten-dynamic-workers-concurrently"><a href="/changelog/post/2026-08-28-durable-objects-dynamic-workers-limit/">Durable Objects can use up to ten Dynamic Workers concurrently</a></h2>
<p><em>2026-08-28</em></p>
<p><a href="/durable-objects/">Durable Objects</a> can have up to ten distinct <a href="/dynamic-workers/">Dynamic Workers</a> with in-flight requests, increased from four. This limit applies across all concurrent requests to the same Durable Object because they share an input/output (I/O) context. Other Workers can have up to four distinct Dynamic Workers with in-flight requests per request.</p>
<p>Multiple in-flight requests to the same Dynamic Worker count as one toward this limit.</p>
<p>For more information, refer to <a href="/dynamic-workers/platform/limits/">Dynamic Workers limits</a>.</p>


<h2 id="preserve-exception-details-in-console-logs"><a href="/changelog/post/2026-08-24-preserve-exception-info/">Preserve exception details in console logs</a></h2>
<p><em>2026-08-24</em></p>
<p>Console methods now preserve exception details in your Worker's logs. When your Worker logs an exception, the corresponding log entry includes the exception name, message, and stack.</p>
<p>For example, your Worker can catch and log an exception:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17814.md")</div>
<p>If you use <a href="/workers/observability/">Workers Observability</a>, your log is automatically enriched with structured error information. The following example shows how the enriched log appears in the Cloudflare dashboard:</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2026-08-24-error-info.png" alt="Workers Observability log entry showing a caught exception and its stack trace" /></p>
<p>The exception's stack trace appears directly in the log message.</p>
<p>If you send telemetry to a <a href="/workers/observability/logs/tail-workers/">Tail Worker</a>, the Tail Worker now receives a log entry with an <code>errorInfo</code> array:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;message&quot;: [&quot;Request failed:&quot;, &quot;RangeError: Value out of range&quot;],&#10;	&quot;errorInfo&quot;: [&#10;		null,&#10;		{&#10;			&quot;name&quot;: &quot;RangeError&quot;,&#10;			&quot;message&quot;: &quot;Value out of range&quot;,&#10;			&quot;stack&quot;: &quot;RangeError: Value out of range\n    at ...&quot;&#10;		}&#10;	],&#10;	&quot;level&quot;: &quot;error&quot;,&#10;	&quot;timestamp&quot;: 1784851200000&#10;}&#10;</code></pre>
<p>Each <code>errorInfo</code> item corresponds to the console argument at the same index in <code>message</code>. Arguments that are not exceptions have a <code>null</code> entry.</p>


<h2 id="choose-oauth-scopes-for-wrangler-and-the-cloudflare-api-mcp-server"><a href="/changelog/post/2026-08-22-wrangler-mcp-optional-oauth-scopes/">Choose OAuth scopes for Wrangler and the Cloudflare API MCP server</a></h2>
<p><em>2026-08-22</em></p>
<p>Wrangler and the <a href="/agents/model-context-protocol/cloudflare/servers-for-cloudflare/">Cloudflare API MCP server</a> now use optional OAuth scopes. During authorization, you can choose which optional scopes to grant instead of approving every scope requested by each client.</p>
<p>The consent dialog now includes the option to edit the permissions you grant to Wrangler or the Cloudflare API MCP server:</p>
<p><img src="/assets/upstream/images/agents/oauth-optional-scopes-review.png" alt="OAuth consent dialog with an Edit Permissions button" /></p>
<p>You can then choose which specific permissions to grant:</p>
<p><img src="/assets/upstream/images/agents/oauth-optional-scopes-edit.png" alt="OAuth permission editor with controls for individual scopes" /></p>
<p>Required scopes remain selected. Choosing fewer optional scopes limits each tool's access to the permissions needed for your workflow.</p>
<p>If a command or tool call needs a scope that you declined, reauthorize the client and grant that scope.</p>
<p>For more information, refer to <a href="/workers/wrangler/commands/general/#login"><code>wrangler login</code></a> and <a href="/fundamentals/oauth/authorizing-an-application/#edit-optional-permissions">Edit optional permissions</a>.</p>


<h2 id="view-deployments-for-durable-objects-in-the-dashboard"><a href="/changelog/post/2026-08-20-durable-objects-deployments-tab/">View deployments for Durable Objects in the dashboard</a></h2>
<p><em>2026-08-20</em></p>
<p>Durable Object namespaces now have a <strong>Deployments</strong> tab in the Cloudflare dashboard, showing the <a href="/workers/versions-and-deployments/#versions">versions</a> of the backing Worker that are currently live and the traffic split between them.</p>
<p><img src="/assets/upstream/images/changelog/durable-objects/durable-objects-deployments-tab.png" alt="The Deployments tab for a Durable Object namespace, showing two versions with their traffic %, requests/sec, error rate, and median wall time" /></p>
<div class="nb-dash-button"></div>
<p>A Durable Object namespace is backed by a Worker script, so its deployments are the same as that Worker's deployments. Previously, checking on a <a href="/workers/versions-and-deployments/gradual-deployments/">gradual deployment</a> in progress for a Durable Object meant navigating to the backing Worker. The new tab surfaces that information directly on the namespace, alongside the metrics that matter for it: requests, error rate, and wall time per version.</p>
<p>The tab is read-only — promoting, rolling back, or splitting traffic on a deployment is still managed from the backing Worker's Deployments tab.</p>
<h4 id="2026-08-20-durable-objects-deployments-tab-actual-vs-configured-traffic-split">Actual vs. configured traffic split</h4>
<p>The <strong>Traffic %</strong> column, for both Workers and Durable Objects, now shows the actual, observed traffic share for each version next to the percentage you configured. Previously, this column only showed the configured percentage. If you moved a deployment from 50/50 to 100% on a new version, the configured number updated immediately, but requests take time to catch up, and there was no way to tell how far along that shift was without checking metrics elsewhere.</p>
<p>The configured split assigns Worker versions to individual Durable Objects, not to individual requests. Because <a href="/workers/versions-and-deployments/gradual-deployments/with-durable-objects/">each Durable Object is pinned to the version it started on until you create a new deployment</a> and some objects naturally receive more traffic than others, the observed split can differ from the configured one for as long as multiple versions are active.</p>
<p>Actual traffic share is calculated from the same <a href="/analytics/graphql-api/">GraphQL Analytics API</a> data that powers other Workers and Durable Objects metrics, so standard ingestion delay and <a href="/analytics/faq/graphql-api-inconsistent-results/">sampling</a> apply. Durable Objects analytics can lag Workers analytics by several minutes, so a version's actual share may take a little longer to catch up after a change.</p>
<p>To view this, go to <strong>Workers &amp; Pages</strong> &gt; <strong>Durable Objects</strong>, select a namespace, then select the <strong>Deployments</strong> tab. For more on how gradual deployments work, refer to <a href="/workers/versions-and-deployments/gradual-deployments/">Gradual deployments</a>.</p>


<h2 id="cloudflare-vitest-pool-workers-is-now-cloudflare-vitest-plugin"><a href="/changelog/post/2026-08-19-vitest-plugin/">@cloudflare/vitest-pool-workers is now @cloudflare/vitest-plugin</a></h2>
<p><em>2026-08-19</em></p>
<p>Version 1 of the Workers Vitest integration is published as <a href="https://www.npmjs.com/package/@cloudflare/vitest-plugin"><code>@cloudflare/vitest-plugin</code></a>. The package was formerly named <code>@cloudflare/vitest-pool-workers</code>.</p>
<p>The Vitest configuration API is unchanged. Existing projects must update the dependency name, package imports, and TypeScript <code>types</code> entries.</p>
<p>To migrate automatically, run:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npx @cloudflare/codemods vitest:pool-workers-to-vitest-plugin</code></pre><button type="button" data-nb-pm-copy data-nb-command="npx @cloudflare/codemods vitest:pool-workers-to-vitest-plugin" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn @cloudflare/codemods vitest:pool-workers-to-vitest-plugin</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn @cloudflare/codemods vitest:pool-workers-to-vitest-plugin" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm @cloudflare/codemods vitest:pool-workers-to-vitest-plugin</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm @cloudflare/codemods vitest:pool-workers-to-vitest-plugin" aria-label="Copy to clipboard">Copy</button></div></div>
<p>The codemod updates your dependency, imports, and test TypeScript configuration. For manual migration steps, refer to <a href="/workers/testing/vitest-integration/migration-guides/migrate-to-vitest-plugin/">Migrate to Vitest plugin</a>.</p>
<p>For outbound request mocks in Workers tests, use the <a href="https://github.com/mswjs/cloudflare"><code>@msw/cloudflare</code></a> integration. Refer to <a href="/workers/testing/vitest-integration/mock-outbound-requests/">Mock outbound requests</a>.</p>


<h2 id="you-can-now-enable-access-on-a-worker-or-all-workers-at-once"><a href="/changelog/post/2026-08-14-workers-access/">You can now enable Access on a Worker or all Workers at once</a></h2>
<p><em>2026-08-14</em></p>
<p>You now have two new ways to protect your <a href="/workers/">Workers</a> with <a href="/workers/configuration/cloudflare-access/">Cloudflare Access</a>.</p>
<p><strong>Protect an application across all its domains at once</strong></p>
<p>Until now, if a Worker was reachable on a route, a Custom Domain, and a <code>workers.dev</code> URL, you had to manually add each one to an Access application and keep the list in sync whenever routes or domains changed.</p>
<p>Now, Access attaches the policy to the Worker itself, so every associated domain and preview URL stays protected even when its routes or domains change.</p>
<p><img src="/assets/upstream/images/changelog/workers/protect-one-worker.png" alt="Access setting for protecting a single Worker" /></p>
<p><strong>Protect all new and existing Workers by default</strong></p>
<p>Make all Workers private by default, so every existing and newly created Worker requires sign-in before anyone can reach it.</p>
<p><img src="/assets/upstream/images/changelog/workers/protect-all-workers.png" alt="Account-wide Access setting that protects all Workers" /></p>
<p>If a specific Worker should remain publicly accessible, add a Worker-level bypass to exempt it.</p>
<p><img src="/assets/upstream/images/changelog/workers/make-worker-public.png" alt="Make a Worker public when all Workers are protected" /></p>
<p>Whether you protect a single application or all Workers at once, you can choose whether to protect preview deployments only or both previews and production, and control who can sign in by Cloudflare account membership, email address, or email domain.</p>
<p>For more advanced policy options, edit the policy in <a href="https://dash.cloudflare.com/?to=/:account/one/access/apps">Zero Trust</a>.</p>
<p><img src="/assets/upstream/images/changelog/workers/choose-who-can-sign-in.png" alt="Access policy configuration for controlling who can sign in" /></p>
<p><strong>View all of your Worker Access policies</strong></p>
<p>You can view and manage all of your Access policies in the <strong>Access</strong> tab of the Workers &amp; Pages section in the dashboard.</p>
<p><img src="/assets/upstream/images/changelog/workers/access-policies.png" alt="Access tab showing all configured Access policies" /></p>
<p><strong>See who is accessing your Worker</strong></p>
<p>When Access is enabled on your Worker, every authenticated request includes <code>ctx.access</code>. Call <a href="/workers/runtime-apis/context/#access"><code>ctx.access.getIdentity()</code></a> to get the user's email, name, and groups — no manual JWT validation required.</p>
<pre tabindex="0"><code class="language-js">export default {&#10;  async fetch(request, env, ctx) {&#10;    if (!ctx.access) {&#10;      return new Response(&quot;Access did not run&quot;, { status: 401 });&#10;    }&#10;&#10;    const identity = await ctx.access.getIdentity();&#10;    return Response.json({ aud: ctx.access.aud, email: identity?.email });&#10;  },&#10;};&#10;</code></pre>
<p><strong>Test Access locally</strong></p>
<p>You can now test Cloudflare Access locally with <code>wrangler dev</code>. Add a <code>dev</code> block to your <code>wrangler.jsonc</code>:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;access&quot;: {&#10;    &quot;dev&quot;: {&#10;      &quot;aud&quot;: &quot;my-app&quot;,&#10;      &quot;identity&quot;: { &quot;email&quot;: &quot;admin@example.com&quot; }&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>Your Worker will receive this identity through <code>ctx.access</code> and <code>ctx.access.getIdentity()</code>, letting you test authenticated and unauthenticated flows without deploying. Remove the <code>dev</code> block to simulate unauthenticated requests.</p>
<p><strong>API and programmatic access</strong></p>
<p>You can also set up these policies through the <a href="/workers/configuration/cloudflare-access/">Workers API</a> instead of the dashboard.</p>


<h2 id="agent-traces-for-think-flue-and-ai-sdk-instrumented-by-agents-sdk"><a href="/changelog/post/2026-08-04-agent-tracing/">Agent traces for Think, Flue, and AI SDK instrumented by Agents SDK</a></h2>
<p><em>2026-08-04</em></p>
<p>Agent tracing is now available for applications built with the Agents SDK. Traces show each agent turn alongside model calls, tool runs, approvals, token usage, and Workers runtime operations.</p>
<p>Turn on Workers tracing in your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17683.md")</div>
<p>Think and Flue applications emit agent traces automatically. For direct AI SDK calls, wrap the AI SDK namespace once. <code>wrapAISDK()</code> supports AI SDK v6 and v7. This AI SDK v7 example also supplies the agent identity:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17684.md")</div>
<p>Message and tool payload recording is off by default. Turn it on only when the payloads are safe to store:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17685.md")</div>
<p>Open the <a href="https://dash.cloudflare.com/?to=/:account/agents"><strong>Agents</strong> tab</a> in the Cloudflare dashboard to inspect sessions, replay conversations, and view trace waterfalls. For advanced setup, privacy controls, and trace structure, refer to <a href="/agents/runtime/operations/observability/tracing/">Agent tracing</a>.</p>


<h2 id="ai-agents-can-debug-workers-with-local-tracing"><a href="/changelog/post/2026-08-04-local-tracing/">AI agents can debug Workers with local tracing</a></h2>
<p><em>2026-08-04</em></p>
<p><code>wrangler dev</code> and <code>vite dev</code> automatically capture structured OpenTelemetry traces and correlated console logs during local Worker invocations.</p>
<h4 id="2026-08-04-local-tracing-debug-with-ai-agents">Debug with AI agents</h4>
<p>When the tooling detects an AI agent session, it prints a terminal hint pointing to the <a href="/workers/local-development/local-explorer/#api">Local Explorer API</a> at <code>/cdn-cgi/local/explorer/api</code>. The API serves an OpenAPI schema and exposes a read-only observability query endpoint for discovering telemetry, querying traces and logs, and inspecting binding state.</p>
<p>The agent can identify the exact failing operation, fix the code, rerun the request, and verify the result. This debug loop requires no deployment or temporary logs.</p>
<h4 id="2026-08-04-local-tracing-inspect-traces-in-local-explorer">Inspect traces in Local Explorer</h4>
<p>Humans can inspect the same <a href="/workers/observability/traces/">traces</a> and correlated console logs in the Local Explorer browser UI. Each trace shows spans, timing, attributes, and errors.</p>
<p><img src="/assets/upstream/images/workers/observability/local-trace-failed-request.png" alt="Local Explorer showing a failed Worker trace with spans, timing, and errors" /></p>
<p>Automatic spans cover handler calls, outbound <code>fetch()</code> calls, and binding calls. Custom spans appear alongside these automatic spans.</p>
<p>For more details, refer to the <a href="/workers/local-development/local-explorer/">Local Explorer documentation</a>.</p>


<h2 id="node-js-compatibility-is-now-enabled-by-default"><a href="/changelog/post/2026-08-04-nodejs-compat-default/">Node.js compatibility is now enabled by default</a></h2>
<p><em>2026-08-04</em></p>
<p>Workers now enable the <code>nodejs_compat</code> and <code>nodejs_compat_v2</code> compatibility
flags by default for <a href="/workers/configuration/compatibility-dates/">compatibility dates</a>
of <code>2026-08-04</code> or later. These flags are not used for these compatibility
dates because the compatibility date enables the same behavior.</p>
<p>This means all <a href="/workers/runtime-apis/nodejs/">Node.js built-in APIs</a> supported
by the Workers runtime are available by default, including <code>node:crypto</code>,
<code>node:buffer</code>, <code>node:stream</code>, <code>node:net</code>, <code>node:dns</code>, <code>node:fs</code>, <code>node:http</code>,
and more. npm packages that depend on these APIs will work without additional
configuration.</p>
<p>Workers using an earlier compatibility date are not affected. They can still
opt in by adding <code>nodejs_compat</code> to <code>compatibility_flags</code>.</p>
<p>New projects do not need to add either flag. Existing projects can update their
compatibility date without removing them. Wrangler, Miniflare, the Cloudflare
Vite plugin, and Vitest Pool Workers ignore these redundant flags when starting
the runtime.</p>
<p>To turn off Node.js compatibility completely, remove any <code>nodejs_compat</code> and
<code>nodejs_compat_v2</code> flags. Then add both of the following flags:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17813.md")</div>
<p>For more information, refer to the <a href="/workers/runtime-apis/nodejs/">Node.js compatibility documentation</a>.</p>


<h2 id="log-in-to-wrangler-without-a-local-callback-server"><a href="/changelog/post/2026-08-04-wrangler-login-device-flow/">Log in to Wrangler without a local callback server</a></h2>
<p><em>2026-08-04</em></p>
<p><code>wrangler login</code> now supports the <a href="https://www.rfc-editor.org/rfc/rfc8628">OAuth 2.0 Device Authorization Grant</a>. Pass <code>--device</code> to authenticate without starting a temporary callback server on <code>localhost:8976</code>:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler login --device&#10;</code></pre>
<p>Wrangler prints a verification URL and a short user code, opens the URL in your default browser with the code already filled in, and polls Cloudflare for an access token while you approve the request:</p>
<pre tabindex="0"><code class="language-sh"> ⛅️ wrangler 4.119.0&#10;────────────────────&#10;Attempting to login via OAuth Device Authorization Grant...&#10;To authorize Wrangler, please visit:&#10;&#10;  https://dash.cloudflare.com/oauth2/device&#10;&#10;and enter the code:&#10;&#10;  jPqK6Qvs&#10;&#10;You have 5 minutes to approve this request.&#10;&#10;Opening a link in your default browser: https://dash.cloudflare.com/oauth2/device?user_code=jPqK6Qvs&#10;Successfully logged in.&#10;</code></pre>
<p>The default login flow needs your browser to reach <code>localhost:8976</code>, which is not always possible from containers, remote SSH sessions, or GitHub Codespaces. Previously these environments required forwarding ports or fetching the callback URL with <code>curl</code> from a second terminal session. Because <code>--device</code> has no callback server, those workarounds are no longer necessary.</p>
<p>Since the plain verification URL and user code are both printed to the terminal, you can also approve the request from a phone or another machine. Pass <code>--browser=false</code> to stop Wrangler from opening a browser at all.</p>
<p>Available in Wrangler version 4.119.0 or later. For more information, refer to <a href="/workers/wrangler/commands/general/#login"><code>wrangler login</code></a>.</p>


<h2 id="preview-cloudflare-computer-agent-runtime"><a href="/changelog/post/2026-08-03-cloudflare-computer/">Preview: @cloudflare/computer agent runtime</a></h2>
<p><em>2026-08-03</em></p>
<p>We're releasing an early preview of <a href="https://github.com/cloudflare/computer"><code>@cloudflare/computer</code></a>, an open-source agent runtime that gives every agent its own computer. The runtime dynamically orchestrates between fast, efficient isolates and full Linux containers, so the agent always runs on the right compute primitive for the task at hand.</p>
<p><code>@cloudflare/computer</code> provides a virtual filesystem backed by SQLite, which you can populate from cloud storage, source control, or any files you choose. Agents can read, write, and edit files, run shell commands, and interact with Git repositories. All operations are gated, audited, and observed.</p>
<p>Install the package via npm:</p>
<pre tabindex="0"><code class="language-sh">npm install @cloudflare/computer&#10;</code></pre>
<p>Instantiate a <code>Workspace</code> inside any Durable Object to give your agent a filesystem and execution runtime:</p>
<pre tabindex="0"><code class="language-ts">import { Workspace } from &quot;@cloudflare/computer&quot;;&#10;&#10;export class Agent {&#10;	workspace = new Workspace({&#10;		storage: this.ctx.storage,&#10;	});&#10;}&#10;</code></pre>
<p>Several execution backends are included or you can write your own:</p>
<ul>
<li><strong>Isolate runtime</strong> — fast, horizontally scalable execution via <code>just-bash</code> and Dynamic Workers, ideal for file manipulation and data processing.</li>
<li><strong>Container runtime</strong> — full Linux environment via Cloudflare Containers, mounted through FUSE, for tasks that need native binaries, package managers, or a complete userland.</li>
</ul>
<p>The AI SDK-compatible toolkit provides common agent tools (<code>read</code>, <code>write</code>, <code>edit</code>, <code>ls</code>, <code>exec</code>) and guides the model to choose the appropriate backend for each task.</p>
<p>For more examples, including a step-by-step tutorial, visit the <a href="https://github.com/cloudflare/computer"><code>@cloudflare/computer</code> repository</a>.</p>
<p>Read the announcement blog post for more details: <a href="https://blog.cloudflare.com/cloudflare-computer/">Your agent needs a computer, not a container</a>.</p>


<h2 id="python-and-javascript-workers-can-now-call-each-other-via-rpc"><a href="/changelog/post/2026-08-03-python-javascript-rpc/">Python and JavaScript Workers can now call each other via RPC</a></h2>
<p><em>2026-08-03</em></p>
<p>You can now call methods between Python and JavaScript Workers using <a href="/workers/runtime-apis/rpc/">Workers RPC</a>. This works through <a href="/workers/runtime-apis/bindings/service-bindings/rpc/">Service bindings</a> without extra dependencies, schema definitions, or serialization code.</p>
<p>Cross-language RPC calls behave like ordinary function calls. Exceptions propagate to the call site. You can pass <a href="https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm#supported_types">structured cloneable types</a> as parameters or return values, and Pyodide Foreign Function Interface (FFI) automatically converts types between languages.</p>
<h4 id="2026-08-03-python-javascript-rpc-call-a-typescript-worker-from-python">Call a TypeScript Worker from Python</h4>
<p>Define a method in a TypeScript Worker:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17809.md")</div>
<p>Call it from a Python Worker through a Service binding:</p>
<pre tabindex="0"><code class="language-python">from workers import Response, WorkerEntrypoint&#10;&#10;class Default(WorkerEntrypoint):&#10;	async def fetch(self, request):&#10;		rpc = self.env.RPC&#10;		result = await rpc.add(42, 144)&#10;		return Response.json({&quot;result&quot;: result})&#10;</code></pre>
<p>Configure the Service binding in the Python Worker's Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17810.md")</div>
<h4 id="2026-08-03-python-javascript-rpc-call-a-python-worker-from-javascript">Call a Python Worker from JavaScript</h4>
<p>Define a method in a Python Worker:</p>
<pre tabindex="0"><code class="language-python">from workers import WorkerEntrypoint&#10;&#10;class Default(WorkerEntrypoint):&#10;	async def highlight_code(self, code: str, language: str) -&gt; dict:&#10;		from pygments.formatters import HtmlFormatter&#10;		from pygments import highlight&#10;		from pygments.lexers import get_lexer_by_name&#10;&#10;		lexer = get_lexer_by_name(language, stripall=True)&#10;		formatter = HtmlFormatter(linenos=True, cssclass=&quot;highlight&quot;, style=&quot;monokai&quot;)&#10;		highlighted_html = highlight(code, lexer, formatter)&#10;		css = formatter.get_style_defs(&quot;.highlight&quot;)&#10;&#10;		return {&#10;			&quot;html&quot;: highlighted_html,&#10;			&quot;css&quot;: css&#10;		}&#10;</code></pre>
<p>Call it from a JavaScript Worker through a Service binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17811.md")</div>
<p>Configure the Service binding in the JavaScript Worker's Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17812.md")</div>
<p>For more details on the announcement, read the <a href="https://blog.cloudflare.com/python-workers-rpc/">blog post</a>.</p>
<p>For more information, refer to the <a href="/workers/runtime-apis/rpc/">Workers RPC documentation</a> and the <a href="/workers/languages/python/">Python Workers overview</a>.</p>


<h2 id="inspect-worker-startup-performance-with-wrangler"><a href="/changelog/post/2026-07-31-wrangler-startup-profile-summary/">Inspect Worker startup performance with Wrangler</a></h2>
<p><em>2026-07-31</em></p>
<p><code>wrangler check startup</code> now reports your Worker's raw and compressed bundle sizes. It also summarizes local CPU activity during startup directly in your terminal.</p>
<p>Large bundles and costly startup work can introduce cold-start latency, so use this command to find code and large dependencies that slow your Worker before it handles requests.</p>
<p>The summary includes sampled, active, garbage collection, and idle time. Wrangler continues to save a <code>.cpuprofile</code> file for detailed flamegraph analysis in Chrome DevTools or VS Code.</p>
<pre tabindex="0"><code class="language-bash">⛅️ wrangler 4.116.0&#10;───────────────────────────────────────────────&#10;├ Building your Worker&#10;│ Worker Built! 🎉&#10;│&#10;├ Analysing&#10;│ Startup phase analysed&#10;│&#10;│ Bundle: 7171.25 KiB / gzip: 2197.00 KiB&#10;│&#10;│ Local startup profile:&#10;│   Profile window: 70.3 ms&#10;│   Sampled time: 70.3 ms&#10;│   Active: 38.5 ms (including 3.7 ms garbage collection)&#10;│   Idle: 31.8 ms&#10;│   Samples: 36&#10;│&#10;│ CPU Profile has been written to worker-startup.cpuprofile. Load it into the Chrome DevTools profiler (or directly in VSCode) to view a flamegraph.&#10;│&#10;│ Note that the CPU Profile was measured on your Worker running locally on your machine, which has a different CPU than when your Worker runs on Cloudflare.&#10;│&#10;│ As such, CPU Profile can be used to understand where time is spent at startup, but the overall startup time in the profile should not be expected to exactly match what your Worker&#x27;s startup time will be when deploying to Cloudflare.&#10;</code></pre>
<p>The profile runs locally, so its duration will differ from startup time on Cloudflare. For authoritative startup time, deploy your Worker or upload a version.</p>
<p>Available in Wrangler version 4.116.0 or later. For more information, refer to <a href="/workers/wrangler/commands/workers/#startup"><code>wrangler check startup</code></a>.</p>


<h2 id="node-js-24-is-now-the-default-for-workers-builds"><a href="/changelog/post/2026-07-30-workers-builds-nodejs-24/">Node.js 24 is now the default for Workers Builds</a></h2>
<p><em>2026-07-30</em></p>
<p>Workers Builds now uses Node.js 24.18.0 by default. The build image preinstalls Node.js 22.23.2 and 24.18.0.</p>
<p>You can continue to override the default with the <code>NODE_VERSION</code> environment variable, an <code>.nvmrc</code> file, or a <code>.node-version</code> file. For more information, refer to <a href="/workers/ci-cd/builds/build-image/#overriding-default-versions">Override default versions</a>.</p>


<h2 id="cloudflare-mcp-servers-support-the-new-mcp-2026-07-28-specification"><a href="/changelog/post/2026-07-28-cloudflare-mcp-servers-mcp-2026-07-28/">Cloudflare MCP servers support the new MCP 2026-07-28 Specification</a></h2>
<p><em>2026-07-28</em></p>
<p>Cloudflare's <a href="/agents/model-context-protocol/cloudflare/servers-for-cloudflare/#product-specific-mcp-servers">product-specific MCP servers</a> now support the new MCP 2026-07-28 Specification. Each request runs on a fresh stateless server without an MCP protocol session or protocol-specific Durable Object.</p>
<p>The <code>/mcp</code> endpoint also accepts stateless requests from 2025 Streamable HTTP clients. Most clients can reconnect without configuration changes.</p>
<p>Use <code>/mcp</code> for new connections. Historical <code>/sse</code> URLs continue to work as aliases for the same Streamable HTTP handler, but they no longer serve the deprecated HTTP+SSE transport. If a client forces SSE transport, change it to Streamable HTTP or automatic transport detection.</p>


<nav class="pagination" aria-label="Changelog pages"><span>Page 1 of 10</span><a class="pagination-next" rel="next" href="/changelog/product/workers/2/">Next</a></nav>
