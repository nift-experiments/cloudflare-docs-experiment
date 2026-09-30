<p>Log Explorer enables you to store and explore your Cloudflare logs directly within the Cloudflare dashboard or API, giving you visibility into your logs without the need to forward them to third-party services. Logs are stored on Cloudflare's global network using the R2 object storage platform and can be queried via the dashboard or SQL API.</p>
<h2 id="when-to-use-log-explorer">When to use Log Explorer</h2>
<p>Use Log Explorer when you need to investigate what actually happened with real production traffic:</p>
<ul>
<li>Analyzing historical data and trends</li>
<li>Investigating security incidents after they occur</li>
<li>Searching for patterns across thousands of requests</li>
<li>Monitoring application performance over time</li>
<li>Providing forensic evidence to support teams</li>
</ul>
<p>Use <a href="/rules/trace-request/">Trace</a> when you need to test what would happen with a simulated request:</p>
<ul>
<li>Understanding why a rule did not trigger as expected</li>
<li>Testing how your rules handle different request scenarios</li>
<li>Seeing the evaluation order of your rules</li>
<li>Simulating requests from different geolocations or conditions</li>
</ul>
<p>The key difference is that Log Explorer shows actual traffic, while Trace shows simulated &quot;what-if&quot; scenarios.</p>
<h2 id="use-log-explorer">Use Log Explorer</h2>
<p>You can filter and view your logs via the Cloudflare dashboard or the API.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Log Explorer</strong> &gt; <strong>Log Search</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Dataset</strong> you want to use and in <strong>Columns</strong> select the dataset fields. If you selected a zone scoped dataset, select the zone you would like to use.</li>
<li>Enter a <strong>Limit</strong>. A limit is the maximum number of results to return, for example, 50.</li>
<li>Select the <strong>Time period</strong> from which you want to query, for example, the previous 12 hours.</li>
<li>Select <strong>Add filter</strong> to create your query. Select a <strong>Field</strong>, an <strong>Operator</strong>, and a <strong>Value</strong>, then select <strong>Apply</strong>.</li>
<li>A query preview is displayed. Select <strong>Custom SQL</strong> to change the query.</li>
<li>Select <strong>Run query</strong> when you are done. The results are displayed below within the <strong>Query results</strong> section.</li>
</ol>
<p>For example, to find an HTTP request with a specific <a href="/fundamentals/reference/cloudflare-ray-id/">Ray ID</a>, go to <strong>Custom SQL</strong>, and enter the following SQL query:</p>
<pre><code class="language-sql">SELECT&#10;	clientRequestScheme,&#10;	clientRequestHost,&#10;	clientRequestMethod,&#10;	edgeResponseStatus,&#10;	clientRequestUserAgent&#10;FROM http_requests&#10;WHERE RayID = &#x27;806c30a3cec56817&#x27;&#10;LIMIT 1&#10;</code></pre>
<p>As another example, to find Cloudflare Access requests with selected columns from a specific timeframe you could perform the following SQL query:</p>
<pre><code class="language-sql">SELECT&#10;	CreatedAt,&#10;	AppDomain,&#10;	AppUUID,&#10;	Action,&#10;	Allowed,&#10;	Country,&#10;	RayID,&#10;	Email,&#10;	IPAddress,&#10;	UserUID&#10;FROM access_requests&#10;WHERE Date &gt;= &#x27;2025-02-06&#x27; AND Date &lt;= &#x27;2025-02-06&#x27; AND CreatedAt &gt;= &#x27;2025-02-06T12:28:39Z&#x27; AND CreatedAt &lt;= &#x27;2025-02-06T12:58:39Z&#x27;&#10;</code></pre>
<h3 id="headers-and-cookies">Headers and cookies</h3>
<p>To query request headers, response headers, and cookies you must first enable logging for these fields using <a href="/logs/logpush/logpush-job/custom-fields/">Custom fields</a>. Configure the list of custom fields using the API or the dashboard; there is no need to modify the Logpush job itself.</p>
<p>The example below shows how to query HTTP requests by date, timestamp, client country, and a custom request header. Be sure to log the specific headers or cookies you plan to query in advance.</p>
<pre><code class="language-bash">SELECT clientip, clientrequesthost, clientrequestmethod, edgeendtimestamp, edgestarttimestamp, rayid, clientcountry, requestheaders&#10;FROM http_requests&#10;WHERE Date &gt;= &#x27;2025-07-17&#x27;&#10;  AND Date &lt;= &#x27;2025-07-17&#x27;&#10;  AND edgeendtimestamp &gt;= &#x27;2025-07-17T07:54:19Z&#x27;&#10;  AND edgeendtimestamp &lt;= &#x27;2025-07-18T07:54:19Z&#x27;&#10;  AND clientcountry = &#x27;us&#x27;&#10;  AND requestheaders.&quot;x-test-header&quot; like &#x27;%654AM%&#x27;;&#10;</code></pre>
<h3 id="save-queries">Save queries</h3>
<p>After selecting all the fields for your query, you can save it by selecting <strong>Save query</strong>. Provide a name and description to help identify it later. To view your saved and recent queries, select <strong>Queries</strong> — they will appear in a side panel where you can insert a new query, or delete any query.</p>
<h2 id="integration-with-security-analytics">Integration with Security Analytics</h2>
<p>You can also access the Log Explorer dashboard directly from the <a href="/waf/analytics/security-analytics/#logs">Security Analytics dashboard</a>. When doing so, the filters you applied in Security Analytics will automatically carry over to your query in Log Explorer.</p>
<h2 id="optimize-your-queries">Optimize your queries</h2>
<p>All the tables supported by Log Explorer contain a special column called <code>date</code>, which helps to narrow down the amount of data that is scanned to respond to your query, resulting in faster query response times. The value of <code>date</code> must be in the form of <code>YYYY-MM-DD</code>. For example, to query logs that occurred on October 12, 2023, add the following to your <code>WHERE</code> clause: <code>date = '2023-10-12'</code>. The column supports the standard operators of <code>&lt;</code>, <code>&gt;</code>, and <code>=</code>.</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/login">Cloudflare dashboard</a> and select your account.</li>
<li>Go to <strong>Log Explorer</strong> &gt; <strong>Log Search</strong> &gt; <strong>Custom SQL</strong>.</li>
<li>Enter the following SQL query:</li>
</ol>
<pre><code class="language-sql">SELECT&#10;	clientip,&#10;	clientrequesthost,&#10;	clientrequestmethod,&#10;	clientrequesturi,&#10;	edgeendtimestamp,&#10;	edgeresponsestatus,&#10;	originresponsestatus,&#10;	edgestarttimestamp,&#10;	rayid,&#10;	clientcountry,&#10;	clientrequestpath,&#10;	date&#10;FROM&#10;	http_requests&#10;WHERE&#10;	date = &#x27;2023-10-12&#x27; LIMIT 500&#10;</code></pre>
<h3 id="additional-query-optimization-tips">Additional query optimization tips</h3>
<ul>
<li>Narrow your query time frame. Focus on a smaller time window to reduce the volume of data processed. This helps avoid querying excessive amounts of data and speeds up response times.</li>
<li>Omit <code>ORDER BY</code> and <code>LIMIT</code> clauses. These clauses can slow down queries, especially when dealing with large datasets. For queries that return a large number of records, reduce the time frame instead of limiting to the newest <code>N</code> records from a broader time frame.</li>
<li>Select only necessary columns. For example, replace <code>SELECT *</code> with the list of specific columns you need. You can also use <code>SELECT RayId</code> as a first iteration and follow up with a query that filters by the Ray IDs to retrieve additional columns. Additionally, you can use <code>SELECT COUNT(*)</code> to probe for time frames with matching records without retrieving the full dataset.</li>
</ul>
