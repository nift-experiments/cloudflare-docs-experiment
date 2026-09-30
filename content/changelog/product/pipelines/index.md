<h1 id="changelog">Changelog</h1>

<h2 id="billing-is-now-enabled-for-pipelines"><a href="/changelog/post/2026-08-03-pipelines-billing-enabled/">Billing is now enabled for Pipelines</a></h2>
<p><em>2026-08-03</em></p>
<p>Billing is now enabled for <a href="/pipelines/">Cloudflare Pipelines</a> on non-enterprise accounts. Pipelines usage beyond the included free tier will appear on your next invoice.</p>
<p>Pipelines charges based on two usage dimensions. Ingress into a Pipeline stream remains free regardless of volume:</p>
<ul>
<li><strong>SQL transforms</strong>: $0.04 / GB for stateless transforms (filter, reshape, unnest, cast, compute).</li>
<li><strong>Sinks (egress)</strong>: $0.03 / GB for JSON output, $0.06 / GB for Parquet or Iceberg output.</li>
</ul>
<p>Workers Paid plans include 50 GB / month for both SQL transforms and sinks. Standard <a href="/r2/pricing/">R2 storage and operations</a> charges apply for data written to R2 buckets, and <a href="/r2-data-catalog/platform/pricing/">R2 Data Catalog</a> charges apply when writing to Iceberg tables.</p>
<p>For example, a pipeline that ingests 500 GB of event data per month, uses a SQL transform to filter and reshape it, and writes 300 GB to an R2 Data Catalog Iceberg table would be billed as follows:</p>
<table>
<thead>
<tr>
<th>Dimension</th>
<th>Usage</th>
<th>Included</th>
<th>Billable</th>
<th>Cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>Streams</td>
<td>500 GB</td>
<td>Unlimited</td>
<td>0 GB</td>
<td>$0.00</td>
</tr>
<tr>
<td>SQL transforms</td>
<td>500 GB</td>
<td>50 GB</td>
<td>450 GB</td>
<td>$18.00</td>
</tr>
<tr>
<td>Sinks (Iceberg)</td>
<td>300 GB</td>
<td>50 GB</td>
<td>250 GB</td>
<td>$15.00</td>
</tr>
<tr>
<td><strong>Total</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$33.00</strong></td>
</tr>
</tbody>
</table>
<p>For full pricing details and billing examples, refer to <a href="/pipelines/platform/pricing/">Pipelines pricing</a>.</p>


<h2 id="pipeline-binding-configuration-field-renamed-to-stream"><a href="/changelog/post/2026-05-27-pipeline-binding-stream-field/">Pipeline binding configuration field renamed to stream</a></h2>
<p><em>2026-06-04</em></p>
<p>The <code>pipeline</code> field inside the <code>pipelines</code> binding configuration in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> has been renamed to <code>stream</code>. The old field is deprecated but still accepted.</p>
<p>Update your configuration to use <code>stream</code> to avoid the deprecation warning.</p>
<p><strong>Before (deprecated):</strong></p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17739.md")</div>
<p><strong>After:</strong></p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17740.md")</div>
<p>No other changes are required. The binding name, TypeScript types, and runtime API (<code>env.MY_PIPELINE.send(...)</code>) remain the same.</p>
<p>For more information on configuring pipeline bindings, refer to <a href="/pipelines/streams/writing-to-streams/#configure-pipeline-binding">Writing to streams</a>.</p>


