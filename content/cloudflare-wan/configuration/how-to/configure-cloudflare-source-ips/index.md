<p>You can configure the source IP address range used by Cloudflare whenever a Cloudflare service, such as Cloudflare Load Balancing, sends traffic to a Cloudflare One private network. This address range is referred to as the Cloudflare Source IP Prefix (or <code>cloudflare_source</code> subnet type in the API).</p>
<ul>
<li>IPv4 traffic is sourced from <code>100.64.0.0/12</code>. This range is configurable.</li>
<li>IPv6 traffic is sourced from <code>2606:4700:cf1:5000::/64</code>. This range is not configurable.</li>
</ul>
<p>When Cloudflare services send traffic to your private network, the source IP address determines how return traffic is routed. It also determines whether on-premises security devices can properly inspect the traffic. In legacy routing mode, traffic to private networks is sourced from public Cloudflare IPs, which can cause routing and security issues.</p>
<p>For customers using <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing (beta)</a>, traffic to private networks is sourced from a dedicated, non-internet-routable private IPv4 range by default. This ensures:</p>
<ul>
<li><strong>Symmetric routing</strong> — Return traffic stays on your private network connection instead of taking an asymmetric path over the public Internet.</li>
<li><strong>Firewall state preservation</strong> — On-premises stateful firewalls can track connections end-to-end because they see both request and response traffic.</li>
<li><strong>Security and compliance</strong> — Private traffic stays on secure private paths.</li>
</ul>
<p>Customers may wish to change the default allocated range to avoid IP conflicts or fit with an existing IP Address Management plan.</p>
<p>You must configure routes in your network so that response traffic for these source ranges is sent back to Cloudflare over your Cloudflare One connections.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you begin, ensure that:</p>
<ul>
<li>You have Cloudflare One <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing (beta)</a>. If your account is not yet on Unified Routing, contact your account team to discuss migration and availability.</li>
<li>You have <a href="/fundamentals/api/reference/permissions/">Cloudflare One Networks Write</a> permission.</li>
<li>Your desired new network range meets the following requirements:
<ul>
<li>Your network must be defined as a single CIDR with a prefix length of <code>/12</code>.</li>
<li>Cloudflare One subnets in the same account cannot overlap. Default allocations include:
<ul>
<li>Cloudflare Source IPs (<code>100.64.0.0/12</code>)</li>
<li>Hostname Route Token IPs (<code>172.64.128.0/20</code> by default; configurable)</li>
<li>Cloudflare One Clients (<code>100.96.0.0/12</code>)</li>
<li>Private Load Balancers (<code>100.112.0.0/16</code>)</li>
</ul>
</li>
<li>The source subnet cannot match or contain any existing route in your Cloudflare One routing table. The source subnet can be within a supernet route.</li>
</ul>
</li>
</ul>
<h2 id="affected-connectors-and-services">Affected connectors and services</h2>
<h3 id="connectors">Connectors</h3>
<p>Cloudflare One supports multiple <a href="/cloudflare-wan/zero-trust/connectivity-options/">connectivity options</a>. The following connectors will receive traffic from the <code>cloudflare_source</code> subnet when a Cloudflare service initiates a request to the connected network or endpoint as an offramp:</p>
<ul>
<li><strong>Anycast tunnels:</strong> GRE, IPsec, and CNI</li>
<li><strong>Software connectors:</strong> Cloudflare One Client and Cloudflare Mesh</li>
</ul>
<p>Networks or endpoints connected via Cloudflare Tunnel will not receive traffic from the Cloudflare source IP subnet. Instead, the source IP address will be that of the host running the <code>cloudflared</code> software.</p>
<h3 id="services-that-originate-or-proxy-connections">Services that originate or proxy connections</h3>
<p>All Cloudflare services that originate or proxy connections will send traffic from a Cloudflare source IP.</p>
<p>This includes traffic that is proxied from a private network or endpoint onramp.</p>
<p>For example, traffic onramped from a Cloudflare One Client through Cloudflare Load Balancer or Gateway DNS Resolver will present a Cloudflare source IP to the destination offramp.</p>
<h2 id="configure-source-ips">Configure source IPs</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6919.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6922.md")
</div></div>
