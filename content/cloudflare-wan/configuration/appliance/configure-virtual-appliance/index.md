---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/
  description: Learn how to configure Cloudflare One Virtual Appliance on VMware ESXi or Proxmox Virtual Environment
  full_title: Configure Virtual Appliance · Cloudflare WAN docs
  head_html: <title>Configure Virtual Appliance · Cloudflare WAN docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to configure Cloudflare One Virtual Appliance on VMware ESXi or Proxmox Virtual Environment"><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/index.md"><meta property="og:title" content="Configure Virtual Appliance · Cloudflare WAN docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to configure Cloudflare One Virtual Appliance on VMware ESXi or Proxmox Virtual Environment"><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare WAN"><meta name="algolia_product_filter" content="Cloudflare WAN"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare WAN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/#page","headline":"Configure Virtual Appliance \u00b7 Cloudflare WAN docs","description":"Learn how to configure Cloudflare One Virtual Appliance on VMware ESXi or Proxmox Virtual Environment","url":"https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/configure-virtual-appliance/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-wan/configuration/appliance/configure-virtual-appliance/
  schema: 1
---
<h2 id="register-a-virtual-appliance-and-generate-a-license-key">Register a virtual appliance and generate a license key</h2>
<p>You can register a Cloudflare One Virtual Appliance instance and generate its license key yourself, from either the dashboard or the API — no account team involvement required. Each create or rotate request returns a license key that you use to activate the deployed VM.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6957.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6962.md")
</div></div>
<p>Cloudflare One Virtual Appliance is a virtual device alternative to the hardware based Cloudflare One Appliance. These two versions of Cloudflare One Appliance are identical otherwise.</p>
<p>Currently, you can set up Cloudflare One Virtual Appliance on VMware ESXi and Proxmox Virtual Environment. Support for Proxmox is in beta.</p>
<p>In this page you will find instructions on how to configure Cloudflare One Appliance. This guide provides a step-by-step guide for Cloudflare One Appliance initial setup. You can either return here after setting up your Cloudflare One Appliance, or refer to the <a href="/cloudflare-wan/configuration/appliance/maintenance/">Maintenance</a> section where you will find instructions on how to update your settings.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you can install Cloudflare One Virtual Appliance, you need an Enterprise account with Cloudflare WAN. Additionally, you need to have a VMware or Proxmox host with sufficient compute, memory, and storage to run the virtual machine with Cloudflare One Virtual Appliance. This includes:</p>
<ul>
<li>Intel x86 CPU architecture</li>
<li>ESXi hypervisor 7.0U1 or higher</li>
<li>4 virtual CPUs per virtual appliance (We recommend deployment with a 1:1 virtual CPU to physical core allocation to avoid CPU over contention which will cause packet loss.)</li>
<li>8 GB of RAM per virtual appliance</li>
<li>8 GB of disk per virtual appliance</li>
<li>One vSwitch port group or VLAN with access to the Internet (for example, through a WAN)</li>
<li>One or more vSwitch port group or VLAN that will be the internal LAN</li>
</ul>
<p>For details on installing ESXi and configuring a virtual machine, refer to <a href="https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.esxi.install.doc/GUID-B2F01BF5-078A-4C7E-B505-5DFFED0B8C38.html">VMware's documentation</a>.</p>
<p>For details on installing Virtual environment and configuring a virtual machine, refer to <a href="https://www.proxmox.com/en/products/proxmox-virtual-environment/get-started">Proxmox documentation</a>.</p>
<hr />
<h2 id="before-you-begin">Before you begin</h2>
<p>There are a couple of decisions you need to make when installing your Cloudflare One Virtual Appliance. Review the following topics for more information.</p>
<h3 id="determine-the-need-for-a-high-availability-configuration">Determine the need for a high availability configuration</h3>
<p>You can install up to two instances of Cloudflare One Virtual Appliance for redundancy at each of your sites. If one of your devices fails, traffic will fail over to the other, ensuring that you never lose connectivity to that site.</p>
<p>In this type of high availability (HA) configuration, you will choose a reliable LAN interface as the HA link which will be used to monitor the health of the peer connector. HA links can be dedicated links or can be shared with other LAN traffic.</p>
<p>You must decide the type of configuration you want for your site from the beginning: no redundancy or with redundancy. You cannot add redundancy after finishing the configuration of your dashboard settings. If, at a later stage, you decide to enable redundancy, you will need to delete your Cloudflare One Virtual Appliance device in the Cloudflare dashboard, and start again.</p>
<div class="nb-card"><h3 class="nb-component-title" id="do-you-need-a-high-availability-configuration">Do you need a high availability configuration?</h3>
@markup("md", "content/.markup/bodies/6963.md")
</div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6956.md")
</aside>
<h3 id="decide-on-dhcp-vs-static-ip-connections">Decide on DHCP vs static IP connections</h3>
<p>Cloudflare One Virtual Appliance uses a DHCP connection at first boot to download your settings and go through the activation process. However, if you need to use a static IP in your Cloudflare One Virtual Appliance, and this is a fresh install:</p>
<ol>
<li>Connect the machine with your Cloudflare One Virtual Appliance VM to a DHCP port with access to the Internet.</li>
<li>Follow the <a href="#set-up-cloudflare-dashboard">setup flow</a> and activate your Cloudflare One Virtual Appliance device.</li>
<li>Refer to <a href="#wan-with-a-static-ip-address">WAN with a static IP address</a>.</li>
</ol>
<hr />
<h2 id="configure-a-virtual-machine">Configure a virtual machine</h2>
<p>Select the appropriate tab to configure Cloudflare One Virtual Appliance on VMware ESXi or Proxmox Virtual Environment.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6967.md")
</div></div>
<hr />
<h2 id="set-up-cloudflare-dashboard">Set up Cloudflare dashboard</h2>
<h3 id="create-a-new-profile">Create a new profile</h3>
<p>You need to create a profile for your appliance before connecting it to the Internet.</p>
<p>To create a profile:</p>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to the <strong>Appliances</strong> tab &gt; <strong>Profiles</strong> &gt; <strong>Create a new profile</strong>.</li>
<li>In <strong>Name</strong>, enter a descriptive name for your Cloudflare One Virtual Appliance. Optionally, you can also add a description for it.</li>
<li>You need to decide if you want to turn on high availability for the Cloudflare One Virtual Appliance. For details, refer to <a href="#about-high-availability-configurations">About high availability configurations</a>.</li>
<li>Select <strong>Create and continue</strong>.</li>
<li>Select <strong>Add Appliance</strong>. This will display a list of devices associated with your account. For a Virtual Appliance to appear you need to: <br /><ul><li><strong>VMware:</strong> Have already obtained your OVA package and license keys if you are installing on VMware.</li><li><strong>Proxmox:</strong> Have already obtained your Virtual Appliance Script and license keys if you are installing on Proxmox.</li></ul> For details, refer to <a href="#configure-a-virtual-machine">Configure a virtual machine</a> and select the appropriate tab.</li>
<li>If you have more than one Cloudflare One Virtual Appliance, choose the one that corresponds to the on-ramp you are creating. Cloudflare One Virtual Appliance devices are identified by a serial number, also known as a service tag. Use this information to choose the right Cloudflare One Virtual Appliance. <br /> Select <strong>Add Appliance</strong> when you are ready to proceed.</li>
<li>Cloudflare One Virtual Appliance will be added to your account with an <strong>Interrupt window</strong> defined. The interrupt window is the time period when the Cloudflare One Virtual Appliance software can update, which may result in interruption to existing connections. You can change this later. Refer to <a href="/cloudflare-wan/configuration/appliance/maintenance/interrupt-service-window/">Interrupt window</a> for more details on how to define when the Cloudflare One Virtual Appliance can update its systems.</li>
<li>Select <strong>Continue</strong> to proceed to creating your WAN and LAN networks.</li>
</ol>
<h3 id="create-a-wan">Create a WAN</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6972.md")
</div></div>
<h3 id="create-a-lan">Create a LAN</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6976.md")
</div></div>
<h4 id="network-segmentation">Network segmentation</h4>
<p>After setting up your LANs, you can configure your Cloudflare One Virtual Appliance to enable communication between them without traffic leaving your premises. For details, refer to <a href="/cloudflare-wan/configuration/appliance/network-options/network-segmentation/">Network segmentation</a>.</p>
<h4 id="dhcp-options">DHCP options</h4>
<p>Cloudflare One Virtual Appliance supports different types of DHCP configurations. Cloudflare One Virtual Appliance can:</p>
<ul>
<li>Connect to a DHCP server or use a static IP address instead of connecting to a DHCP server.</li>
<li>Act as a <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-server/">DHCP server</a>.</li>
<li>Use <a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-relay/">DHCP relay</a> to connect to a DHCP server outside the location your Cloudflare One Virtual Appliance is in.</li>
<li><a href="/cloudflare-wan/configuration/appliance/network-options/dhcp/dhcp-static-address-reservation/">Reserve IP addresses</a> for specific devices on your network.</li>
</ul>
<h3 id="add-your-cloudflare-one-virtual-appliance-to-a-site">Add your Cloudflare One Virtual Appliance to a site</h3>
<p>After finishing your Cloudflare One Virtual Appliance configuration, you need to add it to a site. Sites represent the local network of a data center, office, or other physical location, and combine all on-ramps available there. Sites also allow you to check, at a glance, the state of your on-ramps and set up health alert settings so that Cloudflare notifies you when there are issues with the site's on-ramps.</p>
<p>Refer to <a href="/cloudflare-wan/configuration/common-settings/sites/">Set up a site</a> for more information.</p>
<h2 id="activate-appliance">Activate appliance</h2>
<p>Cloudflare One Virtual Appliance is deactivated after you install it, and will only establish a connection to the Cloudflare network when it is activated. Cloudflare recommends leaving it deactivated until you finish <a href="#set-up-cloudflare-dashboard">setting it up in the dashboard</a>.</p>
<p>When the Cloudflare One Virtual Appliance is first activated, one of the ports must be connected to the Internet through a device that supports DHCP. This is required so that the Cloudflare One Virtual Appliance can reach the Cloudflare global network and download the required configurations that you <a href="#set-up-cloudflare-dashboard">set up</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6977.md")
</aside>
<p>When you are ready to connect your Cloudflare One Virtual Appliance to the Cloudflare network:</p>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to the <strong>Appliances</strong> tab &gt; <strong>Appliances</strong>.</li>
<li>Find the Cloudflare One Virtual Appliance you want to activate, select the three dots next to it &gt; <strong>Edit</strong>. Make sure you verify the serial number to choose the right Cloudflare One Virtual Appliance you want to activate.</li>
<li>In the new window, the <strong>Status</strong> dropdown will show as <strong>Deactivated</strong>. Select it to change the status to <strong>Activated</strong>.</li>
<li>The <strong>Interrupt window</strong> is the time period when the Cloudflare One Virtual Appliance software can update, which may result in interruption to existing connections. Choose a time period to minimize disruption to your sites. For details on defining when the Cloudflare One Virtual Appliance can update its systems, refer to <a href="/cloudflare-wan/configuration/appliance/maintenance/interrupt-service-window/">Interrupt window</a>.</li>
<li>Select <strong>Update</strong>.</li>
</ol>
<h2 id="boot-your-virtual-appliance">Boot your Virtual Appliance</h2>
<h3 id="default-password-to-access-virtual-appliance">Default password to access Virtual Appliance</h3>
<p>Your Virtual Appliance's default password is the last seven characters of your license key, all uppercase, plus an <code>!</code> (exclamation mark).</p>
<p>For example, if your license key is <code>mconn-abcdefghijklmnopqrstuvwxyz</code>, your default password will be <code>TUVWXYZ!</code>.</p>
<hr />
<h2 id="wan-with-a-static-ip-address">WAN with a static IP address</h2>
<p>After activating your device, you can use it in a network configuration with the WAN interface set to a static IP address - that is, an Internet configuration that is not automatically set by DHCP. To use your Cloudflare One Virtual Appliance on a network configuration with a static IP, follow these steps:</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/6978.md")
</aside>
<ol>
<li>Connect the machine where you installed the VM with Cloudflare One Virtual Appliance to a DHCP port with access to the Internet.</li>
<li><a href="#create-a-new-profile">Create a new profile</a> in the dashboard.</li>
<li>Create a <a href="#create-a-wan">DHCP WAN</a>.</li>
<li><a href="#activate-appliance">Activate</a> and boot your Cloudflare One Virtual Appliance.</li>
<li>Wait 60 seconds.</li>
<li>Make changes to the <a href="#create-a-wan">WAN settings</a> in the dashboard to a static IP set up.</li>
<li>Wait 60 seconds again.</li>
<li>Modify your <a href="#configure-a-virtual-machine">Port Groups</a> as needed to change the source from which the WAN port obtains its IP address.</li>
<li>Reboot your virtual machine.</li>
</ol>
<hr />
<h2 id="about-high-availability-configurations">About high availability configurations</h2>
<p>You need to install two Virtual Appliances before you can set up a site in high availability. When you set up a site in high availability, the WANs and LANs in your Cloudflare One Virtual Appliance have the same configuration but are replicated on two nodes. In case of failure of one of the devices, the other device becomes the active node, taking over the configuration of the LAN gateway IP and allowing traffic to continue without disruption.</p>
<p>Because Cloudflare One Virtual Appliances in high availability configurations share a single site, you need to set up:</p>
<ul>
<li><strong>Static address</strong>: The IP for the primary node in your site.</li>
<li><strong>Secondary static address</strong>: The IP for the secondary node in your site.</li>
<li><strong>Virtual static address</strong>: The IP that the LAN south of the Cloudflare One Virtual Appliance device will forward traffic to, which is the LAN's gateway IP.</li>
</ul>
<p>Make sure all IPs are part of the same subnet.</p>
<p>For detailed information about the expected behavior of high availability configurations, refer to the <a href="/cloudflare-wan/configuration/appliance/reference/#high-availability-configurations">High availability configurations</a> reference page.</p>
<h3 id="create-a-high-availability-configuration">Create a high availability configuration</h3>
<p>You cannot enable high availability for an existing site. To add high availability to an existing site in the Cloudflare dashboard, you need to delete the site and start again.</p>
<p>To set up a high availability configuration:</p>
<ol>
<li>Follow the steps in <a href="#create-a-new-profile">Create a new profile</a> up until step 4.</li>
<li>After naming your site, select <strong>Turn on high availability</strong>.</li>
<li>Select <strong>Create and continue</strong>.</li>
<li>Select <strong>Add Appliance</strong>.</li>
<li>From the list, choose your first Cloudflare One Virtual Appliance &gt; <strong>Add Appliance</strong>.</li>
<li>Back on the previous screen, select <strong>Add secondary appliance</strong>.</li>
<li>From the list, choose your second Cloudflare One Virtual Appliance &gt; <strong>Add Appliance</strong>.</li>
<li>Select <strong>Continue</strong> to create a WAN. If you are configuring a static IP, configure the IP for the primary node as the static address, and the IP for the secondary node as the secondary static address.</li>
<li>To create a LAN, follow the steps in <a href="#create-a-lan">Create a LAN</a> up until step 4.</li>
<li>In <strong>Static address</strong>, enter the IP for the primary node in your site. For example, <code>192.168.10.1/24</code>.</li>
<li>In <strong>Secondary static address</strong>, enter the IP for the secondary node in your site. For example, <code>192.168.10.2/24</code>.</li>
<li>In <strong>Virtual static address</strong>, enter the IP that the LAN south of the Cloudflare One Virtual Appliance device will forward traffic to. For example, <code>192.168.10.3/24</code>.</li>
<li>Select <strong>Save</strong>.</li>
<li>From the <strong>High availability probing link</strong> drop-down menu, select the port that should be used to monitor the node's health. Cloudflare recommends you choose a reliable interface as the HA probing link. The primary and secondary node's probing link should be connected over a switch, and cannot be a direct connection.</li>
<li>Follow the instructions in <a href="#activate-appliance">Activate appliance</a> to finish setting up your Appliances.</li>
</ol>
<hr />
<h2 id="ipsec-tunnels-and-static-routes">IPsec tunnels and static routes</h2>
<p>Cloudflare One Virtual Appliance automatically creates <a href="/cloudflare-wan/reference/gre-ipsec-tunnels/#ipsec-tunnels">IPsec tunnels</a> and <a href="/cloudflare-wan/reference/traffic-steering/">static routes</a> for you. You cannot configure these manually.</p>
<p>To check the IPsec tunnels and static routes created by your Cloudflare One Virtual Appliance:</p>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>The <strong>IPsec/GRE tunnels</strong> tab shows a list of all the IPsec tunnels created by your Cloudflare One Virtual Appliance.</li>
<li>Go to the <strong>Routes</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="4">
<li>Here you can inspect the static routes created by your Cloudflare One Virtual Appliance.</li>
</ol>
<hr />
<h2 id="next-steps">Next steps</h2>
<ul>
<li><a href="/cloudflare-wan/configuration/appliance/network-options/">Network options</a></li>
<li><a href="/cloudflare-wan/configuration/appliance/maintenance/">Maintenance</a></li>
<li><a href="/cloudflare-wan/configuration/appliance/reference/">Reference information</a></li>
<li><a href="/cloudflare-wan/configuration/appliance/troubleshooting/">Troubleshooting</a></li>
</ul>
