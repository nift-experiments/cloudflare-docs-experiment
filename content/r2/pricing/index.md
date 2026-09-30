---
cp9:
  canonical: https://developers.cloudflare.com/r2/pricing/
  description: R2 pricing for storage, Class A and Class B operations, and free tier details.
  full_title: Pricing · Cloudflare R2 docs
  head_html: <title>Pricing · Cloudflare R2 docs</title><meta name="generator" content="Nift"><meta name="description" content="R2 pricing for storage, Class A and Class B operations, and free tier details."><link rel="canonical" href="https://developers.cloudflare.com/r2/pricing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2/pricing/index.md"><meta property="og:title" content="Pricing · Cloudflare R2 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="R2 pricing for storage, Class A and Class B operations, and free tier details."><meta property="og:url" content="https://developers.cloudflare.com/r2/pricing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2"><meta name="algolia_product_filter" content="R2"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="R2"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2/pricing/#page","headline":"Pricing \u00b7 Cloudflare R2 docs","description":"R2 pricing for storage, Class A and Class B operations, and free tier details.","url":"https://developers.cloudflare.com/r2/pricing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2/pricing/
  schema: 1
---
<p>R2 charges based on the total volume of data stored, along with two classes of operations on that data:</p>
<ol>
<li><a href="#class-a-operations">Class A operations</a> which are more expensive and tend to mutate state.</li>
<li><a href="#class-b-operations">Class B operations</a> which tend to read existing state.</li>
</ol>
<p>For the Infrequent Access storage class, <a href="#data-retrieval">data retrieval</a> fees apply. There are no charges for egress bandwidth for any storage class.</p>
<p>All included usage is on a monthly basis.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/489.md")
</aside>
<h2 id="r2-pricing">R2 pricing</h2>
<table>
<thead>
<tr>
<th></th>
<th>Standard storage</th>
<th>Infrequent Access storage</th>
</tr>
</thead>
<tbody>
<tr>
<td>Storage</td>
<td>$0.015 / GB-month</td>
<td>$0.01 / GB-month</td>
</tr>
<tr>
<td>Class A Operations</td>
<td>$4.50 / million requests</td>
<td>$9.00 / million requests</td>
</tr>
<tr>
<td>Class B Operations</td>
<td>$0.36 / million requests</td>
<td>$0.90 / million requests</td>
</tr>
<tr>
<td>Data Retrieval (processing)</td>
<td>None</td>
<td>$0.01 / GB</td>
</tr>
<tr>
<td>Egress (data transfer to Internet)</td>
<td>Free <sup><a href="#footnote-1">1</a></sup></td>
<td>Free <sup><a href="#footnote-1">1</a></sup></td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="billable-unit-rounding">Billable unit rounding</h3>
@markup("md", "content/.markup/bodies/488.md")
</aside>
<h3 id="free-tier">Free tier</h3>
<p>You can use the following amount of storage and operations each month for free.</p>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
</tr>
</thead>
<tbody>
<tr>
<td>Storage</td>
<td>10 GB-month / month</td>
</tr>
<tr>
<td>Class A Operations</td>
<td>1 million requests / month</td>
</tr>
<tr>
<td>Class B Operations</td>
<td>10 million requests / month</td>
</tr>
<tr>
<td>Egress (data transfer to Internet)</td>
<td>Free <sup><a href="#footnote-1">1</a></sup></td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/487.md")
</aside>
<h3 id="storage-usage">Storage usage</h3>
<p>Storage is billed using gigabyte-month (GB-month) as the billing metric. A GB-month is calculated by averaging the <em>peak</em> storage per day over a billing period (30 days).</p>
<p>For example:</p>
<ul>
<li>Storing 1 GB constantly for 30 days will be charged as 1 GB-month.</li>
<li>Storing 3 GB constantly for 30 days will be charged as 3 GB-month.</li>
<li>Storing 1 GB for 5 days, then 3 GB for the remaining 25 days will be charged as <code>1 GB * 5/30 month + 3 GB * 25/30 month = 2.66 GB-month</code></li>
</ul>
<p>For objects stored in Infrequent Access storage, you will be charged for the object for the minimum storage duration even if the object was deleted or moved before the duration specified.</p>
<h3 id="class-a-operations">Class A operations</h3>
<p>Class A Operations include <code>ListBuckets</code>, <code>PutBucket</code>, <code>ListObjects</code>, <code>PutObject</code>, <code>CopyObject</code>, <code>CompleteMultipartUpload</code>, <code>CreateMultipartUpload</code>, <code>LifecycleStorageTierTransition</code>, <code>ListMultipartUploads</code>, <code>UploadPart</code>, <code>UploadPartCopy</code>, <code>ListParts</code>, <code>PutBucketEncryption</code>, <code>PutBucketCors</code> and <code>PutBucketLifecycleConfiguration</code>.</p>
<h3 id="class-b-operations">Class B operations</h3>
<p>Class B Operations include <code>HeadBucket</code>, <code>HeadObject</code>, <code>GetObject</code>, <code>UsageSummary</code>, <code>GetBucketEncryption</code>, <code>GetBucketLocation</code>, <code>GetBucketCors</code> and <code>GetBucketLifecycleConfiguration</code>.</p>
<h3 id="free-operations">Free operations</h3>
<p>Free operations include <code>DeleteObject</code>, <code>DeleteBucket</code> and <code>AbortMultipartUpload</code>.</p>
<h3 id="data-retrieval">Data retrieval</h3>
<p>Data retrieval fees apply when you access or retrieve data from the Infrequent Access storage class. This includes any time objects are read or copied.</p>
<h3 id="minimum-storage-duration">Minimum storage duration</h3>
<p>For objects stored in Infrequent Access storage, you will be charged for the object for the minimum storage duration even if the object was deleted, moved, or replaced before the specified duration.</p>
<table>
<thead>
<tr>
<th>Storage class</th>
<th>Minimum storage duration</th>
</tr>
</thead>
<tbody>
<tr>
<td>Standard storage</td>
<td>None</td>
</tr>
<tr>
<td>Infrequent Access storage</td>
<td>30 days</td>
</tr>
</tbody>
</table>
<h2 id="r2-data-catalog-pricing">R2 Data Catalog pricing</h2>
<p>R2 Data Catalog charges for catalog operations and compaction data processed, in addition to standard R2 storage and operations. For full details, refer to <a href="/r2-data-catalog/platform/pricing/">R2 Data Catalog pricing</a>.</p>
<h2 id="data-migration-pricing">Data migration pricing</h2>
<h3 id="super-slurper">Super Slurper</h3>
<p>Super Slurper is free to use. You are only charged for the Class A operations that Super Slurper makes to your R2 bucket. Objects with sizes &lt; 100MiB are uploaded to R2 in a single Class A operation. Larger objects use multipart uploads to increase transfer success rates and will perform multiple Class A operations. Note that your source bucket might incur additional charges as Super Slurper copies objects over to R2.</p>
<p>Once migration completes, you are charged for storage &amp; Class A/B operations as described in previous sections.</p>
<h3 id="sippy">Sippy</h3>
<p>Sippy is free to use. You are only charged for the operations Sippy makes to your R2 bucket. If a requested object is not present in R2, Sippy will copy it over from your source bucket. Objects with sizes &lt; 200MiB are uploaded to R2 in a single Class A operation. Larger objects use multipart uploads to increase transfer success rates, and will perform multiple Class A operations. Note that your source bucket might incur additional charges as Sippy copies objects over to R2.</p>
<p>As objects are migrated to R2, they are served from R2, and you are charged for storage &amp; Class A/B operations as described in previous sections.</p>
<h2 id="pricing-calculator">Pricing calculator</h2>
<p>To learn about potential cost savings from using R2, refer to the <a href="https://r2-calculator.cloudflare.com/">R2 pricing calculator</a>.</p>
<h2 id="r2-billing-examples">R2 billing examples</h2>
<h3 id="standard-storage-example">Standard storage example</h3>
<p>If a user writes 1,000 objects in R2 <strong>Standard storage</strong> for 1 month with an average size of 1 GB and reads each object 1,000 times during the month, the estimated cost for the month would be:</p>
<table>
<thead>
<tr>
<th></th>
<th>Usage</th>
<th>Free Tier</th>
<th>Billable Quantity</th>
<th>Price</th>
</tr>
</thead>
<tbody>
<tr>
<td>Storage</td>
<td>(1,000 objects) * (1 GB per object) = 1,000 GB-months</td>
<td>10 GB-months</td>
<td>990 GB-months</td>
<td>$14.85</td>
</tr>
<tr>
<td>Class A Operations</td>
<td>(1,000 objects) * (1 write per object) = 1,000 writes</td>
<td>1 million</td>
<td>0</td>
<td>$0.00</td>
</tr>
<tr>
<td>Class B Operations</td>
<td>(1,000 objects) * (1,000 reads per object) = 1 million reads</td>
<td>10 million</td>
<td>0</td>
<td>$0.00</td>
</tr>
<tr>
<td>Data retrieval (processing)</td>
<td>(1,000 objects) * (1 GB per object) = 1,000 GB</td>
<td>NA</td>
<td>None</td>
<td>$0.00</td>
</tr>
<tr>
<td><strong>TOTAL</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$14.85</strong></td>
</tr>
</tbody>
</table>
<h3 id="infrequent-access-example">Infrequent access example</h3>
<p>If a user writes 1,000 objects in R2 Infrequent Access storage with an average size of 1 GB, stores them for 5 days, and then deletes them (delete operations are free), and during those 5 days each object is read 1,000 times, the estimated cost for the month would be:</p>
<table>
<thead>
<tr>
<th></th>
<th>Usage</th>
<th>Free Tier</th>
<th>Billable Quantity</th>
<th>Price</th>
</tr>
</thead>
<tbody>
<tr>
<td>Storage</td>
<td>(1,000 objects) * (1 GB per object) = 1,000 GB-months</td>
<td>NA</td>
<td>1,000 GB-months</td>
<td>$10.00</td>
</tr>
<tr>
<td>Class A Operations</td>
<td>(1,000 objects) * (1 write per object) = 1,000 writes</td>
<td>NA</td>
<td>1,000</td>
<td>$9.00</td>
</tr>
<tr>
<td>Class B Operations</td>
<td>(1,000 objects) * (1,000 reads per object) = 1 million reads</td>
<td>NA</td>
<td>1 million</td>
<td>$0.90</td>
</tr>
<tr>
<td>Data retrieval (processing)</td>
<td>(1,000 objects) * (1 GB per object) = 1,000 GB</td>
<td>NA</td>
<td>1,000 GB</td>
<td>$10.00</td>
</tr>
<tr>
<td><strong>TOTAL</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$29.90</strong></td>
</tr>
</tbody>
</table>
<p>Note that the minimal storage duration for infrequent access storage is 30 days, which means the billable quantity is 1,000 GB-months, rather than 167 GB-months.</p>
<h3 id="asset-hosting">Asset hosting</h3>
<p>If a user writes 100,000 files with an average size of 100 KB object and reads 10,000,000 objects per day, the estimated cost in a month would be:</p>
<table>
<thead>
<tr>
<th></th>
<th>Usage</th>
<th>Free Tier</th>
<th>Billable Quantity</th>
<th>Price</th>
</tr>
</thead>
<tbody>
<tr>
<td>Storage</td>
<td>(100,000 objects) * (100KB per object)</td>
<td>10 GB-months</td>
<td>0 GB-months</td>
<td>$0.00</td>
</tr>
<tr>
<td>Class A Operations</td>
<td>(100,000 writes)</td>
<td>1 million</td>
<td>0</td>
<td>$0.00</td>
</tr>
<tr>
<td>Class B Operations</td>
<td>(10,000,000 reads per day) * (30 days)</td>
<td>10 million</td>
<td>290,000,000</td>
<td>$104.40</td>
</tr>
<tr>
<td><strong>TOTAL</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$104.40</strong></td>
</tr>
</tbody>
</table>
<h2 id="cloudflare-billing-policy">Cloudflare billing policy</h2>
<p>To learn more about how usage is billed, refer to <a href="/billing/understand/billing-policy/">Cloudflare Billing Policy</a>.</p>
<h2 id="frequently-asked-questions">Frequently asked questions</h2>
<h3 id="will-i-be-charged-for-unauthorized-requests-to-my-r2-bucket">Will I be charged for unauthorized requests to my R2 bucket?</h3>
<p>No. You are not charged for operations when the caller does not have permission to make the request (HTTP 401 <code>Unauthorized</code> response status code).</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Egressing directly from R2, including via the [Workers API](/r2/api/workers/), [S3 API](/r2/api/s3/), and [`r2.dev` domains](/r2/buckets/public-buckets/#enable-managed-public-access) does not incur data transfer (egress) charges and is free. If you connect other metered services to an R2 bucket, you may be charged by those services.</li></ol></section>
