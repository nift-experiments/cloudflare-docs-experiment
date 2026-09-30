<h2 id="recommendations">Recommendations</h2>
<p>For production use cases, we recommend the following baseline configuration:</p>
<ul>
<li>Run a cloudflared replica on two dedicated host machines per network location. Using two hosts enables server-side redundancy. See <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/">tunnel availability and replicas</a> for setup instructions.</li>
<li>Size each host with minimum 4GB of RAM and 4 CPU cores.</li>
</ul>
<p>This setup is usually sufficient to handle traffic from small-medium sized applications. The actual amount of resources used by cloudflared will depend on many variables, including the number of requests per second, bandwidth, network path, and hardware. If usage increases beyond your existing tunnel capacity, you can scale your tunnel by increasing the hardware allocated to the cloudflared hosts.</p>
<h2 id="capacity-calculator">Capacity calculator</h2>
<p>To estimate tunnel capacity requirements for your deployment, refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/system-requirements/">tunnel capacity calculator in the Zero Trust documentation</a>.</p>
<h2 id="scaling-considerations">Scaling considerations</h2>
<p>Monitor tunnel performance and scale accordingly:</p>
<ul>
<li><strong>CPU utilization</strong>: Keep below 70% average usage</li>
<li><strong>Memory usage</strong>: Maintain headroom for traffic spikes</li>
<li><strong>Network bandwidth</strong>: Ensure adequate throughput for peak loads</li>
<li><strong>Connection count</strong>: Scale cloudflared vertically when approaching capacity limits</li>
</ul>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Configure <a href="/workers-vpc/configuration/tunnel/">tunnel deployment</a></li>
<li>Set up <a href="/workers-vpc/configuration/tunnel/">high availability</a> with multiple replicas</li>
</ul>
