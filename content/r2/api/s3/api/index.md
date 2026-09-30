---
cp9:
  canonical: https://developers.cloudflare.com/r2/api/s3/api/
  description: Review which S3 API operations and features R2 supports, including implementation status.
  full_title: S3 API compatibility · Cloudflare R2 docs
  head_html: <title>S3 API compatibility · Cloudflare R2 docs</title><meta name="generator" content="Nift"><meta name="description" content="Review which S3 API operations and features R2 supports, including implementation status."><link rel="canonical" href="https://developers.cloudflare.com/r2/api/s3/api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2/api/s3/api/index.md"><meta property="og:title" content="S3 API compatibility · Cloudflare R2 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Review which S3 API operations and features R2 supports, including implementation status."><meta property="og:url" content="https://developers.cloudflare.com/r2/api/s3/api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2"><meta name="algolia_product_filter" content="R2"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="R2"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2/api/s3/api/#page","headline":"S3 API compatibility \u00b7 Cloudflare R2 docs","description":"Review which S3 API operations and features R2 supports, including implementation status.","url":"https://developers.cloudflare.com/r2/api/s3/api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2/api/s3/api/
  schema: 1
---
<p>R2 implements the S3 API to allow users and their applications to migrate with ease. When comparing to AWS S3, Cloudflare has removed some API operations' features and added others. The S3 API operations are listed below with their current implementation status. Feature implementation is currently in progress. Refer back to this page for updates.
The API is available via the <code>https://&lt;ACCOUNT_ID&gt;.r2.cloudflarestorage.com</code> endpoint. Find your <a href="/fundamentals/account/find-account-and-zone-ids/">account ID in the Cloudflare dashboard</a>.</p>
<h2 id="how-to-read-this-page">How to read this page</h2>
<p>This page has two sections: bucket-level operations and object-level operations.</p>
<p>Each section will have two tables: a table of implemented APIs and a table of unimplemented APIs.</p>
<p>Refer the feature column of each table to review which features of an API have been implemented and which have not.</p>
<p>✅ Feature Implemented <br/>
🚧 Feature Implemented (Experimental) <br/>
❌ Feature Not Implemented</p>
<h2 id="bucket-region">Bucket region</h2>
<p>When using the S3 API, the region for an R2 bucket is <code>auto</code>. For compatibility with tools that do not allow you to specify a region, an empty value and <code>us-east-1</code> will alias to the <code>auto</code> region.</p>
<p>This also applies to the <code>LocationConstraint</code> for the <code>CreateBucket</code> API.</p>
<h2 id="checksum-types">Checksum Types</h2>
<p>Checksums have an algorithm and a <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#ChecksumTypes">type</a>. Refer to the table below.</p>
<table>
<thead>
<tr>
<th>Checksum Algorithm</th>
<th><code>FULL_OBJECT</code></th>
<th><code>COMPOSITE</code></th>
</tr>
</thead>
<tbody>
<tr>
<td>CRC-64/NVME (<code>CRC64NVME</code>)</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>CRC-32 (<code>CRC32</code>)</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>CRC-32C (<code>CRC32C</code>)</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>SHA-1 (<code>SHA1</code>)</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>SHA-256 (<code>SHA256</code>)</td>
<td>❌</td>
<td>✅</td>
</tr>
</tbody>
</table>
<h2 id="bucket-level-operations">Bucket-level operations</h2>
<p>The following tables are related to bucket-level operations.</p>
<h3 id="implemented-bucket-level-operations">Implemented bucket-level operations</h3>
<p>Below is a list of implemented bucket-level operations. Refer to the Feature column to review which features have been implemented (✅) and have not been implemented (❌).</p>
<table>
<thead>
<tr>
<th>API Name</th>
<th>Feature</th>
</tr>
</thead>
<tbody>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html">ListBuckets</a></td>
<td></td>
</tr>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadBucket.html">HeadBucket</a></td>
<td>❌ Bucket Owner: <br/>   ❌ x-amz-expected-bucket-owner</td>
</tr>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html">CreateBucket</a></td>
<td>❌ ACL: <br/>   ❌ x-amz-acl <br/>   ❌ x-amz-grant-full-control <br/>   ❌ x-amz-grant-read <br/>   ❌ x-amz-grant-read-acp <br/>   ❌ x-amz-grant-write <br/>   ❌ x-amz-grant-write-acp <br/> ❌ Object Locking: <br/>   ❌ x-amz-bucket-object-lock-enabled <br/> ❌ Bucket Owner: <br/>   ❌ x-amz-expected-bucket-owner</td>
</tr>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html">DeleteBucket</a></td>
<td>❌ Bucket Owner: <br/>   ❌ x-amz-expected-bucket-owner</td>
</tr>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketCors.html">DeleteBucketCors</a></td>
<td>❌ Bucket Owner: <br/>   ❌ x-amz-expected-bucket-owner</td>
</tr>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketCors.html">GetBucketCors</a></td>
<td>❌ Bucket Owner: <br/>   ❌ x-amz-expected-bucket-owner</td>
</tr>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html">GetBucketLifecycleConfiguration</a></td>
<td>❌ Bucket Owner: <br/>   ❌ x-amz-expected-bucket-owner</td>
</tr>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLocation.html">GetBucketLocation</a></td>
<td>❌ Bucket Owner: <br/>   ❌ x-amz-expected-bucket-owner</td>
</tr>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html">GetBucketEncryption</a></td>
<td>❌ Bucket Owner: <br/> ❌ x-amz-expected-bucket-owner</td>
</tr>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketCors.html">PutBucketCors</a></td>
<td>❌ Checksums: <br/>   ❌ x-amz-sdk-checksum-algorithm <br/>   ❌ x-amz-checksum-algorithm <br/> ❌ Bucket Owner: <br/>   ❌ x-amz-expected-bucket-owner</td>
</tr>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html">PutBucketLifecycleConfiguration</a></td>
<td>❌ Checksums: <br/>   ❌ x-amz-sdk-checksum-algorithm <br/>   ❌ x-amz-checksum-algorithm <br/> ❌ Bucket Owner: <br/>   ❌ x-amz-expected-bucket-owner</td>
</tr>
</tbody>
</table>
<h3 id="unimplemented-bucket-level-operations">Unimplemented bucket-level operations</h3>
<details class="nb-details"><summary>Unimplemented bucket-level operations</summary><div class="nb-details-body">
@input("content/.markup/bodies/11541.md")
</div></details>
<h2 id="object-level-operations">Object-level operations</h2>
<p>The following tables are related to object-level operations.</p>
<h3 id="implemented-object-level-operations">Implemented object-level operations</h3>
<p>Below is a list of implemented object-level operations. Refer to the Feature column to review which features have been implemented (✅) and have not been implemented (❌).</p>
<h4 id="behaviors-limitations">Behaviors &amp; Limitations</h4>
<p><strong>UploadPart:</strong> Uploading to the same part number replaces the previous part. If a subsequent upload to the same part fails, the original part is lost and must be re-uploaded.</p>
<table>
<thead>
<tr>
<th>API Name</th>
<th>Feature</th>
</tr>
</thead>
<tbody>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html">HeadObject</a></td>
<td>✅ Conditional Operations: <br/>   ✅ If-Match <br/>   ✅ If-Modified-Since <br/>   ✅ If-None-Match <br/>   ✅ If-Unmodified-Since <br/> ✅ Range: <br/>   ✅ Range (has no effect in HeadObject) <br/>   ✅ partNumber <br/> ✅ SSE-C: <br/>   ✅ x-amz-server-side-encryption-customer-algorithm <br/>   ✅ x-amz-server-side-encryption-customer-key <br/>   ✅ x-amz-server-side-encryption-customer-key-MD5 <br/> ❌ Request Payer: <br/>   ❌ x-amz-request-payer <br/> ❌ Bucket Owner: <br/>   ❌ x-amz-expected-bucket-owner</td>
</tr>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html">ListObjects</a></td>
<td>Query Parameters: <br/>   ✅ delimiter <br/>   ✅ encoding-type <br/>   ✅ marker <br/>   ✅ max-keys <br/>   ✅ prefix <br/> ❌ Request Payer: <br/>   ❌ x-amz-request-payer <br/> ❌ Bucket Owner: <br/>   ❌ x-amz-expected-bucket-owner</td>
</tr>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html">ListObjectsV2</a></td>
<td>Query Parameters: <br/>   ✅ list-type <br/>   ✅ continuation-token <br/>   ✅ delimiter <br/>   ✅ encoding-type <br/>   ✅ fetch-owner <br/>   ✅ max-keys <br/>   ✅ prefix <br/>   ✅ start-after <br/> ❌ Request Payer: <br/>   ❌ x-amz-request-payer <br/> ❌ Bucket Owner: <br/>   ❌ x-amz-expected-bucket-owner</td>
</tr>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html">GetObject</a></td>
<td>✅ Conditional Operations: <br/>   ✅ If-Match <br/>   ✅ If-Modified-Since <br/>   ✅ If-None-Match <br/>   ✅ If-Unmodified-Since <br/> ✅ Range: <br/>   ✅ Range <br/>   ✅ PartNumber <br/> ✅ SSE-C: <br/>   ✅ x-amz-server-side-encryption-customer-algorithm <br/>   ✅ x-amz-server-side-encryption-customer-key <br/>   ✅ x-amz-server-side-encryption-customer-key-MD5 <br/> ❌ Request Payer: <br/>   ❌ x-amz-request-payer <br/> ❌ Bucket Owner: <br/>   ❌ x-amz-expected-bucket-owner</td>
</tr>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html">PutObject</a></td>
<td>✅ Conditional Operations: <br/>   ✅ If-Match <br/>   ✅ If-Modified-Since <br/>   ✅ If-None-Match <br/>   ✅ If-Unmodified-Since <br/> ✅ System Metadata: <br/>   ✅ Content-Type <br/>   ✅ Cache-Control <br/>   ✅ Content-Disposition <br/>   ✅ Content-Encoding <br/>   ✅ Content-Language <br/>   ✅ Expires <br/>   ✅ Content-MD5 <br/> ✅ Storage Class: <br/>   ✅ x-amz-storage-class <br/>     ✅ STANDARD <br/>     ✅ STANDARD_IA <br/> ❌ Object Lifecycle <br/> ❌ Website: <br/>   ❌ x-amz-website-redirect-location <br/> ❌ SSE: <br/>   ❌ x-amz-server-side-encryption-aws-kms-key-id <br/>   ❌ x-amz-server-side-encryption <br/>   ❌ x-amz-server-side-encryption-context <br/>   ❌ x-amz-server-side-encryption-bucket-key-enabled <br/> ✅ SSE-C: <br/>   ✅ x-amz-server-side-encryption-customer-algorithm <br/>   ✅ x-amz-server-side-encryption-customer-key <br/>   ✅ x-amz-server-side-encryption-customer-key-MD5 <br/> ❌ Request Payer: <br/>   ❌ x-amz-request-payer <br/> ❌ Tagging: <br/>   ❌ x-amz-tagging <br/> ❌ Object Locking: <br/>   ❌ x-amz-object-lock-mode <br/>   ❌ x-amz-object-lock-retain-until-date <br/>   ❌ x-amz-object-lock-legal-hold <br/> ❌ ACL: <br/>   ❌ x-amz-acl <br/>   ❌ x-amz-grant-full-control <br/>   ❌ x-amz-grant-read <br/>   ❌ x-amz-grant-read-acp <br/>   ❌ x-amz-grant-write-acp <br/> ❌ Bucket Owner: <br/>   ❌ x-amz-expected-bucket-owner</td>
</tr>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html">DeleteObject</a></td>
<td>❌ Multi-factor authentication: <br/>   ❌ x-amz-mfa <br/> ❌ Object Locking: <br/>   ❌ x-amz-bypass-governance-retention <br/> ❌ Request Payer: <br/>   ❌ x-amz-request-payer <br/> ❌ Bucket Owner: <br/>   ❌ x-amz-expected-bucket-owner</td>
</tr>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjects.html">DeleteObjects</a></td>
<td>❌ Multi-factor authentication: <br/>   ❌ x-amz-mfa <br/> ❌ Object Locking: <br/>   ❌ x-amz-bypass-governance-retention <br/> ❌ Request Payer: <br/>   ❌ x-amz-request-payer <br/> ❌ Bucket Owner: <br/>   ❌ x-amz-expected-bucket-owner</td>
</tr>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html">ListMultipartUploads</a></td>
<td>✅ Query Parameters: <br/>   ✅ delimiter <br/>   ✅ encoding-type <br/>   ✅ key-marker <br/>   ✅️ max-uploads <br/>   ✅ prefix <br/>   ✅ upload-id-marker</td>
</tr>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html">CreateMultipartUpload</a></td>
<td>✅ System Metadata: <br/>   ✅ Content-Type <br/>   ✅ Cache-Control <br/>   ✅ Content-Disposition <br/>   ✅ Content-Encoding <br/>   ✅ Content-Language <br/>   ✅ Expires <br/>   ✅ Content-MD5 <br/> ✅ Storage Class: <br/>   ✅ x-amz-storage-class <br/>     ✅ STANDARD <br/>     ✅ STANDARD_IA <br/> ❌ Website: <br/>   ❌ x-amz-website-redirect-location <br/> ❌ SSE: <br/>   ❌ x-amz-server-side-encryption-aws-kms-key-id <br/>   ❌ x-amz-server-side-encryption <br/>   ❌ x-amz-server-side-encryption-context <br/>   ❌ x-amz-server-side-encryption-bucket-key-enabled <br/> ✅ SSE-C: <br/>   ✅ x-amz-server-side-encryption-customer-algorithm <br/>   ✅ x-amz-server-side-encryption-customer-key <br/>   ✅ x-amz-server-side-encryption-customer-key-MD5 <br/> ❌ Request Payer: <br/>   ❌ x-amz-request-payer <br/> ❌ Tagging: <br/>   ❌ x-amz-tagging <br/> ❌ Object Locking: <br/>   ❌ x-amz-object-lock-mode <br/>   ❌ x-amz-object-lock-retain-until-date <br/>   ❌ x-amz-object-lock-legal-hold <br/> ❌ ACL: <br/>   ❌ x-amz-acl <br/>   ❌ x-amz-grant-full-control <br/>   ❌ x-amz-grant-read <br/>   ❌ x-amz-grant-read-acp <br/>   ❌ x-amz-grant-write-acp <br/> ❌ Bucket Owner: <br/>   ❌ x-amz-expected-bucket-owner</td>
</tr>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html">CompleteMultipartUpload</a></td>
<td>❌ Bucket Owner: <br/>   ❌ x-amz-expected-bucket-owner <br/> ❌ Request Payer: <br/>   ❌ x-amz-request-payer</td>
</tr>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html">AbortMultipartUpload</a></td>
<td>❌ Request Payer: <br/>   ❌ x-amz-request-payer</td>
</tr>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html">CopyObject</a></td>
<td>✅ Operation Metadata: <br/>   ✅ x-amz-metadata-directive <br/> ✅ System Metadata: <br/>   ✅ Content-Type <br/>   ✅ Cache-Control <br/>   ✅ Content-Disposition <br/>   ✅ Content-Encoding <br/>   ✅ Content-Language <br/>   ✅ Expires <br/> ✅ Conditional Operations: <br/>   ✅ x-amz-copy-source <br/>   ✅ x-amz-copy-source-if-match <br/>   ✅ x-amz-copy-source-if-modified-since <br/>   ✅ x-amz-copy-source-if-none-match <br/>   ✅ x-amz-copy-source-if-unmodified-since <br/> ✅ Storage Class: <br/>   ✅ x-amz-storage-class <br/>     ✅ STANDARD <br/>     ✅ STANDARD_IA <br/> ❌ ACL: <br/>   ❌ x-amz-acl <br/>   ❌ x-amz-grant-full-control <br/>   ❌ x-amz-grant-read <br/>   ❌ x-amz-grant-read-acp <br/>   ❌ x-amz-grant-write-acp <br/> ❌ Website: <br/>   ❌ x-amz-website-redirect-location <br/> ❌ SSE: <br/>   ❌ x-amz-server-side-encryption <br/>   ❌ x-amz-server-side-encryption-aws-kms-key-id <br/>   ❌ x-amz-server-side-encryption-context <br/>   ❌ x-amz-server-side-encryption-bucket-key-enabled <br/> ✅ SSE-C: <br/>   ✅ x-amz-server-side-encryption-customer-algorithm <br/>   ✅ x-amz-server-side-encryption-customer-key <br/>   ✅ x-amz-server-side-encryption-customer-key-MD5 <br/>   ✅ x-amz-copy-source-server-side-encryption-customer-algorithm <br/>   ✅ x-amz-copy-source-server-side-encryption-customer-key <br/>   ✅ x-amz-copy-source-server-side-encryption-customer-key-MD5 <br/> ❌ Request Payer: <br/>   ❌ x-amz-request-payer <br/> ❌ Tagging: <br/>   ❌ x-amz-tagging <br/>   ❌ x-amz-tagging-directive <br/> ❌ Object Locking: <br/>   ❌ x-amz-object-lock-mode <br/>   ❌ x-amz-object-lock-retain-until-date <br/>   ❌ x-amz-object-lock-legal-hold <br/> ❌ Bucket Owner: <br/>   ❌ x-amz-expected-bucket-owner <br/>   ❌ x-amz-source-expected-bucket-owner <br/> ❌ Checksums: <br/>   ❌ x-amz-checksum-algorithm</td>
</tr>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html">UploadPart</a></td>
<td>✅ System Metadata: <br/>   ✅ Content-MD5 <br/> ❌ SSE: <br/>   ❌ x-amz-server-side-encryption <br/> ✅ SSE-C: <br/>   ✅ x-amz-server-side-encryption-customer-algorithm <br/>   ✅ x-amz-server-side-encryption-customer-key <br/>   ✅ x-amz-server-side-encryption-customer-key-MD5 <br/> ❌ Request Payer: <br/>   ❌ x-amz-request-payer <br/> ❌ Bucket Owner: <br/>   ❌ x-amz-expected-bucket-owner</td>
</tr>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html">UploadPartCopy</a></td>
<td>✅ Copy Source: <br/>   ✅ x-amz-copy-source (required) <br/> ❌ Conditional Operations: <br/>   ❌ x-amz-copy-source-if-match <br/>   ❌ x-amz-copy-source-if-modified-since <br/>   ❌ x-amz-copy-source-if-none-match <br/>   ❌ x-amz-copy-source-if-unmodified-since <br/> ✅ Range: <br/>   ✅ x-amz-copy-source-range <br/> ✅ SSE-C: <br/>   ✅ x-amz-server-side-encryption-customer-algorithm <br/>   ✅ x-amz-server-side-encryption-customer-key <br/>   ✅ x-amz-server-side-encryption-customer-key-MD5 <br/>   ✅ x-amz-copy-source-server-side-encryption-customer-algorithm <br/>   ✅ x-amz-copy-source-server-side-encryption-customer-key <br/>   ✅ x-amz-copy-source-server-side-encryption-customer-key-MD5 <br/> ❌ Request Payer: <br/>   ❌ x-amz-request-payer <br/> ❌ Bucket Owner: <br/>   ❌ x-amz-expected-bucket-owner <br/>   ❌ x-amz-source-expected-bucket-owner</td>
</tr>
<tr>
<td>✅ <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html">ListParts</a></td>
<td>Query Parameters: <br/>   ✅ max-parts <br/>   ✅ part-number-marker <br/> ❌ Request Payer: <br/>   ❌ x-amz-request-payer <br/> ❌ Bucket Owner: <br/>   ❌ x-amz-expected-bucket-owner</td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/11540.md")
</aside>
<h3 id="unimplemented-object-level-operations">Unimplemented object-level operations</h3>
<details class="nb-details"><summary>Unimplemented object-level operations</summary><div class="nb-details-body">
@input("content/.markup/bodies/11542.md")
</div></details>
