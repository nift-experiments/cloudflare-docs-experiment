---
cp9:
  canonical: https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/hashing/
  description: Scalar functions for hashing values
  full_title: Hashing functions · Cloudflare Pipelines Docs
  head_html: <title>Hashing functions · Cloudflare Pipelines Docs</title><meta name="generator" content="Nift"><meta name="description" content="Scalar functions for hashing values"><link rel="canonical" href="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/hashing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/hashing/index.md"><meta property="og:title" content="Hashing functions · Cloudflare Pipelines Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Scalar functions for hashing values"><meta property="og:url" content="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/hashing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pipelines"><meta name="algolia_product_filter" content="Pipelines"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_additional_products" content="Pipelines"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/hashing/#page","headline":"Hashing functions \u00b7 Cloudflare Pipelines Docs","description":"Scalar functions for hashing values","url":"https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/hashing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pipelines/sql-reference/scalar-functions/hashing/
  schema: 1
---
<p><em>Cloudflare Pipelines scalar function implementations are based on
<a href="https://arrow.apache.org/datafusion/">Apache DataFusion</a> (via <a href="https://www.arroyo.dev/">Arroyo</a>) and these docs are derived from
the DataFusion function reference.</em></p>
<h2 id="digest"><code>digest</code></h2>
<p>Computes the binary hash of an expression using the specified algorithm.</p>
<pre tabindex="0"><code>digest(expression, algorithm)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
<li><strong>algorithm</strong>: String expression specifying algorithm to use.
Must be one of:
<ul>
<li>md5</li>
<li>sha224</li>
<li>sha256</li>
<li>sha384</li>
<li>sha512</li>
<li>blake2s</li>
<li>blake2b</li>
<li>blake3</li>
</ul>
</li>
</ul>
<h2 id="md5"><code>md5</code></h2>
<p>Computes an MD5 128-bit checksum for a string expression.</p>
<pre tabindex="0"><code>md5(expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
</ul>
<h2 id="sha224"><code>sha224</code></h2>
<p>Computes the SHA-224 hash of a binary string.</p>
<pre tabindex="0"><code>sha224(expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
</ul>
<h2 id="sha256"><code>sha256</code></h2>
<p>Computes the SHA-256 hash of a binary string.</p>
<pre tabindex="0"><code>sha256(expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
</ul>
<h2 id="sha384"><code>sha384</code></h2>
<p>Computes the SHA-384 hash of a binary string.</p>
<pre tabindex="0"><code>sha384(expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
</ul>
<h2 id="sha512"><code>sha512</code></h2>
<p>Computes the SHA-512 hash of a binary string.</p>
<pre tabindex="0"><code>sha512(expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression</strong>: String expression to operate on.
Can be a constant, column, or function, and any combination of string operators.</li>
</ul>
