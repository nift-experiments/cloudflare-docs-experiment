---
cp9:
  canonical: https://developers.cloudflare.com/kv/observability/metrics-analytics/
  description: Query Workers KV operations and storage metrics via the dashboard or the GraphQL Analytics API.
  full_title: Metrics and analytics · Cloudflare Workers KV docs
  head_html: <title>Metrics and analytics · Cloudflare Workers KV docs</title><meta name="generator" content="Nift"><meta name="description" content="Query Workers KV operations and storage metrics via the dashboard or the GraphQL Analytics API."><link rel="canonical" href="https://developers.cloudflare.com/kv/observability/metrics-analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/kv/observability/metrics-analytics/index.md"><meta property="og:title" content="Metrics and analytics · Cloudflare Workers KV docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Query Workers KV operations and storage metrics via the dashboard or the GraphQL Analytics API."><meta property="og:url" content="https://developers.cloudflare.com/kv/observability/metrics-analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="KV"><meta name="algolia_product_filter" content="KV"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="KV"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/kv/observability/metrics-analytics/#page","headline":"Metrics and analytics \u00b7 Cloudflare Workers KV docs","description":"Query Workers KV operations and storage metrics via the dashboard or the GraphQL Analytics API.","url":"https://developers.cloudflare.com/kv/observability/metrics-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /kv/observability/metrics-analytics/
  schema: 1
---
<p>KV exposes analytics that allow you to inspect requests and storage across all namespaces in your account.</p>
<p>The metrics displayed in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> charts are queried from Cloudflare’s <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. You can access the metrics <a href="#query-via-the-graphql-api">programmatically</a> via GraphQL or HTTP client.</p>
<h2 id="metrics">Metrics</h2>
<p>KV currently exposes the below metrics:</p>
<table>
<thead>
<tr>
<th>Dataset</th>
<th>GraphQL Dataset Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Operations</td>
<td><code>kvOperationsAdaptiveGroups</code></td>
<td>This dataset consists of the operations made to your KV namespaces.</td>
</tr>
<tr>
<td>Storage</td>
<td><code>kvStorageAdaptiveGroups</code></td>
<td>This dataset consists of the storage details of your KV namespaces.</td>
</tr>
</tbody>
</table>
<p>Metrics can be queried (and are retained) for the past 31 days.</p>
<h2 id="view-metrics-in-the-dashboard">View metrics in the dashboard</h2>
<p>Per-namespace analytics for KV are available in the Cloudflare dashboard. To view current and historical metrics for a database:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers KV</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
2. Select an existing namespace.
3. Select the **Metrics** tab.
<p>You can optionally select a time window to query. This defaults to the last 24 hours.</p>
<h2 id="query-via-the-graphql-api">Query via the GraphQL API</h2>
<p>You can programmatically query analytics for your KV namespaces via the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>. This API queries the same datasets as the Cloudflare dashboard, and supports GraphQL <a href="/analytics/graphql-api/features/discovery/introspection/">introspection</a>.</p>
<p>To get started using the <a href="/analytics/graphql-api/">GraphQL Analytics API</a>, follow the documentation to setup <a href="/analytics/graphql-api/getting-started/authentication/">Authentication for the GraphQL Analytics API</a>.</p>
<p>To use the GraphQL API to retrieve KV's datasets, you must provide the <code>accountTag</code> filter with your Cloudflare Account ID. The GraphQL datasets for KV include:</p>
<ul>
<li><code>kvOperationsAdaptiveGroups</code></li>
<li><code>kvStorageAdaptiveGroups</code></li>
</ul>
<h3 id="examples">Examples</h3>
<p>The following are common GraphQL queries that you can use to retrieve information about KV analytics. These queries make use of variables <code>$accountTag</code>, <code>$date_geq</code>, <code>$date_leq</code>, and <code>$namespaceId</code>, which should be set as GraphQL variables or replaced in line. These variables should look similar to these:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;accountTag&quot;: &quot;&lt;YOUR_ACCOUNT_ID&gt;&quot;,&#10;	&quot;namespaceId&quot;: &quot;&lt;YOUR_KV_NAMESPACE_ID&gt;&quot;,&#10;	&quot;date_geq&quot;: &quot;2024-07-15&quot;,&#10;	&quot;date_leq&quot;: &quot;2024-07-30&quot;&#10;}&#10;</code></pre>
<h4 id="operations">Operations</h4>
<p>To query the sum of read, write, delete, and list operations for a given <code>namespaceId</code> and for a given date range (<code>start</code> and <code>end</code>), grouped by <code>date</code> and <code>actionType</code>:</p>
<pre tabindex="0"><code class="language-graphql">query KvOperationsSample(&#10;	$accountTag: string!&#10;	$namespaceId: string&#10;	$start: Date&#10;	$end: Date&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			kvOperationsAdaptiveGroups(&#10;				filter: { namespaceId: $namespaceId, date_geq: $start, date_leq: $end }&#10;				limit: 10000&#10;				orderBy: [date_DESC]&#10;			) {&#10;				sum {&#10;					requests&#10;				}&#10;				dimensions {&#10;					date&#10;					actionType&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>To query the distribution of the latency for read operations for a given <code>namespaceId</code> within a given date range (<code>start</code>, <code>end</code>):</p>
<pre tabindex="0"><code class="language-graphql">query KvOperationsSample2(&#10;	$accountTag: string!&#10;	$namespaceId: string&#10;	$start: Date&#10;	$end: Date&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			kvOperationsAdaptiveGroups(&#10;				filter: {&#10;					namespaceId: $namespaceId&#10;					date_geq: $start&#10;					date_leq: $end&#10;					actionType: &quot;read&quot;&#10;				}&#10;				limit: 10000&#10;			) {&#10;				sum {&#10;					requests&#10;				}&#10;				dimensions {&#10;					actionType&#10;				}&#10;				quantiles {&#10;					latencyMsP25&#10;					latencyMsP50&#10;					latencyMsP75&#10;					latencyMsP90&#10;					latencyMsP99&#10;					latencyMsP999&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>To query your account-wide read, write, delete, and list operations across all KV namespaces:</p>
<pre tabindex="0"><code class="language-graphql">query KvOperationsAllSample($accountTag: string!, $start: Date, $end: Date) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			kvOperationsAdaptiveGroups(&#10;				filter: { date_geq: $start, date_leq: $end }&#10;				limit: 10000&#10;			) {&#10;				sum {&#10;					requests&#10;				}&#10;				dimensions {&#10;					actionType&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h4 id="storage">Storage</h4>
<p>To query the storage details (<code>keyCount</code> and <code>byteCount</code>) of a KV namespace for every day of a given date range:</p>
<pre tabindex="0"><code class="language-graphql">query Viewer(&#10;	$accountTag: string!&#10;	$namespaceId: string&#10;	$start: Date&#10;	$end: Date&#10;) {&#10;	viewer {&#10;		accounts(filter: { accountTag: $accountTag }) {&#10;			kvStorageAdaptiveGroups(&#10;				filter: { date_geq: $start, date_leq: $end, namespaceId: $namespaceId }&#10;				limit: 10000&#10;				orderBy: [date_DESC]&#10;			) {&#10;				max {&#10;					keyCount&#10;					byteCount&#10;				}&#10;				dimensions {&#10;					date&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
