<p>Cloudflare One can integrate with SentinelOne to require that users connect to certain applications from managed devices. This service-to-service posture check uses the Cloudflare One Client to read endpoint data from SentinelOne. Devices are identified by their serial numbers. If multiple devices have the same serial number, Cloudflare cannot accurately match a device with a third-party provider device. You must ensure that each of your devices has a unique serial number.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>SentinelOne agent is deployed on the device.</li>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/integrations/service-providers/">Service providers</a>.</p>
<h2 id="set-up-sentinelone-as-a-service-provider">Set up SentinelOne as a service provider</h2>
<h3 id="1-obtain-sentinelone-settings"><ol>
<li>Obtain SentinelOne settings</li>
</ol></h3>
<p>The following SentinelOne values are needed to set up the SentinelOne posture check:</p>
<ul>
<li>API Token</li>
<li>REST API URL</li>
</ul>
<p>To retrieve those values:</p>
<ol>
<li>Log in to your SentinelOne Dashboard.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Users</strong> &gt; <strong>Create new Service User</strong>.</li>
<li>Select <strong>Create New Service User</strong>.</li>
<li>Enter a <strong>Name</strong> and <strong>Expiration Date</strong> and select <strong>Next</strong>.</li>
<li>Set <strong>Scope of Access</strong> to <em>Viewer</em>.</li>
<li>Select <strong>Create User</strong>. SentinelOne will generate an API Token for this user.</li>
<li>Copy the <strong>API Token</strong> to a safe location.</li>
<li>Select <strong>Close</strong>.</li>
<li>Copy the <strong>Rest API URL</strong> from your browser's address bar (for example, <code>https://&lt;S1-DOMAIN&gt;.sentinelone.net</code>).</li>
</ol>
<h3 id="2-add-sentinelone-as-a-service-provider"><ol start="2">
<li>Add SentinelOne as a service provider</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Service providers</strong>.</p>
</li>
<li>
<p>Select <strong>Add new</strong>.</p>
</li>
<li>
<p>Select <strong>SentinelOne</strong>.</p>
</li>
<li>
<p>Enter any name for the provider. This name will be used throughout the dashboard to reference this connection.</p>
</li>
<li>
<p>In <strong>Client Secret</strong>, enter your <strong>API Token</strong>.</p>
</li>
<li>
<p>In <strong>Rest API URL</strong>, enter <code>https://&lt;S1-DOMAIN&gt;.sentinelone.net</code>.</p>
</li>
<li>
<p>Choose a <strong>Polling frequency</strong> for how often Cloudflare One should query SentinelOne for information.</p>
</li>
<li>
<p>Select <strong>Test and save</strong>.</p>
</li>
</ol>
<h3 id="3-configure-the-posture-check"><ol start="3">
<li>Configure the posture check</li>
</ol></h3>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Posture checks</strong> &gt; <strong>Service provider checks</strong>.</li>
<li>Select <strong>Add a check</strong>.</li>
<li>Select the SentinelOne provider.</li>
<li>Enter any name for the posture check.</li>
<li>Configure the <a href="#device-posture-attributes">attributes</a> required for the device to pass the posture check.</li>
<li>Select <strong>Save</strong>.</li>
<li>To test, go to <strong>Insight</strong> &gt; <strong>Logs</strong> &gt; <strong>Posture logs</strong> and verify that the service provider posture check is returning the expected results.</li>
</ol>
<p>You can now use this posture check in a <a href="/cloudflare-one/reusable-components/posture-checks/#3-build-a-device-posture-policy">device posture policy</a>.</p>
<h2 id="device-posture-attributes">Device posture attributes</h2>
<p>Device posture data is gathered from the SentinelOne Management APIs. For more information, refer to <code>https://&lt;S1-DOMAIN&gt;.sentinelone.net/api-doc/overview</code>.</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Infected</td>
<td>Whether the device is infected</td>
</tr>
<tr>
<td>Active Threats</td>
<td>Number of active threats on the device</td>
</tr>
<tr>
<td>Is Active</td>
<td>Whether the SentinelOne Agent is active</td>
</tr>
<tr>
<td>Network status</td>
<td>Whether the SentinelOne Agent is connected to the SentinelOne service</td>
</tr>
<tr>
<td>Operational State</td>
<td>The <a href="https://community.sentinelone.com/s/login/?ec=302&amp;startURL=%2Fs%2Farticle%2F000005285">operational state</a> of the SentinelOne Agent.</td>
</tr>
</tbody>
</table>
<h3 id="detect-user-risk-behavior">Detect user risk behavior</h3>
<p>SentinelOne provides endpoint detection and response (EDR) signals to determine <a href="/cloudflare-one/team-and-resources/users/risk-score/">user risk score</a>. User risk scores allow you to detect users that present security risks to your organization. For more information, refer to <a href="/cloudflare-one/team-and-resources/users/risk-score/#predefined-risk-behaviors">Predefined risk behaviors</a>.</p>
