---
cp9:
  canonical: https://developers.cloudflare.com/pipelines/observability/metrics/
  description: Query Pipelines metrics for data ingested, processed, and delivered via the dashboard or GraphQL API.
  full_title: Metrics and analytics · Cloudflare Pipelines Docs
  head_html: <title>Metrics and analytics · Cloudflare Pipelines Docs</title><meta name="generator" content="Nift"><meta name="description" content="Query Pipelines metrics for data ingested, processed, and delivered via the dashboard or GraphQL API."><link rel="canonical" href="https://developers.cloudflare.com/pipelines/observability/metrics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pipelines/observability/metrics/index.md"><meta property="og:title" content="Metrics and analytics · Cloudflare Pipelines Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Query Pipelines metrics for data ingested, processed, and delivered via the dashboard or GraphQL API."><meta property="og:url" content="https://developers.cloudflare.com/pipelines/observability/metrics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pipelines"><meta name="algolia_product_filter" content="Pipelines"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Pipelines"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pipelines/observability/metrics/#page","headline":"Metrics and analytics \u00b7 Cloudflare Pipelines Docs","description":"Query Pipelines metrics for data ingested, processed, and delivered via the dashboard or GraphQL API.","url":"https://developers.cloudflare.com/pipelines/observability/metrics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pipelines/observability/metrics/
  schema: 1
