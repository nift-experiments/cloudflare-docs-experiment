---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/operators/
  description: Learn about comparison, logical operators, and grouping symbols in Cloudflare's Rules language. Understand precedence and how to structure expressions.
  full_title: Rule operators and grouping symbols · Cloudflare Ruleset Engine docs
  head_html: <title>Rule operators and grouping symbols · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn about comparison, logical operators, and grouping symbols in Cloudflare&#x27;s Rules language. Understand precedence and how to structure expressions."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/operators/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ruleset-engine/rules-language/operators/index.md"><meta property="og:title" content="Rule operators and grouping symbols · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about comparison, logical operators, and grouping symbols in Cloudflare&#x27;s Rules language. Understand precedence and how to structure expressions."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/operators/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Ruleset Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/operators/#page","headline":"Rule operators and grouping symbols \u00b7 Cloudflare Ruleset Engine docs","description":"Learn about comparison, logical operators, and grouping symbols in Cloudflare's Rules language. Understand precedence and how to structure expressions.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/operators/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ruleset-engine/rules-language/operators/
  schema: 1
---
<p>The Cloudflare Rules language supports comparison and logical operators:</p>
<ul>
<li><a href="#comparison-operators">Comparison operators</a> specify how values defined in an expression must relate to the actual HTTP request value for the expression to return <code>true</code>.</li>
<li><a href="#logical-operators">Logical operators</a> combine two expressions to form a compound expression and use order of precedence to determine how an expression is evaluated.</li>
</ul>
<p><a href="#grouping-symbols">Grouping symbols</a> allow you to organize expressions, enforce precedence, and nest expressions.</p>
<h2 id="comparison-operators">Comparison operators</h2>
<p>Comparison operators return <code>true</code> when a value from an HTTP request matches a value defined in an expression.</p>
<p>This is the general pattern for using comparison operators:</p>
<pre tabindex="0"><code class="language-txt">&lt;field&gt; &lt;comparison_operator&gt; &lt;value&gt;&#10;</code></pre>
<p>The Rules language supports these comparison operators:</p>
<div style="width: 100%; overflow-x: auto;">
<table style="width:100%">
<thead>
<tr>
<th>Name</th>
<th colSpan="2" style={{ textAlign: 'center' }}>Operator Notation</th>
<th colSpan="3" style={{ textAlign: 'center' }}>Supported Data Types</th>
<th></th>
</tr>
<tr>
<td></td>
<th>English</th>
<th>C-like</th>
<th>String<sup>1</sup></th>
<th>IP</th>
<th>Number</th>
<th>Example (operator in bold)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Equal</td>
<td><code>eq</code></td>
<td><code>==</code></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>
          <code>http.request.uri.path <strong>eq</strong> "/articles/2008/"</code>
</td>
</tr>
<tr>
<td>Not equal</td>
<td><code>ne</code></td>
<td><code>!=</code></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>
          <code>ip.src <strong>ne</strong> 203.0.113.0</code>
</td>
</tr>
<tr>
<td>Less than</td>
<td><code>lt</code></td>
<td><code>&lt;</code></td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
<td>
          <code>cf.waf.score <strong>lt</strong> 10</code>
</td>
</tr>
<tr>
<td>Less than<br />or equal</td>
<td><code>le</code></td>
<td><code>&lt;=</code></td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
<td>
          <code>cf.waf.score <strong>le</strong> 20</code>
</td>
</tr>
<tr>
<td>Greater than</td>
<td><code>gt</code></td>
<td><code>&gt;</code></td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
<td>
          <code>cf.waf.score <strong>gt</strong> 25</code>
</td>
</tr>
<tr>
<td>Greater than<br />or equal</td>
<td><code>ge</code></td>
<td><code>&gt;=</code></td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
<td>
          <code>cf.waf.score <strong>ge</strong> 60</code>
</td>
</tr>
<tr>
<td>Contains</td>
<td><code>contains</code></td>
<td></td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>
          <code>http.request.uri.path <strong>contains</strong> "/articles/"</code>
</td>
</tr>
<tr>
<td><a href="#wildcard-matching">Wildcard</a><br/>(case-insensitive)</td>
<td><code>wildcard</code></td>
<td></td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>
          <code>http.request.uri.path <strong>wildcard</strong> "/articles/*"</code>
