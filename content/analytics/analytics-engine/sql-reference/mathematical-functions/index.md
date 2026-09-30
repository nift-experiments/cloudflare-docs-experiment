<h2 id="intdiv">intDiv</h2>
<p>Usage:</p>
<pre><code class="language-sql">intDiv(a, b)&#10;</code></pre>
<p>Divide <code>a</code> by <code>b</code>, rounding the answer down to the nearest whole number.</p>
<h2 id="log">log <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">log(&lt;expression&gt;)&#10;</code></pre>
<p><code>log</code> returns the natural logarithm of a provided number. <code>ln</code> is also available as an alias.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- get the natural logarithm of the double1 column&#10;log(double1)&#10;</code></pre>
<h2 id="pow">pow <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">pow(&lt;expression&gt;, &lt;expression&gt;)&#10;</code></pre>
<p><code>pow</code> returns the first argument raised to the power of the second argument.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- get the square of the double1 column&#10;pow(double1, 2)&#10;</code></pre>
<h2 id="round">round <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">round(&lt;expression&gt;[, n])&#10;</code></pre>
<p><code>round</code> returns a number rounded to the nearest whole number, or to a given number of decimal points specified by the second argument.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- round 5.5 to 6&#10;round(5.5)&#10;&#45;- round 3.14 to 3.1&#10;round(3.14, 1)&#10;</code></pre>
<h2 id="floor">floor <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">floor(&lt;expression&gt;[, n])&#10;</code></pre>
<p><code>floor</code> returns a number rounded down to a whole number, or rounded down to a given number of decimal points specified by the second argument.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- round down 5.5 to 5&#10;floor(5.5)&#10;&#45;- round down 3.14 to 3.1&#10;floor(3.14, 1)&#10;</code></pre>
<h2 id="ceil">ceil <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">ceil(&lt;expression&gt;[, n])&#10;</code></pre>
<p><code>ceil</code> returns a number rounded up to a whole number, or rounded up to a given number of decimal points specified by the second argument.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- round up 5.5 to 6&#10;ceil(5.5)&#10;&#45;- round up 3.14 to 3.2&#10;ceil(3.14, 1)&#10;</code></pre>
