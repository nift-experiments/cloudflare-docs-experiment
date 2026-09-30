<p><em>Cloudflare Pipelines scalar function implementations are based on
<a href="https://arrow.apache.org/datafusion/">Apache DataFusion</a> (via <a href="https://www.arroyo.dev/">Arroyo</a>) and these docs are derived from
the DataFusion function reference.</em></p>
<h2 id="struct"><code>struct</code></h2>
<p>Returns an Arrow struct using the specified input expressions.
Fields in the returned struct use the <code>cN</code> naming convention.
For example: <code>c0</code>, <code>c1</code>, <code>c2</code>, etc.</p>
<pre><code>struct(expression1[, ..., expression_n])&#10;</code></pre>
<p>For example, this query converts two columns <code>a</code> and <code>b</code> to a single column with
a struct type of fields <code>c0</code> and <code>c1</code>:</p>
<pre><code>select * from t;&#10;&#43;---+---+&#10;| a | b |&#10;&#43;---+---+&#10;| 1 | 2 |&#10;| 3 | 4 |&#10;&#43;---+---+&#10;&#10;select struct(a, b) from t;&#10;&#43;-----------------+&#10;| struct(t.a,t.b) |&#10;&#43;-----------------+&#10;| {c0: 1, c1: 2}  |&#10;| {c0: 3, c1: 4}  |&#10;&#43;-----------------+&#10;</code></pre>
<h4 id="arguments">Arguments</h4>
<ul>
<li><strong>expression_n</strong>: Expression to include in the output struct.
Can be a constant, column, or function, and any combination of arithmetic or
string operators.</li>
</ul>
