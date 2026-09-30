<p>Human-in-the-loop (HITL) patterns add approval or input at different layers of an Agent. You can respond to an MCP server request, hold application work in a durable Workflow, or approve a connector call before model-generated code invokes a tool.</p>
<h2 id="why-human-in-the-loop">Why human-in-the-loop?</h2>
<ul>
<li><strong>Compliance</strong>: Regulatory requirements may mandate human approval for certain actions</li>
<li><strong>Safety</strong>: High-stakes operations (payments, deletions, external communications) need oversight</li>
<li><strong>Quality</strong>: Human review catches errors AI might miss</li>
<li><strong>Trust</strong>: Users feel more confident when they can approve critical actions</li>
</ul>
<h3 id="common-use-cases">Common use cases</h3>
<p>Common uses include financial approvals, content moderation, bulk data operations, approval before side-effecting tool calls, and access-control changes.</p>
<h2 id="choosing-a-pattern">Choosing a pattern</h2>
<p>Choose the pattern based on who introduces the pause and where it occurs:</p>
<table>
<thead>
<tr>
<th>Pattern</th>
<th>Approval layer</th>
<th>Initiated by</th>
<th>Typical wait</th>
<th>Key API</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>MCP elicitation</strong></td>
<td>MCP request handled by your Agent client</td>
<td>MCP server developer</td>
<td>Minutes</td>
<td><code>configureElicitationHandlers()</code></td>
</tr>
<tr>
<td><strong>Workflow approval</strong></td>
<td>Durable application task or tool operation</td>
<td>Agent application developer</td>
<td>Months or years</td>
<td><code>waitForApproval()</code></td>
</tr>
<tr>
<td><strong>Code Mode approval</strong></td>
<td>Connector call in model-generated code</td>
<td>Code Mode Agent developer</td>
<td>Until configured expiry</td>
<td><code>requiresApproval</code>, <code>approve()</code>, <code>reject()</code></td>
</tr>
</tbody>
</table>
<h2 id="workflow-based-approval">Workflow-based approval</h2>
<p>Use <a href="/workflows/">Cloudflare Workflows</a> when your application needs to hold a task or tool operation for as long as approval requires. <code>waitForApproval()</code> creates a durable gate backed by Cloudflare Workflows, so the wait can continue for months or longer without keeping an Agent running.</p>
<h3 id="basic-pattern">Basic pattern</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2087.md")
</div>
<h3 id="agent-methods-for-approval">Agent methods for approval</h3>
<p>The agent provides methods to approve or reject waiting workflows:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2088.md")
</div>
<h3 id="timeout-handling">Timeout handling</h3>
<p>Set timeouts to prevent workflows from waiting indefinitely:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2089.md")
</div>
<h3 id="escalation-with-scheduling">Escalation with scheduling</h3>
<p>Use <code>schedule()</code> to set up escalation reminders:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2090.md")
</div>
<h3 id="audit-trail-with-sql">Audit trail with SQL</h3>
<p>Use <code>this.sql</code> to maintain an immutable audit trail:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2091.md")
</div>
<h3 id="configuration">Configuration</h3>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2092.md")
</div>
<h2 id="mcp-elicitation">MCP elicitation</h2>
<p>MCP elicitation lets an MCP server developer decide that a tool call needs more information or an out-of-band interaction. Your Agent acts as the MCP client: it presents the request to the user and returns their response. These interactions typically complete within minutes.</p>
<p>Form mode collects structured, non-sensitive input. URL mode asks the user to open an out-of-band flow, such as third-party authorization or payment.</p>
<p>Configure the user-facing handlers in <code>onStart()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2093.md")
</div>
<p>For the complete form, URL, and browser forwarding patterns, refer to <a href="/agents/model-context-protocol/apis/client-api/#elicitation">MCP client elicitation</a>. For the server-side request API, refer to <a href="/agents/model-context-protocol/apis/agent-api/#elicitation">McpAgent elicitation</a>.</p>
<h2 id="durable-code-mode-approvals">Durable Code Mode approvals</h2>
<p>Use the <a href="/agents/tools/codemode/durable-runtime/">durable Code Mode runtime</a> for coding agents and other Agents that use the Code Mode pattern. Mark a connector method with <code>requiresApproval: true</code> to pause model-generated code before it invokes the underlying tool.</p>
<p>The following example marks a GitHub MCP tool as approval-gated, adds the connector to a durable runtime, and exposes methods that a UI can use to inspect, approve, or reject the pending action:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2094.md")
</div>
<p>When generated code calls <code>github.create_issue()</code>, the runtime records the pending method and arguments, then pauses before the MCP tool executes. Approval starts another pass with the same source code and execution ID. Previously completed calls replay from the durable log, the approved call executes, and the generated code continues.</p>
<p>Pending approvals and execution history survive request completion and Durable Object hibernation. For the execution and replay model, refer to <a href="/agents/tools/codemode/how-it-works/#approvals-through-abort-and-replay">Approvals through abort and replay</a>.</p>
<h2 id="build-workflow-approval-uis">Build Workflow approval UIs</h2>
<h3 id="pending-approvals-list">Pending approvals list</h3>
<p>Use the agent's state to display pending approvals in your UI:</p>
<pre><code class="language-tsx">import { useAgent } from &quot;agents/react&quot;;&#10;&#10;function PendingApprovals() {&#10;	const { state, agent } = useAgent({&#10;		agent: &quot;expense-agent&quot;,&#10;		name: &quot;main&quot;,&#10;	});&#10;&#10;	if (!state?.pendingApprovals?.length) {&#10;		return &lt;p&gt;No pending approvals&lt;/p&gt;;&#10;	}&#10;&#10;	return (&#10;		&lt;div className=&quot;approval-list&quot;&gt;&#10;			{state.pendingApprovals.map((item) =&gt; (&#10;				&lt;div key={item.workflowId} className=&quot;approval-card&quot;&gt;&#10;					&lt;h3&gt;${item.amount}&lt;/h3&gt;&#10;					&lt;p&gt;{item.description}&lt;/p&gt;&#10;					&lt;p&gt;Requested by {item.requestedBy}&lt;/p&gt;&#10;&#10;					&lt;div className=&quot;actions&quot;&gt;&#10;						&lt;button&#10;							onClick={() =&gt; agent.stub.approve(item.workflowId, &quot;admin&quot;)}&#10;						&gt;&#10;							Approve&#10;						&lt;/button&gt;&#10;						&lt;button&#10;							onClick={() =&gt; agent.stub.reject(item.workflowId, &quot;Declined&quot;)}&#10;						&gt;&#10;							Reject&#10;						&lt;/button&gt;&#10;					&lt;/div&gt;&#10;				&lt;/div&gt;&#10;			))}&#10;		&lt;/div&gt;&#10;	);&#10;}&#10;</code></pre>
<h2 id="add-multiple-workflow-approvers">Add multiple Workflow approvers</h2>
<p>For sensitive operations requiring multiple approvers:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2095.md")
</div>
<h2 id="best-practices">Best practices</h2>
<ol>
<li><strong>Define clear approval criteria</strong> — Only require confirmation for actions with meaningful consequences (payments, emails, data changes)</li>
<li><strong>Provide detailed context</strong> — Show users exactly what the action will do, including all arguments</li>
<li><strong>Implement timeouts</strong> — Use <code>schedule()</code> to escalate or auto-reject after reasonable periods</li>
<li><strong>Maintain audit trails</strong> — Use <code>this.sql</code> to record all approval decisions for compliance</li>
<li><strong>Handle connection drops</strong> — Store pending approvals in agent state so they survive disconnections</li>
<li><strong>Graceful degradation</strong> — Provide fallback behavior if approvals are rejected</li>
</ol>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/agents/runtime/execution/run-workflows/"><h3 id="card-run-workflows-agents-runtime-execution-run-workflows">Run Workflows</h3><p>Complete waitForApproval() API reference.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/model-context-protocol/apis/client-api/"><h3 id="card-mcp-clients-agents-model-context-protocol-apis-client-api">MCP clients</h3><p>Handle elicitation requests in an Agent acting as an MCP client.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/model-context-protocol/apis/agent-api/"><h3 id="card-mcp-servers-agents-model-context-protocol-apis-agent-api">MCP servers</h3><p>Request form or URL elicitation from an MCP server.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/tools/codemode/durable-runtime/"><h3 id="card-durable-code-mode-runtime-agents-tools-codemode-durable-runtime">Durable Code Mode runtime</h3><p>Pause model-generated code for approval before connector calls.</p></a></p>
