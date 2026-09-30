---
cp9:
  canonical: https://developers.cloudflare.com/r2/platform/limits/
  description: Account, bucket, and object limits for Cloudflare R2 storage.
  full_title: Limits · Cloudflare R2 docs
  head_html: <title>Limits · Cloudflare R2 docs</title><meta name="generator" content="Nift"><meta name="description" content="Account, bucket, and object limits for Cloudflare R2 storage."><link rel="canonical" href="https://developers.cloudflare.com/r2/platform/limits/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2/platform/limits/index.md"><meta property="og:title" content="Limits · Cloudflare R2 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Account, bucket, and object limits for Cloudflare R2 storage."><meta property="og:url" content="https://developers.cloudflare.com/r2/platform/limits/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2"><meta name="algolia_product_filter" content="R2"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="R2"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2/platform/limits/#page","headline":"Limits \u00b7 Cloudflare R2 docs","description":"Account, bucket, and object limits for Cloudflare R2 storage.","url":"https://developers.cloudflare.com/r2/platform/limits/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2/platform/limits/
  schema: 1
---
<table>
<thead>
<tr>
<th>Feature</th>
<th>Limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Data storage per bucket</td>
<td>Unlimited</td>
</tr>
<tr>
<td>Number of objects per bucket</td>
<td>Unlimited</td>
</tr>
<tr>
<td>Maximum number of buckets per account</td>
<td>1,000,000</td>
</tr>
<tr>
<td>Maximum rate of bucket management operations per bucket <sup><a href="#footnote-1">1</a></sup></td>
<td>50 per second</td>
</tr>
<tr>
<td>Number of custom domains per bucket</td>
<td>100</td>
</tr>
<tr>
<td>Object key length</td>
<td>1,024 bytes</td>
</tr>
<tr>
<td>Object metadata size</td>
<td>8,192 bytes</td>
</tr>
<tr>
<td>Object size</td>
<td>5 TiB per object <sup><a href="#footnote-2">2</a></sup></td>
</tr>
<tr>
<td>Maximum upload size <sup><a href="#footnote-3">3</a></sup></td>
<td>5 GiB (single-part) / 4.995 TiB (multi-part) <sup><a href="#footnote-4">4</a></sup></td>
</tr>
<tr>
<td>Maximum upload parts</td>
<td>10,000</td>
</tr>
<tr>
<td>Maximum concurrent writes to the same object name (key)</td>
<td>1 per second <sup><a href="#footnote-5">5</a></sup></td>
</tr>
</tbody>
</table>
<p>Limits specified in MiB (mebibyte), GiB (gibibyte), or TiB (tebibyte) are storage units of measurement based on base-2. 1 GiB (gibibyte) is equivalent to 2<sup>30</sup> bytes (or 1024<sup>3</sup> bytes). This is distinct from 1 GB (gigabyte), which is 10<sup>9</sup> bytes (or 1000<sup>3</sup> bytes).</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="need-a-higher-limit">Need a higher limit?</h3>
@markup("md", "content/.markup/bodies/11376.md")
</aside>
<h2 id="rate-limiting-on-managed-public-buckets-through-r2-dev">Rate limiting on managed public buckets through <code>r2.dev</code></h2>
<p>Managed public bucket access through an <code>r2.dev</code> subdomain is not intended for production usage and has a variable rate limit applied to it. The <code>r2.dev</code> endpoint for your bucket is designed to enable testing.</p>
<ul>
<li>If you exceed the rate limit (hundreds of requests/second), requests to your <code>r2.dev</code> endpoint will be temporarily throttled and you will receive a <code>429 Too Many Requests</code> response.</li>
<li>Bandwidth (throughput) may also be throttled when using the <code>r2.dev</code> endpoint.</li>
</ul>
<p>For production use cases, connect a <a href="/r2/buckets/public-buckets/#custom-domains">custom domain</a> to your bucket. Custom domains allow you to serve content from a domain you control (for example, <code>assets.example.com</code>), configure fine-grained caching, set up redirect and rewrite rules, mutate content via <a href="/workers/">Cloudflare Workers</a>, and get detailed URL-level analytics for content served from your R2 bucket.</p>
<h2 id="cloudflare-rest-api">Cloudflare REST API</h2>
<p>The <a href="/api/resources/r2/">Cloudflare REST API</a> is rate limited to 1,200 requests per five minutes across all R2 REST API operations on your account.</p>
<p>For high-throughput object operations, use the <a href="/r2/api/s3/api/">S3-compatible API</a> or <a href="/r2/api/workers/workers-api-reference/">Workers API</a> instead. The Cloudflare REST API is best suited for lower-volume management and configuration operations.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Bucket management operations include creating, deleting, listing, and configuring buckets. This limit does _not_ apply to reading or writing objects to a bucket.</li>
<li id="footnote-2">The object size limit is 5 GiB less than 5 TiB, so 4.995 TiB.</li>
<li id="footnote-3">Max upload size applies to uploading a file via one request, uploading a part of a multipart upload, or copying into a part of a multipart upload. If you have a Worker, its inbound request size is constrained by [Workers request limits](/workers/platform/limits#request-limits). The max upload size limit does not apply to subrequests.</li>
<li id="footnote-4">The max upload size is 5 MiB less than 5 GiB, so 4.995 GiB.</li>
<li id="footnote-5">Concurrent writes to the same object name (key) at a higher rate return HTTP 429 (rate limited) responses.</li></ol></section>
