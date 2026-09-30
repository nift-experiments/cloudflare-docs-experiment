<p>Before you can begin using Magic Transit, complete the following onboarding steps. Cloudflare can significantly accelerate this timeline during active-attack scenarios.</p>
<h2 id="scope-your-configuration">Scope your configuration</h2>
<p>Magic Transit is not a self-serve product. Start by <a href="https://www.cloudflare.com/network-services/products/magic-transit/">engaging with our team</a> to assess your needs and implementation timeline. During this assessment, Cloudflare reviews specific requirements such as your prefix count and how fast you can go through the necessary steps to implement Magic Transit on your network.</p>
<h2 id="ips">IPs</h2>
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
@markup("md", "content/.markup/bodies/775.md")
</div>. When using Cloudflare-leased IPs, Cloudflare automatically enables [Magic Transit Egress](/magic-transit/reference/egress/), which routes your egress traffic to Cloudflare instead of the Internet. Set up policy-based routing on your end to ensure return traffic routes properly.
<h2 id="verify-router-compatibility">Verify router compatibility</h2>
<p>Magic Transit relies on <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/776.md")
</div> tunnels to transmit <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/777.md")
</div> from Cloudflare's global network to your origin network.
<p>The routers at your tunnel endpoints must meet the following requirements for Magic Transit compatibility.</p>
<ul>
<li>Support GRE tunnels (or IPsec if GRE is not available).</li>
<li>Support at least one tunnel per Internet service provider (ISP).</li>
<li>Support <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/778.md")
</div> clamping.
- Support asymmetric traffic flow (for ingress-only Magic Transit).
<h2 id="draft-letter-of-agency">Draft Letter of Agency</h2>
<p>Draft a <a href="/byoip/concepts/loa/">Letter of Agency (LOA)</a> that identifies the prefixes you want to advertise and authorizes Cloudflare to announce them. Our transit providers require the LOA so they can accept the routes we advertise on your behalf.</p>
<p>If you are an Internet service provider (ISP) and advertising <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/779.md")
</div> on behalf of a customer, you need an LOA for the ISP and for the customer.
<p>If you are using a <a href="#ips">Cloudflare IP address</a>, you do not need to submit an LOA.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/774.md")
</aside>
<h3 id="example-of-a-letter-of-agency">Example of a Letter of Agency</h3>
<pre><code class="language-txt">[COMPANY LETTERHEAD]&#10;&#10;LETTER OF AGENCY (&quot;LOA&quot;)&#10;&#10;[DATE]&#10;&#10;&#10;To whom it may concern:&#10;&#10;[COMPANY NAME] (the &quot;Company&quot;) authorizes Cloudflare, Inc. with AS13335 to advertise the following IP address blocks / originating ASNs:&#10;&#10;&#45; - - - - - - - - - - - - - - - - - -&#10;[Subnet &amp; Originating ASN]&#10;[Subnet &amp; Originating ASN]&#10;[Subnet &amp; Originating ASN]&#10;&#45; - - - - - - - - - - - - - - - - - -&#10;&#10;As a representative of the Company that is the owner of the aforementioned IP address blocks / originating ASNs, I hereby declare that I am authorized to sign this LOA on the Company’s behalf.&#10;&#10;Should you have any questions please email me at [E-MAIL ADDRESS], or call: [TELEPHONE NUMBER]&#10;&#10;Regards,&#10;&#10;&#10;[SIGNATURE]&#10;&#10;&#10;[NAME TYPED]&#10;[TITLE]&#10;[COMPANY NAME]&#10;[COMPANY ADDRESS]&#10;[COMPANY STAMP]&#10;</code></pre>
<h2 id="verify-irr-entries">Verify IRR entries</h2>
<p>Verify that your Internet Routing Registry (IRR) entries match your corresponding origin autonomous system numbers (ASNs) to ensure Magic Transit routes traffic to the correct autonomous systems (AS). For guidance, refer to <a href="/byoip/concepts/irr-entries/best-practices/#verify-an-irr-entry">Verify IRR entries</a>.</p>
<p>If you are using a <a href="#ips">Cloudflare IP</a>, you do not need to verify your IRR entries.</p>
<h3 id="optional-rpki-check-for-prefix-validation">Optional: RPKI check for prefix validation</h3>
<p>You can also use the Resource Public Key Infrastructure (RPKI) as an additional option to validate your prefixes. RPKI is a <a href="https://blog.cloudflare.com/rpki/">security framework method</a> that associates a route with an autonomous system. It uses cryptography to validate the information before being passed to the routers.</p>
<p>If you operate a network (ISP, cloud provider, enterprise, and others), using RPKI ensures that routers correctly recognize your IP prefixes. This prevents service disruptions and protects your brand's reputation. Without RPKI, attackers could announce your IP space, misdirect your traffic, and potentially harm your business.</p>
<p>To check your prefixes, you can use <a href="https://rpki.cloudflare.com/?view=validator">Cloudflare's RPKI Portal</a>.</p>
<h2 id="set-maximum-segment-size">Set maximum segment size</h2>
<p>Before enabling Magic Transit, you must make sure that you set up the maximum segment size on your network. Cloudflare Magic Transit uses tunnels to deliver <a href="https://www.cloudflare.com/learning/network-layer/what-is-a-packet/">packets</a> from our global network to your data centers. Cloudflare encapsulates these packets adding new headers. You must account for the space consumed by these headers when configuring the maximum transmission unit (MTU) and maximum segment size (MSS) values for your network.</p>
<h3 id="mss-clamping-recommendations">MSS clamping recommendations</h3>
<h4 id="gre-tunnels-as-off-ramp">GRE tunnels as off-ramp</h4>
<p>The MSS value depends on how your network is set up.</p>
<ul>
<li>
<p><strong>Magic Transit ingress-only traffic (DSR):</strong></p>
<ul>
<li><strong>On your edge router transit ports</strong>: Set a TCP MSS clamp to a maximum of 1,436 bytes.</li>
<li><strong>On any IPsec/GRE tunnels with third parties on your Magic Transit prefix</strong>: Apply the MSS clamp on the internal tunnel interface (most likely on a separate firewall behind the GRE-terminating router) to reduce the current value by 24 bytes.</li>
</ul>
</li>
<li>
<p><strong>For Magic Transit ingress + egress traffic:</strong></p>
<ul>
<li><strong>On the Magic Transit GRE tunnel internal interface</strong>: Meaning where the Magic Transit egress traffic will traverse. Your devices may do this automatically once the tunnel is configured, but it depends on your devices. Set the TCP MSS clamp to 1,436 bytes maximum.</li>
<li><strong>On any IPsec/GRE tunnels with third parties on your Magic Transit prefix</strong>: On the internal tunnel interface (most likely on a separate firewall behind the GRE-terminating router) to reduce its current value by 24 bytes.</li>
</ul>
</li>
</ul>
<h4 id="ipsec-tunnels">IPsec tunnels</h4>
<p>For IPsec tunnels, the value you need to specify depends on how your network is set up. The MSS clamping value is lower than for GRE tunnels because the physical interface sees IPsec-encrypted <a href="https://www.cloudflare.com/learning/network-layer/what-is-a-packet/">packets</a>, not TCP packets, and MSS clamping does not apply to those.</p>
<ul>
<li>
<p><strong>Magic Transit ingress-only traffic (DSR):</strong></p>
<ul>
<li><strong>On your edge router transit ports</strong>: Set the TCP MSS clamp to 1,436 bytes maximum.</li>
<li><strong>On any IPsec/GRE tunnels with third parties on your Magic Transit prefix</strong>: On the internal tunnel interface (most likely on a separate firewall behind the GRE-terminating router) to reduce its current value by 140 bytes.</li>
</ul>
</li>
<li>
<p><strong>Magic Transit ingress + egress traffic:</strong></p>
<ul>
<li><strong>On your edge router</strong>: Apply this on your Magic Transit IPsec tunnel internal interface (that is, where the Magic Transit egress traffic will traverse). Your devices may do this automatically once the tunnel is configured, but it depends on your devices. Set the TCP MSS clamp to 1,360 bytes maximum.</li>
<li><strong>On any IPsec/GRE tunnels with third parties on your Magic Transit prefix</strong>: On the internal tunnel interface (most likely on a separate firewall behind the IPsec-terminating device in your premises) to reduce its current value by 140 bytes.</li>
</ul>
</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/773.md")
</aside>
<p>Refer to <a href="/magic-transit/reference/mtu-mss/">Maximum transmission unit and maximum segment size</a> for more details.</p>
<h4 id="clear-do-not-fragment-df">Clear Do not fragment (DF)</h4>
<p>If you are unable to set the MSS on your physical interfaces to a value lower than 1500 bytes, you can clear the <code>do not fragment</code> bit in the IP header. When this option is enabled, Cloudflare fragments <a href="https://www.cloudflare.com/learning/network-layer/what-is-a-packet/">packets</a> greater than 1500 bytes, and the packets are reassembled on your infrastructure after decapsulation. In most environments, enabling this option does not have a significant impact on traffic throughput.</p>
<p>To enable this option for your network, contact your account team.</p>
<p>Refer to <a href="/magic-transit/reference/mtu-mss/">Maximum transmission unit and maximum segment size</a> for more details.</p>
<h2 id="follow-router-vendor-guidelines">Follow router vendor guidelines</h2>
<p>Instructions to adjust MSS by applying MSS clamps vary depending on the vendor of your router.</p>
<p>The following table lists several commonly used router vendors with links to MSS clamping instructions:</p>
<table>
<thead>
<tr>
<th>Router device</th>
<th>URL</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cisco</td>
<td><a href="https://www.cisco.com/en/US/docs/ios-xml/ios/ipapp/command/ip_tcp_adjust-mss_through_ip_wccp_web-cache_accelerated.html#GUID-68044D35-A53E-42C1-A7AB-9236333DA8C4">TCP IP Adjust MSS</a></td>
</tr>
<tr>
<td>Juniper</td>
<td><a href="https://www.juniper.net/documentation/en_US/junos/topics/reference/configuration-statement/tcp-mss-edit-system.html">TCP MSS - Edit System</a></td>
</tr>
</tbody>
</table>
<h2 id="configure-tunnels">Configure tunnels</h2>
<p><a href="/magic-transit/how-to/configure-tunnel-endpoints/">Configure the tunnels</a> on both the Cloudflare side and your router side to connect to your origin infrastructure.</p>
<h2 id="configure-static-routes-or-bgp-peering-beta">Configure static routes or BGP peering (beta)</h2>
<p>Configure <a href="/magic-transit/how-to/configure-routes/#configure-static-routes">static routes</a> or <a href="/magic-transit/how-to/configure-routes/#configure-bgp-routes">BGP peering</a> to route traffic from Cloudflare's global network to your locations.</p>
<h2 id="run-pre-flight-checks">Run pre-flight checks</h2>
<p>After setting up your tunnels and routes, Cloudflare validates:</p>
<ul>
<li>Tunnel connectivity</li>
<li>Tunnel and endpoint <a href="/magic-transit/reference/tunnel-health-checks/#tunnel-health-checks">health checks</a></li>
<li>
<div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
</li>
</ul>
@markup("md", "content/.markup/bodies/780.md")
</div>
- Internet Routing Registry (IRR)
- <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/781.md")
</div>
<p>Cloudflare applies configurations to the global network, which takes around one day to roll out.</p>
<h2 id="advertise-prefixes">Advertise prefixes</h2>
<p>Once pre-flight checks are completed, Cloudflare unlocks your <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/782.md")
</div> for you to [advertise via the dashboard, API or BGP](/magic-transit/how-to/advertise-prefixes/) at a time of your choosing. Refer to [Dynamic advertisement best practices](/byoip/concepts/dynamic-advertisement/best-practices/) to learn more about advertising prefixes.
<p>If you are using a Cloudflare IP, you do not need to advertise your prefixes.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/772.md")
</aside>
<h2 id="next-steps">Next steps</h2>
<p>After your prefixes are advertised, configure your DDoS protection settings:</p>
<ol>
<li>Review and customize your <a href="/magic-transit/ddos/">DDoS protection</a> settings, including <a href="/ddos-protection/managed-rulesets/network/">network-layer DDoS managed rulesets</a>.</li>
<li>If your network handles TCP traffic, enable <a href="/ddos-protection/advanced-ddos-systems/overview/advanced-tcp-protection/">Advanced TCP Protection</a>. If your network receives DNS over UDP traffic, enable <a href="/ddos-protection/advanced-ddos-systems/overview/advanced-dns-protection/">Advanced DNS Protection</a>. These systems provide stateful analysis beyond the managed rulesets.</li>
</ol>
