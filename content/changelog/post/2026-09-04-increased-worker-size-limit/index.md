<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 4, 2026</time><h2 id="post-title">Deploy larger Workers — up to 64 MiB for both free and paid plans</h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now deploy Workers with larger dependencies, heavier frameworks, and more code without hitting size limits.</p>
<p>When you deploy a Worker, Wrangler bundles your code and compresses it before uploading. Previously, Cloudflare checked that compressed size and rejected deploys over 3 MB (Free) or 10 MB (Paid). That limit has been removed. Cloudflare now only checks the uncompressed size of your bundle, which is 64 MiB across all plans.</p>
<p>To check your Worker's bundle size before deploying:</p>
<pre><code class="language-sh">wrangler deploy --outdir bundled/ --dry-run&#10;</code></pre>
<pre><code class="language-sh">Total Upload: 259.61 KiB / gzip: 47.23 KiB&#10;</code></pre>
<p>The <code>Total Upload</code> value is your uncompressed bundle size. This is what counts against the 64 MiB limit. The <code>gzip</code> value is shown for reference but is no longer a limit.</p>
<p>For more information, refer to the <a href="/workers/platform/limits/#worker-size">Worker size limits documentation</a>.</p>
</div></article></div>
