<p>Logpush delivers logs in batches as quickly as possible, with no minimum batch size, potentially delivering files more than once per minute. This capability enables Cloudflare to provide information almost in real time, in smaller file sizes.</p>
<p>The push frequency is automatic and cannot be adjusted—Cloudflare pushes logs in batches as soon as possible. However, users can configure the batch size <a href="/logs/logpush/logpush-job/api-configuration/#max-upload-parameters">using the API</a> for improved control in case the log destination has specific requirements.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important-limitation">Important limitation</h3>
@markup("md", "content/.markup/bodies/10475.md")
</aside>
<p>Logpush does not offer storage or search functionality for logs; its primary aim is to send logs as quickly as they arrive.</p>
<p>Cloudflare Logpush supports pushing logs to storage services, SIEMs, and log management providers via the Cloudflare dashboard or API.</p>
<p>Cloudflare aims to support additional services in the future. Interested in a particular service? Take this <a href="https://goo.gl/forms/0KpMfae63WMPjBmD2">survey</a>.</p>
<h2 id="estimating-log-volume">Estimating log volume</h2>
<p>Before setting up a Logpush job, you can estimate the total volume of data that will be pushed to your destination. The volume depends on your traffic, selected fields, and compression.</p>
<h3 id="quick-sizing-for-http-requests">Quick sizing for HTTP Requests</h3>
<p>A quick sizing estimate for an <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/">HTTP Requests</a> dataset:</p>
<ul>
<li>~100–250 bytes per request (compressed, depending on fields selected)</li>
<li>1M requests/day → ~100–250 MB/day</li>
<li>30M requests/month → ~3–7.5 GB/month</li>
</ul>
<h3 id="daily-storage-by-traffic-volume">Daily storage by traffic volume</h3>
<ul>
<li>100k req/day → ~25–50 MB/day</li>
<li>1M req/day → ~250–500 MB/day</li>
<li>10M req/day → ~2.5–5 GB/day</li>
<li>100M req/day → ~25–50 GB/day</li>
</ul>
<p>These ranges reflect field selection, compression, and whether you include extra fields or <a href="/logs/logpush/logpush-job/custom-fields/">custom fields</a>. Other datasets (Firewall, Workers, Load Balancing) add volume separately.</p>
<p>For precise estimates, you can <a href="/logs/logpull/additional-details/#estimating-daily-data-volume">sample your logs via Logpull</a> using a 1-hour sample.</p>
<h2 id="limits">Limits</h2>
<p>There is currently a max limit of <strong>4 Logpush jobs per zone</strong>. Trying to create a job once the limit has been reached will result in an error message: <code>creating a new job is not allowed: exceeded max jobs allowed</code>.</p>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10474.md")
</aside>
