<p>This tutorial provides information on how to connect Cloudflare WAN (formerly Magic WAN) to your Azure Virtual Network, using the Azure Virtual Network Gateway.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>You will need to have an existing Resource group, Virtual Network, and Virtual Machine created in your Azure account. Refer to <a href="https://learn.microsoft.com/en-us/azure/virtual-network/">Microsoft's documentation</a> to learn more on how to create these.</p>
<h2 id="configure-azure-virtual-network-gateway">Configure Azure Virtual Network Gateway</h2>
<h3 id="1-create-a-gateway-subnet"><ol>
<li>Create a Gateway subnet</li>
</ol></h3>
<p>You should already have a Virtual Network (VNET) created with a subnet assigned to it. The next step is to create a gateway subnet that Azure will use for addressing services related to Azure's Virtual Network Gateway. If you already have a gateway subnet, Azure will prevent you from creating a second one. If that is your case, update your gateway subnet settings.</p>
<ol>
<li>Go to your <strong>Virtual Network</strong> &gt; <strong>Subnets</strong>.</li>
<li>Select the option to add a <strong>Gateway subnet</strong>.</li>
<li>Configure the subnet address range. The gateway subnet must be contained by the address space of the virtual network, and have a subnet mask of <code>/27</code> or greater.</li>
<li>Make sure all other settings are set to <strong>None</strong>.</li>
</ol>
<h3 id="2-create-a-virtual-network-gateway"><ol start="2">
<li>Create a Virtual Network Gateway</li>
</ol></h3>
<p>The Virtual Network Gateway is used to form the tunnel to the devices on your premises.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5821.md")
</aside>
<h4 id="active-active-configuration">Active/Active configuration</h4>
<ol>
<li>Create a Virtual Network Gateway.</li>
<li>Create two new public IP addresses or use existing IPs. Take note of the public IP addresses assigned to the Virtual Network Gateway as these will be the <strong>Customer endpoint</strong> for Cloudflare WAN's IPsec tunnels configuration.</li>
<li>Navigate to the Virtual Network Gateway created earlier.</li>
<li>In <strong>Configuration</strong>, enable <strong>Active-active mode</strong> and disable <strong>Gateway Private IPs</strong>.</li>
<li>Select <strong>Create</strong>.</li>
</ol>
<h4 id="active-standby-configuration">Active/Standby configuration</h4>
<ol>
<li>Create a Virtual Network Gateway.</li>
<li>Create a new public IP address or use an existing IP. Take note of the public IP address assigned to the Virtual Network Gateway as this will be the <strong>Customer endpoint</strong> for Cloudflare WAN's IPsec tunnels configuration.</li>
<li>Select the resource group and VNET you have already created.</li>
<li>In <strong>Configuration</strong>, disable <strong>Active-active mode</strong> and <strong>Gateway Private IPs</strong>.</li>
<li>Select <strong>Create</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5820.md")
</aside>
<h2 id="configure-cloudflare-wan">Configure Cloudflare WAN</h2>
<ol>
<li>Create an <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/#add-tunnels">IPsec tunnel</a> in the Cloudflare dashboard.</li>
<li>Make sure you have the following settings:
<ol>
<li><strong>Interface address</strong>: As the Azure Local Network Gateway will only permit specifying the lower IP address in a <code>/31</code> subnet, add the upper IP address within the <code>/31</code> subnet. You will configure the corresponding <code>/32</code> address in Azure in a later step (refer to <a href="#2-configure-local-network-gateway-for-ipsec-tunnel-health-checks">Configure Local Network Gateway for IPsec tunnel health checks</a>). Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">Tunnel endpoints</a> for more details.</li>
<li><strong>Customer endpoint</strong>: The Public IP associated with your Azure Virtual Network Gateway. For example, <code>40.xxx.xxx.xxx</code>.</li>
<li><strong>Cloudflare endpoint</strong>: Use one of the Cloudflare anycast addresses assigned to your account, available in <a href="https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space">Leased IPs</a>. This will also be the IP address corresponding to the Local Network Gateway in Azure. For example, <code>162.xxx.xxx.xxx</code>.</li>
<li><strong>Health check rate</strong>: Leave the default option (Medium) selected.</li>
<li><strong>Health check type</strong>: Leave the default option (Reply) selected.</li>
<li><strong>Health check direction</strong>: Leave default option (Bidirectional) selected.</li>
<li><strong>Health check target</strong>: Select <strong>Custom</strong>.</li>
<li><strong>Target address</strong>: Enter the same address that is used in the <strong>Customer endpoint</strong> field.</li>
<li><strong>Add pre-shared key later</strong>: Select this option to create a PSK that will be used later in Azure.</li>
<li><strong>Replay protection</strong>: <strong>Enable</strong>.</li>
</ol>
</li>
<li>If you are using the Active/Active configuration, select <strong>Add IPsec tunnel</strong> and repeat step 2 to create the second Cloudflare WAN IPsec tunnel. Use the same <strong>Cloudflare endpoint</strong> as for the first tunnel.</li>
<li>Select <strong>Add Tunnels</strong> when you are finished.</li>
<li>The Cloudflare dashboard will show you a list of your tunnels. Edit the tunnel(s) you have created &gt; select <strong>Generate a new pre-shared key</strong> &gt; copy the generated key. If using the Active/Active configuration, select <strong>Change to a new custom pre-shared key</strong> on the second tunnel and use the PSK generated for the first tunnel.</li>
<li>Create <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-routes/#create-a-static-route">static routes</a> for your Azure Virtual Network subnets, specifying the newly created tunnel as the next hop.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5819.md")
</aside>
<h2 id="complete-the-azure-configuration">Complete the Azure Configuration</h2>
<h3 id="1-create-a-local-network-gateway"><ol>
<li>Create a Local Network Gateway</li>
</ol></h3>
<p>The Local Network Gateway typically refers to your on-premises location. In this case, the Local Network Gateway represents the Cloudflare side of the connection.</p>
<p>We recommend creating a Local Network Gateway for your Cloudflare IPsec tunnel.</p>
<ol>
<li>Create a new local network gateway.</li>
<li>In <strong>Instance details</strong> &gt; <strong>Endpoint</strong>, select <strong>IP address</strong> and enter the Cloudflare anycast address in the IP address field.</li>
<li>In <strong>Address space(s)</strong>, specify the address range of any subnets you wish to access remotely through the Cloudflare WAN connection. For example, if you want to reach a network with an IP range of <code>192.168.1.0/24</code>, and this network is connected to your Cloudflare WAN tenant, you would add <code>192.168.1.0/24</code> to the local network gateway address space.</li>
<li>Go to the <strong>Advanced</strong> tab &gt; <strong>BGP settings</strong>, and make sure you select <strong>No</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5818.md")
</aside>
<h3 id="2-configure-local-network-gateway-for-ipsec-tunnel-health-checks"><ol start="2">
<li>Configure Local Network Gateway for IPsec tunnel health checks</li>
</ol></h3>
<p>Cloudflare WAN uses <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/tunnel-health-checks/">Tunnel Health Checks</a> to monitor whether a tunnel is available.</p>
<p>Tunnel health checks make use of ICMP probes sent from the Cloudflare side of the IPsec tunnel to the remote endpoint (Azure). Probes are sent from the tunnel's interface address, which you specify in two places:</p>
<ol>
<li><strong>Cloudflare Dashboard:</strong> In your IPsec tunnel configuration as the address of the virtual tunnel interface (VTI) (so that Cloudflare knows what address to send probes from). Cloudflare requires this address in Classless Inter-Domain Routing (CIDR) notation with a <code>/31</code> netmask.</li>
<li><strong>Azure Portal:</strong> In your VPN site's address space (so that Azure routes probe responses back over the tunnel). Azure requires this address in CIDR notation with a <code>/32</code> netmask.</li>
</ol>
<p>Cloudflare recommends customers select a unique <code>/31</code> subnet (<a href="https://datatracker.ietf.org/doc/html/rfc1918">RFC 1918 - Address Allocation for Private Internets</a>) for each IPsec tunnel which is treated as a Point-to-Point Link and provides the ideal addressing scheme to satisfy both requirements.</p>
<p>Example:</p>
<ul>
<li>Select 10.252.3.55/31 as your unique point-to-point link subnet.</li>
<li>In the Cloudflare dashboard, set <code>10.252.3.55/31</code> as your tunnel's <strong>IPv4 Interface address</strong> (refer to <a href="#configure-cloudflare-wan">Configure Cloudflare WAN</a>).</li>
<li>In the Azure portal, add <code>10.252.3.55/32</code> to your Local Network Gateway's <strong>Address space</strong>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5817.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5816.md")
</aside>
<p>To configure the Address Space for the Local Network Gateway to support Tunnel Health Checks:</p>
<ol>
<li>Edit the Local Network Gateway configured in the previous section.</li>
<li>Select <strong>Connections</strong>.</li>
<li>Under <strong>Address Space(s)</strong> add the Interface Address of the IPsec Tunnel from the Cloudflare dashboard in CIDR notation (for example, <code>10.252.3.55/32</code>).</li>
<li>If using an Active/Active configuration, also add the Interface Address of the second IPsec Tunnel from the Cloudflare Dashboard in CIDR notation (for example, <code>10.252.3.56/32</code>) under <strong>Address Space(s)</strong>. Both tunnel interface addresses must be configured in the Local Network Gateway Address Space to ensure both tunnels remain healthy.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5815.md")
</aside>
<h3 id="3-create-an-ipsec-vpn-connection"><ol start="3">
<li>Create an IPsec VPN Connection</li>
</ol></h3>
<p>Choose the following settings when creating your VPN Connection:</p>
<ol>
<li><strong>Virtual network gateway</strong>: Select the Virtual Network Gateway you created in <a href="#2-create-a-virtual-network-gateway">Create a Virtual Network Gateway</a>.</li>
<li><strong>Local network gateway</strong>: Select the Local Network Gateway created in <a href="#1-create-a-local-network-gateway">Create a Local Network Gateway</a>.</li>
<li><strong>Use Azure Private IP Address</strong>: <strong>Disabled</strong></li>
<li><strong>BGP</strong>: <strong>Disabled</strong></li>
<li><strong>IPsec / IKE policy</strong>: <strong>Custom</strong>
<ol>
<li><strong>IKE Phase 1</strong>
<ol>
<li><strong>Encryption</strong>: <em>GCMAES256</em></li>
<li><strong>Integrity/PRF</strong>: <em>SHA384</em></li>
<li><strong>DH Group</strong>: <em>ECP384</em></li>
</ol>
</li>
<li><strong>IKE Phase 2(IPsec)</strong>
<ol>
<li><strong>IPsec Encryption</strong>: <em>GCMAES256</em></li>
<li><strong>IPsec Integrity</strong>: <em>GCMAES256</em></li>
<li><strong>PFS Group</strong>: <em>ECP384</em></li>
</ol>
</li>
<li><strong>IPsec SA lifetime in KiloBytes</strong>: <code>0</code></li>
<li><strong>IPsec SA lifetime in seconds</strong>: <code>28800</code></li>
<li><strong>Use policy based traffic selector</strong>: <strong>Disable</strong></li>
<li><strong>DPD timeout in seconds</strong>: <code>45</code></li>
<li><strong>Connection mode</strong>: <strong>InitiatorOnly</strong></li>
<li><strong>Use custom traffic selectors</strong>: <strong>Disabled</strong></li>
</ol>
</li>
<li>After the connection is created, select <strong>Settings</strong> &gt; <strong>Authentication</strong>, and input your PSK (this will need to match the PSK used by the Cloudflare WAN configuration).</li>
</ol>
<p>Repeat this process to define the settings for the Connection to the Local Network Gateway that corresponds to the redundant Cloudflare anycast IP address.</p>
<h3 id="4-route-all-internet-traffic-through-cloudflare-wan-and-cloudflare-gateway"><ol start="4">
<li>Route all Internet traffic through Cloudflare WAN and Cloudflare Gateway</li>
</ol></h3>
<p>Cloudflare Zero Trust customers can route Internet-bound traffic through Cloudflare WAN to the Internet through Cloudflare Gateway.</p>
<p>Microsoft does not permit specifying a default route (<code>0.0.0.0/0</code>) under Address Space in the Local Network Gateway. However, it is possible to work around this limitation through the use of route summarization.</p>
<ol>
<li>Go to <strong>Local network gateways</strong> and select the desired object.</li>
<li>Go to <strong>Configuration</strong> &gt; <strong>Address Space(s)</strong> and specify the following two subnets: <code>0.0.0.0/1</code> &amp; <code>128.0.0.0/1</code>.</li>
<li>Do not remove the subnet configured to support the Tunnel Health Checks.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="install-cloudflare-zero-trust-ca-certificate">Install Cloudflare Zero Trust CA Certificate</h2>
<p>If you opt to route all Internet bound traffic through Cloudflare WAN and want to take advantage of <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/">HTTPS TLS decryption</a>, it will be necessary to install and trust the Cloudflare Zero Trust root certificate authority (CA) certificate on your user's devices. You can either install the certificate provided by Cloudflare (default option), or generate your own custom certificate and upload it to Cloudflare.</p>
<p>More details on how to install the root CA certificate can be found in <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">User-side certificates</a> in the Cloudflare Zero Trust documentation.</p>
<p>Once the root CA certificate is installed, open a web browser or use curl to validate Internet connectivity:</p>
<pre><code class="language-sh">curl https://ipinfo.io&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;ip&quot;: &quot;104.xxx.xxx.225&quot;,&#10;	&quot;city&quot;: &quot;Reston&quot;,&#10;	&quot;region&quot;: &quot;Virginia&quot;,&#10;	&quot;country&quot;: &quot;US&quot;,&#10;	&quot;loc&quot;: &quot;xx.xxxx,-xx.xxxx&quot;,&#10;	&quot;org&quot;: &quot;AS13335 Cloudflare, Inc.&quot;,&#10;	&quot;postal&quot;: &quot;20190&quot;,&#10;	&quot;timezone&quot;: &quot;America/New_York&quot;,&#10;	&quot;readme&quot;: &quot;https://ipinfo.io/missingauth&quot;&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5814.md")
</aside>
<h2 id="validate-connectivity-and-disable-azure-virtual-network-gateway-anti-replay-protection">Validate connectivity and disable Azure Virtual Network Gateway anti-replay protection</h2>
<p>Once you have determined that connectivity has been established, Cloudflare recommends you disable anti-replay protection for the Azure Virtual Network Gateway site-to-site VPN connection. This can be accomplished through Microsoft Azure API.</p>
<ol>
<li>Determine the API token via PowerShell:</li>
</ol>
<pre><code class="language-powershell">Get-AzAccessToken&#10;</code></pre>
<pre><code class="language-txt">Token: eyJ0e&lt;REDACTED&gt;AH-PdSPg&#10;ExpiresOn : 04/08/2024 23:32:47 +00:00&#10;Type      : Bearer&#10;TenantId  : xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx&#10;UserId    : user@domain.com&#10;</code></pre>
<ol start="2">
<li>Issue the API call to display the details of the site-to-site VPN Connection associated with the Azure Virtual Network Gateway (<code>GET</code> request):</li>
</ol>
<pre><code class="language-bash">curl --location &#x27;https://management.azure.com/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.Network/virtualNetworkGateways/{{virtualNetworkGatewayName}}?api-version=2022-05-01&#x27; \&#10;&#45;-header &#x27;Authorization: Bearer eyJ0e&lt;REDACTED&gt;AH-PdSPg&#x27;&#10;</code></pre>
<ol start="3">
<li>Copy/paste the entire response into a text editor:</li>
</ol>
<pre><code class="language-json">{&#10;    &quot;name&quot;: &quot;{{virtualNetworkGatewayName}}&quot;,&#10;    &quot;id&quot;: &quot;/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.Network/virtualNetworkGateways/{{virtualNetworkGatewayName}}&quot;,&#10;    &quot;etag&quot;: &quot;W/\&quot;xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\&quot;&quot;,&#10;    &quot;type&quot;: &quot;Microsoft.Network/virtualNetworkGateways&quot;,&#10;    &quot;location&quot;: &quot;eastus&quot;&#10;    },&#10;    &quot;properties&quot;: {&#10;        &quot;provisioningState&quot;: &quot;Succeeded&quot;,&#10;        &quot;resourceGuid&quot;: &quot;xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx&quot;,&#10;        &quot;packetCaptureDiagnosticState&quot;: &quot;None&quot;,&#10;        &quot;enablePrivateIpAddress&quot;: false,&#10;        &quot;isMigrateToCSES&quot;: false,&#10;        &quot;ipConfigurations&quot;: [&#10;            {&#10;                &quot;name&quot;: &quot;default&quot;,&#10;                &quot;id&quot;: &quot;/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.Network/virtualNetworkGateways/{{virtualNetworkGatewayName}}/ipConfigurations/default&quot;,&#10;                &quot;etag&quot;: &quot;W/\&quot;xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\&quot;&quot;,&#10;                &quot;type&quot;: &quot;Microsoft.Network/virtualNetworkGateways/ipConfigurations&quot;,&#10;                &quot;properties&quot;: {&#10;                    &quot;provisioningState&quot;: &quot;Succeeded&quot;,&#10;                    &quot;privateIPAllocationMethod&quot;: &quot;Dynamic&quot;,&#10;                    &quot;publicIPAddress&quot;: {&#10;                        &quot;id&quot;: &quot;/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.Network/publicIPAddresses/{{virtualNetworkGatewayPublicIpAddress}}&quot;&#10;                    },&#10;                    &quot;subnet&quot;: {&#10;                        &quot;id&quot;: &quot;/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.Network/virtualNetworks/{{virtualNetworkGatewayName}}/subnets/GatewaySubnet&quot;&#10;                    }&#10;                }&#10;            }&#10;        ],&#10;        &quot;natRules&quot;: [],&#10;        &quot;virtualNetworkGatewayPolicyGroups&quot;: [],&#10;        &quot;enableBgpRouteTranslationForNat&quot;: false,&#10;        &quot;disableIPSecReplayProtection&quot;: false,&#10;        &quot;sku&quot;: {&#10;            &quot;name&quot;: &quot;VpnGw2AZ&quot;,&#10;            &quot;tier&quot;: &quot;VpnGw2AZ&quot;,&#10;            &quot;capacity&quot;: 2&#10;        },&#10;        &quot;gatewayType&quot;: &quot;Vpn&quot;,&#10;        &quot;vpnType&quot;: &quot;RouteBased&quot;,&#10;        &quot;enableBgp&quot;: false,&#10;        &quot;activeActive&quot;: false,&#10;        &quot;bgpSettings&quot;: {&#10;            &quot;asn&quot;: 65515,&#10;            &quot;bgpPeeringAddress&quot;: &quot;172.25.40.30&quot;,&#10;            &quot;peerWeight&quot;: 0,&#10;            &quot;bgpPeeringAddresses&quot;: [&#10;                {&#10;                    &quot;ipconfigurationId&quot;: &quot;/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.Network/virtualNetworkGateways/{{virtualNetworkGatewayName}}/ipConfigurations/default&quot;,&#10;                    &quot;defaultBgpIpAddresses&quot;: [&#10;                        &quot;172.25.40.30&quot;&#10;                    ],&#10;                    &quot;customBgpIpAddresses&quot;: [],&#10;                    &quot;tunnelIpAddresses&quot;: [&#10;                        &quot;{{CF ANYCAST IP}}&quot;&#10;                    ]&#10;                }&#10;            ]&#10;        },&#10;        &quot;gatewayDefaultSite&quot;: {&#10;            &quot;id&quot;: &quot;/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.Network/localNetworkGateways/{{localNetworkGatewayName}}&quot;&#10;        },&#10;        &quot;vpnGatewayGeneration&quot;: &quot;Generation2&quot;,&#10;        &quot;allowRemoteVnetTraffic&quot;: false,&#10;        &quot;allowVirtualWanTraffic&quot;: false&#10;    }&#10;}&#10;</code></pre>
<ol start="4">
<li>Locate the line that controls disabling IPsec anti-replay protection, and change it from <code>false</code> to <code>true</code>:</li>
</ol>
<pre><code class="language-txt">&quot;disableIPSecReplayProtection&quot;: true&#10;</code></pre>
<ol start="5">
<li>Upload the entire response in a subsequent API call (<code>PUT</code> request):</li>
</ol>
<pre><code class="language-bash">curl --location --request PUT \&#10;&#x27;https://management.azure.com/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.Network/virtualNetworkGateways/{{virtualNetworkGatewayName}}?api-version=2022-05-01&#x27; \&#10;&#45;-header &quot;Authorization: Bearer eyJ0e&lt;REDACTED&gt;AH-PdSPg&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;    &quot;name&quot;: &quot;{{virtualNetworkGatewayName}}&quot;,&#10;    &quot;id&quot;: &quot;/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.Network/virtualNetworkGateways/{{virtualNetworkGatewayName}}&quot;,&#10;    &quot;etag&quot;: &quot;W/\&quot;xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\&quot;&quot;,&#10;    &quot;type&quot;: &quot;Microsoft.Network/virtualNetworkGateways&quot;,&#10;    &quot;location&quot;: &quot;eastus&quot;&#10;    },&#10;    &quot;properties&quot;: {&#10;        &quot;provisioningState&quot;: &quot;Succeeded&quot;,&#10;        &quot;resourceGuid&quot;: &quot;xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx&quot;,&#10;        &quot;packetCaptureDiagnosticState&quot;: &quot;None&quot;,&#10;        &quot;enablePrivateIpAddress&quot;: false,&#10;        &quot;isMigrateToCSES&quot;: false,&#10;        &quot;ipConfigurations&quot;: [&#10;            {&#10;                &quot;name&quot;: &quot;default&quot;,&#10;                &quot;id&quot;: &quot;/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.Network/virtualNetworkGateways/{{virtualNetworkGatewayName}}/ipConfigurations/default&quot;,&#10;                &quot;etag&quot;: &quot;W/\&quot;xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\&quot;&quot;,&#10;                &quot;type&quot;: &quot;Microsoft.Network/virtualNetworkGateways/ipConfigurations&quot;,&#10;                &quot;properties&quot;: {&#10;                    &quot;provisioningState&quot;: &quot;Succeeded&quot;,&#10;                    &quot;privateIPAllocationMethod&quot;: &quot;Dynamic&quot;,&#10;                    &quot;publicIPAddress&quot;: {&#10;                        &quot;id&quot;: &quot;/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.Network/publicIPAddresses/{{virtualNetworkGatewayPublicIpAddress}}&quot;&#10;                    },&#10;                    &quot;subnet&quot;: {&#10;                        &quot;id&quot;: &quot;/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.Network/virtualNetworks/{{virtualNetworkGatewayName}}/subnets/GatewaySubnet&quot;&#10;                    }&#10;                }&#10;            }&#10;        ],&#10;        &quot;natRules&quot;: [],&#10;        &quot;virtualNetworkGatewayPolicyGroups&quot;: [],&#10;        &quot;enableBgpRouteTranslationForNat&quot;: false,&#10;        &quot;disableIPSecReplayProtection&quot;: true,&#10;        &quot;sku&quot;: {&#10;            &quot;name&quot;: &quot;VpnGw2AZ&quot;,&#10;            &quot;tier&quot;: &quot;VpnGw2AZ&quot;,&#10;            &quot;capacity&quot;: 2&#10;        },&#10;        &quot;gatewayType&quot;: &quot;Vpn&quot;,&#10;        &quot;vpnType&quot;: &quot;RouteBased&quot;,&#10;        &quot;enableBgp&quot;: false,&#10;        &quot;activeActive&quot;: false,&#10;        &quot;bgpSettings&quot;: {&#10;            &quot;asn&quot;: 65515,&#10;            &quot;bgpPeeringAddress&quot;: &quot;172.25.40.30&quot;,&#10;            &quot;peerWeight&quot;: 0,&#10;            &quot;bgpPeeringAddresses&quot;: [&#10;                {&#10;                    &quot;ipconfigurationId&quot;: &quot;/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.Network/virtualNetworkGateways/{{virtualNetworkGatewayName}}/ipConfigurations/default&quot;,&#10;                    &quot;defaultBgpIpAddresses&quot;: [&#10;                        &quot;172.25.40.30&quot;&#10;                    ],&#10;                    &quot;customBgpIpAddresses&quot;: [],&#10;                    &quot;tunnelIpAddresses&quot;: [&#10;                        &quot;{{CF ANYCAST IP}}&quot;&#10;                    ]&#10;                }&#10;            ]&#10;        },&#10;        &quot;gatewayDefaultSite&quot;: {&#10;            &quot;id&quot;: &quot;/subscriptions/{{subscriptionId}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.Network/localNetworkGateways/{{localNetworkGatewayName}}&quot;&#10;        },&#10;        &quot;vpnGatewayGeneration&quot;: &quot;Generation2&quot;,&#10;        &quot;allowRemoteVnetTraffic&quot;: false,&#10;        &quot;allowVirtualWanTraffic&quot;: false&#10;    }&#10;}&#x27;&#10;</code></pre>
<ol start="6">
<li>Leave the replay protection setting checked in the Cloudflare dashboard, and wait several minutes before validating connectivity again.</li>
</ol>
