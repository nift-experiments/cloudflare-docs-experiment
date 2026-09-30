<p>Speed tests allow administrators to remotely measure network performance from end-user devices running the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One client</a>. Each test runs from the client to Cloudflare's network edge and reports metrics for internet speed, latency, and network quality.</p>
<p>Speed tests help IT teams:</p>
<ul>
<li>Objectively measure network performance with the Cloudflare One client turned on.</li>
<li>Identify performance bottlenecks affecting specific users, devices, or locations.</li>
<li>Respond to user reports of slow connectivity with concrete data.</li>
</ul>
<details class="nb-details"><summary>Feature compatibility</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4975.md")
</div></details>
<p>To run a speed test from a device:</p>
<ol>
<li>In <a href="https://dash.cloudflare.com/one">Zero Trust</a>, go to <strong>Insights</strong> &gt; <strong>Digital experience</strong> &gt; <strong>Diagnostics</strong>.</li>
<li>Select <strong>Run diagnostics</strong>.</li>
<li>Search for a device by user email, device name, or device ID.</li>
<li>Select the device, then select <strong>Device speed test</strong>.</li>
</ol>
<p>The test runs in the background on the selected device. Results appear in the diagnostics view once the test completes.</p>
<h2 id="speed-test-metrics">Speed test metrics</h2>
<p>Each speed test reports the following metrics:</p>
<h3 id="internet-speed">Internet speed</h3>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Download throughput</td>
<td>The rate at which data is received by the device from Cloudflare's network edge, measured in Mbps.</td>
</tr>
<tr>
<td>Upload throughput</td>
<td>The rate at which data is sent from the device to Cloudflare's network edge, measured in Mbps.</td>
</tr>
</tbody>
</table>
<h3 id="latency">Latency</h3>
<table>
<thead>
<tr>
<th>Metric</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Download latency</td>
<td>The round-trip time measured during an active download, reflecting latency under load.</td>
</tr>
<tr>
<td>Upload latency</td>
<td>The round-trip time measured during an active upload, reflecting latency under load.</td>
</tr>
<tr>
<td>Unloaded latency</td>
<td>The baseline round-trip time measured when no significant data transfer is occurring. This reflects the inherent latency of the connection.</td>
</tr>
<tr>
<td>Jitter</td>
<td>The variation in latency over time. High jitter can cause inconsistent performance in real-time applications.</td>
</tr>
</tbody>
</table>
<h3 id="network-quality-score">Network quality score</h3>
<p>Network quality scores estimate the end-user experience for common application types based on the measured speed and latency values.</p>
<table>
<thead>
<tr>
<th>Score</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Video streaming</td>
<td>Rates the connection quality for video streaming applications based on throughput and latency.</td>
</tr>
<tr>
<td>Video streaming</td>
<td>Estimates the connection quality for video streaming applications based on throughput and latency.</td>
</tr>
<tr>
<td>Web chat / RTC</td>
<td>Estimates the connection quality for real-time communication applications such as video calls and VoIP.</td>
</tr>
</tbody>
</table>
