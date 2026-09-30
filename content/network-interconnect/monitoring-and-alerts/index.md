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
