---
cp9:
  canonical: https://developers.cloudflare.com/multi-cloud-networking/cloud-on-ramps/
  description: Connect cloud providers to Cloudflare with cloud on-ramps.
  full_title: Cloud on-ramps · Cloudflare Multi-Cloud Networking docs
  head_html: <title>Cloud on-ramps · Cloudflare Multi-Cloud Networking docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect cloud providers to Cloudflare with cloud on-ramps."><link rel="canonical" href="https://developers.cloudflare.com/multi-cloud-networking/cloud-on-ramps/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/multi-cloud-networking/cloud-on-ramps/index.md"><meta property="og:title" content="Cloud on-ramps · Cloudflare Multi-Cloud Networking docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect cloud providers to Cloudflare with cloud on-ramps."><meta property="og:url" content="https://developers.cloudflare.com/multi-cloud-networking/cloud-on-ramps/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Multi-Cloud Networking"><meta name="algolia_product_filter" content="Multi-Cloud Networking"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Multi-Cloud Networking"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/multi-cloud-networking/cloud-on-ramps/#page","headline":"Cloud on-ramps \u00b7 Cloudflare Multi-Cloud Networking docs","description":"Connect cloud providers to Cloudflare with cloud on-ramps.","url":"https://developers.cloudflare.com/multi-cloud-networking/cloud-on-ramps/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /multi-cloud-networking/cloud-on-ramps/
  schema: 1
---
<p>Multi-Cloud Networking (formerly Magic Cloud Networking) (beta) allows you to create on-ramps from your cloud networks to Cloudflare WAN (formerly Magic WAN). Cloudflare will create virtual private network (VPN) tunnels between Cloudflare WAN and your cloud provider, configuring both sides of the connection on your behalf. Cloudflare orchestrates the cloud provider's native VPN functionality, without requiring deployment of any additional compute virtual machines (VMs).</p>
<p>There are two types of on-ramps: single virtual private cloud (VPC) and hubs.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before creating on-ramps from your cloud networks to Cloudflare WAN, make sure you:</p>
<ul>
<li>Have a Cloudflare WAN account. Contact your account team to learn more.</li>
<li>Went through the process of <a href="/multi-cloud-networking/get-started/">setting up your cloud provider</a>.</li>
<li>Have the correct cloud resources. Refer to <a href="/multi-cloud-networking/reference/">Reference</a> to check resources by cloud provider.</li>
</ul>
<h2 id="available-on-ramps">Available on-ramps</h2>
<p>Multi-Cloud Networking has the following cloud on-ramps integrations:</p>
<ul>
<li>AWS (single VPC and hubs)</li>
<li>Azure (single VPC)</li>
<li>GCP (single VPC)</li>
</ul>
<p>Refer to <a href="/multi-cloud-networking/reference/">Reference</a> to learn more about how Cloudflare orchestrates VPN connectivity to your cloud networks.</p>
<hr />
<h2 id="set-up-on-ramps">Set up on-ramps</h2>
<h3 id="single-virtual-private-cloud">Single virtual private cloud</h3>
<p>Choose this option if you have a single VPC in your cloud to connect to Cloudflare WAN. To set up a single-VPC on-ramp:</p>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Cloud (beta)</strong> tab.</li>
<li>Select <strong>Add new on-ramp</strong>.</li>
<li>Go to <strong>Connect an existing VPC to Cloudflare</strong> &gt; <strong>Select</strong>.</li>
<li>Give your new on-ramp a name and a description (optional), then select <strong>Continue</strong>.</li>
<li>From the drop-down menu, choose your cloud provider. You can choose between AWS, GCP, and Azure. Then, select <strong>Continue</strong>.</li>
<li>Select the network that you want to connect to. This list comes from the <a href="/multi-cloud-networking/get-started/">cloud integrations</a> you have already set up. When you are done, select <strong>Continue</strong>.</li>
<li><strong>Configure route propagation</strong> shows where Cloudflare will install the new routes. Installing these routes is required to correctly configure both Cloudflare WAN and your cloud provider, and ensure successful communication between them:
<ul>
<li><strong>Add routes for your Cloudflare WAN address space to your cloud network</strong>: Select this option to install routes for reaching Cloudflare WAN in your cloud network's route tables (refer to <a href="#cloudflare-wan-address-space">Cloudflare WAN address space</a> to learn what routes are installed and how to customize them). If you prefer to do this manually, unselect this option.</li>
</ul>
</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/741.md")
</aside>
   - **Add routes for your cloud network to Cloudflare WAN**: Select this option to create routes for reaching your cloud network in Cloudflare WAN.
