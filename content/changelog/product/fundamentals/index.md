---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/fundamentals/
  description: '2026-09-17'
  full_title: fundamentals changelog | Cloudflare Docs
  head_html: <title>fundamentals changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-09-17"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/fundamentals/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="fundamentals changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-09-17"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/fundamentals/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/fundamentals/#page","headline":"fundamentals changelog | Cloudflare Docs","description":"2026-09-17","url":"https://developers.cloudflare.com/changelog/product/fundamentals/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/fundamentals/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="create-additional-free-accounts-through-the-dashboard-and-api"><a href="/changelog/post/2026-09-15-free-account-creation/">Create additional Free accounts through the dashboard and API</a></h2>
<p><em>2026-09-17</em></p>
<p>We're expanding how customers create accounts across Cloudflare, making it easier to self-serve account creation in the dashboard, automate standalone account creation with user-owned API tokens or OAuth access tokens, and create Free accounts directly within Enterprise Organizations.</p>
<h4 id="2026-09-15-free-account-creation-what-s-new">What's New</h4>
<p><strong>Dashboard account creation:</strong> All cloudflare customers can create additional Free accounts directly through self-serve flows in the Cloudflare dashboard.</p>
<p><strong>Enterprise Organization account creation:</strong> Super Administrators can now create up to five Free accounts directly within an Enterprise Organization. This makes it easier to provision and manage additional accounts and directly associate them with your Organization.</p>
<p><strong>API and OAuth account creation:</strong> Customers can now create standalone Free accounts programmatically via User-owned API tokens or OAuth access tokens.</p>
<p>For more information:</p>
<ul>
<li><a href="/fundamentals/account/create-account/">Create a Free account in the dashboard</a></li>
<li><a href="/api/resources/accounts/methods/create/">Create an account via the API</a></li>
<li><a href="/fundamentals/organizations/for-enterprise/#create-new-accounts">Create Free accounts in an Enterprise Organization</a></li>
</ul>


<h2 id="enterprise-customers-can-self-serve-cdn-upload-limits-up-to-5-gb"><a href="/changelog/post/2026-09-04-enterprise-self-serve-upload-limits/">Enterprise customers can self-serve CDN upload limits up to 5 GB</a></h2>
<p><em>2026-09-04</em></p>
<p>Enterprise customers can now configure a zone's CDN <strong>Maximum Upload Size</strong> up to 5 GB directly from the <strong>Network</strong> page in the Cloudflare dashboard. This removes the need to contact your account team or Cloudflare Support when applications need to accept request bodies larger than 500 MB and no greater than 5 GB.</p>
<p>The default maximum upload size remains 500 MB. Upload limits above 5 GB still require additional configuration through your account team or <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a>.</p>
<p>Very large uploads may reach connection or read timeouts before reaching the configured size limit. Make sure clients and origins allow enough time to complete the transfer when increasing this setting.</p>
<p>Refer to <a href="/cache/concepts/default-cache-behavior/#upload-limits">Cache upload limits</a> and <a href="/workers/platform/limits/#request-and-response-limits">Workers request body size limits</a> for details.</p>


<h2 id="enriched-403-responses-for-the-cloudflare-api"><a href="/changelog/post/2026-08-20-contextual-403s/">Enriched 403 responses for the Cloudflare API</a></h2>
<p><em>2026-08-21</em></p>
<p>Cloudflare API <code>403 Forbidden</code> responses now include a <code>documentation_url</code> field that links directly to the API documentation for the endpoint that was denied. This gives developers, administrators, and agents an immediate path to the relevant docs with role information instead of guessing at which role or permission they are missing for that endpoint.</p>
<p><strong>What's New</strong></p>
<p><strong>Enriched 403 error responses</strong>: When a Cloudflare API request is denied, the error response now includes a <code>documentation_url</code> field that points to the documentation for that specific endpoint. Contextual 403 responses are now available across nearly all Cloudflare product APIs.</p>
<p><strong>Faster troubleshooting</strong>: The linked API docs surface the roles required for each endpoint, making it easier to self-serve access issues.</p>
<p><strong>Better support for tools and agents</strong>: Agents can use the \documentation_url` field to immediately fetch the endpoint's documentation from the 403 error response, identify the accepted permissions for the denied action, and use that context to drive third-party approval workflows.`</p>
<p>Example 403 response:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;success&quot;: false,&#10;  &quot;errors&quot;: [&#10;    {&#10;      &quot;code&quot;: 10000,&#10;      &quot;message&quot;: &quot;Forbidden&quot;,&#10;      &quot;documentation_url&quot;: &quot;https://developers.cloudflare.com/api/resources/workers/subresources/beta/subresources/workers/methods/list&quot;&#10;    }&#10;  ],&#10;  &quot;messages&quot;: [],&#10;  &quot;result&quot;: null&#10;}&#10;</code></pre>
<p>For more info:</p>
<ul>
<li><a href="/api/">Browse the Cloudflare API documentation</a></li>
<li><a href="/fundamentals/manage-members/roles/">Review Cloudflare roles</a></li>
<li><a href="/fundamentals/api/reference/permissions/">Review API token permissions</a></li>
</ul>


<h2 id="saved-login-profiles-for-returning-users"><a href="/changelog/post/2026-08-21-one-click-login/">Saved login profiles for returning users</a></h2>
<p><em>2026-08-21</em></p>
<p>Cloudflare Dashboard users can now save login profiles on a device for faster sign-in on future visits.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-08-21-one-click-login.png" alt="Saved login profiles for returning users" /></p>
<p><strong>What's New</strong></p>
<p><strong>Save login profiles on a device</strong>: After a successful sign-in, users can choose to save a login profile on that device. Saved profiles store the email address, login method, and last-used profile locally in the browser.</p>
<p><strong>Faster sign-in for returning users</strong>: Saved profiles appear directly on the login page. Selecting one can prefill the email field for password logins or resume the associated SSO or social login flow.</p>
<p>Up to five login profiles can be saved per device, and saved profiles can be removed from the profile list at any time.</p>
<p>For more info:</p>
<ul>
<li><a href="/fundamentals/user-profiles/login/">Log in to Cloudflare</a></li>
<li><a href="/fundamentals/manage-members/dashboard-sso/">Set up dashboard SSO</a></li>
</ul>


