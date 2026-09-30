---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/alibaba-cloud/
  description: Integrate Alibaba Cloud VPN Gateway with Zero Trust networking.
  full_title: Alibaba Cloud VPN Gateway · Cloudflare One docs
  head_html: <title>Alibaba Cloud VPN Gateway · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Alibaba Cloud VPN Gateway with Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/alibaba-cloud/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/alibaba-cloud/index.md"><meta property="og:title" content="Alibaba Cloud VPN Gateway · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Alibaba Cloud VPN Gateway with Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/alibaba-cloud/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="IPsec"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/alibaba-cloud/#page","headline":"Alibaba Cloud VPN Gateway \u00b7 Cloudflare One docs","description":"Integrate Alibaba Cloud VPN Gateway with Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/alibaba-cloud/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["IPsec"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/alibaba-cloud/
  schema: 1
---
<p>This tutorial shows you how to connect Alibaba Cloud infrastructure to Cloudflare WAN (formerly Magic WAN) through IPsec tunnels. For more information regarding Alibaba Cloud technology, refer to <a href="https://www.alibabacloud.com/help/en/vpn-gateway">Alibaba's documentation</a>.</p>
<h2 id="alibaba-cloud">Alibaba Cloud</h2>
<h3 id="1-create-a-vpc"><ol>
<li>Create a VPC</li>
</ol></h3>
<ol>
<li>Log in to your Alibaba Cloud account.</li>
<li>Go to <strong>VPC</strong> &gt; <strong>VPN Gateways</strong>, and select <strong>Create VPC</strong> to create a new Virtual Private Cloud (VPC).</li>
<li>Give your VPC a descriptive name. For example, <code>Cloudflare-Magic-WAN</code>.</li>
<li>Choose the <strong>Region</strong> that aligns with where your servers are located.</li>
<li>In <strong>IPv4 CIDR block</strong>, choose from one of the recommended Internet Protocol (IP) blocks in Classless Inter-Domain Routing (CIDR) notation. For example, <code>192.168.20.0/24</code>. Take note of the IP block you choose, as you will need it to create a static route in Cloudflare WAN.</li>
</ol>
<h3 id="2-create-a-vpn-gateway"><ol start="2">
<li>Create a VPN gateway</li>
</ol></h3>
<ol>
<li>Still in your Alibaba Cloud account, go to <strong>VPC</strong> &gt; <strong>VPN Gateway</strong>, and select <strong>Create VPN Gateway</strong>.</li>
<li>Give your VPN Gateway a descriptive name. For example, <code>VPN-Gateway-Magic-WAN</code>.</li>
<li>In <strong>Region</strong>, choose the server that is best for your geographic region. For example, <strong>US (Silicon Valley)</strong>.</li>
<li>For <strong>Gateway Type</strong>, choose <strong>Standard</strong>.</li>
<li>In <strong>Network Type</strong>, choose <strong>Public</strong>.</li>
<li>For <strong>Tunnels</strong>, select <strong>Single-tunnel</strong>.</li>
<li>In the <strong>VPC</strong> dropdown menu, choose the name of the VPC you created before for Cloudflare WAN. For example, <code>Cloudflare-Magic-WAN</code>.</li>
<li>In the <strong>VSwitch</strong> drop-down menu, choose the VSwitch you created previously. For example, <code>VSwitch-CF</code>.</li>
<li>For options such as <strong>Maximum Bandwidth</strong>, <strong>Traffic</strong>, and <strong>Duration</strong>, select the options that best suit your use case.</li>
<li>In <strong>IPsec-VPN</strong>, select <strong>Enable</strong>.</li>
<li>For <strong>SSL-VPN</strong>, select <strong>Disable</strong>.</li>
<li>When you are finished configuring your VPN gateway, return to the main VPN Gateway window.</li>
<li>Select the VPN gateway you have just created, and then select <strong>Destination-based Routing</strong>.</li>
<li>Select <strong>Add Route Entry</strong>, and enter the subnets needed to reach the required destinations. For example, you can add a default route to send all traffic through your IPsec tunnel.</li>
<li>When you are finished, return to the main window.</li>
<li>Select <strong>Publish</strong> &gt; <strong>OK</strong> to publish the route.</li>
</ol>
<h3 id="3-create-ipsec-connections"><ol start="3">
<li>Create IPsec connections</li>
</ol></h3>
<ol>
<li>Go to <strong>VPC</strong> &gt; <strong>Customer Gateways</strong> &gt; <strong>Create Customer Gateway</strong>.</li>
<li>Create a customer gateway with one of the Cloudflare anycast IP addresses assigned to your account, available in <a href="https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space">Leased IPs</a>. This typically starts with <code>162.xx.xx.xx</code>.</li>
<li>Now, go to <strong>VPC</strong> &gt; <strong>IPsec Connections</strong> &gt; <strong>Create IPsec Connection</strong>.</li>
<li>Create an IPsec connection with the following settings:
<ol>
<li><strong>Name</strong>: give it a descriptive name, like <code>CF-Magic-WAN-IPsec</code>.</li>
<li><strong>Associate Resource</strong>: <strong>VPN Gateway</strong>.</li>
<li><strong>VPN Gateway</strong>: From the dropdown menu, choose the VPN gateway you created previously. In our example, <code>VPN-Gateway-Magic-WAN</code>.</li>
<li><strong>Customer Gateway</strong>: Select the customer gateway you created above for Cloudflare WAN.</li>
<li><strong>Routing Mode</strong>: <strong>Destination Routing Mode</strong>.</li>
<li><strong>Effective Immediately</strong>: <strong>Yes</strong>.</li>
<li><strong>Pre-Shared Key</strong>: This is the pre-shared key (PSK) you will have to use in the Cloudflare WAN IPsec tunnel. If you do not specify one here, the Alibaba system will generate a random pre-shared key for you.</li>
</ol>
</li>
<li>Go to <strong>Advanced Settings</strong>, and expand the <strong>Encryption Configuration</strong> settings.</li>
<li>In <strong>IKE Configurations</strong>, select the following settings to configure the IPsec connection. These settings have to match the supported configuration parameters for <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/gre-ipsec-tunnels/#supported-configuration-parameters">Cloudflare WAN IPsec tunnels</a>:
<ol>
<li><strong>Version</strong>: <em>ikev2</em></li>
<li><strong>Negotiation Mode</strong>: <em>main</em></li>
<li><strong>Encryption Algorithm</strong>: <em>aes256</em></li>
<li><strong>Authentication Algorithm</strong>: <em>sha256</em></li>
<li><strong>DH Group</strong>: <em>group20</em></li>
<li><strong>Localid</strong>: This is the customer endpoint. These are generally IP addresses provided by your ISP. For example, <code>47.xxx.xxx.xxx</code>.</li>
</ol>
</li>
</ol>
<h2 id="cloudflare-wan">Cloudflare WAN</h2>
<h3 id="1-ipsec-tunnels"><ol>
<li>IPsec tunnels</li>
</ol></h3>
<ol>
<li>Follow the <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/#add-tunnels">Add tunnels</a> instructions to create the required IPsec tunnels with the following options:
<ol>
<li><strong>Tunnel name</strong>: Give your tunnel a descriptive name, like <code>Alibaba</code>.</li>
<li><strong>Interface address</strong>: Choose from the subnet in your Alibaba Cloud configuration. For example, if your Alibaba default configuration is <code>169.xx.xx.1/30</code>, you might want to choose <code>169.xx.xx.2/30</code> for your Cloudflare WAN side of the IPsec tunnel.</li>
<li><strong>Customer endpoint</strong>: This is the IP address you entered for <strong>Localid</strong> in Alibaba's IPsec connection. For example, <code>47.xxx.xxx.xxx</code>.</li>
<li><strong>Cloudflare endpoint</strong>: Enter the same anycast IP address provided by Cloudflare you have entered for Alibaba's Customer Gateway. Typically starts with <code>162.xx.xx.xx</code>.</li>
<li><strong>Pre-shared key</strong>: Select <strong>Use my own pre-shared key</strong>, and enter the PSK key from your Alibaba Cloud IPsec tunnel.</li>
<li><strong>Replay protection</strong>: <strong>Enabled</strong>.</li>
</ol>
</li>
<li>Select <strong>Add tunnels</strong> when you are done.</li>
</ol>
<h3 id="2-static-route"><ol start="2">
<li>Static route</li>
</ol></h3>
<ol>
<li>Follow the <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-routes/#create-a-static-route">Configure static routes</a> instructions to create a static route.</li>
<li>In <strong>Prefix</strong>, enter the IP CIDR you used to create your virtual private cloud in the Alibaba Cloud interface. In our example we used <code>192.168.20.0/24</code>.</li>
</ol>
