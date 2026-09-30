<p>Agent tracing helps you understand what an agent did at every turn, including its model calls, tool runs, and approval requests. Use traces to investigate unexpected behavior, find slow operations, and review token usage.</p>
<p>Agent activity appears alongside runtime events such as fetch calls, KV reads, and D1 queries in <a href="/workers/observability/traces/">Workers traces</a>.</p>
<h2 id="enable-tracing">Enable tracing</h2>
<p>Enable tracing in your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/2645.md")
</div>
<h2 id="view-agent-activity">View agent activity</h2>
<p>Open the <a href="https://dash.cloudflare.com/?to=/:account/agents">Agents tab</a> in the Cloudflare Dashboard to see traced agents and subagents. The overview shows each agent's model, session count, runs, and total token usage.</p>
<p>A session is a conversation made up of one or more turns. A turn is one request to an agent and its response.</p>
<p><img src="/assets/upstream/images/workers-observability/agent_overview.png" alt="Agents dashboard showing agents with session, run, and token totals" /></p>
<p>Select an agent to see its traces. Each trace includes its duration, token breakdown, and status.</p>
<p><img src="/assets/upstream/images/workers-observability/agent_tracing_turn_view.png" alt="Agent details showing recent traces and token totals" /></p>
<p>There are two ways to follow what an agent did: <strong>Session replay</strong> and <strong>Trace</strong>.</p>
<p><strong>Session replay</strong> shows the recorded conversation across turns, including messages, reasoning, tool calls, and subagent activity. What appears depends on your <a href="/agents/runtime/operations/observability/tracing/#payload-privacy">payload recording settings</a>.</p>
<p><img src="/assets/upstream/images/workers-observability/agent_tracing_session_replay.png" alt="Session replay showing messages, reasoning, and subagent tool calls" /></p>
<p><strong>Trace</strong> is a waterfall of the operations performed during one turn. It shows when each operation started, how long it took, and which operation called it.</p>
<p><img src="/assets/upstream/images/workers-observability/agent_tracing_waterfall.png" alt="Trace waterfall showing nested agent, model, tool, and D1 spans" /></p>
<h2 id="trace-structure">Trace structure</h2>
<p>Each turn produces a trace made of spans, one for each timed operation:</p>
<pre><code class="language-txt">invoke_agent {agent class}&#10;├── chat {model}&#10;└── execute_tool {tool}&#10;    └── tool_approval {tool}&#10;</code></pre>
<p>The <code>invoke_agent</code> span covers the turn. Model calls, tool runs, and approvals appear as nested spans. Subagent work appears under the operation that invoked it.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2644.md")
</aside>
<h3 id="agent-identity">Agent identity</h3>
<p>Agent spans use three fields to identify the work shown in the dashboard:</p>
<ul>
<li><strong>Agent name</strong> identifies the logical agent implementation. Use a shared name such as <code>booking-agent</code>.</li>
<li><strong>Agent ID</strong> identifies the stable agent instance or resource, such as <code>booking-agent-production</code>.</li>
<li><strong>Conversation ID</strong> identifies the current conversation or session.</li>
</ul>
<p>Do not derive the agent name from a request, conversation, or user identifier. This creates too many distinct agent names in the dashboard.</p>
<h3 id="payload-privacy">Payload privacy</h3>
<p>Message and tool payloads can contain personally identifiable information. Only record payloads that are safe to store. Each integration controls payload recording differently, so configure it in the relevant <a href="/agents/runtime/operations/observability/tracing/#framework-setup">Framework setup</a> section.</p>
<p>Think and <code>wrapAISDK()</code> use <code>storeMessages</code> to record input and output messages on <code>chat</code> spans. They use <code>storeTools</code> to record arguments and results on <code>execute_tool</code> spans.</p>
<h2 id="framework-setup">Framework setup</h2>
<p>Tracing and payload controls depend on the integration. Think and Flue instrument turns automatically. Direct AI SDK calls and custom harnesses need additional setup.</p>
<h3 id="think">Think</h3>
<p>Think automatically instruments your agent and emits the <a href="/agents/runtime/operations/observability/tracing/#trace-structure">standard span structure</a>. No additional tracing setup is required.</p>
<h4 id="store-payloads">Store payloads</h4>
<p>Think does not store message or tool payloads by default. To record them, override the properties on the agent class:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2646.md")
</div>
<h3 id="flue">Flue</h3>
<p><a href="https://flueframework.com/blog/flue-2/">Flue v2+</a> also automatically instruments your agent and emits the <a href="/agents/runtime/operations/observability/tracing/#trace-structure">standard span structure</a>. No additional tracing setup is required.</p>
<h4 id="exclude-payloads">Exclude payloads</h4>
<p>Flue stores messages, system instructions, tool definitions, arguments, and results by default. To stop recording them, set content to false:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2647.md")
</div>
<h3 id="ai-sdk">AI SDK</h3>
<p>For direct <a href="https://sdk.vercel.ai/">AI SDK</a> calls, wrap the namespace once:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2648.md")
</div>
<p><code>wrapAISDK()</code> supports AI SDK v6 and v7. It instruments <code>generateText</code>, <code>streamText</code>, <code>generateObject</code>, and <code>streamObject</code>, creating the <code>invoke_agent</code> parent before model and tool work begins.</p>
<p>Unlike Think, a direct AI SDK call has no Agent instance from which to infer dashboard identity. Supply the <a href="/agents/runtime/operations/observability/tracing/#agent-identity">agent identity fields</a> on each call.</p>
<p>Only include context that is safe to store. Do not include credentials, tokens, user input, or other secrets.</p>
<h4 id="ai-sdk-v7">AI SDK v7</h4>
<p>Use native AI SDK v7 telemetry fields to supply identity. You can include additional scalar context, such as a tenant or route, to make traces easier to query:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2649.md")
</div>
<p>This maps <code>functionId</code>, <code>agentId</code>, and <code>conversationId</code> to <code>gen_ai.agent.name</code>, <code>gen_ai.agent.id</code>, and <code>gen_ai.conversation.id</code>. Other included scalar values use the <code>cloudflare.agents.runtime_context.*</code> namespace.</p>
<h4 id="ai-sdk-v6">AI SDK v6</h4>
<p>AI SDK v6 uses <code>experimental_telemetry.metadata</code> for the same identity and additional span data:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2650.md")
</div>
<p>Additional scalar metadata uses the <code>cloudflare.agents.metadata.*</code> namespace.</p>
<h4 id="store-payloads-1">Store payloads</h4>
<p><code>wrapAISDK()</code> does not store message or tool payloads by default. To record them with AI SDK v6 or v7, pass storage options when wrapping the namespace:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2651.md")
</div>
<h3 id="custom-harnesses">Custom harnesses</h3>
<p>If your agent does not use one of our currently supported frameworks, instrument it with the <a href="/workers/observability/traces/custom-spans/">Workers custom spans API</a>. Create an <code>invoke_agent</code> span for each turn, with <code>chat</code> spans for model calls, <code>execute_tool</code> spans for tool runs, and <code>tool_approval</code> spans for approvals.</p>
<p>For span names, attributes, and implementation examples, refer to the <a href="https://github.com/open-telemetry/semantic-conventions-genai/blob/main/reference/README.md">OpenTelemetry GenAI reference implementations</a>. Adapt these examples to the Workers custom spans API.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2643.md")
</aside>
<h4 id="add-agent-identity">Add agent identity</h4>
<p>Add these attributes to both the <code>invoke_agent</code> and <code>chat</code> spans so the Agents dashboard can associate the telemetry with the agent and conversation:</p>
<table>
<thead>
<tr>
<th>Attribute</th>
<th><code>invoke_agent</code> span</th>
<th><code>chat</code> span</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gen_ai.operation.name</code></td>
<td><code>invoke_agent</code></td>
<td><code>chat</code></td>
</tr>
<tr>
<td><code>gen_ai.agent.name</code></td>
<td>A shared agent name, such as <code>booking-agent</code></td>
<td>The same agent name</td>
</tr>
<tr>
<td><code>gen_ai.agent.id</code></td>
<td>A stable identifier for the agent instance</td>
<td>The same agent ID</td>
</tr>
<tr>
<td><code>gen_ai.conversation.id</code></td>
<td>The conversation, session, or thread identifier</td>
<td>The same conversation, session, or thread ID</td>
</tr>
</tbody>
</table>
<h4 id="store-payloads-2">Store payloads</h4>
<p>For custom spans, add payload attributes manually. Use <code>gen_ai.input.messages</code>, <code>gen_ai.output.messages</code>, and <code>gen_ai.system_instructions</code> on model spans. Use <code>gen_ai.tool.call.arguments</code> and <code>gen_ai.tool.call.result</code> on tool spans. The custom spans API accepts scalar attribute values, so serialize structured payloads with <code>JSON.stringify()</code>. These values are recorded whenever the invocation is sampled. Only add payloads that are safe to store.</p>
<h2 id="exporting-traces">Exporting traces</h2>
<p>Span attributes follow the <a href="https://github.com/open-telemetry/semantic-conventions-genai">OpenTelemetry Generative AI semantic conventions</a>, so any tool that reads OpenTelemetry data can consume them. To send traces to an external destination, <a href="/workers/observability/exporting-opentelemetry-data/">configure an OpenTelemetry Protocol (OTLP) endpoint</a> in Workers Observability.</p>
<h2 id="pricing">Pricing</h2>
<p>Agent traces use <a href="/workers/observability/traces/">Workers tracing</a> and follow Workers Observability pricing.</p>
<p>The Agents view shows your agent's operations. The full Worker trace may include additional spans from SDK internals and other Worker-level operations. To inspect the full trace, select <strong>View in Observability</strong>.</p>
<p>Every span counts as one observability event, including spans not shown in the Agents view. Tracing is free while in beta. Beginning October 1, 2026, tracing will be included in existing Workers Observability pricing:</p>
<table>
<thead>
<tr>
<th>Tier</th>
<th>Included events</th>
<th>Retention</th>
</tr>
</thead>
<tbody>
<tr>
<td>Workers Free</td>
<td>200,000 per day</td>
<td>3 days</td>
</tr>
<tr>
<td>Workers Paid</td>
<td>20 million per month ($0.60 per additional million)</td>
<td>7 days</td>
</tr>
</tbody>
</table>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Use agent traces for debugging and observability. Traces are not a complete or lossless record of a conversation.</li>
<li>Payload data is subject to span size limits. Long messages, reasoning, tool arguments, and results may be truncated. These limits may change.</li>
<li>Session replay does not display images.</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/agents/runtime/operations/observability/diagnostics-channels/"><h3 id="card-diagnostics-channels-agents-runtime-operations-observability-diagnostics-channels">Diagnostics channels</h3><p>Subscribe to structured agent events for state changes, schedules, workflows, and more.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/operations/configuration/"><h3 id="card-configuration-agents-runtime-operations-configuration">Configuration</h3><p>wrangler.jsonc setup and deployment.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/agents-api/"><h3 id="card-agents-api-agents-runtime-agents-api">Agents API</h3><p>Complete API reference for the Agents SDK.</p></a></p>