<h2 id="improved-scim-2-0-group-synchronization"><a href="/changelog/post/2026-08-21-scim-put-group-synchronization/">Improved SCIM 2.0 group synchronization</a></h2>
<p><em>2026-08-21</em></p>
<p>Dashboard SCIM now supports replacing groups using HTTP <code>PUT</code>, as defined by <a href="https://datatracker.ietf.org/doc/html/rfc7644#section-3.5.1">RFC 7644 section 3.5.1</a>. This allows identity providers to synchronize a group's full state, including its display name, external ID, and members, in a single request.</p>
<p><strong>What's New</strong></p>
<p><strong>Group replacement via <code>PUT</code></strong>: Full-state group synchronization improves compatibility with identity providers that use replacement semantics and helps keep Cloudflare groups aligned with their source identity provider.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17732.md")</aside>
<p>For more information:</p>
<ul>
<li><a href="/fundamentals/account/account-security/scim-setup/">SCIM provisioning overview</a></li>
</ul>


<h2 id="optional-oauth-scopes"><a href="/changelog/post/2026-08-20-oauth-optional-scopes/">Optional OAuth scopes</a></h2>
<p><em>2026-08-20</em></p>
<p>We're announcing the GA of Optional OAuth Scopes.</p>
<p>OAuth client developers can now classify configured scopes as required or optional in the Cloudflare dashboard. By default, all configured scopes remain required .</p>
<h4 id="2026-08-20-oauth-optional-scopes-what-s-new">What's New</h4>
<p><strong>Optional Scopes:</strong> OAuth clients can now mark configured scopes as optional, allowing applications to request them without requiring users to approve them.</p>
<p><strong>Scope Selection:</strong> On the consent screen, users must grant required scopes but can decline optional scopes. This helps customers apply least-privilege access to applications, CLIs, and workloads. Optional scopes are selected by default.</p>
<p><strong>Templates:</strong> The consent screen now includes <strong>Read Only</strong> and <strong>Full Access</strong> templates to make scope selection faster and easier.</p>
<p><strong>Search:</strong> Users can now search scopes in the consent screen.</p>
<p>Learn how to <a href="/fundamentals/oauth/create-an-oauth-client/#select-scopes">select client scopes</a> and <a href="/fundamentals/oauth/authorizing-an-application/#edit-optional-permissions">edit optional permissions</a>.</p>


<h2 id="access-resource-lists-now-support-resource-scoped-roles"><a href="/changelog/post/2026-08-19-granular-permissions-resource-lists/">Access resource lists now support resource-scoped roles</a></h2>
<p><em>2026-08-19</em></p>
<p>Members with only resource-scoped Access roles can now open Access resource list pages in the Cloudflare dashboard and call list endpoints in the API. They no longer need an additional account-scoped read-only role to list resources.</p>
<p>The dashboard and API return only resources included in the member's permission policy scopes. Filtering applies to Access applications, policies, service tokens, and identity providers. This allows administrators to delegate specific Access resources without granting account-wide visibility. Previously, the dashboard blocked these list pages and API list requests returned <code>403</code> responses.</p>
<p>For members with the Cloudflare Access App Admin role, policy lists include policies attached directly to the selected application. Reusable policies appear only when the member has the Cloudflare Access Policy Admin role for those policies.</p>
<p>For role definitions and assignment details, refer to <a href="/fundamentals/manage-members/roles/#resource-scoped-roles">Resource-scoped roles</a> and <a href="/fundamentals/manage-members/scope/">Role scopes</a>.</p>


<h2 id="improved-publisher-verification-details-on-oauth-consent-screens"><a href="/changelog/post/2026-08-04-oauth-consent-shields/">Improved publisher verification details on OAuth consent screens</a></h2>
<p><em>2026-08-05</em></p>
<p>OAuth consent screens now display a shield icon with explanatory text beneath the consent screen title. Each shield icon indicates who owns the application and whether its domain ownership is verified.</p>
<ul>
<li><strong>Green filled shield</strong>: Cloudflare owns and manages the application.</li>
<li><strong>Blue outlined shield</strong>: A third-party application with verified ownership of its domain.</li>
<li><strong>Amber filled shield</strong>: A third-party application without verified ownership of a domain.</li>
</ul>
<p>Domain verification only confirms that the application owner controls the displayed domain.</p>
<p>For more information, refer to <a href="/fundamentals/oauth/authorizing-an-application/">Authorizing an application</a>.</p>


<h2 id="create-free-accounts-from-the-dashboard"><a href="/changelog/post/2026-08-04-free-dashboard-button/">Create Free accounts from the dashboard</a></h2>
<p><em>2026-08-04</em></p>
<p>You can now create standalone Free accounts directly from the Cloudflare dashboard using the new <strong>Create Account</strong> button. This feature is currently available to all users.</p>
<p>When creating a Free account:</p>
<ul>
<li>You can create up to <strong>5 Free accounts</strong>.</li>
<li>Your user account must have at least <strong>7 days of tenure</strong> to be eligible.</li>
<li>The account is created immediately and ready to use.</li>
</ul>
<p>To create a Free account, go to the <a href="https://dash.cloudflare.com/"><strong>Cloudflare dashboard</strong></a> and select <strong>Create Account</strong> from either the account switcher in the top left (where your account name appears) or from the <strong>Accounts</strong> page.</p>
<h4 id="2026-08-04-free-dashboard-button-limitations">Limitations</h4>
* This feature can only be used to create a Cloudflare Free account. To create an Enterprise Account under your existing contract, please contact Cloudflare Support. 
* All users can create a Cloudflare Free account, however, Enterprises wish to restrict this action to only Super Administrators. We will deliver this improvement in a future release. 
<h4 id="2026-08-04-free-dashboard-button-next-steps">Next steps</h4>
<p>After creating your Free account, you can:</p>
<ul>
<li><a href="/billing/get-started/create-billing-profile/">Add a payment method</a> to enable additional Cloudflare products and services.</li>
<li><a href="/billing/get-started/update-billing-info/">Update billing information</a> to manage payment methods, billing address, or tax IDs.</li>
<li><a href="/billing/understand/how-billing-works/">Review how Cloudflare billing works</a> to understand the billing lifecycle and charge types.</li>
<li><a href="/fundamentals/organizations/for-enterprise/">Assign accounts to an Enterprise Organization</a> to centrally manage multiple accounts from a single dashboard.</li>
</ul>


