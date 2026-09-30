---
cp9:
  canonical: https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/datadog/
  description: Push Cloudflare logs to Datadog.
  full_title: Enable Logpush to Datadog · Cloudflare Logs docs
  head_html: <title>Enable Logpush to Datadog · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Push Cloudflare logs to Datadog."><link rel="canonical" href="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/datadog/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/datadog/index.md"><meta property="og:title" content="Enable Logpush to Datadog · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Push Cloudflare logs to Datadog."><meta property="og:url" content="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/datadog/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Logpush"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/datadog/#page","headline":"Enable Logpush to Datadog \u00b7 Cloudflare Logs docs","description":"Push Cloudflare logs to Datadog.","url":"https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/datadog/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/logpush/logpush-job/enable-destinations/datadog/
  schema: 1
---
<p>Cloudflare Logpush supports pushing logs directly to Datadog via the Cloudflare dashboard or via API.</p>
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
<p>In <strong>Select a destination</strong>, choose <strong>Datadog</strong>.</p>
</li>
<li>
<p>Enter or select the following destination information:</p>
<ul>
<li><strong>Datadog URL Endpoint</strong>, which can be either one below. You can find the difference at <a href="https://docs.datadoghq.com/api/latest/logs/">Datadog API reference</a>.</li>
</ul>
</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10568.md")
</div></div>
<ul>
<li>
<p><strong>Datadog API Key</strong>, can be retrieved by following <a href="https://docs.datadoghq.com/account_management/api-app-keys/#add-an-api-key-or-client-token">these steps</a>.</p>
</li>
<li>
<p><strong>Service</strong>, <strong>Hostname</strong>, <strong>Datadog ddsource field</strong>, and <strong>ddtags</strong> fields can be set as URL parameters. For more information, refer to the <a href="https://docs.datadoghq.com/api/latest/logs/">Logs section</a> in Datadog's documentation. While these parameters are optional, they can be useful for indexing or processing logs. Note that the values of these parameters may contain special characters, which should be URL encoded.</p>
</li>
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
<p>To set up a Datadog Logpush job:</p>
<ol>
<li>Create a job with the appropriate endpoint URL and authentication parameters.</li>
<li>Enable the job to begin pushing logs.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/10565.md")
</aside>
<p>Ensure <strong>Log Share</strong> permissions are enabled, before attempting to read or configure a Logpush job. For more information refer to the <a href="/logs/logpush/permissions/#roles">Roles section</a>.</p>
<h3 id="1-create-a-job"><ol>
<li>Create a job</li>
</ol></h3>
<p>To create a job, make a <code>POST</code> request to the Logpush jobs endpoint with the following fields:</p>
<ul>
<li><strong>name</strong> (optional) - Use your domain name as the job name.</li>
<li><strong>destination_conf</strong> - A log destination consisting of an endpoint URL, authorization header, and zero or more optional parameters that Datadog supports in the string format below.
<ul>
<li><strong>&lt;DATADOG_ENDPOINT_URL&gt;</strong>: The Datadog HTTP logs intake endpoint, which can be either one below. You can find the difference at <a href="https://docs.datadoghq.com/api/latest/logs/">Datadog API reference</a>.</li>
</ul>
</li>
</ul>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10571.md")
</div></div>
<ul>
<li><code>&lt;DATADOG_API_KEY&gt;</code>: The Datadog API token can be retrieved by following <a href="https://docs.datadoghq.com/account_management/api-app-keys/#add-an-api-key-or-client-token">these steps</a>. For example, <code>20e6d94e8c57924ad1be3c29bcaee0197d</code>.</li>
<li><code>ddsource</code>: Set to <code>cloudflare</code>.</li>
<li><code>service</code>, <code>host</code>, <code>ddtags</code>: Optional parameters allowed by Datadog.</li>
</ul>
<pre tabindex="0"><code class="language-bash">&quot;datadog://&lt;DATADOG_ENDPOINT_URL&gt;?header_DD-API-KEY=&lt;DATADOG_API_KEY&gt;&amp;ddsource=cloudflare&amp;service=&lt;SERVICE&gt;&amp;host=&lt;HOST&gt;&amp;ddtags=&lt;TAGS&gt;&quot;&#10;</code></pre>
<ul>
<li><strong>dataset</strong> - The category of logs you want to receive. Refer to <a href="/logs/logpush/logpush-job/datasets/">Datasets</a> for the full list of supported datasets.</li>
<li><strong>output_options</strong> (optional) - To configure fields, sample rate, and timestamp format, refer to <a href="/logs/logpush/logpush-job/log-output-options/">Log Output Options</a>.</li>
</ul>
<p>Example request using cURL:</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/logpush/jobs \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;name&quot;: &quot;&lt;DOMAIN_NAME&gt;&quot;,&#10;  &quot;destination_conf&quot;: &quot;datadog://&lt;DATADOG_ENDPOINT_URL&gt;?header_DD-API-KEY=&lt;DATADOG_API_KEY&gt;&amp;ddsource=cloudflare&amp;service=&lt;SERVICE&gt;&amp;host=&lt;HOST&gt;&amp;ddtags=&lt;TAGS&gt;&quot;,&#10;  &quot;output_options&quot;: {&#10;    &quot;field_names&quot;: [&#10;      &quot;ClientIP&quot;,&#10;      &quot;ClientRequestHost&quot;,&#10;      &quot;ClientRequestMethod&quot;,&#10;      &quot;ClientRequestURI&quot;,&#10;      &quot;EdgeEndTimestamp&quot;,&#10;      &quot;EdgeResponseBytes&quot;,&#10;      &quot;EdgeResponseStatus&quot;,&#10;      &quot;EdgeStartTimestamp&quot;,&#10;      &quot;RayID&quot;&#10;    ],&#10;    &quot;timestamp_format&quot;: &quot;rfc3339&quot;&#10;  },&#10;  &quot;dataset&quot;: &quot;http_requests&quot;,&#10;  &quot;enabled&quot;: true&#10;}&#x27;</code></pre>
<p>Response:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;id&quot;: &lt;JOB_ID&gt;,&#10;    &quot;dataset&quot;: &quot;http_requests&quot;,&#10;    &quot;kind&quot;: &quot;&quot;,&#10;    &quot;enabled&quot;: true,&#10;    &quot;name&quot;: &quot;&lt;DOMAIN_NAME&gt;&quot;,&#10;    &quot;output_options&quot;: {&#10;      &quot;field_names&quot;: [&quot;ClientIP&quot;, &quot;ClientRequestHost&quot;, &quot;ClientRequestMethod&quot;, &quot;ClientRequestURI&quot;, &quot;EdgeEndTimestamp&quot;, &quot;EdgeResponseBytes&quot;, &quot;EdgeResponseStatus&quot; ,&quot;EdgeStartTimestamp&quot;, &quot;RayID&quot;],&#10;      &quot;timestamp_format&quot;: &quot;rfc3339&quot;&#10;    },&#10;    &quot;destination_conf&quot;: &quot;datadog://&lt;DATADOG_ENDPOINT_URL&gt;?header_DD-API-KEY=&lt;DATADOG_API_KEY&gt;&quot;,&#10;    &quot;last_complete&quot;: null,&#10;    &quot;last_error&quot;: null,&#10;    &quot;error_message&quot;: null&#10;  },&#10;  &quot;success&quot;: true&#10;}&#10;</code></pre>
<p>Refer to <a href="/logs/logpush/examples/example-logpush-curl/">Manage Logpush with cURL</a> to update a job (including enabling and disabling).</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note-1">Note</h3>
@markup("md", "content/.markup/bodies/10564.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note-2">Note</h3>
@markup("md", "content/.markup/bodies/10563.md")
</aside>
<h2 id="limitations">Limitations</h2>
<p>Note the following Logpush sending limitations, as described in the <a href="https://docs.datadoghq.com/api/latest/logs/">Datadog documentation</a>.</p>
<p>Send your logs to your Datadog platform over HTTP. Limits per HTTP request are the following:</p>
<ul>
<li>Maximum content size per payload (uncompressed): 5 MB</li>
<li>Maximum size for a single log: 1 MB</li>
<li>Maximum array size if sending multiple logs in an array: 1,000 entries</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/10562.md")
</aside>
