<h2 id="bitand">bitAnd <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">bitAnd(a, b)&#10;</code></pre>
<p><code>bitAnd</code> returns the bitwise AND of expressions <code>a</code> and <code>b</code>.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- perform 0b1 &amp; 0b11&#10;bitAnd(1, 3)&#10;&#45;- extract the least significant bit of the integer value of double1&#10;bitAnd(toUInt8(double1), 1)&#10;</code></pre>
<h2 id="bitcount">bitCount <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">bitCount(a)&#10;</code></pre>
<p><code>bitCount</code> returns the number of bits set to one in the binary representation of <code>a</code>.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- get the number of 1 bits in the binary representation of the float `double1`&#10;bitCount(double1)&#10;&#45;- get the number of 1 bits in the binary representation of `double1` as an integer&#10;bitCount(toUInt32(double1))&#10;&#45;- select rows where at least 5 bits are 1&#10;SELECT * WHERE bitCount(double1) &gt; 5&#10;</code></pre>
<h2 id="bithammingdistance">bitHammingDistance <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">bitHammingDistance(x, y)&#10;</code></pre>
<p><code>bitHammingDistance</code> returns the number of bits that differ between <code>x</code> and <code>y</code>.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- returns zero&#10;bitHammingDistance(1, 1)&#10;&#45;- returns 2&#10;bitHammingDistance(3, 0)&#10;</code></pre>
<h2 id="bitnot">bitNot <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">bitNot(a)&#10;</code></pre>
<p><code>bitNot</code> returns <code>a</code> with all bits flipped.</p>
<p>Examples:</p>
<pre><code class="language-sql">bitNot(1)&#10;</code></pre>
<h2 id="bitor">bitOr <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">bitOr(a, b)&#10;</code></pre>
<p><code>bitOr</code> returns the inclusive bitwise or of <code>a</code> and <code>b</code>.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- returns 3&#10;bitOr(1, 2)&#10;</code></pre>
<h2 id="bitrotateleft">bitRotateLeft <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">bitRotateLeft(a, n)&#10;</code></pre>
<p><code>bitRotateLeft</code> rotates all bits in <code>a</code> left by <code>n</code> positions.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- returns 2&#10;bitRotateLeft(1, 1)&#10;&#45;- returns 1&#10;bitRotateLeft(128, 1)&#10;</code></pre>
<h2 id="bitrotateright">bitRotateRight <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">bitRotateRight(a, n)&#10;</code></pre>
<p><code>bitRotateRight</code> rotates all bits in <code>a</code> right by <code>n</code> positions.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- returns 128&#10;bitRotateRight(1, 1)&#10;&#45;- returns 3&#10;bitRotateRight(12, 2)&#10;</code></pre>
<h2 id="bitshiftleft">bitShiftLeft <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">bitShiftLeft(a, n)&#10;</code></pre>
<p><code>bitShiftLeft</code> shifts all bits in <code>a</code> left by <code>n</code> positions.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- returns 2&#10;bitShiftLeft(1, 1)&#10;&#45;- returns 0&#10;bitShiftLeft(128, 1)&#10;</code></pre>
<h2 id="bitshiftright">bitShiftRight <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">bitShiftRight(a, n)&#10;</code></pre>
<p><code>bitShiftRight</code> shifts all bits in <code>a</code> right by <code>n</code> positions.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- returns 0&#10;bitShiftRight(1, 1)&#10;&#45;- returns 3&#10;bitShiftRight(12, 2)&#10;</code></pre>
<h2 id="bittest">bitTest <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">bitTest(a, n)&#10;</code></pre>
<p><code>bitTest</code> returns the value of bit <code>n</code> in number <code>a</code>.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- returns 1&#10;bitTest(3, 1)&#10;&#45;- return 0&#10;bitTest(2, 1)&#10;&#45;- select rows where a particular bit is 1&#10;SELECT * WHERE bitTest(double1, 2)&#10;</code></pre>
<h2 id="bitxor">bitXor <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">bitXor(a, b)&#10;</code></pre>
<p><code>bitXor</code> returns the bitwise exclusive-or of <code>a</code> and <code>b</code>.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- returns 3&#10;bitXor(1, 2)&#10;&#45;- returns 0&#10;bitXor(3, 3)&#10;</code></pre>
