<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4793.md")
</aside>
<p>Existing <strong>Private Network</strong> applications continue to function and can still be managed. These applications were originally configured with the following steps:</p>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong> &gt; <strong>Add an application</strong>.</p>
</li>
<li>
<p>Select <strong>Private Network</strong>.</p>
</li>
<li>
<p>Name your application.</p>
</li>
<li>
<p>For <strong>Application type</strong>, select <em>Destination IP</em>.</p>
</li>
<li>
<p>For <strong>Value</strong>, enter the IP address for your application (for example, <code>10.128.0.7</code>).</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4792.md")
</aside>
<ol start="6">
<li>
<p>Configure your <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a> visibility and logo.</p>
</li>
<li>
<p>Select <strong>Next</strong>. You will see two auto-generated Gateway Network policies: one that allows access to the destination IP and another that blocks access.</p>
</li>
<li>
<p>Modify the policies to include additional identity-based conditions. For example:</p>
<ul>
<li><strong>Policy 1</strong></li>
</ul>
</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Destination IP</td>
<td>in</td>
<td><code>10.128.0.7</code></td>
<td>And</td>
<td>Allow</td>
</tr>
<tr>
<td>User Email</td>
<td>matches regex</td>
<td><code>.*@example.com</code></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<ul>
<li><strong>Policy 2</strong></li>
</ul>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Destination IP</td>
<td>in</td>
<td><code>10.128.0.7</code></td>
<td>Block</td>
</tr>
</tbody>
</table>
<p>Policies are evaluated in <a href="/cloudflare-one/traffic-policies/order-of-enforcement/#order-of-precedence">numerical order</a>, so a user with an email ending in @example.com will be able to access <code>10.128.0.7</code> while all others will be blocked. For more information on building network policies, refer to our <a href="/cloudflare-one/traffic-policies/network-policies/">dedicated documentation</a>.</p>
<ol start="9">
<li>Select <strong>Add application</strong>.</li>
</ol>
<p>Your application will appear on the <strong>Applications</strong> page.</p>
