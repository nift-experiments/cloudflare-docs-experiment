---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/azure/
  description: Azure in Zero Trust networking.
  full_title: Deploy cloudflared in Azure · Cloudflare One docs
  head_html: <title>Deploy cloudflared in Azure · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Azure in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/azure/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/azure/index.md"><meta property="og:title" content="Deploy cloudflared in Azure · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Azure in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/azure/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Azure"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/azure/#page","headline":"Deploy cloudflared in Azure \u00b7 Cloudflare One docs","description":"Azure in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/azure/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Azure"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-tunnel/deployment-guides/azure/
  schema: 1
---
<p>This guide covers how to connect an Azure Virtual Machine to Cloudflare using our lightweight connector, <code>cloudflared</code>.</p>
<p>We will deploy:</p>
<ul>
<li>An Azure VM that runs a basic HTTP server.</li>
<li>A Cloudflare Tunnel that allows users to connect to the service via either a public hostname or a private IP address.</li>
</ul>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/5338.md")
</aside>
<h3 id="prerequisites">Prerequisites</h3>
<p>To complete the following procedure, you will need to:</p>
<ul>
<li><a href="/fundamentals/manage-domains/add-site/">Add a website to Cloudflare</a></li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/">Deploy the Cloudflare One Client</a> on an end-user device</li>
</ul>
<h2 id="1-create-a-vm-instance-in-azure"><ol>
<li>Create a VM instance in Azure</li>
</ol></h2>
<ol>
<li>
<p>In the Azure portal, go to <strong>Virtual Machines</strong> &gt; <strong>Create</strong> &gt; <strong>Azure virtual machine</strong>.</p>
</li>
<li>
<p>Select a <strong>Resource group</strong> or create a new one.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/connections/connect-apps/azure-1.png" alt="Azure group" /></p>
<ol start="3">
<li>
<p>Enter a name for the VM and select a region. For <strong>Image</strong>, select <em>Ubuntu Server 24.04 LTS</em>. For <strong>Size</strong>, select an appropriate size (for example, <em>Standard_B1s</em>).</p>
</li>
<li>
<p>Under <strong>Administrator account</strong>, select <strong>SSH public key</strong> and enter your key pair.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/connections/connect-apps/azure-2.png" alt="Azure keypair" /></p>
<ol start="5">
<li>Under <strong>Inbound port rules</strong>, allow SSH (<code>22</code>). For testing purposes, also allow HTTP (<code>80</code>) and HTTPS (<code>443</code>).</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/connections/connect-apps/azure-3.png" alt="Azure ports" /></p>
<ol start="6">
<li>
<p>Select <strong>Review + create</strong>, then <strong>Create</strong>.</p>
</li>
<li>
<p>Once the VM is running, copy its <strong>Public IP address</strong> from the VM overview page. Also record the <strong>Private IP address</strong> — Azure by default uses the <code>10.0.0.0/8</code> subnet.</p>
</li>
<li>
<p>SSH into the instance:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">ssh -i &quot;your-key.pem&quot; azureuser@&lt;PUBLIC_IP&gt;&#10;</code></pre>
<ol start="9">
<li>
<p>Run <code>sudo su</code> to gain full admin rights to the VM.</p>
</li>
<li>
<p>For testing purposes, you can deploy a basic Apache web server on port <code>80</code>:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-bash">apt update&#10;&#10;apt -y install apache2&#10;&#10;cat &lt;&lt;EOF &gt; /var/www/html/index.html&#10;&lt;html&gt;&lt;body&gt;&lt;h1&gt;Hello Cloudflare!&lt;/h1&gt;&#10;&lt;p&gt;This page was created for a Cloudflare demo.&lt;/p&gt;&#10;&lt;/body&gt;&lt;/html&gt;&#10;EOF&#10;</code></pre>
<ol start="11">
<li>To verify that the Apache server is running, open a browser and go to <code>http://&lt;PUBLIC_IP&gt;</code> (make sure to connect over <code>http</code>, not <code>https</code>). You should see the <strong>Hello Cloudflare!</strong> test page.</li>
</ol>
<h2 id="2-create-a-cloudflare-tunnel"><ol start="2">
<li>Create a Cloudflare Tunnel</li>
</ol></h2>
<p>Create a Cloudflare Tunnel and run it on the Azure VM.</p>
<ol>
<li>Log in to the Cloudflare dashboard and go to <strong>Networking</strong> &gt; <strong>Tunnels</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select <strong>Create a tunnel</strong>.</p>
</li>
<li>
<p>Enter a name for your tunnel (for example, <code>azure-tunnel</code>).</p>
</li>
<li>
<p>Select <strong>Create Tunnel</strong>.</p>
</li>
<li>
<p>Choose your operating system (select <strong>Debian</strong> for your Azure VM). Copy the installation command and run it on your Azure VM.</p>
</li>
<li>
<p>Wait for the tunnel to connect. Once the connection is established, select <strong>Continue</strong>.</p>
</li>
</ol>
<h2 id="3-connect-using-a-public-hostname"><ol start="3">
<li>Connect using a public hostname</li>
</ol></h2>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/routing-to-tunnel/">Published applications</a> allow anyone on the Internet to connect to HTTP resources hosted on your virtual private cloud (VPC). To add a published application for your Cloudflare Tunnel:</p>
<ol>
<li>On the <strong>Routes</strong> tab, select <strong>Add route</strong>, then select <strong>Published application</strong>.</li>
<li>Enter a hostname for the application (for example, <code>hellocloudflare.&lt;your-domain&gt;.com</code>).</li>
<li>Under <strong>Service</strong>, enter <code>http://localhost:80</code>.</li>
<li>Select <strong>Add route</strong>.</li>
<li>To test, open a browser and go to <code>http://hellocloudflare.&lt;your-domain&gt;.com</code>. You should see the <strong>Hello Cloudflare!</strong> test page.</li>
</ol>
<p>You can optionally <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">create an Access application</a> to control who can access the service.</p>
<h2 id="4-connect-using-a-private-ip"><ol start="4">
<li>Connect using a private IP</li>
</ol></h2>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/">Private network routes</a> allow users to connect to your Azure Virtual Network (VNet) using the Cloudflare One Client. To add a private network route for your Cloudflare Tunnel:</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Routes</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Select <strong>Create route</strong> &gt; <strong>Tunnel CIDR</strong>. Select the tunnel you just created, enter the <strong>Private IP address</strong> of your Azure VM (for example, <code>10.0.0.4</code>), and select <strong>Create route</strong>. You can expand the IP range later if necessary.</p>
</li>
<li>
<p>In your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#add-a-route">Split Tunnel configuration</a>, make sure the private IP is routing through the Cloudflare One Client. For example, if you are using Split Tunnels in <strong>Exclude</strong> mode, delete <code>10.0.0.0/8</code>. We recommend re-adding the IPs that are not explicitly used by your Azure VM.</p>
<pre tabindex="0"><code>To determine which IP addresses to re-add, subtract your Azure VM IPs from &lt;code&gt;10.0.0.0/8&lt;/code&gt;:&#10;</code></pre>
</li>
</ol>
<div class="nb-interactive-component" data-cf-component="SubtractIPCalculator"></div>
<pre tabindex="0"><code>    Add the results back to your Split Tunnel Exclude mode list.&#10;</code></pre>
<ol start="4">
<li>
<p>To test on a user device:</p>
<ol>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/">Log in to the Cloudflare One Client</a>.</li>
<li>Open a terminal window and connect to the service using its private IP:</li>
</ol>
<pre tabindex="0"><code class="language-sh">`curl 10.0.0.4`</code></pre>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">&lt;html&gt;&lt;body&gt;&lt;h1&gt;Hello Cloudflare!&lt;/h1&gt;&#10;&lt;p&gt;This page was created for a Cloudflare demo.&lt;/p&gt;&#10;&lt;/body&gt;&lt;/html&gt;&#10;</code></pre>
<p>You can optionally <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/#4-recommended-filter-network-traffic-with-gateway">create Gateway network policies</a> to control who can access the Azure VM via its private IP.</p>
<h2 id="firewall-configuration">Firewall configuration</h2>
<p>To secure your Azure VM, you can configure your <a href="https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview">Network Security Group (NSG)</a> to deny all inbound traffic and allow only outbound traffic to the <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-with-firewall/#required-for-tunnel-operation">Cloudflare Tunnel IP addresses</a>. All NSG rules are evaluated by priority; traffic that does not match an allow rule is blocked by the default deny rules. Therefore, you can delete all custom inbound rules and leave only the relevant outbound rules.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5337.md")
</aside>
<p>After configuring your NSG rules, verify that you can still access the service through Cloudflare Tunnel via its <a href="#3-connect-using-a-public-hostname">public hostname</a> or <a href="#4-connect-using-a-private-ip">private IP</a>. The service should no longer be accessible from outside Cloudflare Tunnel — for example, direct access to the VM's public IP should no longer work.</p>
