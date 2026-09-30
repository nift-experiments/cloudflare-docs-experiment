---
cp9:
  canonical: https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/ibm-cloud-logs/
  description: Push Cloudflare logs to IBM Cloud Logs.
  full_title: Enable Logpush IBM Cloud Logs · Cloudflare Logs docs
  head_html: <title>Enable Logpush IBM Cloud Logs · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Push Cloudflare logs to IBM Cloud Logs."><link rel="canonical" href="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/ibm-cloud-logs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/ibm-cloud-logs/index.md"><meta property="og:title" content="Enable Logpush IBM Cloud Logs · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Push Cloudflare logs to IBM Cloud Logs."><meta property="og:url" content="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/ibm-cloud-logs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Logpush"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/ibm-cloud-logs/#page","headline":"Enable Logpush IBM Cloud Logs \u00b7 Cloudflare Logs docs","description":"Push Cloudflare logs to IBM Cloud Logs.","url":"https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/ibm-cloud-logs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/logpush/logpush-job/enable-destinations/ibm-cloud-logs/
  schema: 1
---
<p>Cloudflare Logpush supports pushing logs directly to IBM Cloud Logs via dashboard or API.</p>
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
<p>In <strong>Select a destination</strong>, choose <strong>IBM Cloud Logs</strong>.</p>
</li>
<li>
<p>Enter the following destination information:</p>
</li>
</ol>
<ul>
<li><strong>HTTP Source Address</strong> - For example, <code>ibmcl://&lt;INSTANCE_ID&gt;.ingress.&lt;REGION&gt;.logs.cloud.ibm.com/logs/v1/singles</code>.</li>
<li><strong>IBM API Key</strong> - For more information refer to the <a href="https://cloud.ibm.com/docs/cloud-logs">IBM Cloud Logs documentation</a>.</li>
</ul>
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
<p>To set up an IBM Cloud Logs job:</p>
<ol>
<li>Create a job with the appropriate endpoint URL and authentication parameters.</li>
<li>Enable the job to begin pushing logs.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/10557.md")
</aside>
<h3 id="1-create-a-job"><ol>
<li>Create a job</li>
</ol></h3>
<p>To create a job, make a <code>POST</code> request to the Logpush jobs endpoint with the following fields:</p>
<ul>
<li><strong>name</strong> (optional) - Use your domain name as the job name.</li>
<li><strong>output_options</strong> (optional) - This parameter is used to define the desired output format and structure. Below are the configurable fields:
<ul>
<li>output_type</li>
<li>timestamp_format</li>
<li>batch_prefix and batch_suffix</li>
<li>record_prefix and record_suffix</li>
<li>record_delimiter</li>
</ul>
</li>
<li><strong>destination_conf</strong> - A log destination consisting of Instance ID, Region and <a href="https://cloud.ibm.com/docs/account?topic=account-iamtoken_from_apikey">IBM API Key</a> in the string format below.</li>
</ul>
<p><code>ibmcl://&lt;INSTANCE_ID&gt;.ingress.&lt;REGION&gt;.logs.cloud.ibm.com/logs/v1/singles?ibm_api_key=&lt;IBM_API_KEY&gt;</code></p>
<ul>
<li><strong>max_upload_records</strong> (optional) - The maximum number of log lines per batch. This must be at least 1,000 lines or more. Note that there is no way to specify a minimum number of log lines per batch. This means that log files may contain many fewer lines than specified.</li>
<li><strong>max_upload_bytes</strong> (optional) - The maximum uncompressed file size for a batch of logs. We recommend a default value of 2 MB per upload based on IBM's limits, which our system will enforce for this destination. Since minimum file sizes cannot be set, log files may be smaller than the specified batch size.</li>
<li><strong>dataset</strong> - The category of logs you want to receive. Refer to <a href="/logs/logpush/logpush-job/datasets/">Datasets</a> for the full list of supported datasets.</li>
</ul>
<p>Example request using cURL:</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/logpush/jobs \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;&lt;DOMAIN_NAME&gt;&quot;,&#10;  &quot;output_options&quot;: {&#10;    &quot;output_type&quot;: &quot;ndjson&quot;,&#10;    &quot;timestamp_format&quot;: &quot;rfc3339&quot;,&#10;    &quot;batch_prefix&quot;: &quot;[&quot;,&#10;    &quot;batch_suffix&quot;: &quot;]&quot;,&#10;    &quot;record_prefix&quot;: &quot;{\&quot;applicationName\&quot;:\&quot;ibm-platform-log\&quot;,\&quot;subsystemName\&quot;:\&quot;internet-svcs:logpush\&quot;,\&quot;text\&quot;:{&quot;,&#10;    &quot;record_suffix&quot;: &quot;}}&quot;,&#10;    &quot;record_delimiter&quot;: &quot;,&quot;&#10;  },&#10;  &quot;destination_conf&quot;: &quot;ibmcl://&lt;INSTANCE_ID&gt;.ingress.&lt;REGION&gt;.logs.cloud.ibm.com/logs/v1/singles?ibm_api_key=&lt;IBM_API_KEY&gt;&quot;,&#10;  &quot;max_upload_bytes&quot;: 2000000,&#10;  &quot;dataset&quot;: &quot;http_requests&quot;,&#10;  &quot;enabled&quot;: true&#10;}&#x27;</code></pre>
<p>Response:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;id&quot;: &lt;JOB_ID&gt;,&#10;    &quot;dataset&quot;: &quot;http_requests&quot;,&#10;    &quot;kind&quot;: &quot;&quot;,&#10;    &quot;max_upload_bytes&quot;: 2000000,&#10;    &quot;enabled&quot;: true,&#10;    &quot;name&quot;: &quot;&lt;DOMAIN_NAME&gt;&quot;,&#10;    &quot;output_options&quot;: {&#10;      &quot;output_type&quot;: &quot;ndjson&quot;,&#10;      &quot;timestamp_format&quot;: &quot;rfc3339&quot;,&#10;      &quot;batch_prefix&quot;: &quot;[&quot;,&#10;      &quot;batch_suffix&quot;: &quot;]&quot;,&#10;      &quot;record_prefix&quot;: &quot;{\&quot;applicationName\&quot;:\&quot;ibm-platform-log\&quot;,\&quot;subsystemName\&quot;:\&quot;internet-svcs:logpush\&quot;,\&quot;text\&quot;:{&quot;,&#10;      &quot;record_suffix&quot;: &quot;}}&quot;,&#10;      &quot;record_delimiter&quot;: &quot;,&quot;&#10;    },&#10;    &quot;destination_conf&quot;: &quot;ibmcl://&lt;INSTANCE_ID&gt;.ingress.&lt;REGION&gt;.logs.cloud.ibm.com/logs/v1/singles?ibm_api_key=&lt;IBM_API_KEY&gt;&quot;,&#10;    &quot;last_complete&quot;: null,&#10;    &quot;last_error&quot;: null,&#10;    &quot;error_message&quot;: null&#10;  },&#10;  &quot;success&quot;: true&#10;}&#10;</code></pre>
<p>Refer to <a href="/logs/logpush/examples/example-logpush-curl/">Manage Logpush with cURL</a> to update a job (including enabling and disabling).</p>
