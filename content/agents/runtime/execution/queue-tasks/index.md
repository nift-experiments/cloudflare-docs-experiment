<p>The Agents SDK provides a built-in queue system that allows you to schedule tasks for asynchronous execution. This is useful for background processing, delayed operations, and managing workloads that do not need immediate execution.</p>
<h2 id="overview">Overview</h2>
<p>The queue system is built into the base <code>Agent</code> class. Tasks are stored in a SQLite table and processed automatically in FIFO (First In, First Out) order.</p>
<h2 id="queueitem-type"><code>QueueItem</code> type</h2>
<pre><code class="language-ts">type QueueItem&lt;T&gt; = {&#10;	id: string; // Unique identifier for the queued task&#10;	payload: T; // Data to pass to the callback function&#10;	callback: keyof Agent; // Name of the method to call&#10;	created_at: number; // Timestamp when the task was created&#10;	retry?: RetryOptions; // Retry options for this task&#10;};&#10;</code></pre>
<h2 id="core-methods">Core methods</h2>
<h3 id="queue"><code>queue()</code></h3>
<p>Adds a task to the queue for future execution.</p>
<pre><code class="language-ts">async queue&lt;T&gt;(&#10;  callback: keyof this,&#10;  payload: T,&#10;  options?: { retry?: RetryOptions }&#10;): Promise&lt;string&gt;&#10;</code></pre>
<p><strong>Parameters:</strong></p>
<ul>
<li><code>callback</code> - The name of the method to call when processing the task</li>
<li><code>payload</code> - Data to pass to the callback method</li>
<li><code>options</code> - Optional configuration:
<ul>
<li><code>retry</code> - Retry options for the callback execution. If the callback throws, it is retried with exponential backoff. Refer to <a href="/agents/runtime/execution/retries/">Retries</a> for details on <code>RetryOptions</code></li>
</ul>
</li>
</ul>
<p><strong>Returns:</strong> The unique ID of the queued task</p>
<p><strong>Example:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2534.md")
</div>
<h3 id="dequeue"><code>dequeue()</code></h3>
<p>Removes a specific task from the queue by ID. This method is synchronous.</p>
<pre><code class="language-ts">dequeue(id: string): void&#10;</code></pre>
<p><strong>Parameters:</strong></p>
<ul>
<li><code>id</code> - The ID of the task to remove</li>
</ul>
<p><strong>Example:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2535.md")
</div>
<h3 id="dequeueall"><code>dequeueAll()</code></h3>
<p>Removes all tasks from the queue. This method is synchronous.</p>
<pre><code class="language-ts">dequeueAll(): void&#10;</code></pre>
<p><strong>Example:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2536.md")
</div>
<h3 id="dequeueallbycallback"><code>dequeueAllByCallback()</code></h3>
<p>Removes all tasks that match a specific callback method. This method is synchronous.</p>
<pre><code class="language-ts">dequeueAllByCallback(callback: string): void&#10;</code></pre>
<p><strong>Parameters:</strong></p>
<ul>
<li><code>callback</code> - Name of the callback method</li>
</ul>
<p><strong>Example:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2537.md")
</div>
<h3 id="getqueue"><code>getQueue()</code></h3>
<p>Retrieves a specific queued task by ID. This method is synchronous.</p>
<pre><code class="language-ts">getQueue&lt;T&gt;(id: string): QueueItem&lt;T&gt; | undefined&#10;</code></pre>
<p><strong>Parameters:</strong></p>
<ul>
<li><code>id</code> - The ID of the task to retrieve</li>
</ul>
<p><strong>Returns:</strong> The <code>QueueItem</code> with parsed payload or <code>undefined</code> if not found</p>
<p>The payload is automatically parsed from JSON before being returned.</p>
<p><strong>Example:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2538.md")
</div>
<h3 id="getqueues"><code>getQueues()</code></h3>
<p>Retrieves all queued tasks that match a specific key-value pair in their payload. This method is synchronous.</p>
<pre><code class="language-ts">getQueues&lt;T&gt;(key: string, value: string): QueueItem&lt;T&gt;[]&#10;</code></pre>
<p><strong>Parameters:</strong></p>
<ul>
<li><code>key</code> - The key to filter by in the payload</li>
<li><code>value</code> - The value to match</li>
</ul>
<p><strong>Returns:</strong> Array of matching <code>QueueItem</code> objects</p>
<p>This method fetches all queue items and filters them in memory by parsing each payload and checking if the specified key matches the value.</p>
<p><strong>Example:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2539.md")
</div>
<h2 id="how-queue-processing-works">How queue processing works</h2>
<ol>
<li><strong>Validation</strong>: When calling <code>queue()</code>, the method validates that the callback exists as a function on the agent.</li>
<li><strong>Automatic processing</strong>: After queuing, the system automatically attempts to flush the queue.</li>
<li><strong>FIFO order</strong>: Tasks are processed in the order they were created (<code>created_at</code> timestamp).</li>
<li><strong>Context preservation</strong>: Each queued task runs with the same agent context (connection, request, email).</li>
<li><strong>Automatic dequeue</strong>: Successfully executed tasks are automatically removed from the queue.</li>
<li><strong>Error handling</strong>: If a callback method does not exist at execution time, an error is logged and the task is skipped.</li>
<li><strong>Persistence</strong>: Tasks are stored in the <code>cf_agents_queues</code> SQL table and survive agent restarts.</li>
</ol>
<h2 id="queue-callback-methods">Queue callback methods</h2>
<p>When defining callback methods for queued tasks, they must follow this signature:</p>
<pre><code class="language-ts">async callbackMethod(payload: unknown, queueItem: QueueItem): Promise&lt;void&gt;&#10;</code></pre>
<p><strong>Example:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2540.md")
</div>
<h2 id="use-cases">Use cases</h2>
<h3 id="background-processing">Background processing</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2541.md")
</div>
<h3 id="batch-operations">Batch operations</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2542.md")
</div>
<h2 id="error-handling">Error handling</h2>
<p>Use the built-in <code>retry</code> option instead of manual re-queue logic. When a callback throws, the task is automatically retried with exponential backoff:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2543.md")
</div>
<p>If no <code>retry</code> option is provided, the class-level defaults from <code>static options.retry</code> are used (3 attempts, 100ms base delay, 3s max delay). Refer to <a href="/agents/runtime/execution/retries/">Retries</a> for full details.</p>
<h2 id="best-practices">Best practices</h2>
<ol>
<li><strong>Keep payloads small</strong>: Payloads are JSON-serialized and stored in the database.</li>
<li><strong>Idempotent operations</strong>: Design callback methods to be safe to retry.</li>
<li><strong>Error handling</strong>: Include proper error handling in callback methods.</li>
<li><strong>Monitoring</strong>: Use logging to track queue processing.</li>
<li><strong>Cleanup</strong>: Regularly clean up completed or failed tasks if needed.</li>
</ol>
<h2 id="integration-with-other-features">Integration with other features</h2>
<p>The queue system works with other Agent SDK features:</p>
<ul>
<li><strong>State management</strong>: Access agent state within queued callbacks.</li>
<li><strong>Scheduling</strong>: Combine with <a href="/agents/runtime/execution/schedule-tasks/"><code>schedule()</code></a> for time-based queue processing.</li>
<li><strong>Context</strong>: Queued tasks maintain the original request context.</li>
<li><strong>Database</strong>: Uses the same database as other agent data.</li>
</ul>
<h2 id="limitations">Limitations</h2>
<ul>
<li>Tasks are processed sequentially, not in parallel.</li>
<li>No priority system (FIFO only).</li>
<li>Queue processing happens during agent execution, not as separate background jobs.</li>
</ul>
<h2 id="queue-vs-schedule">Queue vs Schedule</h2>
<p>Use <strong>queue</strong> when you want tasks to execute as soon as possible in order. Use <a href="/agents/runtime/execution/schedule-tasks/"><strong>schedule</strong></a> when you need tasks to run at specific times or on a recurring basis.</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Queue</th>
<th>Schedule</th>
</tr>
</thead>
<tbody>
<tr>
<td>Execution timing</td>
<td>Immediate (FIFO)</td>
<td>Specific time or cron</td>
</tr>
<tr>
<td>Use case</td>
<td>Background processing</td>
<td>Delayed or recurring tasks</td>
</tr>
<tr>
<td>Storage</td>
<td><code>cf_agents_queues</code> table</td>
<td><code>cf_agents_schedules</code> table</td>
</tr>
</tbody>
</table>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/agents/runtime/agents-api/"><h3 id="card-agents-api-agents-runtime-agents-api">Agents API</h3><p>Complete API reference for the Agents SDK.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/execution/schedule-tasks/"><h3 id="card-schedule-tasks-agents-runtime-execution-schedule-tasks">Schedule tasks</h3><p>Time-based execution with cron and delays.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/execution/run-workflows/"><h3 id="card-run-workflows-agents-runtime-execution-run-workflows">Run Workflows</h3><p>Durable multi-step background processing.</p></a></p>
