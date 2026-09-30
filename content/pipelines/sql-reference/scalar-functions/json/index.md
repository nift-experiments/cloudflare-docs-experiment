---
cp9:
  canonical: https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/json/
  description: Scalar functions for manipulating JSON
  full_title: JSON functions · Cloudflare Pipelines Docs
  head_html: <title>JSON functions · Cloudflare Pipelines Docs</title><meta name="generator" content="Nift"><meta name="description" content="Scalar functions for manipulating JSON"><link rel="canonical" href="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/json/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/json/index.md"><meta property="og:title" content="JSON functions · Cloudflare Pipelines Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Scalar functions for manipulating JSON"><meta property="og:url" content="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/json/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pipelines"><meta name="algolia_product_filter" content="Pipelines"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_additional_products" content="Pipelines"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/json/#page","headline":"JSON functions \u00b7 Cloudflare Pipelines Docs","description":"Scalar functions for manipulating JSON","url":"https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/json/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pipelines/sql-reference/scalar-functions/json/
  schema: 1
---
<p>Cloudflare Pipelines provides two set of JSON functions, the first based on PostgreSQL's SQL
functions and syntax, and the second based on the
<a href="https://jsonpath.com/">JSONPath</a> standard.</p>
<h2 id="sql-functions">SQL functions</h2>
<p>The SQL functions provide basic JSON parsing functions similar to those found in
PostgreSQL.</p>
<h3 id="json-contains">json_contains</h3>
<p>Returns <code>true</code> if the JSON string contains the specified key(s).</p>
<pre tabindex="0"><code class="language-sql">SELECT json_contains(&#x27;{&quot;a&quot;: 1, &quot;b&quot;: 2, &quot;c&quot;: 3}&#x27;, &#x27;a&#x27;) FROM source;&#10;true&#10;</code></pre>
<p>Also available via the <code>?</code> operator:</p>
<pre tabindex="0"><code class="language-sql">SELECT &#x27;{&quot;a&quot;: 1, &quot;b&quot;: 2, &quot;c&quot;: 3}&#x27; ? &#x27;a&#x27; FROM source;&#10;true&#10;</code></pre>
<h3 id="json-get">json_get</h3>
<p>Retrieves the value from a JSON string by the specified path (keys). Returns the
value as its native type (string, int, etc.).</p>
<pre tabindex="0"><code class="language-sql">SELECT json_get(&#x27;{&quot;a&quot;: {&quot;b&quot;: 2}}&#x27;, &#x27;a&#x27;, &#x27;b&#x27;) FROM source;&#10;2&#10;</code></pre>
<p>Also available via the <code>-&gt;</code> operator:</p>
<pre tabindex="0"><code class="language-sql">SELECT &#x27;{&quot;a&quot;: {&quot;b&quot;: 2}}&#x27;-&gt;&#x27;a&#x27;-&gt;&#x27;b&#x27; FROM source;&#10;2&#10;</code></pre>
<p>Various permutations of <code>json_get</code> functions are available for retrieving values as
a specific type, or you can use SQL type annotations:</p>
<pre tabindex="0"><code class="language-sql">SELECT json_get(&#x27;{&quot;a&quot;: {&quot;b&quot;: 2}}&#x27;, &#x27;a&#x27;, &#x27;b&#x27;)::int FROM source;&#10;2&#10;</code></pre>
<h3 id="json-get-str">json_get_str</h3>
<p>Retrieves a string value from a JSON string by the specified path. Returns an
empty string if the value does not exist or is not a string.</p>
<pre tabindex="0"><code class="language-sql">SELECT json_get_str(&#x27;{&quot;a&quot;: {&quot;b&quot;: &quot;hello&quot;}}&#x27;, &#x27;a&#x27;, &#x27;b&#x27;) FROM source;&#10;&quot;hello&quot;&#10;</code></pre>
<h3 id="json-get-int">json_get_int</h3>
<p>Retrieves an integer value from a JSON string by the specified path. Returns <code>0</code>
if the value does not exist or is not an integer.</p>
<pre tabindex="0"><code class="language-sql">SELECT json_get_int(&#x27;{&quot;a&quot;: {&quot;b&quot;: 42}}&#x27;, &#x27;a&#x27;, &#x27;b&#x27;) FROM source;&#10;42&#10;</code></pre>
<h3 id="json-get-float">json_get_float</h3>
<p>Retrieves a float value from a JSON string by the specified path. Returns <code>0.0</code>
if the value does not exist or is not a float.</p>
<pre tabindex="0"><code class="language-sql">SELECT json_get_float(&#x27;{&quot;a&quot;: {&quot;b&quot;: 3.14}}&#x27;, &#x27;a&#x27;, &#x27;b&#x27;) FROM source;&#10;3.14&#10;</code></pre>
<h3 id="json-get-bool">json_get_bool</h3>
<p>Retrieves a boolean value from a JSON string by the specified path. Returns
<code>false</code> if the value does not exist or is not a boolean.</p>
<pre tabindex="0"><code class="language-sql">SELECT json_get_bool(&#x27;{&quot;a&quot;: {&quot;b&quot;: true}}&#x27;, &#x27;a&#x27;, &#x27;b&#x27;) FROM source;&#10;true&#10;</code></pre>
<h3 id="json-get-json">json_get_json</h3>
<p>Retrieves a nested JSON string from a JSON string by the specified path. The
value is returned as raw JSON.</p>
<pre tabindex="0"><code class="language-sql">SELECT json_get_json(&#x27;{&quot;a&quot;: {&quot;b&quot;: {&quot;c&quot;: 1}}}&#x27;, &#x27;a&#x27;, &#x27;b&#x27;) FROM source;&#10;&#x27;{&quot;c&quot;: 1}&#x27;&#10;</code></pre>
<h3 id="json-as-text">json_as_text</h3>
<p>Retrieves any value from a JSON string by the specified path and returns it as a
string, regardless of the original type.</p>
<pre tabindex="0"><code class="language-sql">SELECT json_as_text(&#x27;{&quot;a&quot;: {&quot;b&quot;: 42}}&#x27;, &#x27;a&#x27;, &#x27;b&#x27;) FROM source;&#10;&quot;42&quot;&#10;</code></pre>
<p>Also available via the <code>-&gt;&gt;</code> operator:</p>
<pre tabindex="0"><code class="language-sql">SELECT &#x27;{&quot;a&quot;: {&quot;b&quot;: 42}}&#x27;-&gt;&gt;&#x27;a&#x27;-&gt;&gt;&#x27;b&#x27; FROM source;&#10;&quot;42&quot;&#10;</code></pre>
<h3 id="json-length">json_length</h3>
<p>Returns the length of a JSON object or array at the specified path. Returns <code>0</code>
if the path does not exist or is not an object/array.</p>
<pre tabindex="0"><code class="language-sql">SELECT json_length(&#x27;{&quot;a&quot;: [1, 2, 3]}&#x27;, &#x27;a&#x27;) FROM source;&#10;3&#10;</code></pre>
<h2 id="json-path-functions">Json path functions</h2>
<p>JSON functions provide basic json parsing functions using
<a href="https://goessner.net/articles/JsonPath/">JsonPath</a>, an evolving standard for
querying JSON objects.</p>
<h3 id="extract-json">extract_json</h3>
<p>Returns the JSON elements in the first argument that match the JsonPath in the second argument.
The returned value is an array of json strings.</p>
<pre tabindex="0"><code class="language-sql">SELECT extract_json(&#x27;{&quot;a&quot;: 1, &quot;b&quot;: 2, &quot;c&quot;: 3}&#x27;, &#x27;$.a&#x27;) FROM source;&#10;[&#x27;1&#x27;]&#10;</code></pre>
<h3 id="extract-json-string">extract_json_string</h3>
<p>Returns an unescaped String for the first item matching the JsonPath, if it is a string.</p>
<pre tabindex="0"><code class="language-sql">SELECT extract_json_string(&#x27;{&quot;a&quot;: &quot;a&quot;, &quot;b&quot;: 2, &quot;c&quot;: 3}&#x27;, &#x27;$.a&#x27;) FROM source;&#10;&#x27;a&#x27;&#10;</code></pre>
