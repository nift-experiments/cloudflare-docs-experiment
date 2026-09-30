<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 30, 2025</time><h2 id="post-title">Graceful withdrawal of BYOIP prefixes</h2>
<div class="changelog-badges"><span>magic-transit</span></div><div class="changelog-body"><p>Magic Transit customers can now configure AS prepending on their BYOIP prefixes advertised at the Cloudflare edge. This allows for smoother traffic migration and minimizes packet loss when changing providers.</p>
<p>AS prepending makes the Cloudflare route less preferred by increasing the AS path length. You can use this to gradually shift traffic away from Cloudflare before withdrawing a prefix, avoiding abrupt routing changes.</p>
<p>Prepending can be configured via the API or through BGP community values when peering with the Magic Transit routing table. For more information, refer to <a href="/magic-transit/how-to/advertise-prefixes/">Advertise prefixes</a>.</p>
</div></article></div>
