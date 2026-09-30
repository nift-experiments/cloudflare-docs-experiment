<p>The following limits apply to Workers Analytics Engine:</p>
<ul>
<li>Analytics Engine will accept up to twenty blobs, twenty doubles, and one index per call to <code>writeDataPoint</code>.</li>
<li>The total size of all blobs in a request must not exceed <strong>16 KB</strong>. The 16 KB size limit for the blobs field applies to <strong>each individual data point</strong>, regardless of how many are included in a single request using writeDataPoints().</li>
<li>Each index must not be more than 96 bytes.</li>
<li>You can write a maximum of 250 data points per Worker invocation (client HTTP request). Each call to <code>writeDataPoint</code> counts towards this limit.</li>
</ul>
<h2 id="data-retention">Data retention</h2>
<p>Data written to Workers Analytics Engine is stored for three months.</p>
<p>Interested in longer retention periods? Join the <code>#analytics-engine</code> channel in the <a href="https://discord.cloudflare.com/">Cloudflare Developers Discord</a> and tell us more about what you are building.</p>
