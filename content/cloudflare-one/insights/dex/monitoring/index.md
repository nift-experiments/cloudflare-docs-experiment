---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/insights/dex/monitoring/
  description: Device monitoring in Zero Trust analytics.
  full_title: Device monitoring · Cloudflare One docs
  head_html: <title>Device monitoring · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Device monitoring in Zero Trust analytics."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/insights/dex/monitoring/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/insights/dex/monitoring/index.md"><meta property="og:title" content="Device monitoring · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Device monitoring in Zero Trust analytics."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/insights/dex/monitoring/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/insights/dex/monitoring/#page","headline":"Device monitoring \u00b7 Cloudflare One docs","description":"Device monitoring in Zero Trust analytics.","url":"https://developers.cloudflare.com/cloudflare-one/insights/dex/monitoring/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/insights/dex/monitoring/
  schema: 1
---
<p>Monitor performance and network status for your organization's <a href="/cloudflare-one/insights/dex/monitoring/#fleet-status">fleet</a> (all devices with the Cloudflare One Client installed and connected to your Zero Trust organization) or individual <a href="/cloudflare-one/insights/dex/monitoring/#device-monitoring">user devices</a>.</p>
<p>Network and device performance data helps IT administrators troubleshoot performance issues, investigate network connectivity problems, and monitor device health.</p>
<h2 id="device-overview">Device overview</h2>
<p>A fleet is a collection of user devices. All devices in a fleet have the Cloudflare One Client installed and are connected to a <a href="/cloudflare-one/setup/#2-create-a-zero-trust-organization">Cloudflare Zero Trust organization</a>.</p>
<p>To view fleet status:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Insights</strong> &gt; <strong>Digital experience</strong>.</li>
<li>Review the information under <strong>Live analytics</strong>.</li>
</ol>
<h3 id="view-metrics">View metrics</h3>
<p>The <strong>Device overview</strong> tab shows real-time and historical connectivity metrics for all devices in your organization.</p>
<p>To view analytics on a per-device level, go to <a href="/cloudflare-one/insights/dex/monitoring/#device-monitoring">Device monitoring</a>.</p>
<h3 id="available-metrics">Available metrics</h3>
<ul>
<li>
<p><strong>Devices connected by colo</strong>: Number of devices connected to a given <a href="https://www.cloudflarestatus.com/">Cloudflare data center</a>.</p>
</li>
<li>
<p><strong>Connectivity status</strong>: Percentage of devices in a given Cloudflare One Client state.</p>
</li>
</ul>
<table>
<thead>
<tr>
<th>Status</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Connected</td>
<td>The Cloudflare One Client has successfully established a connection to the Cloudflare global network.</td>
</tr>
<tr>
<td>Disconnected</td>
<td>The Cloudflare One Client has been intentionally or unintentionally disconnected from the Cloudflare global network.</td>
</tr>
<tr>
<td>Paused</td>
<td>A user or administrator has taken an explicit action to temporarily turn off WARP, for example by entering an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-admin-override-codes">admin override code</a>. Paused clients will <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#auto-connect">auto-connect</a> after a timeout period.</td>
</tr>
<tr>
<td>Connecting</td>
<td>The Cloudflare One Client is pending connection, but is actively trying to establish a connection to the Cloudflare global network.</td>
</tr>
</tbody>
</table>
<ul>
<li>
<p><strong>Mode</strong>: <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/">Client mode</a> deployed on the device.</p>
</li>
<li>
<p><strong>Colo</strong>: Percentage of devices connected to a given Cloudflare data center.</p>
</li>
<li>
<p><strong>Platform</strong>: Operating system of the device.</p>
</li>
<li>
<p><strong>Major Version</strong>: Cloudflare One Client version installed on the device.</p>
</li>
<li>
<p><strong>Device Status Over Time</strong>: Cloudflare One Client connection status over the selected time period.</p>
</li>
<li>
<p><strong>Connection Methods Over Time</strong>: Client mode used by the device over the selected time period.</p>
</li>
</ul>
<h2 id="device-monitoring">Device monitoring</h2>
<p>Review network and device performance for a device enrolled in your fleet.</p>
<h3 id="view-a-device-s-performance">View a device's performance</h3>
<p>To view a device's network and device performance metrics:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Your devices</strong>.</li>
<li>Select a device &gt; <strong>View details</strong>.</li>
<li>Select the <strong>DEX</strong> tab.</li>
<li>In <strong>Device Monitoring</strong>, scroll down to <strong>Network performance</strong> and <strong>Device Performance</strong>.</li>
</ol>
<h3 id="network-and-device-performance-metrics">Network and device performance metrics</h3>
<h4 id="network-performance-metrics">Network performance metrics</h4>
<ul>
<li>
<p><strong>Unique networks over time</strong>: How many unique SSIDs (Wi-Fi network names) the device was connected to.</p>
</li>
<li>
<p><strong>Network I/O</strong>: How much data the device transferred (uploads and downloads) over the primary network interface.</p>
</li>
</ul>
<h4 id="device-performance-metrics">Device performance metrics</h4>
<ul>
<li>
<p><strong>Battery percentage and cycles</strong>: Displays battery percentage and <a href="https://support.apple.com/en-us/102888">battery cycles</a> over time. Use this metric to debug potential performance issues possibly related to battery health or power-saving measures that trigger at low-battery levels.</p>
</li>
<li>
<p><strong>CPU usage</strong>: CPU utilization over time. Use this metric to debug slow system performance due to high CPU usage.</p>
</li>
<li>
<p><strong>Memory utilization</strong>: Memory utilization over time. Use this metric to debug performance issues related to an overtaxed memory.</p>
</li>
<li>
<p><strong>Disk I/O</strong>: Displays number of disk read/write operations over time. Use this metric to debug performance errors due to heavy disk operations.</p>
</li>
</ul>
<h2 id="export-dex-device-state-event-logs">Export DEX device state event logs</h2>
<p>The log data for all <a href="/logs/logpush/logpush-job/datasets/account/dex_device_state_events/">DEX device state events</a> can be exported to <a href="/r2/">R2</a>, a cloud bucket, or a SIEM via <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a>.</p>
