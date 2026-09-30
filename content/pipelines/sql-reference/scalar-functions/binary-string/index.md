---
cp9:
  canonical: https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/binary-string/
  description: Scalar functions for manipulating binary strings
  full_title: Binary string functions · Cloudflare Pipelines Docs
  head_html: <title>Binary string functions · Cloudflare Pipelines Docs</title><meta name="generator" content="Nift"><meta name="description" content="Scalar functions for manipulating binary strings"><link rel="canonical" href="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/binary-string/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/binary-string/index.md"><meta property="og:title" content="Binary string functions · Cloudflare Pipelines Docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Scalar functions for manipulating binary strings"><meta property="og:url" content="https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/binary-string/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Pipelines"><meta name="algolia_product_filter" content="Pipelines"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_additional_products" content="Pipelines"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/binary-string/#page","headline":"Binary string functions \u00b7 Cloudflare Pipelines Docs","description":"Scalar functions for manipulating binary strings","url":"https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/binary-string/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /pipelines/sql-reference/scalar-functions/binary-string/
  schema: 1
---
<p><em>Cloudflare Pipelines scalar function implementations are based on
<a href="https://arrow.apache.org/datafusion/">Apache DataFusion</a> (via <a href="https://www.arroyo.dev/">Arroyo</a>) and these docs are derived from
the DataFusion function reference.</em></p>
<h2 id="encode"><code>encode</code></h2>
<p>Encode binary data into a textual representation.</p>
<pre tabindex="0"><code>encode(expression, format)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li>
<p><strong>expression</strong>: Expression containing string or binary data</p>
</li>
<li>
<p><strong>format</strong>: Supported formats are: <code>base64</code>, <code>hex</code></p>
</li>
</ul>
<p><strong>Related functions</strong>:
<a href="#decode">decode</a></p>
<h2 id="decode"><code>decode</code></h2>
<p>Decode binary data from textual representation in string.</p>
<pre tabindex="0"><code>decode(expression, format)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li>
<p><strong>expression</strong>: Expression containing encoded string data</p>
</li>
<li>
<p><strong>format</strong>: Same arguments as <a href="#encode">encode</a></p>
</li>
</ul>
<p><strong>Related functions</strong>:
<a href="#encode">encode</a></p>
