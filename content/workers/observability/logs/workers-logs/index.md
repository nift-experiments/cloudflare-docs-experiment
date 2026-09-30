---
cp9:
  canonical: https://developers.cloudflare.com/workers/observability/logs/workers-logs/
  description: Store, filter, and analyze log data emitted from Cloudflare Workers.
  full_title: Workers Logs · Cloudflare Workers docs
  head_html: <title>Workers Logs · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Store, filter, and analyze log data emitted from Cloudflare Workers."><link rel="canonical" href="https://developers.cloudflare.com/workers/observability/logs/workers-logs/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/observability/logs/workers-logs/index.md"><meta property="og:title" content="Workers Logs · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Store, filter, and analyze log data emitted from Cloudflare Workers."><meta property="og:url" content="https://developers.cloudflare.com/workers/observability/logs/workers-logs/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/observability/logs/workers-logs/#page","headline":"Workers Logs \u00b7 Cloudflare Workers docs","description":"Store, filter, and analyze log data emitted from Cloudflare Workers.","url":"https://developers.cloudflare.com/workers/observability/logs/workers-logs/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/observability/logs/workers-logs/
  schema: 1
---
<p>Workers Logs lets you automatically collect, store, filter, and analyze logging data emitted from Cloudflare Workers. Data is written to your Cloudflare Account, and you can query it in the dashboard for each of your Workers. All newly created Workers will come with the observability setting enabled by default.</p>
<p>Logs include <a href="/workers/observability/logs/workers-logs/#invocation-logs">invocation logs</a>, <a href="/workers/observability/logs/workers-logs/#custom-logs">custom logs</a>, errors, and uncaught exceptions.</p>
<p><img src="/assets/upstream/images/workers-observability/wobs_workers_events_122.png" alt="Example showing the Workers Logs Dashboard" /></p>
<p>To send logs to a third party, use <a href="/workers/observability/exporting-opentelemetry-data/">OpenTelemetry export</a> (recommended), <a href="/workers/observability/logs/logpush/">Workers Logpush</a>, or <a href="/workers/observability/logs/tail-workers/">Tail Workers</a>.</p>
<h2 id="enable-workers-logs">Enable Workers Logs</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="wrangler-version">Wrangler version</h3>
@markup("md", "content/.markup/bodies/17028.md")
</aside>
<p>You must add the observability setting for your Worker to write logs to Workers Logs. Add the following setting to your Worker's Wrangler file and redeploy your Worker.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17029.md")
</div>
<p><a href="/workers/observability/logs/workers-logs/#head-based-sampling">Head-based sampling</a> allows you set the percentage of Workers requests that are logged.</p>
<h3 id="enabling-with-environments">Enabling with environments</h3>
<p><a href="/workers/wrangler/environments/">Environments</a> allow you to deploy the same Worker application with different configurations. For example, you may want to configure a different <code>head_sampling_rate</code> to staging and production. To configure observability for an environment named <code>staging</code>: 1. Add the following configuration below <code>[env.staging]</code></p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17030.md")
</div>
<pre tabindex="0"><code>2. Deploy your Worker with `npx wrangler deploy -e staging`&#10;3. Repeat step 1 and 2 for each environment.&#10;</code></pre>
<h2 id="view-logs-from-the-dashboard">View logs from the dashboard</h2>
<p>Access logs for your Worker from the Cloudflare dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>Overview</strong>, select your <strong>Worker</strong>.</li>
<li>Select <strong>Observability</strong>.</li>
</ol>
<h2 id="best-practices">Best Practices</h2>
<h3 id="logging-structured-json-objects">Logging structured JSON objects</h3>
<p>To get the most out of Workers Logs, it is recommended you log in JSON format. Workers Logs automatically extracts the fields and indexes them intelligently in the database. The benefit of this structured logging technique is in how it allows you to easily segment data across any dimension for fields with unlimited cardinality. Consider the following scenarios:</p>
<table>
<thead>
<tr>
<th>Scenario</th>
<th>Logging Code</th>
<th>Event Log (Partial)</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td><code>console.log(&quot;user_id: &quot; + 123)</code></td>
<td><code>{message: &quot;user_id: 123&quot;}</code></td>
</tr>
<tr>
<td>2</td>
<td><code>console.log({user_id: 123})</code></td>
<td><code>{user_id: 123}</code></td>
</tr>
<tr>
<td>3</td>
<td><code>console.log({user_id: 123, user_email: &quot;a@example.com&quot;})</code></td>
<td><code>{user_id: 123, user_email: &quot;a@example.com&quot;}</code></td>
</tr>
</tbody>
</table>
<p>The difference between these examples is in how you index your logs to enable faster queries. In scenario 1, the <code>user_id</code> is embedded within a message. To find all logs relating to a particular user_id, you would have to run a text match. In scenarios 2 and 3, your logs can be filtered against the keys <code>user_id</code> and <code>user_email</code>.</p>
<h2 id="features">Features</h2>
<h3 id="invocation-logs">Invocation Logs</h3>
<p>Each Workers invocation returns a single invocation log that contains details such as the Request, Response, and related metadata. These invocation logs can be identified by the field <code>$cloudflare.$metadata.type = &quot;cf-worker-event&quot;</code>. Each invocation log is enriched with information available to Cloudflare in the context of the invocation.</p>
<p>In the Workers Logs UI, logs are presented with a localized timestamp and a message. The message is dependent on the invocation handler. For example, Fetch requests will have a message describing the request method and the request URL, while cron events will be listed as cron. Below is a list of invocation handlers along with their invocation message.</p>
<p>Invocation logs can be disabled in wrangler by adding the <code>invocation_logs = false</code> configuration.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17031.md")
</div>
<table>
<thead>
<tr>
<th>Invocation Handler</th>
<th>Invocation Message</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/durable-objects/api/alarms/">Alarm</a></td>
<td>&lt;Scheduled Time&gt;</td>
</tr>
<tr>
<td><a href="/email-service/api/route-emails/email-handler/">Email</a></td>
<td>&lt;Email Recipient&gt;</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/handlers/fetch/">Fetch</a></td>
<td>&lt;Method&gt; &lt;URL&gt;</td>
</tr>
<tr>
<td><a href="/queues/configuration/javascript-apis/#consumer">Queue</a></td>
<td>&lt;Queue Name&gt;</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/handlers/scheduled/">Cron</a></td>
<td>&lt;UNIX-cron schedule&gt;</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/handlers/tail/">Tail</a></td>
<td>tail</td>
</tr>
<tr>
<td><a href="/workers/runtime-apis/rpc/">RPC</a></td>
<td>&lt;RPC method&gt;</td>
</tr>
<tr>
<td><a href="/workers/examples/websockets/">WebSocket</a></td>
<td>&lt;WebSocket Event Type&gt;</td>
</tr>
</tbody>
</table>
<h3 id="custom-logs">Custom logs</h3>
<p>By default a Worker will emit <a href="/workers/observability/logs/workers-logs/#invocation-logs">invocation logs</a> containing details about the request, response and related metadata.</p>
<p>You can also add custom logs throughout your code. Any <code>console.log</code> statements within your Worker will be visible in Workers Logs. The following example demonstrates a custom <code>console.log</code> within a Worker request handler.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/17034.md")
</div></div>
<p>After you deploy the code above, view your Worker's logs in <a href="/workers/observability/logs/workers-logs/#view-logs-from-the-dashboard">the dashboard</a> or with <a href="/workers/observability/logs/real-time-logs/">real-time logs</a>.</p>
<h3 id="head-based-sampling">Head-based sampling</h3>
<p>Head-based sampling allows you to log a percentage of incoming requests to your Cloudflare Worker. Especially for high-traffic applications, this helps reduce log volume and manage costs, while still providing meaningful insights into your application's performance. When you configure a head-based sampling rate, you can control the percentage of requests that get logged. All logs within the context of the request are collected.</p>
<p>To enable head-based sampling, set <code>head_sampling_rate</code> within the observability configuration. The valid range is from 0 to 1, where 0 indicates zero out of one hundred requests are logged, and 1 indicates every request is logged. If <code>head_sampling_rate</code> is unspecified, it is configured to a default value of 1 (100%). In the example below, <code>head_sampling_rate</code> is set to 0.01, which means one out of every one hundred requests is logged.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17035.md")
</div>
<h2 id="limits">Limits</h2>
<table>
<thead>
<tr>
<th>Description</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Maximum log retention period</td>
<td>7 Days</td>
</tr>
<tr>
<td>Maximum logs per account per day<sup>1</sup></td>
<td>5 Billion</td>
</tr>
<tr>
<td>Maximum log size<sup>2</sup></td>
<td>256 KB</td>
</tr>
</tbody>
</table>
<p><sup>1</sup> There is a daily limit of 5 billion logs per account per day. After
the limit is exceed, a 1% head-based sample will be applied for the remainder of
the day.</p>
<p><sup>2</sup> A single log has a maximum size limit of <a href="/workers/platform/limits/#log-size">256
KB</a>. Logs exceeding that size will be
truncated and the log's <code>$cloudflare.truncated</code> field will be set to true.</p>
<h2 id="pricing">Pricing</h2>
<p>Workers Logs is included in both the Free and Paid <a href="/workers/platform/pricing/">Workers plans</a>.</p>
<table>
<thead>
<tr>
<th></th>
<th>Log Events Written</th>
<th>Retention</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Workers Free</strong></td>
<td>200,000 per day</td>
<td>3 Days</td>
</tr>
<tr>
<td><strong>Workers Paid</strong></td>
<td>20 million included per month <br /> +$0.60 per additional million</td>
<td>7 Days</td>
</tr>
</tbody>
</table>
<h3 id="examples">Examples</h3>
<h4 id="example-1">Example 1</h4>
<p>A Worker serves 15 million requests per month. Each request emits 1 invocation log and 1 <code>console.log</code>. <code>head_sampling_rate</code> is configured to 1.</p>
<table>
<thead>
<tr>
<th></th>
<th>Monthly Costs</th>
<th>Formula</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Logs</strong></td>
<td>$6.00</td>
<td>((15,000,000 requests per month * 2 logs per request * 100% sample) - 20,000,000 included logs) / 1,000,000 * $0.60</td>
</tr>
<tr>
<td><strong>Total</strong></td>
<td>$6.00</td>
<td></td>
</tr>
</tbody>
</table>
<h4 id="example-2">Example 2</h4>
<p>A Worker serves 1 billion requests per month. Each request emits 1 invocation log and 1 <code>console.log</code>. <code>head_sampling_rate</code> is configured to 0.1.</p>
<table>
<thead>
<tr>
<th></th>
<th>Monthly Costs</th>
<th>Formula</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Logs</strong></td>
<td>$108.00</td>
<td>((1,000,000,000 requests per month * 2 logs per request * 10% sample) - 20,000,000 included logs) / 1,000,000 * $0.60</td>
</tr>
<tr>
<td><strong>Total</strong></td>
<td>$108.00</td>
<td></td>
</tr>
</tbody>
</table>
