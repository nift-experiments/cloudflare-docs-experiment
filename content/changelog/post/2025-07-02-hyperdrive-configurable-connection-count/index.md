<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 3, 2025</time><h2 id="post-title">Hyperdrive now supports configuring the amount of database connections</h2>
<div class="changelog-badges"><span>hyperdrive</span></div><div class="changelog-body"><p>You can now specify the number of connections your Hyperdrive configuration uses to connect to your origin database.</p>
<p>All configurations have a minimum of 5 connections. The maximum connection count for a Hyperdrive configuration depends on the <a href="/hyperdrive/platform/limits/">Hyperdrive limits of your Workers plan</a>.</p>
<p>This feature allows you to right-size your connection pool based on your database capacity and application requirements. You can configure connection counts through the Cloudflare dashboard or API.</p>
<p>Refer to the <a href="/hyperdrive/concepts/connection-pooling/">Hyperdrive configuration documentation</a> for more information.</p>
</div></article></div>
