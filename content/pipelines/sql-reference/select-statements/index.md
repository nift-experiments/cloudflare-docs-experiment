<p>SELECT statements are used to transform data in Cloudflare Pipelines. The general form is:</p>
<pre><code class="language-sql">[WITH with_query [, ...]]&#10;SELECT select_expr [, ...]&#10;FROM from_item&#10;[WHERE condition]&#10;</code></pre>
<p>A pipeline runs one or more <code>INSERT INTO sink SELECT ... FROM stream</code> statements. To write to multiple sinks from the same pipeline, separate the statements with semicolons. See <a href="#multiple-statements">Multiple statements</a>.</p>
<h2 id="with-clause">WITH clause</h2>
<p>The WITH clause allows you to define named subqueries that can be referenced in the main query. This can improve query readability by breaking down complex transformations.</p>
<p>Syntax:</p>
<pre><code class="language-sql">WITH query_name AS (subquery) [, ...]&#10;</code></pre>
<p>Simple example:</p>
<pre><code class="language-sql">WITH filtered_events AS&#10;    (SELECT user_id, event_type, amount&#10;        FROM user_events WHERE amount &gt; 50)&#10;SELECT user_id, amount * 1.1 as amount_with_tax&#10;FROM filtered_events&#10;WHERE event_type = &#x27;purchase&#x27;;&#10;</code></pre>
<h2 id="select-clause">SELECT clause</h2>
<p>The SELECT clause is a comma-separated list of expressions, with optional aliases. Column names must be unique.</p>
<pre><code class="language-sql">SELECT select_expr [, ...]&#10;</code></pre>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- Select specific columns&#10;SELECT user_id, event_type, amount FROM events&#10;&#10;&#45;- Use expressions and aliases&#10;SELECT&#10;    user_id,&#10;    amount * 1.1 as amount_with_tax,&#10;    UPPER(event_type) as event_type_upper&#10;FROM events&#10;&#10;&#45;- Select all columns&#10;SELECT * FROM events&#10;</code></pre>
<h2 id="from-clause">FROM clause</h2>
<p>The FROM clause specifies the data source for the query. It will be either a table name or subquery. The table name can be either a stream name or a table created in the WITH clause.</p>
<pre><code class="language-sql">FROM from_item&#10;</code></pre>
<p>Tables can be given aliases:</p>
<pre><code class="language-sql">SELECT e.user_id, e.amount&#10;FROM user_events e&#10;WHERE e.event_type = &#x27;purchase&#x27;&#10;</code></pre>
<h2 id="where-clause">WHERE clause</h2>
<p>The WHERE clause filters data using boolean conditions. Predicates are applied to input rows.</p>
<pre><code class="language-sql">WHERE condition&#10;</code></pre>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- Filter by field value&#10;SELECT * FROM events WHERE event_type = &#x27;purchase&#x27;&#10;&#10;&#45;- Multiple conditions&#10;SELECT * FROM events&#10;WHERE event_type = &#x27;purchase&#x27; AND amount &gt; 50&#10;&#10;&#45;- String operations&#10;SELECT * FROM events&#10;WHERE user_id LIKE &#x27;user_%&#x27;&#10;&#10;&#45;- Null checks&#10;SELECT * FROM events&#10;WHERE description IS NOT NULL&#10;</code></pre>
<h2 id="unnest-operator">UNNEST operator</h2>
<p>The UNNEST operator converts arrays into multiple rows. This is useful for processing list data types.</p>
<p>UNNEST restrictions:</p>
<ul>
<li>May only appear in the SELECT clause</li>
<li>Only one array may be unnested per SELECT statement</li>
</ul>
<p>Example:</p>
<pre><code class="language-sql">SELECT&#10;    UNNEST([1, 2, 3]) as numbers&#10;FROM events;&#10;</code></pre>
<p>This will produce:</p>
<pre><code>&#43;---------+&#10;| numbers |&#10;&#43;---------+&#10;|       1 |&#10;|       2 |&#10;|       3 |&#10;&#43;---------+&#10;</code></pre>
<h2 id="multiple-statements">Multiple statements</h2>
<p>A pipeline can contain multiple <code>INSERT</code> statements, separated by semicolons. Each statement reads from a stream and writes to a sink. Use multiple statements to route events from a single stream into several sinks based on their content.</p>
<pre><code class="language-sql">INSERT INTO purchases_sink&#10;SELECT user_id, product_id, amount FROM events&#10;WHERE event_type = &#x27;purchase&#x27;;&#10;&#10;INSERT INTO signups_sink&#10;SELECT user_id, created_at FROM events&#10;WHERE event_type = &#x27;signup&#x27;;&#10;</code></pre>
<p>To provide multiple statements with the Wrangler CLI, pass a file with the <code>--sql-file</code> flag:</p>
<pre><code class="language-bash">npx wrangler pipelines create my-pipeline --sql-file pipeline.sql&#10;</code></pre>
<p>For a worked example, refer to <a href="/pipelines/examples/bluesky-firehose-fanout/">Fan out a stream to multiple Iceberg tables</a>.</p>
