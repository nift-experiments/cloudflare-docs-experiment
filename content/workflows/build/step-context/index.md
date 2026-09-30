<p>Every <code>step.do</code> callback receives a <strong>context object</strong> (<code>WorkflowStepContext</code>) as its first argument. The context gives your step code runtime information about the step itself, the current retry attempt, and the resolved configuration for that step.</p>
<h2 id="workflowstepcontext">WorkflowStepContext</h2>
<pre><code class="language-ts">type WorkflowStepContext = {&#10;	step: {&#10;		name: string;&#10;		count: number;&#10;	};&#10;	attempt: number;&#10;	config: WorkflowStepConfig;&#10;};&#10;</code></pre>
<h3 id="properties">Properties</h3>
<table>
<thead>
<tr>
<th>Property</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>step.name</code></td>
<td><code>string</code></td>
<td>The name you passed to <code>step.do</code>.</td>
</tr>
<tr>
<td><code>step.count</code></td>
<td><code>number</code></td>
<td>How many times <code>step.do</code> has been called with this name so far in the current Workflow run. Starts at <code>1</code> for the first call with a given name.</td>
</tr>
<tr>
<td><code>attempt</code></td>
<td><code>number</code></td>
<td>The current attempt number (1-indexed). <code>1</code> on the first try, <code>2</code> on the first retry, and so on.</td>
</tr>
<tr>
<td><code>config</code></td>
<td><a href="/workflows/build/workers-api/#workflowstepconfig"><code>WorkflowStepConfig</code></a></td>
<td>The resolved retry and timeout configuration for this step, including any defaults applied by the runtime.</td>
</tr>
</tbody>
</table>
<p>If a step config's <code>retries.delay</code> is a function, the dynamic delay is not exposed on <code>ctx.config.retries.delay</code>. The delay function receives its own context object with the current step context and the error that caused the retry.</p>
<h2 id="access-the-context">Access the context</h2>
<p>Pass a parameter to your <code>step.do</code> callback to receive the context object:</p>
<pre><code class="language-ts">await step.do(&quot;my-step&quot;, async (ctx) =&gt; {&#10;	console.log(ctx.step.name); // &quot;my-step&quot;&#10;	console.log(ctx.step.count); // 1&#10;	console.log(ctx.attempt); // 1 on first try, 2 on first retry, etc.&#10;	console.log(ctx.config); // { retries: { limit: 5, ... }, timeout: &quot;10 minutes&quot; }&#10;});&#10;</code></pre>
<p>The context is also available when you pass a custom <code>WorkflowStepConfig</code>:</p>
<pre><code class="language-ts">await step.do(&#10;	&quot;call an API&quot;,&#10;	{&#10;		retries: {&#10;			limit: 10,&#10;			delay: &quot;10 seconds&quot;,&#10;			backoff: &quot;exponential&quot;,&#10;		},&#10;		timeout: &quot;30 minutes&quot;,&#10;	},&#10;	async (ctx) =&gt; {&#10;		console.log(ctx.config.retries.limit); // 10&#10;		console.log(ctx.config.timeout); // &quot;30 minutes&quot;&#10;	},&#10;);&#10;</code></pre>
<p>To configure delay functions, refer to <a href="/workflows/build/sleeping-and-retrying/#set-a-dynamic-retry-delay">Set a dynamic retry delay</a>.</p>
<h2 id="examples">Examples</h2>
<h3 id="adjust-behavior-based-on-retry-attempt">Adjust behavior based on retry attempt</h3>
<p>Use <code>ctx.attempt</code> to change how your step behaves on retries. For example, you might use a fallback endpoint after a certain number of retries:</p>
<pre><code class="language-ts">await step.do(&#10;	&quot;fetch data&quot;,&#10;	{ retries: { limit: 5, delay: &quot;5 seconds&quot;, backoff: &quot;linear&quot; } },&#10;	async (ctx) =&gt; {&#10;		const url =&#10;			ctx.attempt &lt;= 3&#10;				? &quot;https://api.example.com/primary&quot;&#10;				: &quot;https://api.example.com/fallback&quot;;&#10;&#10;		const response = await fetch(url);&#10;		if (!response.ok) {&#10;			throw new Error(`Request failed with status ${response.status}`);&#10;		}&#10;		return await response.json();&#10;	},&#10;);&#10;</code></pre>
<h3 id="log-step-metadata-for-observability">Log step metadata for observability</h3>
<p>Use <code>ctx.step</code> to add structured metadata to your logs:</p>
<pre><code class="language-ts">await step.do(&quot;process-order&quot;, async (ctx) =&gt; {&#10;	console.log(&#10;		JSON.stringify({&#10;			step: ctx.step.name,&#10;			stepCount: ctx.step.count,&#10;			attempt: ctx.attempt,&#10;			retryLimit: ctx.config.retries?.limit,&#10;		}),&#10;	);&#10;&#10;	// Your step logic here&#10;});&#10;</code></pre>
