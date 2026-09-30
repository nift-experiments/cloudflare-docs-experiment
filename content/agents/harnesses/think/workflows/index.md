<p><code>ThinkWorkflow</code> connects Think to Cloudflare Workflows when a durable job needs one model-driven reasoning step.</p>
<p>Use it when the Workflow owns the process:</p>
<ul>
<li>durable multi-step orchestration</li>
<li>approval gates or long waits</li>
<li>retryable deterministic side effects</li>
<li>a Think turn that should produce typed structured output</li>
</ul>
<p>Keep recurring prompts as <a href="/agents/harnesses/think/scheduled-tasks/">scheduled tasks</a>, and keep simple one-off background turns on <a href="/agents/harnesses/think/programmatic-submissions/"><code>submitMessages()</code></a>. Workflows are for jobs where the steps matter.</p>
<h2 id="api">API</h2>
<p>Import from <code>@cloudflare/think/workflows</code>:</p>
<pre><code class="language-ts">import { ThinkWorkflow } from &quot;@cloudflare/think/workflows&quot;;&#10;</code></pre>
<p>Extend <code>ThinkWorkflow</code> and call <code>step.prompt()</code> inside <code>run()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2096.md")
</div>
<p>Start the Workflow from inside your Think Agent with <code>runWorkflow()</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2097.md")
</div>
<p><code>runWorkflow()</code> creates the Workflow instance and injects the Agent identity that <code>ThinkWorkflow</code> needs to reconnect to <code>this.agent</code> inside <code>run()</code>. Prefer it over calling the Workflows binding directly:</p>
<pre><code class="language-ts">// Avoid this for Agent workflows. It does not include Agent context.&#10;await this.env.TRIAGE_WORKFLOW.create({ params: { issueNumber } });&#10;</code></pre>
<p>Use <code>sendWorkflowEvent()</code> from the Agent when a waiting Workflow needs an external signal, such as human approval:</p>
<pre><code class="language-ts">await this.sendWorkflowEvent(&quot;TRIAGE_WORKFLOW&quot;, workflowId, {&#10;	type: &quot;approval&quot;,&#10;	payload: { approved: true },&#10;});&#10;</code></pre>
<p><code>step.prompt()</code> accepts a prompt string and a Zod object schema. The schema is converted to JSON Schema before the Workflow calls the Agent. Think then runs a full agentic turn: the Agent may use its tools across multiple steps and returns the structured result by calling an internal <code>final_answer</code> tool whose arguments match the schema. This uses ordinary tool calling rather than a streaming <code>response_format</code>, so it works across every provider Think supports — including Workers AI, which rejects JSON Schema responses on streaming requests. When the Workflow resumes, the payload is validated again with the original Zod schema before the typed value is returned.</p>
<p>Unsupported Zod features that cannot be represented as JSON Schema fail while creating the prompt step. Think does not silently repair invalid model output. If the model does not produce a valid <code>final_answer</code> call, the submission reaches a terminal error state and <code>step.prompt()</code> throws.</p>
<h3 id="behavior-notes">Behavior notes</h3>
<ul>
<li><strong>The Agent may use its tools first.</strong> A <code>step.prompt()</code> turn is a full agentic turn: the Agent can call its own tools across multiple steps and then call the final-answer tool. Allow at least <code>maxSteps: 2</code> if you expect the Agent to use a tool before answering — with <code>maxSteps: 1</code> it is forced to answer on the first step and cannot call any other tool.</li>
<li><strong>Tool use is forced during a structured turn.</strong> To guarantee the Agent terminates with a structured answer (rather than replying in plain text), Think sets <code>toolChoice</code> for the turn. Do not override <code>toolChoice</code> from <code>beforeTurn</code> on a <code>step.prompt()</code> turn — doing so can prevent the Agent from calling the final-answer tool, which makes the prompt fail.</li>
<li><strong><code>think_final_answer</code> is reserved.</strong> Think injects an internal <code>think_final_answer</code> tool to carry the structured result. This name (and any <code>think_final_answer_*</code> variant) is reserved; its call and result are stripped from the persisted conversation, so the transcript and later turns do not see Think's internal plumbing.</li>
<li><strong>The model must support streaming tool calls.</strong> Think streams every turn, so <code>step.prompt()</code> works only with models that reliably emit a forced tool call while streaming. Strong tool-callers (for example OpenAI <code>gpt-4o-mini</code>, Anthropic <code>claude-haiku-4-5</code>, and Workers AI <code>@cf/moonshotai/kimi-k2.6</code>) are verified to work. Some models honor a forced <code>toolChoice</code> only on non-streaming requests and will reply in plain text and stop while streaming — for example Workers AI <code>@cf/meta/llama-3.3-70b-instruct-fp8-fast</code>. With those models the turn ends without a <code>think_final_answer</code> call and <code>step.prompt()</code> fails (<code>Model ended the turn without calling the think_final_answer tool</code>); use a model with working streaming tool calls instead.</li>
</ul>
<h2 id="how-it-runs">How it runs</h2>
<p>The call reads like a blocking step, but it does not hold a long-lived Durable Object RPC open.</p>
<ol>
<li><code>step.do(&quot;&lt;name&gt;:submit&quot;, ...)</code> creates or finds an idempotent Think submission.</li>
<li>Think runs the submitted turn through the normal submission queue.</li>
<li>When the submission reaches <code>completed</code>, <code>error</code>, <code>aborted</code>, or <code>skipped</code>, Think records a pending workflow notification.</li>
<li>Think drains the notification outbox with <code>sendWorkflowEvent()</code> and Durable Object alarms until delivery succeeds.</li>
<li><code>step.waitForEvent(&quot;&lt;name&gt;:wait&quot;, ...)</code> resumes the Workflow.</li>
<li><code>step.prompt()</code> validates the structured output or throws a typed error.</li>
</ol>
<p>The machine-readable output is carried in the pending notification and Workflow event payload. Think does not store a separate <code>output_json</code> column on the submission ledger, and clears the notification payload after delivery. After delivery, the Workflow owns the durable result.</p>
<h2 id="idempotency">Idempotency</h2>
<p>By default, <code>step.prompt()</code> infers the idempotency key from Workflow identity and step name:</p>
<pre><code class="language-text">think-workflow:&lt;workflowName&gt;:&lt;workflowId&gt;:&lt;stepName&gt;&#10;</code></pre>
<p>For loops, pass a string <code>key</code> to distinguish repeated uses of the same step name:</p>
<pre><code class="language-ts">await step.prompt(&quot;summarize-file&quot;, {&#10;	key: file.path,&#10;	prompt: `Summarize ${file.path}`,&#10;	output: summarySchema,&#10;});&#10;</code></pre>
<p>Prompt text is not part of the inferred key, but Think stores workflow metadata and a prompt/config fingerprint for diagnostics.</p>
<h2 id="timeouts">Timeouts</h2>
<p>Pass <code>timeout</code> to control how long the Workflow waits for the terminal event. If the wait times out, <code>step.prompt()</code> cancels the Think submission by default and throws <code>ThinkPromptTimeoutError</code>.</p>
<p>Set <code>cancelOnTimeout: false</code> when you intentionally want the Think submission to continue after the Workflow stops waiting.</p>
<h2 id="boundary-with-other-primitives">Boundary with other primitives</h2>
<p>Use <a href="/agents/harnesses/think/scheduled-tasks/"><code>getScheduledTasks()</code></a> for recurring prompt submissions or deterministic scheduled handlers:</p>
<pre><code class="language-ts">getScheduledTasks() {&#10;	return {&#10;		dailySummary: {&#10;			schedule: &quot;every day at 09:00&quot;,&#10;			timezone: &quot;UTC&quot;,&#10;			prompt: &quot;Generate the daily report.&quot;&#10;		},&#10;		dailyWorkflow: {&#10;			schedule: &quot;every day at 09:00&quot;,&#10;			timezone: &quot;UTC&quot;,&#10;			retry: { maxAttempts: 3 },&#10;			handler: async ({ idempotencyKey, scheduledFor, timezone }) =&gt; {&#10;				await this.env.REPORT_WORKFLOW.create({&#10;					id: idempotencyKey,&#10;					params: { scheduledFor, timezone }&#10;				});&#10;			}&#10;		}&#10;	};&#10;}&#10;</code></pre>
<p>Use <a href="/agents/harnesses/think/programmatic-submissions/"><code>submitMessages()</code></a> for durable one-off turns where the caller can inspect submission status later.</p>
<p>Use <a href="/agents/runtime/execution/durable-execution/#startfiber"><code>startFiber()</code></a> for app-owned idempotent Agent jobs that need recovery inside the Agent. Think's workflow notification delivery does not use fibers; it uses a private outbox because it needs to store an event until delivery succeeds.</p>
<p>Use Workflows when the process has multiple deterministic steps, long waits, or human approval.</p>
