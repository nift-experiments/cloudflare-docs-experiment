<p>The Web Application Firewall (WAF) contains rules managed by Cloudflare to block requests that contain malicious content.</p>
<h2 id="waf-action">WAF Action</h2>
<table>
<thead>
<tr>
<th>Value</th>
<th>Action</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><span style="font-weight: 400;"><code>0</code></span></td>
<td>Unknown</td>
<td>Take no other action.</td>
</tr>
<tr>
<td><span style="font-weight: 400;"><code>1</code></span></td>
<td>Allow</td>
<td>Bypass all subsequent WAF rules.</td>
</tr>
<tr>
<td><span style="font-weight: 400;"><code>2</code></span></td>
<td>Drop</td>
<td>Block with an HTTP 403 response.</td>
</tr>
<tr>
<td><span style="font-weight: 400;"><code>3</code></span></td>
<td>Challenge Allow</td>
<td>Issue a Managed Challenge.</td>
</tr>
<tr>
<td><span style="font-weight: 400;"><code>4</code></span></td>
<td>Challenge Drop</td>
<td>Unused.</td>
</tr>
<tr>
<td><span style="font-weight: 400;"><code>5</code></span></td>
<td>Log</td>
<td>Take no action other than logging the event.</td>
</tr>
</tbody>
</table>
<h2 id="deprecated-fields-for-internal-cloudflare-use">Deprecated fields for internal Cloudflare use</h2>
<p>The values of these fields are subject to change by Cloudflare at any time and are irrelevant for customer data analysis:</p>
<ul>
<li>WAFFlags</li>
<li>WAFMatchedVar</li>
</ul>
