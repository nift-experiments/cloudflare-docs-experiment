<p>D1 allows you to define generated columns based on the values of one or more other columns, SQL functions, or even <a href="/d1/sql-api/query-json/">extracted JSON values</a>.</p>
<p>This allows you to normalize your data as you write to it or read it from a table, making it easier to query and reducing the need for complex application logic.</p>
<p>Generated columns can also have <a href="/d1/best-practices/use-indexes/">indexes defined</a> against them, which can dramatically increase query performance over frequently queried fields.</p>
<h2 id="types-of-generated-columns">Types of generated columns</h2>
<p>There are two types of generated columns:</p>
<ul>
<li><code>VIRTUAL</code> (default): the column is generated when read. This has the benefit of not consuming storage, but can increase compute time (and thus reduce query performance), especially for larger queries.</li>
<li><code>STORED</code>: the column is generated when the row is written. The column takes up storage space just as a regular column would, but the column does not need to be generated on every read, which can improve read query performance.</li>
</ul>
<p>When omitted from a generated column expression, generated columns default to the <code>VIRTUAL</code> type. The <code>STORED</code> type is recommended when the generated column is compute intensive. For example, when parsing large JSON structures.</p>
<h2 id="define-a-generated-column">Define a generated column</h2>
<p>Generated columns can be defined during table creation in a <code>CREATE TABLE</code> statement or afterwards via the <code>ALTER TABLE</code> statement.</p>
<p>To create a table that defines a generated column, you use the <code>AS</code> keyword:</p>
<pre><code class="language-sql">CREATE TABLE some_table (&#10;    &#45;- other columns omitted&#10;    some_generated_column AS &lt;function_that_generates_the_column_data&gt;&#10;)&#10;</code></pre>
<p>As a concrete example, to automatically extract the <code>location</code> value from the following JSON sensor data, you can define a generated column called <code>location</code> (of type <code>TEXT</code>), based on a <code>raw_data</code> column that stores the raw representation of our JSON data.</p>
<pre><code class="language-json">{&#10;    &quot;measurement&quot;: {&#10;        &quot;temp_f&quot;: &quot;77.4&quot;,&#10;        &quot;aqi&quot;: [21, 42, 58],&#10;        &quot;o3&quot;: [18, 500],&#10;        &quot;wind_mph&quot;: &quot;13&quot;,&#10;        &quot;location&quot;: &quot;US-NY&quot;&#10;    }&#10;}&#10;</code></pre>
<p>To define a generated column with the value of <code>$.measurement.location</code>, you can use the <a href="/d1/sql-api/query-json/#extract-values"><code>json_extract</code></a> function to extract the value from the <code>raw_data</code> column each time you write to that row:</p>
<pre><code class="language-sql">CREATE TABLE sensor_readings (&#10;    event_id INTEGER PRIMARY KEY,&#10;    timestamp INTEGER NOT NULL,&#10;    raw_data TEXT,&#10;    location as (json_extract(raw_data, &#x27;$.measurement.location&#x27;)) STORED&#10;);&#10;</code></pre>
<p>Generated columns can optionally be specified with the <code>column_name GENERATED ALWAYS AS &lt;function&gt; [STORED|VIRTUAL]</code> syntax. The <code>GENERATED ALWAYS</code> syntax is optional and does not change the behavior of the generated column when omitted.</p>
<h2 id="add-a-generated-column-to-an-existing-table">Add a generated column to an existing table</h2>
<p>A generated column can also be added to an existing table. If the <code>sensor_readings</code> table did not have the generated <code>location</code> column, you could add it by running an <code>ALTER TABLE</code> statement:</p>
<pre><code class="language-sql">ALTER TABLE sensor_readings&#10;ADD COLUMN location as (json_extract(raw_data, &#x27;$.measurement.location&#x27;));&#10;</code></pre>
<p>This defines a <code>VIRTUAL</code> generated column that runs <code>json_extract</code> on each read query.</p>
<p>Generated column definitions cannot be directly modified. To change how a generated column generates its data, you can use <code>ALTER TABLE table_name REMOVE COLUMN</code> and then <code>ADD COLUMN</code> to re-define the generated column, or <code>ALTER TABLE table_name RENAME COLUMN current_name TO new_name</code> to rename the existing column before calling <code>ADD COLUMN</code> with a new definition.</p>
<h2 id="examples">Examples</h2>
<p>Generated columns are not just limited to JSON functions like <code>json_extract</code>: you can use almost any available function to define how a generated column is generated.</p>
<p>For example, you could generate a <code>date</code> column based on the <code>timestamp</code> column from the previous <code>sensor_reading</code> table, automatically converting a Unix timestamp into a <code>YYYY-MM-dd</code> format within your database:</p>
<pre><code class="language-sql">ALTER TABLE your_table&#10;&#45;- date(timestamp, &#x27;unixepoch&#x27;) converts a Unix timestamp to a YYYY-MM-dd formatted date&#10;ADD COLUMN formatted_date AS (date(timestamp, &#x27;unixepoch&#x27;))&#10;</code></pre>
<p>Alternatively, you could define an <code>expires_at</code> column that calculates a future date, and filter on that date in your queries:</p>
<pre><code class="language-sql">&#45;- Filter out &quot;expired&quot; results based on your generated column:&#10;&#45;- SELECT * FROM your_table WHERE current_date() &gt; expires_at&#10;ALTER TABLE your_table&#10;&#45;- calculates a date (YYYY-MM-dd) 30 days from the timestamp.&#10;ADD COLUMN expires_at AS (date(timestamp, &#x27;+30 days&#x27;));&#10;</code></pre>
<h2 id="additional-considerations">Additional considerations</h2>
<ul>
<li>Tables must have at least one non-generated column. You cannot define a table with only generated column(s).</li>
<li>Expressions can only reference other columns in the same table and row, and must only use <a href="https://www.sqlite.org/deterministic.html">deterministic functions</a>. Functions like <code>random()</code>, sub-queries or aggregation functions cannot be used to define a generated column.</li>
<li>Columns added to an existing table via <code>ALTER TABLE ... ADD COLUMN</code> must be <code>VIRTUAL</code>. You cannot add a <code>STORED</code> column to an existing table.</li>
</ul>