<h2 id="pipelines-pricing-announced"><a href="/changelog/post/2026-05-11-pipelines-pricing-announced/">Pipelines pricing announced</a></h2>
<p><em>2026-05-28</em></p>
<p><a href="/pipelines/">Cloudflare Pipelines</a> is a streaming data platform that ingests events, transforms them with SQL, and writes to <a href="/r2/">R2</a> as JSON, Parquet, or <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables. Pipelines now has published pricing based on two usage dimensions: the volume of data processed by SQL transforms and the volume of data delivered to sinks. Ingress into a Pipeline stream is free.</p>
<p><strong>Billing is not yet enabled. We will provide at least 30 days notice before we start charging for Pipelines usage.</strong></p>
<p>Pipelines pricing model is designed to charge per GB based on what you use:</p>
<ul>
<li><strong>Streams (ingress)</strong>: Free, regardless of volume.</li>
<li><strong>SQL transforms</strong>: $0.04 / GB for stateless transforms (filter, reshape, unnest, cast, compute).</li>
<li><strong>Sinks</strong>: $0.03 / GB for JSON, $0.06 / GB for Parquet or Iceberg output.</li>
</ul>
<p>Workers Free plans include 1 GB / month for each dimension. Workers Paid plans include 50 GB / month.</p>
<p>For full pricing details and billing examples, refer to <a href="/pipelines/platform/pricing/">Pipelines pricing</a>.</p>


<h2 id="pipelines-and-r2-data-catalog-now-supported-in-terraform"><a href="/changelog/post/2026-04-27-terraform-support/">Pipelines and R2 Data Catalog now supported in Terraform</a></h2>
<p><em>2026-05-04</em></p>
<p><a href="/pipelines/">Cloudflare Pipelines</a> ingests streaming data via <a href="/workers/">Workers</a> or HTTP endpoints, transforms it with SQL, and writes it to <a href="/r2/">R2</a> as Apache Iceberg tables. <a href="/r2-data-catalog/">R2 Data Catalog</a> manages those Iceberg tables, compaction, and compatibility with query engines like <a href="/r2-sql/">R2 SQL</a>, <a href="/r2-data-catalog/config-examples/spark-scala/">Spark</a>, and <a href="/r2-data-catalog/config-examples/duckdb/">DuckDB</a>.</p>
<p>You can now create and manage both products using Terraform, supported in the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Cloudflare Terraform provider v5.19.0</a>.</p>
<p>This adds four new resources that let you define your entire data pipeline as infrastructure-as-code: a data catalog, a stream for ingestion, a sink that writes to R2 Data Catalog or R2, and a pipeline that connects them with SQL.</p>
<p>The new Terraform resources are:</p>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/r2_data_catalog"><code>cloudflare_r2_data_catalog</code></a> — enable the data catalog on an R2 bucket</li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/pipeline_stream"><code>cloudflare_pipeline_stream</code></a> — create a stream that receives events via HTTP or Worker bindings</li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/pipeline_sink"><code>cloudflare_pipeline_sink</code></a> — create a sink that writes to R2 Data Catalog or R2</li>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/pipeline"><code>cloudflare_pipeline</code></a> — create a pipeline with SQL connecting a stream to a sink</li>
</ul>
<p>Here is a minimal example that creates a stream, an R2 Data Catalog sink, and a pipeline:</p>
<pre><code class="language-hcl">resource &quot;cloudflare_pipeline_stream&quot; &quot;my_stream&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  name       = &quot;my_stream&quot;&#10;  format     = { type = &quot;json&quot; }&#10;  schema = {&#10;    fields = [{&#10;      name     = &quot;value&quot;&#10;      type     = &quot;json&quot;&#10;      required = true&#10;    }]&#10;  }&#10;  http           = { enabled = true, authentication = false, cors = {} }&#10;  worker_binding = { enabled = false }&#10;}&#10;&#10;resource &quot;cloudflare_pipeline_sink&quot; &quot;my_sink&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  name       = &quot;my_sink&quot;&#10;  type       = &quot;r2_data_catalog&quot;&#10;  format     = { type = &quot;parquet&quot; }&#10;  schema     = { fields = [] }&#10;  config = {&#10;    account_id = var.cloudflare_account_id&#10;    bucket     = &quot;my-pipeline-bucket&quot;&#10;    table_name = &quot;my_table&quot;&#10;    token      = var.catalog_token&#10;  }&#10;}&#10;&#10;resource &quot;cloudflare_pipeline&quot; &quot;my_pipeline&quot; {&#10;  account_id = var.cloudflare_account_id&#10;  name       = &quot;my_pipeline&quot;&#10;  sql        = &quot;INSERT INTO ${cloudflare_pipeline_sink.my_sink.name} SELECT * FROM ${cloudflare_pipeline_stream.my_stream.name}&quot;&#10;}&#10;</code></pre>
<p>For a full end-to-end example that includes R2 bucket creation, data catalog setup, and scoped API token provisioning, refer to the <a href="/pipelines/reference/terraform/">Pipelines Terraform documentation</a>.</p>


