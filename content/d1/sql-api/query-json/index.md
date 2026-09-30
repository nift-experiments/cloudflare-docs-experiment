<p>D1 has built-in support for querying and parsing JSON data stored within a database. This enables you to:</p>
<ul>
<li><a href="#extract-values">Query paths</a> within a stored JSON object - for example, extracting the value of named key or array index directly, which is especially useful with larger JSON objects.</li>
<li>Insert and/or replace values within an object or array.</li>
<li><a href="#expand-arrays-for-in-queries">Expand the contents of a JSON object</a> or array into multiple rows - for example, for use as part of a <code>WHERE ... IN</code> predicate.</li>
<li>Create <a href="/d1/reference/generated-columns/">generated columns</a> that are automatically populated with values from JSON objects you insert.</li>
</ul>
<p>One of the biggest benefits to parsing JSON within D1 directly is that it can directly reduce the number of round-trips (queries) to your database. It reduces the cases where you have to read a JSON object into your application (1), parse it, and then write it back (2).</p>
<p>This allows you to more precisely query over data and reduce the result set your application needs to additionally parse and filter on.</p>
<h2 id="types">Types</h2>
<p>JSON data is stored as a <code>TEXT</code> column in D1. JSON types follow the same <a href="/d1/worker-api/#type-conversion">type conversion rules</a> as D1 in general, including:</p>
<ul>
<li>A JSON null is treated as a D1 <code>NULL</code>.</li>
<li>A JSON number is treated as an <code>INTEGER</code> or <code>REAL</code>.</li>
<li>Booleans are treated as <code>INTEGER</code> values: <code>true</code> as <code>1</code> and <code>false</code> as <code>0</code>.</li>
<li>Object and array values as <code>TEXT</code>.</li>
</ul>
<h2 id="supported-functions">Supported functions</h2>
<p>The following table outlines the JSON functions built into D1 and example usage.</p>
<ul>
<li>The <code>json</code> argument placeholder can be a JSON object, array, string, number or a null value.</li>
<li>The <code>value</code> argument accepts string literals (only) and treats input as a string, even if it is well-formed JSON. The exception to this rule is when nesting <code>json_*</code> functions: the outer (wrapping) function will interpret the inner (wrapped) functions return value as JSON.</li>
<li>The <code>path</code> argument accepts path-style traversal syntax - for example, <code>$</code> to refer to the top-level object/array, <code>$.key1.key2</code> to refer to a nested object, and <code>$.key[2]</code> to index into an array.</li>
</ul>
<table>
<thead>
<tr>
<th>Function</th>
<th>Description</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>json(json)</code></td>
<td>Validates the provided string is JSON and returns a minified version of that JSON object.</td>
<td><code>json('{&quot;hello&quot;:[&quot;world&quot; ,&quot;there&quot;] }')</code> returns <code>{&quot;hello&quot;:[&quot;world&quot;,&quot;there&quot;]}</code></td>
</tr>
<tr>
<td><code>json_array(value1, value2, value3, ...)</code></td>
<td>Return a JSON array from the values.</td>
<td><code>json_array(1, 2, 3)</code> returns <code>[1, 2, 3]</code></td>
</tr>
<tr>
<td><code>json_array_length(json)</code> - <code>json_array_length(json, path)</code></td>
<td>Return the length of the JSON array</td>
<td><code>json_array_length('{&quot;data&quot;:[&quot;x&quot;, &quot;y&quot;, &quot;z&quot;]}', '$.data')</code> returns <code>3</code></td>
</tr>
<tr>
<td><code>json_extract(json, path)</code></td>
<td>Extract the value(s) at the given path using <code>$.path.to.value</code> syntax.</td>
<td><code>json_extract('{&quot;temp&quot;:&quot;78.3&quot;, &quot;sunset&quot;:&quot;20:44&quot;}', '$.temp')</code> returns <code>&quot;78.3&quot;</code></td>
</tr>
<tr>
<td><code>json -&gt; path</code></td>
<td>Extract the value(s) at the given path using path syntax and return it as JSON.</td>
<td></td>
</tr>
<tr>
<td><code>json -&gt;&gt; path</code></td>
<td>Extract the value(s) at the given path using path syntax and return it as a SQL type.</td>
<td></td>
</tr>
<tr>
<td><code>json_insert(json, path, value)</code></td>
<td>Insert a value at the given path. Does not overwrite an existing value.</td>
<td></td>
</tr>
<tr>
<td><code>json_object(label1, value1, ...)</code></td>
<td>Accepts pairs of (keys, values) and returns a JSON object.</td>
<td><code>json_object('temp', 45, 'wind_speed_mph', 13)</code> returns <code>{&quot;temp&quot;:45,&quot;wind_speed_mph&quot;:13}</code></td>
</tr>
<tr>
<td><code>json_patch(target, patch)</code></td>
<td>Uses a JSON <a href="https://tools.ietf.org/html/rfc7396">MergePatch</a> approach to merge the provided patch into the target JSON object.</td>
<td></td>
</tr>
<tr>
<td><code>json_remove(json, path, ...)</code></td>
<td>Remove the key and value at the specified path.</td>
<td><code>json_remove('[60,70,80,90]', '$[0]')</code> returns <code>70,80,90]</code></td>
</tr>
<tr>
<td><code>json_replace(json, path, value)</code></td>
<td>Insert a value at the given path. Overwrites an existing value, but does not create a new key if it doesn't exist.</td>
<td></td>
</tr>
<tr>
<td><code>json_set(json, path, value)</code></td>
<td>Insert a value at the given path. Overwrites an existing value.</td>
<td></td>
</tr>
<tr>
<td><code>json_type(json)</code> - <code>json_type(json, path)</code></td>
<td>Return the type of the provided value or value at the specified path. Returns one of <code>null</code>, <code>true</code>, <code>false</code>, <code>integer</code>, <code>real</code>, <code>text</code>, <code>array</code>, or <code>object</code>.</td>
<td><code>json_type('{&quot;temperatures&quot;:[73.6, 77.8, 80.2]}', '$.temperatures')</code> returns <code>array</code></td>
</tr>
<tr>
<td><code>json_valid(json)</code></td>
<td>Returns 0 (false) for invalid JSON, and 1 (true) for valid JSON.</td>
<td><code>json_valid({invalid:json})</code>returns<code>0\</code></td>
</tr>
<tr>
<td><code>json_quote(value)</code></td>
<td>Converts the provided SQL value into its JSON representation.</td>
<td><code>json_quote('[1, 2, 3]')</code> returns <code>[1,2,3]</code></td>
</tr>
<tr>
<td><code>json_group_array(value)</code></td>
<td>Returns the provided value(s) as a JSON array.</td>
<td></td>
</tr>
<tr>
<td><code>json_each(value)</code> - <code>json_each(value, path)</code></td>
<td>Returns each element within the object as an individual row. It will only traverse the top-level object.</td>
<td></td>
</tr>
<tr>
<td><code>json_tree(value)</code> - <code>json_tree(value, path)</code></td>
<td>Returns each element within the object as an individual row. It traverses the full object.</td>
<td></td>
</tr>
</tbody>
</table>
<p>The SQLite <a href="https://www.sqlite.org/json1.html">JSON extension</a>, on which D1 builds on, has additional usage examples.</p>
<h2 id="error-handling">Error Handling</h2>
<p>JSON functions will return a <code>malformed JSON</code> error when operating over data that isn't JSON and/or is not valid JSON. D1 considers valid JSON to be <a href="https://www.rfc-editor.org/rfc/rfc7159.txt">RFC 7159</a> conformant.</p>
<p>In the following example, calling <code>json_extract</code> over a string (not valid JSON) will cause the query to return a <code>malformed JSON</code> error:</p>
<pre><code class="language-sql">SELECT json_extract(&#x27;not valid JSON: just a string&#x27;, &#x27;$&#x27;)&#10;</code></pre>
<p>This will return an error:</p>
<pre><code class="language-txt">ERROR 9015: SQL engine error: query error: Error code 1: SQL error or missing database (malformed&#10;  JSON)`&#10;</code></pre>
<h2 id="generated-columns">Generated columns</h2>
<p>D1's support for <a href="/d1/reference/generated-columns/">generated columns</a> allows you to create dynamic columns that are generated based on the values of other columns, including extracted or calculated values of JSON data.</p>
<p>These columns can be queried like any other column, and can have <a href="/d1/best-practices/use-indexes/">indexes</a> defined on them. If you have JSON data that you frequently query and filter over, creating a generated column and an index can dramatically improve query performance.</p>
<p>For example, to define a column based on a value within a larger JSON object, use the <code>AS</code> keyword combined with a <a href="#supported-functions">JSON function</a> to generate a typed column:</p>
<pre><code class="language-sql">CREATE TABLE some_table (&#10;    &#45;- other columns omitted&#10;    raw_data TEXT -- JSON: {&quot;measurement&quot;:{&quot;aqi&quot;:[21,42,58],&quot;wind_mph&quot;:&quot;13&quot;,&quot;location&quot;:&quot;US-NY&quot;}}&#10;    location AS (json_extract(raw_data, &#x27;$.measurement.location&#x27;)) STORED&#10;)&#10;</code></pre>
<p>Refer to <a href="/d1/reference/generated-columns/">Generated columns</a> to learn more about how to generate columns.</p>
<h2 id="example-usage">Example usage</h2>
<h3 id="extract-values">Extract values</h3>
<p>There are three ways to extract a value from a JSON object in D1:</p>
<ul>
<li>The <code>json_extract()</code> function - for example, <code>json_extract(text_column_containing_json, '$.path.to.value)</code>.</li>
<li>The <code>-&gt;</code> operator, which returns a JSON representation of the value.</li>
<li>The <code>-&gt;&gt;</code> operator, which returns an SQL representation of the value.</li>
</ul>
<p>The <code>-&gt;</code> and <code>-&gt;&gt;</code> operators functions both operate similarly to the same operators in PostgreSQL and MySQL/MariaDB.</p>
<p>Given the following JSON object in a column named <code>sensor_reading</code>, you can extract values from it directly.</p>
<pre><code class="language-json">{&#10;    &quot;measurement&quot;: {&#10;        &quot;temp_f&quot;: &quot;77.4&quot;,&#10;        &quot;aqi&quot;: [21, 42, 58],&#10;        &quot;o3&quot;: [18, 500],&#10;        &quot;wind_mph&quot;: &quot;13&quot;,&#10;        &quot;location&quot;: &quot;US-NY&quot;&#10;    }&#10;}&#10;</code></pre>
<pre><code class="language-sql">&#45;- Extract the temperature value&#10;json_extract(sensor_reading, &#x27;$.measurement.temp_f&#x27;)-- returns &quot;77.4&quot; as TEXT&#10;</code></pre>
<pre><code class="language-sql">&#45;- Extract the maximum PM2.5 air quality reading&#10;sensor_reading -&gt; &#x27;$.measurement.aqi[3]&#x27; -- returns 58 as a JSON number&#10;</code></pre>
<pre><code class="language-sql">&#45;- Extract the o3 (ozone) array in full&#10;sensor_reading -\-&gt; &#x27;$.measurement.o3&#x27; -- returns &#x27;[18, 500]&#x27; as TEXT&#10;</code></pre>
<h3 id="get-the-length-of-an-array">Get the length of an array</h3>
<p>You can get the length of a JSON array in two ways:</p>
<ol>
<li>By calling <code>json_array_length(value)</code> directly</li>
<li>By calling <code>json_array_length(value, path)</code> to specify the path to an array within an object or outer array.</li>
</ol>
<p>For example, given the following JSON object stored in a column called <code>login_history</code>, you could get a count of the last logins directly:</p>
<pre><code class="language-json">{&#10;    &quot;user_id&quot;: &quot;abc12345&quot;,&#10;    &quot;previous_logins&quot;: [&quot;2023-03-31T21:07:14-05:00&quot;, &quot;2023-03-28T08:21:02-05:00&quot;, &quot;2023-03-28T05:52:11-05:00&quot;]&#10;}&#10;</code></pre>
<pre><code class="language-sql">json_array_length(login_history, &#x27;$.previous_logins&#x27;) --&gt; returns 3 as an INTEGER&#10;</code></pre>
<p>You can also use <code>json_array_length</code> as a predicate in a more complex query - for example, <code>WHERE json_array_length(some_column, '$.path.to.value') &gt;= 5</code>.</p>
<h3 id="insert-a-value-into-an-existing-object">Insert a value into an existing object</h3>
<p>You can insert a value into an existing JSON object or array using <code>json_insert()</code>. For example, if you have a <code>TEXT</code> column called <code>login_history</code> in a <code>users</code> table containing the following object:</p>
<pre><code class="language-json">{&quot;history&quot;: [&quot;2023-05-13T15:13:02+00:00&quot;, &quot;2023-05-14T07:11:22+00:00&quot;, &quot;2023-05-15T15:03:51+00:00&quot;]}&#10;</code></pre>
<p>To add a new timestamp to the <code>history</code> array within our <code>login_history</code> column, write a query resembling the following:</p>
<pre><code class="language-sql">UPDATE users&#10;SET login_history = json_insert(login_history, &#x27;$.history[#]&#x27;, &#x27;2023-05-15T20:33:06+00:00&#x27;)&#10;WHERE user_id = &#x27;aba0e360-1e04-41b3-91a0-1f2263e1e0fb&#x27;&#10;</code></pre>
<p>Provide three arguments to <code>json_insert</code>:</p>
<ol>
<li>The name of our column containing the JSON you want to modify.</li>
<li>The path to the key within the object to modify.</li>
<li>The JSON value to insert. Using <code>[#]</code> tells <code>json_insert</code> to append to the end of your array.</li>
</ol>
<p>To replace an existing value, use <code>json_replace()</code>, which will overwrite an existing key-value pair if one already exists. To set a value regardless of whether it already exists, use <code>json_set()</code>.</p>
<h3 id="expand-arrays-for-in-queries">Expand arrays for IN queries</h3>
<p>Use <code>json_each</code> to expand an array into multiple rows. This can be useful when composing a <code>WHERE column IN (?)</code> query over several values. For example, if you wanted to update a list of users by their integer <code>id</code>, use <code>json_each</code> to return a table with each value as a column called <code>value</code>:</p>
<pre><code class="language-sql">UPDATE users&#10;SET last_audited = &#x27;2023-05-16T11:24:08+00:00&#x27;&#10;WHERE id IN (SELECT value FROM json_each(&#x27;[183183, 13913, 94944]&#x27;))&#10;</code></pre>
<p>This would extract only the <code>value</code> column from the table returned by <code>json_each</code>, with each row representing the user IDs you passed in as an array.</p>
<p><code>json_each</code> effectively returns a table with multiple columns, with the most relevant being:</p>
<ul>
<li><code>key</code> - the key (or index).</li>
<li><code>value</code> - the literal value of each element parsed by <code>json_each</code>.</li>
<li><code>type</code> - the type of the value: one of <code>null</code>, <code>true</code>, <code>false</code>, <code>integer</code>, <code>real</code>, <code>text</code>, <code>array</code>, or <code>object</code>.</li>
<li><code>fullkey</code> - the full path to the element: e.g. <code>$[1]</code> for the second element in an array, or <code>$.path.to.key</code> for a nested object.</li>
<li><code>path</code> - the top-level path - <code>$</code> as the path for an element with a <code>fullkey</code> of <code>$[0]</code>.</li>
</ul>
<p>In this example, <code>SELECT * FROM json_each('[183183, 13913, 94944]')</code> would return a table resembling the below:</p>
<pre><code class="language-sql">key|value|type|id|fullkey|path&#10;0|183183|integer|1|$[0]|$&#10;1|13913|integer|2|$[1]|$&#10;2|94944|integer|3|$[2]|$&#10;</code></pre>
<p>You can use <code>json_each</code> with <a href="/d1/worker-api/">D1 Workers Binding API</a> in a Worker by creating a statement and using <code>JSON.stringify</code> to pass an array as a <a href="/d1/worker-api/d1-database/#guidance">bound parameter</a>:</p>
<pre><code class="language-ts">const stmt = context.env.DB&#10;    .prepare(&quot;UPDATE users SET last_audited = ? WHERE id IN (SELECT value FROM json_each(?1))&quot;)&#10;const resp = await stmt.bind(&#10;    &quot;2023-05-16T11:24:08+00:00&quot;,&#10;    JSON.stringify([183183, 13913, 94944])&#10;    ).run()&#10;</code></pre>
<p>This would only update rows in your <code>users</code> table where the <code>id</code> matches one of the three provided.</p>
