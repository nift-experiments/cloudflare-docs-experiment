<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 5, 2025</time><h2 id="post-title">Bidirectional tunnel health checks are compatible with all Magic on-ramps</h2>
<div class="changelog-badges"><span>cloudflare-wan</span></div><div class="changelog-body"><p>All bidirectional tunnel health check return packets are accepted by any Magic on-ramp.</p>
<p>Previously, when a Magic tunnel had a bidirectional health check configured, the bidirectional health check would pass when the return packets came back to Cloudflare over the same tunnel that was traversed by the forward packets.</p>
<p>There are SD-WAN devices, like VeloCloud, that do not offer controls to steer traffic over one tunnel versus another in a high availability tunnel configuration.</p>
<p>Now, when a Magic tunnel has a bidirectional health check configured, the bidirectional health check will pass when the return packet traverses over any tunnel in a high availability configuration.</p>
</div></article></div>
