---
cp9:
  canonical: https://developers.cloudflare.com/logs/instant-logs/
  description: Stream live traffic logs from the dashboard or CLI.
  full_title: Instant Logs · Cloudflare Logs docs
  head_html: <title>Instant Logs · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Stream live traffic logs from the dashboard or CLI."><link rel="canonical" href="https://developers.cloudflare.com/logs/instant-logs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/instant-logs/index.md"><meta property="og:title" content="Instant Logs · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Stream live traffic logs from the dashboard or CLI."><meta property="og:url" content="https://developers.cloudflare.com/logs/instant-logs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Logs"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/instant-logs/#page","headline":"Instant Logs \u00b7 Cloudflare Logs docs","description":"Stream live traffic logs from the dashboard or CLI.","url":"https://developers.cloudflare.com/logs/instant-logs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/instant-logs/
  schema: 1
---
<p>Instant Logs allows Cloudflare customers to access a live stream of the traffic for their domain from the Cloudflare dashboard or from a command-line interface (CLI). Seeing data in real time allows you to investigate an attack, troubleshoot, debug or test out changes made to your network. Instant Logs is lightweight, simple to use and does not require any additional setup.</p>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="instant-logs-via-cloudflare-dashboard">Instant Logs via Cloudflare Dashboard</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Instant Logs</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select <strong>Start streaming</strong>.</p>
</li>
<li>
<p>(optional) Select <strong>Add filter</strong> to narrow down the events to be shown.</p>
</li>
</ol>
<p>Fields supported in our <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/">HTTP requests dataset</a> can be used when you add filters. Some fields with additional subscriptions required are not supported in the dashboard, you will need to use CLI instead.</p>
<p>Once a filter is selected and the stream has started, only log lines that match the filter criteria will appear. Filters are not applied retroactively to logs already showing in the dashboard.</p>
<h2 id="instant-logs-via-cli">Instant Logs via CLI</h2>
<h3 id="1-create-an-instant-logs-job"><ol>
<li>Create an Instant Logs Job</li>
</ol></h3>
<p>Create a session by sending a <code>POST</code> request to the Instant Logs job endpoint with the following parameters:</p>
<ul>
<li>
<p><strong>Fields</strong> - List any field available in the <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/">HTTP requests dataset</a>.</p>
</li>
<li>
<p><strong>Sample</strong> - The sample parameter is the sample rate of the records set by the client: <code>&quot;sample&quot;: 1</code> is 100% of records <code>&quot;sample&quot;: 10</code> is 10% and so on.</p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/791.md")
</aside>
<ul>
<li><strong>Filters</strong> - Use filters to drill down into specific events. Filters consist of three parts: key, operator and value.</li>
</ul>
<p>All supported operators can be found in the <a href="/logs/logpush/logpush-job/filters/">Filters</a> page.</p>
<p>Below we have three examples of filters:</p>
<pre tabindex="0"><code class="language-bash">&#35; Filter when client IP country is not Canada:&#10;&quot;filter&quot;: &quot;{\&quot;where\&quot;:{\&quot;and\&quot;:[{\&quot;key\&quot;:\&quot;ClientCountry\&quot;,\&quot;operator\&quot;:\&quot;neq\&quot;,\&quot;value\&quot;:\&quot;ca\&quot;}]}}&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">&#35; Filter when the status code returned from Cloudflare is either 200 or 201:&#10;&quot;filter&quot;: &quot;{\&quot;where\&quot;:{\&quot;and\&quot;:[{\&quot;key\&quot;:\&quot;EdgeResponseStatus\&quot;,\&quot;operator\&quot;:\&quot;in\&quot;,\&quot;value\&quot;:[200,201]}]}}&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-bash">&#35; Filter when the request path contains &quot;/static&quot; and the request hostname is &quot;example.com&quot;:&#10;&quot;filter&quot;: &quot;{\&quot;where\&quot;:{\&quot;and\&quot;:[{\&quot;key\&quot;:\&quot;ClientRequestPath\&quot;,\&quot;operator\&quot;:\&quot;contains\&quot;,\&quot;value\&quot;:\&quot;/static\&quot;}, {\&quot;where\&quot;:{\&quot;and\&quot;:[{\&quot;key\&quot;:\&quot;ClientRequestHost\&quot;,\&quot;operator\&quot;:\&quot;eq\&quot;,\&quot;value\&quot;:\&quot;example.com\&quot;}]}}&quot;&#10;</code></pre>
<p>Example request using cURL:</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/logpush/edge/jobs \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;fields&quot;: &quot;ClientIP,ClientRequestHost,ClientRequestMethod,ClientRequestURI,EdgeEndTimestamp,EdgeResponseBytes,EdgeResponseStatus,EdgeStartTimestamp,RayID&quot;,&#10;  &quot;sample&quot;: 100,&#10;  &quot;filter&quot;: &quot;&quot;,&#10;  &quot;kind&quot;: &quot;instant-logs&quot;&#10;}&#x27;</code></pre>
<p>Response:</p>
<p>The response will include a new field called <strong>destination_conf</strong>. The value of this field is your unique WebSocket address that will receive messages from Cloudflare's global network.</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: {&#10;    &quot;id&quot;: &lt;JOB_ID&gt;,&#10;    &quot;fields&quot;: &quot;ClientIP,ClientRequestHost,ClientRequestMethod,ClientRequestURI,EdgeEndTimestamp,EdgeResponseBytes,EdgeResponseStatus,EdgeStartTimestamp,RayID&quot;,&#10;    &quot;sample&quot;: 100,&#10;    &quot;filter&quot;: &quot;&quot;,&#10;    &quot;destination_conf&quot;: &quot;wss://logs.cloudflare.com/instant-logs/ws/sessions/&lt;SESSION_ID&gt;&quot;,&#10;    &quot;kind&quot;: &quot;instant-logs&quot;&#10;  },&#10;  &quot;success&quot;: true&#10;}&#10;</code></pre>
<h3 id="2-connect-to-websocket"><ol start="2">
<li>Connect to WebSocket</li>
</ol></h3>
<p>Using a CLI utility like <a href="https://github.com/vi/websocat">Websocat</a>, you can connect to the WebSocket and start immediately receiving logs.</p>
<pre tabindex="0"><code class="language-bash">websocat wss://logs.cloudflare.com/instant-logs/ws/sessions/&lt;SESSION_ID&gt;&#10;</code></pre>
<p>Response:</p>
<p>Once connected to the websocket, you will receive messages of line-delimited JSON.</p>
<h3 id="angle-grinder">Angle Grinder</h3>
<p>Now that you have a connection to Cloudflare's websocket and are receiving logs from Cloudflare's global network, you can start slicing and dicing the logs. A handy tool for this is <a href="https://github.com/rcoh/angle-grinder">Angle Grinder</a>. Angle Grinder lets you apply filtering, transformations and aggregations on stdin with first class JSON support. For example, to get the number of visitors from each country you can sum the number of events by the <code>ClientCountry</code> field.</p>
<pre tabindex="0"><code class="language-bash">websocat wss://logs.cloudflare.com/instant-logs/ws/sessions/&lt;SESSION_ID&gt; | agrind &#x27;* | json | sum(sampleInterval) by ClientCountry&#x27;&#10;</code></pre>
<p>Response:</p>
<table>
<thead>
<tr>
<th><strong>ClientCountry</strong></th>
<th><strong>_sum</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>pt</td>
<td><code>4</code></td>
</tr>
<tr>
<td>fr</td>
<td><code>3</code></td>
</tr>
<tr>
<td>us</td>
<td><code>3</code></td>
</tr>
<tr>
<td>om</td>
<td><code>2</code></td>
</tr>
<tr>
<td>ar</td>
<td><code>1</code></td>
</tr>
<tr>
<td>au</td>
<td><code>1</code></td>
</tr>
</tbody>
</table>
<h2 id="datasets-available">Datasets available</h2>
<p>For the moment, <code>HTTP requests</code> is the only dataset supported. In the future, we will expand to other datasets.</p>
<h2 id="export">Export</h2>
<p>You can download the table of logs that appears in the dashboard, in JSON format via the <strong>Export</strong> button.</p>
<h2 id="limits">Limits</h2>
<p>Instant Logs has three limits set in place:</p>
<ul>
<li>Only one active Instant Logs session per zone.</li>
<li>Maximum session time is 60 minutes.</li>
<li>If you stop listening to a socket for more than five minutes.</li>
</ul>
<p>If either of these limits are reached, the logs stream will automatically stop.</p>
<h2 id="connect-with-us">Connect with us</h2>
<p>If you have any feature requests or notice any bugs, share your feedback directly with us by joining the <a href="https://discord.cloudflare.com">Cloudflare Developers community on Discord</a>.</p>
