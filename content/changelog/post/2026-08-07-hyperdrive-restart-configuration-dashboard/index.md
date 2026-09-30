<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 7, 2026</time><h2 id="post-title">Restart a Hyperdrive configuration from the dashboard</h2>
<div class="changelog-badges"><span>hyperdrive</span></div><div class="changelog-body"><p>You can now restart a Hyperdrive configuration from the Cloudflare dashboard. Restarting drains the connection pool and forces Hyperdrive to establish new connections to your origin database.</p>
<p>Restarting is a break-glass action. Hyperdrive automatically detects and recovers from most database failovers. Use a manual restart only when you need to force the pool to drain immediately.</p>
<p>To restart, select your Hyperdrive configuration in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>, go to the <strong>Settings</strong> tab, and select <strong>Restart</strong> under <strong>Danger zone</strong>. Restarting requires the <a href="/fundamentals/manage-members/roles/"><strong>Hyperdrive Admin</strong> role</a>. After a restart, the <strong>Settings</strong> tab shows when the configuration was last manually restarted.</p>
<p><img src="/assets/upstream/images/hyperdrive/dashboard-restart-danger-zone.png" alt="The Danger zone section of the Hyperdrive Settings tab, showing the Restart and Delete actions." /></p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/17734.md")</aside>
<p>For more information, refer to <a href="/hyperdrive/concepts/connection-pooling/">Connection pooling</a>.</p>
</div></article></div>
