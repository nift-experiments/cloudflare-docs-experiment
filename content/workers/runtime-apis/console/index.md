<p>The <code>console</code> object provides a set of methods to help you emit logs, warnings, and debug code.</p>
<p>All standard <a href="https://developer.mozilla.org/en-US/docs/Web/API/console">methods of the <code>console</code> API</a> are present on the <code>console</code> object in Workers.</p>
<p>However, some methods are no ops — they can be called, and do not emit an error, but do not do anything. This ensures compatibility with libraries which may use these APIs.</p>
<p>The table below enumerates each method, and the extent to which it is supported in Workers.</p>
<p>All methods noted as &quot;✅ supported&quot; have the following behavior:</p>
<ul>
<li>They will be written to the console in local dev (<code>npx wrangler@latest dev</code>)</li>
<li>They will appear in real-time logs when tailing logs in the dashboard or running <a href="/workers/observability/logs/real-time-logs/#view-logs-using-wrangler-tail"><code>wrangler tail</code></a></li>
<li>They will create entries in the <code>logs</code> field of <a href="/workers/observability/logs/tail-workers/">Tail Worker</a> events and <a href="/logs/logpush/logpush-job/datasets/account/workers_trace_events/">Workers Trace Events</a>. You can use <a href="/workers/observability/logs/logpush/">Logpush</a> to send Workers Trace Event Logs to a supported destination.</li>
</ul>
<p>All methods noted as &quot;🟡 partial support&quot; have the following behavior:</p>
<ul>
<li>In both production and local development the method can be safely called, but will do nothing (no op)</li>
<li>In the <a href="https://workers.cloudflare.com/playground">Workers Playground</a>, Quick Editor in the Workers dashboard, and remote preview mode (<code>wrangler dev --remote</code>) calling the method will behave as expected, print to the console, etc.</li>
</ul>
<p>Refer to <a href="/workers/observability/logs/">Logs</a> for more information about debugging and adding logs to Workers.</p>
<table>
<thead>
<tr>
<th>Method</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/debug_static"><code>console.debug()</code></a></td>
<td>✅ supported</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/error_static"><code>console.error()</code></a></td>
<td>✅ supported</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/info_static"><code>console.info()</code></a></td>
<td>✅ supported</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/log_static"><code>console.log()</code></a></td>
<td>✅ supported</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/warn_static"><code>console.warn()</code></a></td>
<td>✅ supported</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/clear_static"><code>console.clear()</code></a></td>
<td>🟡 partial support</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/count_static"><code>console.count()</code></a></td>
<td>🟡 partial support</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/group_static"><code>console.group()</code></a></td>
<td>🟡 partial support</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/table_static"><code>console.table()</code></a></td>
<td>🟡 partial support</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/trace_static"><code>console.trace()</code></a></td>
<td>🟡 partial support</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/assert_static"><code>console.assert()</code></a></td>
<td>⚪ no op</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/countreset_static"><code>console.countReset()</code></a></td>
<td>⚪ no op</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/dir_static"><code>console.dir()</code></a></td>
<td>⚪ no op</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/dirxml_static"><code>console.dirxml()</code></a></td>
<td>⚪ no op</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/groupcollapsed_static"><code>console.groupCollapsed()</code></a></td>
<td>⚪ no op</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/groupend_static"><code>console.groupEnd</code></a></td>
<td>⚪ no op</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/profile_static"><code>console.profile()</code></a></td>
<td>⚪ no op</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/profileend_static"><code>console.profileEnd()</code></a></td>
<td>⚪ no op</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/time_static"><code>console.time()</code></a></td>
<td>⚪ no op</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/timeend_static"><code>console.timeEnd()</code></a></td>
<td>⚪ no op</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/timelog_static"><code>console.timeLog()</code></a></td>
<td>⚪ no op</td>
</tr>
<tr>
<td><a href="https://developer.mozilla.org/en-US/docs/Web/API/console/timestamp_static"><code>console.timeStamp()</code></a></td>
<td>⚪ no op</td>
</tr>
<tr>
<td><a href="https://developer.chrome.com/blog/devtools-modern-web-debugging/#linked-stack-traces"><code>console.createTask()</code></a></td>
<td>🔴 Will throw an exception in production, but works in local dev, Quick Editor, and remote preview</td>
</tr>
</tbody>
</table>