<h2 id="account-role-api-deprecated"><a href="/changelog/post/2026-07-21-account-role-api-deprecated/">Account Role API deprecated</a></h2>
<p><em>2026-07-21</em></p>
<p>The <a href="/api/resources/accounts/subresources/roles/">Account Roles API</a> is deprecated and is being replaced by the <a href="/api/resources/iam/subresources/permission_groups/">Permission Groups API</a>. An end of life date has not yet been established.</p>
<h4 id="2026-07-21-account-role-api-deprecated-what-you-need-to-do">What you need to do</h4>
<p>Review the <a href="/api/resources/iam/subresources/permission_groups/">Permission Groups API</a> documentation; the response schema differs from the legacy Roles response.</p>
<h4 id="2026-07-21-account-role-api-deprecated-highlights">Highlights</h4>
<ul>
<li>Integrations migrating to the Permission Groups API must obtain Permission Group IDs from that API and use them in the Account Members API policies request shape. Integrations that persist legacy Role IDs will need to remap their assignments.</li>
<li>The legacy <code>Role</code> response includes a top-level <code>description</code> and a <code>permissions</code> object keyed by resource type with edit/read flags.</li>
<li>The <code>PermissionGroup</code> response replaces those with a <code>meta</code> object containing <code>label</code> and <code>scopes</code>. Individual permissions are not returned as part of the permission group.</li>
<li>The new API supports the <a href="/fundamentals/api/get-started/create-token/">API Token</a> authorization scheme. The legacy Email + API Key authorization schema is provided for backwards compatibility.</li>
</ul>
<p>For more information, refer to <a href="/fundamentals/api/reference/deprecations/">API deprecations</a>.</p>


<h2 id="distributor-mssp-and-agency-partners-can-manage-organization-members-directly"><a href="/changelog/post/2026-07-17-distributor-mssp-self-serve-members/">Distributor, MSSP, and Agency partners can manage Organization members directly</a></h2>
<p><em>2026-07-17</em></p>
<p>Distributor, MSSP, and Agency partners on Cloudflare <a href="/fundamentals/organizations/">Organizations</a> can now add and manage Organization Members directly from the Cloudflare dashboard, without help from Cloudflare.</p>
<p>Previously, adding a member to a Distributor, MSSP, or Agency Organization was a manual, Cloudflare-assisted process that required a request to Cloudflare and enrollment in a closed beta, and the dashboard <strong>Add member</strong> flow was blocked for these Organizations.</p>
<p>Now, Organization admins can add members themselves from <strong>Organization</strong> &gt; <strong>Members</strong> &gt; <strong>Add member</strong>, with no beta enrollment required.</p>
<p>New members receive access to the Organization's accounts through the same implicit-access model already used for enterprise Organizations. The <strong>Accounts</strong> list and the account switcher classify Distributor, MSSP, and Agency Organizations consistently with enterprise Organizations, so their accounts are labeled and grouped correctly in the dashboard.</p>
<p>Agency partners also gain access to the Organizations dashboard, while retaining access to their existing Tenant management dashboard.</p>
<p>Distributor, MSSP, and Agency Organizations are currently in beta.</p>
<p>For more information, refer to <a href="/fundamentals/organizations/manage-members/">Manage Organization members</a>.</p>


<h2 id="origin-content-signals-for-markdown-for-agents"><a href="/changelog/post/2026-07-13-markdown-for-agents-header-preservation/">Origin Content Signals for Markdown for Agents</a></h2>
<p><em>2026-07-13</em></p>
<p><a href="/fundamentals/reference/markdown-for-agents/">Markdown for Agents</a> now preserves security- and cache-relevant response headers from your origin when converting HTML to Markdown:</p>
<ul>
<li>Markdown for Agents preserves security headers such as <code>Strict-Transport-Security</code> (HSTS), <code>Content-Security-Policy</code> (CSP), <code>X-Frame-Options</code>, <code>Set-Cookie</code>, and CORS headers (for example, <code>Access-Control-Allow-Origin</code>) on the converted response.</li>
<li>Caching headers (<code>Cache-Control</code>, <code>Expires</code>, <code>Age</code>) continue to pass through.</li>
</ul>
<p>Your origin's <a href="https://contentsignals.org/">Content Signals</a> policy is now authoritative. If your origin sets a <code>content-signal</code> header, Markdown for Agents preserves it. When the origin does not send one, Cloudflare adds the default <code>Content-Signal: ai-train=yes, search=yes, ai-input=yes</code>.</p>
<p>This release also fixes relative link resolution for directory-style base URLs (those ending in a trailing slash). Previously, relative links such as <code>../page/</code> could resolve one path segment too high and return a <code>404</code>. Links are now resolved correctly per <a href="https://www.rfc-editor.org/rfc/rfc3986#section-5.2.3">RFC 3986</a>.</p>
<p>Refer to our <a href="/fundamentals/reference/markdown-for-agents/">developer documentation</a> for more details.</p>


