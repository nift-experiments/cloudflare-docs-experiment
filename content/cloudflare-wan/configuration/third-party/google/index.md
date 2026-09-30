---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/google/
  description: Connect Google Cloud VPN to Cloudflare WAN.
  full_title: Google Cloud VPN · Cloudflare WAN docs
  head_html: <title>Google Cloud VPN · Cloudflare WAN docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect Google Cloud VPN to Cloudflare WAN."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/google/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/google/index.md"><meta property="og:title" content="Google Cloud VPN · Cloudflare WAN docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect Google Cloud VPN to Cloudflare WAN."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/google/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare WAN"><meta name="algolia_product_filter" content="Cloudflare WAN"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare WAN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/google/#page","headline":"Google Cloud VPN \u00b7 Cloudflare WAN docs","description":"Connect Google Cloud VPN to Cloudflare WAN.","url":"https://developers.cloudflare.com/cloudflare-wan/configuration/third-party/google/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-wan/configuration/third-party/google/
  schema: 1
---
<p>This tutorial explains how to configure IPsec VPN between Cloudflare WAN (formerly Magic WAN) and a Google Cloud Platform (GCP) Cloud VPN.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>You need to have a GCP VPN gateway created in your GCP account. This is needed to route traffic between your GCP virtual private cloud (VPC) and Cloudflare WAN. Refer to the <a href="https://cloud.google.com/network-connectivity/docs/vpn/how-to/creating-static-vpns">GCP documentation</a> for more information about creating a Cloud VPN gateway.</p>
<p>A Classic VPN Gateway is required to support static routing. Route tables will also need to be manually configured to allow the routing between the VPN and Cloudflare WAN to work. Refer to <a href="https://cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#ts-tun-routing">GCP routing options</a> to learn more about GCP VPC routing.</p>
<h2 id="google-cloud-platform">Google Cloud Platform</h2>
<h3 id="create-a-gcp-cloud-vpn-gateway">Create a GCP Cloud VPN Gateway</h3>
<ol>
<li>Go to <strong>Network Connectivity</strong> &gt; <strong>VPN</strong>.</li>
<li>Select the <strong>Cloud VPN Gateways</strong> tab &gt; <strong>Create VPN Gateway</strong>.</li>
<li>Give your gateway a descriptive name.</li>
<li>Choose the network you want to connect to with this Cloud VPN Gateway (VPC).</li>
<li>Select a region where this Cloud VPN Gateway should be located.</li>
<li>Choose <strong>IPv4</strong> as the IP traffic type that will flow through this Gateway.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6840.md")
</aside>
<h3 id="configure-the-vpn-connection">Configure the VPN connection</h3>
<ol>
<li>Go to <strong>Network Connectivity</strong> &gt; <strong>VPN</strong>.</li>
<li>Select the <strong>Cloud VPN Tunnels</strong> tab &gt; <strong>Create VPN Tunnel</strong>.</li>
<li>Select the VPN Gateway you have created &gt; <strong>Continue</strong>.</li>
<li>Give your tunnel a descriptive name.</li>
<li>For <strong>Remote Peer IP Address</strong>, use one of the Cloudflare anycast IP addresses assigned to your account, available in <a href="https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space">Leased IPs</a>.</li>
<li>In <strong>IKE version</strong>, select <strong>IKEv2</strong>.</li>
<li>You can generate an IKE pre-shared key, or add one you already own. If you generate one during this set up, keep it somewhere safe since you will need it in other steps to finish setting up Cloudflare WAN and GCP.</li>
<li>Choose <strong>Route-based</strong> as routing option.</li>
<li>In <strong>Remote network IP range</strong> define the network you are going to expose to GCP via Cloudflare WAN.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6839.md")
</aside>
<ol start="10">
<li>Repeat steps 2-9 using your second Cloudflare anycast IP to create a second VPN tunnel.</li>
</ol>
<h3 id="static-routes">Static Routes</h3>
<p>Static routing is necessary to route traffic between your VPN and Cloudflare WAN. Follow these steps to create them for your VPC. Refer to <a href="https://cloud.google.com/vpc/docs/routes">VPN route documentation</a> to learn more about VPN routing.</p>
<ol>
<li>Go to <strong>VPC network</strong> &gt; <strong>Routes</strong>.</li>
<li>Select <strong>Route Management</strong>.</li>
<li>Create a route.</li>
<li>Choose the VPC network you want to use for that route.</li>
<li>In <strong>Route type</strong> select <strong>Static Routing</strong>.</li>
<li>In <strong>IP Version</strong> select <strong>IPv4</strong>.</li>
<li>Configure the network you want to expose to your VPN in the <strong>Destination IPv4 Range</strong>.</li>
<li>Choose a priority for your static route.</li>
<li>(Optional) You can link that route to a specific instance tag, so only impacted instances will use that route.</li>
<li>In <strong>Next hop</strong> select the VPN tunnel you created previously.</li>
<li>Select <strong>Create</strong>.</li>
</ol>
<h2 id="cloudflare-wan">Cloudflare WAN</h2>
<p>After configuring the Cloud VPN gateway VPN and the tunnels as mentioned above, go to the Cloudflare dashboard and create the corresponding IPsec tunnels and static routes on the Cloudflare WAN side.</p>
<h3 id="ipsec-tunnels">IPsec tunnels</h3>
<ol>
<li>Refer to <a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/#add-tunnels">Add tunnels</a> to learn how to add an IPsec tunnel. When creating your IPsec tunnel, make sure you define the following settings:
<ul>
<li><strong>Tunnel name</strong>: <code>tunnel01</code></li>
<li><strong>Interface address</strong>: The IPsec tunnel inner <code>/30</code> Classless Inter-Domain Routing (CIDR) block. For example, <code>169.254.244.2</code>.</li>
<li><strong>Customer endpoint</strong>: The IP address from GCP VPN tunnel outside IP address. For example, <code>35.xx.xx.xx</code>.</li>
<li><strong>Cloudflare endpoint</strong>: Enter the first of your two anycast IPs.</li>
<li><strong>Pre-shared key</strong>: Choose <strong>Use my own pre-shared key</strong>, and enter the PSK you created for the GCP VPN tunnel.</li>
<li><strong>Health check type</strong>: Choose <strong>Reply</strong></li>
<li><strong>Health check destination</strong>: Choose <strong>custom</strong> and set the IP corresponding to the interface address for the tunnel</li>
<li><strong>Health check direction</strong>: Choose <strong>Bidirectional</strong></li>
<li><strong>Replay protection</strong>: Select <strong>Enabled</strong>.</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
<li>Repeat the above steps for <code>tunnel02</code>. Chose the same prefix, but select the second IPsec tunnel for <strong>Tunnel/Next hop</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6838.md")
</aside>
<h3 id="static-routes-1">Static routes</h3>
<p>Create a static route in Cloudflare WAN that points to the appropriate virtual machine (VM) subnet you created inside your GCP virtual private cloud. For example, if your VM has a subnet of <code>192.168.192.0/26</code>, you should use it as the prefix for your static route.</p>
<p>To create a static route:</p>
<ol>
<li>Refer to <a href="/cloudflare-wan/configuration/how-to/configure-routes/#create-a-static-route">Create a static route</a> to learn how to create one.</li>
<li>In <strong>Prefix</strong>, enter the subnet for your VM. For example, <code>192.168.192.0/26</code>.</li>
<li>For the <strong>Tunnel/Next hop</strong>, choose the IPsec tunnel you created in the previous step.</li>
<li>Repeat the steps above for the second IPsec tunnel you created.</li>
</ol>
