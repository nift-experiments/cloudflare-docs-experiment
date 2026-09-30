<p>Cloudflare bot detection includes additional signals to catch different kinds of automated traffic.</p>
<p>Bot management customers automatically benefit from the residential proxy detection improvement below, which lowers the <a href="/bots/concepts/bot-score/">bot score</a> for matched requests. Using the detection ID in <a href="/waf/custom-rules/">custom rules</a> provides even more visibility and control over mitigating residential proxy traffic.</p>
<table>
<thead>
<tr>
<th><span style="width:100px">Detection ID</span></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>50331651</code></td>
<td>Observes traffic from residential proxy networks and similar commercial proxies. <br /><br />When the ID matches a request, Bot Management sets the bot score to 29 and uses <a href="/bots/concepts/bot-detection-engines/#anomaly-detection-enterprise">anomaly detection</a> as its score source.</td>
</tr>
</tbody>
</table>
