<p>This guide shares considerations when migrating from the deprecated <code>httpRequests1mByColoGroups</code> and <code>httpRequests1dByColoGroups</code> GraphQL API nodes to the <code>httpRequestsAdaptiveGroups</code> GraphQL API node.</p>
<p>For example, if you wanted to see which five data centers had the most number of requests, the total number of those requests, and the total amount of data transfer, in the past you used the <code>httpRequests1mByColoGroups</code> GraphQL API node as in the following example:</p>
<pre><code class="language-graphql">{&#10;	viewer {&#10;		zones(filter: { zoneTag: $zoneTag }) {&#10;			series: httpRequests1mByColoGroups(&#10;				limit: 5&#10;				orderBy: [sum_requests_DESC]&#10;				filter: { datetime_geq: $start, datetime_lt: $end }&#10;			) {&#10;				sum {&#10;					requests&#10;					bytes&#10;				}&#10;				dimensions {&#10;					coloCode&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<details class="nb-details"><summary>Response</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3168.md")
</div></details>
<h2 id="httprequestsadaptivegroups-graphql-api-node"><code>httpRequestsAdaptiveGroups</code> GraphQL API node</h2>
<p>With the deprecation of the <code>httpRequests1mByColoGroups</code> and <code>httpRequests1dByColoGroups</code> GraphQL API nodes, use the <code>httpRequestsAdaptiveGroups</code> GraphQL API node to access the same data (<code>count</code>, <code>sum(edgeResponseBytes)</code>, and <code>visits</code>).</p>
<p><strong>Request</strong></p>
<pre><code class="language-graphql">query MigrationSample($zoneTag: string, $start: Time, $end: Time) {&#10;	viewer {&#10;		zones(filter: { zoneTag: $zoneTag }) {&#10;			series: httpRequestsAdaptiveGroups(&#10;				limit: 5&#10;				orderBy: [count_DESC]&#10;				filter: {&#10;					datetime_geq: $start&#10;					datetime_lt: $end&#10;					requestSource: &quot;eyeball&quot;&#10;				}&#10;			) {&#10;				count&#10;				avg {&#10;					sampleInterval&#10;				}&#10;				sum {&#10;					visits&#10;					edgeResponseBytes&#10;				}&#10;				dimensions {&#10;					coloCode&#10;				}&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<details class="nb-details"><summary>Response</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3169.md")
</div></details>
<p>This query says:</p>
<ul>
<li>Given the indicated <code>zones</code>, <code>limit</code>, and <code>time range</code>.</li>
<li>Fetch the total number of requests (as <code>count</code>), the total amount of data transfer (as <code>edgeResponseBytes</code> of <code>sum</code> object), and the total number of <code>visits</code> per data center.</li>
</ul>
<p>A few points to note:</p>
<ul>
<li>Adding the <code>requestSource</code> filter for <code>eyeball</code> returns request, data transfer, and visit data about only the end users of your website.</li>
<li>Instead of <code>requests</code>, the <code>httpRequestsAdaptiveGroups</code> node reports <code>count</code>, which indicates the number of requests per data center.</li>
<li>To measure data transfer, use <code>sum(edgeResponseBytes)</code>. Note that in the old API this was called <code>bandwidth</code> even though it actually measured data transfer.</li>
<li><code>unique visitors per colocation</code> is not supported in <code>httpRequestsAdaptiveGroups</code>, but the <code>httpRequestsAdaptiveGroups</code> API does support <code>visits</code>. A visit is defined as a page view that originated from a different website or direct link. Cloudflare checks where the HTTP referer does not match the hostname. One visit can consist of multiple page views.</li>
</ul>
