---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/aws/
  description: Integrate Amazon AWS Transit Gateway with Zero Trust networking.
  full_title: Amazon AWS Transit Gateway · Cloudflare One docs
  head_html: <title>Amazon AWS Transit Gateway · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Amazon AWS Transit Gateway with Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/aws/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/aws/index.md"><meta property="og:title" content="Amazon AWS Transit Gateway · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Amazon AWS Transit Gateway with Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/aws/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="AWS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/aws/#page","headline":"Amazon AWS Transit Gateway \u00b7 Cloudflare One docs","description":"Integrate Amazon AWS Transit Gateway with Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/aws/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AWS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/aws/
  schema: 1
---
<p>This tutorial provides information and examples of how to configure IPsec VPN between Cloudflare WAN (formerly Magic WAN) with an AWS Transit Gateway.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>You need to have an AWS transit gateway created in your AWS account. This is needed to route traffic between your AWS virtual private cloud (VPC) and Cloudflare WAN. Refer to the <a href="https://docs.aws.amazon.com/vpc/latest/tgw/tgw-getting-started.html">AWS documentation</a> to learn more about creating a transit gateway.</p>
<p>Additionally, you also need to configure the necessary route table entries for the virtual machine (VM) in your VPC, as well as the route table entries for the transit gateway. Otherwise, connectivity between your VM and another VM routed through Cloudflare WAN will not work. Refer to the <a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html">AWS documentation</a> to learn more about routing tables.</p>
<h2 id="aws">AWS</h2>
<h3 id="create-aws-transit-gateway-vpn-attachment">Create AWS transit gateway VPN attachment</h3>
<ol>
<li>Go to <strong>Transit gateways</strong> &gt; <strong>Transit gateway attachments</strong>, and select <strong>Create transit gateway attachment</strong>.</li>
<li>Select the <strong>Transit gateway ID</strong> that you created previously from the drop-down menu.</li>
<li>For <strong>Attachment type</strong>, select <em>VPN</em>.</li>
<li>Under VPN attachment, select the following settings (you can leave settings not mentioned here with their default values):
<ol>
<li><strong>Customer Gateway</strong>: Select <strong>New</strong>.</li>
<li><strong>IP Address</strong>: Enter your Cloudflare anycast IP address.</li>
<li><strong>Routing options</strong>: Select <strong>Static</strong>.</li>
</ol>
</li>
<li>Select <strong>Create transit gateway attachment</strong>.</li>
</ol>
<h3 id="configure-the-vpn-connection">Configure the VPN connection</h3>
<ol>
<li>
<p>Select the VPN connection you created &gt; <strong>Download configuration</strong>.</p>
</li>
<li>
<p>This action downloads a text file. Search for the IP range that the AWS Transit Gateway assigned your tunnel. The first IP range should be the one used by the AWS Transit Gateway. Use the second IP range to configure your <a href="#ipsec-tunnels">Interface address</a> in Cloudflare WAN.</p>
</li>
<li>
<p>Select the VPN connection you created &gt; <strong>Actions</strong> &gt; <strong>Modify VPN tunnel options</strong>.</p>
</li>
<li>
<p>From the <strong>VPN tunnel outside IP address</strong> drop-down menu, select one of the tunnels.</p>
</li>
<li>
<p>Take note of the <strong>IP address</strong> you chose, as this corresponds to the customer endpoint IP that you will need to configure on the Cloudflare side of the IPsec tunnel.</p>
</li>
<li>
<p>The number of options for the VPN connection will expand. Take note of the <strong>Pre-shared key</strong>.  You will need it to create the IPsec tunnel on Cloudflare's side.</p>
</li>
<li>
<p>In <strong>Inside IPv4 CIDR</strong>, AWS enforces that only a <code>/30</code> block within the <code>169.254.0.0/16</code> range can be used. To accommodate this, Cloudflare supports a subset of this IP block. Namely, Cloudflare supports <code>169.254.240.0/20</code> to be assigned as the IPsec tunnel's (internal) interface IPs. This example will use <code>169.254.244.0/30</code> as the CIDR block for the IPsec tunnel: <code>169.254.244.1</code> for the AWS side of the tunnel, and <code>169.254.244.2</code> for the Cloudflare side of the tunnel.</p>
</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5636.md")
</aside>
<ol start="8">
<li>
<p>Configure the following settings for the IPsec tunnel. Note that the <strong>Startup action</strong> needs to be set to <strong>Start</strong>, which means the AWS side will initiate IPsec negotiation. Settings not mentioned here can be left at their default settings:</p>
<ul>
<li><strong>Phase 1 encryption algorithms</strong>: <code>AES256-GCM-16</code></li>
<li><strong>Phase 2 encryption algorithms</strong>: <code>AES256-GCM-16</code></li>
<li><strong>Phase 1 integrity algorithms</strong>: <code>SHA2-256</code></li>
<li><strong>Phase 2 integrity algorithms</strong>: <code>SHA2-256</code></li>
<li><strong>Phase 1 DH group numbers</strong>: <code>20</code></li>
<li><strong>Phase 2 DH group numbers</strong>: <code>20</code></li>
<li><strong>IKE Version</strong>: <code>ikev2</code></li>
<li><strong>Startup action</strong>: <strong>Start</strong></li>
<li><strong>DPD timeout action</strong>: <code>Restart</code></li>
</ul>
</li>
<li>
<p>Select <strong>Save changes</strong>.</p>
</li>
<li>
<p>Repeat the steps above to configure the second VPN connection. Use the second outside IP address, and make the appropriate changes to IP addresses as well when configuring Cloudflare's side of the tunnel.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5635.md")
</aside>
<h2 id="cloudflare-wan">Cloudflare WAN</h2>
<p>After configuring the AWS transit gateway VPN connection and the tunnel as mentioned above, go to the Cloudflare dashboard and create the corresponding IPsec tunnel and static routes on the Cloudflare WAN side.</p>
<h3 id="ipsec-tunnels">IPsec tunnels</h3>
<ol>
<li>Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/#add-tunnels">Add tunnels</a> to learn how to add an IPsec tunnel. When creating your IPsec tunnel, make sure you define the following settings:
<ul>
<li><strong>Tunnel name</strong>: <code>tunnel01</code></li>
<li><strong>Interface address</strong>: The <code>/30</code> CIDR block enforced by AWS (first usable IP is for the AWS side). For example, <code>169.254.244.2</code>.</li>
<li><strong>Customer endpoint</strong>: The IP address from AWS's VPN tunnel outside IP address. For example, <code>35.xx.xx.xx</code>.</li>
<li><strong>Cloudflare endpoint</strong>: Enter the first of your two anycast IPs.</li>
<li><strong>Pre-shared key</strong>: Select <strong>Use my own pre-shared key</strong>, and enter the PSK you created for the AWS VPN tunnel.</li>
<li><strong>Health check type</strong>: Select <strong>Request</strong></li>
<li><strong>Health check direction</strong>: Select <strong>Bidirectional</strong></li>
<li><strong>Replay protection</strong>: Select <strong>Enabled</strong>.</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
<li>Repeat the above steps for <code>tunnel02</code>. Select the same prefix, but select the second IPsec tunnel for <strong>Tunnel/Next hop</strong>.</li>
</ol>
<h3 id="static-routes">Static routes</h3>
<p>The static route in Cloudflare WAN should point to the appropriate virtual machine (VM) subnet you created inside your AWS virtual private cloud. For example, if your VM has a subnet of  <code>192.168.192.0/26</code>, you should use it as the prefix for your static route.</p>
<p>To create a static route:</p>
<ol>
<li>Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-routes/#create-a-static-route">Create a static route</a> to learn how to create one.</li>
<li>In <strong>Prefix</strong>, enter the subnet for your VM. For example, <code>192.xx.xx.xx/24</code>.</li>
<li>For the <strong>Tunnel/Next hop</strong>, select the IPsec tunnel you created in the previous step.</li>
<li>Repeat the steps above for the second IPsec tunnel you created.</li>
</ol>