9. Select **Continue**. Applying your settings might take a few seconds to complete.
10. Review the changes in your cloud environment, and select **Approve changes**.
<p>You have successfully created your Cloudflare WAN on-ramp. However, on-ramp creation can take up to an hour before you can use it.</p>
<h3 id="hubs">Hubs</h3>
<p>If you want to connect multiple VPCs to Cloudflare WAN, the best way to connect them is using a hub. A hub is a cloud VPN gateway that peers with multiple VPCs, allowing them to share a VPN tunnel to Cloudflare WAN. Each cloud provider has their own term for hubs, so refer to your cloud provider for more information.</p>
<p>Depending on how you have set up your cloud provider, you can:</p>
<ul>
<li><strong>Connect to an existing hub</strong>: Choose this option if you already have a VPN hub in your cloud and you want to connect it to Cloudflare WAN.</li>
<li><strong>Create a new hub</strong>: Choose this option if you want to create a new hub and connect it to Cloudflare WAN.</li>
</ul>
<p>When you configure a hub on-ramp, Cloudflare always manages the VPN tunnel between Cloudflare WAN and the hub. Optionally, you can also choose to have Cloudflare manage peering with VPCs and/or with other hubs:</p>
<ul>
<li><strong>Manage VPC peering:</strong> If you enable this option, Cloudflare will attach your chosen VPCs to the hub.</li>
<li><strong>Manage hub peering:</strong> Hubs are regional, so in order to connect VPCs attached to hubs in different regions, those hubs need to be peered. If you enable this option, Cloudflare will peer your chosen hubs to this hub.</li>
</ul>
<h4 id="connect-to-an-existing-hub">Connect to an existing hub</h4>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Cloud (beta)</strong> tab.</li>
<li>Select <strong>Add new on-ramp</strong>.</li>
<li>Go to <strong>Connect an existing hub to Cloudflare</strong> &gt; <strong>Select</strong>.</li>
<li>Give your new on-ramp a name and a description (optional), then select <strong>Continue</strong>.</li>
<li>From the drop-down menu, choose your cloud provider. You can choose between AWS, GCP, and Azure. Then, select <strong>Continue</strong>.</li>
<li>Choose an existing hub. This list comes from the <a href="/multi-cloud-networking/get-started/">cloud integrations</a> you have already set up. When you are done, select <strong>Continue</strong>.</li>
<li>(<em>Optional</em>) In <strong>VPC peering configuration</strong>, you can enable <strong>Manage VPC peering</strong>. This allows Cloudflare to attach your chosen VPCs to the hub:
<ol>
<li>Select <strong>Manage VPC peering</strong> to enable this feature.</li>
<li>Choose the VPCs you want Cloudflare to attach to the hub.</li>
</ol>
</li>
<li>Select <strong>Continue</strong>.</li>
<li>(<em>Optional</em>) In <strong>Configure hub peering</strong>, you can enable <strong>Manage hub peering</strong>. Enabling this option allows Cloudflare to attach remote hubs you have chosen to this hub (establishing connectivity between VPCs attached to any of the peered hubs):
<ol>
<li>Select <strong>Manage hub peering</strong> to enable this feature.</li>
<li>Select the remote hubs you want Cloudflare to attach to this hub.</li>
</ol>
</li>
<li>Select <strong>Continue</strong>.</li>
<li><strong>Configure route propagation</strong> shows where Cloudflare will install the new routes. Installing these routes is required to correctly configure both Cloudflare WAN and your cloud provider, and ensure successful communication between them:
<ol>
<li><strong>Add routes for your Cloudflare WAN address space to your cloud network</strong>: Select this option to install routes for reaching Cloudflare WAN in your cloud network's route tables (refer to <a href="#cloudflare-wan-address-space">Cloudflare WAN address space</a> to learn what routes are installed and how to customize them). If you prefer to do this manually, unselect this option.</li>
</ol>
</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning-1">Warning</h3>
@markup("md", "content/.markup/bodies/740.md")
</aside>
    2. **Add routes for your cloud network to Cloudflare WAN**: Select this option to create routes for reaching your cloud network in Cloudflare WAN.
