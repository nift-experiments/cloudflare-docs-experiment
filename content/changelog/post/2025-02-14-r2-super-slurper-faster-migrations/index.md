<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 14, 2025</time><h2 id="post-title">Super Slurper now transfers data to R2 up to 5x faster</h2>
<div class="changelog-badges"><span>r2</span></div><div class="changelog-body"><p><a href="/r2/data-migration/super-slurper/">Super Slurper</a> now transfers data from cloud object storage providers like AWS S3 and Google Cloud Storage to <a href="/r2/">Cloudflare R2</a> up to 5x faster than it did before.</p>
<p>We moved from a centralized service to a distributed system built on the Cloudflare Developer Platform — using <a href="/workers/">Cloudflare Workers</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/queues/">Queues</a> — to both improve performance and increase system concurrency capabilities (and we'll share more details about how we did it soon!)</p>
<p><img src="/assets/upstream/images/r2/slurper-objects-over-time-border.png" alt="Super Slurper Objects Migrated" /></p>
<p><em>Time to copy 75,000 objects from AWS S3 to R2 decreased from 15 minutes 30 seconds (old) to 3 minutes 25 seconds (after performance improvements)</em></p>
<p>For more information on Super Slurper and how to migrate data from existing object storage to R2, refer to our <a href="/r2/data-migration/super-slurper/">documentation</a>.</p>
</div></article></div>
