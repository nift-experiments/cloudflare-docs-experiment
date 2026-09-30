<p>Cloudflare Tunnel exposes logs, metrics, and diagnostic tools to help you monitor tunnel health and resolve issues.</p>
<h2 id="tunnel-health">Tunnel health</h2>
<p>You can check your tunnel connection status in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> by going to <strong>Networking</strong> &gt; <strong>Tunnels</strong>, or by running <code>cloudflared tunnel list</code>.</p>
<div class="nb-dash-button"></div>
<table>
<thead>
<tr>
<th>Status</th>
<th>Meaning</th>
<th>Recommended Action</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Healthy</strong></td>
<td>The tunnel is active and serving traffic through four connections to the Cloudflare global network.</td>
<td>No action is required. Your tunnel is running correctly.</td>
</tr>
<tr>
<td><strong>Inactive</strong></td>
<td>The tunnel has been created (via the API or dashboard) but the <code>cloudflared</code> connector has never been run to establish a connection.</td>
<td>Install and run <code>cloudflared</code> on your origin server to connect the tunnel to Cloudflare. You can find the installation command in the Cloudflare dashboard under <strong>Networking</strong> &gt; <strong>Tunnels</strong> — select your tunnel, then on the <strong>Overview</strong> tab select <strong>Add a replica</strong>. For API-based setup, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel-api/#4-install-and-run-the-tunnel">Install and run the tunnel</a>.</td>
</tr>
<tr>
<td><strong>Down</strong></td>
<td>The tunnel was previously connected but is currently disconnected because the <code>cloudflared</code> process has stopped.</td>
<td>1. Ensure the <code>cloudflared</code> <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/local-management/as-a-service/">service</a> or process is actively running on your server. <br /> 2. Check for server-side issues, such as the machine being powered off, an application crash, or recent network changes.</td>
</tr>
<tr>
<td><strong>Degraded</strong></td>
<td>The <code>cloudflared</code> connector is running and the tunnel is serving traffic, but at least one individual connection has failed. Further degradation in <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">tunnel availability</a> could risk the tunnel going down and failing to serve traffic.</td>
<td>1. Review your <code>cloudflared</code> <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/">logs</a> for connection failures or error messages. <br /> 2. Investigate local network and firewall rules to ensure they are not blocking connections to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/">Cloudflare Tunnel IPs and ports</a>. <br /></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="tunnel-status-scope">Tunnel status scope</h3>
@markup("md", "content/.markup/bodies/14890.md")
</aside>
<h3 id="notifications">Notifications</h3>
<p>Administrators can receive alerts when tunnels change health or deployment status. Notifications can be delivered by email, webhook, or third-party services.</p>
<p>To configure tunnel notifications, refer to <a href="/notifications/get-started/#create-a-notification">Create a notification</a>.</p>
<details><summary>Tunnel Creation or Deletion Event</summary><strong>Who is it for?</strong><p>Customers who want to receive a notification when Cloudflare Tunnels are created or deleted in their account.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>All Cloudflare Zero Trust plans.</p>
<strong>What should you do if you receive one?</strong><p>No action is needed.</p>
</details><details><summary>Tunnel Health Alert</summary><strong>Who is it for?</strong><p>Customers who want to be warned about changes in health status for their Cloudflare Tunnels.</p>
<strong>Other options / filters</strong><p>None.</p>
<strong>Included with</strong><p>All Cloudflare Zero Trust plans.</p>
<strong>What should you do if you receive one?</strong><p>Monitor tunnel health over time and consider deploying <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/"><code>cloudflared</code> replicas or load balancers</a>.</p>
<strong>Additional information</strong><p>Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/common-errors/#tunnel-status">Tunnel status</a> to review the list of possible tunnel statuses (<code>Healthy</code>, <code>Inactive</code>, <code>Down</code> and <code>Degraded</code>).</p>
</details>
<h2 id="logs">Logs</h2>
<p>Tunnel logs record all activity between <code>cloudflared</code> and the Cloudflare global network, and all activity between <code>cloudflared</code> and your origin server.</p>
<h3 id="server-side-logs">Server-side logs</h3>
<p>If you have access to the origin server, you can use the <a href="/tunnel/reference/run-parameters/#loglevel"><code>--loglevel</code> flag</a> to enable logging when you start the tunnel. By default, <code>cloudflared</code> writes logs to standard error (<code>stderr</code>) and does not store logs on the server.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14889.md")
</aside>
<p>To format each log line as a JSON object, add <code>--output json</code> before <code>run</code>:</p>
<pre><code class="language-sh">cloudflared tunnel --output json run &lt;UUID&gt;&#10;</code></pre>
<p>This format is useful for Kubernetes deployments and log collection systems that consume JSON.</p>
<p>For routine persistent logging, <a href=/tunnel/reference/run-parameters/#add-run-parameters-to-tunnel-service#log-directory>run the tunnel</a> with <code>--log-directory &lt;PATH&gt;</code>. This flag writes logs to <code>cloudflared.log</code> in the specified directory, rotates the file when it reaches 1 MB, and keeps up to five backups. It does not remove logs based on age.</p>
<pre><code class="language-sh">cloudflared tunnel --loglevel info --log-directory &lt;PATH&gt; run &lt;UUID&gt;&#10;</code></pre>
<p>Use the <a href="/tunnel/reference/run-parameters/#logfile"><code>--logfile</code> flag</a> instead for short troubleshooting sessions or when another tool manages rotation. <code>cloudflared</code> does not rotate the file specified by <code>--logfile</code>. If you set both flags, <code>--logfile</code> takes precedence.</p>
<h3 id="remote-log-streaming">Remote log streaming</h3>
<p>You can stream real-time logs from a running tunnel without SSH access to the server.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14894.md")
</div></div>
<h2 id="metrics">Metrics</h2>
<hr />
<hr />
<p>Tunnel metrics show a Cloudflare Tunnel's throughput and resource usage over time. When you run a tunnel, <code>cloudflared</code> will spin up a Prometheus metrics endpoint — an HTTP server that exposes metrics in <a href="https://prometheus.io/docs/introduction/overview/">Prometheus</a> format. You can use the Prometheus toolkit on a remote machine to scrape metrics data from the <code>cloudflared</code> server.</p>
<h3 id="default-metrics-server-address">Default metrics server address</h3>
<p>In non-containerized environments, <code>cloudflared</code> starts the metrics server on <code>127.0.0.1:&lt;PORT&gt;/metrics</code>, where <code>&lt;PORT&gt;</code> is the first available port in the range <code>20241</code> to <code>20245</code>. If all ports are unavailable, <code>cloudflared</code> binds to a random port. In containerized environments (Docker, Kubernetes), the default address is <code>0.0.0.0:&lt;PORT&gt;/metrics</code>.</p>
<p>To determine the default port, check your <a href="#server-side-logs">tunnel logs</a> around the time when the tunnel started. For example:</p>
<pre><code class="language-text">2024-12-19T21:17:58Z INF Starting metrics server on 127.0.0.1:20241/metrics&#10;</code></pre>
<h3 id="configure-a-custom-address">Configure a custom address</h3>
<p>To serve metrics on a custom IP address and port, perform these steps on the <code>cloudflared</code> host:</p>
<ol>
<li><a href="/tunnel/reference/run-parameters/#add-run-parameters-to-tunnel-service">Run the tunnel</a> using the
<code>--metrics</code> flag. For example,</li>
</ol>
<pre><code class="language-sh">cloudflared tunnel --metrics 127.0.0.1:60123 run my-tunnel&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14888.md")
</aside>
<ol start="2">
<li>Verify that the metrics server is running by going to <code>http://localhost:60123/metrics</code>. This will only work if you configured a localhost IP (<code>127.0.0.1</code> or <code>0.0.0.0</code>).</li>
</ol>
<p>You can now export the metrics to Prometheus and Grafana to visualize and query the data. Refer to the <a href="/tunnel/tutorials/grafana/">Grafana tutorial</a> for instructions on getting started with these tools.</p>
<details class="nb-details"><summary>cloudflared metrics</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14895.md")
</div></details>
<details class="nb-details"><summary>Prometheus metrics</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14896.md")
</div></details>
<details class="nb-details"><summary>Go runtime metrics</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14897.md")
</div></details>
<h2 id="diagnostic-logs">Diagnostic logs</h2>
<p>Cloudflare Tunnel generates diagnostic reports that collect data from a single <code>cloudflared</code> instance running on the local machine. This requires <code>cloudflared</code> version 2024.12.2 or later.</p>
<h3 id="generate-diagnostics">Generate diagnostics</h3>
<ol>
<li>(Linux only) To include network diagnostics in the logs, allow the <code>cloudflared</code> user to create RAW and PACKET sockets without root permissions:</li>
</ol>
<pre><code class="language-sh">sudo setcap cap_net_raw+ep /usr/bin/traceroute &amp;&amp; sudo setcap cap_net_raw+ep /usr/bin/traceroute&#10;</code></pre>
<p>If you do not set <code>cap_net_raw</code>, then traceroute data will be unavailable.</p>
<ol start="2">
<li>Get diagnostic logs:</li>
</ol>
<pre><code class="language-sh">cloudflared tunnel diag&#10;</code></pre>
<p>If multiple instances of <code>cloudflared</code> are running on the same host, specify the <a href="#configure-a-custom-address">metrics server IP and port</a> for the instance you want to diagnose. For example:</p>
<pre><code class="language-sh">cloudflared tunnel diag --metrics 127.0.0.1:20241&#10;</code></pre>
<p>This command will output the status of each diagnostic task and place a <code>cloudflared-diag-YYYY-MM-DDThh-mm-ss.zip</code> file in your working directory.</p>
<details class="nb-details"><summary>Docker diagnostics</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14898.md")
</div></details>
<details class="nb-details"><summary>Kubernetes diagnostics</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14899.md")
</div></details>
<h3 id="diagnostic-file-contents">Diagnostic file contents</h3>
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
<td><a href="/tunnel/reference/run-parameters/">Tunnel run parameters</a> used when starting the tunnel</td>
<td>diagnosee</td>
</tr>
<tr>
<td><code>cloudflared_logs.txt</code></td>
<td><a href="#logs">Tunnel log file</a><sup><a href="#footnote-cloudflare-one-tunnel-diagnostics-tunnel-diag-file-mdx-1">1</a></sup></td>
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
<td>Snapshot of <a href="#metrics">Tunnel metrics</a> at the time of diagnosis</td>
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
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-cloudflare-one-tunnel-diagnostics-tunnel-diag-file-mdx-1">If the log file is blank, you may need to <a href="#server-side-logs">set `--loglevel` to `debug`</a> when you start the tunnel. The `--loglevel` parameter is only required if you ran the tunnel from the CLI using a `cloudflared tunnel run` command. It is not necessary if the tunnel runs as a Linux/macOS service or runs in Docker/Kubernetes.</li></ol></section>
