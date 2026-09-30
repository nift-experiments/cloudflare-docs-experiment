<h1 id="changelog">Changelog</h1>

<h2 id="delete-workflow-instances-individually-or-in-batches"><a href="/changelog/post/2026-09-17-instance-delete/">Delete Workflow instances individually or in batches</a></h2>
<p><em>2026-09-17 12:00:00 UTC</em></p>
<p>You can now delete one or up to 100 Workflow instances and their stored state via the <a href="/workflows/build/workers-api/">Workflows API</a> or Wrangler 4.125.0 and later. Deleting an instance frees its stored state and stops its current execution. <a href="/workflows/reference/pricing/#storage-usage">Storage billing</a> is based on the average daily peak.</p>
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


<h2 id="reject-busy-synchronous-inference-requests"><a href="/changelog/post/2026-09-17-reject-if-busy/">Reject busy synchronous inference requests</a></h2>
<p><em>2026-09-17</em></p>
<p>The <code>rejectIfBusy</code> option lets synchronous Workers AI inference requests fail when capacity is unavailable. Use it when your application should not wait in a capacity queue.</p>
<p>Pass the option as the third argument to the Workers AI binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17820.md")</div>
<p>For the native REST API, add the option to the request body:</p>
<pre><code class="language-bash">curl --request POST \&#10;  &#45;-url &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai/run/@cf/google/gemma-4-26b-a4b-it&quot; \&#10;  &#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;messages&quot;: [{ &quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;Explain capacity queues.&quot; }],&#10;    &quot;options&quot;: { &quot;rejectIfBusy&quot;: true }&#10;  }&#x27;&#10;</code></pre>
<p>Refer to <a href="/workers-ai/features/reject-if-busy/">Reject busy requests</a> for OpenAI-compatible usage and error behavior.</p>


<h2 id="hyperdrive-support-for-python-workers"><a href="/changelog/post/2026-09-16-hyperdrive-python-workers/">Hyperdrive support for Python Workers</a></h2>
<p><em>2026-09-16</em></p>
<p><a href="/workers/languages/python/">Python Workers</a> can now connect to PostgreSQL and MySQL through Hyperdrive.</p>
<p>For setup, code examples, and limitations, refer to <a href="/hyperdrive/examples/python-workers/">Use Hyperdrive from Python Workers</a>.</p>


<h2 id="r2-data-catalog-adds-table-maintenance-visibility-and-manual-queueing"><a href="/changelog/post/2026-09-16-table-maintenance-dashboard/">R2 Data Catalog adds table maintenance visibility and manual queueing</a></h2>
<p><em>2026-09-16</em></p>
<p><a href="/r2-data-catalog/">R2 Data Catalog</a> now provides table-level maintenance visibility and manual compaction queueing in the Cloudflare dashboard. These updates make it easier to understand when maintenance is eligible to run, inspect completed operations, and request maintenance without leaving the table view.</p>
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