<h2 id="new-permissions-and-roles-for-gateway-policies-and-lists"><a href="/changelog/post/2026-06-30-gateway-granular-permissions/">New permissions and roles for Gateway policies and lists</a></h2>
<p><em>2026-06-30</em></p>
<p>You can now assign granular, resource-scoped roles for <a href="/cloudflare-one/traffic-policies/">Cloudflare Gateway</a> firewall policies and <a href="/cloudflare-one/reusable-components/lists/">Zero Trust lists</a>. Administrators can delegate access to specific policy types or list management without granting account-wide or product-wide control.</p>
<h4 id="2026-06-30-gateway-granular-permissions-what-is-new">What is new</h4>
<p>When you <a href="/fundamentals/manage-members/manage/">add a member</a> or create a <a href="/fundamentals/manage-members/policies/">permission policy</a>, the following resource-scoped roles are now available:</p>
<table>
<thead>
<tr>
<th>Role</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Zero Trust Gateway Firewall Policies Admin</td>
<td>Can view and edit all Gateway firewall policies, including DNS, HTTP, and Network policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway DNS Policies Admin</td>
<td>Can view and edit Gateway DNS policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway HTTP Policies Admin</td>
<td>Can view and edit Gateway HTTP policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Network Policies Admin</td>
<td>Can view and edit Gateway Network policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Egress Policies Admin</td>
<td>Can view and edit Gateway Egress policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Resolver Policies Admin</td>
<td>Can view and edit Gateway Resolver policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Policies Admin</td>
<td>Can view and edit all Gateway policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Policies Read</td>
<td>Can view all Gateway policies.</td>
</tr>
<tr>
<td>Zero Trust Gateway Read Only</td>
<td>Can view all Gateway resources.</td>
</tr>
<tr>
<td>Zero Trust DNS Locations Admin</td>
<td>Can view and edit DNS locations.</td>
</tr>
<tr>
<td>Zero Trust Proxy Endpoints Admin</td>
<td>Can view and edit Gateway Proxy Endpoints.</td>
</tr>
<tr>
<td>Zero Trust Account Lists Admin</td>
<td>Can view and edit all Gateway and Access lists.</td>
</tr>
<tr>
<td>Zero Trust Account Lists Read</td>
<td>Can view all Gateway and Access lists.</td>
</tr>
</tbody>
</table>
<p>These roles allow you to:</p>
<ul>
<li>Grant a network engineer write access to Network policies only, without exposing DNS or HTTP policy configuration.</li>
<li>Allow a security analyst to view all Gateway policies in read-only mode for auditing purposes.</li>
<li>Delegate list management to a team that maintains block and allow lists without giving them access to policy configuration.</li>
</ul>
<p>You can also now assign <em>Resource-scoped roles</em>. These roles are complementary to existing account-level roles, and allow you to grant access to a specific resource, like an individual Gateway policy or Cloudflare One list. <strong>Existing account-level roles continue to work.</strong> A member with the <code>Cloudflare Gateway</code> or <code>Cloudflare Zero Trust</code> role retains full access to all Gateway resources. This ensures backward compatibility for existing automation and API tokens.</p>
<h4 id="2026-06-30-gateway-granular-permissions-get-started">Get started</h4>
<ul>
<li>Review the <a href="/fundamentals/manage-members/roles/#resource-scoped-roles">resource-scoped roles</a> on the Cloudflare role reference.</li>
<li>Learn how to <a href="/fundamentals/manage-members/policies/">create permission policies</a> that use these roles.</li>
</ul>


<h2 id="search-api-tokens-by-name"><a href="/changelog/post/2026-06-25-api-token-search/">Search API tokens by name</a></h2>
<p><em>2026-06-25</em></p>
<p>You can now search API tokens by name, making it easier to find specific tokens across large token lists without manually paginating.</p>
<h4 id="2026-06-25-api-token-search-what-s-new">What's new</h4>
<ul>
<li><strong>Dashboard search</strong>: Both <a href="https://dash.cloudflare.com/?to=/:account/account-api-tokens">account API tokens</a> and <a href="https://dash.cloudflare.com/profile/api-tokens">user API tokens</a> pages now include a search bar. Type a name to filter results.</li>
<li><strong>API search support</strong>: The <a href="/api/resources/user/subresources/tokens/methods/list/"><code>/user/tokens</code></a> and <a href="/api/resources/accounts/subresources/tokens/methods/list/"><code>/accounts/{account_id}/tokens</code></a> endpoints now accept a <code>name</code> query parameter to filter tokens by name.</li>
</ul>
<p>For more information, refer to <a href="/fundamentals/api/get-started/create-token/">Create an API token</a> and <a href="/fundamentals/api/get-started/account-owned-tokens/">Account API tokens</a>.</p>


<h2 id="billable-usage-and-budget-alerts-now-in-product-sidebars"><a href="/changelog/post/2026-06-04-billable-usage-product-sidebar/">Billable usage and budget alerts now in product sidebars</a></h2>
<p><em>2026-06-04</em></p>
<p>Pay-as-you-go customers can now view billable usage and create <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">budget alerts</a> directly from the product overview pages for <a href="/workers/">Workers &amp; Pages</a>, <a href="/d1/">D1</a>, <a href="/r2/">R2</a>, <a href="/kv/">Workers KV</a>, <a href="/queues/">Queues</a>, <a href="/vectorize/">Vectorize</a>, <a href="/durable-objects/">Durable Objects</a>, and <a href="/containers/">Containers</a>. A new sidebar widget shows current-period spend and the billing cycle date range, alongside a button to create a budget alert.</p>
<p>The widget pulls from the same data as the <a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">Billable Usage dashboard</a> and aligns to your billing cycle (or the current day on Free plans), so the numbers match your invoice. Enterprise contract accounts are not yet supported.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-06-04-billable-usage-product-sidebar.png" alt="Billable usage widget in the Durable Objects product sidebar showing current-period spend and a breakdown by service" /></p>
<p>Selecting <strong>Create budget alert</strong> opens the budget alert flow inline so you can set a dollar threshold in the same place you are reviewing usage. Budget alerts apply to your total account-level spend across all products, not just the product page you create them from.</p>
<p>For more information, refer to the <a href="/billing/">Usage-based billing documentation</a>.</p>


<h2 id="introducing-self-managed-oauth-clients"><a href="/changelog/post/2026-06-03-public-oauth-clients/">Introducing self-managed OAuth clients</a></h2>
<p><em>2026-06-03</em></p>
<p>Today we are launching self-managed OAuth, enabling developers to build third-party applications that integrate with Cloudflare via OAuth. This provides a more secure, user-friendly, and manageable alternative to API tokens.</p>
<p>OAuth lets third-party applications act on behalf of a user to access their Cloudflare account. For example, after a user grants consent, Wrangler can deploy Workers into that account.</p>
<h4 id="2026-06-03-public-oauth-clients-what-is-new">What is new</h4>
<p>Cloudflare Developers can now create and manage their own OAuth applications to integrate with Cloudflare.</p>
<h4 id="2026-06-03-public-oauth-clients-create-an-application">Create an application</h4>
<p>To create an application, go to <strong>Manage account</strong> &gt; <strong>OAuth clients</strong> in your account on the Cloudflare dashboard.</p>
<div class="nb-dash-button"></div>
<h4 id="2026-06-03-public-oauth-clients-select-limited-scopes">Select limited scopes</h4>
<p>If you have used an API token to call Cloudflare APIs, OAuth client scopes will look familiar. Select only the scopes your application needs during application creation, and include that scope list when sending users to Cloudflare for consent.</p>
<p>Users can review the requested scopes before they consent.</p>
<h4 id="2026-06-03-public-oauth-clients-apps-for-both-private-and-public-use">Apps for both private and public use</h4>
<p>Applications start with <code>private</code> visibility. Private applications can only be used by members of the account where the application was created.</p>
<p>To make an application available to any Cloudflare user, complete the prerequisites for <code>public</code> visibility.</p>
<p>For more information, refer to <a href="/fundamentals/oauth/create-an-oauth-client/#private-and-public-clients">client visibility</a>.</p>
<h4 id="2026-06-03-public-oauth-clients-client-domain-verification">Client domain verification</h4>
<p>Before an application can be made public, you must verify the client domain. Domain verification helps users confirm that the application owner controls the domain shown on the consent page.</p>
<p>After verification, users see a verified badge on the consent page.</p>
<p>For more information, refer to <a href="/fundamentals/oauth/create-an-oauth-client/#client-url-domain-ownership-verification">domain verification</a>.</p>
<h4 id="2026-06-03-public-oauth-clients-learn-more">Learn more</h4>
<p>For more information, refer to <a href="/fundamentals/oauth/">OAuth clients</a>.</p>