</td>
</tr>
<tr>
<td><a href="#wildcard-matching">Strict wildcard</a><br/>(case-sensitive)</td>
<td><code>strict wildcard</code></td>
<td></td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>
          <code>http.request.uri.path <strong>strict wildcard</strong> "/AdminTeam/*"</code>
</td>
</tr>
<tr>
<td><a href="#regular-expression-matching">Matches<br />regex</a><sup>2</sup></td>
<td><code>matches</code></td>
<td><code>~</code></td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>
          <code>http.request.uri.path <strong>matches</strong> "^/articles/200[7-8]/$"</code>
</td>
</tr>
<tr>
<td>Is in set of values / list<sup>3</sup></td>
<td><code>in</code></td>
<td></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>
          <code>ip.src <strong>in</strong> {"{ 203.0.113.0 203.0.113.1 }"}</code><br/>
					<code>ip.src.asnum <strong>in</strong> $&lt;LIST&gt;</code>
</td>
</tr>
</tbody>
</table>
</div>
<p><sup>1</sup> All string operators are case-sensitive unless explicitly stated as case-insensitive, such as the <code>wildcard</code> operator.<br/>
<sup>2</sup> Access to the <code>matches</code> operator requires a Cloudflare Business or Enterprise plan.<br/>
<sup>3</sup> Currently, not all Cloudflare products support lists in their expressions. For more information on lists, refer to <a href="/ruleset-engine/rules-language/values/#inline-lists">Inline lists</a> and <a href="/waf/tools/lists/">Lists</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13251.md")
</aside>
<h3 id="additional-operators-in-the-cloudflare-dashboard">Additional operators in the Cloudflare dashboard</h3>
<p>The Cloudflare dashboard may show the following additional operators, depending on the exact field and the type of rule:</p>
<ul>
<li>
<p><em>starts with</em> (corresponding to the <a href="/ruleset-engine/rules-language/functions/#starts_with"><code>starts_with()</code></a> function): Returns <code>true</code> when a string starts with a given substring, and <code>false</code> otherwise.</p>
</li>
<li>
<p><em>ends with</em> (corresponding to the <a href="/ruleset-engine/rules-language/functions/#ends_with"><code>ends_with()</code></a> function): Returns <code>true</code> when a string ends with a given substring, and <code>false</code> otherwise.</p>
</li>
<li>
<p><em>is in list</em> (corresponding to <code>&lt;FIELD&gt; in $&lt;LIST_NAME&gt;</code>): Returns <code>true</code> when the field value is present in the specified <a href="/waf/tools/lists/">list</a>, and <code>false</code> otherwise. For more information, refer to <a href="/waf/tools/lists/use-in-expressions/">Use lists in expressions</a>.</p>
</li>
<li>
<p><em>is not in list</em> (corresponding to <code>not &lt;FIELD&gt; in $&lt;LIST_NAME&gt;</code>): Returns <code>true</code> when the field value is not present in the specified <a href="/waf/tools/lists/">list</a>, and <code>false</code> otherwise. For more information, refer to <a href="/waf/tools/lists/use-in-expressions/">Use lists in expressions</a>.</p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13250.md")
</aside>
<h3 id="comparing-string-values">Comparing string values</h3>
<p>String comparison in rule expressions is case-sensitive. To account for possible variations of string capitalization in an expression, you can use the <a href="/ruleset-engine/rules-language/functions/#lower"><code>lower()</code></a> function and compare the result with a lowercased string, like in the following example:</p>
<pre tabindex="0"><code class="language-txt">lower(http.request.uri.path) contains &quot;/wp-login.php&quot;&#10;</code></pre>
<p><a href="#wildcard-matching">Wildcard matching</a> is only supported with the <code>wildcard</code> and <code>strict wildcard</code> operators, and <a href="#regular-expression-matching">regular expression matching</a> is only supported with the <code>matches</code> operator.</p>
<h3 id="wildcard-matching">Wildcard matching</h3>
<p>The <code>wildcard</code> operator performs a case-insensitive match between a field value and a literal string containing zero or more <code>*</code> metacharacters. Each <code>*</code> metacharacter represents zero or more characters. The <code>strict wildcard</code> operator performs a similar match, but is case-sensitive.</p>
<p>When using the <code>wildcard</code>/<code>strict wildcard</code> operator, the entire field value must match the literal string with wildcards (the literal after the operator).</p>
<pre tabindex="0"><code class="language-txt">&#35; The following expression:&#10;http.request.full_uri wildcard &quot;http*://example.com/a/*&quot;&#10;&#10;&#35; Would match the following URIs:&#10;&#35; - https://example.com/a/           (the &#x27;*&#x27; matches zero characters)&#10;&#35; - http://example.com/a/&#10;&#35; - https://example.com/a/page.html&#10;&#35; - https://example.com/a/sub/folder/?name=value&#10;&#10;&#35; Would NOT match the following URIs:&#10;&#35; - https://example.com/ab/&#10;&#35; - https://example.com/b/page.html&#10;&#35; - https://sub.example.com/a/&#10;</code></pre>
<details class="nb-details"><summary>Example B</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13252.md")
</div></details>
<details class="nb-details"><summary>Example C</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13253.md")
</div></details>
<p>The matching algorithm used by the <code>wildcard</code> operator is case-insensitive. To perform case-sensitive wildcard matching, use the <code>strict wildcard</code> operator.</p>
<p>To enter a literal <code>*</code> character in a literal string with wildcards you must escape it using <code>\*</code>. Additionally, you must also escape <code>\</code> using <code>\\</code>. Two unescaped <code>*</code> characters in a row (<code>**</code>) in a wildcard literal string are considered invalid and cannot be used. If you need to perform character escaping, it is recommended that you use the <a href="/ruleset-engine/rules-language/values/#raw-string-syntax">raw string syntax</a> to specify a literal string with wildcards.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="wildcard-matching-versus-regex-matching">Wildcard matching versus regex matching</h3>
@markup("md", "content/.markup/bodies/13249.md")
</aside>
<h3 id="regular-expression-matching">Regular expression matching</h3>
<p>Customers on Business and Enterprise plans have access to the <code>matches</code> operator. Regular expression matching is performed using the Rust regular expression engine.</p>
<p>If you are using a regular expression, you can test it using a tool like <a href="https://regex101.com/?flavor=rust&amp;regex=">Regular Expressions 101</a> or <a href="https://rustexp.lpil.uk/">Rustexp</a>.</p>
<p>For more information on regular expressions, refer to <a href="/ruleset-engine/rules-language/values/#string-values-and-regular-expressions">String values and regular expressions</a>.</p>
<h2 id="logical-operators">Logical operators</h2>
<p>Logical operators combine two or more expressions into a single compound expression. A compound expression has this general syntax:</p>
<pre tabindex="0"><code class="language-txt">&lt;expression&gt; &lt;logical_operator&gt; &lt;expression&gt;&#10;</code></pre>
<h3 id="supported-logical-operators">Supported logical operators</h3>
<p>Each logical operator has an <a href="#order-of-precedence">order of precedence</a>. The order of precedence (along with <a href="#grouping-symbols">grouping symbols</a>) determines the order in which Cloudflare evaluates logical operators in an expression. The <code>not</code> operator ranks first in order of precedence.</p>
<div style={{ width: "100%" }}>
<table style={{ width: "100%" }}>
<thead>
<tr>
<th>Name</th>
<th>English<br />Notation</th>
<th>C-like<br />Notation</th>
<th>Example</th>
<th>Order of Precedence</th>
</tr>
</thead>
<tbody>
<tr>
<td>Logical NOT</td>
<td><code>not</code></td>
<td><code>!</code></td>
<td>
          <code><strong>not</strong> ( http.host eq "www<span>&#8203;</span>.cloudflare<span>&#8203;</span>.com" and ip.src in {"{203.0.113.0/24}"} )</code>
