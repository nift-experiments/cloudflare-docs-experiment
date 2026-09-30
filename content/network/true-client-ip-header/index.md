<p>Enabling the True-Client-IP Header adds the <a href="/fundamentals/reference/http-headers/#true-client-ip-enterprise-plan-only"><code>True-Client-IP</code> header</a> to all requests to your origin server, which includes the end user's IP address.</p>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="add-true-client-ip-header">Add True-Client-IP Header</h2>
<p>The recommended procedure to access client IP information is to <a href="/rules/transform/managed-transforms/reference/#add-true-client-ip-header">enable the <strong>Add &quot;True-Client-IP&quot; header</strong> Managed Transform</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/665.md")
</aside>
<h2 id="additional-resources">Additional resources</h2>
<p>For additional guidance on using True-Client-IP Header with Cloudflare, refer to the following resources:</p>
<ul>
<li><a href="/rules/transform/managed-transforms/reference/#add-true-client-ip-header">Available Managed Transforms</a></li>
<li><a href="/fundamentals/reference/http-headers/#true-client-ip-enterprise-plan-only">Cloudflare HTTP headers</a></li>
<li><a href="/support/troubleshooting/restoring-visitor-ips/restoring-original-visitor-ips/">Restoring original visitor IPs</a></li>
</ul>
