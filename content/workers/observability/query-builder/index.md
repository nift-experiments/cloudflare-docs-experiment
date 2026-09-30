<p>The Query Builder helps you write structured queries to investigate and visualize your telemetry data. The Query Builder searches the Workers Observability dataset, which currently includes all logs stored by <a href="/workers/observability/logs/workers-logs/">Workers Logs</a>.</p>
<p>You can also run the same queries programmatically using the <a href="/api/resources/workers/subresources/observability/">Workers Observability REST API</a>, which exposes endpoints to list dataset keys, run a query, and list the values for a key.</p>
<p>The Query Builder can be found in the <strong>Observability</strong> page of the Cloudflare dashboard:</p>
<div class="nb-dash-button"></div>
<div class="video-frame"><iframe src="https://www.youtube-nocookie.com/embed/nu4pTU8fR78" title="YouTube video" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<h2 id="enable-query-builder">Enable Query Builder</h2>
<p>The Query Builder is available to all developers and requires no enablement. Queries search all Workers Logs stored by Cloudflare. If you have not yet enabled Workers Logs, you can do so by adding the following setting to your <a href="/workers/observability/logs/workers-logs/#enable-workers-logs">Worker's Wrangler file</a> and redeploying your Worker.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16248.md")
</div>
<h2 id="write-a-query-in-the-cloudflare-dashboard">Write a query in the Cloudflare dashboard</h2>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select your Worker.</li>
<li>Select <strong>Observability</strong> in the left-hand navigation panel, and then the <strong>Overview</strong> tab.</li>
<li>Select a <strong>Visualization</strong>.</li>
<li>Optional: Add fields to Filter, Group By, Order By, and Limit. For more information, see what <a href="/workers/observability/query-builder/#query-composition">composes a query</a>.</li>
<li>Optional: Select the appropriate time range.</li>
<li>Select <strong>Run</strong>. The query will automatically run whenever changes are made.</li>
</ol>
<h2 id="query-composition">Query composition</h2>
<h3 id="visualization">Visualization</h3>
<p>The Query Builder supports many visualization operators, including:</p>
<table>
<thead>
<tr>
<th>Function</th>
<th>Arguments</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Count</strong></td>
<td>n/a</td>
<td>The total number of rows matching the query conditions</td>
</tr>
<tr>
<td><strong>Count Distinct</strong></td>
<td>any field</td>
<td>The number of occurrences of the unique values in the dataset</td>
</tr>
<tr>
<td><strong>Min</strong></td>
<td>numeric field</td>
<td>The smallest value for the field in the dataset</td>
</tr>
<tr>
<td><strong>Max</strong></td>
<td>numeric field</td>
<td>The largest value for the field in the dataset</td>
</tr>
<tr>
<td><strong>Sum</strong></td>
<td>numeric field</td>
<td>The total of all of the values for the field in the dataset</td>
</tr>
<tr>
<td><strong>Average</strong></td>
<td>numeric field</td>
<td>The average of the field in the dataset</td>
</tr>
<tr>
<td><strong>Standard Deviation</strong></td>
<td>numeric field</td>
<td>The standard deviation of the field in the dataset</td>
</tr>
<tr>
<td><strong>Variance</strong></td>
<td>numeric field</td>
<td>The variance of the field in the dataset</td>
</tr>
<tr>
<td><strong>P001</strong></td>
<td>numeric field</td>
<td>The value of the field below which 0.1% of the data falls</td>
</tr>
<tr>
<td><strong>P01</strong></td>
<td>numeric field</td>
<td>The value of the field below with 1% of the data falls</td>
</tr>
<tr>
<td><strong>P05</strong></td>
<td>numeric field</td>
<td>The value of the field below with 5% of the data falls</td>
</tr>
<tr>
<td><strong>P10</strong></td>
<td>numeric field</td>
<td>The value of the field below with 10% of the data falls</td>
</tr>
<tr>
<td><strong>P25</strong></td>
<td>numeric field</td>
<td>The value of the field below with 25% of the data falls</td>
</tr>
<tr>
<td><strong>Median (P50)</strong></td>
<td>numeric field</td>
<td>The value of the field below with 50% of the data falls</td>
</tr>
<tr>
<td><strong>P75</strong></td>
<td>numeric field</td>
<td>The value of the field below with 75% of the data falls</td>
</tr>
<tr>
<td><strong>P90</strong></td>
<td>numeric field</td>
<td>The value of the field below with 90% of the data falls</td>
</tr>
<tr>
<td><strong>P95</strong></td>
<td>numeric field</td>
<td>The value of the field below with 95% of the data falls</td>
</tr>
<tr>
<td><strong>P99</strong></td>
<td>numeric field</td>
<td>The value of the field below with 99% of the data falls</td>
</tr>
<tr>
<td><strong>P999</strong></td>
<td>numeric field</td>
<td>The value of the field below with 99.9% of the data falls</td>
</tr>
</tbody>
</table>
<p>You can add multiple visualizations in a single query. Each visualization renders a graph. A single summary table is also returned, which shows the raw query results.</p>
<p><img src="/assets/upstream/images/workers-observability/wobs_QB_visualization_122.png" alt="Example of showing the Query Builder with multiple visualization" /></p>
<p>All methods are aggregate functions. Most methods operate on a specific field in the log event. <code>Count</code> is an exception, and is an aggregate function that returns the number of log events matching the filter conditions.</p>
<h3 id="filter">Filter</h3>
<p>Filters help return the columns that match the specified conditions. Filters have three components: a key, an operator, and a value.</p>
<p>The key is any field in a log event. For example, you may choose <code>$workers.cpuTimeMs</code> or <code>$metadata.message</code>.</p>
<p>The operator is a logical condition that evaluates to true or false. See the table below for supported conditions:</p>
<table>
<thead>
<tr>
<th>Data Type</th>
<th>Valid Conditions (Operators)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Numeric</td>
<td>Equals, Does not equal, Greater, Greater or equals, Less, Less or equals, Exists, Does not exist</td>
</tr>
<tr>
<td>String</td>
<td>Equals, Does not equal, Includes, Does not include, Regex, Exists, Does not exist, Starts with</td>
</tr>
</tbody>
</table>
<p>The value for a numeric field is an integer. The value for a string field is any string.</p>
<p>To add a filter:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16249.md")
</div>
<p>When you run the query with the filter specified above, only log events where <code>$workers.cpuTimeMs &gt; 100</code> will be returned.</p>
<p>Adding multiple filters combines them with an AND operator, meaning that only events matching all the filters will be returned.</p>
<h3 id="search">Search</h3>
<p>Search is a text filter that returns only events containing the specified text. Search can be helpful as a quick filtering mechanism, or to search for unique identifiable values in your logs.</p>
<h3 id="group-by">Group By</h3>
<p>Group By combines rows that have the same value into summary rows. For example, if a query adds <code>$workers.event.request.cf.country</code> as a Group By field, then the summary table will group by country.</p>
<h3 id="order-by">Order By</h3>
<p>Order By affects how the results are sorted in the summary table. If <code>asc</code> is selected, the results are sorted in ascending order - from least to greatest. If <code>desc</code> is selected, the results are sorted in descending order - from greatest to least.</p>
<h3 id="limit">Limit</h3>
<p>Limit restricts the number of results returned. When paired with <a href="/workers/observability/query-builder/#order-by">Order By</a>, it can be used to return the &quot;top&quot; or &quot;first&quot; N results.</p>
<h3 id="select-time-range">Select time range</h3>
<p>When you select a time range, you specify the time interval where you want to look for matching events. The retention period is dependent on your <a href="/workers/observability/logs/workers-logs/#pricing">plan type</a>.</p>
<h2 id="viewing-query-results">Viewing query results</h2>
<p>There are three views for queries: Visualizations, Invocations, and Events.</p>
<h3 id="visualizations-tab">Visualizations tab</h3>
<p>The <strong>Visualizations</strong> tab shows graphs and a summary table for the query.</p>
<p><img src="/assets/upstream/images/workers-observability/wobs_visualizations_tab_122.png" alt="Visualization Overview" /></p>
<h3 id="invocations-tab">Invocations tab</h3>
<p>The <strong>Invocations</strong> tab shows all logs, grouped by the invocation, and ordered by timestamp. Only invocations matching the query criteria are returned.</p>
<p><img src="/assets/upstream/images/workers-observability/wobs_invocation_logs_full_list_122.png" alt="Invocations Overview" /></p>
<h3 id="events-tab">Events tab</h3>
<p>The <strong>Events</strong> tab shows all logs, ordered by timestamp. Only events matching the query criteria are returned. The Events tab can be customized to add additional fields in the view.</p>
<p><img src="/assets/upstream/images/workers-observability/wobs_events_dropdown_122.png" alt="Overview" /></p>
<h2 id="save-queries">Save queries</h2>
<p>It is recommended to save queries that may be reused for future investigations. You can save a query with a name, description, and custom tags by selecting <strong>Save Query</strong>. Queries are saved at the account-level and are accessible to all users in the account.</p>
<p>Saved queries can be re-run by selecting the relevant query from the <strong>Queries</strong> tab. You can edit the query and save edits.</p>
<p>Queries can be starred by users. Starred queries are unique to the user, and not to the account.</p>
<h2 id="delete-queries">Delete queries</h2>
<p>Saved queries can be deleted from the <strong>Queries</strong> tab. If you delete a query, the query is deleted for all users in the account.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Observability</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Queries</strong> tab.</li>
<li>On the right-hand side, select the three dots for additional actions.</li>
<li>Select <strong>Delete Query</strong> and follow the instructions.</li>
</ol>
<h2 id="share-queries">Share queries</h2>
<p>Saved queries are assigned a unique URL and can be shared with any user in the account.</p>
<h2 id="example-composing-a-query">Example: Composing a query</h2>
<p>In this example, we will construct a query to find and debug all paths that respond with 5xx errors. First, we create a base query. In this base query, we want to visualize by
the raw event count. We can add a filter for <code>$workers.event.response.status</code> that is greater than 500.
Then, we group by <code>$workers.event.request.path</code> and <code>$workers.event.response.status</code> to identify the number of requests that were
affected by this behavior.</p>
<p><img src="/assets/upstream/images/workers-observability/wobs_QB_visualization_122.png" alt="Constructing a query" /></p>
<p>The results show that the <code>/agents/chat/default</code> path has been experiencing 404s and 500s. Now, we can apply a filter for this path and investigate.</p>
<p><img src="/assets/upstream/images/workers-observability/wobs_QB_visualization_filter_122.png" alt="Adding an additional field to the query" /></p>
<p>Now, we can investigate by selecting the <strong>Invocations</strong> tab. We can see that there were two logged invocations of this error.</p>
<p><img src="/assets/upstream/images/workers-observability/wobs_invocation_logs_full_list_122.png" alt="Examining the Invocations tab in the Query Builder" /></p>
<p>We can expand a single invocation to view the relevant logs, and continue to debug.</p>
<p><img src="/assets/upstream/images/workers-observability/wobs_invocation_logs_122.png" alt="Viewing the logs for a single Invocation" /></p>
