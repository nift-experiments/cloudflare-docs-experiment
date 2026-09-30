<p>Code Mode is a tool-use pattern where a model writes code instead of requesting each operation separately. The model receives one code-execution tool. Its code becomes a compact plan that calls tools, processes results, and returns the information needed for a response.</p>
<p>Code Mode exposes configured tools as typed methods. Models use those methods to express multi-step work with familiar programming constructs. Depending on the integration, tool definitions can be provided up front or discovered when needed.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2672.md")
</aside>
<h2 id="code-as-a-plan">Code as a plan</h2>
<p>With direct tool use, the model selects one tool, receives its result, and then decides what to do next. Each operation can require another round trip through the model.</p>
<p>Code Mode moves that intermediate logic into executable code. A single plan can:</p>
<ul>
<li>Compose several dependent tool calls.</li>
<li>Loop over collections of results.</li>
<li>Filter and transform returned data.</li>
<li>Branch based on earlier results.</li>
<li>Shape the final returned value.</li>
</ul>
<p>This approach keeps control flow and data handling together. It is useful when the model must coordinate several operations before producing an answer.</p>
<h2 id="progressive-tool-discovery">Progressive tool discovery</h2>
<p>Large tool catalogs can consume significant model context if every definition is loaded up front. Connector-based Code Mode runtimes support progressive discovery through <code>codemode.search()</code> and <code>codemode.describe()</code>.</p>
<p>Search finds relevant connectors, methods, and saved snippets. Describe returns detailed type information for a selected target. These results enter the running code, so the model can pull the definitions it needs instead of receiving the entire catalog with every request.</p>
<h2 id="choose-between-code-mode-and-direct-tool-calls">Choose between Code Mode and direct tool calls</h2>
<p>With direct tool calls, each result returns to the model before it chooses the next operation. Intermediate data consumes context, even when the model only needs a small part of it for the final answer.</p>
<p>Code Mode keeps that work inside one sandbox execution. Generated code can pass results between tools, filter intermediate data, and return only the final value the model needs. This makes multi-tool tasks more efficient and easier to generalize or repeat.</p>
<p>Use direct tool calls for simple tasks with a small, fixed tool set. Use Code Mode when a task needs composition, dependent calls, progressive discovery, reusable logic, or control flow:</p>
<table>
<thead>
<tr>
<th>Pattern</th>
<th>Best suited for</th>
</tr>
</thead>
<tbody>
<tr>
<td>Direct tool calls</td>
<td>Simple tasks using a small, known tool set</td>
</tr>
<tr>
<td>Code Mode</td>
<td>Composed or dependent calls, large tool catalogs, loops, branching, filtering, result shaping, or reusable logic</td>
</tr>
</tbody>
</table>
<h2 id="choose-an-integration">Choose an integration</h2>
<p>Code Mode provides surfaces for agent runtimes, AI frameworks, browsers, and Model Context Protocol (MCP) systems.</p>
<div class="nb-card-grid">
@input("content/.markup/bodies/2673.md")
</div>
<h2 id="understand-the-pattern">Understand the pattern</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/2674.md")
</div>
