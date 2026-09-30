<p>Cloudflare GraphQL API exposes more than 70 datasets to its customers. These
datasets represent different Cloudflare products with very different data
shapes; thus, each has its configuration of <a href="/analytics/graphql-api/limits/">limits</a>.</p>
<p>Although we allow access to ALL plans for the essential datasets (like
<code>httpRequestsAdaptiveGroups</code>, <code>firewallEventsAdaptive</code>, etc), users on larger
plans benefit from an extended set of datasets and wider query limits.</p>
<p>In addition to <a href="/analytics/graphql-api/features/discovery/introspection/">introspection</a>, users can use the Settings node that is
available for both zones and accounts scopes.</p>
<h2 id="format">Format</h2>
<p><code>Settings</code> node has all datasets from <code>zones</code> and <code>accounts</code> as fields.</p>
<pre><code class="language-graphql">{&#10;  viewer {&#10;    accounts(filter: { accountTag : $accountTag }) {&#10;      settings {&#10;        &#35; any dataset(s) from accounts&#10;      }&#10;    }&#10;    zones(filter: { zoneTag : $zoneTag }) {&#10;      settings {&#10;        &#35; any dataset(s) from zones&#10;      }&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>Every subnode of <code>settings</code> node could consist of these fields:</p>
<ul>
<li><code>enabled</code> - shows whether the node is available for a requester or not;</li>
<li><code>availableFields</code> - shows the list of fields available for a requester. If
it is a nested field, the path will be returned, like <code>sum_requests</code>;</li>
<li><code>maxPageSize</code> - retrieves the maximum number of records that can be returned</li>
<li><code>maxNumberOfFields</code> - answers on how many fields could be used in a single
query for that node;</li>
<li><code>notOlderThan</code> - returns a number of seconds on how far back in time a query
can read;</li>
<li><code>maxDuration</code> - shows how wide the requested time range could be.</li>
</ul>
<h2 id="a-sample-query">A sample query</h2>
<pre><code class="language-graphql">query SampleQuery($zoneTag: string) {&#10;	viewer {&#10;		zones(filter: { zoneTag: $zoneTag }) {&#10;			settings {&#10;				firewallEventsAdaptive {&#10;					enabled&#10;					maxDuration&#10;					maxNumberOfFields&#10;					maxPageSize&#10;					notOlderThan&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;data&quot;: {&#10;		&quot;viewer&quot;: {&#10;			&quot;zones&quot;: [&#10;				{&#10;					&quot;settings&quot;: {&#10;						&quot;firewallEventsAdaptive&quot;: {&#10;							&quot;enabled&quot;: true,&#10;							&quot;maxDuration&quot;: 259200,&#10;							&quot;maxNumberOfFields&quot;: 30,&#10;							&quot;maxPageSize&quot;: 10000,&#10;							&quot;notOlderThan&quot;: 2678400&#10;						}&#10;					}&#10;				}&#10;			]&#10;		}&#10;	},&#10;	&quot;errors&quot;: null&#10;}&#10;</code></pre>
<p>To get more details on how to execute queries, please refer to our how to get
started <a href="/analytics/graphql-api/getting-started/">guides</a>.</p>
