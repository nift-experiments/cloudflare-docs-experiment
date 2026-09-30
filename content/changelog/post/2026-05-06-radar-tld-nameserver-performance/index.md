<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>May 6, 2026</time><h2 id="post-title">TLD Nameserver Performance in Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now provides TLD authoritative nameserver performance insights, measuring response time (latency) as observed from Cloudflare's <a href="/1.1.1.1/">1.1.1.1</a> resolver infrastructure when forwarding queries upstream to TLD nameservers.</p>
<p>New widgets on <a href="https://radar.cloudflare.com/tlds/com">TLD detail pages</a>:</p>
<ul>
<li><a href="https://radar.cloudflare.com/tlds/com#tld-ns-latency"><strong>Aggregate nameserver latency</strong></a>: Response time percentiles (p25/p50/p75) for all authoritative nameservers of the selected TLD.</li>
<li><a href="https://radar.cloudflare.com/tlds/com#tld-ns-latency-by-ns"><strong>Latency per nameserver</strong></a>: Median response time (p50) broken down by each authoritative nameserver over time.</li>
</ul>
<p><img src="/assets/upstream/images/radar/tld-nameserver-latency-by-ns.png" alt="Latency per nameserver chart" /></p>
<ul>
<li><a href="https://radar.cloudflare.com/tlds/com#geographical-distribution"><strong>Median latency geographic distribution</strong></a>: p50 response time by Cloudflare data center country, displayed on a choropleth map.</li>
<li><a href="https://radar.cloudflare.com/tlds/com#tld-ranking"><strong>TLD ranking over time</strong></a>: Daily DNS magnitude rank and magnitude value with a Rank/Magnitude toggle.</li>
<li><a href="https://radar.cloudflare.com/tlds"><strong>Rank change deltas</strong></a>: 1 week, 4 weeks, and 3 months rank changes added to the TLD magnitude table and the TLD detail info panel.</li>
</ul>
<p><img src="/assets/upstream/images/radar/tld-magnitude-rank-deltas.webp" alt="TLD Rankings by DNS Magnitude table with rank change deltas" /></p>
<p>The new <a href="/api/resources/radar/subresources/tlds/subresources/performance/"><code>TLD Performance</code></a> API provides the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/tlds/subresources/performance/methods/summary/"><code>/tlds/performance/summary/{dimension}</code></a> — TLD nameserver performance summarized by dimension.</li>
<li><a href="/api/resources/radar/subresources/tlds/subresources/performance/methods/timeseries_groups/"><code>/tlds/performance/timeseries_groups/{dimension}</code></a> — TLD nameserver performance over time grouped by dimension.</li>
</ul>
<p>Available dimensions: <code>LATENCY</code> (aggregate p25/p50/p75), <code>NAMESERVER_LATENCY</code> (per-nameserver p50), <code>LOCATION_LATENCY</code> (per-data-center-country p50).</p>
<p>TLD Performance is also available as a dataset in the <a href="https://radar.cloudflare.com/explorer?dataSet=tlds.performance">Data Explorer</a>.</p>
<p>Check out the updated <a href="https://radar.cloudflare.com/tlds/com">TLD detail page</a>.</p>
</div></article></div>