<h2 id="granular-permissions-for-cloudflare-tunnel-and-cloudflare-mesh"><a href="/changelog/post/2026-05-21-tunnel-mesh-granular-permissions/">Granular permissions for Cloudflare Tunnel and Cloudflare Mesh</a></h2>
<p><em>2026-05-21</em></p>
<p>You can now scope Cloudflare permissions to individual <a href="/tunnel/">Cloudflare Tunnel</a> instances and <a href="/mesh/">Cloudflare Mesh</a> nodes. Administrators can delegate access to specific Tunnels or Mesh nodes without granting account-wide control over private networking.</p>
<h4 id="2026-05-21-tunnel-mesh-granular-permissions-what-is-new">What is new</h4>
<p>When you <a href="/fundamentals/manage-members/manage/">add a member</a> or create a <a href="/fundamentals/manage-members/policies/">permission policy</a>, the resource picker now lists <a href="/tunnel/">Cloudflare Tunnel</a> instances and <a href="/mesh/">Cloudflare Mesh</a> nodes as scopable resource types. You can:</p>
<ul>
<li>Grant a read-only role on a single Cloudflare Tunnel instance to a support operator for log streaming and diagnostics — without exposing other Tunnels or destructive actions.</li>
<li>Grant a write role on a specific Cloudflare Mesh node to an application team — without giving them access to the rest of your private network.</li>
<li>Scope a single policy to one or many Tunnels and Mesh nodes at once.</li>
</ul>
<h4 id="2026-05-21-tunnel-mesh-granular-permissions-how-it-works">How it works</h4>
<p>Granular permissions are a parallel layer to existing account-level roles — they do not replace them.</p>
<ul>
<li><strong>Existing account-level roles continue to work.</strong> A member with <code>Cloudflare Access</code> or <code>Cloudflare Zero Trust</code> retains write access to every Tunnel and Mesh node in the account. This ensures backward compatibility for existing automation and tokens.</li>
<li><strong>Granular permissions are additive.</strong> For any API request on a specific Tunnel or Mesh node, access is granted if the principal has <strong>either</strong> the account-level role <strong>or</strong> a granular permission for that resource.</li>
<li><strong>Resource enumeration is authorization-aware.</strong> Listing endpoints (<code>GET /accounts/{id}/cfd_tunnel</code>, <code>GET /accounts/{id}/warp_connector</code>) return only the resources the principal has at least read access to.</li>
</ul>
<h4 id="2026-05-21-tunnel-mesh-granular-permissions-get-started">Get started</h4>
<ul>
<li>Configure <a href="/tunnel/guides/granular-permissions/">granular permissions for Cloudflare Tunnel</a>.</li>
<li>Configure <a href="/cloudflare-one/networks/connectors/granular-permissions/">granular permissions for Cloudflare Tunnel and Cloudflare Mesh in Cloudflare One</a>.</li>
<li>Review the <a href="/fundamentals/manage-members/roles/#resource-scoped-roles">resource-scoped roles</a> on the Cloudflare role reference.</li>
</ul>


<h2 id="keyboard-shortcuts-for-the-cloudflare-dashboard"><a href="/changelog/post/2026-05-04-keyboard-shortcuts/">Keyboard shortcuts for the Cloudflare dashboard</a></h2>
<p><em>2026-05-04</em></p>
<p>You can now navigate, switch context, and take common actions in the Cloudflare dashboard without leaving your keyboard. Press <code>?</code> anywhere to see the full list. Keyboard shortcuts can be disabled by visiting your <a href="https://dash.cloudflare.com/profile/settings">profile settings</a>.</p>
<h4 id="2026-05-04-keyboard-shortcuts-navigate">Navigate</h4>
<table>
<thead>
<tr>
<th>Shortcut</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>g h</code></td>
<td>Go to Home</td>
</tr>
<tr>
<td><code>g a</code></td>
<td>Go to account overview</td>
</tr>
<tr>
<td><code>g z</code></td>
<td>Go to zone overview</td>
</tr>
<tr>
<td><code>g p</code></td>
<td>Go to your profile</td>
</tr>
<tr>
<td><code>g w</code></td>
<td>Go to Workers &amp; Pages</td>
</tr>
<tr>
<td><code>g o</code></td>
<td>Go to Zero Trust</td>
</tr>
<tr>
<td><code>g b</code></td>
<td>Go to billing</td>
</tr>
<tr>
<td><code>g 1</code> – <code>g 5</code></td>
<td>Go to a recent or pinned item (by position in sidebar)</td>
</tr>
<tr>
<td><code>t →</code></td>
<td>Move to the next tab</td>
</tr>
<tr>
<td><code>t ←</code></td>
<td>Move to the previous tab</td>
</tr>
<tr>
<td><code>p →</code></td>
<td>Move to the next page of a table</td>
</tr>
<tr>
<td><code>p ←</code></td>
<td>Move to the previous page of a table</td>
</tr>
</tbody>
</table>
<h4 id="2026-05-04-keyboard-shortcuts-take-action">Take action</h4>
<table>
<thead>
<tr>
<th>Shortcut</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/</code></td>
<td>Open quick search</td>
</tr>
<tr>
<td><code>?</code></td>
<td>Show keyboard shortcuts</td>
</tr>
<tr>
<td><code>s a</code></td>
<td>Switch account</td>
</tr>
<tr>
<td><code>s z</code></td>
<td>Switch zone</td>
</tr>
<tr>
<td><code>s .</code></td>
<td>Star or unstar the current zone</td>
</tr>
<tr>
<td><code>p .</code></td>
<td>Pin or unpin the current page</td>
</tr>
<tr>
<td><code>t s</code></td>
<td>Toggle the sidebar open or closed</td>
</tr>
<tr>
<td><code>t m</code></td>
<td>Expand or collapse all sidebar menus</td>
</tr>
<tr>
<td><code>t a</code></td>
<td>Toggle Ask AI sidebar</td>
</tr>
<tr>
<td><code>d .</code></td>
<td>Toggle dark mode</td>
</tr>
<tr>
<td><code>c u</code></td>
<td>Copy the current URL</td>
</tr>
<tr>
<td><code>c d</code></td>
<td>Copy a deep link URL</td>
</tr>
</tbody>
</table>


