<p>To use Magic Transit, you need to own a publicly routable IP address block with a minimum size of <code>/24</code>. If you do not own a <code>/24</code> address block, you can use Magic Transit with a Cloudflare-owned IP address. This option is helpful if you do not meet the <code>/24</code> prefix length requirements or want to protect a smaller network.</p>
<p>To protect your network with a Cloudflare IP address, contact your account manager. After you receive your IP address:</p>
<ul>
<li><a href="/magic-transit/how-to/configure-tunnel-endpoints/">Create a tunnel</a>.</li>
<li><a href="/magic-transit/how-to/configure-routes/#configure-static-routes">Set up static routes</a> or <a href="/magic-transit/how-to/configure-routes/#configure-bgp-routes">BGP peering (beta)</a>.</li>
<li><a href="/magic-transit/network-health/run-endpoint-health-checks/">Configure health checks</a>.</li>
<li>Confirm you properly configured <a href="/magic-transit/network-health/update-tunnel-health-checks-frequency/">tunnel</a> and endpoint health checks.</li>
<li>Update your infrastructure at your own pace to use the allocated Cloudflare IPs.</li>
</ul>
<p>When you use a Cloudflare-owned IP space, you do not need a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/784.md")
</div>. When using Cloudflare-leased IPs, Cloudflare automatically enables [Magic Transit Egress](/magic-transit/reference/egress/), which routes your egress traffic to Cloudflare instead of the Internet. Set up policy-based routing on your end to ensure return traffic routes properly.
<h2 id="check-your-cloudflare-ips">Check your Cloudflare IPs</h2>
<p>You can find your leased Anycast IPs for Magic Transit on the dashboard under <a href="https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space"><strong>Address space</strong> &gt; <strong>Leased IPs</strong></a>.</p>
