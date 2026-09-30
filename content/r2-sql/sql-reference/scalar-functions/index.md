---
cp9:
  canonical: https://developers.cloudflare.com/r2-sql/sql-reference/scalar-functions/
  description: Reference for the scalar functions supported in R2 SQL, organized by category.
  full_title: Scalar functions · R2 SQL docs
  head_html: <title>Scalar functions · R2 SQL docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference for the scalar functions supported in R2 SQL, organized by category."><link rel="canonical" href="https://developers.cloudflare.com/r2-sql/sql-reference/scalar-functions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2-sql/sql-reference/scalar-functions/index.md"><meta property="og:title" content="Scalar functions · R2 SQL docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference for the scalar functions supported in R2 SQL, organized by category."><meta property="og:url" content="https://developers.cloudflare.com/r2-sql/sql-reference/scalar-functions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2 SQL"><meta name="algolia_product_filter" content="R2 SQL"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="R2 SQL"><meta name="pcx_tags" content="SQL"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2-sql/sql-reference/scalar-functions/#page","headline":"Scalar functions \u00b7 R2 SQL docs","description":"Reference for the scalar functions supported in R2 SQL, organized by category.","url":"https://developers.cloudflare.com/r2-sql/sql-reference/scalar-functions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SQL"]}</script>
  markdown: true
  noindex: false
  route: /r2-sql/sql-reference/scalar-functions/
  schema: 1
