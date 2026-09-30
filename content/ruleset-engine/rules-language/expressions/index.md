<p>The Rules language supports two kinds of expressions: simple and compound.</p>
<h2 id="simple-expressions">Simple expressions</h2>
<p><strong>Simple expressions</strong> compare a value from an HTTP request to a value defined in the expression. For example, this simple expression matches Microsoft Exchange Autodiscover requests:</p>
<pre><code class="language-txt">http.request.uri.path matches &quot;/autodiscover\.(xml|src)$&quot;&#10;</code></pre>
<p>Simple expressions have the following syntax:</p>
<pre><code class="language-txt">&lt;field&gt; &lt;comparison_operator&gt; &lt;value&gt;&#10;</code></pre>
<p>Where:</p>
<ul>
<li>
<p><a href="/ruleset-engine/rules-language/fields/">Fields</a> specify properties associated with an HTTP request.</p>
</li>
<li>
<p><a href="/ruleset-engine/rules-language/operators/#comparison-operators">Comparison operators</a> define how values must relate to actual request data for an expression to return <code>true</code>.</p>
</li>
<li>
<p><a href="/ruleset-engine/rules-language/values/">Values</a> represent the data associated with fields. When evaluating a rule, Cloudflare compares these values with the actual data obtained from the request.</p>
</li>
</ul>
<h2 id="compound-expressions">Compound expressions</h2>
<p><strong>Compound expressions</strong> use <a href="/ruleset-engine/rules-language/operators/#logical-operators">logical operators</a> such as <code>and</code> to combine two or more expressions into a single expression.</p>
<p>For example, this expression uses the <code>and</code> operator to target requests to <code>www.example.com</code> that are not on ports 80 or 443:</p>
<pre><code class="language-txt">http.host eq &quot;www.example.com&quot; and not cf.edge.server_port in {80 443}&#10;</code></pre>
<p>Compound expressions have the following general syntax:</p>
<pre><code class="language-txt">&lt;expression&gt; &lt;logical_operator&gt; &lt;expression&gt;&#10;</code></pre>
<p>Compound expressions allow you to generate sophisticated, highly targeted rules.</p>
<h2 id="maximum-rule-expression-length">Maximum rule expression length</h2>
<p>The maximum length of a rule expression is 4,096 characters.</p>
<p>This limit applies whether you use the visual <a href="/ruleset-engine/rules-language/expressions/edit-expressions/#expression-builder">Expression Builder</a> to define your expression, or write the expression manually in the <a href="/ruleset-engine/rules-language/expressions/edit-expressions/#expression-editor">Expression Editor</a>.</p>
<h2 id="maximum-regular-expressions-per-rule">Maximum regular expressions per rule</h2>
<p>Each rule can contain a maximum of 64 regular expressions in its expression. This limit applies across all rule types that use the <a href="/ruleset-engine/rules-language/">Rules language</a>.</p>
<p>Rules that exceed this limit cannot be created or updated. Existing rules above this limit continue to work but cannot be modified until the expression is simplified.</p>
<h2 id="additional-features">Additional features</h2>
<p>You can also use the following Rules language features in your expressions:</p>
<ul>
<li>
<p><a href="/ruleset-engine/rules-language/operators/#grouping-symbols">Grouping symbols</a> allow you to explicitly group expressions that should be evaluated together.</p>
</li>
<li>
<p><a href="/ruleset-engine/rules-language/functions/">Functions</a> allow you to manipulate and validate values in expressions.</p>
</li>
</ul>
