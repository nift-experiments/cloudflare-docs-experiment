<p>Cloudflare One can integrate with Uptycs to require that users connect to certain applications from managed devices. This service-to-service posture check uses the Cloudflare One Client to read endpoint data from Uptycs. Devices are identified by their serial numbers. If multiple devices have the same serial number, Cloudflare cannot accurately match a device with a third-party provider device. You must ensure that each of your devices has a unique serial number.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Uptycs agent is deployed on the device.</li>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/integrations/service-providers/">Service providers</a>.</p>
<h2 id="1-obtain-uptycs-settings"><ol>
<li>Obtain Uptycs Settings</li>
</ol></h2>
<p>The following Uptycs values are needed to set up the Uptycs posture check:</p>
<ul>
<li>Client key</li>
<li>Client Secret</li>
<li>Customer ID</li>
</ul>
<p>To obtain these values:</p>
<ol>
<li>Open your Uptycs console.</li>
<li>Go to <strong>Account Settings</strong> &gt; <strong>API Key</strong>.</li>
<li>Generate and download your <code>.json</code> file. This file will contain your <strong>Client key</strong>, <strong>Client Secret</strong> and <strong>Customer ID</strong>.</li>
</ol>
<h2 id="2-add-uptycs-as-a-service-provider"><ol start="2">
<li>Add Uptycs as a service provider</li>
</ol></h2>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Service providers</strong>.</p>
</li>
<li>
<p>Select <strong>Add new</strong>.</p>
</li>
<li>
<p>Select <strong>Uptycs</strong>.</p>
</li>
<li>
<p>Enter any name for the provider. This name will be used throughout the dashboard to reference this connection.</p>
</li>
<li>
<p>Enter the <strong>Client ID</strong>, <strong>Client secret</strong> and <strong>Customer ID</strong> as you noted down above.</p>
</li>
<li>
<p>Select a <strong>Polling frequency</strong> for how often Cloudflare One should query Uptycs for information.</p>
</li>
<li>
<p>Select <strong>Test and save</strong>.</p>
</li>
</ol>
<h2 id="3-configure-the-posture-check"><ol start="3">
<li>Configure the posture check</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Posture checks</strong> &gt; <strong>Service provider checks</strong>.</li>
<li>Select <strong>Add a check</strong>.</li>
<li>Select the Uptycs provider.</li>
<li>Enter any name for the posture check.</li>
<li>Configure the <a href="#device-posture-attributes">attributes</a> required for the device to pass the posture check.</li>
<li>Select <strong>Save</strong>.</li>
<li>To test, go to <strong>Insight</strong> &gt; <strong>Logs</strong> &gt; <strong>Posture logs</strong> and verify that the service provider posture check is returning the expected results.</li>
</ol>
<p>You can now use this posture check in a <a href="/cloudflare-one/reusable-components/posture-checks/#3-build-a-device-posture-policy">device posture policy</a>.</p>
<h2 id="device-posture-attributes">Device posture attributes</h2>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Score</td>
<td>Zero Trust score assigned to the device by Uptycs</td>
</tr>
</tbody>
</table>
