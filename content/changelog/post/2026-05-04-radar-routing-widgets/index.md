<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 4, 2026</time><h2 id="post-title">New routing widgets on Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> is expanding its <a href="https://radar.cloudflare.com/routing">Routing section</a> with two new widgets that give a deeper view into how networks announce address space and how RPKI ROA coverage evolves over time.</p>
<h4 id="top-ases-by-announced-ip-space-on-country-pages">Top ASes by announced IP space on country pages</h4>
<p>Country routing pages now include a <strong>Top ASes by announced IP space</strong> chart, breaking down the IPv4 and IPv6 address space announced from a country across the autonomous systems that originate it. The chart stacks the IPv4 and IPv6 views vertically, with the top contributing ASes called out by color and the remaining networks aggregated as <strong>Other</strong>.</p>
<p><img src="/assets/upstream/images/radar/country-top-ases-ip-space.png" alt="Screenshot of the top ASes by announced IP space chart on a country routing page" /></p>
<h4 id="rpki-roa-deployment-timeseries">RPKI ROA deployment timeseries</h4>
<p>The <a href="https://radar.cloudflare.com/routing/rpki">RPKI sub-page</a> adds an <strong>RPKI ROA deployment</strong> timeseries widget that tracks the share of announced BGP space covered by a valid Route Origin Authorization (ROA) over time, with separate IPv4 and IPv6 lines. A toggle switches the view between the share of covered <strong>prefixes</strong> and the share of covered <strong>IP address space</strong>. The widget is available on global, country, and AS views, so operators can monitor RPKI adoption progress and compare deployment trends across different scopes.</p>
<p><img src="/assets/upstream/images/radar/rpki-roa-deployment-timeseries.png" alt="Screenshot of the RPKI ROA deployment timeseries widget" /></p>
<h4 id="api-endpoints">API endpoints</h4>
<p>The data behind these widgets is also available through two new endpoints on the <a href="/api/resources/radar/subresources/bgp/"><code>BGP</code></a> API:</p>
<ul>
<li><a href="/api/resources/radar/subresources/bgp/subresources/ips/subresources/top/methods/ases/"><code>/bgp/ips/top/ases</code></a> - Returns the top autonomous systems by announced IP space (IPv4 <code>/24</code>s or IPv6 <code>/48</code>s), globally or filtered by country, snapped to the nearest 8-hour RIB boundary.</li>
<li><a href="/api/resources/radar/subresources/bgp/subresources/rpki/subresources/roas/methods/timeseries/"><code>/bgp/rpki/roas/timeseries</code></a> - Returns RPKI ROA validation coverage over time, by share of prefixes or share of IP address space, split by IP version, with optional ASN or location filters.</li>
</ul>
<p>Visit the <a href="https://radar.cloudflare.com/routing">Radar routing section</a> to explore both widgets.</p>
</div></article></div>
