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
