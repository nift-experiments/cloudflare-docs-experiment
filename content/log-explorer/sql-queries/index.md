---
cp9:
  canonical: https://developers.cloudflare.com/log-explorer/sql-queries/
  description: Review SQL syntax supported by Log Explorer.
  full_title: SQL queries supported · Cloudflare Log Explorer docs
  head_html: <title>SQL queries supported · Cloudflare Log Explorer docs</title><meta name="generator" content="Nift"><meta name="description" content="Review SQL syntax supported by Log Explorer."><link rel="canonical" href="https://developers.cloudflare.com/log-explorer/sql-queries/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/log-explorer/sql-queries/index.md"><meta property="og:title" content="SQL queries supported · Cloudflare Log Explorer docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review SQL syntax supported by Log Explorer."><meta property="og:url" content="https://developers.cloudflare.com/log-explorer/sql-queries/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Log Explorer"><meta name="algolia_product_filter" content="Log Explorer"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Log Explorer"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/log-explorer/sql-queries/#page","headline":"SQL queries supported \u00b7 Cloudflare Log Explorer docs","description":"Review SQL syntax supported by Log Explorer.","url":"https://developers.cloudflare.com/log-explorer/sql-queries/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /log-explorer/sql-queries/
  schema: 1
---
<p>This page outlines the SQL features supported by Log Explorer, including common aggregation functions, expressions, and query clauses.</p>
<p>The diagram below illustrates the general shape of a valid query supported in Log Explorer. It shows how standard SQL clauses — such as <code>SELECT</code>, <code>WHERE</code>, <code>GROUP BY</code>, and <code>ORDER BY</code> — can be composed to form supported queries.</p>
<p><img src="/assets/upstream/images/log-explorer/supported-sql-grammar-graph.png" alt="Supported SQL grammar" /></p>
<p>Examples of queries include:</p>
<ul>
<li><code>SELECT * FROM table WHERE (a = 1 OR b = &quot;hello&quot;) AND c &lt; 25.89</code></li>
<li><code>SELECT a, b, c FROM table WHERE d &gt;= &quot;GB&quot; LIMIT 10</code></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/808.md")
</aside>
<h3 id="sql-clauses-in-detail">SQL Clauses in detail</h3>
<p>The following SQL clauses define the structure and logic of queries in Log Explorer:</p>
<ul>
<li><code>SELECT</code> - The <code>SELECT</code> clause specifies the columns that you want to retrieve from the database tables. It can include individual column names, expressions, or even wildcard characters to select all columns.</li>
<li><code>FROM</code> - The <code>FROM</code> clause specifies the tables from which to retrieve data. It indicates the source of the data for the <code>SELECT</code> statement.</li>
<li><code>WHERE</code> - The <code>WHERE</code> clause filters the rows returned by a query based on specified conditions. It allows you to specify conditions that must be met for a row to be included in the result set.</li>
<li><code>SELECT DISTINCT</code> - Removes duplicate rows from the result set.</li>
<li><code>GROUP BY</code> - Groups rows for aggregation. The <code>GROUP BY</code> clause is used to group rows that have the same values into summary rows.</li>
<li><code>ORDER BY</code> - Sorts the result set. The <code>ORDER BY</code> clause is used to sort the result set by one or more columns in ascending or descending order.</li>
<li><code>LIMIT</code> - Restricts the number of rows returned. The <code>LIMIT</code> clause is used to constrain the number of rows returned by a query. It is often used in conjunction with the <code>ORDER BY</code> clause to retrieve the top <code>N</code> rows or to implement pagination.</li>
<li><code>OFFSET</code> - Skips a specified number of rows before returning results.</li>
</ul>
<p>The sections that follow break down the remaining components shown in the diagram — such as aggregation functions, string and numeric expressions, and supported operators — in more detail.</p>
<h2 id="functions">Functions</h2>
<p>Log Explorer supports a range of SQL functions to transform, evaluate, or summarize data. These include scalar and aggregation functions.</p>
<h3 id="scalar-functions">Scalar functions</h3>
<p>These help manipulate or evaluate values (often strings):</p>
<ul>
<li>
<p><code>ARRAY_CONTAINS(array, element)</code> –  Checks if the array contains the element.</p>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
</li>
</ul>
@markup("md", "content/.markup/bodies/809.md")
</div></details>
<ul>
<li>
<p><code>SUBSTRING(string, from_number, for_number)</code> – Extracts part of a string.</p>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
</li>
</ul>
@markup("md", "content/.markup/bodies/810.md")
</div></details>
<ul>
<li>
<p><code>LOWER(string)</code> – Converts to lowercase.</p>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
</li>
</ul>
@markup("md", "content/.markup/bodies/811.md")
</div></details>
<ul>
<li>
<p><code>UPPER(string)</code> – Converts to uppercase.</p>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
</li>
</ul>
@markup("md", "content/.markup/bodies/812.md")
</div></details>
<h3 id="aggregation-functions">Aggregation functions</h3>
<p>Used to perform calculations on sets of rows:</p>
<ul>
<li>
<p><code>SUM(expression)</code> – Total of values.</p>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
</li>
</ul>
@markup("md", "content/.markup/bodies/813.md")
</div></details>
<ul>
<li>
<p><code>MIN(expression)</code> – Minimum value.</p>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
</li>
</ul>
@markup("md", "content/.markup/bodies/814.md")
</div></details>
<ul>
<li>
<p><code>MAX(expression)</code> – Maximum value.</p>
 <details class="nb-details"><summary>Example</summary><div class="nb-details-body">
