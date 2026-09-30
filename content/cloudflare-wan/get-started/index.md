<p>Cloudflare WAN (formerly Magic WAN) allows you to achieve any-to-any connectivity across branch and retail sites and data centers, with the Cloudflare connectivity cloud.</p>
<p>If you are migrating from MPLS or a traditional WAN, refer to <a href="/cloudflare-wan/wan-transformation/">WAN transformation</a> to compare approaches and plan an incremental migration.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>Cloudflare WAN is an Enterprise-only product. <a href="https://www.cloudflare.com/magic-wan/">Contact Cloudflare</a> to acquire Cloudflare WAN. If you plan on using Cloudflare One Appliance to automatically onboard your locations to Cloudflare, you will need to purchase Cloudflare WAN first.</p>
<h2 id="set-up-method">Set up method</h2>
<p>Cloudflare WAN supports an automatic setup and a manual setup. The automatic setup through Cloudflare One Appliance is the preferred method.</p>
<h3 id="automatic-setup">Automatic setup</h3>
<p>Setting up Cloudflare WAN automatically is done through Cloudflare One Appliance, and is the preferred method. You can choose between the hardware version and the virtual version of Cloudflare One Appliance. The virtual version can be installed on your own machines.</p>
<p>If you plan on using Cloudflare One Appliance, you can skip the prerequisites below, and refer to <a href="/cloudflare-wan/configuration/appliance/">Configure with Cloudflare One Appliance</a> for more information on how to continue.</p>
<h3 id="manual-setup">Manual setup</h3>
<p>Setting up Cloudflare WAN manually is done through a combination of third-party devices in your premises and the Cloudflare dashboard. To be successful, you need to:</p>
<ol>
<li>Read the <a href="#prerequisites">Prerequisites</a> below.</li>
<li>Follow the steps in <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">Manual configuration</a>.</li>
</ol>
<h2 id="prerequisites">Prerequisites</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1287.md")
</aside>
<h3 id="use-compatible-tunnel-endpoint-routers">Use compatible tunnel endpoint routers</h3>
<p>Cloudflare WAN relies on <a href="/cloudflare-wan/reference/gre-ipsec-tunnels/">GRE</a> and <a href="/cloudflare-wan/reference/gre-ipsec-tunnels/#ipsec-tunnels">IPsec tunnels</a> to transmit <a href="https://www.cloudflare.com/learning/network-layer/what-is-a-packet/">packets</a> from Cloudflare's global network to your origin network. To ensure compatibility with Cloudflare WAN, the routers at your tunnel endpoints must:</p>
<ul>
<li>Allow configuration of at least one tunnel per Internet service provider (ISP).</li>
<li>Support <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></li>
</ul>
@markup("md", "content/.markup/bodies/1288.md")
</div> clamping.
- Support the configuration parameters for IPsec mentioned in [IPsec tunnels](/cloudflare-wan/reference/gre-ipsec-tunnels/#supported-configuration-parameters).
<h3 id="set-maximum-segment-size">Set maximum segment size</h3>
<p>Before enabling Cloudflare WAN, you must make sure that you set up the maximum segment size on your network. Cloudflare Cloudflare WAN uses tunnels to deliver <a href="https://www.cloudflare.com/learning/network-layer/what-is-a-packet/">packets</a> from our global network to your data centers. Cloudflare encapsulates these packets adding new headers. You must account for the space consumed by these headers when configuring the maximum transmission unit (MTU) and maximum segment size (MSS) values for your network.</p>
<h4 id="mss-clamping-recommendations">MSS clamping recommendations</h4>
<h5 id="gre-tunnels-as-off-ramp">GRE tunnels as off-ramp</h5>
<p>The MSS value depends on how your network is set up.</p>
<ul>
<li><strong>On your edge router</strong>: Apply the clamp to the GRE tunnel internal interface (meaning where the egress traffic will traverse). Set the MSS clamp to 1,436 bytes. Your devices may do this automatically once the tunnel is configured, but it depends on your devices.</li>
</ul>
<h5 id="ipsec-tunnels">IPsec tunnels</h5>
<p>For IPsec tunnels, the value you need to specify depends on how your network is set up. The MSS clamping value is lower than for GRE tunnels because the physical interface sees IPsec-encrypted packets, not TCP packets, and MSS clamping does not apply to those.</p>
<ul>
<li><strong>On your edge router</strong>: Apply this on your IPsec tunnel internal interface (meaning where the egress traffic will traverse). Your devices may do this automatically once the tunnel is configured, but it depends on your devices. Set the TCP MSS clamp to 1,360 bytes maximum.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/1286.md")
</aside>
<p>Refer to <a href="/cloudflare-wan/reference/mtu-mss/">Maximum transmission unit and maximum segment size</a> for more details.</p>
<h3 id="follow-router-vendor-guidelines">Follow router vendor guidelines</h3>
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
