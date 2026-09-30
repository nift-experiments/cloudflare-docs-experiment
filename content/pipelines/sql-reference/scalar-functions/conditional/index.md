---
cp9:
  canonical: https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/conditional/
  description: Scalar functions to implement conditional logic
  full_title: Conditional functions · Cloudflare Pipelines Docs
  head_html: <title>Conditional functions · Cloudflare Pipelines Docs</title><meta name="generator" content="Nift"><meta name="description" content="Scalar functions to implement conditional logic"><link rel="canonical" href="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/conditional/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/conditional/index.md"><meta property="og:title" content="Conditional functions · Cloudflare Pipelines Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Scalar functions to implement conditional logic"><meta property="og:url" content="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/conditional/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pipelines"><meta name="algolia_product_filter" content="Pipelines"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_additional_products" content="Pipelines"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/conditional/#page","headline":"Conditional functions \u00b7 Cloudflare Pipelines Docs","description":"Scalar functions to implement conditional logic","url":"https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/conditional/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pipelines/sql-reference/scalar-functions/conditional/
  schema: 1
---
<p><em>Cloudflare Pipelines scalar function implementations are based on
<a href="https://arrow.apache.org/datafusion/">Apache DataFusion</a> (via <a href="https://www.arroyo.dev/">Arroyo</a>) and these docs are derived from
the DataFusion function reference.</em></p>
<h2 id="coalesce"><code>coalesce</code></h2>
<p>Returns the first of its arguments that is not <em>null</em>.
Returns <em>null</em> if all arguments are <em>null</em>.
This function is often used to substitute a default value for <em>null</em> values.</p>
<pre tabindex="0"><code>coalesce(expression1[, ..., expression_n])&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression1, expression_n</strong>:
Expression to use if previous expressions are <em>null</em>.
Can be a constant, column, or function, and any combination of arithmetic operators.
Pass as many expression arguments as necessary.</li>
</ul>
<h2 id="nullif"><code>nullif</code></h2>
<p>Returns <em>null</em> if <em>expression1</em> equals <em>expression2</em>; otherwise it returns <em>expression1</em>.
This can be used to perform the inverse operation of <a href="#coalesce"><code>coalesce</code></a>.</p>
<pre tabindex="0"><code>nullif(expression1, expression2)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression1</strong>: Expression to compare and return if equal to expression2.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>expression2</strong>: Expression to compare to expression1.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="nvl"><code>nvl</code></h2>
<p>Returns <em>expression2</em> if <em>expression1</em> is NULL; otherwise it returns <em>expression1</em>.</p>
<pre tabindex="0"><code>nvl(expression1, expression2)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression1</strong>: return if expression1 not is NULL.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>expression2</strong>: return if expression1 is NULL.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="nvl2"><code>nvl2</code></h2>
<p>Returns <em>expression2</em> if <em>expression1</em> is not NULL; otherwise it returns <em>expression3</em>.</p>
<pre tabindex="0"><code>nvl2(expression1, expression2, expression3)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression1</strong>: conditional expression.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>expression2</strong>: return if expression1 is not NULL.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>expression3</strong>: return if expression1 is NULL.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="ifnull"><code>ifnull</code></h2>
<p><em>Alias of <a href="#nvl">nvl</a>.</em></p>
