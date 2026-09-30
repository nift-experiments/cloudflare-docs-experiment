<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 17, 2026</time><h2 id="post-title">New `us` jurisdiction for R2</h2>
<div class="changelog-badges"><span>r2</span></div><div class="changelog-body"><p>R2 now supports a <code>us</code> <a href="/r2/reference/data-location/#jurisdictional-restrictions">jurisdiction</a>, which guarantees that bucket data is stored and processed within the United States. Use this jurisdiction when you need explicit US data residency guarantees.</p>
<p>Use the jurisdiction-specific S3 endpoint to create and access buckets in the <code>us</code> jurisdiction:</p>
<p><code>https://&lt;ACCOUNT_ID&gt;.us.r2.cloudflarestorage.com</code></p>
<p>To access a bucket in the <code>us</code> jurisdiction from Workers, set <code>jurisdiction</code> in your R2 binding:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17741.md")</div>
<p>Once an R2 bucket is created, its jurisdiction cannot be changed.</p>
<p>For setup instructions and the full list of supported jurisdictions, refer to <a href="/r2/reference/data-location/#jurisdictional-restrictions">R2 data location</a>.</p>
</div></article></div>
