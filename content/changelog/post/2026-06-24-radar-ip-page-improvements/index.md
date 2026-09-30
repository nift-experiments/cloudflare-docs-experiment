<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 24, 2026</time><h2 id="post-title">Precise IP location and richer AS details on the Cloudflare Radar IP page</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now plots your IPv4 and IPv6 locations on the <a href="https://radar.cloudflare.com/ip">IP page</a>, shows the Cloudflare data centers serving your connection, and includes more detail about the autonomous system (AS) your primary IP belongs to.</p>
<h4 id="your-ip-location-on-the-map">Your IP location on the map</h4>
<p>The map of your connection now shows:</p>
<ul>
<li><strong>IP location markers</strong> — The primary IP will show as a red marker. When both IP addresses do not geolocate to the same place, a second marker will appear in blue with a note explaining why IPv4 and IPv6 can resolve to different locations.</li>
<li><strong>Cloudflare data center markers</strong> — Cloudflare data centers now show as orange dots on the map and the one you are connected to is highlighted.</li>
<li><strong>Data center connectors</strong> — Each line connects your IP markers to their respective data centers.</li>
</ul>
<p><img src="/assets/upstream/images/radar/ip-page-geolocation.png" alt="Map showing Cloudflare data centers and a marker representing the IP location with a line connected to a data center" /></p>
<p>Due to the data policies of our geolocation provider, this detailed location is only available for your own IP. Other IP addresses keep the current country-level view.</p>
<h4 id="extended-as-information">Extended AS information</h4>
<p>The AS card on the IP page now shows additional detail about the network an IP belongs to — including alternate names, the operator website, and an estimate of the AS user population — alongside the AS number and country.</p>
<p>Visit the <a href="https://radar.cloudflare.com/ip">Cloudflare Radar IP page</a> to explore more details about your IP.</p>
</div></article></div>
