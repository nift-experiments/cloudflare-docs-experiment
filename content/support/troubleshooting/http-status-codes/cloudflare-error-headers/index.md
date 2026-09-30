<p>When Cloudflare generates an error page (as opposed to forwarding an error from your origin server), the response includes two diagnostic headers:</p>
<ul>
<li><strong><code>cf-error-type</code></strong>: Identifies the error category. Common values:
<ul>
<li><code>1000</code> — DNS resolution failure (A record points to a Cloudflare IP)</li>
<li><code>1016</code> — Origin DNS error (CNAME target does not resolve)</li>
<li><code>1101</code> — Worker threw an unhandled exception</li>
<li><code>1102</code> — Worker exceeded resource limits (CPU or memory)</li>
<li><code>52x</code> — Origin connectivity error (521, 522, 523, 524, 525, 526)</li>
</ul>
</li>
<li><strong><code>cf-error-origin</code></strong>: Identifies which Cloudflare system generated the error.</li>
</ul>
<p>These headers are present <strong>only on Cloudflare-generated error pages</strong>, not on errors forwarded from your origin server.</p>
<h2 id="how-to-capture-these-headers">How to capture these headers</h2>
<p>Reproduce the error and inspect response headers using one of:</p>
<ul>
<li><code>curl -v https://example.com</code> — look for <code>cf-error-type</code> in the response headers</li>
<li>Browser DevTools: select <strong>Network</strong> &gt; select the failing request &gt; <strong>Headers</strong></li>
<li>Export a HAR file and inspect the response headers</li>
</ul>
<h2 id="using-cf-error-type-for-diagnosis">Using cf-error-type for diagnosis</h2>
<table>
<thead>
<tr>
<th><code>cf-error-type</code> prefix</th>
<th>Origin</th>
<th>Next step</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1xxx</code></td>
<td>DNS / routing layer</td>
<td>Check DNS records; verify no Cloudflare IP in A record</td>
</tr>
<tr>
<td><code>1101</code> / <code>1102</code></td>
<td>Workers runtime</td>
<td>Check <code>wrangler tail</code> for the exception</td>
</tr>
<tr>
<td><code>52x</code></td>
<td>Origin connectivity</td>
<td>Check origin server is up and reachable</td>
</tr>
</tbody>
</table>
