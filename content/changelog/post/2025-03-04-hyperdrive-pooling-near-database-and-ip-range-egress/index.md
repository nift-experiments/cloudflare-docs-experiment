<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>March 7, 2025</time><h2 id="post-title">Hyperdrive reduces query latency by up to 90% and now supports IP access control lists</h2>
<div class="changelog-badges"><span>hyperdrive</span></div><div class="changelog-body"><p>Hyperdrive now pools database connections in one or more regions close to your database. This means that your uncached queries and new database connections have up to 90% less latency as measured from connection pools.</p>
<p><img src="/assets/upstream/images/hyperdrive/configuration/hyperdrive-regional-pooling-query-latency-improvement.png" alt="Hyperdrive query latency decreases by 90% during Hyperdrive's gradual rollout of regional pooling." /></p>
<p>By improving placement of Hyperdrive database connection pools, Workers' Smart Placement is now more effective when used with Hyperdrive, ensuring that your Worker can be placed as close to your database as possible.</p>
<p>With this update, Hyperdrive also uses <a href="https://www.cloudflare.com/ips/">Cloudflare's standard IP address ranges</a> to connect to your database. This enables you to configure the firewall policies (IP access control lists) of your database to only allow access from Cloudflare and Hyperdrive.</p>
<p>Refer to <a href="/hyperdrive/concepts/how-hyperdrive-works/">documentation on how Hyperdrive makes connecting to regional databases from Cloudflare Workers fast</a>.</p>
<p>This improvement is enabled on all Hyperdrive configurations.</p>
</div></article></div>
