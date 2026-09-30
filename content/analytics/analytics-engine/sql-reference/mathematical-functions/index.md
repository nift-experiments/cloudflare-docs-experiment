---
cp9:
  canonical: https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/mathematical-functions/
  description: Mathematical SQL functions for Analytics Engine.
  full_title: SQL Reference · Cloudflare Analytics docs
  head_html: <title>SQL Reference · Cloudflare Analytics docs</title><meta name="generator" content="Nift"><meta name="description" content="Mathematical SQL functions for Analytics Engine."><link rel="canonical" href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/mathematical-functions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/mathematical-functions/index.md"><meta property="og:title" content="SQL Reference · Cloudflare Analytics docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Mathematical SQL functions for Analytics Engine."><meta property="og:url" content="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/mathematical-functions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Analytics"><meta name="algolia_product_filter" content="Analytics"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Workers Analytics Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/mathematical-functions/#page","headline":"SQL Reference \u00b7 Cloudflare Analytics docs","description":"Mathematical SQL functions for Analytics Engine.","url":"https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/mathematical-functions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /analytics/analytics-engine/sql-reference/mathematical-functions/
  schema: 1
---
<h2 id="intdiv">intDiv</h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">intDiv(a, b)&#10;</code></pre>
<p>Divide <code>a</code> by <code>b</code>, rounding the answer down to the nearest whole number.</p>
<h2 id="log">log <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">log(&lt;expression&gt;)&#10;</code></pre>
<p><code>log</code> returns the natural logarithm of a provided number. <code>ln</code> is also available as an alias.</p>
<p>Examples:</p>
<pre tabindex="0"><code class="language-sql">&#45;- get the natural logarithm of the double1 column&#10;log(double1)&#10;</code></pre>
<h2 id="pow">pow <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">pow(&lt;expression&gt;, &lt;expression&gt;)&#10;</code></pre>
<p><code>pow</code> returns the first argument raised to the power of the second argument.</p>
<p>Examples:</p>
<pre tabindex="0"><code class="language-sql">&#45;- get the square of the double1 column&#10;pow(double1, 2)&#10;</code></pre>
<h2 id="round">round <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">round(&lt;expression&gt;[, n])&#10;</code></pre>
<p><code>round</code> returns a number rounded to the nearest whole number, or to a given number of decimal points specified by the second argument.</p>
<p>Examples:</p>
<pre tabindex="0"><code class="language-sql">&#45;- round 5.5 to 6&#10;round(5.5)&#10;&#45;- round 3.14 to 3.1&#10;round(3.14, 1)&#10;</code></pre>
<h2 id="floor">floor <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">floor(&lt;expression&gt;[, n])&#10;</code></pre>
<p><code>floor</code> returns a number rounded down to a whole number, or rounded down to a given number of decimal points specified by the second argument.</p>
<p>Examples:</p>
<pre tabindex="0"><code class="language-sql">&#45;- round down 5.5 to 5&#10;floor(5.5)&#10;&#45;- round down 3.14 to 3.1&#10;floor(3.14, 1)&#10;</code></pre>
<h2 id="ceil">ceil <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre tabindex="0"><code class="language-sql">ceil(&lt;expression&gt;[, n])&#10;</code></pre>
<p><code>ceil</code> returns a number rounded up to a whole number, or rounded up to a given number of decimal points specified by the second argument.</p>
<p>Examples:</p>
<pre tabindex="0"><code class="language-sql">&#45;- round up 5.5 to 6&#10;ceil(5.5)&#10;&#45;- round up 3.14 to 3.2&#10;ceil(3.14, 1)&#10;</code></pre>
