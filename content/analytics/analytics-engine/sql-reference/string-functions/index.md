<h2 id="length">length</h2>
<p>Usage:</p>
<pre><code class="language-sql">length({string})&#10;</code></pre>
<p>Returns the length of a string. This function is UTF-8 compatible.</p>
<p>Examples:</p>
<pre><code class="language-sql">SELECT length(&#x27;a string&#x27;) AS s;&#10;SELECT length(blob1) AS s FROM your_dataset;&#10;</code></pre>
<p>For backwards-compatibility, this function is the equivalent of ClickHouse's <code>lengthUTF8</code> function, rather than ClickHouse's <code>length</code> function.</p>
<h2 id="empty">empty</h2>
<p>Usage:</p>
<pre><code class="language-sql">empty({string})&#10;</code></pre>
<p>Returns a boolean saying whether the string was empty. This computation can also be done as a binary operation: <code>{string} = ''</code>.</p>
<p>Examples:</p>
<pre><code class="language-sql">SELECT empty(&#x27;a string&#x27;) AS b;&#10;SELECT empty(blob1) AS b FROM your_dataset;&#10;</code></pre>
<p>For backwards compatibility, this function can also be called using <code>empty(&lt;string&gt;)</code>.</p>
<h2 id="lower">lower</h2>
<p>Usage:</p>
<pre><code class="language-sql">lower({string})&#10;</code></pre>
<p>Returns the string converted to lowercase. This function is NOT Unicode compatible - refer to <code>lowerUTF8</code> for that.</p>
<p>Examples:</p>
<pre><code class="language-sql">SELECT lower(&#x27;STRING TO DOWNCASE&#x27;) AS s;&#10;SELECT lower(blob1) AS s FROM your_dataset;&#10;</code></pre>
<h2 id="lowerutf8">lowerUTF8 <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">lowerUTF8({string})&#10;</code></pre>
<p>Returns the string converted to lowercase. This function is Unicode compatible. This may not be perfect for all languages and users with stringent needs, should do the operation in their own code.</p>
<p>Examples:</p>
<pre><code class="language-sql">SELECT lowerUTF8(&#x27;STRING TO DOWNCASE&#x27;) AS s;&#10;SELECT lowerUTF8(blob1) AS s FROM your_dataset;&#10;</code></pre>
<p>For backwards compatibility, this function can also be called using <code>toLower({string})</code>.</p>
<h2 id="upper">upper</h2>
<p>Usage:</p>
<pre><code class="language-sql">upper({string})&#10;</code></pre>
<p>Returns the string converted to uppercase. This function is NOT Unicode compatible - refer to <code>upperUTF8</code> for that.</p>
<p>Examples:</p>
<pre><code class="language-sql">SELECT upper(&#x27;string to uppercase&#x27;) AS s;&#10;SELECT upper(blob1) AS s FROM your_dataset;&#10;</code></pre>
<h2 id="upperutf8">upperUTF8 <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">upperUTF8({string})&#10;</code></pre>
<p>Returns the string converted to uppercase. This function is Unicode compatible. The results may not be perfect for all languages and users with strict needs. These users should do the operation in their own code.</p>
<p>Examples:</p>
<pre><code class="language-sql">SELECT upperUTF8(&#x27;string to uppercase&#x27;) AS s;&#10;SELECT upperUTF8(blob1) AS s FROM your_dataset;&#10;</code></pre>
<p>For backwards compatibility, this function can also be called using <code>toUpper({string})</code>.</p>
<h2 id="startswith">startsWith</h2>
<p>Usage:</p>
<pre><code class="language-sql">startsWith({string}, {string})&#10;</code></pre>
<p>Returns a boolean of whether the first string has the second string at its start.</p>
<p>Examples:</p>
<pre><code class="language-sql">SELECT startsWith(&#x27;prefix ...&#x27;, &#x27;prefix&#x27;) AS b;&#10;SELECT startsWith(blob1, &#x27;prefix&#x27;) AS b FROM your_dataset;&#10;</code></pre>
<h2 id="endswith">endsWith</h2>
<p>Usage:</p>
<pre><code class="language-sql">endsWith({string}, {string})&#10;</code></pre>
<p>Returns a boolean of whether the first string contains the second string at its end.</p>
<p>Examples:</p>
<pre><code class="language-sql">SELECT endsWith(&#x27;prefix suffix&#x27;, &#x27;suffix&#x27;) AS b;&#10;SELECT endsWith(blob1, &#x27;suffix&#x27;) AS b FROM your_dataset;&#10;</code></pre>
<h2 id="position">position</h2>
<p>Usage:</p>
<pre><code class="language-sql">position({needle:string} IN {haystack:string})&#10;</code></pre>
<p>Returns the position of one string, <code>needle</code>, in another, <code>haystack</code>. In SQL, indexes are usually 1-based. That means that position returns <code>1</code> if your needle is at the start of the haystack. It only returns <code>0</code> if your string is not found.</p>
<p>Examples:</p>
<pre><code class="language-sql">SELECT position(&#x27;:&#x27; IN &#x27;hello: world&#x27;) AS p;&#10;SELECT position(&#x27;:&#x27; IN blob1) AS p FROM your_dataset;&#10;</code></pre>
<h2 id="substring">substring</h2>
<p>Usage:</p>
<pre><code class="language-sql">substring({string}, {offset:integer}[. {length:integer}])&#10;</code></pre>
<p>Extracts part of a string, starting at the Unicode code point indicated by the offset and returning the number of code points requested by the length. As previously mentioned, in SQL, indexes are usually 1-based. That means that the offset provided to substring should be at least <code>1</code>.</p>
<p>Examples:</p>
<pre><code class="language-sql">SELECT substring(&#x27;hello world&#x27;, 6) AS s;&#10;SELECT substring(&#x27;hello: world&#x27;, 1, position(&#x27;:&#x27; IN &#x27;hello: world&#x27;)-1) AS s;&#10;</code></pre>
<h2 id="format">format</h2>
<p>Usage:</p>
<pre><code class="language-sql">format({string}[, ...])&#10;</code></pre>
<p>This function supports formatting strings, integers, floats, datetimes, intervals, etc, except <code>NULL</code>. The function does not support literal <code>{</code> and <code>}</code> characters in the format string.</p>
<p>Examples:</p>
<pre><code class="language-sql">SELECT format(&#x27;blob1: {}&#x27;, blob1) AS s FROM dataset;&#10;</code></pre>
<p>The <a href="/analytics/analytics-engine/sql-reference/date-time-functions/#formatdatetime">formatDateTime</a> function might also be useful.</p>
<h2 id="extract">extract</h2>
<p>Usage:</p>
<pre><code class="language-sql">extract(&lt;time unit&gt; from &lt;datetime&gt;)&#10;</code></pre>
<p><code>extract</code> returns an integer number of time units from a datetime. It supports
<code>YEAR</code>, <code>MONTH</code>, <code>DAY</code>, <code>HOUR</code>, <code>MINUTE</code> and <code>SECOND</code>.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- extract the number of seconds from a timestamp (returns 15 in this example)&#10;extract(SECOND from toDateTime(&#x27;2022-06-06 11:30:15&#x27;))&#10;</code></pre>
