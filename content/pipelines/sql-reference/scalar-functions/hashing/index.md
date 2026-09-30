<p><em>Cloudflare Pipelines scalar function implementations are based on
<a href="https://arrow.apache.org/datafusion/">Apache DataFusion</a> (via <a href="https://www.arroyo.dev/">Arroyo</a>) and these docs are derived from
the DataFusion function reference.</em></p>
<h2 id="digest"><code>digest</code></h2>
<p>Computes the binary hash of an expression using the specified algorithm.</p>
<pre><code>digest(expression, algorithm)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>algorithm</strong>: String expression specifying algorithm to use.
Must be one of:
<ul>
<li>md5</li>
<li>sha224</li>
<li>sha256</li>
<li>sha384</li>
<li>sha512</li>
<li>blake2s</li>
<li>blake2b</li>
<li>blake3</li>
</ul>
</li>
</ul>
<h2 id="md5"><code>md5</code></h2>
<p>Computes an MD5 128-bit checksum for a string expression.</p>
<pre><code>md5(expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
</ul>
<h2 id="sha224"><code>sha224</code></h2>
<p>Computes the SHA-224 hash of a binary string.</p>
<pre><code>sha224(expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
</ul>
<h2 id="sha256"><code>sha256</code></h2>
<p>Computes the SHA-256 hash of a binary string.</p>
<pre><code>sha256(expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
</ul>
<h2 id="sha384"><code>sha384</code></h2>
<p>Computes the SHA-384 hash of a binary string.</p>
<pre><code>sha384(expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
</ul>
<h2 id="sha512"><code>sha512</code></h2>
<p>Computes the SHA-512 hash of a binary string.</p>
<pre><code>sha512(expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
</ul>
