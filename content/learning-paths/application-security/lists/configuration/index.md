<p>Both Custom and Managed Lists are located in the account settings. Refer to <a href="/learning-paths/application-security/lists/features/">Features by plan type</a> for more information on plan eligibility.</p>
<h2 id="custom-lists">Custom Lists</h2>
<p>Using a Custom List is an alternative to creating individual Firewall rules with long lists of IP addresses or other types of identifiers. They are easier to read and update, especially when they are used across many security rules. Lists are often used in conjunction with in-house or third party security feeds.</p>
<h2 id="managed-lists">Managed Lists</h2>
<p>The following lists are managed by the Cloudflare team and are regularly updated.</p>
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
<h2 id="creating-a-rule">Creating a rule</h2>
<p>Refer to <a href="/waf/tools/lists/use-in-expressions/">Use lists in expressions</a> to learn how to invoke a Managed List.</p>
