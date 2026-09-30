<p>Integrate <a href="/workflows/">Cloudflare Workflows</a> with Agents for durable, multi-step background processing while Agents handle real-time communication.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="agents-vs-workflows">Agents vs. Workflows</h3>
@markup("md", "content/.markup/bodies/2489.md")
</aside>
<h2 id="quick-start">Quick start</h2>
<h3 id="1-define-a-workflow"><ol>
<li>Define a Workflow</li>
</ol></h3>
<p>Extend <code>AgentWorkflow</code> for typed access to the originating Agent:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2490.md")
</div>
<h3 id="2-start-a-workflow-from-an-agent"><ol start="2">
<li>Start a Workflow from an Agent</li>
</ol></h3>
<p>Use <code>runWorkflow()</code> to start and track workflows:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2491.md")
</div>
<h3 id="3-configure-wrangler"><ol start="3">
<li>Configure Wrangler</li>
</ol></h3>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2492.md")
</div>
<h2 id="agentworkflow-class">AgentWorkflow class</h2>
<p>Base class for Workflows that integrate with Agents.</p>
<h3 id="type-parameters">Type parameters</h3>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>AgentType</code></td>
<td>The Agent class type for typed RPC</td>
</tr>
<tr>
<td><code>Params</code></td>
<td>Parameters passed to the workflow</td>
</tr>
<tr>
<td><code>ProgressType</code></td>
<td>Type for progress reporting (defaults to <code>DefaultProgress</code>)</td>
</tr>
<tr>
<td><code>Env</code></td>
<td>Environment type (defaults to <code>Cloudflare.Env</code>)</td>
</tr>
</tbody>
</table>
<h3 id="properties">Properties</h3>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>agent</code></td>
<td>Stub</td>
<td>Typed stub for calling Agent methods. For workflows started from a sub-agent, this is an RPC-only stub back to the originating facet; use sub-agent routing for HTTP or WebSocket <code>fetch()</code> traffic</td>
</tr>
<tr>
<td><code>instanceId</code></td>
<td>string</td>
<td>The workflow instance ID</td>
</tr>
<tr>
<td><code>workflowName</code></td>
<td>string</td>
<td>The workflow binding name</td>
</tr>
<tr>
<td><code>env</code></td>
<td>Env</td>
<td>Environment bindings</td>
</tr>
</tbody>
</table>
<h3 id="instance-methods-non-durable">Instance methods (non-durable)</h3>
<p>These methods may repeat on retry. Use for lightweight, frequent updates.</p>
<h4 id="reportprogress-progress">reportProgress(progress)</h4>
<p>Report progress to the Agent. Triggers <code>onWorkflowProgress</code> callback.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2493.md")
</div>
<h4 id="broadcasttoclients-message">broadcastToClients(message)</h4>
<p>Broadcast a message to all WebSocket clients connected to the Agent.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2494.md")
</div>
<h4 id="waitforapproval-step-options">waitForApproval(step, options?)</h4>
<p>Wait for an approval event. Throws <code>WorkflowRejectedError</code> if rejected.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2495.md")
</div>
<h3 id="step-methods-durable">Step methods (durable)</h3>
<p>These methods are idempotent and will not repeat on retry. Use for state changes that must persist.</p>
<table>
<thead>
<tr>
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>step.reportComplete(result?)</code></td>
<td>Report successful completion</td>
</tr>
<tr>
<td><code>step.reportError(error)</code></td>
<td>Report an error</td>
</tr>
<tr>
<td><code>step.sendEvent(event)</code></td>
<td>Send a custom event to the Agent</td>
</tr>
<tr>
<td><code>step.updateAgentState(state)</code></td>
<td>Replace Agent state (broadcasts to clients)</td>
</tr>
<tr>
<td><code>step.mergeAgentState(partial)</code></td>
<td>Merge into Agent state (broadcasts to clients)</td>
</tr>
<tr>
<td><code>step.resetAgentState()</code></td>
<td>Reset Agent state to initialState</td>
</tr>
</tbody>
</table>
<h3 id="defaultprogress-type">DefaultProgress type</h3>
<pre><code class="language-ts">type DefaultProgress = {&#10;	step?: string;&#10;	status?: &quot;pending&quot; | &quot;running&quot; | &quot;complete&quot; | &quot;error&quot;;&#10;	message?: string;&#10;	percent?: number;&#10;	[key: string]: unknown;&#10;};&#10;</code></pre>
<h2 id="agent-workflow-methods">Agent workflow methods</h2>
<p>Methods available on the <code>Agent</code> class for Workflow management.</p>
<h3 id="runworkflow-workflowname-params-options">runWorkflow(workflowName, params, options?)</h3>
<p>Start a workflow instance and track it in the Agent database.</p>
<p><strong>Parameters:</strong></p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>workflowName</code></td>
<td>string</td>
<td>Workflow binding name from <code>env</code></td>
</tr>
<tr>
<td><code>params</code></td>
<td>object</td>
<td>Parameters to pass to the workflow</td>
</tr>
<tr>
<td><code>options.id</code></td>
<td>string</td>
<td>Custom workflow ID (auto-generated if not provided)</td>
</tr>
<tr>
<td><code>options.metadata</code></td>
<td>object</td>
<td>Metadata stored for querying (not passed to workflow)</td>
</tr>
<tr>
<td><code>options.agentBinding</code></td>
<td>string</td>
<td>Agent binding name (auto-detected if not provided). When called from a sub-agent, this is the root Agent binding name</td>
</tr>
</tbody>
</table>
<p><strong>Returns:</strong> <code>Promise&lt;string&gt;</code> - Workflow instance ID</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2496.md")
</div>
<h4 id="starting-workflows-from-sub-agents">Starting workflows from sub-agents</h4>
<p>Sub-agents can call <code>this.runWorkflow()</code> directly. The workflow is tracked in the originating sub-agent's SQLite database, and <code>this.agent</code> inside <code>AgentWorkflow</code> routes back to that same sub-agent for RPC calls, callbacks, state updates, and broadcasts.</p>
<p>Parent agents do not automatically list or control workflows that a sub-agent starts. <code>SubAgentStub&lt;T&gt;</code> only exposes user-defined methods, not inherited <code>Agent</code> methods such as <code>approveWorkflow()</code> or <code>getWorkflow()</code>. To control a child-started workflow from the parent, define small wrapper methods on the child and call those wrappers through the sub-agent stub.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2497.md")
</div>
<p>For sub-agent origins, <code>AgentWorkflow.agent</code> is an RPC-only stub. Use it to call Agent methods, but use <code>routeSubAgentRequest()</code> or the <code>/agents/{parent}/{name}/sub/{child}/{name}</code> URL shape for external HTTP or WebSocket routing instead of <code>this.agent.fetch()</code>.</p>
<h4 id="routing-constraints">Routing constraints</h4>
<p>Because the originating identity is persisted durably in the workflow params and replayed on every callback, a few constraints apply to all workflows (sub-agent and top-level alike):</p>
<ul>
<li><strong>Callbacks resolve the Agent by name.</strong> The runtime re-resolves the originating Agent with <code>getAgentByName(...)</code>. If you addressed the Agent by a raw Durable Object ID (<code>idFromString</code> / <code>get(id)</code>) instead of by name, callbacks land on a different instance. Start workflows from name-addressed Agents.</li>
<li><strong>Class names must survive bundling.</strong> The originating path is keyed by <code>constructor.name</code>. Configure your bundler to preserve class names (esbuild <code>keepNames: true</code>) so progress, completion, and <code>this.agent</code> RPC can be routed back to the right facet.</li>
<li><strong><code>agentBinding</code> is the root binding.</strong> When you pass <code>options.agentBinding</code> from a sub-agent, use the <strong>root</strong> Agent's Durable Object binding name, not a child binding.</li>
</ul>
<h3 id="sendworkflowevent-workflowname-instanceid-event">sendWorkflowEvent(workflowName, instanceId, event)</h3>
<p>Send an event to a running workflow.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2498.md")
</div>
<h3 id="getworkflowstatus-workflowname-instanceid">getWorkflowStatus(workflowName, instanceId)</h3>
<p>Get the status of a workflow and update the tracking record.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2499.md")
</div>
<h3 id="getworkflow-instanceid">getWorkflow(instanceId)</h3>
<p>Get a tracked workflow by ID.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2500.md")
</div>
<h3 id="getworkflows-criteria">getWorkflows(criteria?)</h3>
<p>Query tracked workflows with cursor-based pagination. Returns a <code>WorkflowPage</code> with workflows, total count, and cursor for the next page.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2501.md")
</div>
<p>The <code>WorkflowPage</code> type:</p>
<pre><code class="language-ts">type WorkflowPage = {&#10;	workflows: WorkflowInfo[];&#10;	total: number; // Total matching workflows&#10;	nextCursor: string | null; // null when no more pages&#10;};&#10;</code></pre>
<h3 id="deleteworkflow-instanceid">deleteWorkflow(instanceId)</h3>
<p>Delete a single workflow instance tracking record. Returns <code>true</code> if deleted, <code>false</code> if not found.</p>
<h3 id="deleteworkflows-criteria">deleteWorkflows(criteria?)</h3>
<p>Delete workflow instance tracking records matching criteria.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2502.md")
</div>
<h3 id="terminateworkflow-instanceid">terminateWorkflow(instanceId)</h3>
<p>Terminate a running workflow immediately. Sets status to <code>&quot;terminated&quot;</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2503.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2488.md")
</aside>
<h3 id="pauseworkflow-instanceid">pauseWorkflow(instanceId)</h3>
<p>Pause a running workflow. The workflow can be resumed later with <code>resumeWorkflow()</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2504.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2487.md")
</aside>
<h3 id="resumeworkflow-instanceid">resumeWorkflow(instanceId)</h3>
<p>Resume a paused workflow.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2505.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2486.md")
</aside>
<h3 id="restartworkflow-instanceid-options">restartWorkflow(instanceId, options?)</h3>
<p>Restart a workflow instance from the beginning with the same ID.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2506.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2485.md")
</aside>
<h3 id="approveworkflow-instanceid-options">approveWorkflow(instanceId, options?)</h3>
<p>Approve a waiting workflow. Use with <code>waitForApproval()</code> in the workflow.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2507.md")
</div>
<h3 id="rejectworkflow-instanceid-options">rejectWorkflow(instanceId, options?)</h3>
<p>Reject a waiting workflow. Causes <code>waitForApproval()</code> to throw <code>WorkflowRejectedError</code>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2508.md")
</div>
<h3 id="migrateworkflowbinding-oldname-newname">migrateWorkflowBinding(oldName, newName)</h3>
<p>Migrate tracked workflows after renaming a workflow binding.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2509.md")
</div>
<h2 id="lifecycle-callbacks">Lifecycle callbacks</h2>
<p>Override these methods in your Agent to handle workflow events:</p>
<table>
<thead>
<tr>
<th>Callback</th>
<th>Parameters</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>onWorkflowProgress</code></td>
<td><code>workflowName</code>, <code>instanceId</code>, <code>progress</code></td>
<td>Called when workflow reports progress</td>
</tr>
<tr>
<td><code>onWorkflowComplete</code></td>
<td><code>workflowName</code>, <code>instanceId</code>, <code>result?</code></td>
<td>Called when workflow completes</td>
</tr>
<tr>
<td><code>onWorkflowError</code></td>
<td><code>workflowName</code>, <code>instanceId</code>, <code>error</code></td>
<td>Called when workflow errors</td>
</tr>
<tr>
<td><code>onWorkflowEvent</code></td>
<td><code>workflowName</code>, <code>instanceId</code>, <code>event</code></td>
<td>Called when workflow sends an event</td>
</tr>
<tr>
<td><code>onWorkflowCallback</code></td>
<td><code>callback: WorkflowCallback</code></td>
<td>Called for all callback types</td>
</tr>
</tbody>
</table>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2510.md")
</div>
<h2 id="workflow-tracking">Workflow tracking</h2>
<p>Workflows started with <code>runWorkflow()</code> are automatically tracked in the originating Agent's internal database. You can query, filter, and manage workflows using the methods described above (<code>getWorkflow()</code>, <code>getWorkflows()</code>, <code>deleteWorkflow()</code>, etc.).</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="sub-agent-scoping">Sub-agent scoping</h3>
@markup("md", "content/.markup/bodies/2484.md")
</aside>
<h3 id="status-values">Status values</h3>
<table>
<thead>
<tr>
<th>Status</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>queued</code></td>
<td>Waiting to start</td>
</tr>
<tr>
<td><code>running</code></td>
<td>Currently executing</td>
</tr>
<tr>
<td><code>paused</code></td>
<td>Paused by user</td>
</tr>
<tr>
<td><code>waiting</code></td>
<td>Waiting for event</td>
</tr>
<tr>
<td><code>complete</code></td>
<td>Finished successfully</td>
</tr>
<tr>
<td><code>errored</code></td>
<td>Failed with error</td>
</tr>
<tr>
<td><code>terminated</code></td>
<td>Manually terminated</td>
</tr>
</tbody>
</table>
<p>Use the <code>metadata</code> option in <code>runWorkflow()</code> to store queryable information (like user IDs or task types) that you can filter on later with <code>getWorkflows()</code>.</p>
<h2 id="examples">Examples</h2>
<h3 id="human-in-the-loop-approval">Human-in-the-loop approval</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2511.md")
</div>
<h3 id="retry-with-backoff">Retry with backoff</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2512.md")
</div>
<h3 id="state-synchronization">State synchronization</h3>
<p>Workflows can update Agent state durably via <code>step</code>, which automatically broadcasts to all connected clients:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2513.md")
</div>
<h3 id="custom-progress-types">Custom progress types</h3>
<p>Define custom progress types for domain-specific reporting:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2514.md")
</div>
<h3 id="cleanup-strategy">Cleanup strategy</h3>
<p>The internal <code>cf_agents_workflows</code> table can grow unbounded, so implement a retention policy:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2515.md")
</div>
<h2 id="bidirectional-communication">Bidirectional communication</h2>
<h3 id="workflow-to-agent">Workflow to Agent</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2516.md")
</div>
<h3 id="agent-to-workflow">Agent to Workflow</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2517.md")
</div>
<h2 id="best-practices">Best practices</h2>
<ol>
<li><strong>Keep workflows focused</strong> — One workflow per logical task</li>
<li><strong>Use meaningful step names</strong> — Helps with debugging and observability</li>
<li><strong>Report progress regularly</strong> — Keeps users informed</li>
<li><strong>Handle errors gracefully</strong> — Use <code>reportError()</code> before throwing</li>
<li><strong>Clean up completed workflows</strong> — Implement a retention policy for the tracking table</li>
<li><strong>Handle workflow binding renames</strong> — Use <code>migrateWorkflowBinding()</code> when renaming workflow bindings in <code>wrangler.jsonc</code></li>
</ol>
<h2 id="limitations">Limitations</h2>
<table>
<thead>
<tr>
<th>Constraint</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Maximum steps</td>
<td>10,000 per workflow (default) / configurable up to 25,000</td>
</tr>
<tr>
<td>State size</td>
<td>10 MB per workflow</td>
</tr>
<tr>
<td>Event wait time</td>
<td>1 year maximum</td>
</tr>
<tr>
<td>Step execution time</td>
<td>30 minutes per step</td>
</tr>
</tbody>
</table>
<p>Workflows cannot open WebSocket connections directly. Use <code>broadcastToClients()</code> to communicate with connected clients through the Agent.</p>
<h2 id="related-resources">Related resources</h2>
<p><a class="nb-card nb-link-card" href="/workflows/"><h3 id="card-workflows-documentation-workflows">Workflows documentation</h3><p>Learn about Cloudflare Workflows fundamentals.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/lifecycle/state/"><h3 id="card-store-and-sync-state-agents-runtime-lifecycle-state">Store and sync state</h3><p>Persist and synchronize agent state.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/execution/schedule-tasks/"><h3 id="card-schedule-tasks-agents-runtime-execution-schedule-tasks">Schedule tasks</h3><p>Time-based task execution.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/concepts/agentic-patterns/human-in-the-loop/"><h3 id="card-human-in-the-loop-agents-concepts-agentic-patterns-human-in-the-loop">Human-in-the-loop</h3><p>Approval flows and manual intervention patterns.</p></a></p>
