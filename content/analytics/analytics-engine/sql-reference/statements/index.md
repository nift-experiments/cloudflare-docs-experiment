<h2 id="show-tables-statement">SHOW TABLES statement</h2>
<p><code>SHOW TABLES</code> can be used to list the tables on your account. The table name is the name you specified as <code>dataset</code> when configuring the workers binding (refer to <a href="/analytics/analytics-engine/get-started/">Get started with Workers Analytics Engine</a>, for more information). The table is automatically created when you write event data in your worker.</p>
<pre><code class="language-sql">SHOW TABLES&#10;[FORMAT &lt;format&gt;]&#10;</code></pre>
<p>Refer to <a href="#format-clause">FORMAT clause</a> for the available <code>FORMAT</code> options.</p>
<h2 id="show-timezones-statement">SHOW TIMEZONES statement</h2>
<p><code>SHOW TIMEZONES</code> can be used to list all of the timezones supported by the SQL API. Most common timezones are supported.</p>
<pre><code class="language-sql">SHOW TIMEZONES&#10;[FORMAT &lt;format&gt;]&#10;</code></pre>
<h2 id="show-timezone-statement">SHOW TIMEZONE statement</h2>
<p><code>SHOW TIMEZONE</code> responds with the current default timezone in use by SQL API. This should always be <code>Etc/UTC</code>.</p>
<pre><code class="language-sql">SHOW TIMEZONE&#10;[FORMAT &lt;format&gt;]&#10;</code></pre>
<h2 id="select-statement">SELECT statement</h2>
<p><code>SELECT</code> is used to query tables.</p>
<p>Usage:</p>
<pre><code class="language-sql">SELECT &lt;expression_list&gt;&#10;[FROM &lt;table&gt;|(&lt;subquery&gt;)]&#10;[WHERE &lt;expression&gt;]&#10;[GROUP BY &lt;expression&gt;, ...]&#10;[HAVING &lt;expression&gt;]&#10;[ORDER BY &lt;expression_list&gt;]&#10;[LIMIT &lt;n&gt;|ALL]&#10;[FORMAT &lt;format&gt;]&#10;</code></pre>
<p>Below you can find the syntax of each clause. Refer to the <a href="/analytics/analytics-engine/sql-api/">SQL API</a> documentation for some example queries.</p>
<h3 id="select-clause">SELECT clause</h3>
<p>The <code>SELECT</code> clause specifies the list of columns to be included in the result.
Columns can be aliased using the <code>AS</code> keyword.</p>
<p>Usage:</p>
<pre><code class="language-sql">SELECT &lt;expression&gt; [AS &lt;alias&gt;], ...&#10;</code></pre>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- return the named columns&#10;SELECT blob2, double3&#10;&#10;&#45;- return all columns&#10;SELECT *&#10;&#10;&#45;- alias columns to more descriptive names&#10;SELECT&#10;    blob2 AS probe_name,&#10;    double3 AS temperature&#10;</code></pre>
<p>Additionally, expressions using supported functions and <a href="/analytics/analytics-engine/sql-reference/operators/">operators</a> can be used in place of column names:</p>
<pre><code class="language-sql">SELECT&#10;    blob2 AS probe_name,&#10;    double3 AS temp_c,&#10;    double3*1.8+32 AS temp_f -- compute a value&#10;&#10;SELECT&#10;    blob2 AS probe_name,&#10;    if(double3 &lt;= 0, &#x27;FREEZING&#x27;, &#x27;NOT FREEZING&#x27;) AS description -- use of functions&#10;&#10;SELECT&#10;    blob2 AS probe_name,&#10;    avg(double3) AS avg_temp -- aggregation function&#10;</code></pre>
<h3 id="from-clause">FROM clause</h3>
<p><code>FROM</code> is used to specify the source of the data for the query.</p>
<p>Usage:</p>
<pre><code class="language-sql">FROM &lt;table_name&gt;|(subquery)&#10;</code></pre>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- query data written to a workers dataset called &quot;temperatures&quot;&#10;FROM temperatures&#10;&#10;&#45;- use a subquery to manipulate the table&#10;FROM (&#10;    SELECT&#10;        blob1 AS probe_name,&#10;        count() as num_readings&#10;    FROM&#10;        temperatures&#10;    GROUP BY&#10;        probe_name&#10;)&#10;</code></pre>
<p>Note that queries can only operate on a single table. <code>UNION</code>, <code>JOIN</code> etc. are not currently supported.</p>
<h3 id="where-clause">WHERE clause</h3>
<p><code>WHERE</code> is used to filter the rows returned by a query before grouping and aggregation.</p>
<p>Usage:</p>
<pre><code class="language-sql">WHERE &lt;condition&gt;&#10;</code></pre>
<p><code>&lt;condition&gt;</code> can be any expression that evaluates to a boolean.</p>
<p><a href="/analytics/analytics-engine/sql-reference/operators/#comparison-operators">Comparison operators</a> can be used to compare values and <a href="/analytics/analytics-engine/sql-reference/operators/#boolean-operators">boolean operators</a> can be used to combine conditions.</p>
<p>Expressions containing functions and <a href="/analytics/analytics-engine/sql-reference/operators/">operators</a> are supported.</p>
<p>To filter results after grouping and aggregation, use the <a href="#having-clause"><code>HAVING</code> clause</a> instead.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- simple comparisons&#10;WHERE blob1 = &#x27;test&#x27;&#10;WHERE double1 = 4&#10;&#10;&#45;- inequalities&#10;WHERE double1 &gt; 4&#10;&#10;&#45;- use of operators (see below for supported operator list)&#10;WHERE double1 + double2 &gt; 4&#10;WHERE blob1 = &#x27;test1&#x27; OR blob2 = &#x27;test2&#x27;&#10;&#10;&#45;- expression using inequalities, functions and operators&#10;WHERE if(unit = &#x27;f&#x27;, (temp-32)/1.8, temp) &lt;= 0&#10;</code></pre>
<h3 id="group-by-clause">GROUP BY clause</h3>
<p>When using aggregate functions, <code>GROUP BY</code> specifies the groups over which the aggregation is run.</p>
<p>Usage:</p>
<pre><code class="language-sql">GROUP BY &lt;expression&gt;, ...&#10;</code></pre>
<p>For example, if you had a table of temperature readings:</p>
<pre><code class="language-sql">&#45;- return the average temperature for each probe&#10;SELECT&#10;    blob1 AS probe_name,&#10;    avg(double1) AS average_temp&#10;FROM temperature_readings&#10;GROUP BY probe_name&#10;</code></pre>
<p>In the usual case the <code>&lt;expression&gt;</code> can just be a column name but it is also possible to supply a complex expression here. Multiple expressions or column names can be supplied separated by commas.</p>
<h3 id="having-clause">HAVING clause <span class="nb-badge">New</span></h3>
<p><code>HAVING</code> is used to filter the results after grouping and aggregation.</p>
<p>Usage:</p>
<pre><code class="language-sql">HAVING &lt;condition&gt;&#10;</code></pre>
<p><code>&lt;condition&gt;</code> can be any expression that evaluates to a boolean, and can reference aggregate functions or grouped columns.</p>
<p>Unlike <code>WHERE</code>, which filters rows before grouping, <code>HAVING</code> filters groups after aggregation. This allows you to filter based on aggregate values.</p>
<p><a href="/analytics/analytics-engine/sql-reference/operators/#comparison-operators">Comparison operators</a> can be used to compare values and <a href="/analytics/analytics-engine/sql-reference/operators/#boolean-operators">boolean operators</a> can be used to combine conditions.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- filter groups where the average is greater than 10&#10;SELECT&#10;    blob1 AS probe_name,&#10;    avg(double1) AS average_temp&#10;FROM temperature_readings&#10;GROUP BY probe_name&#10;HAVING average_temp &gt; 10&#10;&#10;&#45;- filter groups with more than 100 readings&#10;SELECT&#10;    blob1 AS probe_name,&#10;    count() AS num_readings&#10;FROM temperature_readings&#10;GROUP BY probe_name&#10;HAVING num_readings &gt; 100&#10;&#10;&#45;- combine multiple conditions&#10;SELECT&#10;    blob1 AS city,&#10;    avg(double1) AS avg_temp,&#10;    count() AS readings&#10;FROM weather_data&#10;GROUP BY city&#10;HAVING avg_temp &gt; 20 AND readings &gt;= 50&#10;</code></pre>
<h3 id="order-by-clause">ORDER BY clause</h3>
<p><code>ORDER BY</code> can be used to control the order in which rows are returned.</p>
<p>Usage:</p>
<pre><code class="language-sql">ORDER BY &lt;expression&gt; [ASC|DESC], ...&#10;</code></pre>
<p><code>&lt;expression&gt;</code> can just be a column name.</p>
<p><code>ASC</code> or <code>DESC</code> determines if the ordering is ascending or descending. <code>ASC</code> is the default, and can be omitted.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- order by double2 then double3, both in ascending order&#10;ORDER BY double2, double3&#10;&#10;&#45;- order by double2 in ascending order then double3 is descending order&#10;ORDER BY double2, double3 DESC&#10;</code></pre>
<h3 id="limit-clause">LIMIT clause</h3>
<p><code>LIMIT</code> specifies a maximum number of rows to return.</p>
<p>Usage:</p>
<pre><code class="language-sql">LIMIT &lt;n&gt;|ALL&#10;</code></pre>
<p>Supply the maximum number of rows to return or <code>ALL</code> for no restriction.</p>
<p>For example:</p>
<pre><code class="language-sql">LIMIT 10 -- return at most 10 rows&#10;</code></pre>
<h3 id="offset-clause">OFFSET clause</h3>
<p><code>OFFSET</code> specifies a number of rows to skip in the query result.</p>
<p>Usage:</p>
<pre><code class="language-sql">OFFSET &lt;n&gt;&#10;</code></pre>
<p>For example:</p>
<pre><code class="language-sql">OFFSET 10 -- skip the first 10 result rows&#10;</code></pre>
<h3 id="format-clause">FORMAT clause</h3>
<p><code>FORMAT</code> controls how to the returned data is encoded.</p>
<p>Usage:</p>
<pre><code class="language-sql">FORMAT [JSON|JSONEachRow|TabSeparated]&#10;</code></pre>
<p>If no format clause is included then the default format of <code>JSON</code> will be used.</p>
<p>Override the default by setting a format. For example:</p>
<pre><code class="language-sql">FORMAT JSONEachRow&#10;</code></pre>
<p>The following formats are supported:</p>
<h4 id="json">JSON</h4>
<p>Data is returned as a single JSON object with schema data included:</p>
<pre><code class="language-json">{&#10;    &quot;meta&quot;: [&#10;        {&#10;            &quot;name&quot;: &quot;&lt;column 1 name&gt;&quot;,&#10;            &quot;type&quot;: &quot;&lt;column 1 type&gt;&quot;&#10;        },&#10;        {&#10;            &quot;name&quot;: &quot;&lt;column 2 name&gt;&quot;,&#10;            &quot;type&quot;: &quot;&lt;column 2 type&gt;&quot;&#10;        },&#10;        ...&#10;    ],&#10;    &quot;data&quot;: [&#10;        {&#10;            &quot;&lt;column 1 name&gt;&quot;: &quot;&lt;column 1 value&gt;&quot;,&#10;            &quot;&lt;column 2 name&gt;&quot;: &quot;&lt;column 2 value&gt;&quot;,&#10;            ...&#10;        },&#10;        {&#10;            &quot;&lt;column 1 name&gt;&quot;: &quot;&lt;column 1 value&gt;&quot;,&#10;            &quot;&lt;column 2 name&gt;&quot;: &quot;&lt;column 2 value&gt;&quot;,&#10;            ...&#10;        },&#10;        ...&#10;    ],&#10;    &quot;rows&quot;: 10&#10;}&#10;</code></pre>
<h4 id="jsoneachrow">JSONEachRow</h4>
<p>Data is returned with a separate JSON object per row. Rows are newline separated and there is no header line or schema data:</p>
<pre><code class="language-json">{&quot;&lt;column 1 name&gt;&quot;: &quot;&lt;column 1 value&gt;&quot;, &quot;&lt;column 2 name&gt;&quot;: &quot;&lt;column 2 value&gt;&quot;}&#10;{&quot;&lt;column 1 name&gt;&quot;: &quot;&lt;column 1 value&gt;&quot;, &quot;&lt;column 2 name&gt;&quot;: &quot;&lt;column 2 value&gt;&quot;}&#10;...&#10;</code></pre>
<h4 id="tabseparated">TabSeparated</h4>
<p>Data is returned with newline separated rows. Columns are separated with tabs. There is no header.</p>
<pre><code class="language-txt">column 1 value  column 2 value&#10;column 1 value  column 2 value&#10;...&#10;</code></pre>
