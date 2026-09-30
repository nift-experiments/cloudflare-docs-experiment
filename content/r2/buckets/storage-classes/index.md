---
cp9:
  canonical: https://developers.cloudflare.com/r2/buckets/storage-classes/
  description: Choose between R2 Standard and Infrequent Access storage to optimize cost and access patterns.
  full_title: Storage classes · Cloudflare R2 docs
  head_html: <title>Storage classes · Cloudflare R2 docs</title><meta name="generator" content="Nift"><meta name="description" content="Choose between R2 Standard and Infrequent Access storage to optimize cost and access patterns."><link rel="canonical" href="https://developers.cloudflare.com/r2/buckets/storage-classes/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2/buckets/storage-classes/index.md"><meta property="og:title" content="Storage classes · Cloudflare R2 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Choose between R2 Standard and Infrequent Access storage to optimize cost and access patterns."><meta property="og:url" content="https://developers.cloudflare.com/r2/buckets/storage-classes/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2"><meta name="algolia_product_filter" content="R2"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="R2"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2/buckets/storage-classes/#page","headline":"Storage classes \u00b7 Cloudflare R2 docs","description":"Choose between R2 Standard and Infrequent Access storage to optimize cost and access patterns.","url":"https://developers.cloudflare.com/r2/buckets/storage-classes/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2/buckets/storage-classes/
  schema: 1
---
<p>Storage classes allow you to trade off between the cost of storage and the cost of accessing data. Every object stored in R2 has an associated storage class.</p>
<p>All storage classes share the following characteristics:</p>
<ul>
<li>Compatible with Workers API, S3 API, and public buckets.</li>
<li>99.999999999% (eleven 9s) of annual durability.</li>
<li>No minimum object size.</li>
</ul>
<h2 id="available-storage-classes">Available storage classes</h2>
<table>
<thead>
<tr>
<th>Storage class</th>
<th>Minimum storage duration</th>
<th>Data retrieval fees (processing)</th>
<th>Egress fees (data transfer to Internet)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Standard</td>
<td>None</td>
<td>None</td>
<td>None</td>
</tr>
<tr>
<td>Infrequent Access</td>
<td>30 days</td>
<td>Yes</td>
<td>None</td>
</tr>
</tbody>
</table>
<p>For more information on how storage classes impact pricing, refer to <a href="/r2/pricing/">Pricing</a>.</p>
<h3 id="standard-storage">Standard storage</h3>
<p>Standard storage is designed for data that is accessed frequently. This is the default storage class for new R2 buckets unless otherwise specified.</p>
<h4 id="example-use-cases">Example use cases</h4>
<ul>
<li>Website and application data</li>
<li>Media content (e.g., images, video)</li>
<li>Storing large datasets for analysis and processing</li>
<li>AI training data</li>
<li>Other workloads involving frequently accessed data</li>
</ul>
<h3 id="infrequent-access-storage">Infrequent Access storage</h3>
<p>Infrequent Access storage is ideal for data that is accessed less frequently. This storage class offers lower storage cost compared to Standard storage, but includes <a href="/r2/pricing/#data-retrieval">retrieval fees</a> and a 30 day <a href="/r2/pricing/#minimum-storage-duration">minimum storage duration</a> requirement.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11477.md")
</aside>
<h4 id="example-use-cases-1">Example use cases</h4>
<ul>
<li>Long-term data archiving (for example, logs and historical records needed for compliance)</li>
<li>Data backup and disaster recovery</li>
<li>Long tail user-generated content</li>
</ul>
<h2 id="set-default-storage-class-for-buckets">Set default storage class for buckets</h2>
<p>By setting the default storage class for a bucket, all objects uploaded into the bucket will automatically be assigned the selected storage class unless otherwise specified. Default storage class can be changed after bucket creation in the Dashboard.</p>
<p>To learn more about creating R2 buckets, refer to <a href="/r2/buckets/create-buckets/">Create new buckets</a>.</p>
<h2 id="set-storage-class-for-objects">Set storage class for objects</h2>
<h3 id="specify-storage-class-during-object-upload">Specify storage class during object upload</h3>
<p>To learn more about how to specify the storage class for new objects, refer to the <a href="/r2/api/workers/">Workers API</a> and <a href="/r2/api/s3/">S3 API</a> documentation.</p>
<h3 id="use-object-lifecycle-rules-to-transition-objects-to-infrequent-access-storage">Use object lifecycle rules to transition objects to Infrequent Access storage</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11476.md")
</aside>
<p>To learn more about how to transition objects from Standard storage to Infrequent Access storage, refer to <a href="/r2/buckets/object-lifecycles/">Object lifecycles</a>.</p>
<h2 id="change-storage-class-for-objects">Change storage class for objects</h2>
<p>You can change the storage class of an object which is already stored in R2 using the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html"><code>CopyObject</code> API</a>.</p>
<p>Use the <code>x-amz-storage-class</code> header to change between <code>STANDARD</code> and <code>STANDARD_IA</code>.</p>
<p>An example of switching an object from <code>STANDARD</code> to <code>STANDARD_IA</code> using <code>aws cli</code> is shown below:</p>
<pre tabindex="0"><code class="language-sh">aws s3api copy-object \&#10;  &#45;-endpoint-url https://&lt;ACCOUNT_ID&gt;.r2.cloudflarestorage.com \&#10;  &#45;-bucket bucket-name \&#10;  &#45;-key path/to/object.txt \&#10;  &#45;-copy-source /bucket-name/path/to/object.txt \&#10;  &#45;-storage-class STANDARD_IA&#10;</code></pre>
<ul>
<li>Refer to <a href="/r2/examples/aws/aws-cli/">aws CLI</a> for more information on using <code>aws CLI</code>.</li>
<li>Refer to <a href="/r2/api/s3/api/#object-level-operations">object-level operations</a> for the full list of object-level API operations with R2-compatible S3 API.</li>
</ul>
