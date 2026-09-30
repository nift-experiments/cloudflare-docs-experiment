<p>Tunnel logs record all activity between a <code>cloudflared</code> instance and Cloudflare's global network, as well as all activity between <code>cloudflared</code> and your origin server. These logs allow you to investigate connectivity or performance issues with a Cloudflare Tunnel. You can configure your server to store persistent logs, or you can stream real-time logs from any client machine.</p>
<h2 id="view-logs-on-the-server">View logs on the server</h2>
<p>If you have access to the origin server, you can use the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#loglevel"><code>--loglevel</code> flag</a> to enable logging when you start the tunnel. By default, <code>cloudflared</code> writes logs to standard error (<code>stderr</code>) and does not store logs on the server.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5290.md")
</aside>
<p>To format each log line as a JSON object, add <code>--output json</code> before <code>run</code>:</p>
<pre><code class="language-sh">cloudflared tunnel --output json run &lt;UUID&gt;&#10;</code></pre>
<p>This format is useful for Kubernetes deployments and log collection systems that consume JSON.</p>
<p>For routine persistent logging, <a href=/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#add-run-parameters-to-tunnel-service#log-directory>run the tunnel</a> with <code>--log-directory &lt;PATH&gt;</code>. This flag writes logs to <code>cloudflared.log</code> in the specified directory, rotates the file when it reaches 1 MB, and keeps up to five backups. It does not remove logs based on age.</p>
<pre><code class="language-sh">cloudflared tunnel --loglevel info --log-directory &lt;PATH&gt; run &lt;UUID&gt;&#10;</code></pre>
<p>Use the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#logfile"><code>--logfile</code> flag</a> instead for short troubleshooting sessions or when another tool manages rotation. <code>cloudflared</code> does not rotate the file specified by <code>--logfile</code>. If you set both flags, <code>--logfile</code> takes precedence.</p>
<h2 id="view-logs-on-your-local-machine">View logs on your local machine</h2>
<p>You can view real-time logs for a Cloudflare Tunnel via the dashboard or from any machine that has <code>cloudflared</code> installed. With remote log streams, you do not need to SSH into the server that is running the tunnel. To get remote logs, the tunnel must be active and able to receive requests.</p>
<h3 id="dashboard">Dashboard</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5289.md")
</aside>
<hr />
<hr />
<p>To stream tunnel logs from the dashboard:</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Tunnels</strong> and select your tunnel.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to the <strong>Live logs</strong> tab.</li>
<li>Select <strong>Live</strong> to start streaming.</li>
</ol>
<h4 id="view-logs-for-a-replica">View logs for a replica</h4>
<p>If you are running multiple <code>cloudflared</code> instances for the same tunnel (also known as <a href="/tunnel/configuration/#replicas-and-high-availability">replicas</a>), logs from all connected replicas are streamed automatically and grouped by hostname, making it easy to identify which host machine produced each log entry.</p>
<p>To filter the stream to specific replicas, select the <strong>Filter</strong> icon and expand the <strong>Replicas</strong> section. You can also filter by <strong>Log Level</strong> and <strong>Event Type</strong>.</p>
<h3 id="cli">CLI</h3>
<p>The <code>cloudflared</code> daemon can stream logs from any tunnel in your account to the local command line. <code>cloudflared</code> must be installed on both your local machine and the origin server.</p>
<hr />
<hr />
<p>The <code>cloudflared</code> daemon can stream logs from any tunnel in your account to the local command line. <code>cloudflared</code> must be installed on both your local machine and the origin server.</p>
<ol>
<li>On your local machine, authenticate <code>cloudflared</code> to your Cloudflare account:</li>
</ol>
<pre><code class="language-sh">cloudflared tunnel login&#10;</code></pre>
<ol start="2">
<li>Run <code>cloudflared tail</code> for a specific tunnel:</li>
</ol>
<pre><code class="language-sh">cloudflared tail &lt;UUID&gt;&#10;</code></pre>
<p>For a more structured view of the JSON message, you can pipe the output to tools like <a href="https://stedolan.github.io/jq/">jq</a>:</p>
<pre><code class="language-sh">cloudflared tail --output=json &lt;UUID&gt; | jq .&#10;</code></pre>
<h4 id="filter-logs">Filter logs</h4>
<p>You can filter logs by event type (<code>--event</code>), event level (<code>--level</code>), or sampling rate (<code>-sampling</code>) to reduce the volume of logs streamed from the origin. This helps mitigate the performance impact on the origin, especially when the origin is normally under high load. For example:</p>
<pre><code class="language-sh">cloudflared tail --level debug &lt;UUID&gt;&#10;</code></pre>
<table>
<thead>
<tr>
<th>Flag</th>
<th>Description</th>
<th>Allowed values</th>
<th>Default value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>--event</code></td>
<td>Filter by the type of event / request.</td>
<td><code>cloudflared</code>, <code>http</code>, <code>tcp</code>, <code>udp</code></td>
<td>All events</td>
</tr>
<tr>
<td><code>--level</code></td>
<td>Return logs at this level and above. Works independently of the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/run-parameters/#loglevel"><code>--loglevel</code></a> setting on the server.</td>
<td><code>debug</code>, <code>info</code>, <code>warn</code>, <code>error</code>, <code>fatal</code></td>
<td><code>debug</code></td>
</tr>
<tr>
<td><code>--sampling</code></td>
<td>Sample a fraction of the total logs.</td>
<td>Number from <code>0.0</code> to <code>1.0</code></td>
<td><code>1.0</code></td>
</tr>
</tbody>
</table>
<h4 id="view-logs-for-a-replica-1">View logs for a replica</h4>
<p>If you are running multiple <code>cloudflared</code> instances for the same tunnel (also known as <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">replicas</a>), you must specify an individual instance to stream logs from:</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Tunnels</strong> and select your tunnel.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Find the <strong>Connector ID</strong> for the <code>cloudflared</code> instance you want to view.</li>
<li>Specify the Connector ID in <code>cloudflared tail</code>:</li>
</ol>
<pre><code class="language-sh">cloudflared tail --connector-id &lt;CONNECTOR ID&gt; &lt;UUID&gt;&#10;</code></pre>
<h3 id="performance-considerations">Performance considerations</h3>
<ul>
<li>The logging session will only be held open for one hour. All logging systems introduce some level of performance overhead, and this limit helps prevent long term impact to your tunnel's end-to-end latencies.</li>
<li>When streaming logs for a high throughput tunnel, Cloudflare intentionally prioritizes service stability over log delivery. To reduce the number of dropped logs, try <a href="#filter-logs">requesting fewer logs</a>. To ensure that you are seeing all logs, <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/#view-logs-on-the-server">view logs on the server</a> instead of streaming the logs remotely.</li>
</ul>