13. Select **Continue**. Applying your settings might take a few seconds to complete.
14. Review the changes in your cloud environment, and select **Approve changes**.
<p>You have successfully created your Cloudflare WAN on-ramp. However, on-ramp creation can take up to an hour before you can use it.</p>
<h4 id="create-a-new-hub">Create a new hub</h4>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Cloud (beta)</strong> tab.</li>
<li>Select <strong>Add new on-ramp</strong>.</li>
<li>Go to <strong>Create a new hub &amp; connect it to Cloudflare</strong> &gt; <strong>Select</strong>.</li>
<li>Give your new on-ramp a name and a description (optional), then select <strong>Continue</strong>.</li>
<li>Configure your cloud in <strong>Select your cloud details</strong>:
<ol>
<li>From the drop-down menu, choose your cloud provider. You can choose between AWS, GCP, and Azure.</li>
<li>Choose an existing integration. This list comes from the <a href="/multi-cloud-networking/get-started/">cloud integrations</a> you have already set up.</li>
<li>Choose a region in which to create the new hub.</li>
<li>Select <strong>Continue</strong>.</li>
</ol>
</li>
<li>(<em>Optional</em>) In <strong>VPC peering configuration</strong>, you can enable <strong>Manage VPC peering</strong>. This allows Cloudflare to attach your chosen VPCs to the hub:
<ol>
<li>Select <strong>Manage VPC peering</strong> to enable this feature.</li>
<li>Choose the VPCs you want Cloudflare to attach to the hub.</li>
</ol>
</li>
<li>Select <strong>Continue</strong>.</li>
<li>(<em>Optional</em>) In <strong>Configure hub peering</strong>, you can enable <strong>Manage hub peering</strong>. Enabling this option allows Cloudflare to attach remote hubs you have chosen to this hub (establishing connectivity between VPCs attached to any of the peered hubs):
<ol>
<li>Select <strong>Manage hub peering</strong> to enable this feature.</li>
<li>Select the remote hubs you want Cloudflare to attach to this hub.</li>
</ol>
</li>
<li>Select <strong>Continue</strong>.</li>
<li><strong>Configure route propagation</strong> shows where Cloudflare will install the new routes. Installing these routes is required to correctly configure both Cloudflare WAN and your cloud provider, and ensure successful communication between them:
<ol>
<li><strong>Add routes for your Cloudflare WAN address space to your cloud network</strong>: Select this option to install routes for reaching Cloudflare WAN in your cloud network's route tables (refer to <a href="#cloudflare-wan-address-space">Cloudflare WAN address space</a> to learn what routes are installed and how to customize them). If you prefer to do this manually, unselect this option.</li>
</ol>
</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning-2">Warning</h3>
@markup("md", "content/.markup/bodies/739.md")
</aside>
    2. **Add routes for your cloud network to Cloudflare WAN**: Select this option to create routes for reaching your cloud network in Cloudflare WAN.
