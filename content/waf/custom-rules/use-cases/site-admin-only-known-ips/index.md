<p>If an attack compromises the administrative area of your website, the consequences can be severe. With custom rules, you can protect your site's admin area by blocking requests for access to admin paths that do not come from a known IP address.</p>
<p>This example <a href="/waf/custom-rules/create-dashboard/">custom rule</a> limits access to the WordPress admin area, <code>/wp-admin/</code>, by blocking requests that do not originate from a specified set of IP addresses:</p>
<ul>
<li><strong>When incoming requests match</strong>:</li>
</ul>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
</tr>
</thead>
<tbody>
<tr>
<td>IP Source Address</td>
<td>is not in</td>
<td><code>10.20.30.40</code> <code>192.168.1.0/24</code></td>
<td>And</td>
</tr>
<tr>
<td>URI Path</td>
<td>wildcard</td>
<td><code>/wp-admin/*</code></td>
<td></td>
</tr>
</tbody>
</table>
<p>If you are using the expression editor:<br/>
<code>(not ip.src in {10.20.30.40 192.168.1.0/24} and http.request.uri.path wildcard &quot;/wp-admin/*&quot;)</code></p>
<ul>
<li><strong>Then take action</strong>: <em>Block</em></li>
</ul>
<h2 id="other-resources">Other resources</h2>
<ul>
<li><a href="/waf/custom-rules/use-cases/allow-traffic-from-ips-in-allowlist/">Use case: Allow traffic from IP addresses in allowlist only</a></li>
</ul>
