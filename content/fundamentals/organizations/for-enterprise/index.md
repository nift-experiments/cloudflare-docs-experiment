---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/organizations/for-enterprise/
  description: Set up and manage an Enterprise Organization to manage multiple Cloudflare accounts from a single dashboard.
  full_title: Organizations for Enterprise · Cloudflare Fundamentals docs
  head_html: <title>Organizations for Enterprise · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Set up and manage an Enterprise Organization to manage multiple Cloudflare accounts from a single dashboard."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/organizations/for-enterprise/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/organizations/for-enterprise/index.md"><meta property="og:title" content="Organizations for Enterprise · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set up and manage an Enterprise Organization to manage multiple Cloudflare accounts from a single dashboard."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/organizations/for-enterprise/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/organizations/for-enterprise/#page","headline":"Organizations for Enterprise \u00b7 Cloudflare Fundamentals docs","description":"Set up and manage an Enterprise Organization to manage multiple Cloudflare accounts from a single dashboard.","url":"https://developers.cloudflare.com/fundamentals/organizations/for-enterprise/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/organizations/for-enterprise/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8824.md")
</aside>
<p>Organizations provides a single-tier structure for Enterprise customers to manage multiple Cloudflare accounts from one unified dashboard.</p>
<h2 id="who-is-this-for">Who is this for?</h2>
<p>Organizations is designed for <strong>Enterprise customers of any size</strong> who manage multiple Cloudflare accounts. Whether you have 5 accounts or 500, Organizations helps you manage them from one dashboard.</p>
<p>Common use cases:</p>
<ul>
<li>Multi-brand companies managing separate accounts per brand</li>
<li>Regional operations with accounts per geography</li>
<li>Business units or subsidiaries with independent accounts</li>
<li>Development workflows with separate accounts per environment</li>
<li>Growing companies consolidating account management</li>
</ul>
<p>Looking for MSSP (Managed Security Service Provider) or Distributor documentation? Refer to <a href="/fundamentals/organizations/for-mssp-distributors/">Organizations for MSSP and Distributors</a>.</p>
<h2 id="hierarchy-structure">Hierarchy structure</h2>
<p>Enterprise Organizations use a <strong>single-tier structure</strong>:</p>
<pre tabindex="0"><code>Organization&#10;├── Account 1&#10;│   ├── Zone A&#10;│   └── Zone B&#10;├── Account 2&#10;│   ├── Zone C&#10;│   └── Zone D&#10;└── Account 3&#10;    └── Zone E&#10;</code></pre>
<p><strong>Key characteristics:</strong></p>
<ul>
<li>One Organization contains multiple accounts</li>
<li>Each account can contain multiple zones</li>
<li>All accounts are at the same level (no sub-organizations)</li>
<li>Organization members have <a href="#implicit-access">implicit access</a> to all accounts</li>
<li>Maximum: <strong>500 accounts</strong> and <strong>5,000 zones</strong> per Organization</li>
</ul>
<h2 id="example-company-a">Example: Company A</h2>
<p><strong>Company A</strong> is a SaaS company with 12 Cloudflare accounts:</p>
<ul>
<li>3 accounts for different product lines (Product Alpha, Product Beta, Product Gamma)</li>
<li>3 environments per product (Development, Staging, Production)</li>
<li>Each account manages its own zones and configurations</li>
</ul>
<p><strong>Before Organizations:</strong></p>
<ul>
<li>Security team manually copies WAF rules to all 12 accounts</li>
<li>Admins switch between accounts individually</li>
<li>No unified view of traffic or security events</li>
<li>Each new admin needs explicit access to all 12 accounts</li>
</ul>
<p><strong>With Organizations:</strong></p>
<ul>
<li>Create one Organization containing all 12 accounts</li>
<li>Security team creates WAF rules once, shares to all production accounts</li>
<li>Admins see all accounts in one dashboard with the enhanced account switcher</li>
<li>View aggregate HTTP analytics across all accounts</li>
<li>New Organization members automatically get access to all 12 accounts</li>
<li>Use tags to organize accounts by product line and environment</li>
</ul>
<h2 id="set-up-your-organization">Set up your Organization</h2>
<h3 id="prerequisites">Prerequisites</h3>
<p>Before you create an Organization:</p>
<ul>
<li>Your user must have Super Admin role access to an account with an Enterprise plan.</li>
<li>You (the Organization creator) must have <a href="/fundamentals/user-profiles/2fa/">two-factor authentication (2FA)</a> or <a href="/fundamentals/manage-members/dashboard-sso/">single sign-on (SSO)</a> enabled on your Cloudflare user account. This is a per-user requirement — 2FA/SSO is not an account-level setting.</li>
<li>You must be a Super Administrator on the accounts you want to assign. You can add accounts of any plan type (eg Enterprise, or Free).</li>
<li>Each Organization supports a maximum of <strong>500 accounts</strong> and <strong>5,000 zones</strong>. Refer to <a href="/fundamentals/organizations/limitations/">Limitations</a> for details.</li>
<li>You may only create a single Organization. You, or another member of your company, must not have already created an Organization.</li>
<li>Your accounts must not already belong to another Organization.</li>
</ul>
<h3 id="create-an-organization">Create an Organization</h3>
<ol>
<li>Log in to the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>.</li>
<li>Select <strong>Organizations</strong>.</li>
<li>Select <strong>Create organization</strong>.</li>
<li>Enter a name for the Organization.</li>
<li>Select <strong>Create</strong>.</li>
</ol>
<p>The Organization overview page displays after creation.</p>
<h3 id="assign-accounts">Assign accounts</h3>
<p>After creating an Organization, you can assign existing accounts to manage them centrally. You can add accounts of any plan type (eg Enterprise, or Free) as long as you are a Super Administrator of the account.</p>
<ol>
<li>From the Organization overview, select <strong>Assign an account</strong>.</li>
<li>Search for an account name. Only accounts where you are a Super Administrator will appear.</li>
<li>Select the account.</li>
<li>Select <strong>Assign to organization</strong>.</li>
</ol>
<p>The assigned account now appears on the Organization overview page. From here, you can view the account, copy its ID, or rename it.</p>
<p>To remove an account from your Organization, contact <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a>.</p>
<h3 id="create-new-accounts">Create new accounts</h3>
<p>Organization Super Administrators can create up to five Free accounts within an Enterprise Organization.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/8825.md")
</div>
<p>The new account starts on the Free plan. It does not inherit payment methods, plans, subscriptions, or entitlements from the Organization.</p>
<p>API tokens and OAuth access tokens cannot create accounts within an Organization.</p>
<h2 id="manage-members">Manage members</h2>
<h3 id="organization-super-administrator">Organization Super Administrator</h3>
<p>When you create an Organization, you become the Organization Super Administrator. This role provides <a href="#implicit-access">implicit access</a> to all accounts in your Organization and allows you to manage memberships at the Organization level.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8823.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8822.md")
</aside>
<h3 id="implicit-access">Implicit access</h3>
<p>Organization members receive <strong>implicit access</strong> to all accounts in the Organization. Implicit access means:</p>
<ul>
<li>You do not need explicit membership on each individual account.</li>
<li>When you go to any account within your Organization, you automatically have Super Administrator permissions on that account.</li>
<li>Implicit access is granted at the Organization level — you cannot grant implicit access to a subset of accounts.</li>
<li>Implicit access is equivalent to Super Administrator. There is no read-only implicit access today.</li>
</ul>
<p>Implicit access is separate from any existing per-account membership. If you were already an explicit member of an account before it was added to the Organization, that existing membership is unaffected.</p>
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
<p>Organizations also supports <a href="/cloudflare-one/integrations/identity-providers/idp-federation/">IdP federation</a>, which lets you configure a single identity provider (such as Okta or Entra ID) in one account and share it across all accounts in your Organization. Shared IdP connections are read-only in recipient accounts and are automatically provisioned or removed as accounts join or leave the Organization.</p>
<p>For detailed instructions, refer to <a href="/fundamentals/organizations/policy-sharing/">Policy sharing</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8821.md")
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
<pre tabindex="0"><code class="language-bash">GET https://api.cloudflare.com/client/v4/organizations/{organization_id}/logs/audit&#10;</code></pre>
<p>If you are viewing account-level audit logs and the account belongs to an Organization where you are an Organization Super Administrator, you can select <strong>View Organization Audit Logs</strong> to go to the parent Organization's audit logs.</p>
<p>For more details on audit log structure, filtering, and retention, refer to <a href="/fundamentals/account/account-security/audit-logs/#organization-activity-logs">Audit Logs — Organization Activity Logs</a>.</p>
<h3 id="api">API</h3>
<p>You can manage Organizations programmatically using the <a href="/api/resources/organizations/">Cloudflare Organizations API</a>. The API supports creating, updating, deleting Organizations, managing members, and assigning accounts.</p>
<h3 id="terraform">Terraform</h3>
<p>You can manage Organizations using the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/organization">Cloudflare Terraform provider</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8820.md")
</aside>
<h2 id="what-you-cannot-do">What you cannot do</h2>
<h3 id="create-sub-organizations">Create sub-organizations</h3>
Enterprise Organizations use a flat structure. You cannot create sub-organizations or nested containers. Use **tags** to organize accounts by business unit, region, or environment.
<h3 id="move-accounts">Move accounts</h3>
Accounts cannot be moved between Enterprise Organizations.
<p>If you encounter errors during setup, refer to <a href="/fundamentals/organizations/limitations/#troubleshooting">Troubleshooting</a>.</p>
