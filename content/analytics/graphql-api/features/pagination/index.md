<p>Pagination – breaking up your query results into smaller parts – can be done using <code>limit</code>, <code>orderBy</code>, and filtering parameters. The GraphQL Analytics API does not support cursors for pagination.</p>
<ul>
<li><code>limit</code> (integer) defines how many records to return.</li>
<li><code>orderBy</code> (string) defines the sort order for the data.</li>
</ul>
<h2 id="query-pages-without-cursors">Query pages without cursors</h2>
<p>Our examples assume that the <code>date</code> and <code>clientCountryName</code> relationships are unique.</p>
<h3 id="get-the-first-n-results-of-a-query">Get the first <em>n</em> results of a query</h3>
<p>To limit results, add the <code>limit</code> parameter as an integer. For example, query the first two records:</p>
<pre><code class="language-javascript">&#10;firewallEventsAdaptive (limit: 2, orderBy: [datetime_ASC, clientCountryName_ASC]) {&#10;    datetime&#10;    clientCountryName&#10;}&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3173.md")
</aside>
<p><strong>Response</strong></p>
<pre><code class="language-javascript">&#10;{&#10;  &quot;firewallEventsAdaptive&quot; : [&#10;    {&#10;      &quot;datetime&quot;: &quot;2018-11-12T00:00:00Z&quot;,&#10;      &quot;clientCountryName&quot;: &quot;UM&quot;&#10;    },&#10;    {&#10;      &quot;datetime&quot;: &quot;2018-11-12T00:00:00Z&quot;,&#10;      &quot;clientCountryName&quot;: &quot;US&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<h3 id="query-for-the-next-page-using-filters">Query for the next page using filters</h3>
<p>To get the next <em>n</em> results, specify a filter to exclude the last result from the previous query. Taking the previous example, you can do this by appending the greater-than operator (<code>_gt</code>) to the <code>clientCountryName</code> field and the greater-or-equal operator (<code>_geq</code>) to the <code>datetime</code> field. This is where being specific about sort order comes into play. You are less likely to miss results using a more granular sort order.</p>
<pre><code class="language-javascript">&#10;firewallEventsAdaptive (limit: 2, orderBy: [datetime_ASC, clientCountryName_ASC], filter: {datetime_geq: &quot;2018-11-12T00:00:00Z&quot;, clientCountryName_gt: &quot;US&quot;}) {&#10;    datetime&#10;    clientCountryName&#10;}&#10;</code></pre>
<p><strong>Response</strong></p>
<pre><code class="language-javascript">&#10;{&#10;  &quot;firewallEventsAdaptive&quot; : [&#10;    {&#10;      &quot;datetime&quot;: &quot;2018-11-12T00:00:00Z&quot;,&#10;      &quot;clientCountryName&quot;: &quot;UY&quot;&#10;    },&#10;    {&#10;      &quot;datetime&quot;: &quot;2018-11-12T00:00:00Z&quot;,&#10;      &quot;clientCountryName&quot;: &quot;UZ&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
<h3 id="query-the-previous-page">Query the previous page</h3>
<p>To get the previous <em>n</em> results, reverse the filters and sort order.</p>
<pre><code class="language-javascript">&#10;firewallEventsAdaptive (limit: 2, orderBy: [datetime_DESC, clientCountryName_DESC, filter: {datetime_leq: &quot;2018-11-12T00:00:00Z&quot;, clientCountryName_lt: &quot;UY&quot;}]) {&#10;  datetime&#10;  clientCountryName&#10;}&#10;</code></pre>
<p><strong>Response</strong></p>
<pre><code class="language-javascript">&#10;{&#10;  &quot;firewallEventsAdaptive&quot; : [&#10;    {&#10;      &quot;datetime&quot;: &quot;2018-11-12T00:00:00Z&quot;,&#10;      &quot;clientCountryName&quot;: &quot;US&quot;&#10;    },&#10;    {&#10;      &quot;datetime&quot;: &quot;2018-11-12T00:00:00Z&quot;,&#10;      &quot;clientCountryName&quot;: &quot;UM&quot;&#10;    }&#10;  ]&#10;}&#10;</code></pre>