<h2 id="cloudflare-pipelines-as-a-logpush-destination"><a href="/changelog/post/2026-04-20-pipelines-logpush-destination/">Cloudflare Pipelines as a Logpush destination</a></h2>
<p><em>2026-04-20</em></p>
<p>Logpush has traditionally been great at delivering Cloudflare logs to a variety of destinations in JSON format. While JSON is flexible and easily readable, it can be inefficient to store and query at scale.</p>
<p>With this release, you can now send your logs directly to <a href="/pipelines/">Pipelines</a> to ingest, transform, and store your logs in <a href="/r2/">R2</a> as Parquet files or Apache Iceberg tables managed by <a href="/r2-data-catalog/">R2 Data Catalog</a>. This makes the data footprint more compact and more efficient at querying your logs instantly with <a href="/r2-sql/">R2 SQL</a> or any other query engine that supports Apache Iceberg or Parquet.</p>
<h4 id="2026-04-20-pipelines-logpush-destination-transform-logs-before-storage">Transform logs before storage</h4>
<p>Pipelines SQL runs on each log record in-flight, so you can reshape your data before it is written. For example, you can drop noisy fields, redact sensitive values, or derive new columns:</p>
<pre><code class="language-sql">INSERT INTO http_logs_sink&#10;SELECT&#10;  ClientIP,&#10;  EdgeResponseStatus,&#10;  to_timestamp_micros(EdgeStartTimestamp) AS event_time,&#10;  upper(ClientRequestMethod) AS method,&#10;  sha256(ClientIP) AS hashed_ip&#10;FROM http_logs_stream&#10;WHERE EdgeResponseStatus &gt;= 400;&#10;</code></pre>
<p>Pipelines SQL supports string functions, regex, hashing, JSON extraction, timestamp conversion, conditional expressions, and more. For the full list, refer to the <a href="/pipelines/sql-reference/">Pipelines SQL reference</a>.</p>
<h4 id="2026-04-20-pipelines-logpush-destination-get-started">Get started</h4>
<p>To configure Pipelines as a Logpush destination, refer to <a href="/logs/logpush/logpush-job/enable-destinations/pipelines/">Enable Cloudflare Pipelines</a>.</p>


