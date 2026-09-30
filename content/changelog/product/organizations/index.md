<h1 id="changelog">Changelog</h1>

<h2 id="distributor-mssp-and-agency-partners-can-manage-organization-members-directly"><a href="/changelog/post/2026-07-17-distributor-mssp-self-serve-members/">Distributor, MSSP, and Agency partners can manage Organization members directly</a></h2>
<p><em>2026-07-17</em></p>
<p>Distributor, MSSP, and Agency partners on Cloudflare <a href="/fundamentals/organizations/">Organizations</a> can now add and manage Organization Members directly from the Cloudflare dashboard, without help from Cloudflare.</p>
<p>Previously, adding a member to a Distributor, MSSP, or Agency Organization was a manual, Cloudflare-assisted process that required a request to Cloudflare and enrollment in a closed beta, and the dashboard <strong>Add member</strong> flow was blocked for these Organizations.</p>
<p>Now, Organization admins can add members themselves from <strong>Organization</strong> &gt; <strong>Members</strong> &gt; <strong>Add member</strong>, with no beta enrollment required.</p>
<p>New members receive access to the Organization's accounts through the same implicit-access model already used for enterprise Organizations. The <strong>Accounts</strong> list and the account switcher classify Distributor, MSSP, and Agency Organizations consistently with enterprise Organizations, so their accounts are labeled and grouped correctly in the dashboard.</p>
<p>Agency partners also gain access to the Organizations dashboard, while retaining access to their existing Tenant management dashboard.</p>
<p>Distributor, MSSP, and Agency Organizations are currently in beta.</p>
<p>For more information, refer to <a href="/fundamentals/organizations/manage-members/">Manage Organization members</a>.</p>


<h2 id="organizations-is-now-in-public-beta-for-enterprises"><a href="/changelog/post/2026-04-06-organizations-public-beta/">Organizations is now in public beta for enterprises</a></h2>
<p><em>2026-04-06</em></p>
<p>We're announcing the public beta of <strong>Organizations</strong> for enterprise customers, a new top-level Cloudflare container that lets Cloudflare customers manage multiple accounts, members, analytics, and shared policies from one centralized location.</p>
<p><strong>What's New</strong></p>
<p><strong>Organizations [BETA]</strong>: <a href="/fundamentals/organizations/">Organizations</a> are a new top-level container for centrally managing multiple accounts. Each Organization supports up to 500 accounts and 5000 zones, giving larger teams a single place to administer resources at scale.</p>
<p><strong>Self-serve onboarding</strong>: Enterprise customers can <a href="/fundamentals/organizations/setup/">create an Organization</a> in the dashboard and assign accounts where they are already Super Administrators.</p>
<p><strong>Centralized Account Management</strong>: At launch, every Organization member has the Organization Super Admin role. Organization Super Admins can invite other users and manage any child account under the Organization implicitly.
<strong>Shared policies</strong>: Share <a href="/waf/custom-rules/">WAF</a> or <a href="/cloudflare-one/traffic-policies/tiered-policies/organizations/">Gateway</a> policies across multiple accounts within your Organization to simplify centralized policy management.
<strong>Implicit access</strong>: Members of an Organization automatically receive Super Administrator permissions across child accounts, removing the need for explicit membership on each account. Additional Org-level roles will be available over the course of the year.</p>
<p><strong>Unified analytics</strong>: View, filter, and download aggregate HTTP analytics across all Organization child accounts from a single dashboard for centralized visibility into traffic patterns and security events.</p>
<p><strong>Terraform provider support</strong>: Manage Organizations with infrastructure as code from day one. Provision organizations, assign accounts, and configure settings programmatically with the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/organization">Cloudflare Terraform provider</a>.</p>
<p><strong>Shared policies</strong>: Share <a href="/waf/custom-rules/">WAF</a> or <a href="/cloudflare-one/traffic-policies/">Gateway</a> policies across multiple accounts within your Organization to simplify centralized policy management.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17731.md")</aside>
<p>For more info:</p>
<ul>
<li><a href="/fundamentals/organizations/">Get started with Organizations</a></li>
<li><a href="/fundamentals/organizations/setup/">Set up your Organization</a></li>
<li><a href="/fundamentals/organizations/limitations/">Review limitations</a></li>
</ul>



