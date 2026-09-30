<p>Network Flow (formerly Magic Network Monitoring) rules monitor your network traffic for Distributed Denial of Service (DDoS) attacks targeting specific IP addresses or prefixes. When traffic exceeds a rule's threshold or matches a known DDoS attack fingerprint, you receive an alert.</p>
<h2 id="rule-types">Rule types</h2>
<p>Network Flow supports three rule types:</p>
<table>
<thead>
<tr>
<th align="left">Rule Type</th>
<th align="left">Description</th>
<th align="left">Availability</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><a href="/network-flow/rules/dynamic-threshold/">Dynamic threshold</a> (recommended)</td>
<td align="left">Analyzes your network's traffic patterns over time and automatically adjusts the DDoS threshold (bits or packets) based on traffic history.</td>
<td align="left">API only</td>
</tr>
<tr>
<td align="left"><a href="/network-flow/rules/static-threshold/">Static threshold</a></td>
<td align="left">You define a fixed threshold (bits or packets) for DDoS traffic monitoring.</td>
<td align="left">API and dashboard</td>
</tr>
<tr>
<td align="left"><a href="/network-flow/rules/s-flow-ddos-attack/">sFlow DDoS attack</a></td>
<td align="left">If you send sFlow data to Cloudflare, you can receive alerts when a specific DDoS attack type is detected in your traffic.</td>
<td align="left">API only (sFlow data only)</td>
</tr>
</tbody>
</table>
<h2 id="create-rules-in-the-dashboard">Create rules in the dashboard</h2>
<p>You can only configure static traffic threshold rules in the Cloudflare dashboard.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="invalid-account-settings-error-when-trying-to-create-a-rule">Invalid account settings error when trying to create a rule</h3>
@markup("md", "content/.markup/bodies/10802.md")
</aside>
<p>To create a new rule:</p>
<ol>
<li>Go to the <strong>Network flow</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Configure Network flow</strong>.</li>
<li>In the <strong>Configure rules</strong> tab, select <strong>Add new rule</strong>.</li>
<li>Fill in the rule fields. For details on each field, refer to <a href="/network-flow/rules/static-threshold/">Static threshold rules</a>.</li>
<li>Select <strong>Create a new rule</strong> when you are finished.</li>
</ol>
<h2 id="edit-rules-in-the-dashboard">Edit rules in the dashboard</h2>
<ol>
<li>Go to the <strong>Network flow</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Configure Network flow</strong>.</li>
<li>In the <strong>Configure rules</strong> tab, find the static threshold rule you want to edit, and select <strong>Edit</strong>.</li>
<li>Edit the appropriate fields. Refer to <a href="/network-flow/rules/static-threshold/#rule-configuration-fields">Rule configuration fields</a> for more information on what each field does.</li>
<li>Select <strong>Save</strong> when you are finished.</li>
</ol>
<h2 id="delete-rules-in-the-dashboard">Delete rules in the dashboard</h2>
<ol>
<li>Go to the <strong>Network flow</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Configure Network flow</strong>.</li>
<li>In the <strong>Configure rules</strong> tab, find the static threshold rule you want to delete, and select <strong>Delete</strong>.</li>
<li>Select <strong>I understand that deleting a rule is permanent</strong>, and select <strong>Delete</strong> again.</li>
</ol>
<h2 id="common-settings-that-apply-to-all-rule-types">Common settings that apply to all rule types</h2>
<h3 id="rule-auto-advertisement">Rule Auto-Advertisement</h3>
<p>Auto-Advertisement automatically activates <a href="/magic-transit/">Magic Transit</a> when a rule triggers, routing your traffic through Cloudflare for DDoS mitigation without manual intervention.</p>
<p>This feature is available to Enterprise customers using <a href="/magic-transit/on-demand">Magic Transit On Demand</a>. You can enable it for any dynamic threshold, static threshold, or sFlow DDoS attack rule.</p>
<p>Follow the previous steps to <a href="#create-rules-in-the-dashboard">create</a> or <a href="#edit-rules-in-the-dashboard">edit</a> a rule. Then, enable <strong>Auto-Advertisement</strong>.</p>
<h4 id="rule-auto-advertisement-notifications">Rule Auto-Advertisement notifications</h4>
<p>Webhook, PagerDuty, and email notifications are sent following an auto-advertisement attempt for all prefixes inside the flagged rule.</p>
<p>You will receive the status of the advertisement for each prefix with the following available statuses:</p>
<ul>
<li><strong>Advertised</strong>: The prefix was successfully advertised.</li>
<li><strong>Already Advertised</strong>: The prefix was advertised prior to the auto advertisement attempt.</li>
<li><strong>Delayed</strong>: The prefix cannot currently be advertised but will attempt advertisement. After the prefix can be advertised, a new notification is sent with the updated status.</li>
<li><strong>Locked</strong>: The prefix is locked and cannot be advertised.</li>
<li><strong>Could not Advertise</strong>: Cloudflare was unable to advertise the prefix. This status can occur for multiple reasons, but usually occurs when you are not allowed to advertise a prefix.</li>
<li><strong>Error</strong>: A general error occurred during prefix advertisement.</li>
</ul>
<h3 id="rule-ip-prefixes">Rule IP prefixes</h3>
<p>Each rule must include one or more IP prefixes. All prefixes in a rule are evaluated as aggregate traffic — their combined volume is measured against the threshold.</p>
<ul>
<li>To alert on the <strong>combined</strong> traffic of multiple prefixes, add them to the same rule.</li>
<li>To alert on <strong>individual</strong> prefix traffic, create a separate rule for each prefix.</li>
</ul>
<h4 id="rule-ip-prefixes-example">Rule IP prefixes example</h4>
<p>In the following example, the rule triggers when the <strong>combined</strong> packet traffic of <code>192.168.0.0/24</code> and <code>172.118.0.0/24</code> exceeds <code>10000</code> packets. If Auto-Advertisement is enabled, Cloudflare advertises both prefixes when the rule triggers.</p>
<p>You can also <a href="/api/resources/magic_network_monitoring/subresources/rules/">configure rule IP prefixes at scale using the API</a>.</p>
<pre><code class="language-json">{&#10;	&quot;rules&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;Too many packets&quot;,&#10;			&quot;prefixes&quot;: [&quot;192.168.0.0/24&quot;, &quot;172.118.0.0/24&quot;],&#10;			&quot;packet_threshold&quot;: 10000,&#10;			&quot;automatic_advertisement&quot;: true,&#10;			&quot;duration&quot;: &quot;1m0s&quot;,&#10;			&quot;type&quot;: &quot;threshold&quot;&#10;		}&#10;	]&#10;}&#10;</code></pre>
<p>To set a threshold for a single prefix, create a separate rule:</p>
<pre><code class="language-json">{&#10;	&quot;rules&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;Too many packets&quot;,&#10;			&quot;prefixes&quot;: [&quot;172.118.0.0/24&quot;],&#10;			&quot;packet_threshold&quot;: 1000,&#10;			&quot;automatic_advertisement&quot;: true,&#10;			&quot;duration&quot;: &quot;1m0s&quot;,&#10;			&quot;type&quot;: &quot;threshold&quot;&#10;		}&#10;	]&#10;}&#10;</code></pre>
