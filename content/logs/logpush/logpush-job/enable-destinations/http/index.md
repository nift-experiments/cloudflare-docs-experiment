<p>Cloudflare Logpush now supports the ability to send logs to configurable HTTP endpoints.</p>
<p>Note that when using Logpush to HTTP endpoints, Cloudflare customers are expected to perform their own authentication of the pushed logs. For example, customers may specify a secret token in the URL or an HTTP header of the Logpush destination.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="endpoint-requirements">Endpoint requirements</h3>
@markup("md", "content/.markup/bodies/10559.md")
</aside>
<h2 id="manage-via-the-cloudflare-dashboard">Manage via the Cloudflare dashboard</h2>
<ol>
<li>
<p>In the Cloudflare dashboard, go to the <strong>Logpush</strong> page at the account or or domain (also known as zone) level.</p>
<p>For account: <div class="nb-dash-button"></div></p>
<p>For domain (also known as zone): <div class="nb-dash-button"></div></p>
</li>
<li>
<p>Depending on your choice, you have access to <a href="/logs/logpush/logpush-job/datasets/account/">account-scoped datasets</a> and <a href="/logs/logpush/logpush-job/datasets/zone/">zone-scoped datasets</a>, respectively.</p>
</li>
<li>
<p>Select <strong>Create a Logpush job</strong>.</p>
</li>
<li>
<p>In <strong>Select a destination</strong>, choose <strong>HTTP destination</strong>.</p>
</li>
<li>
<p>Enter the <strong>HTTP endpoint</strong> where you want to send the logs to, and select <strong>Continue</strong>. - You can use <code>&quot;header_*&quot;</code> URL parameters to set request headers, for example, to pass an authentication token to your HTTP endpoint.</p>
</li>
<li>
<p>Select the dataset to push to the storage service.</p>
</li>
<li>
<p>In the next step, you need to configure your logpush job:</p>
<ul>
<li>Enter the <strong>Job name</strong>.</li>
<li>Under <strong>If logs match</strong>, you can select the events to include and/or remove from your logs. Refer to <a href="/logs/logpush/logpush-job/filters/">Filters</a> for more information. Not all datasets have this option available.</li>
<li>In <strong>Send the following fields</strong>, you can choose to either push all logs to your storage destination or selectively choose which logs you want to push.</li>
</ul>
</li>
<li>
<p>In <strong>Advanced Options</strong>, you can:</p>
<ul>
<li>Choose the format of timestamp fields in your logs (<code>RFC3339</code> (default), <code>Unix</code>, or <code>UnixNano</code>).</li>
<li>Select a <a href="/logs/logpush/logpush-job/api-configuration/#sampling-rate">sampling rate</a> for your logs or push a randomly-sampled percentage of logs.</li>
<li>Enable redaction for <code>CVE-2021-44228</code>. This option will replace every occurrence of <code>${</code> with <code>x{</code>.</li>
</ul>
</li>
<li>
<p>Select <strong>Submit</strong> once you are done configuring your logpush job.</p>
</li>
</ol>
<h2 id="manage-via-api">Manage via API</h2>
<p>To create a Logpush job, make a <code>POST</code> request to the <a href="/logs/logpush/logpush-job/api-configuration/">Logpush job creation endpoint URL</a> with the appropriate parameters.</p>
<p>The supported parameters are as follows:</p>
<ul>
<li>Fields that are unchanged from other sources:
<ul>
<li><strong>dataset</strong> (required): For example, <code>http_requests</code>.</li>
<li><strong>name</strong> (optional): We suggest using your domain name as the job name.</li>
<li><strong>output_options</strong> (optional): Refer to <a href="/logs/logpush/logpush-job/log-output-options/">Log Output Options</a> to configure fields, sample rate, and timestamp format.</li>
</ul>
</li>
<li>Unique fields:
<ul>
<li><strong>destination_conf</strong>: Where to send the logs. This consists of an endpoint URL and HTTP headers used.
<ul>
<li>Any <code>&quot;header_*&quot;</code> URL parameters will be used to set request headers.
<ul>
<li>The HTTPS endpoint cannot have custom URL parameters that conflicts with any <code>&quot;header_*&quot;</code> URL parameters you have set.</li>
<li>These parameters must be properly URL-encoded (that is, use <code>&quot;%20&quot;</code> for a whitespace), otherwise some special characters may be decoded incorrectly.</li>
</ul>
</li>
<li><code>destination_conf</code> may have more URL parameters in addition to special <code>&quot;header_*&quot;</code> parameters.
<ul>
<li>Non URL-encoded special characters will be encoded when uploading.</li>
</ul>
</li>
<li>Example: <code>https://logs.example.com?header_Authorization=Basic%20REDACTED&amp;tags=host:theburritobot.com,dataset:http_requests</code></li>
</ul>
</li>
<li><strong>max_upload_bytes</strong> (optional): The maximum uncompressed file size of a batch of logs. This setting value must be between 5 MB and 1 GB. Note that you cannot set a minimum file size; this means that log files may be much smaller than this batch size.</li>
<li><strong>max_upload_records</strong> (optional): The maximum number of log lines per batch. This setting must be between 1,000 and 1,000,000 lines. Note that you cannot to specify a minimum number of log lines per batch; this means that log files may contain many fewer lines than this.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/10558.md")
</aside>
<p>Example request using cURL:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/logpush/jobs \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;&lt;DOMAIN_NAME&gt;&quot;,&#10;  &quot;destination_conf&quot;: &quot;https://logs.example.com?header_Authorization=Basic%20REDACTED&amp;tags=host:theburritobot.com,dataset:http_requests&quot;,&#10;  &quot;output_options&quot;: {&#10;    &quot;field_names&quot;: [&#10;      &quot;ClientIP&quot;,&#10;      &quot;ClientRequestHost&quot;,&#10;      &quot;ClientRequestMethod&quot;,&#10;      &quot;ClientRequestURI&quot;,&#10;      &quot;EdgeEndTimestamp&quot;,&#10;      &quot;EdgeResponseBytes&quot;,&#10;      &quot;EdgeResponseStatus&quot;,&#10;      &quot;EdgeStartTimestamp&quot;,&#10;      &quot;RayID&quot;&#10;    ],&#10;    &quot;timestamp_format&quot;: &quot;rfc3339&quot;&#10;  },&#10;  &quot;max_upload_bytes&quot;: 5000000,&#10;  &quot;max_upload_records&quot;: 1000,&#10;  &quot;dataset&quot;: &quot;http_requests&quot;,&#10;  &quot;enabled&quot;: true&#10;}&#x27;</code></pre>
<p>Response:</p>
<pre><code class="language-json">{&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;id&quot;: &lt;JOB_ID&gt;,&#10;    &quot;dataset&quot;: &quot;http_requests&quot;,&#10;    &quot;kind&quot;: &quot;&quot;,&#10;    &quot;max_upload_bytes&quot;: 5000000,&#10;    &quot;max_upload_records&quot;: 1000,&#10;    &quot;enabled&quot;: true,&#10;    &quot;name&quot;: &quot;&lt;DOMAIN_NAME&gt;&quot;,&#10;    &quot;output_options&quot;: {&#10;      &quot;field_names&quot;: [&quot;ClientIP&quot;, &quot;ClientRequestHost&quot;, &quot;ClientRequestMethod&quot;, &quot;ClientRequestURI&quot;, &quot;EdgeEndTimestamp&quot;, &quot;EdgeResponseBytes&quot;, &quot;EdgeResponseStatus&quot; ,&quot;EdgeStartTimestamp&quot;, &quot;RayID&quot;],&#10;      &quot;timestamp_format&quot;: &quot;rfc3339&quot;&#10;    },&#10;    &quot;destination_conf&quot;: &quot;https://logs.example.com?header_Authorization=Basic%20REDACTED&amp;tags=host:theburritobot.com,dataset:http_requests&quot;,&#10;    &quot;last_complete&quot;: null,&#10;    &quot;last_error&quot;: null,&#10;    &quot;error_message&quot;: null&#10;  },&#10;  &quot;success&quot;: true&#10;}&#10;</code></pre>
<p>Refer to <a href="/logs/logpush/examples/example-logpush-curl/">Manage Logpush with cURL</a> to update a job (including enabling and disabling).</p>
