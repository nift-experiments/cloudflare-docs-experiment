---
cp9:
  canonical: https://developers.cloudflare.com/r2/platform/release-notes/
  description: Latest changes and updates to Cloudflare R2 object storage.
  full_title: Release notes · Cloudflare R2 docs
  head_html: <title>Release notes · Cloudflare R2 docs</title><meta name="generator" content="Nift"><meta name="description" content="Latest changes and updates to Cloudflare R2 object storage."><link rel="canonical" href="https://developers.cloudflare.com/r2/platform/release-notes/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2/platform/release-notes/index.md"><link rel="alternate" type="application/rss+xml" href="https://developers.cloudflare.com/r2/platform/release-notes/index.xml"><meta property="og:title" content="Release notes · Cloudflare R2 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Latest changes and updates to Cloudflare R2 object storage."><meta property="og:url" content="https://developers.cloudflare.com/r2/platform/release-notes/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_product" content="R2"><meta name="algolia_product_filter" content="R2"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Changelog"><meta name="algolia_content_type" content="Changelog"><meta name="pcx_additional_products" content="R2"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/r2/platform/release-notes/#page","headline":"Release notes \u00b7 Cloudflare R2 docs","description":"Latest changes and updates to Cloudflare R2 object storage.","url":"https://developers.cloudflare.com/r2/platform/release-notes/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2/platform/release-notes/
  schema: 1
