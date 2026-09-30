---
cp9:
  canonical: https://developers.cloudflare.com/learning-paths/data-center-protection/enable-notifications/
  description: Learn about enable notifications in this guide.
  full_title: Enable Notifications · Cloudflare Learning Paths
  head_html: <title>Enable Notifications · Cloudflare Learning Paths</title><meta name="generator" content="Nift"><meta name="description" content="Learn about enable notifications in this guide."><link rel="canonical" href="https://developers.cloudflare.com/learning-paths/data-center-protection/enable-notifications/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/learning-paths/data-center-protection/enable-notifications/index.md"><meta property="og:title" content="Enable Notifications · Cloudflare Learning Paths"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about enable notifications in this guide."><meta property="og:url" content="https://developers.cloudflare.com/learning-paths/data-center-protection/enable-notifications/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Learning Paths"><meta name="algolia_product_filter" content="Learning Paths"><meta name="pcx_content_group" content="Docs collections"><meta name="pcx_content_type" content="Learning unit"><meta name="algolia_content_type" content="Learning unit"><meta name="pcx_additional_products" content="Magic Transit,DDoS Protection"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/learning-paths/data-center-protection/enable-notifications/#page","headline":"Enable Notifications \u00b7 Cloudflare Learning Paths","description":"Learn about enable notifications in this guide.","url":"https://developers.cloudflare.com/learning-paths/data-center-protection/enable-notifications/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /learning-paths/data-center-protection/enable-notifications/
  schema: 1
---
<p>You can configure Tunnel Health Alerts (formerly Magic Tunnel health alerts) to receive email, webhook, and PagerDuty notifications when the percentage of successful <span class="nb-glossary-tooltip" title="tunnel health-check">health checks</span> for an IPsec/GRE tunnel drops below the selected <a href="/magic-transit/reference/how-cloudflare-calculates-tunnel-health-alerts/">service-level objective (SLO)</a>.</p>
<p>Tunnel health alerts monitor the health check success rate of each IPsec/GRE tunnel included in the alert that has actively transferred customer traffic (excluding health check traffic) over the past six hours. You can define an SLO threshold for the percentage of health checks that must be successful for each IPsec/GRE tunnel. If the number of successful health checks for the IPsec/GRE tunnel(s) included in the alert drops below the SLO threshold, an alert fires.</p>
<h2 id="alert-data">Alert data</h2>
<p>When a Tunnel health alert fires, you receive the following data in the email, webhook, and PagerDuty notification:</p>
<ul>
<li>Cloudflare account name</li>
<li>Cloudflare account ID</li>
<li>Alert type</li>
<li>Tunnel name</li>
<li>Tunnel ID</li>
<li>Tunnel status</li>
<li>Alert SLO</li>
<li>Timestamp</li>
</ul>
<h2 id="slo-thresholds">SLO thresholds</h2>
<p>Currently, there are seven SLO threshold values that you can configure through the Cloudflare dashboard. For a more granular approach, use the <a href="#set-up-tunnel-health-alerts">API</a>.</p>
<p>The SLO threshold for Tunnel health alerts is the percentage of successful health checks for each IPsec/GRE tunnel in the alert:</p>
<table>
<thead>
<tr>
<th>Alert Sensitivity Level</th>
<th>SLO threshold</th>
</tr>
</thead>
<tbody>
<tr>
<td>Minimum</td>
<td>95.0</td>
</tr>
<tr>
<td>Very low</td>
<td>96.0</td>
</tr>
<tr>
<td>Low</td>
<td>97.0</td>
</tr>
<tr>
<td>Medium</td>
<td>98.0</td>
</tr>
<tr>
<td>High</td>
<td>99.0</td>
</tr>
<tr>
<td>Very high</td>
<td>99.5</td>
</tr>
<tr>
<td>Maximum</td>
<td>99.9</td>
</tr>
</tbody>
</table>
<p>The time it takes to receive alerts depends on the sensitivity level you configure for your SLO thresholds. Higher sensitivity levels notify you faster when a tunnel's health degrades, but they may also trigger alerts for brief or minor disruptions. Lower sensitivity levels reduce the chance of false alarms but may delay notifications for less severe issues.</p>
<p>While the underlying detection timing remains consistent across sensitivity levels, the speed of notification depends on how significantly the tunnel's health has dropped and the sensitivity you have chosen. Cloudflare recommends that you <a href="#test-slos">test SLO thresholds</a> to determine which one better serves your use case.</p>
<p>For details, refer to <a href="/magic-transit/reference/how-cloudflare-calculates-tunnel-health-alerts/">How Cloudflare calculates Tunnel health alerts</a>.</p>
<h2 id="set-up-tunnel-health-alerts">Set up Tunnel Health Alerts</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9616.md")
</div></div>
<h2 id="test-slos">Test SLOs</h2>
<p>To test whether a specific alert sensitivity level works for your use case:</p>
<ol>
<li><a href="#set-up-tunnel-health-alerts">Create an alert</a> with a specific sensitivity level for a tunnel with active traffic within the past six hours. If you are unsure which tunnels to choose, refer to <a href="/magic-transit/analytics/network-analytics/">Network Analytics</a> for real-time and historical data about your network.</li>
<li>Disable the tunnel you are testing, so there is 100% <a href="/magic-transit/reference/tunnel-health-checks/">health check failure</a>.</li>
<li>The time it takes for Cloudflare to send you an alert depends on the sensitivity you chose for your alerts.</li>
</ol>
<h2 id="other-notifications">Other notifications</h2>
<p>Cloudflare also recommends that you enable the following account notifications for your Magic Transit service:</p>
<ul>
<li>Layer 3/4 DDoS Attack Alert</li>
<li>Route Leak Detection Alert (to detect BGP Hijacks)</li>
<li>(Optional) Advanced Layer 3/4 DDoS Attack Alert</li>
<li>(Optional) Cloudflare status - Maintenance Notification (in case you want to be alerted regarding maintenance in specific Cloudflare data centers).</li>
</ul>
<p>Refer to <a href="/notifications/">Cloudflare Notifications</a> for more information on how to enable these notifications.</p>
