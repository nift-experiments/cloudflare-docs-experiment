---
cp9:
  canonical: https://developers.cloudflare.com/r2-data-catalog/observability/metrics/
  description: Query R2 Data Catalog metrics for Iceberg REST API operations and table maintenance jobs via the GraphQL Analytics API.
  full_title: Metrics and analytics · Cloudflare R2 Data Catalog docs
  head_html: <title>Metrics and analytics · Cloudflare R2 Data Catalog docs</title><meta name="generator" content="Nift"><meta name="description" content="Query R2 Data Catalog metrics for Iceberg REST API operations and table maintenance jobs via the GraphQL Analytics API."><link rel="canonical" href="https://developers.cloudflare.com/r2-data-catalog/observability/metrics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2-data-catalog/observability/metrics/index.md"><meta property="og:title" content="Metrics and analytics · Cloudflare R2 Data Catalog docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Query R2 Data Catalog metrics for Iceberg REST API operations and table maintenance jobs via the GraphQL Analytics API."><meta property="og:url" content="https://developers.cloudflare.com/r2-data-catalog/observability/metrics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2 Data Catalog"><meta name="algolia_product_filter" content="R2 Data Catalog"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="R2 Data Catalog"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2-data-catalog/observability/metrics/#page","headline":"Metrics and analytics \u00b7 Cloudflare R2 Data Catalog docs","description":"Query R2 Data Catalog metrics for Iceberg REST API operations and table maintenance jobs via the GraphQL Analytics API.","url":"https://developers.cloudflare.com/r2-data-catalog/observability/metrics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2-data-catalog/observability/metrics/
  schema: 1
