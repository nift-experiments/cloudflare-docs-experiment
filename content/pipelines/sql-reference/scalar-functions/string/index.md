---
cp9:
  canonical: https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/string/
  description: Scalar functions for manipulating strings
  full_title: String functions · Cloudflare Pipelines Docs
  head_html: <title>String functions · Cloudflare Pipelines Docs</title><meta name="generator" content="Nift"><meta name="description" content="Scalar functions for manipulating strings"><link rel="canonical" href="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/string/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/string/index.md"><meta property="og:title" content="String functions · Cloudflare Pipelines Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Scalar functions for manipulating strings"><meta property="og:url" content="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/string/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pipelines"><meta name="algolia_product_filter" content="Pipelines"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_additional_products" content="Pipelines"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/string/#page","headline":"String functions \u00b7 Cloudflare Pipelines Docs","description":"Scalar functions for manipulating strings","url":"https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/string/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pipelines/sql-reference/scalar-functions/string/
  schema: 1
---
<p><em>Cloudflare Pipelines scalar function implementations are based on
<a href="https://arrow.apache.org/datafusion/">Apache DataFusion</a> (via <a href="https://www.arroyo.dev/">Arroyo</a>) and these docs are derived from
the DataFusion function reference.</em></p>
<h2 id="ascii"><code>ascii</code></h2>
<p>Returns the ASCII value of the first character in a string.</p>
<pre tabindex="0"><code>ascii(str)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
</ul>
<p><strong>Related functions</strong>:
<a href="#chr">chr</a></p>
<h2 id="bit-length"><code>bit_length</code></h2>
<p>Returns the bit length of a string.</p>
<pre tabindex="0"><code>bit_length(str)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
</ul>
<p><strong>Related functions</strong>:
<a href="#length">length</a>,
<a href="#octet_length">octet_length</a></p>
<h2 id="btrim"><code>btrim</code></h2>
<p>Trims the specified trim string from the start and end of a string.
If no trim string is provided, all whitespace is removed from the start and end
of the input string.</p>
<pre tabindex="0"><code>btrim(str[, trim_str])&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>trim_str</strong>: String expression to trim from the beginning and end of the input string.
Can be a constant, column, or function, and any combination of arithmetic operators.
<em>Default is whitespace characters.</em></li>
</ul>
<p><strong>Related functions</strong>:
<a href="#ltrim">ltrim</a>,
<a href="#rtrim">rtrim</a></p>
<p><strong>Aliases</strong></p>
<ul>
<li>trim</li>
</ul>
<h2 id="char-length"><code>char_length</code></h2>
<p><em>Alias of <a href="#length">length</a>.</em></p>
<h2 id="character-length"><code>character_length</code></h2>
<p><em>Alias of <a href="#length">length</a>.</em></p>
<h2 id="concat"><code>concat</code></h2>
<p>Concatenates multiple strings together.</p>
<pre tabindex="0"><code>concat(str[, ..., str_n])&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to concatenate.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>str_n</strong>: Subsequent string column or literal string to concatenate.</li>
</ul>
<p><strong>Related functions</strong>:
<a href="#concat_ws">concat_ws</a></p>
<h2 id="concat-ws"><code>concat_ws</code></h2>
<p>Concatenates multiple strings together with a specified separator.</p>
<pre tabindex="0"><code>concat(separator, str[, ..., str_n])&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>separator</strong>: Separator to insert between concatenated strings.</li>
<li><strong>str</strong>: String expression to concatenate.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>str_n</strong>: Subsequent string column or literal string to concatenate.</li>
</ul>
<p><strong>Related functions</strong>:
<a href="#concat">concat</a></p>
<h2 id="chr"><code>chr</code></h2>
<p>Returns the character with the specified ASCII or Unicode code value.</p>
<pre tabindex="0"><code>chr(expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression</strong>: Expression containing the ASCII or Unicode code value to operate on.
Can be a constant, column, or function, and any combination of arithmetic or
string operators.</li>
</ul>
<p><strong>Related functions</strong>:
<a href="#ascii">ascii</a></p>
<h2 id="ends-with"><code>ends_with</code></h2>
<p>Tests if a string ends with a substring.</p>
<pre tabindex="0"><code>ends_with(str, substr)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to test.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>substr</strong>: Substring to test for.</li>
</ul>
<h2 id="initcap"><code>initcap</code></h2>
<p>Capitalizes the first character in each word in the input string.
Words are delimited by non-alphanumeric characters.</p>
<pre tabindex="0"><code>initcap(str)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
</ul>
<p><strong>Related functions</strong>:
<a href="#lower">lower</a>,
<a href="#upper">upper</a></p>
<h2 id="instr"><code>instr</code></h2>
<p><em>Alias of <a href="#strpos">strpos</a>.</em></p>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>substr</strong>: Substring expression to search for.
Can be a constant, column, or function, and any combination of string operators.</li>
</ul>
<h2 id="left"><code>left</code></h2>
<p>Returns a specified number of characters from the left side of a string.</p>
<pre tabindex="0"><code>left(str, n)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>n</strong>: Number of characters to return.</li>
</ul>
<p><strong>Related functions</strong>:
<a href="#right">right</a></p>
<h2 id="length"><code>length</code></h2>
<p>Returns the number of characters in a string.</p>
<pre tabindex="0"><code>length(str)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
</ul>
<p><strong>Aliases</strong></p>
<ul>
<li>char_length</li>
<li>character_length</li>
</ul>
<p><strong>Related functions</strong>:
<a href="#bit_length">bit_length</a>,
<a href="#octet_length">octet_length</a></p>
<h2 id="lower"><code>lower</code></h2>
<p>Converts a string to lower-case.</p>
<pre tabindex="0"><code>lower(str)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
</ul>
<p><strong>Related functions</strong>:
<a href="#initcap">initcap</a>,
<a href="#upper">upper</a></p>
<h2 id="lpad"><code>lpad</code></h2>
<p>Pads the left side of a string with another string to a specified string length.</p>
<pre tabindex="0"><code>lpad(str, n[, padding_str])&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>n</strong>: String length to pad to.</li>
<li><strong>padding_str</strong>: String expression to pad with.
Can be a constant, column, or function, and any combination of string operators.
<em>Default is a space.</em></li>
</ul>
<p><strong>Related functions</strong>:
<a href="#rpad">rpad</a></p>
<h2 id="ltrim"><code>ltrim</code></h2>
<p>Trims the specified trim string from the beginning of a string.
If no trim string is provided, all whitespace is removed from the start
of the input string.</p>
<pre tabindex="0"><code>ltrim(str[, trim_str])&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>trim_str</strong>: String expression to trim from the beginning of the input string.
Can be a constant, column, or function, and any combination of arithmetic operators.
<em>Default is whitespace characters.</em></li>
</ul>
<p><strong>Related functions</strong>:
<a href="#btrim">btrim</a>,
<a href="#rtrim">rtrim</a></p>
<h2 id="octet-length"><code>octet_length</code></h2>
<p>Returns the length of a string in bytes.</p>
<pre tabindex="0"><code>octet_length(str)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
</ul>
<p><strong>Related functions</strong>:
<a href="#bit_length">bit_length</a>,
<a href="#length">length</a></p>
<h2 id="repeat"><code>repeat</code></h2>
<p>Returns a string with an input string repeated a specified number.</p>
<pre tabindex="0"><code>repeat(str, n)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to repeat.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>n</strong>: Number of times to repeat the input string.</li>
</ul>
<h2 id="replace"><code>replace</code></h2>
<p>Replaces all occurrences of a specified substring in a string with a new substring.</p>
<pre tabindex="0"><code>replace(str, substr, replacement)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to repeat.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>substr</strong>: Substring expression to replace in the input string.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>replacement</strong>: Replacement substring expression.
Can be a constant, column, or function, and any combination of string operators.</li>
</ul>
<h2 id="reverse"><code>reverse</code></h2>
<p>Reverses the character order of a string.</p>
<pre tabindex="0"><code>reverse(str)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to repeat.
Can be a constant, column, or function, and any combination of string operators.</li>
</ul>
<h2 id="right"><code>right</code></h2>
<p>Returns a specified number of characters from the right side of a string.</p>
<pre tabindex="0"><code>right(str, n)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>n</strong>: Number of characters to return.</li>
</ul>
<p><strong>Related functions</strong>:
<a href="#left">left</a></p>
<h2 id="rpad"><code>rpad</code></h2>
<p>Pads the right side of a string with another string to a specified string length.</p>
<pre tabindex="0"><code>rpad(str, n[, padding_str])&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>n</strong>: String length to pad to.</li>
<li><strong>padding_str</strong>: String expression to pad with.
Can be a constant, column, or function, and any combination of string operators.
<em>Default is a space.</em></li>
</ul>
<p><strong>Related functions</strong>:
<a href="#lpad">lpad</a></p>
<h2 id="rtrim"><code>rtrim</code></h2>
<p>Trims the specified trim string from the end of a string.
If no trim string is provided, all whitespace is removed from the end
of the input string.</p>
<pre tabindex="0"><code>rtrim(str[, trim_str])&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>trim_str</strong>: String expression to trim from the end of the input string.
Can be a constant, column, or function, and any combination of arithmetic operators.
<em>Default is whitespace characters.</em></li>
</ul>
<p><strong>Related functions</strong>:
<a href="#btrim">btrim</a>,
<a href="#ltrim">ltrim</a></p>
<h2 id="split-part"><code>split_part</code></h2>
<p>Splits a string based on a specified delimiter and returns the substring in the
specified position.</p>
<pre tabindex="0"><code>split_part(str, delimiter, pos)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to spit.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>delimiter</strong>: String or character to split on.</li>
<li><strong>pos</strong>: Position of the part to return.</li>
</ul>
<h2 id="starts-with"><code>starts_with</code></h2>
<p>Tests if a string starts with a substring.</p>
<pre tabindex="0"><code>starts_with(str, substr)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to test.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>substr</strong>: Substring to test for.</li>
</ul>
<h2 id="strpos"><code>strpos</code></h2>
<p>Returns the starting position of a specified substring in a string.
Positions begin at 1.
If the substring does not exist in the string, the function returns 0.</p>
<pre tabindex="0"><code>strpos(str, substr)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>substr</strong>: Substring expression to search for.
Can be a constant, column, or function, and any combination of string operators.</li>
</ul>
<p><strong>Aliases</strong></p>
<ul>
<li>instr</li>
</ul>
<h2 id="substr"><code>substr</code></h2>
<p>Extracts a substring of a specified number of characters from a specific
starting position in a string.</p>
<pre tabindex="0"><code>substr(str, start_pos[, length])&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>start_pos</strong>: Character position to start the substring at.
The first character in the string has a position of 1.</li>
<li><strong>length</strong>: Number of characters to extract.
If not specified, returns the rest of the string after the start position.</li>
</ul>
<h2 id="translate"><code>translate</code></h2>
<p>Translates characters in a string to specified translation characters.</p>
<pre tabindex="0"><code>translate(str, chars, translation)&#10;</code></pre>
<ul>
<li><strong>str</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>chars</strong>: Characters to translate.</li>
<li><strong>translation</strong>: Translation characters. Translation characters replace only
characters at the same position in the <strong>chars</strong> string.</li>
</ul>
<h2 id="to-hex"><code>to_hex</code></h2>
<p>Converts an integer to a hexadecimal string.</p>
<pre tabindex="0"><code>to_hex(int)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>int</strong>: Integer expression to convert.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="trim"><code>trim</code></h2>
<p><em>Alias of <a href="#btrim">btrim</a>.</em></p>
<h2 id="upper"><code>upper</code></h2>
<p>Converts a string to upper-case.</p>
<pre tabindex="0"><code>upper(str)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
</ul>
<p><strong>Related functions</strong>:
<a href="#initcap">initcap</a>,
<a href="#lower">lower</a></p>
<h2 id="uuid"><code>uuid</code></h2>
<p>Returns UUID v4 string value which is unique per row.</p>
<pre tabindex="0"><code>uuid()&#10;</code></pre>
<h2 id="overlay"><code>overlay</code></h2>
<p>Returns the string which is replaced by another string from the specified position and specified count length.
For example, <code>overlay('Txxxxas' placing 'hom' from 2 for 4) → Thomas</code></p>
<pre tabindex="0"><code>overlay(str PLACING substr FROM pos [FOR count])&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to operate on.</li>
<li><strong>substr</strong>: the string to replace part of str.</li>
<li><strong>pos</strong>: the start position to replace of str.</li>
<li><strong>count</strong>: the count of characters to be replaced from start position of str. If not specified, will use substr length instead.</li>
</ul>
<h2 id="levenshtein"><code>levenshtein</code></h2>
<p>Returns the Levenshtein distance between the two given strings.
For example, <code>levenshtein('kitten', 'sitting') = 3</code></p>
<pre tabindex="0"><code>levenshtein(str1, str2)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str1</strong>: String expression to compute Levenshtein distance with str2.</li>
<li><strong>str2</strong>: String expression to compute Levenshtein distance with str1.</li>
</ul>
<h2 id="substr-index"><code>substr_index</code></h2>
<p>Returns the substring from str before count occurrences of the delimiter delim.
If count is positive, everything to the left of the final delimiter (counting from the left) is returned.
If count is negative, everything to the right of the final delimiter (counting from the right) is returned.
For example, <code>substr_index('www.apache.org', '.', 1) = www</code>, <code>substr_index('www.apache.org', '.', -1) = org</code></p>
<pre tabindex="0"><code>substr_index(str, delim, count)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to operate on.</li>
<li><strong>delim</strong>: the string to find in str to split str.</li>
<li><strong>count</strong>: The number of times to search for the delimiter. Can be both a positive or negative number.</li>
</ul>
<h2 id="find-in-set"><code>find_in_set</code></h2>
<p>Returns a value in the range of 1 to N if the string str is in the string list strlist consisting of N substrings.
For example, <code>find_in_set('b', 'a,b,c,d') = 2</code></p>
<pre tabindex="0"><code>find_in_set(str, strlist)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>str</strong>: String expression to find in strlist.</li>
<li><strong>strlist</strong>: A string list is a string composed of substrings separated by , characters.</li>
</ul>
