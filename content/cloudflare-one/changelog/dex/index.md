<h2 id="2026-07-09">2026-07-09</h2>

<strong>Wi-Fi signal and network performance analytics for Cloudflare One Client devices</strong>

<p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into device, network, and application performance across your Cloudflare SASE deployment.</p>
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


<h2 id="2026-04-29">2026-04-29</h2>

<strong>Digital experience tests to authenticated resources and enhanced configuration</strong>

<p><a href="/cloudflare-one/insights/dex/tests/">Digital experience tests</a> now support testing applications protected by Cloudflare Access or third-party authentication. All authentication secrets are managed via <a href="/secrets-store/">Cloudflare Secret Store</a>.</p>
<p>Digital experience tests also have enhanced configuration options including:</p>
<ul>
<li>New HTTP methods (DELETE, PATCH, POST, PUT)</li>
<li>Secret Store headers, custom plain text headers, and custom request bodies</li>
<li>Advanced settings: follow redirects, response bodies, response headers, and allow untrusted certificates</li>
</ul>
<p><img src="/assets/upstream/images/changelog/dex/dex_test_auth_config.png" alt="Digital experience test configuration for Cloudflare Access applications" />
<img src="/assets/upstream/images/changelog/dex/dex_test_enhanced_config.png" alt="Digital experience enhanced test configuration" /></p>


<h2 id="2026-04-28">2026-04-28</h2>

<strong>Internet outage notifications for devices</strong>

<p><a href="/cloudflare-one/insights/dex/">Digital Experience</a> will display a dashboard notification when an Internet outage or traffic anomaly may impact a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> device based on its geographic location or network connection.</p>
<p>This Internet outage and traffic anomaly data is pulled from <a href="https://radar.cloudflare.com/">Cloudflare Radar</a>. All Internet outage and traffic anomaly observations can be viewed in the <a href="https://radar.cloudflare.com/outage-center">Radar Outage Center</a>.</p>
<p><img src="/assets/upstream/images/changelog/dex/dex_radar_ux_notification.png" alt="Digital Experience Monitoring dashboard notification for Internet outage impacting Cloudflare One Client devices" />
<img src="/assets/upstream/images/changelog/dex/dex_radar_analytics.png" alt="Digital Experience Monitoring dashboard analytics for Internet outage impacting Cloudflare One Client devices" /></p>


<h2 id="2026-04-28-1">2026-04-28</h2>

<strong>Cloudflare One Client speed tests</strong>

<p>IT teams can now remotely run speed tests from the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> to Cloudflare's network edge.</p>
<p>Each speed test includes the following metrics:</p>
<ul>
<li>Internet speed: download and upload throughput</li>
<li>Latency: download, upload, unloaded latency, and jitter</li>
<li>Network quality score: video streaming, webchat/real-time communication (RTC)</li>
</ul>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Digital experience</strong> &gt; <strong>Diagnostics</strong> and select <strong>Run diagnostics</strong> to use the feature today.</p>
<p><img src="/assets/upstream/images/changelog/dex/dex_speed_test.png" alt="Cloudflare One client speed test result" /></p>


<h2 id="2026-04-15">2026-04-15</h2>

<strong>Last seen timestamp for Cloudflare One Client devices is more consistent</strong>

<p>The last seen timestamp for <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> devices is now more consistent across the dashboard. IT teams will see more consistent information about the most recent client event between a device and Cloudflare's network.</p>


<h2 id="2026-02-19">2026-02-19</h2>

<strong>DEX Supports EU Customer Metadata Boundary</strong>

<p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into <a href="/warp-client/">WARP</a> device connectivity and performance to any internal or external application.</p>
<p>Now, all DEX logs are fully compatible with Cloudflare's <a href="/data-localization/metadata-boundary/">Customer Metadata Boundary</a> (CMB) setting for the 'EU' (European Union), which ensures that DEX logs will not be stored outside the 'EU' when the option is configured.</p>
<p>If a Cloudflare One customer using DEX enables CMB 'EU', they will not see any DEX data in the Cloudflare One dashboard. Customers can ingest DEX data via <a href="/logs/logpush/">LogPush</a>, and build their own analytics and dashboards.</p>
<p>If a customer enables CMB in their account, they will see the following message in the Digital Experience dashboard: &quot;DEX data is unavailable because Customer Metadata Boundary configuration is on. Use Cloudflare LogPush to export DEX datasets.&quot;</p>
<p><img src="/assets/upstream/images/changelog/dex/dex_supports_cmb.png" alt="Digital Experience Monitoring message when Customer Metadata Boundary for the EU is enabled" /></p>


<h2 id="2025-11-12">2025-11-12</h2>

<strong>DEX Logpush jobs</strong>

