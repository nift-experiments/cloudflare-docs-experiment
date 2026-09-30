<p>When an HTTP request reaches the Cloudflare global network, Cloudflare creates a table of field–value pairs against which to match expressions. This table exists for as long as the current request is being processed.</p>
<p>The values that populate the lookup tables of the Rules language are drawn from a variety of sources:</p>
<ul>
<li><strong>Primitive properties</strong> are obtained directly from the request (<code>http.request.uri.path</code>, for example).</li>
<li><strong>Derived values</strong> are the product of a transformation, composition, or basic operation. For example, the transformation <code>lower(http.request.uri.path)</code> converts the value of <code>http.request.uri.path</code> to lowercase.</li>
<li><strong>Computed values</strong> are the product of a lookup, computation, or other intelligence. For example, Cloudflare uses a machine learning process to dynamically calculate attack scores, represented by <code>cf.waf.score*</code> fields.</li>
</ul>
<p>Besides these values, expressions may also contain literal values. These are static, known values that you incorporate into expressions to compare them with values from request/response fields with or without any transformations.</p>
<p>When working with values in rule expressions, keep in mind the information in the following sections.</p>
<h2 id="string-values-and-regular-expressions">String values and regular expressions</h2>
<p>Strings are sequences of bytes enclosed by specific delimiters.</p>
<p>Cloudflare rules support two formats for specifying literal strings, including regular expressions: <a href="#quoted-string-syntax">quoted literal strings</a> and <a href="#raw-string-syntax">raw strings</a>. These formats have different delimiters and escaping mechanisms.</p>
<p>You can use either of the two string formats to specify regular expressions in an expression. However, Cloudflare recommends that you use the <a href="#raw-string-syntax">raw string syntax</a>, since the quoted string syntax has complex escaping rules and can lead to unexpected behaviors if not thoroughly tested.</p>
<p>Regular expression matching is performed using the Rust regular expression engine.</p>
<h3 id="quoted-string-syntax">Quoted string syntax</h3>
<p>When using the quoted string syntax, a string literal is delimited by <code>&quot;</code> (double quote) characters. This format requires that you escape special characters <code>&quot;</code> and <code>\</code> using <code>\&quot;</code> and <code>\\</code>, respectively.</p>
<p>The quoted string syntax has the following additional escaping requirements:</p>
<ul>
<li>When used to specify a regular expression on the right-hand side of the <a href="/ruleset-engine/rules-language/operators/#comparison-operators">regex operator</a> (<code>matches</code> or <code>~</code>), the string is parsed using regex escaping rules.</li>
<li>When used on the right hand-side of expressions with other operators, or in <a href="/ruleset-engine/rules-language/functions/">function parameters</a>, the string is parsed using basic escaping rules.</li>
</ul>
<pre><code class="language-txt">&#35; Test if URI path contains &#x27;a&quot;b&#x27;&#10;http.request.uri.path matches &quot;a\&quot;b&quot;&#10;&#10;&#35; Test if URI path contains &#x27;a&quot;#b&#x27;&#10;http.request.uri.path matches &quot;a\&quot;#b&quot;&#10;&#10;&#35; Replace &#x27;a&#x27; with &#x27;\&#x27; (backslash)&#10;regex_replace(http.host, &quot;a&quot;, &quot;\\&quot;)&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13247.md")
</aside>
<h3 id="raw-string-syntax">Raw string syntax</h3>
<p>To specify a string (or regular expression) using the raw string syntax you use special delimiters:</p>
<ul>
<li>The initial delimiter is composed of an <code>r</code> character, optionally followed by one or more <code>#</code> characters (up to 255), followed by a <code>&quot;</code> (double quote) character.</li>
<li>The ending delimiter is a <code>&quot;</code> (double quote) character followed by the same number of <code>#</code> characters as in the initial delimiter (from 0 to 255).</li>
</ul>
<p>In a raw string there are no special characters, so all characters up to the ending delimiter are interpreted as is (there are no escape sequences).</p>
<p>Unlike the quoted string syntax, the raw string syntax is always the same, regardless of the context where it is being used (for example, as a regular expression with a <a href="/ruleset-engine/rules-language/operators/#comparison-operators">regex operator</a> or as a parameter of a <a href="/ruleset-engine/rules-language/functions/">function call</a>).</p>
<pre><code class="language-txt">&#35; Test if URI path contains &#x27;a&quot;b&#x27;&#10;http.request.uri.path matches r#&quot;a&quot;b&quot;#&#10;&#10;&#35; Test if URI path contains &#x27;a&quot;#b&#x27;&#10;http.request.uri.path matches r##&quot;a&quot;#b&quot;##&#10;&#10;&#35; Replace &#x27;\&#x27; (backslash) with &#x27;a&#x27;&#10;&#35; You must still escape the &#x27;\&#x27; character in the following raw string because it has a special meaning in regular expressions&#10;regex_replace(http.host, r&quot;\\&quot;, &quot;a&quot;)&#10;&#10;&#35; Test if URI path ends with &#x27;/api/login.aspx&#x27;&#10;&#35; You must still escape the &#x27;.&#x27; character in the following raw string because it has a special meaning in regular expressions (&quot;any character&quot;)&#10;http.request.uri.path matches r&quot;/api/login\.aspx$&quot;&#10;</code></pre>
<h3 id="case-sensitivity-in-string-comparisons">Case sensitivity in string comparisons</h3>
<p>Since the evaluation of string literal values in expressions is case-sensitive, consider one of the following options to capture capitalization variants in your expression:</p>
<ul>
<li>Use the <a href="/ruleset-engine/rules-language/operators/#wildcard-matching"><code>wildcard</code></a> operator, which is case-insensitive, to match a string literal.</li>
<li>Use the <a href="/ruleset-engine/rules-language/functions/#lower"><code>lower()</code></a> function to convert the string to lowercase before comparison.</li>
<li>Use the <a href="/ruleset-engine/rules-language/operators/#regular-expression-matching"><code>matches</code></a> operator (only available in Business and Enterprise plans) with a regular expression that matches different variants.</li>
<li>Write several sub-expressions with the <a href="/ruleset-engine/rules-language/operators/#comparison-operators"><code>eq</code></a> or <a href="/ruleset-engine/rules-language/operators/#comparison-operators"><code>contains</code></a> operator, joined with the <a href="/ruleset-engine/rules-language/operators/#supported-logical-operators"><code>or</code></a> operator, to capture different variations of the string literal (for example, <code>&lt;field&gt; eq &quot;a&quot; or &lt;field&gt; eq &quot;A&quot;</code>).</li>
</ul>
<h3 id="regular-expression-limits">Regular expression limits</h3>
<p>Cloudflare has a few limits in place regarding regular expressions. One of those limits is that each rule supports a maximum of 64 regular expressions (regexes), regardless of your domain's plan.</p>
<p>You can use the following strategies to reduce the number of regular expressions in a rule:</p>
<ul>
<li>Use the <a href="/ruleset-engine/rules-language/operators/#comparison-operators"><code>contains</code></a> operator.</li>
<li>Use the <a href="/ruleset-engine/rules-language/operators/#wildcard-matching"><code>wildcard</code></a> / <a href="/ruleset-engine/rules-language/operators/#wildcard-matching"><code>strict wildcard</code></a> operators.</li>
<li>Use the <a href="/ruleset-engine/rules-language/functions/#starts_with"><code>starts_with()</code></a> and <a href="/ruleset-engine/rules-language/functions/#ends_with"><code>ends_with()</code></a> functions.</li>
</ul>
<h2 id="boolean-values">Boolean values</h2>
<p>Simple expressions using boolean fields do not require operator notations or values. You only need to insert the field on its own, as shown in the <code>ssl</code> example below.</p>
<pre><code class="language-sql">ssl&#10;</code></pre>
<p>This simple expression matches requests where the value of the <code>ssl</code> field is <code>true</code>.</p>
<p>To match requests where <code>ssl</code> is <code>false</code>, use the boolean <code>not</code> operator :</p>
<pre><code class="language-sql">not ssl&#10;</code></pre>
<h2 id="arrays">Arrays</h2>
<p>The Cloudflare Rules language includes <a href="/ruleset-engine/rules-language/fields/">fields</a> of <code>Array</code> type and <a href="/ruleset-engine/rules-language/functions/">functions</a> with <code>Array</code> arguments and return values.</p>
<p>You can access individual array elements using an index (a non-negative value) between square brackets (<code>[]</code>). Array indexes start at <code>0</code> (zero).</p>
<p>Use the special notation <code>[*]</code> when specifying an expression that will be evaluated for each array element (like the <a href="https://wikipedia.org/wiki/Map_(higher-order_function)"><code>map</code> high-order function</a>). This special index notation will unpack the array, call the enclosing function for all its elements individually, and return a new array containing all the individual return values.</p>
<h3 id="examples">Examples</h3>
<p>Consider the <code>http.request.headers.names</code> field with type <code>Array&lt;String&gt;</code> in the following examples:</p>
<ul>
<li>
<p>Obtain the first element in the array:<br/>
<code>http.request.headers.names[0]</code></p>
</li>
<li>
<p>Check if the first array element is equal to <code>Content-Type</code> (case sensitive):<br/>
<code>http.request.headers.names[0] == &quot;Content-Type&quot;</code></p>
</li>
<li>
<p>Check if any array element is equal to <code>Content-Type</code> (case sensitive):<br/>
<code>any(http.request.headers.names[*] == &quot;Content-Type&quot;)</code></p>
</li>
<li>
<p>Check if any array element is equal to <code>Content-Type</code>, ignoring the case:<br/>
<code>any(lower(http.request.headers.names[*])[*] == &quot;content-type&quot;)</code></p>
</li>
</ul>
<p>In the last example, the <code>lower()</code> function includes the <code>[*]</code> notation so that the function is evaluated for each array element. This function, used along <code>[*]</code>, returns a new array where each element of the input array is converted to lowercase. Then, the string comparison uses <code>[*]</code> to transform the array resulting from applying <code>lower()</code> to each header name into an array of boolean values. Finally, <code>any()</code> evaluates to true if at least one of these array elements is true.</p>
<h3 id="notes">Notes</h3>
<p>It is not possible to define your own arrays. You can only use arrays returned by fields, either directly or modified by functions.</p>
<p>Accessing an out-of-bounds array index produces a &quot;missing value&quot;. A missing value has the following behavior:</p>
<ul>
<li>Any comparison <code>&lt;expr&gt; &lt;op&gt; &lt;literal&gt;</code> where <code>&lt;expr&gt;</code> evaluates to a missing value will evaluate to false.</li>
<li>Function calls like <code>function(&lt;expr&gt;)</code>, where <code>&lt;expr&gt;</code> evaluates to a missing value, will return a missing value in most cases, but the exact behavior can vary per function.</li>
</ul>
<p>You can only use <code>[*]</code> multiple times in the same expression if applied to the same array. Also, you can only use <code>[*]</code> in the first argument of a function call.</p>
<p>The Rules language <a href="/ruleset-engine/rules-language/operators/">operators</a> do not directly support arrays or the <code>[*]</code> operator — however, they support indexed array elements like <code>array_value[0]</code>. For example, you cannot use <code>[*]</code> with the <code>==</code> operator outside the context of an enclosing function call:</p>
<ul>
<li><code>http.request.headers.names[*] == &quot;Content-Type&quot;</code> — <strong>Invalid</strong> expression</li>
<li><code>any(http.request.headers.names[*] == &quot;Content-Type&quot;)</code> — <strong>Valid</strong> expression</li>
</ul>
<h2 id="maps">Maps</h2>
<p>A map, also called associative array, is a data structure that stores a collection of key-value pairs, where the key must be a <code>String</code> and the value can be of any type (for example, a <code>String</code> or an array of values). All values in a map must have the same type.</p>
<p>The Cloudflare Rules language includes several <a href="/ruleset-engine/rules-language/fields/">fields</a> of <code>Map</code> data type. The type notation for map fields, for example <code>Map&lt;Array&lt;String&gt;&gt;</code>, indicates the data type of the values associated with keys (an <code>Array</code> of <code>String</code> elements). This means that when you access the value of key <code>&quot;foo&quot;</code> you will get either an array of <code>String</code> elements or a <a href="#notes-1">missing value</a>.</p>
<p>To access a value in a map, enter the key between square brackets (<code>[]</code>):</p>
<pre><code class="language-txt">&lt;MAP_FIELD&gt;[&lt;KEY&gt;]&#10;</code></pre>
<p>For maps where the values have an <code>Array</code> type, you cannot directly use <a href="/ruleset-engine/rules-language/operators/">operators</a> with the obtained (array) value, since these operators do not support arrays directly. To use an operator on an item of the array, use the special notation <code>[*]</code> when specifying an expression. This special index notation will unpack the array, call the enclosing function for all its elements individually, and return a new array containing all the individual return values.</p>
<h3 id="examples-1">Examples</h3>
<p>The following example is based on the <a href="/ruleset-engine/rules-language/fields/reference/http.request.headers/"><code>http.request.headers</code></a> field with a data type of <code>Map&lt;Array&lt;String&gt;&gt;</code>, where array elements are of <code>String</code> data type.</p>
<p>If an incoming HTTP request included a single <code>Accept: application/json</code> HTTP header, the following expressions would evaluate to the indicated values:</p>
<pre><code class="language-txt">http.request.headers[&quot;accept&quot;]     # ==&gt; [&quot;application/json&quot;]&#10;http.request.headers[&quot;accept&quot;][0]  # ==&gt; &quot;application/json&quot;&#10;&#10;any(http.request.headers[&quot;accept&quot;][*] == &quot;application/json&quot;) # ==&gt; true&#10;any(http.request.headers[&quot;accept&quot;][*] == &quot;text/plain&quot;)       # ==&gt; false&#10;</code></pre>
<p>The following example is based on the <a href="/ruleset-engine/rules-language/fields/reference/http.request.uri.args/"><code>http.request.uri.args</code></a> field with a data type of <code>Map&lt;Array&lt;String&gt;&gt;</code>, where array elements are of <code>String</code> data type.</p>
<p>If an HTTP request included three <code>filter</code> URI arguments <code>waf</code>, <code>botm</code>, and <code>cdn</code>, the following expressions would evaluate to the indicated values:</p>
<pre><code class="language-txt">&#35; Example request URL:&#10;&#35; https://example.com/?filter=waf&amp;filter=botm&amp;filter=cdn&#10;&#10;http.request.uri.args[&quot;filter&quot;]          # ==&gt; [&quot;waf&quot;, &quot;botm&quot;, &quot;cdn&quot;]&#10;&#10;len(http.request.uri.args[&quot;filter&quot;][1])  # ==&gt; 4&#10;&#10;&#35; Check if the length of all &#x27;filter&#x27; values is always 3 or 4&#10;all(len(http.request.uri.args[&quot;filter&quot;][*])[*] in {3 4})      # ==&gt; true&#10;&#10;&#35; Check if the length of &#x27;filter&#x27; values (if any) is never 3 or 4&#10;all(not len(http.request.uri.args[&quot;filter&quot;][*])[*] in {3 4})  # ==&gt; false&#10;&#10;&#35; Check if the http.request.uri.args map contains a &quot;filter&quot; key&#10;len(http.request.uri.args[&quot;filter&quot;]) &gt;= 0     # ==&gt; true&#10;&#10;&#35; Check if the http.request.uri.args map does not contain an &quot;order&quot; key&#10;not len(http.request.uri.args[&quot;order&quot;]) &gt;= 0  # ==&gt; true&#10;</code></pre>
<p>For more information on <code>any()</code>, <code>all()</code>, <code>len()</code>, and other available functions, refer to <a href="/ruleset-engine/rules-language/functions/">Functions</a>.</p>
<h3 id="notes-1">Notes</h3>
<p>It is not possible to define your own maps. You can only use maps returned by fields.</p>
<p>Accessing a non-existing key in a map produces a &quot;missing value&quot;. A missing value has the following behavior:</p>
<ul>
<li>Any comparison <code>&lt;expr&gt; &lt;op&gt; &lt;literal&gt;</code> where <code>&lt;expr&gt;</code> evaluates to a missing value will evaluate to false.</li>
<li>Function calls like <code>function(&lt;expr&gt;)</code>, where <code>&lt;expr&gt;</code> evaluates to a missing value, will return a missing value in most cases, but the exact behavior can vary per function.</li>
</ul>
<h2 id="lists">Lists</h2>
<p>Lists allow you to create a group of items and refer to them collectively, by name, in your expressions. Each list type supports items of a specific data type. All items in a list must have the same data type. For details on the available list types, refer to <a href="/waf/tools/lists/#supported-lists">Lists</a>.</p>
<p>To refer to a list in a rule expression, use <code>$&lt;list_name&gt;</code> and specify the <code>in</code> <a href="/ruleset-engine/rules-language/operators/">operator</a>. Only one value in the list has to match the left-hand side of the expression (before the <code>in</code> operator) for the simple expression to evaluate to <code>true</code>. If there is no match, the expression will evaluate to <code>false</code>.</p>
<p>The following example expression filters requests from IP addresses that are in an <a href="/waf/tools/lists/custom-lists/#ip-lists">IP list</a> named <code>office_network</code>:</p>
<pre><code class="language-sql">(ip.src in $office_network)&#10;</code></pre>
<p>List names can only include lowercase letters, numbers, and the underscore (<code>_</code>) character. For guidance on creating and managing lists, refer to <a href="/waf/tools/lists/">Lists</a>.</p>
<h3 id="inline-lists">Inline lists</h3>
<p>Inline lists allow you to directly include a list of values in a simple expression that uses the <code>in</code> operator.</p>
<p>Elements in an inline list can be strings, integers, or IP addresses/ranges. All elements of an inline list must have the same data type and they must be literal values. To specify inline list elements, enter them individually, separating elements with a space. Inline lists can contain duplicate values.</p>
<p>Additionally, for some data types you can use ranges as elements:</p>
<ul>
<li>
<p>For integer values, enter ranges in the form <code>&lt;start_value&gt;..&lt;end_value&gt;</code>. An inline list can contain both integer ranges and integer values.</p>
</li>
<li>
<p>For IP addresses, you can enter:</p>
<ul>
<li>Explicit IP ranges in the form <code>&lt;start_address&gt;..&lt;end_address&gt;</code> (for example, <code>198.51.100.3..198.51.100.7</code>).</li>
<li>CIDR ranges (for example, <code>192.0.2.0/24</code> or <code>2001:0db8::/32</code>).</li>
</ul>
<p>An inline list can contain explicit IP ranges, CIDR ranges, and individual IP addresses.</p>
</li>
</ul>
<pre><code class="language-sql">http.host in {&quot;example.com&quot; &quot;example.net&quot;}&#10;&#10;ip.src in {198.51.100.1 198.51.100.3..198.51.100.7 192.0.2.0/24 2001:0db8::/32}&#10;&#10;tcp.dstport in {8000..8009 8080..8089}&#10;</code></pre>
