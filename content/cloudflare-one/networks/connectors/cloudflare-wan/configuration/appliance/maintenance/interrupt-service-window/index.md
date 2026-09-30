<p>The Interrupt window defines when Cloudflare One Appliance (formerly Magic WAN Connector) can update its systems. When Cloudflare One Appliance is updating, this may result in an interruption to existing connections. Set up a time window that minimizes disruption to your sites.</p>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, and go to <strong>Networking</strong> &gt; <strong>Connectors</strong>.</li>
<li>In <strong>Appliances</strong> &gt; <strong>Appliances</strong>, select the Cloudflare One Appliance for which you want to set up the update window &gt; <strong>Edit</strong>.</li>
<li>In <strong>Interrupt window</strong>, select the most appropriate time for the Cloudflare One Appliance to update its systems:
<ul>
<li><strong>Timezone</strong>: Select the time zone for the Cloudflare One Appliance to update.</li>
<li><strong>Start time</strong>: Choose an hour for the Cloudflare One Appliance to start updating. Cloudflare recommends you choose an hour when there is minimal activity in your network, to avoid potential disruptions.</li>
<li><strong>Duration</strong>: Duration indicates the time window during which the Cloudflare One Appliance is scheduled to update. For example, if you configure your Cloudflare One Appliance to update at <code>22:00</code> and specify a <strong>Duration</strong> of <code>4 hours</code>, the Cloudflare One Appliance will attempt to update within the four-hour period following <code>22:00</code>.</li>
</ul>
</li>
</ol>
