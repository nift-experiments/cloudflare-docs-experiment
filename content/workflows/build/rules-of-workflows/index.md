<p>A Workflow contains one or more steps. Each step is a self-contained, individually retryable component of a Workflow. Steps may emit (optional) state that allows a Workflow to persist and continue from that step, even if a Workflow fails due to a network or infrastructure issue.</p>
<p>This is a small guidebook on how to build more resilient and correct Workflows.</p>
<h3 id="ensure-api-binding-calls-are-idempotent">Ensure API/Binding calls are idempotent</h3>
<p>Because a step might be retried multiple times, your steps should (ideally) be idempotent. For context, idempotency is a logical property where the operation (in this case a step),
can be applied multiple times without changing the result beyond the initial application.</p>
<p>As an example, let us assume you have a Workflow that charges your customers, and you really do not want to charge them twice by accident. Before charging them, you should
check if they were already charged:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17562.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17561.md")
</aside>
<h3 id="make-your-steps-granular">Make your steps granular</h3>
<p>Steps should be as self-contained as possible. This allows your own logic to be more durable in case of failures in third-party APIs, network errors, and so on.</p>
<p>You can also think of it as a transaction, or a unit of work.</p>
<ul>
<li>✅ Minimize the number of API/binding calls per step (unless you need multiple calls to prove idempotency).</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17563.md")
</div>
<p>Otherwise, your entire Workflow might not be as durable as you might think, and you may encounter some undefined behaviour. You can avoid them by following the rules below:</p>
<ul>
<li>🔴 Do not encapsulate your entire logic in one single step.</li>
<li>🔴 Do not call separate services in the same step (unless you need it to prove idempotency).</li>
<li>🔴 Do not make too many service calls in the same step (unless you need it to prove idempotency).</li>
<li>🔴 Do not do too much CPU-intensive work inside a single step - sometimes the engine may have to restart, and it will start over from the beginning of that step.</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17564.md")
</div>
<h3 id="do-not-rely-on-state-outside-of-a-step">Do not rely on state outside of a step</h3>
<p>Workflows may hibernate and lose all in-memory state. This will happen when engine detects that there is no pending work and can hibernate until it needs to wake-up (because of a sleep, retry, or event).</p>
<p>This means that you should not store state outside of a step:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17565.md")
</div>
<p>Instead, you should build top-level state exclusively comprised of <code>step.do</code> returns:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17566.md")
</div>
<h3 id="avoid-doing-side-effects-outside-of-a-step-do">Avoid doing side effects outside of a <code>step.do</code></h3>
<p>It is not recommended to write code with any side effects outside of steps, unless you would like it to be repeated, because the Workflow engine may restart while an instance is running. If the engine restarts, the step logic will be preserved, but logic outside of the steps may be duplicated.</p>
<p>For example, a <code>console.log()</code> outside of workflow steps may cause the logs to print twice when the engine restarts.</p>
<p>However, logic involving non-serializable resources, like a database connection, should be executed outside of steps. Operations outside of a <code>step.do</code> might be repeated more than once, due to the nature of the Workflows' instance lifecycle.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17560.md")
</aside>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17567.md")
</div>
<h3 id="do-not-mutate-your-incoming-events">Do not mutate your incoming events</h3>
<p>The <code>event</code> passed to your Workflow's <code>run</code> method is immutable: changes you make to the event are not persisted across steps and/or Workflow restarts.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17568.md")
</div>
<h3 id="name-steps-deterministically">Name steps deterministically</h3>
<p>Steps should be named deterministically (that is, not using the current date/time, randomness, etc). This ensures that their state is cached, and prevents the step from being rerun unnecessarily. Step names act as the &quot;cache key&quot; in your Workflow.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17569.md")
</div>
<h3 id="take-care-with-promise-race-and-promise-any">Take care with <code>Promise.race()</code> and <code>Promise.any()</code></h3>
<p>Workflows allows the usage steps within the <code>Promise.race()</code> or <code>Promise.any()</code> methods as a way to achieve concurrent steps execution. However, some considerations must be taken.</p>
<p>Due to the nature of Workflows' instance lifecycle, and given that a step inside a Promise will run until it finishes, the step that is returned during the first passage may not be the actual cached step, as <a href="#name-steps-deterministically">steps are cached by their names</a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17570.md")
</div>
<p>To ensure consistency, we suggest to surround the <code>Promise.race()</code> or <code>Promise.any()</code> within a <code>step.do()</code>, as this will ensure caching consistency across multiple passages.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17571.md")
</div>
<h3 id="instance-ids-are-unique">Instance IDs are unique</h3>
<p>Workflow <a href="/workflows/build/workers-api/#workflowinstance">instance IDs</a> are unique per Workflow. The ID is the unique identifier that associates logs, metrics, state and status of a run to a specific instance, even after completion. Allowing ID re-use would make it hard to understand if a Workflow instance ID referred to an instance that run yesterday, last week or today.</p>
<p>It would also present a problem if you wanted to run multiple different Workflow instances with different <a href="/workflows/build/events-and-parameters/">input parameters</a> for the same user ID, as you would immediately need to determine a new ID mapping.</p>
<p>If you need to associate multiple instances with a specific user, merchant or other &quot;customer&quot; ID in your system, consider using a composite ID or using randomly generated IDs and storing the mapping in a database like <a href="/d1/">D1</a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17572.md")
</div>
<h3 id="await-your-steps"><code>await</code> your steps</h3>
<p>When calling <code>step.do</code> or <code>step.sleep</code>, use <code>await</code> to avoid introducing bugs and race conditions into your Workflow code.</p>
<p>If you don't call <code>await step.do</code> or <code>await step.sleep</code>, you create a dangling Promise. This occurs when a Promise is created but not properly <code>await</code>ed, leading to potential bugs and race conditions.</p>
<p>This happens when you do not use the <code>await</code> keyword or fail to chain <code>.then()</code> methods to handle the result of a Promise. For example, calling <code>fetch(GITHUB_URL)</code> without awaiting its response will cause subsequent code to execute immediately, regardless of whether the fetch completed. This can cause issues like premature logging, exceptions being swallowed (and not terminating the Workflow), and lost return values (state).</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17573.md")
</div>
<h3 id="use-conditional-logic-carefully">Use conditional logic carefully</h3>
<p>You can use <code>if</code> statements, loops, and other control flow outside of steps. However, conditions must be based on <strong>deterministic values</strong> — either values from <code>event.payload</code> or return values from previous steps. Non-deterministic conditions (such as <code>Math.random()</code> or <code>Date.now()</code>) outside of steps can cause unexpected behavior if the Workflow restarts.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17574.md")
</div>
<h3 id="batch-multiple-workflow-invocations">Batch multiple Workflow invocations</h3>
<p>When creating multiple Workflow instances, use the <a href="/workflows/build/workers-api/#createBatch"><code>createBatch</code></a> method to batch the invocations together. This allows you to create multiple Workflow instances in a single request, which will reduce the number of requests made to the Workflows API. However, each individual instance in the batch will still count towards the <a href="/workflows/reference/limits/">creation rate limit</a>. Unlike <code>create</code>, <code>createBatch</code> is idempotent: if an existing instance with the same ID is still within its <a href="/workflows/reference/limits/">retention limit</a>, it will be skipped and excluded from the returned array.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17575.md")
</div>
<h3 id="limit-timeouts-to-30-minutes-or-less">Limit timeouts to 30 minutes or less</h3>
<p>When setting a <a href="/workflows/build/workers-api/#workflowstep">WorkflowStep timeout</a>, ensure that its duration is 30 minutes or less. If your use case requires a timeout greater than 30 minutes, consider using <code>step.waitForEvent()</code> instead.</p>
<h3 id="keep-non-stream-step-return-values-under-1-mib">Keep non-stream step return values under 1 MiB</h3>
<p>A non-stream <code>step.do()</code> return value can persist up to 1 MiB (2^20 bytes). If your step returns structured data exceeding this limit, the step will fail. This is a common issue when fetching large API responses or processing large files.</p>
<p>In JavaScript Workflows, <code>ReadableStream&lt;Uint8Array&gt;</code> is a supported serializable return type for larger binary output. When persisting this kind of output, you should:</p>
<ul>
<li>Return a new stream from the step callback.</li>
<li>Keep individual chunks under 16 MB.</li>
<li>Do not return a locked stream or a stream that has already been read.</li>
<li>Rely only on streams returned from steps.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17559.md")
</aside>
<p>Note that streamed outputs are still considered part of the Workflow instance storage limit.</p>
<p>If these storage limits still do not work for you, consider storing your step outputs externally (for example, in <a href="/r2">R2</a>) and saving a reference to it.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17576.md")
</div>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers/best-practices/workers-best-practices/">Workers Best Practices</a>: code patterns for request handling, observability, and security that apply to the Workers triggering your Workflows.</li>
<li><a href="/durable-objects/best-practices/rules-of-durable-objects/">Rules of Durable Objects</a>: best practices for stateful, coordinated applications — useful when combining Durable Objects with Workflows.</li>
</ul>
