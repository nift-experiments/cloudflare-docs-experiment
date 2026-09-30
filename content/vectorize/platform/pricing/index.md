---
cp9:
  canonical: https://developers.cloudflare.com/vectorize/platform/pricing/
  description: Vectorize pricing based on queried and stored vector dimensions.
  full_title: Pricing · Cloudflare Vectorize docs
  head_html: <title>Pricing · Cloudflare Vectorize docs</title><meta name="generator" content="Nift"><meta name="description" content="Vectorize pricing based on queried and stored vector dimensions."><link rel="canonical" href="https://developers.cloudflare.com/vectorize/platform/pricing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/vectorize/platform/pricing/index.md"><meta property="og:title" content="Pricing · Cloudflare Vectorize docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Vectorize pricing based on queried and stored vector dimensions."><meta property="og:url" content="https://developers.cloudflare.com/vectorize/platform/pricing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Vectorize"><meta name="algolia_product_filter" content="Vectorize"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Vectorize"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/vectorize/platform/pricing/#page","headline":"Pricing \u00b7 Cloudflare Vectorize docs","description":"Vectorize pricing based on queried and stored vector dimensions.","url":"https://developers.cloudflare.com/vectorize/platform/pricing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /vectorize/platform/pricing/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="vectorize-is-now-generally-available">Vectorize is now Generally Available</h3>
@markup("md", "content/.markup/bodies/15261.md")
</aside>
<p>Vectorize bills are based on:</p>
<ul>
<li><strong>Queried Vector Dimensions</strong>: The total number of vector dimensions queried. If you have 10,000 vectors with 384-dimensions in an index, and make 100 queries against that index, your total queried vector dimensions would sum to 3.878 million (<code>(10000 + 100) * 384</code>).</li>
<li><strong>Stored Vector Dimensions</strong>: The total number of vector dimensions stored. If you have 1,000 vectors with 1536-dimensions in an index, your stored vector dimensions would sum to 1.536 million (<code>1000 * 1536</code>).</li>
</ul>
<p>You are not billed for CPU, memory, &quot;active index hours&quot;, or the number of indexes you create. If you are not issuing queries against your indexes, you are not billed for queried vector dimensions.</p>
<h2 id="billing-metrics">Billing metrics</h2>
<table>
<thead>
<tr>
<th></th>
<th><a href="/workers/platform/pricing/#workers">Workers Free</a></th>
<th><a href="/workers/platform/pricing/#workers">Workers Paid</a></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Total queried vector dimensions</strong></td>
<td>30 million queried vector dimensions / month</td>
<td>First 50 million queried vector dimensions / month included + $0.01 per million</td>
</tr>
<tr>
<td><strong>Total stored vector dimensions</strong></td>
<td>5 million stored vector dimensions</td>
<td>First 10 million stored vector dimensions + $0.05 per 100 million</td>
</tr>
</tbody>
</table>
<h3 id="calculating-vector-dimensions">Calculating vector dimensions</h3>
<p>To calculate your potential usage, calculate the queried vector dimensions and the stored vector dimensions, and multiply by the unit price. The formula is defined as <code>((queried vectors + stored vectors) * dimensions * ($0.01 / 1,000,000)) + (stored vectors * dimensions * ($0.05 / 100,000,000))</code></p>
<ul>
<li>For example, inserting 10,000 vectors of 768 dimensions each, and querying those 1,000 times per day (30,000 times per month) would be calculated as <code>((30,000 + 10,000) * 768) = 30,720,000</code> queried dimensions and <code>(10,000 * 768) = 7,680,000</code> stored dimensions (within the included monthly allocation)</li>
<li>Separately, and excluding the included monthly allocation, this would be calculated as <code>(30,000 + 10,000) * 768 * ($0.01 / 1,000,000) + (10,000 * 768 * ($0.05 / 100,000,000))</code> and sum to $0.31 per month.</li>
</ul>
<h3 id="usage-examples">Usage examples</h3>
<p>The following table defines a number of example use-cases and the estimated monthly cost for querying a Vectorize index. These estimates do not include the Vectorize usage that is part of the Workers Free and Paid plans.</p>
<table>
<thead>
<tr>
<th>Workload</th>
<th>Dimensions per vector</th>
<th>Stored dimensions</th>
<th>Queries per month</th>
<th>Calculation</th>
<th>Estimated total</th>
</tr>
</thead>
<tbody>
<tr>
<td>Experiment</td>
<td>384</td>
<td>5,000 vectors</td>
<td>10,000</td>
<td><code>((10000+5000)*384*(0.01/1000000))      + (5000*384*(0.05/100000000))</code></td>
<td>$0.06 / mo <sup>included</sup></td>
</tr>
<tr>
<td>Scaling</td>
<td>768</td>
<td>25,000 vectors</td>
<td>50,000</td>
<td><code>((50000+25000)*768*(0.01/1000000))     + (25000*768*(0.05/100000000))</code></td>
<td>$0.59 / mo <sup>most</sup></td>
</tr>
<tr>
<td>Production</td>
<td>768</td>
<td>50,000 vectors</td>
<td>200,000</td>
<td><code>((200000+50000)*768*(0.01/1000000))    + (50000*768*(0.05/100000000))</code></td>
<td>$1.94 / mo</td>
</tr>
<tr>
<td>Large</td>
<td>768</td>
<td>250,000 vectors</td>
<td>500,000</td>
<td><code>((500000+250000)*768*(0.01/1000000))   + (250000*768*(0.05/100000000))</code></td>
<td>$5.86 / mo</td>
</tr>
<tr>
<td>XL</td>
<td>1536</td>
<td>500,000 vectors</td>
<td>1,000,000</td>
<td><code>((1000000+500000)*1536*(0.01/1000000)) + (500000*1536*(0.05/100000000))</code></td>
<td>$23.42 / mo</td>
</tr>
</tbody>
</table>
<p><sup>included</sup> All of this usage would fall into the Vectorize usage
included in the Workers Free or Paid plan.</p>
<p><sup>most</sup> Most of this usage would fall into the Vectorize usage included
within the Workers Paid plan.</p>
<h2 id="frequently-asked-questions">Frequently Asked Questions</h2>
<p>Frequently asked questions related to Vectorize pricing:</p>
<ul>
<li>Will Vectorize always have a free tier?</li>
</ul>
<p>Yes, the <a href="/workers/platform/pricing/#workers">Workers free tier</a> will always include the ability to prototype and experiment with Vectorize for free.</p>
<ul>
<li>What happens if I exceed the monthly included reads, writes and/or storage on the paid tier?</li>
</ul>
<p>You will be billed for the additional reads, writes and storage according to <a href="#billing-metrics">Vectorize's pricing</a>.</p>
<ul>
<li>Does Vectorize charge for data transfer / egress?</li>
</ul>
<p>No.</p>
<ul>
<li>Do queries I issue from the HTTP API or the Wrangler command-line count as billable usage?</li>
</ul>
<p>Yes: any queries you issue against your index, including from the Workers API, HTTP API and CLI all count as usage.</p>
<ul>
<li>Does an empty index, with no vectors, contribute to storage?</li>
</ul>
<p>No. Empty indexes do not count as stored vector dimensions.</p>
