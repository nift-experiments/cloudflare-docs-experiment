<p>Cloudflare One Appliance (formerly Magic WAN Connector) communicates periodically with Cloudflare via HTTPS. This is also known as a heartbeat, and lets Cloudflare know that the Cloudflare One Appliance in question is connected to the Internet and reachable.</p>
<p>The heartbeat calls are made to <code>api.cloudflare.com</code>. Each Cloudflare One Appliance has a heartbeat frequency of 10 seconds, independently of the number of WAN interfaces you have running on your device.</p>
<p>There are three symbols for the heartbeat signal that allow you to quickly check the status of Cloudflare One Appliance:</p>
<ul>
<li><strong>Blue <code>i</code></strong>: Cloudflare One Appliance is contacting Cloudflare as expected.</li>
<li><strong>Yellow triangle</strong>: Cloudflare One Appliance has not yet connected to Cloudflare.</li>
<li><strong>Red triangle</strong>: There is a potential problem with Cloudflare One Appliance.</li>
</ul>
<h3 id="access-cloudflare-one-appliance-s-heartbeat">Access Cloudflare One Appliance's heartbeat</h3>
<ol>
<li>Log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, and go to <strong>Networks</strong>.</li>
<li>Go to <strong>Connectors</strong> &gt; <strong>Appliances</strong> &gt; <strong>Appliances</strong>.</li>
<li>Find your Cloudflare One Appliance, and place your cursor over the icon on the <strong>Status</strong> column to check the timestamp. The timestamp displays the last time Cloudflare One Appliance successfully contacted Cloudflare.</li>
</ol>
