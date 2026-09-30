---
cp9:
  canonical: https://developers.cloudflare.com/sandbox/api/storage/
  description: Mount S3-compatible storage buckets into the Sandbox SDK filesystem for persistent data access.
  full_title: Storage · Cloudflare Sandbox SDK docs
  head_html: <title>Storage · Cloudflare Sandbox SDK docs</title><meta name="generator" content="Nift"><meta name="description" content="Mount S3-compatible storage buckets into the Sandbox SDK filesystem for persistent data access."><link rel="canonical" href="https://developers.cloudflare.com/sandbox/api/storage/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/sandbox/api/storage/index.md"><meta property="og:title" content="Storage · Cloudflare Sandbox SDK docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Mount S3-compatible storage buckets into the Sandbox SDK filesystem for persistent data access."><meta property="og:url" content="https://developers.cloudflare.com/sandbox/api/storage/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Sandbox SDK"><meta name="algolia_product_filter" content="Sandbox SDK"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Sandbox SDK"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/sandbox/api/storage/#page","headline":"Storage \u00b7 Cloudflare Sandbox SDK docs","description":"Mount S3-compatible storage buckets into the Sandbox SDK filesystem for persistent data access.","url":"https://developers.cloudflare.com/sandbox/api/storage/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /sandbox/api/storage/
  schema: 1
