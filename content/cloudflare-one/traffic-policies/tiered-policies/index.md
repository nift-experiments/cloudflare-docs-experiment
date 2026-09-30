<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6407.md")
</aside>
<p>Gateway tiered policies allow you to share and enforce Gateway policies across multiple Zero Trust accounts. This enables centralized policy management for organizations that manage multiple accounts.</p>
<p>There are two approaches for setting up tiered policies, depending on your deployment model and policy requirements:</p>
<ul>
<li><strong><a href="/cloudflare-one/traffic-policies/tiered-policies/organizations/">Cloudflare Organizations</a></strong> — Share DNS, network, HTTP, and resolver policies across accounts in a Cloudflare Organization using the dashboard.</li>
<li><strong><a href="/cloudflare-one/traffic-policies/tiered-policies/tenant-api/">Tenant API</a></strong> — Manage DNS policies across parent and child accounts for Managed Service Provider (MSP) deployments.</li>
</ul>
<h2 id="organizations-vs-tenant-api">Organizations vs. Tenant API</h2>
<table>
<thead>
<tr>
<th>Feature</th>
<th><a href="/cloudflare-one/traffic-policies/tiered-policies/organizations/">Cloudflare Organizations</a></th>
<th><a href="/cloudflare-one/traffic-policies/tiered-policies/tenant-api/">Tenant API</a></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Supported policy types</strong></td>
<td>DNS, Network, HTTP, Resolver</td>
<td>DNS only</td>
</tr>
<tr>
<td><strong>Account model</strong></td>
<td>Source / Recipient accounts</td>
<td>Parent / Child accounts</td>
</tr>
<tr>
<td><strong>Shareable settings</strong></td>
<td>Block pages, extended email matching</td>
<td>Block pages</td>
</tr>
<tr>
<td><strong>Setup</strong></td>
<td>Dashboard (self-serve)</td>
<td>API-only</td>
</tr>
<tr>
<td><strong>Availability</strong></td>
<td>Enterprise (beta)</td>
<td>Enterprise (GA)</td>
</tr>
</tbody>
</table>
