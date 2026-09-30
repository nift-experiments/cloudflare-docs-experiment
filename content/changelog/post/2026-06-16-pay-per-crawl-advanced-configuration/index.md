<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 16, 2026</time><h2 id="post-title">Pay Per Crawl advanced configuration</h2>
<div class="changelog-badges"><span>ai-crawl-control</span></div><div class="changelog-body"><p>You can now configure advanced Pay Per Crawl settings for your zone, including:</p>
<ul>
<li><strong>Disable Pay Per Crawl by URI pattern</strong> using <a href="/rules/configuration-rules/">Configuration Rules</a> to offer free access to specific pages while charging for others.</li>
<li><strong>Dynamic pricing</strong> by having your origin return a <code>crawler-price</code> response header, or by using a <a href="/workers/">Cloudflare Worker</a> to set prices based on request properties.</li>
</ul>
<p>When dynamic pricing is enabled, Pay Per Crawl adds a <code>cf-pay-per-crawl</code> request header to origin requests so your origin or Worker can determine the appropriate price.</p>
<p>Refer to the <a href="/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-site-owner/advanced-configuration/">Advanced configuration documentation</a> for details.</p>
</div></article></div>
