<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 14, 2025</time><h2 id="post-title">Customize queue message retention periods</h2>
<div class="changelog-badges"><span>queues</span></div><div class="changelog-body"><p>You can now customize a queue's message retention period, from a minimum of 60 seconds to a maximum of 14 days. Previously, it was fixed to the default of 4 days.</p>
<p><img src="/assets/upstream/images/queues/customize-retention-period.png" alt="Customize a queue's message retention period" /></p>
<p>You can customize the retention period on the settings page for your queue, or using Wrangler:</p>
<pre><code class="language-bash">$ wrangler queues update my-queue --message-retention-period-secs 600&#10;</code></pre>
<p>This feature is available on all new and existing queues. If you haven't used Cloudflare Queues before, <a href="/queues/get-started">get started with the Cloudflare Queues guide</a>.</p>
</div></article></div>
