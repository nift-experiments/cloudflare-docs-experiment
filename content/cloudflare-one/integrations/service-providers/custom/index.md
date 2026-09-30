<p>Cloudflare One allows you to enforce custom device posture checks on your applications. This involves configuring a Cloudflare One Client service-to-service integration that periodically calls the external API of your choice, whether it is a third-party endpoint provider or a home built solution. When called, the API will receive device identifying information from Cloudflare and be expected to return a value between <code>0</code> to <code>100</code>. You can then set up a device posture check that determines if the returned value counts as a pass or fail; for example, you could allow access to a user only if their device has a posture value greater than <code>60</code>.</p>
<pre><code class="language-mermaid">sequenceDiagram&#10;    participant Cloudflare One Client&#10;		participant Cloudflare Access&#10;    participant External API&#10;    Cloudflare One Client-&gt;&gt;Cloudflare Access: Client ID and Secret&#10;		Cloudflare Access-&gt;&gt;External API: Application token&#10;		Cloudflare One Client-&gt;&gt;External API: JSON with user and device identity&#10;    External API--&gt;&gt;Cloudflare One Client: JSON with 0-100 result&#10;</code></pre>
<h2 id="external-api-requirements">External API requirements</h2>
<p>The custom service provider integration works with any API service that meets the following specifications. For an example of a custom device posture integration API, refer to our <a href="https://github.com/cloudflare/custom-device-posture-integration-example-worker">Cloudflare Workers sample code</a>.</p>
<h3 id="authentication">Authentication</h3>
<p>The Cloudflare One Client authenticates to the external API through Cloudflare Access. The external API should <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/">validate the application token</a> issued by Cloudflare Access to ensure that any requests which bypass Access (for example, due to a network misconfiguration) are rejected.</p>
<h3 id="data-passed-to-external-api">Data passed to external API</h3>
<p>Cloudflare will pass the following parameters to the configured API endpoint. You can use this data to identify the device and assign a posture score. For some devices, not all identifying information will apply, in which case the field will be blank. A maximum of 1,000 devices will be sent per a request.</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>device_id</code></td>
<td>Device UUID assigned by the Cloudflare One Client</td>
</tr>
<tr>
<td><code>email</code></td>
<td>Email address used to authenticate the Cloudflare One Client</td>
</tr>
<tr>
<td><code>serial_number</code></td>
<td>Device serial number</td>
</tr>
<tr>
<td><code>mac_address</code></td>
<td>Device MAC address</td>
</tr>
<tr>
<td><code>virtual_ipv4</code></td>
<td>Device virtual IPv4 address</td>
</tr>
<tr>
<td><code>hostname</code></td>
<td>Device name</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5025.md")
</aside>
<p>Example request body:</p>
<pre><code class="language-json">{&#10;  &quot;devices&quot;: {&#10;    [&#10;      {&#10;        &quot;device_id&quot;: &quot;9ece5fab-7398-488a-a575-e25a9a3dec07&quot;,&#10;        &quot;email&quot;: &quot;jdoe@mycompany.com&quot;,&#10;        &quot;serial_number&quot;: &quot;jdR44P3d&quot;,&#10;        &quot;mac_address&quot;: &quot;74:1d:3e:23:e0:fe&quot;,&#10;        &quot;virtual_ipv4&quot;: &quot;100.96.0.10&quot;,&#10;        &quot;hostname&quot;: &quot;string&quot;,&#10;      },&#10;      {...},&#10;      {...}&#10;    ]&#10;  }&#10;}&#10;</code></pre>
<h3 id="expected-response-from-external-api">Expected response from external API</h3>
<p>For each Cloudflare <code>device_id</code>, the API service is expected to return a posture score and optionally a third-party device ID.</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>s2s_id</code></td>
<td>Third party device ID (empty string if unavailable)</td>
</tr>
<tr>
<td><code>score</code></td>
<td>Integer value between <code>0</code> - <code>100</code></td>
</tr>
</tbody>
</table>
<p>Example response body:</p>
<pre><code class="language-json">{&#10;  &quot;result&quot;: {&#10;    &quot;9ece5fab-7398-488a-a575-e25a9a3dec07&quot;: {&#10;      &quot;s2s_id&quot;: &quot;&quot;,&#10;      &quot;score&quot;: 10&#10;    },&#10;    &quot;device_id2&quot;: {...},&#10;    &quot;device_id3&quot;: {...}&#10;  }&#10;}&#10;</code></pre>
<h2 id="set-up-custom-device-posture-checks">Set up custom device posture checks</h2>
<h3 id="1-create-a-service-token"><ol>
<li>Create a service token</li>
</ol></h3>
<p>The Cloudflare One Client uses an Access Client ID and Access Client Secret to securely authenticate to the external API. If you do not already have an Access Client ID and Access Client Secret, <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/#create-a-service-token">create a new service token</a>.</p>
<h3 id="2-create-an-access-application"><ol start="2">
<li>Create an Access application</li>
</ol></h3>
<p>Next, secure the external API behind Cloudflare Access so that the Cloudflare One Client can authenticate with the service token. To add the API endpoint to Access:</p>
<ol>
<li><a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">Create a self-hosted application</a> for your API endpoint.</li>
<li>Add the following Access policy to the application. Make sure that <strong>Action</strong> is set to <em>Service Auth</em> (not <em>Allow</em>).</li>
</ol>
<table>
<thead>
<tr>
<th>Action</th>
<th>Rule type</th>
<th>Selector</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Service Auth</td>
<td>Include</td>
<td>Service Token</td>
<td><code>&lt;TOKEN-NAME&gt;</code></td>
</tr>
</tbody>
</table>
<h3 id="3-add-a-service-provider-integration"><ol start="3">
<li>Add a service provider integration</li>
</ol></h3>
<p>To create a custom service-to-service integration:</p>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Service providers</strong>.</p>
</li>
<li>
<p>Select <strong>Add new</strong>.</p>
</li>
<li>
<p>Select <strong>Custom service provider</strong>.</p>
</li>
<li>
<p>Enter any name for the provider. This name will be used throughout the dashboard to reference this connection.</p>
</li>
<li>
<p>In <strong>Access client ID</strong> and <strong>Access client secret</strong>, enter the Access service token used to authenticate to your external API.</p>
</li>
<li>
<p>In <strong>Rest API URL</strong>, enter the external API endpoint that Cloudflare will query for posture information (for example, <code>https://api.example.com</code>). For more information, refer to <a href="#external-api-requirements">External API requirements</a>.</p>
</li>
<li>
<p>In <strong>Polling frequency</strong>, choose how often Cloudflare One should query the external API for information.</p>
</li>
<li>
<p>Select <strong>Test and save</strong>. The test checks if Cloudflare can authenticate to the API URL using the provided Access credentials.</p>
</li>
</ol>
<p>Next, <a href="#4-configure-the-posture-check">configure a device posture check</a> to determine if a given posture score constitutes a pass or fail.</p>
<h3 id="4-configure-the-posture-check"><ol start="4">
<li>Configure the posture check</li>
</ol></h3>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Posture checks</strong> &gt; <strong>Service provider checks</strong>.</li>
<li>Select <strong>Add a check</strong>.</li>
<li>Select the Custom service provider provider.</li>
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
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Score</td>
<td>Posture score returned by external API</td>
<td><code>0</code> to <code>100</code></td>
</tr>
</tbody>
</table>
