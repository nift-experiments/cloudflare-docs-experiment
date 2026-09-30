<p>This guide adds a durable Code Mode runtime to an Agents SDK application. The runtime stores execution history, pending approvals, and snippets across Durable Object hibernation.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/2679.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<p>You need an existing Agents SDK application with a Durable Object and Vite. The example uses <code>AIChatAgent</code> and the AI SDK.</p>
<h2 id="integrate-code-mode">Integrate Code Mode</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2684.md")
</div>
<h2 id="use-the-runtime-without-the-ai-sdk">Use the runtime without the AI SDK</h2>
<p>Use <code>execute()</code>, <code>search()</code>, and <code>describe()</code> when an MCP server or another host invokes Code Mode without an AI SDK tool adapter:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2685.md")
</div>
<p><code>search()</code> and <code>describe()</code> do not run sandbox code. Their results include <code>requiresApproval: true</code> for connector methods that pause before execution.</p>
<p><code>execute()</code> returns the same durable result as the model-facing tool. A result can complete, pause, or contain an execution error. Resolve a paused result with <code>approve()</code> or <code>reject()</code>.</p>
<h2 id="verify-the-integration">Verify the integration</h2>
<p>Ask the model to list saved notes. The model receives one <code>codemode</code> tool and can discover connector methods inside the sandbox:</p>
<pre><code class="language-js">async () =&gt; {&#10;	const matches = await codemode.search(&quot;list saved notes&quot;);&#10;	const docs = await codemode.describe(matches.results[0].path);&#10;	const savedNotes = await notes.listNotes();&#10;&#10;	return { docs, savedNotes };&#10;};&#10;</code></pre>
<p>When the model calls <code>notes.createNote()</code>, the execution pauses. Use <code>pendingApprovals()</code> to show the pending action. Pass its <code>executionId</code> to <code>approveExecution()</code>, or pass both <code>executionId</code> and <code>seq</code> to <code>rejectExecution()</code>.</p>
<p>Approval resumes the same script through replay. Completed calls return recorded results instead of running again. Rejection ends the paused execution without undoing earlier actions.</p>
<p>Call <code>rollbackExecution()</code> to compensate for applied calls whose currently configured connector provides <code>revert</code>. Save only completed executions as snippets.</p>
