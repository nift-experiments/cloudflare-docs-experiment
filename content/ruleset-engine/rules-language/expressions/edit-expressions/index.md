<p>In the Cloudflare dashboard, there are two options for editing <a href="/ruleset-engine/rules-language/expressions/">expressions</a>:</p>
<ul>
<li><a href="/ruleset-engine/rules-language/expressions/edit-expressions/#expression-builder">Expression Builder</a>: Allows you to create expressions using drop-down lists, emphasizing a visual approach to defining an expression.</li>
<li><a href="/ruleset-engine/rules-language/expressions/edit-expressions/#expression-editor">Expression Editor</a>: A text-only interface that supports advanced features, such as grouping symbols and functions for transforming and validating values.</li>
</ul>
<p>In general, you can switch back and forth between the Expression Builder and the Expression Editor. However, the Expression Builder does not support advanced features like:</p>
<ul>
<li><a href="#create-nested-expressions">Nested expressions</a></li>
<li><a href="/ruleset-engine/rules-language/functions/">Function calls</a></li>
</ul>
<p>The builder may also not show all the fields you can use in the expression you are editing.</p>
<p>If you use advanced expression features or enter unlisted fields in your expression when using the editor, you may not be able to switch to the Expression Builder. You will get a warning popup stating that the expression is not supported in the builder. To proceed, you may discard any changes made in the editor, or cancel the switch and continue working in the editor.</p>
<h2 id="expression-builder">Expression Builder</h2>
<p>The Expression Builder allows you to visually create rule expressions by using drop-down lists and entering field values to define one or multiple sub-expressions.</p>
<p><img src="/assets/upstream/images/ruleset-engine/language/expression-builder.png" alt="The Expression Builder interface used to visually define expressions" /></p>
<p>The <strong>Expression Preview</strong> displays the expression in text:</p>
<pre><code class="language-sql">(ip.src.country ne &quot;GB&quot;)&#10;</code></pre>
<p>The Expression Builder will <a href="#escape-special-characters">automatically escape</a> the backslash (<code>\</code>) and double quote (<code>&quot;</code>) special characters in string literals when using the <a href="/ruleset-engine/rules-language/values/#quoted-string-syntax">quoted string syntax</a>.</p>
<h2 id="expression-editor">Expression Editor</h2>
<p>The <strong>Expression Editor</strong> is a text-only interface for defining rule expressions that supports the entire specification of Cloudflare's <a href="/ruleset-engine/rules-language/">Rules language</a>, including parentheses as grouping symbols.</p>
<p><img src="/assets/upstream/images/ruleset-engine/language/expression-editor.png" alt="The Expression Editor used to enter advanced expressions" /></p>
<p>To access the Expression Editor, select <strong>Edit expression</strong> next to the <strong>Expression Preview</strong>:</p>
<p><img src="/assets/upstream/images/ruleset-engine/language/expression-builder.png" alt="Selecting Edit expression in the Create custom rule page to switch to the Expression Editor" /></p>
<p>To switch back from the Expression Editor to the Expression Builder, select <strong>Use expression builder</strong>.</p>
<h3 id="escape-special-characters">Escape special characters</h3>
<p>In expressions using the <a href="/ruleset-engine/rules-language/values/#quoted-string-syntax">quoted string syntax</a>, all backslash (<code>\</code>) and double quote (<code>&quot;</code>) characters in string literals must be escaped. The visual Expression Builder will automatically escape these special characters by prepending a backslash such that <code>\</code> and <code>&quot;</code> become <code>\\</code> and <code>\&quot;</code>, respectively.</p>
<pre><code class="language-txt">&#35; Example of an expression with a &quot; character written using quoted string syntax&#10;http.request.uri.path eq &quot;/foo\&quot;bar&quot;&#10;</code></pre>
<p>The Expression Builder supports both the <a href="/ruleset-engine/rules-language/values/#quoted-string-syntax">quoted string syntax</a> and the <a href="/ruleset-engine/rules-language/values/#raw-string-syntax">raw string syntax</a>. In the raw string syntax, there are no special characters or escape sequences, so all characters up to the ending delimiter are interpreted as is.</p>
<pre><code class="language-txt">&#35; Example of an expression with a &quot; character written using the raw string syntax&#10;http.request.uri.path eq r#&quot;/foo&quot;bar&quot;#&#10;</code></pre>
<p>When you select <em>Matches regex</em> in the <strong>Operator</strong> dropdown in the dashboard, the expression preview will automatically use the raw string syntax. In other situations, you may need to switch to the Expression Editor to manually enter a string using the raw string syntax. In this case, switching back to the Expression Builder will keep the syntax you used in the editor.</p>
<p>When you write a <a href="/ruleset-engine/rules-language/operators/#regular-expression-matching">regular expression</a> using the quoted string syntax, you may need to perform additional escaping — refer to <a href="/ruleset-engine/rules-language/values/#quoted-string-syntax">Quoted string syntax</a> for details.</p>
<p>To write complex regular expressions, Cloudflare recommends that you use the <a href="/ruleset-engine/rules-language/values/#raw-string-syntax">raw string syntax</a>, which needs less escaping.</p>
<h3 id="create-nested-expressions">Create nested expressions</h3>
<p>The Expression Editor supports parentheses as <a href="/ruleset-engine/rules-language/operators/#grouping-symbols">grouping symbols</a>. Use parentheses to explicitly group and nest expressions and, in turn, create highly targeted expressions.</p>
<p>The following rule expression will match requests from any visitor who is not from Malaysia and tries to access WordPress URI paths.</p>
<pre><code class="language-txt">((http.request.uri.path contains &quot;/xmlrpc.php&quot;) or (http.request.uri.path&#10;contains &quot;/wp-login.php&quot;) or (http.request.uri.path contains &quot;/wp-admin/&quot;&#10;and not http.request.uri.path contains &quot;/wp-admin/admin-ajax.php&quot; and not&#10;http.request.uri.path contains &quot;/wp-admin/theme-editor.php&quot;)) and&#10;ip.src.country ne &quot;MY&quot;&#10;</code></pre>
<p>Only the Expression Editor supports nested expressions such as the one above. If you create a rule with nested expressions in the Expression Editor and try to switch to the Expression Builder, a dialog will warn you that the expression is not supported in the builder. You will be prompted to <strong>Discard changes</strong> and switch to the Expression Builder or <strong>Cancel</strong> and continue working in the editor.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13300.md")
</aside>
<h2 id="expression-validation">Expression validation</h2>
<p>Cloudflare validates all expressions before saving them, so if your expression has errors, you will receive an error message in the Cloudflare dashboard, similar to the following:</p>
<pre><code class="language-txt">Filter parsing error (1:313): ((http.request.uri.path contains&#10;&quot;/xmlrpc.php&quot;) or (http.request.uri.path contains &quot;/wp-login.php&quot;) or&#10;(http.request.uri.path contains &quot;/wp-admin/&quot; and not&#10;http.request.uri.path contains &quot;/wp-admin/admin-ajax.php&quot; and not&#10;http.request.uri.path contains &quot;/wp-admin/theme-editor.php&quot;)) and&#10;ip.src.country ne &quot;MY&quot;) ^ unrecognised input&#10;</code></pre>
