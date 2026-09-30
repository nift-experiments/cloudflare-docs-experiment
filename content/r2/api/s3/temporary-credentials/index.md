<p>Temporary credentials are short-lived, scoped S3 credentials derived from an existing <a href="/r2/api/tokens/">R2 API token</a>. They authenticate with AWS Signature Version 4, the same as a long-lived token, but include a session token and expire automatically. The session token is sent with every request via the <code>X-Amz-Security-Token</code> header; all S3-compatible clients expose this as a standard session token credential field.</p>
<p>Use temporary credentials to delegate access without issuing a long-lived token. For example, granting a mobile client read access to a single prefix for 15 minutes, or issuing per-request upload credentials scoped to one object.</p>
<h2 id="choosing-an-approach">Choosing an approach</h2>
<p>R2 supports two patterns for time-limited access. They overlap but have different trade-offs:</p>
<table>
<thead>
<tr>
<th>Pattern</th>
<th>Grants</th>
<th>Good for</th>
</tr>
</thead>
<tbody>
<tr>
<td>Temporary credentials (this page)</td>
<td>Multiple S3 operations, scoped to a bucket and a set of permitted operations, and optionally to specific paths</td>
<td>Callers that use a standard S3 client or SDK to perform multiple operations in a scoped session</td>
</tr>
<tr>
<td><a href="/r2/api/s3/presigned-urls/">Presigned URLs</a></td>
<td>A single S3 operation on a single object</td>
<td>Granting direct HTTP access to a single object without an S3 client, such as a browser upload or a shareable download link</td>
</tr>
</tbody>
</table>
<h2 id="generate-temporary-credentials">Generate temporary credentials</h2>
<h3 id="via-the-temporary-credentials-api">Via the Temporary Credentials API</h3>
<p>The <a href="/api/resources/r2/subresources/temporary_credentials/methods/create/">Temporary Credentials API</a> accepts a parent API token, the bucket name, and optional scoping parameters, and returns a new access key ID, secret access key, and session token. Cloudflare signs the session token on your behalf.</p>
<p>Use this method when you want Cloudflare to manage the signing flow for you.</p>
<p>For a runnable walkthrough, refer to <a href="/r2/examples/authenticate-r2-temp-credentials/">Authenticate against R2 with temporary credentials</a>.</p>
<h3 id="locally-client-side-signing">Locally (client-side signing)</h3>
<p>You can also generate temporary credentials locally by signing a JWT with your parent API token's secret access key and using it as the session token.</p>
<p>Use this method when:</p>
<ul>
<li>You are issuing many short-lived credentials and want to avoid per-mint API latency.</li>
<li>You need to mint credentials in an environment that cannot reach the Cloudflare API.</li>
<li>You want to scope credentials by S3 action (see <a href="#actions">Scope by action</a>), which is currently supported via local signing only.</li>
</ul>
<p>Signing happens in three steps:</p>
<ol>
<li>Build a JWT payload that identifies the bucket and the scope of access.</li>
<li>Sign the JWT with HS256 using your parent secret access key.</li>
<li>Derive the temporary secret access key by taking the SHA-256 hex digest of the signed JWT. Encode the session token as <code>base64(&quot;jwt/&quot; + &lt;signed-jwt&gt;)</code>.</li>
</ol>
<p>The parent access key ID is reused as the temporary access key ID.</p>
<p>A complete, runnable example is available in <a href="/r2/examples/authenticate-r2-temp-credentials/">Authenticate against R2 with temporary credentials</a>.</p>
<h2 id="scope-of-a-credential">Scope of a credential</h2>
<p>Every temporary credential is bound to a single bucket and a set of permitted operations. You can optionally restrict the credential further to specific paths within the bucket.</p>
<p>A temporary credential cannot exceed the permissions of its parent token.</p>
<h3 id="bucket">Bucket</h3>
<p>A temporary credential is bound to exactly one bucket, identified by name. Cross-bucket access is not supported within a single credential.</p>
<h3 id="permitted-operations">Permitted operations</h3>
<p>Specify permitted operations using <code>scope</code> (passed as <code>permission</code> to the API) or <code>actions</code>. You must provide at least one.</p>
<h4 id="scope">Scope</h4>
<p><code>scope</code> is a preset category of operations. Refer to <a href="/r2/api/tokens/#permissions">Permissions</a> for full definitions.</p>
<table>
<thead>
<tr>
<th>Scope</th>
<th>Allows</th>
</tr>
</thead>
<tbody>
<tr>
<td style="white-space: nowrap"><code>object-read-only</code></td>
<td>Read and list objects in the bucket.</td>
</tr>
<tr>
<td style="white-space: nowrap"><code>object-read-write</code></td>
<td>Read, write, and list objects in the bucket.</td>
</tr>
<tr>
<td style="white-space: nowrap"><code>admin-read-only</code></td>
<td>Read and list objects, view bucket configuration, and read from the data catalog.</td>
</tr>
<tr>
<td style="white-space: nowrap"><code>admin-read-write</code></td>
<td>Read, write, and list objects, edit bucket configuration, and read and write to the data catalog.</td>
</tr>
</tbody>
</table>
<h4 id="actions">Actions</h4>
<p><code>actions</code> is an explicit list of permitted S3 operations.</p>
<p>For example, <code>actions: [&quot;GetObject&quot;, &quot;HeadObject&quot;]</code> grants read of individual objects but denies <code>ListObjectsV2</code>, even though the broader <code>object-read-only</code> scope would allow listing.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/11528.md")
</aside>
<p>Valid actions:</p>
<table>
<thead>
<tr>
<th>Category</th>
<th>Actions</th>
</tr>
</thead>
<tbody>
<tr>
<td>Read</td>
<td><code>HeadObject</code>, <code>GetObject</code>, <code>GetBucketLocation</code>, <code>ListObjectsV1</code>, <code>ListObjectsV2</code>, <code>ListMultipartUploads</code>, <code>ListParts</code></td>
</tr>
<tr>
<td>Write</td>
<td><code>PutObject</code>, <code>DeleteObject</code>, <code>DeleteObjects</code>, <code>CopyObject</code></td>
</tr>
<tr>
<td>Multipart</td>
<td><code>CreateMultipartUpload</code>, <code>UploadPart</code>, <code>UploadPartCopy</code>, <code>AbortMultipartUpload</code>, <code>CompleteMultipartUpload</code></td>
</tr>
</tbody>
</table>
<h3 id="paths">Paths</h3>
<p>Restrict access to specific prefixes or objects within the bucket. Omit these fields to grant access to the entire bucket, subject to the permitted operations.</p>
<p><strong>Temporary Credentials API:</strong> pass <code>prefixes</code> and <code>objects</code> as top-level fields on the request body.</p>
<pre><code class="language-jsonc">{&#10;  &quot;prefixes&quot;: [&quot;uploads/user-123/&quot;],&#10;  &quot;objects&quot;: [&quot;shared/manifest.json&quot;]&#10;}&#10;</code></pre>
<p><strong>Local signing:</strong> set <code>paths.prefixPaths</code> and <code>paths.objectPaths</code> on the JWT payload.</p>
<pre><code class="language-jsonc">{&#10;  &quot;paths&quot;: {&#10;    &quot;prefixPaths&quot;: [&quot;uploads/user-123/&quot;],&#10;    &quot;objectPaths&quot;: [&quot;shared/manifest.json&quot;]&#10;  }&#10;}&#10;</code></pre>
<ul>
<li><code>prefixes</code> / <code>prefixPaths</code>: keys starting with any listed prefix.</li>
<li><code>objects</code> / <code>objectPaths</code>: exact object keys.</li>
</ul>
<h2 id="using-temporary-credentials">Using temporary credentials</h2>
<p>Any S3-compatible client that supports session tokens will accept R2 temporary credentials. Pass all three values (access key ID, secret access key, session token) using the client's standard credential fields.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/11532.md")
</div></div>
<h2 id="security-considerations">Security considerations</h2>
<p>Treat temporary credentials as bearer tokens. Anyone in possession of all three values can perform the allowed operations until the credential expires.</p>
<ul>
<li><strong>Scope as narrowly as possible.</strong> Set paths and permission scope so the credential can only do what the caller needs.</li>
<li><strong>Use short TTLs.</strong> Set <code>ttlSeconds</code> to the shortest value that fits your use case. A credential that lives for 15 minutes has a smaller blast radius than one that lives for a day.</li>
<li><strong>A temporary credential cannot exceed its parent.</strong> If you revoke the parent API token, all temporary credentials derived from it stop working immediately.</li>
<li><strong>Never ship your parent secret access key to a client.</strong> Local signing must happen in a trusted environment (such as your backend or a Worker).</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<p><a class="nb-card nb-link-card" href="/r2/examples/authenticate-r2-temp-credentials/"><h3 id="card-authenticate-against-r2-with-temporary-credentials-r2-examples-authenticate-r2-temp-credentials">Authenticate against R2 with temporary credentials</h3><p>End-to-end examples for both the Temporary Credentials API and local JWT signing.</p></a></p>
<p><a class="nb-card nb-link-card" href="/r2/api/s3/presigned-urls/"><h3 id="card-presigned-urls-r2-api-s3-presigned-urls">Presigned URLs</h3><p>Grant single-operation access to a specific object without issuing credentials.</p></a></p>
<p><a class="nb-card nb-link-card" href="/r2/api/tokens/"><h3 id="card-r2-api-tokens-r2-api-tokens">R2 API tokens</h3><p>Create the parent token that temporary credentials derive from.</p></a></p>
<p><a class="nb-card nb-link-card" href="/r2/api/error-codes/"><h3 id="card-error-codes-r2-api-error-codes">Error codes</h3><p>Authentication and authorization error codes returned by R2.</p></a></p>
