<p>Cloudflare One can integrate with Tanium to require that users connect to certain applications from managed devices. This service-to-service posture check uses the Cloudflare One Client to read endpoint data from Tanium. Devices are identified by their serial numbers. If multiple devices have the same serial number, Cloudflare cannot accurately match a device with a third-party provider device. You must ensure that each of your devices has a unique serial number.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Either Tanium Cloud or on-premise installations of Tanium with the Benchmark entitlement</li>
<li>Tanium agent is deployed on the device.</li>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/integrations/service-providers/">Service providers</a>.</p>
<h2 id="set-up-tanium-as-a-service-provider">Set up Tanium as a service provider</h2>
<h3 id="1-get-tanium-settings"><ol>
<li>Get Tanium settings</li>
</ol></h3>
<p>The following Tanium values are needed to set up the Tanium posture check:</p>
<ul>
<li>Client Secret</li>
<li>REST API URL</li>
</ul>
<p>To retrieve the client secret, create an API token:</p>
<ol>
<li>Log in to your Tanium instance.</li>
<li>Go to <strong>Administration</strong> &gt; <strong>API Tokens</strong>.</li>
<li>Select <strong>New API Token</strong>.</li>
<li>Set <strong>Expire in days</strong> to an appropriate value for your organization. When this token expires, all device posture results will begin to fail unless updated.</li>
<li>Set <strong>Trusted IP addresses</strong> to <code>0.0.0.0/0</code>.</li>
<li>Select <strong>Save</strong>.</li>
<li>Copy the <strong>Client Secret</strong> to a safe place.</li>
</ol>
<p>To retrieve the API URL, determine your Tanium Gateway root endpoint:</p>
<ul>
<li>Tanium Cloud: <code>https://&lt;customerName&gt;-api.cloud.tanium.com/plugin/products/gateway/graphql</code></li>
<li>Tanium On Prem: <code>https://&lt;server&gt;/plugin/products/gateway/graphql</code></li>
</ul>
<h3 id="2-add-tanium-as-a-service-provider"><ol start="2">
<li>Add Tanium as a service provider</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Service providers</strong>.</p>
</li>
<li>
<p>Select <strong>Add new</strong>.</p>
</li>
<li>
<p>Select <strong>Tanium</strong>.</p>
</li>
<li>
<p>Enter any name for the provider. This name will be used throughout the dashboard to reference this connection.</p>
</li>
<li>
<p>Enter the <strong>Client Secret</strong> and <strong>REST API URL</strong> you noted down above.</p>
</li>
<li>
<p>Choose a <strong>Polling frequency</strong> for how often Cloudflare One should query Tanium for information.</p>
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
<li>Select the Tanium provider.</li>
<li>Enter any name for the posture check.</li>
<li>Configure the <a href="#device-posture-attributes">attributes</a> required for the device to pass the posture check.</li>
<li>Select <strong>Save</strong>.</li>
<li>To test, go to <strong>Insight</strong> &gt; <strong>Logs</strong> &gt; <strong>Posture logs</strong> and verify that the service provider posture check is returning the expected results.</li>
</ol>
<p>You can now use this posture check in a <a href="/cloudflare-one/reusable-components/posture-checks/#3-build-a-device-posture-policy">device posture policy</a>.</p>
<h2 id="device-posture-attributes">Device posture attributes</h2>
<p>Device posture data is gathered from <a href="https://developer.tanium.com/site/global/apis/graphql/spectaql/index.gsp#definition-EndpointRisk">Tanium's EndpointRisk API</a>. To learn more about how scores are calculated, refer to the <a href="https://help.tanium.com/bundle/ug_benchmark_cloud/page/benchmark/risk_score.html">Tanium risk score documentation</a>.</p>
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
<td>Total score</td>
<td><code>totalScore</code> of the device.</td>
<td><code>1</code> to <code>1000</code></td>
</tr>
<tr>
<td>Risk level</td>
<td><code>riskLevel</code> of the device.</td>
<td>Low, medium, high, or critical</td>
</tr>
<tr>
<td>EID last seen</td>
<td>Elapsed time since the device was last seen, based on its <code>datetime</code> attribute.</td>
<td>In the last 1 hour, 3 hours, 6 hours, 12 hours, 24 hours, 7 days, 30 days, or more than 30 days</td>
</tr>
</tbody>
</table>