</li>
</ul>
@markup("md", "content/.markup/bodies/815.md")
</div></details>
<ul>
<li>
<p><code>COUNT(expression)</code> – Number of rows (can be all rows or non-null values).</p>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
</li>
</ul>
@markup("md", "content/.markup/bodies/816.md")
</div></details>
<ul>
<li>
<p><code>COUNT(DISTINCT expression)</code> – Number of distinct non-null values.</p>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
</li>
</ul>
@markup("md", "content/.markup/bodies/817.md")
</div></details>
<ul>
<li>
<p><code>AVG(expression)</code> – Average of numeric values.</p>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
</li>
</ul>
@markup("md", "content/.markup/bodies/818.md")
</div></details>
<p>The diagram below represents the grammar for SQL expressions including  scalar and aggregate functions.</p>
<p><img src="/assets/upstream/images/log-explorer/scalar-aggregate-functions.png" alt="Scalar and aggregate functions" /></p>
<h2 id="expressions">Expressions</h2>
<p>Conditions or logic used in queries:</p>
<ul>
<li><code>CASE WHEN</code> – Conditional logic (like if-else).</li>
<li><code>AS</code> – Alias for columns or tables.</li>
<li><code>LIKE</code> – Pattern matching.</li>
<li><code>IN (list)</code> – Checks if a value is in a list.</li>
<li><code>BETWEEN ... AND ...</code> – Checks if a value is within a range.</li>
<li><code>Unary operator</code> – Operates on one operand (for example, <code>-5</code>).</li>
<li><code>Binary operator</code> – Operates on two operands (for example, <code>5 + 3</code>).</li>
<li><code>Nested Expressions</code> – Expression wrapped with parentheses, like <code>( x &gt; y )</code> or <code>( 1 )</code>.</li>
<li><code>Compound identifier</code> – Multi-part name (for example, <code>schema.table.column</code>).</li>
<li><code>Array</code> – A collection of values (supported differently across SQL dialects).</li>
<li><code>Literals</code> - represent values such as strings, numbers, or arrays.</li>
</ul>
<p>The diagram below represents the grammar for SQL expressions, detailing the various forms an expression can take, including columns, literals, functions, operators, and aliases.</p>
<p><img src="/assets/upstream/images/log-explorer/expressions.png" alt="SQL expressions" /></p>
<p>The diagram below defines the grammar for unary operators, which operate on a single operand (for example, negation or logical <code>NOT</code>):</p>
<p><img src="/assets/upstream/images/log-explorer/not.png" alt="Grammar for unary operators" /></p>
<h2 id="binary-operators">Binary Operators</h2>
<p>Used for arithmetic, comparison, logical operations:</p>
<ul>
<li>Arithmetic: <code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>, <code>%</code> (modulo)</li>
<li>Comparison: <code>&gt;</code>, <code>&lt;</code>, <code>&gt;=</code>, <code>&lt;=</code>, <code>=</code>, <code>!=</code> (or <code>&lt;&gt;</code>)`</li>
<li>Logical: <code>AND</code>, <code>OR</code>, <code>XOR</code></li>
<li>Bitwise: <code>&amp;</code>, <code>|</code>, <code>^</code>, <code>&gt;&gt;</code>, <code>&lt;&lt;</code></li>
<li>String concat: <code>||</code></li>
</ul>
