---
cp9:
  canonical: https://developers.cloudflare.com/workers/observability/logs/logpush/
  description: Send Workers Trace Event Logs to a supported third party, such as a storage or logging provider.
  full_title: Workers Logpush · Cloudflare Workers docs
  head_html: <title>Workers Logpush · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Send Workers Trace Event Logs to a supported third party, such as a storage or logging provider."><link rel="canonical" href="https://developers.cloudflare.com/workers/observability/logs/logpush/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/observability/logs/logpush/index.md"><meta property="og:title" content="Workers Logpush · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Send Workers Trace Event Logs to a supported third party, such as a storage or logging provider."><meta property="og:url" content="https://developers.cloudflare.com/workers/observability/logs/logpush/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/observability/logs/logpush/#page","headline":"Workers Logpush \u00b7 Cloudflare Workers docs","description":"Send Workers Trace Event Logs to a supported third party, such as a storage or logging provider.","url":"https://developers.cloudflare.com/workers/observability/logs/logpush/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/observability/logs/logpush/
  schema: 1
---
<p><a href="/logs/logpush/">Cloudflare Logpush</a> supports the ability to send <a href="/logs/logpush/logpush-job/datasets/account/workers_trace_events/">Workers Trace Event Logs</a> to a <a href="/logs/logpush/logpush-job/enable-destinations/">supported destination</a>. Workers Trace Events Logpush includes metadata about requests and responses, unstructured <code>console.log()</code> messages and any uncaught exceptions. This product is available on the Workers Paid plan. For pricing information, refer to <a href="/workers/platform/pricing/#workers-trace-events-logpush">Pricing</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="prefer-opentelemetry-export">Prefer OpenTelemetry export</h3>
@markup("md", "content/.markup/bodies/17043.md")
</aside>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17042.md")
</aside>
<h2 id="verify-your-logpush-access">Verify your Logpush access</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="wrangler-version">Wrangler version</h3>
@markup("md", "content/.markup/bodies/17041.md")
</aside>
<p>To configure a Logpush job, verify that your Cloudflare account role can use Logpush. To check your role:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Members</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Check your account permissions. Roles with Logpush configuration access are different than Workers permissions. Super Administrators, Administrators, and the Log Share roles have full access to Logpush.</li>
</ol>
<p>Alternatively, create a new <a href="/fundamentals/api/get-started/create-token/">API token</a> scoped at the Account level with Logs Edit permissions.</p>
<h2 id="create-a-logpush-job">Create a Logpush job</h2>
<h3 id="via-the-cloudflare-dashboard">Via the Cloudflare dashboard</h3>
<p>To create a Logpush job in the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Logpush</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Create a Logpush job</strong>.</li>
<li>Select a destination and configure it, if needed.</li>
<li>Select <strong>Workers trace events</strong> as the data set &gt; <strong>Next</strong>.</li>
<li>If needed, customize your data fields. Otherwise, select <strong>Next</strong>.</li>
<li>Follow the instructions on the dashboard to verify ownership of your data's destination and complete job creation.</li>
</ol>
<h3 id="via-curl">Via cURL</h3>
<p>The following example sends Workers logs to R2. For more configuration options, refer to <a href="/logs/logpush/logpush-job/enable-destinations/">Enable destinations</a> and <a href="/logs/logpush/logpush-job/api-configuration/">API configuration</a> in the Logs documentation.</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/logpush/jobs&quot; \&#10;&#45;-header &#x27;X-Auth-Key: &lt;API_KEY&gt;&#x27; \&#10;&#45;-header &#x27;X-Auth-Email: &lt;EMAIL&gt;&#x27; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;{&#10;  &quot;name&quot;: &quot;workers-logpush&quot;,&#10;  &quot;output_options&quot;: {&#10;    &quot;field_names&quot;: [&quot;Event&quot;, &quot;EventTimestampMs&quot;, &quot;Outcome&quot;, &quot;Exceptions&quot;, &quot;Logs&quot;, &quot;ScriptName&quot;],&#10;  },&#10;  &quot;destination_conf&quot;: &quot;r2://&lt;BUCKET_PATH&gt;/{DATE}?account-id=&lt;ACCOUNT_ID&gt;&amp;access-key-id=&lt;R2_ACCESS_KEY_ID&gt;&amp;secret-access-key=&lt;R2_SECRET_ACCESS_KEY&gt;&quot;,&#10;  &quot;dataset&quot;: &quot;workers_trace_events&quot;,&#10;  &quot;enabled&quot;: true&#10;}&#x27; | jq .&#10;</code></pre>
<p>In Logpush, you can configure <a href="/logs/logpush/logpush-job/filters/">filters</a> and a <a href="/logs/logpush/logpush-job/api-configuration/#sampling-rate">sampling rate</a> to have more control of the volume of data that is sent to your configured destination. For example, if you only want to receive logs for requests that did not result in an exception, add the following <code>filter</code> JSON property below <code>output_options</code>:</p>
<p><code>&quot;filter&quot;:&quot;{\&quot;where\&quot;: {\&quot;key\&quot;:\&quot;Outcome\&quot;,\&quot;operator\&quot;:\&quot;!eq\&quot;,\&quot;value\&quot;:\&quot;exception\&quot;}}&quot;</code></p>
<h2 id="enable-logging-on-your-worker">Enable logging on your Worker</h2>
<h3 id="local-development">Local development</h3>
<p>Enable logging on your Worker by adding a new property, <code>logpush = true</code>, to your Wrangler file. This can be added either in the top-level configuration or under an <a href="/workers/wrangler/environments/">environment</a>. Any new Workers with this property will automatically get picked up by the Logpush job.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17044.md")
</div>
<p>Configure via multipart script upload API:</p>
<pre tabindex="0"><code class="language-bash">curl --request PUT \&#10;&quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/scripts/{script_name}&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-form &#x27;metadata={&quot;main_module&quot;: &quot;my-worker.js&quot;, &quot;logpush&quot;: true}&#x27; \&#10;&#45;-form &#x27;&quot;my-worker.js&quot;=@./my-worker.js;type=application/javascript+module&#x27;&#10;</code></pre>
<h3 id="dashboard">Dashboard</h3>
<p>To enable Logpush logging via the dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your Worker.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Observability</strong>.</li>
<li>For <strong>Logpush</strong>, select <strong>Enable</strong> (this is only available if you have already <a href="/workers/observability/logs/logpush/#create-a-logpush-job">created a logpush job</a>).</li>
</ol>
<h2 id="limits">Limits</h2>
<p>The <code>logs</code> and <code>exceptions</code> fields have a combined limit of 16,384 characters before fields will start being truncated. Characters are counted in the order of all <code>exception.name</code>s, <code>exception.message</code>s, and then <code>log.message</code>s.</p>
<p>Once that character limit is reached all fields will be truncated with <code>&quot;&lt;&lt;&lt;Logpush: *field* truncated&gt;&gt;&gt;&quot;</code> for one message before dropping logs or exceptions.</p>
<h3 id="example">Example</h3>
<p>To illustrate this, suppose our Logpush event looks like the JSON below and the limit is 50 characters (rather than the actual limit of 16,384). The algorithm will:</p>
<ol>
<li>Count the characters in <code>exception.names</code>:
<ol>
<li><code>&quot;SampleError&quot;</code> and <code>&quot;AuthError&quot;</code> as 20 characters.</li>
</ol>
</li>
<li>Count the characters in <code>exception.message</code>:
<ol>
<li><code>&quot;something went wrong&quot;</code> counted as 20 characters leaving 10 characters remaining.</li>
<li>The first 10 characters of <code>&quot;unable to process request authentication from client&quot;</code> will be taken and counted before being truncated to <code>&quot;unable to &lt;&lt;&lt;Logpush: exception messages truncated&gt;&gt;&gt;&quot;</code>.</li>
</ol>
</li>
<li>Count the characters in <code>log.message</code>:
<ol>
<li>We've already begun truncation, so <code>&quot;Hello &quot;</code> will be replaced with <code>&quot;&lt;&lt;&lt;Logpush: messages truncated&gt;&gt;&gt;&quot;</code> and <code>&quot;World!&quot;</code> will be dropped.</li>
</ol>
</li>
</ol>
<h4 id="sample-input">Sample Input</h4>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;Exceptions&quot;: [&#10;		{&#10;			&quot;Name&quot;: &quot;SampleError&quot;,&#10;			&quot;Message&quot;: &quot;something went wrong&quot;,&#10;			&quot;TimestampMs&quot;: 0&#10;		},&#10;		{&#10;			&quot;Name&quot;: &quot;AuthError&quot;,&#10;			&quot;Message&quot;: &quot;unable to process request authentication from client&quot;,&#10;			&quot;TimestampMs&quot;: 1&#10;		}&#10;	],&#10;	&quot;Logs&quot;: [&#10;		{&#10;			&quot;Level&quot;: &quot;log&quot;,&#10;			&quot;Message&quot;: [&quot;Hello &quot;],&#10;			&quot;TimestampMs&quot;: 0&#10;		},&#10;		{&#10;			&quot;Level&quot;: &quot;log&quot;,&#10;			&quot;Message&quot;: [&quot;World!&quot;],&#10;			&quot;TimestampMs&quot;: 0&#10;		}&#10;	]&#10;}&#10;</code></pre>
<h4 id="sample-output">Sample Output</h4>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;Exceptions&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;SampleError&quot;,&#10;			&quot;message&quot;: &quot;something went wrong&quot;,&#10;			&quot;TimestampMs&quot;: 0&#10;		},&#10;		{&#10;			&quot;name&quot;: &quot;AuthError&quot;,&#10;			&quot;message&quot;: &quot;unable to &lt;&lt;&lt;Logpush: exception messages truncated&gt;&gt;&gt;&quot;,&#10;			&quot;TimestampMs&quot;: 1&#10;		}&#10;	],&#10;	&quot;Logs&quot;: [&#10;		{&#10;			&quot;Level&quot;: &quot;log&quot;,&#10;			&quot;Message&quot;: [&quot;&lt;&lt;&lt;Logpush: messages truncated&gt;&gt;&gt;&quot;],&#10;			&quot;TimestampMs&quot;: 0&#10;		}&#10;	]&#10;}&#10;</code></pre>
