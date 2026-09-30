<p>Cloudflare Virtual Network uses a routing table to steer your traffic from Cloudflare's global network to your connected networks via next-hop. You can add entries to the Cloudflare Virtual Network routing table through static route configuration or routes learned from BGP peering (beta) (available over CNI with Dataplane v2, as well as IPsec and GRE tunnels).</p>
<p>Refer to <a href="/cloudflare-wan/reference/traffic-steering/">Traffic Steering</a> for more information about all the technical aspects related to:</p>
<ul>
<li>Routes' priorities and weights</li>
<li>Regional scoping of traffic to reduce latency</li>
<li>BGP peering (beta)</li>
<li><a href="/cloudflare-wan/reference/traffic-steering/#automatic-return-routing-beta">Automatic Return Routing (ARR)</a></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6904.md")
</aside>
<h2 id="configure-static-routes">Configure static routes</h2>
<p>The following IPv4 address ranges are allowed in the Cloudflare Virtual Network routing table:</p>
<ul>
<li><a href="https://datatracker.ietf.org/doc/html/rfc1918">RFC 1918</a> address space, specifically <code>10.0.0.0/8</code>, <code>172.16.0.0/12</code>, and <code>192.168.0.0/16</code>.</li>
</ul>
<p>When using Cloudflare WAN and Cloudflare Tunnel together, consider the IP ranges utilized in the static routes of Cloudflare Tunnel when selecting static routes for Cloudflare WAN. For more information, refer to <a href="/cloudflare-wan/zero-trust/cloudflare-tunnel/">Cloudflare Tunnel</a>.</p>
<p>For prefixes outside RFC 1918, contact your Cloudflare customer service manager.</p>
<h3 id="create-a-static-route">Create a static route</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6907.md")
</div></div>
<h3 id="edit-a-static-route">Edit a static route</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6910.md")
</div></div>
<h3 id="delete-static-route">Delete static route</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6913.md")
</div></div>
<h2 id="configure-automatic-return-routing-beta">Configure Automatic Return Routing (beta)</h2>
<p><a href="/cloudflare-wan/reference/traffic-steering/#automatic-return-routing-beta">Automatic Return Routing (beta)</a> allows Cloudflare to track network flows from your Cloudflare WAN (formerly Magic WAN) connected locations, ensuring return traffic is routed back to the connection where it was received without requiring static or dynamic routes. This functionality requires the new <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing mode (beta)</a>.</p>
<p>To enable ARR:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6916.md")
</div></div>
<h2 id="configure-bgp-routes">Configure BGP routes</h2>
<p>BGP peering is available when using the following on-ramps:</p>
<ul>
<li><a href="/network-interconnect/">CNI with Dataplane v2</a>.</li>
<li><a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">IPsec and GRE tunnels (beta)</a>. Requires <a href="/cloudflare-wan/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing (beta)</a>.</li>
</ul>
<h3 id="choose-an-asn-for-bgp-peering">Choose an ASN for BGP peering</h3>
<p>The Cloudflare Virtual Network routing table is managed by the customer. You can select both the Cloudflare-side ASN (Autonomous System Number) and the ASN for your customer device. The customer device ASN can be 2-byte or 4-byte.</p>
<p>By default, each BGP peering session uses the same Cloudflare-side ASN to represent peering with the Cloudflare Virtual Network routing table. This ASN is called the <strong>CF Account ASN</strong> and is set to <code>13335</code>. You can configure this to a private 2-byte ASN (any value between <code>64512</code> and <code>65534</code>, such as <code>65000</code>).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6899.md")
</aside>
<p>To set this ASN:</p>
<ol>
<li>Go to the Routes page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>WAN configuration</strong>.</li>
<li>In <strong>CF Account ASN</strong>, enter Cloudflare's ASN.</li>
<li>Select <strong>Update</strong>.</li>
</ol>
<p>Cloudflare WAN customers should also be aware of the following:</p>
<ul>
<li>The customer chooses their device ASN, which must be different from the Cloudflare-side ASN.</li>
<li>The Cloudflare side ASN will be included in the <code>AS_PATH</code> of announced routes to any BGP enabled on-ramp (interconnect, IPsec or GRE tunnel).</li>
<li>The customer-announced <code>AS_PATH</code> is transitive between on-ramps — meaning the origin (customer) ASN is visible in the <code>AS_PATH</code> of routes received from Cloudflare via BGP. Due to default BGP loop prevention mechanisms, a router will reject any route that contains its own ASN in the <code>AS_PATH</code>. For example, if two Cloudflare WAN-connected sites both use <code>ASN 65000</code>, site A will not accept routes from site B, and vice versa, because each site sees its own ASN in the advertised <code>AS_PATH</code>. <br />
To enable routing between private networks over Cloudflare WAN, you should either:
<ul>
<li>Assign a unique ASN to each site/network, or</li>
<li>Configure your edge CPE to accept BGP routes that include its own ASN in the <code>AS_PATH</code>.</li>
</ul>
</li>
</ul>
<h3 id="set-up-bgp-peering">Set up BGP peering</h3>
<p>You need to configure two ASNs:</p>
<ul>
<li>The Cloudflare <a href="#choose-an-asn-for-bgp-peering">account-scoped ASN</a> named <strong>CF Account ASN</strong>.</li>
<li>One ASN for each on-ramp you want to configure with BGP.</li>
</ul>
<p>If you have already set up your Cloudflare account ASN, skip steps two and three below.</p>
<h4 id="set-up-bgp-for-an-interconnect">Set up BGP for an interconnect</h4>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6898.md")
</aside>
<ol>
<li>Go to the Routes page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>WAN configuration</strong>.</li>
<li>In <strong>CF Account ASN</strong>, enter Cloudflare's ASN, and select <strong>Update</strong>.</li>
<li>Go to <strong>Interconnects</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="5">
<li>
<p>Locate the CNI interconnect with Dataplane v2 to configure with BGP &gt; select the <strong>three dots</strong> next to it &gt; <strong>Configure BGP</strong>.</p>
</li>
<li>
<p>In <strong>Customer device ASN</strong>, enter the ASN for your network.</p>
 <aside class="nb-aside note">
