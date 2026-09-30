---
cp9:
  canonical: https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/r2/
  description: Push Cloudflare logs to Cloudflare R2.
  full_title: Enable Cloudflare R2 · Cloudflare Logs docs
  head_html: <title>Enable Cloudflare R2 · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Push Cloudflare logs to Cloudflare R2."><link rel="canonical" href="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/r2/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/r2/index.md"><meta property="og:title" content="Enable Cloudflare R2 · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Push Cloudflare logs to Cloudflare R2."><meta property="og:url" content="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/r2/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Logpush,R2"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/r2/#page","headline":"Enable Cloudflare R2 \u00b7 Cloudflare Logs docs","description":"Push Cloudflare logs to Cloudflare R2.","url":"https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/r2/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/logpush/logpush-job/enable-destinations/r2/
  schema: 1
---
<p>Cloudflare Logpush supports pushing logs directly to R2. You can do so via the automatic setup (Cloudflare creates an R2 bucket for you), or you can create your own R2 bucket with the custom setup. The automatic setup is ideal for quickly setting up a bucket or for testing purposes. Instead, use the custom setup if you need full control over the configuration.</p>
<p>For more information about R2, refer to the <a href="/r2/">Cloudflare R2</a> documentation.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10547.md")
</aside>
<h2 id="automatic-setup">Automatic setup</h2>
<p>If you want to use the automatic setup for your logpush job:</p>
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
<p>Select <strong>R2 Object Storage - automatic</strong> as destination.</p>
</li>
<li>
<p>Next, select the dataset and the storage region you want to use.</p>
</li>
<li>
<p>To finalize, select <strong>Create Logpush job</strong>.</p>
</li>
</ol>
<p>Your setup should now be complete. If you require full control over the configuration, consider using the custom setup instead.</p>
<h2 id="custom-setup">Custom setup</h2>
<p>Cloudflare Logpush supports pushing logs directly to R2 via the Cloudflare dashboard or via API.</p>
<p>Before getting started:</p>
<ul>
<li>
<p>Create an R2 bucket and set up R2 API tokens.</p>
<ol>
<li>
<p>Go to the R2 UI &gt; <strong>Create bucket</strong>.</p>
</li>
<li>
<p>Select <strong>Manage R2 API Tokens</strong>.</p>
</li>
<li>
<p>Select <strong>Create API token</strong>.</p>
</li>
<li>
<p>Under <strong>Permission</strong>, select <strong>Edit</strong> permissions for your token.</p>
</li>
<li>
<p>Copy the Secret Access Key and Access Key ID. You will need these when setting up your Logpush job.</p>
</li>
</ol>
</li>
<li>
<p>Ensure that you have the following permissions:</p>
<ul>
<li>R2 write, Logshare Edit.</li>
</ul>
</li>
</ul>
<h3 id="manage-via-the-cloudflare-dashboard">Manage via the Cloudflare dashboard</h3>
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
<p>In <strong>Select a destination</strong>, choose <strong>R2 Object Storage</strong>.</p>
</li>
<li>
<p>Enter or select the following destination details:</p>
<ul>
<li><strong>Bucket</strong> - R2 bucket name</li>
<li><strong>Path</strong> - bucket location, for example, <code>cloudflare-logs/http_requests/example.com</code></li>
<li><strong>Organize logs into daily subfolders</strong> (recommended)</li>
<li>Under <strong>Authentication</strong> add your <strong>R2 Access Key ID</strong> and <strong>R2 Secret Access Key</strong>. Refer to <a href="https://dash.cloudflare.com/b54f07a6c269ecca2fa60f1ae4920c99/r2/api-tokens">Manage R2 API tokens</a> for more information.</li>
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
<h3 id="manage-via-api">Manage via API</h3>
<p>To create a job, make a <code>POST</code> request to the Logpush jobs endpoint with the following fields:</p>
<ul>
<li><strong>name</strong> (optional) - Use your domain name as the job name.</li>
<li><strong>destination_conf</strong> - A log destination consisting of bucket path, account ID, R2 access key ID and R2 secret access key.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/10546.md")
</aside>
<pre tabindex="0"><code class="language-bash">r2://&lt;BUCKET_PATH&gt;/{DATE}?account-id=&lt;ACCOUNT_ID&gt;&amp;access-key-id=&lt;R2_ACCESS_KEY_ID&gt;&amp;secret-access-key=&lt;R2_SECRET_ACCESS_KEY&gt;&#10;</code></pre>
<ul>
<li><strong>dataset</strong> - The category of logs you want to receive. Refer to <a href="/logs/logpush/logpush-job/datasets/">Datasets</a> for the full list of supported datasets.</li>
<li><strong>output_options</strong> (optional) - To configure fields, sample rate, and timestamp format, refer to <a href="/logs/logpush/logpush-job/api-configuration/#options">API configuration options</a>.</li>
</ul>
<p>Example request using cURL:</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/logpush/jobs \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;&lt;DOMAIN_NAME&gt;&quot;,&#10;  &quot;output_options&quot;: {&#10;    &quot;field_names&quot;: [&#10;      &quot;ClientIP&quot;,&#10;      &quot;ClientRequestHost&quot;,&#10;      &quot;ClientRequestMethod&quot;,&#10;      &quot;ClientRequestURI&quot;,&#10;      &quot;EdgeEndTimestamp&quot;,&#10;      &quot;EdgeResponseBytes&quot;,&#10;      &quot;EdgeResponseStatus&quot;,&#10;      &quot;EdgeStartTimestamp&quot;,&#10;      &quot;RayID&quot;&#10;    ],&#10;    &quot;timestamp_format&quot;: &quot;rfc3339&quot;&#10;  },&#10;  &quot;destination_conf&quot;: &quot;r2://&lt;BUCKET_PATH&gt;/{DATE}?account-id=&lt;ACCOUNT_ID&gt;&amp;access-key-id=&lt;R2_ACCESS_KEY_ID&gt;&amp;secret-access-key=&lt;R2_SECRET_ACCESS_KEY&gt;&quot;,&#10;  &quot;dataset&quot;: &quot;http_requests&quot;,&#10;  &quot;enabled&quot;: true&#10;}&#x27;</code></pre>
<p>Response:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;id&quot;: &lt;JOB_ID&gt;,&#10;    &quot;dataset&quot;: &quot;http_requests&quot;,&#10;    &quot;kind&quot;: &quot;&quot;,&#10;    &quot;enabled&quot;: true,&#10;    &quot;name&quot;: &quot;&lt;DOMAIN_NAME&gt;&quot;,&#10;    &quot;output_options&quot;: {&#10;      &quot;field_names&quot;: [&quot;ClientIP&quot;, &quot;ClientRequestHost&quot;, &quot;ClientRequestMethod&quot;, &quot;ClientRequestURI&quot;, &quot;EdgeEndTimestamp&quot;, &quot;EdgeResponseBytes&quot;, &quot;EdgeResponseStatus&quot; ,&quot;EdgeStartTimestamp&quot;, &quot;RayID&quot;],&#10;      &quot;timestamp_format&quot;: &quot;rfc3339&quot;&#10;    },&#10;    &quot;destination_conf&quot;: &quot;r2://&lt;BUCKET_PATH&gt;/{DATE}?account-id=&lt;ACCOUNT_ID&gt;&amp;access-key-id=&lt;R2_ACCESS_KEY_ID&gt;&amp;secret-access-key=&lt;R2_SECRET_ACCESS_KEY&gt;&quot;,&#10;    &quot;last_complete&quot;: null,&#10;    &quot;last_error&quot;: null,&#10;    &quot;error_message&quot;: null&#10;  },&#10;  &quot;success&quot;: true&#10;}&#10;</code></pre>
<p>Refer to <a href="/logs/logpush/examples/example-logpush-curl/">Manage Logpush with cURL</a> to update a job (including enabling and disabling).</p>
<h2 id="download-logs-from-r2">Download logs from R2</h2>
<p>Once your logs are stored in R2, you can download them using various methods:</p>
<h3 id="dashboard">Dashboard</h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>R2</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select your bucket.</p>
</li>
<li>
<p>From your bucket's page, locate the desired log file.</p>
</li>
<li>
<p>Select on the <strong>...</strong> icon next to the file to download it.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/logs/logs-r2.png" alt="Log files list" /></p>
<h3 id="aws-cli">AWS CLI</h3>
<p>Cloudflare R2 is S3-compatible, so you can use the AWS CLI to interact with it.</p>
<ul>
<li>Configure the AWS CLI with your R2 credentials.</li>
<li>Use the <code>aws s3 cp</code> command to download the log file:</li>
</ul>
<pre tabindex="0"><code class="language-bash">aws s3 cp s3://&lt;BUCKET-NAME&gt;/&lt;PATH-TO-LOG-FILE&gt; &lt;LOCAL-DESTINATION&gt;&#10;</code></pre>
<p>Replace <code>&lt;bucket-name&gt;</code>, <code>&lt;path-to-log-file&gt;</code>, and <code>&lt;local-destination&gt;</code> with your specific details.</p>
<p>Downloaded files are gzipped so they must be decompressed before you can open them in a text editor.</p>
