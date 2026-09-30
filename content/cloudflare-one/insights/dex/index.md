---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/insights/dex/
  description: Digital experience resources and guides for Zero Trust analytics.
  full_title: Digital experience · Cloudflare One docs
  head_html: <title>Digital experience · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Digital experience resources and guides for Zero Trust analytics."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/insights/dex/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/insights/dex/index.md"><meta property="og:title" content="Digital experience · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Digital experience resources and guides for Zero Trust analytics."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/insights/dex/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Navigation"><meta name="algolia_content_type" content="Navigation"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/cloudflare-one/insights/dex/#page","headline":"Digital experience \u00b7 Cloudflare One docs","description":"Digital experience resources and guides for Zero Trust analytics.","url":"https://developers.cloudflare.com/cloudflare-one/insights/dex/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/insights/dex/
  schema: 1
---
<p>Digital Experience Monitoring (DEX) provides visibility into device, network, and application performance across your Zero Trust organization.</p>
<p>With DEX, you can monitor the state of your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a> deployment and resolve issues impacting end-user productivity. DEX is designed for IT and security teams who need to proactively monitor and troubleshoot device and network health across distributed environments. DEX is available on all Cloudflare Zero Trust and SASE plans.</p>
<p>Enrolled devices automatically send device-state telemetry to DEX. Synthetic tests are optional checks that administrators create to monitor specific public or private endpoints.</p>
<p>DEX is compatible with Cloudflare's <a href="/data-localization/metadata-boundary/">Customer Metadata Boundary</a> (CMB) for the EU (European Union). When CMB is configured for the EU, customer logs are stored exclusively in the EU region.</p>
<p>Refer to <a href="/cloudflare-one/insights/">Insights overview</a> to learn how to use Analytics dashboards together with <a href="/cloudflare-one/insights/analytics-overview/">Analytics Overview</a> and <a href="/cloudflare-one/insights/dex/">Digital Experience Monitoring (DEX)</a> for complete visibility and troubleshooting.</p>
<h2 id="when-a-user-reports-a-problem">When a user reports a problem</h2>
<p>If a user notifies that “the connection is not working” or “performance is slow,” DEX allows you to:</p>
<ul>
<li>Use <a href="/cloudflare-one/insights/dex/monitoring/">device monitoring</a> to check device health and endpoint connectivity.</li>
<li>Optionally, test network health and application responsiveness with <a href="/cloudflare-one/insights/dex/tests/">synthetic tests</a> that run periodically from user devices.</li>
<li>Identify whether problems originate from the device (such as <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/troubleshooting/troubleshooting-guide/">issues with the Cloudflare One Client</a>), the network, or Cloudflare.</li>
</ul>
<h2 id="troubleshooting-other-cloudflare-one-features">Troubleshooting other Cloudflare One features</h2>
<p>Use DEX to troubleshoot other Cloudflare One features:</p>
<ul>
<li>Test connectivity to a <a href="/cloudflare-one/access-controls/applications/http-apps/saas-apps/">SaaS application secured with Access</a>.</li>
<li>Verify that a website routed through <a href="/cloudflare-one/traffic-policies/">Gateway</a> is reachable from user devices.</li>
<li>Confirm that users can successfully reach internal resources after configuring a <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/create-remote-tunnel/">Tunnel</a>.</li>
</ul>
<h3 id="get-started">Get started</h3>
<p>To start using DEX for device, network, and application monitoring:</p>
<ol>
<li><a href="/cloudflare-one/setup/#2-create-a-zero-trust-organization">Create a Zero Trust organization</a>.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Install the Cloudflare One Client</a> and sign in to register your device to the organization.</li>
<li>(Optional) Create <a href="/cloudflare-one/insights/dex/tests/">tests</a> to verify device connectivity to applications and networks.</li>
<li><a href="/cloudflare-one/insights/dex/monitoring/">Monitor</a> device and network health across your fleet using real-time and historical metrics.</li>
<li>Use <a href="/cloudflare-one/insights/dex/diagnostics/">diagnostics</a> to run speed tests and collect remote captures from user devices.</li>
<li>Set up <a href="/cloudflare-one/insights/dex/notifications/">notifications</a> to get alerts when degraded connectivity or application performance is detected.</li>
</ol>
<h3 id="troubleshooting">Troubleshooting</h3>
<p>For help resolving common issues with Digital Experience Monitoring, refer to <a href="/cloudflare-one/insights/dex/troubleshooting/">Troubleshoot Digital Experience Monitoring</a>.</p>
<h3 id="directory">Directory</h3>
<p>Review all available documentation for DEX capabilities.</p>
<ul class="directory-listing"><li><a href="/cloudflare-one/insights/dex/monitoring/">Device monitoring</a></li><li><a href="/cloudflare-one/insights/dex/tests/">Synthetic tests</a></li><li><a href="/cloudflare-one/insights/dex/rules/">Rules</a></li><li><a href="/cloudflare-one/insights/dex/diagnostics/">Diagnostics</a></li><li><a href="/cloudflare-one/insights/dex/notifications/">Notifications</a></li><li><a href="/cloudflare-one/insights/dex/ip-visibility/">IP visibility</a></li><li><a href="/cloudflare-one/insights/dex/dex-mcp-server/">DEX MCP server</a></li><li><a href="/cloudflare-one/insights/dex/troubleshooting/">Troubleshoot Digital Experience Monitoring</a></li><li><a href="https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/dex-analysis">MCP server</a></li></ul>
