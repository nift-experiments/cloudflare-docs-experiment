<p>An IP Access rule will apply a certain action to incoming traffic based on the visitor's IP address, IP range, Autonomous System Number (ASN), or country.</p>
<h2 id="ip-address">IP address</h2>
<table>
<thead>
<tr>
<th>Type</th>
<th>Example value</th>
</tr>
</thead>
<tbody>
<tr>
<td>IPv4 address</td>
<td><code>192.0.2.3</code></td>
</tr>
<tr>
<td>IPv6 address</td>
<td><code>2001:db8::</code></td>
</tr>
</tbody>
</table>
<h2 id="ip-range">IP range</h2>
<table>
<thead>
<tr>
<th>Type</th>
<th>Example value</th>
<th>Start of range</th>
<th>End of range</th>
<th align="right">Number of addresses</th>
</tr>
</thead>
<tbody>
<tr>
<td>IPv4 <code>/24</code> range</td>
<td><code>192.0.2.0/24</code></td>
<td><code>192.0.2.0</code></td>
<td><code>192.0.2.255</code></td>
<td align="right">256</td>
</tr>
<tr>
<td>IPv4 <code>/16</code> range</td>
<td><code>192.168.0.0/16</code></td>
<td><code>192.168.0.0</code></td>
<td><code>192.168.255.255</code></td>
<td align="right">65,536</td>
</tr>
<tr>
<td>IPv6 <code>/128</code> range</td>
<td><code>2001:db8::/128</code></td>
<td><code>2001:db8::</code></td>
<td><code>2001:db8::</code></td>
<td align="right">1</td>
</tr>
<tr>
<td>IPv6 <code>/64</code> range</td>
<td><code>2001:db8::/64</code></td>
<td><code>2001:db8::</code></td>
<td><code>2001:db8:0000:0000:ffff:ffff:ffff:ffff</code></td>
<td align="right">18,446,744,073,709,551,616</td>
</tr>
<tr>
<td>IPv6 <code>/48</code> range</td>
<td><code>2001:db8::/48</code></td>
<td><code>2001:db8::</code></td>
<td><code>2001:db8:0000:ffff:ffff:ffff:ffff:ffff</code></td>
<td align="right">1,208,925,819,614,629,174,706,176</td>
</tr>
<tr>
<td>IPv6 <code>/32</code> range</td>
<td><code>2001:db8::/32</code></td>
<td><code>2001:db8::</code></td>
<td><code>2001:db8:ffff:ffff:ffff:ffff:ffff:ffff</code></td>
<td align="right">79,228,162,514,264,337,593,543,950,336</td>
</tr>
</tbody>
</table>
<h2 id="autonomous-system-number-asn">Autonomous System Number (ASN)</h2>
<table>
<thead>
<tr>
<th>Type</th>
<th>Example value</th>
</tr>
</thead>
<tbody>
<tr>
<td>ASN</td>
<td><code>AS13335</code></td>
</tr>
</tbody>
</table>
<h2 id="country">Country</h2>
<p>Specify a country using two-letter <a href="https://www.iso.org/iso-3166-country-codes.html">ISO-3166-1 alpha-2 codes</a>. Additionally, the Cloudflare dashboard accepts country names. For example:</p>
<ul>
<li><code>US</code></li>
<li><code>CN</code></li>
<li><code>germany</code> (dashboard only)</li>
</ul>
<p>Cloudflare uses the following special country alpha-2 codes that are not part of the ISO:</p>
<ul>
<li><code>T1</code>: <a href="/network/onion-routing/">Tor exit nodes</a> (country name: <code>Tor</code>)</li>
<li><code>XX</code>: Unknown/reserved</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/15726.md")
</aside>
