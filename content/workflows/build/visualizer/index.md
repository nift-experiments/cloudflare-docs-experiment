<p>View a visual representation of your parsed Workflow code as a diagram on the Cloudflare dashboard.</p>
<p>The diagram illustrates your sequenced &amp; parallel steps, conditionals, loops, and nested logic. To see the Workflow at a high level, view the diagram with loops and conditionals collapsed, or expand for a more detailed view.</p>
<p><img src="/assets/upstream/images/changelog/workflows/2026-02-03-workflows-diagram.png" alt="Example diagram" /></p>
<p>Workflow diagrams are currently in beta for all Typescript and Javascript Workers. View your Workflows in the <a href="https://dash.cloudflare.com/?to=/:account/workers/workflows">Cloudflare dashboard</a> to see their diagrams.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17544.md")
</aside>
<h2 id="node-types">Node types</h2>
<p>The diagrams consist of the following node types:</p>
<table>
<thead>
<tr>
<th>Node type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>StepSleep</code></td>
<td>Pauses Workflow execution for a specified duration.</td>
</tr>
<tr>
<td><code>StepDo</code></td>
<td>Represents a named, retriable step that wraps a unit of work.</td>
</tr>
<tr>
<td><code>StepWaitForEvent</code></td>
<td>Suspends execution until an external event is received.</td>
</tr>
<tr>
<td><code>StepSleepUntil</code></td>
<td>Pauses Workflow execution until a specific date and time.</td>
</tr>
<tr>
<td><code>LoopNode</code></td>
<td>Represents a loop construct (<code>for</code>, <code>while</code>, etc.) that repeats a block of logic.</td>
</tr>
<tr>
<td><code>ParallelNode</code></td>
<td>Groups steps that execute concurrently, such as those inside <code>Promise.all()</code>.</td>
</tr>
<tr>
<td><code>TryNode</code></td>
<td>Represents a <code>try...catch</code> block that handles errors within a Workflow.</td>
</tr>
<tr>
<td><code>BlockNode</code></td>
<td>Groups a sequence of steps into a logical block for display purposes.</td>
</tr>
<tr>
<td><code>IfNode</code></td>
<td>Represents a conditional branch based on an <code>if/else</code> expression.</td>
</tr>
<tr>
<td><code>SwitchNode</code></td>
<td>Represents a <code>switch</code> statement that routes execution across multiple cases.</td>
</tr>
<tr>
<td><code>StartNode</code></td>
<td>Marks the entry point of the Workflow or a function definition.</td>
</tr>
<tr>
<td><code>FunctionCall</code></td>
<td>Represents a call to a named function within the Workflow code.</td>
</tr>
<tr>
<td><code>FunctionDef</code></td>
<td>Represents the definition of a function used within the Workflow.</td>
</tr>
<tr>
<td><code>BreakNode</code></td>
<td>Represents a <code>break</code> statement that exits a loop early.</td>
</tr>
</tbody>
</table>
<h2 id="execution-order">Execution order</h2>
<p>Each node has a <code>starts</code> and <code>resolves</code> field that tracks execution order. These indices indicate when a promise began executing and when it ended, relative to the first promise that started without an immediate conclusion. This corresponds to vertical positioning in the diagram (i.e. all steps with <code>starts: 1</code> will appear inline).</p>
<p>When parsing, unawaited promises or <code>Promise.all()</code> calls are assigned an entry number stored in the <code>starts</code> field. When an <code>await</code> is encountered for that promise, the entry number is incremented and saved as the exit number in the <code>resolves</code> field. This allows the diagram to determine which promises run concurrently and when each will complete relative to the others.</p>
<p>If steps are awaited at the point of declaration, <code>starts</code> and <code>resolves</code> will be undefined, and the Workflow executes in the order the steps appear to the runtime.</p>
