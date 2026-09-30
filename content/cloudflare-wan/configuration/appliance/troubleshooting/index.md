---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/troubleshooting/
  description: Troubleshoot Appliance connectivity and configuration issues.
  full_title: Troubleshooting · Cloudflare WAN docs
  head_html: <title>Troubleshooting · Cloudflare WAN docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot Appliance connectivity and configuration issues."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/troubleshooting/index.md"><meta property="og:title" content="Troubleshooting · Cloudflare WAN docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot Appliance connectivity and configuration issues."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare WAN"><meta name="algolia_product_filter" content="Cloudflare WAN"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Cloudflare WAN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/troubleshooting/#page","headline":"Troubleshooting \u00b7 Cloudflare WAN docs","description":"Troubleshoot Appliance connectivity and configuration issues.","url":"https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-wan/configuration/appliance/troubleshooting/
  schema: 1
---
<h2 id="device-metrics">Device metrics</h2>
<p>Cloudflare customers can inspect metrics for a specific Cloudflare One Appliance (formerly Magic WAN Connector) in the Cloudflare dashboard. These metrics help you troubleshoot potential issues with your device. The information spans categories such as:</p>
<ul>
<li>Performance analytics</li>
<li>Port analytics</li>
<li>Event logs</li>
<li>DHCP leasing information</li>
</ul>
<p>To find the information above and start troubleshooting your Cloudflare One Appliance:</p>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to the <strong>Appliances</strong> tab &gt; <strong>Appliances</strong>, and select the Cloudflare One Appliance you want to check analytics for.</li>
<li>Select <strong>View analytics</strong>.</li>
</ol>
<h3 id="performance-analytics">Performance analytics</h3>
<p>In Performance analytics you can review your Cloudflare One Appliance's performance over time including:</p>
<ul>
<li>Kernel boot time (how long it has been running and if it is activated or not)</li>
<li>Last device snapshot (this also shows the frequency with which your device captures the snapshots that are used in several troubleshooting procedures)</li>
<li>CPU temperature</li>
<li>CPU load over time</li>
<li>Used RAM over time</li>
</ul>
<p>To access performance analytics:</p>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to the <strong>Appliances</strong> tab &gt; <strong>Appliances</strong>, and select the Cloudflare One Appliance you want to check analytics for.</li>
<li>Select <strong>View analytics</strong>.</li>
<li>Select <strong>Performance analytics</strong>.</li>
</ol>
<h3 id="port-analytics">Port analytics</h3>
<p>Port analytics gives you access to information related to the packets sent and received through the ports in your Cloudflare One Appliance. You can adjust the time range for the information displayed in the dashboard regarding to:</p>
<ul>
<li>Rate for packets sent and received</li>
<li>Rate for data sent and received</li>
</ul>
<p>The dashboard provides this information for all active ports in your Cloudflare One Appliance. To access port analytics:</p>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to the <strong>Appliances</strong> tab &gt; <strong>Appliances</strong>, and select the Cloudflare One Appliance you want to check analytics for.</li>
<li>Select <strong>View analytics</strong>.</li>
<li>Select <strong>Port analytics</strong>.</li>
</ol>
<h3 id="event-logs">Event logs</h3>
<p>Use Event logs to identify general patterns and changes over time. This is useful to find correlations with other data and gather deeper insights into your Cloudflare One Appliance. The following event logs are available:</p>
<ul>
<li><code>Init</code>: Initialized <code>mcon-agent</code> process. This process manages the Appliance.</li>
<li><code>Leave</code>: Stopped <code>mcon-agent</code> process.</li>
<li><code>StartAttestation</code>: Started attestation to verify the integrity of the Appliance before allowing the device to connect to your account.</li>
<li><code>FinishAttestationSuccess</code>: Finished attestation successfully.</li>
<li><code>FinishAttestationFailure</code>: Failed attestation.</li>
<li><code>StartRotateCryptKey</code>: Started cryptography key rotation.</li>
<li><code>FinishRotateCryptKeySuccess</code>: Finished cryptography key rotation.</li>
<li><code>FinishRotateCryptKeyFailure</code>: Failed cryptography key rotation.</li>
<li><code>StartRotatePki</code>: Started public key infrastructure (PKI) rotation.</li>
<li><code>FinishRotatePkiSuccess</code>: Finished PKI rotation.</li>
<li><code>FinishRotatePkiFailure</code>: Failed PKI rotation.</li>
<li><code>StartUpgrade</code>: Began Appliance's operating system upgrade.</li>
<li><code>FinishUpgradeSuccess</code>: Finished operating system upgrade.</li>
<li><code>FinishUpgradeFailure</code>: Failed operating system upgrade.</li>
<li><code>Reconcile</code>: Cloudflare is comparing the system's current state against its desired state.</li>
<li><code>ConfigureCloudflaredTunnel</code>: Configured Cloudflare Tunnel to debug device.</li>
</ul>
<p>To access event logs:</p>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to the <strong>Appliances</strong> tab &gt; <strong>Appliances</strong>, and select the Cloudflare One Appliance you want to check analytics for.</li>
<li>Select <strong>View analytics</strong>.</li>
<li>Select <strong>Events</strong>.</li>
<li>You can filter results by specific events, and by time.</li>
</ol>
<h3 id="dhcp-leasing">DHCP leasing</h3>
<p>The DHCP leasing section identifies DHCP assigned leases and their expiration dates. To access DHCP leasing:</p>
<ol>
<li>Go to the <strong>Connectors</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to the <strong>Appliances</strong> tab &gt; <strong>Appliances</strong>, and select the Cloudflare One Appliance you want to check analytics for.</li>
<li>Select <strong>View analytics</strong>.</li>
<li>Select <strong>DHCP leasing</strong>.</li>
</ol>
<h2 id="troubleshooting-tips">Troubleshooting tips</h2>
<p>If you are experiencing difficulties with your Cloudflare One Appliance, refer to the following tips to troubleshoot what might be happening.</p>
<h2 id="i-have-set-up-a-site-but-my-cloudflare-one-appliance-is-not-working">I have set up a site, but my Cloudflare One Appliance is not working</h2>
<p>Make sure that you have <a href="/cloudflare-wan/configuration/appliance/configure-hardware-appliance/#activate-appliance">activated your Cloudflare One Appliance</a>. Cloudflare ships the Cloudflare One Appliance deactivated, and the it will only establish a connection to the Cloudflare network when it is activated.</p>
<h2 id="i-have-tried-to-activate-cloudflare-one-appliance-but-it-is-still-not-working">I have tried to activate Cloudflare One Appliance, but it is still not working</h2>
<p>Check if your Cloudflare One Appliance is connected to the Internet via a port that can serve DHCP. This is required the first time a Cloudflare One Appliance boots up so that it can reach the Cloudflare global network and download the required configurations that you set up in the Site configuration step. For details, refer to <a href="/cloudflare-wan/configuration/appliance/configure-hardware-appliance/#activate-appliance">Activate Appliance</a>.</p>
<p>If you have a firewall deployed upstream of the Cloudflare One Appliance, <a href="/cloudflare-wan/configuration/appliance/configure-hardware-appliance/#firewall-settings-required">check your firewall settings</a>. You might need to configure your firewall to allow traffic in specific ports for the Cloudflare One Appliance to work properly.</p>
<h2 id="i-can-access-cloudflare-one-appliance-s-health-checks-but-there-is-no-traffic">I can access Cloudflare One Appliance's health checks, but there is no traffic</h2>
<p>If you have a firewall deployed upstream of the Cloudflare One Appliance, make sure you review your <a href="/cloudflare-wan/configuration/appliance/configure-hardware-appliance/#firewall-settings-required">firewall settings</a>. You might need to configure your firewall to allow traffic in specific ports for the Cloudflare One Appliance to work properly.</p>
<h2 id="devices-i-have-behind-cloudflare-one-appliance-cannot-connect-to-the-internet">Devices I have behind Cloudflare One Appliance cannot connect to the Internet</h2>
<p>If you have other routing appliances behind Cloudflare One Appliance, make sure you create policy-based routing policies to send traffic from your devices through Cloudflare One Appliance, instead of these other routing devices.</p>
<h2 id="how-do-i-know-if-my-device-is-contacting-cloudflare">How do I know if my device is contacting Cloudflare?</h2>
<p>Cloudflare One Appliance sends a heartbeat periodically to Cloudflare. You can <a href="/cloudflare-wan/configuration/appliance/maintenance/heartbeat/">access the dashboard</a>, and check for the heartbeat status of your Appliance device.</p>
<h2 id="what-do-i-do-in-the-event-of-hardware-issues-with-cloudflare-one-appliance">What do I do in the event of hardware issues with Cloudflare One Appliance?</h2>
<p>Cloudflare is the single point of contact for any issues related to Cloudflare One Appliance, including issues with hardware. When required, Cloudflare Support will work with our partner, TD Synnex, to resolve any issues with the physical device.</p>
