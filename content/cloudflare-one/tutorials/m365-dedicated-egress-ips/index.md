<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4297.md")
</aside>
<p>This tutorial covers how to secure access to your Microsoft 365 applications with Cloudflare Gateway dedicated egress IPs.</p>
<p>You can map a named location in Microsoft Entra ID to a location associated with your dedicated egress IPs. Traffic will egress from Cloudflare with these IP addresses. If users attempt to access your Microsoft applications without these IPs, Entra ID will block access.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>Make sure you have:</p>
<ul>
<li>In Cloudflare, a Zero Trust Enterprise plan with <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/">dedicated egress IPs</a></li>
<li>In Microsoft 365, an organization managed with <a href="https://learn.microsoft.com/en-us/entra/identity/">Microsoft Entra ID</a></li>
</ul>
<h2 id="create-an-egress-policy-in-cloudflare-gateway">Create an egress policy in Cloudflare Gateway</h2>
<ol>
<li>
<p>In <a href="https://one.dash.cloudflare.com/">Cloudflare One</a>, go to <strong>Traffic policies</strong> &gt; <strong>Egress policies</strong>.</p>
</li>
<li>
<p>Select <strong>Add a policy</strong>.</p>
</li>
<li>
<p>Name your policy, then add conditions to check users are configured in Microsoft Entra ID. For example, you can check for <a href="/cloudflare-one/traffic-policies/identity-selectors/">identity conditions</a>:</p>
</li>
</ol>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>User Group Names</td>
<td>in</td>
<td><code>Sales and Marketing</code>, <code>Retail</code>, <code>U.S. Sales</code></td>
</tr>
</tbody>
</table>
<p>Additionally, you can check for <a href="/cloudflare-one/reusable-components/posture-checks/">device posture conditions</a>:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Operator</th>
<th>Value</th>
<th>Logic</th>
</tr>
</thead>
<tbody>
<tr>
<td>Passed Device Posture Check</td>
<td>is</td>
<td><code>CrowdStrike Overall ZTA score (Crowdstrike s2s)</code></td>
<td>And</td>
</tr>
<tr>
<td>Passed Device Posture Check</td>
<td>is</td>
<td><code>AppCheckMac - Required Software (Application)</code></td>
<td></td>
</tr>
</tbody>
</table>
<ol start="4">
<li>Enable <strong>Use dedicated Cloudflare egress IPs</strong>. Select your desired IPv4 and IPv6 addresses. For example:</li>
</ol>
<table>
<thead>
<tr>
<th>Primary IPv4 address</th>
<th>IPv6 address</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>203.0.113.0</code></td>
<td><code>2001:db8::/32</code></td>
</tr>
</tbody>
</table>
<h2 id="create-a-named-ip-range-location-in-microsoft-entra-id">Create a named IP range location in Microsoft Entra ID</h2>
<ol>
<li>Log in to the <a href="https://aka.ms/azureportal">Microsoft Azure portal</a>.</li>
<li>In the sidebar, select <strong>Microsoft Entra ID</strong>.</li>
<li>Go to <strong>Security</strong> &gt; <strong>Named locations</strong>.</li>
<li>Select <strong>IP ranges location</strong>.</li>
<li>Name your location, then add the IP addresses used in your Cloudflare dedicated egress IP policy.</li>
<li>Select <strong>Upload</strong>.</li>
</ol>
<p>This named location corresponds with the locations of your dedicated egress IPs.</p>
<h2 id="create-a-conditional-access-policy-in-microsoft-entra-id">Create a conditional access policy in Microsoft Entra ID</h2>
<ol>
<li>In <strong>Protect</strong>, go to <strong>Conditional Access</strong>.</li>
<li>Select <strong>Create new policy</strong>.</li>
<li>Configure which Entra ID users you want to limit access for, and which traffic, applications, or actions you want to protect.</li>
<li>In <strong>Conditions</strong>, select <strong>Locations</strong>. Enable <strong>Configure</strong>.</li>
<li>In <strong>Include</strong>, select <em>Any location</em>. In <strong>Exclude</strong>, select the named location you created.</li>
<li>In <strong>Access controls</strong>, go to <strong>Grant</strong>. Enable <em>Block access</em>.</li>
</ol>
<p>Your policy will block access for your selected users from any location except those using your dedicated egress IPs.</p>
<h2 id="test-your-policies">Test your policies</h2>
<ol>
<li>Using <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a>, sign in to your Zero Trust organization with a user's account.</li>
<li>Go to any Microsoft 365 app within your organization. Entra ID should allow access.</li>
<li>Disconnect the Cloudflare One Client from your Zero Trust organization. Entra ID should block access to any Microsoft 365 applications.</li>
</ol>
