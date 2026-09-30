---
cp9:
  canonical: https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/bit-functions/
  description: Bitwise SQL functions for Analytics Engine.
  full_title: SQL Reference · Cloudflare Analytics docs
  head_html: <title>SQL Reference · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Bitwise SQL functions for Analytics Engine."><link rel="canonical" href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/bit-functions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/bit-functions/index.md"><meta property="og:title" content="SQL Reference · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Bitwise SQL functions for Analytics Engine."><meta property="og:url" content="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/bit-functions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers Analytics Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/bit-functions/#page","headline":"SQL Reference \u00b7 Cloudflare Analytics docs","description":"Bitwise SQL functions for Analytics Engine.","url":"https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/bit-functions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/analytics-engine/sql-reference/bit-functions/
  schema: 1
---
<h2 id="bitand">bitAnd <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">bitAnd(a, b)&#10;</code></pre>
<p><code>bitAnd</code> returns the bitwise AND of expressions <code>a</code> and <code>b</code>.</p>
<p>Examples:</p>
<pre tabindex="0"><code class="language-sql">&#45;- perform 0b1 &amp; 0b11&#10;bitAnd(1, 3)&#10;&#45;- extract the least significant bit of the integer value of double1&#10;bitAnd(toUInt8(double1), 1)&#10;</code></pre>
<h2 id="bitcount">bitCount <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">bitCount(a)&#10;</code></pre>
<p><code>bitCount</code> returns the number of bits set to one in the binary representation of <code>a</code>.</p>
<p>Examples:</p>
<pre tabindex="0"><code class="language-sql">&#45;- get the number of 1 bits in the binary representation of the float `double1`&#10;bitCount(double1)&#10;&#45;- get the number of 1 bits in the binary representation of `double1` as an integer&#10;bitCount(toUInt32(double1))&#10;&#45;- select rows where at least 5 bits are 1&#10;SELECT * WHERE bitCount(double1) &gt; 5&#10;</code></pre>
<h2 id="bithammingdistance">bitHammingDistance <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">bitHammingDistance(x, y)&#10;</code></pre>
<p><code>bitHammingDistance</code> returns the number of bits that differ between <code>x</code> and <code>y</code>.</p>
<p>Examples:</p>
<pre tabindex="0"><code class="language-sql">&#45;- returns zero&#10;bitHammingDistance(1, 1)&#10;&#45;- returns 2&#10;bitHammingDistance(3, 0)&#10;</code></pre>
<h2 id="bitnot">bitNot <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">bitNot(a)&#10;</code></pre>
<p><code>bitNot</code> returns <code>a</code> with all bits flipped.</p>
<p>Examples:</p>
<pre tabindex="0"><code class="language-sql">bitNot(1)&#10;</code></pre>
<h2 id="bitor">bitOr <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">bitOr(a, b)&#10;</code></pre>
<p><code>bitOr</code> returns the inclusive bitwise or of <code>a</code> and <code>b</code>.</p>
<p>Examples:</p>
<pre tabindex="0"><code class="language-sql">&#45;- returns 3&#10;bitOr(1, 2)&#10;</code></pre>
<h2 id="bitrotateleft">bitRotateLeft <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">bitRotateLeft(a, n)&#10;</code></pre>
<p><code>bitRotateLeft</code> rotates all bits in <code>a</code> left by <code>n</code> positions.</p>
<p>Examples:</p>
<pre tabindex="0"><code class="language-sql">&#45;- returns 2&#10;bitRotateLeft(1, 1)&#10;&#45;- returns 1&#10;bitRotateLeft(128, 1)&#10;</code></pre>
<h2 id="bitrotateright">bitRotateRight <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">bitRotateRight(a, n)&#10;</code></pre>
<p><code>bitRotateRight</code> rotates all bits in <code>a</code> right by <code>n</code> positions.</p>
<p>Examples:</p>
<pre tabindex="0"><code class="language-sql">&#45;- returns 128&#10;bitRotateRight(1, 1)&#10;&#45;- returns 3&#10;bitRotateRight(12, 2)&#10;</code></pre>
<h2 id="bitshiftleft">bitShiftLeft <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">bitShiftLeft(a, n)&#10;</code></pre>
<p><code>bitShiftLeft</code> shifts all bits in <code>a</code> left by <code>n</code> positions.</p>
<p>Examples:</p>
<pre tabindex="0"><code class="language-sql">&#45;- returns 2&#10;bitShiftLeft(1, 1)&#10;&#45;- returns 0&#10;bitShiftLeft(128, 1)&#10;</code></pre>
<h2 id="bitshiftright">bitShiftRight <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">bitShiftRight(a, n)&#10;</code></pre>
<p><code>bitShiftRight</code> shifts all bits in <code>a</code> right by <code>n</code> positions.</p>
<p>Examples:</p>
<pre tabindex="0"><code class="language-sql">&#45;- returns 0&#10;bitShiftRight(1, 1)&#10;&#45;- returns 3&#10;bitShiftRight(12, 2)&#10;</code></pre>
<h2 id="bittest">bitTest <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">bitTest(a, n)&#10;</code></pre>
<p><code>bitTest</code> returns the value of bit <code>n</code> in number <code>a</code>.</p>
<p>Examples:</p>
<pre tabindex="0"><code class="language-sql">&#45;- returns 1&#10;bitTest(3, 1)&#10;&#45;- return 0&#10;bitTest(2, 1)&#10;&#45;- select rows where a particular bit is 1&#10;SELECT * WHERE bitTest(double1, 2)&#10;</code></pre>
<h2 id="bitxor">bitXor <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">bitXor(a, b)&#10;</code></pre>
<p><code>bitXor</code> returns the bitwise exclusive-or of <code>a</code> and <code>b</code>.</p>
<p>Examples:</p>
<pre tabindex="0"><code class="language-sql">&#45;- returns 3&#10;bitXor(1, 2)&#10;&#45;- returns 0&#10;bitXor(3, 3)&#10;</code></pre>
