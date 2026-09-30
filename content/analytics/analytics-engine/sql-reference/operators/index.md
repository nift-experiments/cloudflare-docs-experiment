<p>The following operators are supported:</p>
<h2 id="arithmetic-operators">Arithmetic operators</h2>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>+</code></td>
<td>addition</td>
</tr>
<tr>
<td><code>-</code></td>
<td>subtraction</td>
</tr>
<tr>
<td><code>*</code></td>
<td>multiplication</td>
</tr>
<tr>
<td><code>/</code></td>
<td>division</td>
</tr>
<tr>
<td><code>%</code></td>
<td>modulus</td>
</tr>
</tbody>
</table>
<h2 id="comparison-operators">Comparison operators</h2>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>=</code></td>
<td>equals</td>
</tr>
<tr>
<td><code>&lt;</code></td>
<td>less than</td>
</tr>
<tr>
<td><code>&gt;</code></td>
<td>greater than</td>
</tr>
<tr>
<td><code>&lt;=</code></td>
<td>less than or equal to</td>
</tr>
<tr>
<td><code>&gt;=</code></td>
<td>greater than or equal to</td>
</tr>
<tr>
<td><code>&lt;&gt;</code> or <code>!=</code></td>
<td>not equal</td>
</tr>
<tr>
<td><code>IN</code></td>
<td>true if the preceding expression's value is in the list<br/><code>column IN ('a', 'list', 'of', 'values')</code></td>
</tr>
<tr>
<td><code>NOT IN</code></td>
<td>true if the preceding expression's value is not in the list<br/><code>column NOT IN ('a', 'list', 'of', 'values')</code></td>
</tr>
</tbody>
</table>
<p>We also support the <code>BETWEEN</code> operator for checking a value is in an inclusive range: <code>a [NOT] BETWEEN b AND c</code>.</p>
<h3 id="pattern-matching-operators">Pattern matching operators <span class="nb-badge">New</span></h3>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>LIKE</code></td>
<td>true if the string matches the pattern (case-sensitive)<br/><code>column LIKE 'pattern%'</code></td>
</tr>
<tr>
<td><code>NOT LIKE</code></td>
<td>true if the string does not match the pattern (case-sensitive)<br/><code>column NOT LIKE 'pattern%'</code></td>
</tr>
<tr>
<td><code>ILIKE</code></td>
<td>true if the string matches the pattern (case-insensitive)<br/><code>column ILIKE 'pattern%'</code></td>
</tr>
<tr>
<td><code>NOT ILIKE</code></td>
<td>true if the string does not match the pattern (case-insensitive)<br/><code>column NOT ILIKE 'pattern%'</code></td>
</tr>
</tbody>
</table>
<p>Pattern matching supports two wildcard characters:</p>
<ul>
<li><code>%</code> matches any sequence of zero or more characters</li>
<li><code>_</code> matches any single character</li>
</ul>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- Match strings starting with &quot;error&quot;&#10;WHERE blob1 LIKE &#x27;error%&#x27;&#10;&#10;&#45;- Match strings ending with &quot;.jpg&quot; (case-insensitive)&#10;WHERE blob2 ILIKE &#x27;%.jpg&#x27;&#10;&#10;&#45;- Match strings containing &quot;test&quot; anywhere&#10;WHERE blob3 LIKE &#x27;%test%&#x27;&#10;&#10;&#45;- Match exactly 5 characters starting with &quot;log&quot;&#10;WHERE blob4 LIKE &#x27;log__&#x27;&#10;&#10;&#45;- Exclude strings containing &quot;debug&quot; (case-insensitive)&#10;WHERE blob5 NOT ILIKE &#x27;%debug%&#x27;&#10;</code></pre>
<h2 id="boolean-operators">Boolean operators</h2>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>AND</code></td>
<td>boolean &quot;AND&quot; (true if both sides are true)</td>
</tr>
<tr>
<td><code>OR</code></td>
<td>boolean &quot;OR&quot; (true if either side or both sides are true)</td>
</tr>
<tr>
<td><code>NOT</code></td>
<td>boolean &quot;NOT&quot; (true if following expression is false and visa-versa)</td>
</tr>
</tbody>
</table>
<h2 id="unary-operators">Unary operators</h2>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>-</code></td>
<td>negation operator (for example, <code>-42</code>)</td>
</tr>
</tbody>
</table>
