<p>Flagship supports 11 comparison operators for targeting rule conditions. Each operator compares an attribute from the <a href="/flagship/concepts/#evaluation-context">evaluation context</a> against a specified value.</p>
<h2 id="operator-reference">Operator reference</h2>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Description</th>
<th>Example</th>
<th>Value type</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>equals</code></td>
<td>Returns true if the attribute value matches the specified value.</td>
<td><code>country equals &quot;US&quot;</code></td>
<td>String</td>
</tr>
<tr>
<td><code>not_equals</code></td>
<td>Returns true if the attribute value does not match the specified value.</td>
<td><code>plan not_equals &quot;free&quot;</code></td>
<td>String</td>
</tr>
<tr>
<td><code>greater_than</code></td>
<td>Returns true if the attribute value is greater than the specified value.</td>
<td><code>age greater_than 18</code></td>
<td>Number, ISO 8601 datetime</td>
</tr>
<tr>
<td><code>less_than</code></td>
<td>Returns true if the attribute value is less than the specified value.</td>
<td><code>loginCount less_than 5</code></td>
<td>Number, ISO 8601 datetime</td>
</tr>
<tr>
<td><code>greater_than_or_equals</code></td>
<td>Returns true if the attribute value is greater than or equal to the specified value.</td>
<td><code>score greater_than_or_equals 90</code></td>
<td>Number, ISO 8601 datetime</td>
</tr>
<tr>
<td><code>less_than_or_equals</code></td>
<td>Returns true if the attribute value is less than or equal to the specified value.</td>
<td><code>createdAt less_than_or_equals &quot;2025-01-01T00:00:00Z&quot;</code></td>
<td>Number, ISO 8601 datetime</td>
</tr>
<tr>
<td><code>contains</code></td>
<td>Returns true if the attribute value contains the specified substring.</td>
<td><code>email contains &quot;@cloudflare.com&quot;</code></td>
<td>String</td>
</tr>
<tr>
<td><code>starts_with</code></td>
<td>Returns true if the attribute value starts with the specified prefix.</td>
<td><code>path starts_with &quot;/api/v2&quot;</code></td>
<td>String</td>
</tr>
<tr>
<td><code>ends_with</code></td>
<td>Returns true if the attribute value ends with the specified suffix.</td>
<td><code>domain ends_with &quot;.dev&quot;</code></td>
<td>String</td>
</tr>
<tr>
<td><code>in</code></td>
<td>Returns true if the attribute value is in the specified array.</td>
<td><code>country in [&quot;US&quot;, &quot;CA&quot;, &quot;UK&quot;]</code></td>
<td>Array</td>
</tr>
<tr>
<td><code>not_in</code></td>
<td>Returns true if the attribute value is not in the specified array.</td>
<td><code>userId not_in [&quot;blocked-1&quot;, &quot;blocked-2&quot;]</code></td>
<td>Array</td>
</tr>
</tbody>
</table>
<h2 id="operator-categories">Operator categories</h2>
<h3 id="equality-operators">Equality operators</h3>
<p><code>equals</code>, <code>not_equals</code></p>
<p>Use these operators for exact string matching. The comparison is case-sensitive.</p>
<h3 id="comparison-operators">Comparison operators</h3>
<p><code>greater_than</code>, <code>less_than</code>, <code>greater_than_or_equals</code>, <code>less_than_or_equals</code></p>
<p>These operators work with numeric values and ISO 8601 datetime strings. When comparing datetimes, provide the value in ISO 8601 format (for example, <code>&quot;2025-01-01T00:00:00Z&quot;</code>).</p>
<h3 id="string-operators">String operators</h3>
<p><code>contains</code>, <code>starts_with</code>, <code>ends_with</code></p>
<p>These operators perform substring matching against the attribute value. All string comparisons are case-sensitive.</p>
<h3 id="array-operators">Array operators</h3>
<p><code>in</code>, <code>not_in</code></p>
<p>The value must be an array. Flagship checks whether the attribute value is a member of the specified array.</p>
