<p>Origin Analytics shows how your origin server responds to Cloudflare, using data collected at the edge without an agent on your origin.</p>
<p>Use Origin Analytics to identify slow endpoints, monitor origin response times, and diagnose errors. When something goes wrong, Origin Analytics shows whether the source is your origin, the network path, or Cloudflare. For common error codes, refer to <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/">Cloudflare 5xx errors</a>.</p>
<h2 id="view-origin-analytics">View Origin Analytics</h2>
<p>To open the Origin Analytics tab:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> and select your account and domain.</li>
<li>Go to <strong>Speed</strong> &gt; <strong>Origin Analytics</strong>.</li>
</ol>
<h2 id="metrics">Metrics</h2>
<p>The dashboard displays the following metrics, derived from your zone's edge logs.</p>
<h3 id="origin-response-time">Origin response time</h3>
<p>Use this metric to spot slowdowns and catch requests approaching your timeout threshold before they result in <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-524/">524 errors</a>.</p>
<p>Origin response time shows how long your origin takes to respond to Cloudflare, measured at the 50th, 95th, and 99th percentiles. A reference line indicates your zone's configured origin timeout.</p>
<p>The clock starts when Cloudflare decides the request must go to origin (a cache miss) and stops when Cloudflare receives the response headers — not the full body — back from your origin. It includes DNS resolution, TCP and TLS handshakes, request transmission, origin processing, and response receipt. If <a href="/argo-smart-routing/">Argo Smart Routing</a> or <a href="/cache/how-to/tiered-cache/">Tiered Cache</a> is enabled, the metric also includes time spent routing through those services.</p>
<p>Because this measures the full upstream round trip, Origin Analytics shows higher response times than your origin's own monitoring tools (for example, Grafana or Datadog), which measure only server-side processing time.</p>
<h3 id="origin-status-codes">Origin status codes</h3>
<p>Use this metric to understand what your origin actually returned when users report errors. The error code the end user sees can differ from what your origin returned, because Cloudflare wraps certain origin failures in its own error codes (such as <code>520</code>, <code>522</code>, or <code>524</code>).</p>
<p>Origin Analytics shows both values: the response code from your origin (<code>originResponseStatus</code>) and the code Cloudflare served to the end user (<code>edgeResponseStatus</code>). Status codes are grouped by class (2xx, 3xx, 4xx, 5xx) and shown over time.</p>
<p>The following table shows common scenarios where these values differ:</p>
<table>
<thead>
<tr>
<th>What happened</th>
<th><code>originResponseStatus</code></th>
<th><code>edgeResponseStatus</code></th>
</tr>
</thead>
<tbody>
<tr>
<td>Origin returned <code>200</code> with malformed headers</td>
<td><code>200</code></td>
<td><code>520</code></td>
</tr>
<tr>
<td>Origin returned a server error</td>
<td><code>503</code></td>
<td><code>503</code> or <code>520</code></td>
</tr>
<tr>
<td>Origin closed the connection mid-response</td>
<td><code>0</code></td>
<td><code>520</code></td>
</tr>
<tr>
<td>Origin did not respond in time</td>
<td><code>0</code></td>
<td><code>524</code></td>
</tr>
<tr>
<td>TCP connection to origin failed</td>
<td><code>0</code></td>
<td><code>522</code></td>
</tr>
<tr>
<td>Request served from cache</td>
<td><code>0</code></td>
<td><code>200</code></td>
</tr>
<tr>
<td>Worker handled the request</td>
<td><code>0</code></td>
<td>Varies</td>
</tr>
</tbody>
</table>
<p>A status code of <code>0</code> means Cloudflare did not receive an HTTP response from the origin. This can indicate a connection failure, a timeout, or that the request was served from cache or handled by a <a href="/workers/">Worker</a> before reaching the origin.</p>
<h3 id="top-endpoints">Top endpoints</h3>
<p>Use this table to narrow down which specific path is causing slowdowns or errors. Request paths are ranked by P95 response time, error rate, request volume, or TCP failure rate.</p>
<h2 id="common-diagnostic-flows">Common diagnostic flows</h2>
<p>The following table describes how to use Origin Analytics to investigate common origin errors.</p>
<table>
<thead>
<tr>
<th>Issue</th>
<th>What to check</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-524/">524 timeout errors</a></td>
<td>Origin response time chart. If P95 is approaching the timeout threshold, identify slow paths in the <strong>Top endpoints</strong> table.</td>
</tr>
<tr>
<td><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-522/">522 connection errors</a></td>
<td>Verify that your firewall allows <a href="https://www.cloudflare.com/ips/">Cloudflare IP ranges</a> and that your origin is listening on the expected port.</td>
</tr>
<tr>
<td><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-520/">520 unknown errors</a></td>
<td>Origin status code chart. If the origin returned a <code>200</code> but Cloudflare served a <code>520</code>, the origin response was malformed (for example, oversized headers or an early connection close).</td>
</tr>
</tbody>
</table>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/">Cloudflare 5xx errors</a> — diagnose specific error codes like 520, 522, and 524.</li>
<li><a href="/logs/logpush/">Logpush</a> — export per-request logs with origin timing fields not available in the dashboard.</li>
<li><a href="/analytics/graphql-api/">GraphQL Analytics API</a> — query origin metrics programmatically, including fields not shown in the dashboard.</li>
<li><a href="/speed/observatory/dashboard/">Observatory dashboard</a> — monitor end-user performance with synthetic tests and real user data.</li>
</ul>
