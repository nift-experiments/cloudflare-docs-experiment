<p>Cloudflare Pipelines provides two set of JSON functions, the first based on PostgreSQL's SQL
functions and syntax, and the second based on the
<a href="https://jsonpath.com/">JSONPath</a> standard.</p>
<h2 id="sql-functions">SQL functions</h2>
<p>The SQL functions provide basic JSON parsing functions similar to those found in
PostgreSQL.</p>
<h3 id="json-contains">json_contains</h3>
<p>Returns <code>true</code> if the JSON string contains the specified key(s).</p>
<pre><code class="language-sql">SELECT json_contains(&#x27;{&quot;a&quot;: 1, &quot;b&quot;: 2, &quot;c&quot;: 3}&#x27;, &#x27;a&#x27;) FROM source;&#10;true&#10;</code></pre>
<p>Also available via the <code>?</code> operator:</p>
<pre><code class="language-sql">SELECT &#x27;{&quot;a&quot;: 1, &quot;b&quot;: 2, &quot;c&quot;: 3}&#x27; ? &#x27;a&#x27; FROM source;&#10;true&#10;</code></pre>
<h3 id="json-get">json_get</h3>
<p>Retrieves the value from a JSON string by the specified path (keys). Returns the
value as its native type (string, int, etc.).</p>
<pre><code class="language-sql">SELECT json_get(&#x27;{&quot;a&quot;: {&quot;b&quot;: 2}}&#x27;, &#x27;a&#x27;, &#x27;b&#x27;) FROM source;&#10;2&#10;</code></pre>
<p>Also available via the <code>-&gt;</code> operator:</p>
<pre><code class="language-sql">SELECT &#x27;{&quot;a&quot;: {&quot;b&quot;: 2}}&#x27;-&gt;&#x27;a&#x27;-&gt;&#x27;b&#x27; FROM source;&#10;2&#10;</code></pre>
<p>Various permutations of <code>json_get</code> functions are available for retrieving values as
a specific type, or you can use SQL type annotations:</p>
<pre><code class="language-sql">SELECT json_get(&#x27;{&quot;a&quot;: {&quot;b&quot;: 2}}&#x27;, &#x27;a&#x27;, &#x27;b&#x27;)::int FROM source;&#10;2&#10;</code></pre>
<h3 id="json-get-str">json_get_str</h3>
<p>Retrieves a string value from a JSON string by the specified path. Returns an
empty string if the value does not exist or is not a string.</p>
<pre><code class="language-sql">SELECT json_get_str(&#x27;{&quot;a&quot;: {&quot;b&quot;: &quot;hello&quot;}}&#x27;, &#x27;a&#x27;, &#x27;b&#x27;) FROM source;&#10;&quot;hello&quot;&#10;</code></pre>
<h3 id="json-get-int">json_get_int</h3>
<p>Retrieves an integer value from a JSON string by the specified path. Returns <code>0</code>
if the value does not exist or is not an integer.</p>
<pre><code class="language-sql">SELECT json_get_int(&#x27;{&quot;a&quot;: {&quot;b&quot;: 42}}&#x27;, &#x27;a&#x27;, &#x27;b&#x27;) FROM source;&#10;42&#10;</code></pre>
<h3 id="json-get-float">json_get_float</h3>
<p>Retrieves a float value from a JSON string by the specified path. Returns <code>0.0</code>
if the value does not exist or is not a float.</p>
<pre><code class="language-sql">SELECT json_get_float(&#x27;{&quot;a&quot;: {&quot;b&quot;: 3.14}}&#x27;, &#x27;a&#x27;, &#x27;b&#x27;) FROM source;&#10;3.14&#10;</code></pre>
<h3 id="json-get-bool">json_get_bool</h3>
<p>Retrieves a boolean value from a JSON string by the specified path. Returns
<code>false</code> if the value does not exist or is not a boolean.</p>
<pre><code class="language-sql">SELECT json_get_bool(&#x27;{&quot;a&quot;: {&quot;b&quot;: true}}&#x27;, &#x27;a&#x27;, &#x27;b&#x27;) FROM source;&#10;true&#10;</code></pre>
<h3 id="json-get-json">json_get_json</h3>
<p>Retrieves a nested JSON string from a JSON string by the specified path. The
value is returned as raw JSON.</p>
<pre><code class="language-sql">SELECT json_get_json(&#x27;{&quot;a&quot;: {&quot;b&quot;: {&quot;c&quot;: 1}}}&#x27;, &#x27;a&#x27;, &#x27;b&#x27;) FROM source;&#10;&#x27;{&quot;c&quot;: 1}&#x27;&#10;</code></pre>
<h3 id="json-as-text">json_as_text</h3>
<p>Retrieves any value from a JSON string by the specified path and returns it as a
string, regardless of the original type.</p>
<pre><code class="language-sql">SELECT json_as_text(&#x27;{&quot;a&quot;: {&quot;b&quot;: 42}}&#x27;, &#x27;a&#x27;, &#x27;b&#x27;) FROM source;&#10;&quot;42&quot;&#10;</code></pre>
<p>Also available via the <code>-&gt;&gt;</code> operator:</p>
<pre><code class="language-sql">SELECT &#x27;{&quot;a&quot;: {&quot;b&quot;: 42}}&#x27;-&gt;&gt;&#x27;a&#x27;-&gt;&gt;&#x27;b&#x27; FROM source;&#10;&quot;42&quot;&#10;</code></pre>
<h3 id="json-length">json_length</h3>
<p>Returns the length of a JSON object or array at the specified path. Returns <code>0</code>
if the path does not exist or is not an object/array.</p>
<pre><code class="language-sql">SELECT json_length(&#x27;{&quot;a&quot;: [1, 2, 3]}&#x27;, &#x27;a&#x27;) FROM source;&#10;3&#10;</code></pre>
<h2 id="json-path-functions">Json path functions</h2>
<p>JSON functions provide basic json parsing functions using
<a href="https://goessner.net/articles/JsonPath/">JsonPath</a>, an evolving standard for
querying JSON objects.</p>
<h3 id="extract-json">extract_json</h3>
<p>Returns the JSON elements in the first argument that match the JsonPath in the second argument.
The returned value is an array of json strings.</p>
<pre><code class="language-sql">SELECT extract_json(&#x27;{&quot;a&quot;: 1, &quot;b&quot;: 2, &quot;c&quot;: 3}&#x27;, &#x27;$.a&#x27;) FROM source;&#10;[&#x27;1&#x27;]&#10;</code></pre>
<h3 id="extract-json-string">extract_json_string</h3>
<p>Returns an unescaped String for the first item matching the JsonPath, if it is a string.</p>
<pre><code class="language-sql">SELECT extract_json_string(&#x27;{&quot;a&quot;: &quot;a&quot;, &quot;b&quot;: 2, &quot;c&quot;: 3}&#x27;, &#x27;$.a&#x27;) FROM source;&#10;&#x27;a&#x27;&#10;</code></pre>
