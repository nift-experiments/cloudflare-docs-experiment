---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-wan/configuration/common-settings/sites/
  description: Set up WAN sites for your network locations.
  full_title: Set up a site · Cloudflare WAN docs
  head_html: <title>Set up a site · Cloudflare WAN docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up WAN sites for your network locations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-wan/configuration/common-settings/sites/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-wan/configuration/common-settings/sites/index.md"><meta property="og:title" content="Set up a site · Cloudflare WAN docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up WAN sites for your network locations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-wan/configuration/common-settings/sites/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare WAN"><meta name="algolia_product_filter" content="Cloudflare WAN"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare WAN"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-wan/configuration/common-settings/sites/#page","headline":"Set up a site \u00b7 Cloudflare WAN docs","description":"Set up WAN sites for your network locations.","url":"https://developers.cloudflare.com/cloudflare-wan/configuration/common-settings/sites/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-wan/configuration/common-settings/sites/
  schema: 1
---
<p>Sites represent the local network of a data center, office, or other physical location, and combine all on-ramps available there. Sites also allow you to quickly check the state of your on-ramps and set up health alert settings so that you get notified when there are issues with the site's on-ramps.</p>
<p>To use a site, start by setting up your on-ramps. On-ramps can be:</p>
<ul>
<li><a href="/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/">GRE or IPsec tunnels</a></li>
<li><a href="/cloudflare-wan/configuration/appliance/">Cloudflare One Appliance</a></li>
<li>Direct <a href="/cloudflare-wan/network-interconnect/">CNI link</a></li>
</ul>
<p>Before creating a site, ensure you have set up at least one on-ramp. Then, follow these steps:</p>
<h2 id="add-a-site">Add a site</h2>
<ol>
<li>Go to the <strong>Network health</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>Network overview</strong>, select <strong>Add a site</strong>.</li>
<li>Add a name and description for your new site. Optionally, you can also add the geographical coordinates for your site in <strong>Latitude</strong> and <strong>Longitude</strong>. If you add geographical coordinates, your site's location will appear in the map once created.</li>
<li>Select <strong>Create and continue</strong>.</li>
<li>Choose one or more on-ramps for your site from the list. Remember to only choose the on-ramps available to that particular site, as the list might include on-ramps available on other locations.</li>
<li>Select <strong>Continue</strong>.</li>
<li>In <strong>Define alert settings</strong> you set up alerts to notify you when there are issues with your site's on-ramps. If you want to set up alerts later, select <strong>Skip this for now</strong> to complete your setup. Otherwise, continue reading.</li>
<li>In <strong>Tunnel Health Check Alert</strong> &gt; <strong>Notification name</strong>, enter a name for the site's alert.</li>
<li>Under <strong>Alert settings</strong>, choose how you want to be notified when there is an issue. You can add webhooks as well as email addresses.</li>
<li>In <strong>Alert sensitivity level</strong> define the threshold for Tunnel health alerts to be fired. For details, refer to <a href="/cloudflare-wan/reference/how-cloudflare-calculates-tunnel-health-alerts/">How Cloudflare calculates Tunnel health alerts</a>.</li>
<li>Select <strong>Complete setup</strong> to finish setting up your site.</li>
</ol>
<p>Your site is now set up. If you have other sites you need to set up, repeat the steps above. If you did not set up alerts, we strongly recommend that you do it. Otherwise you will not be notified when there is a problem with one of your on-ramps.</p>
<hr />
<h2 id="network-overview">Network overview</h2>
<p>After adding your sites, the Network overview section of the dashboard provides a summary of the connectivity status and traffic analytics for all your sites. This is a great place to start if you receive a Cloudflare WAN alert, need to begin the troubleshooting process, or are performing routine monitoring.</p>
<p>Network overview has the following data types available:</p>
<details class="nb-details"><summary>Geographic map summary</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6930.md")
</div></details>
<details class="nb-details"><summary>Cloudflare WAN site data table</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6931.md")
</div></details>
<details class="nb-details"><summary>Cloudflare WAN site data</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6932.md")
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
<p>The dashboard displays the number of sites with no location set, meaning sites for which you did not set up a geographic location. To add a location to a site, find the site you want to add location to, and select <strong>no location set</strong> to edit its location settings. Refer to <a href="#set-geographic-coordinates">Set geographic coordinates</a> for more information.</p>
<h3 id="traffic-overview">Traffic overview</h3>
<p>Traffic overview aggregates all Cloudflare WAN sites configured in your account. Here, you can check summary information about each site like:</p>
<ul>
<li>Site status</li>
<li>Traffic sent and received</li>
</ul>
<p>Select one of your sites to have access to a more detailed view of its traffic, including traffic by tunnel.</p>
<hr />
<h2 id="edit-a-site">Edit a site</h2>
<h3 id="add-or-remove-on-ramps">Add or remove on-ramps</h3>
<ol>
<li>Go to the <strong>Network health</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Go to <strong>Network overview</strong> &gt; <strong>Traffic overview</strong>.</li>
<li>Find your site &gt; select the three dots in front of it &gt; <strong>Edit</strong>.</li>
<li>Select <strong>On-ramps</strong>.</li>
<li>Select <strong>Add</strong> to add a new on-ramp.</li>
<li>If you want to remove an on-ramp, select the three dots in front of your on-ramp &gt; <strong>Remove</strong>.</li>
</ol>
<h3 id="set-geographic-coordinates">Set geographic coordinates</h3>
<p>If you add geographic coordinates to your site, it will appear in the Network map. To set up or edit geographic coordinates to an existing site:</p>
<ol>
<li>Go to the <strong>Network health</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>Go to <strong>Network overview</strong> &gt; <strong>Traffic overview</strong>.</p>
</li>
<li>
<p>Find your site &gt; select the three dots in front of it &gt; <strong>Edit</strong>.</p>
</li>
<li>
<p>In <strong>Basic information</strong>, edit your site's <strong>Latitude</strong> and <strong>Longitude</strong> coordinates.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<h3 id="set-thresholds-for-site-health">Set thresholds for site health</h3>
<p>When you set up an alert for your site, you will be notified when there is an issue with one or more on-ramps. These alerts are sent when the percentage of successful health checks for a Cloudflare WAN on-ramp drops below the selected service-level objective (SLO). Setting health alerts will also display unhealthy tunnels in the Network map and in the Traffic overview sections.</p>
<p>To set up health alerts:</p>
<ol>
<li>Configure <a href="/cloudflare-wan/configuration/common-settings/configure-tunnel-health-alerts/">Tunnel health alerts</a> across all of the tunnels associated with each Cloudflare WAN site.</li>
<li>After configuring Tunnel health alerts, any Cloudflare WAN site with a tunnel (on-ramp) that is outside of its SLO threshold will be labeled unhealthy in Network map and Traffic overview.</li>
</ol>
