<p>This guide explains how to provide human feedback for AI Gateway evaluations using Worker bindings.</p>
<h2 id="1-run-an-ai-evaluation"><ol>
<li>Run an AI Evaluation</li>
</ol></h2>
<p>Start by sending a prompt to the AI model through your AI Gateway.</p>
<pre><code class="language-javascript">const resp = await env.AI.run(&#10;	&quot;@cf/meta/llama-3.1-8b-instruct&quot;,&#10;	{&#10;		prompt: &quot;tell me a joke&quot;,&#10;	},&#10;	{&#10;		gateway: {&#10;			id: &quot;my-gateway&quot;,&#10;		},&#10;	},&#10;);&#10;&#10;const myLogId = env.AI.aiGatewayLogId;&#10;</code></pre>
<p>Let the user interact with or evaluate the AI response. This interaction will inform the feedback you send back to the AI Gateway.</p>
<h2 id="2-send-human-feedback"><ol start="2">
<li>Send Human Feedback</li>
</ol></h2>
<p>Use the <a href="/ai-gateway/usage/worker-binding-methods/#patchlog"><code>patchLog()</code></a> method to provide feedback for the AI evaluation.</p>
<pre><code class="language-javascript">await env.AI.gateway(&quot;my-gateway&quot;).patchLog(myLogId, {&#10;	feedback: 1, // all fields are optional; set values that fit your use case&#10;	score: 100,&#10;	metadata: {&#10;		user: &quot;123&quot;, // Optional metadata to provide additional context&#10;	},&#10;});&#10;</code></pre>
<h2 id="feedback-parameters-explanation">Feedback parameters explanation</h2>
<ul>
<li><code>feedback</code>: is either <code>-1</code> for negative or <code>1</code> to positive, <code>0</code> is considered not evaluated.</li>
<li><code>score</code>: A number between 0 and 100.</li>
<li><code>metadata</code>: An object containing additional contextual information.</li>
</ul>
<h3 id="patchlog-send-feedback">patchLog: Send Feedback</h3>
<p>The <code>patchLog</code> method allows you to send feedback, score, and metadata for a specific log ID. All object properties are optional, so you can include any combination of the parameters:</p>
<pre><code class="language-javascript">gateway.patchLog(&quot;my-log-id&quot;, {&#10;	feedback: 1,&#10;	score: 100,&#10;	metadata: {&#10;		user: &quot;123&quot;,&#10;	},&#10;});&#10;</code></pre>
<p>Returns: <code>Promise&lt;void&gt;</code> (Make sure to <code>await</code> the request.)</p>
