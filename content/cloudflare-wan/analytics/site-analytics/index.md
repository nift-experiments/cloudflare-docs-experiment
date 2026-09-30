---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-wan/analytics/site-analytics/
  description: View network overview analytics for your WAN sites.
  full_title: Cloudflare WAN network overview · Cloudflare WAN docs
  head_html: <title>Cloudflare WAN network overview · Cloudflare WAN docs</title><meta name="generator" content="Nift"><meta name="description" content="View network overview analytics for your WAN sites."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-wan/analytics/site-analytics/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-wan/analytics/site-analytics/index.md"><meta property="og:title" content="Cloudflare WAN network overview · Cloudflare WAN docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="View network overview analytics for your WAN sites."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-wan/analytics/site-analytics/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare WAN"><meta name="algolia_product_filter" content="Cloudflare WAN"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare WAN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-wan/analytics/site-analytics/#page","headline":"Cloudflare WAN network overview \u00b7 Cloudflare WAN docs","description":"View network overview analytics for your WAN sites.","url":"https://developers.cloudflare.com/cloudflare-wan/analytics/site-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-wan/analytics/site-analytics/
  schema: 1
---
<p>After adding your sites, the Network overview section of the dashboard provides a summary of the connectivity status and traffic analytics for all your sites. This is a great place to start if you receive a Cloudflare WAN alert, need to begin the troubleshooting process, or are performing routine monitoring. Refer to <a href="/cloudflare-wan/configuration/common-settings/sites/">Set up a site</a> for more information on how to set up a site.</p>
<p>Network overview has the following data types available:</p>
<details class="nb-details"><summary>Geographic map summary</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6817.md")
</div></details>
<details class="nb-details"><summary>Cloudflare WAN site data table</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6818.md")
</div></details>
<details class="nb-details"><summary>Cloudflare WAN site data</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6819.md")
</div></details>
<p>To start using network overview:</p>
<div class="nb-dash-button"></div>
<p>You will have access to an overview map with all your active sites, and any alerts for sites that are unhealthy or have no status available to them.</p>
<p>Review the following topics to learn more about the options available to you.</p>
<h3 id="network-map-and-traffic-overview">Network map and traffic overview</h3>
<p>The network map section shows all the sites configured with Cloudflare WAN. At a glance, you can check:</p>
<ul>
<li>How many active sites you have</li>
<li>Location for sites in a map (if you set up their geographic location)</li>
<li>Sites that are healthy or unhealthy</li>
<li>Sites that have no status available</li>
<li>Sites that have no location set</li>
</ul>
<p>The Traffic overview section displays a more granular list of your sites and their status.</p>
<h4 id="site-health">Site health</h4>
<p>Sites can be healthy or unhealthy, and Cloudflare WAN uses this information to route traffic. Refer to <a href="#set-thresholds-for-site-health">Set thresholds for site health</a> to learn more about this topic.</p>
<h4 id="no-status-available">No status available</h4>
<p>The status of a site refers to its health. If your sites show a <strong>No status available</strong> message, this means you did not configure your alert settings when creating your site. For instructions, refer to <a href="/cloudflare-wan/configuration/common-settings/configure-tunnel-health-alerts/">Configure Tunnel health alerts</a>.</p>
<h4 id="no-location-set">No location set</h4>
<p>The dashboard displays the number of sites with no location set, meaning sites for which you did not set up a geographic location. To add a location to a site, find the site you want to add location to, and select <strong>no location set</strong> to edit its location settings. Refer to <a href="/cloudflare-wan/configuration/common-settings/sites/#set-geographic-coordinates">Set geographic coordinates</a> for more information.</p>
<h3 id="traffic-overview">Traffic overview</h3>
<p>Traffic overview aggregates all Cloudflare WAN sites configured in your account. Here, you can check summary information about each site like:</p>
<ul>
<li>Site status</li>
<li>Traffic sent and received</li>
</ul>
<p>Select one of your sites to have access to a more detailed view of its traffic, including traffic by tunnel.</p>
<h3 id="set-thresholds-for-site-health">Set thresholds for site health</h3>
<p>When you set up an alert for your site, you will be notified when there is an issue with one or more on-ramps. These alerts are sent when the percentage of successful health checks for a Cloudflare WAN on-ramp drops below the selected service-level objective (SLO). Setting health alerts will also display unhealthy tunnels in the Network map and in the Traffic overview sections.</p>
<p>To set up health alerts:</p>
<ol>
<li>Configure <a href="/cloudflare-wan/configuration/common-settings/configure-tunnel-health-alerts/">Tunnel health alerts</a> across all of the tunnels associated with each Cloudflare WAN site.</li>
<li>After configuring Tunnel health alerts, any Cloudflare WAN site with a tunnel (on-ramp) that is outside of its SLO threshold will be labeled unhealthy in Network map and Traffic overview.</li>
</ol>
