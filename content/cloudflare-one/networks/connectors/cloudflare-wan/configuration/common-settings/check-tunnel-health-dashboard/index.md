---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/check-tunnel-health-dashboard/
  description: Check tunnel health in the dashboard in Zero Trust networking.
  full_title: Check tunnel health in the dashboard · Cloudflare One docs
  head_html: <title>Check tunnel health in the dashboard · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Check tunnel health in the dashboard in Zero Trust networking."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/check-tunnel-health-dashboard/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/check-tunnel-health-dashboard/index.md"><meta property="og:title" content="Check tunnel health in the dashboard · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Check tunnel health in the dashboard in Zero Trust networking."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/check-tunnel-health-dashboard/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/check-tunnel-health-dashboard/#page","headline":"Check tunnel health in the dashboard \u00b7 Cloudflare One docs","description":"Check tunnel health in the dashboard in Zero Trust networking.","url":"https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/check-tunnel-health-dashboard/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/check-tunnel-health-dashboard/
  schema: 1
---
<p>The Cloudflare dashboard monitors the health of all <span class="nb-glossary-tooltip" title="anycast">anycast</span> tunnels on your account that route traffic from Cloudflare to your origin network.</p>
<p>The dashboard shows the view of tunnel health as measured from each Cloudflare location where your traffic is likely to land. If the tunnels are healthy on your side, you will see the majority of servers reporting an <strong>up</strong> status. It is normal for a subset of these locations to report tunnel status as degraded or unhealthy, since the Internet is not homogeneous and intermediary path issues between Cloudflare and your network can cause interruptions for specific paths.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5712.md")
</aside>
<p>Not all data centers are relevant to you at all times. You can refer to the <strong>Traffic volume (1 hour)</strong> column to understand if a given data center is receiving traffic for your network, and if its health status is relevant to you.</p>
<h2 id="check-tunnel-health">Check tunnel health</h2>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> and go to <strong>Insights</strong>.</li>
<li>Go to <strong>Network health</strong> &gt; <strong>WAN connector health</strong>.</li>
<li>In this view you can access a list of your tunnels and their current health status. You can also check the amount of health checks passed in the last hour as well as traffic volume for each tunnel.</li>
<li>Find the tunnel you want to inspect, select the three dots next to it, and choose:
<ul>
<li><strong>Create alert</strong>: Opens the <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/common-settings/configure-tunnel-health-alerts/">notifications wizard</a> so you can create specific alerts for that tunnel when specific conditions are met.</li>
<li><strong>Network Analytics</strong>: Opens the Analytics section of the dash, prefiltered with the tunnel you want to inspect.</li>
</ul>
</li>
<li>Alternatively, from the list of tunnels, select the tunnel you want to inspect to access details about it.</li>
</ol>
<h2 id="check-tunnel-health-for-a-specific-tunnel">Check tunnel health for a specific tunnel</h2>
<p>You can drill down into a specific tunnel to check its health status and other information.</p>
<ol>
<li>
<p>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> and go to <strong>Insights</strong>.</p>
</li>
<li>
<p>Go to <strong>Network health</strong> &gt; <strong>WAN connector health</strong>.</p>
</li>
<li>
<p>Find and select the tunnel you want to inspect.</p>
</li>
</ol>
<p>The next view displays detailed information about the tunnel, including:</p>
<ul>
<li>Status information
<ul>
<li>Up: More than 80% of health checks pass.</li>
<li>Degraded: More than 40% of health checks pass.</li>
<li>Down: Less than 40% of health checks pass.</li>
</ul>
</li>
<li>Health checks passed in the last hour</li>
<li>Traffic volume in the last hour</li>
</ul>
<p>If you select the three dots in front of the tunnel you want to inspect, you have access to the following tools:</p>
<ul>
<li>Packet captures: Collect <a href="/cloudflare-network-firewall/packet-captures/">packet level data for your traffic</a></li>
<li>Network Analytics: Leverage real-time insights into <a href="/cloudflare-one/networks/connectors/cloudflare-wan/analytics/network-analytics/">network analytics</a>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5711.md")
</aside>
<h2 id="connectors">Connectors</h2>
<p>Cloudflare One Appliance (formerly Magic WAN Connector) also includes a heartbeat function, an additional way of communicating its health status which does not depend on successfully setting up any tunnels. The heartbeat function communicates periodically with Cloudflare through HTTPS and lets Cloudflare know that the Cloudflare One Appliance in question is connected to the Internet and reachable.</p>
<p>Refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/configuration/appliance/maintenance/heartbeat/">Heartbeat</a> to learn more.</p>
<h2 id="troubleshooting">Troubleshooting</h2>
<p>If you received a tunnel health alert but are unsure whether it affects your traffic, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/troubleshooting/connectivity/">Troubleshoot connectivity</a> to determine whether the alert is relevant.</p>
<p>If your tunnels show as unhealthy or degraded, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-wan/troubleshooting/tunnel-health/">Troubleshoot tunnel health</a> for common issues and solutions.</p>
