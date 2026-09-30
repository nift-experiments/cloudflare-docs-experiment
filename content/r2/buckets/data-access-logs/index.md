<p>R2 Data Access Logs provide per-request records for object operations in a bucket. The logs are generally available for R2 buckets without a <a href="/r2/reference/data-location/#jurisdictional-restrictions">jurisdiction</a>.</p>
<p>Data Access Logs differ from <a href="/r2/platform/audit-logs/">Audit Logs</a>, which record bucket configuration changes. They also differ from <a href="/r2/platform/metrics-analytics/">R2 metrics</a>, which provide aggregated request and storage data.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11491.md")
</aside>
<h2 id="supported-interfaces">Supported interfaces</h2>
<p>Data Access Logs record requests from these interfaces:</p>
<table>
<thead>
<tr>
<th>Interface</th>
<th>Source</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>S3</code></td>
<td>Requests through the S3-compatible API.</td>
</tr>
<tr>
<td><code>API</code></td>
<td>Object operations from the Cloudflare dashboard or API.</td>
</tr>
<tr>
<td><code>Workers</code></td>
<td>Object operations through an R2 binding. These events include the Worker script name.</td>
</tr>
<tr>
<td><code>Public</code></td>
<td>Requests to public buckets through <code>r2.dev</code> or custom domains. These requests are unauthenticated.</td>
</tr>
</tbody>
</table>
<h2 id="logged-operations">Logged operations</h2>
<p>Data Access Logs record the following operations:</p>
<table>
<thead>
<tr>
<th>Category</th>
<th>Operations</th>
</tr>
</thead>
<tbody>
<tr>
<td>Read</td>
<td><code>GetObject</code>, <code>HeadObject</code></td>
</tr>
<tr>
<td>Write and copy</td>
<td><code>PutObject</code>, <code>CopyObject</code></td>
</tr>
<tr>
<td>List</td>
<td><code>ListObjectsV1</code>, <code>ListObjectsV2</code></td>
</tr>
<tr>
<td>Multipart upload</td>
<td><code>CreateMultipartUpload</code>, <code>UploadPart</code>, <code>UploadPartCopy</code>, <code>CompleteMultipartUpload</code>, <code>AbortMultipartUpload</code>, <code>ListMultipartUploads</code>, <code>ListParts</code></td>
</tr>
<tr>
<td>Delete</td>
<td><code>DeleteObject</code>, <code>DeleteObjects</code>, <code>DeleteObjectsByPrefix</code></td>
</tr>
</tbody>
</table>
<p>Bucket and configuration operations are not included. Failed requests with an HTTP status code of <code>400</code> or greater are also not included.</p>
<h2 id="turn-on-data-access-logs">Turn on Data Access Logs</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11492.md")
</div>
<p>R2 records new supported operations after you turn on Data Access Logs. Earlier operations are not added retroactively.</p>
<h2 id="view-data-access-logs">View Data Access Logs</h2>
<p>In the <strong>Data Access Logs</strong> section of the bucket settings, select <strong>View logs in Workers Observability</strong>. The <strong>Events</strong> view opens with the <code>r2</code> dataset and current bucket selected for the previous hour.</p>
<p>Use the <a href="/workers/observability/query-builder/">Query Builder</a> to change the time range, add filters, or aggregate events.</p>
<h2 id="turn-off-data-access-logs">Turn off Data Access Logs</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11493.md")
</div>
<h2 id="log-fields">Log fields</h2>
<p>Every event can include these fields:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>$metadata.timestamp</code></td>
<td>Event timestamp in Unix milliseconds.</td>
</tr>
<tr>
<td><code>$metadata.service</code></td>
<td>Bucket name used as the service name.</td>
</tr>
<tr>
<td><code>$metadata.namespace</code></td>
<td>Event namespace. The value is <code>r2</code>.</td>
</tr>
<tr>
<td><code>action</code></td>
<td>R2 operation name.</td>
</tr>
<tr>
<td><code>actor.type</code></td>
<td>Actor type: <code>user</code> or <code>service</code>. Public bucket requests use <code>service</code>.</td>
</tr>
<tr>
<td><code>actor.id</code></td>
<td>Identifier for the authenticated actor. Public bucket requests use <code>public</code>.</td>
</tr>
<tr>
<td><code>actor.email</code></td>
<td>Email address for a user actor.</td>
</tr>
<tr>
<td><code>actor.accessKeyId</code></td>
<td>Access key ID for a request authenticated with AWS Signature Version 4.</td>
</tr>
<tr>
<td><code>bucket</code></td>
<td>Target bucket name.</td>
</tr>
<tr>
<td><code>interface</code></td>
<td>Request interface: <code>S3</code>, <code>API</code>, <code>Workers</code>, or <code>Public</code>.</td>
</tr>
<tr>
<td><code>request.bytes</code></td>
<td>Request <code>Content-Length</code> value in bytes.</td>
</tr>
<tr>
<td><code>response.bytes</code></td>
<td>Response <code>Content-Length</code> value in bytes.</td>
</tr>
<tr>
<td><code>response.errorCode</code></td>
<td>Response error code. This value is <code>NotModified</code> for a <code>304</code> response and <code>null</code> for a <code>2xx</code> response.</td>
</tr>
<tr>
<td><code>response.errorMessage</code></td>
<td>Response error message. This value describes a <code>304</code> response and is <code>null</code> for a <code>2xx</code> response.</td>
</tr>
<tr>
<td><code>requestMetadata.colo</code></td>
<td>Cloudflare data center code, or <code>XXX</code> when the data center is unavailable.</td>
</tr>
</tbody>
</table>
<p>S3-compatible API, Cloudflare API, and public bucket events can also include these fields:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>request.method</code></td>
<td>HTTP request method.</td>
</tr>
<tr>
<td><code>request.uri</code></td>
<td>Request path.</td>
</tr>
<tr>
<td><code>response.status</code></td>
<td>HTTP response status code.</td>
</tr>
<tr>
<td><code>requestMetadata.ip</code></td>
<td>Client IP address.</td>
</tr>
<tr>
<td><code>requestMetadata.userAgent</code></td>
<td>Client user agent.</td>
</tr>
</tbody>
</table>
<p>Workers binding events include this additional field:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>scriptName</code></td>
<td>Name of the Worker script that triggered the operation.</td>
</tr>
</tbody>
</table>
<p>Workers binding events do not include the HTTP method, URI, response status, client IP address, or user agent.</p>
<p>An event can include these operation-specific fields:</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>resource.key</code></td>
<td>Object key.</td>
</tr>
<tr>
<td><code>resource.type</code></td>
<td>Resource type: <code>object</code> or <code>multipart_upload</code>.</td>
</tr>
<tr>
<td><code>resource.size</code></td>
<td>Object size in bytes when available.</td>
</tr>
<tr>
<td><code>resource.uploadId</code></td>
<td>Upload ID for a multipart upload.</td>
</tr>
<tr>
<td><code>sourceResource</code></td>
<td>Source bucket, key, and resource type for a copy operation.</td>
</tr>
<tr>
<td><code>prefix</code></td>
<td>Prefix used by a list or prefix-delete operation.</td>
</tr>
<tr>
<td><code>delimiter</code></td>
<td>Delimiter used by a list operation.</td>
</tr>
<tr>
<td><code>maxKeys</code></td>
<td>Maximum keys requested by an object list operation.</td>
</tr>
<tr>
<td><code>maxUploads</code></td>
<td>Maximum uploads requested by a multipart upload list operation.</td>
</tr>
<tr>
<td><code>objects</code></td>
<td>Object keys included in a bulk delete operation.</td>
</tr>
</tbody>
</table>
<p>The <code>request.bytes</code> and <code>response.bytes</code> fields reflect <code>Content-Length</code> values, not exact transferred-byte measurements. A byte count or resource size of <code>0</code> can mean either zero bytes or that the value was unavailable when R2 created the event.</p>
