<p>Agents publish structured events to <a href="/workers/runtime-apis/nodejs/diagnostics-channel/">diagnostics channels</a> for every significant operation -- RPC calls, state changes, schedule execution, workflow transitions, MCP connections, and more. Publishing has zero overhead when nobody is listening.</p>
<h2 id="event-structure">Event structure</h2>
<p>Every event has these fields:</p>
<pre><code class="language-ts">{&#10;  type: &quot;rpc&quot;,                        // what happened&#10;  agent: &quot;MyAgent&quot;,                   // which agent class emitted it&#10;  name: &quot;user-123&quot;,                   // which agent instance (Durable Object name)&#10;  payload: { method: &quot;getWeather&quot; },  // details&#10;  timestamp: 1758005142787            // when (ms since epoch)&#10;}&#10;</code></pre>
<p><code>agent</code> and <code>name</code> identify the source agent — <code>agent</code> is the class name and <code>name</code> is the Durable Object instance name.</p>
<h2 id="channels">Channels</h2>
<p>Events are routed to named channels based on their type:</p>
<table>
<thead>
<tr>
<th>Channel</th>
<th>Event types</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>agents:state</code></td>
<td><code>state:update</code></td>
<td>State sync events</td>
</tr>
<tr>
<td><code>agents:rpc</code></td>
<td><code>rpc</code>, <code>rpc:error</code></td>
<td>RPC method calls and failures</td>
</tr>
<tr>
<td><code>agents:message</code></td>
<td><code>message:request</code>, <code>message:response</code>, <code>message:clear</code>, <code>message:cancel</code>, <code>message:error</code>, <code>tool:result</code>, <code>tool:approval</code>, <code>submission:create</code>, <code>submission:status</code>, <code>submission:error</code></td>
<td>Chat message, tool, and Think submission lifecycle</td>
</tr>
<tr>
<td><code>agents:chat</code></td>
<td><code>chat:request:failed</code>, <code>chat:recovery:*</code>, <code>chat:stream:stalled</code>, <code>chat:context:compacted</code></td>
<td>Chat request, recovery, stream-stall, and context-compaction lifecycle</td>
</tr>
<tr>
<td><code>agents:transcript</code></td>
<td><code>chat:transcript:repaired</code></td>
<td>Transcript repair events</td>
</tr>
<tr>
<td><code>agents:fiber</code></td>
<td><code>fiber:run:*</code>, <code>fiber:recovery:*</code></td>
<td>Durable fiber lifecycle</td>
</tr>
<tr>
<td><code>agents:agent_tool</code></td>
<td><code>agent_tool:recovery:*</code></td>
<td>Parent/child agent-tool recovery</td>
</tr>
<tr>
<td><code>agents:schedule</code></td>
<td><code>schedule:create</code>, <code>schedule:execute</code>, <code>schedule:cancel</code>, <code>schedule:retry</code>, <code>schedule:error</code>, <code>schedule:duplicate_warning</code>, <code>queue:create</code>, <code>queue:retry</code>, <code>queue:error</code></td>
<td>Scheduled and queued task lifecycle</td>
</tr>
<tr>
<td><code>agents:lifecycle</code></td>
<td><code>connect</code>, <code>disconnect</code>, <code>destroy</code></td>
<td>Agent connection and teardown</td>
</tr>
<tr>
<td><code>agents:workflow</code></td>
<td><code>workflow:start</code>, <code>workflow:event</code>, <code>workflow:approved</code>, <code>workflow:rejected</code>, <code>workflow:terminated</code>, <code>workflow:paused</code>, <code>workflow:resumed</code>, <code>workflow:restarted</code></td>
<td>Workflow state transitions</td>
</tr>
<tr>
<td><code>agents:mcp</code></td>
<td><code>mcp:client:preconnect</code>, <code>mcp:client:connect</code>, <code>mcp:client:authorize</code>, <code>mcp:client:discover</code></td>
<td>MCP client operations</td>
</tr>
<tr>
<td><code>agents:email</code></td>
<td><code>email:receive</code>, <code>email:reply</code>, <code>email:send</code></td>
<td>Email processing</td>
</tr>
</tbody>
</table>
<h2 id="subscribing-to-events">Subscribing to events</h2>
<h3 id="typed-subscribe-helper">Typed subscribe helper</h3>
<p>The <code>subscribe()</code> function from <code>agents/observability</code> provides type-safe access to events on a specific channel:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2652.md")
</div>
<p>The callback is fully typed — <code>event</code> is narrowed to only the event types that flow through that channel.</p>
<p>The typed helper uses camelCase keys, so agent-tool recovery is <code>subscribe(&quot;agentTool&quot;, ...)</code>. Raw diagnostics channel subscribers should use the emitted channel name, <code>agents:agent_tool</code>.</p>
<h3 id="raw-diagnostics-channel">Raw diagnostics_channel</h3>
<p>You can also subscribe directly using the Node.js API:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2653.md")
</div>
<h2 id="tail-workers-production">Tail Workers (production)</h2>
<p>In production, all diagnostics channel messages are automatically forwarded to <a href="/workers/observability/logs/tail-workers/">Tail Workers</a>. No subscription code is needed in the agent itself — attach a Tail Worker and access events via <code>event.diagnosticsChannelEvents</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2654.md")
</div>
<p>This gives you structured, filterable observability in production with zero overhead in the agent hot path.</p>
<h2 id="custom-observability">Custom observability</h2>
<p>You can override the default implementation by providing your own <code>Observability</code> interface:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2655.md")
</div>
<p>Set <code>observability</code> to <code>undefined</code> to disable all event emission:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2656.md")
</div>
<h2 id="event-reference">Event reference</h2>
<h3 id="rpc-events">RPC events</h3>
<table>
<thead>
<tr>
<th>Type</th>
<th>Payload</th>
<th>When</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>rpc</code></td>
<td><code>{ method, streaming? }</code></td>
<td>A <code>@callable</code> method is invoked</td>
</tr>
<tr>
<td><code>rpc:error</code></td>
<td><code>{ method, error }</code></td>
<td>A <code>@callable</code> method throws</td>
</tr>
</tbody>
</table>
<h3 id="state-events">State events</h3>
<table>
<thead>
<tr>
<th>Type</th>
<th>Payload</th>
<th>When</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>state:update</code></td>
<td><code>{}</code></td>
<td><code>setState()</code> is called</td>
</tr>
</tbody>
</table>
<h3 id="message-tool-and-submission-events">Message, tool, and submission events</h3>
<p>These events track chat message lifecycle, client-side tool interactions, and Think durable submissions.</p>
<table>
<thead>
<tr>
<th>Type</th>
<th>Payload</th>
<th>When</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>message:request</code></td>
<td><code>{}</code></td>
<td>A chat message is received</td>
</tr>
<tr>
<td><code>message:response</code></td>
<td><code>{}</code></td>
<td>A chat response stream completes</td>
</tr>
<tr>
<td><code>message:clear</code></td>
<td><code>{}</code></td>
<td>Chat history is cleared</td>
</tr>
<tr>
<td><code>message:cancel</code></td>
<td><code>{ requestId }</code></td>
<td>A streaming request is cancelled</td>
</tr>
<tr>
<td><code>message:error</code></td>
<td><code>{ error }</code></td>
<td>A chat stream fails</td>
</tr>
<tr>
<td><code>tool:result</code></td>
<td><code>{ toolCallId, toolName }</code></td>
<td>A client tool result is received</td>
</tr>
<tr>
<td><code>tool:approval</code></td>
<td><code>{ toolCallId, approved }</code></td>
<td>A tool call is approved or rejected</td>
</tr>
<tr>
<td><code>submission:create</code></td>
<td><code>{ submissionId }</code></td>
<td>A Think submission is accepted</td>
</tr>
<tr>
<td><code>submission:status</code></td>
<td><code>{ submissionId, status }</code></td>
<td>A Think submission status changes</td>
</tr>
<tr>
<td><code>submission:error</code></td>
<td><code>{ submissionId, error }</code></td>
<td>A Think submission fails</td>
</tr>
</tbody>
</table>
<h3 id="chat-recovery-events">Chat recovery events</h3>
<table>
<thead>
<tr>
<th>Type</th>
<th>Payload</th>
<th>When</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>chat:request:failed</code></td>
<td><code>{ requestId?, stage, messagesPersisted?, error }</code></td>
<td>A Think chat request fails while parsing, persisting, running, or streaming</td>
</tr>
<tr>
<td><code>chat:recovery:detected</code></td>
<td><code>{ incidentId, requestId, attempt, maxAttempts, recoveryKind }</code></td>
<td>An interrupted chat fiber is first observed</td>
</tr>
<tr>
<td><code>chat:recovery:attempt</code></td>
<td><code>{ incidentId, requestId, attempt, maxAttempts, recoveryKind }</code></td>
<td>The framework begins a recovery attempt</td>
</tr>
<tr>
<td><code>chat:recovery:scheduled</code></td>
<td><code>{ incidentId, requestId, attempt, maxAttempts, recoveryKind }</code></td>
<td>A retry or continuation callback is scheduled</td>
</tr>
<tr>
<td><code>chat:recovery:completed</code></td>
<td><code>{ incidentId, requestId, attempt, maxAttempts, recoveryKind }</code></td>
<td>Recovery completed successfully</td>
</tr>
<tr>
<td><code>chat:recovery:skipped</code></td>
<td><code>{ incidentId, requestId, attempt, maxAttempts, recoveryKind, reason? }</code></td>
<td>Recovery was skipped because the conversation changed or was no longer recoverable</td>
</tr>
<tr>
<td><code>chat:recovery:failed</code></td>
<td><code>{ incidentId, requestId, attempt, maxAttempts, recoveryKind, reason? }</code></td>
<td>Recovery ran but failed</td>
</tr>
<tr>
<td><code>chat:recovery:exhausted</code></td>
<td><code>{ incidentId, requestId, attempt, maxAttempts, recoveryKind, reason }</code></td>
<td>Recovery exceeded its configured attempt budget</td>
</tr>
<tr>
<td><code>chat:stream:stalled</code></td>
<td><code>{ requestId, timeoutMs }</code></td>
<td>The inactivity watchdog fired because no stream chunk arrived within <code>chatStreamStallTimeoutMs</code>. The turn routes into durable recovery</td>
</tr>
</tbody>
</table>
<p><code>recoveryKind</code> is <code>&quot;retry&quot;</code> when recovery replays an unanswered user turn and <code>&quot;continue&quot;</code> when it continues a partial assistant turn.</p>
<h3 id="chat-context-events">Chat context events</h3>
<table>
<thead>
<tr>
<th>Type</th>
<th>Payload</th>
<th>When</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>chat:context:compacted</code></td>
<td><code>{ reason, shortened, requestId?, attempt? }</code></td>
<td>Think compacts the session to handle a context-window overflow. <code>reason</code> is <code>&quot;proactive&quot;</code> (the <code>contextOverflow.proactive</code> guard fired before a step) or <code>&quot;reactive&quot;</code> (<code>contextOverflow.reactive</code> fired after an overflow). <code>shortened</code> is whether compaction actually reduced history — <code>false</code> means a retry would overflow again. Refer to <a href="/agents/harnesses/think/recovery/#context-window-overflow-recovery">Context-window overflow recovery</a>.</td>
</tr>
</tbody>
</table>
<h3 id="transcript-events">Transcript events</h3>
<table>
<thead>
<tr>
<th>Type</th>
<th>Payload</th>
<th>When</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>chat:transcript:repaired</code></td>
<td><code>{ requestId?, removedToolCalls, normalizedInputs, toolCallIds? }</code></td>
<td>Think repairs a persisted transcript before sending it to the provider. <code>removedToolCalls</code> counts orphaned tool calls healed; <code>normalizedInputs</code> counts stringified or missing tool inputs repaired</td>
</tr>
</tbody>
</table>
<h3 id="fiber-events">Fiber events</h3>
<table>
<thead>
<tr>
<th>Type</th>
<th>Payload</th>
<th>When</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>fiber:run:started</code></td>
<td><code>{ fiberId, fiberName, managed? }</code></td>
<td>A durable fiber starts</td>
</tr>
<tr>
<td><code>fiber:run:completed</code></td>
<td><code>{ fiberId, fiberName, managed?, elapsedMs? }</code></td>
<td>A durable fiber completes</td>
</tr>
<tr>
<td><code>fiber:run:failed</code></td>
<td><code>{ fiberId, fiberName, managed?, error, elapsedMs? }</code></td>
<td>A durable fiber throws</td>
</tr>
<tr>
<td><code>fiber:run:interrupted</code></td>
<td><code>{ fiberId, fiberName, managed?, recoveryReason, elapsedMs? }</code></td>
<td>Startup finds an interrupted fiber</td>
</tr>
<tr>
<td><code>fiber:recovery:detected</code></td>
<td><code>{ fiberId, fiberName, managed?, recoveryReason, elapsedMs? }</code></td>
<td>Recovery sees an interrupted fiber</td>
</tr>
<tr>
<td><code>fiber:recovery:attempt</code></td>
<td><code>{ fiberId, fiberName, managed?, recoveryReason }</code></td>
<td>A recovery hook starts</td>
</tr>
<tr>
<td><code>fiber:recovery:handled</code></td>
<td><code>{ fiberId, fiberName, managed?, recoveryReason, status, elapsedMs? }</code></td>
<td>Recovery handling completes</td>
</tr>
<tr>
<td><code>fiber:recovery:skipped</code></td>
<td><code>{ fiberId, fiberName, managed?, reason, elapsedMs? }</code></td>
<td>A recovery scan skips remaining work</td>
</tr>
<tr>
<td><code>fiber:recovery:failed</code></td>
<td><code>{ fiberId, fiberName, managed?, error, reason?, elapsedMs? }</code></td>
<td>A recovery hook fails</td>
</tr>
</tbody>
</table>
<h3 id="agent-tool-recovery-events">Agent-tool recovery events</h3>
<table>
<thead>
<tr>
<th>Type</th>
<th>Payload</th>
<th>When</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>agent_tool:recovery:begin</code></td>
<td><code>{ runCount, totalTimeoutMs? }</code></td>
<td>Parent recovery starts scanning stale agent-tool runs</td>
</tr>
<tr>
<td><code>agent_tool:recovery:row</code></td>
<td><code>{ runId, agentType, status, reason?, elapsedMs? }</code></td>
<td>One stale run is reconciled</td>
</tr>
<tr>
<td><code>agent_tool:recovery:deadline</code></td>
<td><code>{ runId, agentType, elapsedMs? }</code></td>
<td>Total recovery deadline is exhausted before inspecting a row</td>
</tr>
<tr>
<td><code>agent_tool:recovery:complete</code></td>
<td><code>{ runCount, elapsedMs? }</code></td>
<td>Parent recovery finishes scanning rows</td>
</tr>
<tr>
<td><code>agent_tool:recovery:failed</code></td>
<td><code>{ error }</code></td>
<td>Parent recovery fails unexpectedly</td>
</tr>
</tbody>
</table>
<h3 id="schedule-and-queue-events">Schedule and queue events</h3>
<table>
<thead>
<tr>
<th>Type</th>
<th>Payload</th>
<th>When</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>schedule:create</code></td>
<td><code>{ callback, id }</code></td>
<td>A schedule is created</td>
</tr>
<tr>
<td><code>schedule:execute</code></td>
<td><code>{ callback, id }</code></td>
<td>A scheduled callback starts</td>
</tr>
<tr>
<td><code>schedule:cancel</code></td>
<td><code>{ callback, id }</code></td>
<td>A schedule is cancelled</td>
</tr>
<tr>
<td><code>schedule:retry</code></td>
<td><code>{ callback, id, attempt, maxAttempts }</code></td>
<td>A scheduled callback is retried</td>
</tr>
<tr>
<td><code>schedule:error</code></td>
<td><code>{ callback, id, error, attempts }</code></td>
<td>A scheduled callback fails after all retries</td>
</tr>
<tr>
<td><code>schedule:duplicate_warning</code></td>
<td><code>{ callback }</code></td>
<td>A non-idempotent schedule may duplicate work</td>
</tr>
<tr>
<td><code>queue:create</code></td>
<td><code>{ callback, id }</code></td>
<td>A task is enqueued</td>
</tr>
<tr>
<td><code>queue:retry</code></td>
<td><code>{ callback, id, attempt, maxAttempts }</code></td>
<td>A queued callback is retried</td>
</tr>
<tr>
<td><code>queue:error</code></td>
<td><code>{ callback, id, error, attempts }</code></td>
<td>A queued callback fails after all retries</td>
</tr>
</tbody>
</table>
<h3 id="lifecycle-events">Lifecycle events</h3>
<table>
<thead>
<tr>
<th>Type</th>
<th>Payload</th>
<th>When</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>connect</code></td>
<td><code>{ connectionId }</code></td>
<td>A WebSocket connection is established</td>
</tr>
<tr>
<td><code>disconnect</code></td>
<td><code>{ connectionId, code, reason }</code></td>
<td>A WebSocket connection is closed</td>
</tr>
<tr>
<td><code>destroy</code></td>
<td><code>{}</code></td>
<td>The agent is destroyed</td>
</tr>
</tbody>
</table>
<h3 id="workflow-events">Workflow events</h3>
<table>
<thead>
<tr>
<th>Type</th>
<th>Payload</th>
<th>When</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>workflow:start</code></td>
<td><code>{ workflowId, workflowName? }</code></td>
<td>A workflow instance is started</td>
</tr>
<tr>
<td><code>workflow:event</code></td>
<td><code>{ workflowId, eventType? }</code></td>
<td>An event is sent to a workflow</td>
</tr>
<tr>
<td><code>workflow:approved</code></td>
<td><code>{ workflowId, reason? }</code></td>
<td>A workflow is approved</td>
</tr>
<tr>
<td><code>workflow:rejected</code></td>
<td><code>{ workflowId, reason? }</code></td>
<td>A workflow is rejected</td>
</tr>
<tr>
<td><code>workflow:terminated</code></td>
<td><code>{ workflowId, workflowName? }</code></td>
<td>A workflow is terminated</td>
</tr>
<tr>
<td><code>workflow:paused</code></td>
<td><code>{ workflowId, workflowName? }</code></td>
<td>A workflow is paused</td>
</tr>
<tr>
<td><code>workflow:resumed</code></td>
<td><code>{ workflowId, workflowName? }</code></td>
<td>A workflow is resumed</td>
</tr>
<tr>
<td><code>workflow:restarted</code></td>
<td><code>{ workflowId, workflowName? }</code></td>
<td>A workflow is restarted</td>
</tr>
</tbody>
</table>
<h3 id="mcp-events">MCP events</h3>
<table>
<thead>
<tr>
<th>Type</th>
<th>Payload</th>
<th>When</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>mcp:client:preconnect</code></td>
<td><code>{ serverId }</code></td>
<td>Before connecting to an MCP server</td>
</tr>
<tr>
<td><code>mcp:client:connect</code></td>
<td><code>{ url, transport, state, error? }</code></td>
<td>An MCP connection attempt completes or fails</td>
</tr>
<tr>
<td><code>mcp:client:authorize</code></td>
<td><code>{ serverId, authUrl, clientId? }</code></td>
<td>An MCP OAuth flow begins</td>
</tr>
<tr>
<td><code>mcp:client:discover</code></td>
<td><code>{ url?, state?, error?, capability? }</code></td>
<td>MCP capability discovery succeeds or fails</td>
</tr>
</tbody>
</table>
<h3 id="email-events">Email events</h3>
<table>
<thead>
<tr>
<th>Type</th>
<th>Payload</th>
<th>When</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>email:receive</code></td>
<td><code>{ from, to, subject? }</code></td>
<td>An email is received</td>
</tr>
<tr>
<td><code>email:reply</code></td>
<td><code>{ from, to, subject? }</code></td>
<td>A reply email is sent</td>
</tr>
<tr>
<td><code>email:send</code></td>
<td><code>{ from, to, subject? }</code></td>
<td>An email is sent</td>
</tr>
</tbody>
</table>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/agents/runtime/operations/observability/tracing/"><h3 id="card-tracing-agents-runtime-operations-observability-tracing">Tracing</h3><p>Trace model calls, tool runs, and approvals with Workers traces.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/operations/configuration/"><h3 id="card-configuration-agents-runtime-operations-configuration">Configuration</h3><p>wrangler.jsonc setup and deployment.</p></a></p>
<p><a class="nb-card nb-link-card" href="/workers/observability/logs/tail-workers/"><h3 id="card-tail-workers-workers-observability-logs-tail-workers">Tail Workers</h3><p>Forward diagnostics channel events to a Tail Worker for production monitoring.</p></a></p>
