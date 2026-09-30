<p>The Cloudflare Rules language provides functions for manipulating and validating values in an expression:</p>
<ul>
<li><a href="#transformation-functions">Transformation functions</a> manipulate values extracted from an HTTP request.</li>
<li>The <a href="#hmac-validation">HMAC validation function</a> tests the validity of an HMAC token. Use it to write expressions that target requests based on the presence of a valid HMAC token.</li>
</ul>
<h2 id="transformation-functions">Transformation functions</h2>
<p>The Rules language supports several functions that transform values extracted from HTTP requests. A common use case for transformation functions is the conversion of a string of characters to uppercase or lowercase, since by default, string evaluation is case-sensitive.</p>
<p>For example, the <code>lower()</code> function converts all uppercase characters in a string to lowercase.</p>
<p>In the expression below, the <code>lower()</code> function transforms <code>http.host</code> values to lowercase so that they match the target value <code>&quot;www.cloudflare.com&quot;</code>:</p>
<pre><code class="language-sql">lower(http.host) == &quot;www.cloudflare.com&quot;&#10;</code></pre>
<p>Transformation functions that do not take arrays as an argument type require the <code>[*]</code> index notation. Refer to <a href="/ruleset-engine/rules-language/values/#arrays">Arrays</a> for more information.</p>
<p>The Rules language supports these transformation functions:</p>
<h3 id="any"><code>any</code></h3>
<p><code>any(<span class="nb-type">Array&lt;Boolean&gt;</span>)</code>: <span class="nb-type">Boolean</span></p>
<p>Returns <code>true</code> when the comparison operator in the argument returns <code>true</code> for <em>any</em> of the values in the argument array. Returns <code>false</code> otherwise.</p>
<p>Example:</p>
<pre><code class="language-txt">any(url_decode(http.request.body.form.values[*])[*] contains &quot;an xss attack&quot;)&#10;</code></pre>
<h3 id="all"><code>all</code></h3>
<p><code>all(<span class="nb-type">Array&lt;Boolean&gt;</span>)</code>: <span class="nb-type">Boolean</span></p>
<p>Returns <code>true</code> when the comparison operator in the argument returns <code>true</code> for <em>all</em> values in the argument array. Returns <code>false</code> otherwise.</p>
<p>Example:</p>
<pre><code>all(http.request.headers[&quot;content-type&quot;][*] == &quot;application/json&quot;)&#10;</code></pre>
<h3 id="encode-base64"><code>encode_base64</code></h3>
<p><code>encode_base64(input <span class="nb-type">String | Bytes</span> [, flags <span class="nb-type">String</span>])</code>: <span class="nb-type">String</span></p>
<p>Encodes an <code>input</code> string or byte array to Base64 format.</p>
<p>The <code>flags</code> parameter is optional. You can provide one or more flags as a single string. The available flags are the following:</p>
<ul>
<li><code>u</code>: Uses URL-safe Base64 encoding (uses <code>-</code> and <code>_</code> instead of <code>+</code> and <code>/</code>).</li>
<li><code>p</code>: Adds padding (appends <code>=</code> characters to make the output length a multiple of 4, as required by some systems).</li>
</ul>
<p>By default, the output uses standard Base64 encoding without padding.</p>
<p>Examples:</p>
<pre><code class="language-txt">encode_base64(&quot;hello world&quot;)          will return &quot;aGVsbG8gd29ybGQ&quot;&#10;encode_base64(&quot;hello world&quot;, &quot;p&quot;)     will return &quot;aGVsbG8gd29ybGQ=&quot;&#10;encode_base64(&quot;hello world&quot;, &quot;u&quot;)     will return &quot;aGVsbG8gd29ybGQ&quot;&#10;encode_base64(&quot;hello world&quot;, &quot;up&quot;)    will return &quot;aGVsbG8gd29ybGQ=&quot;&#10;</code></pre>
<p>You can combine <code>encode_base64()</code> with other functions to create signed request headers:</p>
<pre><code class="language-txt">encode_base64(sha256(concat(to_string(ip.src), http.host, &quot;my-secret&quot;)))&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13269.md")
</aside>
<h3 id="cidr"><code>cidr</code></h3>
<p><code>cidr(address <span class="nb-type">IP address</span>, ipv4_network_bits <span class="nb-type">Integer</span>, ipv6_network_bits <span class="nb-type">Integer</span>)</code>: <span class="nb-type">IP address</span></p>
<p>Returns the network address corresponding to an IP address (IPv4 or IPv6), given the provided IPv4 and IPv6 network bits (which determine the corresponding netmasks).</p>
<p>The <code>address</code> parameter must be a field, that is, it cannot be a literal String.</p>
<p>The <code>ipv4_network_bits</code> value must be between 1 and 32, and the <code>ipv6_network_bits</code> value must be between 1 and 128.</p>
<p>Examples:</p>
<ul>
<li>If <code>ip.src</code> is <code>113.10.0.2</code>, <code>cidr(ip.src, 24, 24)</code> will return <code>113.10.0.0</code>.</li>
<li>If <code>ip.src</code> is <code>2001:0000:130F:0000:0000:09C0:876A:130B</code>, <code>cidr(ip.src, 24, 24)</code> will return <code>2001:0000:0000:0000:0000:0000:0000:0000</code>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13268.md")
</aside>
<h3 id="cidr6"><code>cidr6</code></h3>
<p><code>cidr6(address <span class="nb-type">IP address</span>, ipv6_network_bits <span class="nb-type">Integer</span>)</code>: <span class="nb-type">IP address</span></p>
<p>Returns the IPv6 network address corresponding to an IPv6 address, given the provided network bits (which determine the netmask). If you provide an IPv4 address in the first parameter, it will be returned unchanged.</p>
<p>The <code>address</code> parameter must be a field, that is, it cannot be a literal String.</p>
<p>The <code>ipv6_network_bits</code> value must be between 1 and 128.</p>
<p>This function is equivalent to: <code>cidr(&lt;address&gt;, 32, &lt;ipv6_network_bits&gt;)</code>.</p>
<p>Examples:</p>
<ul>
<li>If <code>ip.src</code> is <code>2001:0000:130F:0000:0000:09C0:876A:130B</code>, <code>cidr6(ip.src, 24)</code> will return <code>2001:0000:0000:0000:0000:0000:0000:0000</code>.</li>
<li>If <code>ip.src</code> is <code>113.10.0.2</code>, <code>cidr6(ip.src, 24)</code> will return <code>113.10.0.2</code> (unchanged).</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13267.md")
</aside>
<h3 id="concat"><code>concat</code></h3>
<p><code>concat(<span class="nb-type">String | Bytes | Array</span>)</code>: <span class="nb-type">String | Array</span></p>
<p>Takes a comma-separated list of values. Concatenates the argument values into a single String or array.</p>
<p>The return type depends on the type of input arguments. For example, if you concatenate arrays, the function will return an array.</p>
<p>For example, <code>concat(&quot;String1&quot;, &quot; &quot;, &quot;String&quot;, &quot;2&quot;)</code> will return <code>&quot;String1 String2&quot;</code>.</p>
<h3 id="decode-base64"><code>decode_base64</code></h3>
<p><code>decode_base64(source <span class="nb-type">String</span>)</code>: <span class="nb-type">String</span></p>
<p>Decodes a Base64-encoded String specified in <code>source</code>.</p>
<p><code>source</code> must be a field, that is, it cannot be a literal String.</p>
<p>For example, with the following HTTP request header: <code>client_id: MTIzYWJj</code>, <code>(any(decode_base64(http.request.headers[&quot;client_id&quot;][*])[*] eq &quot;123abc&quot;))</code> would return <code>true</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13266.md")
</aside>
<h3 id="ends-with"><code>ends_with</code></h3>
<p><code>ends_with(source <span class="nb-type">String</span>, substring <span class="nb-type">String</span>)</code>: <span class="nb-type">Boolean</span></p>
<p>Returns <code>true</code> when the source ends with a given substring. Returns <code>false</code> otherwise. The source cannot be a literal value (like <code>&quot;foo&quot;</code>).</p>
<p>For example, if <code>http.request.uri.path</code> is <code>&quot;/welcome.html&quot;</code>, then <code>ends_with(http.request.uri.path, &quot;.html&quot;)</code> will return <code>true</code>.</p>
<h3 id="join"><code>join</code></h3>
<p><code>join(items <span class="nb-type">Array&lt;String&gt;</span>, separator <span class="nb-type">String</span>)</code>: <span class="nb-type">String</span></p>
<p>Returns a string which is the concatenation of the strings in <code>items</code> with the <code>separator</code> between each item.</p>
<p>If any of the arguments is nil, the returned value will be nil.<br/>
If the <code>items</code> array is empty, the returned value will be an empty string.<br/>
If the <code>items</code> array contains a single item, then no concatenation occurs and the (single) item will be returned as is.</p>
<p>This function does the opposite of the <a href="#split"><code>split()</code></a> function.</p>
<p>Example:</p>
<pre><code class="language-txt">&#35; Joins all HTTP request header names into a single string, with names separated by commas&#10;join(http.request.headers.names, &quot;,&quot;)&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13265.md")
</aside>
<h3 id="has-key"><code>has_key</code></h3>
<p><code>has_key(map: <span class="nb-type">Map&lt;T&gt;</span>, key: <span class="nb-type">String</span>)</code>: <span class="nb-type">Boolean</span></p>
<p>Returns true if the <code>key</code> specified in the second argument, which can be a literal or a dynamic string, is an existing key in the <code>map</code> provided as first argument; returns false otherwise.</p>
<p>The data type of the values in <code>map</code> (indicated by <code>T</code>) can be any type.</p>
<p>If any of the arguments is nil, the returned value will be nil.</p>
<p>Examples:</p>
<pre><code class="language-txt">&#35; Check if an HTTP request header exists:&#10;has_key(http.request.headers, &quot;x-my-header&quot;)&#10;&#10;&#35; Check if a request header exists based on the name of the first query argument:&#10;has_key(http.request.headers, lower(http.request.uri.args.names[0]))&#10;</code></pre>
<h3 id="has-value"><code>has_value</code></h3>
<p><code>has_value(collection: <span class="nb-type">Map&lt;T&gt; | Array&lt;T&gt;</span>, value: <span class="nb-type">T</span>)</code>: <span class="nb-type">Boolean</span></p>
<p>Returns true if the <code>value</code> specified in the second argument, which can be a literal or a dynamic value, is found in the <code>collection</code> provided as first argument; returns false otherwise.</p>
<p>The data type of the values in the <code>collection</code> (indicated by <code>T</code>) must match the data type of the provided <code>value</code>. Additionally, <code>T</code> must be a primitive data type, that is, it must be one of <code>Boolean</code>, <code>Integer</code>, <code>String</code>, <code>Bytes</code>, or <code>IP address</code>.</p>
<p>If any of the arguments is nil, the returned value will be nil.</p>
<p>Examples:</p>
<pre><code class="language-txt">&#35; Check if there is an HTTP request header with the exact name &#x27;X-My-Header&#x27;&#10;has_value(http.request.headers.names, &quot;X-My-Header&quot;)&#10;&#10;&#35; Check if there is a request header with the exact name provided as the first query argument:&#10;has_value(http.request.headers.names, http.request.uri.args.names[0])&#10;</code></pre>
<h3 id="is-jwt-present"><code>is_jwt_present</code></h3>
<p><code>is_jwt_present(token_configuration_id: <span class="nb-type">String</span>)</code>: <span class="nb-type">Boolean</span></p>
<p>Returns true if the request has a token as configured in the token configuration with the ID <code>token_configuration_id</code>.</p>
<p><code>token_configuration_id</code> must be the ID of an existing <a href="/api-shield/security/jwt-validation/api/#token-configurations">token configuration</a>.</p>
<p>Example:</p>
<pre><code class="language-txt">is_jwt_present(&quot;51231d16-01f1-48e3-93f8-91c99e81288e&quot;)&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13264.md")
</aside>
<h3 id="is-jwt-valid"><code>is_jwt_valid</code></h3>
<p><code>is_jwt_valid(token_configuration_id: <span class="nb-type">String</span>)</code>: <span class="nb-type">Boolean</span></p>
<p>Returns true if the request has a valid token according to the token configuration with the ID <code>token_configuration_id</code>.</p>
<p><code>token_configuration_id</code> must be the ID of an existing <a href="/api-shield/security/jwt-validation/api/#token-configurations">token configuration</a>. The function returns false if the token is missing from the request.</p>
<pre><code class="language-txt">is_jwt_valid(&quot;51231d16-01f1-48e3-93f8-91c99e81288e&quot;)&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13263.md")
</aside>
<h3 id="len"><code>len</code></h3>
<p><code>len(<span class="nb-type">String | Bytes | Array</span>)</code>: <span class="nb-type">Integer</span></p>
<p>Returns the byte length of a String or Bytes value, or the number of elements in an array.</p>
<p>For example, if the value of <code>http.host</code> is <code>&quot;example.com&quot;</code>, then <code>len(http.host)</code> will return <code>11</code>.</p>
<h3 id="lookup-json-integer"><code>lookup_json_integer</code></h3>
<p><code>lookup_json_integer(field <span class="nb-type">String</span>, key <span class="nb-type">String | Integer</span>, key <span class="nb-type">String | Integer</span> <span class="nb-metainfo">optional</span>, ...)</code>: <span class="nb-type">Integer</span></p>
<p>Returns the integer value associated with the supplied <code>key</code> in <code>field</code>.</p>
<p>The <code>field</code> must be a string representation of a valid JSON document.</p>
<p>The <code>key</code> can be an attribute name, a zero-based position number in a JSON array, or a combination of these two options (as extra function parameters), while following the hierarchy of the JSON document to obtain a specific integer value.<br/></p>
<p>Note: This function only works for plain integers. For example, it will not work for floating numbers with a zero decimal part such as <code>42.0</code>.</p>
<p>Examples:</p>
<ul>
<li>
<p>Given the following JSON object contained in the <code>http.request.body.raw</code> field:<br/>
<code>{ &quot;record_id&quot;: &quot;aed53a&quot;, &quot;version&quot;: 2 }</code><br/>
Then <code>lookup_json_integer(http.request.body.raw, &quot;version&quot;)</code> will return <code>2</code>.</p>
</li>
<li>
<p>Given the following nested object:<br/>
<code>{ &quot;product&quot;: { &quot;id&quot;: 356 } }</code><br/>
Then <code>lookup_json_integer(http.request.body.raw, &quot;product&quot;, &quot;id&quot;)</code> will return <code>356</code>.</p>
</li>
<li>
<p>Given the following JSON array at the root level:<br/>
<code>[&quot;first_item&quot;, -234]</code><br/>
Then <code>lookup_json_integer(http.request.body.raw, 1)</code> will return <code>-234</code>.</p>
</li>
<li>
<p>Given the following array in a JSON object attribute:<br/>
<code>{ &quot;network_ids&quot;: [123, 456] }</code><br/>
Then <code>lookup_json_integer(http.request.body.raw, &quot;network_ids&quot;, 0)</code> will return <code>123</code>.</p>
</li>
<li>
<p>Given the following root-level array of JSON objects:<br/>
<code>[{ &quot;product_id&quot;: 123 }, { &quot;product_id&quot;: 456 }]</code><br/>
Then <code>lookup_json_integer(http.request.body.raw, 1, &quot;product_id&quot;)</code> will return <code>456</code>.</p>
</li>
</ul>
<h3 id="lookup-json-string"><code>lookup_json_string</code></h3>
<p><code>lookup_json_string(field <span class="nb-type">String</span>, key <span class="nb-type">String | Integer</span>, key <span class="nb-type">String | Integer</span> <span class="nb-metainfo">optional</span>, ...)</code>: <span class="nb-type">String</span></p>
<p>Returns the string value associated with the supplied <code>key</code> in <code>field</code>.</p>
<p>The <code>field</code> must be a string representation of a valid JSON document.</p>
<p>The <code>key</code> can be an attribute name, a zero-based position number in a JSON array, or a combination of these two options (as extra function parameters), while following the hierarchy of the JSON document to obtain a specific value.</p>
<p>Examples:</p>
<ul>
<li>
<p>Given the following JSON object contained in the <code>http.request.body.raw</code> field:<br/>
<code>{ &quot;company&quot;: &quot;cloudflare&quot;, &quot;product&quot;: &quot;rulesets&quot; }</code><br/>
Then <code>lookup_json_string(http.request.body.raw, &quot;company&quot;) == &quot;cloudflare&quot;</code> will return <code>true</code>.</p>
</li>
<li>
<p>Given the following nested object:<br/>
<code>{ &quot;network&quot;: { &quot;name&quot;: &quot;cloudflare&quot; } }</code><br/>
Then <code>lookup_json_string(http.request.body.raw, &quot;network&quot;, &quot;name&quot;) == &quot;cloudflare&quot;</code> will return <code>true</code>.</p>
</li>
<li>
<p>Given the following JSON array at the root level:<br/>
<code>[&quot;other_company&quot;, &quot;cloudflare&quot;]</code><br/>
Then <code>lookup_json_string(http.request.body.raw, 1) == &quot;cloudflare&quot;</code> will return <code>true</code>.</p>
</li>
<li>
<p>Given the following array in a JSON object attribute:<br/>
<code>{ &quot;networks&quot;: [&quot;other_company&quot;, &quot;cloudflare&quot;] }</code><br/>
Then <code>lookup_json_string(http.request.body.raw, &quot;networks&quot;, 1) == &quot;cloudflare&quot;</code> will return <code>true</code>.</p>
</li>
<li>
<p>Given the following root-level array of JSON objects:<br/>
<code>[{ &quot;network&quot;: &quot;other_company&quot; }, { &quot;network&quot;: &quot;cloudflare&quot; }]</code><br/>
Then <code>lookup_json_string(http.request.body.raw, 1, &quot;network&quot;) == &quot;cloudflare&quot;</code> will return <code>true</code>.</p>
</li>
</ul>
<h3 id="lower"><code>lower</code></h3>
<p><code>lower(<span class="nb-type">String</span>)</code>: <span class="nb-type">String</span></p>
<p>Converts a string field to lowercase. Only uppercase ASCII bytes are converted. All other bytes are unaffected.</p>
<p>For example, if <code>http.host</code> is <code>&quot;WWW.cloudflare.com&quot;</code>, then <code>lower(http.host) == &quot;www.cloudflare.com&quot;</code> will return <code>true</code>.</p>
<h3 id="regex-replace"><code>regex_replace</code></h3>
<p><code>regex_replace(source <span class="nb-type">String</span>, regular_expression <span class="nb-type">String</span>, replacement <span class="nb-type">String</span>)</code>: <span class="nb-type">String</span></p>
<p>Replaces a part of a source string matched by a regular expression with a replacement string, returning the result. The replacement string can contain references to regular expression capture groups (for example, <code>${1}</code> and <code>${2}</code>), up to eight replacement references.</p>
<p>Examples:</p>
<ul>
<li>
<p>Literal match replace:<br/>
<code>regex_replace(&quot;/foo/bar&quot;, &quot;/bar$&quot;, &quot;/baz&quot;) == &quot;/foo/baz&quot;</code></p>
</li>
<li>
<p>If there is no match, the input string does not change:<br/>
<code>regex_replace(&quot;/x&quot;, &quot;^/y$&quot;, &quot;/mumble&quot;) == &quot;/x&quot;</code></p>
</li>
<li>
<p>Match is case-sensitive by default:<br/>
<code>regex_replace(&quot;/foo&quot;, &quot;^/FOO$&quot;, &quot;/x&quot;) == &quot;/foo&quot;</code></p>
</li>
<li>
<p>When there are multiple matches, only one replacement occurs (the first one):<br/>
<code>regex_replace(&quot;/a/a&quot;, &quot;/a&quot;, &quot;/b&quot;) == &quot;/b/a&quot;</code></p>
</li>
<li>
<p>Escape a <code>$</code> in the replacement string by prefixing it with another <code>$</code>:<br/>
<code>regex_replace(&quot;/b&quot;, &quot;^/b$&quot;, &quot;/b$$&quot;) == &quot;/b$&quot;</code></p>
</li>
<li>
<p>Replace with capture groups:<br/>
<code>regex_replace(&quot;/foo/a/path&quot;, &quot;^/foo/([^/]*)/(.*)$&quot;, &quot;/bar/${2}/${1}&quot;) == &quot;/bar/path/a/&quot;</code></p>
</li>
</ul>
<p>Create capture groups by putting part of the regular expression in parentheses. Then, reference a capture group using <code>${&lt;NUMBER&gt;}</code> in the replacement string, where <code>&lt;NUMBER&gt;</code> is the number of the capture group.</p>
<p>You can only use the <code>regex_replace()</code> function once in an expression, and you cannot nest it with the <a href="/ruleset-engine/rules-language/functions/#wildcard_replace"><code>wildcard_replace()</code></a> function.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13262.md")
</aside>
<h3 id="remove-bytes"><code>remove_bytes</code></h3>
<p><code>remove_bytes(<span class="nb-type">Bytes</span>)</code>: <span class="nb-type">Bytes</span></p>
<p>Returns a new byte array with all the occurrences of the given bytes removed.</p>
<p>For example, if <code>http.host</code> is <code>&quot;www.cloudflare.com&quot;</code>, then <code>remove_bytes(http.host, &quot;\x2e\x77&quot;)</code> will return <code>&quot;cloudflarecom&quot;</code>.</p>
<h3 id="remove-query-args"><code>remove_query_args</code></h3>
<p><code>remove_query_args(field <span class="nb-type">String</span>, query_param1 <span class="nb-type">String</span>, query_param2 <span class="nb-type">String</span>, ...)</code>: <span class="nb-type">String</span></p>
<p>Removes one or more query string parameters from a URI query string. Returns a string without the specified parameters.</p>
<p>The <code>field</code> must be one of the following:</p>
<ul>
<li><code>http.request.uri.query</code></li>
<li><code>raw.http.request.uri.query</code></li>
</ul>
<p>The <code>field</code> cannot be a literal value such as <code>&quot;search=foo&amp;order=asc&quot;</code>.</p>
<p>The <code>remove_query_args()</code> function will remove all specified parameters (as <code>query_param1</code>, <code>query_param2</code>, etc.) , including repeated occurrences of the same parameter.</p>
<p>The ordering of unaffected query parameters will be preserved.</p>
<p>Examples:</p>
<pre><code class="language-txt">// If http.request.uri.query is &quot;order=asc&amp;country=GB&quot;:&#10;&#10;remove_query_args(http.request.uri.query, &quot;country&quot;)  will return &quot;order=asc&quot;&#10;remove_query_args(http.request.uri.query, &quot;order&quot;)    will return &quot;country=GB&quot;&#10;remove_query_args(http.request.uri.query, &quot;search&quot;)   will return &quot;order=asc&amp;country=GB&quot; (unchanged)&#10;&#10;// If http.request.uri.query is &quot;category=Foo&amp;order=desc&amp;category=Bar&quot;:&#10;&#10;remove_query_args(http.request.uri.query, &quot;order&quot;)    will return &quot;category=Foo&amp;category=Bar&quot;&#10;remove_query_args(http.request.uri.query, &quot;category&quot;) will return &quot;order=desc&quot;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13261.md")
</aside>
<h3 id="sha256"><code>sha256</code></h3>
<p><code>sha256(input <span class="nb-type">String | Bytes</span>)</code>: <span class="nb-type">Bytes</span></p>
<p>Computes the SHA-256 cryptographic hash of the <code>input</code> string or byte array. Returns a 32-byte hash value.</p>
<p>Use this function to generate signed request headers, validate request integrity, or create secure tokens directly in rule expressions.</p>
<p>Examples:</p>
<pre><code class="language-txt">sha256(&quot;my-token&quot;)&#10;</code></pre>
<p>The example above returns a 32-byte hash that your origin can validate to authenticate requests.</p>
<p>You can combine <code>sha256()</code> with <a href="#encode_base64"><code>encode_base64()</code></a> to create Base64-encoded signatures:</p>
<pre><code class="language-txt">encode_base64(sha256(&quot;my-token&quot;))&#10;</code></pre>
<p>To create a signed header value from request attributes:</p>
<pre><code class="language-txt">encode_base64(sha256(concat(to_string(ip.src), to_string(http.request.timestamp.sec), &quot;my-secret-key&quot;)))&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/13260.md")
</aside>
<h3 id="split"><code>split</code></h3>
<p><code>split(input <span class="nb-type">String</span>, separator <span class="nb-type">String</span>, limit <span class="nb-type">Integer</span>)</code>: <span class="nb-type">Array&lt;String&gt;</span></p>
<p>Splits the <code>input</code> string into an array of strings by breaking the initial string at every occurrence of the <code>separator</code> string. The returned array will contain at most <code>limit</code> number of elements.</p>
<p>If you provide a <code>limit</code> value lower than the actual number of substrings in the split string, the last element of the returned array will contain the remainder of the string.</p>
<p>The <code>separator</code> must be a non-empty literal string.</p>
<p>The <code>limit</code> is mandatory, and it must be a literal integer between 1 and 128.</p>
<p>If <code>input</code> is nil, the returned value will be nil.</p>
<p>This function does the opposite of the <a href="#join"><code>join()</code></a> function.</p>
<p>Examples:</p>
<pre><code class="language-txt">&#35; Split a comma-separated list of categories obtained from an HTTP request header.&#10;&#10;&#35; A) Consider the following HTTP request header:&#10;x-categories: groceries,electronics,diy,auto&#10;&#10;split(http.request.headers[&quot;x-categories&quot;][0], &quot;,&quot;, 64)  will return [&quot;groceries&quot;, &quot;electronics&quot;, &quot;diy&quot;, &quot;auto&quot;]&#10;split(http.request.headers[&quot;x-categories&quot;][0], &quot;,&quot;, 3)   will return [&quot;groceries&quot;, &quot;electronics&quot;, &quot;diy,auto&quot;]&#10;&#10;&#35; B) Consider the following HTTP request header:&#10;x-categories: groceries,,electronics&#10;&#10;split(http.request.headers[&quot;x-categories&quot;][0], &quot;,&quot;, 64)  will return [&quot;groceries&quot;, &quot;&quot;, &quot;electronics&quot;]&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13259.md")
</aside>
<h3 id="starts-with"><code>starts_with</code></h3>
<p><code>starts_with(source <span class="nb-type">String</span>, substring <span class="nb-type">String</span>)</code>: <span class="nb-type">Boolean</span></p>
<p>Returns <code>true</code> when the source starts with a given substring. Returns <code>false</code> otherwise. The source cannot be a literal value (like <code>&quot;foo&quot;</code>).</p>
<p>For example, if <code>http.request.uri.path</code> is <code>&quot;/blog/first-post&quot;</code>, then <code>starts_with(http.request.uri.path, &quot;/blog&quot;)</code> will return <code>true</code>.</p>
<h3 id="substring"><code>substring</code></h3>
<p><code>substring(field <span class="nb-type">String | Bytes</span>, start <span class="nb-type">Integer</span>, end <span class="nb-type">Integer</span> <span class="nb-metainfo">optional</span>)</code>: <span class="nb-type">String</span></p>
<p>Returns part of the <code>field</code> value (the value of a String or Bytes <a href="/ruleset-engine/rules-language/fields/reference/">field</a>) from the <code>start</code> byte index up to (but excluding) the <code>end</code> byte index. The first byte in <code>field</code> has index <code>0</code>. If you do not provide the optional <code>end</code> index, the function returns the part of the string from <code>start</code> index to the end of the string.</p>
<p>The <code>start</code> and <code>end</code> indexes can be negative integer values, which allows you to access characters from the end of the string instead of the beginning.</p>
<p>Examples:</p>
<pre><code class="language-txt">// If http.request.body.raw is &quot;asdfghjk&quot;:&#10;&#10;substring(http.request.body.raw, 2, 5)   will return &quot;dfg&quot;&#10;substring(http.request.body.raw, 2)      will return &quot;dfghjk&quot;&#10;substring(http.request.body.raw, -2)     will return &quot;jk&quot;&#10;substring(http.request.body.raw, 0, -2)  will return &quot;asdfgh&quot;&#10;</code></pre>
<h3 id="to-string"><code>to_string</code></h3>
<p><code>to_string(<span class="nb-type">Integer | Boolean | IP address</span>)</code>: <span class="nb-type">String</span></p>
<p>Returns the string representation of an Integer, Boolean, or IP address value.</p>
<p>Examples:</p>
<pre><code class="language-txt">// If cf.bot_management.score is 5:&#10;to_string(cf.bot_management.score)   will return &quot;5&quot;&#10;&#10;// If ssl is true:&#10;to_string(ssl)                       will return &quot;true&quot;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13258.md")
</aside>
<h3 id="upper"><code>upper</code></h3>
<p><code>upper(<span class="nb-type">String</span>)</code>: <span class="nb-type">String</span></p>
<p>Converts a string field to uppercase. Only lowercase ASCII bytes are converted. All other bytes are unaffected.</p>
<p>For example, if <code>http.host</code> is<code>&quot;www.cloudflare.com&quot;</code>, then <code>upper(http.host)</code> will return <code>&quot;WWW.CLOUDFLARE.COM&quot;</code>.</p>
<h3 id="url-decode"><code>url_decode</code></h3>
<p><code>url_decode(source <span class="nb-type">String</span>, options <span class="nb-type">String</span> <span class="nb-metainfo">optional</span>)</code>: <span class="nb-type">String</span></p>
<p>Decodes a URL-formatted string defined in <code>source</code>, as in the following:</p>
<ul>
<li>
<p><code>%20</code> and <code>+</code> decode to a space character (<code> </code>).</p>
</li>
<li>
<p><code>%E4%BD</code> decodes to <code>ä½</code>.</p>
</li>
</ul>
<p>The <code>source</code> must be a field, that is, it cannot be a literal string.</p>
<p>The <code>options</code> parameter is optional. You must provide any options as a single string wrapped in quotes, such as <code>&quot;r&quot;</code> or <code>&quot;ur&quot;</code>. The available options are the following:</p>
<ul>
<li><code>r</code>: Applies recursive decoding. For example, <code>%2520</code> will be decoded twice (recursively) to a space character (<code> </code>).</li>
<li><code>u</code>: Enables Unicode percent decoding. The result will be encoded in UTF-8. For example, <code>&quot;%u2601&quot;</code> would be decoded to a cloud emoji (<code>☁️</code>) encoded in UTF-8 (<code>&quot;\xe2\x98\x81&quot;</code>, with a size of 3 bytes).</li>
</ul>
<p>Examples:</p>
<pre><code class="language-txt">url_decode(&quot;John%20Doe&quot;)   will return &quot;John Doe&quot;&#10;url_decode(&quot;John+Doe&quot;)     will return &quot;John Doe&quot;&#10;url_decode(&quot;%2520&quot;)        will return &quot;%20&quot;&#10;url_decode(&quot;%2520&quot;, &quot;r&quot;)   will return &quot; &quot;&#10;&#10;// Using url_decode() with the any() function:&#10;any(url_decode(http.request.body.form.values[*])[*] contains &quot;an xss attack&quot;)&#10;&#10;// Using the u option to match a specific alphabet&#10;url_decode(http.request.uri.path) matches &quot;(?u)\p{Hangul}+&quot;&#10;</code></pre>
<h3 id="uuidv4"><code>uuidv4</code></h3>
<p><code>uuidv4(source <span class="nb-type">Bytes</span>)</code>: <span class="nb-type">String</span></p>
<p>Generates a random UUIDv4 (Universally Unique Identifier, version 4) based on the given argument (a source of randomness). To obtain an array of random bytes, use the <a href="/ruleset-engine/rules-language/fields/reference/cf.random_seed/"><code>cf.random_seed</code></a> field.</p>
<p>For example, <code>uuidv4(cf.random_seed)</code> will return a UUIDv4 similar to <code>49887398-6bcf-485f-8899-f15dbef4d1d5</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13257.md")
</aside>
<h3 id="wildcard-replace"><code>wildcard_replace</code></h3>
<p><code>wildcard_replace(source <span class="nb-type">Bytes</span>, wildcard_pattern <span class="nb-type">Bytes</span>, replacement <span class="nb-type">Bytes</span>, flags <span class="nb-type">Bytes</span> <span class="nb-metainfo">optional</span>)</code>: <span class="nb-type">String</span></p>
<p>Replaces a <code>source</code> string, matched by a literal with zero or more <code>*</code> wildcard metacharacters, with a replacement string, returning the result. The replacement string can contain references to wildcard capture groups (for example, <code>${1}</code> and <code>${2}</code>), up to eight replacement references.</p>
<p>If there is no match, the function will return <code>source</code> unchanged.</p>
<p>The <code>source</code> parameter must be a field (it cannot be a literal string). Additionally, the entire <code>source</code> value must match the <code>wildcard_pattern</code> parameter (it cannot match only part of the field value).</p>
<p>To enter a literal <code>*</code> character in the <code>wildcard_pattern</code> parameter, you must escape it using <code>\*</code>. Additionally, you must also escape <code>\</code> using <code>\\</code>. Two unescaped <code>*</code> characters in a row (<code>**</code>) in this parameter are considered invalid and cannot be used. If you need to perform character escaping, it is recommended that you use the <a href="/ruleset-engine/rules-language/values/#raw-string-syntax">raw string syntax</a> for the <code>wildcard_pattern</code> parameter.</p>
<p>To enter a literal <code>$</code> character in the <code>replacement</code> parameter, you must escape it using <code>$$</code>.</p>
<p>To perform case-sensitive wildcard matching, set the <code>flags</code> parameter to <code>&quot;s&quot;</code>.</p>
<p>This function uses lazy matching, that is, it tries to match each <code>*</code> metacharacter with the shortest possible string.</p>
<p>You can only use the <code>wildcard_replace()</code> function once in an expression, and you cannot nest it with the <a href="/ruleset-engine/rules-language/functions/#regex_replace"><code>regex_replace()</code></a> function.</p>
<p>Examples:</p>
<ul>
<li>
<p>If the full URI is <code>https://apps.example.com/calendar/admin?expand=true</code>,<br/>
<code>wildcard_replace(http.request.full_uri, &quot;https://*.example.com/*/*&quot;, &quot;https://example.com/${1}/${2}/${3}&quot;)</code> will return <code>https://example.com/apps/calendar/admin?expand=true</code></p>
</li>
<li>
<p>If the full URI is <code>https://example.com/applications/app1</code>,<br/>
<code>wildcard_replace(http.request.full_uri, &quot;/applications/*&quot;, &quot;/apps/${1}&quot;)</code> will return <code>https://example.com/applications/app1</code> (unchanged value, since there is no match for the full URI value; you should use the <code>http.request.uri.path</code> field for URI path matching).</p>
</li>
<li>
<p>If the URI path is <code>/calendar</code>,<br/>
<code>wildcard_replace(http.request.uri.path, &quot;/*&quot;, &quot;/apps/${1}&quot;)</code> will return <code>/apps/calendar</code>.</p>
</li>
<li>
<p>If the URI path is <code>/Apps/calendar</code>,<br/>
<code>wildcard_replace(http.request.uri.path, &quot;/apps/*&quot;, &quot;/${1}&quot;)</code> will return <code>/calendar</code> (case-insensitive match by default).</p>
</li>
<li>
<p>If the URI path is <code>/Apps/calendar</code>,<br/>
<code>wildcard_replace(http.request.uri.path, &quot;/apps/*&quot;, &quot;/${1}&quot;, &quot;s&quot;)</code> will return <code>/Apps/calendar</code> (unchanged value) because there is no case-sensitive match.</p>
</li>
<li>
<p>If the URI path is <code>/apps/calendar/login</code>,<br/>
<code>wildcard_replace(http.request.uri.path, &quot;/apps/*/login&quot;, &quot;/${1}/login&quot;)</code> will return <code>/calendar/login</code>.</p>
</li>
</ul>
<p>For more examples of wildcard matching, refer to <a href="/ruleset-engine/rules-language/operators/#wildcard-matching">Wildcard matching</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13256.md")
</aside>
<h2 id="cloudflare-network-firewall-functions">Cloudflare Network Firewall Functions</h2>
<h3 id="bit-slice"><code>bit_slice</code></h3>
<p><code>bit_slice(protocol <span class="nb-type">String</span>, offset_start <span class="nb-type">Number</span>, offset_end <span class="nb-type">Number</span>)</code>: <span class="nb-type">Number</span></p>
<p>This function looks for matches on a given slice of bits.</p>
<p>The offset starts on the given protocol header. For example, to match on the first bit of payload for a UDP packet, you must set <code>offset_start</code> to <code>64</code>.</p>
<p>This is primarily intended for use with <code>ip</code>, <code>udp</code>, and <code>tcp</code>.</p>
<p>The slice (<code>offset_end</code> – <code>offset_start</code>) cannot be longer than 32 bits, but multiple calls can be joined together by using logical expressions.</p>
<p>The <code>bit_slice</code> offset cannot exceed 2,040 bits.</p>
<h2 id="hmac-validation">HMAC validation</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13255.md")
</aside>
<h3 id="overview">Overview</h3>
<p>You can validate hash-based message authentication code (HMAC) tokens in a rule expression by using the <code>is_timed_hmac_valid_v0()</code> function, which has this signature:</p>
<pre><code class="language-java">is_timed_hmac_valid_v0(&#10;  &lt;String literal as Key&gt;,&#10;  &lt;String field as MessageMAC&gt;,&#10;  &lt;Integer literal as ttl&gt;,&#10;  &lt;Integer as currentTimeStamp&gt;,&#10;  &lt;Optional Integer literal as lengthOfSeparator, default: 0&gt;,&#10;  &lt;Optional String literal as flags&gt;&#10;) -&gt; &lt;Bool as result&gt;&#10;</code></pre>
<p>The <code>is_timed_hmac_valid_v0()</code> function has these parameter definitions:</p>
<ul>
<li>
<p><code>Key</code> <span class="nb-type">String literal</span></p>
<ul>
<li>Specifies the secret cryptographic key for validating the HMAC.</li>
</ul>
</li>
<li>
<p><code>MessageMAC</code> <span class="nb-type">String</span></p>
<ul>
<li>Contains a concatenation of these HMAC elements: <code>message</code>, <code>separator</code>, <code>timestamp</code>, <code>mac</code>. For a definition and an example, refer to <a href="#messagemac">MessageMAC</a>.</li>
</ul>
</li>
<li>
<p><code>ttl</code> <span class="nb-type">Integer literal</span></p>
<ul>
<li>Defines the time-to-live for the HMAC token, expressed in seconds. Determines how long the token is valid, relative to the time it was issued.</li>
</ul>
</li>
<li>
<p><code>currentTimeStamp</code> <span class="nb-type">Integer</span></p>
<ul>
<li>Represents the UNIX timestamp when Cloudflare received the request, expressed in seconds. Pass the <code>http.request.timestamp.sec</code> field as an approximate value to this argument.</li>
</ul>
</li>
<li>
<p><code>lengthOfSeparator</code> <span class="nb-type">Integer literal</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Specifies the length of the <code>separator</code> between the <code>timestamp</code> and the <code>message</code> in the <code>MessageMAC</code>. Expressed in bytes, with a default value of <code>0</code>.</li>
</ul>
</li>
<li>
<p><code>flags</code> <span class="nb-type">String literal</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>
<p>When you set this optional argument to <code>'s'</code>, the function expects the value of the Base64-encoded <code>mac</code> in the <code>MessageMAC</code> argument to use the URL-safe character set with no padding.</p>
</li>
<li>
<p>When you do <strong>not</strong> set the value of <code>flags</code> to <code>'s'</code>, you must URL encode the Base64 value for <code>mac</code> in the <code>MessageMAC</code> argument.</p>
</li>
</ul>
</li>
</ul>
<h3 id="usage">Usage</h3>
<p>The <code>is_timed_hmac_valid_v0()</code> function uses the supplied <em>Key</em> to generate a message authentication code (MAC) from the <code>message</code> and the <code>timestamp</code> regions of the MessageMAC. When the generated MAC matches the <code>mac</code> region of the MessageMAC and the token has not expired, the HMAC is valid and the function returns <code>true</code>.</p>
<p>For example, the following expression matches requests to <code>downloads.example.com</code> that do not include valid HMAC tokens:</p>
<pre><code class="language-java">http.host == &quot;downloads.example.com&quot;&#10;and not is_timed_hmac_valid_v0(&quot;mysecretkey&quot;, http.request.uri, 100000, http.request.timestamp.sec, 8)&#10;</code></pre>
<p>For examples of rules that use HMAC validation, refer to <a href="/waf/custom-rules/use-cases/configure-token-authentication/">Configure token authentication</a> in the WAF documentation.</p>
<h3 id="messagemac">MessageMAC</h3>
<p>A valid MessageMAC satisfies the following regular expression:</p>
<pre><code class="language-txt">(.+)(.*)(\d{10})-(.{43,})&#10;</code></pre>
<p>and is composed of these parentheses-delimited expressions:</p>
<table>
<thead>
<tr>
<th>Expression</th>
<th>Description</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>(.+)</code></td>
<td>The <code>message</code> to validate.</td>
<td><code>/download/cat.jpg</code></td>
</tr>
<tr>
<td><code>(.*)</code></td>
<td>The <code>separator</code> between message and timestamp, commonly a parameter name.</td>
<td><code>&amp;verify=</code></td>
</tr>
<tr>
<td><code>(\d{10})</code></td>
<td>The 10-digit UNIX <code>timestamp</code> when the MAC was issued, expressed in seconds.</td>
<td><code>1484063137</code></td>
</tr>
<tr>
<td><code>(.{43,})</code></td>
<td>A Base64-encoded version of the <code>mac</code>. When you do not set the value of the <code>urlSafe</code> argument in the HMAC validation function to <code>'s'</code>, you must URL-encode the Base64 value for <code>mac</code>. When the Base64 MAC encoding is URL-safe, the <code>mac</code> value contains 43 bytes. Otherwise, the value will be 44 bytes or more, because of URL encoding.</td>
<td><code>IaLGSmELTvlhfd0ItdN6PhhHTFhzx73EX8uy%2FcSDiIU%3D</code></td>
</tr>
</tbody>
</table>
<p>For details on generating a MessageMAC, refer to <a href="/waf/custom-rules/use-cases/configure-token-authentication/#hmac-token-generation">HMAC token generation</a>.</p>
<h2 id="hmac-validation-examples">HMAC validation examples</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13254.md")
</aside>
<h3 id="messagemac-in-a-single-field">MessageMAC in a single field</h3>
<p>Consider the case where the MessageMAC is contained entirely within a single field, as in this example URI path:</p>
<pre><code class="language-txt">/download/cat.jpg?verify=1484063787-IaLGSmELTvlhfd0ItdN6PhhHTFhzx73EX8uy%2FcSDiIU%3D&#10;</code></pre>
<p>Note how the URI maps to the elements of the MessageMAC:</p>
<table>
<thead>
<tr>
<th>Element</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>message</code></td>
<td><code>/download/cat.jpg</code></td>
</tr>
<tr>
<td><code>separator</code></td>
<td><code>?verify=</code> (with length <code>8</code>)</td>
</tr>
<tr>
<td><code>timestamp</code></td>
<td><code>1484063787</code></td>
</tr>
<tr>
<td><code>mac</code></td>
<td><code>IaLGSmELTvlhfd0ItdN6PhhHTFhzx73EX8uy%2FcSDiIU%3D</code></td>
</tr>
</tbody>
</table>
<p>When the MessageMAC is contained entirely within a single field such as <code>http.request.uri</code>, pass the field name to the <code>MessageMAC</code> argument of the HMAC validation function:</p>
<pre><code class="language-java">is_timed_hmac_valid_v0(&#10;  &quot;mysecretkey&quot;,&#10;  http.request.uri,&#10;  100000,&#10;  http.request.timestamp.sec,&#10;  8&#10;)&#10;</code></pre>
<h3 id="concatenated-messagemac-argument">Concatenated MessageMAC argument</h3>
<p>To compose a MessageMAC from more than one field, use the <a href="#concat"><code>concat()</code></a> function.</p>
<p>This example constructs the value of the <code>MessageMAC</code> argument by concatenating the request URI and two header fields:</p>
<pre><code class="language-java">is_timed_hmac_valid_v0(&#10;  &quot;mysecretkey&quot;,&#10;  concat(&#10;    http.request.uri,&#10;    http.request.headers[&quot;timestamp&quot;][0],&#10;    &quot;-&quot;,&#10;    http.request.headers[&quot;mac&quot;][0]),&#10;  100000,&#10;  http.request.timestamp.sec,&#10;  0&#10;)&#10;</code></pre>
