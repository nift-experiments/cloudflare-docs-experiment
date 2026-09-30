<p><em>Cloudflare Pipelines scalar function implementations are based on
<a href="https://arrow.apache.org/datafusion/">Apache DataFusion</a> (via <a href="https://www.arroyo.dev/">Arroyo</a>) and these docs are derived from
the DataFusion function reference.</em></p>
<h2 id="abs"><code>abs</code></h2>
<p>Returns the absolute value of a number.</p>
<pre><code>abs(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="acos"><code>acos</code></h2>
<p>Returns the arc cosine or inverse cosine of a number.</p>
<pre><code>acos(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="acosh"><code>acosh</code></h2>
<p>Returns the area hyperbolic cosine or inverse hyperbolic cosine of a number.</p>
<pre><code>acosh(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="asin"><code>asin</code></h2>
<p>Returns the arc sine or inverse sine of a number.</p>
<pre><code>asin(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="asinh"><code>asinh</code></h2>
<p>Returns the area hyperbolic sine or inverse hyperbolic sine of a number.</p>
<pre><code>asinh(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="atan"><code>atan</code></h2>
<p>Returns the arc tangent or inverse tangent of a number.</p>
<pre><code>atan(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="atanh"><code>atanh</code></h2>
<p>Returns the area hyperbolic tangent or inverse hyperbolic tangent of a number.</p>
<pre><code>atanh(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="atan2"><code>atan2</code></h2>
<p>Returns the arc tangent or inverse tangent of <code>expression_y / expression_x</code>.</p>
<pre><code>atan2(expression_y, expression_x)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression_y</strong>: First numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>expression_x</strong>: Second numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="cbrt"><code>cbrt</code></h2>
<p>Returns the cube root of a number.</p>
<pre><code>cbrt(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="ceil"><code>ceil</code></h2>
<p>Returns the nearest integer greater than or equal to a number.</p>
<pre><code>ceil(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="cos"><code>cos</code></h2>
<p>Returns the cosine of a number.</p>
<pre><code>cos(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="cosh"><code>cosh</code></h2>
<p>Returns the hyperbolic cosine of a number.</p>
<pre><code>cosh(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="degrees"><code>degrees</code></h2>
<p>Converts radians to degrees.</p>
<pre><code>degrees(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="exp"><code>exp</code></h2>
<p>Returns the base-e exponential of a number.</p>
<pre><code>exp(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to use as the exponent.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="factorial"><code>factorial</code></h2>
<p>Factorial. Returns 1 if value is less than 2.</p>
<pre><code>factorial(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="floor"><code>floor</code></h2>
<p>Returns the nearest integer less than or equal to a number.</p>
<pre><code>floor(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="gcd"><code>gcd</code></h2>
<p>Returns the greatest common divisor of <code>expression_x</code> and <code>expression_y</code>. Returns 0 if both inputs are zero.</p>
<pre><code>gcd(expression_x, expression_y)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression_x</strong>: First numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>expression_y</strong>: Second numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="isnan"><code>isnan</code></h2>
<p>Returns true if a given number is +NaN or -NaN otherwise returns false.</p>
<pre><code>isnan(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="iszero"><code>iszero</code></h2>
<p>Returns true if a given number is +0.0 or -0.0 otherwise returns false.</p>
<pre><code>iszero(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="lcm"><code>lcm</code></h2>
<p>Returns the least common multiple of <code>expression_x</code> and <code>expression_y</code>. Returns 0 if either input is zero.</p>
<pre><code>lcm(expression_x, expression_y)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression_x</strong>: First numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>expression_y</strong>: Second numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="ln"><code>ln</code></h2>
<p>Returns the natural logarithm of a number.</p>
<pre><code>ln(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="log"><code>log</code></h2>
<p>Returns the base-x logarithm of a number.
Can either provide a specified base, or if omitted then takes the base-10 of a number.</p>
<pre><code>log(base, numeric_expression)&#10;log(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>base</strong>: Base numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="log10"><code>log10</code></h2>
<p>Returns the base-10 logarithm of a number.</p>
<pre><code>log10(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="log2"><code>log2</code></h2>
<p>Returns the base-2 logarithm of a number.</p>
<pre><code>log2(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="nanvl"><code>nanvl</code></h2>
<p>Returns the first argument if it's not <em>NaN</em>.
Returns the second argument otherwise.</p>
<pre><code>nanvl(expression_x, expression_y)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression_x</strong>: Numeric expression to return if it's not <em>NaN</em>.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>expression_y</strong>: Numeric expression to return if the first expression is <em>NaN</em>.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="pi"><code>pi</code></h2>
<p>Returns an approximate value of π.</p>
<pre><code>pi()&#10;</code></pre>
<h2 id="power"><code>power</code></h2>
<p>Returns a base expression raised to the power of an exponent.</p>
<pre><code>power(base, exponent)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>base</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>exponent</strong>: Exponent numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<p><strong>Aliases</strong></p>
<ul>
<li>pow</li>
</ul>
<h2 id="pow"><code>pow</code></h2>
<p><em>Alias of <a href="#power">power</a>.</em></p>
<h2 id="radians"><code>radians</code></h2>
<p>Converts degrees to radians.</p>
<pre><code>radians(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="random"><code>random</code></h2>
<p>Returns a random float value in the range [0, 1).
The random seed is unique to each row.</p>
<pre><code>random()&#10;</code></pre>
<h2 id="round"><code>round</code></h2>
<p>Rounds a number to the nearest integer.</p>
<pre><code>round(numeric_expression[, decimal_places])&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>decimal_places</strong>: Optional. The number of decimal places to round to.
Defaults to 0.</li>
</ul>
<h2 id="signum"><code>signum</code></h2>
<p>Returns the sign of a number.
Negative numbers return <code>-1</code>.
Zero and positive numbers return <code>1</code>.</p>
<pre><code>signum(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="sin"><code>sin</code></h2>
<p>Returns the sine of a number.</p>
<pre><code>sin(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="sinh"><code>sinh</code></h2>
<p>Returns the hyperbolic sine of a number.</p>
<pre><code>sinh(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="sqrt"><code>sqrt</code></h2>
<p>Returns the square root of a number.</p>
<pre><code>sqrt(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="tan"><code>tan</code></h2>
<p>Returns the tangent of a number.</p>
<pre><code>tan(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="tanh"><code>tanh</code></h2>
<p>Returns the hyperbolic tangent of a number.</p>
<pre><code>tanh(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="trunc"><code>trunc</code></h2>
<p>Truncates a number to a whole number or truncated to the specified decimal places.</p>
<pre><code>trunc(numeric_expression[, decimal_places])&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li>
<p><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</p>
</li>
<li>
<p><strong>decimal_places</strong>: Optional. The number of decimal places to
truncate to. Defaults to 0 (truncate to a whole number). If
<code>decimal_places</code> is a positive integer, truncates digits to the
right of the decimal point. If <code>decimal_places</code> is a negative
integer, replaces digits to the left of the decimal point with <code>0</code>.</p>
</li>
</ul>
