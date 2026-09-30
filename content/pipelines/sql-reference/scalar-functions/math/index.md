---
cp9:
  canonical: https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/math/
  description: Scalar functions for mathematical operations
  full_title: Math functions · Cloudflare Pipelines Docs
  head_html: <title>Math functions · Cloudflare Pipelines Docs</title><meta name="generator" content="Nift"><meta name="description" content="Scalar functions for mathematical operations"><link rel="canonical" href="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/math/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/math/index.md"><meta property="og:title" content="Math functions · Cloudflare Pipelines Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Scalar functions for mathematical operations"><meta property="og:url" content="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/math/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pipelines"><meta name="algolia_product_filter" content="Pipelines"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_additional_products" content="Pipelines"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/math/#page","headline":"Math functions \u00b7 Cloudflare Pipelines Docs","description":"Scalar functions for mathematical operations","url":"https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/math/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pipelines/sql-reference/scalar-functions/math/
  schema: 1
---
<p><em>Cloudflare Pipelines scalar function implementations are based on
<a href="https://arrow.apache.org/datafusion/">Apache DataFusion</a> (via <a href="https://www.arroyo.dev/">Arroyo</a>) and these docs are derived from
the DataFusion function reference.</em></p>
<h2 id="abs"><code>abs</code></h2>
<p>Returns the absolute value of a number.</p>
<pre tabindex="0"><code>abs(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="acos"><code>acos</code></h2>
<p>Returns the arc cosine or inverse cosine of a number.</p>
<pre tabindex="0"><code>acos(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="acosh"><code>acosh</code></h2>
<p>Returns the area hyperbolic cosine or inverse hyperbolic cosine of a number.</p>
<pre tabindex="0"><code>acosh(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="asin"><code>asin</code></h2>
<p>Returns the arc sine or inverse sine of a number.</p>
<pre tabindex="0"><code>asin(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="asinh"><code>asinh</code></h2>
<p>Returns the area hyperbolic sine or inverse hyperbolic sine of a number.</p>
<pre tabindex="0"><code>asinh(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="atan"><code>atan</code></h2>
<p>Returns the arc tangent or inverse tangent of a number.</p>
<pre tabindex="0"><code>atan(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="atanh"><code>atanh</code></h2>
<p>Returns the area hyperbolic tangent or inverse hyperbolic tangent of a number.</p>
<pre tabindex="0"><code>atanh(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="atan2"><code>atan2</code></h2>
<p>Returns the arc tangent or inverse tangent of <code>expression_y / expression_x</code>.</p>
<pre tabindex="0"><code>atan2(expression_y, expression_x)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression_y</strong>: First numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>expression_x</strong>: Second numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="cbrt"><code>cbrt</code></h2>
<p>Returns the cube root of a number.</p>
<pre tabindex="0"><code>cbrt(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="ceil"><code>ceil</code></h2>
<p>Returns the nearest integer greater than or equal to a number.</p>
<pre tabindex="0"><code>ceil(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="cos"><code>cos</code></h2>
<p>Returns the cosine of a number.</p>
<pre tabindex="0"><code>cos(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="cosh"><code>cosh</code></h2>
<p>Returns the hyperbolic cosine of a number.</p>
<pre tabindex="0"><code>cosh(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="degrees"><code>degrees</code></h2>
<p>Converts radians to degrees.</p>
<pre tabindex="0"><code>degrees(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="exp"><code>exp</code></h2>
<p>Returns the base-e exponential of a number.</p>
<pre tabindex="0"><code>exp(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to use as the exponent.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="factorial"><code>factorial</code></h2>
<p>Factorial. Returns 1 if value is less than 2.</p>
<pre tabindex="0"><code>factorial(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="floor"><code>floor</code></h2>
<p>Returns the nearest integer less than or equal to a number.</p>
<pre tabindex="0"><code>floor(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="gcd"><code>gcd</code></h2>
<p>Returns the greatest common divisor of <code>expression_x</code> and <code>expression_y</code>. Returns 0 if both inputs are zero.</p>
<pre tabindex="0"><code>gcd(expression_x, expression_y)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression_x</strong>: First numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>expression_y</strong>: Second numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="isnan"><code>isnan</code></h2>
<p>Returns true if a given number is +NaN or -NaN otherwise returns false.</p>
<pre tabindex="0"><code>isnan(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="iszero"><code>iszero</code></h2>
<p>Returns true if a given number is +0.0 or -0.0 otherwise returns false.</p>
<pre tabindex="0"><code>iszero(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="lcm"><code>lcm</code></h2>
<p>Returns the least common multiple of <code>expression_x</code> and <code>expression_y</code>. Returns 0 if either input is zero.</p>
<pre tabindex="0"><code>lcm(expression_x, expression_y)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression_x</strong>: First numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>expression_y</strong>: Second numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="ln"><code>ln</code></h2>
<p>Returns the natural logarithm of a number.</p>
<pre tabindex="0"><code>ln(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="log"><code>log</code></h2>
<p>Returns the base-x logarithm of a number.
Can either provide a specified base, or if omitted then takes the base-10 of a number.</p>
<pre tabindex="0"><code>log(base, numeric_expression)&#10;log(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>base</strong>: Base numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="log10"><code>log10</code></h2>
<p>Returns the base-10 logarithm of a number.</p>
<pre tabindex="0"><code>log10(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="log2"><code>log2</code></h2>
<p>Returns the base-2 logarithm of a number.</p>
<pre tabindex="0"><code>log2(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="nanvl"><code>nanvl</code></h2>
<p>Returns the first argument if it's not <em>NaN</em>.
Returns the second argument otherwise.</p>
<pre tabindex="0"><code>nanvl(expression_x, expression_y)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression_x</strong>: Numeric expression to return if it's not <em>NaN</em>.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>expression_y</strong>: Numeric expression to return if the first expression is <em>NaN</em>.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="pi"><code>pi</code></h2>
<p>Returns an approximate value of π.</p>
<pre tabindex="0"><code>pi()&#10;</code></pre>
<h2 id="power"><code>power</code></h2>
<p>Returns a base expression raised to the power of an exponent.</p>
<pre tabindex="0"><code>power(base, exponent)&#10;</code></pre>
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
<pre tabindex="0"><code>radians(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="random"><code>random</code></h2>
<p>Returns a random float value in the range [0, 1).
The random seed is unique to each row.</p>
<pre tabindex="0"><code>random()&#10;</code></pre>
<h2 id="round"><code>round</code></h2>
<p>Rounds a number to the nearest integer.</p>
<pre tabindex="0"><code>round(numeric_expression[, decimal_places])&#10;</code></pre>
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
<pre tabindex="0"><code>signum(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="sin"><code>sin</code></h2>
<p>Returns the sine of a number.</p>
<pre tabindex="0"><code>sin(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="sinh"><code>sinh</code></h2>
<p>Returns the hyperbolic sine of a number.</p>
<pre tabindex="0"><code>sinh(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="sqrt"><code>sqrt</code></h2>
<p>Returns the square root of a number.</p>
<pre tabindex="0"><code>sqrt(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="tan"><code>tan</code></h2>
<p>Returns the tangent of a number.</p>
<pre tabindex="0"><code>tan(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="tanh"><code>tanh</code></h2>
<p>Returns the hyperbolic tangent of a number.</p>
<pre tabindex="0"><code>tanh(numeric_expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>numeric_expression</strong>: Numeric expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="trunc"><code>trunc</code></h2>
<p>Truncates a number to a whole number or truncated to the specified decimal places.</p>
<pre tabindex="0"><code>trunc(numeric_expression[, decimal_places])&#10;</code></pre>
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
