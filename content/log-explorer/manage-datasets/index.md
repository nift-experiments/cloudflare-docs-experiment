<p>Log Explorer allows you to enable, disable, or delete datasets available to query in Log Search.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/822.md")
</aside>
<h2 id="supported-datasets">Supported datasets</h2>
<p>Log Explorer currently supports the following datasets:</p>
<h3 id="zone-level">Zone level</h3>
<ul>
<li><a href="/logs/logpush/logpush-job/datasets/zone/http_requests/">HTTP Requests</a> (<code>http_requests</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/zone/firewall_events/">Firewall Events</a> (<code>firewall_events</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/zone/dns_logs/">DNS Logs</a> (<code>dns_logs</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/zone/nel_reports/">NEL Reports</a> (<code>nel_reports</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/zone/page_shield_events/">Page Shield Events</a> (<code>page_shield_events</code>) (events for client-side security)</li>
<li><a href="/logs/logpush/logpush-job/datasets/zone/spectrum_events/">Spectrum Events</a> (<code>spectrum_events</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/zone/zaraz_events/">Zaraz Events</a> (<code>zaraz_events</code>)</li>
</ul>
<h3 id="account-level">Account level</h3>
<ul>
<li><a href="/logs/logpush/logpush-job/datasets/account/access_requests/">Access requests</a> (<code>access_requests</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/casb_findings/">CASB findings</a> (<code>casb_findings</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/device_posture_results/">Device posture results</a> (<code>device_posture_results</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/gateway_dns/">Gateway DNS</a> (<code>gateway_dns</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/gateway_http/">Gateway HTTP</a> (<code>gateway_http</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/gateway_network/">Gateway Network</a> (<code>gateway_network</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/zero_trust_network_sessions/">Zero Trust Network Session Logs</a> (<code>zero_trust_network_sessions</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/audit_logs/">Audit Logs</a> (<code>audit_logs</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/audit_logs_v2/">Audit_logs_v2</a> (<code>audit_logs_v2</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/biso_user_actions/">Browser Isolation User Actions</a> (<code>biso_user_actions</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/dns_firewall_logs/">DNS firewall logs</a> (<code>dns_firewall_logs</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/email_security_alerts/">Email security alerts</a> (<code>email_security_alerts</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/magic_bgp_logs/">Magic BGP Logs</a> (<code>magic_bgp_logs</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/magic_ids_detections/">Magic IDS Detections</a> (<code>magic_ids_detections</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/network_analytics_logs/">Network Analytics</a> (<code>network_analytics_logs</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/sinkhole_http_logs/">Sinkhole HTTP Logs</a> (<code>sinkhole_http_logs</code>)</li>
<li><a href="/logs/logpush/logpush-job/datasets/account/ipsec_logs/">IP Sec Logs</a> (<code>ipsec_logs</code>)</li>
</ul>
<h2 id="enable-log-explorer">Enable Log Explorer</h2>
<p>To begin storing logs, enable the desired datasets through the dashboard or API.</p>
<h3 id="dashboard">Dashboard</h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/823.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/821.md")
</aside>
<h4 id="configure-fields-and-filters">Configure fields and filters</h4>
<p>Use <strong>Select fields</strong> to control which data points Log Explorer stores. Fields are grouped by category, and each category shows its selected field count. Select a category to add or remove all fields in that group, or expand the category to select individual fields. Each field shows its data type.</p>
<p>Required fields remain selected and are marked <strong>Required</strong>. Fields that Cloudflare no longer recommends are marked <strong>Deprecated</strong>. Select <strong>Select all</strong> to include every available field, or <strong>Reset to default</strong> to restore the dataset defaults.</p>
<p>Use <strong>Filter logs</strong> to ingest <strong>All events</strong> or <strong>Only events matching a filter</strong>. A filter condition consists of a field, an operator, and a value. All conditions within a group must match. An event can match any filter group.</p>
<p>To change the fields or filter for an enabled dataset, go to <strong>Log Explorer</strong> &gt; <strong>Manage datasets</strong>. Find the dataset, select <strong>Actions</strong> &gt; <strong>Edit</strong>, update the configuration, and select <strong>Update</strong>.</p>
<h3 id="api">API</h3>
<p>Use the Log Explorer API to enable each dataset you want to store. It may take a few minutes after a log stream is enabled before you can view the logs.</p>
<p>The following <code>curl</code> command is an example for enabling the zone-level dataset <code>http_requests</code>, as well as the expected response when the command succeeds.</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/zones/{zone_id}/logs/explorer/datasets \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-json &#x27;{&#10;  &quot;dataset&quot;: &quot;http_requests&quot;&#10;}&#x27;&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: {&#10;		&quot;dataset&quot;: &quot;http_requests&quot;,&#10;		&quot;object_type&quot;: &quot;zone&quot;,&#10;		&quot;object_id&quot;: &quot;&lt;ZONE ID&gt;&quot;,&#10;		&quot;created_at&quot;: &quot;2025-06-03T14:33:16Z&quot;,&#10;		&quot;updated_at&quot;: &quot;2025-06-03T14:33:16Z&quot;,&#10;		&quot;dataset_id&quot;: &quot;01973635f7e273a1964a02f4d4502499&quot;,&#10;		&quot;enabled&quot;: true,&#10;		&quot;deletion_protection&quot;: true&#10;	},&#10;	&quot;success&quot;: true,&#10;	&quot;errors&quot;: [],&#10;	&quot;messages&quot;: []&#10;}&#10;</code></pre>
<p>To enable an account-level dataset, replace <code>zones/{zone_id}</code> with <code>accounts/{account_id}</code> in the <code>curl</code> command. For example:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{account_id}/logs/explorer/datasets \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-json &#x27;{&#10;  &quot;dataset&quot;: &quot;access_requests&quot;&#10;}&#x27;&#10;</code></pre>
<h2 id="delete-a-dataset">Delete a dataset</h2>
<p>Deleting a dataset permanently removes the dataset and its stored data. Deletion runs asynchronously. You cannot recreate the same dataset for the account or zone while deletion is in progress.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/820.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/826.md")
</div></div>