---
<p>Mount S3-compatible storage buckets (R2, S3, GCS) into the sandbox filesystem for persistent data access. <code>mountBucket()</code> supports R2 binding mounts, local R2 binding sync during development, and remote S3-compatible endpoint mounts.</p>
<h2 id="methods">Methods</h2>
<h3 id="mountbucket"><code>mountBucket()</code></h3>
<p>Mount an S3-compatible bucket to a local path in the sandbox.</p>
<pre tabindex="0"><code class="language-ts">await sandbox.mountBucket(&#10;  bucket: string,&#10;  mountPath: string,&#10;  options?: MountBucketOptions&#10;): Promise&lt;void&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>bucket</code> - Bucket identifier
<ul>
<li>When <code>options.endpoint</code> is omitted, pass the Worker R2 binding name (for example, <code>&quot;MY_BUCKET&quot;</code>)</li>
<li>When <code>options.endpoint</code> is provided, pass the remote bucket name (for example, <code>&quot;my-r2-bucket&quot;</code>)</li>
</ul>
</li>
<li><code>mountPath</code> - Local filesystem path to mount at (e.g., <code>&quot;/data&quot;</code>)</li>
<li><code>options</code> (optional) - Mount configuration (see <a href="#mountbucketoptions"><code>MountBucketOptions</code></a>)</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13601.md")
</div>
<p><strong>Throws</strong>:</p>
<ul>
<li><code>InvalidMountPointError</code> - Invalid mount path or conflicts with existing mounts</li>
<li><code>BucketAccessError</code> - Bucket does not exist or insufficient permissions</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="authentication">Authentication</h3>
@markup("md", "content/.markup/bodies/13600.md")
</aside>
<h3 id="unmountbucket"><code>unmountBucket()</code></h3>
<p>Unmount a previously mounted bucket.</p>
<pre tabindex="0"><code class="language-ts">await sandbox.unmountBucket(mountPath: string): Promise&lt;void&gt;&#10;</code></pre>
<p><strong>Parameters</strong>:</p>
<ul>
<li><code>mountPath</code> - Path where the bucket is mounted (e.g., <code>&quot;/data&quot;</code>)</li>
</ul>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/13602.md")
</div>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="automatic-cleanup">Automatic cleanup</h3>
@markup("md", "content/.markup/bodies/13599.md")
</aside>
<h2 id="types">Types</h2>
<h3 id="mountbucketoptions"><code>MountBucketOptions</code></h3>
<pre tabindex="0"><code class="language-ts">interface RemoteMountBucketOptions {&#10;  endpoint: string;&#10;  provider?: BucketProvider;&#10;  credentials?: BucketCredentials;&#10;  credentialProxy?: boolean;&#10;  readOnly?: boolean;&#10;  s3fsOptions?: string[];&#10;  prefix?: string;&#10;}&#10;&#10;interface LocalMountBucketOptions {&#10;  localBucket: true;&#10;  prefix?: string;&#10;  readOnly?: boolean;&#10;}&#10;&#10;interface R2BindingMountBucketOptions {&#10;  endpoint?: never;&#10;  prefix?: string;&#10;  readOnly?: boolean;&#10;  s3fsOptions?: string[];&#10;}&#10;&#10;type MountBucketOptions =&#10;  | RemoteMountBucketOptions&#10;  | LocalMountBucketOptions&#10;  | R2BindingMountBucketOptions;&#10;</code></pre>
<p><code>mountBucket()</code> supports these three modes:</p>
<ul>
<li>
<p><strong>R2 binding mount</strong> - Omit <code>endpoint</code> to mount by Worker binding name in production</p>
<ul>
<li>Uses credential-less egress interception for R2</li>
<li>Supports <code>prefix</code>, <code>readOnly</code>, and <code>s3fsOptions</code></li>
</ul>
</li>
<li>
<p><strong>Local R2 binding mount</strong> - Set <code>localBucket: true</code> during <code>wrangler dev</code></p>
<ul>
<li>Uses the Worker R2 binding directly through local synchronization</li>
<li>Supports <code>prefix</code> and <code>readOnly</code></li>
</ul>
</li>
<li>
<p><strong>Remote endpoint mount</strong> - Set <code>endpoint</code> to mount any S3-compatible provider</p>
<ul>
<li>Supports explicit <code>credentials</code> or environment variable auto-detection</li>
<li>Set <code>credentialProxy: true</code> to keep credentials out of the container (egress interception)</li>
<li>Supports <code>provider</code>, <code>prefix</code>, <code>readOnly</code>, and <code>s3fsOptions</code></li>
</ul>
</li>
</ul>
<p><strong>Field details</strong>:</p>
<ul>
<li>
<p><code>endpoint</code> (remote endpoint mode only) - S3-compatible endpoint URL</p>
<ul>
<li>R2: <code>'https://YOUR_ACCOUNT_ID.r2.cloudflarestorage.com'</code></li>
<li>S3: <code>'https://s3.amazonaws.com'</code></li>
<li>GCS: <code>'https://storage.googleapis.com'</code></li>
</ul>
</li>
<li>
<p><code>localBucket</code> (local development mode only) - Mount an R2 bucket using the Worker's R2 binding during local development with <code>wrangler dev</code></p>
<ul>
<li>When <code>true</code>, the SDK syncs the R2 binding directly instead of using an S3 endpoint</li>
</ul>
</li>
<li>
<p><code>provider</code> (remote endpoint mode only) - Storage provider hint</p>
<ul>
<li>Enables provider-specific optimizations</li>
<li>Values: <code>'r2'</code>, <code>'s3'</code>, <code>'gcs'</code></li>
</ul>
</li>
<li>
<p><code>credentials</code> (remote endpoint mode only) - API credentials</p>
<ul>
<li>Contains <code>accessKeyId</code> and <code>secretAccessKey</code></li>
<li>If not provided, uses environment variables</li>
</ul>
</li>
<li>
<p><code>credentialProxy</code> (remote endpoint mode only) - Route S3 requests through the Durable Object for signing</p>
<ul>
<li>When <code>true</code>, credentials are never written to the container's disk. The Durable Object intercepts and re-signs all outbound S3 requests at the network layer before forwarding them upstream.</li>
<li>Supports <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html">AWS SigV4</a> signing for S3-compatible endpoints (including R2) and HMAC signing for Google Cloud Storage</li>
<li>Requires <code>ContainerProxy</code> to be exported from your Worker entrypoint</li>
<li>Default: <code>false</code> (backwards compatibility — recommended to set to <code>true</code>; will become the default in a future version)</li>
</ul>
</li>
<li>
<p><code>readOnly</code> (optional) - Mount in read-only mode</p>
<ul>
<li>Default: <code>false</code></li>
</ul>
</li>
<li>
<p><code>prefix</code> (optional) - Subdirectory within the bucket to mount</p>
<ul>
<li>When specified, only contents under this prefix are visible at the mount point</li>
<li>Must start with <code>/</code> (for example, <code>/data/uploads</code> or <code>/data/uploads/</code>)</li>
<li>Default: Mount entire bucket</li>
</ul>
</li>
<li>
<p><code>s3fsOptions</code> (R2 binding and remote endpoint modes only) - Advanced s3fs mount flags</p>
<ul>
<li>Type: <code>string[]</code></li>
<li>Example: <code>['use_cache=/tmp/cache', 'stat_cache_expire=1']</code></li>
</ul>
</li>
</ul>
<h3 id="bucketprovider"><code>BucketProvider</code></h3>
<p>Storage provider hint for automatic s3fs flag optimization.</p>
<pre tabindex="0"><code class="language-ts">type BucketProvider = &quot;r2&quot; | &quot;s3&quot; | &quot;gcs&quot;;&#10;</code></pre>
<ul>
<li><code>'r2'</code> - Cloudflare R2 (recommended, applies <code>nomixupload</code> flag)</li>
<li><code>'s3'</code> - Amazon S3</li>
<li><code>'gcs'</code> - Google Cloud Storage</li>
</ul>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/sandbox/guides/mount-buckets/">Mount Buckets guide</a> - Complete bucket mounting walkthrough</li>
<li><a href="/sandbox/api/files/">Files API</a> - Read and write files</li>
</ul>
