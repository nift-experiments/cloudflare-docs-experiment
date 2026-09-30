---
cp9:
  canonical: https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-magic-transit-endpoint-healthcheck-results/
  description: Query Magic Transit endpoint health checks.
  full_title: Querying Magic Transit endpoint health check results with GraphQL · Cloudflare Analytics docs
  head_html: <title>Querying Magic Transit endpoint health check results with GraphQL · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Query Magic Transit endpoint health checks."><link rel="canonical" href="https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-magic-transit-endpoint-healthcheck-results/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-magic-transit-endpoint-healthcheck-results/index.md"><meta property="og:title" content="Querying Magic Transit endpoint health check results with GraphQL · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Query Magic Transit endpoint health checks."><meta property="og:url" content="https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-magic-transit-endpoint-healthcheck-results/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Analytics,GraphQL Analytics API,Magic Transit"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-magic-transit-endpoint-healthcheck-results/#page","headline":"Querying Magic Transit endpoint health check results with GraphQL \u00b7 Cloudflare Analytics docs","description":"Query Magic Transit endpoint health checks.","url":"https://developers.cloudflare.com/analytics/graphql-api/tutorials/querying-magic-transit-endpoint-healthcheck-results/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/graphql-api/tutorials/querying-magic-transit-endpoint-healthcheck-results/
  schema: 1
