<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5908.md")
</aside>
<p>Cloudflare Access can use endpoint data from <a href="https://www.tanium.com/">Tanium™</a> to determine if a request should be allowed to reach a protected resource. When users attempt to connect to a resource protected by Access with a Tanium rule, Cloudflare Access will validate the user's identity, and the browser will connect to the Tanium agent before making a decision to grant access.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="gateway-policy-limitation">Gateway policy limitation</h3>
@markup("md", "content/.markup/bodies/5907.md")
</aside>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Tanium Core Platform version 7.2 or later</li>
<li></li>
</ul>
<p>Cloudflare One Client is <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/">deployed</a> on the device. For a list of supported modes and operating systems, refer to <a href="/cloudflare-one/reusable-components/posture-checks/access-integrations/">Access integrations</a>.</p>
<h2 id="integrate-tanium-with-cloudflare-access">Integrate Tanium with Cloudflare Access</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5906.md")
</aside>
<ol>
<li>
<p>Configure your Tanium deployment using the <a href="https://docs.tanium.com/endpoint_identity/endpoint_identity/userguide.html">step-by-step documentation</a> provided. You will need the public key to integrate your Tanium deployment with Cloudflare Access.</p>
</li>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Reusable components</strong> &gt; <strong>Posture checks</strong>.</p>
</li>
<li>
<p>Go to <strong>Cloudflare One Client checks</strong> and select <strong>Add a check</strong>.</p>
</li>
<li>
<p>Select <strong>Tanium</strong> from the list of providers.</p>
</li>
<li>
<p>Enter any <strong>Name</strong> for the integration.</p>
</li>
<li>
<p>For <strong>Port</strong>, enter <code>17472</code>.</p>
<p>This is the default port used by the Tanium endpoints to communicate inbound and outbound with Cloudflare Access. You may need to modify it to reflect your organization's deployment.</p>
</li>
<li>
<p>Input the public certificate generated in Step 1.</p>
<p>Adding the certificate allows Cloudflare to validate that the response from the Tanium agent is valid.</p>
</li>
</ol>
<p>You can now build <a href="/cloudflare-one/access-controls/policies/">Access policies</a> that check <a href="#tanium-endpoint-signals">device posture signals</a> from the Tanium endpoint.</p>
<h2 id="example-access-policy">Example Access policy</h2>
<p>This example will only grant access to users who are part of your team's email domain and running the Tanium agent.</p>
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
<td>Allow</td>
<td>Include</td>
<td>Emails Ending in</td>
<td><code>@team.com</code></td>
</tr>
<tr>
<td></td>
<td>Require</td>
<td>Device Posture - Tanium</td>
<td><code>Managed</code></td>
</tr>
</tbody>
</table>
<p>The Tanium rule will require that the device connecting is managed in your Tanium deployment and has checked into the Tanium server in the last 7 days.</p>
<h2 id="tanium-endpoint-signals">Tanium endpoint signals</h2>
<table>
<thead>
<tr>
<th>Signal</th>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Managed</td>
<td>Boolean</td>
<td>Validates that the device is managed in your organization's Tanium account.</td>
</tr>
</tbody>
</table>
