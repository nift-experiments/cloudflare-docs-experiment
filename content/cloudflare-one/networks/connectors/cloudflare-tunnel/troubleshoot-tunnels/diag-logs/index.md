<p>Cloudflare Tunnel generates a set of diagnostic logs that can be used to troubleshoot issues with <code>cloudflared</code>. A diagnostic report collects data from a single instance of <code>cloudflared</code> running on the local machine.</p>
<h2 id="get-diagnostic-logs">Get diagnostic logs</h2>
<p>The steps for getting diagnostic logs depend on your <code>cloudflared</code> deployment environment.</p>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li><code>cloudflared</code> version 2024.12.2 or later installed on the host</li>
</ul>
<h3 id="host-environment">Host environment</h3>
<p>These instructions apply to remotely-managed and locally-managed tunnels running directly on the host machine.</p>
<ol>
<li>(Linux only) To include network diagnostics in the logs, allow the <code>cloudflared</code> user to create RAW and PACKET sockets without root permissions:</li>
</ol>
<pre><code class="language-sh">sudo setcap cap_net_raw+ep /usr/bin/traceroute &amp;&amp; sudo setcap cap_net_raw+ep /usr/bin/traceroute&#10;</code></pre>
<p>If you do not set <code>cap_net_raw</code>, then traceroute data will be unavailable.</p>
<ol start="2">
<li>Get diagnostic logs:</li>
</ol>
<pre><code class="language-sh">cloudflared tunnel diag&#10;</code></pre>
<p>If multiple instances of <code>cloudflared</code> are running on the same host, specify the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/metrics/#configure-the-metrics-server-address">metrics server IP and port</a> for the instance you want to diagnose. For example:</p>
<pre><code class="language-sh">cloudflared tunnel diag --metrics 127.0.0.1:20241&#10;</code></pre>
<p>This command will output the status of each diagnostic task and place a <code>cloudflared-diag-YYYY-MM-DDThh-mm-ss.zip</code> file in your working directory.</p>
<h3 id="docker">Docker</h3>
<p><code>cloudflared</code> reads diagnostic data from the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/metrics/">tunnel metrics server</a>. To get diagnostic logs, the metrics server must be exposed from the Docker container and reachable from the host machine.</p>
<ol>
<li>
<p>Determine the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/metrics/#default-metrics-server-address">metrics server port</a> for the <code>cloudflared</code> instance running in Docker.</p>
</li>
<li>
<p>Ensure the container is deployed with port forwarding enabled. The diagnostic feature will request information from the Docker instance using local port <code>20241</code>, therefore you should forward port <code>20241</code> to the container port obtained in Step 1:</p>
</li>
</ol>
<pre><code class="language-sh">docker run -d -p 20241:&lt;metrics_port&gt; docker.io/cloudflare/cloudflared tunnel ...&#10;</code></pre>
<ol start="3">
<li>Verify that you can reach the metrics server address from the Docker host environment:</li>
</ol>
<pre><code class="language-sh">curl localhost:20241/diag/tunnel&#10;</code></pre>
<p>This command should return a JSON:</p>
<pre><code class="language-json">{&#10;  &quot;tunnelID&quot;: &quot;ef96b330-a7f5-4bce-a00e-827ce5be077f&quot;,&#10;  &quot;connectorID&quot;: &quot;d236670a-9f74-422f-adf1-030f5c5f0523&quot;,&#10;  &quot;connections&quot;: [&#10;    { &quot;isConnected&quot;: true, &quot;protocol&quot;: 1, &quot;edgeAddress&quot;: &quot;198.41.192.167&quot;},&#10;    {&quot;isConnected&quot;: true, &quot;protocol&quot;: 1, &quot;edgeAddress&quot;: &quot;198.41.200.113&quot;, &quot;index&quot;: 1},&#10;    {&quot;isConnected&quot;: true, &quot;protocol&quot;: 1, &quot;edgeAddress&quot;: &quot;198.41.192.47&quot;, &quot;index&quot;: 2},&#10;    {&quot;isConnected&quot;: true, &quot;protocol&quot;: 1, &quot;edgeAddress&quot;: &quot;198.41.200.73&quot;, &quot;index&quot;: 3}&#10;  ],&#10;  &quot;icmp_sources&quot;: [&quot;192.168.1.243&quot;, &quot;fe80::c59:bd4a:e815:ed6&quot;]&#10;}&#10;</code></pre>
<ol start="4">
<li>Run the diagnostic using the Docker container ID:</li>
</ol>
<pre><code class="language-sh">cloudflared tunnel diag --diag-container-id=&lt;containerID&gt;&#10;</code></pre>
<p>Alternatively, you can specify the container's name instead of its ID:</p>
<pre><code class="language-sh">cloudflared tunnel diag --diag-container-id=&lt;containerName&gt;&#10;</code></pre>
<p>Running the diagnostic command with the container ID allows <code>cloudflared</code> to collect information from the Docker environment such as logs and container details.</p>
<p>This command will output the status of each diagnostic task and place a <code>cloudflared-diag-YYYY-MM-DDThh-mm-ss.zip</code> file in your working directory.</p>
<h3 id="kubernetes">Kubernetes</h3>
<p>The diagnostic feature will request data from the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/metrics/">tunnel metrics server</a> using ports <code>20241</code> to <code>20245</code>. You will need to use port forwarding to allow the local <code>cloudflared</code> instance to connect to the metrics server on one of these ports.</p>
<ol>
<li>
<p>Determine the tunnel's <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/metrics/#default-metrics-server-address">metrics server port</a>.</p>
</li>
<li>
<p>Enable port forwarding:</p>
</li>
</ol>
<pre><code class="language-sh">kubectl port-forward &lt;pod&gt; &lt;diagnostic_port&gt;:&lt;metrics_port&gt;&#10;</code></pre>
<ul>
<li><code>&lt;pod&gt;</code>: Name of the pod where the tunnel is running</li>
<li><code>&lt;diagnostic_port&gt;</code> is any local port in the range <code>20241</code> to <code>20245</code>.</li>
<li><code>&lt;metrics_port&gt;</code> is the Kubernetes pod port for the <code>cloudflared</code> instance you want to diagnose (obtained in Step 1).</li>
</ul>
<p>For example, if you set the metrics server address to <code>0.0.0.0:12345</code>:</p>
<pre><code class="language-sh">kubectl port-forward cloudflared-6d4897585b-r8kfz 20244:12345&#10;</code></pre>
<p>Connections made to local port <code>20244</code> are forwarded to port <code>12345</code> of the pod that is running the tunnel.</p>
<ol start="3">
<li>Run the diagnostic:</li>
</ol>
<pre><code class="language-sh">cloudflared tunnel diag --diag-pod-id=&lt;podID&gt;&#10;</code></pre>
<p>If the pod has multiple applications/services running and <code>cloudflared</code> is not the first in the pod, you must specify either the container ID or name:</p>
<pre><code class="language-sh">cloudflared tunnel diag --diag-pod-id=&lt;podID&gt; --diag-container-id=&lt;containerName&gt;&#10;</code></pre>
<p>This command will output the status of each diagnostic task and place a <code>cloudflared-diag-YYYY-MM-DDThh-mm-ss.zip</code> file in your working directory.</p>
<h2 id="cloudflared-diag-files">cloudflared-diag files</h2>
<p>The <code>cloudflared-diag-YYYY-MM-DDThh-mm-ss.zip</code> archive contains the files listed below. The data in a file either applies to the <code>cloudflared</code> instance being diagnosed (<code>diagnosee</code>) or the instance that triggered the diagnosis (<code>diagnoser</code>). For example, if your tunnel is running in a Docker container, the diagnosee is the Docker instance and the diagnoser is the host instance.</p>
<table>
<thead>
<tr>
<th>File name</th>
<th>Description</th>
<th>Instance</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>cli-configuration.json</code></td>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/">Tunnel run parameters</a> used when starting the tunnel</td>
<td>diagnosee</td>
</tr>
<tr>
<td><code>cloudflared_logs.txt</code></td>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">Tunnel log file</a><sup><a href="#footnote-cloudflare-one-tunnel-diagnostics-tunnel-diag-file-mdx-1">1</a></sup></td>
<td>diagnosee</td>
</tr>
<tr>
<td><code>configuration.json</code></td>
<td>Tunnel configuration parameters</td>
<td>diagnosee</td>
</tr>
<tr>
<td><code>goroutine.pprof</code></td>
<td>goroutine profile made available by <code>pprof</code></td>
<td>diagnosee</td>
</tr>
<tr>
<td><code>heap.pprof</code></td>
<td>heap profile made available by <code>pprof</code></td>
<td>diagnosee</td>
</tr>
<tr>
<td><code>metrics.txt</code></td>
<td>Snapshot of <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/metrics/#available-metrics">Tunnel metrics</a> at the time of diagnosis</td>
<td>diagnosee</td>
</tr>
<tr>
<td><code>network.txt</code></td>
<td>JSON traceroutes to Cloudflare's global network using IPv4 and IPv6</td>
<td>diagnoser</td>
</tr>
<tr>
<td><code>raw-network.txt</code></td>
<td>Raw traceroutes to Cloudflare's global network using IPv4 and IPv6</td>
<td>diagnoser</td>
</tr>
<tr>
<td><code>systeminformation.json</code></td>
<td>Operating system information and resource usage</td>
<td>diagnosee</td>
</tr>
<tr>
<td><code>task-result.json</code></td>
<td>Result of each diagnostic task</td>
<td>diagnoser</td>
</tr>
<tr>
<td><code>tunnelstate.json</code></td>
<td>Tunnel connections at the time of diagnosis</td>
<td>diagnosee</td>
</tr>
</tbody>
</table>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-cloudflare-one-tunnel-diagnostics-tunnel-diag-file-mdx-1">If the log file is blank, you may need to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/#view-logs-on-the-server">set `--loglevel` to `debug`</a> when you start the tunnel. The `--loglevel` parameter is only required if you ran the tunnel from the CLI using a `cloudflared tunnel run` command. It is not necessary if the tunnel runs as a Linux/macOS service or runs in Docker/Kubernetes.</li></ol></section>
