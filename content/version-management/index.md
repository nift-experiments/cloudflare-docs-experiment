<div class="nb-description">
@markup("md", "content/.markup/bodies/179.md")
</div>
<div class="nb-plan">
<p>Enterprise-only</p>
</div>
<h2 id="benefits">Benefits</h2>
<p>By using Version Management, you can:</p>
<ul>
<li>Create independent versions to make changes with no risk of impacting live traffic.</li>
<li>Safely deploy changes to staging environments ahead of deploy to production.</li>
<li>Quickly roll back deployed changes when issues occur.</li>
</ul>
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
<p>For access, <a href="/version-management/how-to/enable/">enable</a> Zone Versioning in the Cloudflare dashboard.</p>
<h2 id="limitations">Limitations</h2>
<p>Version Management does not currently support or have limited support for the following products or features:</p>
<details class="nb-details"><summary>API Shield</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/180.md")
</div></details>
<details class="nb-details"><summary>Authenticated Origin Pull</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/181.md")
</div></details>
<details class="nb-details"><summary>Cache</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/182.md")
</div></details>
<details class="nb-details"><summary>Cache Rules when used with Cloudflare Images</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/183.md")
</div></details>
<details class="nb-details"><summary>Workers Cache API</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/184.md")
</div></details>
<details class="nb-details"><summary>China Network</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/185.md")
</div></details>
<details class="nb-details"><summary>Cloudflare API</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/186.md")
</div></details>
<details class="nb-details"><summary>Domain-scoped Roles</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/187.md")
</div></details>
<details class="nb-details"><summary>Image Transformations</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/188.md")
</div></details>
<details class="nb-details"><summary>Network Error Logging</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/189.md")
</div></details>
<details class="nb-details"><summary>Client-side security</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/190.md")
</div></details>
<details class="nb-details"><summary>Rules</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/191.md")
</div></details>
<details class="nb-details"><summary>Security Insights</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/192.md")
</div></details>
<details class="nb-details"><summary>Terraform</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/193.md")
</div></details>
<details class="nb-details"><summary>WAF Attack Score</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/194.md")
</div></details>
<details class="nb-details"><summary>Waiting Room</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/195.md")
</div></details>
<details class="nb-details"><summary>Wrangler</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/196.md")
</div></details>
<h2 id="requirements">Requirements</h2>
<p>To use Version Management, the following must all be true:</p>
<ul>
<li>Your zone is on an Enterprise plan.</li>
<li>Your zone is in an <a href="/dns/zone-setups/reference/domain-status/">active</a> state.</li>
<li>Your zone uses <a href="/waf/managed-rules/">WAF managed rules</a>.</li>
<li>Your zone has migrated to use <a href="/waf/custom-rules/">custom rules</a> instead of Firewall Rules (deprecated).</li>
<li>Your account uses the <a href="https://blog.cloudflare.com/new-cloudflare-waf/">new WAF</a> (if not, contact your account team).</li>
<li>Your user account must have a Super Administrator or Administrator <a href="/fundamentals/manage-members/roles/">role</a>. <strong>Zone Versioning</strong> roles cannot create new versions.</li>
<li>Your user account must have an API Key provisioned (if not, <a href="/fundamentals/api/get-started/keys/#view-your-global-api-key">view your API Key</a>).</li>
<li>Your user account must have API Access enabled. Refer to <a href="/fundamentals/api/how-to/control-api-access/">control API Access</a> for more information.</li>
<li>You must use the dashboard to manage versioning.</li>
</ul>
