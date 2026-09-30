<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-09-17">Sep 17, 2026</time><div>
<h2 id="post-2026-09-17-instance-delete"><a href="/changelog/post/2026-09-17-instance-delete/">Delete Workflow instances individually or in batches</a></h2>
<div class="changelog-badges"><span>workflows</span><span>workers</span></div><div class="changelog-body"><p>You can now delete one or up to 100 Workflow instances and their stored state via the <a href="/workflows/build/workers-api/">Workflows API</a> or Wrangler 4.125.0 and later. Deleting an instance frees its stored state and stops its current execution. <a href="/workflows/reference/pricing/#storage-usage">Storage billing</a> is based on the average daily peak.</p>
<p>Delete one instance by calling <a href="/workflows/build/workers-api/#delete"><code>delete()</code></a> on its handle:</p>
<pre><code class="language-ts">const instance = await env.MY_WORKFLOW.get(&quot;instance-abc&quot;);&#10;await instance.delete();&#10;</code></pre>
<p>If a Workflow deletes its own instance, execution stops during <code>await instance.delete()</code>. Code after the call does not run.</p>
<p>Delete multiple instances by calling <a href="/workflows/build/workers-api/#deletebatch"><code>deleteBatch()</code></a> on the Workflow binding:</p>
<pre><code class="language-ts">const result = await env.MY_WORKFLOW.deleteBatch([&#10;	&quot;instance-abc&quot;,&#10;	&quot;instance-def&quot;,&#10;]);&#10;&#10;console.log(result.deleted);&#10;console.log(result.errors);&#10;</code></pre>
<p>The batch result contains <code>{ id }</code> entries for successful deletions and per-instance errors. IDs that do not exist are returned as errors. Duplicate IDs count toward the limit and are deleted once, with the result repeated for each input position.</p>
<p>Wrangler accepts positional instance IDs, a file containing a top-level JSON array of strings, or both, up to 100 IDs total. Use <code>latest</code> to delete the most recently created instance. Use <code>--local</code> against a local <code>wrangler dev</code> session:</p>
<pre><code class="language-json">[&quot;instance-abc&quot;, &quot;instance-def&quot;]&#10;</code></pre>
<pre><code class="language-sh">npx wrangler workflows instances delete my-workflow &lt;INSTANCE_ID&gt;&#10;npx wrangler workflows instances delete my-workflow &lt;INSTANCE_ID&gt; &lt;INSTANCE_ID&gt;&#10;npx wrangler workflows instances delete my-workflow latest&#10;npx wrangler workflows instances delete my-workflow --filename ./instance-ids.json&#10;npx wrangler workflows instances delete my-workflow &lt;INSTANCE_ID&gt; --local&#10;</code></pre>
<p>For more information, refer to <a href="/workflows/build/trigger-workflows/#delete-workflow-instances">Delete Workflow instances</a>, <a href="/workflows/build/workers-api/#delete"><code>delete</code></a>, and <a href="/workflows/build/workers-api/#deletebatch"><code>deleteBatch</code></a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-17">Sep 17, 2026</time><div>
<h2 id="post-2026-09-15-free-account-creation"><a href="/changelog/post/2026-09-15-free-account-creation/">Create additional Free accounts through the dashboard and API</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>We're expanding how customers create accounts across Cloudflare, making it easier to self-serve account creation in the dashboard, automate standalone account creation with user-owned API tokens or OAuth access tokens, and create Free accounts directly within Enterprise Organizations.</p>
<h4 id="2026-09-15-free-account-creation-what-s-new">What's New</h4>
<p><strong>Dashboard account creation:</strong> All cloudflare customers can create additional Free accounts directly through self-serve flows in the Cloudflare dashboard.</p>
<p><strong>Enterprise Organization account creation:</strong> Super Administrators can now create up to five Free accounts directly within an Enterprise Organization. This makes it easier to provision and manage additional accounts and directly associate them with your Organization.</p>
<p><strong>API and OAuth account creation:</strong> Customers can now create standalone Free accounts programmatically via User-owned API tokens or OAuth access tokens.</p>
<p>For more information:</p>
<ul>
<li><a href="/fundamentals/account/create-account/">Create a Free account in the dashboard</a></li>
<li><a href="/api/resources/accounts/methods/create/">Create an account via the API</a></li>
<li><a href="/fundamentals/organizations/for-enterprise/#create-new-accounts">Create Free accounts in an Enterprise Organization</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-17">Sep 17, 2026</time><div>
<h2 id="post-2026-09-17-javascript-rpc-session-spans"><a href="/changelog/post/2026-09-17-javascript-rpc-session-spans/">Workers traces now automatically include JavaScript RPC session spans</a></h2>
<div class="changelog-badges"><span>workers</span><span>durable-objects</span></div><div class="changelog-body"><p>Workers traces can now follow JavaScript RPC calls across Worker boundaries and into Durable Objects. Previously, a trace stopped at the caller's RPC boundary. The dashboard now shows the caller-side session and method calls alongside the callee invocation, nested calls, and callbacks into another Worker.</p>
<p>A session span covers the lifetime of a caller-side session and groups calls that reuse it. Individual call spans show each method invocation. Execution colors distinguish the Workers or Durable Object entrypoints involved, while arrows mark outgoing and incoming calls. Together, these details show where time was spent, which calls reused a session, and how returned stubs and callbacks fit into the request.</p>
<p><img src="/assets/upstream/images/workers/changelog/jsrpc-session-spans.png" alt="A Workers trace of a Worker-to-Worker RPC session, showing the session span, the caller's getCounter and increment call spans, and the callee's invocation and matching call spans" /></p>
<p>Enable tracing with one setting in your <a href="/workers/wrangler/configuration/#observability">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17815.md")</div>
<p>Cloudflare records these spans automatically. You do not need to change your application code or add an observability SDK.</p>
<p>For supported spans and attributes, refer to <a href="/workers/observability/traces/spans-and-attributes/">Spans and attributes</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-17">Sep 17, 2026</time><div>
<h2 id="post-2026-09-17-reject-if-busy"><a href="/changelog/post/2026-09-17-reject-if-busy/">Reject busy synchronous inference requests</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>The <code>rejectIfBusy</code> option lets synchronous Workers AI inference requests fail when capacity is unavailable. Use it when your application should not wait in a capacity queue.</p>
<p>Pass the option as the third argument to the Workers AI binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17820.md")</div>
<p>For the native REST API, add the option to the request body:</p>
<pre><code class="language-bash">curl --request POST \&#10;  &#45;-url &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai/run/@cf/google/gemma-4-26b-a4b-it&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;messages&quot;: [{ &quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;Explain capacity queues.&quot; }],&#10;    &quot;options&quot;: { &quot;rejectIfBusy&quot;: true }&#10;  }&#x27;&#10;</code></pre>
<p>Refer to <a href="/workers-ai/features/reject-if-busy/">Reject busy requests</a> for OpenAI-compatible usage and error behavior.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-16">Sep 16, 2026</time><div>
<h2 id="post-2026-09-16-hyperdrive-python-workers"><a href="/changelog/post/2026-09-16-hyperdrive-python-workers/">Hyperdrive support for Python Workers</a></h2>
<div class="changelog-badges"><span>workers</span><span>hyperdrive</span></div><div class="changelog-body"><p><a href="/workers/languages/python/">Python Workers</a> can now connect to PostgreSQL and MySQL through Hyperdrive.</p>
<p>For setup, code examples, and limitations, refer to <a href="/hyperdrive/examples/python-workers/">Use Hyperdrive from Python Workers</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-16">Sep 16, 2026</time><div>
<h2 id="post-2026-09-16-table-maintenance-dashboard"><a href="/changelog/post/2026-09-16-table-maintenance-dashboard/">R2 Data Catalog adds table maintenance visibility and manual queueing</a></h2>
<div class="changelog-badges"><span>r2</span><span>r2-data-catalog</span></div><div class="changelog-body"><p><a href="/r2-data-catalog/">R2 Data Catalog</a> now provides table-level maintenance visibility and manual compaction queueing in the Cloudflare dashboard. These updates make it easier to understand when maintenance is eligible to run, inspect completed operations, and request maintenance without leaving the table view.</p>
<p>To view table maintenance details:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/17742.md")</div>
<p><img src="/assets/upstream/images/r2-data-catalog/table-maintenance-view.png" alt="Maintenance tab for an R2 Data Catalog table showing schedules and recent runs" /></p>
<p>The updated dashboard includes:</p>
<ul>
<li><strong>Maintenance tab</strong> — View compaction and snapshot expiration settings, schedules, and next eligibility alongside the table's <strong>Schema</strong> and <strong>Metadata</strong> tabs.</li>
<li><strong>Recent runs</strong> — Review a paginated audit log with job status, duration, and expandable details for manifest rewrites, compaction, and snapshot expiration. Expanded rows include operation metrics for each maintenance operation.</li>
<li><strong>Manual queueing</strong> — Select <strong>Queue maintenance</strong> to request compaction during normal scheduler polling. The dashboard checks permissions and explains when another maintenance job conflicts with the request or the daily accepted-request limit has been reached.</li>
<li><strong>Updated catalog layout</strong> — Find catalog metrics in the <strong>Metrics</strong> tab, use the renamed <strong>Explorer</strong> tab to browse data, and switch between table details using tabs instead of a scroll-to-section sidebar.</li>
<li><strong>Improved schema browser</strong> — For accounts with the schema browser enabled, select a namespace to open its tables in the right pane while also expanding the namespace tree. The tree can now be collapsed to provide more space for table details.</li>
</ul>
<p>For more information about compaction and snapshot expiration, refer to <a href="/r2-data-catalog/table-maintenance/">Table maintenance</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-15">Sep 15, 2026</time><div>
<h2 id="post-2026-09-15-instance-event-subscriptions"><a href="/changelog/post/2026-09-15-instance-event-subscriptions/">Stream Workflow instance events in your Worker or via the API with .subscribe()</a></h2>
<div class="changelog-badges"><span>workflows</span><span>workers</span></div><div class="changelog-body"><p>You can now stream Workflow instance events via <code>WorkflowInstance.subscribe()</code> and the <code>GET /subscribe</code> API endpoint. Workers and HTTP clients can react to <a href="/workflows/build/events-and-parameters/">workflow</a> and <a href="/workflows/build/step-context/#workflowstepcontext">step</a> events, including attempts, sleeps, waits, and rollbacks, without polling for instance status.</p>
<p>A subscription first streams the entire event history of the Workflow instance. After streaming past events, the subscription waits for new events as the instance runs. You can use <code>filter</code> to receive only specific event types or <code>cursor</code> to start a subscription at a specific event.</p>
<p>Use <code>.subscribe()</code> to update Workflow status in user-facing dashboards, send notifications when steps complete, or trigger follow-up work for specific events.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17835.md")</div>
<p>For event types, available fields, and subscription options, refer to <a href="/workflows/build/subscribe-to-instance-events/">Subscribe to events</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-15">Sep 15, 2026</time><div>
<h2 id="post-2026-09-15-infrastructure-target-tags"><a href="/changelog/post/2026-09-15-infrastructure-target-tags/">Access for Infrastructure now supports tagged targets and tag-based target criteria</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span><span>access</span></div><div class="changelog-body"><p><a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Access for Infrastructure</a> now integrates with <a href="/resource-tagging/">Resource Tagging</a>. You can attach key-value tags to <a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/#1-add-a-target">infrastructure targets</a> and use them in access policies.</p>
<p>You can manage tags on targets inline when you create or edit a target or through the central <a href="/resource-tagging/how-to/manage-tags/">Resource Tagging API</a>. Cloudflare keeps tags in sync across both methods.</p>
<p>Infrastructure applications also support a target criteria model with <code>include</code>, <code>require</code>, and <code>exclude</code> operators. Each operator can match targets by hostname, tag, or both.</p>
<ul>
<li><strong>Include</strong> matches targets that have any of the specified values.</li>
<li><strong>Require</strong> matches targets that have all of the specified values.</li>
<li><strong>Exclude</strong> rejects targets that have any of the specified values.</li>
</ul>
<p><img src="/assets/upstream/images/cloudflare-one/access/tags-in-infra-app.png" alt="Infrastructure application builder showing target criteria with an included tag, port 22, and SSH as the selected protocol" /></p>
<p>For more information, refer to <a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Add an infrastructure application</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-15">Sep 15, 2026</time><div>
<h2 id="post-2026-09-15-waf-release"><a href="/changelog/post/2026-09-15-waf-release/">WAF Release - 2026-09-15</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This release introduces new threat detections to enhance protection against command injection attempts, Server-Side Request Forgery (SSRF) targeting cloud metadata, and information disclosure within version control history.</p>
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
				<code class="nb-rule-id" title="b2170b7b1a2c4b8eba0b498eca453d31">ca453d31</code>
</td>
<td>N/A</td>
<td>SSRF - Cloud - 3</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="02c818297e6d42aaa55e67f5e540f17f">e540f17f</code>
</td>
<td>N/A</td>
<td>Version Control - Information Disclosure - Beta</td>
<td>Log</td>
<td>Block</td>
<td>This rule is merged into the original rule "Version Control - Information Disclosure" (ID:{" "}<code class="nb-rule-id" title="23548ee2b36547a1be09bb2c0550c529">0550c529</code>).</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="93793848937f4f988f1dfdabba458b4b">ba458b4b</code>
</td>
<td>N/A</td>
<td>Command Injection - Generic 10</td>
<td>Log</td>
<td>Block</td>
<td>This is a new detection.</td>
</tr>        
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-15">Sep 15, 2026</time><div>
<h2 id="post-scheduled-waf-release"><a href="/changelog/post/scheduled-waf-release/">WAF Release - Scheduled changes for 2026-09-22</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><table style="width: 100%">
<thead>
<tr>
<th>Announcement Date</th>
<th>Release Date</th>
<th>Release Behavior</th>
<th>Legacy Rule ID</th>
<th>Rule ID</th>
<th>Description</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>2026-09-15</td>
<td>2026-09-22</td>
<td>Log</td>
<td>N/A</td>
<td>
				<code class="nb-rule-id" title="40b93de7a8f848709c4ec3e60f0313d6">0f0313d6</code>
</td>
<td>SSRF - Block jar HTTP loopback payload</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>2026-09-15</td>
<td>2026-09-22</td>
<td>Log</td>
<td>N/A</td>
<td>
				<code class="nb-rule-id" title="ca05d6c847834f75a317c33b5f21b651">5f21b651</code>
</td>
<td>SSRF - Cloud,Link-Local non-standard IP notation</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>2026-09-15</td>
<td>2026-09-22</td>
<td>Log</td>
<td>N/A</td>
<td>
				<code class="nb-rule-id" title="48dfa3e5bef84063914edfe175cd912a">75cd912a</code>
</td>
<td>SSRF - Local non-standard IP notation</td>
<td>
				This is a new detection.
</td>
</tr>	
<tr>
<td>2026-09-15</td>
<td>2026-09-22</td>
<td>Log</td>
<td>N/A</td>
<td>
				<code class="nb-rule-id" title="cd1de1fd21c443508f9073f2a1ba83f6">a1ba83f6</code>
</td>
<td>SSTI - Jinja Dangerous Globals Chain</td>
<td>
				This is a new detection.
</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-15">Sep 15, 2026</time><div>
<h2 id="post-2026-09-15-granular-worker-permissions"><a href="/changelog/post/2026-09-15-granular-worker-permissions/">Grant teammates and agents access to specific Workers</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now grant access to specific Workers and choose from four roles to control the level of access you give teammates, agents, and CI/CD workflows.</p>
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
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-14">Sep 14, 2026</time><div>
<h2 id="post-2026-09-14-saml-force-authentication"><a href="/changelog/post/2026-09-14-saml-force-authentication/">Require fresh authentication for SAML identity providers</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>Cloudflare Access can now request fresh authentication from a SAML identity provider for every login. Turn on <strong>Require reauthentication</strong> in the Cloudflare dashboard, or set <code>force_authn</code> to <code>true</code> through the API. Access will then set <code>ForceAuthn</code> to <code>true</code> in signed and unsigned SAML authentication requests.</p>
<p>This option is useful when an application requires users to reauthenticate at the identity provider instead of relying on an existing identity provider session. The default value is <code>false</code>.</p>
<p>For configuration details, refer to <a href="/cloudflare-one/integrations/identity-providers/generic-saml/#require-fresh-authentication-at-the-identity-provider">Require fresh authentication at the identity provider</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-14">Sep 14, 2026</time><div>
<h2 id="post-2026-09-14-require-provider-credentials"><a href="/changelog/post/2026-09-14-require-provider-credentials/">Prevent Unified Billing fallback for BYOK third-party providers</a></h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p>AI Gateway can now require credentials for third-party provider requests. Credentials must accompany the request or be stored on the gateway. This setting prevents fallback to Unified Billing with Cloudflare-managed credentials.</p>
<p>Turn on <strong>Require provider credentials</strong> in your gateway settings. To use the API, set <code>byok_only</code> to <code>true</code> in the request body of a <a href="/api/resources/ai_gateway/methods/update/"><code>PUT</code> request to update the gateway</a>:</p>
<pre><code class="language-json">{&#10;	&quot;byok_only&quot;: true&#10;}&#10;</code></pre>
<p>To require provider credentials for one third-party request, set the <code>cf-aig-no-wholesale</code> header to <code>true</code>. This header cannot relax the gateway setting.</p>
<p>Requests without applicable credentials then return an HTTP <code>400</code> response. Workers AI requests remain allowed, and the setting does not change their configured billing mode.</p>
<p>For configuration details and request-level controls, refer to <a href="/ai-gateway/features/unified-billing/#prevent-unified-billing-fallback-for-byok-third-party-providers">Prevent Unified Billing fallback for BYOK third-party providers</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-14">Sep 14, 2026</time><div>
<h2 id="post-2026-09-14-guardrails"><a href="/changelog/post/2026-09-14-guardrails/">Control which hostnames Browser Run sessions can access</a></h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p><a href="/browser-run/">Browser Run</a> now supports <a href="/browser-run/features/guardrails/">guardrails</a>, which limit a browser session's HTTP and HTTPS requests to permitted hostnames.</p>
<p>Use guardrails when you need to:</p>
<ul>
<li>Keep a browser workflow limited to a specific website and its subdomains.</li>
<li>Load only known third-party APIs, scripts, images, and fonts.</li>
<li>Generate a screenshot or PDF from HTML you provide while preventing it from loading external content.</li>
</ul>
<p>Set guardrails when starting a session with Puppeteer, Playwright, or the REST API. With a browser binding named <code>MYBROWSER</code>, pass <code>guardrails</code> when launching Puppeteer:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17700.md")</div>
<p>In addition to session guardrails, Browser Run now supports a read-only mode for <a href="/browser-run/features/live-view/">Live View</a>. Live View lets you watch and interact with an active Browser Run session in real time. A read-only link lets someone watch without clicking, typing, navigating, or running JavaScript.</p>
<p>To create a read-only link, set <code>{ mode: &quot;readonly&quot; }</code> when generating the Live View URL. This setting affects only the person using that link. The session's hostname restrictions remain unchanged.</p>
<p>Refer to the <a href="/browser-run/features/guardrails/">guardrails documentation</a> for more information.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-14">Sep 14, 2026</time><div>
<h2 id="post-2026-09-14-passive-detection"><a href="/changelog/post/2026-09-14-passive-detection/">Discover where sensitive data goes before you create a Data Loss Prevention policy</a></h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p><strong>Passive Detection</strong> for <a href="/cloudflare-one/data-loss-prevention/">Cloudflare Data Loss Prevention (DLP)</a> lets you learn from your Gateway traffic before deciding what to log or block. Discover the sensitive data types in sampled traffic, explore their destinations, and use the findings to build policies around your organization's needs.</p>
<p>The dashboard brings together detections from sampled HTTP request and response bodies. Select an entry to follow its detections over time, review destinations, and check policy coverage. You do not need a Gateway DLP policy to get these insights, and existing Gateway policies continue to apply.</p>
<p><img src="/assets/upstream/images/changelog/dlp/passive-detection.gif" alt="Passive Detection dashboard showing detection totals, data type distribution, policy coverage, and detection entries" /></p>
<p>Passive Detection is generally available. The detection entries available to your account depend on your <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/">Zero Trust plan</a>.</p>
<p>To get started, refer to the <a href="/cloudflare-one/data-loss-prevention/passive-detection/">Passive Detection documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-14">Sep 14, 2026</time><div>
<h2 id="post-2026-09-14-shadowed-record-warnings"><a href="/changelog/post/2026-09-14-shadowed-record-warnings/">Shadowed record warnings are now available for all zones</a></h2>
<div class="changelog-badges"><span>dns</span></div><div class="changelog-body"><p>Cloudflare now displays warnings for shadowed records in all zones. A record is shadowed when a subdomain delegation gives authority for its name, or a name below it, to another set of nameservers. The record remains present, but your zone is not authoritative for it thus Cloudflare will not respond with it to matching DNS queries. These warnings help you find records that may no longer resolve from the expected zone.</p>
<p>Shadow metadata is also available in DNS records API responses when you set <code>include_shadow_metadata=true</code>. The metadata identifies the delegating <code>NS</code> records and, when applicable, whether an <code>A</code> or <code>AAAA</code> record is glue. For more information, refer to <a href="/dns/manage-dns-records/reference/shadowed-records/">Shadowed records</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-11">Sep 11, 2026</time><div>
<h2 id="post-2026-09-11-voice-diagnostics-turn-metrics"><a href="/changelog/post/2026-09-11-voice-diagnostics-turn-metrics/">Inspect Voice Agent turn latency and outcomes</a></h2>
<div class="changelog-badges"><span>agents</span></div><div class="changelog-body"><p><code>@cloudflare/voice</code> v0.4.0 now lets you inspect where each Voice Agent turn spends time and how it ends.</p>
<pre><code class="language-ts">client.addEventListener(&quot;turnmetrics&quot;, (turn) =&gt; {&#10;	console.log(turn.outcome, turn.turnTotalMs);&#10;});&#10;</code></pre>
<h4 id="2026-09-11-voice-diagnostics-turn-metrics-about-the-voice-package">About the Voice package</h4>
<p>The <code>@cloudflare/voice</code> package lets you build real-time voice agents with Cloudflare Agents. It streams microphone audio to an Agent over WebSocket, transcribes speech, runs your model through <code>onTurn()</code>, converts the response to speech, and streams audio back to the caller.</p>
<p>A turn moves through several stages:</p>
<pre><code class="language-txt">User speaks -&gt; speech-to-text -&gt; model -&gt; text-to-speech -&gt; audio&#10;</code></pre>
<p>Previously, the package's four aggregate metrics covered successful, non-empty speech turns. They did not show how failed, aborted, empty, or text turns ended.</p>
<h4 id="2026-09-11-voice-diagnostics-turn-metrics-turn-metrics">Turn metrics</h4>
<p>Each speech or text turn now produces a typed <code>VoiceTurnMetrics</code> summary with:</p>
<ul>
<li>A <code>turnId</code> for correlating events from the same turn.</li>
<li>A terminal outcome such as <code>completed</code>, <code>no_output</code>, <code>output_limit</code>, <code>content_filtered</code>, <code>model_error</code>, <code>tts_error</code>, or <code>aborted</code>.</li>
<li>Timings for important stages, including speech-to-final-transcript, model-to-first-text, TTS-to-first-audio, and total turn duration.</li>
</ul>
<p>These timings can overlap and are not additive. Timings for stages that a turn did not reach are omitted.</p>
<p>The latest summary is available through <code>VoiceClient</code>, <code>useVoiceAgent()</code>, and <code>useVoiceInput()</code>. Voice input includes only the speech and transcription timings it can measure.</p>
<p>If an agent produces no audio, you can now distinguish between the model returning no output, reaching an output limit, encountering content filtering, or failing.</p>
<h4 id="2026-09-11-voice-diagnostics-turn-metrics-additional-diagnostics">Additional diagnostics</h4>
<p>For local debugging, you can forward server lifecycle events to the browser console:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17686.md")</div>
<p>The browser console combines server lifecycle events with local microphone, connection, and playback events, including model start, first model text, first audio, and playback start. Diagnostics are off by default, and their event names and fields can change.</p>
<p><code>VoiceClient</code> also exposes typed events for speech-to-text failures, connection errors, and model outcomes. The SDK removes known content fields and does not read arbitrary provider responses, but custom error messages must not contain sensitive data.</p>
<p>Install the release with a compatible Agents SDK version:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/voice@^0.4.0 agents@^0.22.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/voice@^0.4.0 agents@^0.22.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/voice@^0.4.0 agents@^0.22.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/voice@^0.4.0 agents@^0.22.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/voice@^0.4.0 agents@^0.22.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/voice@^0.4.0 agents@^0.22.0" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/voice@^0.4.0 agents@^0.22.0</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/voice@^0.4.0 agents@^0.22.0" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Refer to the <a href="/agents/communication-channels/voice/#pipeline-metrics">Voice pipeline metrics</a> and <a href="https://github.com/cloudflare/agents/tree/main/examples/voice-agent">Voice Agent example</a> to get started.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-11">Sep 11, 2026</time><div>
<h2 id="post-2026-09-11-extensionless-r2-content-type"><a href="/changelog/post/2026-09-11-extensionless-r2-content-type/">AI Search supports extensionless R2 objects with Content-Type metadata</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p>AI Search can index R2 objects without filename extensions when they include supported <code>Content-Type</code> metadata. This supports object keys that do not include file extensions while preserving file-type validation during indexing.</p>
<p>For supported file types and Content-Type requirements, refer to <a href="/ai-search/configuration/data-source/r2/">R2 data sources</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-10">Sep 10, 2026</time><div>
<h2 id="post-2026-09-10-paid-retention-default"><a href="/changelog/post/2026-09-10-paid-retention-default/">Default instance retention for new Workflows on Workers Paid is seven days</a></h2>
<div class="changelog-badges"><span>workflows</span></div><div class="changelog-body"><p><a href="/workflows/">Workflows</a> created on or after September 10, 2026, on the Workers Paid plan retain completed and errored instance state for seven days by default (previously 30 days). The seven day default helps to reduce storage costs by default. The maximum retention <a href="/workflows/reference/limits/">limit</a> remains 30 days.</p>
<p>The retention period for existing Workflows is unchanged. The Workers Free plan retains its three-day default and limit.</p>
<p>To set the retention period for a Workflow instance, specify <code>successRetention</code>, <code>errorRetention</code>, or both:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17834.md")</div>
<p>You can also set the retention period per Workflow and per instance in the <a href="https://dash.cloudflare.com/?to=/:account/workers/workflows">Cloudflare dashboard</a>.</p>
<p>For retention details, refer to <a href="/workflows/reference/pricing/">Workflows pricing</a> and the <a href="/workflows/build/workers-api/#workflowinstancecreateoptions"><code>WorkflowInstanceCreateOptions</code> API reference</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-10">Sep 10, 2026</time><div>
<h2 id="post-2026-09-10-using-openai-agents-api-with-cloudflare-containers"><a href="/changelog/post/2026-09-10-using-openai-agents-api-with-cloudflare-containers/">Use Cloudflare Containers with Codex via the OpenAI Agents API</a></h2>
<div class="changelog-badges"><span>containers</span></div><div class="changelog-body"><p>The OpenAI Agents API gives your application access to Codex through an OpenAI-managed API.</p>
<p>OpenAI manages sessions, orchestration, context compaction, and recovery while your application provides tools and uses Cloudflare Containers as the execution environment.</p>
<p>Cloudflare Containers can now provide self-hosted execution environments for the OpenAI Agents API. The open-source <a href="https://github.com/cloudflare/sandbox-sdk/tree/main/openai/agents-api">OpenAI Agents API Workers template</a> provides a reference implementation. The Worker maintains a Cloudflare Container for each Codex session, keeps active work running, reconnects on follow-up input, and shuts down automatically when idle.</p>
<p>You can configure the reference implementation to meet your needs by extending the Container to provide controlled access to data and the network or by integrating it with other Cloudflare products.</p>
<p>To get started, refer to <a href="/sandbox/tutorials/openai-agents-api/">Run Codex on Cloudflare using the OpenAI Agents API</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-10">Sep 10, 2026</time><div>
<h2 id="post-2026-09-10-emergency-waf-release"><a href="/changelog/post/2026-09-10-emergency-waf-release/">WAF Release - 2026-09-10 - Emergency</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This update provides immediate defense against a high-severity, actively exploited zero-day vulnerability targeting Adobe Commerce and Magento Open Source storefronts.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>Adobe Commerce and Magento RCE (CVE-2026-75650 / &quot;StyleSmuggler&quot;): Unauthenticated Remote Code Execution (RCE) vulnerability caused by improper neutralization of special elements in the platform's template engine. Unauthenticated attackers can inject arbitrary PHP payloads through style properties to execute system commands and deploy persistent malware.</li>
</ul>
<p><strong>Impact</strong></p>
<p>This emergency rule provides immediate edge-level mitigation and virtual patching, origin applications must be urgently updated. We strongly recommend to apply the hotfix outlined in Adobe Security Bulletin <a href="https://experienceleague.adobe.com/en/docs/commerce-knowledge-base/kb/announcements/commerce-apsb26-146">APSB26-146</a> and immediately rotate all potentially exposed encryption keys, integration tokens, and system credentials, as patching alone does not remediate an existing compromise.</p>
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
				<code class="nb-rule-id" title="f9a3026b0fdc4d63b7338346440f5c55">440f5c55</code>
</td>
<td>N/A</td>
<td>Adobe Commerce - Remote Code Execution - CVE:CVE-2026-75650</td>
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
<time datetime="2026-09-10">Sep 10, 2026</time><div>
<h2 id="post-2026-09-09-warp-macos-beta"><a href="/changelog/post/2026-09-09-warp-macos-beta/">Cloudflare One Client for macOS (version 2026.8.1290.1)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new Beta release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This beta release includes the following changes and improvements:</p>
<ul>
<li>Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.</li>
<li>Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.</li>
<li>Improved API reliability by retrying requests dropped when reusing pooled connections.</li>
<li>Fixed Extra Logging failing to capture packets across all interfaces.</li>
<li>Fixed an issue that could prevent remote diagnostics from completing.</li>
<li>Fixed DNS connectivity checks failing on IPv6-only networks.</li>
<li>Fixed the client service exiting when its route-monitoring socket was closed after sleep or wake.</li>
<li>Fixed DNS enforcement checks making the client service unresponsive on systems with large routing tables.</li>
<li>Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.</li>
<li>Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.</li>
<li>Fixed the client continuing to report 'No network' after a successful manual disconnect.</li>
<li>Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.</li>
<li>Fixed a startup crash when date formatting data for the system locale had not yet loaded.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>None</li>
</ul>
<p>For Zero Trust documentation, see: <a href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/</a><br />
For Consumer documentation, see: <a href="https://developers.cloudflare.com/warp-client/">https://developers.cloudflare.com/warp-client/</a></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-10">Sep 10, 2026</time><div>
<h2 id="post-2026-09-09-warp-windows-beta"><a href="/changelog/post/2026-09-09-warp-windows-beta/">Cloudflare One Client for Windows (version 2026.8.1290.1)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new Beta release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This beta release includes the following changes and improvements:</p>
<ul>
<li>Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.</li>
<li>Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.</li>
<li>Improved API reliability by retrying requests dropped when reusing pooled connections.</li>
<li>The client no longer requires the Windows WLAN AutoConfig service to be running.</li>
<li>Implemented a service recovery mechanism backed by Windows scheduler task to start WARP service on system unlock if not already started.</li>
<li>Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.</li>
<li>Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.</li>
<li>Fixed the client continuing to report 'No network' after a successful manual disconnect.</li>
<li>Fixed Digital Experience Monitoring (DEX) HTTP tests failing TLS validation on Windows.</li>
<li>Fixed the client UI crashing at startup when it could not write to the Windows registry.</li>
<li>Fixed latency spikes and traffic interruptions during TPM-backed API authentication when hardware-backed registration is enabled.</li>
<li>Fixed trailing whitespace in BIOS serial numbers causing serial-number and client-certificate device posture checks to fail.</li>
<li>Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.</li>
<li>Fixed a startup crash when date formatting data for the system locale had not yet loaded.</li>
</ul>
<p><strong>Known issues</strong></p>
<ul>
<li>None</li>
</ul>
<p>For Zero Trust documentation, see: <a href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/</a><br />
For Consumer documentation, see: <a href="https://developers.cloudflare.com/warp-client/">https://developers.cloudflare.com/warp-client/</a></p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-09">Sep 9, 2026</time><div>
<h2 id="post-2026-09-09-custom-cache-token-costs"><a href="/changelog/post/2026-09-09-custom-cache-token-costs/">AI Gateway custom costs support cache tokens</a></h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p>AI Gateway custom costs now support cache-read and cache-write token rates. This lets custom cost metrics reflect negotiated cache pricing across providers.</p>
<p>Add <code>per_cache_read_token</code> or <code>per_cache_write_token</code> to the <code>cf-aig-custom-cost</code> header:</p>
<pre><code class="language-json">{&#10;	&quot;per_token_in&quot;: 0.000001,&#10;	&quot;per_token_out&quot;: 0.000002,&#10;	&quot;per_cache_read_token&quot;: 0.0000001,&#10;	&quot;per_cache_write_token&quot;: 0.0000005&#10;}&#10;</code></pre>
<p>Cache-token pricing activates when either cache rate is present. An omitted cache rate defaults to <code>per_token_in</code>. If both cache rates are omitted, AI Gateway preserves the existing input and output calculation.</p>
<p>Providers can include cache tokens within input tokens or report them separately. AI Gateway automatically accounts for these differences and prevents double-counting.</p>
<p>For more information, refer to <a href="/ai-gateway/configuration/custom-costs/">Custom costs</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-09-09">Sep 9, 2026</time><div>
<h2 id="post-2026-09-09-ios-tap-to-type"><a href="/changelog/post/2026-09-09-ios-tap-to-type/">Improved iOS tap-to-type experience for Browser Isolation</a></h2>
<div class="changelog-badges"><span>browser-isolation</span><span>cloudflare-one</span></div><div class="changelog-body"><p><a href="/cloudflare-one/remote-browser-isolation/">Browser Isolation</a> has improved the tap-to-type experience for users on iOS devices.</p>
<p>Previously, Browser Isolation displayed a full-screen overlay with the message <code>tap to type</code> when users focused a text field. The prompt now appears inline over the focused text field, reducing disruption when users enter text in isolated sessions.</p>
<p>If the focused text field is too small to display the full prompt, Browser Isolation displays a keyboard icon in the center of the text field instead.</p>
<p><img src="/assets/upstream/images/cloudflare-one/rbi/tap-to-type.jpg" alt="Inline tap-to-type prompt over a focused text field in Browser Isolation" /></p>
<p>iOS users should tap twice to begin entering text. This update applies automatically to Browser Isolation sessions on iOS.</p>
<p>For more information on why this interaction is required, refer to <a href="/cloudflare-one/remote-browser-isolation/known-limitations/#ios">iOS limitations</a>.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><span>Page 1 of 50</span><a class="pagination-next" rel="next" href="/changelog/2/">Next</a></nav>
</div>
