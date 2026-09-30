<p>The HTTP Event Collector (HEC) is a reliable method to send log data to SentinelOne Singularity Data Lake. Cloudflare Logpush supports pushing logs directly to SentinelOne HEC via the Cloudflare dashboard or API.</p>
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
<p>In <strong>Select a destination</strong>, choose <strong>SentinelOne</strong>.</p>
</li>
<li>
<p>Enter or select the following destination information:</p>
<ul>
<li><strong>SentinelOne HEC URL</strong></li>
<li><strong>Auth Token</strong> - Event Collector token.</li>
<li><strong>Source Type</strong> - For example, <code>marketplace-cloudflare-latest</code>.</li>
</ul>
</li>
</ol>
<p>When you are done entering the destination details, select <strong>Continue</strong>.</p>
<ol start="6">
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
<p>To set up a SentinelOne Logpush job:</p>
<ol>
<li>Create a job with the appropriate endpoint URL and authentication parameters.</li>
<li>Enable the job to begin pushing logs.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10543.md")
</aside>
<p>Ensure <strong>Log Share</strong> permissions are enabled, before attempting to read or configure a Logpush job. For more information refer to the <a href="/logs/logpush/permissions/#roles">Roles section</a>.</p>
<h3 id="1-create-a-job"><ol>
<li>Create a job</li>
</ol></h3>
<p>To create a job, make a <code>POST</code> request to the Logpush jobs endpoint with the following fields:</p>
<ul>
<li><strong>name</strong> (optional) - Use your domain name as the job name.</li>
<li><strong>destination_conf</strong> - A log destination consisting of an endpoint URL, source type, authorization header in the string format below.
<ul>
<li><strong>&lt;SENTINELONE_ENDPOINT_URL&gt;</strong>: The SentinelOne raw HTTP Event Collector URL with port. For example: <code>sentinelone://ingest.us1.sentinelone.net/services/collector/raw</code>. Cloudflare expects the SentinelOne endpoint to be <code>/services/collector/raw</code> while configuring and setting up the Logpush job.</li>
<li><strong>&lt;SENTINELONE_AUTH_TOKEN&gt;</strong>: The SentinelOne authorization token that is URL-encoded. For example: <code>Bearer 0e6d94e8c-5792-4ad1-be3c-29bcaee0197d</code>.</li>
<li><strong>&lt;SOURCE_TYPE&gt;</strong>: The SentinelOne source type. For example: <code>marketplace-cloudflare-latest</code>.</li>
</ul>
</li>
</ul>
<pre><code class="language-bash">&quot;https://&lt;SENTINELONE_ENDPOINT_URL&gt;?sourcetype=&lt;SOURCE_TYPE&gt;&amp;header_Authorization=&lt;SENTINELONE_AUTH_TOKEN&gt;&quot;&#10;</code></pre>
<ul>
<li>
<p><strong>dataset</strong> - The category of logs you want to receive. Refer to <a href="/logs/logpush/logpush-job/datasets/">Datasets</a> for the full list of supported datasets.</p>
</li>
<li>
<p><strong>output_options</strong> (optional) - To configure fields, sample rate, and timestamp format, refer to <a href="/logs/logpush/logpush-job/log-output-options/">Log Output Options</a>. For timestamp, Cloudflare recommends using <code>timestamps=rfc3339</code>.</p>
</li>
</ul>
<p>Example request using cURL:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/logpush/jobs \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;&lt;DOMAIN_NAME&gt;&quot;,&#10;  &quot;destination_conf&quot;: &quot;sentinelone://&lt;SENTINELONE_ENDPOINT_URL&gt;?sourcetype=&lt;SOURCE_TYPE&gt;&amp;header_Authorization=&lt;SENTINELONE_AUTH_TOKEN&gt;&quot;,&#10;  &quot;output_options&quot;: {&#10;    &quot;field_names&quot;: [&#10;      &quot;ClientIP&quot;,&#10;      &quot;ClientRequestHost&quot;,&#10;      &quot;ClientRequestMethod&quot;,&#10;      &quot;ClientRequestURI&quot;,&#10;      &quot;EdgeEndTimestamp&quot;,&#10;      &quot;EdgeResponseBytes&quot;,&#10;      &quot;EdgeResponseStatus&quot;,&#10;      &quot;EdgeStartTimestamp&quot;,&#10;      &quot;RayID&quot;&#10;    ],&#10;    &quot;timestamp_format&quot;: &quot;rfc3339&quot;&#10;  },&#10;  &quot;dataset&quot;: &quot;http_requests&quot;,&#10;  &quot;enabled&quot;: true&#10;}&#x27;</code></pre>
<p>Response:</p>
<pre><code class="language-json">{&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;id&quot;: &lt;JOB_ID&gt;,&#10;    &quot;dataset&quot;: &quot;http_requests&quot;,&#10;    &quot;kind&quot;: &quot;&quot;,&#10;    &quot;enabled&quot;: true,&#10;    &quot;name&quot;: &quot;&lt;DOMAIN_NAME&gt;&quot;,&#10;    &quot;output_options&quot;: {&#10;      &quot;field_names&quot;: [&quot;ClientIP&quot;, &quot;ClientRequestHost&quot;, &quot;ClientRequestMethod&quot;, &quot;ClientRequestURI&quot;, &quot;EdgeEndTimestamp&quot;,&quot;EdgeResponseBytes&quot;, &quot;EdgeResponseStatus&quot;, &quot;EdgeStartTimestamp&quot;, &quot;RayID&quot;],&#10;      &quot;timestamp_format&quot;: &quot;rfc3339&quot;&#10;    },&#10;    &quot;destination_conf&quot;: &quot;sentinelone://&lt;SENTINELONE_ENDPOINT_URL&gt;?sourcetype=&lt;SOURCE_TYPE&gt;&amp;header_Authorization=&lt;SENTINELONE_AUTH_TOKEN&gt;&quot;,&#10;    &quot;last_complete&quot;: null,&#10;    &quot;last_error&quot;: null,&#10;    &quot;error_message&quot;: null&#10;  },&#10;  &quot;success&quot;: true&#10;}&#10;</code></pre>
<p>Refer to <a href="/logs/logpush/examples/example-logpush-curl/">Manage Logpush with cURL</a> to update a job (including enabling and disabling).</p>
<p>Refer to the <a href="/logs/faq/logpush/">Logpush FAQ</a> for troubleshooting information.</p>
