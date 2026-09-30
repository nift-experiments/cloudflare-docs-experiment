<p>R2 implements some extensions on top of the basic S3 API. This page outlines these additional, available features. Some of the functionality described in this page requires setting a custom header. For examples on how to do so, refer to <a href="/r2/examples/aws/custom-header">Configure custom headers</a>.</p>
<h2 id="extended-metadata-using-unicode">Extended metadata using Unicode</h2>
<p>The <a href="/r2/api/workers/workers-api-reference/">Workers R2 API</a> supports Unicode in keys and values natively without requiring any additional encoding or decoding for the <code>customMetadata</code> field. These fields map to the <code>x-amz-meta-</code>-prefixed headers used within the R2 S3-compatible API endpoint.</p>
<p>HTTP header names and values may only contain ASCII characters, which is a small subset of the Unicode character library. To easily accommodate users, R2 adheres to <a href="https://datatracker.ietf.org/doc/html/rfc2047">RFC 2047</a> and automatically decodes all <code>x-amz-meta-*</code> header values before storage. On retrieval, any metadata values with unicode are RFC 2047-encoded before rendering the response. The length limit for metadata values is applied to the decoded Unicode value.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="metadata-variance">Metadata variance</h3>
@markup("md", "content/.markup/bodies/11539.md")
</aside>
<p>These headers map to the <code>httpMetadata</code> field in the <a href="/workers/runtime-apis/bindings/">R2 bindings</a>:</p>
<table>
<thead>
<tr>
<th>HTTP Header</th>
<th>Property Name</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Content-Encoding</code></td>
<td><code>httpMetadata.contentEncoding</code></td>
</tr>
<tr>
<td><code>Content-Type</code></td>
<td><code>httpMetadata.contentType</code></td>
</tr>
<tr>
<td><code>Content-Language</code></td>
<td><code>httpMetadata.contentLanguage</code></td>
</tr>
<tr>
<td><code>Content-Disposition</code></td>
<td><code>httpMetadata.contentDisposition</code></td>
</tr>
<tr>
<td><code>Cache-Control</code></td>
<td><code>httpMetadata.cacheControl</code></td>
</tr>
<tr>
<td><code>Expires</code></td>
<td><code>httpMetadata.expires</code></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>If using Unicode in object key names, refer to <a href="/r2/reference/unicode-interoperability/">Unicode Interoperability</a>.</p>
<h2 id="auto-creating-buckets-on-upload">Auto-creating buckets on upload</h2>
<p>If you are creating buckets on demand, you might initiate an upload with the assumption that a target bucket exists. In this situation, if you received a <code>NoSuchBucket</code> error, you would probably issue a <code>CreateBucket</code> operation. However, following this approach can cause issues: if the body has already been partially consumed, the upload will need to be aborted. A common solution to this issue, followed by other object storage providers, is to use the <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/100">HTTP <code>100</code></a> response to detect whether the body should be sent, or if the bucket must be created before retrying the upload. However, Cloudflare does not support the HTTP <code>100</code> response. Even if the HTTP <code>100</code> response was supported, you would still have additional latency due to the round trips involved.</p>
<p>To support sending an upload with a streaming body to a bucket that may not exist yet, upload operations such as <code>PutObject</code> or <code>CreateMultipartUpload</code> allow you to specify a header that will ensure the <code>NoSuchBucket</code> error is not returned. If the bucket does not exist at the time of upload, it is implicitly instantiated with the following <code>CreateBucket</code> request:</p>
<pre><code class="language-txt">PUT / HTTP/1.1&#10;Host: bucket.account.r2.cloudflarestorage.com&#10;&lt;CreateBucketConfiguration xmlns=&quot;http://s3.amazonaws.com/doc/2006-03-01/&quot;&gt;&#10;   &lt;LocationConstraint&gt;auto&lt;/LocationConstraint&gt;&#10;&lt;/CreateBucketConfiguration&gt;&#10;</code></pre>
<p>This is only useful if you are creating buckets on demand because you do not know the name of the bucket or the preferred access location ahead of time. For example, you have one bucket per one of your customers and the bucket is created on first upload to the bucket and not during account registration. In these cases, the <a href="#listbuckets"><code>ListBuckets</code> extension</a>, which supports accounts with more than 1,000 buckets, may also be useful.</p>
<h2 id="putobject-and-createmultipartupload">PutObject and CreateMultipartUpload</h2>
<h3 id="cf-create-bucket-if-missing">cf-create-bucket-if-missing</h3>
<p>Add a <code>cf-create-bucket-if-missing</code> header with the value <code>true</code> to implicitly create the bucket if it does not exist yet. Refer to <a href="#auto-creating-buckets-on-upload">Auto-creating buckets on upload</a> for a more detailed explanation of when to add this header.</p>
<h2 id="copyobject">CopyObject</h2>
<h3 id="merge-metadata-directive">MERGE metadata directive</h3>
<p>The <code>x-amz-metadata-directive</code> allows a <code>MERGE</code> value, in addition to the standard <code>COPY</code> and <code>REPLACE</code> options. When used, <code>MERGE</code> is a combination of <code>COPY</code> and <code>REPLACE</code>, which will <code>COPY</code> any metadata keys from the source object and <code>REPLACE</code> those that are specified in the request with the new value. You cannot use <code>MERGE</code> to remove existing metadata keys from the source — use <code>REPLACE</code> instead.</p>
<h2 id="listbuckets"><code>ListBuckets</code></h2>
<p><code>ListBuckets</code> supports all the same search parameters as <code>ListObjectsV2</code> in R2 because some customers may have more than 1,000 buckets. Because tooling, like existing S3 libraries, may not expose a way to set these search parameters, these values may also be sent in via headers. Values in headers take precedence over the search parameters.</p>
<table>
<thead>
<tr>
<th>Search parameter</th>
<th>HTTP Header</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>prefix</code></td>
<td><code>cf-prefix</code></td>
<td>Show buckets with this prefix only.</td>
</tr>
<tr>
<td><code>start-after</code></td>
<td><code>cf-start-after</code></td>
<td>Show buckets whose name appears lexicographically in the account.</td>
</tr>
<tr>
<td><code>continuation-token</code></td>
<td><code>cf-continuation-token</code></td>
<td>Resume listing from a previously returned continuation token.</td>
</tr>
<tr>
<td><code>max-keys</code></td>
<td><code>cf-max-keys</code></td>
<td>Return this maximum number of buckets. Default and max is <code>1000</code>.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<p>The XML response contains a <code>NextContinuationToken</code> and <code>IsTruncated</code> elements as appropriate. Since these may not be accessible from existing S3 APIs, these are also available in response headers:</p>
<table>
<thead>
<tr>
<th>XML Response Element</th>
<th>HTTP Response Header</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>IsTruncated</code></td>
<td><code>cf-is-truncated</code></td>
<td>This is set to <code>true</code> if the list of buckets returned is not all the buckets on the account.</td>
</tr>
<tr>
<td><code>NextContinuationToken</code></td>
<td><code>cf-next-continuation-token</code></td>
<td>This is set to continuation token to pass on a subsequent <code>ListBuckets</code> to resume the listing.</td>
</tr>
<tr>
<td><code>StartAfter</code></td>
<td></td>
<td>This is the start-after value that was passed in on the request.</td>
</tr>
<tr>
<td><code>KeyCount</code></td>
<td></td>
<td>The number of buckets returned.</td>
</tr>
<tr>
<td><code>ContinuationToken</code></td>
<td></td>
<td>The continuation token that was supplied in the request.</td>
</tr>
<tr>
<td><code>MaxKeys</code></td>
<td></td>
<td>The max keys that were specified in the request.</td>
</tr>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h3 id="conditional-operations-in-copyobject-for-the-destination-object">Conditional operations in <code>CopyObject</code> for the destination object</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11538.md")
</aside>
<p><code>CopyObject</code> already supports conditions that relate to the source object through the <code>x-amz-copy-source-if-...</code> headers as part of our compliance with the S3 API. In addition to this, R2 supports an R2 specific set of headers that allow the <code>CopyObject</code> operation to be conditional on the target object:</p>
<ul>
<li><code>cf-copy-destination-if-match</code></li>
<li><code>cf-copy-destination-if-none-match</code></li>
<li><code>cf-copy-destination-if-modified-since</code></li>
<li><code>cf-copy-destination-if-unmodified-since</code></li>
</ul>
<p>These headers work akin to the similarly named conditional headers supported on <code>PutObject</code>. When the preceding state of the destination object to does not match the specified conditions the <code>CopyObject</code> operation will be rejected with a <code>412 PreconditionFailed</code> error code.</p>
<h4 id="non-atomicity-relative-to-x-amz-copy-source-if">Non-atomicity relative to <code>x-amz-copy-source-if</code></h4>
<p>The <code>x-amz-copy-source-if-...</code> headers are guaranteed to be checked when the source object for the copy operation is selected, and the <code>cf-copy-destination-if-...</code> headers are guaranteed to be checked when the object is committed to the bucket state.
However, the time at which the source object is selected for copying, and the point in time when the destination object is committed to the bucket state are not necessarily the same. This means that the <code>cf-copy-destination-if-...</code> headers are not atomic in relation to the <code>x-amz-copy-source-if...</code> headers.</p>
