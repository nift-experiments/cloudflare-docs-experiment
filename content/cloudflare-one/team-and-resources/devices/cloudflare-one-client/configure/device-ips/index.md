<details class="nb-details"><summary>Feature availability</summary><div class="nb-details-body">
@input("content/.markup/bodies/6191.md")
</div></details>
<p>A device IP identifies and routes traffic to a specific device in your Zero Trust organization. When a user registers the Cloudflare One Client (formerly WARP), Cloudflare assigns a virtual IPv4 and IPv6 address to the <a href="/cloudflare-one/team-and-resources/devices/device-registration/">device registration</a>. The Cloudflare One Client uses these IP addresses to create a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/client-architecture/#ip-traffic">virtual network interface</a> on the device, which allows your private network to reach the device via <a href="/mesh/">Cloudflare Mesh</a> or <a href="/cloudflare-one/networks/connectors/cloudflare-wan/">Cloudflare WAN</a> on-ramps.</p>
<p>You can verify device IPs and, if needed, reconfigure address pools to avoid overlapping IPs with existing internal resources.</p>
<h2 id="default-device-ips">Default device IPs</h2>
<p>By default, Cloudflare assigns device IPs from the following address space:</p>
<ul>
<li>Default IPv4: <code>100.96.0.0/12</code></li>
<li>Default IPv6: <code>2606:4700:0cf1:1000::/64</code></li>
</ul>
<p>If your organization already uses the default IPv4 range for internal networking, or if you require more granular IP assignments for firewall policy management, you can configure custom device IPv4 subnets. You can assign different IPv4 subnets to devices based on the user's identity.</p>
<p>The default IPv6 range is owned by Cloudflare and therefore should not conflict with services on your private network. The device IPv6 range is not configurable.</p>
<h2 id="create-an-ip-subnet">Create an IP subnet</h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6190.md")
</aside>
<p>Create a custom IP subnet when the <a href="#default-device-ips">default IPv4 range</a> conflicts with services on your private network.</p>
<p>To define a custom IPv4 subnet for device IPs:</p>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Device profiles</strong>.</p>
</li>
<li>
<p>Under <strong>Device IP subnets</strong>, select <strong>Add new IP subnet</strong>.</p>
</li>
<li>
<p>Enter any name for the subnet.</p>
</li>
<li>
<p>In <strong>CIDR</strong>, enter a valid IPv4 CIDR block from the supported private ranges:</p>
<ul>
<li><code>10.0.0.0/8</code></li>
<li><code>172.16.0.0/12</code></li>
<li><code>192.168.0.0/16</code></li>
<li><code>100.64.0.0/10</code></li>
</ul>
<p>The configured CIDR block must be at least size <code>/24</code>.</p>
</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="avoid-ip-conflicts">Avoid IP conflicts</h3>
@markup("md", "content/.markup/bodies/6189.md")
</aside>
<ol start="5">
<li>Select <strong>Add subnet</strong> to save.</li>
</ol>
<p>Next, <a href="#assign-device-ips">assign this subnet</a> to a group of devices.</p>
<h2 id="assign-device-ips">Assign device IPs</h2>
<p>Assign <a href="#create-an-ip-subnet">custom IP subnets</a> to ensure devices are provisioned within a predictable address space based on specific user identity criteria.</p>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#assign-a-unique-ip-address-to-each-device"><strong>Assign a unique IP address to each device</strong></a> is enabled in your <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">general device profiles</a>.</li>
</ul>
<h3 id="create-an-ip-profile">Create an IP profile</h3>
<p>To assign IP subnets to your devices:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Device profiles</strong>.</li>
<li>Under <strong>Device IP profiles</strong>, select <strong>Add new IP profile</strong>.</li>
<li>Enter a name for this group of devices (for example, <code>IT department</code>).</li>
<li>Create rules to define the users or devices that will receive these IPs. Learn more about the available <a href="#selectors">Selectors</a>, <a href="#comparison-operators">Operators</a>, and <a href="#value">Values</a>.</li>
<li>Choose an existing IPv4 subnet from the dropdown menu, or <a href="#create-an-ipv4-subnet">create a new subnet</a>.</li>
<li>Select <strong>Assign IP address</strong>.</li>
<li>(Optional) In the <strong>Device IP profiles</strong> table, change the <a href="#order-of-precedence">order of precedence</a> of IP profiles.</li>
</ol>
<p>Devices that match your rules are assigned a random IP from this address space upon registration. Only newly registered devices will receive a new IP; existing devices will not see any impact to connectivity. To assign a new IP to an existing device, you must <a href="/cloudflare-one/team-and-resources/devices/device-registration/#delete-a-device-registration">delete its registration</a> and then <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/">re-enroll the device</a> in your Zero Trust organization.</p>
<p>Organizations are currently <a href="/cloudflare-one/account-limits/#warp">limited</a> to 30 custom device IP profiles per account.</p>
<h3 id="selectors">Selectors</h3>
<p>You can configure IP profiles to match against the following selectors or criteria. Identity-based selectors are only available if the user <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/">enrolled the device</a> by logging in to an identity provider (IdP).</p>
<h4 id="user-email">User email</h4>
<p>Apply a device profile based on the user's email.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example value</th>
</tr>
</thead>
<tbody>
<tr>
<td>User email</td>
<td><code>identity.email == &quot;user-name@company.com&quot;</code></td>
</tr>
</tbody>
</table>
<h4 id="user-group-emails">User group emails</h4>
<p>Apply a device IP profile based on an <a href="/cloudflare-one/traffic-policies/identity-selectors/#idp-groups-in-gateway">IdP group</a> email address of which the user is configured as a member in the IdP.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>User group emails</td>
<td><code>identity.groups.email == &quot;contractors@company.com&quot;</code></td>
</tr>
</tbody>
</table>
<h4 id="user-group-ids">User group IDs</h4>
<p>Apply a device IP profile based on an <a href="/cloudflare-one/traffic-policies/identity-selectors/#idp-groups-in-gateway">IdP group</a> ID of which the user is configured as a member in the IdP.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>User group IDs</td>
<td><code>identity.groups.id == &quot;12jf495bhjd7893ml09o&quot;</code></td>
</tr>
</tbody>
</table>
<h4 id="user-group-names">User group names</h4>
<p>Apply a device IP profile based on an <a href="/cloudflare-one/traffic-policies/identity-selectors/#idp-groups-in-gateway">IdP group</a> name of which the user is configured as a member in the IdP.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>User group names</td>
<td><code>identity.groups.name == &quot;\&quot;finance\&quot;&quot;</code></td>
</tr>
</tbody>
</table>
<h4 id="user-name">User name</h4>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>User Name</td>
<td><code>identity.name == &quot;user-name&quot;</code></td>
</tr>
</tbody>
</table>
<h4 id="saml-attributes">SAML attributes</h4>
<p>Apply a device IP profile based on an attribute name and value from a <a href="/cloudflare-one/traffic-policies/identity-selectors/#generic-saml-idp">SAML IdP</a>.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>SAML Attributes</td>
<td><code>identity.saml_attributes == &quot;\&quot;group=finance\&quot;&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="comparison-operators">Comparison operators</h3>
<p>Comparison operators determine how device IP profiles match a selector.</p>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>in</td>
<td>matches at least one of the defined values</td>
</tr>
<tr>
<td>not in</td>
<td>does not match any of the defined values</td>
</tr>
<tr>
<td>is</td>
<td>equals the defined value</td>
</tr>
<tr>
<td>matches</td>
<td>regular expression (regex) evaluates to true</td>
</tr>
</tbody>
</table>
<h3 id="value">Value</h3>
<p>In the <strong>Value</strong> field, you can input a single value when using an equality comparison operator (such as <em>is</em>) or multiple values when using a containment comparison operator (such as <em>in</em>). Additionally, you can use <a href="#regular-expressions">regular expressions</a> (or regex) to specify a range of values for supported selectors.</p>
<h3 id="regular-expressions">Regular expressions</h3>
<p>Regular expressions are evaluated using Rust. The Rust implementation is slightly different than regex libraries used elsewhere. For more information, refer to our guide for <a href="/cloudflare-one/access-controls/policies/app-paths/#wildcards">Wildcards</a>. To evaluate if your regex matches, you can use <a href="https://rustexp.lpil.uk/">Rustexp</a>.</p>
<p>If you want to match multiple values, you can use the pipe symbol (<code>|</code>) as an OR operator. You do not need to use an escape character (<code>\</code>) before the pipe symbol. For example, the following expression evaluates to true when the user's email domain matches either <code>@acme.com</code> or <code>@widgets.com</code>:</p>
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
<td>User email</td>
<td>matches</td>
<td><code>@acme.com|@widgets.com</code></td>
</tr>
</tbody>
</table>
<p>In addition to regular expressions, you can use <a href="#logical-operators">logical operators</a> to match multiple values.</p>
<h3 id="logical-operators">Logical operators</h3>
<p>To evaluate multiple conditions in an expression, select a logical operator:</p>
<table>
<thead>
<tr>
<th>Operator</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>And</td>
<td>match all of the conditions in the expression</td>
</tr>
<tr>
<td>Or</td>
<td>match any of the conditions in the expression</td>
</tr>
</tbody>
</table>
<h3 id="order-of-precedence">Order of precedence</h3>
<p>The Cloudflare One Client checks the IP profiles from top to bottom as they appear in the Cloudflare One dashboard (lowest precedence number is checked first). The client follows the first match principle — once a device matches an IP profile, the client stops evaluating and no subsequent IP profiles can override the decision. You can rearrange the IP profiles in the Cloudflare One dashboard according to your desired order of precedence.</p>
<h2 id="verify-device-ips">Verify device IPs</h2>
<h3 id="via-the-dashboard">Via the dashboard</h3>
<p>To check the virtual IP addresses assigned to a specific device registration:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong>.</li>
<li>Select your device &gt; <strong>View details</strong>.</li>
</ol>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="device-filters">Device filters</h3>
@markup("md", "content/.markup/bodies/6188.md")
</aside>
3. Scroll down to **Users**. You will see the registrations associated with this device along with their assigned IPv4 and IPv6 addresses.
<h3 id="via-the-cli">Via the CLI</h3>
<p>To check the device IP used by the device client's virtual network interface:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6195.md")
</div></div>
<p>In the example above, the device IPv4 address is <code>172.16.0.2</code>.</p>
<h2 id="view-subnet-usage">View subnet usage</h2>
<p>Monitor the consumption of your IPv4 subnets to ensure you have enough addresses for new device registrations. Devices will be unable to register if they match a subnet with no available IPs.</p>
<p>Use the Cloudflare One dashboard to view a high-level overview of assigned and available IPs:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Device profiles</strong>.</li>
<li>Locate the <strong>Device IP subnets</strong> table.</li>
<li>The <strong>IPs assigned</strong> column displays the total number of IPs currently assigned to active device registrations versus the total capacity of the CIDR block.</li>
</ol>
<p>If your subnet is approaching capacity, you can <a href="#edit-an-ip-subnet">expand your subnet</a> to increase the number of available IPs. Alternatively, you can free up IPs by <a href="/cloudflare-one/team-and-resources/devices/device-registration/#delete-a-device-registration">deleting existing device registrations</a>, particularly revoked registrations that may be consuming IP space despite the device no longer being in use.</p>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="delete-device-registrations-instead-of-revoking">Delete device registrations instead of revoking</h3>
@markup("md", "content/.markup/bodies/6187.md")
</aside>
<p>To get a list of all device registrations in a subnet (including revoked registrations), use the <a href="/api/resources/zero_trust/subresources/devices/subresources/registrations/methods/list/">Cloudflare API</a>. For example, the following script fetches all device registrations and their device IPs, and outputs all registrations within the specified CIDR block.</p>
<details class="nb-details"><summary>Example script to filter registrations by IP</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6196.md")
</div></details>
<h2 id="edit-an-ip-subnet">Edit an IP subnet</h2>
<p>Cloudflare does not support editing an existing IPv4 subnet definition. To assign a different IPv4 subnet to your devices:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Team &amp; Resources</strong> &gt; <strong>Devices</strong> &gt; <strong>Device profiles</strong>.</li>
<li>Under <strong>Device IP profiles</strong>, find the device group associated with the old subnet and select <strong>Edit</strong>.</li>
<li>Select <strong>Create new subnet IP range</strong> to define a new subnet.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>The new subnet will appear in the <strong>Device IP subnets</strong> table. You can now delete the old subnet. Devices will only get an IP from the new subnet when they <a href="/cloudflare-one/team-and-resources/devices/device-registration/#delete-a-device-registration">re-register</a>; existing registrations will retain their <a href="#verify-device-ips">current IP</a>.</p>
