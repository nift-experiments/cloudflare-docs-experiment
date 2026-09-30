---
cp9:
  canonical: https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/other/
  description: Miscellaneous scalar functions
  full_title: Other functions · Cloudflare Pipelines Docs
  head_html: <title>Other functions · Cloudflare Pipelines Docs</title><meta name="generator" content="Nift"><meta name="description" content="Miscellaneous scalar functions"><link rel="canonical" href="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/other/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/other/index.md"><meta property="og:title" content="Other functions · Cloudflare Pipelines Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Miscellaneous scalar functions"><meta property="og:url" content="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/other/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pipelines"><meta name="algolia_product_filter" content="Pipelines"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_additional_products" content="Pipelines"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/other/#page","headline":"Other functions \u00b7 Cloudflare Pipelines Docs","description":"Miscellaneous scalar functions","url":"https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/other/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pipelines/sql-reference/scalar-functions/other/
  schema: 1
---
<p><em>Cloudflare Pipelines scalar function implementations are based on
<a href="https://arrow.apache.org/datafusion/">Apache DataFusion</a> (via <a href="https://www.arroyo.dev/">Arroyo</a>) and these docs are derived from
the DataFusion function reference.</em></p>
<h2 id="arrow-cast"><code>arrow_cast</code></h2>
<p>Casts a value to a specific Arrow data type:</p>
<pre tabindex="0"><code>arrow_cast(expression, datatype)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression</strong>: Expression to cast.
Can be a constant, column, or function, and any combination of arithmetic or
string operators.</li>
<li><strong>datatype</strong>: <a href="https://docs.rs/arrow/latest/arrow/datatypes/enum.DataType.html">Arrow data type</a> name
to cast to, as a string. The format is the same as that returned by [<code>arrow_typeof</code>]</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select arrow_cast(-5, &#x27;Int8&#x27;) as a,&#10;  arrow_cast(&#x27;foo&#x27;, &#x27;Dictionary(Int32, Utf8)&#x27;) as b,&#10;  arrow_cast(&#x27;bar&#x27;, &#x27;LargeUtf8&#x27;) as c,&#10;  arrow_cast(&#x27;2023-01-02T12:53:02&#x27;, &#x27;Timestamp(Microsecond, Some(&quot;+08:00&quot;))&#x27;) as d&#10;  ;&#10;&#43;----+-----+-----+---------------------------+&#10;| a  | b   | c   | d                         |&#10;&#43;----+-----+-----+---------------------------+&#10;| -5 | foo | bar | 2023-01-02T12:53:02+08:00 |&#10;&#43;----+-----+-----+---------------------------+&#10;1 row in set. Query took 0.001 seconds.&#10;</code></pre>
<h2 id="arrow-typeof"><code>arrow_typeof</code></h2>
<p>Returns the name of the underlying <a href="https://docs.rs/arrow/latest/arrow/datatypes/enum.DataType.html">Arrow data type</a> of the expression:</p>
<pre tabindex="0"><code>arrow_typeof(expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression</strong>: Expression to evaluate.
Can be a constant, column, or function, and any combination of arithmetic or
string operators.</li>
</ul>
<p><strong>Example</strong></p>
<pre tabindex="0"><code>&gt; select arrow_typeof(&#x27;foo&#x27;), arrow_typeof(1);&#10;&#43;---------------------------+------------------------+&#10;| arrow_typeof(Utf8(&quot;foo&quot;)) | arrow_typeof(Int64(1)) |&#10;&#43;---------------------------+------------------------+&#10;| Utf8                      | Int64                  |&#10;&#43;---------------------------+------------------------+&#10;1 row in set. Query took 0.001 seconds.&#10;</code></pre>
