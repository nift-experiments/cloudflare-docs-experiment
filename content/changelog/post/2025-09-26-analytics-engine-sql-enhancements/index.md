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
