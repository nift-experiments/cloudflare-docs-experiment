<p>R2 SQL supports querying struct, array, and map column types stored in Iceberg tables. This page covers access patterns, supported functions, and examples for each type.</p>
<hr />
<h2 id="structs">Structs</h2>
<p>Struct columns contain named fields. Access fields using bracket notation or the <code>get_field()</code> function.</p>
<h3 id="bracket-notation">Bracket notation</h3>
<pre><code class="language-sql">SELECT pricing[&#x27;price&#x27;] AS price,&#10;       pricing[&#x27;discount_percent&#x27;] AS discount&#10;FROM my_namespace.products&#10;LIMIT 5&#10;</code></pre>
<h3 id="get-field-function">get_field function</h3>
<pre><code class="language-sql">SELECT get_field(pricing, &#x27;price&#x27;) AS price,&#10;       get_field(pricing, &#x27;discount_percent&#x27;) AS discount&#10;FROM my_namespace.products&#10;LIMIT 5&#10;</code></pre>
<h3 id="struct-fields-in-where">Struct fields in WHERE</h3>
<pre><code class="language-sql">SELECT customer_id, pricing[&#x27;price&#x27;] AS price&#10;FROM my_namespace.products&#10;WHERE pricing[&#x27;price&#x27;] &gt; 50&#10;LIMIT 10&#10;</code></pre>
<h3 id="struct-fields-in-order-by">Struct fields in ORDER BY</h3>
<pre><code class="language-sql">SELECT customer_id, pricing[&#x27;price&#x27;] AS price&#10;FROM my_namespace.products&#10;WHERE pricing[&#x27;price&#x27;] IS NOT NULL&#10;ORDER BY pricing[&#x27;price&#x27;] DESC&#10;LIMIT 10&#10;</code></pre>
<h3 id="struct-fields-in-group-by">Struct fields in GROUP BY</h3>
<pre><code class="language-sql">SELECT platforms[&#x27;windows&#x27;] AS windows_support,&#10;       COUNT(*) AS product_count,&#10;       AVG(pricing[&#x27;price&#x27;]) AS avg_price&#10;FROM my_namespace.products&#10;WHERE pricing[&#x27;price&#x27;] IS NOT NULL&#10;GROUP BY platforms[&#x27;windows&#x27;]&#10;</code></pre>
<h3 id="creating-structs-inline">Creating structs inline</h3>
<pre><code class="language-sql">&#45;- named_struct creates a struct with named fields&#10;SELECT named_struct(&#x27;id&#x27;, customer_id, &#x27;amount&#x27;, total_amount) AS info&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL&#10;LIMIT 1&#10;&#10;&#45;- struct creates a struct with positional fields&#10;SELECT struct(customer_id, total_amount, region) AS info&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL&#10;LIMIT 1&#10;</code></pre>
<hr />
<h2 id="arrays">Arrays</h2>
<p>Array columns contain ordered lists of values. Array indexing is <strong>1-based</strong>.</p>
<h3 id="index-access">Index access</h3>
<pre><code class="language-sql">SELECT customer_id, tags[1] AS first_tag, tags[2] AS second_tag&#10;FROM my_namespace.products&#10;LIMIT 5&#10;</code></pre>
<h3 id="create-arrays">Create arrays</h3>
<h4 id="make-array">make_array</h4>
<p>Creates an array from a list of values.</p>
<pre><code class="language-sql">SELECT make_array(1, 2, 3) AS nums&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="string-to-array">string_to_array</h4>
<p>Splits a string into an array by a delimiter.</p>
<pre><code class="language-sql">SELECT string_to_array(categories, &#x27;,&#x27;) AS cat_array&#10;FROM my_namespace.products&#10;WHERE categories IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h4 id="range">range</h4>
<p>Generates an array of integers from start (inclusive) to stop (exclusive).</p>
<pre><code class="language-sql">SELECT range(0, 5) AS nums&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="generate-series">generate_series</h4>
<p>Generates an array of integers from start to stop (inclusive).</p>
<pre><code class="language-sql">SELECT generate_series(1, 5) AS nums&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="inspect-arrays">Inspect arrays</h3>
<h4 id="array-length">array_length</h4>
<p>Returns the number of elements in an array.</p>
<pre><code class="language-sql">SELECT customer_id, array_length(tags) AS tag_count&#10;FROM my_namespace.products&#10;LIMIT 5&#10;</code></pre>
<h4 id="cardinality">cardinality</h4>
<p>Returns the total number of elements in an array. Alias for <code>array_length</code>.</p>
<pre><code class="language-sql">SELECT customer_id, cardinality(tags) AS tag_count&#10;FROM my_namespace.products&#10;LIMIT 5&#10;</code></pre>
<h4 id="empty">empty</h4>
<p>Returns true if an array has zero elements.</p>
<pre><code class="language-sql">SELECT customer_id, empty(tags) AS has_no_tags&#10;FROM my_namespace.products&#10;LIMIT 5&#10;</code></pre>
<h4 id="array-ndims">array_ndims</h4>
<p>Returns the number of dimensions of an array.</p>
<pre><code class="language-sql">SELECT array_ndims(make_array(1, 2, 3)) AS ndims&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="array-dims">array_dims</h4>
<p>Returns the dimensions of an array.</p>
<pre><code class="language-sql">SELECT array_dims(make_array(1, 2, 3)) AS dims&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="search-arrays">Search arrays</h3>
<h4 id="array-has">array_has</h4>
<p>Returns true if an array contains a value.</p>
<pre><code class="language-sql">SELECT customer_id, array_has(tags, &#x27;premium&#x27;) AS is_premium&#10;FROM my_namespace.products&#10;LIMIT 5&#10;</code></pre>
<h4 id="array-has-all">array_has_all</h4>
<p>Returns true if the first array contains all elements of the second.</p>
<pre><code class="language-sql">SELECT array_has_all(make_array(1, 2, 3, 4), make_array(2, 3)) AS has_all&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="array-has-any">array_has_any</h4>
<p>Returns true if the first array contains any element of the second.</p>
<pre><code class="language-sql">SELECT array_has_any(make_array(1, 2, 3), make_array(3, 4, 5)) AS has_any&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="array-position">array_position</h4>
<p>Returns the position of the first occurrence of a value (1-indexed). Returns 0 if not found.</p>
<pre><code class="language-sql">SELECT array_position(make_array(&#x27;a&#x27;, &#x27;b&#x27;, &#x27;c&#x27;, &#x27;b&#x27;), &#x27;b&#x27;) AS pos&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="array-positions">array_positions</h4>
<p>Returns all positions of a value as an array.</p>
<pre><code class="language-sql">SELECT array_positions(make_array(1, 2, 1, 3, 1), 1) AS positions&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="transform-arrays">Transform arrays</h3>
<h4 id="array-sort">array_sort</h4>
<p>Sorts array elements.</p>
<pre><code class="language-sql">SELECT array_sort(make_array(3, 1, 2)) AS sorted&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="array-reverse">array_reverse</h4>
<p>Reverses the order of array elements.</p>
<pre><code class="language-sql">SELECT array_reverse(make_array(1, 2, 3)) AS reversed&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="array-distinct">array_distinct</h4>
<p>Removes duplicate elements from an array.</p>
<pre><code class="language-sql">SELECT array_distinct(make_array(1, 2, 2, 3, 3, 3)) AS unique_vals&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="flatten">flatten</h4>
<p>Flattens a nested array by one level.</p>
<pre><code class="language-sql">SELECT flatten(make_array(make_array(1, 2), make_array(3, 4))) AS flat&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="array-slice">array_slice</h4>
<p>Returns a slice of an array from a start index to an end index (both inclusive, 1-indexed).</p>
<pre><code class="language-sql">SELECT array_slice(make_array(10, 20, 30, 40, 50), 2, 4) AS sliced&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="modify-arrays">Modify arrays</h3>
<h4 id="array-append">array_append</h4>
<p>Appends a value to the end of an array.</p>
<pre><code class="language-sql">SELECT array_append(make_array(1, 2, 3), 4) AS appended&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="array-prepend">array_prepend</h4>
<p>Prepends a value to the beginning of an array.</p>
<pre><code class="language-sql">SELECT array_prepend(0, make_array(1, 2, 3)) AS prepended&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="array-concat">array_concat</h4>
<p>Concatenates two or more arrays.</p>
<pre><code class="language-sql">SELECT array_concat(make_array(1, 2), make_array(3, 4)) AS merged&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="array-remove">array_remove</h4>
<p>Removes the first occurrence of a value from an array.</p>
<pre><code class="language-sql">SELECT array_remove(make_array(1, 2, 3, 2), 2) AS result&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="array-remove-all">array_remove_all</h4>
<p>Removes all occurrences of a value from an array.</p>
<pre><code class="language-sql">SELECT array_remove_all(make_array(1, 2, 3, 2, 2), 2) AS result&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="array-remove-n">array_remove_n</h4>
<p>Removes the first <em>n</em> occurrences of a value from an array.</p>
<pre><code class="language-sql">SELECT array_remove_n(make_array(1, 2, 2, 2, 3), 2, 2) AS result&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="array-replace">array_replace</h4>
<p>Replaces the first occurrence of a value in an array.</p>
<pre><code class="language-sql">SELECT array_replace(make_array(1, 2, 3), 2, 99) AS result&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="array-replace-n">array_replace_n</h4>
<p>Replaces the first <em>n</em> occurrences of a value in an array.</p>
<pre><code class="language-sql">SELECT array_replace_n(make_array(1, 2, 2, 2, 3), 2, 99, 2) AS result&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="array-replace-all">array_replace_all</h4>
<p>Replaces all occurrences of a value in an array.</p>
<pre><code class="language-sql">SELECT array_replace_all(make_array(1, 2, 3, 2), 2, 99) AS result&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="array-pop-back">array_pop_back</h4>
<p>Removes the last element from an array.</p>
<pre><code class="language-sql">SELECT array_pop_back(make_array(1, 2, 3)) AS result&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="array-pop-front">array_pop_front</h4>
<p>Removes the first element from an array.</p>
<pre><code class="language-sql">SELECT array_pop_front(make_array(1, 2, 3)) AS result&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="array-repeat">array_repeat</h4>
<p>Repeats a value a given number of times as an array.</p>
<pre><code class="language-sql">SELECT array_repeat(region, 3) AS repeated&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="array-resize">array_resize</h4>
<p>Resizes an array to a given length, filling with a default value.</p>
<pre><code class="language-sql">SELECT array_resize(make_array(1, 2), 5, 0) AS resized&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="set-operations-on-arrays">Set operations on arrays</h3>
<h4 id="array-intersect">array_intersect</h4>
<p>Returns elements common to both arrays.</p>
<pre><code class="language-sql">SELECT array_intersect(make_array(1, 2, 3), make_array(2, 3, 4)) AS common&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="array-union">array_union</h4>
<p>Returns all unique elements from both arrays.</p>
<pre><code class="language-sql">SELECT array_union(make_array(1, 2, 3), make_array(3, 4, 5)) AS merged&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="array-except">array_except</h4>
<p>Returns elements in the first array that are not in the second.</p>
<pre><code class="language-sql">SELECT array_except(make_array(1, 2, 3, 4), make_array(2, 4)) AS diff&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="aggregate-array-values">Aggregate array values</h3>
<h4 id="array-max">array_max</h4>
<p>Returns the maximum value in an array.</p>
<pre><code class="language-sql">SELECT customer_id, array_max(scores) AS max_score&#10;FROM my_namespace.products&#10;LIMIT 5&#10;</code></pre>
<h4 id="array-min">array_min</h4>
<p>Returns the minimum value in an array.</p>
<pre><code class="language-sql">SELECT customer_id, array_min(scores) AS min_score&#10;FROM my_namespace.products&#10;LIMIT 5&#10;</code></pre>
<h4 id="array-any-value">array_any_value</h4>
<p>Returns the first non-NULL value in an array.</p>
<pre><code class="language-sql">SELECT array_any_value(make_array(NULL, 42, NULL)) AS first_val&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h4 id="array-element">array_element</h4>
<p>Returns the element at a given index (1-indexed). Equivalent to bracket-notation access (<code>arr[idx]</code>).</p>
<pre><code class="language-sql">SELECT array_element(make_array(10, 20, 30), 2) AS second_val&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="convert-arrays">Convert arrays</h3>
<h4 id="array-to-string">array_to_string</h4>
<p>Joins array elements into a string with a separator.</p>
<pre><code class="language-sql">SELECT customer_id, array_to_string(tags, &#x27;, &#x27;) AS tag_list&#10;FROM my_namespace.products&#10;LIMIT 5&#10;</code></pre>
<hr />
<h2 id="maps">Maps</h2>
<p>Map columns store key-value pairs. Use <code>map_keys</code>, <code>map_values</code>, and <code>map_extract</code> to query them.</p>
<h3 id="map-keys">map_keys</h3>
<p>Returns all keys from a map as an array.</p>
<pre><code class="language-sql">SELECT map_keys(metadata) AS keys&#10;FROM my_namespace.products&#10;LIMIT 5&#10;</code></pre>
<h3 id="map-values">map_values</h3>
<p>Returns all values from a map as an array.</p>
<pre><code class="language-sql">SELECT map_values(metadata) AS vals&#10;FROM my_namespace.products&#10;LIMIT 5&#10;</code></pre>
<h3 id="map-extract">map_extract</h3>
<p>Returns the value for a specific key.</p>
<pre><code class="language-sql">SELECT map_extract(metadata, &#x27;source&#x27;) AS source,&#10;       map_extract(metadata, &#x27;store_name&#x27;) AS store&#10;FROM my_namespace.products&#10;LIMIT 5&#10;</code></pre>
<h3 id="creating-maps-inline">Creating maps inline</h3>
<pre><code class="language-sql">SELECT map(make_array(&#x27;a&#x27;, &#x27;b&#x27;), make_array(1, 2)) AS m&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<hr />
<h2 id="complete-function-index">Complete function index</h2>
<h3 id="struct-functions">Struct functions</h3>
<table>
<thead>
<tr>
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>struct_col['field']</code></td>
<td align="left">Bracket notation field access</td>
</tr>
<tr>
<td align="left"><code>get_field(struct, 'field')</code></td>
<td align="left">Function-based field access</td>
</tr>
<tr>
<td align="left"><code>named_struct(k1, v1, ...)</code></td>
<td align="left">Create struct with named fields</td>
</tr>
<tr>
<td align="left"><code>struct(v1, v2, ...)</code></td>
<td align="left">Create struct with positional fields</td>
</tr>
</tbody>
</table>
<h3 id="array-functions">Array functions</h3>
<table>
<thead>
<tr>
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>make_array(v1, v2, ...)</code></td>
<td align="left">Create array from values</td>
</tr>
<tr>
<td align="left"><code>string_to_array(str, delim)</code></td>
<td align="left">Split string into array</td>
</tr>
<tr>
<td align="left"><code>range(start, stop)</code></td>
<td align="left">Generate integer range (exclusive stop)</td>
</tr>
<tr>
<td align="left"><code>generate_series(start, stop)</code></td>
<td align="left">Generate integer series (inclusive stop)</td>
</tr>
<tr>
<td align="left"><code>array_length(arr)</code></td>
<td align="left">Number of elements</td>
</tr>
<tr>
<td align="left"><code>cardinality(arr)</code></td>
<td align="left">Number of elements</td>
</tr>
<tr>
<td align="left"><code>empty(arr)</code></td>
<td align="left">True if empty</td>
</tr>
<tr>
<td align="left"><code>array_ndims(arr)</code></td>
<td align="left">Number of dimensions</td>
</tr>
<tr>
<td align="left"><code>array_dims(arr)</code></td>
<td align="left">Dimension information</td>
</tr>
<tr>
<td align="left"><code>array_has(arr, val)</code></td>
<td align="left">Contains check</td>
</tr>
<tr>
<td align="left"><code>array_has_all(arr, arr2)</code></td>
<td align="left">Contains all check</td>
</tr>
<tr>
<td align="left"><code>array_has_any(arr, arr2)</code></td>
<td align="left">Contains any check</td>
</tr>
<tr>
<td align="left"><code>array_position(arr, val)</code></td>
<td align="left">First position of value</td>
</tr>
<tr>
<td align="left"><code>array_positions(arr, val)</code></td>
<td align="left">All positions of value</td>
</tr>
<tr>
<td align="left"><code>array_sort(arr)</code></td>
<td align="left">Sort elements</td>
</tr>
<tr>
<td align="left"><code>array_reverse(arr)</code></td>
<td align="left">Reverse order</td>
</tr>
<tr>
<td align="left"><code>array_distinct(arr)</code></td>
<td align="left">Remove duplicates</td>
</tr>
<tr>
<td align="left"><code>flatten(arr)</code></td>
<td align="left">Flatten one level</td>
</tr>
<tr>
<td align="left"><code>array_slice(arr, start, end)</code></td>
<td align="left">Extract sub-array</td>
</tr>
<tr>
<td align="left"><code>array_append(arr, val)</code></td>
<td align="left">Append to end</td>
</tr>
<tr>
<td align="left"><code>array_prepend(val, arr)</code></td>
<td align="left">Prepend to start</td>
</tr>
<tr>
<td align="left"><code>array_concat(arr1, arr2)</code></td>
<td align="left">Concatenate arrays</td>
</tr>
<tr>
<td align="left"><code>array_remove(arr, val)</code></td>
<td align="left">Remove first occurrence</td>
</tr>
<tr>
<td align="left"><code>array_remove_all(arr, val)</code></td>
<td align="left">Remove all occurrences</td>
</tr>
<tr>
<td align="left"><code>array_remove_n(arr, val, n)</code></td>
<td align="left">Remove first <em>n</em> occurrences</td>
</tr>
<tr>
<td align="left"><code>array_replace(arr, old, new)</code></td>
<td align="left">Replace first occurrence</td>
</tr>
<tr>
<td align="left"><code>array_replace_n(arr, old, new, n)</code></td>
<td align="left">Replace first <em>n</em> occurrences</td>
</tr>
<tr>
<td align="left"><code>array_replace_all(arr, old, new)</code></td>
<td align="left">Replace all occurrences</td>
</tr>
<tr>
<td align="left"><code>array_pop_back(arr)</code></td>
<td align="left">Remove last element</td>
</tr>
<tr>
<td align="left"><code>array_pop_front(arr)</code></td>
<td align="left">Remove first element</td>
</tr>
<tr>
<td align="left"><code>array_repeat(val, n)</code></td>
<td align="left">Repeat value <em>n</em> times</td>
</tr>
<tr>
<td align="left"><code>array_resize(arr, size, default)</code></td>
<td align="left">Resize with default fill</td>
</tr>
<tr>
<td align="left"><code>array_intersect(arr1, arr2)</code></td>
<td align="left">Common elements</td>
</tr>
<tr>
<td align="left"><code>array_union(arr1, arr2)</code></td>
<td align="left">Union of elements</td>
</tr>
<tr>
<td align="left"><code>array_except(arr1, arr2)</code></td>
<td align="left">Difference of elements</td>
</tr>
<tr>
<td align="left"><code>array_max(arr)</code></td>
<td align="left">Maximum value</td>
</tr>
<tr>
<td align="left"><code>array_min(arr)</code></td>
<td align="left">Minimum value</td>
</tr>
<tr>
<td align="left"><code>array_any_value(arr)</code></td>
<td align="left">First non-NULL value</td>
</tr>
<tr>
<td align="left"><code>array_to_string(arr, delim)</code></td>
<td align="left">Join elements as string</td>
</tr>
<tr>
<td align="left"><code>array_element(arr, idx)</code></td>
<td align="left">Element at index</td>
</tr>
</tbody>
</table>
<h3 id="map-functions">Map functions</h3>
<table>
<thead>
<tr>
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>map(keys_arr, vals_arr)</code></td>
<td align="left">Create map from key and value arrays</td>
</tr>
<tr>
<td align="left"><code>map_keys(map)</code></td>
<td align="left">All keys as array</td>
</tr>
<tr>
<td align="left"><code>map_values(map)</code></td>
<td align="left">All values as array</td>
</tr>
<tr>
<td align="left"><code>map_extract(map, key)</code></td>
<td align="left">Value for a specific key</td>
</tr>
</tbody>
</table>
