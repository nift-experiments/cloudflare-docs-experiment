<p>Logs Engine gives you the ability to store your logs in R2 and query them directly.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/802.md")
</aside>
<h2 id="store-logs-in-r2">Store logs in R2</h2>
<ul>
<li>Set up a <a href="/logs/logpush/logpush-job/enable-destinations/r2/">Logpush to R2</a> job.</li>
<li>Create an <a href="/r2/api/tokens/">R2 access key</a> with at least R2 read permissions.</li>
<li>Ensure that you have Logshare read permissions.</li>
<li>Alternatively, create a Cloudflare API token with the following permissions:
<ul>
<li>Account scope</li>
<li>Logs read permissions</li>
</ul>
</li>
</ul>
<h2 id="query-logs">Query logs</h2>
<p>You can use the API to query and download your logs by time range or <a href="/fundamentals/reference/cloudflare-ray-id/">RayID</a>.</p>
<h2 id="authentication">Authentication</h2>
<p>The following headers are required for all API calls:</p>
<ul>
<li><code>X-Auth-Email</code> - the Cloudflare account email address associated with the domain</li>
<li><code>X-Auth-Key</code> - the Cloudflare API key</li>
</ul>
<p>Alternatively, API tokens with Logs edit permissions can also be used for authentication:</p>
<ul>
<li><code>Authorization: Bearer &lt;API_TOKEN&gt;</code></li>
</ul>
<h3 id="required-headers">Required headers</h3>
<p>In addition to the required authentication headers mentioned, the following headers are required for the API to access logs stored in your R2 bucket.</p>
<ul>
<li><code>R2-access-key-id</code> (required) - <a href="/r2/api/tokens/">R2 Access Key Id</a></li>
<li><code>R2-secret-access-key</code> (required) - <a href="/r2/api/tokens/">R2 Secret Access Key</a></li>
</ul>
<h2 id="list-files">List files</h2>
<p>List relevant R2 objects containing logs matching the provided query parameters, using the endpoint <code>GET /accounts/{accountId}/logs/list</code>.</p>
<h3 id="query-parameters">Query parameters</h3>
<ul>
<li>
<p><code>start</code> (required) string (TimestampRFC3339) - Start time in RFC 3339 format, for example <code>start=2022-06-06T16:00:00Z</code>.</p>
</li>
<li>
<p><code>end</code> (required) string (TimestampRFC3339) - End time in RFC 3339 format, for example <code>end=2022-06-06T16:00:00Z</code>.</p>
</li>
<li>
<p><code>bucket</code> (required) string (Bucket) - R2 bucket name, for example <code>bucket=cloudflare-logs</code>.</p>
</li>
<li>
<p><code>prefix</code> string (Prefix) - R2 bucket prefix logs are stored under, for example <code>prefix=http_requests/example.com/{DATE}</code>.</p>
</li>
<li>
<p><code>limit</code> number (Limit) - Maximum number of results to return, for example <code>limit=100</code>.</p>
</li>
</ul>
<h2 id="retrieve-logs-by-time-range">Retrieve logs by time range</h2>
<p>Stream logs stored in R2 that match the provided query parameters, using the endpoint <code>GET /accounts/{accountId}/logs/retrieve</code>.</p>
<h3 id="query-parameters-1">Query parameters</h3>
<ul>
<li>
<p><code>start</code> (required) string (TimestampRFC3339) - Start time in RFC 3339 format, for example <code>start=2022-06-06T16:00:00Z</code></p>
</li>
<li>
<p><code>end</code> (required) string (TimestampRFC3339) - End time in RFC 3339 format, for example <code>end=2022-06-06T16:00:00Z</code></p>
</li>
<li>
<p><code>bucket</code> (required) string (Bucket) - R2 bucket name, for example <code>bucket=cloudflare-logs</code></p>
</li>
<li>
<p><code>prefix</code> string (Prefix) - R2 bucket prefix logs are stored under, for example <code>prefix=http_requests/example.com/{DATE}</code></p>
</li>
</ul>
<h3 id="example-api-request">Example API request</h3>
<pre><code class="language-bash">curl --globoff &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/logs/retrieve?start=2022-06-01T16:00:00Z&amp;end=2022-06-01T16:05:00Z&amp;bucket=cloudflare-logs&amp;prefix=http_requests/example.com/{DATE}&quot; \&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; \&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot; \&#10;&#45;-header &quot;R2-Access-Key-Id: R2_ACCESS_KEY_ID&quot; \&#10;&#45;-header &quot;R2-Secret-Access-Key: R2_SECRET_ACCESS_KEY&quot;&#10;</code></pre>
<p>Results can be piped to a file using <code>&gt; logs.json</code>.</p>
<p>Additionally, if you want to receive the raw GZIP bytes without them being transparently decompressed by your client, include the header <code>--header &quot;Accept-Encoding: gzip&quot;</code>.</p>
<h2 id="retrieve-logs-by-ray-id">​Retrieve logs by Ray ID</h2>
<p>Using your logs stored in R2 - the Logpull RayID Lookup feature allows you to query an indexed time range for the presence of an RayID and return the matching result. This feature is available to users with the Logpull RayID Lookup beta subscription.</p>
<p>The ability to look up a RayID is a two-step process. First, a time range needs to be indexed before being able to request a record by the RayID.</p>
<p>Indexes will automatically expire after seven days of no usage.</p>
<h3 id="index-a-time-range">Index a time range</h3>
<p>Before executing your query, you can specify the time range you would like to index in order to narrow down the scope of the query. In the following example, we index one minute of logs stored in the R2 bucket <code>&quot;cloudflare-logs&quot;</code> under the prefix <code>&quot;http_requests/{DATE}&quot;</code>.</p>
<h3 id="example-api-request-1">Example API request</h3>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{account_id}/logs/rayids/index \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;R2-Access-Key-Id: &lt;R2_ACCESS_KEY_ID&gt;&quot; \&#10;&#45;-header &quot;R2-Secret-Access-Key: &lt;R2_SECRET_ACCESS_KEY&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data-raw &#x27;{&#10;  &quot;start&quot;: &quot;2022-08-16T20:30:00Z&quot;,&#10;  &quot;end&quot;: &quot;2022-08-16T20:31:00&quot;,&#10;  &quot;bucket&quot;: &quot;cloudflare-logs&quot;,&#10;  &quot;prefix&quot;: &quot;http_requests/example.com/{DATE}&quot;&#10;}&#x27;&#10;</code></pre>
<h2 id="lookup-a-rayid">Lookup a RayID</h2>
<p>After indexing a time range, perform a <code>GET</code> request with the RayID. If a matching result is found in the indexed time range, the record will be returned. Note that the parameters have moved from the request body and into the URL. The <code>-g</code> flag is required to avoid the <code>{DATE}</code> parameter from being misinterpreted by cURL.</p>
<h3 id="example-api-request-2">Example API request</h3>
<pre><code class="language-bash">curl --globoff &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/logs/rayids/&lt;RAY_ID&gt;?bucket=cloudflare-logs&amp;prefix=http_requests/example.com/{DATE}&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;R2-Access-Key-Id: &lt;R2_ACCESS_KEY_ID&gt;&quot; \&#10;&#45;-header &quot;R2-Secret-Access-Key: &lt;R2_SECRET_ACCESS_KEY&gt;&quot;&#10;</code></pre>
<h2 id="troubleshooting">Troubleshooting</h2>
<details class="nb-details"><summary>I am getting an error when accessing the API</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/803.md")
</div></details>
<details class="nb-details"><summary>How do I know what time range to index?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/804.md")
</div></details>
<details class="nb-details"><summary>What is the time delay between when an event happens and when I can query for it?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/805.md")
</div></details>
<details class="nb-details"><summary>Does R2 have retention controls?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/806.md")
</div></details>
<details class="nb-details"><summary>Which datasets is Logs Engine compatible with?</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/807.md")
</div></details>
