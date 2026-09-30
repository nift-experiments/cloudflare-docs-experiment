<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>October 27, 2025</time><h2 id="post-title">TLD Insights in Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> now introduces Top-Level Domain (TLD) insights, providing visibility into popularity based on the DNS magnitude metric, detailed TLD information including its type, manager, DNSSEC support, RDAP support, and WHOIS data, and trends such as DNS query volume and geographic distribution observed by the <a href="/1.1.1.1/">1.1.1.1</a> DNS resolver.</p>
<p>The following dimensions were added to the Radar DNS API, specifically, to the <a href="/api/resources/radar/subresources/dns/methods/summary_v2/"><code>/dns/summary/{dimension}</code></a> and <a href="/api/resources/radar/subresources/dns/methods/timeseries_groups_v2/"><code>/dns/timeseries_groups/{dimension}</code></a> endpoints:</p>
<ul>
<li><code>tld</code>: Top-level domain extracted from DNS queries; can also be used as a filter.</li>
<li><code>tld_dns_magnitude</code>: Top-level domain ranking by <a href="/radar/glossary#dns-magnitude">DNS magnitude</a>.</li>
</ul>
<p>And the following endpoints were added:</p>
<ul>
<li><a href="/api/resources/radar/subresources/tlds/methods/list/"><code>/tlds</code></a> - Lists all TLDs.</li>
<li><a href="/api/resources/radar/subresources/tlds/methods/get/"><code>/tlds/{tld}</code></a> - Retrieves information about a specific TLD.</li>
</ul>
<p><img src="/assets/upstream/images/radar/tld-ranking-by-dns-magnitude.png" alt="Screenshot of the TLD ranking by DNS magnitude" /></p>
<p>Learn more about the new Radar DNS insights in our <a href="https://blog.cloudflare.com/introducing-tld-insights-on-cloudflare-radar/">blog post</a>, and check out the <a href="https://radar.cloudflare.com/tlds">new Radar page</a>.</p>
</div></article></div>
