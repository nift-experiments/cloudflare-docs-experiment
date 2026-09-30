<p>The ServiceNow integration detects a variety of data loss prevention, account misconfiguration, and user security risks in an integrated ServiceNow instance that could leave you and your organization vulnerable.</p>
<h2 id="integration-prerequisites">Integration prerequisites</h2>
<ul>
<li><code>admin</code> access to a ServiceNow instance</li>
<li>Ability to <a href="https://docs.servicenow.com/csh?topicname=t_CreateEndpointforExternalClients">create an OAuth API endpoint for external clients</a></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5090.md")
</aside>
<h2 id="integration-permissions">Integration permissions</h2>
<p>For the ServiceNow integration to function, Cloudflare CASB requires the following permissions:</p>
<ul>
<li><code>Global</code> application scope</li>
</ul>
<p>These permissions follow the principle of least privilege to ensure that only the minimum required access is granted. To learn more about each permission, refer to the <a href="https://docs.servicenow.com/bundle/utah-application-development/page/build/applications/concept/c_GlobalScope.html">ServiceNow Application scope documentation</a>.</p>
<h2 id="security-findings">Security findings</h2>
<p>The ServiceNow integration currently scans for the following findings, or security risks. Findings are grouped by category and then ordered by <a href="/cloudflare-one/cloud-and-saas-findings/manage-findings/#severity-levels">severity level</a>.</p>
<p>To stay up-to-date with new CASB findings as they are added, bookmark this page or subscribe to its <a href="https://github.com/cloudflare/cloudflare-docs/commits/production/src/content/docs/cloudflare-one/integrations/cloud-and-saas/servicenow.mdx.atom">RSS feed</a>.</p>
<h3 id="instance-security">Instance security</h3>
<p>Identify security risks related to the ServiceNow instance itself.</p>
<table>
<thead>
<tr>
<th>Finding type</th>
<th>FindingTypeID</th>
<th>Severity</th>
</tr>
</thead>
<tbody>
<tr>
<td>ServiceNow: Production instance with exposed admin credentials</td>
<td><code>6c75c56f-df42-454d-85ee-c919bba70191</code></td>
<td>Critical</td>
</tr>
<tr>
<td>ServiceNow: Production instance with exposed database user credentials</td>
<td><code>37652a12-93d3-453f-961b-de32f419ed33</code></td>
<td>High</td>
</tr>
<tr>
<td>ServiceNow: Instance with exposed admin credentials</td>
<td><code>8235e0a2-6a53-4596-adff-632203c60ab2</code></td>
<td>High</td>
</tr>
<tr>
<td>ServiceNow: Instance with exposed database user credentials</td>
<td><code>4f8bf0e4-fa79-44fc-b171-84926cbc73c7</code></td>
<td>Medium</td>
</tr>
</tbody>
</table>
<h3 id="user-security">User security</h3>
<p>Flag user-related security risks and misconfigurations.</p>
<table>
<thead>
<tr>
<th>Finding type</th>
<th>FindingTypeID</th>
<th>Severity</th>
</tr>
</thead>
<tbody>
<tr>
<td>ServiceNow: User with pending password reset</td>
<td><code>42097604-73db-46b3-9a5c-c3e0d2629531</code></td>
<td>High</td>
</tr>
<tr>
<td>ServiceNow: User with 3+ failed login attempts</td>
<td><code>49079a4b-5280-4c9c-bf61-a45b53c2fd9f</code></td>
<td>Medium</td>
</tr>
<tr>
<td>ServiceNow: User with locked account</td>
<td><code>344f5a37-7df5-4a26-a0fe-4d3c4215df61</code></td>
<td>Low</td>
</tr>
<tr>
<td>ServiceNow: User without multi-factor authentication enabled</td>
<td><code>4efbe128-608d-4b19-b7c8-10c312e4cd9f</code></td>
<td>Low</td>
</tr>
<tr>
<td>ServiceNow: User with no assigned roles</td>
<td><code>8b5ca10d-951c-46d8-b786-223756b39165</code></td>
<td>Low</td>
</tr>
<tr>
<td>ServiceNow: Inactive user</td>
<td><code>a3ee8ec7-85de-480c-bd98-6bc9581bacf9</code></td>
<td>Low</td>
</tr>
<tr>
<td>ServiceNow: User with no recent activity</td>
<td><code>2477faf4-1887-44bc-b663-94373afb03d7</code></td>
<td>Low</td>
</tr>
</tbody>
</table>
<h3 id="incident-management">Incident management</h3>
<p>Identify issues related to ServiceNow incidents.</p>
<table>
<thead>
<tr>
<th>Finding type</th>
<th>FindingTypeID</th>
<th>Severity</th>
</tr>
</thead>
<tbody>
<tr>
<td>ServiceNow: High priority incident with no assigned user</td>
<td><code>8bd04e4e-4f2f-4b44-9c6c-df6341822521</code></td>
<td>High</td>
</tr>
<tr>
<td>ServiceNow: Incident with no assigned user</td>
<td><code>0ea6e2dc-4748-436f-9407-bf24997ae574</code></td>
<td>Medium</td>
</tr>
</tbody>
</table>
<h3 id="knowledge-management">Knowledge management</h3>
<p>Highlight potential misconfigurations in ServiceNow knowledge articles.</p>
<table>
<thead>
<tr>
<th>Finding type</th>
<th>FindingTypeID</th>
<th>Severity</th>
</tr>
</thead>
<tbody>
<tr>
<td>ServiceNow: Knowledge article without expiration date</td>
<td><code>0bd59519-a5ec-4327-92ec-c74f26184a5c</code></td>
<td>Low</td>
</tr>
<tr>
<td>ServiceNow: Knowledge article without any roles</td>
<td><code>3caf029c-9840-43e4-a024-6d4af9f3d57e</code></td>
<td>Low</td>
</tr>
<tr>
<td>ServiceNow: Knowledge article with flagged status</td>
<td><code>12bd46d5-e627-4bba-8644-59e01cca6646</code></td>
<td>Low</td>
</tr>
</tbody>
</table>
<h3 id="integration-and-access">Integration and access</h3>
<p>Detect issues related to ServiceNow integrations and access controls.</p>
<table>
<thead>
<tr>
<th>Finding type</th>
<th>FindingTypeID</th>
<th>Severity</th>
</tr>
</thead>
<tbody>
<tr>
<td>ServiceNow: Internal Integration user</td>
<td><code>fa63799a-24ce-4f5f-8e88-09dbf87a6fb9</code></td>
<td>Low</td>
</tr>
<tr>
<td>ServiceNow: Web Service Access only user</td>
<td><code>3523fbb4-8725-4ffc-b200-9aef44bbbe98</code></td>
<td>Low</td>
</tr>
</tbody>
</table>