<h2 id="instant-bank-payments-via-link"><a href="/changelog/post/2026-04-29-instant-bank-payments-via-link/">Instant Bank Payments via Link</a></h2>
<p><em>2026-04-29</em></p>
<p>You can now pay for Cloudflare services directly from your bank account using <a href="/billing/payment-methods/instant-bank-payments-link/">Instant Bank Payments via Link</a>.</p>
<h4 id="2026-04-29-instant-bank-payments-via-link-what-changed">What changed</h4>
<p><a href="https://link.co/">Link</a> now supports bank account payments in addition to cards. If you have a bank account saved in Link, it appears as a payment option at checkout. If not, you can connect one during the checkout flow.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-04-29-instant-bank-payments-link.png" alt="Instant Bank Payments via Link at checkout" /></p>
<h4 id="2026-04-29-instant-bank-payments-via-link-how-to-use-it">How to use it</h4>
<ol>
<li>During checkout, select your bank account from your saved Link payment methods.</li>
<li>Confirm the payment.</li>
</ol>
<p>After your first Link authentication, your bank account is available for future purchases without re-entering details.</p>
<h4 id="2026-04-29-instant-bank-payments-via-link-who-is-eligible">Who is eligible</h4>
<p>Instant Bank Payments via Link is available to US-based self-serve accounts across all Cloudflare products. Your existing cards remain available at checkout.</p>
<p>Bank-based Link payments appear in your billing history with the payment method shown as <code>link</code> and last four digits as <code>0000</code>. For details, refer to the <a href="/billing/payment-methods/instant-bank-payments-link/">Instant Bank Payments via Link documentation</a>.</p>


