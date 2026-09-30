<p><a href="/logs/faq/">❮ Back to FAQ</a></p>
<h3 id="why-do-i-see-504-responses-with-originresponsestatus-0-in-logpush-that-do-not-appear-in-the-dashboard">Why do I see 504 responses with <code>OriginResponseStatus=0</code> in Logpush that do not appear in the dashboard?</h3>
<p>If you ingest Cloudflare Logpush into Splunk, Datadog, or another SIEM, you may see log entries with <code>EdgeResponseStatus=504</code> and <code>OriginResponseStatus=0</code> that do not appear anywhere in the Cloudflare dashboard.</p>
<p>In most cases these are internal Cloudflare subrequests, not real end-user errors. The most common sources are <a href="/cache/advanced-configuration/early-hints/">Early Hints</a> cache MISS lookups and Workers <a href="/workers/runtime-apis/cache/">Cache API</a> <code>cache.match()</code> MISS returns. These subrequests never reach your origin, so your site continues to work normally for end users.</p>
<p>Cache Analytics and the dashboard filter these subrequests out by design. Logpush ships every log line the edge produces, including internal subrequests, so the same data appears in two places with two different default filters. Filter the subrequests out in your SIEM using the <code>RequestSource</code> field.</p>
<h3 id="what-a-matching-log-entry-looks-like">What a matching log entry looks like</h3>
<p>A typical entry in your SIEM looks like this:</p>
<pre><code class="language-txt">EdgeResponseStatus: 504&#10;OriginResponseStatus: 0&#10;ClientRequestHost: www.example.com&#10;EdgeStartTimestamp: 2026-04-15T10:23:17Z&#10;</code></pre>
<p>Your application is working normally, your origin is healthy, and no 504 responses appear in the dashboard for this zone. Your SIEM dashboards may still show tens of thousands of these entries per day.</p>
<h3 id="what-the-fields-mean">What the fields mean</h3>
<p>From the <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/">HTTP requests dataset reference</a>:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>EdgeResponseStatus</code></td>
<td>HTTP status code returned by Cloudflare to the client.</td>
</tr>
<tr>
<td><code>OriginResponseStatus</code></td>
<td>Status returned by the upstream server. The value <code>0</code> means that there was no response received from the origin server and the response was served by Cloudflare's edge. If the zone has a Worker running on it, <code>0</code> can also be the result of a Workers subrequest made to the origin.</td>
</tr>
</tbody>
</table>
<p><code>OriginResponseStatus=0</code> on its own is not an error signal. It means Cloudflare did not make a successful origin fetch for that log line. This is normal for cache hits, Worker responses, WAF blocks, redirects, and internal subrequests.</p>
<h3 id="why-the-combination-occurs">Why the combination occurs</h3>
<p>The <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-502-504/">Error 502/504 page</a> calls out two documented, benign causes for <code>504</code> entries in logs: cache MISS responses from Early Hints, and Workers Cache API <code>cache.match</code> operations that return cache MISS.</p>
<h4 id="cause-1-early-hints-cache-miss">Cause 1: Early Hints cache MISS</h4>
<p>From the <a href="/cache/advanced-configuration/early-hints/#emit-early-hints">Early Hints documentation</a>:</p>
<blockquote>
<p>You may see an influx of <code>504</code> responses with the <code>RequestSource</code> of <code>earlyHintsCache</code> in Cloudflare Logs when Early Hints is enabled, which is expected and benign. Requests from <code>earlyHintsCache</code> are internal subrequests for cached Early Hints, and they are neither end user requests, nor do they go to your origin.</p>
</blockquote>
<p>Their response status only indicates whether there are cached Early Hints for the request URI: <code>200</code> on cache HIT, <code>504</code> on cache MISS.</p>
<p>This happens when Early Hints is enabled on the zone and Cloudflare is looking up whether there are any cached <code>Link: &lt;...&gt;; rel=preload</code> or <code>rel=preconnect</code> headers to send to the browser ahead of the main response. A cache MISS means there are no cached <code>Link</code> headers for that URL, so the lookup returns <code>504</code> internally.</p>
<p>If your origin does not emit <code>Link</code> preload or preconnect headers, every Early Hints lookup is a MISS and every request on the zone produces one of these internal <code>504</code> log lines. At scale, this can be millions of entries per day.</p>
<h4 id="cause-2-workers-cache-api-cache-match-miss">Cause 2: Workers Cache API <code>cache.match</code> MISS</h4>
<p>From the <a href="/workers/runtime-apis/cache/#errors">Workers Cache API documentation</a>:</p>
<blockquote>
<p><code>cache.match</code> generates a <code>504</code> error response when the requested content is missing or expired. The Cache API does not expose this <code>504</code> directly to the Worker script, instead returning <code>undefined</code>. Nevertheless, the underlying <code>504</code> is still visible in Cloudflare Logs. If you use Cloudflare Logs, you may see these <code>504</code> responses with the <code>RequestSource</code> of <code>edgeWorkerCacheAPI</code>.</p>
</blockquote>
<p>This happens when a Worker on the zone calls <code>caches.default.match(request)</code> (or similar) and the content is not in the cache, or has expired. The API returns <code>undefined</code> to the Worker, but the internal <code>504</code> still appears in your logs.</p>
<h3 id="why-the-dashboard-does-not-show-these-entries">Why the dashboard does not show these entries</h3>
<p>The Cloudflare dashboard applies a <code>requestSource = &quot;eyeball&quot;</code> filter to every analytics view — Cache Analytics, HTTP Analytics, and Security Analytics. That filter strips out internal subrequests by design.</p>
<p>Logpush is a raw log stream with no such filter. It ships every log line the edge produces, including internal subrequests. The same data appears in both places with two different default filters, so the dashboard hides these entries and your SIEM does not.</p>
<p>To replicate the dashboard's filter in the GraphQL Analytics API, refer to <a href="/analytics/graphql-api/features/filtering/#filter-end-users">Filter end users</a>.</p>
<h3 id="confirm-what-you-are-seeing">Confirm what you are seeing</h3>
<p>Add the <code>RequestSource</code> field to your Logpush job's <code>output_options.field_names</code>. Field changes propagate in approximately 10–15 minutes, per the <a href="/logs/logpush/logpush-job/api-configuration/">API configuration reference</a>.</p>
<pre><code class="language-bash">curl -X PUT &quot;https://api.cloudflare.com/client/v4/zones/$ZONE_ID/logpush/jobs/$JOB_ID&quot; \&#10;  &#45;H &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;output_options&quot;: {&#10;      &quot;field_names&quot;: [&quot;...existing fields...&quot;, &quot;RequestSource&quot;]&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>Once the field flows, re-check your <code>504</code> / <code>0</code> entries:</p>
<table>
<thead>
<tr>
<th><code>RequestSource</code> value</th>
<th>Meaning</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>earlyHintsCache</code></td>
<td>Early Hints internal subrequest (benign)</td>
<td>Filter out</td>
</tr>
<tr>
<td><code>edgeWorkerCacheAPI</code></td>
<td>Workers Cache API MISS (benign)</td>
<td>Filter out</td>
</tr>
<tr>
<td><code>eyeball</code> or empty</td>
<td>Real end-user request</td>
<td>Investigate as a genuine <code>504</code></td>
</tr>
</tbody>
</table>
<h3 id="filter-in-your-siem">Filter in your SIEM</h3>
<p>Add a filter equivalent to the following to your SIEM dashboards, alerts, and queries. This replicates the filter the Cloudflare dashboard applies to its analytics views.</p>
<p><strong>Splunk:</strong></p>
<pre><code class="language-txt">NOT RequestSource IN (&quot;earlyHintsCache&quot;, &quot;edgeWorkerCacheAPI&quot;)&#10;</code></pre>
<p><strong>Datadog:</strong></p>
<pre><code class="language-txt">NOT @RequestSource:(&quot;earlyHintsCache&quot; OR &quot;edgeWorkerCacheAPI&quot;)&#10;</code></pre>
<p><strong>Sumo Logic or generic:</strong></p>
<pre><code class="language-txt">!(RequestSource = &quot;earlyHintsCache&quot; OR RequestSource = &quot;edgeWorkerCacheAPI&quot;)&#10;</code></pre>
<h3 id="when-504-with-origin-status-0-is-a-real-problem">When 504 with origin status 0 is a real problem</h3>
<p>Not every <code>504</code> with <code>OriginResponseStatus=0</code> is an internal subrequest. Real origin-side failures produce the same field combination:</p>
<ul>
<li><strong>Origin timeout</strong> — Cloudflare opened the connection (or tried to) but got no response. <code>OriginResponseStatus</code> stays <code>0</code> because no status was received.</li>
<li><strong>Cloudflare Tunnel cannot reach origin</strong> — <code>cloudflared</code> is connected but cannot reach the configured service. Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/">Tunnel common errors</a>.</li>
<li><strong>Worker <code>fetch()</code> to origin fails or times out</strong> — per the <code>OriginResponseStatus</code> field definition, if the zone has a Worker running on it, the value <code>0</code> can be the result of a Workers subrequest made to the origin.</li>
</ul>
<p>The <code>RequestSource</code> field distinguishes these from internal subrequests. If <code>RequestSource</code> is <code>eyeball</code> or empty and the edge returned <code>504</code>, investigate origin health, Tunnel connectivity, or Worker reliability.</p>
<h3 id="stop-the-noise-at-the-source">Stop the noise at the source</h3>
<p>If you do not benefit from Early Hints — for example, your origin does not emit <code>Link</code> preload or preconnect headers — you can turn Early Hints off entirely:</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Speed</strong> &gt; <strong>Optimization</strong> &gt; <strong>Content Optimization</strong>.</li>
<li>Turn <strong>Early Hints</strong> off.</li>
</ol>
<p>This eliminates the <code>earlyHintsCache</code> subrequests at source rather than filtering them downstream. To check whether Early Hints is doing anything useful for your zone, query the GraphQL Analytics API for <code>103</code> status codes served to clients. If that count is zero while <code>earlyHintsCache</code> activity is high, Early Hints is on but not serving anything.</p>
<p>For the Workers Cache API case, the <code>504</code> MISS behavior is intrinsic to how <code>cache.match</code> signals a miss. Filtering in your SIEM is the appropriate fix.</p>
<h3 id="summary">Summary</h3>
<ol>
<li>Add <code>RequestSource</code> to your Logpush job's <code>field_names</code>.</li>
<li>Wait approximately 15 minutes for the change to propagate.</li>
<li>Check the <code>RequestSource</code> value on your <code>504</code> / <code>0</code> entries.</li>
<li>Filter out <code>earlyHintsCache</code> and <code>edgeWorkerCacheAPI</code> in your SIEM.</li>
<li>If all your <code>504</code> / <code>0</code> entries are <code>earlyHintsCache</code> and you do not serve <code>Link</code> preload headers, consider turning Early Hints off in Speed settings.</li>
<li>Only investigate entries where <code>RequestSource</code> is <code>eyeball</code> or empty as real origin issues.</li>
</ol>
<h3 id="related-resources">Related resources</h3>
<ul>
<li><a href="/logs/logpush/logpush-job/datasets/zone/http_requests/">HTTP requests dataset — field reference</a></li>
<li><a href="/cache/advanced-configuration/early-hints/#emit-early-hints">Early Hints — Emit Early Hints</a></li>
<li><a href="/workers/runtime-apis/cache/#errors">Workers Cache API — Errors</a></li>
<li><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-502-504/">Error 502 or 504</a></li>
<li><a href="/analytics/graphql-api/features/filtering/#filter-end-users">GraphQL Analytics API — Filter end users</a></li>
<li><a href="/logs/logpush/logpush-job/api-configuration/">Logpush API configuration</a></li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/">Cloudflare Tunnel — Common errors</a></li>
<li><a href="/logs/faq/worker-subrequests/">Worker subrequests — Why origin fields appear on Worker subrequest log entries</a></li>
</ul>
