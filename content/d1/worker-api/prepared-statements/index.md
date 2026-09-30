---
cp9:
  canonical: https://developers.cloudflare.com/d1/worker-api/prepared-statements/
  description: Bind parameters and run D1 prepared statements using the run, all, first, and raw methods.
  full_title: Prepared statement methods · Cloudflare D1 docs
  head_html: <title>Prepared statement methods · Cloudflare D1 docs</title><meta name="generator" content="Nift"><meta name="description" content="Bind parameters and run D1 prepared statements using the run, all, first, and raw methods."><link rel="canonical" href="https://developers.cloudflare.com/d1/worker-api/prepared-statements/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/d1/worker-api/prepared-statements/index.md"><meta property="og:title" content="Prepared statement methods · Cloudflare D1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Bind parameters and run D1 prepared statements using the run, all, first, and raw methods."><meta property="og:url" content="https://developers.cloudflare.com/d1/worker-api/prepared-statements/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="D1"><meta name="algolia_product_filter" content="D1"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="D1"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/d1/worker-api/prepared-statements/#page","headline":"Prepared statement methods \u00b7 Cloudflare D1 docs","description":"Bind parameters and run D1 prepared statements using the run, all, first, and raw methods.","url":"https://developers.cloudflare.com/d1/worker-api/prepared-statements/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /d1/worker-api/prepared-statements/
  schema: 1
