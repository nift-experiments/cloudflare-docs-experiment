---
cp9:
  canonical: https://developers.cloudflare.com/r2/api/error-codes/
  description: Reference of R2 error codes returned by the Workers API and S3-compatible API.
  full_title: Error codes · Cloudflare R2 docs
  head_html: <title>Error codes · Cloudflare R2 docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference of R2 error codes returned by the Workers API and S3-compatible API."><link rel="canonical" href="https://developers.cloudflare.com/r2/api/error-codes/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/r2/api/error-codes/index.md"><meta property="og:title" content="Error codes · Cloudflare R2 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference of R2 error codes returned by the Workers API and S3-compatible API."><meta property="og:url" content="https://developers.cloudflare.com/r2/api/error-codes/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="R2"><meta name="algolia_product_filter" content="R2"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="R2"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/r2/api/error-codes/#page","headline":"Error codes \u00b7 Cloudflare R2 docs","description":"Reference of R2 error codes returned by the Workers API and S3-compatible API.","url":"https://developers.cloudflare.com/r2/api/error-codes/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /r2/api/error-codes/
  schema: 1
---
<p>This page documents error codes returned by R2 when using the <a href="/r2/api/workers/">Workers API</a> or the <a href="/r2/api/s3/">S3-compatible API</a>, along with recommended fixes to help with troubleshooting.</p>
<h2 id="how-errors-are-returned">How errors are returned</h2>
<p>For the <strong>Workers API</strong>, R2 operations throw exceptions that you can catch. The error code is included at the end of the <code>message</code> property:</p>
<pre tabindex="0"><code class="language-js">try {&#10;  await env.MY_BUCKET.put(&quot;my-key&quot;, data, { customMetadata: largeMetadata });&#10;} catch (error) {&#10;  console.error(error.message);&#10;  // &quot;put: Your metadata headers exceed the maximum allowed metadata size. (10012)&quot;&#10;}&#10;</code></pre>
<p>For the <strong>S3-compatible API</strong>, errors are returned as XML in the response body:</p>
<pre tabindex="0"><code class="language-xml">&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;&#10;&lt;Error&gt;&#10;  &lt;Code&gt;NoSuchKey&lt;/Code&gt;&#10;  &lt;Message&gt;The specified key does not exist.&lt;/Message&gt;&#10;&lt;/Error&gt;&#10;</code></pre>
<h2 id="error-code-reference">Error code reference</h2>
<h3 id="authentication-and-authorization-errors">Authentication and authorization errors</h3>
<table>
<thead>
<tr>
<th>Error Code</th>
<th>S3 Code</th>
<th>HTTP Status</th>
<th>Details</th>
<th>Recommended Fix</th>
</tr>
</thead>
<tbody>
<tr>
<td>10002</td>
<td>Unauthorized</td>
<td>401</td>
<td>Missing or invalid authentication credentials.</td>
<td>Verify your <a href="/r2/api/tokens/">API token</a> or access key credentials are correct and have not expired.</td>
</tr>
<tr>
<td>10003</td>
<td>AccessDenied</td>
<td>403</td>
<td>Insufficient permissions for the requested operation.</td>
<td>Check that your <a href="/r2/api/tokens/">API token</a> has the required permissions for the bucket and operation.</td>
</tr>
<tr>
<td>10018</td>
<td>ExpiredRequest</td>
<td>403</td>
<td>Presigned URL or request signature has expired.</td>
<td>Regenerate the <a href="/r2/api/s3/presigned-urls/">presigned URL</a> or signature.</td>
</tr>
<tr>
<td>10035</td>
<td>SignatureDoesNotMatch</td>
<td>403</td>
<td>Request signature does not match calculated signature.</td>
<td>Verify your secret key and signing algorithm. Check for URL encoding issues.</td>
</tr>
<tr>
<td>10042</td>
<td>NotEntitled</td>
<td>403</td>
<td>Account not entitled to this feature.</td>
<td>Ensure your account has an <a href="/r2/pricing/">R2 subscription</a>.</td>
</tr>
</tbody>
</table>
<h3 id="bucket-errors">Bucket errors</h3>
<table>
<thead>
<tr>
<th>Error Code</th>
<th>S3 Code</th>
<th>HTTP Status</th>
<th>Details</th>
<th>Recommended Fix</th>
</tr>
</thead>
<tbody>
<tr>
<td>10005</td>
<td>InvalidBucketName</td>
<td>400</td>
<td>Bucket name does not meet naming requirements.</td>
<td>Bucket names must be 3-63 chars, lowercase alphanumeric and hyphens, start/end with alphanumeric.</td>
</tr>
<tr>
<td>10006</td>
<td>NoSuchBucket</td>
<td>404</td>
<td>The specified bucket does not exist.</td>
<td>Verify the bucket name is correct and the bucket exists in your account.</td>
</tr>
<tr>
<td>10008</td>
<td>BucketNotEmpty</td>
<td>409</td>
<td>Cannot delete bucket that contains objects.</td>
<td>Delete all objects in the bucket before deleting the bucket.</td>
</tr>
<tr>
<td>10009</td>
<td>TooManyBuckets</td>
<td>400</td>
<td>Account bucket limit exceeded (default: 1,000,000 buckets).</td>
<td>Request a limit increase via the <a href="https://forms.gle/eX6pXvit1wBv77Yw5">Limits Increase Request Form</a>.</td>
</tr>
<tr>
<td>10073</td>
<td>BucketConflict</td>
<td>409</td>
<td>Bucket name already exists.</td>
<td>Choose a different bucket name. Bucket names must be unique within your account.</td>
</tr>
</tbody>
</table>
<h3 id="object-errors">Object errors</h3>
<table>
<thead>
<tr>
<th>Error Code</th>
<th>S3 Code</th>
<th>HTTP Status</th>
<th>Details</th>
<th>Recommended Fix</th>
</tr>
</thead>
<tbody>
<tr>
<td>10007</td>
<td>NoSuchKey</td>
<td>404</td>
<td>The specified object key does not exist. For the <a href="/r2/api/workers/workers-api-reference/">Workers API</a>, <code>get()</code> and <code>head()</code> return <code>null</code> instead of throwing.</td>
<td>Verify the object key is correct and the object has not been deleted.</td>
</tr>
<tr>
<td>10020</td>
<td>InvalidObjectName</td>
<td>400</td>
<td>Object key contains invalid characters or is too long.</td>
<td>Use valid UTF-8 characters. Maximum key length is 1024 bytes.</td>
</tr>
<tr>
<td>100100</td>
<td>EntityTooLarge</td>
<td>400</td>
<td>Object exceeds maximum size (5 GiB for single upload, 5 TiB for multipart).</td>
<td>Use <a href="/r2/objects/upload-objects/#multipart-upload">multipart upload</a> for objects larger than 5 GiB. Maximum object size is 5 TiB.</td>
</tr>
<tr>
<td>10012</td>
<td>MetadataTooLarge</td>
<td>400</td>
<td>Custom metadata exceeds the 8,192 byte limit.</td>
<td>Reduce custom metadata size. Maximum is 8,192 bytes total for all custom metadata.</td>
</tr>
<tr>
<td>10069</td>
<td>ObjectLockedByBucketPolicy</td>
<td>403</td>
<td>Object is protected by a bucket lock rule and cannot be modified or deleted.</td>
<td>Wait for the retention period to expire. Refer to <a href="/r2/buckets/bucket-locks/">bucket locks</a>.</td>
</tr>
</tbody>
</table>
<h3 id="upload-and-request-errors">Upload and request errors</h3>
<table>
<thead>
<tr>
<th>Error Code</th>
<th>S3 Code</th>
<th>HTTP Status</th>
<th>Details</th>
<th>Recommended Fix</th>
</tr>
</thead>
<tbody>
<tr>
<td>10033</td>
<td>MissingContentLength</td>
<td>411</td>
<td><code>Content-Length</code> header required but missing.</td>
<td>Include the <code>Content-Length</code> header in PUT/POST requests.</td>
</tr>
<tr>
<td>10013</td>
<td>IncompleteBody</td>
<td>400</td>
<td>Request body terminated before expected <code>Content-Length</code>.</td>
<td>Ensure the full request body is sent. Check for network interruptions or client timeouts.</td>
</tr>
<tr>
<td>10014</td>
<td>InvalidDigest</td>
<td>400</td>
<td>Checksum header format is malformed.</td>
<td>Ensure checksums are properly encoded (base64 for SHA/CRC checksums).</td>
</tr>
<tr>
<td>10037</td>
<td>BadDigest</td>
<td>400</td>
<td>Provided checksum does not match the uploaded content.</td>
<td>Verify data integrity and retry the upload.</td>
</tr>
<tr>
<td>10039</td>
<td>InvalidRange</td>
<td>416</td>
<td>Requested byte range is not satisfiable.</td>
<td>Ensure the range start is less than object size. Check <code>Range</code> header format.</td>
</tr>
<tr>
<td>10031</td>
<td>PreconditionFailed</td>
<td>412</td>
<td>Conditional headers (<code>If-Match</code>, <code>If-Unmodified-Since</code>, etc.) were not satisfied.</td>
<td>Object's ETag or modification time does not match your condition. Refetch and retry. Refer to <a href="/r2/api/s3/extensions/#conditional-operations-in-putobject">conditional operations</a>.</td>
</tr>
</tbody>
</table>
<h3 id="multipart-upload-errors">Multipart upload errors</h3>
<table>
<thead>
<tr>
<th>Error Code</th>
<th>S3 Code</th>
<th>HTTP Status</th>
<th>Details</th>
<th>Recommended Fix</th>
</tr>
</thead>
<tbody>
<tr>
<td>10011</td>
<td>EntityTooSmall</td>
<td>400</td>
<td>Multipart part is below minimum size (5 MiB), except for the last part.</td>
<td>Ensure each part (except the last) is at least 5 MiB.</td>
</tr>
<tr>
<td>10024</td>
<td>NoSuchUpload</td>
<td>404</td>
<td>Multipart upload does not exist or was aborted.</td>
<td>Verify the <code>uploadId</code> is correct. By default, incomplete multipart uploads expire after 7 days. Refer to <a href="/r2/buckets/object-lifecycles/">object lifecycles</a>.</td>
</tr>
<tr>
<td>10025</td>
<td>InvalidPart</td>
<td>400</td>
<td>One or more parts could not be found when completing the upload.</td>
<td>Verify each part was uploaded successfully and use the exact ETag returned from <code>UploadPart</code>.</td>
</tr>
<tr>
<td>10048</td>
<td>InvalidPart</td>
<td>400</td>
<td>All non-trailing parts must have the same size.</td>
<td>Ensure all parts except the last have identical sizes. R2 requires uniform part sizes for multipart uploads.</td>
</tr>
</tbody>
</table>
<h3 id="service-errors">Service errors</h3>
<table>
<thead>
<tr>
<th>Error Code</th>
<th>S3 Code</th>
<th>HTTP Status</th>
<th>Details</th>
<th>Recommended Fix</th>
</tr>
</thead>
<tbody>
<tr>
<td>10001</td>
<td>InternalError</td>
<td>500</td>
<td>An internal error occurred.</td>
<td>Retry the request. If persistent, check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a> or contact support.</td>
</tr>
<tr>
<td>10043</td>
<td>ServiceUnavailable</td>
<td>503</td>
<td>Service is temporarily unavailable.</td>
<td>Retry with exponential backoff. Check <a href="https://www.cloudflarestatus.com">Cloudflare Status</a>.</td>
</tr>
<tr>
<td>10054</td>
<td>ClientDisconnect</td>
<td>400</td>
<td>Client disconnected before request completed.</td>
<td>Check network connectivity and retry.</td>
</tr>
<tr>
<td>10058</td>
<td>TooManyRequests</td>
<td>429</td>
<td>Rate limit exceeded. Often caused by multiple concurrent requests to the same object key (limit: 1 write/second per key).</td>
<td>Check if multiple clients are accessing the same object key. See <a href="/r2/platform/limits/">R2 limits</a>.</td>
</tr>
</tbody>
</table>
