<div class="nb-description">
@markup("md", "content/.markup/bodies/827.md")
</div>
<p>Log Explorer is Cloudflare's native observability and forensics product that enables security teams and developers to analyze, investigate, and monitor issues directly from the Cloudflare dashboard, without the expense and complexity of forwarding logs to third-party tools.</p>
<p>Log Explorer provides access to Cloudflare logs with all the context available within the Cloudflare platform. You can monitor security and performance issues with custom dashboards or investigate and troubleshoot issues with log search. Benefits include:</p>
<ul>
<li><strong>Reduced cost and complexity</strong>: Drastically reduce the expense and operational overhead associated with forwarding, storing, and analyzing terabytes of log data in external tools.</li>
<li><strong>Faster detection and triage</strong>: Access Cloudflare-native logs directly, eliminating cumbersome data pipelines and the ingest lags that delay critical security insights.</li>
<li><strong>Accelerated investigations with full context</strong>: Investigate incidents with Cloudflare's unparalleled contextual data, accelerating your analysis and understanding of &quot;What exactly happened?&quot; and &quot;How did it happen?&quot;</li>
<li><strong>Minimal recovery time</strong>: Seamlessly transition from investigation to action with direct mitigation capabilities via the Cloudflare platform.</li>
</ul>
<p>Contract customers can choose to store their logs in Log Explorer for up to two years, at an additional cost of $0.10 per GB per month. Customers interested in this feature can contact their account team to have it added to their contract.</p>
<h2 id="permissions">Permissions</h2>
<p>Access to Log Explorer features is controlled through specific permissions. Each permission grants users the ability to perform certain actions, such as querying logs, managing datasets, or creating dashboards.</p>
<table>
<thead>
<tr>
<th>Feature</th>
<th>Required Permission</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Manage datasets</strong></td>
<td><code>Logs Edit</code></td>
<td>Add, enable, or disable datasets.</td>
</tr>
<tr>
<td><strong>Log Search</strong></td>
<td><code>Logs Read</code></td>
<td>Query logs in the dashboard or via API.</td>
</tr>
<tr>
<td><strong>Log Search (save query)</strong></td>
<td><code>Logs Write</code></td>
<td>Save log search queries.</td>
</tr>
<tr>
<td><strong>Custom dashboards</strong></td>
<td><code>Analytics Read</code></td>
<td>Create and view custom dashboards.</td>
</tr>
</tbody>
</table>
<p>These permissions apply across both the dashboard and the API, and must be granted at either the account or zone level depending on which datasets you need to access.</p>
<p>Authentication with the API can be done via an API token or API key with an email. Refer to <a href="/fundamentals/api/get-started/create-token/">Create API token</a> for further instructions.</p>
<h2 id="features">Features</h2>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/828.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/829.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/830.md")
</div>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/831.md")
</div>
<h2 id="related-products">Related products</h2>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/832.md")
</div>
<div class="nb-data-component" data-cf-component="RelatedProduct">
@markup("md", "content/.markup/bodies/833.md")
</div>
