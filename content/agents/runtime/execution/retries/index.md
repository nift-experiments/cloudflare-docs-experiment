<p>Retry failed operations with exponential backoff and jitter. The Agents SDK provides built-in retry support for scheduled tasks, queued tasks, and a general-purpose <code>this.retry()</code> method for your own code.</p>
<h2 id="overview">Overview</h2>
<p>Transient failures are common when calling external APIs, interacting with other services, or running background tasks. The retry system handles these automatically:</p>
<ul>
<li><strong>Exponential backoff</strong> — each retry waits longer than the last</li>
<li><strong>Jitter</strong> — randomized delays prevent thundering herd problems</li>
<li><strong>Configurable</strong> — tune attempts, delays, and caps per call site</li>
<li><strong>Built-in</strong> — schedule, queue, and workflow operations retry automatically</li>
</ul>
<h2 id="quick-start">Quick start</h2>
<p>Use <code>this.retry()</code> to retry any async operation:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2518.md")
</div>
<p>By default, <code>this.retry()</code> retries up to three times with jittered exponential backoff.</p>
<h2 id="this-retry"><code>this.retry()</code></h2>
<p>The <code>retry()</code> method is available on every <code>Agent</code> instance. It retries the provided function on any thrown error by default.</p>
<pre><code class="language-ts">async retry&lt;T&gt;(&#10;  fn: (attempt: number) =&gt; Promise&lt;T&gt;,&#10;  options?: RetryOptions &amp; {&#10;    shouldRetry?: (err: unknown, nextAttempt: number) =&gt; boolean;&#10;  }&#10;): Promise&lt;T&gt;&#10;</code></pre>
<p><strong>Parameters:</strong></p>
<ul>
<li><code>fn</code> — the async function to retry. Receives the current attempt number (1-indexed).</li>
<li><code>options</code> — optional retry configuration (refer to <a href="#retryoptions">RetryOptions</a> below). Options are validated eagerly — invalid values throw immediately.</li>
<li><code>options.shouldRetry</code> — optional predicate called with the thrown error and the next attempt number. Return <code>false</code> to stop retrying immediately. If not provided, all errors are retried.</li>
</ul>
<p><strong>Returns:</strong> the result of <code>fn</code> on success.</p>
<p><strong>Throws:</strong> the last error if all attempts fail or <code>shouldRetry</code> returns <code>false</code>.</p>
<h3 id="examples">Examples</h3>
<p><strong>Basic retry:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2519.md")
</div>
<p><strong>Custom retry options:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2520.md")
</div>
<p><strong>Using the attempt number:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2521.md")
</div>
<p><strong>Selective retry with <code>shouldRetry</code>:</strong></p>
<p>Use <code>shouldRetry</code> to stop retrying on specific errors. The predicate receives both the error and the next attempt number:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2522.md")
</div>
<h2 id="retries-in-schedules">Retries in schedules</h2>
<p>Pass retry options when creating a schedule:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2523.md")
</div>
<p>If the callback throws, it is retried according to the retry options. If all attempts fail, the error is logged and routed through <code>onError()</code>. The schedule is still removed (for one-time schedules) or rescheduled (for cron/interval) regardless of success or failure.</p>
<h2 id="retries-in-queues">Retries in queues</h2>
<p>Pass retry options when adding a task to the queue:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2524.md")
</div>
<p>If the callback throws, it is retried before the task is dequeued. After all attempts are exhausted, the task is dequeued and the error is logged.</p>
<h2 id="validation">Validation</h2>
<p>Retry options are validated eagerly when you call <code>this.retry()</code>, <code>queue()</code>, <code>schedule()</code>, or <code>scheduleEvery()</code>. Invalid options throw immediately instead of failing later at execution time:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2525.md")
</div>
<p>Validation resolves partial options against class-level or built-in defaults before checking cross-field constraints. This means <code>{ baseDelayMs: 5000 }</code> is caught immediately when the resolved <code>maxDelayMs</code> is 3000, rather than failing later at execution time.</p>
<h2 id="default-behavior">Default behavior</h2>
<p>Even without explicit retry options, scheduled and queued callbacks are retried with sensible defaults:</p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>maxAttempts</code></td>
<td>3</td>
</tr>
<tr>
<td><code>baseDelayMs</code></td>
<td>100</td>
</tr>
<tr>
<td><code>maxDelayMs</code></td>
<td>3000</td>
</tr>
</tbody>
</table>
<p>These defaults apply to <code>this.retry()</code>, <code>queue()</code>, <code>schedule()</code>, and <code>scheduleEvery()</code>. Per-call-site options override them.</p>
<h3 id="class-level-defaults">Class-level defaults</h3>
<p>Override the defaults for your entire agent via <code>static options</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2526.md")
</div>
<p>You only need to specify the fields you want to change — unset fields fall back to the built-in defaults:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2527.md")
</div>
<p>Class-level defaults are used as fallbacks when a call site does not specify retry options. Per-call-site options always take priority:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2528.md")
</div>
<p>To disable retries for a specific task, set <code>maxAttempts: 1</code>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2529.md")
</div>
<h2 id="retryoptions">RetryOptions</h2>
<pre><code class="language-ts">interface RetryOptions {&#10;	/** Maximum number of attempts (including the first). Must be an integer &gt;= 1. Default: 3 */&#10;	maxAttempts?: number;&#10;	/** Base delay in milliseconds for exponential backoff. Must be &gt; 0 and &lt;= maxDelayMs. Default: 100 */&#10;	baseDelayMs?: number;&#10;	/** Maximum delay cap in milliseconds. Must be &gt; 0. Default: 3000 */&#10;	maxDelayMs?: number;&#10;}&#10;</code></pre>
<p>The delay between retries uses <strong>full jitter exponential backoff</strong>:</p>
<pre><code>delay = random(0, min(2^attempt * baseDelayMs, maxDelayMs))&#10;</code></pre>
<p>This means early retries are fast (often under 200ms), and later retries back off to avoid overwhelming a failing service. The randomization (jitter) prevents multiple agents from retrying at the exact same moment.</p>
<h2 id="how-it-works">How it works</h2>
<h3 id="backoff-strategy">Backoff strategy</h3>
<p>The retry system uses the &quot;Full Jitter&quot; strategy from the <a href="https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/">AWS Architecture Blog</a>. Given 3 attempts with default settings:</p>
<table>
<thead>
<tr>
<th>Attempt</th>
<th>Upper Bound</th>
<th>Actual Delay</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>min(2^1 * 100, 3000) = 200ms</td>
<td>random(0, 200ms)</td>
</tr>
<tr>
<td>2</td>
<td>min(2^2 * 100, 3000) = 400ms</td>
<td>random(0, 400ms)</td>
</tr>
<tr>
<td>3</td>
<td>(no retry — final attempt)</td>
<td>—</td>
</tr>
</tbody>
</table>
<p>With <code>maxAttempts: 5</code> and <code>baseDelayMs: 500</code>:</p>
<table>
<thead>
<tr>
<th>Attempt</th>
<th>Upper Bound</th>
<th>Actual Delay</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>min(2 * 500, 3000) = 1000ms</td>
<td>random(0, 1000ms)</td>
</tr>
<tr>
<td>2</td>
<td>min(4 * 500, 3000) = 2000ms</td>
<td>random(0, 2000ms)</td>
</tr>
<tr>
<td>3</td>
<td>min(8 * 500, 3000) = 3000ms</td>
<td>random(0, 3000ms)</td>
</tr>
<tr>
<td>4</td>
<td>min(16 * 500, 3000) = 3000ms</td>
<td>random(0, 3000ms)</td>
</tr>
<tr>
<td>5</td>
<td>(no retry — final attempt)</td>
<td>—</td>
</tr>
</tbody>
</table>
<h3 id="mcp-server-retries">MCP server retries</h3>
<p>When adding an MCP server, you can configure retry options for connection and reconnection attempts:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2530.md")
</div>
<p>These options are persisted and used when:</p>
<ul>
<li>Restoring server connections after hibernation</li>
<li>Establishing connections after OAuth completion</li>
</ul>
<p>Default: 3 attempts, 500ms base delay, 5s max delay.</p>
<h2 id="patterns">Patterns</h2>
<h3 id="retry-with-logging">Retry with logging</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2531.md")
</div>
<h3 id="retry-with-fallback">Retry with fallback</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2532.md")
</div>
<h3 id="combining-retries-with-scheduling">Combining retries with scheduling</h3>
<p>For operations that might take a long time to recover (minutes or hours), combine <code>this.retry()</code> for immediate retries with <code>this.schedule()</code> for delayed retries:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2533.md")
</div>
<h2 id="limitations">Limitations</h2>
<ul>
<li><strong>No dead-letter queue.</strong> If a queued or scheduled task fails all retry attempts, it is removed. Implement your own persistence if you need to track failed tasks.</li>
<li><strong>Retry delays block the agent.</strong> During the backoff delay, the Durable Object is awake but idle. For short delays (under 3 seconds) this is fine. For longer recovery times, use <code>this.schedule()</code> instead.</li>
<li><strong>Queue retries are head-of-line blocking.</strong> Queue items are processed sequentially. If one item is being retried with long delays, it blocks all subsequent items. If you need independent retry behavior, use <code>this.retry()</code> inside the callback rather than per-task retry options on <code>queue()</code>.</li>
<li><strong>No circuit breaker.</strong> The retry system does not track failure rates across calls. If a service is persistently down, each task will exhaust its retry budget independently.</li>
<li><strong><code>shouldRetry</code> is only available on <code>this.retry()</code>.</strong> The <code>shouldRetry</code> predicate cannot be used with <code>schedule()</code> or <code>queue()</code> because functions cannot be serialized to the database. For scheduled/queued tasks, handle non-retryable errors inside the callback itself.</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-card nb-link-card" href="/agents/runtime/execution/schedule-tasks/"><h3 id="card-schedule-tasks-agents-runtime-execution-schedule-tasks">Schedule tasks</h3><p>Schedule tasks for future execution.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/execution/queue-tasks/"><h3 id="card-queue-tasks-agents-runtime-execution-queue-tasks">Queue tasks</h3><p>Background task queue for immediate processing.</p></a></p>
<p><a class="nb-card nb-link-card" href="/agents/runtime/execution/run-workflows/"><h3 id="card-run-workflows-agents-runtime-execution-run-workflows">Run Workflows</h3><p>Durable multi-step processing with automatic retries.</p></a></p>
