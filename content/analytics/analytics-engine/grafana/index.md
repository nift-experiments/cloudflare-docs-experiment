<p>Workers Analytics Engine is optimized for powering time series analytics that can be visualized using tools like Grafana. Every event written from the runtime is automatically populated with a <code>timestamp</code> field.</p>
<h2 id="grafana-plugin-setup">Grafana plugin setup</h2>
<p>We recommend the use of the <a href="https://grafana.com/grafana/plugins/vertamedia-clickhouse-datasource/">Altinity plugin for Clickhouse</a> for querying Workers Analytics Engine from Grafana.</p>
<p>Configure the plugin as follows:</p>
<ul>
<li>URL: <code>https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/analytics_engine/sql</code>. Replace <code>&lt;account_id&gt;</code> with your 32 character account ID (available in the Cloudflare dashboard).</li>
<li>Leave all auth settings off.</li>
<li>Add a custom header with a name of <code>Authorization</code> and value set to <code>Bearer &lt;token&gt;</code>. Replace <code>&lt;token&gt;</code> with suitable API token string (refer to the <a href="/analytics/analytics-engine/sql-api/#authentication">SQL API docs</a> for more information on this).</li>
<li>No other options need to be set.</li>
</ul>
<h2 id="querying-timeseries-data">Querying timeseries data</h2>
<p>For use in a dashboard, you usually want to aggregate some metric per time interval. This can be achieved by rounding and then grouping by the <code>timestamp</code> field. The following query rounds and groups in this way, and then computes an average across each time interval whilst taking into account <a href="/analytics/analytics-engine/sql-api/#sampling">sampling</a>.</p>
<pre><code class="language-sql">SELECT&#10;    intDiv(toUInt32(timestamp), 60) * 60 AS t,&#10;    blob1 AS label,&#10;    SUM(_sample_interval * double1) / SUM(_sample_interval) AS average_metric&#10;FROM dataset_name&#10;WHERE &#10;    timestamp &lt;= NOW() &#10;    AND timestamp &gt; NOW() - INTERVAL &#x27;1&#x27; DAY&#10;GROUP BY blob1, t&#10;ORDER BY t&#10;</code></pre>
<p>The Altinity plugin provides some useful macros that can simplify writing queries of this type. The macros require setting <code>Column:DateTime</code> to <code>timestamp</code> in the query builder, then they can be used like this:</p>
<pre><code class="language-sql">SELECT&#10;    $timeSeries AS t,&#10;    blob1 AS label,&#10;    SUM(_sample_interval * double1) / SUM(_sample_interval) AS average_metric&#10;FROM dataset_name&#10;WHERE $timeFilter&#10;GROUP BY blob1, t&#10;ORDER BY t&#10;</code></pre>
<p>This query will automatically adjust the rounding time depending on the zoom level and filter to the correct time range that is currently being displayed.</p>
