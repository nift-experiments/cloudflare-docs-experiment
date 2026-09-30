<p>Magic Transit Virtual Network uses a routing table to steer your traffic from Cloudflare's global network to your connected networks via next-hop. You can add entries to the Magic Transit Virtual Network routing table through static route configuration or routes learned from BGP peering (beta) (available over CNI with Dataplane v2, as well as IPsec and GRE tunnels).</p>
<p>Refer to <a href="/magic-transit/reference/traffic-steering/">Traffic Steering</a> for more information about all the technical aspects related to:</p>
<ul>
<li>Routes' priorities and weights</li>
<li>Regional scoping of traffic to reduce latency</li>
<li>BGP peering (beta)</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="anycast-routing">Anycast routing</h3>
@markup("md", "content/.markup/bodies/10683.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10684.md")
</aside>
<h2 id="configure-static-routes">Configure static routes</h2>
<h3 id="create-a-static-route">Create a static route</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10687.md")
</div></div>
<h3 id="edit-a-static-route">Edit a static route</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10690.md")
</div></div>
<h3 id="delete-static-route">Delete static route</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/10693.md")
</div></div>
<h2 id="configure-bgp-routes">Configure BGP routes</h2>
<p>BGP peering is available when using the following on-ramps:</p>
<ul>
<li><a href="/network-interconnect/">CNI with Dataplane v2</a>.</li>
<li><a href="/magic-transit/how-to/configure-tunnel-endpoints/">IPsec and GRE tunnels (beta)</a>. Requires <a href="/magic-transit/reference/traffic-steering/#unified-routing-mode-beta">Unified Routing (beta)</a>.</li>
</ul>
<h3 id="choose-an-asn-for-bgp-peering">Choose an ASN for BGP peering</h3>
<p>The Magic Transit Virtual Network routing table is managed by the customer. You can select both the Cloudflare-side ASN (Autonomous System Number) and the ASN for your customer device. The customer device ASN can be 2-byte or 4-byte. <a href="/magic-transit/how-to/advertise-prefixes/#cloudflare-asn-vs-your-own-asn">Public ASNs used for Magic Transit</a> are verified during the onboarding process.</p>
<p>By default, each BGP peering session uses the same Cloudflare-side ASN to represent peering with the Magic Transit Virtual Network routing table. This ASN is called the <strong>CF Account ASN</strong> and is set to <code>13335</code>. You can configure this to a private 2-byte ASN (any value between <code>64512</code> and <code>65534</code>, such as <code>65000</code>).</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10678.md")
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
<p>Magic Transit customers should also be aware of the following:</p>
<ul>
<li>The Cloudflare side ASN will never be exposed in <code>AS_PATH</code> of anycast announcements from the Cloudflare edge. In those announcements, Cloudflare will always use the Cloudflare ASN of <code>13335</code> optionally prepended with a bring-your-own ASN as described in <a href="/magic-transit/how-to/advertise-prefixes/#cloudflare-asn-vs-your-own-asn">Cloudflare ASN vs. your own ASN</a>.</li>
<li>The customer device ASN can be a private ASN or the ASN they are using for Magic Transit anycast announcements at the edge: this has no impact on the ASN for the anycast announced prefix at the edge of the Cloudflare global network.</li>
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
@markup("md", "content/.markup/bodies/10677.md")
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
<li>Locate the CNI interconnect with Dataplane v2 to configure with BGP &gt; select the <strong>three dots</strong> next to it &gt; <strong>Configure BGP</strong>.</li>
<li>In <strong>Customer device ASN</strong>, enter the ASN for your network.</li>
<li>In <strong>MD5 key</strong>, you can optionally enter the key for your network. Note that this is meant to prevent accidental misconfigurations and is not a security mechanism.</li>
<li>(Optional) In <strong>Additional Advertised prefix list</strong>, input any additional prefixes you want to advertise alongside your existing routes. Leave this blank if you do not want to advertise extra routes. Typical prefixes to configure here include:
<ul>
<li>A route to <code>0.0.0.0/0</code>, the default route — to attract all Internet-bound traffic if using Magic Transit with Egress.</li>
<li>A route to <code>100.96.0.0/12</code>, the portion of CGNAT space <a href="/mesh/features/routes/#return-traffic-routing">used by default with Cloudflare One Clients</a>.</li>
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
<li>In <strong>IPsec/GRE tunnels</strong>, locate the tunnel you want to configure with BGP &gt; select the <strong>three dots</strong> next to it &gt; <strong>Configure BGP</strong>.</li>
<li>In <strong>Customer device ASN</strong>, enter the ASN for your network.</li>
<li>In <strong>MD5 key</strong>, you can optionally enter the key for your network. Note that this is meant to prevent accidental misconfigurations and is not a security mechanism.</li>
<li>(Optional) In <strong>Additional Advertised prefix list</strong>, input any additional prefixes you want to advertise alongside your existing routes. Leave this blank if you do not want to advertise extra routes. Typical prefixes to configure here include:
<ul>
<li>A route to <code>0.0.0.0/0</code>, the default route — to attract all Internet-bound traffic if using Magic Transit with Egress.</li>
<li>A route to <code>100.96.0.0/12</code>, the portion of CGNAT space <a href="/mesh/features/routes/#return-traffic-routing">used by default with Cloudflare One Clients</a>.</li>
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
@markup("md", "content/.markup/bodies/10676.md")
</aside>
- Hold time must be greater than 0 seconds (BGP `KEEPALIVE` messages are required). Cloudflare recommends at least 45 seconds. Cloudflare advertises a hold time of 90 seconds for GRE/IPsec tunnels. If you set a value greater than 90 seconds, the negotiated hold time will be 90 seconds, according to the standard way BGP has of negotiating hold times.
- Connect retry time should be low (for example, five or 10 seconds).
- Your CPE may advertise up to 5,000 prefixes on one BGP session.
- MD5 authentication is optional. You can use a maximum of 80 characters. Supported characters include ``a-zA-Z0-9'!@#$%^&*()+[]{}<>/.,;:_-~`= \\|``
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/10675.md")
</aside>
