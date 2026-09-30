<p>Cloudflare Logpush supports pushing logs directly to New Relic via the Cloudflare dashboard or via API.</p>
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
<p>In <strong>Select a destination</strong>, choose <strong>New Relic</strong>.</p>
</li>
<li>
<p>Enter the <strong>New Relic Logs Endpoint</strong>:</p>
</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10554.md")
</div></div>
<p>Use the region that matches the one that has been set on your New Relic account. The <strong>License key</strong> field can be found on the New Relic dashboard. It can be retrieved by following <a href="https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/#manage-license-key">these steps</a>.</p>
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
<p>Ensure <strong>Log Share</strong> permissions are enabled, before attempting to read or configure a Logpush job. For more information refer to the <a href="/logs/logpush/permissions/#roles">Roles section</a>.</p>
<h3 id="1-create-a-job"><ol>
<li>Create a job</li>
</ol></h3>
<p>To create a job, make a <code>POST</code> request to the Logpush jobs endpoint with the following fields:</p>
<ul>
<li>
<p><strong>name</strong> (optional) - Use your domain name as the job name.</p>
</li>
<li>
<p><strong>output_options</strong> (optional) - To configure fields, sample rate, and timestamp format, refer to <a href="/logs/logpush/logpush-job/log-output-options/">Log Output Options</a>.</p>
</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/10551.md")
</aside>
<ul>
<li>
<p><strong>destination_conf</strong> - A log destination consisting of an endpoint URL, a license key and a format in the string format below.</p>
<ul>
<li>
<p><strong>&lt;NR_ENDPOINT_URL&gt;</strong>: The New Relic HTTP logs intake endpoint, which is <code>https://log-api.newrelic.com/log/v1</code> for US or <code>https://log-api.eu.newrelic.com/log/v1</code> for the EU, depending on the region that has been set on your New Relic account.</p>
</li>
<li>
<p><strong>&lt;NR_LICENSE_KEY&gt;</strong>: This key can be found on the New Relic dashboard and it can be retrieved by following <a href="https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/#manage-license-key">these steps</a>.</p>
</li>
<li>
<p><strong>format</strong>: The format is <code>cloudflare</code>.</p>
<p>US: <code>&quot;https://log-api.newrelic.com/log/v1?Api-Key=&lt;NR_LICENSE_KEY&gt;&amp;format=cloudflare&quot;</code></p>
<p>EU: <code>&quot;https://log-api.eu.newrelic.com/log/v1?Api-Key=&lt;NR_LICENSE_KEY&gt;&amp;format=cloudflare&quot;</code></p>
</li>
</ul>
</li>
<li>
<p><strong>max_upload_records</strong> (optional) - The maximum number of log lines per batch. This must be at least 1,000 lines or more. Note that there is no way to specify a minimum number of log lines per batch. This means that log files may contain many fewer lines than specified.</p>
</li>
<li>
<p><strong>max_upload_bytes</strong> (optional) - The maximum uncompressed file size of a batch of logs. This must be at least 5 MB. Note that there is no way to set a minimum file size. This means that log files may be much smaller than this batch size. Nevertheless, it is recommended to set this parameter to 5,000,000.</p>
</li>
<li>
<p><strong>dataset</strong> - The category of logs you want to receive. Refer to <a href="/logs/logpush/logpush-job/datasets/">Datasets</a> for the full list of supported datasets.</p>
</li>
</ul>
<p>Example request using cURL:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/logpush/jobs \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;&lt;DOMAIN_NAME&gt;&quot;,&#10;  &quot;output_options&quot;: {&#10;    &quot;field_names&quot;: [&#10;      &quot;ClientIP&quot;,&#10;      &quot;ClientRequestHost&quot;,&#10;      &quot;ClientRequestMethod&quot;,&#10;      &quot;ClientRequestURI&quot;,&#10;      &quot;EdgeEndTimestamp&quot;,&#10;      &quot;EdgeResponseBytes&quot;,&#10;      &quot;EdgeResponseStatus&quot;,&#10;      &quot;EdgeStartTimestamp&quot;,&#10;      &quot;RayID&quot;&#10;    ],&#10;    &quot;timestamp_format&quot;: &quot;unix&quot;&#10;  },&#10;  &quot;destination_conf&quot;: &quot;https://log-api.newrelic.com/log/v1?Api-Key=&lt;NR_LICENSE_KEY&gt;&amp;format=cloudflare&quot;,&#10;  &quot;max_upload_bytes&quot;: 5000000,&#10;  &quot;dataset&quot;: &quot;http_requests&quot;,&#10;  &quot;enabled&quot;: true&#10;}&#x27;</code></pre>
<p>Response:</p>
<pre><code class="language-json">{&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;id&quot;: &lt;JOB_ID&gt;,&#10;    &quot;dataset&quot;: &quot;http_requests&quot;,&#10;    &quot;kind&quot;: &quot;&quot;,&#10;    &quot;max_upload_bytes&quot;: 5000000,&#10;    &quot;enabled&quot;: true,&#10;    &quot;name&quot;: &quot;&lt;DOMAIN_NAME&gt;&quot;,&#10;    &quot;output_options&quot;: {&#10;      &quot;field_names&quot;: [&quot;ClientIP&quot;, &quot;ClientRequestHost&quot;, &quot;ClientRequestMethod&quot;, &quot;ClientRequestURI&quot;, &quot;EdgeEndTimestamp&quot;,&quot;EdgeResponseBytes&quot;, &quot;EdgeResponseStatus&quot;, &quot;EdgeStartTimestamp&quot;, &quot;RayID&quot;],&#10;      &quot;timestamp_format&quot;: &quot;unix&quot;&#10;    },&#10;    &quot;destination_conf&quot;: &quot;https://log-api.newrelic.com/log/v1?Api-Key=&lt;NR_LICENSE_KEY&gt;&amp;format=cloudflare&quot;,&#10;    &quot;last_complete&quot;: null,&#10;    &quot;last_error&quot;: null,&#10;    &quot;error_message&quot;: null&#10;  },&#10;  &quot;success&quot;: true&#10;}&#10;</code></pre>
<p>Refer to <a href="/logs/logpush/examples/example-logpush-curl/">Manage Logpush with cURL</a> to update a job (including enabling and disabling).</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note-1">Note</h3>
@markup("md", "content/.markup/bodies/10550.md")
</aside>
