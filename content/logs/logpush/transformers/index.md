<p><span class="nb-badge">Beta</span></p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="closed-beta">Closed beta</h3>
@markup("md", "content/.markup/bodies/10468.md")
</aside>
<p>Transformers let you run a SQL query against each batch of records before Logpush delivers them to your destination. Use them to filter records you do not want to store, reshape fields to match a downstream schema, redact sensitive values, compute new fields, or add static metadata.</p>
<p>You write the logic as a single SQL query, attach it to a Logpush job, and Cloudflare runs it on every batch. The <code>FROM</code> clause names the Logpush dataset (for example, <code>http_requests</code> or <code>audit_logs_v2</code>) and field names come from that dataset's schema.</p>
<h2 id="key-features">Key features</h2>
<ul>
<li><strong>SQL-based transforms</strong> - a single-statement SQL query per Logpush job.</li>
<li><strong>Per-record execution</strong> - runs on each NDJSON record before Cloudflare delivers the batch.</li>
<li><strong>Advanced filtering and reshaping</strong> - drop, rename, redact, compute, or tag fields.</li>
<li><strong>Attach and detach without redeploying</strong> - manage transformers from the Cloudflare dashboard or the API.</li>
<li><strong>Version history</strong> - every save creates a new version; older versions remain viewable.</li>
</ul>
<p>Before you begin, you need:</p>
<ul>
<li>A Logpush job that uses the <code>ndjson</code> output format. Transformers are only available for NDJSON jobs, and are supported for both account-scoped and zone-scoped datasets.</li>
<li>An API token with the <code>Logs Write</code> permission for the account.</li>
<li>Familiarity with the <a href="/logs/logpush/logpush-job/datasets/">dataset</a> whose records you plan to transform. Your SQL references its field names directly.</li>
</ul>
<h2 id="access-transformers">Access Transformers</h2>
<p>You can create, preview, attach, and manage transformers through the Cloudflare dashboard or the API.</p>
<h3 id="transformer-studio-ui">Transformer Studio (UI)</h3>
<p>Transformer Studio is the workspace that includes a SQL editor where you write, preview, and manage Transformers. Open it from the Logpush page in the Cloudflare dashboard.</p>
<div class="nb-dash-button"></div>
<p>From Studio you can:</p>
<ul>
<li>Create a new transformer by writing a SQL query against a Logpush dataset.</li>
<li>Preview a transformer against a canned sample record for the target dataset before saving.</li>
<li>Attach a transformer to any eligible Logpush job on the account or zone. Only NDJSON jobs matching the transformer's dataset appear as available attach targets. CSV jobs are not shown.</li>
<li>Detach a transformer from a job.</li>
<li>Save a new version each time you edit and save the SQL. Older versions remain available to view.</li>
<li>Rename a transformer or update its description.</li>
<li>Delete a transformer. A transformer cannot be deleted while any Logpush job references it.</li>
</ul>
<h3 id="api">API</h3>
<p>Every transformer action is available through the Cloudflare API. To authenticate, use an <a href="/fundamentals/api/get-started/create-token/">API token</a> with the <code>Logs Write</code> permission.</p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Method</th>
<th>Endpoint</th>
</tr>
</thead>
<tbody>
<tr>
<td>List transformers</td>
<td><code>GET</code></td>
<td><code>accounts/:account_id/logpush/transformers</code></td>
</tr>
<tr>
<td>Create a transformer</td>
<td><code>POST</code></td>
<td><code>accounts/:account_id/logpush/transformers</code></td>
</tr>
<tr>
<td>Preview a transformer</td>
<td><code>POST</code></td>
<td><code>accounts/:account_id/logpush/transformers/preview</code></td>
</tr>
<tr>
<td>Get a transformer</td>
<td><code>GET</code></td>
<td><code>accounts/:account_id/logpush/transformers/:id</code></td>
</tr>
<tr>
<td>Download SQL</td>
<td><code>GET</code></td>
<td><code>accounts/:account_id/logpush/transformers/:id/content</code></td>
</tr>
<tr>
<td>List versions</td>
<td><code>GET</code></td>
<td><code>accounts/:account_id/logpush/transformers/:id/versions</code></td>
</tr>
<tr>
<td>Update a transformer</td>
<td><code>PUT</code></td>
<td><code>accounts/:account_id/logpush/transformers/:id</code></td>
</tr>
<tr>
<td>Delete a transformer</td>
<td><code>DELETE</code></td>
<td><code>accounts/:account_id/logpush/transformers/:id</code></td>
</tr>
</tbody>
</table>
<p>To attach or detach a transformer from a job, set <code>transformer_id</code> on the Logpush job. Refer to <a href="/logs/logpush/logpush-job/">Logpush job setup</a> for job endpoints.</p>
<h2 id="the-sql-transformer-contract">The SQL transformer contract</h2>
<p>A transformer is a single SQL query. The Logpush dataset is the source table; the query output becomes the delivered record.</p>
<pre><code class="language-sql">SELECT ClientIP, RayID, EdgeResponseStatus&#10;FROM http_requests&#10;WHERE EdgeResponseStatus &gt;= 400&#10;</code></pre>
<p>The <code>FROM</code> table name must match the dataset of the Logpush job the transformer is attached to. If it does not, attachment fails.</p>
<p>Records that do not match the <code>WHERE</code> clause are dropped from the output.</p>
<h3 id="supported-sql">Supported SQL</h3>
<p>Transformers use the same SQL dialect as <a href="/pipelines/sql-reference/">Cloudflare Pipelines</a>. The following operations are supported:</p>
<ul>
<li><strong>Projection</strong> - <code>SELECT</code> specific fields, rename with <code>AS</code>, compute new fields with expressions.</li>
<li><strong>Filtering</strong> - <code>WHERE</code> clauses with the standard comparison, boolean, and null-check operators.</li>
<li><strong>CTEs</strong> - <code>WITH ... AS (...)</code> common table expressions.</li>
<li><strong><code>UNNEST</code></strong> - expand array or list fields into rows.</li>
<li><strong>JSON access</strong> - the <code>-&gt;</code> operator returns a JSON object; <code>-&gt;&gt;</code> returns a string. For example, <code>RequestHeaders -&gt;&gt; 'Host'</code>.</li>
<li><strong>Nested output</strong> - <code>named_struct('key', value, ...)</code> builds a nested JSON object.</li>
<li><strong>Array output</strong> - <code>[value1, value2]</code> builds a JSON array.</li>
<li><strong>Scalar functions</strong> - standard SQL functions including <code>UPPER</code>, <code>LOWER</code>, <code>COALESCE</code>, <code>CAST</code>, <code>extract</code>, and <code>to_timestamp</code>.</li>
</ul>
<h3 id="not-supported">Not supported</h3>
<ul>
<li>Joins</li>
<li>Subqueries</li>
<li>Aggregation (<code>GROUP BY</code>, <code>HAVING</code>, <code>COUNT</code>, <code>SUM</code>)</li>
<li>Window functions</li>
<li><code>ORDER BY</code></li>
<li>Multiple statements - one query per transformer</li>
</ul>
<h3 id="validation">Validation</h3>
<p>Every SQL query is validated against the target dataset's schema before it is saved. Unknown fields, wrong types, invalid syntax, unknown datasets, and unsupported operations are rejected at upload time.</p>
<p>In the dashboard, validation errors appear inline in the editor with line and column numbers. Through the API, they are returned in the <code>errors</code> array of the response.</p>
<h3 id="limits">Limits</h3>
<table>
<thead>
<tr>
<th>Limit</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>SQL query size</td>
<td>10 KB</td>
</tr>
<tr>
<td>Transformer name length</td>
<td>255 bytes</td>
</tr>
<tr>
<td>Transformer description length</td>
<td>4,096 bytes</td>
</tr>
<tr>
<td>Filesystem access from a query</td>
<td>None</td>
</tr>
<tr>
<td>Network access from a query</td>
<td>None</td>
</tr>
<tr>
<td>Batch chunk size</td>
<td>1,000 rows</td>
</tr>
</tbody>
</table>
<h2 id="examples">Examples</h2>
<p>The examples below apply every capability from <a href="#key-features">Key features</a> in a single query. Each keeps a subset of records, reshapes the survivors, and drops fields the downstream pipeline does not need.</p>
<h3 id="filter-and-reshape-audit-log-records">Filter and reshape audit log records</h3>
<p>This transformer keeps only <code>update</code> actions from the audit trail and reshapes the surviving records for downstream delivery. Specifically, it:</p>
<ul>
<li>Excludes every record whose <code>ActionType</code> is not <code>update</code>.</li>
<li>Converts <code>ActionTimestamp</code> from RFC3339 into a Unix epoch integer, renamed <code>unix_ts</code>.</li>
<li>Uppercases <code>ActionType</code> and renames it <code>action_type</code>.</li>
<li>Adds a hardcoded <code>provider</code> field with the value <code>Cloudflare</code>.</li>
<li>Groups <code>ActorType</code>, <code>ActorEmail</code>, and <code>ActorIPAddress</code> into a nested <code>actor</code> object.</li>
<li>Derives a boolean <code>is_zone</code> flag from <code>ResourceType = 'zone'</code>.</li>
<li>Builds a <code>resource_meta</code> array from <code>ResourceType</code> and <code>ResourceID</code>.</li>
<li>Drops <code>ActorID</code>, <code>AccountID</code>, and <code>ActorContext</code> by omission from the <code>SELECT</code>.</li>
</ul>
<p>Input record from the <a href="/logs/logpush/logpush-job/datasets/account/audit_logs_v2/"><code>audit_logs_v2</code></a> dataset:</p>
<pre><code class="language-json">{&#10;  &quot;ActionType&quot;: &quot;update&quot;,&#10;  &quot;ActorEmail&quot;: &quot;user@example.com&quot;,&#10;  &quot;ActorID&quot;: &quot;a1b2c3d4&quot;,&#10;  &quot;ActorIPAddress&quot;: &quot;203.0.113.42&quot;,&#10;  &quot;ActorType&quot;: &quot;user&quot;,&#10;  &quot;ActionTimestamp&quot;: &quot;2026-05-21T15:00:00Z&quot;,&#10;  &quot;AccountID&quot;: &quot;90796717&quot;,&#10;  &quot;ResourceID&quot;: &quot;r1s2t3u4&quot;,&#10;  &quot;ResourceType&quot;: &quot;zone&quot;,&#10;  &quot;ActorContext&quot;: &quot;dashboard&quot;&#10;}&#10;</code></pre>
<p>Transformer:</p>
<pre><code class="language-sql">SELECT&#10;  extract(epoch FROM to_timestamp(ActionTimestamp)) AS unix_ts,&#10;  UPPER(ActionType) AS action_type,&#10;  &#x27;Cloudflare&#x27; AS provider,&#10;  named_struct(&#10;    &#x27;type&#x27;, ActorType,&#10;    &#x27;email&#x27;, ActorEmail,&#10;    &#x27;ip&#x27;, ActorIPAddress&#10;  ) AS actor,&#10;  ResourceType = &#x27;zone&#x27; AS is_zone,&#10;  [ResourceType, ResourceID] AS resource_meta&#10;FROM audit_logs_v2&#10;WHERE ActionType = &#x27;update&#x27;&#10;</code></pre>
<p>Delivered record:</p>
<pre><code class="language-json">{&#10;  &quot;action_type&quot;: &quot;UPDATE&quot;,&#10;  &quot;actor&quot;: {&#10;    &quot;email&quot;: &quot;user@example.com&quot;,&#10;    &quot;ip&quot;: &quot;203.0.113.42&quot;,&#10;    &quot;type&quot;: &quot;user&quot;&#10;  },&#10;  &quot;is_zone&quot;: true,&#10;  &quot;provider&quot;: &quot;Cloudflare&quot;,&#10;  &quot;resource_meta&quot;: [&quot;zone&quot;, &quot;r1s2t3u4&quot;],&#10;  &quot;unix_ts&quot;: 1779375600&#10;}&#10;</code></pre>
<h3 id="filter-and-reshape-http-request-records">Filter and reshape HTTP request records</h3>
<p>This transformer keeps all HTTP traffic <strong>except</strong> health checks, metrics scrapers, and internal-facing hostnames. This is a common pattern for teams that want the full log stream, minus predictable noise. Specifically, it:</p>
<ul>
<li>Excludes every request to <code>internal.example.com</code> and <code>health.example.com</code>.</li>
<li>Excludes every request to paths starting with <code>/healthz</code> or <code>/metrics</code>.</li>
<li>Converts <code>EdgeStartTimestamp</code> from RFC3339 into a Unix epoch integer, renamed <code>unix_ts</code>.</li>
<li>Uppercases <code>ClientRequestMethod</code> and renames it <code>method</code>.</li>
<li>Adds a hardcoded <code>provider</code> field with the value <code>Cloudflare</code>.</li>
<li>Groups <code>ClientRequestHost</code>, <code>ClientRequestPath</code>, and <code>ClientRequestMethod</code> into a nested <code>request</code> object.</li>
<li>Derives a boolean <code>is_server_error</code> flag from <code>EdgeResponseStatus &gt;= 500</code>.</li>
<li>Builds a <code>request_meta</code> array from <code>ClientRequestHost</code> and <code>ClientRequestPath</code>.</li>
<li>Drops <code>ClientIP</code>, <code>ClientRequestUserAgent</code>, <code>RayID</code>, <code>OriginResponseTime</code>, and <code>WAFAction</code> by omission from the <code>SELECT</code>.</li>
</ul>
<p>Input record from the <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/"><code>http_requests</code></a> dataset:</p>
<pre><code class="language-json">{&#10;  &quot;ClientIP&quot;: &quot;203.0.113.42&quot;,&#10;  &quot;ClientRequestHost&quot;: &quot;example.com&quot;,&#10;  &quot;ClientRequestMethod&quot;: &quot;POST&quot;,&#10;  &quot;ClientRequestPath&quot;: &quot;/api/checkout&quot;,&#10;  &quot;ClientRequestUserAgent&quot;: &quot;curl/7.85.0&quot;,&#10;  &quot;EdgeResponseStatus&quot;: 502,&#10;  &quot;EdgeStartTimestamp&quot;: &quot;2026-05-21T15:00:00Z&quot;,&#10;  &quot;RayID&quot;: &quot;8e2a1c60ef9e1c9a&quot;,&#10;  &quot;OriginResponseTime&quot;: 3200000000,&#10;  &quot;WAFAction&quot;: &quot;unknown&quot;&#10;}&#10;</code></pre>
<p>This example assumes <code>EdgeStartTimestamp</code> is delivered as an RFC3339 string. If your job delivers timestamps as Unix nanoseconds, drop the <code>to_timestamp()</code> wrapper and divide by 1e9 instead.</p>
<p>Transformer:</p>
<pre><code class="language-sql">SELECT&#10;  extract(epoch FROM to_timestamp(EdgeStartTimestamp)) AS unix_ts,&#10;  UPPER(ClientRequestMethod) AS method,&#10;  &#x27;Cloudflare&#x27; AS provider,&#10;  named_struct(&#10;    &#x27;host&#x27;, ClientRequestHost,&#10;    &#x27;path&#x27;, ClientRequestPath,&#10;    &#x27;method&#x27;, ClientRequestMethod&#10;  ) AS request,&#10;  EdgeResponseStatus &gt;= 500 AS is_server_error,&#10;  [ClientRequestHost, ClientRequestPath] AS request_meta&#10;FROM http_requests&#10;WHERE ClientRequestHost NOT IN (&#x27;internal.example.com&#x27;, &#x27;health.example.com&#x27;)&#10;  AND ClientRequestPath NOT LIKE &#x27;/healthz%&#x27;&#10;  AND ClientRequestPath NOT LIKE &#x27;/metrics%&#x27;&#10;</code></pre>
<p>Delivered record:</p>
<pre><code class="language-json">{&#10;  &quot;is_server_error&quot;: true,&#10;  &quot;method&quot;: &quot;POST&quot;,&#10;  &quot;provider&quot;: &quot;Cloudflare&quot;,&#10;  &quot;request&quot;: {&#10;    &quot;host&quot;: &quot;example.com&quot;,&#10;    &quot;method&quot;: &quot;POST&quot;,&#10;    &quot;path&quot;: &quot;/api/checkout&quot;&#10;  },&#10;  &quot;request_meta&quot;: [&quot;example.com&quot;, &quot;/api/checkout&quot;],&#10;  &quot;unix_ts&quot;: 1779375600&#10;}&#10;</code></pre>
<h2 id="errors-and-troubleshooting">Errors and troubleshooting</h2>
<h3 id="api-errors">API errors</h3>
<table>
<thead>
<tr>
<th>HTTP</th>
<th>Message</th>
<th>Cause</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>403</code></td>
<td><code>transformer feature is not available for this account</code></td>
<td>Your account does not have access to Transformers. Contact your Cloudflare Account Executive.</td>
</tr>
<tr>
<td><code>400</code></td>
<td><code>missing required field: name</code></td>
<td>Add a <code>name</code> field to the request body.</td>
</tr>
<tr>
<td><code>400</code></td>
<td><code>missing required field: code</code></td>
<td>Add a non-empty <code>code</code> field with your SQL query.</td>
</tr>
<tr>
<td><code>400</code></td>
<td>Schema validation error (unknown column, invalid syntax)</td>
<td>The SQL references a field that does not exist, uses unsupported syntax, or has a type mismatch. Fix the query and retry.</td>
</tr>
<tr>
<td><code>413</code></td>
<td>(request entity too large)</td>
<td>The SQL query exceeds 10 KB. Shorten the query.</td>
</tr>
<tr>
<td><code>400</code></td>
<td><code>transformer N not found for this account</code></td>
<td>The transformer ID does not exist, or belongs to a different account.</td>
</tr>
<tr>
<td><code>400</code></td>
<td><code>transformer N dataset &quot;X&quot; does not match job dataset &quot;Y&quot;</code></td>
<td>The transformer's <code>FROM</code> table does not match the job's dataset.</td>
</tr>
</tbody>
</table>
<h3 id="runtime-failures">Runtime failures</h3>
<p>If a transformer fails while processing a batch, the batch fails: nothing is delivered for it, an error is recorded on the Logpush job, and Logpush retries the batch on its normal schedule. There is no automatic raw-log fallback.</p>
<p>If failures continue, records in the affected batches are eventually dropped and cannot be recovered.</p>
<p>The last error appears on the job's <code>last_error</code> field. Common causes:</p>
<ul>
<li><strong>The output exceeded the size limit.</strong> Reduce output per record or drop more records with <code>WHERE</code>.</li>
<li><strong>An internal Cloudflare error occurred.</strong> Contact Cloudflare Support with the job ID and timestamp.</li>
</ul>
<p>To debug, open the transformer in <a href="#transformer-studio-ui">Transformer Studio</a> and use the <strong>Run</strong> button to preview it against a sample record. Validation and execution logic are the same, so problems visible in production usually reproduce in preview.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/logs/logpush/logpush-job/datasets/">Logpush datasets</a> - the fields your SQL queries reference</li>
<li><a href="/logs/logpush/logpush-job/">Logpush job setup</a> - creating and managing Logpush jobs</li>
<li><a href="/logs/reference/log-fields/">Log fields reference</a> - full field descriptions across datasets</li>
<li><a href="/logs/logpush/logpush-job/filters/">Filters</a> - simpler filtering without SQL</li>
</ul>
