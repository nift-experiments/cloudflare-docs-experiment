<p><em>Cloudflare Pipelines scalar function implementations are based on
<a href="https://arrow.apache.org/datafusion/">Apache DataFusion</a> (via <a href="https://www.arroyo.dev/">Arroyo</a>) and these docs are derived from
the DataFusion function reference.</em></p>
<h2 id="coalesce"><code>coalesce</code></h2>
<p>Returns the first of its arguments that is not <em>null</em>.
Returns <em>null</em> if all arguments are <em>null</em>.
This function is often used to substitute a default value for <em>null</em> values.</p>
<pre><code>coalesce(expression1[, ..., expression_n])&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression1, expression_n</strong>:
Expression to use if previous expressions are <em>null</em>.
Can be a constant, column, or function, and any combination of arithmetic operators.
Pass as many expression arguments as necessary.</li>
</ul>
<h2 id="nullif"><code>nullif</code></h2>
<p>Returns <em>null</em> if <em>expression1</em> equals <em>expression2</em>; otherwise it returns <em>expression1</em>.
This can be used to perform the inverse operation of <a href="#coalesce"><code>coalesce</code></a>.</p>
<pre><code>nullif(expression1, expression2)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression1</strong>: Expression to compare and return if equal to expression2.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>expression2</strong>: Expression to compare to expression1.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="nvl"><code>nvl</code></h2>
<p>Returns <em>expression2</em> if <em>expression1</em> is NULL; otherwise it returns <em>expression1</em>.</p>
<pre><code>nvl(expression1, expression2)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression1</strong>: return if expression1 not is NULL.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>expression2</strong>: return if expression1 is NULL.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="nvl2"><code>nvl2</code></h2>
<p>Returns <em>expression2</em> if <em>expression1</em> is not NULL; otherwise it returns <em>expression3</em>.</p>
<pre><code>nvl2(expression1, expression2, expression3)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression1</strong>: conditional expression.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>expression2</strong>: return if expression1 is not NULL.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>expression3</strong>: return if expression1 is NULL.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="ifnull"><code>ifnull</code></h2>
<p><em>Alias of <a href="#nvl">nvl</a>.</em></p>
