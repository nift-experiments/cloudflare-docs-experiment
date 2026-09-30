<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>September 29, 2025</time><h2 id="post-title">Regional Data in Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now introduces Regional Data, providing traffic insights that bring a more localized perspective to the traffic trends shown on Radar.</p>
<p>The following API endpoints are now available:</p>
<ul>
<li><a href="/api/resources/radar/subresources/geolocations/methods/get/"><code>Get Geolocation</code></a> - Retrieves geolocation by <code>geoId</code>.</li>
<li><a href="/api/resources/radar/subresources/geolocations/methods/list/"><code>List Geolocations</code></a> - Lists geolocations.</li>
<li><a href="/api/resources/radar/subresources/netflows/methods/summary_v2/"><code>NetFlows Summary By Dimension</code></a> - Retrieves NetFlows summary by dimension.</li>
</ul>
<p>All <code>summary</code> and <code>timeseries_groups</code> endpoints in <a href="/api/resources/radar/subresources/http/"><code>HTTP</code></a> and <a href="/api/resources/radar/subresources/netflows/"><code>NetFlows</code></a> now include an <code>adm1</code> dimension for grouping data by first level administrative division (for example, state, province, etc.)</p>
<p>A new filter <code>geoId</code> was also added to all endpoints in <a href="/api/resources/radar/subresources/http/"><code>HTTP</code></a> and <a href="/api/resources/radar/subresources/netflows/"><code>NetFlows</code></a>, allowing filtering by a specific administrative division.</p>
<p>Check out the new Regional traffic insights on a country specific traffic page <a href="https://radar.cloudflare.com/traffic/pt">new Radar page</a>.</p>
</div></article></div>
