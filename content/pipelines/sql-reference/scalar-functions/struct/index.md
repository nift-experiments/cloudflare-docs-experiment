---
cp9:
  canonical: https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/struct/
  description: Scalar functions for manipulating structs
  full_title: Struct functions · Cloudflare Pipelines Docs
  head_html: <title>Struct functions · Cloudflare Pipelines Docs</title><meta name="generator" content="Nift"><meta name="description" content="Scalar functions for manipulating structs"><link rel="canonical" href="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/struct/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/struct/index.md"><meta property="og:title" content="Struct functions · Cloudflare Pipelines Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Scalar functions for manipulating structs"><meta property="og:url" content="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/struct/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pipelines"><meta name="algolia_product_filter" content="Pipelines"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_additional_products" content="Pipelines"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/struct/#page","headline":"Struct functions \u00b7 Cloudflare Pipelines Docs","description":"Scalar functions for manipulating structs","url":"https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/struct/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pipelines/sql-reference/scalar-functions/struct/
  schema: 1
---
<p><em>Cloudflare Pipelines scalar function implementations are based on
<a href="https://arrow.apache.org/datafusion/">Apache DataFusion</a> (via <a href="https://www.arroyo.dev/">Arroyo</a>) and these docs are derived from
the DataFusion function reference.</em></p>
<h2 id="struct"><code>struct</code></h2>
<p>Returns an Arrow struct using the specified input expressions.
Fields in the returned struct use the <code>cN</code> naming convention.
For example: <code>c0</code>, <code>c1</code>, <code>c2</code>, etc.</p>
<pre tabindex="0"><code>struct(expression1[, ..., expression_n])&#10;</code></pre>
<p>For example, this query converts two columns <code>a</code> and <code>b</code> to a single column with
a struct type of fields <code>c0</code> and <code>c1</code>:</p>
<pre tabindex="0"><code>select * from t;&#10;&#43;---+---+&#10;| a | b |&#10;&#43;---+---+&#10;| 1 | 2 |&#10;| 3 | 4 |&#10;&#43;---+---+&#10;&#10;select struct(a, b) from t;&#10;&#43;-----------------+&#10;| struct(t.a,t.b) |&#10;&#43;-----------------+&#10;| {c0: 1, c1: 2}  |&#10;| {c0: 3, c1: 4}  |&#10;&#43;-----------------+&#10;</code></pre>
<h4 id="arguments">Arguments</h4>
<ul>
<li><strong>expression_n</strong>: Expression to include in the output struct.
Can be a constant, column, or function, and any combination of arithmetic or
string operators.</li>
</ul>
