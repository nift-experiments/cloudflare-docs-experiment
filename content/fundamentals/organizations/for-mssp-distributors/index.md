<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8819.md")
</aside>
<p>Organizations provides a multi-tier structure for MSSP (Managed Security Service Provider) and Distributor partners to manage customer accounts and create child partner Organizations.</p>
<h2 id="who-is-this-for">Who is this for?</h2>
<p>Organizations for MSSP and Distributors is designed for:</p>
<ul>
<li><strong>Distributors</strong> managing multiple MSSP partner Organizations</li>
<li><strong>MSSPs</strong> managing multiple end-customer accounts</li>
<li><strong>Channel partners</strong> providing managed Cloudflare services</li>
</ul>
<p>Looking for Enterprise documentation? Refer to <a href="/fundamentals/organizations/for-enterprise/">Organizations for Enterprise</a>.</p>
<h2 id="hierarchy-structure">Hierarchy structure</h2>
<p>MSSP/Distributor Organizations use a <strong>multi-tier structure</strong>:</p>
<pre><code>Distributor Organization&#10;├── MSSP Organization A&#10;│   ├── Sub-Organization A1&#10;│   │   ├── Customer Account 1&#10;│   │   │   ├── Zone A&#10;│   │   │   └── Zone B&#10;│   │   └── Customer Account 2&#10;│   │       └── Zone C&#10;│   └── Customer Account 3&#10;│       └── Zone D&#10;├── MSSP Organization B&#10;│   ├── Customer Account 4&#10;│   │   └── Zone E&#10;│   └── Customer Account 5&#10;│       └── Zone F&#10;└── MSSP Organization C&#10;    └── Sub-Organization C1&#10;        └── Customer Account 6&#10;            └── Zone G&#10;</code></pre>
<p><strong>Key characteristics:</strong></p>
<ul>
<li>Distributors create and manage child MSSP Organizations</li>
<li>MSSP Organizations can create up to 5 levels of nested sub-organizations</li>
<li>Each MSSP Organization manages its own customer accounts</li>
<li>MSSP Organization members have <a href="#implicit-access">implicit access</a> to their customer accounts</li>
<li>Accounts can be moved between MSSP Organizations</li>
<li>Maximum: <strong>500 accounts</strong> and <strong>5,000 zones</strong> per Organization</li>
</ul>
<h2 id="example-distributor-a">Example: Distributor A</h2>
<p><strong>Distributor A</strong> is a Cloudflare channel partner with 15 MSSP partners:</p>
<ul>
<li>Each MSSP partner manages 5-50 end-customer accounts</li>
<li>Total: 15 MSSP Organizations, 300+ customer accounts</li>
</ul>
<p><strong>Distributor A's structure:</strong></p>
<pre><code>Distributor A Organization&#10;├── Security MSSP&#10;│   ├── Retail Customer 1 (10 zones)&#10;│   ├── Healthcare Customer 2 (25 zones)&#10;│   └── Finance Customer 3 (40 zones)&#10;├── Web Performance MSSP&#10;│   ├── E-commerce Customer 4 (15 zones)&#10;│   └── Media Customer 5 (30 zones)&#10;└── [13 more MSSP Organizations...]&#10;</code></pre>
<p><strong>What Distributor A can do:</strong></p>
<ul>
<li>Create new MSSP Organizations for new partners</li>
<li>Create customer accounts within each MSSP Organization</li>
<li>Move customer accounts between MSSP Organizations if ownership changes</li>
<li>View aggregate analytics across all MSSP Organizations</li>
<li>Share security policies across MSSP Organizations</li>
</ul>
<p><strong>What each MSSP can do:</strong></p>
<ul>
<li>Manage their own customer accounts</li>
<li>Create new customer accounts for new clients</li>
<li>Invite MSSP team members with implicit access to all customer accounts</li>
<li>Share WAF and Gateway policies across their customer accounts</li>
<li>View aggregate analytics across their customer accounts</li>
</ul>
<h2 id="set-up-your-organization">Set up your Organization</h2>
<p>MSSP/Distributor Organizations cannot be self-serve created by customers. To get started:</p>
<ol>
<li>Contact your <strong>Cloudflare account team</strong> to request an MSSP or Distributor Organization.</li>
<li>Cloudflare will create your Organization and assign the initial Organization Super Administrator.</li>
<li>The initial Organization Super Administrator must have <a href="/fundamentals/user-profiles/2fa/">two-factor authentication (2FA)</a> or <a href="/fundamentals/manage-members/dashboard-sso/">single sign-on (SSO)</a> enabled on their Cloudflare user account.</li>
<li>Once created, the Organization Super Administrator can begin managing the Organization from the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8818.md")
</aside>
<h3 id="create-child-mssp-organizations">Create child MSSP Organizations</h3>
<p>Distributors can create child MSSP partner Organizations. Each MSSP Organization operates independently and manages its own customer accounts.</p>
<h3 id="create-new-accounts">Create new accounts</h3>
<p>MSSP Organizations can self-serve create new customer accounts within their Organization. Enterprise Organizations can self-serve create up to five Free accounts within their Organization.</p>
<h3 id="move-accounts-between-organizations">Move accounts between Organizations</h3>
<p>Move customer accounts from one MSSP Organization to another when ownership changes or customers switch providers.</p>
<h2 id="manage-members">Manage members</h2>
<p>Distributor and MSSP Organization Super Administrators can add and manage Organization members directly from the Cloudflare dashboard. No support ticket is required.</p>
<h3 id="organization-super-administrator">Organization Super Administrator</h3>
<p>When your Organization is created, the initial user becomes the Organization Super Administrator. This role provides <a href="#implicit-access">implicit access</a> to all accounts in your Organization and allows you to manage memberships at the Organization level.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8817.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8816.md")
</aside>
<h3 id="implicit-access">Implicit access</h3>
<p>Organization members receive <strong>implicit access</strong> to all accounts in the Organization. Implicit access means:</p>
<ul>
<li>You do not need explicit membership on each individual account.</li>
<li>When you go to any account within your Organization, you automatically have Super Administrator permissions on that account.</li>
<li>Implicit access is granted at the Organization level — you cannot grant implicit access to a subset of accounts.</li>
<li>Implicit access is equivalent to Super Administrator. There is no read-only implicit access today.</li>
<li>For Distributor Organizations, implicit access applies within each tier — Distributor admins access all child MSSP Organizations and their accounts.</li>
</ul>
<p>Implicit access is separate from any existing per-account membership. If a user was already an explicit member of an account before it was added to the Organization, that existing membership is unaffected.</p>
<h3 id="invite-members">Invite members</h3>
<p>You can invite additional members to your Organization. Invited members receive implicit Super Administrator access to all accounts in the Organization.</p>
<ol>
<li>From the Organization overview, select <strong>Members</strong>.</li>
<li>Select <strong>Invite member</strong>.</li>
<li>Enter the email address.</li>
<li>Select <strong>Send invitation</strong>.</li>
</ol>
<p>The user receives an email invitation. After accepting, they have implicit access to all accounts in the Organization.</p>
<h3 id="member-authentication-requirements">Member authentication requirements</h3>
<p>All users who will be Organization members must have <a href="/fundamentals/user-profiles/2fa/">two-factor authentication (2FA)</a> or <a href="/fundamentals/manage-members/dashboard-sso/">single sign-on (SSO)</a> enabled on their Cloudflare user account <strong>before</strong> they can accept an Organization invitation. This is a per-user requirement, not an account-level setting.</p>
<ul>
<li>If a user does not have 2FA or SSO enabled, they will not be able to accept the invitation.</li>
<li>Ask the user to enable 2FA or SSO first, then resend the invitation.</li>
<li>For instructions on enabling 2FA, refer to <a href="/fundamentals/user-profiles/2fa/">Set up 2FA</a>.</li>
<li>For SSO configuration, refer to <a href="/fundamentals/manage-members/dashboard-sso/">Dashboard SSO</a>.</li>
</ul>
<h2 id="share-policies">Share policies</h2>
<p>Organizations allows you to share WAF custom rulesets and Zero Trust Gateway policies (DNS, Network, HTTP, Resolver) across accounts in your Organization. Shared policies are read-only in receiving accounts and automatically stay in sync when updated in the source account.</p>
<p>For Distributor Organizations, policies can be shared across MSSP Organization boundaries within the same Distributor Organization.</p>
<p>Organizations also supports <a href="/cloudflare-one/integrations/identity-providers/idp-federation/">IdP federation</a>, which lets you configure a single identity provider (such as Okta or Entra ID) in one account and share it across all accounts in your Organization. Shared IdP connections are read-only in recipient accounts and are automatically provisioned or removed as accounts join or leave the Organization.</p>
<p>For detailed instructions, refer to <a href="/fundamentals/organizations/policy-sharing/">Policy sharing</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8815.md")
</aside>
<h2 id="view-aggregate-analytics">View aggregate analytics</h2>
<p>You can view, filter, and download aggregate HTTP analytics across all accounts in your Organization:</p>
<ol>
<li>From the Organization overview, select <strong>Analytics &amp; Logs</strong>.</li>
<li>Use filters to narrow results by date range, account, domain, or other criteria.</li>
<li>To export data, select <strong>Download</strong>.</li>
</ol>
<p>The data includes traffic for proxied hostnames and may be based on a sample. This data does not reflect billable usage.</p>
<h2 id="manage-your-organization">Manage your Organization</h2>
<h3 id="rename-your-organization">Rename your Organization</h3>
<ol>
<li>Go to <strong>Organizations</strong> &gt; <strong>Manage Organization</strong>.</li>
<li>Next to <strong>Organization name</strong>, select <strong>Rename</strong>.</li>
<li>Enter the new name.</li>
<li>Select <strong>Rename</strong>.</li>
</ol>
<h3 id="edit-customer-identification-data">Edit customer identification data</h3>
<ol>
<li>Go to <strong>Organizations</strong> &gt; <strong>Manage Organization</strong>.</li>
<li>Next to <strong>Customer identification data</strong>, select <strong>Edit</strong>.</li>
<li>Update the information.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h3 id="view-audit-logs">View audit logs</h3>
<p>Organization audit logs capture user-initiated actions performed by Organization Super Administrators through Organization-level APIs and the dashboard. These logs are separate from account-level audit logs — actions performed within a specific account continue to appear in that account's audit logs.</p>
<p>To view Organization audit logs in the dashboard:</p>
<ol>
<li>Go to <strong>Organizations</strong> &gt; <strong>Manage Organization</strong>.</li>
<li>Select <strong>Audit Logs</strong>.</li>
</ol>
<p>You can also retrieve Organization audit logs via the API:</p>
<pre><code class="language-bash">GET https://api.cloudflare.com/client/v4/organizations/{organization_id}/logs/audit&#10;</code></pre>
<p>If you are viewing account-level audit logs and the account belongs to an Organization where you are an Organization Super Administrator, you can select <strong>View Organization Audit Logs</strong> to go to the parent Organization's audit logs.</p>
<p>For more details on audit log structure, filtering, and retention, refer to <a href="/fundamentals/account/account-security/audit-logs/#organization-activity-logs">Audit Logs — Organization Activity Logs</a>.</p>
<h3 id="api">API</h3>
<p>You can manage Organizations programmatically using the <a href="/api/resources/organizations/">Cloudflare Organizations API</a>. The API supports creating, updating, deleting Organizations, managing members, and assigning accounts.</p>
<h3 id="terraform">Terraform</h3>
<p>You can manage Organizations using the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/organization">Cloudflare Terraform provider</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8814.md")
</aside>
<p>If you encounter errors during setup or management, refer to <a href="/fundamentals/organizations/limitations/#troubleshooting">Troubleshooting</a>.</p>
<h2 id="what-you-cannot-do-today">What you cannot do (today)</h2>
<h3 id="assign-existing-accounts">Assign existing accounts</h3>
MSSP/Distributor Organizations cannot assign existing accounts. Use account creation to add new accounts to your Organization.
