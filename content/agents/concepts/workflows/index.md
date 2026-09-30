<h2 id="what-are-workflows">What are Workflows?</h2>
<p><a href="/workflows/">Cloudflare Workflows</a> provide durable, multi-step execution for tasks that need to survive failures, retry automatically, and wait for external events. When integrated with Agents, Workflows handle long-running background processing while Agents manage real-time communication.</p>
<h3 id="agents-vs-workflows">Agents vs. Workflows</h3>
<p>Agents and Workflows have complementary strengths:</p>
<table>
<thead>
<tr>
<th>Capability</th>
<th>Agents</th>
<th>Workflows</th>
</tr>
</thead>
<tbody>
<tr>
<td>Execution model</td>
<td>Long-lived identity that wakes on events</td>
<td>Run to completion</td>
</tr>
<tr>
<td>Real-time communication</td>
<td>WebSockets, HTTP streaming</td>
<td>Not supported</td>
</tr>
<tr>
<td>State persistence</td>
<td>Built-in SQL database</td>
<td>Step-level persistence</td>
</tr>
<tr>
<td>Failure handling</td>
<td>Application-defined</td>
<td>Automatic retries and recovery</td>
</tr>
<tr>
<td>External events</td>
<td>Direct handling</td>
<td>Pause and wait for events</td>
</tr>
<tr>
<td>User interaction</td>
<td>Direct (chat, UI)</td>
<td>Through Agent callbacks</td>
</tr>
</tbody>
</table>
<p>Agents can loop, branch, and interact directly with users. Workflows execute steps sequentially with guaranteed delivery and can pause for days waiting for approvals or external data.</p>
<h3 id="when-to-use-each">When to use each</h3>
<p><strong>Use Agents alone for:</strong></p>
<ul>
<li>Chat and messaging applications</li>
<li>Quick API calls and responses</li>
<li>Real-time collaborative features</li>
<li>Tasks under 30 seconds</li>
<li>One durable Think chat turn with <a href="/agents/harnesses/think/programmatic-submissions/#submitmessages"><code>submitMessages()</code></a></li>
</ul>
<p><strong>Use Agents with Workflows for:</strong></p>
<ul>
<li>Data processing pipelines</li>
<li>Report generation</li>
<li>Human-in-the-loop approval flows</li>
<li>Tasks requiring guaranteed delivery</li>
<li>Multi-step operations with retry requirements</li>
</ul>
<p><strong>Use Workflows alone for:</strong></p>
<ul>
<li>Background jobs with or without user approval</li>
<li>Scheduled data synchronization</li>
<li>Event-driven processing pipelines</li>
</ul>
<h2 id="how-agents-and-workflows-communicate">How Agents and Workflows communicate</h2>
<p>The <code>AgentWorkflow</code> class (imported from <code>agents/workflows</code>) provides bidirectional communication between Workflows and their originating Agent.</p>
<h3 id="workflow-to-agent">Workflow to Agent</h3>
<p>Workflows can communicate with Agents through several mechanisms:</p>
<ul>
<li><strong>RPC calls</strong>: Directly call Agent methods with full type safety via <code>this.agent</code></li>
<li><strong>Progress reporting</strong>: Send progress updates via <code>this.reportProgress()</code> that trigger Agent callbacks</li>
<li><strong>State updates</strong>: Modify Agent state via <code>step.updateAgentState()</code> or <code>step.mergeAgentState()</code>, which broadcasts to connected clients</li>
<li><strong>Client broadcasts</strong>: Send messages to all WebSocket clients via <code>this.broadcastToClients()</code></li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1938.md")
</div>
<h3 id="agent-to-workflow">Agent to Workflow</h3>
<p>Agents can interact with running Workflows by:</p>
<ul>
<li><strong>Starting workflows</strong>: Launch new workflow instances with <code>runWorkflow()</code></li>
<li><strong>Sending events</strong>: Dispatch events with <code>sendWorkflowEvent()</code></li>
<li><strong>Approval/rejection</strong>: Respond to approval requests with <code>approveWorkflow()</code> / <code>rejectWorkflow()</code></li>
<li><strong>Workflow control</strong>: Pause, resume, terminate, or restart workflows</li>
<li><strong>Status queries</strong>: Check workflow progress with <code>getWorkflow()</code> / <code>getWorkflows()</code></li>
</ul>
<h2 id="durable-vs-non-durable-operations">Durable vs. non-durable operations</h2>
<p>Understanding durability is key to using workflows effectively:</p>
<h3 id="non-durable-may-repeat-on-retry">Non-durable (may repeat on retry)</h3>
<p>These operations are lightweight and suitable for frequent updates, but may execute multiple times if the workflow retries:</p>
<ul>
<li><code>this.reportProgress()</code> — Progress reporting</li>
<li><code>this.broadcastToClients()</code> — WebSocket broadcasts</li>
<li>Direct RPC calls to <code>this.agent</code></li>
</ul>
<h3 id="durable-idempotent-won-t-repeat">Durable (idempotent, won't repeat)</h3>
<p>These operations use the <code>step</code> parameter and are guaranteed to execute exactly once:</p>
<ul>
<li><code>step.do()</code> — Execute durable steps</li>
<li><code>step.reportComplete()</code> / <code>step.reportError()</code> — Completion reporting</li>
<li><code>step.sendEvent()</code> — Custom events</li>
<li><code>step.updateAgentState()</code> / <code>step.mergeAgentState()</code> — State synchronization</li>
</ul>
<h2 id="durability-guarantees">Durability guarantees</h2>
<p>Workflows provide durability through step-based execution:</p>
<ol>
<li><strong>Step completion is permanent</strong> — Once a step completes, it will not re-execute even if the workflow restarts</li>
<li><strong>Automatic retries</strong> — Failed steps retry with configurable backoff</li>
<li><strong>Event persistence</strong> — Workflows can wait for events for up to one year</li>
<li><strong>State recovery</strong> — Workflow state survives infrastructure failures</li>
</ol>
<p>This durability model means workflows are well-suited for tasks where partial completion must be preserved, such as multi-stage data processing or transactions spanning multiple systems.</p>
<h2 id="workflow-tracking">Workflow tracking</h2>
<p>When an Agent starts a workflow using <code>runWorkflow()</code>, the workflow is automatically tracked in the Agent's internal database. This enables:</p>
<ul>
<li>Querying workflow status by ID, name, or metadata with cursor-based pagination</li>
<li>Monitoring progress through lifecycle callbacks (<code>onWorkflowProgress</code>, <code>onWorkflowComplete</code>, <code>onWorkflowError</code>)</li>
<li>Workflow control: pause, resume, terminate, restart</li>
<li>Cleaning up completed workflow records with <code>deleteWorkflow()</code> / <code>deleteWorkflows()</code></li>
<li>Correlating workflows with users or sessions through metadata</li>
</ul>
<h2 id="common-patterns">Common patterns</h2>
<h3 id="background-processing-with-progress">Background processing with progress</h3>
<p>An Agent receives a request, starts a Workflow for heavy processing, and broadcasts progress updates to connected clients as the Workflow executes each step.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1939.md")
</div>
<h3 id="human-in-the-loop-approval">Human-in-the-loop approval</h3>
<p>A Workflow prepares a request, pauses to wait for approval using <code>waitForApproval()</code>, and the Agent provides UI for users to approve or reject via <code>approveWorkflow()</code> / <code>rejectWorkflow()</code>. The Workflow resumes or throws <code>WorkflowRejectedError</code> based on the decision.</p>
<h3 id="resilient-external-api-calls">Resilient external API calls</h3>
<p>A Workflow wraps external API calls in durable steps with retry logic. If the API fails or the workflow restarts, completed calls are not repeated and failed calls retry automatically.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/1940.md")
</div>
<h3 id="state-synchronization">State synchronization</h3>
<p>A Workflow updates Agent state at key milestones using <code>step.updateAgentState()</code> or <code>step.mergeAgentState()</code>. These state changes broadcast to all connected clients, keeping UIs synchronized without polling.</p>
<h2 id="related-resources">Related resources</h2>
<p><a class="nb-card nb-link-card" href="/agents/runtime/execution/run-workflows/"><h3 id="card-run-workflows-api-agents-runtime-execution-run-workflows">Run Workflows API</h3><p>Implementation details for agent workflows.</p></a></p>
<p><a class="nb-card nb-link-card" href="/workflows/"><h3 id="card-cloudflare-workflows-workflows">Cloudflare Workflows</h3><p>Workflow fundamentals and documentation.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/concepts/agentic-patterns/human-in-the-loop/"><h3 id="card-human-in-the-loop-agents-concepts-agentic-patterns-human-in-the-loop">Human-in-the-loop</h3><p>Approval flows and manual intervention.</p></a></p>