<p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into WARP device metrics, connectivity, and network performance across your Cloudflare SASE deployment.</p>
<p>We've released four new WARP and DEX device data sets that can be exported via <a href="/cloudflare-one/insights/logs/logpush/">Cloudflare Logpush</a>. These Logpush data sets can be exported to R2, a cloud bucket, or a SIEM to build a customized logging and analytics experience.</p>
<ol>
<li><a href="/logs/logpush/logpush-job/datasets/account/dex_application_tests/">DEX Application Tests</a></li>
<li><a href="/logs/logpush/logpush-job/datasets/account/dex_device_state_events/">DEX Device State Events</a></li>
<li><a href="/logs/logpush/logpush-job/datasets/account/warp_config_changes/">WARP Config Changes</a></li>
<li><a href="/logs/logpush/logpush-job/datasets/account/warp_toggle_changes/">WARP Toggle Changes</a></li>
</ol>
<p>To create a new DEX or WARP Logpush job, customers can go to the account level of the Cloudflare dashboard &gt; Analytics &amp; Logs &gt; Logpush to get started.</p>
<p><img src="/assets/upstream/images/changelog/dex/dex_logpush_datasets.png" alt="DEX logpush job creation dashboard" /></p>


<h2 id="2025-08-29">2025-08-29</h2>

<strong>DEX MCP Server</strong>

<p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into device connectivity and performance across your Cloudflare SASE deployment.</p>
<p>We've released an MCP server <a href="https://cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/">(Model Context Protocol)</a> for DEX.</p>
<p>The DEX MCP server is an AI tool that allows customers to ask a question like, &quot;Show me the connectivity and performance metrics for the device used by carly‌@acme.com&quot;, and receive an answer that contains data from the DEX API.</p>
<p>Any Cloudflare One customer using a Free, Pay-as-you-go, or Enterprise account can access the DEX MCP Server. This feature is available to everyone.</p>
<p>Customers can test the new DEX MCP server in less than one minute. To learn more, read the <a href="/cloudflare-one/insights/dex/dex-mcp-server/">DEX MCP server documentation</a>.</p>


<h2 id="2025-03-07">2025-03-07</h2>

<strong>Cloudflare One Agent now supports Endpoint Monitoring</strong>

<p><a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> provides visibility into device, network, and application performance across your Cloudflare SASE deployment. The latest release of the Cloudflare One agent (v2025.1.861) now includes device endpoint monitoring capabilities
to provide deeper visibility into end-user device performance which can be analyzed directly from the dashboard.</p>
<p>Device health metrics are now automatically collected, allowing administrators to:</p>
<ul>
<li>View the last network a user was connected to</li>
<li>Monitor CPU and RAM utilization on devices</li>
<li>Identify resource-intensive processes running on endpoints</li>
</ul>
<p><img src="/assets/upstream/images/changelog/dex/cloudflare-one-agent-health-monitoring.gif" alt="Device endpoint monitoring dashboard" /></p>
<p>This feature complements existing DEX features like <a href="/cloudflare-one/insights/dex/tests/">synthetic application monitoring</a> and <a href="/cloudflare-one/insights/dex/tests/traceroute/">network path visualization</a>, creating a comprehensive troubleshooting workflow that connects application performance with device state.</p>
<p>For more details refer to our <a href="/cloudflare-one/insights/dex/">DEX</a> documentation.</p>


<h2 id="2025-01-24">2025-01-24</h2>
<p><strong>IP visibility</strong></p>
<p><a href="/cloudflare-one/insights/dex/ip-visibility/">IP visibility</a> enables admins to inspect the different IP addresses associated with an end-user device. IP types available for review on the Cloudflare dashboard include: the device's private IP, the public IP assigned to the device by the ISP, and the router's (that the device is connected to) private IP.</p>
<h2 id="2024-12-19">2024-12-19</h2>
<p><strong>Remote captures</strong></p>
<p>Admins can now collect packet captures (PCAPs) and WARP diagnostic logs from end-user devices. For more information, refer to <a href="/cloudflare-one/insights/dex/diagnostics/client-packet-capture/">Remote captures</a>.</p>
<h2 id="2024-05-20">2024-05-20</h2>
<p><strong>Last seen ISP</strong></p>
<p>Admins can view the last ISP seen for a device by going to <strong>My Team</strong> &gt; <strong>Devices</strong>. Requires setting up a <a href="/cloudflare-one/insights/dex/tests/traceroute/">traceroute test</a>.</p>
<h2 id="2024-05-13">2024-05-13</h2>
<p><strong>DEX alerts</strong></p>
<p>Admins can now set <a href="/cloudflare-one/insights/dex/notifications/">DEX alerts</a> using <a href="/notifications/">Cloudflare Notifications</a>. Three new DEX alert types:</p>
<ul>
<li>Device connectivity anomaly</li>
<li>Test latency</li>
<li>Test low availability</li>
</ul>


