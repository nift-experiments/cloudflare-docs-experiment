---
cp9:
  canonical: https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/encoding-functions/
  description: Encoding SQL functions for Analytics Engine queries.
  full_title: SQL Reference · Cloudflare Analytics docs
  head_html: <title>SQL Reference · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Encoding SQL functions for Analytics Engine queries."><link rel="canonical" href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/encoding-functions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/encoding-functions/index.md"><meta property="og:title" content="SQL Reference · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Encoding SQL functions for Analytics Engine queries."><meta property="og:url" content="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/encoding-functions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers Analytics Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/encoding-functions/#page","headline":"SQL Reference \u00b7 Cloudflare Analytics docs","description":"Encoding SQL functions for Analytics Engine queries.","url":"https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/encoding-functions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/analytics-engine/sql-reference/encoding-functions/
  schema: 1
---
<h2 id="bin">bin <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">bin(&lt;expression&gt;)&#10;</code></pre>
<p><code>bin</code> returns a string containing the binary representation of its argument.</p>
<p>Examples:</p>
<pre tabindex="0"><code class="language-sql">&#45;- get the binary representation of 1&#10;bin(1)&#10;&#45;- get the binary representation of a string`&#10;bin(&#x27;abc&#x27;)&#10;</code></pre>
<h2 id="hex">hex <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">hex(&lt;expression&gt;)&#10;</code></pre>
<p><code>hex</code> returns a string containing the hexadecimal representation of its argument.</p>
<p>Examples:</p>
<pre tabindex="0"><code class="language-sql">&#45;- get the hexadecimal representation of 1&#10;hex(1)&#10;&#45;- get the hexadecimal representation of a string`&#10;hex(&#x27;abc&#x27;)&#10;</code></pre>
