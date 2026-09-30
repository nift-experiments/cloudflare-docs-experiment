---
cp9:
  canonical: https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/
  description: Configure Logpush jobs via the API.
  full_title: API configuration · Cloudflare Logs docs
  head_html: <title>API configuration · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure Logpush jobs via the API."><link rel="canonical" href="https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/index.md"><meta property="og:title" content="API configuration · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure Logpush jobs via the API."><meta property="og:url" content="https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Logpush"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/#page","headline":"API configuration \u00b7 Cloudflare Logs docs","description":"Configure Logpush jobs via the API.","url":"https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/logpush/logpush-job/api-configuration/
  schema: 1
---
<h2 id="endpoints">Endpoints</h2>
<p>The table below summarizes the job operations available for both Logpush and Edge Log Delivery jobs. Make sure that Account-scoped datasets use <code>/accounts/{account_id}</code> and Zone-scoped datasets use <code>/zone/{zone_id}</code>. For more information, refer to the <a href="/logs/logpush/logpush-job/datasets/">Datasets</a> page.</p>
<p>You can locate <code>{zone_id}</code> and <code>{account_id}</code> arguments based on the <a href="/fundamentals/account/find-account-and-zone-ids/">Find zone and account IDs</a> page.
The <code>{job_id}</code> argument is numeric, like 123456.
The <code>{dataset_id}</code> argument indicates the log category (such as <code>http_requests</code> or <code>audit_logs</code>).</p>
<table>
<thead>
<tr>
<th>Operation</th>
<th>Description</th>
<th>API</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>POST</code></td>
<td>Create job</td>
<td><a href="/api/resources/logpush/subresources/jobs/methods/create/">Documentation</a></td>
</tr>
<tr>
<td><code>GET</code></td>
<td>Retrieve job details</td>
<td><a href="/api/resources/logpush/subresources/datasets/subresources/jobs/methods/get/">Documentation</a></td>
</tr>
<tr>
<td><code>GET</code></td>
<td>Retrieve all jobs for all datasets</td>
<td><a href="/api/resources/logpush/subresources/jobs/methods/list/">Documentation</a></td>
</tr>
<tr>
<td><code>GET</code></td>
<td>Retrieve all jobs for a dataset</td>
<td><a href="/api/resources/logpush/subresources/datasets/subresources/jobs/methods/get/">Documentation</a></td>
</tr>
<tr>
<td><code>GET</code></td>
<td>Retrieve all available fields for a dataset</td>
<td><a href="/api/resources/logpush/subresources/datasets/subresources/fields/methods/get/">Documentation</a></td>
</tr>
<tr>
<td><code>PUT</code></td>
<td>Update job</td>
<td><a href="/api/resources/logpush/subresources/jobs/methods/update/">Documentation</a></td>
</tr>
<tr>
<td><code>DELETE</code></td>
<td>Delete job</td>
<td><a href="/api/resources/logpush/subresources/jobs/methods/delete/">Documentation</a></td>
</tr>
<tr>
<td><code>POST</code></td>
<td>Check whether destination exists</td>
<td><a href="/api/resources/logpush/subresources/validate/methods/destination/">Documentation</a></td>
</tr>
<tr>
<td><code>POST</code></td>
<td>Get ownership challenge</td>
<td><a href="/api/resources/logpush/subresources/ownership/methods/validate/">Documentation</a></td>
</tr>
<tr>
<td><code>POST</code></td>
<td>Validate ownership challenge</td>
<td><a href="/api/resources/logpush/subresources/ownership/methods/validate/">Documentation</a></td>
</tr>
<tr>
<td><code>POST</code></td>
<td>Validate log options</td>
<td><a href="/api/resources/logpush/subresources/validate/methods/origin/">Documentation</a></td>
</tr>
</tbody>
</table>
<p>For concrete examples, refer to the tutorials in <a href="/logs/logpush/examples/">Logpush examples</a>.</p>
<h2 id="connecting">Connecting</h2>
<p>The Logpush API requires credentials like any other Cloudflare API.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/logpush/jobs \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h2 id="ownership">Ownership</h2>
<p>Before creating a new job, ownership of the destination must be proven.</p>
<p>To issue an ownership challenge token to your destination:</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/logpush/ownership \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;destination_conf&quot;: &quot;s3://&lt;BUCKET_PATH&gt;?region=us-west-2&quot;&#10;}&#x27;</code></pre>
<p>A challenge file will be written to the destination, and the filename will be in the response (the filename may be expressed as a path, if appropriate for your destination):</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;valid&quot;: true,&#10;    &quot;message&quot;: &quot;&quot;,&#10;    &quot;filename&quot;: &quot;&lt;PATH_TO_CHALLENGE_FILE&gt;.txt&quot;&#10;  },&#10;  &quot;success&quot;: true&#10;}&#10;</code></pre>
<p>You will need to provide the token contained in the file when creating a job.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/10534.md")
</aside>
<h2 id="destination">Destination</h2>
<p>You can specify your cloud service provider destination via the required <strong>destination_conf</strong> parameter.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note-1">Note</h3>
@markup("md", "content/.markup/bodies/10533.md")
</aside>
<p>The <code>destination_conf</code> parameter must follow this format:</p>
<pre tabindex="0"><code>&lt;scheme&gt;://&lt;destination-address&gt;&#10;</code></pre>
<p>Supported schemes are listed below, each tailored to specific providers such as
R2, S3, etc. Additionally, generic use cases like <code>https</code> are also covered:</p>
<ul>
<li><code>r2</code>,</li>
<li><code>gs</code>,</li>
<li><code>s3</code>,</li>
<li><code>sumo</code>,</li>
<li><code>https</code>,</li>
<li><code>azure</code>,</li>
<li><code>splunk</code>,</li>
<li><code>sentinelone</code>,</li>
<li><code>datadog</code>.</li>
</ul>
<p>The <code>destination-address</code> should generally be provided by the destination
provider. However, for certain providers, we require the <code>destination-address</code>
to follow a specific format:</p>
<ul>
<li><strong>Cloudflare R2</strong> (scheme <code>r2</code>): bucket path + account ID + R2 access key ID + R2 secret access key; for example: <code>r2://&lt;BUCKET_PATH&gt;?account-id=&lt;ACCOUNT_ID&gt;&amp;access-key-id=&lt;R2_ACCESS_KEY_ID&gt;&amp;secret-access-key=&lt;R2_SECRET_ACCESS_KEY&gt;</code></li>
<li><strong>AWS S3</strong> (scheme <code>s3</code>): bucket + optional directory + region + optional encryption parameter (if required by your policy); for example: <code>s3://bucket/[dir]?region=&lt;REGION&gt;[&amp;sse=AES256]</code></li>
<li><strong>Datadog</strong> (scheme <code>datadog</code>): Datadog endpoint URL + Datadog API key + optional parameters; for example: <code>datadog://&lt;DATADOG_ENDPOINT_URL&gt;?header_DD-API-KEY=&lt;DATADOG_API_KEY&gt;&amp;ddsource=cloudflare&amp;service=&lt;SERVICE&gt;&amp;host=&lt;HOST&gt;&amp;ddtags=&lt;TAGS&gt;</code></li>
<li><strong>Google Cloud Storage</strong> (scheme <code>gs</code>): bucket + optional directory; for example: <code>gs://bucket/[dir]</code></li>
<li><strong>Microsoft Azure</strong> (scheme <code>azure</code>): service-level SAS URL with <code>https</code> replaced by <code>azure</code> + optional directory added before query string; for example: <code>azure://&lt;BLOB_CONTAINER_PATH&gt;/[dir]?&lt;QUERY_STRING&gt;</code></li>
<li><strong>New Relic</strong> (use scheme <code>https</code>): New Relic endpoint URL which is <code>https://log-api.newrelic.com/log/v1</code> for US or <code>https://log-api.eu.newrelic.com/log/v1</code> for EU + a license key + a format; for example: for US <code>&quot;https://log-api.newrelic.com/log/v1?Api-Key=&lt;NR_LICENSE_KEY&gt;&amp;format=cloudflare&quot;</code> and for EU <code>&quot;https://log-api.eu.newrelic.com/log/v1?Api-Key=&lt;NR_LICENSE_KEY&gt;&amp;format=cloudflare&quot;</code></li>
<li><strong>Splunk</strong> (scheme <code>splunk</code>): Splunk endpoint URL + Splunk channel ID + insecure-skip-verify flag + Splunk sourcetype + Splunk authorization token; for example: <code>splunk://&lt;SPLUNK_ENDPOINT_URL&gt;?channel=&lt;SPLUNK_CHANNEL_ID&gt;&amp;insecure-skip-verify=&lt;INSECURE_SKIP_VERIFY&gt;&amp;sourcetype=&lt;SOURCE_TYPE&gt;&amp;header_Authorization=&lt;SPLUNK_AUTH_TOKEN&gt;</code></li>
<li><strong>Sumo Logic</strong> (scheme <code>sumo</code>): HTTP source address URL with <code>https</code> replaced by <code>sumo</code>; for example: <code>sumo://&lt;SUMO_ENDPOINT_URL&gt;/receiver/v1/http/&lt;UNIQUE_HTTP_COLLECTOR_CODE&gt;</code></li>
<li><strong>SentinelOne</strong> (scheme <code>sentinelone</code>): SentinelOne endpoint URL + SentinelOne sourcetype + SentinelOne authorization token; for example: <code>sentinelone://&lt;SENTINELONE_ENDPOINT_URL&gt;?sourcetype=&lt;SOURCE_TYPE&gt;&amp;header_Authorization=&lt;SENTINELONE_AUTH_TOKEN&gt;</code></li>
</ul>
<p>For <strong>R2</strong>, <strong>S3</strong>, <strong>Google Cloud Storage</strong>, and <strong>Azure</strong>, you can organize logs into daily subdirectories by including the special placeholder <code>{DATE}</code> in the URL path. This placeholder will automatically be replaced with the date in the <code>YYYYMMDD</code> format (for example, <code>20180523</code>).</p>
<p>For example:</p>
<ul>
<li><code>s3://mybucket/logs/{DATE}?region=us-east-1&amp;sse=AES256</code></li>
<li><code>azure://myblobcontainer/logs/{DATE}?[QueryString]</code></li>
</ul>
<p>This approach is useful when you want your logs grouped by day.</p>
<p>For more information on the value for your cloud storage provider, consult the following conventions:</p>
<ul>
<li><a href="https://docs.aws.amazon.com/cli/latest/reference/s3/index.html">AWS S3 CLI</a> (S3Uri path argument type)</li>
<li><a href="https://cloud.google.com/storage/docs/gsutil">Google Cloud Storage CLI</a> (Syntax for accessing resources)</li>
<li><a href="https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview">Microsoft Azure Shared Access Signature</a></li>
<li><a href="https://help.sumologic.com/03Send-Data/Sources/02Sources-for-Hosted-Collectors/HTTP-Source">Sumo Logic HTTP Source</a></li>
</ul>
<p>To check if a destination is already in use:</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/logpush/validate/destination/exists \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;destination_conf&quot;: &quot;s3://foo&quot;&#10;}&#x27;</code></pre>
<p>Response</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;exists&quot;: false&#10;  },&#10;  &quot;success&quot;: true&#10;}&#10;</code></pre>
<h2 id="name">Name</h2>
<p>A human-readable, optional job name that does not need to be unique. We recommend choosing a meaningful name, such as the domain name, to help you easily identify and manage your job. You can update the name later if needed.</p>
<h2 id="kind">Kind</h2>
<p>The kind parameter (optional) is used to differentiate between Logpush and Edge Log Delivery jobs. For Logpush jobs, this parameter can be left empty or omitted. For Edge Log Delivery jobs, set <code>&quot;kind&quot;: &quot;edge&quot;</code>. Currently, Edge Log Delivery is only supported for the <code>http_requests</code> dataset.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note-2">Note</h3>
@markup("md", "content/.markup/bodies/10532.md")
</aside>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/logpush/jobs \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;&lt;DOMAIN_NAME&gt;&quot;,&#10;  &quot;destination_conf&quot;: &quot;s3://&lt;BUCKET_PATH&gt;?region=us-west-2&quot;,&#10;  &quot;dataset&quot;: &quot;http_requests&quot;,&#10;  &quot;output_options&quot;: {&#10;    &quot;field_names&quot;: [&#10;      &quot;ClientIP&quot;,&#10;      &quot;ClientRequestHost&quot;,&#10;      &quot;ClientRequestMethod&quot;,&#10;      &quot; ClientRequestURI&quot;,&#10;      &quot;EdgeEndTimestamp&quot;,&#10;      &quot;EdgeResponseBytes&quot;,&#10;      &quot;EdgeResponseStatus&quot;,&#10;      &quot;EdgeStartTimestamp&quot;,&#10;      &quot;RayID&quot;&#10;    ],&#10;    &quot;timestamp_format&quot;: &quot;rfc3339&quot;&#10;  },&#10;  &quot;kind&quot;: &quot;edge&quot;&#10;}&#x27;</code></pre>
<h2 id="options">Options</h2>
<p>Logpull_options has been replaced with Custom Log Formatting output_options. Please refer to the <a href="/logs/logpush/logpush-job/log-output-options/">Log Output Options</a> documentation for instructions on configuring these options and updating your existing jobs to use these options.</p>
<p>If you are still using logpull_options, here are the options that you can customize:</p>
<ol>
<li><strong>Fields</strong> (optional): Refer to <a href="/logs/logpush/logpush-job/datasets/">Datasets</a> for the currently available fields. The list of fields is also accessible directly from the API: <code>https://api.cloudflare.com/client/v4/zones/{zone_id}/logpush/datasets/{dataset_id}/fields</code>. Default fields: <code>https://api.cloudflare.com/client/v4/zones/{zone_id}/logpush/datasets/{dataset_id}/fields/default</code>.</li>
<li><strong>Timestamp format</strong> (optional): The format in which timestamp fields will be returned. Value options: <code>unixnano</code> (nanoseconds unit - default), <code>unix</code> (seconds unit), <code>rfc3339</code> (seconds unit).</li>
<li><strong>Redaction for CVE-2021-44228</strong> (optional): This option will replace every occurrence of <code>${</code> with <code>x{</code>.  To enable it, set <code>&quot;CVE-2021-44228&quot;: true</code>.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note-3">Note</h3>
@markup("md", "content/.markup/bodies/10531.md")
</aside>
<p>To check if the selected <strong>logpull_options</strong> are valid:</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/logpush/validate/origin \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;logpull_options&quot;: &quot;fields=RayID,ClientIP,EdgeStartTimestamp&amp;timestamps=rfc3339&amp;CVE-2021-44228=true&quot;,&#10;  &quot;dataset&quot;: &quot;http_requests&quot;&#10;}&#x27;</code></pre>
<p>Response</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;valid&quot;: true,&#10;    &quot;message&quot;: &quot;&quot;&#10;  },&#10;  &quot;success&quot;: true&#10;}&#10;</code></pre>
<h2 id="configuration-change-timing">Configuration change timing</h2>
<p>When you modify a Logpush job configuration, changes do not take effect immediately.</p>
<h3 id="destination-changes">Destination changes</h3>
<p>If you reconfigure a job to use a new destination, logs may continue to be sent to the old destination for approximately 10-15 minutes during the transition period. This delay allows the system to complete in-flight uploads and propagate the new configuration across Cloudflare's network.</p>
<h3 id="field-changes">Field changes</h3>
<p>When you add new fields to an existing Logpush job, the new fields will appear in your logs within approximately 10-15 minutes. This timing is an estimate and may vary based on system load.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10530.md")
</aside>
<h2 id="filter">Filter</h2>
<p>Use filters to select the events to include and/or remove from your logs. For more information, refer to <a href="/logs/logpush/logpush-job/filters/">Filters</a>.</p>
<h2 id="sampling-rate">Sampling rate</h2>
<p>Value can range from <code>0.0</code> (exclusive) to <code>1.0</code> (inclusive). <code>sample=0.1</code> means return 10% (1 in 10) of all records. The default value is <code>1</code>, meaning logs will be unsampled.</p>
<h3 id="understanding-sample-rate-and-sampleinterval">Understanding sample_rate and SampleInterval</h3>
<p>The <code>sample_rate</code> parameter and <code>SampleInterval</code> field are independent mechanisms that operate at different stages of the logging pipeline:</p>
<ul>
<li>
<p><strong><code>sample_rate</code></strong>: A configuration parameter you set on your Logpush job to control what percentage of logs are delivered to your destination (0.0-1.0). For example, setting <code>sample_rate: 0.1</code> delivers approximately 10% of logs.</p>
</li>
<li>
<p><strong><code>SampleInterval</code></strong>: A data field that appears in certain datasets (particularly <a href="/logs/logpush/logpush-job/datasets/account/network_analytics_logs/">Network Analytics Logs</a>) indicating upstream sampling applied during data collection. A <code>SampleInterval</code> of 1000 means the log entry represents 1 in 1000 packets.</p>
</li>
</ul>
<p>The <code>sample_rate</code> you configure applies on top of any pre-existing sampling. If your data already has <code>SampleInterval: 1000</code> and you set <code>sample_rate: 0.1</code>, you receive approximately 1 in 10,000 of the original events (1000 × 10).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10529.md")
</aside>
<h2 id="max-upload-parameters">Max upload parameters</h2>
<p>These parameters control the size of each upload batch — not how quickly data is delivered. Use them to prevent overloading your destination with uploads that are too large or too small.</p>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Description</th>
<th>Default</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>max_upload_bytes</code></td>
<td>Maximum uncompressed file size of a batch of logs.</td>
<td>Varies by destination</td>
</tr>
<tr>
<td><code>max_upload_records</code></td>
<td>Maximum number of log lines per batch.</td>
<td>100,000</td>
</tr>
<tr>
<td><code>max_upload_interval_seconds</code></td>
<td>Maximum time-span of log data per batch (used during catch-up scenarios).</td>
<td>Varies by destination</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10528.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10527.md")
</aside>
<h3 id="when-to-adjust-these-parameters">When to adjust these parameters</h3>
<ul>
<li>Reduce <code>max_upload_records</code> if your destination struggles with large payloads or runs out of memory processing big batches.</li>
<li>Increase <code>max_upload_records</code> if you want fewer, larger files (for example, when pushing to object storage like R2 or S3).</li>
<li>For destinations like Datadog that have strict payload limits, Logpush automatically uses smaller batch sizes (for example, 1,000 rows).</li>
</ul>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/10526.md")
</aside>
<h2 id="custom-fields">Custom fields</h2>
<p>You can add custom fields to your HTTP request log entries in the form of HTTP request headers, HTTP response headers, and cookies. Custom fields configuration applies to all the Logpush jobs in a zone that use the HTTP requests dataset. To learn more, refer to <a href="/logs/logpush/logpush-job/custom-fields/">Custom fields</a>.</p>
<h2 id="audit">Audit</h2>
<p>The following Logpush actions are recorded in <strong>Cloudflare Audit Logs</strong>: create, update, and delete job.</p>
