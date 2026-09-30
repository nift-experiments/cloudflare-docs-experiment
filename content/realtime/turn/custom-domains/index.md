<p>Cloudflare Realtime TURN service supports using custom domains for UDP, and TCP - but not TLS protocols. Custom domains do not affect any of the performance of Cloudflare Realtime TURN and is set up via a simple CNAME DNS record on your domain.</p>
<table>
<thead>
<tr>
<th>Protocol</th>
<th>Custom domains</th>
<th>Primary port</th>
<th>Alternate port</th>
</tr>
</thead>
<tbody>
<tr>
<td>STUN over UDP</td>
<td>✅</td>
<td>3478/udp</td>
<td></td>
</tr>
<tr>
<td>TURN over UDP</td>
<td>✅</td>
<td>3478/udp</td>
<td></td>
</tr>
<tr>
<td>TURN over TCP</td>
<td>✅</td>
<td>3478/tcp</td>
<td>80/tcp</td>
</tr>
<tr>
<td>TURN over TLS</td>
<td>No</td>
<td>5349/tcp</td>
<td>443/tcp</td>
</tr>
</tbody>
</table>
<h2 id="setting-up-a-cname-record">Setting up a CNAME record</h2>
<p>To use custom domains for TURN, you must create a CNAME DNS record pointing to <code>turn.cloudflare.com</code>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11570.md")
</aside>
<p>Any DNS provider, including Cloudflare DNS can be used to set up a CNAME for custom domains.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11569.md")
</aside>
<p>There is no additional charge to using a custom hostname with Cloudflare Realtime TURN.</p>
