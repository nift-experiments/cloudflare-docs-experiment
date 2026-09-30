<p>The in-Worker R2 API is accessed by binding an R2 bucket to a <a href="/workers">Worker</a>. The Worker you write can expose external access to buckets via a route or manipulate R2 objects internally.</p>
<p>The R2 API includes some extensions and semantic differences from the S3 API. If you need S3 compatibility, consider using the <a href="/r2/api/s3/">S3-compatible API</a>.</p>
<h2 id="concepts">Concepts</h2>
<p>R2 organizes the data you store, called objects, into containers, called buckets. Buckets are the fundamental unit of performance, scaling, and access within R2.</p>
<h2 id="create-a-binding">Create a binding</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="bindings">Bindings</h3>
@markup("md", "content/.markup/bodies/11520.md")
</aside>
<p>To bind your R2 bucket to your Worker, add the following to your Wrangler file. Update the <code>binding</code> property to a valid JavaScript variable identifier and <code>bucket_name</code> to the name of your R2 bucket:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/11521.md")
</div>
<p>Within your Worker, your bucket binding is now available under the <code>MY_BUCKET</code> variable and you can begin interacting with it using the <a href="#bucket-method-definitions">bucket methods</a> described below.</p>
<h2 id="bucket-method-definitions">Bucket method definitions</h2>
<p>The following methods are available on the bucket binding object injected into your code.</p>
<p>For example, to issue a <code>PUT</code> object request using the binding above:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11524.md")
</div></div>
<ul>
<li>
<p><code>head</code> <span class="nb-type">(key: string): Promise&lt;R2Object | null&gt;</span></p>
<ul>
<li>Retrieves the <code>R2Object</code> for the given key containing only object metadata, if the key exists, and <code>null</code> if the key does not exist.</li>
</ul>
</li>
<li>
<p><code>get</code> <span class="nb-type">(key: string, options?: R2GetOptions): Promise&lt;R2ObjectBody | R2Object | null&gt;</span></p>
<ul>
<li>Retrieves the <code>R2ObjectBody</code> for the given key containing object metadata and the object body as a <code>ReadableStream</code>, if the key exists, and <code>null</code> if the key does not exist.</li>
<li>In the event that a precondition specified in <code>options</code> fails, <code>get()</code> returns an <code>R2Object</code> with <code>body</code> undefined.</li>
</ul>
</li>
<li>
<p><code>put</code> <span class="nb-type">(key: string, value: ReadableStream | ArrayBuffer | ArrayBufferView | string | null | Blob, options?: R2PutOptions): Promise&lt;R2Object | null&gt;</span></p>
<ul>
<li>Stores the given <code>value</code> and metadata under the associated <code>key</code>. Once the write succeeds, returns an <code>R2Object</code> containing metadata about the stored Object.</li>
<li>In the event that a precondition specified in <code>options</code> fails, <code>put()</code> returns <code>null</code>, and the object will not be stored.</li>
<li>R2 writes are strongly consistent. Once the Promise resolves, all subsequent read operations will see this key value pair globally.</li>
</ul>
</li>
<li>
<p><code>delete</code> <span class="nb-type">(key: string | string[]): Promise&lt;void&gt;</span></p>
<ul>
<li>Deletes the given <code>values</code> and metadata under the associated <code>keys</code>. Once the delete succeeds, returns <code>void</code>.</li>
<li>R2 deletes are strongly consistent. Once the Promise resolves, all subsequent read operations will no longer see the provided key value pairs globally.</li>
<li>Up to 1000 keys may be deleted per call.</li>
</ul>
</li>
<li>
<p><code>list</code> <span class="nb-type">(options?: R2ListOptions): Promise&lt;R2Objects&gt;</span></p>
<ul>
<li>Returns an <code>R2Objects</code> containing a list of <code>R2Object</code> contained within the bucket.</li>
<li>The returned list of objects is ordered lexicographically.</li>
<li>Returns up to 1000 entries, but may return less in order to minimize memory pressure within the Worker.</li>
<li>To explicitly set the number of objects to list, provide an <a href="/r2/api/workers/workers-api-reference/#r2listoptions">R2ListOptions</a> object with the <code>limit</code> property set.</li>
</ul>
</li>
</ul>
<ul>
<li>
<p><code>createMultipartUpload</code> <span class="nb-type">(key: string, options?: R2MultipartOptions): Promise&lt;R2MultipartUpload&gt;</span></p>
<ul>
<li>Creates a multipart upload.</li>
<li>Returns Promise which resolves to an <code>R2MultipartUpload</code> object representing the newly created multipart upload. Once the multipart upload has been created, the multipart upload can be immediately interacted with globally, either through the Workers API, or through the S3 API.</li>
</ul>
</li>
</ul>
<ul>
<li>
<p><code>resumeMultipartUpload</code> <span class="nb-type">(key: string, uploadId: string): R2MultipartUpload</span></p>
<ul>
<li>Returns an object representing a multipart upload with the given key and uploadId.</li>
<li>The resumeMultipartUpload operation does not perform any checks to ensure the validity of the uploadId, nor does it verify the existence of a corresponding active multipart upload. This is done to minimize latency before being able to call subsequent operations on the <code>R2MultipartUpload</code> object.</li>
</ul>
</li>
</ul>
<h2 id="r2object-definition"><code>R2Object</code> definition</h2>
<p><code>R2Object</code> is created when you <code>PUT</code> an object into an R2 bucket. <code>R2Object</code> represents the metadata of an object based on the information provided by the uploader. Every object that you <code>PUT</code> into an R2 bucket will have an <code>R2Object</code> created.</p>
<ul>
<li>
<p><code>key</code> <span class="nb-type">string</span></p>
<ul>
<li>The object's key.</li>
</ul>
</li>
<li>
<p><code>version</code> <span class="nb-type">string</span></p>
<ul>
<li>Random unique string associated with a specific upload of a key.</li>
</ul>
</li>
<li>
<p><code>size</code> <span class="nb-type">number</span></p>
<ul>
<li>Size of the object in bytes.</li>
</ul>
</li>
<li>
<p><code>etag</code> <span class="nb-type">string</span></p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11519.md")
</aside>
<ul>
<li>
<p>The etag associated with the object upload.</p>
</li>
<li>
<p><code>httpEtag</code> <span class="nb-type">string</span></p>
<ul>
<li>The object's etag, in quotes so as to be returned as a header.</li>
</ul>
</li>
<li>
<p><code>uploaded</code> <span class="nb-type">Date</span></p>
<ul>
<li>A Date object representing the time the object was uploaded.</li>
</ul>
</li>
<li>
<p><code>httpMetadata</code> <span class="nb-type">R2HTTPMetadata</span></p>
<ul>
<li>Various HTTP headers associated with the object. Refer to <a href="#http-metadata">HTTP Metadata</a>.</li>
</ul>
</li>
<li>
<p><code>customMetadata</code> <span class="nb-type">Record&lt;string, string&gt;</span></p>
<ul>
<li>A map of custom, user-defined metadata associated with the object.</li>
</ul>
</li>
<li>
<p><code>range</code> <span class="nb-type">R2Range</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A <code>R2Range</code> object containing the returned range of the object.</li>
</ul>
</li>
<li>
<p><code>checksums</code> <span class="nb-type">R2Checksums</span></p>
<ul>
<li>A <code>R2Checksums</code> object containing the stored checksums of the object. Refer to <a href="#checksums">checksums</a>.</li>
</ul>
</li>
<li>
<p><code>writeHttpMetadata</code> <span class="nb-type">(headers: Headers): void</span></p>
<ul>
<li>Retrieves the <code>httpMetadata</code> from the <code>R2Object</code> and applies their corresponding HTTP headers to the <code>Headers</code> input object. Refer to <a href="#http-metadata">HTTP Metadata</a>.</li>
</ul>
</li>
<li>
<p><code>storageClass</code> <span class="nb-type">Standard' | 'InfrequentAccess</span></p>
<ul>
<li>The storage class associated with the object. Refer to <a href="#storage-class">Storage Classes</a>.</li>
</ul>
</li>
<li>
<p><code>ssecKeyMd5</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Hex-encoded MD5 hash of the <a href="/r2/examples/ssec">SSE-C</a> key used for encryption (if one was provided). Hash can be used to identify which key is needed to decrypt object.</li>
</ul>
</li>
</ul>
<h2 id="r2objectbody-definition"><code>R2ObjectBody</code> definition</h2>
<p><code>R2ObjectBody</code> represents an object's metadata combined with its body. It is returned when you <code>GET</code> an object from an R2 bucket. The full list of keys for <code>R2ObjectBody</code> includes the list below and all keys inherited from <a href="#r2object-definition"><code>R2Object</code></a>.</p>
<ul>
<li>
<p><code>body</code> <span class="nb-type">ReadableStream</span></p>
<ul>
<li>The object's value.</li>
</ul>
</li>
<li>
<p><code>bodyUsed</code> <span class="nb-type">boolean</span></p>
<ul>
<li>Whether the object's value has been consumed or not.</li>
</ul>
</li>
<li>
<p><code>arrayBuffer</code> <span class="nb-type">(): Promise&lt;ArrayBuffer&gt;</span></p>
<ul>
<li>Returns a Promise that resolves to an <code>ArrayBuffer</code> containing the object's value.</li>
</ul>
</li>
<li>
<p><code>text</code> <span class="nb-type">(): Promise&lt;string&gt;</span></p>
<ul>
<li>Returns a Promise that resolves to a string containing the object's value.</li>
</ul>
</li>
<li>
<p><code>json</code> <span class="nb-type">&lt;T&gt;() : Promise&lt;T&gt;</span></p>
<ul>
<li>Returns a Promise that resolves to the given object containing the object's value.</li>
</ul>
</li>
<li>
<p><code>blob</code> <span class="nb-type">(): Promise&lt;Blob&gt;</span></p>
<ul>
<li>Returns a Promise that resolves to a binary Blob containing the object's value.</li>
</ul>
</li>
</ul>
<h2 id="r2multipartupload-definition"><code>R2MultipartUpload</code> definition</h2>
<p>An <code>R2MultipartUpload</code> object is created when you call <code>createMultipartUpload</code> or <code>resumeMultipartUpload</code>. <code>R2MultipartUpload</code> is a representation of an ongoing multipart upload.</p>
<p>Uncompleted multipart uploads will be automatically aborted after 7 days.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11518.md")
</aside>
<ul>
<li>
<p><code>key</code> <span class="nb-type">string</span></p>
<ul>
<li>The <code>key</code> for the multipart upload.</li>
</ul>
</li>
<li>
<p><code>uploadId</code> <span class="nb-type">string</span></p>
<ul>
<li>The <code>uploadId</code> for the multipart upload.</li>
</ul>
</li>
<li>
<p><code>uploadPart</code> <span class="nb-type">(partNumber: number, value: ReadableStream | ArrayBuffer | ArrayBufferView | string | Blob, options?: R2MultipartOptions): Promise&lt;R2UploadedPart&gt;</span></p>
<ul>
<li>Uploads a single part with the specified part number to this multipart upload. Each part must be uniform in size with an exception for the final part which can be smaller.</li>
<li>Returns an <code>R2UploadedPart</code> object containing the <code>etag</code> and <code>partNumber</code>. These <code>R2UploadedPart</code> objects are required when completing the multipart upload.</li>
</ul>
</li>
<li>
<p><code>abort</code> <span class="nb-type">(): Promise&lt;void&gt;</span></p>
<ul>
<li>Aborts the multipart upload. Returns a Promise that resolves when the upload has been successfully aborted.</li>
</ul>
</li>
<li>
<p><code>complete</code> <span class="nb-type">(uploadedParts: R2UploadedPart[]): Promise&lt;R2Object&gt;</span></p>
<ul>
<li>Completes the multipart upload with the given parts.</li>
<li>Returns a Promise that resolves when the complete operation has finished. Once this happens, the object is immediately accessible globally by any subsequent read operation.</li>
</ul>
</li>
</ul>
<h2 id="method-specific-types">Method-specific types</h2>
<h3 id="r2getoptions">R2GetOptions</h3>
<ul>
<li>
<p><code>onlyIf</code> <span class="nb-type">R2Conditional | Headers</span></p>
<ul>
<li>Specifies that the object should only be returned given satisfaction of certain conditions in the <code>R2Conditional</code> or in the conditional Headers. Refer to <a href="#conditional-operations">Conditional operations</a>.</li>
</ul>
</li>
<li>
<p><code>range</code> <span class="nb-type">R2Range | Headers</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Specifies that only a specific length (from an optional offset) or suffix of bytes from the object should be returned given the range in the <code>R2Range</code> or in the range <code>Headers</code>. Refer to <a href="#ranged-reads">Ranged reads</a>.</li>
</ul>
</li>
<li>
<p><code>ssecKey</code> <span class="nb-type">ArrayBuffer | string</span></p>
<ul>
<li>Specifies a key to be used for <a href="/r2/examples/ssec">SSE-C</a>. Key must be 32 bytes in length, in the form of a hex-encoded string or an ArrayBuffer.</li>
</ul>
</li>
</ul>
<h4 id="ranged-reads">Ranged reads</h4>
<p><code>R2GetOptions</code> accepts a <code>range</code> parameter, which can be used to restrict the data returned in <code>body</code>.</p>
<p>There are 3 variations of arguments that can be used in a range:</p>
<ul>
<li>
<p>An offset with an optional length.</p>
</li>
<li>
<p>An optional offset with a length.</p>
</li>
<li>
<p>A suffix.</p>
</li>
<li>
<p><code>offset</code> <span class="nb-type">number</span></p>
<ul>
<li>The byte to begin returning data from, inclusive.</li>
</ul>
</li>
<li>
<p><code>length</code> <span class="nb-type">number</span></p>
<ul>
<li>The number of bytes to return. If more bytes are requested than exist in the object, fewer bytes than this number may be returned.</li>
</ul>
</li>
<li>
<p><code>suffix</code> <span class="nb-type">number</span></p>
<ul>
<li>The number of bytes to return from the end of the file, starting from the last byte. If more bytes are requested than exist in the object, fewer bytes than this number may be returned.</li>
</ul>
</li>
</ul>
<h3 id="r2putoptions">R2PutOptions</h3>
<ul>
<li>
<p><code>onlyIf</code> <span class="nb-type">R2Conditional | Headers</span></p>
<ul>
<li>Specifies that the object should only be stored given satisfaction of certain conditions in the <code>R2Conditional</code>. Refer to <a href="#conditional-operations">Conditional operations</a>.</li>
</ul>
</li>
<li>
<p><code>httpMetadata</code> <span class="nb-type">R2HTTPMetadata | Headers</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Various HTTP headers associated with the object. Refer to <a href="#http-metadata">HTTP Metadata</a>.</li>
</ul>
</li>
<li>
<p><code>customMetadata</code> <span class="nb-type">Record&lt;string, string&gt;</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A map of custom, user-defined metadata that will be stored with the object.</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11517.md")
</aside>
<ul>
<li>
<p><code>md5</code> <span class="nb-type">ArrayBuffer | string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A md5 hash to use to check the received object's integrity.</li>
</ul>
</li>
<li>
<p><code>sha1</code> <span class="nb-type">ArrayBuffer | string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A SHA-1 hash to use to check the received object's integrity.</li>
</ul>
</li>
<li>
<p><code>sha256</code> <span class="nb-type">ArrayBuffer | string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A SHA-256 hash to use to check the received object's integrity.</li>
</ul>
</li>
<li>
<p><code>sha384</code> <span class="nb-type">ArrayBuffer | string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A SHA-384 hash to use to check the received object's integrity.</li>
</ul>
</li>
<li>
<p><code>sha512</code> <span class="nb-type">ArrayBuffer | string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A SHA-512 hash to use to check the received object's integrity.</li>
</ul>
</li>
<li>
<p><code>storageClass</code> <span class="nb-type">Standard' | 'InfrequentAccess</span></p>
<ul>
<li>Sets the storage class of the object if provided. Otherwise, the object will be stored in the default storage class associated with the bucket. Refer to <a href="#storage-class">Storage Classes</a>.</li>
</ul>
</li>
<li>
<p><code>ssecKey</code> <span class="nb-type">ArrayBuffer | string</span></p>
<ul>
<li>Specifies a key to be used for <a href="/r2/examples/ssec">SSE-C</a>. Key must be 32 bytes in length, in the form of a hex-encoded string or an ArrayBuffer.</li>
</ul>
</li>
</ul>
<h3 id="r2multipartoptions">R2MultipartOptions</h3>
<ul>
<li>
<p><code>httpMetadata</code> <span class="nb-type">R2HTTPMetadata | Headers</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Various HTTP headers associated with the object. Refer to <a href="#http-metadata">HTTP Metadata</a>.</li>
</ul>
</li>
<li>
<p><code>customMetadata</code> <span class="nb-type">Record&lt;string, string&gt;</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A map of custom, user-defined metadata that will be stored with the object.</li>
</ul>
</li>
<li>
<p><code>storageClass</code> <span class="nb-type">string</span></p>
<ul>
<li>Sets the storage class of the object if provided. Otherwise, the object will be stored in the default storage class associated with the bucket. Refer to <a href="#storage-class">Storage Classes</a>.</li>
</ul>
</li>
<li>
<p><code>ssecKey</code> <span class="nb-type">ArrayBuffer | string</span></p>
<ul>
<li>Specifies a key to be used for <a href="/r2/examples/ssec">SSE-C</a>. Key must be 32 bytes in length, in the form of a hex-encoded string or an ArrayBuffer.</li>
</ul>
</li>
</ul>
<h3 id="r2listoptions">R2ListOptions</h3>
<ul>
<li>
<p><code>limit</code> <span class="nb-type">number</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>
<p>The number of results to return. Defaults to <code>1000</code>, with a maximum of <code>1000</code>.</p>
</li>
<li>
<p>If <code>include</code> is set, you may receive fewer than <code>limit</code> results in your response to accommodate metadata.</p>
</li>
</ul>
</li>
<li>
<p><code>prefix</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The prefix to match keys against. Keys will only be returned if they start with given prefix.</li>
</ul>
</li>
<li>
<p><code>cursor</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>An opaque token that indicates where to continue listing objects from. A cursor can be retrieved from a previous list operation.</li>
</ul>
</li>
<li>
<p><code>delimiter</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The character to use when grouping keys.</li>
</ul>
</li>
<li>
<p><code>include</code> <span class="nb-type">Array&lt;string&gt;</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>
<p>Can include <code>httpMetadata</code> and/or <code>customMetadata</code>. If included, items returned by the list will include the specified metadata.</p>
</li>
<li>
<p>Note that there is a limit on the total amount of data that a single <code>list</code> operation can return. If you request data, you may receive fewer than <code>limit</code> results in your response to accommodate metadata.</p>
</li>
<li>
<p>The <a href="/workers/configuration/compatibility-dates/">compatibility date</a> must be set to <code>2022-08-04</code> or later in your Wrangler file. If not, then the <code>r2_list_honor_include</code> compatibility flag must be set. Otherwise it is treated as <code>include: ['httpMetadata', 'customMetadata']</code> regardless of what the <code>include</code> option provided actually is.</p>
</li>
</ul>
<p>This means applications must be careful to avoid comparing the amount of returned objects against your <code>limit</code>. Instead, use the <code>truncated</code> property to determine if the <code>list</code> request has more data to be returned.</p>
</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11527.md")
</div></div>
<h3 id="r2objects">R2Objects</h3>
<p>An object containing an <code>R2Object</code> array, returned by <code>BUCKET_BINDING.list()</code>.</p>
<ul>
<li>
<p><code>objects</code> <span class="nb-type">Array&lt;R2Object&gt;</span></p>
<ul>
<li>An array of objects matching the <code>list</code> request.</li>
</ul>
</li>
<li>
<p><code>truncated</code> boolean</p>
<ul>
<li>If true, indicates there are more results to be retrieved for the current <code>list</code> request.</li>
</ul>
</li>
<li>
<p><code>cursor</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>A token that can be passed to future <code>list</code> calls to resume listing from that point. Only present if truncated is true.</li>
</ul>
</li>
<li>
<p><code>delimitedPrefixes</code> <span class="nb-type">Array&lt;string&gt;</span></p>
<ul>
<li>
<p>If a delimiter has been specified, contains all prefixes between the specified prefix and the next occurrence of the delimiter.</p>
</li>
<li>
<p>For example, if no prefix is provided and the delimiter is '/', <code>foo/bar/baz</code> would return <code>foo</code> as a delimited prefix. If <code>foo/</code> was passed as a prefix with the same structure and delimiter, <code>foo/bar</code> would be returned as a delimited prefix.</p>
</li>
</ul>
</li>
</ul>
<h3 id="conditional-operations">Conditional operations</h3>
<p>You can pass an <code>R2Conditional</code> object to <code>R2GetOptions</code> and <code>R2PutOptions</code>. If the condition check for <code>get()</code> fails, the body will not be returned. This will make <code>get()</code> have lower latency.</p>
<p>If the condition check for <code>put()</code> fails, <code>null</code> will be returned instead of the <code>R2Object</code>.</p>
<ul>
<li>
<p><code>etagMatches</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Performs the operation if the object's etag matches the given string.</li>
</ul>
</li>
<li>
<p><code>etagDoesNotMatch</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Performs the operation if the object's etag does not match the given string.</li>
</ul>
</li>
<li>
<p><code>uploadedBefore</code> <span class="nb-type">Date</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Performs the operation if the object was uploaded before the given date.</li>
</ul>
</li>
<li>
<p><code>uploadedAfter</code> <span class="nb-type">Date</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>Performs the operation if the object was uploaded after the given date.</li>
</ul>
</li>
</ul>
<p>Alternatively, you can pass a <code>Headers</code> object containing conditional headers to <code>R2GetOptions</code> and <code>R2PutOptions</code>. For information on these conditional headers, refer to <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Conditional_requests#conditional_headers">the MDN docs on conditional requests</a>. All conditional headers aside from <code>If-Range</code> are supported.</p>
<p>For more specific information about conditional requests, refer to <a href="https://datatracker.ietf.org/doc/html/rfc7232">RFC 7232</a>.</p>
<h3 id="http-metadata">HTTP Metadata</h3>
<p>Generally, these fields match the HTTP metadata passed when the object was created. They can be overridden when issuing <code>GET</code> requests, in which case, the given values will be echoed back in the response.</p>
<ul>
<li>
<p><code>contentType</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
</li>
<li>
<p><code>contentLanguage</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
</li>
<li>
<p><code>contentDisposition</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
</li>
<li>
<p><code>contentEncoding</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
</li>
<li>
<p><code>cacheControl</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
</li>
<li>
<p><code>cacheExpiry</code> <span class="nb-type">Date</span> <span class="nb-metainfo">optional</span></p>
</li>
</ul>
<h3 id="checksums">Checksums</h3>
<p>If a checksum was provided when using the <code>put()</code> binding, it will be available on the returned object under the <code>checksums</code> property. The MD5 checksum will be included by default for non-multipart objects.</p>
<ul>
<li>
<p><code>md5</code> <span class="nb-type">ArrayBuffer</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The MD5 checksum of the object.</li>
</ul>
</li>
<li>
<p><code>sha1</code> <span class="nb-type">ArrayBuffer</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The SHA-1 checksum of the object.</li>
</ul>
</li>
<li>
<p><code>sha256</code> <span class="nb-type">ArrayBuffer</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The SHA-256 checksum of the object.</li>
</ul>
</li>
<li>
<p><code>sha384</code> <span class="nb-type">ArrayBuffer</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The SHA-384 checksum of the object.</li>
</ul>
</li>
<li>
<p><code>sha512</code> <span class="nb-type">ArrayBuffer</span> <span class="nb-metainfo">optional</span></p>
<ul>
<li>The SHA-512 checksum of the object.</li>
</ul>
</li>
</ul>
<h3 id="r2uploadedpart"><code>R2UploadedPart</code></h3>
<p>An <code>R2UploadedPart</code> object represents a part that has been uploaded. <code>R2UploadedPart</code> objects are returned from <code>uploadPart</code> operations and must be passed to <code>completeMultipartUpload</code> operations.</p>
<ul>
<li>
<p><code>partNumber</code> <span class="nb-type">number</span></p>
<ul>
<li>The number of the part.</li>
</ul>
</li>
<li>
<p><code>etag</code> <span class="nb-type">string</span></p>
<ul>
<li>The <code>etag</code> of the part.</li>
</ul>
</li>
</ul>
<h3 id="storage-class">Storage Class</h3>
<p>The storage class where an <code>R2Object</code> is stored. The available storage classes are <code>Standard</code> and <code>InfrequentAccess</code>. Refer to <a href="/r2/buckets/storage-classes/">Storage classes</a>
for more information.</p>