</td>
<td>1</td>
</tr>
<tr>
<td>Logical AND</td>
<td><code>and</code></td>
<td><code>&amp;&amp;</code></td>
<td>
          <code>http.host eq "www<span>&#8203;</span>.cloudflare<span>&#8203;</span>.com" <strong>and</strong> ip.src in {"{203.0.113.0/24}"}</code>
</td>
<td>2</td>
</tr>
<tr>
<td>Logical XOR<br />(exclusive OR)</td>
<td><code>xor</code></td>
<td><code>^^</code></td>
<td>
          <code>http.host eq "www<span>&#8203;</span>.cloudflare<span>&#8203;</span>.com" <strong>xor</strong> ip.src in {"{203.0.113.0/24}"}</code>
</td>
<td>3</td>
</tr>
<tr>
<td>Logical OR</td>
<td><code>or</code></td>
<td><code>||</code></td>
<td>
          <code>http.host eq "www<span>&#8203;</span>.cloudflare<span>&#8203;</span>.com" <strong>or</strong> ip.src in 203.0.113.0/24</code>
</td>
<td>4</td>
</tr>
</tbody>
</table>
</div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13248.md")
</aside>
<h3 id="order-of-precedence">Order of precedence</h3>
<p>When writing compound expressions, it is important to be aware of the precedence of logical operators so that your expression is evaluated the way you expect.</p>
<p>For example, consider the following generic expression, which uses <code>and</code> and <code>or</code> operators:</p>
<pre tabindex="0"><code class="language-java">Expression1 and Expression2 or Expression3&#10;</code></pre>
<p>If these operators had no order of precedence, it would not be clear which of two interpretations is correct:</p>
<ol>
<li>Match when Expression 1 and Expression 2 are both true <strong>or</strong> when Expression 3 is true.</li>
<li>Match when Expression 1 is true <strong>and</strong> either Expression 2 or Expression 3 is true.</li>
</ol>
<p>Since the logical <code>and</code> operator has precedence over logical <code>or</code>, the <code>and</code> operator must be evaluated first. Interpretation 1 is correct.</p>
<p>To avoid ambiguity when working with logical operators, use grouping symbols so that the order of evaluation is explicit.</p>
<h2 id="grouping-symbols">Grouping symbols</h2>
<p>The Rules language supports parentheses (<code>(</code>,<code>)</code>) as grouping symbols. Grouping symbols allow you to organize expressions, enforce precedence, and nest expressions.</p>
<p>Only the <a href="/ruleset-engine/rules-language/expressions/edit-expressions/#expression-editor">Expression Editor</a> and the <a href="/api/">Cloudflare API</a> support grouping symbols. The <a href="/ruleset-engine/rules-language/expressions/edit-expressions/#expression-builder">Expression Builder</a> does not.</p>
<h3 id="group-expressions">Group expressions</h3>
<p>Use parentheses to explicitly group expressions that should be evaluated together. In this example, the parentheses do not alter the evaluation of the expression, but they unambiguously call out which logical operators to evaluate first.</p>
<pre tabindex="0"><code class="language-java">(Expression1 and Expression2) or Expression3&#10;</code></pre>
<p>Because grouping symbols are so explicit, you are less likely to make errors when you use them to write compound expressions.</p>
<h3 id="enforce-precedence">Enforce precedence</h3>
<p>Grouping symbols are a powerful tool to enforce precedence for grouped elements of a compound expression. In this example, parentheses force the logical <code>or</code> operator to be evaluated before the logical <code>and</code>:</p>
<pre tabindex="0"><code class="language-java">Expression1 and (Expression2 or Expression3)&#10;</code></pre>
<p>Without parentheses, the logical <code>and</code> operator would take precedence.</p>
<h3 id="nest-expressions">Nest expressions</h3>
<p>You can nest expressions grouped by parentheses inside other groups to create very precise, sophisticated expressions, such as this example for a rule designed to block access to a domain:</p>
<pre tabindex="0"><code class="language-sql">(&#10; (http.host eq &quot;api.example.com&quot; and http.request.uri.path eq &quot;/api/v2/auth&quot;) or&#10; (http.host matches &quot;^(www|store|blog)\.example\.com&quot; and http.request.uri.path contains &quot;wp-login.php&quot;) or&#10; ip.src.country in {&quot;CN&quot; &quot;TH&quot; &quot;US&quot; &quot;ID&quot; &quot;KR&quot; &quot;MY&quot; &quot;IT&quot; &quot;SG&quot; &quot;GB&quot;} or ip.src.asnum in {12345 54321 11111}&#10;) and not ip.src in {11.22.33.0/24}&#10;</code></pre>
<p>Note that when evaluating the precedence of logical operators, parentheses inside strings delimited by quotes are ignored, such as those in the following regular expression, drawn from the example above:</p>
<pre tabindex="0"><code class="language-sql">&quot;^(www|store|blog)\.example\.com&quot;&#10;</code></pre>