<h2 id="structured-error-responses-for-cloudflare-5xx-errors"><a href="/changelog/post/2026-04-27-structured-responses-for-5xx-errors/">Structured error responses for Cloudflare 5xx errors</a></h2>
<p><em>2026-04-27</em></p>
<p>Cloudflare-generated 5xx error responses now return structured JSON and Markdown when agents request them, matching the format already available for 1xxx errors. Responses follow <a href="https://www.rfc-editor.org/rfc/rfc9457">RFC 9457 (Problem Details for HTTP APIs)</a> and include a <code>Retry-After</code> HTTP header on retryable codes.</p>
<h4 id="2026-04-27-structured-responses-for-5xx-errors-changes">Changes</h4>
<p><strong>5xx coverage.</strong> Ten Cloudflare-generated error codes (500, 502, 504, 520-526) now serve structured responses. These are errors Cloudflare itself generates when it cannot reach or understand the origin server. Origin-generated 5xx responses that Cloudflare passes through are not affected.</p>
<p><strong>Fault attribution.</strong> The <code>error_category</code> field tells agents where the fault lies:</p>
<ul>
<li><code>origin</code> (502, 504, 520-524) — the origin server is responsible. Transient; retry with the backoff in <code>retry_after</code>.</li>
<li><code>cloudflare</code> (500) — Cloudflare's fault, not the website or the request. Short retry.</li>
<li><code>ssl</code> (525, 526) — the origin's TLS configuration is broken. Do not retry.</li>
</ul>
<p><strong>Retry-After header.</strong> Retryable codes (500, 502, 504, 520-524) include a <code>Retry-After</code> HTTP header matching the <code>retry_after</code> body field. Non-retryable codes (525, 526) do not include the header.</p>
<h4 id="2026-04-27-structured-responses-for-5xx-errors-negotiation-behavior">Negotiation behavior</h4>
<table>
<thead>
<tr>
<th>Request header sent</th>
<th>Response format</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Accept: application/json</code></td>
<td>JSON (<code>application/json</code> content type)</td>
</tr>
<tr>
<td><code>Accept: application/problem+json</code></td>
<td>JSON (<code>application/problem+json</code> content type)</td>
</tr>
<tr>
<td><code>Accept: application/json, text/markdown;q=0.9</code></td>
<td>JSON</td>
</tr>
<tr>
<td><code>Accept: text/markdown</code></td>
<td>Markdown</td>
</tr>
<tr>
<td><code>Accept: text/markdown, application/json</code></td>
<td>Markdown (equal <code>q</code>, first-listed wins)</td>
</tr>
<tr>
<td><code>Accept: */*</code></td>
<td>HTML (default)</td>
</tr>
</tbody>
</table>
<h4 id="2026-04-27-structured-responses-for-5xx-errors-availability">Availability</h4>
<p>Available now for all zones on all plans.</p>
<h4 id="2026-04-27-structured-responses-for-5xx-errors-get-started">Get started</h4>
<p>Get JSON response for error 522:</p>
<pre tabindex="0"><code class="language-bash">curl -s --compressed -H &quot;Accept: application/json&quot; -A &quot;TestAgent/1.0&quot; -H &quot;Accept-Encoding: gzip, deflate&quot; &quot;&lt;YOUR_DOMAIN&gt;/cdn-cgi/error/522&quot; | jq .&#10;</code></pre>
<p>Check presence of the <code>Retry-After</code> HTTP header associated with the JSON response for error 521:</p>
<pre tabindex="0"><code class="language-bash">curl -s --compressed -D - -o /dev/null -H &quot;Accept: application/json&quot; -A &quot;TestAgent/1.0&quot; -H &quot;Accept-Encoding: gzip, deflate&quot; &quot;&lt;YOUR_DOMAIN&gt;/cdn-cgi/error/521&quot; | grep -i retry-after&#10;</code></pre>
<p>References:</p>
<ul>
<li><a href="https://www.rfc-editor.org/rfc/rfc9457">RFC 9457 — Problem Details for HTTP APIs</a></li>
<li><a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/">Cloudflare 5xx error documentation</a></li>
</ul>


<h2 id="resource-tagging-enters-public-beta"><a href="/changelog/post/2026-04-27-resource-tagging-public-beta/">Resource Tagging enters public beta</a></h2>
<p><em>2026-04-27</em></p>
<p>Resource Tagging is now in public beta and rolling out to all Cloudflare accounts over the coming days. You can attach custom key-value metadata to your Cloudflare resources and query across your entire account to find what you need.</p>
<h4 id="2026-04-27-resource-tagging-public-beta-what-s-included">What's included</h4>
<ul>
<li><strong>Broad resource type support</strong> — Tag zones, custom hostnames, Cloudflare Tunnels, Workers, D1 databases, R2 buckets, KV namespaces, Durable Object namespaces, Queues, Stream videos, Images, Access applications, Gateway rules, AI Gateways, and more. Refer to the <a href="/resource-tagging/reference/resource-types/">full list of supported resource types</a>.</li>
<li><strong>Powerful filtering</strong> — Query tagged resources using AND/OR logic, negation, and key-only matching. Combine up to 20 filters per query to build precise resource views.</li>
<li><strong>Account and zone-level endpoints</strong> — Full CRUD operations across both scopes.</li>
<li><strong>Token-based authentication</strong> — Tagging supports <a href="/fundamentals/api/get-started/account-owned-tokens/">Account Owned Tokens</a> that persist independently of individual users, so your automation keeps running through credential rotations and team changes.</li>
<li><strong>Flexible role support</strong> — Super Administrators, Workers Admins, and Tag Admins can all manage tags.</li>
</ul>
<h4 id="2026-04-27-resource-tagging-public-beta-api-first-by-design">API-first by design</h4>
<p>The API is the primary interface for Resource Tagging and the recommended path for all workflows — scripting tag assignments, building CI/CD pipelines, or integrating with your infrastructure-as-code toolchain.</p>
<h4 id="2026-04-27-resource-tagging-public-beta-dashboard-ui">Dashboard UI</h4>
<p>You can also view and manage tagged resources directly in the Cloudflare dashboard. Navigate to <strong>Manage Account</strong> &gt; <strong>Resource Tagging</strong> to see all tagged resources across your account, filter by resource name or tag, and add or edit tags inline.</p>
<p><img src="/assets/upstream/images/changelog/resource-tagging/tagged-resources-dashboard.png" alt="Tagged Resources dashboard" /></p>
<h4 id="2026-04-27-resource-tagging-public-beta-what-s-coming-next">What's coming next</h4>
<p>In future releases, expect support for additional resource types across the Cloudflare platform, tag-based access control policies for scoping user permissions to tagged resources, billing and usage attribution by tag for breaking down costs by team, project, or environment, and Terraform provider support for managing tags declaratively.</p>
<h4 id="2026-04-27-resource-tagging-public-beta-current-limitations">Current limitations</h4>
<ul>
<li><code>PUT</code> replaces all tags on a resource (no partial update). Use the <a href="/resource-tagging/how-to/manage-tags/#add-a-single-tag">GET, merge, PUT workflow</a> to modify individual tags safely.</li>
<li><code>DELETE</code> removes all tags from a resource. To remove a single tag, PUT the remaining tags back.</li>
<li>Querying tags for a resource that has never been tagged returns <code>500</code> instead of <code>404</code>. This is a known beta limitation.</li>
</ul>
<p>To get started, refer to the <a href="/resource-tagging/">Resource Tagging documentation</a>.</p>


<h2 id="network-overview-page-in-the-dashboard"><a href="/changelog/post/2026-04-21-network-overview-page/">Network Overview page in the dashboard</a></h2>
<p><em>2026-04-21T12:00:00</em></p>
<p>A new <strong>Network Overview</strong> page in the Cloudflare dashboard gives you a single starting point for network security and connectivity products.</p>
<p>From the Network Overview page, you can:</p>
<ul>
<li><strong>Connect resources with <a href="/tunnel/">Cloudflare Tunnel</a></strong> - Create tunnels to connect your infrastructure to Cloudflare without exposing it to the public Internet.</li>
<li><strong>Monitor traffic with Network Flow</strong> - Get real-time visibility into traffic volume from your routers.</li>
<li><strong>Configure Address Maps</strong> - Map dedicated static IPs or BYOIP prefixes to specific hostnames.</li>
<li><strong>Explore Magic Transit and Cloudflare WAN</strong> - Set up DDoS protection for your networks and connectivity for your branch offices and data centers.</li>
</ul>
<p>To find it, go to <a href="https://dash.cloudflare.com/?to=/:account/magic-networks/overview"><strong>Networking</strong></a> in the dashboard sidebar.</p>
<p>If you already use <a href="/magic-transit/">Magic Transit</a>, <a href="/cloudflare-wan/">Cloudflare WAN</a>, or other Cloudflare network services products, your existing experience is unchanged.</p>
<p><img src="/assets/upstream/images/fundamentals/network-overview.png" alt="Network Overview page in the Cloudflare dashboard" /></p>


<h2 id="introducing-billable-usage-dashboard-and-budget-alerts"><a href="/changelog/post/2026-04-13-billable-usage-dashboard-and-budget-alerts/">Introducing Billable Usage dashboard and Budget alerts</a></h2>
<p><em>2026-04-21</em></p>
<p>Pay-as-you-go customers can now monitor usage-based costs and configure spend alerts through two new features: the Billable Usage dashboard and Budget alerts.</p>
<h4 id="2026-04-13-billable-usage-dashboard-and-budget-alerts-billable-usage-dashboard">Billable Usage dashboard</h4>
<p>The Billable Usage dashboard provides daily visibility into usage-based costs across your Cloudflare account. The data comes from the same system that generates your monthly invoice, so the figures match your bill.</p>
<p>The dashboard displays:</p>
<ul>
<li>A bar chart showing daily usage charges for your billing period</li>
<li>A sortable table breaking down usage by product, including total usage, billable usage, and cumulative costs</li>
<li>Ability to view previous billing periods</li>
</ul>
<p>Usage data aligns to your billing cycle, not the calendar month. The total usage cost shown at the end of a completed billing period matches the usage overage charges on your corresponding invoice.</p>
<p>To access the dashboard, go to <strong>Manage Account</strong> &gt; <strong>Billing</strong> &gt; <strong>Billable Usage</strong>.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-04-13-billable-usage-dashboard.png" alt="Screenshot of the Billable Usage dashboard in the Cloudflare dashboard" /></p>
<h4 id="2026-04-13-billable-usage-dashboard-and-budget-alerts-budget-alerts">Budget alerts</h4>
<p>Budget alerts allow you to set dollar-based thresholds for your account-level usage spend. You receive an email notification when your projected monthly spend reaches your configured threshold, giving you proactive visibility into your bill before month-end.</p>
<p>To configure a budget alert:</p>
<ol>
<li>Go to <strong>Manage Account</strong> &gt; <strong>Billing</strong> &gt; <strong>Billable Usage</strong>.</li>
<li>Select <strong>Set Budget Alert</strong>.</li>
<li>Enter a budget threshold amount greater than $0.</li>
<li>Select <strong>Create</strong>.</li>
</ol>
<p>Alternatively, configure alerts via <strong>Notifications</strong> &gt; <strong>Add</strong> &gt; <strong>Budget Alert</strong>.</p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2026-04-13-budget-alert-modal.png" alt="Create Budget Alert modal in the Cloudflare dashboard" /></p>
<p>You can create multiple budget alerts at different dollar amounts. The notifications system automatically deduplicates alerts if multiple thresholds trigger at the same time. Budget alerts are calculated daily based on your usage trends and fire once per billing cycle when your projected spend first crosses your threshold.</p>
<p>Both features are available to Pay-as-you-go accounts with usage-based products (Workers, R2, Images, etc.). Enterprise contract accounts are not supported.</p>
<p>For more information, refer to the <a href="/billing/understand/usage-based-billing/">Usage based billing documentation</a>.</p>


<h2 id="improved-oauth-experience-for-consent-and-management"><a href="/changelog/post/2026-04-14-oauth-consent-and-revoke/">Improved OAuth experience for consent and management</a></h2>
<p><em>2026-04-14</em></p>
<p>OAuth allows third-party applications to access your Cloudflare account on your behalf — like when Wrangler deploys Workers or when monitoring tools read your analytics. You now have <strong>granular control</strong> over which accounts these applications can access, plus the ability to revoke access anytime.</p>
<h4 id="2026-04-14-oauth-consent-and-revoke-what-s-new">What's new</h4>
<h4 id="2026-04-14-oauth-consent-and-revoke-choose-which-accounts-to-authorize">Choose which accounts to authorize</h4>
When authorizing an OAuth application, you can now **select specific accounts** instead of granting access to all your accounts:
- **Account-by-account selection** — Choose exactly which accounts the application can access
- **"All accounts" option** — Still available for trusted tools like Wrangler
This gives you precise control who can access your data.
<h4 id="2026-04-14-oauth-consent-and-revoke-clear-consent-screens">Clear consent screens</h4>
The OAuth consent screen now shows:
- **What the application can access** — Explicit list of permissions being requested
- **Who created the application** — Application owner and contact information  
- **Which accounts you're authorizing** — Checkboxes for account selection
<h4 id="2026-04-14-oauth-consent-and-revoke-revoke-access-anytime">Revoke access anytime</h4>
Manage authorized OAuth applications from your profile:
- **See all connected apps** — View every OAuth application with access to your accounts
- **Review permissions and scope** — Check what each application can do and which accounts it can access
- **Revoke instantly** — Remove access with one click when you no longer need it
To manage your OAuth applications, navigate to **Profile** > **Access Management** > **[Connected Applications](https://dash.cloudflare.com/profile/access-management/authorization)**.
<h4 id="2026-04-14-oauth-consent-and-revoke-why-this-matters">Why this matters</h4>
These updates give you:
- **Granular control** — Authorize apps per-account instead of all-or-nothing
- **Transparency** — Know exactly what you're authorizing before you consent
- **Security** — Limit blast radius by restricting access to only necessary accounts
- **Easy cleanup** — Revoke access when applications are no longer needed
<h4 id="2026-04-14-oauth-consent-and-revoke-learn-more">Learn more</h4>
Read more about these improvements in our blog post: [Improving the OAuth consent experience](https://blog.cloudflare.com/improved-developer-security/#improving-the-oauth-consent-experience).


<h2 id="api-tokens-now-detectable-by-secret-scanning-tools"><a href="/changelog/post/2026-04-10-secret-scanning-support/">API tokens now detectable by secret scanning tools</a></h2>
<p><em>2026-04-10</em></p>
<p>Cloudflare API tokens now include <strong>identifiable patterns</strong> that enable secret scanning tools to automatically detect them when leaked in code repositories, configuration files, or other public locations.</p>
<h4 id="2026-04-10-secret-scanning-support-what-changed">What changed</h4>
<p>API tokens generated by Cloudflare now follow a standardized format that secret scanning tools can recognize. When a Cloudflare token is accidentally committed to GitHub, GitLab, or another platform with secret scanning enabled, the tool will flag it and alert you.</p>
<h4 id="2026-04-10-secret-scanning-support-why-this-matters">Why this matters</h4>
<p>Leaked credentials are a common security risk. By making Cloudflare tokens detectable by scanning tools, you can:</p>
<ul>
<li><strong>Detect leaks faster</strong> — Get notified immediately when a token is exposed.</li>
<li><strong>Reduce risk window</strong> — Exposed tokens are deactivated immediately, before they can be exploited.</li>
<li><strong>Automate security</strong> — Leverage existing secret scanning infrastructure without additional configuration.</li>
</ul>
<h4 id="2026-04-10-secret-scanning-support-what-happens-when-a-leak-is-detected">What happens when a leak is detected</h4>
<p>When a third-party secret scanning tool detects a leaked Cloudflare API token:</p>
<ol>
<li><strong>Cloudflare immediately deactivates the token</strong> to prevent unauthorized access.</li>
<li><strong>The token creator receives an email notification</strong> alerting them to the leak.</li>
<li><strong>The token is marked as &quot;Exposed&quot;</strong> in the Cloudflare dashboard.</li>
<li><strong>You can then roll or delete the token</strong> from the token management pages.</li>
</ol>
<h4 id="2026-04-10-secret-scanning-support-supported-platforms">Supported platforms</h4>
<ul>
<li><strong>GitHub Secret Scanning</strong> — Automatically enabled for public repositories</li>
</ul>
<p>For more information on token formats and secret scanning, refer to <a href="/fundamentals/api/get-started/token-formats/">API token formats</a>.</p>


<nav class="pagination" aria-label="Changelog pages"><span>Page 1 of 3</span><a class="pagination-next" rel="next" href="/changelog/product/fundamentals/2/">Next</a></nav>
