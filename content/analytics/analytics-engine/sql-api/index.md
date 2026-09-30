<p>The Workers Analytics Engine SQL API is an HTTP API that allows executing SQL queries against your Workers Analytics Engine datasets.</p>
<p>The API is hosted at <code>https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/analytics_engine/sql</code>.</p>
<h2 id="authentication">Authentication</h2>
<p>Authentication is done via bearer token. An <code>Authorization: Bearer &lt;token&gt;</code> header must be supplied with every request to the API.</p>
<p>Use the dashboard to create a token with permission to read analytics data on your account:</p>
<ol>
<li>Visit the <a href="https://dash.cloudflare.com/profile/api-tokens">API tokens</a> page in the Cloudflare dashboard.</li>
<li>Select <strong>Create Token</strong>.</li>
<li>Select <strong>Create Custom Token</strong>.</li>
<li>Complete the <strong>Create Custom Token</strong> form as follows:
<ul>
<li>Give your token a descriptive name.</li>
<li>For <strong>Permissions</strong> select <em>Account</em> | <em>Account Analytics</em> | <em>Read</em></li>
<li>Optionally configure account and IP restrictions and TTL.</li>
<li>Submit and confirm the form to create the token.</li>
</ul>
</li>
<li>Make a note of the token string.</li>
</ol>
<h2 id="querying-the-api">Querying the API</h2>
<p>Submit the query text in the body of a <code>POST</code> request to the API address. The format of the data returned can be selected using the <a href="/analytics/analytics-engine/sql-reference/statements/#format-clause"><code>FORMAT</code></a> option in your query.</p>
<p>You can use cURL to test the API as follows, replacing the <code>&lt;account_id&gt;</code> with your 32 character account ID (available in the dashboard) and the <code>&lt;token&gt;</code> with the token string you generated above.</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/analytics_engine/sql&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-data &quot;SELECT &#x27;Hello Workers Analytics Engine&#x27; AS message&quot;&#10;</code></pre>
<p>If you have already published some data, you might try executing the following to confirm that the dataset has been created in the DB.</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/analytics_engine/sql&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-data &quot;SHOW TABLES&quot;&#10;</code></pre>
<p>Refer to the Workers Analytics Engine <a href="/analytics/analytics-engine/sql-reference/">SQL reference</a>, for the full supported query syntax.</p>
<h2 id="table-structure">Table structure</h2>
<p>A new table will automatically be created for each dataset once you start writing events to it from your worker.</p>
<p>The table will have the following columns:</p>
<table>
<thead>
<tr>
<th>Name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>dataset</td>
<td>string</td>
<td>This column will contain the dataset name in every row.</td>
</tr>
<tr>
<td>timestamp</td>
<td>DateTime</td>
<td>The timestamp at which the event was logged in your worker.</td>
</tr>
<tr>
<td>_sample_interval</td>
<td>integer</td>
<td>In case that the data has been sampled, this column indicates what the sample rate is for this row (that is, how many rows of the original data are represented by this row). Refer to the <a href="#sampling">sampling</a> section below for more information.</td>
</tr>
<tr>
<td>index1</td>
<td>string</td>
<td>The index value that was logged with the event. The value in this column is used as the key for sampling.</td>
</tr>
<tr>
<td>blob1<br/>...<br/>blob20</td>
<td>string</td>
<td>The blob values that were logged with the event.</td>
</tr>
<tr>
<td>double1<br/>...<br/>double20</td>
<td>double</td>
<td>The double values that were logged with the event.</td>
</tr>
</tbody>
</table>
<h2 id="sampling">Sampling</h2>
<p>At very high volumes of data, Analytics Engine will downsample data in order to be able to maintain performance. Sampling can occur on write and on read.
Sampling is based on the index of your dataset so that only indexes that receive large numbers of events will be sampled. For example, if your worker serves multiple customers, you might consider making customer ID the index field. This would mean that if one customer starts making a high rate of requests then events from that customer could be sampled while other customers data remains unsampled.</p>
<p>We have tested this system of sampling over a number of years at Cloudflare and it has enabled us to scale our web analytics systems to very high throughput, while still providing statistically meaningful results irrespective of the amount of traffic a website receives.</p>
<p>The rate at which the data is sampled is exposed via the <code>_sample_interval</code> column. This means that if you are doing statistical analysis of your data, you may need to take this column into account. For example:</p>
<table>
<thead>
<tr>
<th>Original query</th>
<th>Query taking into account sampling</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>SELECT COUNT() FROM ... </code></td>
<td><code>SELECT SUM(_sample_interval) FROM ...</code></td>
</tr>
<tr>
<td><code>SELECT SUM(double1) FROM ...</code></td>
<td><code>SELECT SUM(_sample_interval * double1) FROM ...</code></td>
</tr>
<tr>
<td><code>SELECT AVG(double1) FROM ...</code></td>
<td><code>SELECT SUM(_sample_interval * double1) / SUM(_sample_interval) FROM ...</code></td>
</tr>
</tbody>
</table>
<p>Additionally, the <a href="/analytics/analytics-engine/sql-reference/aggregate-functions/#quantileexactweighted">QUANTILEEXACTWEIGHTED</a> function is designed to be used with sample interval as the third argument.</p>
<h2 id="example-queries">Example queries</h2>
<h3 id="select-data-with-column-aliases">Select data with column aliases</h3>
<p>Column aliases can be used in queries to give names to the blobs and doubles in your dataset:</p>
<pre><code class="language-sql">SELECT&#10;    timestamp,&#10;    blob1 AS location_id,&#10;    double1 AS inside_temp,&#10;    double2 AS outside_temp&#10;FROM temperatures&#10;WHERE timestamp &gt; NOW() - INTERVAL &#x27;1&#x27; DAY&#10;</code></pre>
<h3 id="aggregation-taking-into-account-sample-interval">Aggregation taking into account sample interval</h3>
<p>Calculate number of readings taken at each location in the last 7 days. In this case, we are grouping by the index field so an exact count can be calculated even in the case that the data has been sampled:</p>
<pre><code class="language-sql">SELECT&#10;    index1 AS location_id,&#10;    SUM(_sample_interval) AS n_readings&#10;FROM temperatures&#10;WHERE timestamp &gt; NOW() - INTERVAL &#x27;7&#x27; DAY&#10;GROUP BY index1&#10;</code></pre>
<p>Calculate the average temperature over the last 7 days at each location. Sample interval is taken into account:</p>
<pre><code class="language-sql">SELECT&#10;    index1 AS location_id,&#10;    SUM(_sample_interval * double1) / SUM(_sample_interval) AS average_temp&#10;FROM temperatures&#10;WHERE timestamp &gt; NOW() - INTERVAL &#x27;7&#x27; DAY&#10;GROUP BY index1&#10;</code></pre>
