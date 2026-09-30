<p>Cloudflare provides Managed Lists you can use in rule expressions. These lists are regularly updated.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15711.md")
</aside>
<h2 id="managed-ip-lists">Managed IP Lists</h2>
<p>Use Managed IP Lists to access Cloudflare's IP threat intelligence.</p>
<p>Cloudflare provides the following Managed IP Lists:</p>
<table>
<thead>
<tr>
<th>Display name</th>
<th>Name in expressions</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Open Proxies</td>
<td><code>cf.open_proxies</code></td>
<td>IP addresses of known open HTTP and SOCKS proxy endpoints, which are frequently used to launch attacks and hide attackers identity.</td>
</tr>
<tr>
<td>Cloudflare Anonymizers</td>
<td><code>cf.anonymizer</code></td>
<td>IP addresses of known anonymizers (Open SOCKS Proxies, VPNs, and TOR nodes).</td>
</tr>
<tr>
<td>Cloudflare VPNs</td>
<td><code>cf.vpn</code></td>
<td>IP addresses of known VPN servers.</td>
</tr>
<tr>
<td>Cloudflare Malware</td>
<td><code>cf.malware</code></td>
<td>IP addresses of known sources of malware.</td>
</tr>
<tr>
<td>Cloudflare Botnets, Command and Control Servers</td>
<td><code>cf.botnetcc</code></td>
<td>IP addresses of known botnet command-and-control servers.</td>
</tr>
</tbody>
</table>
<br />
