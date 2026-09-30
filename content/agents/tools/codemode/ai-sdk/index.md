<p>The <code>@cloudflare/codemode/ai</code> entry point converts AI SDK tools into one Code Mode tool. The model writes JavaScript that calls your tools, and an executor runs that code in an isolated sandbox.</p>
<p>Choose between two integration patterns:</p>
<table>
<thead>
<tr>
<th>Pattern</th>
<th>Use case</th>
<th>Approval behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>createCodeTool()</code></td>
<td>Simple, stateless execution with one or more tool providers</td>
<td>Excludes tools that use <code>needsApproval</code></td>
</tr>
<tr>
<td><code>ToolSetConnector</code> or <code>toolSetConnector()</code></td>
<td>Durable execution through a Code Mode runtime</td>
<td>Maps <code>needsApproval</code> to durable runtime approval</td>
</tr>
</tbody>
</table>
<h2 id="create-a-stateless-code-mode-tool">Create a stateless Code Mode tool</h2>
<p><code>createCodeTool()</code> accepts an AI SDK <code>ToolSet</code> or an array of tool providers. It also requires an executor. It returns a standard AI SDK tool for use with <code>streamText()</code> or <code>generateText()</code>.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2695.md")
</div>
<p>The example uses <code>generateText()</code> for a completed response. You can pass the same <code>codemode</code> tool to <code>streamText()</code> for streaming. The generated tool description includes TypeScript definitions for <code>getWeather</code>. The model still writes JavaScript, such as:</p>
<pre><code class="language-js">async () =&gt; {&#10;	const weather = await codemode.getWeather({ city: &quot;Lisbon&quot; });&#10;	return weather.conditions;&#10;};&#10;</code></pre>
<p>The default namespace is <code>codemode</code>. <code>createCodeTool()</code> also accepts a custom <code>description</code>. Include <code>{{types}}</code> in that description where Code Mode should insert the generated definitions.</p>
<h2 id="organize-tools-with-providers">Organize tools with providers</h2>
<p>A tool provider groups tools under one sandbox namespace. Pass the tool set directly when every tool belongs under <code>codemode.*</code>.</p>
<p>Use <code>aiTools()</code> when combining AI SDK tools with providers from other packages. The following optional workspace example also requires <code>@cloudflare/shell</code>:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/shell</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/shell" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/shell</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/shell" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/shell</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/shell" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/shell</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/shell" aria-label="Copy to clipboard">Copy</button></div></div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2696.md")
</div>
<p>This example exposes AI SDK tools as <code>codemode.*</code> and workspace tools as <code>state.*</code>.</p>
<p>To assign custom namespaces, pass provider objects instead:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2697.md")
</div>
<p>The generated code can then call <code>weather.getWeather()</code> and <code>notifications.send()</code>. Provider names must be unique, valid JavaScript identifiers.</p>
<h2 id="use-ai-sdk-tools-with-the-durable-runtime">Use AI SDK tools with the durable runtime</h2>
<p>Use <code>ToolSetConnector</code> or its <code>toolSetConnector()</code> convenience function when runs need durable state. The connector adapts an AI SDK <code>ToolSet</code> for <code>createCodemodeRuntime()</code>. The helper returns <code>new ToolSetConnector(ctx, options)</code>.</p>
<p>Create the connector from inside an Agent or another Durable Object:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2698.md")
</div>
<p>The example exports <code>CodemodeRuntime</code> manually. If you configure the Code Mode Vite plugin as described in <a href="/agents/tools/codemode/durable-runtime/">Create a durable Code Mode runtime</a>, remove that manual export because the plugin adds it.</p>
<p>The connector defaults to the <code>tools</code> namespace when <code>name</code> is omitted. It excludes tools without an <code>execute</code> function from both generated types and sandbox bindings.</p>
<p>The durable runtime adds an execution log, pause and resume behavior, and on-demand connector discovery. The model can find methods with <code>codemode.search()</code> and inspect their types with <code>codemode.describe()</code>.</p>
<h2 id="approval-behavior">Approval behavior</h2>
<p>The two integration patterns handle AI SDK approvals differently.</p>
<h3 id="createcodetool-approvals"><code>createCodeTool()</code> approvals</h3>
<p><code>createCodeTool()</code> filters out tools where <code>needsApproval</code> is <code>true</code> or a function. Filtered tools do not appear in generated types and cannot run from sandbox code. A tool with <code>needsApproval: false</code> remains available.</p>
<p>This stateless path does not pause execution for AI SDK approval. Use a standard AI SDK tool outside Code Mode if that tool needs the AI SDK approval flow.</p>
<h3 id="toolsetconnector-approvals"><code>ToolSetConnector</code> approvals</h3>
<p><code>ToolSetConnector</code> maps AI SDK <code>needsApproval</code> to the durable runtime's <code>requiresApproval</code> annotation. Calling that tool pauses the run. Your application can inspect pending actions and resume the same execution with <code>runtime.approve({ executionId })</code>.</p>
<p>A function-valued <code>needsApproval</code> cannot be evaluated before the sandbox supplies arguments. The connector therefore treats the tool as always requiring approval. <code>needsApproval: false</code> executes without pausing.</p>
<p>This approval uses the Code Mode runtime's durable pause, approval, and replay flow. It does not use the AI SDK per-call approval flow.</p>
