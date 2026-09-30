<p>Cloudflare One can integrate with Kolide to require that users connect to certain applications from managed devices. This service-to-service posture check uses the Cloudflare One Client to read endpoint data from Kolide. Devices are identified by their serial numbers. If multiple devices have the same serial number, Cloudflare cannot accurately match a device with a third-party provider device. You must ensure that each of your devices has a unique serial number.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Kolide agent is deployed on the device.</li>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/integrations/service-providers/">Service providers</a>.</p>
<h2 id="set-up-kolide-as-a-service-provider">Set up Kolide as a service provider</h2>
<h3 id="1-create-a-client-secret-in-kolide"><ol>
<li>Create a Client Secret in Kolide</li>
</ol></h3>
<ol>
<li>Log in to your Kolide dashboard.</li>
<li>Select your profile and go to <strong>Settings</strong> &gt; <strong>Developers</strong>.</li>
<li>Select <strong>Create New Key</strong>.</li>
<li>Enter a <strong>Key Name</strong> and select <strong>Save</strong>.</li>
<li>Copy the <strong>Secret token</strong> to a safe place. This will be your Client Secret.</li>
</ol>
<h3 id="2-add-kolide-as-a-service-provider"><ol start="2">
<li>Add Kolide as a service provider</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Service providers</strong>.</p>
</li>
<li>
<p>Select <strong>Add new</strong>.</p>
</li>
<li>
<p>Select <strong>Kolide</strong>.</p>
</li>
<li>
<p>Enter any name for the provider. This name will be used throughout the dashboard to reference this connection.</p>
</li>
<li>
<p>Enter the <strong>Client secret</strong> you noted down above.</p>
</li>
<li>
<p>Choose a <strong>Polling frequency</strong> for how often Cloudflare One should query Kolide for information.</p>
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
<li>Select the Kolide provider.</li>
<li>Enter any name for the posture check.</li>
<li>Configure the <a href="#device-posture-attributes">attributes</a> required for the device to pass the posture check.</li>
<li>Select <strong>Save</strong>.</li>
<li>To test, go to <strong>Insight</strong> &gt; <strong>Logs</strong> &gt; <strong>Posture logs</strong> and verify that the service provider posture check is returning the expected results.</li>
</ol>
<p>You can now use this posture check in a <a href="/cloudflare-one/reusable-components/posture-checks/#3-build-a-device-posture-policy">device posture policy</a>.</p>
<h2 id="device-posture-attributes">Device posture attributes</h2>
<p>Device posture data is gathered from the <a href="https://kolideapi.readme.io/reference/get_devices-id">Kolide API</a>.</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Auth state</td>
<td>The authorization status of the device, one of: 'Good', 'Notified', 'Will Block', or 'Blocked'</td>
</tr>
</tbody>
</table>