---
<p>Pipelines expose metrics which allow you to measure data ingested, processed, and delivered to sinks.</p>
<p>The metrics displayed in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> are queried from Cloudflare's <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. You can access the metrics <a href="#query-via-the-graphql-api">programmatically</a> via GraphQL or HTTP client.</p>
<h2 id="metrics">Metrics</h2>
<h3 id="operator-metrics">Operator metrics</h3>
<p>Pipelines export the below metrics within the <code>pipelinesOperatorAdaptiveGroups</code> dataset. These metrics track data read and processed by pipeline operators.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>GraphQL Field Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Bytes In</td>
<td><code>bytesIn</code></td>
<td>Total number of bytes read by the pipeline (filter by <code>streamId_neq: &quot;&quot;</code> to get data read from streams)</td>
</tr>
<tr>
<td>Records In</td>
<td><code>recordsIn</code></td>
<td>Total number of records read by the pipeline (filter by <code>streamId_neq: &quot;&quot;</code> to get data read from streams)</td>
</tr>
<tr>
<td>Decode Errors</td>
<td><code>decodeErrors</code></td>
<td>Number of messages that could not be deserialized in the stream schema</td>
</tr>
</tbody>
</table>
<p>For a detailed breakdown of why events were dropped (including specific error types like <code>missing_field</code>, <code>type_mismatch</code>, <code>parse_failure</code>, and <code>null_value</code>), refer to <a href="#user-error-metrics">User error metrics</a>.</p>
<p>The <code>pipelinesOperatorAdaptiveGroups</code> dataset provides the following dimensions for filtering and grouping queries:</p>
<ul>
<li><code>pipelineId</code> - ID of the pipeline</li>
<li><code>streamId</code> - ID of the source stream</li>
<li><code>datetime</code> - Timestamp of the operation</li>
<li><code>date</code> - Timestamp of the operation, truncated to the start of a day</li>
<li><code>datetimeHour</code> - Timestamp of the operation, truncated to the start of an hour</li>
</ul>
<h3 id="sink-metrics">Sink metrics</h3>
<p>Pipelines export the below metrics within the <code>pipelinesSinkAdaptiveGroups</code> dataset. These metrics track data delivery to sinks.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>GraphQL Field Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Bytes Written</td>
<td><code>bytesWritten</code></td>
<td>Total number of bytes written to the sink, after compression</td>
</tr>
<tr>
<td>Records Written</td>
<td><code>recordsWritten</code></td>
<td>Total number of records written to the sink</td>
</tr>
<tr>
<td>Files Written</td>
<td><code>filesWritten</code></td>
<td>Number of files written to the sink</td>
</tr>
<tr>
<td>Row Groups Written</td>
<td><code>rowGroupsWritten</code></td>
<td>Number of row groups written (for Parquet files)</td>
</tr>
<tr>
<td>Uncompressed Bytes Written</td>
<td><code>uncompressedBytesWritten</code></td>
<td>Total number of bytes written before compression</td>
</tr>
</tbody>
</table>
<p>The <code>pipelinesSinkAdaptiveGroups</code> dataset provides the following dimensions for filtering and grouping queries:</p>
<ul>
<li><code>pipelineId</code> - ID of the pipeline</li>
<li><code>sinkId</code> - ID of the destination sink</li>
<li><code>datetime</code> - Timestamp of the operation</li>
<li><code>date</code> - Timestamp of the operation, truncated to the start of a day</li>
<li><code>datetimeHour</code> - Timestamp of the operation, truncated to the start of an hour</li>
</ul>
<h3 id="user-error-metrics">User error metrics</h3>
<p>Pipelines track events that are dropped during processing due to deserialization errors. When a structured stream receives events that do not match its defined schema, those events are accepted during ingestion but dropped during processing. The <code>pipelinesUserErrorsAdaptiveGroups</code> dataset provides visibility into these dropped events, telling you which events were dropped and why. You can explore the full schema of this dataset using GraphQL <a href="/analytics/graphql-api/features/discovery/introspection/">introspection</a>.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>GraphQL Field Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Count</td>
<td><code>count</code></td>
<td>Number of events that failed validation</td>
</tr>
</tbody>
</table>
<p>The <code>pipelinesUserErrorsAdaptiveGroups</code> dataset provides the following dimensions for filtering and grouping queries:</p>
<ul>
<li><code>pipelineId</code> - ID of the pipeline</li>
<li><code>errorFamily</code> - Category of the error (for example, <code>deserialization</code>)</li>
<li><code>errorType</code> - Specific error type within the family</li>
<li><code>date</code> - Date of the error, truncated to start of day</li>
<li><code>datetime</code> - Timestamp of the error</li>
<li><code>datetimeHour</code> - Timestamp of the error, truncated to the start of an hour</li>
<li><code>datetimeMinute</code> - Timestamp of the error, truncated to the start of a minute</li>
</ul>
<h4 id="known-error-types">Known error types</h4>
<table>
<thead>
<tr>
<th>Error family</th>
<th>Error type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>deserialization</code></td>
<td><code>missing_field</code></td>
<td>A required field defined in the stream schema was not present in the event</td>
</tr>
<tr>
<td><code>deserialization</code></td>
<td><code>type_mismatch</code></td>
<td>A field value did not match the expected type in the schema (for example, string sent where number expected)</td>
</tr>
<tr>
<td><code>deserialization</code></td>
<td><code>parse_failure</code></td>
<td>The event could not be parsed as valid JSON, or a field value could not be parsed into the expected type</td>
</tr>
<tr>
<td><code>deserialization</code></td>
<td><code>null_value</code></td>
<td>A required field was present but had a null value</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11112.md")
</aside>
<h2 id="view-metrics-and-errors-in-the-dashboard">View metrics and errors in the dashboard</h2>
<p>Per-pipeline analytics are available in the Cloudflare dashboard. To view current and historical metrics for a pipeline:</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> and select your account.</li>
<li>Go to <strong>Pipelines</strong> &gt; <strong>Pipelines</strong>.</li>
<li>Select a pipeline.</li>
<li>Go to the <strong>Metrics</strong> tab to view its metrics or <strong>Errors</strong> tab to view dropped events.</li>
</ol>
<p>You can optionally select a time window to query. This defaults to the last 24 hours.</p>
<h2 id="query-via-the-graphql-api">Query via the GraphQL API</h2>
<p>You can programmatically query analytics for your pipelines via the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. This API queries the same datasets as the Cloudflare dashboard and supports GraphQL <a href="/analytics/graphql-api/features/discovery/introspection/">introspection</a>.</p>
<p>Pipelines GraphQL datasets require an <code>accountTag</code> filter with your Cloudflare account ID.</p>
<h3 id="measure-operator-metrics-over-time-period">Measure operator metrics over time period</h3>
<p>This query returns the total bytes and records read by a pipeline from streams, along with any decode errors.</p>
<pre tabindex="0"><code class="language-graphql">query PipelineOperatorMetrics(&#10;	$accountTag: String!&#10;	$pipelineId: String!&#10;	$datetimeStart: Time!&#10;	$datetimeEnd: Time!&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			pipelinesOperatorAdaptiveGroups(&#10;				limit: 10000&#10;				filter: {&#10;					pipelineId: $pipelineId&#10;					streamId_neq: &quot;&quot;&#10;					datetime_geq: $datetimeStart&#10;					datetime_leq: $datetimeEnd&#10;				}&#10;			) {&#10;				sum {&#10;					bytesIn&#10;					recordsIn&#10;					decodeErrors&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="measure-sink-delivery-metrics">Measure sink delivery metrics</h3>
<p>This query returns detailed metrics about data written to a specific sink, including file and compression statistics.</p>
<pre tabindex="0"><code class="language-graphql">query PipelineSinkMetrics(&#10;	$accountTag: String!&#10;	$pipelineId: String!&#10;	$sinkId: String!&#10;	$datetimeStart: Time!&#10;	$datetimeEnd: Time!&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			pipelinesSinkAdaptiveGroups(&#10;				limit: 10000&#10;				filter: {&#10;					pipelineId: $pipelineId&#10;					sinkId: $sinkId&#10;					datetime_geq: $datetimeStart&#10;					datetime_leq: $datetimeEnd&#10;				}&#10;			) {&#10;				sum {&#10;					bytesWritten&#10;					recordsWritten&#10;					filesWritten&#10;					rowGroupsWritten&#10;					uncompressedBytesWritten&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="query-dropped-event-errors">Query dropped event errors</h3>
<p>This query returns a summary of events that were dropped due to schema validation failures, grouped by error type and ordered by frequency.</p>
<pre tabindex="0"><code class="language-graphql">query GetPipelineUserErrors(&#10;	$accountTag: String!&#10;	$pipelineId: String!&#10;	$datetimeStart: Time!&#10;	$datetimeEnd: Time!&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			pipelinesUserErrorsAdaptiveGroups(&#10;				limit: 100&#10;				filter: {&#10;					pipelineId: $pipelineId&#10;					datetime_geq: $datetimeStart&#10;					datetime_leq: $datetimeEnd&#10;				}&#10;				orderBy: [count_DESC]&#10;			) {&#10;				count&#10;				dimensions {&#10;					date&#10;					errorFamily&#10;					errorType&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>Example response:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;data&quot;: {&#10;		&quot;viewer&quot;: {&#10;			&quot;accounts&quot;: [&#10;				{&#10;					&quot;pipelinesUserErrorsAdaptiveGroups&quot;: [&#10;						{&#10;							&quot;count&quot;: 679,&#10;							&quot;dimensions&quot;: {&#10;								&quot;date&quot;: &quot;2026-02-19&quot;,&#10;								&quot;errorFamily&quot;: &quot;deserialization&quot;,&#10;								&quot;errorType&quot;: &quot;missing_field&quot;&#10;							}&#10;						},&#10;						{&#10;							&quot;count&quot;: 392,&#10;							&quot;dimensions&quot;: {&#10;								&quot;date&quot;: &quot;2026-02-19&quot;,&#10;								&quot;errorFamily&quot;: &quot;deserialization&quot;,&#10;								&quot;errorType&quot;: &quot;type_mismatch&quot;&#10;							}&#10;						},&#10;						{&#10;							&quot;count&quot;: 363,&#10;							&quot;dimensions&quot;: {&#10;								&quot;date&quot;: &quot;2026-02-19&quot;,&#10;								&quot;errorFamily&quot;: &quot;deserialization&quot;,&#10;								&quot;errorType&quot;: &quot;parse_failure&quot;&#10;							}&#10;						},&#10;						{&#10;							&quot;count&quot;: 44,&#10;							&quot;dimensions&quot;: {&#10;								&quot;date&quot;: &quot;2026-02-19&quot;,&#10;								&quot;errorFamily&quot;: &quot;deserialization&quot;,&#10;								&quot;errorType&quot;: &quot;null_value&quot;&#10;							}&#10;						}&#10;					]&#10;				}&#10;			]&#10;		}&#10;	},&#10;	&quot;errors&quot;: null&#10;}&#10;</code></pre>
<p>You can filter by a specific error type by adding <code>errorType</code> to the filter:</p>
<pre tabindex="0"><code class="language-graphql">pipelinesUserErrorsAdaptiveGroups(&#10;	limit: 100&#10;	filter: {&#10;		pipelineId: $pipelineId&#10;		datetime_geq: $datetimeStart&#10;		datetime_leq: $datetimeEnd&#10;		errorType: &quot;type_mismatch&quot;&#10;	}&#10;	orderBy: [count_DESC]&#10;)&#10;</code></pre>
<p>To query errors across all pipelines on an account, omit the <code>pipelineId</code> filter and include <code>pipelineId</code> in the dimensions:</p>
<pre tabindex="0"><code class="language-graphql">pipelinesUserErrorsAdaptiveGroups(&#10;	limit: 100&#10;	filter: {&#10;		datetime_geq: $datetimeStart&#10;		datetime_leq: $datetimeEnd&#10;	}&#10;	orderBy: [count_DESC]&#10;) {&#10;	count&#10;	dimensions {&#10;		pipelineId&#10;		errorFamily&#10;		errorType&#10;	}&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11111.md")
</aside>
