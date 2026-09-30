<p><a href="/fundamentals/account/account-security/review-audit-logs/">Audit logs</a> provide a comprehensive summary of changes made within your Cloudflare account, including those made to R2 buckets. This functionality is available on all plan types, free of charge, and is always enabled.</p>
<h2 id="viewing-audit-logs">Viewing audit logs</h2>
<p>To view audit logs for your R2 buckets, go to the <strong>Audit logs</strong> page.</p>
<div class="nb-dash-button"></div>
<p>For more information on how to access and use audit logs, refer to <a href="/fundamentals/account/account-security/review-audit-logs/">Review audit logs</a>.</p>
<h2 id="logged-operations">Logged operations</h2>
<p>The following configuration actions are logged:</p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>CreateBucket</td>
<td>Creation of a new bucket.</td>
</tr>
<tr>
<td>DeleteBucket</td>
<td>Deletion of an existing bucket.</td>
</tr>
<tr>
<td>AddCustomDomain</td>
<td>Addition of a custom domain to a bucket.</td>
</tr>
<tr>
<td>RemoveCustomDomain</td>
<td>Removal of a custom domain from a bucket.</td>
</tr>
<tr>
<td>ChangeBucketVisibility</td>
<td>Change to the managed public access (<code>r2.dev</code>) settings of a bucket.</td>
</tr>
<tr>
<td>PutBucketStorageClass</td>
<td>Change to the default storage class of a bucket.</td>
</tr>
<tr>
<td>PutBucketLifecycleConfiguration</td>
<td>Change to the object lifecycle configuration of a bucket.</td>
</tr>
<tr>
<td>DeleteBucketLifecycleConfiguration</td>
<td>Deletion of the object lifecycle configuration for a bucket.</td>
</tr>
<tr>
<td>PutBucketCors</td>
<td>Change to the CORS configuration for a bucket.</td>
</tr>
<tr>
<td>DeleteBucketCors</td>
<td>Deletion of the CORS configuration for a bucket.</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11377.md")
</aside>
<h2 id="example-log-entry">Example log entry</h2>
<p>Below is an example of an audit log entry showing the creation of a new bucket:</p>
<pre><code class="language-json">{&#10;	&quot;action&quot;: { &quot;info&quot;: &quot;CreateBucket&quot;, &quot;result&quot;: true, &quot;type&quot;: &quot;create&quot; },&#10;	&quot;actor&quot;: {&#10;		&quot;email&quot;: &quot;&lt;ACTOR_EMAIL&gt;&quot;,&#10;		&quot;id&quot;: &quot;3f7b730e625b975bc1231234cfbec091&quot;,&#10;		&quot;ip&quot;: &quot;fe32:43ed:12b5:526::1d2:13&quot;,&#10;		&quot;type&quot;: &quot;user&quot;&#10;	},&#10;	&quot;id&quot;: &quot;5eaeb6be-1234-406a-87ab-1971adc1234c&quot;,&#10;	&quot;interface&quot;: &quot;API&quot;,&#10;	&quot;metadata&quot;: { &quot;zone_name&quot;: &quot;r2.cloudflarestorage.com&quot; },&#10;	&quot;newValue&quot;: &quot;&quot;,&#10;	&quot;newValueJson&quot;: {},&#10;	&quot;oldValue&quot;: &quot;&quot;,&#10;	&quot;oldValueJson&quot;: {},&#10;	&quot;owner&quot;: { &quot;id&quot;: &quot;1234d848c0b9e484dfc37ec392b5fa8a&quot; },&#10;	&quot;resource&quot;: { &quot;id&quot;: &quot;my-bucket&quot;, &quot;type&quot;: &quot;r2.bucket&quot; },&#10;	&quot;when&quot;: &quot;2024-07-15T16:32:52.412Z&quot;&#10;}&#10;</code></pre>
