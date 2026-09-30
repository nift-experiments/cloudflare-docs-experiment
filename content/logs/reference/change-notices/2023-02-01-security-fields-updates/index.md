<p>Cloudflare will deploy some updates to security-related fields in Cloudflare Logs. These updates will affect the following datasets:</p>
<ul>
<li><a href="/logs/logpush/logpush-job/datasets/zone/http_requests/">HTTP Requests</a></li>
<li><a href="/logs/logpush/logpush-job/datasets/zone/firewall_events/">Firewall Events</a></li>
</ul>
<h2 id="timeline">Timeline</h2>
<p>To minimize possible impacts on our customers' existing <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/10577.md")
</div> configurations, these updates will happen in two phases according to the following timeline:
<h3 id="phase-1-february-1-2023">Phase 1 (February 1, 2023)</h3>
<p>For the log fields being added, Cloudflare will gradually start adding them to logs datasets.</p>
<p>For the log fields being renamed, Cloudflare will:</p>
<ul>
<li><strong>Add new fields</strong> with the same data as the fields that will be removed on phase 2 (described in this document as old fields). These new fields will become gradually available. Refer to the next sections for details.</li>
<li><strong>Announce the deprecation of the old fields.</strong> Cloudflare will remove these fields from logs datasets on August 1, 2023.</li>
</ul>
<p>For the log fields being removed, Cloudflare is announcing them as deprecated. Their removal from logs datasets will occur on August 1, 2023.</p>
<p>In addition to these Cloudflare Logs changes, Cloudflare will also add new security-related fields to the following <a href="/analytics/graphql-api/features/data-sets/">GraphQL datasets</a>:</p>
<ul>
<li><code>httpRequestsAdaptive </code></li>
<li><code>httpRequestsAdaptiveGroups</code></li>
<li><code>firewallEventsAdaptive</code></li>
<li><code>firewallEventsAdaptiveGroups</code></li>
<li><code>firewallEventsAdaptiveByTimeGroups</code></li>
</ul>
<h3 id="phase-2-august-1-2023">Phase 2 (August 1, 2023)</h3>
<p>For the log fields being renamed, Cloudflare will remove the old fields from the Cloudflare logs datasets. From August 1, 2023 onwards, only the new fields will be available.</p>
<p>For the log fields being removed, Cloudflare will also remove them from the Cloudflare logs datasets. From August 1, 2023 onwards, these fields will no longer be available.</p>
<h2 id="concepts">Concepts</h2>
<p>The following concepts are used below in the reviewed field descriptions:</p>
<ul>
<li>
<p><strong>Terminating action:</strong> One of the following actions:</p>
<ul>
<li><code>block</code></li>
<li><code>js_challenge</code></li>
<li><code>managed_challenge</code></li>
<li><code>challenge</code> (<em>Interactive Challenge</em>)</li>
</ul>
</li>
</ul>
<p>For more information on these actions, refer to the <a href="/ruleset-engine/rules-language/actions/">Actions</a> reference in the Rules language documentation.</p>
<ul>
<li>
<p><strong>Security rule:</strong> One of the following rule types:</p>
<ul>
<li><a href="/waf/managed-rules/">WAF managed rule</a></li>
<li><a href="/waf/custom-rules/">WAF custom rule</a></li>
<li><a href="/waf/rate-limiting-rules/">WAF rate limiting rule</a></li>
</ul>
</li>
</ul>
<h2 id="http-requests-dataset-changes">HTTP Requests dataset changes</h2>
<p>The following fields will be renamed in the <a href="/logs/logpush/logpush-job/datasets/zone/http_requests/">HTTP Requests</a> dataset according to the two-phase strategy outlined in the <a href="#timeline">timeline</a>:</p>
<table>
<thead>
<tr>
<th>New field name</th>
<th>Type</th>
<th>Description</th>
<th>Old field name<br/>(deprecated on Aug 1, 2023)</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>SecurityRuleID</code></td>
<td>String</td>
<td>Rule ID of the security rule that triggered a terminating action, if any.</td>
<td><code>WAFRuleID</code></td>
</tr>
<tr>
<td><code>SecurityRuleDescription</code></td>
<td>String</td>
<td>Rule description of the security rule that triggered a terminating action, if any.</td>
<td><code>WAFRuleMessage</code></td>
</tr>
<tr>
<td><code>SecurityAction</code></td>
<td>String</td>
<td>Rule action of the security rule that triggered a terminating action, if any.</td>
<td><code>WAFAction</code></td>
</tr>
<tr>
<td><code>SecurityRuleIDs</code></td>
<td>String Array</td>
<td>Array of security rule IDs that matched the request.</td>
<td><code>FirewallMatchesRuleIDs</code></td>
</tr>
<tr>
<td><code>SecurityActions</code></td>
<td>String Array</td>
<td>Array of actions that Cloudflare security products performed on the request.</td>
<td><code>FirewallMatchesActions</code></td>
</tr>
<tr>
<td><code>SecuritySources</code></td>
<td>String Array</td>
<td>Array of Cloudflare security products that matched the request.</td>
<td><code>FirewallMatchesSources</code></td>
</tr>
</tbody>
</table>
<p>The following fields are now deprecated and they will be removed from the HTTP Requests dataset on August 1, 2023:</p>
<table>
<thead>
<tr>
<th>Deprecated field name</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>WAFProfile</code></td>
<td>Used in the previous version of WAF managed rules (now deprecated).</td>
</tr>
<tr>
<td><code>EdgeRateLimitAction</code></td>
<td>Used in the previous version of rate limiting rules (now deprecated).</td>
</tr>
<tr>
<td><code>EdgeRateLimitID</code></td>
<td>Used in the previous version of rate limiting rules (now deprecated).</td>
</tr>
<tr>
<td><code>SecurityLevel</code></td>
<td>N/A</td>
</tr>
</tbody>
</table>
<h2 id="firewall-events-dataset-changes">Firewall Events dataset changes</h2>
<p>The following fields will be added to the <a href="/logs/logpush/logpush-job/datasets/zone/firewall_events/">Firewall Events</a> dataset:</p>
<table>
<thead>
<tr>
<th>Field name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Description</code></td>
<td>String</td>
<td>The description of the rule triggered by the request.</td>
</tr>
<tr>
<td><code>Ref</code></td>
<td>String</td>
<td>The user-defined identifier for the rule triggered by the request.</td>
</tr>
</tbody>
</table>
<h2 id="changes-to-graphql-datasets">Changes to GraphQL datasets</h2>
<p>Cloudflare will add the following fields to the <code>httpRequestsAdaptive </code>and <code>httpRequestsAdaptiveGroups </code>datasets:</p>
<table>
<thead>
<tr>
<th>Field name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>securityAction</code></td>
<td>String</td>
<td>Action of the security rule that triggered a terminating action, if any.</td>
</tr>
<tr>
<td><code>securitySource</code></td>
<td>String</td>
<td>Source of the security rule that triggered a terminating action, if any.</td>
</tr>
</tbody>
</table>
<p>Cloudflare will also add the following field to the <code>firewallEventsAdaptive</code>, <code>firewallEventsAdaptiveGroups</code>, and <code>firewallEventsAdaptiveByTimeGroups</code> datasets:</p>
<table>
<thead>
<tr>
<th>Field name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>description</code></td>
<td>String</td>
<td>The description of the rule triggered by the request.</td>
</tr>
</tbody>
</table>
<p>These new fields will become gradually available.</p>
<p>For more information on the available datasets, refer to <a href="/analytics/graphql-api/features/data-sets/">GraphQL datasets</a>.</p>
<h2 id="update-your-logpush-jobs-and-siem-systems">Update your Logpush jobs and SIEM systems</h2>
<p>Cloudflare will not update existing Logpush jobs to use the renamed fields. You will need to update the jobs according to the instructions provided below.</p>
<p>After updating Logpush jobs, you may need to update external filters or reports in your SIEM systems to reflect the log field changes.</p>
<h3 id="update-logpush-job-in-the-dashboard">Update Logpush job in the dashboard</h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Logpush</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Edit</strong> next to the Logpush job you wish to edit.</li>
<li>Under <strong>Select data fields</strong>, update the fields in your job. The new security log fields are available under <strong>General</strong>.</li>
<li>Select <strong>Save changes</strong>.</li>
</ol>
<h3 id="update-logpush-job-via-api">Update Logpush job via API</h3>
<p>Follow the instructions in <a href="/logs/logpush/examples/example-logpush-curl/#optional---update-output_options">Update output_options</a> to update the fields in the Logpush job.</p>
<h3 id="update-logpush-job-via-terraform">Update Logpush job via Terraform</h3>
<p>If you are already managing Logpush jobs via Terraform, update the <code>logpull_options</code> in your existing <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/logpush_job"><code>cloudflare_logpush_job</code></a> Terraform resource. For example:</p>
<pre><code class="language-diff">  resource &quot;cloudflare_logpush_job&quot; &quot;example_job&quot; {&#10;    enabled             = true&#10;    zone_id             = &quot;&lt;ZONE_ID&gt;&quot;&#10;    name                = &quot;My-logpush-job&quot;&#10;&#45;   logpull_options     = &quot;fields=RayID,ClientIP,EdgeStartTimestamp,WAFAction,WAFProfile&amp;timestamps=rfc3339&quot;&#10;&#43;   logpull_options     = &quot;fields=RayID,ClientIP,EdgeStartTimestamp,SecurityAction&amp;timestamps=rfc3339&quot;&#10;    destination_conf = &quot;r2://cloudflare-logs/http_requests/date={DATE}?account-id=${var.account_id}&amp;access-key-id=${cloudflare_api_token.logpush_r2_token.id}&amp;secret-access-key=${sha256(cloudflare_api_token.logpush_r2_token.value)}&quot;&#10;    dataset             = &quot;http_requests&quot;&#10;  }&#10;</code></pre>
