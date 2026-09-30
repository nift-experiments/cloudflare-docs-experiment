---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/configure-hardware-appliance/
  description: Configure hardware Connector in Zero Trust networking.
  full_title: Configure hardware Connector · Cloudflare One docs
  head_html: <title>Configure hardware Connector · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure hardware Connector in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/configure-hardware-appliance/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/configure-hardware-appliance/index.md"><meta property="og:title" content="Configure hardware Connector · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure hardware Connector in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/configure-hardware-appliance/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/configure-hardware-appliance/#page","headline":"Configure hardware Connector \u00b7 Cloudflare One docs","description":"Configure hardware Connector in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/configure-hardware-appliance/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/configure-hardware-appliance/
  schema: 1
---
<p>In this page you will find instructions on how to configure Cloudflare One Appliance. This guide provides a step-by-step guide for Cloudflare One Appliance initial setup. You can either return here after setting up your Cloudflare One Appliance, or refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/">Maintenance</a> section where you will find instructions on how to update your settings.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>You need to purchase <a href="https://www.cloudflare.com/magic-wan/">Cloudflare WAN</a> before you can purchase and use Cloudflare One Appliance. Cloudflare One Appliance can function as your primary edge device for your network, or be deployed in-line with existing network gear.</p>
<p>You also need to purchase Cloudflare One Appliance before you can start configuring your settings in the Cloudflare dashboard. Contact your account representative to learn more about purchasing options for Cloudflare One Appliance.</p>
<hr />
<h2 id="before-you-begin">Before you begin</h2>
<p>There are a couple of decisions you need to make when installing your Cloudflare One Appliance. Review the following topics for more information.</p>
<h3 id="determine-the-need-for-a-high-availability-configuration">Determine the need for a high availability configuration</h3>
<p>You can install up to two instances of Cloudflare One Appliance for redundancy at each of your sites. If one of your devices fails, traffic will fail over to the other, ensuring that you never lose connectivity to that site.</p>
<p>In this type of high availability (HA) configuration, you will choose a reliable LAN interface as the HA link which will be used to monitor the health of the peer connector. HA links can be dedicated links or can be shared with other LAN traffic.</p>
<p>You must decide the type of configuration you want for your site from the beginning: no redundancy or with redundancy. You cannot add redundancy after finishing the configuration of your dashboard settings. If, at a later stage, you decide to enable redundancy, you will need to delete your Cloudflare One Appliance device in the Cloudflare dashboard, and start again.</p>
<div class="nb-card"><h3 class="nb-component-title" id="do-you-need-a-high-availability-configuration">Do you need a high availability configuration?</h3>
@markup("md", "content/.markup/bodies/5767.md")
</div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5766.md")
</aside>
<h3 id="decide-on-dhcp-vs-static-ip-connections">Decide on DHCP vs static IP connections</h3>
<p>You can use Cloudflare One Appliance in both DHCP networks and networks that require a static IP configuration. At first boot, however, Cloudflare One Appliance needs to reach out to Cloudflare to download your settings and go through the activation process. If any of the networks plugged into your Cloudflare One Appliance device are DHCP enabled, do not use a VLAN, and have an Internet connection, that process is handled automatically. However, if all of the networks require more information to utilize, (such as a network with static IPs, or tagged VLAN networks) your Cloudflare One Appliance might need some more information to proceed.</p>
<p>There are couple of ways to provide this information. Choose the one that fits your workflow:</p>
<h4 id="option-one-activate-on-a-dhcp-network">Option one - Activate on a DHCP Network</h4>
<ol>
<li>Connect Cloudflare One Appliance to a DHCP port with access to the Internet.</li>
<li>Follow the <a href="#set-up-cloudflare-dashboard">setup flow</a> and activate your Cloudflare One Appliance device.</li>
<li>Refer to <a href="#wan-with-a-static-ip-address">WAN with a static IP address</a>.</li>
</ol>
<h4 id="option-two-bootstrap-via-serial-console">Option two - Bootstrap via Serial Console</h4>
<p>Refer to the <a href="#bootstrap-via-serial-console">Bootstrap workflow</a>.</p>
<hr />
<h2 id="port-speeds">Port speeds</h2>
<p>The hardware version of the Cloudflare One Appliance includes two <a href="https://en.wikipedia.org/wiki/Small_Form-factor_Pluggable">SFP+ ports</a> that support 10G throughput, as well as six RJ45 ports that support 1G throughput.</p>
<p>Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/configure-hardware-appliance/sfp-port-information/">SFP+ port information</a> for details on this topic.</p>
<hr />
<h2 id="set-up-cloudflare-dashboard">Set up Cloudflare dashboard</h2>
<h3 id="register-your-appliance">Register your Appliance</h3>
<p>To set up and use the hardware version of Cloudflare One Appliance (formerly Magic WAN Connector), you first need to register it with your account. This is not applicable to Virtual Cloudflare One Appliance.</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, and go to <strong>Networks</strong>.</li>
<li>Go to <strong>Connectors</strong> &gt; <strong>Appliances</strong>, and select <strong>Register an appliance</strong>.</li>
<li>In <strong>Appliance details</strong> &gt; <strong>Serial number</strong>, insert the serial number for your device. You can optionally add notes about the Cloudflare One Appliance you are adding to the dashboard.</li>
<li>(Optional) Select <strong>Add</strong> under <strong>Serial number</strong> to add multiple Cloudflare One Appliances at once to your account.</li>
<li>Select <strong>Register appliance</strong>.</li>
</ol>
<p>Your device is now registered with your account.</p>
<h3 id="create-a-new-profile">Create a new profile</h3>
<p>You need to create a profile for your appliance before connecting it to the Internet.</p>
<p>To create a profile:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, and go to <strong>Networks</strong>.</li>
<li>Go to <strong>Connectors</strong> &gt; <strong>Appliances</strong> &gt; <strong>Create a profile</strong>.</li>
<li>In <strong>Name</strong>, enter a descriptive name for your Cloudflare One Appliance. Optionally, you can also add a description for it.</li>
<li>You need to decide if you want to turn on high availability for the Cloudflare One Appliance. For details, refer to <a href="#about-high-availability-configurations">About high availability configurations</a>.</li>
<li>Select <strong>Create and continue</strong>.</li>
<li>Select <strong>Add Appliance</strong>. This will display a list of devices associated with your account. You need to have bought a Connector already for it to show up here. Refer to <a href="#prerequisites">Prerequisites</a> if no Connector shows up in this list.</li>
<li>If you have more than one Cloudflare One Appliance, choose the one that corresponds to the on-ramp you are creating. Cloudflare One Appliance devices are identified by a serial number, also known as a service tag. Use this information to choose the right Cloudflare One Appliance. <br /> Select <strong>Add Appliance</strong> when you are ready to proceed.</li>
<li>Cloudflare One Appliance will be added to your account with an <strong>Interrupt window</strong> defined. The interrupt window is the time period when the Cloudflare One Appliance software can update, which may result in interruption to existing connections. You can change this later. Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/interrupt-service-window/">Interrupt window</a> for more details on how to define when the Cloudflare One Appliance can update its systems.</li>
<li>Select <strong>Continue</strong> to proceed to creating your WAN and LAN networks.</li>
</ol>
<h3 id="create-a-wan">Create a WAN</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5772.md")
</div></div>
<h3 id="create-a-lan">Create a LAN</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5776.md")
</div></div>
<h4 id="network-segmentation">Network segmentation</h4>
<p>After setting up your LANs, you can configure your Cloudflare One Appliance to enable communication between them without traffic leaving your premises. For details, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/network-segmentation/">Network segmentation</a>.</p>
<h4 id="dhcp-options">DHCP options</h4>
<p>Cloudflare One Appliance supports different types of DHCP configurations. Cloudflare One Appliance can:</p>
<ul>
<li>Connect to a DHCP server or use a static IP address instead of connecting to a DHCP server.</li>
<li>Act as a <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-server/">DHCP server</a>.</li>
<li>Use <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-relay/">DHCP relay</a> to connect to a DHCP server outside the location your Cloudflare One Appliance is in.</li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-static-address-reservation/">Reserve IP addresses</a> for specific devices on your network.</li>
</ul>
<h3 id="add-your-cloudflare-one-appliance-to-a-site">Add your Cloudflare One Appliance to a site</h3>
<p>After finishing your Cloudflare One Appliance configuration, you need to add it to a site. Sites represent the local network of a data center, office, or other physical location, and combine all on-ramps available there. Sites also allow you to check, at a glance, the state of your on-ramps and set up health alert settings so that Cloudflare notifies you when there are issues with the site's on-ramps.</p>
<p>Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/sites/">Set up a site</a> for more information.</p>
<h2 id="set-up-your-cloudflare-one-appliance">Set up your Cloudflare One Appliance</h2>
<h3 id="device-installation">Device installation</h3>
<p>There are several deployment options for Cloudflare One Appliance. Cloudflare One Appliance can act like a DHCP server for your local network, or integrate with your local setup and have static IP addresses assigned to it.</p>
<p>When Cloudflare One Appliance acts like the WAN router for your site, deployment will be something like this:</p>
<pre tabindex="0" class="mermaid">&#10;&#10;{`flowchart LR&#10;	accTitle: Appliance as WAN router&#10;	accDescr: Cloudflare One Appliance set up as a DHCP server, and connecting to the Internet.&#10;	a(Cloudflare One Appliance)--> b(Internet) --> c(Cloudflare)&#10;&#10;	subgraph Customer site&#10;	d[LAN 1] --> a&#10;	e[LAN 2] --> a&#10;	end&#10;&#10;	classDef orange fill:#f48120,color: black&#10;	class a,c orange`}&#10;&#10;</pre>
<p><em>Cloudflare One Appliance set up as a DHCP server, and connecting to the Internet.</em></p>
<p>In the following example, the Cloudflare One Appliance device sits behind the WAN router in your site, and on-ramps only some of the existing LANs to Cloudflare.</p>
<pre tabindex="0" class="mermaid">&#10;&#10;{`flowchart LR&#10;	accTitle: Appliance behind site router&#10;	accDescr: Cloudflare One Appliance connects to the router in the site, and only some of the LANs connect to Appliance.&#10;	a(Cloudflare One Appliance)--> b((Site's router)) --> c(Internet) --> i(Cloudflare)&#10;&#10;	subgraph Customer site&#10;	d[LAN 1] --> a&#10;	e[LAN 2] --> a&#10;	g(LAN 3) --> b&#10;	h(LAN 4) --> b&#10;	end&#10;&#10;	classDef orange fill:#f48120,color: black&#10;	class a,i orange`}&#10;&#10;</pre>
<p><em>Cloudflare One Appliance connects to the router in the site, and only some of the LANs connect to Appliance.</em></p>
<p>Refer to <a href="/reference-architecture/diagrams/sase/cloudflare-one-appliance-deployment/">Cloudflare One Appliance deployment options</a> for a high-level explanation of the deployment options that make sense to most environments, as well as a few advanced use cases.</p>
<h4 id="firewall-settings-required">Firewall settings required</h4>
<p>If there is a firewall deployed upstream of Cloudflare One Appliance, configure the firewall to allow the following traffic:</p>
<table>
<thead>
<tr>
<th>Protocol/port</th>
<th>Destination IP/URL</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>UDP/53</code></td>
<td>DNS destination IP <code>1.1.1.1</code></td>
<td>Needed to allow DNS traffic to Cloudflare DNS servers. Cloudflare uses this port for DNS lookups of control plane API.</td>
</tr>
<tr>
<td><code>TCP/443</code></td>
<td>-</td>
<td>Cloudflare One Appliance will open outbound HTTPS connections over this port for control plane operations.</td>
</tr>
<tr>
<td><code>UDP/4500</code></td>
<td>Destination IP <code>162.159.64.1</code></td>
<td>Needed for Cloudflare One Appliance initialization and discovery through outbound connections.</td>
</tr>
<tr>
<td><code>UDP/4500</code></td>
<td>Destination IP - Cloudflare anycast IPs</td>
<td>Needed for the Cloudflare anycast IPs assigned to your account for tunnel outbound connections. This traffic is tunnel traffic.</td>
</tr>
<tr>
<td><code>TCP/7844</code>, <code>UDP/7844</code></td>
<td>Outbound connections</td>
<td>Used to support debugging features in Cloudflare One Appliance.</td>
</tr>
<tr>
<td><code>UDP/123</code></td>
<td><code>http://time.cloudflare.com/</code></td>
<td>Needed for Cloudflare One Appliance to periodically contact Cloudflare's Time Services.</td>
</tr>
</tbody>
</table>
<h2 id="activate-appliance">Activate appliance</h2>
<p>The Connector is shipped to you deactivated, and will only establish a connection to the Cloudflare network when it is activated. Cloudflare recommends leaving it deactivated until you finish <a href="#set-up-cloudflare-dashboard">setting it up in the dashboard</a>.</p>
<p>When Cloudflare One Appliance is first activated, you need to have Internet connection. If you chose to set up your Cloudflare One Appliance with DHCP you will need to have one of the Cloudflare One Appliance ports connected to the Internet through a device that supports DHCP. This is required so that the Cloudflare One Appliance can reach the Cloudflare global network and download the required configurations that you <a href="#set-up-cloudflare-dashboard">set up</a>.</p>
<p>If you set up your Cloudflare One Appliance with a static IP through the bootstrap method, you do not need a DHCP port. For details, refer to <a href="#decide-on-dhcp-vs-static-ip-connections">DHCP vs static IP connections</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5777.md")
</aside>
<p>When you are ready to connect your Cloudflare One Appliance to the Cloudflare network:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, and go to <strong>Networks</strong>.</li>
<li>Go to <strong>Connectors</strong> &gt; <strong>Appliances</strong>.</li>
<li>Find the Cloudflare One Appliance you want to activate, select the three dots next to it &gt; <strong>Edit</strong>. Make sure you verify the serial number to choose the right Cloudflare One Appliance you want to activate.</li>
<li>In the new window, the <strong>Status</strong> dropdown will show as <strong>Deactivated</strong>. Select it to change the status to <strong>Activated</strong>.</li>
<li>The <strong>Interrupt window</strong> is the time period when the Cloudflare One Appliance software can update, which may result in interruption to existing connections. Choose a time period to minimize disruption to your sites. For details on defining when the Cloudflare One Appliance can update its systems, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/interrupt-service-window/">Interrupt window</a>.</li>
<li>Select <strong>Update</strong>.</li>
</ol>
<hr />
<h2 id="wan-with-a-static-ip-address">WAN with a static IP address</h2>
<p>After activating your device, you can use it in a network configuration with the WAN interface set to a static IP address — that is, an Internet configuration that is not automatically set by DHCP. To use your Cloudflare One Appliance on a network configuration with a static IP, follow these steps:</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5778.md")
</aside>
<ol>
<li>Connect Cloudflare One Appliance to a DHCP port with access to the Internet.</li>
<li><a href="#create-a-new-profile">Create a new profile</a> in the dashboard.</li>
<li>Create a <a href="#create-a-wan">DHCP WAN</a>.</li>
<li><a href="#activate-appliance">Activate</a> and power on your Cloudflare One Appliance.</li>
<li>Wait 60 seconds.</li>
<li>Make changes to the <a href="#create-a-wan">WAN settings</a> in the dashboard to a static IP set up.</li>
<li>Wait 60 seconds again.</li>
<li>Cloudflare One Appliance will go offline. This is normal and expected behavior.</li>
<li>Adjust your physical connections as required to match the static configuration.</li>
<li>Cloudflare One Appliance comes back online.</li>
</ol>
<h2 id="bootstrap-via-serial-console">Bootstrap via Serial Console</h2>
<p>Advanced users can locally configure their Cloudflare One Appliance to work in a static IP configuration. This local method does not require having access to a DHCP Internet connection. However, it does require being comfortable with using tools to access the serial port on Cloudflare One Appliance as well as using a serial terminal client to access the environment in your Cloudflare One Appliance.</p>
<p>The following is a detailed description of how to use the serial port to configure your Cloudflare One Appliance locally.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5779.md")
</aside>
<h3 id="equipment-required">Equipment required</h3>
<p>To access the serial port on Cloudflare One Appliance you will need the following equipment:</p>
<ul>
<li>The Cloudflare One Appliance device</li>
<li>A Phillips-head screwdriver</li>
<li>A micro-USB to USB-A cable (there should be one included in the packaging of your Cloudflare One Appliance device)</li>
<li>A computer with an available USB port</li>
<li>A serial terminal client</li>
<li>Optional: if needed, a USB-A to USB-C converter dongle if your computer requires it</li>
</ul>
<h3 id="1-access-the-device-s-serial-port"><ol>
<li>Access the device's serial port</li>
</ol></h3>
<ol>
<li>Using the Phillips screwdriver, loosen the screw covering the serial console panel on the back of the Cloudflare One Appliance and turn the panel out of the way.
<ul>
<li>Pictures and more instructions can be found on <a href="https://www.dell.com/support/kbdoc/en-us/000134440/how-to-access-console-port-of-dell-emc-networking-virtual-edge-platform-1405-series">Dell's Technical Documents</a>.</li>
</ul>
</li>
<li>Connect your computer to your Cloudflare One Appliance device using the USB cable.</li>
</ol>
<h4 id="default-password">Default password</h4>
<p>The default password for your Cloudflare One Appliance device is the serial number (also known as a Service Tag for Dell devices), all uppercase followed by an <code>!</code> (for example, <code>A1B2C3D!</code>)</p>
<h3 id="2-install-a-serial-terminal-client"><ol start="2">
<li>Install a serial terminal client</li>
</ol></h3>
<p>To access the Cloudflare One Appliance device environment you need a serial terminal client. Follow these instructions to install one, based on your operating system.</p>
<h4 id="windows">Windows</h4>
<p>Cloudflare recommends using PuTTY for Windows. Download PuTTY from the <a href="https://www.putty.org/">official website</a> and then install it.</p>
<ol>
<li>Check the COM port of the USB to UART device in the Windows Device Manager. It should appear as something similar to <code>Silicon Labs CP210x USB to UART Bridge (COMX)</code>.</li>
<li>Take note of the value in the parentheses (COMX).
<ul>
<li>For details on creating a serial console connection, refer to the <a href="https://infohub.delltechnologies.com/l/virtual-edge-platform-vep-1405-series-diag-os-and-tools-release-notes/bios-installation-and-configuration">Dell Documentation Page</a>.</li>
</ul>
</li>
<li>Launch PuTTY.</li>
<li>Under <strong>Category</strong>, make sure that <strong>Session</strong> (the first item) is selected.</li>
<li>Under <strong>Connection type</strong>, select <strong>Serial</strong>.</li>
<li>In the <strong>Serial Line</strong>, type in the COM port found in step 2 (for example, <code>COM1</code>).</li>
<li>In the <strong>Speed</strong>, enter <code>115200</code>.</li>
<li>Select Open on the bottom of the dialog box. A terminal window should pop up.</li>
<li>The screen may need to be manually refreshed when a new device is connected. You can do that by pressing <code>CTRL + C</code>.</li>
</ol>
<h4 id="macos">macOS</h4>
<p>Cloudflare recommends installing Screen for macOS. You can install Screen via <code>brew install screen</code>. If you do not have <code>brew</code> installed, follow the instructions on <a href="https://brew.sh/">Brew's Official Website</a> to install it.</p>
<ol>
<li>Open the macOS Terminal.</li>
<li>Run <code>ls /dev/cu.*</code> to list the connected serial devices.</li>
<li>The command should return an output similar to <code>/dev/cu.usbserial-0001</code>. Copy this output to the clipboard or note this down somewhere else.</li>
<li>Run <code>sudo screen -adRUS mconn &lt;PATH_FROM_STEP_3&gt; 115200</code>.</li>
<li>The screen may need to be manually refreshed when a new device is connected. You can do that by pressing <code>CMD + C</code>.</li>
</ol>
<h4 id="linux">Linux</h4>
<p>Cloudflare recommends installing Screen for Linux. You can install Screen via your package manager of choice. For example, for Debian/Ubuntu, install by running <code>sudo apt update &amp;&amp; sudo apt install screen</code></p>
<ol>
<li>Open Terminal.</li>
<li>List the connected serial devices by running <code>ls /dev/serial/by-id/*</code>.</li>
<li>The command should return an output similar to <code>/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0</code>. Copy this to the clipboard or note this down.</li>
<li>Run <code>sudo screen -adRUS mconn &lt;PATH_FROM_STEP_3&gt; 115200</code>.</li>
<li>The screen may need to be manually refreshed when a new device is connected. You can do that by pressing <code>CTRL + C</code>.</li>
</ol>
<h3 id="3-configure-a-static-ip"><ol start="3">
<li>Configure a static IP</li>
</ol></h3>
<p>The <code>reset device</code> option in your Cloudflare One Appliance clears most of the configuration that is locally cached, resets the password to the default, and reboots.</p>
<ol>
<li>Log into your Cloudflare One Appliance device. You will be prompted to change your password if you attempt to log in with the default password.</li>
<li>From the menu, go to <strong>Bootstrap</strong> with the arrow keys and select it with the Enter key.</li>
<li>Select the jack (physical port) you want to configure for the initialization of the appliance.</li>
<li>Enter the VLAN tag (if applicable) of the network. Leave it blank if untagged.</li>
<li>Select the <code>static</code> option as your network type.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5780.md")
</aside>
<ol start="6">
<li>Enter the IP address you would like the appliance to have in CIDR form (for example, <code>10.0.0.2/24</code>).</li>
<li>Enter the IP address of the Internet gateway (this must be in the same subnet as the previous IP address you entered and must not be the same address).</li>
<li>Select <strong>Save</strong> and confirm that you want to use the new settings.</li>
<li>The Cloudflare One Appliance will download the rest of the settings from Cloudflare. The last heartbeat of the Cloudflare One Appliance should update once it has made contact with Cloudflare.</li>
</ol>
<hr />
<h2 id="about-high-availability-configurations">About high availability configurations</h2>
<p>You need to deploy two Connectors in your premises before you can set up a site in high availability. When you set up a site in high availability, the WANs and LANs in your Cloudflare One Appliance have the same configuration but are replicated on two nodes. In case of failure of one of the devices, the other device becomes the active node, taking over the configuration of the LAN gateway IP and allowing traffic to continue without disruption.</p>
<p>Because Cloudflare One Appliances in high availability configurations share a single site, you need to set up:</p>
<ul>
<li><strong>Static address</strong>: The IP for the primary node in your site.</li>
<li><strong>Secondary static address</strong>: The IP for the secondary node in your site.</li>
<li><strong>Virtual static address</strong>: The IP that the LAN south of the Cloudflare One Appliance device will forward traffic to, which is the LAN's gateway IP.</li>
</ul>
<p>Make sure all IPs are part of the same subnet.</p>
<p>For detailed information about the expected behavior of high availability configurations, refer to the <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/reference/#high-availability-configurations">High availability configurations</a> reference page.</p>
<h3 id="create-a-high-availability-configuration">Create a high availability configuration</h3>
<p>You cannot enable high availability for an existing site. To add high availability to an existing site in the Cloudflare dashboard, you need to delete the site and start again.</p>
<p>To set up a high availability configuration:</p>
<ol>
<li>Follow the steps in <a href="#create-a-new-profile">Create a new profile</a> up until step 4.</li>
<li>After naming your site, select <strong>Turn on high availability</strong>.</li>
<li>Select <strong>Create and continue</strong>.</li>
<li>Select <strong>Add Appliance</strong>.</li>
<li>From the list, choose your first Cloudflare One Appliance &gt; <strong>Add Appliance</strong>.</li>
<li>Back on the previous screen, select <strong>Add secondary appliance</strong>.</li>
<li>From the list, choose your second Cloudflare One Appliance &gt; <strong>Add Appliance</strong>.</li>
<li>Select <strong>Continue</strong> to create a WAN. If you are configuring a static IP, configure the IP for the primary node as the static address, and the IP for the secondary node as the secondary static address.</li>
<li>To create a LAN, follow the steps in <a href="#create-a-lan">Create a LAN</a> up until step 4.</li>
<li>In <strong>Static address</strong>, enter the IP for the primary node in your site. For example, <code>192.168.10.1/24</code>.</li>
<li>In <strong>Secondary static address</strong>, enter the IP for the secondary node in your site. For example, <code>192.168.10.2/24</code>.</li>
<li>In <strong>Virtual static address</strong>, enter the IP that the LAN south of the Cloudflare One Appliance device will forward traffic to. For example, <code>192.168.10.3/24</code>.</li>
<li>Select <strong>Save</strong>.</li>
<li>From the <strong>High availability probing link</strong> drop-down menu, select the port that should be used to monitor the node's health. Cloudflare recommends you choose a reliable interface as the HA probing link. The primary and secondary node's probing link should be connected over a switch, and cannot be a direct connection.</li>
<li>Follow the instructions in <a href="#set-up-your-cloudflare-one-appliance">Set up your Cloudflare One Appliance</a> and <a href="#activate-appliance">Activate appliance</a> to finish setting up your Appliances.</li>
</ol>
<hr />
<h2 id="ipsec-tunnels-and-static-routes">IPsec tunnels and static routes</h2>
<p>Cloudflare One Appliance automatically creates <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/gre-ipsec-tunnels/#ipsec-tunnels">IPsec tunnels</a> and <a href="/cloudflare-one/networks/connectors/cloudflare-wan/reference/traffic-steering/">static routes</a> for you. You cannot configure these manually.</p>
<p>To check the IPsec tunnels and static routes created by your Cloudflare One Appliance:</p>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, and go to <strong>Connectors</strong>.</li>
<li>In <strong>Cloudflare WAN</strong> you can inspect the IPsec tunnels created by your Cloudflare One Appliance.</li>
<li>In <strong>Routes</strong> you can inspect the static routes created by your Cloudflare One Appliance.</li>
</ol>
<hr />
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/network-options/">Network options</a></li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/">Maintenance</a></li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/reference/">Reference information</a></li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/troubleshooting/">Troubleshooting</a></li>
</ul>
