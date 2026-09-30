<p>R2 exposes analytics that allow you to inspect the requests and storage of the buckets in your account.</p>
<p>The metrics displayed for a bucket in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> are queried from Cloudflare's <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. You can access the metrics <a href="#query-via-the-graphql-api">programmatically</a> via GraphQL or HTTP client.</p>
<h2 id="metrics">Metrics</h2>
<p>R2 currently has two datasets:</p>
<table>
<thead>
<tr>
<th>Dataset</th>
<th>GraphQL Dataset Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Operations</td>
<td><code>r2OperationsAdaptiveGroups</code></td>
<td>This dataset consists of the operations taken on a bucket within an account.</td>
</tr>
<tr>
<td>Storage</td>
<td><code>r2StorageAdaptiveGroups</code></td>
<td>This dataset consists of the storage of a bucket within an account.</td>
</tr>
</tbody>
</table>
<h3 id="operations-dataset">Operations Dataset</h3>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>actionType</td>
<td>The name of the operation performed.</td>
</tr>
<tr>
<td>actionStatus</td>
<td>The status of the operation. Can be <code>success</code>, <code>userError</code>, or <code>internalError</code>.</td>
</tr>
<tr>
<td>bucketName</td>
<td>The bucket this operation was performed on if applicable. For buckets with a jurisdiction specified, you must include the jurisdiction followed by an underscore before the bucket name. For example: <code>eu_your-bucket-name</code></td>
</tr>
<tr>
<td>objectName</td>
<td>The object this operation was performed on if applicable.</td>
</tr>
<tr>
<td>responseStatusCode</td>
<td>The http status code returned by this operation.</td>
</tr>
<tr>
<td>datetime</td>
<td>The time of the request.</td>
</tr>
</tbody>
</table>
<h3 id="storage-dataset">Storage Dataset</h3>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>bucketName</td>
<td>The bucket this storage value is for. For buckets with a jurisdiction specified, you must include the <a href="https://developers.cloudflare.com/r2/reference/data-location/#jurisdictional-restrictions">jurisdiction</a> followed by an underscore before the bucket name. For example: <code>eu_your-bucket-name</code></td>
</tr>
<tr>
<td>payloadSize</td>
<td>The size of the objects in the bucket.</td>
</tr>
<tr>
<td>metadataSize</td>
<td>The size of the metadata of the objects in the bucket.</td>
</tr>
<tr>
<td>objectCount</td>
<td>The number of objects in the bucket.</td>
</tr>
<tr>
<td>uploadCount</td>
<td>The number of pending multipart uploads in the bucket.</td>
</tr>
<tr>
<td>datetime</td>
<td>The time that this storage value represents.</td>
</tr>
</tbody>
</table>
<p>Metrics can be queried (and are retained) for the past 31 days. These datasets require an <code>accountTag</code> filter with your Cloudflare account ID.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="querying-buckets-with-jurisdiction-restriction">Querying buckets with jurisdiction restriction</h3>
@markup("md", "content/.markup/bodies/11375.md")
</aside>
<h2 id="view-via-the-dashboard">View via the dashboard</h2>
<p>Per-bucket analytics for R2 are available in the Cloudflare dashboard. To view current and historical metrics for a bucket:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2 object storage</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your bucket.</li>
<li>Select the <strong>Metrics</strong> tab.</li>
</ol>
<p>You can optionally select a time window to query. This defaults to the last 24 hours.</p>
<h2 id="query-via-the-graphql-api">Query via the GraphQL API</h2>
<p>You can programmatically query analytics for your R2 buckets via the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. This API queries the same dataset as the Cloudflare dashboard, and supports GraphQL <a href="/analytics/graphql-api/features/discovery/introspection/">introspection</a>.</p>
<h2 id="examples">Examples</h2>
<h3 id="operations">Operations</h3>
<p>To query the volume of each operation type on a bucket for a given time period you can run a query as such</p>
<pre><code class="language-graphql">query R2VolumeExample(&#10;	$accountTag: string!&#10;	$startDate: Time&#10;	$endDate: Time&#10;	$bucketName: string&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			r2OperationsAdaptiveGroups(&#10;				limit: 10000&#10;				filter: {&#10;					datetime_geq: $startDate&#10;					datetime_leq: $endDate&#10;					bucketName: $bucketName&#10;				}&#10;			) {&#10;				sum {&#10;					requests&#10;				}&#10;				dimensions {&#10;					actionType&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>The <code>bucketName</code> field can be removed to get an account level overview of operations. The volume of operations can be broken down even further by adding more dimensions to the query.</p>
<h3 id="storage">Storage</h3>
<p>To query the storage of a bucket over a given time period you can run a query as such.</p>
<pre><code class="language-graphql">query R2StorageExample(&#10;	$accountTag: string!&#10;	$startDate: Time&#10;	$endDate: Time&#10;	$bucketName: string&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			r2StorageAdaptiveGroups(&#10;				limit: 10000&#10;				filter: {&#10;					datetime_geq: $startDate&#10;					datetime_leq: $endDate&#10;					bucketName: $bucketName&#10;				}&#10;				orderBy: [datetime_DESC]&#10;			) {&#10;				max {&#10;					objectCount&#10;					uploadCount&#10;					payloadSize&#10;					metadataSize&#10;				}&#10;				dimensions {&#10;					datetime&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