---
<p>Use the <a href="/analytics/graphql-api/">GraphQL Analytics API</a> to query endpoint health check results for your account. The <code>magicEndpointHealthCheckAdaptiveGroups</code> dataset returns probe results aggregated by the dimensions and time interval you specify.</p>
<p>Send all GraphQL queries as HTTP <code>POST</code> requests to <code>https://api.cloudflare.com/client/v4/graphql</code>.</p>
<h3 id="prerequisites">Prerequisites</h3>
<p>You need the following to query endpoint health check data:</p>
<ul>
<li>Your <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a>.</li>
<li>An <a href="/fundamentals/api/get-started/create-token/">API token</a> with <code>Account &gt; Account Analytics &gt; Read</code> permissions. For details, refer to <a href="/analytics/graphql-api/getting-started/authentication/api-token-auth/">Configure an Analytics API token</a>.</li>
</ul>
<h3 id="query-parameters">Query parameters</h3>
<p>The following parameters are some of the most common ones in the <code>filter</code> object:</p>
<table>
<thead>
<tr>
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>date_geq</code></td>
<td align="left">Start date for the query in <code>YYYY-MM-DD</code> format (for example, <code>2026-01-01</code>). When used with a date-based truncation dimension, returns results from this date onward. You can also use a full ISO 8601 timestamp (for example, <code>2026-01-01T00:00:00Z</code>).</td>
</tr>
<tr>
<td align="left"><code>date_leq</code></td>
<td align="left"><em>(Optional)</em> End date for the query. Uses the same format as <code>date_geq</code>.</td>
</tr>
<tr>
<td align="left"><code>datetime_geq</code></td>
<td align="left"><em>(Optional)</em> Start timestamp in ISO 8601 format (for example, <code>2026-01-01T00:00:00Z</code>). Use instead of <code>date_geq</code> for time-based truncation dimensions.</td>
</tr>
<tr>
<td align="left"><code>datetime_leq</code></td>
<td align="left"><em>(Optional)</em> End timestamp in ISO 8601 format.</td>
</tr>
<tr>
<td align="left"><code>limit</code></td>
<td align="left">Maximum number of result groups to return.</td>
</tr>
</tbody>
</table>
<p>You can also filter on any dimension listed in the <a href="#available-dimensions">Available dimensions</a> table. Append an operator suffix to the dimension name to create a filter — for example, <code>endpoint_in</code> to filter by a list of endpoints, or <code>checkType_neq</code> to exclude a specific check type. Using a dimension name without a suffix filters for equality. For the full list of supported operators, refer to <a href="/analytics/graphql-api/features/filtering/">Filtering</a>.</p>
<h3 id="available-dimensions">Available dimensions</h3>
<p>You can query the following dimensions in the <code>dimensions</code> field:</p>
<table>
<thead>
<tr>
<th align="left">Dimension</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>checkId</code></td>
<td align="left">The unique ID of the configured health check.</td>
</tr>
<tr>
<td align="left"><code>checkType</code></td>
<td align="left">The type of health check (for example, <code>icmp</code>).</td>
</tr>
<tr>
<td align="left"><code>endpoint</code></td>
<td align="left">The IP address of the endpoint being checked.</td>
</tr>
<tr>
<td align="left"><code>name</code></td>
<td align="left">The name assigned to the health check when configured (may be empty if not set).</td>
</tr>
<tr>
<td align="left"><code>date</code></td>
<td align="left">Event timestamp truncated to the day.</td>
</tr>
<tr>
<td align="left"><code>datetime</code></td>
<td align="left">Full event timestamp.</td>
</tr>
<tr>
<td align="left"><code>datetimeMinute</code></td>
<td align="left">Event timestamp truncated to the minute.</td>
</tr>
<tr>
<td align="left"><code>datetimeFiveMinutes</code></td>
<td align="left">Event timestamp truncated to five-minute intervals.</td>
</tr>
<tr>
<td align="left"><code>datetimeFifteenMinutes</code></td>
<td align="left">Event timestamp truncated to 15-minute intervals.</td>
</tr>
<tr>
<td align="left"><code>datetimeHalfOfHour</code></td>
<td align="left">Event timestamp truncated to 30-minute intervals.</td>
</tr>
<tr>
<td align="left"><code>datetimeHour</code></td>
<td align="left">Event timestamp truncated to the hour.</td>
</tr>
</tbody>
</table>
<h3 id="available-metrics">Available metrics</h3>
<table>
<thead>
<tr>
<th align="left">Metric</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>count</code></td>
<td align="left">Total number of health check events in the group.</td>
</tr>
<tr>
<td align="left"><code>sum.total</code></td>
<td align="left">Total number of health check probes sent.</td>
</tr>
<tr>
<td align="left"><code>sum.failures</code></td>
<td align="left">Number of failed health check probes.</td>
</tr>
<tr>
<td align="left"><code>avg.lossPercentage</code></td>
<td align="left">Average calculated loss percentage (0-100).</td>
</tr>
</tbody>
</table>
<h3 id="api-call">API call</h3>
<p>The following example queries endpoint health check results for a specific account, returning probe counts aggregated in five-minute intervals. Replace <code>&lt;ACCOUNT_ID&gt;</code> with your <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a> and <code>&lt;API_TOKEN&gt;</code> with your <a href="/analytics/graphql-api/getting-started/authentication/api-token-auth/">API token</a>.</p>
<pre tabindex="0"><code class="language-bash">echo &#x27;{ &quot;query&quot;:&#10;  &quot;query GetEndpointHealthCheckResults($accountTag: string, $datetimeStart: string) {&#10;    viewer {&#10;      accounts(filter: {accountTag: $accountTag}) {&#10;        magicEndpointHealthCheckAdaptiveGroups(&#10;          filter: {&#10;            datetime_geq: $datetimeStart&#10;          }&#10;          limit: 10&#10;        ) {&#10;          count&#10;          dimensions {&#10;            checkId&#10;            checkType&#10;            endpoint&#10;            datetimeFiveMinutes&#10;          }&#10;          sum {&#10;            failures&#10;            total&#10;          }&#10;        }&#10;      }&#10;    }&#10;  }&quot;,&#10;  &quot;variables&quot;: {&#10;    &quot;accountTag&quot;: &quot;&lt;ACCOUNT_ID&gt;&quot;,&#10;    &quot;datetimeStart&quot;: &quot;2026-01-21T00:00:00Z&quot;&#10;  }&#10;}&#x27; | tr -d &#x27;\n&#x27; | curl --silent \&#10;https://api.cloudflare.com/client/v4/graphql \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Accept: application/json&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data @-&#10;</code></pre>
<p>Pipe the output to <code>jq</code> to format the JSON response for easier reading:</p>
<pre tabindex="0"><code class="language-bash">... | curl --silent \&#10;https://api.cloudflare.com/client/v4/graphql \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Accept: application/json&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data @- | jq .&#10;</code></pre>
<h3 id="example-response">Example response</h3>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;data&quot;: {&#10;    &quot;viewer&quot;: {&#10;      &quot;accounts&quot;: [&#10;        {&#10;          &quot;magicEndpointHealthCheckAdaptiveGroups&quot;: [&#10;            {&#10;              &quot;count&quot;: 288,&#10;              &quot;dimensions&quot;: {&#10;                &quot;checkId&quot;: &quot;90b478c7-bb51-4640-b94b-2c3050e9fa00&quot;,&#10;                &quot;checkType&quot;: &quot;icmp&quot;,&#10;                &quot;datetimeFiveMinutes&quot;: &quot;2026-01-21T12:00:00Z&quot;,&#10;                &quot;endpoint&quot;: &quot;103.21.244.100&quot;&#10;              },&#10;              &quot;sum&quot;: {&#10;                &quot;failures&quot;: 0,&#10;                &quot;total&quot;: 288&#10;              }&#10;            },&#10;            {&#10;              &quot;count&quot;: 288,&#10;              &quot;dimensions&quot;: {&#10;                &quot;checkId&quot;: &quot;90b478c7-bb51-4640-b94b-2c3050e9fa00&quot;,&#10;                &quot;checkType&quot;: &quot;icmp&quot;,&#10;                &quot;datetimeFiveMinutes&quot;: &quot;2026-01-21T12:05:00Z&quot;,&#10;                &quot;endpoint&quot;: &quot;103.21.244.100&quot;&#10;              },&#10;              &quot;sum&quot;: {&#10;                &quot;failures&quot;: 2,&#10;                &quot;total&quot;: 288&#10;              }&#10;            }&#10;          ]&#10;        }&#10;      ]&#10;    }&#10;  },&#10;  &quot;errors&quot;: null&#10;}&#10;</code></pre>
<p>In this response, <code>sum.total</code> is the number of probes sent during the interval and <code>sum.failures</code> is the number that did not receive a reply. A <code>failures</code> value of <code>0</code> indicates the endpoint was fully reachable during that period.</p>
