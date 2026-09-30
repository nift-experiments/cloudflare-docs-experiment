<p>Email security returns five potential verdicts for every email it scans. Review the detections and consider how you would treat them once an auto-move is enabled. Below is an overview of the disposition and recommendation actions by Cloudflare:</p>
<table>
<thead>
<tr>
<th>Disposition</th>
<th>Description</th>
<th>Recommendation</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>MALICIOUS</td>
<td>Traffic invoked multiple phishing verdict triggers, met thresholds for bad behavior, and is associated with active campaigns.</td>
<td>Block</td>
<td></td>
</tr>
<tr>
<td>SUSPICIOUS</td>
<td>Traffic associated with phishing campaigns (and is under further analysis by our automated systems).</td>
<td>Research these messages internally to evaluate legitimacy.</td>
<td></td>
</tr>
<tr>
<td>SPOOF</td>
<td>Traffic associated with phishing campaigns that is either non-compliant with your email authentication policies (<a href="https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-spf-record/">SPF</a>, <a href="https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dkim-record/">DKIM</a>, <a href="https://www.cloudflare.com/en-gb/learning/dns/dns-records/dns-dmarc-record/">DMARC</a>), or have mismatching Envelope From and Header From values.</td>
<td>Block after investigating (can be triggered by third-party mail services).</td>
<td></td>
</tr>
<tr>
<td>SPAM</td>
<td>Traffic associated with non-malicious, commercial campaigns.</td>
<td>Route to existing Spam quarantine folder.</td>
<td></td>
</tr>
<tr>
<td>BULK</td>
<td>Traffic associated with <a href="https://en.wikipedia.org/wiki/Graymail">Graymail</a>, that falls in between the definitions of SPAM and SUSPICIOUS. For example, a marketing email that intentionally obscures its unsubscribe link.</td>
<td>Monitor or tag</td>
<td></td>
</tr>
</tbody>
</table>
