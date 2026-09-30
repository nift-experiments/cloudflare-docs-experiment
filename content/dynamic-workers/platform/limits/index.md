<p>Cloudflare limits the number of distinct Dynamic Workers with in-flight requests. Multiple in-flight requests to the same Dynamic Worker count as one toward this limit.</p>
<table>
<thead>
<tr>
<th>Context</th>
<th>Concurrent Dynamic Workers</th>
</tr>
</thead>
<tbody>
<tr>
<td>Worker request</td>
<td>4</td>
</tr>
<tr>
<td><a href="/durable-objects/">Durable Object</a></td>
<td>10 (previously 4)</td>
</tr>
</tbody>
</table>
<p>In a Worker, each request has its own input/output (I/O) context. Each request can therefore have up to four distinct Dynamic Workers with in-flight requests.</p>
<p>A Durable Object shares one I/O context across all concurrent requests to the same object. Those requests can collectively have up to ten distinct Dynamic Workers with in-flight requests. To set lower CPU time or subrequest limits, refer to <a href="/dynamic-workers/usage/limits/">Custom resource limits</a>.</p>
