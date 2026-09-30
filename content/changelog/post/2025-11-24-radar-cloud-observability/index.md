<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>November 24, 2025</time><h2 id="post-title">Cloud Services Observability in Cloudflare Radar</h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><p><a href="/radar/"><strong>Radar</strong></a> introduces HTTP Origins insights, providing visibility into the status of traffic between Cloudflare's global network and cloud-based origin infrastructure.</p>
<p>The new <a href="/api/resources/radar/subresources/origins/"><code>Origins</code></a> API provides provides the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/origins/methods/list/"><code>/origins</code></a> - Lists all origins (cloud providers and associated regions).</li>
<li><a href="/api/resources/radar/subresources/origins/methods/get/"><code>/origins/{origin}</code></a> - Retrieves information about a specific origin (cloud provider).</li>
<li><a href="/api/resources/radar/subresources/origins/methods/timeseries/"><code>/origins/timeseries</code></a> - Retrieves normalized time series data for a specific origin, including the following metrics:
<ul>
<li><code>REQUESTS</code>: Number of requests</li>
<li><code>CONNECTION_FAILURES</code>: Number of connection failures</li>
<li><code>RESPONSE_HEADER_RECEIVE_DURATION</code>: Duration of the response header receive</li>
<li><code>TCP_HANDSHAKE_DURATION</code>: Duration of the TCP handshake</li>
<li><code>TCP_RTT</code>: TCP round trip time</li>
<li><code>TLS_HANDSHAKE_DURATION</code>: Duration of the TLS handshake</li>
</ul>
</li>
<li><a href="/api/resources/radar/subresources/origins/methods/summary/"><code>/origins/summary</code></a> - Retrieves HTTP requests to origins summarized by a dimension.</li>
<li><a href="/api/resources/radar/subresources/origins/methods/timeseries_groups/"><code>/origins/timeseries_groups</code></a> - Retrieves timeseries data for HTTP requests to origins grouped by a dimension.</li>
</ul>
<p>The following dimensions are available for the <code>summary</code> and <code>timeseries_groups</code> endpoints:</p>
<ul>
<li><code>region</code>: Origin region</li>
<li><code>success_rate</code>: Success rate of requests (2XX versus 5XX response codes)</li>
<li><code>percentile</code>: Percentiles of metrics listed above</li>
</ul>
<p>Additionally, the <a href="/api/resources/radar/subresources/annotations/"><code>Annotations</code></a> and <a href="/api/resources/radar/subresources/traffic_anomalies/"><code>Traffic Anomalies</code></a> APIs have been extended to support origin outages and anomalies, enabling automated detection and alerting for origin infrastructure issues.</p>
<p><img src="/assets/upstream/images/radar/cloud-service-status.png" alt="Screenshot of the cloud service status heatmap" /></p>
<p>Check out the <a href="https://radar.cloudflare.com/cloud-observatory">new Radar page</a>.</p>
</div></article></div>
