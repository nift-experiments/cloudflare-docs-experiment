---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-09-26-analytics-engine-sql-enhancements/
  description: New updates and improvements at Cloudflare.
  full_title: Workers Analytics Engine adds supports for new SQL functions · Changelog
  head_html: <title>Workers Analytics Engine adds supports for new SQL functions · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-09-26-analytics-engine-sql-enhancements/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Workers Analytics Engine adds supports for new SQL functions · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-09-26-analytics-engine-sql-enhancements/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-26-analytics-engine-sql-enhancements/#page","headline":"Workers Analytics Engine adds supports for new SQL functions \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-09-26-analytics-engine-sql-enhancements/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-09-26-analytics-engine-sql-enhancements/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 2, 2025</time><h2 id="post-title">Workers Analytics Engine adds supports for new SQL functions</h2>
<div class="changelog-badges"><span>workers-analytics-engine</span><span>workers</span></div><div class="changelog-body"><p>You can now perform more powerful queries directly in <a href="https://developers.cloudflare.com/analytics/analytics-engine/">Workers Analytics Engine</a> with a major expansion of our SQL function library.</p>
<p>Workers Analytics Engine allows you to ingest and store high-cardinality data at scale (such as custom analytics) and query your data through a simple SQL API.</p>
<p>Today, we've expanded Workers Analytics Engine's SQL capabilities with several new functions:</p>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/aggregate-functions/"><strong>New aggregate functions:</strong></a></p>
<ul>
<li><code>argMin()</code> - Returns the value associated with the minimum in a group</li>
<li><code>argMax()</code> - Returns the value associated with the maximum in a group</li>
<li><code>topK()</code> - Returns an array of the most frequent values in a group</li>
<li><code>topKWeighted()</code> - Returns an array of the most frequent values in a group using weights</li>
<li><code>first_value()</code> - Returns the first value in an ordered set of values within a partition</li>
<li><code>last_value()</code> - Returns the last value in an ordered set of values within a partition</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/bit-functions/"><strong>New bit functions:</strong></a></p>
<ul>
<li><code>bitAnd()</code> - Returns the bitwise AND of two expressions</li>
<li><code>bitCount()</code> - Returns the number of bits set to one in the binary representation of a number</li>
<li><code>bitHammingDistance()</code> - Returns the number of bits that differ between two numbers</li>
<li><code>bitNot()</code> - Returns a number with all bits flipped</li>
<li><code>bitOr()</code> - Returns the inclusive bitwise OR of two expressions</li>
<li><code>bitRotateLeft()</code> - Rotates all bits in a number left by specified positions</li>
<li><code>bitRotateRight()</code> - Rotates all bits in a number right by specified positions</li>
<li><code>bitShiftLeft()</code> - Shifts all bits in a number left by specified positions</li>
<li><code>bitShiftRight()</code> - Shifts all bits in a number right by specified positions</li>
<li><code>bitTest()</code> - Returns the value of a specific bit in a number</li>
<li><code>bitXor()</code> - Returns the bitwise exclusive-or of two expressions</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/mathematical-functions/"><strong>New mathematical functions:</strong></a></p>
<ul>
<li><code>abs()</code> - Returns the absolute value of a number</li>
<li><code>log()</code> - Computes the natural logarithm of a number</li>
<li><code>round()</code> - Rounds a number to a specified number of decimal places</li>
<li><code>ceil()</code> - Rounds a number up to the nearest integer</li>
<li><code>floor()</code> - Rounds a number down to the nearest integer</li>
<li><code>pow()</code> - Returns a number raised to the power of another number</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/string-functions/"><strong>New string functions:</strong></a></p>
<ul>
<li><code>lowerUTF8()</code> - Converts a string to lowercase using UTF-8 encoding</li>
<li><code>upperUTF8()</code> - Converts a string to uppercase using UTF-8 encoding</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/encoding-functions/"><strong>New encoding functions:</strong></a></p>
<ul>
<li><code>hex()</code> - Converts a number to its hexadecimal representation</li>
<li><code>bin()</code> - Converts a string to its binary representation</li>
</ul>
<p><a href="https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/type-conversion-functions/"><strong>New type conversion functions:</strong></a></p>
<ul>
<li><code>toUInt8()</code> - Converts any numeric expression, or expression resulting in a string representation of a decimal, into an unsigned 8 bit integer</li>
</ul>
<h4 id="ready-to-get-started">Ready to get started?</h4>
Whether you're building usage-based billing systems, customer analytics dashboards, or other custom analytics, these functions let you get the most out of your data. [Get started ](/analytics/analytics-engine/get-started/) with Workers Analytics Engine and explore all available functions in our [SQL reference documentation](/analytics/analytics-engine/sql-reference/).
</div></article></div>