---
<h2 id="2026-04-27">2026-04-27</h2><ul>
<li>You can now <a href="/r2/buckets/delete-buckets/">empty a bucket</a> or <a href="/r2/objects/delete-objects/#delete-a-folder">delete folders</a> directly from the R2 dashboard without writing scripts or configuring lifecycle rules.</li>
</ul><h2 id="2025-09-23">2025-09-23</h2><ul>
<li>Fixed a bug where you could attempt to delete objects even if they had a bucket lock rule applied on the dashboard. Previously, they would momentarily vanish from the table but reappear after a page refresh. Now, the delete action is disabled on locked objects in the dashboard.</li>
</ul><h2 id="2025-09-22">2025-09-22</h2><ul>
<li>We’ve updated the R2 dashboard with a cleaner look to make it easier to find what you need and take action. You can find instructions for how you can use R2 with the various API interfaces in the side panel, and easily access documentation at the bottom.</li>
</ul><h2 id="2025-07-03">2025-07-03</h2><ul>
<li>The CRC-64/NVME Checksum algorithm is now supported for both single and multipart objects. This also brings support for the <code>FULL_OBJECT</code> Checksum Type on Multipart Uploads. See Checksum Type Compatibility <a href="/r2/api/s3/api/">here</a>.</li>
</ul><h2 id="2024-12-03">2024-12-03</h2><ul>
<li><a href="/r2/examples/ssec/">Server-side Encryption with Customer-Provided Keys</a> is now available to all users via the Workers and S3-compatible APIs.</li>
</ul><h2 id="2024-11-21">2024-11-21</h2><ul>
<li>Sippy can now be enabled on buckets in <a href="/r2/reference/data-location/#jurisdictional-restrictions">jurisdictions</a> (e.g., EU, FedRAMP).</li>
<li>Fixed an issue with Sippy where GET/HEAD requests to objects with certain special characters would result in error responses.</li>
</ul><h2 id="2024-11-20">2024-11-20</h2><ul>
<li>Oceania (OC) is now available as an R2 region.</li>
<li>The default maximum number of buckets per account is now 1 million. If you need more than 1 million buckets, contact <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a>.</li>
<li>Public buckets accessible via custom domain now support Smart <a href="/r2/buckets/public-buckets/#caching">Tiered Cache</a>.</li>
</ul><h2 id="2024-11-19">2024-11-19</h2><ul>
<li>R2 <a href="/workers/wrangler/commands/#r2-bucket-lifecycle-add"><code>bucket lifecycle</code> command</a> added to Wrangler. Supports listing, adding, and removing object lifecycle rules.</li>
</ul><h2 id="2024-11-14">2024-11-14</h2><ul>
<li>R2 <a href="/workers/wrangler/commands/r2-bucket-info"><code>bucket info</code> command</a> added to Wrangler. Displays location of bucket and common metrics.</li>
</ul><h2 id="2024-11-08">2024-11-08</h2><ul>
<li>R2 <a href="/workers/wrangler/commands/#r2-bucket-dev-url-enable"><code>bucket dev-url</code> command</a> added to Wrangler. Supports enabling, disabling, and getting status of bucket's <a href="/r2/buckets/public-buckets/#enable-managed-public-access">r2.dev public access URL</a>.</li>
</ul><h2 id="2024-11-06">2024-11-06</h2><ul>
<li>R2 <a href="/workers/wrangler/commands/#r2-bucket-domain-add"><code>bucket domain</code> command</a> added to Wrangler. Supports listing, adding, removing, and updating <a href="/r2/buckets/public-buckets/#custom-domains">R2 bucket custom domains</a>.</li>
</ul><h2 id="2024-11-01">2024-11-01</h2><ul>
<li>Add <code>minTLS</code> to response of <a href="/api/resources/r2/subresources/buckets/subresources/domains/subresources/custom/methods/list/">list custom domains</a> endpoint.</li>
</ul><h2 id="2024-10-28">2024-10-28</h2><ul>
<li>Add <a href="/api/resources/r2/subresources/buckets/subresources/domains/subresources/custom/methods/get/">get custom domain</a> endpoint.</li>
</ul><h2 id="2024-10-21">2024-10-21</h2><ul>
<li>Event notifications can now be configured for R2 buckets in <a href="/r2/reference/data-location/#jurisdictional-restrictions">jurisdictions</a> (e.g., EU, FedRAMP).</li>
</ul><h2 id="2024-09-26">2024-09-26</h2><ul>
<li><a href="https://blog.cloudflare.com/builder-day-2024-announcements/#event-notifications-for-r2-is-now-ga">Event notifications for R2</a> is now generally available. Event notifications now support higher throughput (up to 5,000 messages per second per Queue), can be configured in the dashboard and Wrangler, and support for lifecycle deletes.</li>
</ul><h2 id="2024-09-18">2024-09-18</h2><ul>
<li>Add the ability to set and <a href="/r2/buckets/public-buckets/#minimum-tls-version">update minimum TLS version</a> for R2 bucket custom domains.</li>
</ul><h2 id="2024-08-26">2024-08-26</h2><ul>
<li>Added support for configuring R2 bucket custom domains via <a href="/api/resources/r2/subresources/buckets/subresources/domains/subresources/custom/methods/create/">API</a>.</li>
</ul><h2 id="2024-08-21">2024-08-21</h2><ul>
<li><a href="/r2/data-migration/sippy/">Sippy</a> is now generally available. Metrics for ongoing migrations can now be found in the dashboard or via the GraphQL analytics API.</li>
</ul><h2 id="2024-07-08">2024-07-08</h2><ul>
<li>Added migration log for <a href="/r2/data-migration/super-slurper/">Super Slurper</a> to the migration summary in the dashboard.</li>
</ul><h2 id="2024-06-12">2024-06-12</h2><ul>
<li><a href="/r2/data-migration/super-slurper/">Super Slurper</a> now supports migrating objects up to 1TB in size.</li>
</ul><h2 id="2024-06-07">2024-06-07</h2><ul>
<li>Fixed an issue that prevented Sippy from copying over objects from S3 buckets with SSE set up.</li>
</ul><h2 id="2024-06-06">2024-06-06</h2><ul>
<li>R2 will now ignore the <code>x-purpose</code> request parameter.</li>
</ul><h2 id="2024-05-29">2024-05-29</h2><ul>
<li>Added support for <a href="/r2/buckets/storage-classes/">Infrequent Access</a> storage class (beta).</li>
</ul><h2 id="2024-05-24">2024-05-24</h2><ul>
<li>Added <a href="/api/resources/r2/subresources/temporary_credentials/methods/create/">create temporary access tokens</a> endpoint.</li>
</ul><h2 id="2024-04-03">2024-04-03</h2><ul>
<li><a href="/r2/buckets/event-notifications/">Event notifications</a> for R2 is now available as an open beta.</li>
<li>Super Slurper now supports migration from <a href="/r2/data-migration/super-slurper/#supported-cloud-storage-providers">Google Cloud Storage</a>.</li>
</ul><h2 id="2024-02-20">2024-02-20</h2><ul>
<li>When an <code>OPTIONS</code> request against the public entrypoint does not include an <code>origin</code> header, an <code>HTTP 400</code> instead of an <code>HTTP 401</code> is returned.</li>
</ul><h2 id="2024-02-06">2024-02-06</h2><ul>
<li>The response shape of <code>GET /buckets/:bucket/sippy</code> has changed.</li>
<li>The <code>/buckets/:bucket/sippy/validate</code> endpoint is exposed over APIGW to validate Sippy's configuration.</li>
<li>The shape of the configuration object when modifying Sippy's configuration has changed.</li>
</ul><h2 id="2024-02-02">2024-02-02</h2><ul>
<li>Updated <a href="/api/resources/r2/subresources/buckets/methods/get/">GetBucket</a> endpoint: Now fetches by <code>bucket_name</code> instead of <code>bucket_id</code>.</li>
</ul><h2 id="2024-01-30">2024-01-30</h2><ul>
<li>Fixed a bug where the API would accept empty strings in the <code>AllowedHeaders</code> property of <code>PutBucketCors</code> actions.</li>
</ul><h2 id="2024-01-26">2024-01-26</h2><ul>
<li>Parts are now automatically sorted in ascending order regardless of input during <code>CompleteMultipartUpload</code>.</li>
</ul><h2 id="2024-01-11">2024-01-11</h2><ul>
<li>Sippy is available for Google Cloud Storage (GCS) beta.</li>
</ul><h2 id="2023-12-11">2023-12-11</h2><ul>
<li>The <code>x-id</code> query param for <code>S3 ListBuckets</code> action is now ignored.</li>
<li>The <code>x-id</code> query param is now ignored for all S3 actions.</li>
</ul><h2 id="2023-10-23">2023-10-23</h2><ul>
<li><code>PutBucketCors</code> now only accepts valid origins.</li>
</ul><h2 id="2023-09-01">2023-09-01</h2><ul>
<li>Fixed an issue with <code>ListBuckets</code> where the <code>name_contains</code> parameter would also search over the jurisdiction name.</li>
</ul><h2 id="2023-08-23">2023-08-23</h2><ul>
<li>Config Audit Logs GA.</li>
</ul><h2 id="2023-08-11">2023-08-11</h2><ul>
<li>Users can now complete conditional multipart publish operations. When a condition failure occurs when publishing an upload, the upload is no longer available and is treated as aborted.</li>
</ul><h2 id="2023-07-05">2023-07-05</h2><ul>
<li>Improved performance for ranged reads on very large files. Previously ranged reads near the end of very large files would be noticeably slower than
ranged reads on smaller files. Performance should now be consistently good independent of filesize.</li>
</ul><h2 id="2023-06-21">2023-06-21</h2><ul>
<li><a href="/r2/objects/upload-objects/#etags">Multipart ETags</a> are now MD5
hashes.</li>
</ul><h2 id="2023-06-16">2023-06-16</h2><ul>
<li>Fixed a bug where calling <a href="/api/resources/r2/subresources/buckets/methods/get/">GetBucket</a> on a non-existent bucket would return a 500 instead of a 404.</li>
<li>Improved S3 compatibility for ListObjectsV1, now nextmarker is only set when truncated is true.</li>
<li>The R2 worker bindings now support parsing conditional headers with multiple etags. These etags can now be strong, weak or a wildcard. Previously the bindings only accepted headers containing a single strong etag.</li>
<li>S3 putObject now supports sha256 and sha1 checksums. These were already supported by the R2 worker bindings.</li>
<li>CopyObject in the S3 compatible api now supports Cloudflare specific headers which allow the copy operation to be conditional on the state of the destination object.</li>
</ul><h2 id="2023-04-01">2023-04-01</h2><ul>
<li><a href="/api/resources/r2/subresources/buckets/methods/get/">GetBucket</a> is now available for use through the Cloudflare API.</li>
<li><a href="https://developers.cloudflare.com/r2/reference/data-location/">Location hints</a> can now be set when creating a bucket, both through the S3 API, and the dashboard.</li>
</ul><h2 id="2023-03-16">2023-03-16</h2><ul>
<li>The ListParts API has been implemented and is available for use.</li>
<li>HTTP2 is now enabled by default for new custom domains linked to R2 buckets.</li>
<li>Object Lifecycles are now available for use.</li>
<li>Bug fix: Requests to public buckets will now return the <code>Content-Encoding</code> header for gzip files when <code>Accept-Encoding: gzip</code> is used.</li>
</ul><h2 id="2023-01-27">2023-01-27</h2><ul>
<li>R2 authentication tokens created via the R2 token page are now scoped
to a single account by default.</li>
</ul><h2 id="2022-12-07">2022-12-07</h2><ul>
<li>Fix CORS preflight requests for the S3 API, which allows using the S3 SDK in the browser.</li>
<li>Passing a range header to the <code>get</code> operation in the R2 bindings API should now work as expected.</li>
</ul><h2 id="2022-11-30">2022-11-30</h2><ul>
<li>Requests with the header <code>x-amz-acl: public-read</code> are no longer rejected.</li>
<li>Fixed issues with wildcard CORS rules and presigned URLs.</li>
<li>Fixed an issue where <code>ListObjects</code> would time out during delimited listing of unicode-normalized keys.</li>
<li>S3 API's <code>PutBucketCors</code> now rejects requests with unknown keys in the XML body.</li>
<li>Signing additional headers no longer breaks CORS preflight requests for presigned URLs.</li>
</ul><h2 id="2022-11-21">2022-11-21</h2><ul>
<li>Fixed a bug in <code>ListObjects</code> where <code>startAfter</code> would skip over objects with keys that have numbers right after the <code>startAfter</code> prefix.</li>
<li>Add worker bindings for multipart uploads.</li>
</ul><h2 id="2022-11-17">2022-11-17</h2><ul>
<li>Unconditionally return HTTP 206 on ranged requests to match behavior of other S3 compatible implementations.</li>
<li>Fixed a CORS bug where <code>AllowedHeaders</code> in the CORS config were being treated case-sensitively.</li>
</ul><h2 id="2022-11-08">2022-11-08</h2><ul>
<li>Copying multipart objects via <code>CopyObject</code> is re-enabled.</li>
<li><code>UploadPartCopy</code> is re-enabled.</li>
</ul><h2 id="2022-10-28">2022-10-28</h2><ul>
<li>Multipart upload part sizes are always expected to be of the same size, but this enforcement is now done when you complete an upload instead of being done very time you upload a part.</li>
<li>Fixed a performance issue where concurrent multipart part uploads would get rejected.</li>
</ul><h2 id="2022-10-26">2022-10-26</h2><ul>
<li>Fixed ranged reads for multipart objects with part sizes unaligned
to 64KiB.</li>
</ul><h2 id="2022-10-19">2022-10-19</h2><ul>
<li><code>HeadBucket</code> now sets <code>x-amz-bucket-region</code> to <code>auto</code> in the response.</li>
</ul><h2 id="2022-10-06">2022-10-06</h2><ul>
<li>Temporarily disabled <code>UploadPartCopy</code> while we investigate an issue.</li>
</ul><h2 id="2022-09-29">2022-09-29</h2><ul>
<li>Fixed a CORS issue where <code>Access-Control-Allow-Headers</code> was not being
set for preflight requests.</li>
</ul><h2 id="2022-09-28">2022-09-28</h2><ul>
<li>Fixed a bug where CORS configuration was not being applied to S3 endpoint.</li>
<li>No-longer render the <code>Access-Control-Expose-Headers</code> response header if <code>ExposeHeader</code> is not defined.</li>
<li>Public buckets will no-longer return the <code>Content-Range</code> response header unless the response is partial.</li>
<li>Fixed CORS rendering for the S3 <code>HeadObject</code> operation.</li>
<li>Fixed a bug where no matching CORS configuration could result in a <code>403</code> response.</li>
<li>Temporarily disable copying objects that were created with multipart uploads.</li>
<li>Fixed a bug in the Workers bindings where an internal error was being returned for malformed ranged <code>.get</code> requests.</li>
</ul><h2 id="2022-09-27">2022-09-27</h2><ul>
<li>CORS preflight responses and adding CORS headers for other responses is now implemented for S3 and public buckets. Currently, the only way to configure CORS is via the S3 API.</li>
<li>Fixup for bindings list truncation to work more correctly when listing keys with custom metadata that have <code>&quot;</code> or when some keys/values contain certain multi-byte UTF-8 values.</li>
<li>The S3 <code>GetObject</code> operation now only returns <code>Content-Range</code> in response to a ranged request.</li>
</ul><h2 id="2022-09-19">2022-09-19</h2><ul>
<li>The R2 <code>put()</code> binding options can now be given an <code>onlyIf</code> field, similar to <code>get()</code>, that performs a conditional upload.</li>
<li>The R2 <code>delete()</code> binding now supports deleting multiple keys at once.</li>
<li>The R2 <code>put()</code> binding now supports user-specified SHA-1, SHA-256, SHA-384, SHA-512 checksums in options.</li>
<li>User-specified object checksums will now be available in the R2 <code>get()</code> and <code>head()</code> bindings response. MD5 is included by default for non-multipart uploaded objects.</li>
</ul><h2 id="2022-09-06">2022-09-06</h2><ul>
<li>The S3 <code>CopyObject</code> operation now includes <code>x-amz-version-id</code> and <code>x-amz-copy-source-version-id</code> in the response headers for consistency with other methods.</li>
<li>The <code>ETag</code> for multipart files uploaded until shortly after Open Beta uploaded now include the number of parts as a suffix.</li>
</ul><h2 id="2022-08-17">2022-08-17</h2><ul>
<li>The S3 <code>DeleteObjects</code> operation no longer trims the space from around the keys before deleting. This would result in files with leading / trailing spaces not being able to be deleted. Additionally, if there was an object with the trimmed key that existed it would be deleted instead. The S3 <code>DeleteObject</code> operation was not affected by this.</li>
<li>Fixed presigned URL support for the S3 <code>ListBuckets</code> and <code>ListObjects</code> operations.</li>
</ul><h2 id="2022-08-06">2022-08-06</h2><ul>
<li>Uploads will automatically infer the <code>Content-Type</code> based on file body
if one is not explicitly set in the <code>PutObject</code> request. This functionality will
come to multipart operations in the future.</li>
</ul><h2 id="2022-07-30">2022-07-30</h2><ul>
<li>Fixed S3 conditionals to work properly when provided the <code>LastModified</code> date of the last upload, bindings fixes will come in the next release.</li>
<li><code>If-Match</code> / <code>If-None-Match</code> headers now support arrays of ETags, Weak ETags and wildcard (<code>*</code>) as per the HTTP standard and undocumented AWS S3 behavior.</li>
</ul><h2 id="2022-07-21">2022-07-21</h2><ul>
<li>Added dummy implementation of the following operation that mimics
the response that a basic AWS S3 bucket will return when first created: <code>GetBucketAcl</code>.</li>
</ul><h2 id="2022-07-20">2022-07-20</h2><ul>
<li>
<p>Added dummy implementations of the following operations that mimic the response that a basic AWS S3 bucket will return when first created:</p>
<ul>
<li><code>GetBucketVersioning</code></li>
<li><code>GetBucketLifecycleConfiguration</code></li>
<li><code>GetBucketReplication</code></li>
<li><code>GetBucketTagging</code></li>
<li><code>GetObjectLockConfiguration</code></li>
</ul>
</li>
</ul><h2 id="2022-07-19">2022-07-19</h2><ul>
<li>Fixed an S3 compatibility issue for error responses with MinIO .NET SDK and any other tooling that expects no <code>xmlns</code> namespace attribute on the top-level <code>Error</code> tag.</li>
<li>List continuation tokens prior to 2022-07-01 are no longer accepted and must be obtained again through a new <code>list</code> operation.</li>
<li>The <code>list()</code> binding will now correctly return a smaller limit if too much data would otherwise be returned (previously would return an <code>Internal Error</code>).</li>
</ul><h2 id="2022-07-14">2022-07-14</h2><ul>
<li>Improvements to 500s: we now convert errors, so things that were previously concurrency problems for some operations should now be <code>TooMuchConcurrency</code> instead of <code>InternalError</code>. We've also reduced the rate of 500s through internal improvements.</li>
<li><code>ListMultipartUpload</code> correctly encodes the returned <code>Key</code> if the <code>encoding-type</code> is specified.</li>
</ul><h2 id="2022-07-13">2022-07-13</h2><ul>
<li>S3 XML documents sent to R2 that have an XML declaration are not rejected with <code>400 Bad Request</code> / <code>MalformedXML</code>.</li>
<li>Minor S3 XML compatibility fix impacting Arq Backup on Windows only (not the Mac version). Response now contains XML declaration tag prefix and the xmlns attribute is present on all top-level tags in the response.</li>
<li>Beta <code>ListMultipartUploads</code> support.</li>
</ul><h2 id="2022-07-06">2022-07-06</h2><ul>
<li>Support the <code>r2_list_honor_include</code> compat flag coming up in an upcoming runtime release (default behavior as of 2022-07-14 compat date). Without that compat flag/date, list will continue to function implicitly as <code>include: ['httpMetadata', 'customMetadata']</code> regardless of what you specify.</li>
<li><code>cf-create-bucket-if-missing</code> can be set on a <code>PutObject</code>/<code>CreateMultipartUpload</code> request to implicitly create the bucket if it does not exist.</li>
<li>Fix S3 compatibility with MinIO client spec non-compliant XML for publishing multipart uploads. Any leading and trailing quotes in <code>CompleteMultipartUpload</code> are now optional and ignored as it seems to be the actual non-standard behavior AWS implements.</li>
</ul><h2 id="2022-07-01">2022-07-01</h2><ul>
<li>Unsupported search parameters to <code>ListObjects</code>/<code>ListObjectsV2</code> are
now rejected with <code>501 Not Implemented</code>.</li>
<li>Fixes for Listing:
<ul>
<li>Fix listing behavior when the number of files within a folder exceeds the limit (you'd end
up seeing a CommonPrefix for that large folder N times where N = number of children
within the CommonPrefix / limit).</li>
<li>Fix corner case where listing could cause
objects with sharing the base name of a &quot;folder&quot; to be skipped.</li>
<li>Fix listing over some files that shared a certain common prefix.</li>
</ul>
</li>
<li><code>DeleteObjects</code> can now handle 1000 objects at a time.</li>
<li>S3 <code>CreateBucket</code> request can specify <code>x-amz-bucket-object-lock-enabled</code> with a value of <code>false</code> and not have the requested rejected with a <code>NotImplemented</code>
error. A value of <code>true</code> will continue to be rejected as R2 does not yet support
object locks.</li>
</ul><h2 id="2022-06-17">2022-06-17</h2><ul>
<li>Fixed a regression for some clients when using an empty delimiter.</li>
<li>Added support for S3 pre-signed URLs.</li>
</ul><h2 id="2022-06-16">2022-06-16</h2><ul>
<li>Fixed a regression in the S3 API <code>UploadPart</code> operation where <code>TooMuchConcurrency</code>
&amp; <code>NoSuchUpload</code> errors were being returned as <code>NoSuchBucket</code>.</li>
</ul><h2 id="2022-06-13">2022-06-13</h2><ul>
<li>Fixed a bug with the S3 API <code>ListObjectsV2</code> operation not returning empty folder/s as common prefixes when using delimiters.</li>
<li>The S3 API <code>ListObjectsV2</code> <code>KeyCount</code> parameter now correctly returns the sum of keys and common prefixes rather than just the keys.</li>
<li>Invalid cursors for list operations no longer fail with an <code>InternalError</code> and now return the appropriate error message.</li>
</ul><h2 id="2022-06-10">2022-06-10</h2><ul>
<li>The <code>ContinuationToken</code> field is now correctly returned in the response if provided in a S3 API <code>ListObjectsV2</code> request.</li>
<li>Fixed a bug where the S3 API <code>AbortMultipartUpload</code> operation threw an error when called multiple times.</li>
</ul><h2 id="2022-05-27">2022-05-27</h2><ul>
<li>Fixed a bug where the S3 API's <code>PutObject</code> or the <code>.put()</code> binding could fail but still show the bucket upload as successful.</li>
<li>If <a href="https://datatracker.ietf.org/doc/html/rfc7232">conditional headers</a> are provided to S3 API <code>UploadObject</code> or <code>CreateMultipartUpload</code> operations, and the object exists, a <code>412 Precondition Failed</code> status code will be returned if these checks are not met.</li>
</ul><h2 id="2022-05-20">2022-05-20</h2><ul>
<li>Fixed a bug when <code>Accept-Encoding</code> was being used in <code>SignedHeaders</code>
when sending requests to the S3 API would result in a <code>SignatureDoesNotMatch</code>
response.</li>
</ul><h2 id="2022-05-17">2022-05-17</h2><ul>
<li>Fixed a bug where requests to the S3 API were not handling non-encoded parameters used for the authorization signature.</li>
<li>Fixed a bug where requests to the S3 API where number-like keys were being parsed as numbers instead of strings.</li>
</ul><h2 id="2022-05-16">2022-05-16</h2><ul>
<li>Add support for S3 <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html">virtual-hosted style paths</a>, such as <code>&lt;BUCKET&gt;.&lt;ACCOUNT_ID&gt;.r2.cloudflarestorage.com</code> instead of path-based routing (<code>&lt;ACCOUNT_ID&gt;.r2.cloudflarestorage.com/&lt;BUCKET&gt;</code>).</li>
<li>Implemented <code>GetBucketLocation</code> for compatibility with external tools, this will always return a <code>LocationConstraint</code> of <code>auto</code>.</li>
</ul><h2 id="2022-05-06">2022-05-06</h2><ul>
<li>S3 API <code>GetObject</code> ranges are now inclusive (<code>bytes=0-0</code> will correctly return the first byte).</li>
<li>S3 API <code>GetObject</code> partial reads return the proper <code>206 Partial Content</code> response code.</li>
<li>Copying from a non-existent key (or from a non-existent bucket) to another bucket now returns the proper <code>NoSuchKey</code> / <code>NoSuchBucket</code> response.</li>
<li>The S3 API now returns the proper <code>Content-Type: application/xml</code> response header on relevant endpoints.</li>
<li>Multipart uploads now have a <code>-N</code> suffix on the etag representing the number of parts the file was published with.</li>
<li><code>UploadPart</code> and <code>UploadPartCopy</code> now return proper error messages, such as <code>TooMuchConcurrency</code> or <code>NoSuchUpload</code>, instead of 'internal error'.</li>
<li><code>UploadPart</code> can now be sent a 0-length part.</li>
</ul><h2 id="2022-05-05">2022-05-05</h2><ul>
<li>When using the S3 API, an empty string and <code>us-east-1</code> will now alias to the <code>auto</code> region for compatibility with external tools.</li>
<li><code>GetBucketEncryption</code>, <code>PutBucketEncryption</code> and <code>DeleteBucketEncrypotion</code> are now supported (the only supported value currently is <code>AES256</code>).</li>
<li>Unsupported operations are explicitly rejected as unimplemented rather than implicitly converting them into <code>ListObjectsV2</code>/<code>PutBucket</code>/<code>DeleteBucket</code> respectively.</li>
<li>S3 API <code>CompleteMultipartUploads</code> requests are now properly escaped.</li>
</ul><h2 id="2022-05-03">2022-05-03</h2><ul>
<li>Pagination cursors are no longer returned when the keys in a bucket is the same as the <code>MaxKeys</code> argument.</li>
<li>The S3 API <code>ListBuckets</code> operation now accepts <code>cf-max-keys</code>, <code>cf-start-after</code> and <code>cf-continuation-token</code> headers behave the same as the respective URL parameters.</li>
<li>The S3 API <code>ListBuckets</code> and <code>ListObjects</code> endpoints now allow <code>per_page</code> to be 0.</li>
<li>The S3 API <code>CopyObject</code> source parameter now requires a leading slash.</li>
<li>The S3 API <code>CopyObject</code> operation now returns a <code>NoSuchBucket</code> error when copying to a non-existent bucket instead of an internal error.</li>
<li>Enforce the requirement for <code>auto</code> in SigV4 signing and the <code>CreateBucket</code> <code>LocationConstraint</code> parameter.</li>
<li>The S3 API <code>CreateBucket</code> operation now returns the proper <code>location</code> response header.</li>
</ul><h2 id="2022-04-14">2022-04-14</h2><ul>
<li>The S3 API now supports unchunked signed payloads.</li>
<li>Fixed <code>.put()</code> for the Workers R2 bindings.</li>
<li>Fixed a regression where key names were not properly decoded when using the S3 API.</li>
<li>Fixed a bug where deleting an object and then another object which is a prefix of the first could result in errors.</li>
<li>The S3 API <code>DeleteObjects</code> operation no longer returns an error even though an object has been deleted in some cases.</li>
<li>Fixed a bug where <code>startAfter</code> and <code>continuationToken</code> were not working in list operations.</li>
<li>The S3 API <code>ListObjects</code> operation now correctly renders <code>Prefix</code>, <code>Delimiter</code>, <code>StartAfter</code> and <code>MaxKeys</code> in the response.</li>
<li>The S3 API <code>ListObjectsV2</code> now correctly honors the <code>encoding-type</code> parameter.</li>
<li>The S3 API <code>PutObject</code> operation now works with <code>POST</code> requests for <code>s3cmd</code> compatibility.</li>
</ul><h2 id="2022-04-04">2022-04-04</h2><ul>
<li>The S3 API <code>DeleteObjects</code> request now properly returns a <code>MalformedXML</code>
error instead of <code>InternalError</code> when provided with more than 128 keys.</li>
</ul>
