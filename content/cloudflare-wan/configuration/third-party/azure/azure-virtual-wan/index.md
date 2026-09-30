<p>This tutorial provides information on how to connect Cloudflare WAN (formerly Magic WAN) to a Microsoft Azure Virtual WAN hub.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>You will need to have an existing Resource group, Virtual Network, and Virtual Machine created in your Azure account. Refer to <a href="https://learn.microsoft.com/en-us/azure/virtual-network/">Microsoft's documentation</a> to learn more on how to create these.</p>
<h2 id="start-azure-configuration">Start Azure configuration</h2>
<h3 id="1-create-a-virtual-wan"><ol>
<li>Create a Virtual WAN</li>
</ol></h3>
<p>To connect one or more VNets to Cloudflare WAN via a Virtual WAN hub, you first need to create a Virtual WAN (vWAN) resource representing your Azure network. If you already have a vWAN that you wish to connect to Cloudflare WAN, continue to the next step. Refer to <a href="https://learn.microsoft.com/en-us/azure/virtual-wan/virtual-wan-site-to-site-portal#openvwan">Microsoft's documentation</a> to learn more.</p>
<ol>
<li>In the Azure portal, go to your <strong>Virtual WANs</strong> page.</li>
<li>Select the option to create a <strong>Virtual WAN</strong>.</li>
<li>Create a Virtual WAN with the <strong>Type</strong> set to <strong>Standard</strong>.</li>
</ol>
<h3 id="2-create-a-virtual-wan-hub"><ol start="2">
<li>Create a Virtual WAN Hub</li>
</ol></h3>
<p>Using traditional hub and spoke terminology, a Virtual WAN Hub deployed within a vWAN is the hub to which your VNet(s) and Cloudflare WAN attach as spokes. The vWAN hub deployed in this step will contain a VPN Gateway for connecting to Cloudflare WAN.</p>
<ol>
<li>Create a <strong>Virtual WAN Hub</strong>.</li>
<li>In <strong>Basics</strong>:
<ol>
<li>Select your resource group as well as your desired region, capacity, and hub routing preference. Microsoft recommends using the default hub routing preference of <strong>ExpressRoute</strong> unless you have a specific need to change this setting. Refer to <a href="https://learn.microsoft.com/en-us/azure/virtual-wan/about-virtual-hub-routing-preference">Microsoft's documentation</a> to learn more about Azure hub routing preferences.</li>
<li>Configure the <strong>Hub Private Address Space</strong>. Choose an <a href="https://learn.microsoft.com/en-us/azure/virtual-wan/virtual-wan-site-to-site-portal#hub">address space with a subnet mask of <code>/24</code> or greater</a> that does not overlap with the address spaces of any VNets you wish to attach to the vWAN Hub, nor with any of your Cloudflare WAN sites.</li>
</ol>
</li>
<li>In <strong>Site to Site</strong>:
<ol>
<li>In <strong>Do you want to create a Site to site (VPN gateway)?</strong> select <strong>Yes</strong>.</li>
<li>Select your desired <strong>Gateway scale units</strong> and <strong>Routing Preference</strong>. Refer to <a href="https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/routing-preference-overview#routing-via-microsoft-global-network">Microsoft's documentation</a> to learn more about Azure routing preferences.</li>
</ol>
</li>
<li>Select <strong>Create</strong>. Note that the deployment time for the vWAN Hub and VPN Gateway may take 30 minutes or more.</li>
<li>After the VPN Gateway has finished provisioning, go to <strong>Virtual WAN</strong> &gt; <strong>Hubs</strong> &gt; <strong>Your vHub</strong> &gt; <strong>Connectivity</strong> &gt; <strong>VPN (Site to site)</strong>.</li>
<li>In the <strong>Essentials</strong> dropdown select the VPN Gateway listed.</li>
<li>Select the JSON View for the VPN Gateway and take note of the JSON attributes at the paths <code>properties.ipConfigurations[0].publicIpAddress</code> and  <code>properties.ipConfigurations[1].publicIpAddress</code>. These will be the customer endpoints needed when configuring IPsec tunnels for Cloudflare WAN.</li>
</ol>
<h3 id="3-create-a-vpn-site"><ol start="3">
<li>Create a VPN site</li>
</ol></h3>
<p>A VPN site represents the remote site your Azure vWAN can reach through a VPN connection. This is typically an on-premises location. In this case, the VPN site represents Cloudflare WAN.</p>
<ol>
<li>Go to <strong>Virtual WAN</strong> &gt; <strong>VPN sites</strong> &gt; <strong>Create site</strong>.</li>
<li>In <strong>Basics</strong>:
<ol>
<li>Configure your desired region and name.</li>
<li>Configure the <strong>Device vendor</strong> as Cloudflare.</li>
<li>In <strong>Private address space</strong>, specify the address range(s) you wish to access from your vWAN through Cloudflare WAN. This could include other private networks connected to your Cloudflare WAN, or a default route (<code>0.0.0.0/0</code>) if you want Internet egress traffic to traverse Cloudflare WAN (that is, to be scanned by Cloudflare Gateway). The address space can be modified after VPN site creation.</li>
</ol>
</li>
<li>In <strong>Links</strong>:
<ol>
<li>Configure a single link. Provide a name, speed (in Mbps), and provider name (here, enter <code>Cloudflare</code>) for your link. For the <strong>Link IP address</strong>, enter your Cloudflare anycast address. The <strong>BGP address</strong> and <strong>ASN</strong> fields should be left empty. BGP is not supported at the time of writing this tutorial.</li>
</ol>
</li>
<li>Select <strong>Create</strong>.</li>
</ol>
<h3 id="4-configure-vpn-site-for-ipsec-tunnel-health-checks"><ol start="4">
<li>Configure VPN site for IPsec tunnel health checks</li>
</ol></h3>
<p>Cloudflare WAN uses <a href="/cloudflare-wan/reference/tunnel-health-checks/">Tunnel Health Checks</a> to monitor whether a tunnel is available.</p>
<p>Tunnel health checks make use of ICMP probes sent from the Cloudflare side of the IPsec tunnel to the remote endpoint (Azure). Probes are sent from the tunnel's interface address, which you specify in two places:</p>
<ul>
<li><strong>Cloudflare Dashboard:</strong> In your IPsec tunnel configuration as the address of the virtual tunnel interface (VTI) (so that Cloudflare knows what address to send probes from). Cloudflare requires this address in CIDR notation with a <code>/31</code> netmask.</li>
<li><strong>Azure Portal:</strong> In your VPN site's address space (so that Azure routes probe responses back over the tunnel). Azure requires this address in CIDR notation with a <code>/32</code> netmask.</li>
</ul>
<p>Cloudflare recommends that you select a unique <code>/31</code> subnet (<a href="https://datatracker.ietf.org/doc/html/rfc1918">RFC 1918 — Address Allocation for Private Internets</a>) for each IPsec tunnel which is treated as a Point-to-Point Link and provides the ideal addressing scheme to satisfy both requirements.</p>
<p>Example:</p>
<ul>
<li>Select <code>169.254.251.137/31</code> as your unique Point-to-Point Link subnet.</li>
<li>In the Cloudflare dashboard, set <code>169.254.251.137/31</code> as your tunnel's <strong>IPv4 Interface address</strong>. (Refer to <a href="#configure-cloudflare-wan">Configure Cloudflare WAN</a> below.)</li>
<li>In the Azure portal, add <code>169.254.251.137/32</code> to your VPN site's <strong>Private address space</strong>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7068.md")
</aside>
<p>To configure the Address Space for the Local Network Gateway to support Tunnel Health Checks:</p>
<ol>
<li>Go to <strong>Virtual WAN</strong> &gt; <strong>VPN sites</strong> &gt; <strong>Your VPN Site</strong> &gt; <strong>Edit site</strong> to edit the VPN site configured in the previous section.</li>
<li>Update the <strong>Private address space</strong> to include two <code>/32</code> subnets in CIDR notation as described above. When using Azure VPN Gateways with vWAN Hubs, a single VPN Gateway Connection maps to two Cloudflare WAN IPsec Tunnels. For this reason, we need to select two unique <code>/31</code> subnets, one for each Cloudflare IPsec Tunnel. The upper address of each <code>/31</code> is then added to the VPN Site's Private address space as a <code>/32</code>subnet.</li>
<li>Select <strong>Confirm</strong>.</li>
</ol>
<h3 id="5-create-a-virtual-network-connection"><ol start="5">
<li>Create a Virtual Network Connection</li>
</ol></h3>
<p>To connect your existing VNet to your newly created vHub:</p>
<ol>
<li>Go to <strong>Virtual WAN</strong> &gt; <strong>Virtual network connections</strong> and select <strong>Add connection</strong>.</li>
<li>Configure the connection to connect the desired VNet to the vHub created above.</li>
<li>Ensure that within the connection's <strong>Routing configuration</strong>:
<ol>
<li><strong>Propagate to none</strong> is set to <strong>No.</strong></li>
<li><strong>Bypass Next Hop IP for workloads within this VNet</strong> is set to <strong>No</strong></li>
<li>And <strong>Propagate static route</strong> is set to <strong>Yes</strong>.</li>
</ol>
</li>
<li>Select <strong>Create</strong>.</li>
</ol>
<h2 id="configure-cloudflare-wan">Configure Cloudflare WAN</h2>
<p>When connecting your Azure vHub VPN Gateway to Cloudflare WAN, you need to create two Cloudflare WAN IPsec tunnels to map to the single Azure VPN Gateway Connection created above. This is because Azure VPN Gateways are deployed with two public IP addresses.</p>
<ol>
<li>Create an <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/#add-tunnels">IPsec tunnel</a> in the Cloudflare dashboard.</li>
<li>Make sure you have the following settings:
<ol>
<li><strong>Interface address</strong>: Add the upper IP address within the first <code>/31</code> subnet selected in step 4 of the Start Azure Configuration section. Refer to <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">Tunnel endpoints</a> for more details.</li>
<li><strong>Customer endpoint</strong>: The first public IP associated with your Azure VPN Gateway. For example, <code>40.xxx.xxx.xxx</code>.</li>
<li><strong>Cloudflare endpoint</strong>: Use one of the Cloudflare anycast addresses assigned to your account, available in <a href="https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space">Leased IPs</a>. This will also be the IP address corresponding to the VPN Site in Azure. For example, <code>162.xxx.xxx.xxx</code>.</li>
<li><strong>Health check rate</strong>: Medium (default).</li>
<li><strong>Health check type</strong>: Reply (default).</li>
<li><strong>Health check direction</strong>: Bidirectional (default).</li>
<li><strong>Health check target</strong>: Custom; enter the customer endpoint.</li>
<li><strong>Add pre-shared key later</strong>: Select this option to create a PSK that will be used later in Azure.</li>
<li><strong>Replay protection</strong>: <strong>Enable</strong>.</li>
</ol>
</li>
<li>Edit the tunnel. Generate a new pre-shared key and copy the key to a safe location.</li>
<li>Create static routes for your Azure Virtual Network subnets, specifying the newly created tunnel as the next hop.</li>
<li>Create the second IPsec tunnel in the Cloudflare dashboard. Copy the configuration of the first tunnel with the following exceptions:
<ol>
<li><strong>Interface address</strong>: Add the upper IP address within the <strong>second</strong> <code>/31</code> subnet selected in step 4 of the Start Azure Configuration section.</li>
<li><strong>Customer endpoint</strong>: The <strong>second</strong> Public IP associated with your Azure VPN Gateway.</li>
<li><strong>Health check target</strong>: Enter the new customer endpoint as a custom target.</li>
<li><strong>Use my own pre-shared key</strong>: Select this option and enter the key generated for the first tunnel.</li>
</ol>
</li>
<li>Create static routes for your Azure Virtual Network subnets, specifying the newly created tunnel as the next hop. To use one tunnel as primary and the other as backup, give the primary tunnel's route a lower priority. To ECMP load balance across both tunnels, assign both routes the same priority.</li>
</ol>
<h2 id="finish-azure-configuration">Finish Azure Configuration</h2>
<h3 id="1-create-an-ipsec-vpn-gateway-connection"><ol>
<li>Create an IPsec VPN Gateway Connection</li>
</ol></h3>
<p>To create a <strong>VPN Gateway Connection</strong>:</p>
<ol>
<li>Go to <strong>Virtual WAN</strong> &gt; <strong>Hubs</strong> &gt; <strong>Your vHub</strong> &gt; <strong>Connectivity</strong> &gt; <strong>VPN (Site to site)</strong> and remove the default filter <strong>Hub association: Connected</strong> to display the <strong>VPN Site</strong> created above.</li>
<li>Check the box next to your VPN Site and select <strong>Connect VPN sites</strong>.</li>
</ol>
<p>Choose the following settings. These settings have been tested by Cloudflare. However, when setting up your VPN connection note that there are other configuration parameters are also technically feasible, as documented in the <a href="https://learn.microsoft.com/en-us/azure/virtual-wan/virtual-wan-ipsec">Azure documentation</a> and in the <a href="/cloudflare-wan/reference/gre-ipsec-tunnels/#supported-configuration-parameters">Cloudflare documentation</a>.</p>
<ol>
<li>
<p><strong>PSK</strong>: Provide the PSK generated by Cloudflare for your IPsec tunnels.</p>
</li>
<li>
<p><strong>Protocol</strong>: <em>IKEv2</em></p>
</li>
<li>
<p><strong>IPsec</strong>: <em>Custom</em></p>
<ol>
<li><strong>IPsec SA lifetime in seconds</strong>: 28800</li>
<li><strong>IKE Phase 1</strong>
<ol>
<li><strong>Encryption</strong>: <em>AES256</em></li>
<li><strong>Integrity/PRF</strong>: <em>SHA256</em></li>
<li><strong>DH Group</strong>: <em>ECP384</em></li>
</ol>
</li>
<li><strong>IKE Phase 2(IPsec)</strong>
<ol>
<li><strong>IPsec Encryption</strong>: <em>AES256</em></li>
<li><strong>IPsec Integrity</strong>: <em>SHA256</em></li>
<li><strong>PFS Group</strong>: <em>ECP384</em></li>
</ol>
</li>
<li><strong>Propagate Default Route:</strong> <strong>Disable</strong></li>
<li><strong>Use policy based traffic selector</strong>: <strong>Disable</strong></li>
<li><strong>Connection mode</strong>: <strong>Initiator Only</strong></li>
<li><strong>Configure traffic selector?</strong>: <strong>Disabled</strong></li>
</ol>
</li>
<li>
<p>Select <strong>Connect</strong>.</p>
</li>
</ol>
