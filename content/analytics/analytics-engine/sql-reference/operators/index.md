---
cp9:
  canonical: https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/operators/
  description: Arithmetic, comparison, and logical SQL operators.
  full_title: Workers Analytics Engine SQL Reference · Cloudflare Analytics docs
  head_html: <title>Workers Analytics Engine SQL Reference · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Arithmetic, comparison, and logical SQL operators."><link rel="canonical" href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/operators/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/operators/index.md"><meta property="og:title" content="Workers Analytics Engine SQL Reference · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Arithmetic, comparison, and logical SQL operators."><meta property="og:url" content="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/operators/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers Analytics Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/operators/#page","headline":"Workers Analytics Engine SQL Reference \u00b7 Cloudflare Analytics docs","description":"Arithmetic, comparison, and logical SQL operators.","url":"https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/operators/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/analytics-engine/sql-reference/operators/
  schema: 1
---
<p>The following operators are supported:</p>
<h2 id="arithmetic-operators">Arithmetic operators</h2>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>+</code></td>
<td>addition</td>
</tr>
<tr>
<td><code>-</code></td>
<td>subtraction</td>
</tr>
<tr>
<td><code>*</code></td>
<td>multiplication</td>
</tr>
<tr>
<td><code>/</code></td>
<td>division</td>
</tr>
<tr>
<td><code>%</code></td>
<td>modulus</td>
</tr>
</tbody>
</table>
<h2 id="comparison-operators">Comparison operators</h2>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>=</code></td>
<td>equals</td>
</tr>
<tr>
<td><code>&lt;</code></td>
<td>less than</td>
</tr>
<tr>
<td><code>&gt;</code></td>
<td>greater than</td>
</tr>
<tr>
<td><code>&lt;=</code></td>
<td>less than or equal to</td>
</tr>
<tr>
<td><code>&gt;=</code></td>
<td>greater than or equal to</td>
</tr>
<tr>
<td><code>&lt;&gt;</code> or <code>!=</code></td>
<td>not equal</td>
</tr>
<tr>
<td><code>IN</code></td>
<td>true if the preceding expression's value is in the list<br/><code>column IN ('a', 'list', 'of', 'values')</code></td>
</tr>
<tr>
<td><code>NOT IN</code></td>
<td>true if the preceding expression's value is not in the list<br/><code>column NOT IN ('a', 'list', 'of', 'values')</code></td>
</tr>
</tbody>
</table>
<p>We also support the <code>BETWEEN</code> operator for checking a value is in an inclusive range: <code>a [NOT] BETWEEN b AND c</code>.</p>
<h3 id="pattern-matching-operators">Pattern matching operators <span class="nb-badge">New</span></h3>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>LIKE</code></td>
<td>true if the string matches the pattern (case-sensitive)<br/><code>column LIKE 'pattern%'</code></td>
</tr>
<tr>
<td><code>NOT LIKE</code></td>
<td>true if the string does not match the pattern (case-sensitive)<br/><code>column NOT LIKE 'pattern%'</code></td>
</tr>
<tr>
<td><code>ILIKE</code></td>
<td>true if the string matches the pattern (case-insensitive)<br/><code>column ILIKE 'pattern%'</code></td>
</tr>
<tr>
<td><code>NOT ILIKE</code></td>
<td>true if the string does not match the pattern (case-insensitive)<br/><code>column NOT ILIKE 'pattern%'</code></td>
</tr>
</tbody>
</table>
<p>Pattern matching supports two wildcard characters:</p>
<ul>
<li><code>%</code> matches any sequence of zero or more characters</li>
<li><code>_</code> matches any single character</li>
</ul>
<p>Examples:</p>
<pre tabindex="0"><code class="language-sql">&#45;- Match strings starting with &quot;error&quot;&#10;WHERE blob1 LIKE &#x27;error%&#x27;&#10;&#10;&#45;- Match strings ending with &quot;.jpg&quot; (case-insensitive)&#10;WHERE blob2 ILIKE &#x27;%.jpg&#x27;&#10;&#10;&#45;- Match strings containing &quot;test&quot; anywhere&#10;WHERE blob3 LIKE &#x27;%test%&#x27;&#10;&#10;&#45;- Match exactly 5 characters starting with &quot;log&quot;&#10;WHERE blob4 LIKE &#x27;log__&#x27;&#10;&#10;&#45;- Exclude strings containing &quot;debug&quot; (case-insensitive)&#10;WHERE blob5 NOT ILIKE &#x27;%debug%&#x27;&#10;</code></pre>
<h2 id="boolean-operators">Boolean operators</h2>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>AND</code></td>
<td>boolean &quot;AND&quot; (true if both sides are true)</td>
</tr>
<tr>
<td><code>OR</code></td>
<td>boolean &quot;OR&quot; (true if either side or both sides are true)</td>
</tr>
<tr>
<td><code>NOT</code></td>
<td>boolean &quot;NOT&quot; (true if following expression is false and visa-versa)</td>
</tr>
</tbody>
</table>
<h2 id="unary-operators">Unary operators</h2>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>-</code></td>
<td>negation operator (for example, <code>-42</code>)</td>
</tr>
</tbody>
</table>
