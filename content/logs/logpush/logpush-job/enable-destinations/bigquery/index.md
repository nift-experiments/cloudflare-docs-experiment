---
cp9:
  canonical: https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/bigquery/
  description: Push Cloudflare logs to Google BigQuery.
  full_title: Enable Logpush to Google BigQuery · Cloudflare Logs docs
  head_html: <title>Enable Logpush to Google BigQuery · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Push Cloudflare logs to Google BigQuery."><link rel="canonical" href="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/bigquery/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/bigquery/index.md"><meta property="og:title" content="Enable Logpush to Google BigQuery · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Push Cloudflare logs to Google BigQuery."><meta property="og:url" content="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/bigquery/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Logpush"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/bigquery/#page","headline":"Enable Logpush to Google BigQuery \u00b7 Cloudflare Logs docs","description":"Push Cloudflare logs to Google BigQuery.","url":"https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/bigquery/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/logpush/logpush-job/enable-destinations/bigquery/
  schema: 1
---
<p>Cloudflare Logpush supports pushing logs directly to Google BigQuery (using Legacy Streaming API) via the Cloudflare dashboard or via API.</p>
<h2 id="create-and-get-access-to-a-bigquery-table">Create and get access to a BigQuery table</h2>
<p>Cloudflare uses Google Application Credentials provided in Logpush job <code>destination_conf</code> to gain write access to your table. The provided service account needs a write permission for the table.</p>
<p>To enable Logpush to BigQuery:</p>
<ol>
<li>Go to Google Cloud Console for your account.</li>
<li>Go to <strong>IAM &amp; Admin</strong> &gt; <strong>Service Accounts</strong>, and create a new service account.</li>
<li>Add <strong>BigQuery Data Editor</strong> role under Permissions. At minimum, it requires <code>bigquery.tables.updateData</code> permission.</li>
<li>Add a key under Keys.
<ol>
<li>Click <strong>Add key</strong>.</li>
<li>Click <strong>Create new key</strong>.</li>
<li>Select Key type <strong>JSON</strong>.</li>
<li>Click <strong>Create</strong>.</li>
<li>Save the Application Credentials JSON file. You will need to use this when setting up a new Logpush job.</li>
</ol>
</li>
<li>In BigQuery, create a dataset and table. Refer to <a href="https://cloud.google.com/bigquery/docs/tables">instructions from BigQuery</a>. For example, using <code>schema.json</code> and <code>bq</code> command:</li>
</ol>
<pre tabindex="0"><code class="language-bash">gcloud auth activate-service-account --key-file=${KEY_FILE}&#10;&#10;PROJECT_ID=&lt;PROJECT_ID&gt;&#10;DATASET_ID=&lt;DATASET_ID&gt;&#10;TABLE_ID=&lt;TABLE_ID&gt;&#10;&#10;bq mk --table &quot;${PROJECT_ID}:${DATASET_ID}.${TABLE_ID}&quot; schema.json&#10;</code></pre>
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
<p>In <strong>Select a destination</strong>, choose <strong>Google BigQuery</strong>.</p>
</li>
<li>
<p>Enter the following destination details:</p>
<ul>
<li><strong>Project ID</strong> - your Google Cloud project ID</li>
<li><strong>Dataset ID</strong> - the BigQuery dataset containing your table</li>
<li><strong>Table ID</strong> - the BigQuery table to push logs to</li>
<li><strong>Service Account Credentials</strong> - paste your Google service account key JSON. This credential is stored encrypted and will not be displayed again.</li>
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
<p>To set up a BigQuery Logpush job:</p>
<ol>
<li>Create a job with the appropriate endpoint URL and authentication parameters.</li>
<li>Enable the job to begin pushing logs.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10572.md")
</aside>
<p>Ensure <strong>Log Share</strong> permissions are enabled, before attempting to read or configure a Logpush job. For more information refer to the <a href="/logs/logpush/permissions/#roles">Roles section</a>.</p>
<h3 id="1-create-a-job"><ol>
<li>Create a job</li>
</ol></h3>
<p>To create a job, make a <code>POST</code> request to the Logpush jobs endpoint with the following fields:</p>
<ul>
<li><strong>name</strong> (optional) - Use your domain name as the job name.</li>
<li><strong>destination_conf</strong> - A log destination consisting of a reference to BigQuery table and credentials in the string format below.
<ul>
<li><strong>&lt;PROJECT_ID&gt;</strong>, <strong>&lt;DATASET_ID&gt;</strong>, <strong>&lt;TABLE_ID&gt;</strong>: Project ID, Dataset ID, and table ID of the designated BigQuery table.</li>
<li><strong>&lt;ENCODED_VALUE&gt;</strong>: The encoded value of Application Credentials JSON as <code>credentials</code>, either base64-encoded with <code>base64:</code> prefix, or URL-encoded  with <code>url:</code> prefix.</li>
</ul>
</li>
</ul>
<pre tabindex="0"><code class="language-bash">&quot;bq://projects/&lt;PROJECT_ID&gt;/datasets/&lt;DATASET_ID&gt;/tables/&lt;TABLE_ID&gt;?credentials=&lt;ENCODED_VALUE&gt;&quot;&#10;</code></pre>
<ul>
<li><strong>dataset</strong> - The category of logs you want to receive. Refer to <a href="/logs/logpush/logpush-job/datasets/">Datasets</a> for the full list of supported datasets.</li>
<li><strong>output_options</strong> (optional) - To configure fields, sample rate, and timestamp format, refer to <a href="/logs/logpush/logpush-job/log-output-options/">Log Output Options</a>. For timestamp, Cloudflare recommends using <code>timestamps=rfc3339</code>.
<ul>
<li>When including custom formatting options, such as <code>output_type</code>, or any prefix / suffix / delimiter / template options, make sure to set <code>stringify_object</code> true, too, otherwise fields with <code>object</code> type may not be serialized in the format compatible to BigQuery Legacy Streaming API.</li>
</ul>
</li>
</ul>
<p>Example request using cURL:</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/logpush/jobs \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;&lt;DOMAIN_NAME&gt;&quot;,&#10;  &quot;destination_conf&quot;: &quot;bq://projects/&lt;PROJECT_ID&gt;/datasets/&lt;DATASET_ID&gt;/tables/&lt;TABLE_ID&gt;?credentials=&lt;ENCODED_VALUE&gt;&quot;,&#10;  &quot;output_options&quot;: {&#10;    &quot;field_names&quot;: [&#10;      &quot;ClientIP&quot;,&#10;      &quot;ClientRequestHost&quot;,&#10;      &quot;ClientRequestMethod&quot;,&#10;      &quot;ClientRequestURI&quot;,&#10;      &quot;EdgeEndTimestamp&quot;,&#10;      &quot;EdgeResponseBytes&quot;,&#10;      &quot;EdgeResponseStatus&quot;,&#10;      &quot;EdgeStartTimestamp&quot;,&#10;      &quot;RayID&quot;&#10;    ],&#10;    &quot;timestamp_format&quot;: &quot;rfc3339&quot;&#10;  },&#10;  &quot;max_upload_bytes&quot;: 5000000,&#10;  &quot;max_upload_records&quot;: 50000,&#10;  &quot;dataset&quot;: &quot;http_requests&quot;,&#10;  &quot;enabled&quot;: true&#10;}&#x27;</code></pre>
<p>Response:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;id&quot;: &lt;JOB_ID&gt;,&#10;    &quot;dataset&quot;: &quot;http_requests&quot;,&#10;    &quot;kind&quot;: &quot;&quot;,&#10;    &quot;max_upload_bytes&quot;: 5000000,&#10;    &quot;max_upload_records&quot;: 50000,&#10;    &quot;enabled&quot;: true,&#10;    &quot;name&quot;: &quot;&lt;DOMAIN_NAME&gt;&quot;,&#10;    &quot;output_options&quot;: {&#10;      &quot;field_names&quot;: [&quot;ClientIP&quot;, &quot;ClientRequestHost&quot;, &quot;ClientRequestMethod&quot;, &quot;ClientRequestURI&quot;, &quot;EdgeEndTimestamp&quot;, &quot;EdgeResponseBytes&quot;, &quot;EdgeResponseStatus&quot; ,&quot;EdgeStartTimestamp&quot;, &quot;RayID&quot;],&#10;      &quot;timestamp_format&quot;: &quot;rfc3339&quot;&#10;    },&#10;    &quot;destination_conf&quot;: &quot;bq://projects/&lt;PROJECT_ID&gt;/datasets/&lt;DATASET_ID&gt;/tables/&lt;TABLE_ID&gt;?credentials=&lt;ENCODED_VALUE&gt;&quot;,&#10;    &quot;last_complete&quot;: null,&#10;    &quot;last_error&quot;: null,&#10;    &quot;error_message&quot;: null&#10;  },&#10;  &quot;success&quot;: true&#10;}&#10;</code></pre>
<p>This will make a test upload with an empty content to verify that Logpush can upload, and you may see a row with empty data.</p>
<p>Refer to <a href="/logs/logpush/examples/example-logpush-curl/">Manage Logpush with cURL</a> to update a job (including enabling and disabling).</p>
<h2 id="limitations">Limitations</h2>
<p>Note the following default quota and limits, as described in the <a href="https://docs.cloud.google.com/bigquery/quotas#streaming_inserts">BigQuery documentation</a>.</p>
<p>The following limits apply to BigQuery streaming inserts:</p>
<ul>
<li>Maximum HTTP request size (uncompressed, may include headers): 10 MB</li>
<li>Maximum row size: 10 MB</li>
<li>Maximum rows per request size: 50,000 rows.</li>
</ul>
<p>These are default quota / limit, and you should adjust the Logpush jobs to match the limit, and/or request Google to increase them when needed.</p>
<h2 id="google-cloud-storage-integration">Google Cloud Storage integration</h2>
<p>Cloudflare Logpush supports pushing logs to <a href="/logs/logpush/logpush-job/enable-destinations/google-cloud-storage/">Google Cloud Storage</a>.</p>
<p>BigQuery supports loading up to 1,500 jobs per table per day (including failures) with up to 10 million files in each load.
That means you can load into BigQuery once per minute and include up to 10 million files in a load.
For more information, refer to BigQuery's quotas for load jobs.</p>
<p>Logpush delivers batches of logs as soon as possible, which means you could receive more than one batch of files per minute. Ensure your BigQuery job is configured to ingest files on a given time interval, like every minute, as opposed to when files are received. Ingesting files into BigQuery as each Logpush file is received could exhaust your BigQuery quota quickly.</p>
<p>For a community-supported example of how to set up a schedule job load with BigQuery, refer to <a href="https://github.com/cloudflare/cloudflare-gcp/tree/master/logpush-to-bigquery">Cloudflare + Google Cloud | Integrations repository</a>. Note that this repository is provided on a best-effort basis and is not maintained routinely.</p>
