---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-device-client/
  description: Connect to RDP using the Cloudflare One Client in Zero Trust networking.
  full_title: Connect to RDP using the Cloudflare One Client · Cloudflare One docs
  head_html: <title>Connect to RDP using the Cloudflare One Client · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect to RDP using the Cloudflare One Client in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-device-client/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-device-client/index.md"><meta property="og:title" content="Connect to RDP using the Cloudflare One Client · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect to RDP using the Cloudflare One Client in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-device-client/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="RDP"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-device-client/#page","headline":"Connect to RDP using the Cloudflare One Client \u00b7 Cloudflare One docs","description":"Connect to RDP using the Cloudflare One Client in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-device-client/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["RDP"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-device-client/
  schema: 1
---
<p>The <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> allows users to connect to RDP servers using their preferred RDP client. Cloudflare Tunnel creates a secure, outbound-only connection from your RDP server to Cloudflare's global network; this requires running the <code>cloudflared</code> daemon on the server (or any other host machine within the private network). Users install the Cloudflare One Client on their device and enroll in your Zero Trust organization. Remote devices will be able to connect as if they were on your private network. By default, all devices enrolled in your organization can connect to the RDP server unless you build policies to allow or block specific users.</p>
<p>This example walks through how to set up an RDP server on a Google Cloud Platform (GCP) virtual machine (VM), but you can use any machine that supports RDP connections.</p>
<h2 id="1-set-up-an-rdp-server-in-gcp"><ol>
<li>Set up an RDP server in GCP</li>
</ol></h2>
<ol>
<li>In your <a href="https://console.cloud.google.com/">Google Cloud Console</a>, <a href="https://developers.google.com/workspace/guides/create-project">create a new project</a>.</li>
<li>Go to <strong>Compute Engine</strong> &gt; <strong>VM instances</strong>.</li>
<li>Select <strong>Create instance</strong>.</li>
<li>Name your VM instance, for example <code>windows-rdp-server</code>.</li>
<li>Configure your VM instance:
<ol>
<li>Scroll down to <strong>Boot Disk</strong> and select <strong>Change</strong>.</li>
<li>For <strong>Operating system</strong>, select <em>Windows Server</em>.</li>
<li>Choose a <strong>Version</strong> with Desktop Experience, for example <em>Windows Server 2016 Datacenter</em>.</li>
</ol>
</li>
<li>Once your VM is running, open the dropdown next to <strong>RDP</strong> and select <em>View gcloud command to reset password</em>.</li>
<li>Select <strong>Run in Cloud Shell</strong>.</li>
<li>Run the command in the Cloud Shell terminal. You will be asked to confirm the password reset.</li>
<li>Copy the auto-generated password and username to a safe place.</li>
</ol>
<h2 id="2-install-microsoft-remote-desktop"><ol start="2">
<li>Install Microsoft Remote Desktop</li>
</ol></h2>
<p>You can use any RDP client to access and configure the RDP server.</p>
<p>To access the server through Microsoft Remote Desktop:</p>
<ol>
<li>Download and install <a href="https://apps.microsoft.com/store/detail/microsoft-remote-desktop/9WZDNCRFJ3PS">Microsoft Remote Desktop</a>.</li>
<li>Once downloaded, open Microsoft Remote Desktop and select <strong>Add a PC</strong>.</li>
<li>For <strong>PC name</strong>, enter the public IP address of your RDP server. In GCP, this is the <strong>External IP</strong> of the VM instance.</li>
<li>For <strong>User account</strong>, select <strong>Add User Account</strong> and enter your auto-generated password and username.</li>
<li>Select <strong>Add</strong>. The PC will display in Microsoft Remote Desktop.</li>
<li>To test basic connectivity, double-click the newly added PC.</li>
<li>When asked if you want to continue, select <strong>Continue</strong>.</li>
</ol>
<p>You can now remotely access the RDP server using its public IP. The next steps will configure access to the server using its private IP.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5493.md")
</aside>
<h2 id="3-connect-the-server-to-cloudflare"><ol start="3">
<li>Connect the server to Cloudflare</li>
</ol></h2>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Tunnels</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/">Create a new tunnel</a> or edit an existing <code>cloudflared</code> tunnel.</p>
</li>
<li>
<p>In the Cloudflare dashboard, go to <strong>Networking</strong> &gt; <strong>Routes</strong>.</p>
</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="4">
<li>
<p>Select <strong>Create route</strong> &gt; <strong>Tunnel CIDR</strong>. Select the tunnel you just created, enter the private IP or CIDR address of your server (in GCP, the server IP is the <strong>Internal IP</strong> of the VM instance), and select <strong>Create route</strong>.</p>
</li>
<li>
<p>(Optional) <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/#4-recommended-filter-network-traffic-with-gateway">Set up Zero Trust policies</a> to fine-tune access to your server.</p>
</li>
</ol>
<h2 id="4-set-up-the-client"><ol start="4">
<li>Set up the client</li>
</ol></h2>
<p>To connect your devices to Cloudflare:</p>
<ol>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">Deploy the Cloudflare One Client</a> on your devices in Traffic and DNS mode or <a href="/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/">generate a proxy endpoint</a> and deploy a PAC file.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/device-enrollment/">Create device enrollment rules</a> to determine which devices can enroll to your Zero Trust organization.</li>
</ol>
<h2 id="5-route-private-network-ips-through-the-cloudflare-one-client"><ol start="5">
<li>Route private network IPs through the Cloudflare One Client</li>
</ol></h2>
<p>By default, WARP excludes traffic bound for <a href="https://datatracker.ietf.org/doc/html/rfc1918">RFC 1918 space</a>, which are IP addresses typically used in private networks and not reachable from the Internet. In order for the Cloudflare One Client to send traffic to your <p>private network</p>
, you must configure <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/">Split Tunnels</a> so that the IP/CIDR of your <p>private network</p>
routes through the Cloudflare One Client.</p>
<ol>
<li>First, check whether your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/split-tunnels/#change-split-tunnels-mode">Split Tunnels mode</a> is set to <strong>Exclude</strong> or <strong>Include</strong> mode.</li>
<li>Edit your Split Tunnel routes depending on the mode:</li>
</ol>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5497.md")
</div></div>
<h2 id="6-connect-as-a-user"><ol start="6">
<li>Connect as a user</li>
</ol></h2>
<p>Once the Cloudflare One Client is configured, you can use your RDP client to connect to the server's private IP address (instead of the public IP address used initially).</p>
<p>To connect in Microsoft Remote Desktop:</p>
<ol>
<li>Open Microsoft Remote Desktop and select <strong>Add a PC</strong>.</li>
<li>For <strong>PC name</strong>, enter the private IP address of your RDP server. In GCP, this is the <strong>Internal IP</strong> of the VM instance.</li>
<li>For <strong>User account</strong>, enter your RDP server username and password.</li>
<li>To test Zero Trust connectivity, double-click the newly added PC.</li>
<li>When asked if you want to continue, select <strong>Continue</strong>.</li>
</ol>
<p>You now have secure, remote access to the RDP server.</p>
