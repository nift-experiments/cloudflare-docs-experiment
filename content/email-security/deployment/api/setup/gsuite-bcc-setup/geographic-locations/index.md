<p>Select from the following BCC addresses to process email in the correct geographic location.</p>
<table>
<thead>
<tr>
<th>Host</th>
<th>Location</th>
<th>Note</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&lt;customer_name&gt;@journaling.mxrecord.io</code></td>
<td>US</td>
<td>Best option to ensure all email traffic processing happens US data centers.</td>
</tr>
<tr>
<td><code>&lt;customer_name&gt;@journaling.mailstream-eu-primary.mxrecord.io</code></td>
<td>EU</td>
<td>Best option to ensure all email traffic processing happens in Germany, with backup to US data centers.</td>
</tr>
<tr>
<td><code>&lt;customer_name&gt;@journaling.mailstream-eu1.mxrecord.io</code></td>
<td>EU</td>
<td>Best option to ensure all email traffic processing happens within the EU without backup to US data centers.</td>
</tr>
<tr>
<td><code>&lt;customer_name&gt;@journaling.mailstream-bom.mxrecord.mx</code></td>
<td>India</td>
<td>Best option to ensure all email traffic processing happens within India.</td>
</tr>
<tr>
<td><code>&lt;customer_name&gt;@journaling.mailstream-india-primary.mxrecord.mx</code></td>
<td>India</td>
<td>Same as <code>mailstream-bom.mxrecord.mx</code>, with backup to US data centers.</td>
</tr>
<tr>
<td><code>&lt;customer_name&gt;@journaling.mailstream-asia.mxrecord.mx</code></td>
<td>India</td>
<td>Best option to ensure all email traffic processing happens in India, with Australia data centers as backup.</td>
</tr>
<tr>
<td><code>&lt;customer_name&gt;@journaling.mailstream-syd.area1.cloudflare.net</code></td>
<td>Australia / New Zealand</td>
<td>Best option to ensure all email traffic processing happens within Australia.</td>
</tr>
<tr>
<td><code>&lt;customer_name&gt;@journaling.mailstream-australia.area1.cloudflare.net</code></td>
<td>Australia / New Zealand</td>
<td>Best option to ensure all email traffic processing happens in Australia, with India and US data centers as backup.</td>
</tr>
</tbody>
</table>
