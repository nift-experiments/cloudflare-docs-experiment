<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>July 9, 2026</time><h2 id="post-title">Wi-Fi signal and network performance analytics for Cloudflare One Client devices</h2>
<div class="changelog-badges"><span>dex</span></div><div class="changelog-body"><p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into device, network, and application performance across your Cloudflare SASE deployment.</p>
<p>The <strong>Device Monitoring</strong> page now analyzes hardware and network data between a Cloudflare One Client device and Cloudflare's edge, so you can diagnose connectivity and performance issues. Previously, this data was only available in raw DEX Device State Event logs, which required you to build your own analytics to interpret it.</p>
<p><img src="/assets/upstream/images/changelog/dex/dex-device-monitoring-summary.png" alt="Device Monitoring summary with connection status, connection mode, Wi-Fi signal strength, traffic performance, and device health" /></p>
<p>A summary at the top of the page shows the health of each category at a glance, using <strong>Good</strong>, <strong>Fair</strong>, and <strong>Poor</strong> labels:</p>
<ul>
<li><strong>Connection</strong> — connection status, Cloudflare One Client mode, and tunnel type over time</li>
<li><strong>Wi-Fi signal strength</strong> — signal measured in dBm over time, with thresholds that flag a weak signal</li>
<li><strong>Traffic performance</strong> — upstream and downstream performance, including network throughput on the active interface</li>
<li><strong>Device health</strong> — hardware metrics such as CPU, memory, and disk</li>
</ul>
<p><img src="/assets/upstream/images/changelog/dex/dex-device-monitoring-wifi-network.png" alt="Wi-Fi signal strength and network throughput charts on the Device Monitoring page" /></p>
<p>You can filter by category and adjust the time range to correlate a device's metrics with a user's reported issue.</p>
<p>These analytics are available to all Cloudflare One customers at no additional cost.</p>
<p>To learn more, refer to the <a href="/cloudflare-one/insights/dex/monitoring/">DEX monitoring documentation</a>.</p>
</div></article></div>