</li>
</ol>
@markup("md", "content/.markup/bodies/6917.md")
</aside>
<ol start="7">
<li>In <strong>MD5 key</strong>, you can optionally enter the key for your network. Note that this is meant to prevent accidental misconfigurations and is not a security mechanism.</li>
<li>(Optional) In <strong>Additional Advertised prefix list</strong>, input any additional prefixes you want to advertise alongside your existing routes. Leave this blank if you do not want to advertise extra routes. Typical prefixes to configure here include:
<ul>
<li>A route to <code>0.0.0.0/0</code>, the default route — to attract all Internet-bound traffic if using Cloudflare WAN with Gateway.</li>
<li>A route to <code>100.96.0.0/12</code>, the portion of CGNAT space <a href="/mesh/features/routes/#return-traffic-routing">used by default with Cloudflare One Clients</a>.</li>
<li>A route to <code>100.64.0.0/12</code>, the portion of CGNAT space <a href="/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips/">used by default for Cloudflare Source IPs</a>.</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h4 id="set-up-bgp-for-ipsec-gre-tunnels">Set up BGP for IPsec/GRE tunnels</h4>
<ol>
<li>Go to the Routes page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>WAN configuration</strong>.</li>
<li>In <strong>CF Account ASN</strong>, enter Cloudflare's ASN, and select <strong>Update</strong>.</li>
<li>Go to <strong>Connectors</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="5">
<li>
<p>In <strong>IPsec/GRE tunnels</strong>, locate the tunnel you want to configure with BGP &gt; select the <strong>three dots</strong> next to it &gt; <strong>Configure BGP</strong>.</p>
</li>
<li>
<p>In <strong>Customer device ASN</strong>, enter the ASN for your network.</p>
 <aside class="nb-aside note">
</li>
</ol>
@markup("md", "content/.markup/bodies/6918.md")
</aside>
<ol start="7">
<li>In <strong>MD5 key</strong>, you can optionally enter the key for your network. Note that this is meant to prevent accidental misconfigurations and is not a security mechanism.</li>
<li>(Optional) In <strong>Additional Advertised prefix list</strong>, input any additional prefixes you want to advertise alongside your existing routes. Leave this blank if you do not want to advertise extra routes. Typical prefixes to configure here include:
<ul>
<li>A route to <code>0.0.0.0/0</code>, the default route — to attract all Internet-bound traffic if using Cloudflare WAN with Gateway.</li>
<li>A route to <code>100.96.0.0/12</code>, the portion of CGNAT space <a href="/mesh/features/routes/#return-traffic-routing">used by default with Cloudflare One Clients</a>.</li>
<li>A route to <code>100.64.0.0/12</code>, the portion of CGNAT space <a href="/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips/">used by default for Cloudflare Source IPs</a>.</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h3 id="important-remarks-for-gre-ipsec-tunnels">Important remarks for GRE/IPsec tunnels</h3>
<p>If you are configuring BGP peering for a tunnel (GRE or IPsec) you must be aware of the following:</p>
<ul>
<li>Your Customer Premises Equipment (CPE) must initiate the BGP peering session. Cloudflare will not initiate.</li>
<li>Your BGP speaker must peer with the tunnel's IPv4 interface address. Your CPE may use any IPv4 address for its side of the peering connection; it does not need to use the other address from the <code>/31</code> or <code>/30</code> interface subnet.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6897.md")
</aside>
- Hold time must be greater than 0 seconds (BGP `KEEPALIVE` messages are required). Cloudflare recommends at least 45 seconds. Cloudflare advertises a hold time of 90 seconds for GRE/IPsec tunnels. If you set a value greater than 90 seconds, the negotiated hold time will be 90 seconds, according to the standard way BGP has of negotiating hold times.
- Connect retry time should be low (for example, five or 10 seconds).
- Your CPE may advertise up to 5,000 prefixes on one BGP session.
- MD5 authentication is optional. You can use a maximum of 80 characters. Supported characters include ``a-zA-Z0-9'!@#$%^&*()+[]{}<>/.,;:_-~`= \\|``
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6896.md")
</aside>
<h2 id="next-steps">Next steps</h2>
<p>Now that you have configured your tunnels and routes, the next step is to create a site. Sites represent the local network of a data center, office, or other physical location, and combine all on-ramps available there. Sites also allow you to check, at a glance, the state of your on-ramps and set up health alert settings so that Cloudflare notifies you when there are issues with the site's on-ramps.</p>
<p>Refer to <a href="/cloudflare-wan/configuration/common-settings/sites/">Set up a site</a> for more information.</p>
