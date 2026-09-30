<p>Functions metrics can help you diagnose issues and understand your workloads by showing performance and usage data for your Functions.</p>
<h2 id="functions-metrics">Functions metrics</h2>
<p>Functions metrics aggregate request data for an individual Pages project. To view your Functions metrics:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select your Pages project.
3. In your Pages project, select **Functions Metrics**.
<p>There are three metrics that can help you understand the health of your Function:</p>
<ol>
<li>Requests success.</li>
<li>Requests errors.</li>
<li>Invocation Statuses.</li>
</ol>
<h3 id="requests">Requests</h3>
<p>In <strong>Functions metrics</strong>, you can see historical request counts broken down into total requests, successful requests and errored requests. Information on subrequests is available by selecting <strong>Subrequests</strong>.</p>
<ul>
<li><strong>Total</strong>: All incoming requests registered by a Function. Requests blocked by <a href="https://www.cloudflare.com/waf/">Web Application Firewall (WAF)</a> or other security features will not count.</li>
<li><strong>Success</strong>: Requests that returned a <code>Success</code> or <code>Client Disconnected</code> <a href="#invocation-statuses">invocation status</a>.</li>
<li><strong>Errors</strong>: Requests that returned a <code>Script Threw Exception</code>, <code>Exceeded Resources</code>, or <code>Internal Error</code> <a href="#invocation-statuses">invocation status</a></li>
<li><strong>Subrequests</strong>: Requests triggered by calling <code>fetch</code> from within a Function. When your Function fetches a static asset, it will count as a subrequest. A subrequest that throws an uncaught error will not be counted.</li>
</ul>
<p>Request traffic data may display a drop off near the last few minutes displayed in the graph for time ranges less than six hours. This does not reflect a drop in traffic, but a slight delay in aggregation and metrics delivery.</p>
<h3 id="invocation-statuses">Invocation statuses</h3>
<p>Function invocation statuses indicate whether a Function executed successfully or failed to generate a response in the Workers runtime. Invocation statuses differ from HTTP status codes. In some cases, a Function invocation succeeds but does not generate a successful HTTP status because of another error encountered outside of the Workers runtime. Some invocation statuses result in a Workers error code being returned to the client.</p>
<table>
<thead>
<tr>
<th>Invocation status</th>
<th>Definition</th>
<th>Workers error code</th>
<th>Graph QL field</th>
</tr>
</thead>
<tbody>
<tr>
<td>Success</td>
<td>Worker script executed successfully</td>
<td></td>
<td>success</td>
</tr>
<tr>
<td>Client disconnected</td>
<td>HTTP client disconnected before the request completed</td>
<td></td>
<td>clientDisconnected</td>
</tr>
<tr>
<td>Script threw exception</td>
<td>Worker script threw an unhandled JavaScript exception</td>
<td>1101</td>
<td>scriptThrewException</td>
</tr>
<tr>
<td>Exceeded resources^1</td>
<td>Worker script exceeded runtime limits</td>
<td>1102, 1027</td>
<td>exceededResources</td>
</tr>
<tr>
<td>Internal error^2</td>
<td>Workers runtime encountered an error</td>
<td></td>
<td>internalError</td>
</tr>
</tbody>
</table>
<ol>
<li>The Exceeded Resources status may appear when the Worker exceeds a <a href="/workers/platform/limits/#request-and-response-limits">runtime limit</a>. The most common cause is excessive CPU time, but is also caused by a script exceeding startup time or free tier limits.</li>
<li>The Internal Error status may appear when the Workers runtime fails to process a request due to an internal failure in our system. These errors are not caused by any issue with the Function code nor any resource limit. While requests with Internal Error status are rare, some may appear during normal operation. These requests are not counted towards usage for billing purposes. If you notice an elevated rate of requests with Internal Error status, review <a href="http://www.cloudflarestatus.com">www.cloudflarestatus.com</a>.</li>
</ol>
<p>To further investigate exceptions, refer to <a href="/pages/functions/debugging-and-logging">Debugging and Logging</a></p>
<h3 id="cpu-time-per-execution">CPU time per execution</h3>
<p>The CPU Time per execution chart shows historical CPU time data broken down into relevant quantiles using <a href="https://en.wikipedia.org/wiki/Reservoir_sampling">reservoir sampling</a>. Learn more about <a href="https://www.statisticshowto.com/quantile-definition-find-easy-steps/">interpreting quantiles</a>.</p>
<p>In some cases, higher quantiles may appear to exceed <a href="/workers/platform/limits/#cpu-time">CPU time limits</a> without generating invocation errors because of a mechanism in the Workers runtime that allows rollover CPU time for requests below the CPU limit.</p>
<h3 id="duration-per-execution">Duration per execution</h3>
<p>The <strong>Duration</strong> chart underneath <strong>Median CPU time</strong> in the <strong>Functions metrics</strong> dashboard shows historical <a href="/workers/platform/limits/#duration">duration</a> per Function execution. The data is broken down into relevant quantiles, similar to the CPU time chart.</p>
<p>Understanding duration on your Function is useful when you are intending to do a significant amount of computation on the Function itself. This is because you may have to use the Standard or Unbound usage model which allows up to 30 seconds of CPU time.</p>
<p>Workers on the <a href="/workers/platform/pricing/#workers">Bundled Usage Model</a> may have high durations, even with a 50 ms CPU time limit, if they are running many network-bound operations like fetch requests and waiting on responses.</p>
<h3 id="metrics-retention">Metrics retention</h3>
<p>Functions metrics can be inspected for up to three months in the past in maximum increments of one week. The <strong>Functions metrics</strong> dashboard in your Pages project includes the charts and information described above.</p>
