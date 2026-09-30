<p>By default, Cloudflare China Network resolves each DNS request at the data center closest to the client. For clients outside of Mainland China, the closest global Cloudflare data center handles the request. For clients in Mainland China, a JD Cloud data center handles the request.</p>
<h2 id="in-china-nameserver">In-China Nameserver</h2>
<p>Cloudflare can deploy DNS service in Mainland China to improve Time to First Byte (TTFB) performance. With this option enabled, DNS queries resolve at data centers in Mainland China instead of at global DNS servers.</p>
<h2 id="when-to-use">When to use</h2>
<p>Before you enable China Authoritative DNS, confirm that the majority (over 90%) of your traffic comes from Mainland China.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3955.md")
</aside>
<h2 id="comparison">Comparison</h2>
<p>The following table compares the default DNS offering with the In-China Nameserver option.</p>
<table>
<thead>
<tr>
<th>DNS option</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td>Default</td>
<td>Uses the DNS server closest to the end user.</td>
</tr>
<tr>
<td>In-China DNS</td>
<td>Uses only DNS in China, operated by JD Cloud.</td>
</tr>
</tbody>
</table>
<h2 id="general-setup">General setup</h2>
<p>After you <a href="/china-network/get-started/">enable the Cloudflare China Network service</a>, do the following:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3958.md")
</div>
<p>For further assistance, contact your account team.</p>
