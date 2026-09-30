<p><em>Cloudflare Pipelines scalar function implementations are based on
<a href="https://arrow.apache.org/datafusion/">Apache DataFusion</a> (via <a href="https://www.arroyo.dev/">Arroyo</a>) and these docs are derived from
the DataFusion function reference.</em></p>
<p>Cloudflare Pipelines uses a
<a href="https://en.wikibooks.org/wiki/Regular_Expressions/Perl-Compatible_Regular_Expressions">PCRE-like</a>
regular expression <a href="https://docs.rs/regex/latest/regex/#syntax">syntax</a> (minus support for several features including
look-around and backreferences).</p>
<h2 id="regexp-like"><code>regexp_like</code></h2>
<p>Returns true if a <a href="https://docs.rs/regex/latest/regex/#syntax">regular expression</a> has at least one match in a string,
false otherwise.</p>
<pre><code>regexp_like(str, regexp[, flags])&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>regexp</strong>: Regular expression to test against the string expression.
Can be a constant, column, or function.</li>
<li><strong>flags</strong>: Optional regular expression flags that control the behavior of the
regular expression. The following flags are supported:
<ul>
<li><strong>i</strong>: case-insensitive: letters match both upper and lower case</li>
<li><strong>m</strong>: multi-line mode: ^ and $ match begin/end of line</li>
<li><strong>s</strong>: allow . to match \n</li>
<li><strong>R</strong>: enables CRLF mode: when multi-line mode is enabled, \r\n is used</li>
<li><strong>U</strong>: swap the meaning of x* and x*?</li>
</ul>
</li>
</ul>
<p><strong>Example</strong></p>
<pre><code class="language-sql">select regexp_like(&#x27;Köln&#x27;, &#x27;[a-zA-Z]ö[a-zA-Z]{2}&#x27;);&#10;&#43;--------------------------------------------------------+&#10;| regexp_like(Utf8(&quot;Köln&quot;),Utf8(&quot;[a-zA-Z]ö[a-zA-Z]{2}&quot;)) |&#10;&#43;--------------------------------------------------------+&#10;| true                                                   |&#10;&#43;--------------------------------------------------------+&#10;SELECT regexp_like(&#x27;aBc&#x27;, &#x27;(b|d)&#x27;, &#x27;i&#x27;);&#10;&#43;--------------------------------------------------+&#10;| regexp_like(Utf8(&quot;aBc&quot;),Utf8(&quot;(b|d)&quot;),Utf8(&quot;i&quot;)) |&#10;&#43;--------------------------------------------------+&#10;| true                                             |&#10;&#43;--------------------------------------------------+&#10;</code></pre>
<p>Additional examples can be found <a href="https://github.com/apache/datafusion/blob/main/datafusion-examples/examples/regexp.rs">here</a></p>
<h2 id="regexp-match"><code>regexp_match</code></h2>
<p>Returns a list of <a href="https://docs.rs/regex/latest/regex/#syntax">regular expression</a> matches in a string.</p>
<pre><code>regexp_match(str, regexp[, flags])&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>regexp</strong>: Regular expression to match against.
Can be a constant, column, or function.</li>
<li><strong>flags</strong>: Optional regular expression flags that control the behavior of the
regular expression. The following flags are supported:
<ul>
<li><strong>i</strong>: case-insensitive: letters match both upper and lower case</li>
<li><strong>m</strong>: multi-line mode: ^ and $ match begin/end of line</li>
<li><strong>s</strong>: allow . to match \n</li>
<li><strong>R</strong>: enables CRLF mode: when multi-line mode is enabled, \r\n is used</li>
<li><strong>U</strong>: swap the meaning of x* and x*?</li>
</ul>
</li>
</ul>
<p><strong>Example</strong></p>
<pre><code class="language-sql">select regexp_match(&#x27;Köln&#x27;, &#x27;[a-zA-Z]ö[a-zA-Z]{2}&#x27;);&#10;&#43;---------------------------------------------------------+&#10;| regexp_match(Utf8(&quot;Köln&quot;),Utf8(&quot;[a-zA-Z]ö[a-zA-Z]{2}&quot;)) |&#10;&#43;---------------------------------------------------------+&#10;| [Köln]                                                  |&#10;&#43;---------------------------------------------------------+&#10;SELECT regexp_match(&#x27;aBc&#x27;, &#x27;(b|d)&#x27;, &#x27;i&#x27;);&#10;&#43;---------------------------------------------------+&#10;| regexp_match(Utf8(&quot;aBc&quot;),Utf8(&quot;(b|d)&quot;),Utf8(&quot;i&quot;)) |&#10;&#43;---------------------------------------------------+&#10;| [B]                                               |&#10;&#43;---------------------------------------------------+&#10;</code></pre>
<p>Additional examples can be found <a href="https://github.com/apache/datafusion/blob/main/datafusion-examples/examples/regexp.rs">here</a></p>
<h2 id="regexp-replace"><code>regexp_replace</code></h2>
<p>Replaces substrings in a string that match a <a href="https://docs.rs/regex/latest/regex/#syntax">regular expression</a>.</p>
<pre><code>regexp_replace(str, regexp, replacement[, flags])&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>regexp</strong>: Regular expression to match against.
Can be a constant, column, or function.</li>
<li><strong>replacement</strong>: Replacement string expression.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>flags</strong>: Optional regular expression flags that control the behavior of the
regular expression. The following flags are supported:
<ul>
<li><strong>g</strong>: (global) Search globally and don't return after the first match</li>
<li><strong>i</strong>: case-insensitive: letters match both upper and lower case</li>
<li><strong>m</strong>: multi-line mode: ^ and $ match begin/end of line</li>
<li><strong>s</strong>: allow . to match \n</li>
<li><strong>R</strong>: enables CRLF mode: when multi-line mode is enabled, \r\n is used</li>
<li><strong>U</strong>: swap the meaning of x* and x*?</li>
</ul>
</li>
</ul>
<p><strong>Example</strong></p>
<pre><code class="language-sql">SELECT regexp_replace(&#x27;foobarbaz&#x27;, &#x27;b(..)&#x27;, &#x27;X\\1Y&#x27;, &#x27;g&#x27;);&#10;&#43;------------------------------------------------------------------------+&#10;| regexp_replace(Utf8(&quot;foobarbaz&quot;),Utf8(&quot;b(..)&quot;),Utf8(&quot;X\1Y&quot;),Utf8(&quot;g&quot;)) |&#10;&#43;------------------------------------------------------------------------+&#10;| fooXarYXazY                                                            |&#10;&#43;------------------------------------------------------------------------+&#10;SELECT regexp_replace(&#x27;aBc&#x27;, &#x27;(b|d)&#x27;, &#x27;Ab\\1a&#x27;, &#x27;i&#x27;);&#10;&#43;-------------------------------------------------------------------+&#10;| regexp_replace(Utf8(&quot;aBc&quot;),Utf8(&quot;(b|d)&quot;),Utf8(&quot;Ab\1a&quot;),Utf8(&quot;i&quot;)) |&#10;&#43;-------------------------------------------------------------------+&#10;| aAbBac                                                            |&#10;&#43;-------------------------------------------------------------------+&#10;</code></pre>
<p>Additional examples can be found <a href="https://github.com/apache/datafusion/blob/main/datafusion-examples/examples/regexp.rs">here</a></p>
<h2 id="position"><code>position</code></h2>
<p>Returns the position of <code>substr</code> in <code>origstr</code> (counting from 1). If <code>substr</code> does
not appear in <code>origstr</code>, return 0.</p>
<pre><code>position(substr in origstr)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>substr</strong>: The pattern string.</li>
<li><strong>origstr</strong>: The model string.</li>
</ul>
