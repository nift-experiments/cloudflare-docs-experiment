<p><em>Cloudflare Pipelines scalar function implementations are based on
<a href="https://arrow.apache.org/datafusion/">Apache DataFusion</a> (via <a href="https://www.arroyo.dev/">Arroyo</a>) and these docs are derived from
the DataFusion function reference.</em></p>
<h2 id="arrow-cast"><code>arrow_cast</code></h2>
<p>Casts a value to a specific Arrow data type:</p>
<pre><code>arrow_cast(expression, datatype)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression</strong>: Expression to cast.
Can be a constant, column, or function, and any combination of arithmetic or
string operators.</li>
<li><strong>datatype</strong>: <a href="https://docs.rs/arrow/latest/arrow/datatypes/enum.DataType.html">Arrow data type</a> name
to cast to, as a string. The format is the same as that returned by [<code>arrow_typeof</code>]</li>
</ul>
<p><strong>Example</strong></p>
<pre><code>&gt; select arrow_cast(-5, &#x27;Int8&#x27;) as a,&#10;  arrow_cast(&#x27;foo&#x27;, &#x27;Dictionary(Int32, Utf8)&#x27;) as b,&#10;  arrow_cast(&#x27;bar&#x27;, &#x27;LargeUtf8&#x27;) as c,&#10;  arrow_cast(&#x27;2023-01-02T12:53:02&#x27;, &#x27;Timestamp(Microsecond, Some(&quot;+08:00&quot;))&#x27;) as d&#10;  ;&#10;&#43;----+-----+-----+---------------------------+&#10;| a  | b   | c   | d                         |&#10;&#43;----+-----+-----+---------------------------+&#10;| -5 | foo | bar | 2023-01-02T12:53:02+08:00 |&#10;&#43;----+-----+-----+---------------------------+&#10;1 row in set. Query took 0.001 seconds.&#10;</code></pre>
<h2 id="arrow-typeof"><code>arrow_typeof</code></h2>
<p>Returns the name of the underlying <a href="https://docs.rs/arrow/latest/arrow/datatypes/enum.DataType.html">Arrow data type</a> of the expression:</p>
<pre><code>arrow_typeof(expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression</strong>: Expression to evaluate.
Can be a constant, column, or function, and any combination of arithmetic or
string operators.</li>
</ul>
<p><strong>Example</strong></p>
<pre><code>&gt; select arrow_typeof(&#x27;foo&#x27;), arrow_typeof(1);&#10;&#43;---------------------------+------------------------+&#10;| arrow_typeof(Utf8(&quot;foo&quot;)) | arrow_typeof(Int64(1)) |&#10;&#43;---------------------------+------------------------+&#10;| Utf8                      | Int64                  |&#10;&#43;---------------------------+------------------------+&#10;1 row in set. Query took 0.001 seconds.&#10;</code></pre>
