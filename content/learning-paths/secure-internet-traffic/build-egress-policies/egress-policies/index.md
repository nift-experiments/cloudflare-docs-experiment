<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10211.md")
</aside>
<p>Egress policies allow you to determine whether your organization's traffic egresses via the default Cloudflare IP or via a <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/">dedicated egress IP</a> assigned to your account.</p>
<p>To create a new egress policy:</p>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Egress policies</strong>.</p>
</li>
<li>
<p>Select <strong>Add a policy</strong>.</p>
</li>
<li>
<p>Name the policy.</p>
</li>
<li>
<p>Build a logical expression that defines the traffic you want to control egress for. For example, you can add a policy to configure all traffic destined for a third-party network to use a static source IP:</p>
</li>
</ol>
<table>
<thead>
<tr>
<th>Policy name</th>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Egress method</th>
</tr>
</thead>
<tbody>
<tr>
<td>Access third-party provider</td>
<td>Destination IP</td>
<td>is</td>
<td><code>198.51.100.158</code></td>
<td>Dedicated Cloudflare egress IPs</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>Primary IPv4 address</th>
<th>IPv6 address</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>203.0.113.88</code></td>
<td><code>2001:db8::/32</code></td>
</tr>
</tbody>
</table>
<ol start="5">
<li>Select <strong>Create policy</strong>.</li>
</ol>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/egress-policies/">Egress policies</a>.</p>
