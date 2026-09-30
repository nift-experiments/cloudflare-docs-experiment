<p>You can specify the order of the query result elements using the <code>orderBy</code> argument. By default, the results are sorted by the primary key of a dataset (table). If you specify another field to sort on, the primary key is also used in the sorting key, allowing results to remain consistent for pagination.</p>
<p>The default order for an aggregated dataset is by the fields on which the aggregated data is grouped. If you specify a different order, the aggregation group is appended to your specified ordering.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/3172.md")
</aside>
<h2 id="examples">Examples</h2>
<h3 id="raw-data-sorting">Raw data sorting</h3>
<pre><code class="language-graphql">firewallEventsAdaptive (orderBy: [clientCountryName_ASC]) {&#10;    clientCountryName&#10;}&#10;</code></pre>
<h3 id="raw-data-sorting-using-multiple-fields">Raw data sorting using multiple fields</h3>
<pre><code class="language-graphql">firewallEventsAdaptive (orderBy: [clientCountryName_ASC, datetime_DESC]) {&#10;    clientCountryName&#10;    datetime&#10;}&#10;</code></pre>
<h3 id="group-sorting-by-aggregation-function">Group sorting by aggregation function</h3>
<pre><code class="language-graphql">httpRequests1hGroups (orderBy: [sum_bytes_DESC]){&#10;    sum {&#10;        bytes&#10;        requests&#10;    }&#10;    dimensions {&#10;        datetime&#10;    }&#10;}&#10;</code></pre>
