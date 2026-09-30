<p><code>cloudflared</code> is lightweight enough to run on a Raspberry Pi or a data center server. Tunnel throughput is primarily limited by the number of ports configured in system software, not hardware.</p>
<h2 id="baseline-recommendations">Baseline recommendations</h2>
<p>Run a <code>cloudflared</code> <a href="/tunnel/configuration/#replicas-and-high-availability">replica</a> on two dedicated hosts per location with a minimum of 4 GB RAM and 4 CPU cores. Allocate 50,000 ports per host.</p>
<h2 id="port-configuration">Port configuration</h2>
---
---
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14887.md")
</div></div>
<h2 id="ulimits-linux-and-macos">ulimits (Linux and macOS)</h2>
<hr />
<hr />
<p>On Linux and macOS, <code>ulimit</code> settings determine the system resources available to a logged-in user. We recommend configuring the following ulimits on the <code>cloudflared</code> server:</p>
<table>
<thead>
<tr>
<th>ulimit</th>
<th>Description</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>-n</code></td>
<td>Maximum number of open files or file descriptors</td>
<td>≥ 70,000</td>
</tr>
</tbody>
</table>
<p>To view your current ulimits, open a terminal and run:</p>
<pre><code class="language-sh">ulimit -a&#10;</code></pre>
<p>To set the open files <code>ulimit</code>:</p>
<pre><code class="language-sh">ulimit -n 70000&#10;</code></pre>
<p>The command above sets the open files limit only for the current terminal session and will not persist after a reboot or new login. To apply this limit permanently, configure it using the persistent method appropriate for your operating system.</p>
<h2 id="capacity-calculator">Capacity calculator</h2>
<p>To estimate tunnel capacity requirements for your deployment:</p>
<ol>
<li>Use the <a href="/tunnel/observability/#cloudflared-metrics">metrics endpoint</a> to measure <code>cloudflared_tcp_total_sessions</code> and <code>cloudflared_udp_total_sessions</code>.</li>
<li>Compute the average <strong>TCP requests per second</strong> by dividing <code>cloudflared_tcp_total_sessions</code> by total time.</li>
<li>Compute the average <strong>Non-DNS UDP requests per second</strong> by dividing <code>cloudflared_udp_total_sessions</code> by total time.</li>
<li>Input <strong>TCP requests per second</strong> and <strong>Non-DNS UDP requests per second</strong> into the calculator below. (You can leave <strong>Private DNS requests per second</strong> as <code>0</code> unless you are using the tunnel for <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/system-requirements/">private network access</a>.)</li>
</ol>
<div class="nb-interactive-component" data-cf-component="TunnelCalculator"><h3 id="system-configuration">System configuration</h3><p>Enter the number of cloudflared replicas and available processor cores.</p><h3 id="metrics">Metrics</h3><p>Provide expected requests, bandwidth, and concurrent connections.</p><h3 id="result">Result</h3><p>Use the estimated throughput to calculate your tunnel capacity.</p></div>
<p>To increase tunnel capacity, add identical hosts running <code>cloudflared</code> replicas.</p>
