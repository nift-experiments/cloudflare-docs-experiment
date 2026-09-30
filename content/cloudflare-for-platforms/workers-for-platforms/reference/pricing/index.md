<p>The Workers for Platforms Paid plan is <strong>$25 monthly</strong>. Workers for Platforms can be purchased through the <a href="https://dash.cloudflare.com/?to=/:account/workers-for-platforms">Cloudflare dashboard</a>.</p>
<p>Workers for Platforms comes with the following usage allotments and overage pricing.</p>
<table>
<thead>
<tr>
<th></th>
<th>Requests<sup>1</sup> <sup>2</sup></th>
<th>Duration</th>
<th>CPU time<sup>2</sup></th>
<th>Scripts</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td>20 million requests included per month <br /><br /> +$0.30 per additional million</td>
<td>No charge or limit for duration</td>
<td>60 million CPU milliseconds included per month<br /><br /> +$0.02 per additional million CPU milliseconds<br /><br/> Max of 30 seconds of CPU time per invocation <br /> Max of 15 minutes of CPU time per <a href="/workers/configuration/cron-triggers/">Cron Trigger</a> or <a href="/queues/configuration/javascript-apis/#consumer">Queue Consumer</a> invocation</td>
<td>1000 scripts <br /> <br />+$0.02 per additional script</td>
</tr>
</tbody>
</table>
<p><sup>1</sup>  Inbound requests to your Worker. Cloudflare does not bill for <a href="/workers/platform/limits/#subrequests">subrequests</a> you make from your Worker. <br /> <sup>2</sup>  Workers for Platforms only charges for 1 request across the chain of <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#dynamic-dispatch-worker">dispatch Worker</a> -&gt; <a href="/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/#user-workers">user Worker</a> -&gt; <a href="/cloudflare-for-platforms/workers-for-platforms/configuration/outbound-workers/">outbound Worker</a>. CPU time is charged across these Workers.</p>
<h2 id="example-pricing">Example pricing:</h2>
<p>A Workers for Platforms project that serves 100 million requests per month, uses an average of 10 milliseconds (ms) of CPU time per request and uses 1200 scripts would have the following estimated costs:</p>
<table>
<thead>
<tr>
<th></th>
<th>Monthly Costs</th>
<th>Formula</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Subscription</strong></td>
<td>$25.00</td>
<td></td>
</tr>
<tr>
<td><strong>Requests</strong></td>
<td>$24.00</td>
<td>(100,000,000 requests - 20,000,000 included requests) / 1,000,000 * $0.30</td>
</tr>
<tr>
<td><strong>CPU time</strong></td>
<td>$18.80</td>
<td>((10 ms of CPU time per request * 100,000,000 requests) - 60,000,000 included CPU ms) / 1,000,000 * $0.02</td>
</tr>
<tr>
<td><strong>Scripts</strong></td>
<td>$4.00</td>
<td>(1200 scripts - 1000 included scripts) * $0.02</td>
</tr>
<tr>
<td><strong>Total</strong></td>
<td>$71.80</td>
<td></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="custom-limits">Custom limits</h3>
@markup("md", "content/.markup/bodies/4189.md")
</aside>
