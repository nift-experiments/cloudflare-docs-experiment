---
cp9:
  canonical: https://developers.cloudflare.com/workers/platform/pricing/
  description: Workers plans and pricing information.
  full_title: Pricing · Cloudflare Workers docs
  head_html: <title>Pricing · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Workers plans and pricing information."><link rel="canonical" href="https://developers.cloudflare.com/workers/platform/pricing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/platform/pricing/index.md"><meta property="og:title" content="Pricing · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Workers plans and pricing information."><meta property="og:url" content="https://developers.cloudflare.com/workers/platform/pricing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/platform/pricing/#page","headline":"Pricing \u00b7 Cloudflare Workers docs","description":"Workers plans and pricing information.","url":"https://developers.cloudflare.com/workers/platform/pricing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/platform/pricing/
  schema: 1
---
<p>By default, users have access to the Workers Free plan. The Workers Free plan includes limited usage of Workers, Pages Functions, Workers KV and Hyperdrive. Read more about the <a href="/workers/platform/limits/#account-plan-limits">Free plan limits</a>.</p>
<p>The Workers Paid plan includes Workers, Pages Functions, Workers KV, Hyperdrive, and Durable Objects usage for a minimum charge of $5 USD per month for an account. The plan includes increased initial usage allotments, with clear charges for usage that exceeds the base plan. There are no additional charges for data transfer (egress) or throughput (bandwidth).</p>
<p>All included usage is on a monthly basis.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="pages-functions-billing">Pages Functions billing</h3>
@markup("md", "content/.markup/bodies/16203.md")
</aside>
<h2 id="workers">Workers</h2>
<p>Users on the Workers Paid plan have access to the Standard usage model. Workers Enterprise accounts are billed based on the usage model specified in their contract. To switch to the Standard usage model, contact your Account Manager.</p>
<table>
<thead>
<tr>
<th></th>
<th>Requests<sup>1, 2, 3, 4</sup></th>
<th>Duration</th>
<th>CPU time</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Free</strong></td>
<td>100,000 per day</td>
<td>No charge for duration</td>
<td>10 milliseconds of CPU time per invocation</td>
</tr>
<tr>
<td><strong>Standard</strong></td>
<td>10 million included per month <br /> +$0.30 per additional million</td>
<td>No charge or limit for duration</td>
<td>30 million CPU milliseconds included per month<br /> +$0.02 per additional million CPU milliseconds<br /><br/> Max of <a href="/workers/platform/limits/#account-plan-limits">5 minutes of CPU time</a> per invocation (default: 30 seconds)<br /> Max of 15 minutes of CPU time per <a href="/workers/configuration/cron-triggers/">Cron Trigger</a> or <a href="/queues/configuration/javascript-apis/#consumer">Queue Consumer</a> invocation</td>
</tr>
</tbody>
</table>
<p><sup>1</sup> Inbound requests to your Worker. Cloudflare does not bill for
<a href="/workers/platform/limits/#subrequests">subrequests</a> you make from your Worker.</p>
<p><sup>2</sup> WebSocket connections made to a Worker are charged as a request,
representing the initial <code>Upgrade</code> connection made to establish the WebSocket.
WebSocket messages routed through a Worker do not count as requests.</p>
<p><sup>3</sup> Requests to static assets are free and unlimited.</p>
<p><sup>4</sup> When <a href="/workers/cache/">Workers Caching</a> is enabled, requests served
from the Worker's cache are billed at the same per-request rate as requests that
invoke the Worker. This includes requests to <a href="/workers/static-assets/billing-and-limitations/">static
assets</a> and <a href="/workers/platform/pricing/#service-bindings">worker-to-worker
invocations</a>.
CPU time is only billed when the Worker runs (on a
cache miss or bypass).</p>
<h3 id="example-pricing">Example pricing</h3>
<h4 id="example-1">Example 1</h4>
<p>A Worker that serves 15 million requests per month, and uses an average of 7 milliseconds (ms) of CPU time per request, would have the following estimated costs:</p>
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
<td><strong>Subscription</strong></td>
<td>$5.00</td>
<td></td>
</tr>
<tr>
<td><strong>Requests</strong></td>
<td>$1.50</td>
<td>(15,000,000 requests - 10,000,000 included requests) / 1,000,000 * $0.30</td>
</tr>
<tr>
<td><strong>CPU time</strong></td>
<td>$1.50</td>
<td>((7 ms of CPU time per request * 15,000,000 requests) - 30,000,000 included CPU ms) / 1,000,000 * $0.02</td>
</tr>
<tr>
<td><strong>Total</strong></td>
<td>$8.00</td>
<td></td>
</tr>
</tbody>
</table>
<h4 id="example-2">Example 2</h4>
<p>A project that serves 15 million requests per month, with 80% (12 million) requests serving <a href="/workers/static-assets/">static assets</a> and the remaining invoking dynamic Worker code. The Worker uses an average of 7 milliseconds (ms) of time per request.</p>
<p>Requests to static assets are free and unlimited. This project would have the following estimated costs:</p>
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
<td><strong>Subscription</strong></td>
<td>$5.00</td>
<td></td>
</tr>
<tr>
<td><strong>Requests to static assets</strong></td>
<td>$0</td>
<td>-</td>
</tr>
<tr>
<td><strong>Requests to Worker</strong></td>
<td>$0</td>
<td>-</td>
</tr>
<tr>
<td><strong>CPU time</strong></td>
<td>$0</td>
<td>-</td>
</tr>
<tr>
<td><strong>Total</strong></td>
<td>$5.00</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h4 id="example-3">Example 3</h4>
<p>A Worker that runs on a <a href="/workers/configuration/cron-triggers/">Cron Trigger</a> once an hour to collect data from multiple APIs, process the data and create a report.</p>
<ul>
<li>720 requests/month</li>
<li>3 minutes (180,000ms) of CPU time per request</li>
</ul>
<p>In this scenario, the estimated monthly cost would be calculated as:</p>
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
<td><strong>Subscription</strong></td>
<td>$5.00</td>
<td></td>
</tr>
<tr>
<td><strong>Requests</strong></td>
<td>$0.00</td>
<td>-</td>
</tr>
<tr>
<td><strong>CPU time</strong></td>
<td>$1.99</td>
<td>((180,000 ms of CPU time per request * 720 requests) - 30,000,000 included CPU ms) / 1,000,000 * $0.02</td>
</tr>
<tr>
<td><strong>Total</strong></td>
<td>$6.99</td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h4 id="example-4">Example 4</h4>
<p>A high traffic Worker that serves 100 million requests per month, and uses an average of 7 milliseconds (ms) of CPU time per request, would have the following estimated costs:</p>
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
<td><strong>Subscription</strong></td>
<td>$5.00</td>
<td></td>
</tr>
<tr>
<td><strong>Requests</strong></td>
<td>$27.00</td>
<td>(100,000,000 requests - 10,000,000 included requests) / 1,000,000 * $0.30</td>
</tr>
<tr>
<td><strong>CPU time</strong></td>
<td>$13.40</td>
<td>((7 ms of CPU time per request * 100,000,000 requests) - 30,000,000 included CPU ms) / 1,000,000 * $0.02</td>
</tr>
<tr>
<td><strong>Total</strong></td>
<td>$45.40</td>
<td></td>
</tr>
</tbody>
</table>
<h4 id="example-5-worker-with-caching">Example 5: Worker with caching</h4>
<p>The same Worker as Example 4, but with <a href="/workers/cache/">Workers Caching</a> enabled and an 80% cache hit rate. 80 million requests are served from cache and 20 million invoke the Worker. Cache hits count as requests but do not consume CPU time.</p>
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
<td><strong>Subscription</strong></td>
<td>$5.00</td>
<td></td>
</tr>
<tr>
<td><strong>Requests</strong></td>
<td>$27.00</td>
<td>(100,000,000 requests - 10,000,000 included requests) / 1,000,000 * $0.30</td>
</tr>
<tr>
<td><strong>CPU time</strong></td>
<td>$2.20</td>
<td>((7 ms of CPU time per request * 20,000,000 requests) - 30,000,000 included CPU ms) / 1,000,000 * $0.02</td>
</tr>
<tr>
<td><strong>Total</strong></td>
<td>$34.20</td>
<td></td>
</tr>
</tbody>
</table>
<p>For details on what is cached and how to enable caching, refer to <a href="/workers/cache/">Cache</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="custom-limits">Custom limits</h3>
@markup("md", "content/.markup/bodies/16202.md")
</aside>
<h3 id="how-to-switch-usage-models">How to switch usage models</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16201.md")
</aside>
<p>Users on the Workers Paid plan have access to the Standard usage model. However, some users may still have a legacy usage model configured.
Legacy usage models include Workers Unbound and Workers Bundled. Users are advised to move to the Workers Standard usage model.
Changing the usage model only affects billable usage, and has no technical implications.</p>
<p>To change your default account-wide usage model:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Find <strong>Usage Model</strong> on the right-side menu &gt; <strong>Change</strong>.</li>
</ol>
<p>Usage models may be changed at the individual Worker level:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>Overview</strong>, select your Worker &gt; <strong>Settings</strong> &gt; <strong>Usage Model</strong>.</li>
</ol>
<p>Existing Workers will not be impacted when changing the default usage model. You may change the usage model for individual Workers without affecting your account-wide default usage model.</p>
<h2 id="workers-logs">Workers Logs</h2>
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
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="workers-logs-documentation">Workers Logs documentation</h3>
@markup("md", "content/.markup/bodies/16200.md")
</aside>
<h2 id="workers-trace-events-logpush">Workers Trace Events Logpush</h2>
<p>Workers Logpush is only available on the Workers Paid plan.</p>
<table>
<thead>
<tr>
<th></th>
<th>Paid plan</th>
</tr>
</thead>
<tbody>
<tr>
<td>Requests <sup>1</sup></td>
<td>10 million / month, +$0.05/million</td>
</tr>
</tbody>
</table>
<p><sup>1</sup> Workers Logpush charges for request logs that reach your end
destination after applying filtering or sampling.</p>
<h2 id="workers-kv">Workers KV</h2>
<p>Workers KV is included in both the Free and Paid <a href="/workers/platform/pricing/">Workers plans</a>.</p>
<table>
<thead>
<tr>
<th></th>
<th>Free plan<sup>1</sup></th>
<th>Paid plan</th>
</tr>
</thead>
<tbody>
<tr>
<td>Keys read</td>
<td>100,000 / day</td>
<td>10 million/month, + $0.50/million</td>
</tr>
<tr>
<td>Keys written</td>
<td>1,000 / day</td>
<td>1 million/month, + $5.00/million</td>
</tr>
<tr>
<td>Keys deleted</td>
<td>1,000 / day</td>
<td>1 million/month, + $5.00/million</td>
</tr>
<tr>
<td>List requests</td>
<td>1,000 / day</td>
<td>1 million/month, + $5.00/million</td>
</tr>
<tr>
<td>Stored data</td>
<td>1 GB</td>
<td>1 GB, + $0.50/ GB-month</td>
</tr>
</tbody>
</table>
<p><sup>1</sup> The Workers Free plan includes limited Workers KV usage. All limits
reset daily at 00:00 UTC. If you exceed any one of these limits, further
operations of that type will fail with an error.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16199.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="kv-documentation">KV documentation</h3>
@markup("md", "content/.markup/bodies/16198.md")
</aside>
<h2 id="hyperdrive">Hyperdrive</h2>
<p>Hyperdrive is included in both the Free and Paid <a href="/workers/platform/pricing/">Workers plans</a>.</p>
<table>
<thead>
<tr>
<th></th>
<th>Free plan<sup><a href="#footnote-workers-hyperdrive-pricing-mdx-1">1</a></sup></th>
<th>Paid plan</th>
</tr>
</thead>
<tbody>
<tr>
<td>Database queries<sup><a href="#footnote-workers-hyperdrive-pricing-mdx-2">2</a></sup></td>
<td>100,000 / day</td>
<td>Unlimited</td>
</tr>
</tbody>
</table>
<details class="nb-details" open><summary>Footnotes</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/16204.md")
</div></details>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-workers-hyperdrive-pricing-mdx-1">The Workers Free plan includes limited Hyperdrive usage. All limits reset daily at 00:00 UTC. If you exceed any one of these limits, further operations of that type will fail with an error.</li>
<li id="footnote-workers-hyperdrive-pricing-mdx-2">Database queries refers to any database statement made via Hyperdrive, whether a query (`SELECT`), a modification (`INSERT`,`UPDATE`, or `DELETE`) or a schema change (`CREATE`, `ALTER`, `DROP`).</li></ol></section>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="hyperdrive-documentation">Hyperdrive documentation</h3>
@markup("md", "content/.markup/bodies/16197.md")
</aside>
<h2 id="queues">Queues</h2>
<p>Cloudflare Queues charges for the total number of operations against each of your queues during a given month.</p>
<ul>
<li>An operation is counted for each 64 KB of data that is written, read, or deleted.</li>
<li>Messages larger than 64 KB are charged as if they were multiple messages: for example, a 65 KB message and a 127 KB message would both incur two operation charges when written, read, or deleted.</li>
<li>A KB is defined as 1,000 bytes, and each message includes approximately 100 bytes of internal metadata.</li>
<li>Operations are per message, not per batch. A batch of 10 messages (the default batch size), if processed, would incur 10x write, 10x read, and 10x delete operations: one for each message in the batch.</li>
<li>There are no data transfer (egress) or throughput (bandwidth) charges.</li>
</ul>
<table>
<thead>
<tr>
<th></th>
<th>Workers Free</th>
<th>Workers Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td>Standard operations</td>
<td>10,000 operations/day included</td>
<td>1,000,000 operations/month included + $0.40/million operations</td>
</tr>
<tr>
<td>Message retention</td>
<td>24 hours (non-configurable)</td>
<td>4 days default, configurable up to 14 days</td>
</tr>
</tbody>
</table>
<p>In most cases, it takes 3 operations to deliver a message: 1 write, 1 read, and 1 delete. Therefore, you can use the following formula to estimate your monthly bill:</p>
<pre tabindex="0"><code class="language-txt">((Number of Messages * 3) - 1,000,000) / 1,000,000  * $0.40&#10;</code></pre>
<p>Additionally:</p>
<ul>
<li>Each retry incurs a read operation. A batch of 10 messages that is retried would incur 10 operations for each retry.</li>
<li>Messages that reach the maximum retries and that are written to a <a href="/queues/configuration/batching-retries/">Dead Letter Queue</a> incur a write operation for each 64 KB chunk. A message that was retried 3 times (the default), fails delivery on the fourth time and is written to a Dead Letter Queue would incur five (5) read operations.</li>
<li>Messages that are written to a queue, but that reach the maximum persistence duration (or &quot;expire&quot;) before they are read, incur only a write and delete operation per 64 KB chunk.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="queues-billing-examples">Queues billing examples</h3>
@markup("md", "content/.markup/bodies/16196.md")
</aside>
<h2 id="workflows">Workflows</h2>
<table>
<thead>
<tr>
<th>Unit</th>
<th>Workers Free</th>
<th>Workers Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td>Requests (millions)</td>
<td>100,000 per day (<a href="/workers/platform/pricing/#workers">shared with Workers requests</a>)</td>
<td>10 million included per month + $0.30 per additional million</td>
</tr>
<tr>
<td>CPU time (ms)</td>
<td>10 milliseconds of CPU time per invocation</td>
<td>30 million CPU milliseconds included per month + $0.02 per additional million CPU milliseconds</td>
</tr>
<tr>
<td>Storage (GB-mo)</td>
<td>1 GB-month</td>
<td>1 GB-month included + $0.20/ GB-month</td>
</tr>
<tr>
<td>Steps</td>
<td>3,000 per day</td>
<td>500,000 included per month + $0.80/ additional 100,000 per month</td>
</tr>
</tbody>
</table>
<p>Cloudflare will not bill step and storage usage before the start date announced in the <a href="/changelog/post/2026-07-07-workflows-billing-updates/">Workflows billing changelog</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="workflows-pricing">Workflows pricing</h3>
@markup("md", "content/.markup/bodies/16195.md")
</aside>
<h2 id="d1">D1</h2>
<p>D1 is available on both the Workers Free and Workers Paid plans.</p>
<table>
<thead>
<tr>
<th></th>
<th><a href="/workers/platform/pricing/#workers">Workers Free</a></th>
<th><a href="/workers/platform/pricing/#workers">Workers Paid</a></th>
</tr>
</thead>
<tbody>
<tr>
<td>Rows read</td>
<td>5 million / day</td>
<td>First 25 billion / month included + $0.001 / million rows</td>
</tr>
<tr>
<td>Rows written</td>
<td>100,000 / day</td>
<td>First 50 million / month included + $1.00 / million rows</td>
</tr>
<tr>
<td>Storage (per GB stored)</td>
<td>5 GB (total)</td>
<td>First 5 GB included + $0.75 / GB-mo</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="track-your-d1-usage">Track your D1 usage</h3>
@markup("md", "content/.markup/bodies/16194.md")
</aside>
<h3 id="definitions">Definitions</h3>
<ol>
<li>Rows read measure how many rows a query reads (scans), regardless of the size of each row. For example, if you have a table with 5000 rows and run a <code>SELECT * FROM table</code> as a full table scan, this would count as 5,000 rows read. A query that filters on an <a href="/d1/best-practices/use-indexes/">unindexed column</a> may return fewer rows to your Worker, but is still required to read (scan) more rows to determine which subset to return.</li>
<li>Rows written measure how many rows were written to D1 database. Write operations include <code>INSERT</code>, <code>UPDATE</code>, and <code>DELETE</code>. Each of these operations contribute towards rows written. A query that <code>INSERT</code> 10 rows into a <code>users</code> table would count as 10 rows written.</li>
<li>DDL operations (for example, <code>CREATE</code>, <code>ALTER</code>, and <code>DROP</code>) are used to define or modify the structure of a database. They may contribute to a mix of read rows and write rows. Ensure you are accurately tracking your usage through the available tools (<a href="/d1/worker-api/return-object/">meta object</a>, <a href="/d1/observability/metrics-analytics/#query-via-the-graphql-api">GraphQL Analytics API</a>, or the <a href="https://dash.cloudflare.com/?to=/:account/workers/d1/">Cloudflare dashboard</a>).</li>
<li>Row size or the number of columns in a row does not impact how rows are counted. A row that is 1 KB and a row that is 100 KB both count as one row.</li>
<li>Defining <a href="/d1/best-practices/use-indexes/">indexes</a> on your table(s) reduces the number of rows read by a query when filtering on that indexed field. For example, if the <code>users</code> table has an index on a timestamp column <code>created_at</code>, the query <code>SELECT * FROM users WHERE created_at &gt; ?1</code> would only need to read a subset of the table.</li>
<li>Indexes will add an additional written row when writes include the indexed column, as there are two rows written: one to the table itself, and one to the index. The performance benefit of an index and reduction in rows read will, in nearly all cases, offset this additional write.</li>
<li>Storage is based on gigabytes stored per month, and is based on the sum of all databases in your account. Tables and indexes both count towards storage consumed.</li>
<li>Free limits reset daily at 00:00 UTC. Monthly included limits reset based on your monthly subscription renewal date, which is determined by the day you first subscribed.</li>
<li>There are no data transfer (egress) or throughput (bandwidth) charges for data accessed from D1.</li>
<li><a href="/d1/best-practices/read-replication/">Read replication</a> does not charge extra for read replicas. You incur the same usage billing based on <code>rows_read</code> and <code>rows_written</code> by your queries.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="d1-billing">D1 billing</h3>
@markup("md", "content/.markup/bodies/16193.md")
</aside>
<h2 id="durable-objects">Durable Objects</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16192.md")
</aside>
<h3 id="compute-billing">Compute billing</h3>
<p>Durable Objects are billed for compute duration (wall-clock time) while the Durable Object is actively running or is idle in memory but unable to <a href="/durable-objects/concepts/durable-object-lifecycle/">hibernate</a>. Durable Objects that are idle and eligible for hibernation are not billed for duration, even before the runtime has hibernated them. Requests to a Durable Object keep it active or create the object if it was inactive.</p>
<p>For each metered dimension, billable usage is the amount consumed in excess of the included monthly allocation. This billable usage is rounded up to the next billable unit before the corresponding rate is applied. For example, 500,000 GB-s of billable compute duration is rounded up to 1,000,000 GB-s and billed accordingly.</p>
<table>
<thead>
<tr>
<th></th>
<th>Free plan</th>
<th>Paid plan</th>
</tr>
</thead>
<tbody>
<tr>
<td>Requests</td>
<td>100,000 / day</td>
<td>1 million / month, + $0.15/million<br/> Includes HTTP requests, RPC sessions<sup>1</sup>, WebSocket messages<sup>2</sup>, and alarm invocations</td>
</tr>
<tr>
<td>Duration<sup>3</sup></td>
<td>13,000 GB-s / day</td>
<td>400,000 GB-s / month, + $12.50/million GB-s<sup>4,5</sup></td>
</tr>
</tbody>
</table>
<details class="nb-details" open><summary>Footnotes</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/16205.md")
</div></details>
<h3 id="storage-billing">Storage billing</h3>
<p>The <a href="/durable-objects/api/sqlite-storage-api/">Durable Objects Storage API</a> is only accessible from within Durable Objects. Pricing depends on the storage backend of your Durable Objects.</p>
<ul>
<li><strong>SQLite-backed Durable Objects (recommended)</strong>: <a href="/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class">SQLite storage backend</a> is recommended for all new Durable Object classes. Workers Free plan can only create and access SQLite-backed Durable Objects.</li>
<li><strong>Key-value backed Durable Objects</strong>: <a href="/durable-objects/reference/durable-object-class-migrations-legacy/#create-durable-object-class-with-key-value-storage">Key-value storage backend</a> is only available on the Workers Paid plan.</li>
</ul>
<h4 id="sqlite-storage-backend">SQLite storage backend</h4>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="storage-billing-on-sqlite-backed-durable-objects">Storage billing on SQLite-backed Durable Objects</h3>
@markup("md", "content/.markup/bodies/16191.md")
</aside>
<table>
<thead>
<tr>
<th></th>
<th>Workers Free plan</th>
<th>Workers Paid plan</th>
</tr>
</thead>
<tbody>
<tr>
<td>Rows reads <sup>1,2</sup></td>
<td>5 million / day</td>
<td>First 25 billion / month included + $0.001 / million rows</td>
</tr>
<tr>
<td>Rows written <sup>1,2,3,4</sup></td>
<td>100,000 / day</td>
<td>First 50 million / month included + $1.00 / million rows</td>
</tr>
<tr>
<td>SQL Stored data <sup>5</sup></td>
<td>5 GB (total)</td>
<td>5 GB-month, + $0.20/ GB-month</td>
</tr>
</tbody>
</table>
<details class="nb-details" open><summary>Footnotes</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/16206.md")
</div></details>
<h4 id="key-value-storage-backend">Key-value storage backend</h4>
<table>
<thead>
<tr>
<th></th>
<th>Workers Paid plan</th>
</tr>
</thead>
<tbody>
<tr>
<td>Read request units<sup>1,2</sup></td>
<td>1 million, + $0.20/million</td>
</tr>
<tr>
<td>Write request units<sup>3</sup></td>
<td>1 million, + $1.00/million</td>
</tr>
<tr>
<td>Delete requests<sup>4</sup></td>
<td>1 million, + $1.00/million</td>
</tr>
<tr>
<td>Stored data<sup>5</sup></td>
<td>1 GB, + $0.20/ GB-month</td>
</tr>
</tbody>
</table>
<details class="nb-details" open><summary>Footnotes</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/16207.md")
</div></details>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="durable-objects-billing-examples">Durable Objects billing examples</h3>
@markup("md", "content/.markup/bodies/16190.md")
</aside>
<h2 id="vectorize">Vectorize</h2>
<p>Vectorize is currently only available on the Workers paid plan.</p>
<table>
<thead>
<tr>
<th></th>
<th><a href="/workers/platform/pricing/#workers">Workers Free</a></th>
<th><a href="/workers/platform/pricing/#workers">Workers Paid</a></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Total queried vector dimensions</strong></td>
<td>30 million queried vector dimensions / month</td>
<td>First 50 million queried vector dimensions / month included + $0.01 per million</td>
</tr>
<tr>
<td><strong>Total stored vector dimensions</strong></td>
<td>5 million stored vector dimensions</td>
<td>First 10 million stored vector dimensions + $0.05 per 100 million</td>
</tr>
</tbody>
</table>
<h3 id="calculating-vector-dimensions">Calculating vector dimensions</h3>
<p>To calculate your potential usage, calculate the queried vector dimensions and the stored vector dimensions, and multiply by the unit price. The formula is defined as <code>((queried vectors + stored vectors) * dimensions * ($0.01 / 1,000,000)) + (stored vectors * dimensions * ($0.05 / 100,000,000))</code></p>
<ul>
<li>For example, inserting 10,000 vectors of 768 dimensions each, and querying those 1,000 times per day (30,000 times per month) would be calculated as <code>((30,000 + 10,000) * 768) = 30,720,000</code> queried dimensions and <code>(10,000 * 768) = 7,680,000</code> stored dimensions (within the included monthly allocation)</li>
<li>Separately, and excluding the included monthly allocation, this would be calculated as <code>(30,000 + 10,000) * 768 * ($0.01 / 1,000,000) + (10,000 * 768 * ($0.05 / 100,000,000))</code> and sum to $0.31 per month.</li>
</ul>
<h2 id="r2">R2</h2>
<p>R2 charges based on the total volume of data stored, along with two classes of operations on that data:</p>
<ol>
<li><strong>Class A operations</strong> which are more expensive and tend to mutate state.</li>
<li><strong>Class B operations</strong> which tend to read existing state.</li>
</ol>
<p>There are no charges for egress bandwidth.</p>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Standard storage</th>
<th>Infrequent Access storage</th>
</tr>
</thead>
<tbody>
<tr>
<td>Storage</td>
<td>10 GB-month / month</td>
<td>$0.015 / GB-month</td>
<td>$0.01 / GB-month</td>
</tr>
<tr>
<td>Class A Operations</td>
<td>1 million requests / month</td>
<td>$4.50 / million requests</td>
<td>$9.00 / million requests</td>
</tr>
<tr>
<td>Class B Operations</td>
<td>10 million requests / month</td>
<td>$0.36 / million requests</td>
<td>$0.90 / million requests</td>
</tr>
<tr>
<td>Data Retrieval (processing)</td>
<td>None</td>
<td>None</td>
<td>$0.01 / GB</td>
</tr>
<tr>
<td>Egress (data transfer to Internet)</td>
<td>Free</td>
<td>Free</td>
<td>Free</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="r2-documentation">R2 documentation</h3>
@markup("md", "content/.markup/bodies/16189.md")
</aside>
<h2 id="containers">Containers</h2>
<p>Containers are billed for every 10ms that they are actively running at the following rates, with included monthly usage as part of the $5 USD per month <a href="/workers/platform/pricing/">Workers Paid plan</a>:</p>
<table>
<thead>
<tr>
<th></th>
<th>Memory</th>
<th>CPU</th>
<th>Disk</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Free</strong></td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr>
<td><strong>Workers Paid</strong></td>
<td>25 GiB-hours/month included <br/> +$0.0000025 per additional GiB-second</td>
<td>375 vCPU-minutes/month <br/>+ $0.000020 per additional vCPU-second</td>
<td>200 GB-hours/month <br/> +$0.00000007 per additional GB-second</td>
</tr>
</tbody>
</table>
<p>You only pay for what you use — charges start when a request is sent to the container or when it is manually started. Charges stop after the container instance goes to sleep, which can happen automatically after a timeout.</p>
<h3 id="network-egress">Network Egress</h3>
<p>Egress from Containers is priced at the following rates:</p>
<table>
<thead>
<tr>
<th>Region</th>
<th>Price per GB</th>
<th>Included Allotment per month</th>
</tr>
</thead>
<tbody>
<tr>
<td>North America &amp; Europe</td>
<td>$0.025</td>
<td>1 TB</td>
</tr>
<tr>
<td>Oceania, Korea, Taiwan</td>
<td>$0.05</td>
<td>500 GB</td>
</tr>
<tr>
<td>Everywhere Else</td>
<td>$0.04</td>
<td>500 GB</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="containers-documentation">Containers documentation</h3>
@markup("md", "content/.markup/bodies/16188.md")
</aside>
<h2 id="service-bindings">Service bindings</h2>
<p>Requests made from your Worker to another worker via a <a href="/workers/runtime-apis/bindings/service-bindings/">Service Binding</a> do not incur additional request fees. This allows you to split apart functionality into multiple Workers, without incurring additional costs.</p>
<p>For example, if Worker A makes a subrequest to Worker B via a Service Binding, or calls an RPC method provided by Worker B via a Service Binding, this is billed as:</p>
<ul>
<li>One request (for the initial invocation of Worker A)</li>
<li>The total amount of CPU time used across both Worker A and Worker B</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="only-available-on-workers-standard-pricing">Only available on Workers Standard pricing</h3>
@markup("md", "content/.markup/bodies/16187.md")
</aside>
<h2 id="fine-print">Fine Print</h2>
<p>Workers Paid plan is separate from any other Cloudflare plan (Free, Professional, Business) you may have. If you are an Enterprise customer, reach out to your account team to confirm pricing details.</p>
<p>Only requests that hit a Worker will count against your limits and your bill. Since Cloudflare Workers runs before the Cloudflare cache, the caching of a request still incurs costs. Refer to <a href="/workers/platform/limits/">Limits</a> to review definitions and behavior after a limit is hit.</p>
