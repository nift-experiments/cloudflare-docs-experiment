---
cp9:
  canonical: https://developers.cloudflare.com/multi-cloud-networking/reference/
  description: Reference information for Multi-Cloud Networking.
  full_title: Reference · Cloudflare Multi-Cloud Networking docs
  head_html: <title>Reference · Cloudflare Multi-Cloud Networking docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Multi-Cloud Networking."><link rel="canonical" href="https://developers.cloudflare.com/multi-cloud-networking/reference/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/multi-cloud-networking/reference/index.md"><meta property="og:title" content="Reference · Cloudflare Multi-Cloud Networking docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Multi-Cloud Networking."><meta property="og:url" content="https://developers.cloudflare.com/multi-cloud-networking/reference/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Multi-Cloud Networking"><meta name="algolia_product_filter" content="Multi-Cloud Networking"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Multi-Cloud Networking"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/multi-cloud-networking/reference/#page","headline":"Reference \u00b7 Cloudflare Multi-Cloud Networking docs","description":"Reference information for Multi-Cloud Networking.","url":"https://developers.cloudflare.com/multi-cloud-networking/reference/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /multi-cloud-networking/reference/
  schema: 1
---
<p>Refer to this page for details about how Cloudflare orchestrates VPN connectivity to your cloud networks.</p>
<h2 id="cloud-on-ramps">Cloud on-ramps</h2>
<h3 id="aws">AWS</h3>
<p><img src="/assets/upstream/images/multi-cloud-networking/reference/aws.png" alt="Diagram showing how Cloudflare creates on-ramps to AWS" /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<p>When using Cloudflare One Multi-Cloud Networking (formerly Magic Cloud Networking) (beta) to automatically create on-ramps to your AWS account, you should be aware of the following configuration changes Cloudflare will make on your behalf:</p>
<ul>
<li>Cloudflare will create a new customer-managed prefix list named <strong>Cloudflare WAN and Cloudflare Edge</strong> populated with your <a href="/multi-cloud-networking/cloud-on-ramps/#cloudflare-wan-address-space">Cloudflare WAN Address Space</a> prefixes and the IPv4 address ranges for Cloudflare's global network servers (the latter prefixes are necessary if you use any Cloudflare L7 processing features). You must create rules in your Network Security Groups (NSGs) allowing traffic to/from this prefix list in order to have connectivity with Cloudflare WAN (formerly Magic WAN). (The prefix list will contain around 15 to 25 entries, which each count against the rules-per-security-group quota for NSGs in your AWS account.)</li>
<li>Cloudflare will create a Virtual Private Gateway and attach it to your Virtual Private Cloud (VPC). If an existing Virtual Private Gateway is already attached to the VPC, on-ramp creation will fail.</li>
<li>Cloudflare will enable route propagation from the Virtual Private Gateway into all route tables in your VPC. This will result in a route for each prefix in your <a href="/multi-cloud-networking/cloud-on-ramps/#cloudflare-wan-address-space">Cloudflare WAN Address Space</a> targeting the gateway.</li>
<li>Cloudflare will add a route in Cloudflare WAN for each IPv4 CIDR (Classless Inter-Domain Routing) block in your VPC.</li>
</ul>
<h3 id="azure">Azure</h3>
<p><img src="/assets/upstream/images/multi-cloud-networking/reference/azure.png" alt="Diagram showing how Cloudflare creates on-ramps to Azure" /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<p>When using Multi-Cloud Networking (beta) to automatically create on-ramps to your Azure account, you should be aware of the following configuration changes Cloudflare will make on your behalf:</p>
<ul>
<li>Cloudflare will create a Virtual Network Gateway in your Virtual Network (VNet). Virtual Network Gateways in Azure require a subnet named <code>GatewaySubnet</code>. Cloudflare will create a <code>GatewaySubnet</code> if one does not already exist in your VNet. If there is not enough unused address space left in your VNet to create a <code>/27</code> subnet for the <code>GatewaySubnet</code>, or if a <code>GatewaySubnet</code> exists but does not have enough address space left for a Virtual Network Gateway, on-ramp creation will fail.</li>
<li>Cloudflare will enable gateway route propagation on all route tables in your VNet. This will result in a route for each prefix in your <a href="/multi-cloud-networking/cloud-on-ramps/#cloudflare-wan-address-space">Cloudflare WAN Address Space</a> pointing to the gateway. If your VNet has other Virtual Network Gateways, their routes will also propagate to your route tables. If you delete the on-ramp, route propagation will not be disabled.</li>
<li>By default, Network Security Groups in Azure contain Allow rules for outbound/inbound traffic to/from the <code>VirtualNetwork</code> service tag, which includes Virtual Network Gateway address space (and therefore your Cloudflare WAN Address Space). If you do not want all resources in your VNet to be accessible from Cloudflare WAN, add the appropriate Deny rules to your Network Security Groups (NSGs).</li>
<li>Cloudflare will add a route in Cloudflare WAN for each IPv4 address range in your VNet.</li>
</ul>
<h3 id="gcp">GCP</h3>
<p><img src="/assets/upstream/images/multi-cloud-networking/reference/gcp.png" alt="Diagram showing how Cloudflare creates on-ramps to GCP" /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<p>When using Multi-Cloud Networking (beta) to automatically create on-ramps to your Google Cloud Platform (GCP) account, you should be aware of the following configuration changes Cloudflare will make on your behalf:</p>
<ul>
<li>Cloudflare will reserve a public Internet routable IP address from GCP.</li>
<li>Cloudflare will create a VPN Gateway and two VPN Tunnels in the region you specify.</li>
<li>Cloudflare will create routes for each prefix in your <a href="/multi-cloud-networking/cloud-on-ramps/#cloudflare-wan-address-space">Cloudflare WAN Address Space</a> within your VPC pointing to the VPN Tunnels.</li>
<li>Cloudflare will add routes in Cloudflare WAN for all subnet CIDR prefixes in your VPC. This includes all regions within the VPC. Traffic bound for a region other than the VPN Gateway's region will be subject to GCP's <a href="https://cloud.google.com/vpc/network-pricing#inter-region-data-transfer">Inter-region Pricing</a>.</li>
<li>Traffic sent to and from your VM instances through the VPN Tunnels is still subject to VPC firewall rules, and may <a href="https://cloud.google.com/network-connectivity/docs/vpn/how-to/configuring-firewall-rules#firewall_rules">require further configuration</a>.</li>
</ul>
<h2 id="supported-resources">Supported resources</h2>
<p>Multi-Cloud Networking (beta) discovers the following resource types in your cloud environments. These resources are used to build a comprehensive view of your cloud network topology and connectivity.</p>
<h3 id="aws-1">AWS</h3>
<ul>
<li>AWS Customer Gateway</li>
<li>AWS EC2 Managed Prefix List</li>
<li>AWS EC2 Transit Gateway</li>
<li>AWS EC2 Transit Gateway Prefix List</li>
<li>AWS EC2 Transit Gateway VPC Attachment</li>
<li>AWS Egress Only Internet Gateway</li>
<li>AWS Internet Gateway</li>
<li>AWS Instance</li>
<li>AWS Network Interface</li>
<li>AWS Route Table</li>
<li>AWS Route Table Association</li>
<li>AWS Security Group</li>
<li>AWS Subnet</li>
<li>AWS VPC</li>
<li>AWS VPC IPv4 CIDR Block Association</li>
<li>AWS VPC Security Group Egress Rule</li>
<li>AWS VPC Security Group Ingress Rule</li>
<li>AWS VPN Connection</li>
<li>AWS VPN Connection Route</li>
<li>AWS VPN Gateway</li>
</ul>
<h3 id="azure-1">Azure</h3>
<ul>
<li>Azure Application Security Group</li>
<li>Azure Load Balancer</li>
<li>Azure Load Balancer Backend Address Pool</li>
<li>Azure Load Balancer NAT Pool</li>
<li>Azure Load Balancer NAT Rule</li>
<li>Azure Load Balancer Rule</li>
<li>Azure Local Network Gateway</li>
<li>Azure Network Interface</li>
<li>Azure Network Interface Application Security Group Association</li>
<li>Azure Network Interface Backend Address Pool Association</li>
<li>Azure Network Interface Security Group Association</li>
<li>Azure Network Security Group</li>
<li>Azure Public IP</li>
<li>Azure Route</li>
<li>Azure Route Table</li>
<li>Azure Subnet</li>
<li>Azure Subnet Route Table Association</li>
<li>Azure Virtual Machine</li>
<li>Azure Virtual Machine Gateway Connection</li>
<li>Azure Virtual Network</li>
<li>Azure Virtual Network Gateway</li>
<li>Azure Virtual Network Gateway Connection</li>
</ul>
<h3 id="gcp-1">GCP</h3>
<ul>
<li>Google Compute Address</li>
<li>Google Compute Forwarding Rule</li>
<li>Google Compute Global Address</li>
<li>Google Compute HA VPN Gateway</li>
<li>Google Compute Interconnect Attachment</li>
<li>Google Compute Network</li>
<li>Google Compute Network Firewall Policy</li>
<li>Google Compute Network Firewall Policy Rule</li>
<li>Google Compute Route</li>
<li>Google Compute Router</li>
<li>Google Compute Subnetwork</li>
<li>Google Compute VPN Gateway</li>
<li>Google Compute VPN Tunnel</li>
</ul>
