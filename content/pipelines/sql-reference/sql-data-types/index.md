---
cp9:
  canonical: https://developers.cloudflare.com/pipelines/sql-reference/sql-data-types/
  description: Supported data types in Cloudflare Pipelines SQL
  full_title: SQL data types · Cloudflare Pipelines Docs
  head_html: <title>SQL data types · Cloudflare Pipelines Docs</title><meta name="generator" content="Nift"><meta name="description" content="Supported data types in Cloudflare Pipelines SQL"><link rel="canonical" href="https://developers.cloudflare.com/pipelines/sql-reference/sql-data-types/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pipelines/sql-reference/sql-data-types/index.md"><meta property="og:title" content="SQL data types · Cloudflare Pipelines Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Supported data types in Cloudflare Pipelines SQL"><meta property="og:url" content="https://developers.cloudflare.com/pipelines/sql-reference/sql-data-types/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pipelines"><meta name="algolia_product_filter" content="Pipelines"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_additional_products" content="Pipelines"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pipelines/sql-reference/sql-data-types/#page","headline":"SQL data types \u00b7 Cloudflare Pipelines Docs","description":"Supported data types in Cloudflare Pipelines SQL","url":"https://developers.cloudflare.com/pipelines/sql-reference/sql-data-types/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pipelines/sql-reference/sql-data-types/
  schema: 1
---
<p>Cloudflare Pipelines supports a set of primitive and composite data types for SQL transformations. These types can be used in stream schemas and SQL literals with automatic type inference.</p>
<h2 id="primitive-types">Primitive types</h2>
<table>
<thead>
<tr>
<th>Pipelines</th>
<th>SQL Types</th>
<th>Example Literals</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>bool</code></td>
<td><code>BOOLEAN</code></td>
<td><code>TRUE</code>, <code>FALSE</code></td>
</tr>
<tr>
<td><code>int32</code></td>
<td><code>INT</code>, <code>INTEGER</code></td>
<td><code>0</code>, <code>1</code>, <code>-2</code></td>
</tr>
<tr>
<td><code>int64</code></td>
<td><code>BIGINT</code></td>
<td><code>0</code>, <code>1</code>, <code>-2</code></td>
</tr>
<tr>
<td><code>float32</code></td>
<td><code>FLOAT</code>, <code>REAL</code></td>
<td><code>0.0</code>, <code>-2.4</code>, <code>1E-3</code></td>
</tr>
<tr>
<td><code>float64</code></td>
<td><code>DOUBLE</code></td>
<td><code>0.0</code>, <code>-2.4</code>, <code>1E-35</code></td>
</tr>
<tr>
<td><code>string</code></td>
<td><code>VARCHAR</code>, <code>CHAR</code>, <code>TEXT</code>, <code>STRING</code></td>
<td><code>&quot;hello&quot;</code>, <code>&quot;world&quot;</code></td>
</tr>
<tr>
<td><code>timestamp</code></td>
<td><code>TIMESTAMP</code></td>
<td><code>'2020-01-01'</code>, <code>'2023-05-17T22:16:00.648662+00:00'</code></td>
</tr>
<tr>
<td><code>binary</code></td>
<td><code>BYTEA</code></td>
<td><code>X'A123'</code> (hex)</td>
</tr>
<tr>
<td><code>json</code></td>
<td><code>JSON</code></td>
<td><code>'{&quot;event&quot;: &quot;purchase&quot;, &quot;amount&quot;: 29.99}'</code></td>
</tr>
</tbody>
</table>
<h2 id="composite-types">Composite types</h2>
<p>In addition to primitive types, Pipelines SQL supports composite types for more complex data structures.</p>
<h3 id="list-types">List types</h3>
<p>Lists group together zero or more elements of the same type. In stream schemas, lists are declared using the <code>list</code> type with an <code>items</code> field specifying the element type. In SQL, lists correspond to arrays and are declared by suffixing another type with <code>[]</code>, for example <code>INT[]</code>.</p>
<p>List values can be indexed using 1-indexed subscript notation (<code>v[1]</code> is the first element of <code>v</code>).</p>
<p>Lists can be constructed via <code>[]</code> literals:</p>
<pre tabindex="0"><code class="language-sql">SELECT [1, 2, 3] as numbers&#10;</code></pre>
<p>Pipelines provides array functions for manipulating list values, and lists may be unnested using the <code>UNNEST</code> operator.</p>
<h3 id="struct-types">Struct types</h3>
<p>Structs combine related fields into a single value. In stream schemas, structs are declared using the <code>struct</code> type with a <code>fields</code> array. In SQL, structs can be created using the <code>struct</code> function.</p>
<p>Example creating a struct in SQL:</p>
<pre tabindex="0"><code class="language-sql">SELECT struct(&#x27;user123&#x27;, &#x27;purchase&#x27;, 29.99) as event_data FROM events&#10;</code></pre>
<p>This creates a struct with fields <code>c0</code>, <code>c1</code>, <code>c2</code> containing the user ID, event type, and amount.</p>
<p>Struct fields can be accessed via <code>.</code> notation, for example <code>event_data.c0</code> for the user ID.</p>
