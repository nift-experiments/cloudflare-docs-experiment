<p><a href="/load-balancing/additional-options/load-balancing-rules/">Load Balancing rules</a> use two kinds of expressions:</p>
<ul>
<li>
<p><a href="#simple-expressions">Simple expressions</a> compare a value from an HTTP request to a value defined in the expression. A simple expression is identified by the presence of a <strong>comparison operator</strong> (<em>equals</em> or <em>less than</em>, for example).</p>
</li>
<li>
<p><a href="#compound-expressions">Compound expressions</a> combine two or more simple expressions into a single expression. Compound expression contains a <strong>logical operator</strong> (<em>and</em>, <em>or</em>, for example). With compound expressions you can tailor rules to specific use cases with a high degree of accuracy and precision.</p>
</li>
</ul>
<hr />
<h2 id="simple-expressions">Simple expressions</h2>
<p>Simple expressions are composed of three elements:</p>
<ol>
<li>A <strong>field</strong> that represents a property of an HTTP request.</li>
<li>A representative <strong>value</strong> for that field which Cloudflare compares to the actual request value.</li>
<li>A <strong>comparison operator</strong>, which specifies how the value defined in the expression must relate to the actual value from the request for the operator to return <code>true</code>.</li>
</ol>
<p>When the comparison operator returns <code>true</code>, the request matches the expression.</p>
<p>This example expression returns true when a request URI path contains <code>/content</code>:</p>
<pre><code class="language-sql">(http.request.uri.path contains &quot;/content&quot;)&#10;</code></pre>
<p>In general, simple expressions use this pattern:</p>
<pre><code class="language-sql">&lt;field&gt; &lt;operator&gt; &lt;value&gt;&#10;</code></pre>
<p>For more details, refer to <a href="/load-balancing/additional-options/load-balancing-rules/reference/">Supported fields and operators</a>.</p>
<hr />
<h2 id="compound-expressions">Compound expressions</h2>
<p>A compound expression uses a <strong>logical operator</strong> (<em>and</em>, <em>or</em>, for example) to combine two or more expressions. Compound expressions allow you to build complex statements within a single expression.</p>
<p>The example expression below returns true when both the HTTP request URI path contains <code>/content</code> and the query string contains <code>webserver</code>:</p>
<pre><code class="language-sql">(http.request.uri.path contains &quot;/content&quot;)&#10;and (http.request.uri.query contains &quot;webserver&quot;)&#10;</code></pre>
<p>In general, compound expressions use this pattern:</p>
<pre><code class="language-sql">&lt;expression&gt; &lt;logical operator&gt; &lt;expression&gt;&#10;</code></pre>
<p>A compound expression can be an operand of a logical operator. This allows multiple operators to construct a compound expression from many individual expressions.</p>
<p>For more details, refer to <a href="/load-balancing/additional-options/load-balancing-rules/reference/">Supported fields and operators</a>.</p>
<hr />
<h2 id="working-with-expressions">Working with expressions</h2>
<p>The Expression Builder’s visual interface allows you to build expressions without worrying about field names and syntax.</p>
<p>By comparison, the Expression Editor is text only, but it supports advanced features not available in the builder.</p>
<h3 id="expression-builder">Expression Builder</h3>
<p>Compound expressions are easier to scan when displayed in the Expression Builder’s visual interface, and the Expression Preview is a great reference for learning to write more advanced expressions.</p>
<p>This Expression Builder screenshot shows the example compound expression described earlier. Compound expressions are easier to scan when displayed in the Expression Builder’s visual interface.</p>
<p><img src="/assets/upstream/images/load-balancing/rules-builder-1.png" alt="Example rule configuration visible in the Expression Builder" /></p>
<p>The <strong>Expression Preview</strong> displays the expression in text:</p>
<pre><code class="language-sql">(http.request.uri.path contains &quot;/content&quot;)&#10;and (http.request.uri.query contains &quot;webserver&quot;)&#10;</code></pre>
<p>For a walkthrough, refer to <a href="/load-balancing/additional-options/load-balancing-rules/create-rules/">Creating Load Balancing rules</a>.</p>
<h3 id="expression-editor">Expression Editor</h3>
<p>The Expression Editor is a text-only interface for creating Load Balancing expressions. Although it lacks the visual simplicity of the Expression Builder, the Expression Editor supports advanced features such as support for grouping symbols (parentheses).</p>
<p>To access the Expression Editor in the <strong>Traffic</strong> app, click <strong>Edit expression</strong> in the <strong>Create Custom Rule</strong> dialog.</p>
<p>To return to the builder, click <strong>Use expression builder</strong>.</p>
<h3 id="rules-lists">Rules lists</h3>
<p>Load Balancing Custom Rules does not support IP list operators.</p>
