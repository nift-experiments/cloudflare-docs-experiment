---
cp9:
  canonical: https://developers.cloudflare.com/network-interconnect/monitoring-and-alerts/
  description: Monitor CNI status and configure maintenance alerts
  full_title: Monitoring and alerts · Cloudflare Network Interconnect docs
  head_html: <title>Monitoring and alerts · Cloudflare Network Interconnect docs</title><meta name="generator" content="Nift"><meta name="description" content="Monitor CNI status and configure maintenance alerts"><link rel="canonical" href="https://developers.cloudflare.com/network-interconnect/monitoring-and-alerts/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/network-interconnect/monitoring-and-alerts/index.md"><meta property="og:title" content="Monitoring and alerts · Cloudflare Network Interconnect docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Monitor CNI status and configure maintenance alerts"><meta property="og:url" content="https://developers.cloudflare.com/network-interconnect/monitoring-and-alerts/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Network Interconnect"><meta name="algolia_product_filter" content="Network Interconnect"><meta name="pcx_content_group" content="Network security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Network Interconnect"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/network-interconnect/monitoring-and-alerts/#page","headline":"Monitoring and alerts \u00b7 Cloudflare Network Interconnect docs","description":"Monitor CNI status and configure maintenance alerts","url":"https://developers.cloudflare.com/network-interconnect/monitoring-and-alerts/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /network-interconnect/monitoring-and-alerts/
  schema: 1
---
<h2 id="monitoring">Monitoring</h2>
<p>The Cloudflare dashboard shows a list of all previously created interconnects, as well as useful information such as IP addresses, speed, type of interconnect, and status. In the Cloudflare dashboard, go to <strong>Interconnects</strong>.</p>
<div class="nb-dash-button"></div>
<p>The Status column displays three statuses:</p>
<ul>
<li><strong>Active</strong>: The interconnect port on the Customer Connectivity Router (CCR) is operationally up. This means that the CCR port sees sufficient light levels and has negotiated an Ethernet link.</li>
<li><strong>Unhealthy</strong>: The link operational state at interconnect port is down. This might mean the CCR does not see light, cannot negotiate an Ethernet signal, or the light levels are below -20 dBm. You can take general troubleshooting steps to solve the issue (such as checking cables and status lights for connectivity issues). If you are unable to solve the issue in this way, contact your account team.</li>
<li><strong>Pending</strong>: The link is not yet active. This is expected and can occur for several reasons: the customer has not received a cross-connect, the device is unresponsive, or physical adjustments may be required, such as swapping RX/TX fibers. The <strong>Pending</strong> status will disappear after the customer completes the cross-connect and status moves to <strong>Active</strong>.</li>
</ul>
<h2 id="alerts-v1-dataplane-only">Alerts (v1 dataplane only)</h2>
<p>You can configure notifications for upcoming CNI maintenance events using the Notifications feature in the Cloudflare dashboard. It is recommended to subscribe to two types of notifications to stay fully informed.</p>
<p><strong>CNI Connection Maintenance Alert:</strong> This alert informs you about maintenance events (scheduled, updated, or canceled) that directly impact your CNI circuits used with the Cloudflare Virtual Network only.</p>
<ul>
<li>You will receive warnings up to two weeks in advance for maintenance impacting your Magic Transit/WAN CNI connections.</li>
<li>You will be notified if the details of a scheduled maintenance change or if it is canceled.</li>
<li>For recently added maintenance, notifications are sent after a six-hour delay to prevent alerting fatigue from minor adjustments.</li>
</ul>
<p><strong>Cloudflare Status Maintenance Notification:</strong> This alert informs you about maintenance for an entire Cloudflare Point of Presence (PoP). While not specific to your CNI, this maintenance will impact all CNI services in that location. This includes connections used only for peering without Cloudflare Virtual Network.</p>
<ul>
<li>You will be warned about potentially disruptive maintenance at the PoP level.</li>
<li>By default, you are notified for all event types (Scheduled, Changed, Canceled), but you can filter these.</li>
<li>By default, you are notified for all Cloudflare PoPs, but you can filter for only the specific locations where you have CNI circuits.</li>
</ul>
<h2 id="how-to-configure-alerts">How to configure alerts</h2>
<h3 id="enable-cni-connection-maintenance-alert">Enable CNI Connection Maintenance Alert</h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Notifications</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Add</strong>.</li>
<li>From the product drop-down menu, select <em>Cloudflare Network Interconnect</em>.</li>
<li>Select <strong>Connection Maintenance Alert</strong>.</li>
<li>Give your notification a name and an optional description.</li>
<li>Choose your preferred notification method, such as email address.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h3 id="enable-cloudflare-status-maintenance-notification">Enable Cloudflare Status Maintenance Notification</h3>
<p>First, identify the PoP code for your CNI circuit:</p>
<ol>
<li>In the Cloudflare dashboard, go to <strong>Interconnects</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select the CNI you want to enable notifications for.</li>
<li>In the menu that appears, note the Data Center code (for example, <code>gru-b</code>).</li>
</ol>
<p>Now, configure the alert:</p>
<ol>
<li>Go to <strong>Notifications</strong> and select <strong>Add</strong>.</li>
<li>From the product drop-down menu, select <em>Cloudflare Status</em>.</li>
<li>Select <strong>Maintenance Notification</strong>.</li>
<li>Give your notification a name and choose your notification method.</li>
<li>Select <strong>Next</strong>.</li>
<li>Optionally, use the <strong>Filter on Event Type</strong> to select only the event types you want to be alerted for (Scheduled, Changed, Canceled).</li>
<li>In <strong>Filter on Points of Presence</strong>, enter the three-letter code for your PoP (for example, for <code>gru-b</code>, enter <code>gru</code>). You can add multiple PoPs, separated by commas.</li>
<li>Select <strong>Create</strong>.</li>
</ol>
