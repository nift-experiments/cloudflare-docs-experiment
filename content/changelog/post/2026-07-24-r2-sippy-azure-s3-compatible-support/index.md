<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 24, 2026</time><h2 id="post-title">Sippy now supports Azure Blob Storage and S3-compatible storage providers</h2>
<div class="changelog-badges"><span>r2</span></div><div class="changelog-body"><p><a href="/r2/data-migration/sippy/">Sippy</a> can now incrementally migrate data from Azure Blob Storage and any S3-compatible object storage provider to <a href="/r2/">Cloudflare R2</a>, in addition to Amazon S3 and Google Cloud Storage. Sippy copies objects to R2 as your application requests them, so you can start serving data from R2 without first moving your entire dataset or paying migration-specific egress fees.</p>
<h4 id="enable-sippy">Enable Sippy</h4>
<p>Run the following command and follow the prompts to select and configure your source storage provider:</p>
<pre><code class="language-sh">npx wrangler r2 bucket sippy enable &lt;BUCKET_NAME&gt;&#10;</code></pre>
<p>For Azure Blob Storage, provide your storage account name, container name, and either an account key or a shared access signature (SAS) token with read and list permissions. For an S3-compatible provider, provide the S3 API endpoint URL and read-only Access Key ID and Secret Access Key.</p>
<p><img src="/assets/upstream/images/r2/sippy-azure-source-configuration.png" alt="Azure Blob Storage source configuration in the R2 dashboard" /></p>
<p>After you enable Sippy, requests for objects that are not yet in R2 are served from your source bucket and copied to R2. Subsequent requests for those objects are served from R2.</p>
<p>For setup instructions and credential requirements, refer to the <a href="/r2/data-migration/sippy/">Sippy documentation</a>.</p>
</div></article></div>