<h2 id="dropped-event-metrics-typed-pipelines-bindings-and-improved-setup"><a href="/changelog/post/2026-02-24-typed-bindings-setup-improvements-error-metrics/">Dropped event metrics, typed Pipelines bindings, and improved setup</a></h2>
<p><em>2026-02-24</em></p>
<p><a href="/pipelines/">Cloudflare Pipelines</a> ingests streaming data via <a href="/workers/">Workers</a> or HTTP endpoints, transforms it with SQL, and writes it to <a href="/r2/">R2</a> as Apache Iceberg tables. Today we're shipping three improvements to help you understand why streaming events get dropped, catch data quality issues early, and set up Pipelines faster.</p>
<h4 id="2026-02-24-typed-bindings-setup-improvements-error-metrics-dropped-event-metrics">Dropped event metrics</h4>
<p>When <a href="/pipelines/streams/">stream</a> events don't match the expected schema, Pipelines accepts them during ingestion but drops them when attempting to deliver them to the <a href="/pipelines/sinks/">sink</a>. To help you identify the root cause of these issues, we are introducing a new dashboard and metrics that surface dropped events with detailed error messages.</p>
<p><img src="/assets/upstream/images/pipelines/pipelines-error-log-dash.png" alt="The Errors tab in the Cloudflare dashboard showing deserialization errors grouped by type with individual error details" /></p>
<p>Dropped events can also be queried programmatically via the new <code>pipelinesUserErrorsAdaptiveGroups</code> GraphQL dataset. The dataset breaks down failures by specific error type (<code>missing_field</code>, <code>type_mismatch</code>, <code>parse_failure</code>, or <code>null_value</code>) so you can trace issues back to the source.</p>
<pre><code class="language-graphql">query GetPipelineUserErrors(&#10;	$accountTag: String!&#10;	$pipelineId: String!&#10;	$datetimeStart: Time!&#10;	$datetimeEnd: Time!&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			pipelinesUserErrorsAdaptiveGroups(&#10;				limit: 100&#10;				filter: {&#10;					pipelineId: $pipelineId&#10;					datetime_geq: $datetimeStart&#10;					datetime_leq: $datetimeEnd&#10;				}&#10;				orderBy: [count_DESC]&#10;			) {&#10;				count&#10;				dimensions {&#10;					errorFamily&#10;					errorType&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>For the full list of dimensions, error types, and additional query examples, refer to <a href="/pipelines/observability/metrics/#user-error-metrics">User error metrics</a>.</p>
<h4 id="2026-02-24-typed-bindings-setup-improvements-error-metrics-typed-pipelines-bindings">Typed Pipelines bindings</h4>
<p>Sending data to a Pipeline from a Worker previously used a generic <code>Pipeline&lt;PipelineRecord&gt;</code> type, which meant schema mismatches (wrong field names, incorrect types) were only caught at runtime as dropped events.</p>
<p>Running <code>wrangler types</code> now generates schema-specific TypeScript types for your <a href="/pipelines/streams/writing-to-streams/#send-via-workers">Pipeline bindings</a>. TypeScript catches missing required fields and incorrect field types at compile time, before your code is deployed.</p>
<pre><code class="language-ts">declare namespace Cloudflare {&#10;	type EcommerceStreamRecord = {&#10;		user_id: string;&#10;		event_type: string;&#10;		product_id?: string;&#10;		amount?: number;&#10;	};&#10;	interface Env {&#10;		STREAM: import(&quot;cloudflare:pipelines&quot;).Pipeline&lt;Cloudflare.EcommerceStreamRecord&gt;;&#10;	}&#10;}&#10;</code></pre>
<p>For more information, refer to <a href="/pipelines/streams/writing-to-streams/#typed-pipeline-bindings">Typed Pipeline bindings</a>.</p>
<h4 id="2026-02-24-typed-bindings-setup-improvements-error-metrics-improved-pipelines-setup">Improved Pipelines setup</h4>
<p>Setting up a new Pipeline previously required multiple manual steps: creating an R2 bucket, enabling R2 Data Catalog, generating an API token, and configuring format, compression, and rolling policies individually.</p>
<p>The <code>wrangler pipelines setup</code> command now offers a <strong>Simple</strong> setup mode that applies recommended defaults and automatically creates the <a href="/r2/buckets/">R2 bucket</a> and enables <a href="/r2-data-catalog/">R2 Data Catalog</a> if they do not already exist. Validation errors during setup prompt you to retry inline rather than restarting the entire process.</p>
<p>For a full walkthrough, refer to the <a href="/pipelines/getting-started/">Getting started guide</a>.</p>


<h2 id="pipelines-now-supports-sql-transformations-and-apache-iceberg"><a href="/changelog/post/2025-09-25-pipelines-sql/">Pipelines now supports SQL transformations and Apache Iceberg</a></h2>
<p><em>2025-09-25T13:00:00</em></p>
<p>Today, we're launching the new <a href="/pipelines/">Cloudflare Pipelines</a>: a streaming data platform that ingests events, transforms them with <a href="/pipelines/sql-reference/select-statements/">SQL</a>, and writes to <a href="/r2/">R2</a> as <a href="https://iceberg.apache.org/">Apache Iceberg</a> tables or Parquet files.</p>
<p>Pipelines can receive events via <a href="/pipelines/streams/writing-to-streams/#send-via-http">HTTP endpoints</a> or <a href="/pipelines/streams/writing-to-streams/#send-via-workers">Worker bindings</a>, transform them with SQL, and deliver to R2 with exactly-once guarantees. This makes it easy to build analytics-ready warehouses for server logs, mobile application events, IoT telemetry, or clickstream data without managing streaming infrastructure.</p>
<p>For example, here's a pipeline that ingests clickstream events and filters out bot traffic while extracting domain information:</p>
<pre><code class="language-sql">INSERT into events_table&#10;SELECT&#10;  user_id,&#10;  lower(event) AS event_type,&#10;  to_timestamp_micros(ts_us) AS event_time,&#10;  regexp_match(url, &#x27;^https?://([^/]+)&#x27;)[1]  AS domain,&#10;  url,&#10;  referrer,&#10;  user_agent&#10;FROM events_json&#10;WHERE event = &#x27;page_view&#x27;&#10;  AND NOT regexp_like(user_agent, &#x27;(?i)bot|spider&#x27;);&#10;</code></pre>
<p>Get started by creating a pipeline in the dashboard or running a single command in <a href="/workers/wrangler/">Wrangler</a>:</p>
<pre><code class="language-bash">npx wrangler pipelines setup&#10;</code></pre>
<p>Check out our <a href="/pipelines/getting-started/">getting started guide</a> to learn how to create a pipeline that delivers events to an <a href="/r2-data-catalog/">Iceberg table</a> you can query with R2 SQL. Read more about today's announcement in our <a href="https://blog.cloudflare.com/cloudflare-data-platform">blog post</a>.</p>


<h2 id="cloudflare-pipelines-now-available-in-beta"><a href="/changelog/post/2025-04-10-launching-pipelines/">Cloudflare Pipelines now available in beta</a></h2>
<p><em>2025-04-10</em></p>
<p><a href="/pipelines">Cloudflare Pipelines</a> is now available in beta, to all users with a <a href="/workers/platform/pricing">Workers Paid</a> plan.</p>
<p>Pipelines let you ingest high volumes of real time data, without managing the underlying infrastructure. A single pipeline can ingest up to 100 MB of data per second, via HTTP or from a <a href="/workers">Worker</a>. Ingested data is automatically batched, written to output files, and delivered to an <a href="/r2">R2 bucket</a> in your account. You can use Pipelines to build a data lake of clickstream data, or to store events from a Worker.</p>
<p>Create your first pipeline with a single command:</p>
<pre><code class="language-bash">$ npx wrangler@latest pipelines create my-clickstream-pipeline --r2-bucket my-bucket&#10;&#10;🌀 Authorizing R2 bucket &quot;my-bucket&quot;&#10;🌀 Creating pipeline named &quot;my-clickstream-pipeline&quot;&#10;✅ Successfully created pipeline my-clickstream-pipeline&#10;&#10;Id:    0e00c5ff09b34d018152af98d06f5a1xvc&#10;Name:  my-clickstream-pipeline&#10;Sources:&#10;  HTTP:&#10;    Endpoint:        https://0e00c5ff09b34d018152af98d06f5a1xvc.pipelines.cloudflare.com/&#10;    Authentication:  off&#10;    Format:          JSON&#10;  Worker:&#10;    Format:  JSON&#10;Destination:&#10;  Type:         R2&#10;  Bucket:       my-bucket&#10;  Format:       newline-delimited JSON&#10;  Compression:  GZIP&#10;Batch hints:&#10;  Max bytes:     100 MB&#10;  Max duration:  300 seconds&#10;  Max records:   100,000&#10;&#10;🎉 You can now send data to your pipeline!&#10;&#10;Send data to your pipeline&#x27;s HTTP endpoint:&#10;curl &quot;https://0e00c5ff09b34d018152af98d06f5a1xvc.pipelines.cloudflare.com/&quot; -d &#x27;[{ ...JSON_DATA... }]&#x27;&#10;&#10;To send data to your pipeline from a Worker, add the following configuration to your config file:&#10;{&#10;  &quot;pipelines&quot;: [&#10;    {&#10;      &quot;pipeline&quot;: &quot;my-clickstream-pipeline&quot;,&#10;      &quot;binding&quot;: &quot;PIPELINE&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<p>Head over to our <a href="/pipelines/getting-started">getting started guide</a> for an in-depth tutorial to building with Pipelines.</p>



