<p>You can view DDoS analytics in different dashboards, depending on your service and plan:</p>
<ul>
<li>
<p>The <a href="/waf/analytics/security-events/">Security Events dashboard</a> provides you with visibility into L7 security events that target your zone, including HTTP DDoS attacks and TCP attacks. The dashboard displays mitigations of HTTP DDoS attacks as HTTP DDoS events. These events are also available via <a href="/logs/">Cloudflare Logs</a>.</p>
</li>
<li>
<p>The <a href="/analytics/network-analytics/">Network Analytics dashboard</a> provides you with visibility into L3/4 traffic and DDoS attacks that target your IP ranges or Spectrum applications.</p>
</li>
</ul>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th>Service</th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>WAF/CDN</td>
<td>Sampled logs only</td>
<td>Security Events</td>
<td>Security Events</td>
<td>Security Events</td>
</tr>
<tr>
<td>Spectrum/BYOIP</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>Network Analytics</td>
</tr>
<tr>
<td>Magic Transit</td>
<td>–</td>
<td>–</td>
<td>–</td>
<td>Network Analytics</td>
</tr>
</tbody>
</table>
<h2 id="remarks">Remarks</h2>
<p>In some situations, the analytics dashboards will not show you the ID of the DDoS managed rule that handled a packet/request. This means that an internal DDoS rule, which Cloudflare does not currently expose publicly, applied an action to the packet/request. These internal DDoS rules have a very low false positive rate and should always be enabled to protect your properties against DDoS attacks. For the same reason, DDoS rule IDs may also be unavailable in Cloudflare logs and API responses.</p>
