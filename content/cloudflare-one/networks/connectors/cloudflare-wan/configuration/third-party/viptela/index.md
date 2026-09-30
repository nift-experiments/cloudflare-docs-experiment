---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/viptela/
  description: Integrate Cisco SD-WAN with Zero Trust networking.
  full_title: Cisco SD-WAN · Cloudflare One docs
  head_html: <title>Cisco SD-WAN · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Cisco SD-WAN with Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/viptela/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/viptela/index.md"><meta property="og:title" content="Cisco SD-WAN · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Cisco SD-WAN with Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/viptela/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="IPsec"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/viptela/#page","headline":"Cisco SD-WAN \u00b7 Cloudflare One docs","description":"Integrate Cisco SD-WAN with Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/viptela/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["IPsec"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/viptela/
  schema: 1
---
<p>Cloudflare partners with Cisco's SD-WAN solution to provide users with an integrated SASE solution. The Cisco SD-WAN appliances (physical and virtual) manage subnets associated with branch offices and cloud instances. Anycast tunnels are set up between these SD-WAN edge devices and Cloudflare to securely route Internet-bound traffic. This tutorial describes how to configure the Cisco Catalyst 8000 Edge Platforms (physical or virtual) in the SD-WAN mode for north-south (Internet-bound) use cases.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before setting up a connection between Cisco SD-WAN and Cloudflare, you must have:</p>
<ul>
<li>Purchased Cloudflare WAN (formerly Magic WAN) and Secure Web Gateway.</li>
<li>Cloudflare provisions Cloudflare WAN and Secure Web Gateway.</li>
<li>Received two Cloudflare tunnel endpoints (anycast IP address) assigned to Cloudflare WAN.</li>
<li>Cisco SD-WAN appliances (physical or virtual). This ensures specific Internet-bound traffic from the sites' private networks is routed over the anycast GRE tunnels to Secure Web Gateway to enforce a user's specific web access policies.</li>
<li>A static IP pair to use with the tunnel endpoints. The static IPs should be <code>/31</code> addresses separate from the IPs used in the subnet deployment.</li>
<li>Release 20.6 Controllers and vEdge Device Builds. You should also pair them with devices that are on at least version Cisco IOS XE SD-WAN 17.6. Refer to <a href="https://www.cisco.com/c/en/us/support/docs/routers/sd-wan/215676-cisco-tac-and-bu-recommended-sd-wan-soft.html">Cisco documentation</a> to learn more about Cisco software versions.</li>
</ul>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/5592.md")
</aside>
<h2 id="1-create-a-sig-template-on-cisco-vmanage"><ol>
<li>Create a SIG template on Cisco vManage</li>
</ol></h2>
<p>Cisco vManage is Cisco's SD-WAN management tool that is used to manage all the SD-WAN appliances in branch offices.</p>
<p>For this example scenario, a generic template for <code>SIG-Branch</code> was created.</p>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/viptela/viptela-flow-diagram-gre.png" alt="Traffic flow diagram for GRE" /></p>
<p><em>Note: Labels in this image may reflect a previous product name.</em></p>
<p>To create a Secure Internet Gateway (SIG) using vManage:</p>
<ol>
<li>From <strong>Cisco vManage</strong> under <strong>Configuration</strong>, select <strong>Generic</strong> and <strong>Add Tunnel</strong>.</li>
<li>The table below shows the setting fields and their options.</li>
</ol>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Type/Detail</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Global Template</strong></td>
<td>Factory_Default_Global_CISCO_Template</td>
</tr>
<tr>
<td><strong>Cisco Banner</strong></td>
<td>Factory_Default_Retail_Banner</td>
</tr>
<tr>
<td><strong>Policy</strong></td>
<td>Branch-Local-Policy</td>
</tr>
</tbody>
</table>
<p><strong>Transport &amp; Management VPN settings</strong></p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Type/Detail</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Cisco VPN 0</strong></td>
<td>GCP-Branch-VPN0</td>
</tr>
<tr>
<td><strong>Cisco Secure Internet Gateway</strong></td>
<td>Branch-SIG-GRE-Template</td>
</tr>
<tr>
<td><strong>Cisco VPN Interface Ethernet</strong></td>
<td>GCP-Branch-Public-Internet-TLOC</td>
</tr>
<tr>
<td><strong>Cisco VPN Interface Ethernet</strong></td>
<td>GCP-VPN0-Interface</td>
</tr>
<tr>
<td><strong>Cisco VPN 512</strong></td>
<td>Default_AWS_TGW_CSR_VPN512_V01</td>
</tr>
</tbody>
</table>
<p><strong>Basic Information settings</strong></p>
<table>
<thead>
<tr>
<th>Setting</th>
<th>Type/Detail</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Cisco System</strong></td>
<td>Default_BootStrap_Cisco_System_Template</td>
</tr>
<tr>
<td><strong>Cisco Logging</strong></td>
<td>Default_Logging_Cisco_V01</td>
</tr>
<tr>
<td><strong>Cisco AAA</strong></td>
<td>AWS-Branch-AAA-Template</td>
</tr>
<tr>
<td><strong>Cisco BFD</strong></td>
<td>Default_BFD_Cisco-V01</td>
</tr>
<tr>
<td><strong>Cisco OMP</strong></td>
<td>Default_AWS_TGW_CSR_OMP_IPv46_...</td>
</tr>
<tr>
<td><strong>Cisco Security</strong></td>
<td>Default_Security_Cisco_V01</td>
</tr>
</tbody>
</table>
<p>When creating the Feature Template, you can choose values that apply globally or that are device specific. For example, the <strong>Tunnel Source IP Address</strong>, <strong>Interface Name</strong> and fields from <strong>Update Tunnel</strong> are device specific and should be chosen accordingly.</p>
<h2 id="2-create-tunnels-in-vmanage"><ol start="2">
<li>Create tunnels in vManage</li>
</ol></h2>
<p>From vManage, select <strong>Configuration</strong> &gt; <strong>Templates</strong>. You should see the newly created template where you will update the device values.</p>
<p>Because the template was created to add GRE tunnels, you only need to update the device values. Note that <strong>VPN0</strong> is the default, and the WAN interface used to build the tunnel must be part of <strong>VPN0</strong>.</p>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/viptela/viptela-update-device-template-gre.png" alt="Update template fields for GRE tunnel" /></p>
<h2 id="3-create-tunnels-in-cloudflare"><ol start="3">
<li>Create tunnels in Cloudflare</li>
</ol></h2>
<p>Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">Configure tunnel endpoints</a> for more information on creating a GRE tunnel.</p>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/viptela/viptela-gre-tunnel.png" alt="Established GRE tunnel in Cloudflare dashboard" /></p>
<h2 id="4-define-static-routes"><ol start="4">
<li>Define static routes</li>
</ol></h2>
<p>Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/how-to/configure-routes/#create-a-static-route">Configure static routes</a> for more information on configuring your static routes.</p>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/viptela/viptela-gre-static-routes.png" alt="Established GRE static routes in Cloudflare dashboard" /></p>
<h2 id="5-validate-traffic-flow"><ol start="5">
<li>Validate traffic flow</li>
</ol></h2>
<p>In the example below, a request for <code>neverssl.com</code> was issued, which has a Cloudflare policy blocking traffic to <code>neverssl.com</code>.</p>
<p>On the client VM (192.168.30.3), a blocked response is visible.</p>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/viptela/viptela-curl-traffic-flow.png" alt="cURL example for a request to neverssl.com" /></p>
<p>A matching blocked log line is visible from the Cloudflare logs.</p>
<p><img src="/assets/upstream/images/cloudflare-wan/third-party/viptela/viptela-gre-swg-traffic.png" alt="A blocked log from Gateway Activity Log in the Cloudflare dashboard" /></p>
<h2 id="add-new-tunnels-using-ipsec">Add new tunnels using IPsec</h2>
<p>IPsec tunnels to Cloudflare can only be created on Cisco 8000v in the router mode today. Refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/third-party/cisco-ios-xe/">Cisco IOS XE</a> for more information.</p>
