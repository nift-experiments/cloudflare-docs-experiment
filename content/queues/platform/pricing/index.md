---
cp9:
  canonical: https://developers.cloudflare.com/queues/platform/pricing/
  description: Cloudflare Queues pricing for standard operations with included free usage.
  full_title: Cloudflare Queues - Pricing · Cloudflare Queues docs
  head_html: <title>Cloudflare Queues - Pricing · Cloudflare Queues docs</title><meta name="generator" content="Nift"><meta name="description" content="Cloudflare Queues pricing for standard operations with included free usage."><link rel="canonical" href="https://developers.cloudflare.com/queues/platform/pricing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/queues/platform/pricing/index.md"><meta property="og:title" content="Cloudflare Queues - Pricing · Cloudflare Queues docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Cloudflare Queues pricing for standard operations with included free usage."><meta property="og:url" content="https://developers.cloudflare.com/queues/platform/pricing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Queues"><meta name="algolia_product_filter" content="Queues"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Queues"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/queues/platform/pricing/#page","headline":"Cloudflare Queues - Pricing \u00b7 Cloudflare Queues docs","description":"Cloudflare Queues pricing for standard operations with included free usage.","url":"https://developers.cloudflare.com/queues/platform/pricing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /queues/platform/pricing/
  schema: 1
---
<p>Cloudflare Queues charges for the total number of operations against each of your queues during a given month.</p>
<ul>
<li>An operation is counted for each 64 KB of data that is written, read, or deleted.</li>
<li>Messages larger than 64 KB are charged as if they were multiple messages: for example, a 65 KB message and a 127 KB message would both incur two operation charges when written, read, or deleted.</li>
<li>A KB is defined as 1,000 bytes, and each message includes approximately 100 bytes of internal metadata.</li>
<li>Operations are per message, not per batch. A batch of 10 messages (the default batch size), if processed, would incur 10x write, 10x read, and 10x delete operations: one for each message in the batch.</li>
<li>There are no data transfer (egress) or throughput (bandwidth) charges.</li>
</ul>
<table>
<thead>
<tr>
<th></th>
<th>Workers Free</th>
<th>Workers Paid</th>
</tr>
</thead>
<tbody>
<tr>
<td>Standard operations</td>
<td>10,000 operations/day included</td>
<td>1,000,000 operations/month included + $0.40/million operations</td>
</tr>
<tr>
<td>Message retention</td>
<td>24 hours (non-configurable)</td>
<td>4 days default, configurable up to 14 days</td>
</tr>
</tbody>
</table>
<p>In most cases, it takes 3 operations to deliver a message: 1 write, 1 read, and 1 delete. Therefore, you can use the following formula to estimate your monthly bill:</p>
<pre tabindex="0"><code class="language-txt">((Number of Messages * 3) - 1,000,000) / 1,000,000  * $0.40&#10;</code></pre>
<p>Additionally:</p>
<ul>
<li>Each retry incurs a read operation. A batch of 10 messages that is retried would incur 10 operations for each retry.</li>
<li>Messages that reach the maximum retries and that are written to a <a href="/queues/configuration/batching-retries/">Dead Letter Queue</a> incur a write operation for each 64 KB chunk. A message that was retried 3 times (the default), fails delivery on the fourth time and is written to a Dead Letter Queue would incur five (5) read operations.</li>
<li>Messages that are written to a queue, but that reach the maximum persistence duration (or &quot;expire&quot;) before they are read, incur only a write and delete operation per 64 KB chunk.</li>
</ul>
<h2 id="examples">Examples</h2>
<p>If an application writes, reads and deletes (consumes) one million messages a day (in a 30 day month), and each message is less than 64 KB in size, the estimated bill for the month would be:</p>
<table>
<thead>
<tr>
<th></th>
<th>Total Usage</th>
<th>Free Usage</th>
<th>Billed Usage</th>
<th>Price</th>
</tr>
</thead>
<tbody>
<tr>
<td>Standard operations</td>
<td>3 * 30 * 1,000,000</td>
<td>1,000,000</td>
<td>89,000,000</td>
<td>$35.60</td>
</tr>
<tr>
<td></td>
<td>(write, read, delete)</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>TOTAL</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$35.60</strong></td>
</tr>
</tbody>
</table>
<p>An application that writes, reads and deletes (consumes) 100 million ~127 KB messages (each message counts as two 64 KB chunks) per month would have an estimated bill resembling the following:</p>
<table>
<thead>
<tr>
<th></th>
<th>Total Usage</th>
<th>Free Usage</th>
<th>Billed Usage</th>
<th>Price</th>
</tr>
</thead>
<tbody>
<tr>
<td>Standard operations</td>
<td>2 * 3 * 100 * 1,000,000</td>
<td>1,000,000</td>
<td>599,000,000</td>
<td>$239.60</td>
</tr>
<tr>
<td></td>
<td>(2x ops for &gt; 64KB messages)</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>TOTAL</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$239.60</strong></td>
</tr>
</tbody>
</table>
