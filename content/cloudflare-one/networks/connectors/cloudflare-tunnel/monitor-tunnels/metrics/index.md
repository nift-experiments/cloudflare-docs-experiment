---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/metrics/
  description: How Metrics works in Zero Trust networking.
  full_title: Tunnel metrics · Cloudflare One docs
  head_html: <title>Tunnel metrics · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="How Metrics works in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/metrics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/metrics/index.md"><meta property="og:title" content="Tunnel metrics · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How Metrics works in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/metrics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/metrics/#page","headline":"Tunnel metrics \u00b7 Cloudflare One docs","description":"How Metrics works in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/metrics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/metrics/
  schema: 1
---
<hr />
<hr />
<p>Tunnel metrics show a Cloudflare Tunnel's throughput and resource usage over time. When you run a tunnel, <code>cloudflared</code> will spin up a Prometheus metrics endpoint — an HTTP server that exposes metrics in <a href="https://prometheus.io/docs/introduction/overview/">Prometheus</a> format. You can use the Prometheus toolkit on a remote machine to scrape metrics data from the <code>cloudflared</code> server.</p>
<h2 id="default-metrics-server-address">Default metrics server address</h2>
<p>In non-containerized environments, <code>cloudflared</code> starts the metrics server on <code>127.0.0.1:&lt;PORT&gt;/metrics</code>, where <code>&lt;PORT&gt;</code> is the first available port in the range <code>20241</code> to <code>20245</code>. If all ports are unavailable, <code>cloudflared</code> binds to a random port. In containerized environments (Docker, Kubernetes), the default address is <code>0.0.0.0:&lt;PORT&gt;/metrics</code>.</p>
<p>To determine the default port, check your <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">tunnel logs</a> around the time when the tunnel started. For example:</p>
<pre tabindex="0"><code class="language-text">2024-12-19T21:17:58Z INF Starting metrics server on 127.0.0.1:20241/metrics&#10;</code></pre>
<h2 id="configure-the-metrics-server-address">Configure the metrics server address</h2>
<p>To serve metrics on a custom IP address and port, perform these steps on the <code>cloudflared</code> host:</p>
<ol>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#add-run-parameters-to-tunnel-service">Run the tunnel</a> using the
<code>--metrics</code> flag. For example,</li>
</ol>
<pre tabindex="0"><code class="language-sh">cloudflared tunnel --metrics 127.0.0.1:60123 run my-tunnel&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5288.md")
</aside>
<ol start="2">
<li>Verify that the metrics server is running by going to <code>http://localhost:60123/metrics</code>. This will only work if you configured a localhost IP (<code>127.0.0.1</code> or <code>0.0.0.0</code>).</li>
</ol>
<p>You can now export the metrics to Prometheus and Grafana to visualize and query the data. Refer to the <a href="/cloudflare-one/tutorials/grafana/">Grafana tutorial</a> for instructions on getting started with these tools.</p>
<h2 id="available-metrics">Available metrics</h2>
<h3 id="cloudflared-metrics">cloudflared metrics</h3>
<hr />
<hr />
<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Type</th>
<th>Labels</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>build_info</code></td>
<td>Build and version information.</td>
<td>GAUGE</td>
<td><code>goversion</code>, <code>revision</code>, <code>type</code>, <code>version</code></td>
</tr>
<tr>
<td><code>cloudflared_config_local_config_pushes</code></td>
<td>Number of local configuration pushes to Cloudflare.</td>
<td>COUNTER</td>
<td></td>
</tr>
<tr>
<td><code>cloudflared_config_local_config_pushes_errors</code></td>
<td>Number of errors that occurred during local configuration pushes.</td>
<td>COUNTER</td>
<td></td>
</tr>
<tr>
<td><code>cloudflared_orchestration_config_version</code></td>
<td>Configuration version.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>cloudflared_tcp_active_sessions</code></td>
<td>Concurrent number of TCP sessions that are being proxied to any origin.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>cloudflared_tcp_total_sessions</code></td>
<td>Total number of TCP sessions that have been proxied to any origin.</td>
<td>COUNTER</td>
<td></td>
</tr>
<tr>
<td><code>cloudflared_tunnel_active_streams</code></td>
<td>Total number of active streams.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>cloudflared_tunnel_concurrent_requests_per_tunnel</code></td>
<td>Concurrent number of requests proxied through each tunnel.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>cloudflared_tunnel_ha_connections</code></td>
<td>Number of active HA connections.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>cloudflared_tunnel_request_errors</code></td>
<td>Number of errors proxying to origin.</td>
<td>COUNTER</td>
<td></td>
</tr>
<tr>
<td><code>cloudflared_tunnel_server_locations</code></td>
<td>Where each tunnel is connected to. <code>1</code> means current location, <code>0</code> means previous locations.</td>
<td>GAUGE</td>
<td><code>connection_id</code>, <code>edge_location</code></td>
</tr>
<tr>
<td><code>cloudflared_tunnel_timer_retries</code></td>
<td>Unacknowledged heart beats count.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>cloudflared_tunnel_total_requests</code></td>
<td>Number of requests proxied through all tunnels.</td>
<td>COUNTER</td>
<td></td>
</tr>
<tr>
<td><code>cloudflared_tunnel_tunnel_authenticate_success</code></td>
<td>Number of successful tunnel authentication events.</td>
<td>COUNTER</td>
<td></td>
</tr>
<tr>
<td><code>cloudflared_tunnel_tunnel_register_success</code></td>
<td>Number of successful tunnel registrations.</td>
<td>COUNTER</td>
<td><code>rpcName</code></td>
</tr>
<tr>
<td><code>cloudflared_udp_active_sessions</code></td>
<td>Concurrent number of UDP sessions that are being proxied to any origin.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>cloudflared_udp_total_sessions</code></td>
<td>Total number of UDP sessions that have been proxied to any origin.</td>
<td>COUNTER</td>
<td></td>
</tr>
<tr>
<td><code>coredns_panics_total</code></td>
<td>Number of panics.</td>
<td>COUNTER</td>
<td></td>
</tr>
<tr>
<td><code>quic_client_closed_connections</code></td>
<td>Number of connections that have been closed.</td>
<td>COUNTER</td>
<td></td>
</tr>
<tr>
<td><code>quic_client_latest_rtt</code></td>
<td>Latest round-trip time (RTT) measured on a connection.</td>
<td>GAUGE</td>
<td><code>conn_index</code></td>
</tr>
<tr>
<td><code>quic_client_lost_packets</code></td>
<td>Number of packets that have been lost from a connection.</td>
<td>COUNTER</td>
<td><code>conn_index</code>, <code>reason</code></td>
</tr>
<tr>
<td><code>quic_client_min_rtt</code></td>
<td>Lowest RTT measured on a connection in ms.</td>
<td>GAUGE</td>
<td><code>conn_index</code></td>
</tr>
<tr>
<td><code>quic_client_packet_too_big_dropped</code></td>
<td>Number of packets received from origin that are too big to send to Cloudflare and are dropped as a result.</td>
<td>COUNTER</td>
<td></td>
</tr>
<tr>
<td><code>quic_client_smoothed_rtt</code></td>
<td>Smoothed RTT calculated for a connection in ms.</td>
<td>GAUGE</td>
<td><code>conn_index</code></td>
</tr>
<tr>
<td><code>quic_client_total_connections</code></td>
<td>Number of connections initiated. For all QUIC metrics, client means the side initiating the connection.</td>
<td>COUNTER</td>
<td></td>
</tr>
</tbody>
</table>
<h3 id="prometheus-metrics">Prometheus metrics</h3>
<hr />
<hr />
<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Type</th>
<th>Labels</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>promhttp_metric_handler_requests_in_flight</code></td>
<td>Current number of scrapes being served.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>promhttp_metric_handler_requests_total</code></td>
<td>Total number of scrapes by HTTP status code.</td>
<td>COUNTER</td>
<td><code>code</code></td>
</tr>
</tbody>
</table>
<h3 id="go-runtime-metrics">Go runtime metrics</h3>
<hr />
<hr />
<table>
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Type</th>
<th>Labels</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>go_gc_duration_seconds</code></td>
<td>A summary of the pause duration of garbage collection cycles.</td>
<td>SUMMARY</td>
<td></td>
</tr>
<tr>
<td><code>go_goroutines</code></td>
<td>Number of goroutines that currently exist.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>go_info</code></td>
<td>Information about the Go environment.</td>
<td>GAUGE</td>
<td><code>version</code></td>
</tr>
<tr>
<td><code>go_memstats_alloc_bytes</code></td>
<td>Number of bytes allocated and still in use.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>go_memstats_alloc_bytes_total</code></td>
<td>Total number of bytes allocated, even if freed.</td>
<td>COUNTER</td>
<td></td>
</tr>
<tr>
<td><code>go_memstats_buck_hash_sys_bytes</code></td>
<td>Number of bytes used by the profiling bucket hash table.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>go_memstats_frees_total</code></td>
<td>Total number of frees.</td>
<td>COUNTER</td>
<td></td>
</tr>
<tr>
<td><code>go_memstats_gc_sys_bytes</code></td>
<td>Number of bytes used for garbage collection system metadata.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>go_memstats_heap_alloc_bytes</code></td>
<td>Number of heap bytes allocated and still in use.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>go_memstats_heap_idle_bytes</code></td>
<td>Number of heap bytes waiting to be used.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>go_memstats_heap_inuse_bytes</code></td>
<td>Number of heap bytes that are in use.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>go_memstats_heap_objects</code></td>
<td>Number of allocated objects.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>go_memstats_heap_released_bytes</code></td>
<td>Number of heap bytes released to OS.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>go_memstats_heap_sys_bytes</code></td>
<td>Number of heap bytes obtained from system.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>go_memstats_last_gc_time_seconds</code></td>
<td>Number of seconds since 1970 of last garbage collection.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>go_memstats_lookups_total</code></td>
<td>Total number of pointer lookups.</td>
<td>COUNTER</td>
<td></td>
</tr>
<tr>
<td><code>go_memstats_mallocs_total</code></td>
<td>Total number of mallocs.</td>
<td>COUNTER</td>
<td></td>
</tr>
<tr>
<td><code>go_memstats_mcache_inuse_bytes</code></td>
<td>Number of bytes in use by mcache structures.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>go_memstats_mcache_sys_bytes</code></td>
<td>Number of bytes used for mcache structures obtained from system.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>go_memstats_mspan_inuse_bytes</code></td>
<td>Number of bytes in use by mspan structures.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>go_memstats_mspan_sys_bytes</code></td>
<td>Number of bytes used for mspan structures obtained from system.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>go_memstats_next_gc_bytes</code></td>
<td>Number of heap bytes when next garbage collection will take place.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>go_memstats_other_sys_bytes</code></td>
<td>Number of bytes used for other system allocations.</td>
<td>GAUGE</td>
<td></td>
</tr>
<tr>
<td><code>go_memstats_stack_inuse_bytes</code></td>
<td>Number of bytes in use by the stack allocator.</td>
<td>GAUGE</td>
<td></td>
</tr>
</tbody>
</table>
