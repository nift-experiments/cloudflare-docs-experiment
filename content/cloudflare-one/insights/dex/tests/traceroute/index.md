<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/4973.md")
</div></details>
<p>A traceroute test measures the network path of an IP packet from an end-user device to a server. The packet passes through a series of intermediate routers — each called a &quot;hop&quot; — and the test records the response time and packet loss at each one. You can use the results to troubleshoot network issues by identifying which hop along the path is causing increased latency or dropped packets.</p>
<h2 id="create-a-test">Create a test</h2>
<p>To set up a traceroute test for an application:</p>
<ol>
<li>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Insights</strong> &gt; <strong>Digital experience</strong>.</li>
<li>Select the <strong>Tests</strong> tab.</li>
<li>Select <strong>Add a Test</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Name</strong>: Enter any name for the test.</li>
<li><strong>Target</strong>: Enter the IP address of the server you want to test (for example, <code>192.0.2.0</code>). You can test either a public-facing endpoint or a private endpoint you have connected to Cloudflare.</li>
<li><strong>Source device profiles</strong>: (Optional) Select the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profiles</a> that you want to run the test on. A device profile defines Cloudflare One Client settings for a specific set of devices in your organization. If no profiles are selected, the test will run on all supported devices connected to your Zero Trust organization.</li>
<li><strong>Test type</strong>: Select <em>Traceroute</em>.</li>
<li><strong>Test frequency</strong>: Specify how often the test will run. Input a minute value between 5 and 60.</li>
</ul>
</li>
<li>Select <strong>Add test</strong>.</li>
</ol>
<p>Next, <a href="/cloudflare-one/insights/dex/tests/view-results/">view the results</a> of your test.</p>
<h2 id="test-results">Test results</h2>
<p>A traceroute test measures the following data:</p>
<table>
<thead>
<tr>
<th>Data</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Network path</td>
<td>IP address, average response time, and packet loss for each hop (router) between the device and the target. This is the core traceroute data — it maps the route your traffic takes.</td>
</tr>
<tr>
<td>Round trip time</td>
<td>Time, in milliseconds, between sending out a packet and receiving a response from the target. This is the end-to-end latency measurement.</td>
</tr>
<tr>
<td>Number of hops</td>
<td>Number of routers encountered between the device and the target.</td>
</tr>
<tr>
<td>Packet loss</td>
<td>Percentage of IP packets that failed to receive a response.</td>
</tr>
<tr>
<td>Availability</td>
<td>Percentage of tests where at least one packet reached the destination. A value below 100% means the destination was completely unreachable during some test runs.</td>
</tr>
<tr>
<td>Last seen ISP</td>
<td>The Internet Service Provider that is managing the connection from the device to Cloudflare. (Only available on macOS and Windows.) <br/> <br/> DEX looks up the IP address of the ISP in a geolocation database and returns the corresponding <a href="https://www.cloudflare.com/learning/network-layer/what-is-an-autonomous-system/">ASO (Autonomous System Organization) and ASN (Autonomous System Number)</a>. If the ASO and ASN are <code>Unknown</code>, it means this information is unavailable in the geolocation data provider.</td>
</tr>
</tbody>
</table>
<h2 id="export-dex-application-test-logs">Export DEX application test logs</h2>
<p>You can use <a href="/cloudflare-one/insights/logs/logpush/">Logpush</a> to export <a href="/logs/logpush/logpush-job/datasets/account/dex_application_tests/">DEX application test</a> data to <a href="/r2/">R2</a> (Cloudflare's object storage), a third-party cloud storage bucket, or a Security Information and Event Management (SIEM) tool. This is useful if you need to retain test data beyond the <a href="/cloudflare-one/insights/logs/#log-retention">7-day log retention period</a> or correlate DEX data with other log sources.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/cloudflare-one/insights/dex/rules/">DEX rules</a> - Define which users or groups a test applies to, using selectors such as user email, user group, operating system, or managed network.</li>
</ul>