---
<p>Scalar functions transform individual values and can be used in <code>SELECT</code>, <code>WHERE</code>, <code>GROUP BY</code>, <code>HAVING</code>, and <code>ORDER BY</code> clauses.</p>
<hr />
<h2 id="core-functions">Core functions</h2>
<h3 id="arrow-cast">arrow_cast</h3>
<p>Casts an expression to a specific Arrow data type by string name.</p>
<pre tabindex="0"><code class="language-sql">SELECT arrow_cast(total_amount, &#x27;Float32&#x27;) AS amount_f32&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL&#10;LIMIT 1&#10;</code></pre>
<h3 id="arrow-typeof">arrow_typeof</h3>
<p>Returns the Arrow data type name of an expression.</p>
<pre tabindex="0"><code class="language-sql">SELECT arrow_typeof(total_amount) AS amount_type,&#10;       arrow_typeof(customer_id) AS id_type&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="coalesce">coalesce</h3>
<p>Returns the first non-NULL argument.</p>
<pre tabindex="0"><code class="language-sql">SELECT coalesce(department, region, &#x27;unknown&#x27;) AS first_val&#10;FROM my_namespace.sales_data&#10;LIMIT 5&#10;</code></pre>
<h3 id="get-field">get_field</h3>
<p>Extracts a field from a struct by name.</p>
<pre tabindex="0"><code class="language-sql">SELECT get_field(named_struct(&#x27;customer&#x27;, customer_id, &#x27;amount&#x27;, total_amount), &#x27;amount&#x27;) AS amt&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL&#10;LIMIT 1&#10;</code></pre>
<h3 id="greatest">greatest</h3>
<p>Returns the largest value from a list of arguments.</p>
<pre tabindex="0"><code class="language-sql">SELECT greatest(total_amount, unit_price, quantity) AS max_val&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="least">least</h3>
<p>Returns the smallest value from a list of arguments.</p>
<pre tabindex="0"><code class="language-sql">SELECT least(total_amount, unit_price, quantity) AS min_val&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="named-struct">named_struct</h3>
<p>Creates a struct with named fields from key-value pairs.</p>
<pre tabindex="0"><code class="language-sql">SELECT named_struct(&#x27;customer&#x27;, customer_id, &#x27;amount&#x27;, total_amount) AS info&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL&#10;LIMIT 1&#10;</code></pre>
<h3 id="nullif">nullif</h3>
<p>Returns NULL if both arguments are equal, otherwise returns the first argument.</p>
<pre tabindex="0"><code class="language-sql">SELECT nullif(department, &#x27;Unknown&#x27;) AS dept&#10;FROM my_namespace.sales_data&#10;LIMIT 5&#10;</code></pre>
<h3 id="nvl">nvl</h3>
<p>Returns the second argument if the first is NULL. Alias: <code>ifnull</code>.</p>
<pre tabindex="0"><code class="language-sql">SELECT nvl(department, &#x27;N/A&#x27;) AS dept&#10;FROM my_namespace.sales_data&#10;LIMIT 5&#10;</code></pre>
<h3 id="nvl2">nvl2</h3>
<p>Returns the second argument if the first is not NULL, otherwise returns the third.</p>
<pre tabindex="0"><code class="language-sql">SELECT nvl2(department, &#x27;has_dept&#x27;, &#x27;no_dept&#x27;) AS dept_status&#10;FROM my_namespace.sales_data&#10;LIMIT 5&#10;</code></pre>
<h3 id="overlay">overlay</h3>
<p>Replaces a substring at a given position.</p>
<pre tabindex="0"><code class="language-sql">SELECT customer_id,&#10;       overlay(customer_id PLACING &#x27;XX&#x27; FROM 1 FOR 2) AS masked&#10;FROM my_namespace.sales_data&#10;LIMIT 3&#10;</code></pre>
<h3 id="struct">struct</h3>
<p>Creates a struct with positional fields. Alias: <code>row</code>.</p>
<pre tabindex="0"><code class="language-sql">SELECT struct(customer_id, total_amount, region) AS info&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL&#10;LIMIT 1&#10;</code></pre>
<hr />
<h2 id="crypto-functions">Crypto functions</h2>
<h3 id="digest">digest</h3>
<p>Returns a hash of a string using a specified algorithm. Supported algorithms: <code>md5</code>, <code>sha224</code>, <code>sha256</code>, <code>sha384</code>, <code>sha512</code>.</p>
<pre tabindex="0"><code class="language-sql">SELECT customer_id, digest(customer_id, &#x27;sha256&#x27;) AS hash&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="md5">md5</h3>
<p>Returns the MD5 hash of a string.</p>
<pre tabindex="0"><code class="language-sql">SELECT customer_id, md5(customer_id) AS hash&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="sha224">sha224</h3>
<p>Returns the SHA-224 hash of a string.</p>
<pre tabindex="0"><code class="language-sql">SELECT sha224(customer_id) AS hash&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="sha256">sha256</h3>
<p>Returns the SHA-256 hash of a string.</p>
<pre tabindex="0"><code class="language-sql">SELECT customer_id, sha256(customer_id) AS hash&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="sha384">sha384</h3>
<p>Returns the SHA-384 hash of a string.</p>
<pre tabindex="0"><code class="language-sql">SELECT sha384(customer_id) AS hash&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="sha512">sha512</h3>
<p>Returns the SHA-512 hash of a string.</p>
<pre tabindex="0"><code class="language-sql">SELECT sha512(customer_id) AS hash&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<hr />
<h2 id="datetime-functions">Datetime functions</h2>
<h3 id="current-date">current_date</h3>
<p>Returns today's date. Alias: <code>today</code>.</p>
<pre tabindex="0"><code class="language-sql">SELECT current_date() AS today_date&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="current-time">current_time</h3>
<p>Returns the current time. Precision is quantized to 10ms boundaries.</p>
<pre tabindex="0"><code class="language-sql">SELECT current_time() AS now_time&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="date-bin">date_bin</h3>
<p>Bins a timestamp into fixed-size intervals aligned to an origin.</p>
<pre tabindex="0"><code class="language-sql">SELECT date_bin(INTERVAL &#x27;1 hour&#x27;, timestamp, &#x27;2025-01-01T00:00:00Z&#x27;) AS hour_bin,&#10;       COUNT(*) AS cnt&#10;FROM my_namespace.sales_data&#10;GROUP BY date_bin(INTERVAL &#x27;1 hour&#x27;, timestamp, &#x27;2025-01-01T00:00:00Z&#x27;)&#10;ORDER BY hour_bin&#10;LIMIT 5&#10;</code></pre>
<h3 id="date-part">date_part</h3>
<p>Extracts a component from a timestamp. Alias: <code>datepart</code>.</p>
<p>Supported fields: <code>year</code>, <code>month</code>, <code>day</code>, <code>hour</code>, <code>minute</code>, <code>second</code>, <code>millisecond</code>, <code>microsecond</code>, <code>week</code>, <code>dow</code>, <code>doy</code>, <code>quarter</code>, <code>epoch</code>.</p>
<pre tabindex="0"><code class="language-sql">SELECT date_part(&#x27;hour&#x27;, timestamp) AS hr,&#10;       date_part(&#x27;minute&#x27;, timestamp) AS mn&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="date-trunc">date_trunc</h3>
<p>Truncates a timestamp to a specified unit. Alias: <code>datetrunc</code>.</p>
<p>Supported units: <code>year</code>, <code>month</code>, <code>week</code>, <code>day</code>, <code>hour</code>, <code>minute</code>, <code>second</code>.</p>
<pre tabindex="0"><code class="language-sql">SELECT date_trunc(&#x27;day&#x27;, timestamp) AS day_trunc, COUNT(*) AS cnt&#10;FROM my_namespace.sales_data&#10;GROUP BY date_trunc(&#x27;day&#x27;, timestamp)&#10;ORDER BY day_trunc&#10;LIMIT 5&#10;</code></pre>
<h3 id="from-unixtime">from_unixtime</h3>
<p>Converts a Unix epoch (seconds) to a timestamp.</p>
<pre tabindex="0"><code class="language-sql">SELECT from_unixtime(1770000000) AS ts&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="make-date">make_date</h3>
<p>Constructs a date from year, month, and day components.</p>
<pre tabindex="0"><code class="language-sql">SELECT make_date(2026, 3, 1) AS d&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="make-time">make_time</h3>
<p>Constructs a time from hour, minute, and second components.</p>
<pre tabindex="0"><code class="language-sql">SELECT make_time(14, 30, 0) AS t&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="now">now</h3>
<p>Returns the current timestamp. Aliases: <code>current_timestamp</code>.</p>
<p>Precision is quantized to 10ms boundaries.</p>
<pre tabindex="0"><code class="language-sql">SELECT now() AS current_ts&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="to-char">to_char</h3>
<p>Formats a timestamp as a string using strftime format. Alias: <code>date_format</code>.</p>
<pre tabindex="0"><code class="language-sql">SELECT to_char(timestamp, &#x27;%Y-%m-%d %H:%M&#x27;) AS formatted&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="to-date">to_date</h3>
<p>Parses a date from a string using a format pattern.</p>
<pre tabindex="0"><code class="language-sql">SELECT to_date(&#x27;2026-03-01&#x27;, &#x27;%Y-%m-%d&#x27;) AS d&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="to-local-time">to_local_time</h3>
<p>Strips timezone information from a timestamp.</p>
<pre tabindex="0"><code class="language-sql">SELECT to_local_time(timestamp) AS local_ts&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="to-time">to_time</h3>
<p>Parses a time from a string using a format pattern.</p>
<pre tabindex="0"><code class="language-sql">SELECT to_time(&#x27;14:30:00&#x27;, &#x27;%H:%M:%S&#x27;) AS t&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="to-timestamp">to_timestamp</h3>
<p>Parses a timestamp from a string using a format pattern.</p>
<pre tabindex="0"><code class="language-sql">SELECT to_timestamp(&#x27;2026-03-01 12:00:00&#x27;, &#x27;%Y-%m-%d %H:%M:%S&#x27;) AS ts&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="to-timestamp-micros">to_timestamp_micros</h3>
<p>Converts microseconds since Unix epoch to a timestamp.</p>
<pre tabindex="0"><code class="language-sql">SELECT to_timestamp_micros(1770000000000000) AS ts&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="to-timestamp-millis">to_timestamp_millis</h3>
<p>Converts milliseconds since Unix epoch to a timestamp.</p>
<pre tabindex="0"><code class="language-sql">SELECT to_timestamp_millis(1770000000000) AS ts&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="to-timestamp-nanos">to_timestamp_nanos</h3>
<p>Converts nanoseconds since Unix epoch to a timestamp. Large values may overflow.</p>
<pre tabindex="0"><code class="language-sql">SELECT to_timestamp_nanos(1770000000000000000) AS ts&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="to-timestamp-seconds">to_timestamp_seconds</h3>
<p>Converts seconds since Unix epoch to a timestamp.</p>
<pre tabindex="0"><code class="language-sql">SELECT to_timestamp_seconds(1770000000) AS ts&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="to-unixtime">to_unixtime</h3>
<p>Converts a timestamp to a Unix epoch (seconds).</p>
<pre tabindex="0"><code class="language-sql">SELECT to_unixtime(timestamp) AS epoch&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<hr />
<h2 id="encoding-functions">Encoding functions</h2>
<h3 id="decode">decode</h3>
<p>Decodes a string to binary data. Supported encoding: <code>base64</code>.</p>
<pre tabindex="0"><code class="language-sql">SELECT decode(&#x27;aGVsbG8=&#x27;, &#x27;base64&#x27;) AS raw&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="encode">encode</h3>
<p>Encodes binary data to a string. Supported encoding: <code>base64</code>.</p>
<pre tabindex="0"><code class="language-sql">SELECT encode(CAST(&#x27;hello&#x27; AS BYTEA), &#x27;base64&#x27;) AS b64&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<hr />
<h2 id="json-functions">JSON functions</h2>
<h3 id="json-as-text">json_as_text</h3>
<p>Returns any JSON value as unquoted text.</p>
<pre tabindex="0"><code class="language-sql">SELECT json_as_text(doc, &#x27;description&#x27;) AS description&#10;FROM my_namespace.sales_data&#10;LIMIT 5&#10;</code></pre>
<h3 id="json-contains">json_contains</h3>
<p>Returns true if the specified key path exists in the JSON.</p>
<pre tabindex="0"><code class="language-sql">SELECT customer_id, json_contains(doc, &#x27;email&#x27;) AS has_email&#10;FROM my_namespace.sales_data&#10;LIMIT 5&#10;</code></pre>
<h3 id="json-get">json_get</h3>
<p>Extracts a value by key path. Returns a union type — use the typed variants (<code>json_get_str</code>, <code>json_get_int</code>, etc.) for predictable results.</p>
<pre tabindex="0"><code class="language-sql">SELECT json_get(doc, &#x27;name&#x27;) AS name&#10;FROM my_namespace.sales_data&#10;LIMIT 5&#10;</code></pre>
<h3 id="json-get-array">json_get_array</h3>
<p>Returns a JSON array as a list of strings.</p>
<pre tabindex="0"><code class="language-sql">SELECT json_get_array(doc, &#x27;tags&#x27;) AS tags&#10;FROM my_namespace.sales_data&#10;LIMIT 5&#10;</code></pre>
<h3 id="json-get-bool">json_get_bool</h3>
<p>Returns a boolean value from a JSON column by key path.</p>
<pre tabindex="0"><code class="language-sql">SELECT json_get_bool(doc, &#x27;active&#x27;) AS is_active&#10;FROM my_namespace.sales_data&#10;LIMIT 5&#10;</code></pre>
<h3 id="json-get-float">json_get_float</h3>
<p>Returns a float value from a JSON column by key path.</p>
<pre tabindex="0"><code class="language-sql">SELECT json_get_float(doc, &#x27;price&#x27;) AS price&#10;FROM my_namespace.sales_data&#10;LIMIT 5&#10;</code></pre>
<h3 id="json-get-int">json_get_int</h3>
<p>Returns an integer value from a JSON column by key path.</p>
<pre tabindex="0"><code class="language-sql">SELECT json_get_int(doc, &#x27;age&#x27;) AS age&#10;FROM my_namespace.sales_data&#10;LIMIT 5&#10;</code></pre>
<h3 id="json-get-json">json_get_json</h3>
<p>Returns nested JSON as a raw JSON string.</p>
<pre tabindex="0"><code class="language-sql">SELECT json_get_json(doc, &#x27;metadata&#x27;) AS metadata&#10;FROM my_namespace.sales_data&#10;LIMIT 5&#10;</code></pre>
<h3 id="json-get-str">json_get_str</h3>
<p>Returns a string value from a JSON column by key path.</p>
<pre tabindex="0"><code class="language-sql">SELECT json_get_str(doc, &#x27;name&#x27;) AS name&#10;FROM my_namespace.sales_data&#10;LIMIT 5&#10;</code></pre>
<h3 id="json-length">json_length</h3>
<p>Returns the length of a JSON array or object.</p>
<pre tabindex="0"><code class="language-sql">SELECT json_length(doc, &#x27;items&#x27;) AS item_count&#10;FROM my_namespace.sales_data&#10;LIMIT 5&#10;</code></pre>
<hr />
<h2 id="math-functions">Math functions</h2>
<h3 id="abs">abs</h3>
<p>Returns the absolute value of a number.</p>
<pre tabindex="0"><code class="language-sql">SELECT abs(total_amount - 500) AS distance_from_500&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="cbrt">cbrt</h3>
<p>Returns the cube root of a number.</p>
<pre tabindex="0"><code class="language-sql">SELECT cbrt(CAST(quantity AS DOUBLE)) AS cbrt_qty&#10;FROM my_namespace.sales_data&#10;WHERE quantity IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="ceil">ceil</h3>
<p>Returns the smallest integer greater than or equal to a number.</p>
<pre tabindex="0"><code class="language-sql">SELECT ceil(total_amount) AS rounded_up&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="degrees">degrees</h3>
<p>Converts radians to degrees.</p>
<pre tabindex="0"><code class="language-sql">SELECT degrees(pi()) AS full_circle&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="exp">exp</h3>
<p>Returns <em>e</em> raised to the given power.</p>
<pre tabindex="0"><code class="language-sql">SELECT exp(total_amount / 1000.0) AS exp_val&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="factorial">factorial</h3>
<p>Returns the factorial of a non-negative integer.</p>
<pre tabindex="0"><code class="language-sql">SELECT factorial(5) AS fact5&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="floor">floor</h3>
<p>Returns the largest integer less than or equal to a number.</p>
<pre tabindex="0"><code class="language-sql">SELECT floor(total_amount) AS rounded_down&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="gcd">gcd</h3>
<p>Returns the greatest common divisor of two integers.</p>
<pre tabindex="0"><code class="language-sql">SELECT gcd(12, 8) AS gcd_val&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="hyperbolic-functions">Hyperbolic functions</h3>
<p><code>sinh</code>, <code>cosh</code>, <code>tanh</code>, <code>asinh</code>, <code>acosh</code>, <code>atanh</code></p>
<pre tabindex="0"><code class="language-sql">SELECT sinh(1.0) AS sh, cosh(1.0) AS ch, tanh(1.0) AS th&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="isnan">isnan</h3>
<p>Returns true if the value is NaN.</p>
<pre tabindex="0"><code class="language-sql">SELECT isnan(0.0 / 0.0) AS is_nan&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="iszero">iszero</h3>
<p>Returns true if the value is zero.</p>
<pre tabindex="0"><code class="language-sql">SELECT iszero(0.0) AS is_zero&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="lcm">lcm</h3>
<p>Returns the least common multiple of two integers.</p>
<pre tabindex="0"><code class="language-sql">SELECT lcm(4, 6) AS lcm_val&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="ln">ln</h3>
<p>Returns the natural logarithm.</p>
<pre tabindex="0"><code class="language-sql">SELECT ln(total_amount) AS ln_val&#10;FROM my_namespace.sales_data&#10;WHERE total_amount &gt; 0&#10;LIMIT 5&#10;</code></pre>
<h3 id="log">log</h3>
<p>Returns the logarithm of a value for a given base.</p>
<pre tabindex="0"><code class="language-sql">SELECT log(10.0, total_amount) AS log10_val&#10;FROM my_namespace.sales_data&#10;WHERE total_amount &gt; 0&#10;LIMIT 5&#10;</code></pre>
<h3 id="log2">log2</h3>
<p>Returns the base-2 logarithm.</p>
<pre tabindex="0"><code class="language-sql">SELECT log2(total_amount) AS log2_val&#10;FROM my_namespace.sales_data&#10;WHERE total_amount &gt; 0&#10;LIMIT 5&#10;</code></pre>
<h3 id="log10">log10</h3>
<p>Returns the base-10 logarithm.</p>
<pre tabindex="0"><code class="language-sql">SELECT log10(total_amount) AS log10_val&#10;FROM my_namespace.sales_data&#10;WHERE total_amount &gt; 0&#10;LIMIT 5&#10;</code></pre>
<h3 id="nanvl">nanvl</h3>
<p>Returns the first argument if it is not NaN, otherwise returns the second.</p>
<pre tabindex="0"><code class="language-sql">SELECT nanvl(0.0 / 0.0, -1.0) AS safe_val&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="pi">pi</h3>
<p>Returns the value of pi.</p>
<pre tabindex="0"><code class="language-sql">SELECT pi() AS pi_val&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="power">power</h3>
<p>Raises a number to a power. Alias: <code>pow</code>.</p>
<pre tabindex="0"><code class="language-sql">SELECT power(total_amount, 2.0) AS amount_squared&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="radians">radians</h3>
<p>Converts degrees to radians.</p>
<pre tabindex="0"><code class="language-sql">SELECT radians(180.0) AS pi_val&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="random">random</h3>
<p>Returns a random float between 0 and 1.</p>
<pre tabindex="0"><code class="language-sql">SELECT random() AS rnd&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="round">round</h3>
<p>Rounds a number to a specified number of decimal places.</p>
<pre tabindex="0"><code class="language-sql">SELECT round(total_amount, 2) AS rounded&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="signum">signum</h3>
<p>Returns the sign of a number: -1, 0, or 1.</p>
<pre tabindex="0"><code class="language-sql">SELECT signum(total_amount - 500) AS sign_val&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="sqrt">sqrt</h3>
<p>Returns the square root of a number.</p>
<pre tabindex="0"><code class="language-sql">SELECT sqrt(CAST(quantity AS DOUBLE)) AS sqrt_qty&#10;FROM my_namespace.sales_data&#10;WHERE quantity IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="trigonometric-functions">Trigonometric functions</h3>
<p><code>sin</code>, <code>cos</code>, <code>tan</code>, <code>asin</code>, <code>acos</code>, <code>atan</code>, <code>atan2</code>, <code>cot</code></p>
<pre tabindex="0"><code class="language-sql">SELECT sin(1.0) AS s, cos(1.0) AS c, tan(1.0) AS t,&#10;       asin(0.5) AS as_val, acos(0.5) AS ac_val, atan(1.0) AS at_val&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="trunc">trunc</h3>
<p>Truncates a number to a specified number of decimal places.</p>
<pre tabindex="0"><code class="language-sql">SELECT trunc(total_amount, 0) AS truncated&#10;FROM my_namespace.sales_data&#10;WHERE total_amount IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<hr />
<h2 id="regex-functions">Regex functions</h2>
<h3 id="regexp-count">regexp_count</h3>
<p>Returns the number of matches of a pattern in a string.</p>
<pre tabindex="0"><code class="language-sql">SELECT department, regexp_count(department, &#x27;[aeiou]&#x27;) AS vowels&#10;FROM my_namespace.sales_data&#10;WHERE department IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="regexp-instr">regexp_instr</h3>
<p>Returns the position of the first match of a pattern.</p>
<pre tabindex="0"><code class="language-sql">SELECT department, regexp_instr(department, &#x27;[0-9]&#x27;) AS digit_pos&#10;FROM my_namespace.sales_data&#10;WHERE department IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="regexp-like">regexp_like</h3>
<p>Returns true if a string matches a regular expression pattern.</p>
<pre tabindex="0"><code class="language-sql">SELECT department, regexp_like(department, &#x27;^[A-Z]{2}&#x27;) AS starts_two_caps&#10;FROM my_namespace.sales_data&#10;WHERE department IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="regexp-match">regexp_match</h3>
<p>Returns the first match of a pattern as an array.</p>
<pre tabindex="0"><code class="language-sql">SELECT department, regexp_match(department, &#x27;([A-Z][a-z]+)&#x27;) AS first_word&#10;FROM my_namespace.sales_data&#10;WHERE department IS NOT NULL&#10;LIMIT 3&#10;</code></pre>
<h3 id="regexp-replace">regexp_replace</h3>
<p>Replaces matches of a pattern with a replacement string.</p>
<pre tabindex="0"><code class="language-sql">SELECT department, regexp_replace(department, &#x27;[0-9]&#x27;, &#x27;#&#x27;) AS no_digits&#10;FROM my_namespace.sales_data&#10;WHERE department IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<hr />
<h2 id="string-functions">String functions</h2>
<h3 id="ascii">ascii</h3>
<p>Returns the ASCII code of the first character.</p>
<pre tabindex="0"><code class="language-sql">SELECT customer_id, ascii(customer_id) AS first_code&#10;FROM my_namespace.sales_data&#10;LIMIT 3&#10;</code></pre>
<h3 id="bit-length">bit_length</h3>
<p>Returns the length of a string in bits.</p>
<pre tabindex="0"><code class="language-sql">SELECT customer_id, bit_length(customer_id) AS bits&#10;FROM my_namespace.sales_data&#10;LIMIT 3&#10;</code></pre>
<h3 id="btrim">btrim</h3>
<p>Trims characters from both sides of a string. Alias: <code>trim</code>.</p>
<pre tabindex="0"><code class="language-sql">SELECT btrim(&#x27;  hello  &#x27;) AS trimmed&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="chr">chr</h3>
<p>Returns the character for a given ASCII code.</p>
<pre tabindex="0"><code class="language-sql">SELECT chr(65) AS letter&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="concat">concat</h3>
<p>Concatenates two or more strings.</p>
<pre tabindex="0"><code class="language-sql">SELECT concat(department, &#x27; - &#x27;, region) AS label&#10;FROM my_namespace.sales_data&#10;WHERE department IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="concat-ws">concat_ws</h3>
<p>Concatenates strings with a separator.</p>
<pre tabindex="0"><code class="language-sql">SELECT concat_ws(&#x27;/&#x27;, region, department) AS path&#10;FROM my_namespace.sales_data&#10;WHERE department IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="contains">contains</h3>
<p>Returns true if a string contains a substring.</p>
<pre tabindex="0"><code class="language-sql">SELECT customer_id, contains(department, &#x27;Sales&#x27;) AS is_sales&#10;FROM my_namespace.sales_data&#10;WHERE department IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="ends-with">ends_with</h3>
<p>Returns true if a string ends with a suffix.</p>
<pre tabindex="0"><code class="language-sql">SELECT customer_id, ends_with(department, &#x27;ing&#x27;) AS ends_ing&#10;FROM my_namespace.sales_data&#10;WHERE department IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="levenshtein">levenshtein</h3>
<p>Returns the Levenshtein edit distance between two strings.</p>
<pre tabindex="0"><code class="language-sql">SELECT department, levenshtein(department, &#x27;Engineering&#x27;) AS dist&#10;FROM my_namespace.sales_data&#10;WHERE department IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="lower">lower</h3>
<p>Converts a string to lowercase.</p>
<pre tabindex="0"><code class="language-sql">SELECT lower(department) AS dept_lower&#10;FROM my_namespace.sales_data&#10;LIMIT 5&#10;</code></pre>
<h3 id="ltrim">ltrim</h3>
<p>Trims characters from the left side of a string.</p>
<pre tabindex="0"><code class="language-sql">SELECT ltrim(&#x27;  hello&#x27;) AS trimmed&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="octet-length">octet_length</h3>
<p>Returns the length of a string in bytes.</p>
<pre tabindex="0"><code class="language-sql">SELECT customer_id, octet_length(customer_id) AS bytes&#10;FROM my_namespace.sales_data&#10;LIMIT 3&#10;</code></pre>
<h3 id="repeat">repeat</h3>
<p>Repeats a string a given number of times.</p>
<pre tabindex="0"><code class="language-sql">SELECT repeat(region, 2) AS doubled&#10;FROM my_namespace.sales_data&#10;LIMIT 3&#10;</code></pre>
<h3 id="replace">replace</h3>
<p>Replaces all occurrences of a substring.</p>
<pre tabindex="0"><code class="language-sql">SELECT department, replace(department, &#x27; &#x27;, &#x27;_&#x27;) AS underscored&#10;FROM my_namespace.sales_data&#10;WHERE department IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="rtrim">rtrim</h3>
<p>Trims characters from the right side of a string.</p>
<pre tabindex="0"><code class="language-sql">SELECT rtrim(&#x27;hello  &#x27;) AS trimmed&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="split-part">split_part</h3>
<p>Splits a string by a delimiter and returns the specified part (1-indexed).</p>
<pre tabindex="0"><code class="language-sql">SELECT customer_id, split_part(customer_id, &#x27;-&#x27;, 1) AS first_part&#10;FROM my_namespace.sales_data&#10;WHERE customer_id IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="starts-with">starts_with</h3>
<p>Returns true if a string starts with a prefix.</p>
<pre tabindex="0"><code class="language-sql">SELECT customer_id, starts_with(department, &#x27;Eng&#x27;) AS is_eng&#10;FROM my_namespace.sales_data&#10;WHERE department IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="to-hex">to_hex</h3>
<p>Converts an integer to a hexadecimal string.</p>
<pre tabindex="0"><code class="language-sql">SELECT to_hex(255) AS hex_ff&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="upper">upper</h3>
<p>Converts a string to uppercase.</p>
<pre tabindex="0"><code class="language-sql">SELECT upper(region) AS region_upper&#10;FROM my_namespace.sales_data&#10;LIMIT 5&#10;</code></pre>
<h3 id="uuid">uuid</h3>
<p>Generates a random UUID.</p>
<pre tabindex="0"><code class="language-sql">SELECT uuid() AS new_id&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<hr />
<h2 id="unicode-functions">Unicode functions</h2>
<h3 id="character-length">character_length</h3>
<p>Returns the number of characters in a string. Aliases: <code>length</code>, <code>char_length</code>.</p>
<pre tabindex="0"><code class="language-sql">SELECT department, character_length(department) AS len&#10;FROM my_namespace.sales_data&#10;WHERE department IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="find-in-set">find_in_set</h3>
<p>Returns the position of a string within a comma-separated list.</p>
<pre tabindex="0"><code class="language-sql">SELECT find_in_set(&#x27;North&#x27;, &#x27;South,North,East,West&#x27;) AS pos&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="initcap">initcap</h3>
<p>Capitalizes the first letter of each word.</p>
<pre tabindex="0"><code class="language-sql">SELECT initcap(&#x27;hello world&#x27;) AS capped&#10;FROM my_namespace.sales_data&#10;LIMIT 1&#10;</code></pre>
<h3 id="left">left</h3>
<p>Returns the leftmost <em>n</em> characters of a string.</p>
<pre tabindex="0"><code class="language-sql">SELECT department, left(department, 5) AS prefix&#10;FROM my_namespace.sales_data&#10;WHERE department IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="lpad">lpad</h3>
<p>Left-pads a string to a specified length.</p>
<pre tabindex="0"><code class="language-sql">SELECT region, lpad(region, 15, &#x27;.&#x27;) AS padded&#10;FROM my_namespace.sales_data&#10;LIMIT 5&#10;</code></pre>
<h3 id="reverse">reverse</h3>
<p>Reverses a string.</p>
<pre tabindex="0"><code class="language-sql">SELECT department, reverse(department) AS rev&#10;FROM my_namespace.sales_data&#10;WHERE department IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="right">right</h3>
<p>Returns the rightmost <em>n</em> characters of a string.</p>
<pre tabindex="0"><code class="language-sql">SELECT department, right(department, 3) AS suffix&#10;FROM my_namespace.sales_data&#10;WHERE department IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="rpad">rpad</h3>
<p>Right-pads a string to a specified length.</p>
<pre tabindex="0"><code class="language-sql">SELECT region, rpad(region, 15, &#x27;.&#x27;) AS padded&#10;FROM my_namespace.sales_data&#10;LIMIT 5&#10;</code></pre>
<h3 id="strpos">strpos</h3>
<p>Returns the position of a substring (1-indexed). Aliases: <code>instr</code>, <code>position</code>.</p>
<pre tabindex="0"><code class="language-sql">SELECT department, strpos(department, &#x27;a&#x27;) AS a_pos&#10;FROM my_namespace.sales_data&#10;WHERE department IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="substr">substr</h3>
<p>Returns a substring starting at a position for a given length. Alias: <code>substring</code>.</p>
<pre tabindex="0"><code class="language-sql">SELECT department, substr(department, 1, 8) AS first_eight&#10;FROM my_namespace.sales_data&#10;WHERE department IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="substr-index">substr_index</h3>
<p>Returns the substring before the <em>n</em>-th occurrence of a delimiter. Alias: <code>substring_index</code>.</p>
<pre tabindex="0"><code class="language-sql">SELECT customer_id, substr_index(customer_id, &#x27;-&#x27;, 1) AS first_segment&#10;FROM my_namespace.sales_data&#10;WHERE customer_id IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
<h3 id="translate">translate</h3>
<p>Replaces characters in a string based on a mapping.</p>
<pre tabindex="0"><code class="language-sql">SELECT department, translate(department, &#x27;aeiou&#x27;, &#x27;12345&#x27;) AS coded&#10;FROM my_namespace.sales_data&#10;WHERE department IS NOT NULL&#10;LIMIT 5&#10;</code></pre>
