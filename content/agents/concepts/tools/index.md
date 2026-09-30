<p>Tools let models retrieve information, process data, and perform actions. Each tool defines an interface that describes its inputs, outputs, and behavior.</p>
<p>A travel agent might use tools to search flights, check hotel rates, process payments, and send confirmation emails. The tool interface lets the model understand when and how to use each capability.</p>
<p>Tool design involves three independent choices:</p>
<ol>
<li><strong>Model interface</strong> — expose tools as direct tool calls or through Code Mode.</li>
<li><strong>Execution location</strong> — run tool implementations in a Worker, browser, or another Agent.</li>
<li><strong>Tool source</strong> — define tools in the application or connect to externally hosted tools through Model Context Protocol (MCP).</li>
</ol>
<p>For example, browser tools can be exposed directly or through Code Mode. An MCP tool can also be exposed through either model interface.</p>
<h2 id="choose-the-model-interface">Choose the model interface</h2>
<p>Direct tool calls and Code Mode define how the model sees and invokes tools. They do not determine where the underlying tool implementations run.</p>
<table>
<thead>
<tr>
<th>Interface</th>
<th>How it works</th>
<th>Use when</th>
</tr>
</thead>
<tbody>
<tr>
<td>Direct tool calls</td>
<td>The model receives individual tool definitions. Each result returns to the model before it chooses the next call.</td>
<td>The task is simple and uses a small, known tool set.</td>
</tr>
<tr>
<td>Code Mode</td>
<td>The model receives one code tool and writes code against typed tool interfaces.</td>
<td>The task needs composition, dependent calls, filtering, branching, repeatable logic, or tool discovery.</td>
</tr>
</tbody>
</table>
<h3 id="direct-tool-calls">Direct tool calls</h3>
<p>Most tool examples use direct tool calls, even when they do not name the pattern. You define each tool and pass its schema to the model. The model selects a tool, your application executes it, and the result returns to the model.</p>
<p>The model sees each intermediate result before choosing another tool. This makes the execution path easy to inspect. However, dependent operations require repeated model turns and consume context with intermediate data.</p>
<h3 id="code-mode">Code Mode</h3>
<p><a href="/agents/tools/codemode/">Code Mode</a> gives the model one code-execution tool. The model writes JavaScript that calls typed tools, passes results between them, and applies control flow.</p>
<p>The generated code can filter large responses and return only the final value the model needs. Intermediate results stay inside the sandbox instead of entering the model context after every operation. This makes Code Mode more efficient for composed workflows and large tool catalogs.</p>
<p>Code Mode also supports progressive discovery. The model can search available connectors and request detailed types only for the methods it needs. Successful programs can be saved as reusable snippets.</p>
<p>For runtime behavior, approvals, replay, and snippets, refer to <a href="/agents/tools/codemode/how-it-works/">How Code Mode works</a>.</p>
<h2 id="choose-where-tools-run">Choose where tools run</h2>
<p>Execution location describes where a tool implementation runs. It is independent from the model interface. Tools in each location can be exposed directly or through Code Mode.</p>
<table>
<thead>
<tr>
<th>Location</th>
<th>Use when</th>
<th>Start here</th>
</tr>
</thead>
<tbody>
<tr>
<td>Worker</td>
<td>The tool calls an API, queries SQL, or uses server-side bindings and secrets.</td>
<td><a href="/agents/communication-channels/chat/chat-agents/#server-side-tools">Server-side tools</a></td>
</tr>
<tr>
<td>Browser</td>
<td>The tool needs geolocation, clipboard, local storage, or other browser APIs.</td>
<td><a href="/agents/communication-channels/chat/chat-agents/#client-side-tools">Client-side tools</a></td>
</tr>
<tr>
<td>Another Agent</td>
<td>A chat-capable Agent should execute as a retained, streaming tool.</td>
<td><a href="/agents/runtime/execution/agent-tools/">Agents as tools</a></td>
</tr>
</tbody>
</table>
<p>With direct tool calls, the model calls the tool and the framework routes execution to the configured location.</p>
<p>With Code Mode, generated code runs in a sandbox. Calls from that code cross the sandbox boundary to the underlying tool implementation. Server tools can execute in the host Worker, browser-owned tools can execute in the parent page, and Agent tools can delegate work to another Agent.</p>
<h2 id="connect-external-tools-with-mcp">Connect external tools with MCP</h2>
<p>The <a href="https://modelcontextprotocol.io/introduction">Model Context Protocol (MCP)</a> standardizes how AI applications discover and invoke externally hosted tools. MCP describes the source and transport of a tool, not how the model must invoke it.</p>
<p>An Agent can expose MCP tools through either model interface:</p>
<ul>
<li>Pass MCP tools directly to a model with the <a href="/agents/tools/mcp/">Agents MCP client</a>.</li>
<li>Expose MCP tools inside Code Mode for composition and progressive discovery with <a href="/agents/tools/codemode/mcp/">MCP connectors</a>.</li>
</ul>
<p>An MCP server can also expose Code Mode itself. For example, it can present one <code>code</code> tool or separate <code>search</code> and <code>execute</code> tools. For these server-side patterns, refer to <a href="/agents/model-context-protocol/codemode/">Code Mode MCP server patterns</a>.</p>
<h2 id="control-side-effects">Control side effects</h2>
<p>Approval policy is also independent from execution location and tool source. Any tool that modifies external state may require user approval.</p>
<p>Direct tools can use the standard <a href="/agents/concepts/agentic-patterns/human-in-the-loop/">human-in-the-loop approval pattern</a>.</p>
<p>The durable Code Mode runtime can pause generated code before an annotated connector method executes. Approval replays completed calls from the execution log, applies the approved action, and continues the same program.</p>