---
<p>R2 Data Catalog exposes metrics that allow you to monitor Iceberg REST API requests and table maintenance jobs (compaction and snapshot expiration) across your warehouses.</p>
<p>The metrics displayed in the Cloudflare dashboard are queried from Cloudflare's <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. You can access the metrics <a href="#query-via-the-graphql-api">programmatically</a> via GraphQL or any HTTP client.</p>
<h2 id="dashboard-metrics">Dashboard metrics</h2>
<p>The <strong>Metrics</strong> tab on each catalog's detail page displays five charts that summarize catalog activity over a configurable time range:</p>
<table>
<thead>
<tr>
<th>Chart</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Bytes Compacted</strong></td>
<td>Total bytes written by compaction jobs</td>
</tr>
<tr>
<td><strong>Files Compacted</strong></td>
<td>Number of input files processed and output files created by compaction</td>
</tr>
<tr>
<td><strong>Catalog Requests</strong></td>
<td>Total Iceberg REST API requests (for example, <code>load-table</code>, <code>list-namespaces</code>, <code>commit-table</code>)</td>
</tr>
<tr>
<td><strong>Storage Size</strong></td>
<td>Current bucket storage size</td>
</tr>
<tr>
<td><strong>Snapshots Expired</strong></td>
<td>Number of snapshots removed by snapshot expiration jobs</td>
</tr>
</tbody>
</table>
<p>The overview page also shows <strong>Catalog Requests</strong> and <strong>Bucket Size</strong> columns in the catalogs table, giving you a quick summary across all your catalogs.</p>
<h2 id="graphql-datasets">GraphQL datasets</h2>
<h3 id="data-operations-metrics">Data operations metrics</h3>
<p>R2 Data Catalog exports the below metrics within the <code>r2CatalogDataOperationsAdaptiveGroups</code> dataset. These metrics track Iceberg REST API requests made to your catalog, such as loading tables, listing namespaces, and committing updates.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>GraphQL Field Name</th>
<th>Aggregation</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Request count</td>
<td><code>count</code></td>
<td>count</td>
<td>Total number of Iceberg REST API requests</td>
</tr>
<tr>
<td>Request body bytes</td>
<td><code>requestBodyBytes</code></td>
<td>sum</td>
<td>Total bytes sent in request bodies</td>
</tr>
<tr>
<td>Request duration</td>
<td><code>requestDurationMs</code></td>
<td>sum, avg, quantiles</td>
<td>Request duration in milliseconds</td>
</tr>
</tbody>
</table>
<p>The <code>r2CatalogDataOperationsAdaptiveGroups</code> dataset provides the following dimensions for filtering and grouping queries:</p>
<ul>
<li><code>warehouseName</code> - The name of the R2 Data Catalog warehouse</li>
<li><code>operation</code> - The Iceberg REST API operation name (for example, <code>load-table</code>, <code>list-namespaces</code>, <code>commit-table</code>)</li>
<li><code>namespaceName</code> - The Iceberg namespace targeted by the request, if applicable</li>
<li><code>tableName</code> - The Iceberg table targeted by the request, if applicable</li>
<li><code>httpStatus</code> - HTTP response status code</li>
<li><code>datetime</code> - Request timestamp</li>
<li><code>date</code> - Request timestamp, truncated to the start of a day</li>
<li><code>datetimeHour</code> - Request timestamp, truncated to the start of an hour</li>
<li><code>datetimeMinute</code> - Request timestamp, truncated to the start of a minute</li>
<li><code>datetimeFiveMinutes</code> - Request timestamp, truncated to the start of five minutes</li>
<li><code>datetimeFifteenMinutes</code> - Request timestamp, truncated to the start of fifteen minutes</li>
</ul>
<h3 id="table-maintenance-metrics">Table maintenance metrics</h3>
<p>R2 Data Catalog exports the below metrics within the <code>r2CatalogTableMaintenanceAdaptiveGroups</code> dataset. These metrics track table maintenance jobs including <a href="/r2-data-catalog/table-maintenance/">compaction and snapshot expiration</a>.</p>
<table>
<thead>
<tr>
<th>Metric</th>
<th>GraphQL Field Name</th>
<th>Aggregation</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Job count</td>
<td><code>count</code></td>
<td>count</td>
<td>Total number of maintenance jobs executed</td>
</tr>
<tr>
<td>Files processed</td>
<td><code>filesProcessed</code></td>
<td>sum</td>
<td>Total input files processed by maintenance jobs</td>
</tr>
<tr>
<td>Files output</td>
<td><code>filesOutput</code></td>
<td>sum</td>
<td>Total output files created by maintenance jobs</td>
</tr>
<tr>
<td>Input bytes</td>
<td><code>inputBytes</code></td>
<td>sum</td>
<td>Total bytes read or scanned by maintenance jobs</td>
</tr>
<tr>
<td>Output bytes</td>
<td><code>outputBytes</code></td>
<td>sum</td>
<td>Total bytes written by maintenance jobs</td>
</tr>
<tr>
<td>Job duration</td>
<td><code>jobDurationMs</code></td>
<td>sum, avg, quantiles</td>
<td>Job duration in milliseconds</td>
</tr>
</tbody>
</table>
<p>The <code>r2CatalogTableMaintenanceAdaptiveGroups</code> dataset provides the following dimensions for filtering and grouping queries:</p>
<ul>
<li><code>warehouseName</code> - The name of the R2 Data Catalog warehouse</li>
<li><code>jobType</code> - The type of maintenance job (<code>compaction</code>, <code>snapshot-expiration</code>)</li>
<li><code>namespaceName</code> - The Iceberg namespace containing the table</li>
<li><code>tableName</code> - The Iceberg table that was maintained</li>
<li><code>success</code> - Whether the job succeeded (<code>1</code>) or failed (<code>0</code>)</li>
<li><code>datetime</code> - Job timestamp</li>
<li><code>date</code> - Job timestamp, truncated to the start of a day</li>
<li><code>datetimeHour</code> - Job timestamp, truncated to the start of an hour</li>
<li><code>datetimeMinute</code> - Job timestamp, truncated to the start of a minute</li>
<li><code>datetimeFiveMinutes</code> - Job timestamp, truncated to the start of five minutes</li>
<li><code>datetimeFifteenMinutes</code> - Job timestamp, truncated to the start of fifteen minutes</li>
</ul>
<h2 id="query-via-the-graphql-api">Query via the GraphQL API</h2>
<p>You can programmatically query analytics for your R2 Data Catalog warehouses via the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. This API queries the same datasets as the Cloudflare dashboard and supports GraphQL <a href="/analytics/graphql-api/features/discovery/introspection/">introspection</a>.</p>
<p>R2 Data Catalog GraphQL datasets require an <code>accountTag</code> filter with your Cloudflare account ID.</p>
<h3 id="measure-data-operations-over-a-time-period">Measure data operations over a time period</h3>
<p>This query returns the total number of Iceberg REST API requests and total request duration, grouped by operation, for a specific warehouse.</p>
<pre tabindex="0"><code class="language-graphql">query CatalogDataOperations(&#10;	$accountTag: String!&#10;	$warehouseName: String!&#10;	$datetimeStart: Time!&#10;	$datetimeEnd: Time!&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			r2CatalogDataOperationsAdaptiveGroups(&#10;				limit: 10000&#10;				filter: {&#10;					warehouseName: $warehouseName&#10;					datetime_geq: $datetimeStart&#10;					datetime_leq: $datetimeEnd&#10;				}&#10;			) {&#10;				count&#10;				dimensions {&#10;					operation&#10;				}&#10;				sum {&#10;					requestBodyBytes&#10;					requestDurationMs&#10;				}&#10;				avg {&#10;					requestDurationMs&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="measure-request-latency-percentiles">Measure request latency percentiles</h3>
<p>This query returns request duration percentiles for a specific warehouse, which is useful for understanding latency distribution.</p>
<pre tabindex="0"><code class="language-graphql">query CatalogLatencyPercentiles(&#10;	$accountTag: String!&#10;	$warehouseName: String!&#10;	$datetimeStart: Time!&#10;	$datetimeEnd: Time!&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			r2CatalogDataOperationsAdaptiveGroups(&#10;				limit: 10000&#10;				filter: {&#10;					warehouseName: $warehouseName&#10;					datetime_geq: $datetimeStart&#10;					datetime_leq: $datetimeEnd&#10;				}&#10;			) {&#10;				count&#10;				dimensions {&#10;					operation&#10;				}&#10;				quantiles {&#10;					requestDurationMsP50&#10;					requestDurationMsP90&#10;					requestDurationMsP99&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="query-table-maintenance-job-metrics">Query table maintenance job metrics</h3>
<p>This query returns a summary of compaction and snapshot expiration jobs for a specific warehouse, including files processed, bytes read and written, and success or failure status.</p>
<pre tabindex="0"><code class="language-graphql">query CatalogMaintenanceMetrics(&#10;	$accountTag: String!&#10;	$warehouseName: String!&#10;	$datetimeStart: Time!&#10;	$datetimeEnd: Time!&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			r2CatalogTableMaintenanceAdaptiveGroups(&#10;				limit: 10000&#10;				filter: {&#10;					warehouseName: $warehouseName&#10;					datetime_geq: $datetimeStart&#10;					datetime_leq: $datetimeEnd&#10;				}&#10;			) {&#10;				count&#10;				dimensions {&#10;					jobType&#10;					tableName&#10;					success&#10;				}&#10;				sum {&#10;					filesProcessed&#10;					filesOutput&#10;					inputBytes&#10;					outputBytes&#10;					jobDurationMs&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="filter-by-operation-or-table">Filter by operation or table</h3>
<p>You can narrow results to a specific Iceberg operation or table. For example, to query only <code>load-table</code> operations for a specific table:</p>
<pre tabindex="0"><code class="language-graphql">query CatalogFilterByOperation(&#10;	$accountTag: String!&#10;	$datetimeStart: Time!&#10;	$datetimeEnd: Time!&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			r2CatalogDataOperationsAdaptiveGroups(&#10;				limit: 10000&#10;				filter: {&#10;					warehouseName: &quot;my-warehouse&quot;&#10;					operation: &quot;load-table&quot;&#10;					tableName: &quot;my_table&quot;&#10;					datetime_geq: $datetimeStart&#10;					datetime_leq: $datetimeEnd&#10;				}&#10;			) {&#10;				count&#10;				sum {&#10;					requestDurationMs&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>To query only failed maintenance jobs:</p>
<pre tabindex="0"><code class="language-graphql">query CatalogFailedMaintenanceJobs(&#10;	$accountTag: String!&#10;	$datetimeStart: Time!&#10;	$datetimeEnd: Time!&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			r2CatalogTableMaintenanceAdaptiveGroups(&#10;				limit: 10000&#10;				filter: {&#10;					warehouseName: &quot;my-warehouse&quot;&#10;					success: 0&#10;					datetime_geq: $datetimeStart&#10;					datetime_leq: $datetimeEnd&#10;				}&#10;			) {&#10;				count&#10;				dimensions {&#10;					jobType&#10;					tableName&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="query-across-all-warehouses">Query across all warehouses</h3>
<p>To query metrics across all warehouses on an account, omit the <code>warehouseName</code> filter and include <code>warehouseName</code> in the dimensions:</p>
<pre tabindex="0"><code class="language-graphql">query CatalogAllWarehouses(&#10;	$accountTag: String!&#10;	$datetimeStart: Time!&#10;	$datetimeEnd: Time!&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			r2CatalogDataOperationsAdaptiveGroups(&#10;				limit: 10000&#10;				filter: { datetime_geq: $datetimeStart, datetime_leq: $datetimeEnd }&#10;			) {&#10;				count&#10;				dimensions {&#10;					warehouseName&#10;					operation&#10;				}&#10;				sum {&#10;					requestDurationMs&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
