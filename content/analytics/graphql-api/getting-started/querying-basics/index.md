<h2 id="structure-of-a-graphql-query">Structure of a GraphQL query</h2>
<p>GraphQL structures data as a graph. GraphQL uses a schema to define the objects
and their hierarchy in your data graph. You can explore the edges of the graph
by using queries to get the needed data. These queries must respect the
structure of the schema.</p>
<p>A <strong>node</strong>, followed by its <strong>fields</strong>, is at the core of a GraphQL query. A
node is an object of a specific <strong>type</strong>; the type specifies the fields that
make up the object.</p>
<p>A field can be another node where the appropriate query would contain nested
elements. Some nodes look like functions that can take on arguments to limit the
scope of what they can act on. You can apply filters at each node.</p>
<h2 id="cloudflare-graphql-schema">Cloudflare GraphQL schema</h2>
<p>A typical query against the Cloudflare GraphQL schema is made up of four main
components:</p>
<ul>
<li><code>viewer</code> - is the root node,</li>
<li><code>zones</code> or <code>accounts</code> - indicate the scope of the query, that is the domain
area or account you want to query. The <code>viewer</code> can access one <code>zones</code> or
<code>accounts</code>, or both,</li>
<li><strong>data node</strong> or <strong>dataset</strong> - represent the data you want to query. <code>zones</code>
or <code>accounts</code> may contain one or more datasets. To find out more about
discovering nodes, please refer to <a href="/analytics/graphql-api/features/discovery/introspection/">introspection</a>,</li>
<li><strong>fieldset</strong> - a set of fields or nested fields of the <strong>dataset</strong>.</li>
</ul>
<p>The query to Cloudflare GraphQL API must be sent over HTTP POST request with
payload in JSON format that consists of these fields:</p>
<pre><code class="language-json">{&#10;	&quot;query&quot;: &quot;&quot;,&#10;	&quot;variables&quot;: {}&#10;}&#10;</code></pre>
<p>From the above structure, the <code>query</code> field must contain a GraphQL query
formatted as a <strong>single line</strong> string (meaning all newline symbols should be
stripped / escaped), when <code>variables</code> is an object that contains all values of
used placeholders in the query itself.</p>
<h2 id="a-single-dataset-example">A single dataset example</h2>
<p>In the following example, the GraphQL query fetches a <code>datetime</code>, <code>action</code>, and
client request HTTP host as <code>host</code> field of 2 WAF events from zone-scoped
<code>firewallEventsAdaptive</code> dataset.</p>
<pre><code class="language-graphql">query ASingleDatasetExample($zoneTag: string, $start: Time, $end: Time) {&#10;	viewer {&#10;		zones(filter: { zoneTag: $zoneTag }) {&#10;			firewallEventsAdaptive(&#10;				filter: { datetime_gt: $start, datetime_lt: $end }&#10;				limit: 2&#10;				orderBy: [datetime_DESC]&#10;			) {&#10;				action&#10;				datetime&#10;				host: clientRequestHTTPHost&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>In the query above, we have variable placeholders: $zoneTag, $start, and $end. We
provide values for those placeholders alongside the query by placing them into
<code>variables</code> field of the payload. Note that the examples below use the UTC timezone, indicated by the letter &quot;Z&quot;.</p>
<pre><code class="language-json">{&#10;	&quot;zoneTag&quot;: &quot;&lt;zone-tag&gt;&quot;,&#10;	&quot;start&quot;: &quot;2020-08-03T02:07:05Z&quot;,&#10;	&quot;end&quot;: &quot;2020-08-03T17:07:05Z&quot;&#10;}&#10;</code></pre>
<p>There are multiple ways to send your query to Cloudflare GraphQL API. You can
use you favourite GraphQL client or CLI to send a request via curl. We have a
<a href="/analytics/graphql-api/getting-started/compose-graphql-query/">how-to guide</a> about using GraphiQL client, also check a guide on how to
execute a query with a curl <a href="/analytics/graphql-api/getting-started/execute-graphql-query/">here</a>.</p>
<pre><code class="language-json">{&#10;	&quot;data&quot;: {&#10;		&quot;viewer&quot;: {&#10;			&quot;zones&quot;: [&#10;				{&#10;					&quot;firewallEventsAdaptive&quot;: [&#10;						{&#10;							&quot;action&quot;: &quot;log&quot;,&#10;							&quot;host&quot;: &quot;cloudflare.guru&quot;,&#10;							&quot;datetime&quot;: &quot;2020-08-03T17:07:03Z&quot;&#10;						},&#10;						{&#10;							&quot;action&quot;: &quot;log&quot;,&#10;							&quot;host&quot;: &quot;cloudflare.guru&quot;,&#10;							&quot;datetime&quot;: &quot;2020-08-03T17:07:01Z&quot;&#10;						}&#10;					]&#10;				}&#10;			]&#10;		}&#10;	},&#10;	&quot;errors&quot;: null&#10;}&#10;</code></pre>
<h2 id="query-multiple-datasets-in-a-single-graphql-api-request">Query multiple datasets in a single GraphQL API request</h2>
<p>As previously mentioned, a query might contain one or multiple nodes (datasets).
At the API level, the data extraction would be done simultaneously, but the
response would be delayed until all dataset queries got their results. If any
fails during the execution, the entire query will be terminated, and the error
will be returned.</p>
<pre><code class="language-graphql">query MultipleDatasetsExample(&#10;	$zoneTag: string&#10;	$start: Time&#10;	$end: Time&#10;	$ts: Date&#10;) {&#10;	viewer {&#10;		zones(filter: { zoneTag: $zoneTag }) {&#10;			last10Events: firewallEventsAdaptive(&#10;				filter: { datetime_gt: $start, datetime_lt: $end }&#10;				limit: 10&#10;				orderBy: [datetime_DESC]&#10;			) {&#10;				action&#10;				datetime&#10;				host: clientRequestHTTPHost&#10;			}&#10;			top3DeviceTypes: httpRequestsAdaptiveGroups(&#10;				filter: { date: $ts }&#10;				limit: 10&#10;				orderBy: [count_DESC]&#10;			) {&#10;				count&#10;				dimensions {&#10;					device: clientDeviceType&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;zoneTag&quot;: &quot;&lt;zone-tag&gt;&quot;,&#10;	&quot;start&quot;: &quot;2022-10-02T00:26:49Z&quot;,&#10;	&quot;end&quot;: &quot;2022-10-04T14:26:49Z&quot;,&#10;	&quot;ts&quot;: &quot;2022-10-04&quot;&#10;}&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;data&quot;: {&#10;		&quot;viewer&quot;: {&#10;			&quot;zones&quot;: [&#10;				{&#10;					&quot;last10Events&quot;: [&#10;						{&#10;							&quot;action&quot;: &quot;block&quot;,&#10;							&quot;country&quot;: &quot;TR&quot;,&#10;							&quot;datetime&quot;: &quot;2022-10-04T08:41:09Z&quot;&#10;						},&#10;						{&#10;							&quot;action&quot;: &quot;block&quot;,&#10;							&quot;country&quot;: &quot;TR&quot;,&#10;							&quot;datetime&quot;: &quot;2022-10-04T08:41:09Z&quot;&#10;						},&#10;						{&#10;							&quot;action&quot;: &quot;block&quot;,&#10;							&quot;country&quot;: &quot;RU&quot;,&#10;							&quot;datetime&quot;: &quot;2022-10-04T01:09:36Z&quot;&#10;						},&#10;						{&#10;							&quot;action&quot;: &quot;block&quot;,&#10;							&quot;country&quot;: &quot;US&quot;,&#10;							&quot;datetime&quot;: &quot;2022-10-03T14:26:49Z&quot;&#10;						},&#10;						{&#10;							&quot;action&quot;: &quot;block&quot;,&#10;							&quot;country&quot;: &quot;US&quot;,&#10;							&quot;datetime&quot;: &quot;2022-10-03T14:26:46Z&quot;&#10;						},&#10;						{&#10;							&quot;action&quot;: &quot;block&quot;,&#10;							&quot;country&quot;: &quot;CN&quot;,&#10;							&quot;datetime&quot;: &quot;2022-10-02T23:51:26Z&quot;&#10;						},&#10;						{&#10;							&quot;action&quot;: &quot;block&quot;,&#10;							&quot;country&quot;: &quot;TR&quot;,&#10;							&quot;datetime&quot;: &quot;2022-10-02T23:39:41Z&quot;&#10;						},&#10;						{&#10;							&quot;action&quot;: &quot;block&quot;,&#10;							&quot;country&quot;: &quot;TR&quot;,&#10;							&quot;datetime&quot;: &quot;2022-10-02T23:39:41Z&quot;&#10;						}&#10;					],&#10;					&quot;top3DeviceTypes&quot;: [&#10;						{&#10;							&quot;count&quot;: 4580,&#10;							&quot;dimensions&quot;: {&#10;								&quot;device&quot;: &quot;desktop&quot;&#10;							}&#10;						}&#10;					]&#10;				}&#10;			]&#10;		}&#10;	},&#10;	&quot;errors&quot;: null&#10;}&#10;</code></pre>
<h2 id="helpful-resources">Helpful Resources</h2>
<p>Here are some helpful articles about working with the Cloudflare Analytics API and GraphQL.</p>
<h3 id="cloudflare-specific">Cloudflare specific</h3>
<ul>
<li><a href="/fundamentals/account/find-account-and-zone-ids/">How to find your zoneTag using the API</a></li>
</ul>
<h3 id="general-info-on-the-graphql-framework">General info on the GraphQL framework</h3>
<ul>
<li><a href="https://www.howtographql.com/">How to use GraphQL (tutorials)</a></li>
<li><a href="https://graphql.org/learn/thinking-in-graphs/">Thinking in Graphs</a></li>
<li><a href="https://graphql.org/learn/schema/">What data can you can query in the GraphQL type system (schemas)</a></li>
<li><a href="https://medium.com/graphql-mastery/graphql-quick-tip-how-to-pass-variables-into-a-mutation-in-graphiql-23ecff4add57">How to pass variables in GraphiQL (Medium article with quick tips)</a></li>
</ul>
