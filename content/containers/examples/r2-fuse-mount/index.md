<p class="article-summary">Mount R2 buckets as filesystems using FUSE in Containers</p>
<p>FUSE (Filesystem in Userspace) allows you to mount <a href="/r2/">R2 buckets</a> as filesystems within Containers. Applications can then interact with R2 using standard filesystem operations rather than object storage APIs.</p>
<p>To run a FUSE container locally, refer to <a href="/containers/guides/local-dev/#fuse-support">FUSE support during local development</a>.</p>
<p>Common use cases include:</p>
<ul>
<li><strong>Bootstrapping containers with assets</strong> - Mount datasets, models, or dependencies for sandboxes and agent environments</li>
<li><strong>Persisting user state</strong> - Store and access user configuration or application state without managing downloads</li>
<li><strong>Large static files</strong> - Avoid bloating container images or downloading files at startup</li>
<li><strong>Editing files</strong> - Make code or config available within the container and save edits across instances.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="performance-considerations">Performance considerations</h3>
@markup("md", "content/.markup/bodies/7140.md")
</aside>
<h2 id="mounting-buckets">Mounting buckets</h2>
<p>To mount an R2 bucket, install a FUSE adapter in your Dockerfile and configure it to run at container startup.</p>
<p>This example uses <a href="https://github.com/tigrisdata/tigrisfs">tigrisfs</a>, which supports S3-compatible storage including R2:</p>
<details class="nb-details"><summary>Dockerfile</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7141.md")
</div></details>
<p>The startup script creates a mount point, starts tigrisfs in the background to mount the bucket, and then lists the mounted directory contents.</p>
<h3 id="passing-credentials-to-the-container">Passing credentials to the container</h3>
<p>Your Container needs <a href="/r2/api/tokens/">R2 credentials</a> and configuration passed as environment variables. Store credentials as <a href="/workers/configuration/secrets/">Worker secrets</a>, then pass them through the <code>envVars</code> property:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/7142.md")
</div>
<p>The <code>AWS_ACCESS_KEY_ID</code> and <code>AWS_SECRET_ACCESS_KEY</code> should be stored as secrets, while <code>R2_BUCKET_NAME</code> and <code>R2_ACCOUNT_ID</code> can be configured as variables in your <code>wrangler.jsonc</code>:</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="creating-your-r2-aws-api-keys">Creating your R2 AWS API keys</h3>
@markup("md", "content/.markup/bodies/7139.md")
</aside>
<pre><code class="language-json">{&#10;  &quot;vars&quot;: {&#10;    &quot;R2_BUCKET_NAME&quot;: &quot;my-bucket&quot;,&#10;    &quot;R2_ACCOUNT_ID&quot;: &quot;your-account-id&quot;&#10;  }&#10;}&#10;</code></pre>
<h3 id="other-s3-compatible-storage-providers">Other S3-compatible storage providers</h3>
<p>Other S3-compatible storage providers, including AWS S3 and Google Cloud Storage, can be mounted using the same approach as R2. You will need to provide the appropriate endpoint URL and access credentials for the storage provider.</p>
<h2 id="mounting-bucket-prefixes">Mounting bucket prefixes</h2>
<p>To mount a specific prefix (subdirectory) within a bucket, most FUSE adapters require mounting the entire bucket and then accessing the prefix path within the mount.</p>
<p>With tigrisfs, mount the bucket and access the prefix via the filesystem path:</p>
<pre><code class="language-dockerfile">RUN printf &#x27;#!/bin/sh\n\&#10;    set -e\n\&#10;    \n\&#10;    mkdir -p /mnt/r2\n\&#10;    \n\&#10;    R2_ENDPOINT=&quot;https://${R2_ACCOUNT_ID}.r2.cloudflarestorage.com&quot;\n\&#10;    /usr/local/bin/tigrisfs --endpoint &quot;${R2_ENDPOINT}&quot; -f &quot;${R2_BUCKET_NAME}&quot; /mnt/r2 &amp;\n\&#10;    sleep 3\n\&#10;    \n\&#10;    echo &quot;Accessing prefix: ${BUCKET_PREFIX}&quot;\n\&#10;    ls -lah &quot;/mnt/r2/${BUCKET_PREFIX}&quot;\n\&#10;    &#x27; &gt; /startup.sh &amp;&amp; chmod +x /startup.sh&#10;</code></pre>
<p>Your application can then read from <code>/mnt/r2/${BUCKET_PREFIX}</code> to access only the files under that prefix. Pass <code>BUCKET_PREFIX</code> as an environment variable alongside your other R2 configuration.</p>
<h2 id="mounting-buckets-as-read-only">Mounting buckets as read-only</h2>
<p>To prevent applications from writing to the mounted bucket, add the <code>-o ro</code> flag to mount the filesystem as read-only:</p>
<pre><code class="language-dockerfile">RUN printf &#x27;#!/bin/sh\n\&#10;    set -e\n\&#10;    \n\&#10;    mkdir -p /mnt/r2\n\&#10;    \n\&#10;    R2_ENDPOINT=&quot;https://${R2_ACCOUNT_ID}.r2.cloudflarestorage.com&quot;\n\&#10;    /usr/local/bin/tigrisfs --endpoint &quot;${R2_ENDPOINT}&quot; -o ro -f &quot;${R2_BUCKET_NAME}&quot; /mnt/r2 &amp;\n\&#10;    sleep 3\n\&#10;    \n\&#10;    ls -lah /mnt/r2\n\&#10;    &#x27; &gt; /startup.sh &amp;&amp; chmod +x /startup.sh&#10;</code></pre>
<p>This is useful for shared assets or configuration files where you want to ensure applications only read data.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/containers/examples/env-vars-and-secrets/">Container environment variables</a> - Learn how to pass secrets and variables to Containers</li>
<li><a href="https://github.com/tigrisdata/tigrisfs">tigrisfs</a> - FUSE adapter for S3-compatible storage including R2</li>
<li><a href="https://github.com/s3fs-fuse/s3fs-fuse">s3fs</a> - Alternative FUSE adapter for S3-compatible storage</li>
<li><a href="https://github.com/GoogleCloudPlatform/gcsfuse">gcsfuse</a> - FUSE adapter for Google Cloud Storage buckets</li>
</ul>
