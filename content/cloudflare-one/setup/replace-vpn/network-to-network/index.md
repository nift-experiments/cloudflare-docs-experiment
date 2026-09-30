---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/network-to-network/
  description: Connect two private networks using Cloudflare Mesh nodes and Cloudflare's network.
  full_title: Network to network · Cloudflare One docs
  head_html: <title>Network to network · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect two private networks using Cloudflare Mesh nodes and Cloudflare&#x27;s network."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/network-to-network/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/network-to-network/index.md"><meta property="og:title" content="Network to network · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect two private networks using Cloudflare Mesh nodes and Cloudflare&#x27;s network."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/network-to-network/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Get started"><meta name="algolia_content_type" content="Get started"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Linux,Private networks"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/network-to-network/#page","headline":"Network to network \u00b7 Cloudflare One docs","description":"Connect two private networks using Cloudflare Mesh nodes and Cloudflare's network.","url":"https://developers.cloudflare.com/cloudflare-one/setup/replace-vpn/network-to-network/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Linux","Private networks"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/setup/replace-vpn/network-to-network/
  schema: 1
---
<p>Connect two separate private networks so devices on each network can send and receive traffic in both directions through Cloudflare. This is useful when you need to link office locations, data centers, or cloud environments. For example, employees in one office could access a file server, printer, or internal application in another office.</p>
<p>To explore other connection scenarios, refer to <a href="/cloudflare-one/setup/replace-vpn/">Replace your VPN</a>.</p>
<h2 id="how-it-works">How it works</h2>
<p><a href="/mesh/">Cloudflare Mesh</a> (formerly WARP Connector) lets you deploy mesh nodes — lightweight network connectors that you install on a single Linux device in each network. That device handles traffic for the entire network: it sends outbound traffic to Cloudflare and receives inbound traffic back, then passes it to the right device on the network. Because of this, other devices on the network do not need to install any software.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a>.</li>
<li>A Linux device or virtual machine on your first private network. This is where you install your first mesh node.</li>
<li>A second Linux device or virtual machine on a separate private network. This is where you install your second mesh node.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5942.md")
</aside>
<h2 id="step-1-create-your-first-mesh-node">Step 1: Create your first mesh node</h2>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Mesh</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Add a node</strong>.</li>
<li>Enter a name for the node (for example, <code>office-a</code>).</li>
<li>Follow the wizard to configure enrollment and device profile settings.</li>
<li>Copy the install commands from the wizard and run them on your Linux device.</li>
<li>After the node connects, the dashboard confirms it is online.</li>
</ol>
<h2 id="step-2-add-a-route-for-the-first-network">Step 2: Add a route for the first network</h2>
<ol>
<li>Go to the node detail page for your first node.</li>
<li>Select the <strong>Routes</strong> tab.</li>
<li>Select <strong>Add a route</strong>.</li>
<li>Enter the IP range of your first network (for example, <code>10.0.0.0/24</code>).</li>
<li>Select <strong>Create</strong>.</li>
</ol>
<h2 id="step-3-create-your-second-mesh-node">Step 3: Create your second mesh node</h2>
<p>Repeat <a href="#step-1-create-your-first-mesh-node">Step 1</a> on a Linux device in your second network. Give it a distinct name (for example, <code>office-b</code>).</p>
<h2 id="step-4-add-a-route-for-the-second-network">Step 4: Add a route for the second network</h2>
<p>Repeat <a href="#step-2-add-a-route-for-the-first-network">Step 2</a> for your second node, entering the IP range of your second network (for example, <code>192.168.1.0/24</code>). The IP range must not overlap with your first network.</p>
<h2 id="step-5-forward-device-traffic">Step 5: Forward device traffic</h2>
<p>If the mesh node is installed on your network's router (the device that serves as the default gateway), other devices on the network automatically send traffic through it. No additional configuration is needed, and you can skip this step.</p>
<p>If the mesh node is installed on a different device, other devices on the network need a static route so they know to send cross-network traffic to the mesh node. Without this route, devices do not know where to send traffic destined for the other network.</p>
<p>For details on routing options, refer to <a href="/mesh/features/routes/">Routes</a>.</p>
<h2 id="step-6-verify-your-connection">Step 6: Verify your connection</h2>
<p>Devices on both networks can now communicate through Cloudflare. To verify connectivity, try reaching a device on the opposite network (for example, <code>ping 192.168.1.100</code> from a device on your first network).</p>
<h2 id="recommended-next-steps">Recommended next steps</h2>
<p>After verifying your connection, consider securing your connected networks with policies and access controls:</p>
<ul>
<li><strong>Set up Gateway policies</strong>: By default, all traffic between your network segments flows through Cloudflare without restriction. Gateway policies let you scan, filter, and log traffic between your networks. For more information, refer to <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS policies</a>, <a href="/cloudflare-one/traffic-policies/network-policies/">Network policies</a>, and <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP policies</a>.</li>
<li><strong>Create an Access application</strong>: Restrict access to specific services or hosts on your connected networks with identity-based rules. For more information, refer to <a href="/cloudflare-one/access-controls/applications/non-http/self-hosted-private-app/">Secure a private IP or hostname</a>.</li>
<li><strong>Enable high availability</strong>: Deploy multiple replicas of each mesh node for automatic failover. For more information, refer to <a href="/mesh/features/high-availability/">High availability</a>.</li>
</ul>
<p>For in-depth guidance on policy design and device posture checks, refer to the <a href="/learning-paths/replace-vpn/concepts/">Replace your VPN learning path</a>.</p>
<h2 id="troubleshoot">Troubleshoot</h2>
<p>If you have issues connecting, refer to these resources:</p>
<ul>
<li><a href="/mesh/best-practices/">Tips and best practices</a>: review common Cloudflare Mesh configuration tips and troubleshooting strategies.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/">Troubleshoot tunnels</a>: diagnose tunnel connectivity and routing problems.</li>
</ul>
