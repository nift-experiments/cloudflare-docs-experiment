---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/fleet/
  description: Fleet in Zero Trust.
  full_title: Fleet · Cloudflare One docs
  head_html: <title>Fleet · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Fleet in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/fleet/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/fleet/index.md"><meta property="og:title" content="Fleet · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Fleet in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/fleet/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/fleet/#page","headline":"Fleet \u00b7 Cloudflare One docs","description":"Fleet in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/fleet/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/partners/fleet/
  schema: 1
---
<p>This guide covers how to deploy the Cloudflare One Client (formerly WARP) using <a href="https://fleetdm.com/">Fleet</a> device management software.</p>
<h2 id="macos">macOS</h2>
<h3 id="1-create-a-custom-mdm-file"><ol>
<li>Create a custom MDM file</li>
</ol></h3>
<ol>
<li><a href="/cloudflare-one/static/mdm/CloudflareWARP.mobileconfig">Download</a> an example <code>.mobileconfig</code> file.</li>
<li>Modify the file with your desired <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/">deployment parameters</a>.</li>
</ol>
<h3 id="2-upload-mdm-file-to-fleet"><ol start="2">
<li>Upload MDM file to Fleet</li>
</ol></h3>
<ol>
<li>In the Fleet admin console, go to <strong>Controls</strong>.</li>
<li>From the <strong>Teams</strong> dropdown, select the team (group of hosts) that requires the Cloudflare One Client.</li>
<li>Select <strong>OS settings</strong> &gt; <strong>Custom settings</strong>.</li>
<li>Select <strong>Add profile</strong> and upload the custom <code>.mobileconfig</code>.</li>
<li>Select the hosts which require the Cloudflare One Client:
<ul>
<li><strong>All hosts</strong>: Deploys the Cloudflare One Client to all hosts in the team.</li>
<li><strong>Custom</strong>: Deploys the Cloudflare One Client to a subset of the hosts in the team. Use <a href="https://fleetdm.com/guides/managing-labels-in-fleet#basic-article">labels</a> to define the hosts that should be included or excluded.</li>
</ul>
</li>
<li>Select <strong>Add profile</strong>.</li>
</ol>
<p>The defined hosts will immediately receive the deployment profile, but the Cloudflare One Client is not yet installed.</p>
<h3 id="3-download-cloudflare-one-client-package-for-macos"><ol start="3">
<li>Download Cloudflare One Client package for macOS</li>
</ol></h3>
<p>Visit the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/#macos">Download page</a> to review system requirements and download the installer for your operating system.</p>
<h3 id="4-upload-cloudflare-one-client-package-to-fleet"><ol start="4">
<li>Upload Cloudflare One Client package to Fleet</li>
</ol></h3>
<p>To add the Cloudflare One Client installer package for distribution to your hosts enrolled in Fleet:</p>
<ol>
<li>In the Fleet admin console, go to <strong>Software</strong>.</li>
<li>From the <strong>Teams</strong> dropdown, select the team (group of hosts) that requires the Cloudflare One Client.</li>
<li>Select <strong>Add Software</strong> and upload the <code>.pkg</code> file that was previously downloaded.</li>
</ol>
<h3 id="5-install-the-cloudflare-one-client-with-fleet"><ol start="5">
<li>Install the Cloudflare One Client with Fleet</li>
</ol></h3>
<p>To deploy the uploaded <code>.pkg</code> file to your hosts:</p>
<ol>
<li>In the Fleet admin console, go to <strong>Hosts</strong>.</li>
<li>Select the host that requires the Cloudflare One Client.</li>
<li>Go to <strong>Software</strong> and search for <code>Cloudflare</code>.</li>
<li>Select <strong>Actions</strong> &gt; <strong>Install</strong>.</li>
</ol>
<p>Installation will happen automatically when the host comes online. To deploy with REST API or GitOps, refer to the <a href="https://fleetdm.com/guides/deploy-software-packages">Fleet documentation</a>.
After deploying the Cloudflare One Client, you can check its connection progress using the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/">Connectivity status</a> messages displayed in the Cloudflare One Client GUI.</p>
<h3 id="6-uninstall-the-cloudflare-one-client-with-fleet"><ol start="6">
<li>Uninstall the Cloudflare One Client with Fleet</li>
</ol></h3>
<p>To uninstall the Fleet-deployed Cloudflare One Client:</p>
<ol>
<li>In the Fleet admin console, go to <strong>Hosts</strong>.</li>
<li>Select the host that requires the Cloudflare One Client to be uninstalled.</li>
<li>Go to <strong>Software</strong> and search for <code>Cloudflare</code>.</li>
<li>Select <strong>Actions</strong> &gt; <strong>Uninstall</strong>.</li>
</ol>
<h2 id="windows">Windows</h2>
<h3 id="1-download-cloudflare-one-client-package-for-windows"><ol>
<li>Download Cloudflare One Client package for Windows</li>
</ol></h3>
<p>Visit the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/#windows">Download page</a> to review system requirements and download the installer for your operating system.</p>
<h3 id="2-upload-cloudflare-one-client-package-to-fleet"><ol start="2">
<li>Upload Cloudflare One Client package to Fleet</li>
</ol></h3>
<p>To add the Cloudflare One Client installer package for distribution to your hosts enrolled in Fleet:</p>
<ol>
<li>In the Fleet admin console, go to <strong>Software</strong>.</li>
<li>From the <strong>Teams</strong> dropdown, select the team (group of hosts) that requires the Cloudflare One Client.</li>
<li>Select <strong>Add Software</strong> and upload the <code>.msi</code> file that was previously downloaded.</li>
<li>(Optional) To allow users to install the Cloudflare One Client from Fleet Desktop, select <strong>Self-service</strong>.</li>
<li>Select <strong>Advanced options</strong>.</li>
<li>In <strong>Install script</strong>, replace the default script with the following:</li>
</ol>
<pre tabindex="0"><code class="language-bash">$logFile = &quot;${env:TEMP}/fleet-install-software.log&quot;&#10;&#10;try {&#10;&#10;$installProcess = Start-Process msiexec.exe `&#10;  &#45;ArgumentList &quot;/quiet /norestart ORGANIZATION=your-team-name SUPPORT_URL=https://example.com /lv ${logFile} /i `&quot;${env:INSTALLER_PATH}`&quot;&quot; `&#10;  &#45;PassThru -Verb RunAs -Wait&#10;&#10;Get-Content $logFile -Tail 500&#10;&#10;Exit $installProcess.ExitCode&#10;&#10;} catch {&#10;  Write-Host &quot;Error: $_&quot;&#10;  Exit 1&#10;}&#10;</code></pre>
<p>Refer to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/">deployment parameters</a> for a description of each argument.</p>
<h3 id="3-install-the-cloudflare-one-client-with-fleet"><ol start="3">
<li>Install the Cloudflare One Client with Fleet</li>
</ol></h3>
<p>To deploy the uploaded <code>.pkg</code> file to your hosts:</p>
<ol>
<li>In the Fleet admin console, go to <strong>Hosts</strong>.</li>
<li>Select the host that requires the Cloudflare One Client.</li>
<li>Go to <strong>Software</strong> and search for <code>Cloudflare</code>.</li>
<li>Select <strong>Actions</strong> &gt; <strong>Install</strong>.</li>
</ol>
<p>Installation will happen automatically when the host comes online. To deploy with REST API or GitOps, refer to the <a href="https://fleetdm.com/guides/deploy-software-packages">Fleet documentation</a>.
After deploying the Cloudflare One Client, you can check its connection progress using the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/connectivity-status/">Connectivity status</a> messages displayed in the Cloudflare One Client GUI.</p>
<h3 id="4-uninstall-the-cloudflare-one-client-with-fleet"><ol start="4">
<li>Uninstall the Cloudflare One Client with Fleet</li>
</ol></h3>
<p>To uninstall the Fleet-deployed Cloudflare One Client:</p>
<ol>
<li>In the Fleet admin console, go to <strong>Hosts</strong>.</li>
<li>Select the host that requires the Cloudflare One Client to be uninstalled.</li>
<li>Go to <strong>Software</strong> and search for <code>Cloudflare</code>.</li>
<li>Select <strong>Actions</strong> &gt; <strong>Uninstall</strong>.</li>
</ol>
<h2 id="linux">Linux</h2>
<p>Fleet allows you to <a href="https://fleetdm.com/guides/scripts">execute custom scripts</a> on Linux hosts. The following example script creates an <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/#linux">MDM file</a> and installs the Cloudflare One Client on an Ubuntu 22.04 host:</p>
<pre tabindex="0"><code class="language-sh">&#35;!/bin/sh&#10;&#10;&#35; Write the mdm.xml file&#10;touch /var/lib/cloudflare-warp/mdm.xml&#10;echo -e &quot;&lt;dict&gt;\n   &lt;key&gt;organization&lt;/key&gt;\n   &lt;string&gt;your-team-name&lt;/string&gt;\n&lt;/dict&gt;&#10;&quot; &gt; /var/lib/cloudflare-warp/mdm.xml&#10;&#10;&#35; Add cloudflare gpg key&#10;curl -fsSL https://pkg.cloudflareclient.com/pubkey.gpg | sudo gpg --yes --dearmor --output /usr/share/keyrings/cloudflare-warp-archive-keyring.gpg&#10;&#10;&#35; Add this repo to your apt repositories&#10;echo &quot;deb [signed-by=/usr/share/keyrings/cloudflare-warp-archive-keyring.gpg] https://pkg.cloudflareclient.com/ any main&quot; | sudo tee /etc/apt/sources.list.d/cloudflare-client.list&#10;&#10;&#35; Install&#10;sudo apt-get -y update &amp;&amp; sudo apt-get -y install cloudflare-warp&#10;</code></pre>
<p>To install the Cloudflare One Client on other Linux distributions, refer to the <a href="https://pkg.cloudflareclient.com/">package repository</a>.</p>
