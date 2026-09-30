<p>Consider the following steps to learn how to configure Private Network Load Balancing solution, using <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel</a> as the off-ramp to securely connect to your private or internal services.</p>
<h2 id="1-configure-a-cloudflare-tunnel-with-an-assigned-virtual-network"><ol>
<li>Configure a Cloudflare tunnel with an assigned virtual network</li>
</ol></h2>
<p>The specific configuration steps can vary depending on your infrastructure and services you are looking to connect. If you are not familiar with Cloudflare Tunnel, the pages linked on each step provide more guidance.</p>
<ol>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/#1-create-a-tunnel">Create a tunnel</a> to connect your data center to Cloudflare.</li>
<li>Create a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/tunnel-virtual-networks/">virtual network</a> and assign it to the tunnel you configured in the previous step.</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10347.md")
</div></div>
<h2 id="2-configure-cloudflare-load-balancing"><ol start="2">
<li>Configure Cloudflare Load Balancing</li>
</ol></h2>
<p>Once you have Cloudflare tunnels with associated virtual networks (VNets) configured, the VNets can be specified for each endpoint when you <a href="/load-balancing/pools/create-pool/#create-a-pool">create or edit a pool</a>. This will enable Cloudflare load balancers to use the correct tunnel and securely reach the private IP endpoints.</p>
<p>The specific configuration will vary depending on your use case. Refer to the following steps to understand the workflow.</p>
<ol>
<li><a href="/load-balancing/monitors/create-monitor/">Create the Load Balancing monitor</a> according to your needs.</li>
<li><a href="/load-balancing/pools/create-pool/">Create the pool</a> specifying your private IP addresses and corresponding virtual networks.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10344.md")
</aside>
<ol start="3">
<li><a href="/load-balancing/load-balancers/create-load-balancer/">Create the load balancer</a>, specifying the pool and monitor you created in the previous steps, as well as the desired <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/">global traffic steering policies</a> and <a href="/load-balancing/additional-options/load-balancing-rules/">custom rules</a>.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="spectrum-limitations">Spectrum limitations</h3>
@markup("md", "content/.markup/bodies/10343.md")
</aside>
