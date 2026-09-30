---
cp9:
  canonical: https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/
  description: Schedule delayed, date-based, cron, and interval tasks on Agents with persistent SQLite-backed execution.
  full_title: Schedule tasks · Cloudflare Agents docs
  head_html: <title>Schedule tasks · Cloudflare Agents docs</title><meta name="generator" content="Nift"><meta name="description" content="Schedule delayed, date-based, cron, and interval tasks on Agents with persistent SQLite-backed execution."><link rel="canonical" href="https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/index.md"><meta property="og:title" content="Schedule tasks · Cloudflare Agents docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Schedule delayed, date-based, cron, and interval tasks on Agents with persistent SQLite-backed execution."><meta property="og:url" content="https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Agents"><meta name="algolia_product_filter" content="Agents"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Agents"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/#page","headline":"Schedule tasks \u00b7 Cloudflare Agents docs","description":"Schedule delayed, date-based, cron, and interval tasks on Agents with persistent SQLite-backed execution.","url":"https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /agents/runtime/execution/schedule-tasks/
  schema: 1
---
<p>Schedule tasks to run in the future — whether that is seconds from now, at a specific date/time, or on a recurring cron schedule. Scheduled tasks survive agent restarts and are persisted to SQLite.</p>
<p>Scheduled tasks can do anything a request or message from a user can: make requests, query databases, send emails, read and write state. Scheduled tasks can invoke any regular method on your Agent.</p>
<h2 id="overview">Overview</h2>
<p>The scheduling system supports four modes:</p>
<table>
<thead>
<tr>
<th>Mode</th>
<th>Syntax</th>
<th>Use case</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Delayed</strong></td>
<td><code>this.schedule(60, ...)</code></td>
<td>Run in 60 seconds</td>
</tr>
<tr>
<td><strong>Scheduled</strong></td>
<td><code>this.schedule(new Date(...), ...)</code></td>
<td>Run at specific time</td>
</tr>
<tr>
<td><strong>Cron</strong></td>
<td><code>this.schedule(&quot;0 8 * * *&quot;, ...)</code></td>
<td>Run on recurring schedule</td>
</tr>
<tr>
<td><strong>Interval</strong></td>
<td><code>this.scheduleEvery(30, ...)</code></td>
<td>Run every 30 seconds</td>
</tr>
</tbody>
</table>
<p>Under the hood, scheduling uses <a href="/durable-objects/api/alarms/">Durable Object alarms</a> to wake the agent at the right time. Tasks are stored in a SQLite table and executed in order.</p>
<h2 id="quick-start">Quick start</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2461.md")
</div>
<h2 id="scheduling-modes">Scheduling modes</h2>
<h3 id="delayed-execution">Delayed execution</h3>
<p>Pass a number to schedule a task to run after a delay in <strong>seconds</strong>:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2462.md")
</div>
<p><strong>Use cases:</strong></p>
<ul>
<li>Debouncing rapid events</li>
<li>Delayed notifications (&quot;You left items in your cart&quot;)</li>
<li>Retry with backoff</li>
<li>Rate limiting</li>
</ul>
<h3 id="scheduled-execution">Scheduled execution</h3>
<p>Pass a <code>Date</code> object to schedule a task at a specific time:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2463.md")
</div>
<p><strong>Use cases:</strong></p>
<ul>
<li>Appointment reminders</li>
<li>Deadline notifications</li>
<li>Scheduled content publishing</li>
<li>Time-based triggers</li>
</ul>
<h3 id="recurring-cron">Recurring (cron)</h3>
<p>Pass a cron expression string for recurring schedules:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2464.md")
</div>
<p><strong>Cron syntax:</strong> <code>minute hour day month weekday</code></p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Values</th>
<th>Special characters</th>
</tr>
</thead>
<tbody>
<tr>
<td>Minute</td>
<td>0-59</td>
<td><code>*</code> <code>,</code> <code>-</code> <code>/</code></td>
</tr>
<tr>
<td>Hour</td>
<td>0-23</td>
<td><code>*</code> <code>,</code> <code>-</code> <code>/</code></td>
</tr>
<tr>
<td>Day of Month</td>
<td>1-31</td>
<td><code>*</code> <code>,</code> <code>-</code> <code>/</code></td>
</tr>
<tr>
<td>Month</td>
<td>1-12</td>
<td><code>*</code> <code>,</code> <code>-</code> <code>/</code></td>
</tr>
<tr>
<td>Day of Week</td>
<td>0-6 (0=Sunday)</td>
<td><code>*</code> <code>,</code> <code>-</code> <code>/</code></td>
</tr>
</tbody>
</table>
<p><strong>Common patterns:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2465.md")
</div>
<p><strong>Use cases:</strong></p>
<ul>
<li>Daily/weekly reports</li>
<li>Periodic cleanup jobs</li>
<li>Polling external services</li>
<li>Health checks</li>
<li>Subscription renewals</li>
</ul>
<p>Cron schedules are idempotent by default — calling <code>schedule()</code> with the same cron expression, callback, and payload multiple times returns the existing schedule instead of creating a duplicate. This makes cron schedules safe to set up in <code>onStart()</code>.</p>
<h3 id="interval">Interval</h3>
<p>Use <code>scheduleEvery()</code> to run a task at fixed intervals (in seconds). Unlike cron, intervals support sub-minute precision and arbitrary durations:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2466.md")
</div>
<p><strong>Key differences from cron:</strong></p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Cron</th>
<th>Interval</th>
</tr>
</thead>
<tbody>
<tr>
<td>Minimum granularity</td>
<td>1 minute</td>
<td>1 second</td>
</tr>
<tr>
<td>Arbitrary intervals</td>
<td>No (must fit cron pattern)</td>
<td>Yes</td>
</tr>
<tr>
<td>Fixed schedule</td>
<td>Yes (for example, &quot;every day at 8am&quot;)</td>
<td>No (relative to start)</td>
</tr>
<tr>
<td>Overlap prevention</td>
<td>No</td>
<td>Yes (built-in)</td>
</tr>
</tbody>
</table>
<p><strong>Idempotency:</strong></p>
<p><code>scheduleEvery()</code> is idempotent on the combination of callback name, interval, and payload — calling it multiple times with the same arguments does not create duplicate schedules. This makes it safe to call in <code>onStart()</code>, which runs on every Durable Object wake:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2467.md")
</div>
<p>A different interval or payload creates a new, independent schedule.</p>
<p><strong>Overlap prevention:</strong></p>
<p>If a callback takes longer than the interval, the next execution is skipped (not queued). This prevents runaway resource usage:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2468.md")
</div>
<p>When a skip occurs, you will see a warning in logs:</p>
<pre tabindex="0"><code class="language-txt">Skipping interval schedule abc123: previous execution still running&#10;</code></pre>
<p><strong>Error resilience:</strong></p>
<p>If the callback throws an error, the interval continues — only that execution fails:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2469.md")
</div>
<p><strong>Use cases:</strong></p>
<ul>
<li>Sub-minute polling (every 10, 30, 45 seconds)</li>
<li>Intervals that do not map to cron (every 90 seconds, every 7 minutes)</li>
<li>Rate-limited API polling with precise control</li>
<li>Real-time data synchronization</li>
</ul>
<h2 id="managing-scheduled-tasks">Managing scheduled tasks</h2>
<h3 id="get-a-schedule">Get a schedule</h3>
<p>Retrieve a scheduled task by its ID:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2470.md")
</div>
<h3 id="list-schedules">List schedules</h3>
<p>Query scheduled tasks with optional filters:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2471.md")
</div>
<h3 id="cancel-a-schedule">Cancel a schedule</h3>
<p>Remove a scheduled task before it executes:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2472.md")
</div>
<p><strong>Example: Cancellable reminders</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2473.md")
</div>
<h2 id="the-schedule-object">The Schedule object</h2>
<p>When you create or retrieve a schedule, you get a <code>Schedule</code> object:</p>
<pre tabindex="0"><code class="language-ts">type Schedule&lt;T&gt; = {&#10;	id: string; // Unique identifier&#10;	callback: string; // Method name to call&#10;	payload: T; // Data passed to the callback&#10;	time: number; // Unix timestamp (seconds) of next execution&#10;} &amp; (&#10;	| { type: &quot;scheduled&quot; } // One-time at specific date&#10;	| { type: &quot;delayed&quot;; delayInSeconds: number } // One-time after delay&#10;	| { type: &quot;cron&quot;; cron: string } // Recurring (cron expression)&#10;	| { type: &quot;interval&quot;; intervalSeconds: number } // Recurring (fixed interval)&#10;);&#10;</code></pre>
<p><strong>Example:</strong></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2474.md")
</div>
<h2 id="patterns">Patterns</h2>
<h3 id="rescheduling-from-callbacks">Rescheduling from callbacks</h3>
<p>For dynamic recurring schedules, schedule the next run from within the callback:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2475.md")
</div>
<h3 id="exponential-backoff-retry">Exponential backoff retry</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2476.md")
</div>
<h3 id="self-destructing-agents">Self-destructing agents</h3>
<p>You can safely call <code>this.destroy()</code> from within a scheduled callback:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2477.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2460.md")
</aside>
<h2 id="ai-assisted-scheduling">AI-assisted scheduling</h2>
<p>The SDK includes utilities for parsing natural language scheduling requests with AI.</p>
<h3 id="getscheduleprompt"><code>getSchedulePrompt()</code></h3>
<p>Returns a system prompt for parsing natural language into scheduling parameters:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2478.md")
</div>
<h3 id="scheduleschema"><code>scheduleSchema</code></h3>
<p>A Zod schema for validating parsed scheduling data. Uses a discriminated union on <code>when.type</code> so each variant only contains the fields it needs:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2479.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/2459.md")
</aside>
<h2 id="scheduling-vs-queue-vs-workflows">Scheduling vs Queue vs Workflows</h2>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Queue</th>
<th>Scheduling</th>
<th>Workflows</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>When</strong></td>
<td>Immediately (FIFO)</td>
<td>Future time</td>
<td>Future time</td>
</tr>
<tr>
<td><strong>Execution</strong></td>
<td>Sequential</td>
<td>At scheduled time</td>
<td>Multi-step</td>
</tr>
<tr>
<td><strong>Retries</strong></td>
<td>Built-in</td>
<td>Built-in</td>
<td>Automatic</td>
</tr>
<tr>
<td><strong>Persistence</strong></td>
<td>SQLite</td>
<td>SQLite</td>
<td>Workflow engine</td>
</tr>
<tr>
<td><strong>Recurring</strong></td>
<td>No</td>
<td>Yes (cron)</td>
<td>No (use scheduling)</td>
</tr>
<tr>
<td><strong>Complex logic</strong></td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td><strong>Human approval</strong></td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<p>Use Queue when:</p>
<ul>
<li>You need background processing without blocking the response</li>
<li>Tasks should run ASAP but do not need to block</li>
<li>Order matters (FIFO)</li>
</ul>
<p>Use Scheduling when:</p>
<ul>
<li>Tasks need to run at a specific time</li>
<li>You need recurring jobs (cron)</li>
<li>Delayed execution (debouncing, retries)</li>
</ul>
<p>Use Workflows when:</p>
<ul>
<li>Multi-step processes with dependencies</li>
<li>Automatic retries with backoff</li>
<li>Human-in-the-loop approvals</li>
<li>Long-running tasks (minutes to hours)</li>
</ul>
<h2 id="api-reference">API reference</h2>
<h3 id="schedule"><code>schedule()</code></h3>
<pre tabindex="0"><code class="language-ts">async schedule&lt;T&gt;(&#10;  when: Date | string | number,&#10;  callback: keyof this,&#10;  payload?: T,&#10;  options?: { retry?: RetryOptions; idempotent?: boolean }&#10;): Promise&lt;Schedule&lt;T&gt;&gt;&#10;</code></pre>
<p>Schedule a task for future execution.</p>
<p><strong>Parameters:</strong></p>
<ul>
<li><code>when</code> - When to execute: <code>number</code> (seconds delay), <code>Date</code> (specific time), or <code>string</code> (cron expression)</li>
<li><code>callback</code> - Name of the method to call</li>
<li><code>payload</code> - Data to pass to the callback (must be JSON-serializable)</li>
<li><code>options.retry</code> - Optional retry configuration. Refer to <a href="/agents/runtime/execution/retries/">Retries</a> for details</li>
<li><code>options.idempotent</code> - Deduplicate by callback + payload. Defaults to <code>true</code> for cron schedules, <code>false</code> for delayed and Date-based schedules</li>
</ul>
<p><strong>Returns:</strong> A <code>Schedule</code> object with the task details</p>
<p><strong>Idempotency:</strong></p>
<p>Cron schedules are idempotent by default — calling <code>schedule(&quot;0 * * * *&quot;, &quot;tick&quot;)</code> multiple times with the same callback, cron expression, and payload returns the existing schedule instead of creating a duplicate. Set <code>idempotent: false</code> to override this.</p>
<p>For delayed and Date-based schedules, set <code>idempotent: true</code> to opt in to the same dedup behavior (matched on callback + payload). This is especially useful when calling <code>schedule()</code> in <code>onStart()</code> to avoid accumulating duplicate rows across Durable Object restarts:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2480.md")
</div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/2458.md")
</aside>
<h3 id="scheduleevery"><code>scheduleEvery()</code></h3>
<pre tabindex="0"><code class="language-ts">async scheduleEvery&lt;T&gt;(&#10;  intervalSeconds: number,&#10;  callback: keyof this,&#10;  payload?: T,&#10;  options?: { retry?: RetryOptions }&#10;): Promise&lt;Schedule&lt;T&gt;&gt;&#10;</code></pre>
<p>Schedule a task to run repeatedly at a fixed interval.</p>
<p><strong>Parameters:</strong></p>
<ul>
<li><code>intervalSeconds</code> - Number of seconds between executions (must be greater than 0)</li>
<li><code>callback</code> - Name of the method to call</li>
<li><code>payload</code> - Data to pass to the callback (must be JSON-serializable)</li>
<li><code>options.retry</code> - Optional retry configuration. Refer to <a href="/agents/runtime/execution/retries/">Retries</a> for details.</li>
</ul>
<p><strong>Returns:</strong> A <code>Schedule</code> object with <code>type: &quot;interval&quot;</code></p>
<p><strong>Behavior:</strong></p>
<ul>
<li>First execution occurs after <code>intervalSeconds</code> (not immediately)</li>
<li>If callback is still running when next execution is due, it is skipped (overlap prevention)</li>
<li>If callback throws an error, the interval continues</li>
<li>Cancel with <code>cancelSchedule(id)</code> to stop the entire interval</li>
</ul>
<h3 id="getschedulebyid"><code>getScheduleById()</code></h3>
<pre tabindex="0"><code class="language-ts">async getScheduleById(id: string): Promise&lt;Schedule&lt;unknown&gt; | undefined&gt;&#10;</code></pre>
<p>Get a scheduled task by ID. Returns <code>undefined</code> if not found. This method works in both top-level agents and sub-agents.</p>
<h3 id="listschedules"><code>listSchedules()</code></h3>
<pre tabindex="0"><code class="language-ts">async listSchedules(criteria?: {&#10;  id?: string;&#10;  type?: &quot;scheduled&quot; | &quot;delayed&quot; | &quot;cron&quot; | &quot;interval&quot;;&#10;  timeRange?: { start?: Date; end?: Date };&#10;}): Promise&lt;Schedule&lt;unknown&gt;[]&gt;&#10;</code></pre>
<p>Get scheduled tasks matching the criteria. This method works in both top-level agents and sub-agents.</p>
<h3 id="getschedule"><code>getSchedule()</code></h3>
<pre tabindex="0"><code class="language-ts">getSchedule&lt;T&gt;(id: string): Schedule&lt;T&gt; | undefined&#10;</code></pre>
<p>Deprecated. Get a scheduled task by ID synchronously. This method only works in top-level agents. Use <code>await this.getScheduleById(id)</code> instead.</p>
<h3 id="getschedules"><code>getSchedules()</code></h3>
<pre tabindex="0"><code class="language-ts">getSchedules&lt;T&gt;(criteria?: {&#10;  id?: string;&#10;  type?: &quot;scheduled&quot; | &quot;delayed&quot; | &quot;cron&quot; | &quot;interval&quot;;&#10;  timeRange?: { start?: Date; end?: Date };&#10;}): Schedule&lt;T&gt;[]&#10;</code></pre>
<p>Deprecated. Get scheduled tasks matching the criteria synchronously. This method only works in top-level agents. Use <code>await this.listSchedules(criteria)</code> instead.</p>
<h3 id="cancelschedule"><code>cancelSchedule()</code></h3>
<pre tabindex="0"><code class="language-ts">async cancelSchedule(id: string): Promise&lt;boolean&gt;&#10;</code></pre>
<p>Cancel a scheduled task. Returns <code>true</code> if cancelled, <code>false</code> if not found.</p>
<h3 id="keepalive"><code>keepAlive()</code></h3>
<pre tabindex="0"><code class="language-ts">async keepAlive(): Promise&lt;() =&gt; void&gt;&#10;</code></pre>
<p>Prevent the Durable Object from being evicted due to inactivity by holding a 30-second alarm-backed heartbeat reference. Returns a disposer function that releases the heartbeat when called. The disposer is idempotent — calling it multiple times is safe.</p>
<p>Always call the disposer when the work is done — otherwise the heartbeat continues indefinitely.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2481.md")
</div>
<h3 id="keepalivewhile"><code>keepAliveWhile()</code></h3>
<pre tabindex="0"><code class="language-ts">async keepAliveWhile&lt;T&gt;(fn: () =&gt; Promise&lt;T&gt;): Promise&lt;T&gt;&#10;</code></pre>
<p>Run an async function while keeping the Durable Object alive. The heartbeat is automatically started before the function runs and stopped when it completes (whether it succeeds or throws). Returns the value returned by the function.</p>
<p>This is the recommended way to use <code>keepAlive</code> — it guarantees cleanup.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2482.md")
</div>
<h2 id="keeping-the-agent-alive">Keeping the agent alive</h2>
<p>Durable Objects are evicted after a period of inactivity (typically 70-140 seconds with no incoming requests, WebSocket messages, or alarms). During long-running operations — streaming LLM responses, waiting on external APIs, running multi-step computations — the agent can be evicted mid-flight.</p>
<p><code>keepAlive()</code> prevents this by holding an in-memory heartbeat reference and using the Durable Object alarm system directly. The alarm firing itself resets the inactivity timer.</p>
<ul>
<li>The heartbeat does not conflict with your own schedules because the alarm system multiplexes through a single alarm slot.</li>
<li>No schedule rows are created, and the heartbeat is invisible to <code>listSchedules()</code>.</li>
<li>Multiple concurrent <code>keepAlive()</code> calls use a reference count, so one disposer does not release another caller's heartbeat.</li>
<li>Inside sub-agents, <code>keepAlive()</code> delegates that heartbeat reference to the top-level parent because facets do not have independent alarm slots.</li>
</ul>
<h3 id="multiple-concurrent-callers">Multiple concurrent callers</h3>
<p>Each <code>keepAlive()</code> call returns an independent disposer:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/2483.md")
</div>
<h3 id="aichatagent">AIChatAgent</h3>
<p><code>AIChatAgent</code> automatically calls <code>keepAlive()</code> during streaming responses. You do not need to add it yourself when using <code>AIChatAgent</code> — every LLM stream is protected from idle eviction by default.</p>
<h3 id="when-to-use-keepalive">When to use keepAlive</h3>
<table>
<thead>
<tr>
<th>Scenario</th>
<th>Use keepAlive?</th>
</tr>
</thead>
<tbody>
<tr>
<td>Streaming LLM responses via <code>AIChatAgent</code></td>
<td>No — already built in</td>
</tr>
<tr>
<td>Long-running computation in a custom Agent</td>
<td>Yes</td>
</tr>
<tr>
<td>Waiting on a slow external API call</td>
<td>Yes</td>
</tr>
<tr>
<td>Multi-step tool execution</td>
<td>Yes</td>
</tr>
<tr>
<td>Short request-response handlers</td>
<td>No — not needed</td>
</tr>
<tr>
<td>Background work via scheduling or workflows</td>
<td>No — alarms already keep the DO active</td>
</tr>
</tbody>
</table>
<h2 id="limits">Limits</h2>
<ul>
<li><strong>Maximum tasks:</strong> Limited by SQLite storage (each task is a row). Practical limit is tens of thousands per agent.</li>
<li><strong>Task size:</strong> Each task (including payload) can be up to 2MB.</li>
<li><strong>Minimum delay:</strong> 0 seconds (runs on next alarm tick)</li>
<li><strong>Cron precision:</strong> Minute-level (not seconds)</li>
<li><strong>Interval precision:</strong> Second-level</li>
<li><strong>Cron jobs:</strong> After execution, automatically rescheduled for the next occurrence</li>
<li><strong>Interval jobs:</strong> After execution, rescheduled for <code>now + intervalSeconds</code>; skipped if still running</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<div class="nb-card nb-link-card"><h3 id="card-push-notifications-agents-communication-channels-webhooks-push-notifications"><a href="/agents/communication-channels/webhooks/push-notifications/">Push notifications</a></h3><p>Send browser push notifications using scheduling and web-push.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-queue-tasks-agents-runtime-execution-queue-tasks"><a href="/agents/runtime/execution/queue-tasks/">Queue tasks</a></h3><p>Immediate background task processing.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-run-workflows-agents-runtime-execution-run-workflows"><a href="/agents/runtime/execution/run-workflows/">Run Workflows</a></h3><p>Durable multi-step background processing.</p></div>
<div class="nb-card nb-link-card"><h3 id="card-agents-api-agents-runtime-agents-api"><a href="/agents/runtime/agents-api/">Agents API</a></h3><p>Complete API reference for the Agents SDK.</p></div>
