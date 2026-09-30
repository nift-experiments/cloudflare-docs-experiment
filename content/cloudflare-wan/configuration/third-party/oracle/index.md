<p>This tutorial shows how to configure IPsec (Internet Protocol Security) between Cloudflare WAN (formerly Magic WAN) and an Oracle Cloud Site-to-site VPN.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>You need a pre-shared key to establish the IPsec tunnel. You can use the following code to create a random key:</p>
<pre><code class="language-js">		const a = new Uint8Array(48);&#10;		crypto.getRandomValues(a);&#10;		let base64String = btoa(String.fromCharCode.apply(null, a));&#10;&#10;		base64String = base64String.replace(/\+/g, &#x27;&#x27;)&#10;								   .replace(/\//g, &#x27;&#x27;)&#10;								   .replace(/=/g, &#x27;&#x27;);&#10;&#10;		console.log(base64String.substring(0, 32));&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6833.md")
</aside>
<p>You can try this code in the <a href="https://workers.cloudflare.com/playground#LYVwNgLglgDghgJwgegGYHsHALQBM4RwDcABAEbogB2+CAngLzbPYDqApmQNJQQBimYACFKNRHSoBzAB4ArAEoBBANYR5AEVYAJAOJCAagA0AXCxYduvAVhHVaEmQpVrNug4YCwAKADC6KhDsAdjqUADOMOhhvFD+xiQYWHgExCRUcMDsDABEUDTs0gB0smHZpKhQYEEZWbn5RSXZ3n4BQRDYACp0MOzxcDAwYFAAxgSxVMiycABucGHDCLAQANTA6Ljg7N7eBZFIJLjsqHDgECQA3l4AkHMSwwnsEMMAFgAUAJQXXtdXw-5hZzgJAYaXYAHcSABVPIQAAcigQCDgdFeABZYe8iD8Ft0IOhCpJHvI4DR0MB9HAwCB2GFXnBMT8qmcyHN2AA2VEAZQgiykwPIeLgr25vMkhVQCDJPmeiD8h0K-UGKKo4DAABoSPSGT8WWF2VyeXlJPzdfqRUbCgh2IM4MN2K9kAAdZbISQagDk7vePyuvr9JADlutYFt9qdyFdHq9Pr9voDJCDNrtDoYkZInu1vr+VABCTylPNfJBpo5hbFYRAZABoteAAYNQBmABMmauVogIAQVFBEPkNMiOftFXSYDLGsufue7DghwQYXiE792WzgWCEG67Gy8WygWkKGeEGAYGyap9AF9T76zwyrhevGesd4zMwLDx+IJbGJ6FI5EpVBptD0Ixmn8Vd2lCCIohiOIEkEZJCFIdJMhyTJCHwQgyjzKokNqMgwHQMgml8UC2k6Dc+gGIZRmgfxJjCfxti8c5lzJeBoDISpeDoAB9dDN2MbIm1rJtUWwWsGzEgB2E8WOANioA4oZ1241AQ0kUpjAAbWyKh1nYEpuL+OSCGyABdNVsmAOA8m4tYNiqLc6kOBpSjPJ9n1fKwP1Eewfycf9XCAwxmG8IA">Workers playground</a>.</p>
<h2 id="oracle-cloud">Oracle Cloud</h2>
<h3 id="1-create-oracle-cloud-customer-premises-equipment"><ol>
<li>Create Oracle Cloud customer-premises equipment</li>
</ol></h3>
<ol>
<li>Go to <strong>Networking</strong> &gt; <strong>Customer connectivity</strong>, and select <strong>Customer-premises equipment</strong>.</li>
<li>Select <strong>Create CPE</strong>.</li>
<li>Select the following settings (you can leave settings not mentioned here with their default values):
<ul>
<li><strong>Name</strong>: Enter a name.</li>
<li><strong>IP Address</strong>: Enter your Cloudflare anycast IP address.</li>
<li><strong>CPE vendor information</strong>: Select <strong>Other</strong>.</li>
</ul>
</li>
<li>Select <strong>Create CPE</strong>.</li>
</ol>
<h3 id="2-create-oracle-cloud-dynamic-routing-gateways"><ol start="2">
<li>Create Oracle Cloud dynamic routing gateways</li>
</ol></h3>
<ol>
<li>Go to <strong>Networking</strong> &gt; <strong>Customer connectivity</strong>, and select <strong>Dynamic routing gateways</strong>.</li>
<li>Select <strong>Create Dynamic routing gateways</strong>.</li>
<li>Select the following settings (you can leave settings not mentioned here with their default values):
<ul>
<li><strong>Name</strong>: Enter a name.</li>
</ul>
</li>
<li>Select <strong>Create Dynamic routing gateways</strong>.</li>
</ol>
<h3 id="3-create-an-ipsec-connection"><ol start="3">
<li>Create an IPsec connection</li>
</ol></h3>
<ol>
<li>Go to <strong>Networking</strong> &gt; <strong>Customer connectivity</strong>, and select <strong>Site-to-Site VPN</strong>.</li>
<li>Select <strong>Create IPsec connection</strong>.</li>
<li>Select the following settings (you can leave settings not mentioned here with their default values):
<ul>
<li><strong>Name</strong>: Enter a name.</li>
<li><strong>Customer-premises equipment (CPE)</strong>: Select the CPE you created in step 1.</li>
<li><strong>Dynamic routing gateways (DRG)</strong>: Select the DRG you created in step 2.</li>
<li><strong>Routes to your on-premises network</strong>: Enter a CIDR (Classless Inter-Domain Routing) range you want to route to Cloudflare WAN.</li>
<li><strong>Tunnel 1</strong>
<ul>
<li><strong>Name</strong>: Enter a name.</li>
<li>Select <strong>Provide custom shared secret</strong>.</li>
<li>Enter the <strong>pre-shared key</strong> you created in the Prerequisites section.</li>
<li><strong>IKE (Internet Key Exchange) version</strong>: <strong>IKEv2</strong></li>
<li><strong>Routing type</strong>: <strong>Static routing</strong></li>
<li><strong>IPv4 inside tunnel interface - CPE</strong>:  Enter the internal tunnel IP on the Cloudflare side of the IPsec tunnel. In this example, it is <code>10.200.1.0/31</code>.</li>
<li><strong>IPv4 inside tunnel interface - Oracle</strong>: Enter the internal tunnel IP on the Oracle side of the IPsec tunnel. In this example, it is <code>10.200.1.1/31</code>. This matches with the Cloudflare side for this tunnel.
<ol>
<li>Select <strong>Show advanced options</strong></li>
<li>Select <strong>Phase one (ISAKMP) configuration</strong>
<ul>
<li>Select <strong>Set custom configurations</strong></li>
<li><strong>Custom encryption algorithm</strong>: <strong>AES_256_CBC</strong></li>
<li><strong>Custom authentication algorithm</strong>: <strong>SHA2_256</strong></li>
<li><strong>Custom Diffie-Hellman group</strong>: <strong>GROUP20</strong></li>
<li><strong>IKE session key lifetime in seconds</strong>: <strong>86400</strong></li>
</ul>
</li>
<li>Select <strong>Phase two (IPsec) configuration</strong>
<ul>
<li>Select <strong>Set custom configurations</strong></li>
<li><strong>Custom encryption algorithm</strong>: <strong>AES_256_CBC</strong></li>
<li><strong>HMAC (Hash-based Message Authentication Code)_SHA2_256_128</strong>: <strong>HMAC_SHA2_256_128</strong></li>
<li><strong>IPsec session key lifetime in seconds</strong>: <strong>28800</strong></li>
<li><strong>Perfect forward secrecy Diffie-Hellman group</strong>: <strong>GROUP20</strong></li>
</ul>
</li>
</ol>
</li>
</ul>
</li>
<li><strong>Tunnel 2</strong>
<ul>
<li>Repeat these steps for Tunnel 2. Select the right IP for <strong>IPv4 inside tunnel interface - CPE (Customer-Premises Equipment)</strong>: <code>10.200.2.0/31</code> and <strong>IPv4 inside tunnel interface - Oracle</strong>: <code>10.200.2.1/31</code></li>
</ul>
</li>
</ul>
</li>
<li>Select <strong>Create IPsec connection</strong></li>
</ol>
<h2 id="cloudflare-wan">Cloudflare WAN</h2>
<p>After configuring the Oracle Site-to-site VPN connection and the tunnels, go to the Cloudflare dashboard and create the corresponding IPsec tunnel and static routes on the Cloudflare WAN side.</p>
<h3 id="ipsec-tunnels">IPsec tunnels</h3>
<ol>
<li>Refer to <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/#add-tunnels">Add tunnels</a> to learn how to add an IPsec tunnel. When creating your IPsec tunnel, make sure you define the following settings:
<ul>
<li><strong>Tunnel name</strong>: Enter a name.</li>
<li><strong>Interface address</strong>: Enter the internal tunnel IP on the Cloudflare side of the IPsec tunnel. In this example, it is <code>10.200.1.0/31</code>.</li>
<li><strong>Customer endpoint</strong>: The Oracle VPN public IP address.</li>
<li><strong>Cloudflare endpoint</strong>: Enter one of the Cloudflare anycast IP addresses assigned to your account, available in <a href="https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space">Leased IPs</a>.</li>
<li><strong>Health check type</strong>: <strong>Request</strong></li>
<li><strong>Health check direction</strong>: <strong>Unidirectional</strong></li>
<li><strong>Health check target</strong>: <strong>Default</strong></li>
<li><strong>Pre-shared key</strong>: Choose <strong>Use my own pre-shared key</strong>, and enter the pre-shared key you created in the Prerequisites section.</li>
<li><strong>Replay protection</strong>: <strong>Enabled</strong>.</li>
</ul>
</li>
<li>Select <strong>Add tunnels</strong>.</li>
<li>Repeat these steps for Tunnel 2. Choose the same Cloudflare anycast IP address and select the right IP for <strong>Interface address</strong>: <code>10.200.2.0/31</code></li>
</ol>
<h3 id="static-routes">Static routes</h3>
<p>The static route in Cloudflare WAN should point to the appropriate virtual machine (VM) subnet you created inside your Oracle Virtual Cloud Network (VCN). For example, if your VM has a subnet of <code>192.168.192.0/26</code>, you should use it as the prefix for your static route.</p>
<p>To create a static route:</p>
<ol>
<li>Refer to <a href="/cloudflare-wan/configuration/how-to/configure-routes/#create-a-static-route">Create a static route</a> to learn how to create one.</li>
<li>In <strong>Prefix</strong>, enter the subnet for your VM. For example, <code>192.xx.xx.xx/24</code>.</li>
<li>For the <strong>Tunnel/Next hop</strong>, choose the IPsec tunnel you created in the previous step.</li>
<li>Repeat these steps for the second IPsec tunnel you created.</li>
</ol>
