<p>This guide provides information and examples of how to configure Cloudflare WAN (formerly Magic WAN) with Internet Protocol Security (IPsec) tunnels in conjunction with Fortinet FortiGate firewalls.</p>
<p>The FortiGate configuration settings presented here support <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/#add-tunnels">bidirectional health checks</a> as required by Cloudflare WAN. However, they do not factor in any other traffic flows outside of the tunnel health checks. The configuration may need to be adjusted based on your current FortiGate configuration.</p>
<h2 id="testing-environment">Testing Environment</h2>
<p>The FortiGate configuration was tested on two different FortiGate firewalls:</p>
<ul>
<li>FortiGate Virtual Appliance version 7.0.8, running on VMware ESXi 6.5</li>
<li>FortiGate FG80F, version 7.0.12</li>
</ul>
<h2 id="cloudflare-wan-configuration">Cloudflare WAN configuration</h2>
<p>To set up Cloudflare WAN, add IPsec tunnels and static routes to your Cloudflare account using the dashboard or API.</p>
<p>Before proceeding, ensure that you have the IPv4 anycast address assigned to your account. You can find it in the Cloudflare dashboard under <strong>Address Space</strong> &gt; <a href="https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space"><strong>Leased IPs</strong></a>.</p>
<h3 id="ipsec-tunnels">IPsec tunnels</h3>
<p>Cloudflare handles failures on its network automatically by advertising your endpoint IP from multiple nodes across many globally distributed data centers. To handle failures on your network, configure two IPsec tunnels from separate routers.</p>
<ol>
<li>Follow the <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/#add-tunnels">Add tunnels</a> instructions to create the required IPsec tunnels with the following options:
<ul>
<li><strong>Health check type</strong>: Change to <em>Request</em>.</li>
<li><strong>Replay Protection</strong>: Do not change from the default setting.</li>
</ul>
</li>
</ol>
<h3 id="static-routes">Static routes</h3>
<p>Add two static routes to define the IP address space that exists behind the IPsec tunnels - one to each of the two IPsec tunnels defined in the previous section.</p>
<p>By default, the static routes are defined with the priority set to <code>100</code>. Cloudflare leverages <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/traffic-steering/#equal-cost-multi-path-routing">Equal Cost Multipath Routing (ECMP)</a> and will load balance the traffic equally across the two tunnels. If you prefer to use an Active/Passive model, you can leave the default value for the first route set to <code>100</code>, and set the value for the second tunnel to <code>150</code> (higher value is a lower priority).</p>
<ol>
<li>
<p>Follow the <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-routes/#create-a-static-route">Configure static routes</a> instructions to create a static route.</p>
</li>
<li>
<p>For the first route, ensure the following settings are defined:</p>
<ul>
<li><strong>Prefix</strong>: Specify the <a href="https://datatracker.ietf.org/doc/html/rfc1918">RFC1918</a> subnet that exists behind the first IPsec tunnel you have defined in the previous section.</li>
<li><strong>Tunnel/Next hop</strong>: Select your first tunnel (Tunnel 01 of 02).</li>
</ul>
</li>
<li>
<p>For the second route, ensure the following settings are defined:</p>
<ul>
<li><strong>Prefix</strong>: Specify the <a href="https://datatracker.ietf.org/doc/html/rfc1918">RFC1918</a> subnet that exists behind the second IPsec tunnel defined in the previous section.</li>
<li><strong>Tunnel/Next hop</strong>: Select your second tunnel (Tunnel 02 of 02).</li>
</ul>
</li>
</ol>
<h2 id="fortinet-fortigate-configuration">Fortinet FortiGate configuration</h2>
<h3 id="enable-asymmetric-routing">Enable asymmetric routing</h3>
<p>Enable asymmetric routing for ICMP to ensure health checks work as expected. This option is required. Otherwise, the tunnel health checks, which are critical for proper Cloudflare WAN functionality, will not work as designed.</p>
<p>Enabling asymmetric routing will affect FortiGate behavior. To learn more, refer to <a href="https://community.fortinet.com/t5/FortiGate/Technical-Note-How-the-FortiGate-behaves-when-asymmetric-routing/ta-p/198575">How FortiGate behaves when asymmetric routing is enabled</a>.</p>
<pre><code class="language-txt">config system settings&#10;    set asymroute-icmp enable&#10;end&#10;</code></pre>
<h3 id="configure-nat-t-optional">Configure NAT-T (optional)</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5615.md")
</aside>
<p>If you have Network Address Translation Traversal (NAT-T) on your network, you can enable this feature and initiate Internet Key Exchange (IKE) communications on port <code>4500</code>.</p>
<p>To set the IKE port, add the following to your system settings:</p>
<pre><code class="language-txt">config system settings&#10;    set ike-port 4500&#10;end&#10;</code></pre>
<p>To enable NAT-T, add <code>set nattraversal enable</code> to the IPsec tunnels you are configuring.</p>
<pre><code class="language-txt">fortigate # config vpn ipsec phase1-interface&#10;    edit &quot;&lt;NAME_OF_YOUR_TUNNEL&gt;&quot;&#10;        set nattraversal enable&#10;</code></pre>
<p>Refer to <a href="https://community.fortinet.com/t5/FortiGate/Technical-Tip-IPSec-VPN-NAT-traversal/ta-p/197873">Fortinet's documentation</a> for more details.</p>
<h3 id="disable-anti-replay-protection">Disable anti-replay protection</h3>
<p>For route-based IPsec configurations, you will need to disable anti-replay protection. The following command disables anti-replay protection globally, but you can also do this per firewall policy. Refer to Fortinet's documentation on <a href="https://community.fortinet.com/t5/FortiGate/Technical-Tip-Anti-Replay-option-support-per-policy/ta-p/191435">anti-replay support per policy</a> to learn more.</p>
<pre><code class="language-txt">config system global&#10;    set anti-replay disable&#10;end&#10;</code></pre>
<h3 id="ipsec-tunnels-1">IPsec tunnels</h3>
<p>IPsec tunnels leverage a route-based site-to-site Virtual Private Network (VPN) model. This model relies on the use of virtual tunnel interfaces and routing to define the traffic that flows across the IPsec tunnels.</p>
<p>Configure two IPsec tunnels using the <code>phase1-interface</code> and <code>phase2-interface</code> objects.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5614.md")
</aside>
<p>The following examples assume <code>wan1</code> is the external/egress interface of the FortiGate firewall.</p>
<h4 id="add-phase-1-interfaces">Add Phase 1 interfaces</h4>
<p><code>MWAN_IPsec_Tun1</code> corresponds to Tunnel 01 of 02 added earlier in the Cloudflare section of the configuration. <code>MWAN_IPsec_Tun2</code> corresponds to Tunnel 02 of 02 added earlier in the Cloudflare section of the configuration.</p>
<pre><code class="language-txt">fortigate # config vpn ipsec phase1-interface&#10;    edit &quot;MWAN_IPsec_Tun1&quot;&#10;        set interface &quot;wan1&quot;&#10;        set ike-version 2&#10;        set keylife 86400&#10;        set peertype any&#10;        set net-device enable&#10;        set proposal aes256gcm-prfsha512 aes256gcm-prfsha384 aes256gcm-prfsha256&#10;        set localid &quot;f1473dXXXXXXX72e33.49561179.ipsec.cloudflare.com&quot;&#10;        set dhgrp 20&#10;        set nattraversal disable&#10;        set remote-gw 162.159.67.210&#10;        set add-gw-route enable&#10;        set psksecret &lt;YOUR_PRE-SHARED_KEY&gt;&#10;    next&#10;    edit &quot;MWAN_IPsec_Tun2&quot;&#10;        set interface &quot;wan1&quot;&#10;        set ike-version 2&#10;        set keylife 86400&#10;        set peertype any&#10;        set net-device enable&#10;        set proposal aes256gcm-prfsha512 aes256gcm-prfsha384 aes256gcm-prfsha256&#10;        set localid &quot;de91565XXXXXXXfbbd6632.49561179.ipsec.cloudflare.com&quot;&#10;        set dhgrp 20&#10;        set nattraversal disable&#10;        set remote-gw 172.XX.XX.210&#10;        set add-gw-route enable&#10;        set psksecret ENC &lt;YOUR_PRE-SHARED_KEY&gt;&#10;    next&#10;end&#10;</code></pre>
<h4 id="add-phase-2-interfaces">Add Phase 2 interfaces</h4>
<p>Add two <code>phase2-interfaces</code> - one for each of the two <code>phase1-interfaces</code> as follows:</p>
<pre><code class="language-txt">fortigate # config vpn ipsec phase2-interface&#10;    edit &quot;MWAN_IPsec_Tun1&quot;&#10;        set phase1name &quot;MWAN_IPsec_Tun1&quot;&#10;        set proposal aes256gcm aes128gcm&#10;        set dhgrp 20&#10;        set replay disable&#10;        set keylifeseconds 28800&#10;        set auto-negotiate enable&#10;        set keepalive enable&#10;    next&#10;    edit &quot;MWAN_IPsec_Tun2&quot;&#10;        set phase1name &quot;MWAN_IPsec_Tun2&quot;&#10;        set proposal aes256gcm aes128gcm&#10;        set dhgrp 20&#10;        set replay disable&#10;        set keylifeseconds 28800&#10;        set auto-negotiate enable&#10;        set keepalive enable&#10;    next&#10;end&#10;</code></pre>
<h3 id="network-interfaces">Network interfaces</h3>
<h4 id="virtual-tunnel-interfaces">Virtual tunnel interfaces</h4>
<p>Configure the virtual tunnel interfaces that were automatically added when specifying the <code>set net-device enable</code> within the <code>phase1-interface</code> settings.</p>
<p>These are the only settings that should need to be added to the virtual tunnel interfaces:</p>
<ul>
<li><code>ip</code>: The local IP address (specify with a <code>/32</code> netmask - <code>255.255.255.255</code>).</li>
<li><code>remote-ip</code>: The value associated with the interface address specified earlier in the IPsec tunnels section (specify with a <code>/31</code> netmask - <code>255.255.255.254</code>).</li>
<li><code>alias</code>: This value is optional.</li>
</ul>
<p>The following examples assume <code>wan1</code> is the external/egress interface of the FortiGate firewall.</p>
<pre><code class="language-txt">fortigate # config system interface&#10;    edit &quot;MWAN_IPsec_Tun1&quot;&#10;        set vdom &quot;root&quot;&#10;        set ip 10.252.2.91 255.255.255.255&#10;        set allowaccess ping&#10;        set type tunnel&#10;        set remote-ip 10.252.2.90 255.255.255.254&#10;        set alias &quot;MWAN_IPsec_Tun1&quot;&#10;        set snmp-index 17&#10;        set interface &quot;wan1&quot;&#10;    next&#10;    edit &quot;MWAN_IPsec_Tun2&quot;&#10;        set vdom &quot;root&quot;&#10;        set ip 10.252.2.93 255.255.255.255&#10;        set allowaccess ping&#10;        set type tunnel&#10;        set remote-ip 10.252.2.92 255.255.255.254&#10;        set alias &quot;MWAN_IPsec_Tun2&quot;&#10;        set snmp-index 18&#10;        set interface &quot;wan1&quot;&#10;    next&#10;end&#10;</code></pre>
<h3 id="validate-communication-across-virtual-tunnel-interfaces">Validate communication across virtual tunnel interfaces</h3>
<p>Once the virtual tunnel interfaces have been configured, you should be able to ping the IP address associated with the <code>remote-ip</code> attribute.</p>
<p>The following examples show successful results from pinging across both virtual tunnel interfaces:</p>
<h4 id="mwan-ipsec-tun1">MWAN_IPsec_Tun1</h4>
<pre><code class="language-txt">fortigate # execute ping 10.252.2.90&#10;PING 10.252.2.90 (10.252.2.90): 56 data bytes&#10;64 bytes from 10.252.2.90: icmp_seq=0 ttl=64 time=5.8 ms&#10;64 bytes from 10.252.2.90: icmp_seq=1 ttl=64 time=5.8 ms&#10;64 bytes from 10.252.2.90: icmp_seq=2 ttl=64 time=5.8 ms&#10;64 bytes from 10.252.2.90: icmp_seq=3 ttl=64 time=5.8 ms&#10;64 bytes from 10.252.2.90: icmp_seq=4 ttl=64 time=5.7 ms&#10;&#10;&#45;-- 10.252.2.90 ping statistics ---&#10;5 packets transmitted, 5 packets received, 0% packet loss&#10;round-trip min/avg/max = 5.7/5.7/5.8 ms&#10;</code></pre>
<h4 id="mwan-ipsec-tun2">MWAN_IPsec_Tun2</h4>
<pre><code class="language-txt">fortigate # execute ping 10.252.2.92&#10;PING 10.252.2.92 (10.252.2.92): 56 data bytes&#10;64 bytes from 10.252.2.92: icmp_seq=0 ttl=64 time=6.1 ms&#10;64 bytes from 10.252.2.92: icmp_seq=1 ttl=64 time=6.1 ms&#10;64 bytes from 10.252.2.92: icmp_seq=2 ttl=64 time=6.1 ms&#10;64 bytes from 10.252.2.92: icmp_seq=3 ttl=64 time=6.1 ms&#10;64 bytes from 10.252.2.92: icmp_seq=4 ttl=64 time=6.0 ms&#10;&#10;&#45;-- 10.252.2.92 ping statistics ---&#10;5 packets transmitted, 5 packets received, 0% packet loss&#10;round-trip min/avg/max = 6.0/6.0/6.1 ms&#10;</code></pre>
<h3 id="zone-objects-optional">Zone objects (optional)</h3>
<p>This sample configuration assumes there are three zones configured on the FortiGate firewall. These zone objects are used in the policies referenced later in this document:</p>
<ul>
<li><code>Trust_Zone</code>: Contains the LAN interface(s).</li>
<li><code>Untrust_Zone</code>: Contains the WAN interface.</li>
<li><code>Cloudflare_Zone</code>: Contains both IPsec Tunnel interfaces.</li>
</ul>
<pre><code class="language-txt">fortigate # config system zone&#10;    edit &quot;Cloudflare_Zone&quot;&#10;        set intrazone allow&#10;        set interface &quot;MWAN_IPsec_Tun1&quot; &quot;MWAN_IPsec_Tun2&quot;&#10;    next&#10;    edit &quot;Trust_Zone&quot;&#10;        set intrazone allow&#10;        set interface &quot;internal&quot;&#10;    next&#10;    edit &quot;Untrust_Zone&quot;&#10;        set intrazone allow&#10;        set interface &quot;wan1&quot;&#10;    next&#10;end&#10;</code></pre>
<h3 id="create-address-objects">Create Address Objects</h3>
<p>Create Address Objects to represent the <a href="https://www.cloudflare.com/ips">Cloudflare IPv4 address space</a> as well as objects for the bidirectional health check anycast IPs:</p>
<pre><code class="language-txt">config firewall address&#10;    edit &quot;Cloudflare_IPv4_01&quot;&#10;        set color 9&#10;        set subnet 173.245.48.0 255.255.240.0&#10;    next&#10;    edit &quot;Cloudflare_IPv4_02&quot;&#10;        set color 9&#10;        set subnet 103.21.244.0 255.255.252.0&#10;    next&#10;    edit &quot;Cloudflare_IPv4_03&quot;&#10;        set color 9&#10;        set subnet 103.22.200.0 255.255.252.0&#10;    next&#10;    edit &quot;Cloudflare_IPv4_04&quot;&#10;        set color 9&#10;        set subnet 103.31.4.0 255.255.252.0&#10;    next&#10;    edit &quot;Cloudflare_IPv4_05&quot;&#10;        set color 9&#10;        set subnet 141.101.64.0 255.255.192.0&#10;    next&#10;    edit &quot;Cloudflare_IPv4_06&quot;&#10;        set color 9&#10;        set subnet 108.162.192.0 255.255.192.0&#10;    next&#10;    edit &quot;Cloudflare_IPv4_07&quot;&#10;        set color 9&#10;        set subnet 190.93.240.0 255.255.240.0&#10;    next&#10;    edit &quot;Cloudflare_IPv4_08&quot;&#10;        set color 9&#10;        set subnet 188.114.96.0 255.255.240.0&#10;    next&#10;    edit &quot;Cloudflare_IPv4_09&quot;&#10;        set color 9&#10;        set subnet 197.234.240.0 255.255.252.0&#10;    next&#10;    edit &quot;Cloudflare_IPv4_10&quot;&#10;        set color 9&#10;        set subnet 198.41.128.0 255.255.128.0&#10;    next&#10;    edit &quot;Cloudflare_IPv4_11&quot;&#10;        set color 9&#10;        set subnet 162.158.0.0 255.254.0.0&#10;    next&#10;    edit &quot;Cloudflare_IPv4_12&quot;&#10;        set color 9&#10;        set subnet 104.16.0.0 255.248.0.0&#10;    next&#10;    edit &quot;Cloudflare_IPv4_13&quot;&#10;        set color 9&#10;        set subnet 104.24.0.0 255.252.0.0&#10;    next&#10;    edit &quot;Cloudflare_IPv4_14&quot;&#10;        set color 9&#10;        set subnet 172.64.0.0 255.248.0.0&#10;    next&#10;    edit &quot;Cloudflare_IPv4_15&quot;&#10;        set color 9&#10;        set subnet 131.0.72.0 255.255.252.0&#10;    next&#10;    edit &quot;Bidirect_HC_Endpoint_01&quot;&#10;        set comment &quot;Bidirectional health check endpoint address&quot;&#10;        set color 9&#10;        set subnet 172.64.240.253 255.255.255.255&#10;    next&#10;    edit &quot;Bidirect_HC_Endpoint_02&quot;&#10;        set comment &quot;Bidirectional health check endpoint address&quot;&#10;        set color 9&#10;        set subnet 172.64.240.254 255.255.255.255&#10;    next&#10;end&#10;</code></pre>
<h3 id="configure-address-group-object">Configure Address Group Object</h3>
<p>Create an Address Object that contains all Cloudflare IPv4 subnets. Copy and paste the following CLI commands into an SSH terminal to create the objects automatically:</p>
<pre><code class="language-txt">config firewall addrgrp&#10;    edit &quot;Cloudflare_IPv4_Nets&quot;&#10;        set member &quot;Cloudflare_IPv4_01&quot; &quot;Cloudflare_IPv4_02&quot; &quot;Cloudflare_IPv4_03&quot; &quot;Cloudflare_IPv4_04&quot; &quot;Cloudflare_IPv4_05&quot; &quot;Cloudflare_IPv4_06&quot; &quot;Cloudflare_IPv4_07&quot; &quot;Cloudflare_IPv4_08&quot; &quot;Cloudflare_IPv4_09&quot; &quot;Cloudflare_IPv4_10&quot; &quot;Cloudflare_IPv4_11&quot; &quot;Cloudflare_IPv4_12&quot; &quot;Cloudflare_IPv4_13&quot; &quot;Cloudflare_IPv4_14&quot; &quot;Cloudflare_IPv4_15&quot;&#10;        set color 9&#10;    next&#10;end&#10;</code></pre>
<h3 id="add-security-policy">Add security policy</h3>
<p>Add a firewall rule to permit the ICMP traffic associated with the reply style bidirectional health checks.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5613.md")
</aside>
<pre><code class="language-txt">fortigate (policy) # show&#10;config firewall policy&#10;    edit 2&#10;        set name &quot;CF_Magic_Health_Checks&quot;&#10;        set uuid 80eb76ce-3033-51ee-c5e5-d5a670dff3b3&#10;        set srcintf &quot;Cloudflare_Zone&quot;&#10;        set action accept&#10;        set srcaddr &quot;Cloudflare_IPv4_Nets&quot;&#10;        set dstaddr &quot;Bidirect_HC_Endpoint_01&quot; &quot;Bidirect_HC_Endpoint_02&quot;&#10;        set schedule &quot;always&quot;&#10;        set service &quot;ALL_ICMP&quot;&#10;        set logtraffic all&#10;    next&#10;end&#10;</code></pre>
<h3 id="policy-based-routing">Policy-based routing</h3>
<p>Add policy-based routing rules to ensure traffic associated with bidirectional health checks received over an IPsec tunnel returns across the same tunnel.</p>
<p>Add two policy-based routing rules, one for each of the two IPsec tunnels.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5612.md")
</aside>
<pre><code class="language-txt">fortigate # config router policy&#10;    edit 1&#10;        set input-device &quot;MWAN_IPsec_Tun1&quot;&#10;        set srcaddr &quot;all&quot;&#10;        set dstaddr &quot;all&quot;&#10;        set gateway 10.252.2.90&#10;        set output-device &quot;MWAN_IPsec_Tun1&quot;&#10;    next&#10;    edit 2&#10;        set input-device &quot;MWAN_IPsec_Tun2&quot;&#10;        set srcaddr &quot;all&quot;&#10;        set dstaddr &quot;all&quot;&#10;        set gateway 10.252.2.92&#10;        set output-device &quot;MWAN_IPsec_Tun2&quot;&#10;    next&#10;end&#10;</code></pre>
<h2 id="monitor-cloudflare-ipsec-tunnel-health-checks">Monitor Cloudflare IPsec tunnel health checks</h2>
<p>The Cloudflare dashboard monitors the health of all anycast tunnels on your account that route traffic from Cloudflare to your origin network. Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/check-tunnel-health-dashboard/">Check tunnel health in the dashboard</a> for more information.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="packet-capture">Packet Capture</h3>
<p>Packet captures determine whether the policy-based routing rules are working as expected.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5611.md")
</aside>
<p>Traffic ingressing Tunnel 01 of 02 should egress the same tunnel, as shown in the following example:</p>
<pre><code class="language-txt">fortigate # diagnose sniffer packet any &#x27;host 172.64.240.253&#x27; 4&#10;interfaces=[any]&#10;filters=[host 172.64.240.253]&#10;0.601569 MWAN_IPsec_Tun1 in 172.64.240.253 -&gt; 162.158.176.118: icmp: echo reply&#10;0.601585 MWAN_IPsec_Tun1 out 172.64.240.253 -&gt; 162.158.176.118: icmp: echo reply&#10;0.611164 MWAN_IPsec_Tun1 in 172.64.240.253 -&gt; 172.71.87.94: icmp: echo reply&#10;0.611178 MWAN_IPsec_Tun1 out 172.64.240.253 -&gt; 172.71.87.94: icmp: echo reply&#10;0.617562 MWAN_IPsec_Tun1 in 172.64.240.253 -&gt; 172.71.129.214: icmp: echo reply&#10;0.617574 MWAN_IPsec_Tun1 out 172.64.240.253 -&gt; 172.71.129.214: icmp: echo reply&#10;0.622042 MWAN_IPsec_Tun1 in 172.64.240.253 -&gt; 172.69.61.43: icmp: echo reply&#10;0.622056 MWAN_IPsec_Tun1 out 172.64.240.253 -&gt; 172.69.61.43: icmp: echo reply&#10;0.624092 MWAN_IPsec_Tun1 in 172.64.240.253 -&gt; 172.68.9.214: icmp: echo reply&#10;</code></pre>
<p>Conversely, traffic ingressing Tunnel 02 of 02 should egress the same tunnel:</p>
<pre><code class="language-txt">fortigate # diagnose sniffer packet any &#x27;host 172.64.240.254&#x27; 4&#10;interfaces=[any]&#10;filters=[host 172.64.240.254]&#10;0.912041 MWAN_IPsec_Tun2 in 172.64.240.254 -&gt; 172.70.177.56: icmp: echo reply&#10;0.912057 MWAN_IPsec_Tun2 out 172.64.240.254 -&gt; 172.70.177.56: icmp: echo reply&#10;0.913579 MWAN_IPsec_Tun2 in 172.64.240.254 -&gt; 172.70.221.154: icmp: echo reply&#10;0.913592 MWAN_IPsec_Tun2 out 172.64.240.254 -&gt; 172.70.221.154: icmp: echo reply&#10;0.914247 MWAN_IPsec_Tun2 in 172.64.240.254 -&gt; 162.158.1.85: icmp: echo reply&#10;0.914260 MWAN_IPsec_Tun2 out 172.64.240.254 -&gt; 162.158.1.85: icmp: echo reply&#10;0.918533 MWAN_IPsec_Tun2 in 172.64.240.254 -&gt; 172.71.125.75: icmp: echo reply&#10;0.918550 MWAN_IPsec_Tun2 out 172.64.240.254 -&gt; 172.71.125.75: icmp: echo reply&#10;0.924465 MWAN_IPsec_Tun2 in 172.64.240.254 -&gt; 172.69.21.134: icmp: echo reply&#10;</code></pre>
<h3 id="flow-debugging">Flow Debugging</h3>
<p>Flow debugging helps determine whether traffic is ingressing/egressing the firewall via the expected path. It provides more detail than the sniffer packet captures in the previous section, but creates substantial logging and should only be enabled when absolutely necessary.</p>
<p>Additionally, customers will likely need to contact Fortinet technical support for assistance with interpreting the flow debug logs, as well as to obtain recommendations in terms of how to configure FortiGate to ensure flows are routed correctly based on the application's requirements.</p>
<pre><code class="language-txt">fortigate # diagnose debug disable&#10;fortigate # diagnose debug flow filter clear&#10;fortigate # diagnose debug reset&#10;fortigate # diagnose debug flow filter addr 172.64.240.253&#10;fortigate # diagnose debug show flow show function-name enable&#10;fortigate # diagnose debug config-error-log timestamps enable&#10;fortigate # diagnose debug flow trace start 999&#10;fortigate # diagnose debug enable&#10;fortigate # 2023-08-01 09:27:26 id=20085 trace_id=2871 func=print_pkt_detail line=5844 msg=&quot;vd-root:0 received a packet(proto=1, 172.64.240.253:56968-&gt;172.70.121.28:0) tun_id=162.159.67.210 from MWAN_IPsec_Tun1. type=0, code=0, id=56968, seq=0.&quot;&#10;2023-08-01 09:27:26 id=20085 trace_id=2871 func=rpdb_srv_match_input line=1036 msg=&quot;Match policy routing id=1: to 10.252.2.90 via ifindex-34&quot;&#10;2023-08-01 09:27:26 id=20085 trace_id=2871 func=vf_ip_route_input_common line=2605 msg=&quot;find a route: flag=00000000 gw-162.159.67.210 via MWAN_IPsec_Tun1&quot;&#10;2023-08-01 09:27:26 id=20085 trace_id=2871 func=ipsecdev_hard_start_xmit line=669 msg=&quot;enter IPSec interface MWAN_IPsec_Tun1, tun_id=0.0.0.0&quot;&#10;2023-08-01 09:27:26 id=20085 trace_id=2871 func=_do_ipsecdev_hard_start_xmit line=229 msg=&quot;output to IPSec tunnel MWAN_IPsec_Tun1&quot;&#10;2023-08-01 09:27:26 id=20085 trace_id=2871 func=esp_output4 line=844 msg=&quot;IPsec encrypt/auth&quot;&#10;2023-08-01 09:27:26 id=20085 trace_id=2871 func=ipsec_output_finish line=544 msg=&quot;send to 172.71.91.34 via intf-wan1&quot;&#10;2023-08-01 09:27:26 id=20085 trace_id=2872 func=print_pkt_detail line=5844 msg=&quot;vd-root:0 received a packet(proto=1, 172.64.240.253:18685-&gt;162.158.209.64:0) tun_id=162.159.67.210 from MWAN_IPsec_Tun1. type=0, code=0, id=18685, seq=0.&quot;&#10;2023-08-01 09:27:26 id=20085 trace_id=2872 func=rpdb_srv_match_input line=1036 msg=&quot;Match policy routing id=1: to 10.252.2.90 via ifindex-34&quot;&#10;2023-08-01 09:27:26 id=20085 trace_id=2872 func=vf_ip_route_input_common line=2605 msg=&quot;find a route: flag=00000000 gw-162.159.67.210 via MWAN_IPsec_Tun1&quot;&#10;2023-08-01 09:27:26 id=20085 trace_id=2872 func=ipsecdev_hard_start_xmit line=669 msg=&quot;enter IPSec interface MWAN_IPsec_Tun1, tun_id=0.0.0.0&quot;&#10;2023-08-01 09:27:26 id=20085 trace_id=2872 func=_do_ipsecdev_hard_start_xmit line=229 msg=&quot;output to IPSec tunnel MWAN_IPsec_Tun1&quot;&#10;2023-08-01 09:27:26 id=20085 trace_id=2872 func=esp_output4 line=844 msg=&quot;IPsec encrypt/auth&quot;&#10;2023-08-01 09:27:26 id=20085 trace_id=2872 func=ipsec_output_finish line=544 msg=&quot;send to 172.71.91.34 via intf-wan1&quot;&#10;</code></pre>
<h3 id="disable-flow-debugging">Disable Flow Debugging</h3>
<p>The typical use of <code>CTRL + C</code> will not stop Flow Debugging.</p>
<p>You can disable Flow Debugging simply by typing the following at any point while the debug logs are scrolling by:</p>
<pre><code class="language-txt">fortigate # diagnose debug disable&#10;</code></pre>
