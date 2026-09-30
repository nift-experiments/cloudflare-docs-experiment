<p>When creating a Cloudflare Zero Trust account, you will be given the Super Administrator role. As a Super Administrator, you can invite members to join your Zero Trust account and assign them different roles. There is no limit to the number of members which can be added to a given account. Any members with the proper permissions will be able to make configuration changes while actively logged into Zero Trust (unless <a href="/cloudflare-one/api-terraform/#set-dashboard-to-read-only">read-only mode</a> is enabled).</p>
<p>To check the list of members in your account, or to manage roles and permissions, refer to our <a href="/fundamentals/manage-members/">Account setup</a> documentation.</p>
<h2 id="zero-trust-roles">Zero Trust roles</h2>
<p>Only Super Administrators will be able to assign or remove the following roles from users in their account. Scroll to the right to see a full list of permissions for each role.</p>
<table>
<thead>
<tr>
<th></th>
<th>Access Read</th>
<th>Access Edit</th>
<th>Gateway Read</th>
<th>Gateway Edit</th>
<th>Gateway Report</th>
<th>DNS Location Read</th>
<th>DNS Location Edit</th>
<th>Billing Read</th>
<th>Billing Edit</th>
<th>DEX Read</th>
<th>DEX Edit</th>
<th>CASB Read</th>
<th>CASB Edit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Super Administrator</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Cloudflare Zero Trust<sup><a href="#footnote-1">1</a></sup></td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Cloudflare Access</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
</tr>
<tr>
<td>Cloudflare Gateway</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
</tr>
<tr>
<td>Cloudflare Zero Trust Read Only</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>Cloudflare Zero Trust Reporting</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
</tr>
<tr>
<td>Cloudflare Zero Trust DNS Locations Write<sup><a href="#footnote-2">2</a></sup></td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
</tr>
<tr>
<td>Cloudflare DEX</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
</tr>
<tr>
<td>Cloudflare CASB Read</td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>Cloudflare CASB</td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>❌</td>
<td>✅</td>
<td>✅</td>
</tr>
</tbody>
</table>
<h3 id="cloudflare-zero-trust-pii">Cloudflare Zero Trust PII</h3>
<p>By default, only Super Administrators can view end users' PII in the Gateway activity logs, such as Device IDs, Source IPs, or user emails. No other roles will have the ability to read PII unless Super Administrators explicitly assign the <strong>Cloudflare Zero Trust PII</strong> role to them.</p>
<p>The Cloudflare Zero Trust PII role should be considered an add-on role, to be combined with any role from the table above. For example, Super Administrators may decide to assign the Cloudflare Gateway role to a user, and add the Cloudflare Zero Trust PII role to allow that user to access PII in the Gateway logs.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1290.md")
</aside>
<h2 id="email-security-roles">Email security roles</h2>
<p>For more information on Email security roles, refer to <a href="/fundamentals/manage-members/roles/#account-scoped-roles">Account-scoped roles</a>.</p>
<ul>
<li><strong>Cloudflare Zero Trust</strong>: Can edit Cloudflare <a href="/cloudflare-one/">Zero Trust</a>. Grants administrator access to all Zero Trust products including Access, Gateway, the Cloudflare One Client, Tunnel, Browser Isolation, CASB, DLP, DEX, and Email security.</li>
<li><strong>Cloudflare Zero Trust PII</strong>: Can read PII in Zero Trust. This includes Email security.</li>
<li><strong>Email security Analyst</strong> and <strong>Email security Configuration Admin</strong>: Has full access to all admin features in Email security.</li>
<li><strong>Email security Integration Admin</strong>: Can read and set up integrations only.</li>
<li><strong>Email security Configuration Admin</strong>: Has administrator access. Cannot take actions on emails, or read emails.</li>
<li><strong>Email security Analyst</strong>: Has analyst access. Can take action on emails and read emails.</li>
<li><strong>Email security Reporting</strong>: Can read metrics.</li>
<li><strong>Email security Read Only</strong>: Can read all information, but cannot take action on anything.</li>
<li><strong>Email security Policy Admin</strong>: Can read all settings, but only write <a href="/cloudflare-one/email-security/settings/detection-settings/allow-policies/">allow policies</a>, <a href="/cloudflare-one/email-security/settings/detection-settings/trusted-domains/">trusted domains</a>, and <a href="/cloudflare-one/email-security/settings/detection-settings/blocked-senders/">blocked senders</a>.</li>
</ul>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">The **Cloudflare Zero Trust** role grants administrator access to all Zero Trust products including Access, Gateway, the Cloudflare One Client, Tunnel, Browser Isolation, CASB, DLP, DEX, and Email security.</li>
<li id="footnote-2">Users with the **Cloudflare Zero Trust DNS Locations Write** role can view all DNS locations for an organization but can only create and edit [secure DNS locations](/cloudflare-one/networks/resolvers-and-proxies/dns/locations/#secure-dns-locations).</li></ol></section>