12. Select **Continue**. Applying your settings might take a few seconds to complete.
13. Review the changes in your cloud environment, and select **Approve changes**.
<p>You have successfully created your Cloudflare WAN on-ramp. However, on-ramp creation can take up to an hour before you can use it.</p>
<h3 id="set-up-with-terraform">Set up with Terraform</h3>
<p>You can download a Terraform configuration for a cloud on-ramp.</p>
<p>You might want to do this to:</p>
<ul>
<li>Review the proposed configuration for an on-ramp before deploying it with Cloudflare.</li>
<li>Deploy the on-ramp using your own infrastructure-as-code pipeline instead of deploying it with Cloudflare.</li>
</ul>
<p>The download will contain two files:</p>
<ul>
<li><code>main.tf</code>: Terraform configuration for the new resources needed to create the on-ramp.</li>
<li><code>instructions.txt</code>: Instructions for modifying resources that already exist in your cloud environment.</li>
</ul>
<p>If you intend to plan and apply the downloaded configuration using Terraform, you will need to use the <a href="/terraform/">Cloudflare Terraform provider</a> (in addition to the Terraform provider for the on-ramp's cloud service provider). Use your Cloudflare <a href="/fundamentals/api/get-started/keys/">Global API Key</a>, not an API Token.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/738.md")
</aside>
<h4 id="download-terraform-configuration-for-a-new-on-ramp">Download Terraform configuration for a new on-ramp</h4>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Cloud (beta)</strong> tab.</li>
<li>In <strong>Cloud on-ramps</strong>, select <strong>Add new on-ramp</strong> and begin the <strong>Create a Cloudflare WAN cloud on-ramp</strong> workflow following the standard steps.</li>
<li>After the <strong>Configure route propagation</strong> step, select <strong>View download options</strong> instead of selecting <strong>Continue</strong>.</li>
<li>Select a download option:
<ol>
<li>Choose <strong>Download file and continue</strong> to download the Terraform configuration, review the configuration, and then continue deploying the on-ramp with Cloudflare.</li>
<li>Choose <strong>Download file and exit</strong> to download the Terraform configuration that you will apply yourself.</li>
</ol>
</li>
</ol>
<h4 id="download-terraform-configuration-for-an-existing-on-ramp">Download Terraform configuration for an existing on-ramp</h4>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Cloud (beta)</strong> tab.</li>
<li>In <strong>Cloud on-ramps</strong>, find the on-ramp you want to download &gt; select the three dots &gt; <strong>Download as Terraform</strong>.</li>
</ol>
<h2 id="update-security-groups">Update security groups</h2>
<p>After setting up your on-ramps, you need to update your network security groups in your cloud provider to allow traffic to/from Cloudflare WAN. Refer to the <a href="/multi-cloud-networking/reference/">Cloud on-ramps</a> reference page for more information.</p>
<hr />
<h2 id="edit-on-ramps">Edit on-ramps</h2>
<h3 id="edit-a-cloudflare-wan-cloud-on-ramp">Edit a Cloudflare WAN cloud on-ramp</h3>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Cloud (beta)</strong> tab.</li>
<li>Select the on-ramp you want to edit.</li>
<li>Select <strong>Edit</strong> in the side panel.</li>
<li>In <strong>Basic information</strong>, you can change the name and description of your on-ramp. Select <strong>Save</strong> when you are finished.</li>
<li>In <strong>Configurations</strong>, you can modify where the required routes are installed. Select <strong>Continue</strong>.
<ol>
<li>Select <strong>Save and review</strong> after making changes.</li>
<li>Review your settings, and select <strong>Approve changes</strong>.</li>
</ol>
</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/737.md")
</aside>
<h3 id="delete-a-cloudflare-wan-cloud-on-ramp">Delete a Cloudflare WAN cloud on-ramp</h3>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Cloud (beta)</strong> tab.</li>
<li>Select the on-ramp you want to delete.</li>
<li>Select <strong>Edit</strong> in the side panel.</li>
<li>Choose <strong>Detach</strong> to proceed. Cloudflare will stop managing the cloud resources that were created to build this on-ramp, but will leave them in place. On-ramp connectivity will not be impacted.</li>
</ol>
<hr />
<h2 id="cloudflare-wan-address-space">Cloudflare WAN address space</h2>
<p>By default, Cloudflare installs the following summarized routes in your cloud route tables to direct traffic to Cloudflare WAN:</p>
<pre tabindex="0"><code class="language-txt">10.0.0.0/8&#10;172.16.0.0/12&#10;192.168.0.0/16&#10;100.64.0.0/10&#10;</code></pre>
<p>To override the defaults with custom prefixes:</p>
<ol>
<li>Go to the <strong>Routes</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>WAN configuration</strong>.</li>
<li>Scroll to <strong>Propagated routes to cloud networks</strong>.</li>
<li>Delete the prefixes, and enter your custom ones.</li>
<li>When you are finished, select <strong>Save changes</strong>.</li>
</ol>
<p>To install a default route to send all traffic to Cloudflare WAN, enter <code>0.0.0.0/0</code> (on Azure, enter <code>0.0.0.0/1</code> and <code>128.0.0.0/1</code>).</p>
<hr />
<h2 id="cost-estimates">Cost estimates</h2>
<p>You can view estimated costs associated with your cloud resources in the Cloudflare dashboard.</p>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the <strong>Cloud (beta)</strong> tab.</li>
<li>In <strong>Cloud on-ramps</strong>, find the cloud on-ramp for which you want to check the estimated costs &gt; select the three dots &gt; <strong>Associated Resources</strong>.</li>
<li>In the <strong>Associated Resources</strong> page, you can view the estimated monthly costs for all the resources associated with the on-ramp you chose. You can also search for a specific resource using the search box.</li>
</ol>
