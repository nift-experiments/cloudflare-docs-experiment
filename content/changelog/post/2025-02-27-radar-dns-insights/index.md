<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>February 27, 2025</time><h2 id="post-title">DNS Insights in Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> has expanded its DNS insights, providing visibility into aggregated traffic and usage trends observed by our <a href="/1.1.1.1/">1.1.1.1</a> DNS resolver.
In addition to global, location, and ASN traffic trends, we are also providing perspectives on protocol usage, query/response characteristics, and DNSSEC usage.</p>
<p>Previously limited to the <a href="/api/resources/radar/subresources/dns/subresources/top/"><code>top</code></a> locations and ASes endpoints, we have now introduced the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/dns/methods/timeseries/"><code>/dns/timeseries</code></a>: Retrieves DNS query volume over time.</li>
<li><a href="/api/resources/radar/subresources/dns/subresources/summary/"><code>/dns/summary/{dimension}</code></a>: Retrieves summaries of DNS query distribution across ten different dimensions.</li>
<li><a href="/api/resources/radar/subresources/dns/subresources/timeseries_groups/"><code>/dns/timeseries_groups/{dimension}</code></a>: Retrieves timeseries data for DNS query distribution across ten different dimensions.</li>
</ul>
<p>For the <code>summary</code> and <code>timeseries_groups</code> endpoints, the following dimensions are available, displaying the distribution of DNS queries based on:</p>
<ul>
<li><code>cache_hit</code>: Cache status (hit vs. miss).</li>
<li><code>dnsssec</code>: DNSSEC support status (secure, insecure, invalid or other).</li>
<li><code>dnsssec_aware</code>: DNSSEC client awareness (aware vs. not-aware).</li>
<li><code>dnsssec_e2e</code>: End-to-end security (secure vs. insecure).</li>
<li><code>ip_version</code>: IP version (IPv4 vs. IPv6).</li>
<li><code>matching_answer</code>: Matching answer status (match vs. no-match).</li>
<li><code>protocol</code>: Transport protocol (UDP, TLS, HTTPS or TCP).</li>
<li><code>query_type</code>: Query type (<code>A</code>, <code>AAAA</code>, <code>PTR</code>, etc.).</li>
<li><code>response_code</code>: Response code (<code>NOERROR</code>, <code>NXDOMAIN</code>, <code>REFUSED</code>, etc.).</li>
<li><code>response_ttl</code>: Response TTL.</li>
</ul>
<p>Learn more about the new Radar DNS insights in our <a href="https://blog.cloudflare.com/new-dns-section-on-cloudflare-radar/">blog post</a>, and check out the <a href="https://radar.cloudflare.com/dns">new Radar page</a>.</p>
</div></article></div>
