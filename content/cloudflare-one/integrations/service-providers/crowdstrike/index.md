<p>Cloudflare One can integrate with Crowdstrike to require that users connect to certain applications from managed devices. This service-to-service posture check uses the Cloudflare One Client to read endpoint data from Crowdstrike. Devices are identified by their serial numbers. If multiple devices have the same serial number, Cloudflare cannot accurately match a device with a third-party provider device. You must ensure that each of your devices has a unique serial number.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Device posture with Crowdstrike requires:</p>
<ul>
<li>Falcon Enterprise plan or above</li>
<li>Crowdstrike agent is deployed on the device.</li>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/integrations/service-providers/">Service providers</a>.</p>
<h2 id="set-up-crowdstrike-as-a-service-provider">Set up CrowdStrike as a service provider</h2>
<h3 id="1-obtain-crowdstrike-settings"><ol>
<li>Obtain CrowdStrike settings</li>
</ol></h3>
<p>The following CrowdStrike values are needed to set up the CrowdStrike posture check:</p>
<ul>
<li>Client ID</li>
<li>Client Secret</li>
<li>Base URL</li>
<li>Customer ID</li>
</ul>
<p>To retrieve those values:</p>
<ol>
<li>Log in to your Falcon Dashboard.</li>
<li>Go to <strong>Support and resources</strong> &gt; <strong>API Clients and Keys</strong>.</li>
<li>Select <strong>Create API client</strong> and enter any name for the client.</li>
<li>Turn on the following API permissions:</li>
</ol>
<table>
<thead>
<tr>
<th>Scope</th>
<th>Permission</th>
</tr>
</thead>
<tbody>
<tr>
<td>Hosts</td>
<td>Read</td>
</tr>
<tr>
<td>Zero Trust Assessment</td>
<td>Read</td>
</tr>
</tbody>
</table>
5. Select **Create**.
6. Copy the **Client ID**, **Client Secret**, and **Base URL** to a safe place.
7. Go to **Host setup and management** > **Sensor downloads** and copy your **Customer ID**.
<h3 id="2-add-crowdstrike-as-a-service-provider"><ol start="2">
<li>Add CrowdStrike as a service provider</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Service providers</strong>.</p>
</li>
<li>
<p>Select <strong>Add new</strong>.</p>
</li>
<li>
<p>Select <strong>Crowdstrike</strong>.</p>
</li>
<li>
<p>Enter any name for the provider. This name will be used throughout the dashboard to reference this connection.</p>
</li>
<li>
<p>Enter the <strong>Client ID</strong> and <strong>Client secret</strong> you noted down above.</p>
</li>
<li>
<p>In <strong>Rest API URL</strong>, enter your <strong>Base URL</strong>.</p>
</li>
<li>
<p>Enter your <strong>Customer ID</strong>.</p>
</li>
<li>
<p>Choose a <strong>Polling frequency</strong> for how often Cloudflare Zero Trust should query CrowdStrike for information.</p>
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
<li>Select the Crowdstrike provider.</li>
<li>Enter any name for the posture check.</li>
<li>Configure the <a href="#device-posture-attributes">attributes</a> required for the device to pass the posture check.</li>
<li>Select <strong>Save</strong>.</li>
<li>To test, go to <strong>Insight</strong> &gt; <strong>Logs</strong> &gt; <strong>Posture logs</strong> and verify that the service provider posture check is returning the expected results.</li>
</ol>
<p>You can now use this posture check in a <a href="/cloudflare-one/reusable-components/posture-checks/#3-build-a-device-posture-policy">device posture policy</a>.</p>
<h2 id="device-posture-attributes">Device posture attributes</h2>
<p>Device posture data is gathered from the <a href="https://falcon.us-2.crowdstrike.com/documentation/156/zero-trust-assessment-apis">CrowdStrike Zero Trust Assessment APIs</a>. To learn more about how scores are calculated, refer to the <a href="https://falcon.us-2.crowdstrike.com/documentation/138/zero-trust-assessment">CrowdStrike Zero Trust Assessment</a> documentation.</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Description</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>OS</td>
<td>OS signal score</td>
<td><code>1</code> to <code>100</code></td>
</tr>
<tr>
<td>Overall</td>
<td>Overall ZTA score</td>
<td><code>1</code> to <code>100</code></td>
</tr>
<tr>
<td>Sensor config</td>
<td>Sensor signal score</td>
<td><code>1</code> to <code>100</code></td>
</tr>
<tr>
<td>Version</td>
<td>ZTA score version</td>
<td><code>2.1.0</code></td>
</tr>
<tr>
<td>State</td>
<td>Current online status of the device</td>
<td><em>Online</em>, <em>Offline</em>, or <em>Unknown</em></td>
</tr>
<tr>
<td>Last seen</td>
<td>Elapsed time since the device was last seen. Only returned if its state is <code>online</code> or <code>unknown</code>.</td>
<td>In the last 1 hour, 3 hours, 6 hours, 12 hours, 24 hours, 7 days, 30 days, or more than 30 days</td>
</tr>
</tbody>
</table>