---
<p>This chapter documents the various ways you can run and retrieve the results of a query after you have <a href="/d1/worker-api/d1-database/#prepare">prepared your statement</a>.</p>
<h2 id="methods">Methods</h2>
<h3 id="bind"><code>bind()</code></h3>
<p>Binds a parameter to the prepared statement.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7170.md")
</div></div>
<h4 id="parameter">Parameter</h4>
<ul>
<li><code>Variable</code>: <span class="nb-type">string</span>
<ul>
<li>The variable to be appended into the prepared statement. See <a href="#guidance">guidance</a> below.</li>
</ul>
</li>
</ul>
<h4 id="return-values">Return values</h4>
<ul>
<li><code>D1PreparedStatement</code>: <span class="nb-type">Object</span>
<ul>
<li>A <code>D1PreparedStatement</code> where the input parameter has been included in the statement.</li>
</ul>
</li>
</ul>
<h4 id="guidance">Guidance</h4>
<ul>
<li>D1 follows the <a href="https://www.sqlite.org/lang_expr.html#varparam">SQLite convention</a> for prepared statements parameter binding. Currently, D1 only supports Ordered (<code>?NNNN</code>) and Anonymous (<code>?</code>) parameters. In the future, D1 will support named parameters as well.</li>
</ul>
<table>
<thead>
<tr>
<th>Syntax</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>?NNN</code></td>
<td>Ordered</td>
<td>A question mark followed by a number <code>NNN</code> holds a spot for the <code>NNN</code>-th parameter. <code>NNN</code> must be between <code>1</code> and <code>SQLITE_MAX_VARIABLE_NUMBER</code></td>
</tr>
<tr>
<td><code>?</code></td>
<td>Anonymous</td>
<td>A question mark that is not followed by a number creates a parameter with a number one greater than the largest parameter number already assigned. If this means the parameter number is greater than <code>SQLITE_MAX_VARIABLE_NUMBER</code>, it is an error. This parameter format is provided for compatibility with other database engines. But because it is easy to miscount the question marks, the use of this parameter format is discouraged. Programmers are encouraged to use one of the symbolic formats below or the <code>?NNN</code> format above instead.</td>
</tr>
</tbody>
</table>
<pre tabindex="0"><code>To bind a parameter, use the `.bind` method.&#10;&#10;Order and anonymous examples:&#10;</code></pre>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7173.md")
</div></div>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7176.md")
</div></div>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7179.md")
</div></div>
<h4 id="static-statements">Static statements</h4>
<p>D1 API supports static statements. Static statements are SQL statements where the variables have been hard coded. When writing a static statement, you manually type the variable within the statement string.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="advantages-of-prepared-statements">Advantages of prepared statements</h3>
@markup("md", "content/.markup/bodies/7167.md")
</aside>
<p>Example of a prepared statement with dynamically bound value:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7182.md")
</div></div>
<p>Example of a static statement:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7185.md")
</div></div>
<h3 id="run"><code>run()</code></h3>
<p>Runs the prepared query (or queries) and returns results. The returned results includes metadata.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7188.md")
</div></div>
<h4 id="parameter-1">Parameter</h4>
<ul>
<li>None.</li>
</ul>
<h4 id="return-values-1">Return values</h4>
<ul>
<li><code>D1Result</code>: <span class="nb-type">Object</span>
<ul>
<li>An object containing the success status, a meta object, and an array of objects containing the query results.</li>
<li>For more information on the object, refer to <a href="/d1/worker-api/return-object/#d1result"><code>D1Result</code></a>.</li>
</ul>
</li>
</ul>
<details class="nb-details" open><summary>Example of return values</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7192.md")
</div></details>
<h4 id="guidance-1">Guidance</h4>
<ul>
<li><code>results</code> is empty for write operations such as <code>UPDATE</code>, <code>DELETE</code>, or <code>INSERT</code>.</li>
<li>When using TypeScript, you can pass a <a href="/d1/worker-api/#typescript-support">type parameter</a> to <a href="#run"><code>D1PreparedStatement::run</code></a> to return a typed result object.</li>
<li><a href="#run"><code>D1PreparedStatement::run</code></a> is functionally equivalent to <code>D1PreparedStatement::all</code>, and can be treated as an alias.</li>
<li>You can choose to extract only the results you expect from the statement by simply returning the <code>results</code> property of the return object.</li>
</ul>
<details class="nb-details"><summary>Example of returning only the �CODE59�</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7196.md")
</div></details>
<h3 id="raw"><code>raw()</code></h3>
<p>Runs the prepared query (or queries), and returns the results as an array of arrays. The returned results do not include metadata.</p>
<p>Column names are not included in the result set by default. To include column names as the first row of the result array, set <code>.raw({columnNames: true})</code>.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7199.md")
</div></div>
<h4 id="parameters">Parameters</h4>
<ul>
<li><code>columnNames</code>: <span class="nb-type">Object</span> <span class="nb-metainfo">Optional</span>
<ul>
<li>A boolean object which includes column names as the first row of the result array.</li>
</ul>
</li>
</ul>
<h4 id="return-values-2">Return values</h4>
<ul>
<li><code>Array</code>: <span class="nb-type">Array</span>
<ul>
<li>An array of arrays. Each sub-array represents a row.</li>
</ul>
</li>
</ul>
<details class="nb-details" open><summary>Example of return values</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7206.md")
</div></details>
<h4 id="guidance-2">Guidance</h4>
<ul>
<li>When using TypeScript, you can pass a <a href="/d1/worker-api/#typescript-support">type parameter</a> to <a href="#raw"><code>D1PreparedStatement::raw</code></a> to return a typed result array.</li>
</ul>
<h3 id="first"><code>first()</code></h3>
<p>Runs the prepared query (or queries), and returns the first row of the query result as an object. This does not return any metadata. Instead, it directly returns the object.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/7209.md")
</div></div>
<h4 id="parameters-1">Parameters</h4>
<ul>
<li><code>columnName</code>: <span class="nb-type">String</span> <span class="nb-metainfo">Optional</span>
<ul>
<li>Specify a <code>columnName</code> to return a value from a specific column in the first row of the query result.</li>
</ul>
</li>
<li>None.
<ul>
<li>Do not pass a parameter to obtain all columns from the first row.</li>
</ul>
</li>
</ul>
<h4 id="return-values-3">Return values</h4>
<ul>
<li>
<p><code>firstRow</code>: <span class="nb-type">Object</span> <span class="nb-metainfo">Optional</span></p>
<ul>
<li>An object containing the first row of the query result.</li>
<li>The return value will be further filtered to a specific attribute if <code>columnName</code> was specified.</li>
</ul>
</li>
<li>
<p><code>null</code>: <span class="nb-type">null</span></p>
<ul>
<li>If the query returns no rows.</li>
</ul>
</li>
</ul>
<details class="nb-details" open><summary>Example of return values</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7216.md")
</div></details>
<h4 id="guidance-3">Guidance</h4>
<ul>
<li>If the query returns rows but <code>column</code> does not exist, then <a href="#first"><code>D1PreparedStatement::first</code></a> throws the <code>D1_ERROR</code> exception.</li>
<li><a href="#first"><code>D1PreparedStatement::first</code></a> does not alter the SQL query. To improve performance, consider appending <code>LIMIT 1</code> to your statement.</li>
<li>When using TypeScript, you can pass a <a href="/d1/worker-api/#typescript-support">type parameter</a> to <a href="#first"><code>D1PreparedStatement::first</code></a> to return a typed result object.</li>
</ul>