<h2 id="prevent-unified-billing-fallback-for-byok-third-party-providers"><a href="/changelog/post/2026-09-14-require-provider-credentials/">Prevent Unified Billing fallback for BYOK third-party providers</a></h2>
<p><em>2026-09-14</em></p>
<p>AI Gateway can now require credentials for third-party provider requests. Credentials must accompany the request or be stored on the gateway. This setting prevents fallback to Unified Billing with Cloudflare-managed credentials.</p>
<p>Turn on <strong>Require provider credentials</strong> in your gateway settings. To use the API, set <code>byok_only</code> to <code>true</code> in the request body of a <a href="/api/resources/ai_gateway/methods/update/"><code>PUT</code> request to update the gateway</a>:</p>
<pre><code class="language-json">{&#10;	&quot;byok_only&quot;: true&#10;}&#10;</code></pre>
<p>To require provider credentials for one third-party request, set the <code>cf-aig-no-wholesale</code> header to <code>true</code>. This header cannot relax the gateway setting.</p>
<p>Requests without applicable credentials then return an HTTP <code>400</code> response. Workers AI requests remain allowed, and the setting does not change their configured billing mode.</p>
<p>For configuration details and request-level controls, refer to <a href="/ai-gateway/features/unified-billing/#prevent-unified-billing-fallback-for-byok-third-party-providers">Prevent Unified Billing fallback for BYOK third-party providers</a>.</p>


<h2 id="control-which-hostnames-browser-run-sessions-can-access"><a href="/changelog/post/2026-09-14-guardrails/">Control which hostnames Browser Run sessions can access</a></h2>
<p><em>2026-09-14</em></p>
<p><a href="/browser-run/">Browser Run</a> now supports <a href="/browser-run/features/guardrails/">guardrails</a>, which limit a browser session's HTTP and HTTPS requests to permitted hostnames.</p>
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


<h2 id="inspect-voice-agent-turn-latency-and-outcomes"><a href="/changelog/post/2026-09-11-voice-diagnostics-turn-metrics/">Inspect Voice Agent turn latency and outcomes</a></h2>
<p><em>2026-09-11</em></p>
<p><code>@cloudflare/voice</code> v0.4.0 now lets you inspect where each Voice Agent turn spends time and how it ends.</p>
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


<h2 id="ai-search-supports-extensionless-r2-objects-with-content-type-metadata"><a href="/changelog/post/2026-09-11-extensionless-r2-content-type/">AI Search supports extensionless R2 objects with Content-Type metadata</a></h2>
<p><em>2026-09-11</em></p>
<p>AI Search can index R2 objects without filename extensions when they include supported <code>Content-Type</code> metadata. This supports object keys that do not include file extensions while preserving file-type validation during indexing.</p>
<p>For supported file types and Content-Type requirements, refer to <a href="/ai-search/configuration/data-source/r2/">R2 data sources</a>.</p>


<h2 id="default-instance-retention-for-new-workflows-on-workers-paid-is-seven-days"><a href="/changelog/post/2026-09-10-paid-retention-default/">Default instance retention for new Workflows on Workers Paid is seven days</a></h2>
<p><em>2026-09-10 12:00:00 UTC</em></p>
<p><a href="/workflows/">Workflows</a> created on or after September 10, 2026, on the Workers Paid plan retain completed and errored instance state for seven days by default (previously 30 days). The seven day default helps to reduce storage costs by default. The maximum retention <a href="/workflows/reference/limits/">limit</a> remains 30 days.</p>
<p>The retention period for existing Workflows is unchanged. The Workers Free plan retains its three-day default and limit.</p>
<p>To set the retention period for a Workflow instance, specify <code>successRetention</code>, <code>errorRetention</code>, or both:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17834.md")</div>
<p>You can also set the retention period per Workflow and per instance in the <a href="https://dash.cloudflare.com/?to=/:account/workers/workflows">Cloudflare dashboard</a>.</p>
<p>For retention details, refer to <a href="/workflows/reference/pricing/">Workflows pricing</a> and the <a href="/workflows/build/workers-api/#workflowinstancecreateoptions"><code>WorkflowInstanceCreateOptions</code> API reference</a>.</p>


<h2 id="use-cloudflare-containers-with-codex-via-the-openai-agents-api"><a href="/changelog/post/2026-09-10-using-openai-agents-api-with-cloudflare-containers/">Use Cloudflare Containers with Codex via the OpenAI Agents API</a></h2>
<p><em>2026-09-10</em></p>
<p>The OpenAI Agents API gives your application access to Codex through an OpenAI-managed API.</p>
<p>OpenAI manages sessions, orchestration, context compaction, and recovery while your application provides tools and uses Cloudflare Containers as the execution environment.</p>
<p>Cloudflare Containers can now provide self-hosted execution environments for the OpenAI Agents API. The open-source <a href="https://github.com/cloudflare/sandbox-sdk/tree/main/openai/agents-api">OpenAI Agents API Workers template</a> provides a reference implementation. The Worker maintains a Cloudflare Container for each Codex session, keeps active work running, reconnects on follow-up input, and shuts down automatically when idle.</p>
<p>You can configure the reference implementation to meet your needs by extending the Container to provide controlled access to data and the network or by integrating it with other Cloudflare products.</p>
<p>To get started, refer to <a href="/sandbox/tutorials/openai-agents-api/">Run Codex on Cloudflare using the OpenAI Agents API</a>.</p>


<h2 id="ai-gateway-custom-costs-support-cache-tokens"><a href="/changelog/post/2026-09-09-custom-cache-token-costs/">AI Gateway custom costs support cache tokens</a></h2>
<p><em>2026-09-09</em></p>
<p>AI Gateway custom costs now support cache-read and cache-write token rates. This lets custom cost metrics reflect negotiated cache pricing across providers.</p>
<p>Add <code>per_cache_read_token</code> or <code>per_cache_write_token</code> to the <code>cf-aig-custom-cost</code> header:</p>
<pre><code class="language-json">{&#10;	&quot;per_token_in&quot;: 0.000001,&#10;	&quot;per_token_out&quot;: 0.000002,&#10;	&quot;per_cache_read_token&quot;: 0.0000001,&#10;	&quot;per_cache_write_token&quot;: 0.0000005&#10;}&#10;</code></pre>
<p>Cache-token pricing activates when either cache rate is present. An omitted cache rate defaults to <code>per_token_in</code>. If both cache rates are omitted, AI Gateway preserves the existing input and output calculation.</p>
<p>Providers can include cache tokens within input tokens or report them separately. AI Gateway automatically accounts for these differences and prevents double-counting.</p>
<p>For more information, refer to <a href="/ai-gateway/configuration/custom-costs/">Custom costs</a>.</p>


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


<h2 id="r2-data-access-logs"><a href="/changelog/post/2026-09-04-r2-data-access-logs/">R2 Data Access Logs</a></h2>
<p><em>2026-09-04</em></p>
<p>R2 Data Access Logs are now generally available. Turn on logging for a bucket to record object read, write, list, multipart upload, and delete operations with response status codes below <code>400</code>.</p>
<p>Data Access Logs cover requests made through the S3-compatible API, Cloudflare API and dashboard, Workers bindings, and public buckets through <code>r2.dev</code> or custom domains. Events are available in Workers Observability, where you can filter by bucket, operation, interface, actor, and other request fields.</p>
<p>Log delivery is asynchronous and best effort. Events may be delayed or omitted, so do not rely on Data Access Logs as a complete record of bucket activity.</p>
<p>Data Access Logs are available for non-jurisdictional buckets. For setup instructions, supported operations, and the event field reference, refer to <a href="/r2/buckets/data-access-logs/">R2 Data Access Logs</a>.</p>


<h2 id="deploy-larger-workers-up-to-64-mib-for-both-free-and-paid-plans"><a href="/changelog/post/2026-09-04-increased-worker-size-limit/">Deploy larger Workers — up to 64 MiB for both free and paid plans</a></h2>
<p><em>2026-09-04</em></p>
<p>You can now deploy Workers with larger dependencies, heavier frameworks, and more code without hitting size limits.</p>
<p>When you deploy a Worker, Wrangler bundles your code and compresses it before uploading. Previously, Cloudflare checked that compressed size and rejected deploys over 3 MB (Free) or 10 MB (Paid). That limit has been removed. Cloudflare now only checks the uncompressed size of your bundle, which is 64 MiB across all plans.</p>
<p>To check your Worker's bundle size before deploying:</p>
<pre><code class="language-sh">wrangler deploy --outdir bundled/ --dry-run&#10;</code></pre>
<pre><code class="language-sh">Total Upload: 259.61 KiB / gzip: 47.23 KiB&#10;</code></pre>
<p>The <code>Total Upload</code> value is your uncompressed bundle size. This is what counts against the 64 MiB limit. The <code>gzip</code> value is shown for reference but is no longer a limit.</p>
<p>For more information, refer to the <a href="/workers/platform/limits/#worker-size">Worker size limits documentation</a>.</p>


<h2 id="new-in-images-text-rasterization-and-updates-to-the-binding"><a href="/changelog/post/2026-09-02-images-binding-updates/">New in Images: text rasterization and updates to the binding</a></h2>
<p><em>2026-09-02</em></p>
<p>We've added more ways to manage and manipulate images with the <a href="/images/optimization/binding/">Images binding</a>. Here's what's new:</p>
<p><strong>Render text into an image.</strong> Output a string of text into its own image or draw it over another image.</p>
<ul>
<li>Use the <a href="/images/optimization/binding/#textcontent-options"><code>.text()</code></a> method to rasterize text with the Images binding.</li>
<li>Style content using the <code>font</code>, <code>size</code>, and <code>color</code> options.</li>
<li>The <a href="/images/optimization/draw-overlays/#draw-with-cfimage"><code>draw</code></a> array in <code>cf.image</code> now accepts a <code>text</code> key.</li>
</ul>
<p><strong>Manage hosted images without an API token.</strong></p>
<ul>
<li><strong>Metadata filtering:</strong> Pass <code>filter.metadata</code> to <a href="/images/storage/binding/#listoptions"><code>.list()</code></a> to return images by custom metadata. Match a bounded range by setting two operators in one condition, for example, <code>priority: { gte: 2, lte: 5 }</code>.</li>
<li><strong>Server-side signing:</strong> Get a signed URL for a private image with <a href="/images/storage/binding/#imageimageidsignedurloptions"><code>.signedUrl()</code></a>.</li>
<li><strong>User uploads:</strong> Create a Direct Creator Upload link with <a href="/images/storage/binding/#createdirectuploadoptions"><code>.createDirectUpload()</code></a> so that a client can upload an image to your storage.</li>
</ul>
<p><strong>Set headers in a single call.</strong></p>
<ul>
<li>Pass a <code>headers</code> option to <a href="/images/optimization/binding/#responseoptions"><code>.response()</code></a> to set headers without rebuilding the <code>Response</code>.</li>
<li><code>Content-Type</code> is always taken from the optimized image and can't be overridden by a specified header.</li>
<li>Set <code>Cache-Control</code> with <a href="/workers/cache/">Workers Cache</a> to cache your optimized image at the edge.</li>
</ul>
<p>For more information, refer to <a href="/images/optimization/binding/">Optimize with Workers</a>, <a href="/images/optimization/draw-overlays/">Draw overlays and watermarks</a>, and <a href="/images/storage/binding/">Manage hosted images with Workers</a>.</p>


<h2 id="create-multiple-cloudflare-tunnel-and-cloudflare-mesh-routes-at-once"><a href="/changelog/post/2026-09-02-tunnel-mesh-bulk-route-creation/">Create multiple Cloudflare Tunnel and Cloudflare Mesh routes at once</a></h2>
<p><em>2026-09-02</em></p>
<p>You can now create multiple <a href="/tunnel/">Cloudflare Tunnel</a> and <a href="/mesh/">Cloudflare Mesh</a> routes from the Routes page in a single action, instead of submitting one route at a time.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/2026-09-01-tunnel-mesh-bulk.gif" alt="Creating multiple Cloudflare Tunnel and Cloudflare Mesh routes at once from the Routes page" /></p>
<p>When creating a route, you can now:</p>
<ul>
<li><strong>Add multiple destinations at once</strong> — Enter a comma-separated list of CIDR ranges or hostnames to create several routes of the same type and connector together.</li>
<li><strong>Queue up multiple routes</strong> — Select <strong>Add another</strong> to stage additional routes, including different types or connectors, before creating them all in one action.</li>
<li><strong>Retry only what failed</strong> — If some routes in a batch fail (for example, an invalid CIDR), the routes that were created successfully are removed from the form automatically, so you only need to fix and resubmit the ones that failed.</li>
</ul>
<p>The same Routes UI already supports bulk creation for <a href="/cloudflare-wan/">Cloudflare WAN</a> static routes, so you can add multiple WAN destinations or queue up several WAN routes before creating them together as well.</p>
<div class="nb-dash-button"></div>
<p>For setup steps, refer to <a href="/cloudflare-one/networks/routes/add-routes/">Add routes</a>.</p>


<h2 id="run-cursor-cloud-agents-on-cloudflare-via-self-hosted-machines"><a href="/changelog/post/2026-09-02-cursor-cloud-agents/">Run Cursor Cloud Agents on Cloudflare via self-hosted machines</a></h2>
<p><em>2026-09-02</em></p>
<p><a href="https://cursor.com/docs/cloud-agent/self-hosted">Cursor self-hosted machines</a> let you run Cursor Cloud Agents on Cloudflare. Each assigned session runs in its own isolated environment backed by <a href="/containers/">Cloudflare Containers</a>.</p>
<p><img src="/assets/upstream/images/changelog/sandbox/cursor-cloud-agents-self-hosted-pool.png" alt="Cursor Cloud Agents environment selector showing the cloudflare-pool self-hosted machine pool" /></p>
<p>Cursor hosts the agent loop, inference, and planning. Cloudflare runs commands, file edits, repository operations, and other tools inside infrastructure that you control. The open-source <a href="https://github.com/anysphere/cloudflare-workers">Cursor Cloudflare Workers template</a> deploys the Worker, Durable Object namespace, container application, R2 bucket binding, and cron trigger used by the integration.</p>
<p>To get started, refer to <a href="/sandbox/tutorials/cursor-cloud-agents/">Run Cursor Cloud Agents on Cloudflare via self-hosted machines</a>.</p>


<h2 id="python-workers-now-support-wsgi-web-frameworks-like-django-and-flask"><a href="/changelog/post/2026-09-02-python-workers-web-framework-support/">Python Workers now support WSGI web frameworks like Django and Flask</a></h2>
<p><em>2026-09-02</em></p>
<p>Python web frameworks following the <a href="https://peps.python.org/pep-3333/">Web Server Gateway Interface (WSGI)</a> or <a href="https://asgi.readthedocs.io/">Asynchronous Server Gateway Interface (ASGI)</a> specification can now be used in Python Workers.</p>
<h4 id="2026-09-02-python-workers-web-framework-support-using-web-frameworks-with-python-workers">Using web frameworks with Python Workers</h4>
<p>Based on the web framework you are using, you can use either <code>wsgi</code> or <code>asgi</code> from the <code>workers</code> module.</p>
<h4 id="2026-09-02-python-workers-web-framework-support-wsgi-frameworks">WSGI frameworks</h4>
<p>For WSGI frameworks like Django or Flask:</p>
<pre><code class="language-python">from workers import wsgi&#10;&#10;from django.core.wsgi import get_wsgi_application&#10;&#10;app = get_wsgi_application()&#10;Default = wsgi.entrypoint(app)&#10;</code></pre>
<p>The <code>wsgi.entrypoint</code> is equivalent to creating a <code>WorkerEntrypoint</code> class and using the <code>wsgi.fetch</code> method. If you want more control over the <code>WorkerEntrypoint</code> class, you can do so:</p>
<pre><code class="language-python">from workers import wsgi, WorkerEntrypoint&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        return await wsgi.fetch(app, request, self.env)&#10;</code></pre>
<h4 id="2026-09-02-python-workers-web-framework-support-asgi-frameworks">ASGI frameworks</h4>
<p>For ASGI frameworks like FastAPI or Starlette:</p>
<pre><code class="language-python">from workers import asgi&#10;&#10;from fastapi import FastAPI&#10;&#10;app = FastAPI()&#10;Default = asgi.entrypoint(app)&#10;</code></pre>
<p>For more information about using individual web frameworks, refer to the <a href="/workers/languages/python/packages/">packages documentation in Python Workers</a>.</p>


<h2 id="ai-gateway-consolidates-monthly-usage-invoice-line-items-and-standardizes-model-names"><a href="/changelog/post/2026-09-01-billing-and-model-names/">AI Gateway consolidates monthly usage invoice line items and standardizes model names</a></h2>
<p><em>2026-09-01</em></p>
<p>AI Gateway monthly usage invoices, issued at the beginning of each month for the previous month's usage, now show a single total cost for each model. These invoices no longer break out input and output token quantities and unit prices into separate line items. This change does not apply to invoices for AI Gateway credit purchases.</p>
<p>For example, an invoice that previously included these separate line items:</p>
<ul>
<li><code>anthropic claude-haiku-4-5-20251001 Input Tokens</code>: 40,000 tokens at $0.000001 ($0.04)</li>
<li><code>anthropic claude-haiku-4-5-20251001 Output Tokens</code>: 24,000 tokens at $0.000005 ($0.12)</li>
</ul>
<p>The updated invoice includes one line item: <code>anthropic/claude-haiku-4.5</code>: $0.16.</p>
<p>AI Gateway has also standardized model names across invoices and logs. Model variants that previously appeared with provider-specific version suffixes now use a consistent <code>provider/model</code> identifier.</p>
<p>For more information, refer to the <a href="/ai-gateway/features/unified-billing/">Unified Billing documentation</a> and <a href="/ai-gateway/observability/logging/">AI Gateway logging documentation</a>.</p>


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


<nav class="pagination" aria-label="Changelog pages"><span>Page 1 of 23</span><a class="pagination-next" rel="next" href="/changelog/product-group/developer-platform/2/">Next</a></nav>
