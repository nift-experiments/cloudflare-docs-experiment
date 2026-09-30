<p>Filters constrain queries to a particular account or set of zones, requests by date, or those from a specific user agent, for example. Without filters, queries can suffer performance degradation, results can exceed supported bounds, and the data returned can be noisy.</p>
<h2 id="filter-structure">Filter Structure</h2>
<p>The GraphQL filter is represented by the <a href="https://graphql.github.io/graphql-spec/June2018/#sec-Input-Objects">GraphQL Input Object</a>, which exposes Boolean algebra on nodes.</p>
<p>You can use filters as an argument on the following resources:</p>
<ul>
<li>zones</li>
<li>accounts</li>
<li>tables (datasets)</li>
</ul>
<h3 id="zone-filter">Zone filter</h3>
<p>Allows querying zone-related data by zone ID (<code>zoneTag</code>).</p>
<pre><code class="language-graphql">zones(filter: {zoneTag: &quot;your Zone ID&quot;}) {&#10;    ...&#10;}&#10;</code></pre>
<p>The zone filter must conform to the following grammar:</p>
<pre><code class="language-graphql">filter&#10;    { zoneTag: t }&#10;    { zoneTag_gt: t }&#10;    { zoneTag_in: [t, ...] }&#10;</code></pre>
<p>Compound filters (comma-separated, <code>AND</code>, <code>OR</code>) are not supported.</p>
<p>Use the <code>zoneTag: t</code> and <code>zoneTag_in: [t, ...]</code> forms when you know the zone IDs. Use the <code>zoneTag_gt: t</code> form with limits to traverse all zones if the zone IDs are not known. Zones always sort alphanumerically.</p>
<p>Omit the filter to get results for all zones (up to the supported limit).</p>
<h3 id="account-filter">Account filter</h3>
<p>The account filter uses the same structure and rules as the zone filter, except that it uses the Account ID (<code>accountTag</code>) instead of the Zone ID (<code>zoneTag</code>).</p>
<p>You must specify an account filter when making an account-scoped query, and you cannot query multiple accounts simultaneously.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3175.md")
</aside>
<h3 id="table-dataset-filter">Table (dataset) filter</h3>
<p>Table filters require that you query at least one node. Use the <code>AND</code> operator to create and combine multi-node filters. Table filters also support the <code>OR</code> operator, which you must specify explicitly.</p>
<p>The following grammar describes the table filter, where <code>k</code> is the GraphQL node on which to filter and <code>op</code> is one of the supported operators for that node:</p>
<pre><code class="language-graphql">filter&#10;  { kvs }&#10;kvs&#10;  kv&#10;  kv, kvs&#10;kv&#10;  k: v&#10;  k_op: v&#10;  AND: [filters]&#10;  OR: [filters]&#10;filters&#10;  filter&#10;  filter, filters&#10;</code></pre>
<h3 id="operators">Operators</h3>
<p>Operator support varies, depending on the node type and node name.</p>
<h4 id="array-operators">Array operators</h4>
<p>The following operators are supported for all array types:</p>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Comparison</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>has</code></td>
<td>array contains a value</td>
</tr>
<tr>
<td><code>hasall</code></td>
<td>array contains all of a list of values</td>
</tr>
<tr>
<td><code>hasany</code></td>
<td>array contains at least one of a list of values</td>
</tr>
</tbody>
</table>
<h4 id="scalar-operators">Scalar operators</h4>
<p>The following operators are supported for all scalar types:</p>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Comparison</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>gt</code></td>
<td>greater than</td>
</tr>
<tr>
<td><code>lt</code></td>
<td>less than</td>
</tr>
<tr>
<td><code>geq</code></td>
<td>greater or equal to</td>
</tr>
<tr>
<td><code>leq</code></td>
<td>less or equal to</td>
</tr>
<tr>
<td><code>neq</code></td>
<td>not equal</td>
</tr>
<tr>
<td><code>in</code></td>
<td>in</td>
</tr>
</tbody>
</table>
<h4 id="string-operators">String operators</h4>
<p>The <code>like</code> operator is available for string comparisons and supports the <code>%</code> character as a wildcard.</p>
<h2 id="examples">Examples</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3174.md")
</aside>
<h3 id="general-example">General example</h3>
<pre><code class="language-graphql">query GeneralExample($zoneTag: string, $start: Time) {&#10;	viewer {&#10;		zones(filter: { zoneTag: $zoneTag }) {&#10;			httpRequestsAdaptiveGroups(&#10;				filter: { datetime_gt: $start, clientCountryName: &quot;GB&quot; }&#10;				limit: 1&#10;			) {&#10;				count&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h3 id="filter-on-a-specific-node">Filter on a specific node</h3>
<p>The following GraphQL example shows how to filter a specific node. The SQL equivalent follows.</p>
<h4 id="graphql">GraphQL</h4>
<pre><code class="language-graphql">httpRequestsAdaptiveGroups(filter: {datetime: &quot;2018-01-01T10:00:00Z&quot;}) {&#10;    ...&#10;}&#10;</code></pre>
<h4 id="sql">SQL</h4>
<pre><code class="language-sql">WHERE datetime=&quot;2018-01-01T10:00:00Z&quot;&#10;</code></pre>
<h3 id="filter-on-multiple-fields">Filter on multiple fields</h3>
<p>The following GraphQL example shows how to apply a filter to multiple fields, in this case two datetime fields. The SQL equivalent follows.</p>
<h4 id="graphql-1">GraphQL</h4>
<pre><code class="language-graphql">httpRequests1hGroups(filter: {datetime_gt: &quot;2018-01-01T10:00:00Z&quot;, datetime_lt: &quot;2018-01-01T11:00:00Z&quot;}) {&#10;    ...&#10;}&#10;</code></pre>
<h4 id="sql-1">SQL</h4>
<pre><code class="language-sql">WHERE (datetime &gt; &quot;2018-01-01T10:00:00Z&quot;) AND (datetime &lt; &quot;2018-01-01T10:00:00Z&quot;)&#10;</code></pre>
<h3 id="filter-using-the-or-operator">Filter using the <code>OR</code> operator</h3>
<p>The following GraphQL example demonstrates using the <code>OR</code> operator in a filter. This <code>OR</code> operator filters for the value <code>US</code> or <code>GB</code> in the <code>clientCountryName</code> field.</p>
<h4 id="graphql-2">GraphQL</h4>
<pre><code class="language-graphql">httpRequestsAdaptiveGroups(&#10;        filter: {&#10;          datetime: &quot;2018-01-01T10:00:00Z&quot;,&#10;          OR:[{clientCountryName: &quot;US&quot;}, {clientCountryName: &quot;GB&quot;}]) {&#10;    ...&#10;}&#10;</code></pre>
<h4 id="sql-2">SQL</h4>
<pre><code class="language-sql">WHERE datetime=&quot;2018-01-01T10:00:00Z&quot;&#10;  AND ((clientCountryName = &quot;US&quot;) OR (clientCountryName = &quot;GB&quot;))&#10;</code></pre>
<h3 id="filter-an-array-by-one-value">Filter an array by one value</h3>
<p>The following GraphQL examples show how to filter an array field to only return data
that includes a specific value. The SQL equivalent follows.</p>
<h4 id="graphql-3">GraphQL</h4>
<pre><code class="language-graphql">mnmFlowDataAdaptiveGroups(filter: {ruleIDs_has: &quot;rule-id&quot;}) {&#10;    ...&#10;}&#10;</code></pre>
<h4 id="sql-3">SQL</h4>
<pre><code class="language-sql">WHERE has(ruleIDs, &#x27;rule-id&#x27;)&#10;</code></pre>
<h3 id="filter-an-array-by-multiple-values">Filter an array by multiple values</h3>
<p>The following GraphQL examples show how to filter an array field to only return data
that includes several values. The SQL equivalent follows.</p>
<h4 id="graphql-4">GraphQL</h4>
<pre><code class="language-graphql">mnmFlowDataAdaptiveGroups(filter: {ruleIDs_hasall: [&quot;rule-id-1&quot;, &quot;rule-id-2&quot;]}) {&#10;    ...&#10;}&#10;</code></pre>
<h4 id="sql-4">SQL</h4>
<pre><code class="language-sql">WHERE has(ruleIDs, &#x27;rule-id-1&#x27;) AND has(ruleIDs, &#x27;rule-id-2&#x27;)&#10;</code></pre>
<h3 id="filter-end-users">Filter end users</h3>
<p>Add the <code>requestSource</code> filter for <code>eyeball</code> to return request, data transfer, and visit data about only the end users of your website. This will exclude actions taken by Cloudflare products (for example, cache purge, healthchecks, Workers subrequests) on your zone.</p>
<h2 id="subqueries-advanced-filters">Subqueries (advanced filters)</h2>
<p>Subqueries are not currently supported. You can use two GraphQL queries as a workaround for this limitation.</p>
