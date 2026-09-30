<p>Mount S3-compatible object storage buckets as local filesystem paths. Access object storage using standard file operations. For Cloudflare R2 in production, you can also mount by Worker R2 binding name so credentials stay in the Worker runtime.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="mounting-workspace">Mounting `/workspace`</h3>
@markup("md", "content/.markup/bodies/13385.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="s3-compatible-providers">S3-compatible providers</h3>
@markup("md", "content/.markup/bodies/13384.md")
</aside>
<h2 id="production-prerequisites-for-r2-binding-mounts">Production prerequisites for R2 binding mounts</h2>
<p>To mount an R2 bucket in production without passing credentials into the container, add an R2 binding and export <code>ContainerProxy</code> from your Worker entrypoint.</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13386.md")
</div>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13387.md")
</div>
<p>When you omit <code>endpoint</code>, the first argument to <code>mountBucket()</code> must be the Worker R2 binding name, such as <code>MY_BUCKET</code>.</p>
<h2 id="when-to-mount-buckets">When to mount buckets</h2>
<p>Mount S3-compatible buckets when you need:</p>
<ul>
<li><strong>Persistent data</strong> - Data survives sandbox destruction</li>
<li><strong>Large datasets</strong> - Process data without downloading</li>
<li><strong>Shared storage</strong> - Multiple sandboxes access the same data</li>
<li><strong>Cost-effective persistence</strong> - Cheaper than keeping sandboxes alive</li>
</ul>
<h2 id="mount-an-r2-bucket">Mount an R2 bucket</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13388.md")
</div>
<p>In this example, <code>MY_BUCKET</code> is the binding name from <code>wrangler.toml</code>. It does not have to match the bucket's dashboard name, although many projects use matching names.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="mounting-affects-entire-sandbox">Mounting affects entire sandbox</h3>
@markup("md", "content/.markup/bodies/13383.md")
</aside>
<h2 id="credentials">Credentials</h2>
<p>R2 binding mounts do not require credentials. Remote endpoint mounts remain supported for Cloudflare R2 and other S3-compatible providers, and those flows can still use automatic credential detection or explicit credentials.</p>
<h3 id="automatic-detection">Automatic detection</h3>
<p>When you include an <code>endpoint</code>, set credentials as Worker secrets and the SDK automatically detects them:</p>
<pre><code class="language-sh">npx wrangler secret put R2_ACCESS_KEY_ID&#10;npx wrangler secret put R2_SECRET_ACCESS_KEY&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="r2-credentials">R2 credentials</h3>
@markup("md", "content/.markup/bodies/13382.md")
</aside>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13389.md")
</div>
<h3 id="explicit-credentials">Explicit credentials</h3>
<p>Pass credentials directly when needed:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13390.md")
</div>
<h3 id="credential-proxy">Credential proxy</h3>
<p>When you mount with explicit credentials, s3fs writes those credentials to a password file on the container's disk. A compromised container process can read and exfiltrate the credentials, or use them to access storage outside the intended bucket scope.</p>
<p>Set <code>credentialProxy: true</code> to keep credentials out of the container entirely. Instead of passing real credentials into the container, the Durable Object intercepts all outbound S3 requests at the network layer, re-signs them with the real credentials, and forwards them upstream. The container only ever holds dummy credentials that are useless outside the proxy.</p>
<p>This works with <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html">AWS SigV4</a> signing for S3-compatible endpoints (including R2) and HMAC signing for Google Cloud Storage. It is recommended to set <code>credentialProxy: true</code> for all endpoint mounts. The option defaults to <code>false</code> for backwards compatibility and will become the default in a future version of the Sandbox SDK.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13391.md")
</div>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="containerproxy-export-required">ContainerProxy export required</h3>
@markup("md", "content/.markup/bodies/13381.md")
</aside>
<h2 id="mount-bucket-subdirectories">Mount bucket subdirectories</h2>
<p>Mount a specific subdirectory within a bucket using the <code>prefix</code> option. Only contents under the prefix are visible at the mount point:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13392.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="prefix-format">Prefix format</h3>
@markup("md", "content/.markup/bodies/13380.md")
</aside>
<h2 id="read-only-mounts">Read-only mounts</h2>
<p>Protect data by mounting buckets in read-only mode:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13393.md")
</div>
<h2 id="local-development">Local development</h2>
<p>You can also mount R2 buckets during local development with <code>wrangler dev</code> by passing the <code>localBucket</code> option. Production R2 binding mounts and local <code>localBucket</code> mounts both avoid explicit credentials, but they are different execution paths. Production uses credential-less egress interception and overlays the target path. Local development uses periodic synchronization with the R2 binding.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13394.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13379.md")
</aside>
<p>The <code>readOnly</code> and <code>prefix</code> options work the same way in local mode:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13395.md")
</div>
<h3 id="local-development-considerations">Local development considerations</h3>
<p>During local development, files are synchronized between R2 and the container using a periodic sync process rather than a direct filesystem mount. Keep the following in mind:</p>
<ul>
<li><strong>Synchronization window</strong> - A brief delay exists between when a file is written and when it appears on the other side. For example, if you upload a file to R2 and then immediately read it from the mounted path in the container, the file may not yet be available. Allow a short window for synchronization to complete before reading recently written data.</li>
<li><strong>High-frequency writes</strong> - Rapid successive writes to the same file path may take slightly longer to fully propagate. For best results, avoid writing to the same file from both R2 and the container at the same time.</li>
<li><strong>Bidirectional sync</strong> - Changes made in the container are synced to R2, and changes made in R2 are synced to the container. Both directions follow the same periodic sync model.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13378.md")
</aside>
<h2 id="unmount-buckets">Unmount buckets</h2>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13396.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="automatic-cleanup">Automatic cleanup</h3>
@markup("md", "content/.markup/bodies/13377.md")
</aside>
<h2 id="other-providers">Other providers</h2>
<p>The SDK supports any S3-compatible object storage. Here are examples for common providers:</p>
<h3 id="amazon-s3">Amazon S3</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13397.md")
</div>
<h3 id="google-cloud-storage">Google Cloud Storage</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13398.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="gcs-requires-hmac-keys">GCS requires HMAC keys</h3>
@markup("md", "content/.markup/bodies/13376.md")
</aside>
<h3 id="other-s3-compatible-providers">Other S3-compatible providers</h3>
<p>For providers like Backblaze B2, MinIO, Wasabi, or others, use the standard mount pattern:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13399.md")
</div>
<p>For provider-specific configuration, see the <a href="https://github.com/s3fs-fuse/s3fs-fuse/wiki/Non-Amazon-S3">s3fs-fuse wiki</a> for supported providers and recommended flags.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="r2-binding-not-found-error">R2 binding not found error</h3>
<p><strong>Error</strong>: <code>R2 binding &quot;MY_BUCKET&quot; not found in Worker env</code></p>
<p><strong>Solution</strong>: Ensure your Worker has an <code>r2_buckets</code> binding and that <code>mountBucket()</code> uses the binding name, not the bucket's dashboard name:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/13400.md")
</div>
<h3 id="credential-less-r2-mount-fails-immediately">Credential-less R2 mount fails immediately</h3>
<p><strong>Solution</strong>: Ensure your Worker entrypoint exports <code>ContainerProxy</code>. If you are using an older Wrangler version, you may also need the <code>enable_ctx_exports</code> compatibility flag.</p>
<h3 id="missing-credentials-error">Missing credentials error</h3>
<p><strong>Error</strong>: <code>MissingCredentialsError: No credentials found</code></p>
<p><strong>Solution</strong>: This error only applies when you mount a remote S3-compatible endpoint by setting <code>endpoint</code>. Set credentials as Worker secrets:</p>
<pre><code class="language-sh">npx wrangler secret put R2_ACCESS_KEY_ID&#10;npx wrangler secret put R2_SECRET_ACCESS_KEY&#10;</code></pre>
<p>or</p>
<pre><code class="language-sh">npx wrangler secret put AWS_ACCESS_KEY_ID&#10;npx wrangler secret put AWS_SECRET_ACCESS_KEY&#10;</code></pre>
<h3 id="mount-failed-error">Mount failed error</h3>
<p><strong>Error</strong>: <code>S3FSMountError: mount failed</code></p>
<p><strong>Common causes</strong>:</p>
<ul>
<li>Incorrect endpoint URL</li>
<li>Invalid credentials</li>
<li>Missing <code>ContainerProxy</code> export, or on older Wrangler versions missing <code>enable_ctx_exports</code></li>
<li>Bucket does not exist</li>
<li>Network connectivity issues</li>
</ul>
<p>Verify your binding or endpoint configuration:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13401.md")
</div>
<h3 id="path-already-mounted-error">Path already mounted error</h3>
<p><strong>Error</strong>: <code>InvalidMountConfigError: Mount path already in use</code></p>
<p><strong>Solution</strong>: Unmount first or use a different path:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13402.md")
</div>
<h3 id="slow-file-access">Slow file access</h3>
<p>File operations on mounted buckets are slower than local filesystem due to network latency.</p>
<p><strong>Solution</strong>: Copy frequently accessed files locally:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13403.md")
</div>
<h2 id="best-practices">Best practices</h2>
<ul>
<li><strong>Mount early</strong> - Mount buckets at sandbox initialization</li>
<li><strong>Choose the right mount mode</strong> - Use R2 binding mounts when you want Worker-managed R2 access, or use <code>endpoint</code> for explicit R2, S3, GCS, and other S3-compatible providers</li>
<li><strong>Secure credentials</strong> - Always use Worker secrets, never hardcode</li>
<li><strong>Read-only when possible</strong> - Protect data with read-only mounts</li>
<li><strong>Mount the narrowest path</strong> - Use prefixes to expose only the data a sandbox needs</li>
<li><strong>Mount paths</strong> - Prefer <code>/data</code>, <code>/storage</code>, or <code>/mnt/*</code>; if you mount under <code>/workspace</code>, account for the mount overlaying that path in production</li>
<li><strong>Handle errors</strong> - Wrap mount operations in <code>try...catch</code> blocks</li>
<li><strong>Optimize access</strong> - Copy frequently accessed files locally</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/tutorials/persistent-storage/">Persistent storage tutorial</a> - Complete R2 example</li>
<li><a href="/sandbox/guides/backup-restore/">Backup and restore</a> - Persist a project directory such as <code>/workspace</code></li>
<li><a href="/sandbox/api/storage/">Storage API reference</a> - Full method documentation</li>
<li><a href="/sandbox/configuration/environment-variables/">Environment variables</a> - Credential configuration for remote endpoint mounts</li>
<li><a href="/sandbox/configuration/wrangler/">Wrangler configuration</a> - Configure R2 bindings and compatibility flags</li>
<li><a href="/r2/">R2 documentation</a> - Learn about Cloudflare R2</li>
<li><a href="/sandbox/guides/outbound-traffic/">Outbound traffic</a> - Learn how <code>ContainerProxy</code> and outbound interception work</li>
</ul>
