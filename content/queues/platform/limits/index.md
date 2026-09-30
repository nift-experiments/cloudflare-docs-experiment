<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11241.md")
</aside>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Queues</td>
<td>10,000 per account</td>
</tr>
<tr>
<td>Message size</td>
<td>128 KB <sup>1</sup></td>
</tr>
<tr>
<td>Message retries</td>
<td>100</td>
</tr>
<tr>
<td>Maximum consumer batch size</td>
<td>100 messages</td>
</tr>
<tr>
<td>Maximum messages per <code>sendBatch</code> call</td>
<td>100 (or 256KB in total)</td>
</tr>
<tr>
<td>Maximum Batch wait time</td>
<td>60 seconds</td>
</tr>
<tr>
<td>Per-queue message throughput</td>
<td>5,000 messages per second <sup>2</sup></td>
</tr>
<tr>
<td>Message retention period <sup>3</sup></td>
<td><a href="/queues/configuration/configure-queues/#queue-configuration">Configurable up to 14 days</a>.</td>
</tr>
<tr>
<td>Per-queue backlog size <sup>4</sup></td>
<td>25GB</td>
</tr>
<tr>
<td>Concurrent consumer invocations</td>
<td>250 <sup>push-based only</sup></td>
</tr>
<tr>
<td>Consumer duration (wall clock time)</td>
<td>15 minutes <sup>5</sup></td>
</tr>
<tr>
<td><a href="/workers/platform/limits/#cpu-time">Consumer CPU time</a></td>
<td><a href="/queues/platform/limits/#increasing-queue-consumer-worker-cpu-limits">Configurable to 5 minutes</a></td>
</tr>
<tr>
<td><code>visibilityTimeout</code> (pull-based queues)</td>
<td>12 hours</td>
</tr>
<tr>
<td><code>delaySeconds</code> (when sending or retrying)</td>
<td>24 hours</td>
</tr>
</tbody>
</table>
<p><sup>1</sup> 1 KB is measured as 1000 bytes. Messages can include up to ~100 bytes of internal metadata that counts towards total message limits.</p>
<p><sup>2</sup> Exceeding the maximum message throughput will cause the <code>send()</code> and <code>sendBatch()</code> methods to throw an exception with a <code>Too Many Requests</code> error until your producer falls below the limit.</p>
<p><sup>3</sup> Messages in a queue that reach the maximum message retention are deleted from the queue. Queues does not delete messages in the same queue that have not reached this limit.</p>
<p><sup>4</sup> Individual queues that reach this limit will receive a <code>Storage Limit Exceeded</code> error when calling <code>send()</code> or <code>sendBatch()</code> on the queue.</p>
<p><sup>5</sup> Refer to <a href="/workers/platform/limits/#cpu-time">Workers limits</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="need-a-higher-limit">Need a higher limit?</h3>
@markup("md", "content/.markup/bodies/11240.md")
</aside>
<h3 id="increasing-queue-consumer-worker-cpu-limits">Increasing Queue Consumer Worker CPU Limits</h3>
[Queue consumer Workers](/queues/reference/how-queues-works/#consumers) are Worker scripts, and share the same [per invocation CPU limits](/workers/platform/limits/#account-plan-limits) as any Workers do. Note that CPU time is active processing time: not time spent waiting on network requests, storage calls, or other general I/O.
<p>By default, the maximum CPU time per consumer Worker invocation is set to 30 seconds, but can be increased by setting <code>limits.cpu_ms</code> in your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11242.md")
</div>
<p>To learn more about CPU time and limits, <a href="/workers/platform/limits/#cpu-time">review the Workers documentation</a>.</p>
<h2 id="wall-time-limits-by-invocation-type">Wall time limits by invocation type</h2>
<p>Wall time (also called wall-clock time) is the total elapsed time from the start to end of an invocation, including time spent waiting on network requests, I/O, and other asynchronous operations. This is distinct from <a href="/workers/platform/limits/#cpu-time">CPU time</a>, which only measures time the CPU spends actively executing your code.</p>
<p>The following table summarizes the wall time limits for different types of Worker invocations across the developer platform:</p>
<table>
<thead>
<tr>
<th>Invocation type</th>
<th>Wall time limit</th>
<th>Details</th>
</tr>
</thead>
<tbody>
<tr>
<td>Incoming HTTP request</td>
<td>Unlimited</td>
<td>No hard limit while the client remains connected. A Worker that is still streaming a response body remains active. <a href="/workers/runtime-apis/context/#waituntil"><code>waitUntil()</code></a> extends execution for up to 30 seconds after the response or disconnect.</td>
</tr>
<tr>
<td><a href="/workers/configuration/cron-triggers/">Cron Triggers</a></td>
<td>15 minutes</td>
<td>Scheduled Workers have a maximum wall time of 15 minutes per invocation.</td>
</tr>
<tr>
<td><a href="/queues/configuration/javascript-apis/#consumer">Queue consumers</a></td>
<td>15 minutes</td>
<td>Each consumer invocation has a maximum wall time of 15 minutes.</td>
</tr>
<tr>
<td><a href="/durable-objects/api/alarms/">Durable Object alarm handlers</a></td>
<td>15 minutes</td>
<td>Alarm handler invocations have a maximum wall time of 15 minutes.</td>
</tr>
<tr>
<td><a href="/durable-objects/">Durable Objects</a> (RPC / HTTP)</td>
<td>Unlimited</td>
<td>No hard limit while the caller stays connected to the Durable Object. Durable Objects remain active while a request, RPC call, response stream, WebSocket, or pending I/O is in flight.</td>
</tr>
<tr>
<td><a href="/workflows/">Workflows</a> (per step)</td>
<td>Unlimited</td>
<td>Each step can run for an unlimited wall time. Individual steps are subject to the configured <a href="/workers/platform/limits/#cpu-time">CPU time limit</a>.</td>
</tr>
</tbody>
</table>
