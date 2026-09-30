---
cp9:
  canonical: https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/splunk/
  description: Push Cloudflare logs to Splunk via HEC.
  full_title: Enable Logpush to Splunk · Cloudflare Logs docs
  head_html: <title>Enable Logpush to Splunk · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Push Cloudflare logs to Splunk via HEC."><link rel="canonical" href="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/splunk/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/splunk/index.md"><meta property="og:title" content="Enable Logpush to Splunk · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Push Cloudflare logs to Splunk via HEC."><meta property="og:url" content="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/splunk/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Logpush"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/splunk/#page","headline":"Enable Logpush to Splunk \u00b7 Cloudflare Logs docs","description":"Push Cloudflare logs to Splunk via HEC.","url":"https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/splunk/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/logpush/logpush-job/enable-destinations/splunk/
  schema: 1
---
<p>The <a href="https://dev.splunk.com/enterprise/docs/devtools/httpeventcollector/">HTTP Event Collector (HEC)</a> is a reliable method to receive data from Splunk Enterprise or Splunk Cloud Platform. Cloudflare Logpush supports pushing logs directly to Splunk HEC via the Cloudflare dashboard or API.</p>
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
<p>In <strong>Select a destination</strong>, choose <strong>Splunk</strong>.</p>
</li>
<li>
<p>Enter or select the following destination information:</p>
<ul>
<li><strong>Splunk HEC URL</strong></li>
<li><strong>Channel ID</strong> - This is a random GUID that you can generate using <a href="https://guidgenerator.com/">guidgenerator.com</a>.</li>
<li><strong>Auth Token</strong> - Event Collector token prefixed with the word <code>Splunk</code>. For example: <code>Splunk 1234EXAMPLEKEY</code>.</li>
<li><strong>Source Type</strong> - For example, <code>cloudflare:json</code>. If you are using the <a href="https://splunkbase.splunk.com/app/4501">Cloudflare App for Splunk</a>, refer to the appropriate source type for the corresponding datasets under the <strong>Details</strong> section. For instance, for Zero Trust Access requests logs, the source type is <code>cloudflare:access</code>.</li>
<li><strong>Use insecure skip verify option</strong> (not recommended).</li>
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
<p>To set up a Splunk Logpush job:</p>
<ol>
<li>Create a job with the appropriate endpoint URL and authentication parameters.</li>
<li>Enable the job to begin pushing logs.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10542.md")
</aside>
<p>Ensure <strong>Log Share</strong> permissions are enabled, before attempting to read or configure a Logpush job. For more information refer to the <a href="/logs/logpush/permissions/#roles">Roles section</a>.</p>
<h3 id="1-create-a-job"><ol>
<li>Create a job</li>
</ol></h3>
<p>To create a job, make a <code>POST</code> request to the Logpush jobs endpoint with the following fields:</p>
<ul>
<li><strong>name</strong> (optional) - Use your domain name as the job name.</li>
<li><strong>destination_conf</strong> - A log destination consisting of an endpoint URL, channel id, insecure-skip-verify flag, source type, authorization header in the string format below.
<ul>
<li><strong>&lt;SPLUNK_ENDPOINT_URL&gt;</strong>: The Splunk raw HTTP Event Collector URL with port. For example: <code>splunk.cf-analytics.com:8088/services/collector/raw</code>.
<ul>
<li>Cloudflare expects the Splunk endpoint to be <code>/services/collector/raw</code> while configuring and setting up the Logpush job.</li>
<li>Ensure you have enabled HEC in Splunk. Refer to <a href="/analytics/analytics-integrations/splunk/">Splunk Analytics Integrations</a> for information on how to set up HEC in Splunk.</li>
<li>You may notice an API request failed with a 504 error, when adding an incorrect URL. Splunk Cloud endpoint URL usually contains <code>http-inputs-</code> or similar text before the hostname.</li>
</ul>
</li>
<li><strong>&lt;SPLUNK_CHANNEL_ID&gt;</strong>: A unique channel ID. This is a random GUID that you can generate by:
<ul>
<li>Using an online tool like the <a href="https://www.guidgenerator.com/">GUID generator</a>.</li>
<li>Using the command line. For example: <code>python -c 'import uuid; print(uuid.uuid4())'</code>.</li>
</ul>
</li>
<li><strong>&lt;INSECURE_SKIP_VERIFY&gt;</strong>: Boolean value. Cloudflare recommends setting this value to <code>false</code>. Setting this value to <code>true</code> is equivalent to using the <code>-k</code> option with <code>curl</code> as shown in Splunk examples and is <strong>not</strong> recommended. Only set this value to <code>true</code> when HEC uses a self-signed certificate.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10541.md")
</aside>
<ul>
<li><strong>&lt;SOURCE_TYPE&gt;</strong>: The Splunk source type. For example: <code>cloudflare:json</code>.</li>
<li><strong>&lt;SPLUNK_AUTH_TOKEN&gt;</strong>: The Splunk authorization token that is URL-encoded and must be prefixed with the word <code>Splunk</code>. For example: <code>Splunk e6d94e8c-5792-4ad1-be3c-29bcaee0197d</code>.</li>
</ul>
<pre tabindex="0"><code class="language-bash">&quot;splunk://&lt;SPLUNK_ENDPOINT_URL&gt;?channel=&lt;SPLUNK_CHANNEL_ID&gt;&amp;insecure-skip-verify=&lt;INSECURE_SKIP_VERIFY&gt;&amp;sourcetype=&lt;SOURCE_TYPE&gt;&amp;header_Authorization=&lt;SPLUNK_AUTH_TOKEN&gt;&quot;&#10;</code></pre>
<ul>
<li>
<p><strong>dataset</strong> - The category of logs you want to receive. Refer to <a href="/logs/logpush/logpush-job/datasets/">Datasets</a> for the full list of supported datasets.</p>
</li>
<li>
<p><strong>output_options</strong> (optional) - To configure fields, sample rate, and timestamp format, refer to <a href="/logs/logpush/logpush-job/log-output-options/">Log Output Options</a>. For timestamp, Cloudflare recommends using <code>timestamps=rfc3339</code>.</p>
</li>
</ul>
<p>Example request using cURL:</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/logpush/jobs \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;&lt;DOMAIN_NAME&gt;&quot;,&#10;  &quot;destination_conf&quot;: &quot;splunk://&lt;SPLUNK_ENDPOINT_URL&gt;?channel=&lt;SPLUNK_CHANNEL_ID&gt;&amp;insecure-skip-verify=&lt;INSECURE_SKIP_VERIFY&gt;&amp;sourcetype=&lt;SOURCE_TYPE&gt;&amp;header_Authorization=&lt;SPLUNK_AUTH_TOKEN&gt;&quot;,&#10;  &quot;output_options&quot;: {&#10;    &quot;field_names&quot;: [&#10;      &quot;ClientIP&quot;,&#10;      &quot;ClientRequestHost&quot;,&#10;      &quot;ClientRequestMethod&quot;,&#10;      &quot;ClientRequestURI&quot;,&#10;      &quot;EdgeEndTimestamp&quot;,&#10;      &quot;EdgeResponseBytes&quot;,&#10;      &quot;EdgeResponseStatus&quot;,&#10;      &quot;EdgeStartTimestamp&quot;,&#10;      &quot;RayID&quot;&#10;    ],&#10;    &quot;timestamp_format&quot;: &quot;rfc3339&quot;&#10;  },&#10;  &quot;dataset&quot;: &quot;http_requests&quot;,&#10;  &quot;enabled&quot;: true&#10;}&#x27;</code></pre>
<p>Response:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;id&quot;: &lt;JOB_ID&gt;,&#10;    &quot;dataset&quot;: &quot;http_requests&quot;,&#10;    &quot;kind&quot;: &quot;&quot;,&#10;    &quot;enabled&quot;: true,&#10;    &quot;name&quot;: &quot;&lt;DOMAIN_NAME&gt;&quot;,&#10;    &quot;output_options&quot;: {&#10;      &quot;field_names&quot;: [&quot;ClientIP&quot;, &quot;ClientRequestHost&quot;, &quot;ClientRequestMethod&quot;, &quot;ClientRequestURI&quot;, &quot;EdgeEndTimestamp&quot;,&quot;EdgeResponseBytes&quot;, &quot;EdgeResponseStatus&quot;, &quot;EdgeStartTimestamp&quot;, &quot;RayID&quot;],&#10;      &quot;timestamp_format&quot;: &quot;rfc3339&quot;&#10;    },&#10;    &quot;destination_conf&quot;: &quot;splunk://&lt;SPLUNK_ENDPOINT_URL&gt;?channel=&lt;SPLUNK_CHANNEL_ID&gt;&amp;insecure-skip-verify=&lt;INSECURE_SKIP_VERIFY&gt;&amp;sourcetype=&lt;SOURCE_TYPE&gt;&amp;header_Authorization=&lt;SPLUNK_AUTH_TOKEN&gt;&quot;,&#10;    &quot;last_complete&quot;: null,&#10;    &quot;last_error&quot;: null,&#10;    &quot;error_message&quot;: null&#10;  },&#10;  &quot;success&quot;: true&#10;}&#10;</code></pre>
<p>Refer to <a href="/logs/logpush/examples/example-logpush-curl/">Manage Logpush with cURL</a> to update a job (including enabling and disabling).</p>
<p>Refer to the <a href="/logs/faq/logpush/">Logpush FAQ</a> for troubleshooting information.</p>
<h3 id="3-create-waf-custom-rule-for-splunk-hec-endpoint-optional"><ol start="3">
<li>Create WAF custom rule for Splunk HEC endpoint (optional)</li>
</ol></h3>
<p>If your logpush destination hostname is proxied through Cloudflare, and you have the Cloudflare Web Application Firewall (WAF) turned on, you may be challenged or blocked when Cloudflare makes a request to Splunk HTTP Event Collector (HEC). To make sure this does not happen, you have to create a <a href="/waf/custom-rules/">custom rule</a> that allows Cloudflare to bypass the HEC endpoint.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security rules</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select <strong>Create rule</strong> &gt; <strong>Custom rules</strong>.</p>
</li>
<li>
<p>Enter a descriptive name for the rule (for example, <code>Splunk</code>).</p>
</li>
<li>
<p>Under <strong>When incoming requests match</strong>, use the <strong>Field</strong>, <strong>Operator</strong>, and <strong>Value</strong> dropdowns to create a rule. After finishing each row, select <strong>And</strong> to create the next row of rules. Refer to the table below for the values you should input:</p>
</li>
</ol>
<table>
<thead>
<tr>
<th>Field</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Request Method</td>
<td><code>equals</code></td>
<td><code>POST</code></td>
</tr>
<tr>
<td>Hostname</td>
<td><code>equals</code></td>
<td>Your Splunk endpoint hostname. For example: <code>splunk.cf-analytics.com</code></td>
</tr>
<tr>
<td>URI Path</td>
<td><code>equals</code></td>
<td><code>/services/collector/raw</code></td>
</tr>
<tr>
<td>URI Query String</td>
<td><code>contains</code></td>
<td><code>channel</code></td>
</tr>
<tr>
<td>AS Num</td>
<td><code>is in</code></td>
<td><code>13335</code>, <code>132892</code>, <code>202623</code></td>
</tr>
<tr>
<td>User Agent</td>
<td><code>equals</code></td>
<td><code>Go-http-client/2.0</code></td>
</tr>
</tbody>
</table>
<ol start="5">
<li>After inputting the values as shown in the table, you should have an Expression Preview with the values you added for your specific rule. The example below reflects the hostname <code>splunk.cf-analytics.com</code>.</li>
</ol>
<pre tabindex="0"><code class="language-txt">(http.request.method eq &quot;POST&quot; and http.host eq &quot;splunk.cf-analytics.com&quot; and http.request.uri.path eq &quot;/services/collector/raw&quot; and http.request.uri.query contains &quot;channel&quot; and ip.geoip.asnum in {13335 132892 202623} and http.user_agent eq &quot;Go-http-client/2.0&quot;)&#10;</code></pre>
<ol start="6">
<li>Under the <strong>Then</strong> &gt; <strong>Choose an action</strong> dropdown, select <em>Skip</em>.</li>
<li>Under <strong>WAF components to skip</strong>, select <em>All managed rules</em>.</li>
<li>Select <strong>Deploy</strong>.</li>
</ol>
<p>The WAF should now ignore requests made to Splunk HEC by Cloudflare.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10540.md")
</aside>
<h2 id="troubleshooting-splunk-destinations">Troubleshooting Splunk destinations</h2>
<h3 id="validating-destination-errors">Validating destination errors</h3>
<p>If you receive a validation error while setting up a Splunk job, check the following:</p>
<ul>
<li><strong>Endpoint URL</strong>: Cloudflare only supports Splunk HEC raw endpoint over HTTPS. Verify your endpoint URL is correct and includes the port (typically <code>:8088</code>).</li>
<li><strong>Authentication token</strong>: Ensure the Splunk authentication token is URL-encoded and prefixed with <code>Splunk</code>. For example, use <code>%20</code> for spaces in the token.</li>
<li><strong>Certificate configuration</strong>: Certificates generated by Splunk or third-party certificates must have the <strong>Common Name</strong> field match the Splunk server's domain name. Otherwise, you may see errors like: <code>x509: certificate is valid for SplunkServerDefaultCert, not &lt;YOUR_INSTANCE&gt;.splunkcloud.com</code>.</li>
</ul>
<h3 id="understanding-insecure-skip-verify">Understanding insecure-skip-verify</h3>
<p>The <code>insecure-skip-verify</code> parameter, when set to <code>true</code>, makes an insecure connection to Splunk. This is equivalent to using the <code>-k</code> option with <code>curl</code> and is <strong>not recommended</strong>.</p>
<p><strong>Why this parameter exists</strong>: Certificates generated by Splunk or third-party certificates should have the <strong>Common Name</strong> field match the Splunk server's domain name. When they do not match (especially with default certificates generated by Splunk on startup), pushes will fail unless certificates are fixed. This parameter exists for rare scenarios where you cannot access or modify certificates, such as with Splunk Cloud instances that do not allow changing server configurations.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10539.md")
</aside>
<h3 id="verifying-hec-before-setup">Verifying HEC before setup</h3>
<p>Before creating a Logpush job, verify that your Splunk HEC is working correctly by publishing test events through <code>curl</code> without the <code>-k</code> flag and with <code>insecure-skip-verify=false</code>:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://&lt;SPLUNK_ENDPOINT_URL&gt;?channel=&lt;SPLUNK_CHANNEL_ID&gt;&amp;insecure-skip-verify=false&amp;sourcetype=&lt;SOURCE_TYPE&gt;&quot; \&#10;&#45;-header &quot;Authorization: Splunk &lt;SPLUNK_AUTH_TOKEN&gt;&quot; \&#10;&#45;-data &#x27;{&quot;BotScore&quot;:99,&quot;BotScoreSrc&quot;:&quot;Machine Learning&quot;,&quot;CacheCacheStatus&quot;:&quot;miss&quot;,&quot;CacheResponseBytes&quot;:2478}&#x27;&#10;</code></pre>
<p>Expected response:</p>
<pre tabindex="0"><code class="language-json">{&quot;text&quot;:&quot;Success&quot;,&quot;code&quot;:0}&#10;</code></pre>
<h3 id="network-port-requirements">Network port requirements</h3>
<p>Cloudflare expects the HEC network port to be configured to <code>:443</code> or <code>:8088</code>. Other ports are not supported.</p>
<h3 id="cloudflare-splunk-app-integration">Cloudflare Splunk App integration</h3>
<p>Logpush integrates with the <a href="https://splunkbase.splunk.com/app/4501/">Cloudflare App for Splunk</a>. As long as you ingest logs using the <code>cloudflare:json</code> source type, you can use the Cloudflare Splunk App to analyze and visualize your logs.</p>
<p>For detailed setup instructions, refer to <a href="/analytics/analytics-integrations/splunk/">Splunk Analytics integration</a>.</p>
