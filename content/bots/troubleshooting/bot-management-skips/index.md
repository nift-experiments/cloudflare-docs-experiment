<p>There are instances in which Bot Management does not run and certain fields, such as the <a href="/bots/additional-configurations/ja3-ja4-fingerprint/">JA3/JA4 field</a>, are not populated because it has been determined that running Bot Management would not be necessary.</p>
<p>Refer to <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/3465.md")
</div> for more information about why a request is not scored.
<h2 id="common-reasons-for-bot-management-to-not-score-a-request">Common reasons for Bot Management to not score a request</h2>
<h3 id="requests-to-internal-endpoints">Requests to internal endpoints</h3>
<p>Requests such as <code>/cdn-cgi/</code> are handled individually and will never receive a Bot Management score. Email Obfuscation, Web Analytics, Trace Requests, Challenge Pages, and JavaScript Detections do not receive bot scores. Refer to the table below for some examples of internal endpoints.</p>
<table>
<thead>
<tr>
<th>Route</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/cdn-cgi/rum</code></td>
</tr>
<tr>
<td><code>/cdn-cgi/script_monitor/report</code></td>
</tr>
<tr>
<td><code>/cdn-cgi/trace</code></td>
</tr>
<tr>
<td><code>/cdn-cgi/challenge-platform/…</code></td>
</tr>
<tr>
<td><code>/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js</code></td>
</tr>
</tbody>
</table>
<h3 id="purge-requests">Purge requests</h3>
<p>All HTTP purge requests will not receive a bot score.</p>
<h3 id="early-hints-cache-requests">Early hints cache requests</h3>
<p>Early hints cache requests will not receive a bot score.</p>
