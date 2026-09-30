<p>Use the <code>@cloudflare/codemode/tanstack-ai</code> entry point to give <code>chat()</code> one Code Mode tool. The model can then write JavaScript that calls your TanStack AI server tools.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>You need an existing Workers project and a configured TanStack AI model adapter. This example uses the OpenAI adapter.</p>
<h2 id="add-code-mode">Add Code Mode</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/2661.md")
</div>
<p><code>createCodeTool()</code> returns a TanStack AI <code>ServerTool</code> named <code>codemode_execute</code>. Its description contains the generated types for both namespaces. The model can write code similar to this:</p>
<pre><code class="language-js">async () =&gt; {&#10;	const weatherResult = await weather.get_weather({ city: &quot;London&quot; });&#10;	const contacts = await directory.find_contacts({ team: &quot;travel&quot; });&#10;	return { weatherResult, contacts };&#10;};&#10;</code></pre>
<h2 id="namespace-behavior">Namespace behavior</h2>
<p><code>tanstackTools(tools, name)</code> converts an array of TanStack AI tools into a Code Mode tool provider. It uses each tool name as the method name and generates types from its input and output schemas.</p>
<p>The optional second argument sets the sandbox namespace. For example, <code>tanstackTools([getWeather], &quot;weather&quot;)</code> exposes <code>weather.get_weather()</code>. If you omit the name, Code Mode uses the default <code>codemode</code> namespace:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2662.md")
</div>
<p>Use distinct namespace names when you combine tool groups. Each provider contributes its generated declarations and executable server tools to the same Code Mode tool.</p>
<h2 id="approval-behavior">Approval behavior</h2>
<p>The <code>createCodeTool()</code> integration does not pause execution for TanStack AI approvals. <code>tanstackTools()</code> excludes a tool when its <code>needsApproval</code> property is <code>true</code> or a function. The excluded tool does not appear in generated type declarations and cannot run in the sandbox.</p>
<p>Tools with <code>needsApproval: false</code> remain available. The durable Code Mode runtime supports paused approvals through connector <code>requiresApproval</code> annotations, but this <code>createCodeTool()</code> integration does not use that approval flow.</p>
