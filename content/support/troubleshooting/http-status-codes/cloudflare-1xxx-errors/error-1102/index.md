<h2 id="error-1102-worker-exceeded-resource-limits">Error 1102: Worker exceeded resource limits</h2>
<p>This error indicates that a Cloudflare Worker has exceeded its CPU time limit or memory limit.</p>
<h3 id="exceeded-cpu-time">Exceeded CPU time</h3>
<p>A Cloudflare Worker exceeds a <a href="/workers/platform/limits/#cpu-time">CPU time limit</a>. CPU time is the time spent executing code (for example, loops, parsing JSON, etc). Time spent on network requests (fetching, responding) does not count towards CPU time.</p>
<h4 id="debugging">Debugging</h4>
<p>To identify CPU-intensive code:</p>
<ol>
<li>Use <a href="/workers/observability/dev-tools/cpu-usage/">CPU profiling with DevTools</a> locally to identify expensive operations.</li>
<li>Review <a href="/workers/observability/logs/workers-logs/">Workers Logs</a> - CPU time is surfaced in the invocation log. This can help find if specific routes or requests are consuming high CPU time.</li>
</ol>
<h4 id="resolution">Resolution</h4>
<p>Contact the developer of your Workers code to optimize code for a reduction in CPU usage. Common optimization strategies include:</p>
<ul>
<li>Reducing the number of iterations in loops</li>
<li>Optimizing JSON parsing operations</li>
<li>Caching computed values</li>
<li>Breaking up large operations into smaller chunks</li>
</ul>
<p>You can also <a href="/workers/platform/limits/#cpu-time">increase the CPU time limit</a> on the Workers Paid plan up to 5 minutes for CPU-bound tasks.</p>
<h3 id="exceeded-memory">Exceeded memory</h3>
<p>A Cloudflare Worker exceeds the <a href="/workers/platform/limits/#memory">128 MB memory limit</a>. This is a per-isolate limit, an isolate may be handling multiple requests concurrently.</p>
<h4 id="debugging-1">Debugging</h4>
<p>To identify memory issues:</p>
<ol>
<li>Use <a href="/workers/observability/dev-tools/memory-usage/">memory profiling with DevTools</a> locally to take memory snapshots and identify leaks.</li>
<li>Look for patterns like buffering a body which could be large (request or response), large objects stored in global scope or accumulating data in arrays.</li>
</ol>
<h4 id="resolution-1">Resolution</h4>
<p>To avoid exceeding memory limits:</p>
<ul>
<li>Avoid buffering large objects or responses in memory</li>
<li>Use streaming APIs such as <a href="/workers/runtime-apis/streams/transformstream/"><code>TransformStream</code></a> or <a href="/workers/runtime-apis/nodejs/streams/"><code>node:stream</code></a> to process data without buffering</li>
<li>Avoid storing large objects in global scope</li>
<li>Be cautious with operations that accumulate data (e.g., appending to strings or arrays repeatedly)</li>
</ul>
<h3 id="related-errors">Related errors</h3>
<ul>
<li><a href="/support/troubleshooting/http-status-codes/cloudflare-1xxx-errors/error-1101/">Error 1101</a> - Workers JavaScript runtime exception</li>
<li><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-503/">Error 503</a> - Service temporarily unavailable (can be caused by Workers CPU or memory limits)</li>
</ul>
