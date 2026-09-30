<p>There are several ways to upload objects to R2. Which approach you choose depends on the size of your objects and your performance requirements.</p>
<h2 id="choose-an-upload-method">Choose an upload method</h2>
<table>
<thead>
<tr>
<th></th>
<th>Single upload (<code>PUT</code>)</th>
<th>Multipart upload</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Best for</strong></td>
<td>Small to medium files (under ~100 MB)</td>
<td>Large files, or when you need parallelism and resumability</td>
</tr>
<tr>
<td><strong>Maximum object size</strong></td>
<td>5 GiB</td>
<td>5 TiB (up to 10,000 parts)</td>
</tr>
<tr>
<td><strong>Part size</strong></td>
<td>N/A</td>
<td>5 MiB – 5 GiB per part</td>
</tr>
<tr>
<td><strong>Resumable</strong></td>
<td>No — must restart the entire upload</td>
<td>Yes — only failed parts need to be retried</td>
</tr>
<tr>
<td><strong>Parallel upload</strong></td>
<td>No</td>
<td>Yes — parts can be uploaded concurrently</td>
</tr>
<tr>
<td><strong>When to use</strong></td>
<td>Quick, simple uploads of small objects</td>
<td>Video, backups, datasets, or any file where reliability matters</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11379.md")
</aside>
<h2 id="upload-via-dashboard">Upload via dashboard</h2>
<p>To upload objects to your bucket from the Cloudflare dashboard:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/11380.md")
</div>
<p>You will receive a confirmation message after a successful upload.</p>
<h3 id="create-a-folder">Create a folder</h3>
<p>You can also create folders from the dashboard by selecting <strong>Create folder</strong>. This creates a zero-byte object with a key ending in <code>/</code> that acts as a placeholder. For more information on how folders work in R2, refer to <a href="/r2/objects/#prefixes-and-folders">Prefixes and folders</a>.</p>
<h2 id="upload-via-workers-api">Upload via Workers API</h2>
<p>Use R2 <a href="/workers/runtime-apis/bindings/">bindings</a> in Workers to upload objects server-side. Refer to <a href="/r2/api/workers/workers-api-usage/">Use R2 from Workers</a> for instructions on setting up an R2 binding.</p>
<h3 id="single-upload">Single upload</h3>
<p>Use <code>put()</code> to upload an object in a single request. This is the simplest approach for small to medium objects.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/11381.md")
</div>
<h3 id="multipart-upload">Multipart upload</h3>
<p>Use <code>createMultipartUpload()</code> and <code>resumeMultipartUpload()</code> for large files or when you need to upload parts in parallel. Each part must be at least 5 MiB (except the last part).</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/11382.md")
</div>
<p>In most cases, the multipart state (the <code>uploadId</code> and uploaded part ETags) is tracked by the client sending requests to your Worker. The following example exposes an HTTP API that a client application can call to create, upload parts for, and complete a multipart upload:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/11383.md")
</div>
<p>For the complete Workers API reference, refer to <a href="/r2/api/workers/workers-api-reference/">Workers API reference</a>.</p>
<h3 id="presigned-urls-workers">Presigned URLs (Workers)</h3>
<p>When you need clients (browsers, mobile apps) to upload directly to R2 without proxying through your Worker, generate a presigned URL server-side and hand it to the client:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/11384.md")
</div>
<p>For full presigned URL documentation including GET, PUT, and security best practices, refer to <a href="/r2/api/s3/presigned-urls/">Presigned URLs</a>.</p>
<h2 id="upload-via-s3-api">Upload via S3 API</h2>
<p>Use S3-compatible SDKs to upload objects. You will need your <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a> and <a href="/r2/api/tokens/">R2 API token</a>.</p>
<h3 id="single-upload-1">Single upload</h3>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11388.md")
</div></div>
<h3 id="multipart-upload-1">Multipart upload</h3>
<p>Most S3 SDKs handle multipart uploads automatically when the file exceeds a configurable threshold. The examples below show both automatic (high-level) and manual (low-level) approaches.</p>
<h4 id="automatic-multipart-upload">Automatic multipart upload</h4>
<p>The SDK splits the file and uploads parts in parallel.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11392.md")
</div></div>
<h4 id="manual-multipart-upload">Manual multipart upload</h4>
<p>Use the low-level API when you need full control over part sizes or upload order.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11396.md")
</div></div>
<h3 id="presigned-urls-s3-api">Presigned URLs (S3 API)</h3>
<p>For client-side uploads where users upload directly to R2 without going through your server, generate a presigned PUT URL. Your server creates the URL and the client uploads to it — no API credentials are exposed to the client.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11400.md")
</div></div>
<p>For full presigned URL documentation, refer to <a href="/r2/api/s3/presigned-urls/">Presigned URLs</a>.</p>
<p>Refer to R2's <a href="/r2/api/s3/api/">S3 API documentation</a> for all supported S3 API methods.</p>
<h2 id="upload-via-cli">Upload via CLI</h2>
<h3 id="rclone">Rclone</h3>
<p><a href="https://rclone.org/">Rclone</a> is a command-line tool for managing files on cloud storage. Rclone works well for uploading multiple files from your local machine or copying data from other cloud storage providers.</p>
<p>To use rclone, install it onto your machine using their official documentation - <a href="https://rclone.org/install/">Install rclone</a>.</p>
<p>Upload files with the <code>rclone copy</code> command:</p>
<pre><code class="language-sh">&#35; Upload a single file&#10;rclone copy /path/to/local/image.png r2:bucket_name&#10;&#10;&#35; Upload everything in a directory&#10;rclone copy /path/to/local/folder r2:bucket_name&#10;</code></pre>
<p>Verify the upload with <code>rclone ls</code>:</p>
<pre><code class="language-sh">rclone ls r2:bucket_name&#10;</code></pre>
<p>For more information, refer to our <a href="/r2/examples/rclone/">rclone example</a>.</p>
<h3 id="wrangler">Wrangler</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11378.md")
</aside>
<p>Use <a href="/workers/wrangler/install-and-update/">Wrangler</a> to upload objects. Run the <a href="/workers/wrangler/commands/r2/#r2-object-put"><code>r2 object put</code> command</a>:</p>
<pre><code class="language-sh">wrangler r2 object put test-bucket/image.png --file=image.png&#10;</code></pre>
<p>You can set the <code>Content-Type</code> (MIME type), <code>Content-Disposition</code>, <code>Cache-Control</code> and other HTTP header metadata through optional flags.</p>
<h2 id="multipart-upload-details">Multipart upload details</h2>
<h3 id="part-size-limits">Part size limits</h3>
<ul>
<li>Minimum part size: 5 MiB (except for the last part)</li>
<li>Maximum part size: 5 GiB</li>
<li>Maximum number of parts: 10,000</li>
<li>All parts except the last must be the same size</li>
</ul>
<h3 id="incomplete-upload-lifecycles">Incomplete upload lifecycles</h3>
<p>Incomplete multipart uploads are automatically aborted after 7 days by default. You can change this by <a href="/r2/buckets/object-lifecycles/">configuring a custom lifecycle policy</a>.</p>
<h3 id="etags">ETags</h3>
<p>ETags for objects uploaded via multipart differ from those uploaded with a single <code>PUT</code>. The ETag of each part is the MD5 hash of that part's contents. The ETag of the completed multipart object is the hash of the concatenated binary MD5 sums of all parts, followed by a hyphen and the number of parts.</p>
<p>For example, if a two-part upload has part ETags <code>bce6bf66aeb76c7040fdd5f4eccb78e6</code> and <code>8165449fc15bbf43d3b674595cbcc406</code>, the completed object's ETag will be <code>f77dc0eecdebcd774a2a22cb393ad2ff-2</code>.</p>
<h2 id="related-resources">Related resources</h2>
<p><a class="nb-card nb-link-card" href="/r2/api/workers/workers-api-reference/"><h3 id="card-workers-api-reference-r2-api-workers-workers-api-reference">Workers API reference</h3><p>Full reference for the R2 Workers API including put(), createMultipartUpload(), and more.</p></a></p>
<p><a class="nb-card nb-link-card" href="/r2/api/s3/api/"><h3 id="card-s3-api-compatibility-r2-api-s3-api">S3 API compatibility</h3><p>Supported S3 API operations and R2-specific behavior.</p></a></p>
<p><a class="nb-card nb-link-card" href="/r2/api/s3/presigned-urls/"><h3 id="card-presigned-urls-r2-api-s3-presigned-urls">Presigned URLs</h3><p>Generate temporary upload and download URLs for client-side access.</p></a></p>
<p><a class="nb-card nb-link-card" href="/r2/buckets/object-lifecycles/"><h3 id="card-object-lifecycles-r2-buckets-object-lifecycles">Object lifecycles</h3><p>Configure automatic cleanup of incomplete multipart uploads.</p></a></p>
