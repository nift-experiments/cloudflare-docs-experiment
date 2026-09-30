---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/entra-id/
  description: Microsoft Entra ID in Zero Trust integrations.
  full_title: Microsoft Entra ID · Cloudflare One docs
  head_html: <title>Microsoft Entra ID · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Microsoft Entra ID in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/entra-id/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/entra-id/index.md"><meta property="og:title" content="Microsoft Entra ID · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Microsoft Entra ID in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/entra-id/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Microsoft Entra ID,SCIM"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/entra-id/#page","headline":"Microsoft Entra ID \u00b7 Cloudflare One docs","description":"Microsoft Entra ID in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/entra-id/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Microsoft Entra ID","SCIM"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/identity-providers/entra-id/
  schema: 1
---
<p>You can integrate Microsoft Entra ID (formerly Azure Active Directory) with Cloudflare One and build policies based on user identity and group membership. Users will authenticate to Cloudflare One using their Entra ID credentials.</p>
<h2 id="set-up-entra-id-as-an-identity-provider">Set up Entra ID as an identity provider</h2>
<h3 id="1-obtain-entra-id-settings"><ol>
<li>Obtain Entra ID settings</li>
</ol></h3>
<p>The following Entra ID values are required to set up the integration:</p>
<ul>
<li>Application (client) ID</li>
<li>Directory (tenant) ID</li>
<li>Client secret</li>
</ul>
<p>To retrieve those values:</p>
<ol>
<li>
<p>Log in to the <a href="https://entra.microsoft.com/">Microsoft Entra admin center</a>.</p>
</li>
<li>
<p>Go to <strong>Applications</strong> &gt; <strong>Enterprise applications</strong>.</p>
</li>
<li>
<p>Select <strong>New application</strong>, then select <strong>Create your own application</strong>.</p>
</li>
<li>
<p>Name your application.</p>
</li>
<li>
<p>Select <strong>Register an application to integrate with Microsoft Entra ID (App you're developing)</strong>. If offered, do not select any of the gallery applications. Select <strong>Create</strong>.</p>
</li>
<li>
<p>Under <strong>Redirect URI</strong>, select the <em>Web</em> platform and enter the following URL.</p>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<pre tabindex="0"><code>You can find your team name in the [Cloudflare dashboard](https://dash.cloudflare.com) under **Settings** &gt; **Team name and domain** &gt; **Team name**.&#10;</code></pre>
<p><img src="/assets/upstream/images/cloudflare-one/identity/azure/name-app.png" alt="Registering an application in Azure" /></p>
<ol start="7">
<li>
<p>Select <strong>Register</strong>.</p>
</li>
<li>
<p>Next, return to Microsoft Entra ID and go to <strong>Applications</strong> &gt; <strong>App registrations</strong>.</p>
</li>
<li>
<p>Select <strong>All applications</strong> and select the app you just created. Copy the <strong>Application (client) ID</strong> and <strong>Directory (tenant) ID</strong>. You will need these values when <a href="/cloudflare-one/integrations/identity-providers/entra-id/#3-add-entra-id-as-an-identity-provider">adding Entra ID as an identity provider in step 3</a>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/azure/azure-values.png" alt="Viewing the Application ID and Directory ID in Azure" /></p>
<ol start="10">
<li>
<p>On the same page, under <strong>Client credentials</strong>, go to <strong>Add a certificate or secret</strong>. Select <strong>New client secret</strong>.</p>
</li>
<li>
<p>Name the client secret and choose an expiration period.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5078.md")
</aside>
<ol start="12">
<li>After the client secret is created, copy its <strong>Value</strong> field. Store the client secret in a safe place, as it can only be viewed immediately after creation. You will need this client secret value when <a href="/cloudflare-one/integrations/identity-providers/entra-id/#3-add-entra-id-as-an-identity-provider">adding Entra ID as an identity provider in step 3</a>.</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/azure/client-cert-value.png" alt="Location of client secret in Azure" /></p>
<h3 id="2-configure-api-permissions-in-entra-id"><ol start="2">
<li>Configure API permissions in Entra ID</li>
</ol></h3>
<ol>
<li>
<p>Go to <strong>App registrations</strong> &gt; <strong>All applications</strong> &gt; select your application &gt; <strong>API permissions</strong>.</p>
</li>
<li>
<p>Select <strong>Add a permission</strong>.</p>
</li>
<li>
<p>Select <strong>Microsoft Graph</strong>.</p>
</li>
<li>
<p>Select <strong>Delegated permissions</strong> and enable the following <a href="https://learn.microsoft.com/graph/permissions-reference">permissions</a>:</p>
<ul>
<li><code>email</code></li>
<li><code>offline_access</code></li>
<li><code>openid</code></li>
<li><code>profile</code></li>
<li><code>User.Read</code></li>
<li><code>Directory.Read.All</code></li>
<li><code>GroupMember.Read.All</code></li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5077.md")
</aside>
<ol start="5">
<li>
<p>Once all seven permissions are enabled, select <strong>Add permissions</strong>.</p>
</li>
<li>
<p>Select <strong>Grant admin consent</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/azure/configured-perms.png" alt="Configured permissions list in Azure" /></p>
<h3 id="3-add-entra-id-as-an-identity-provider"><ol start="3">
<li>Add Entra ID as an identity provider</li>
</ol></h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5082.md")
</div></div>
<h4 id="upn-and-email">UPN and email</h4>
<p>If your organization's UPNs do not match users' email addresses, you must add a custom claim for email. For example, if your organization's email format is <code>user@domain.com</code> but the UPN is <code>u908080@domain.com</code>, you must create an email claim if you are configuring email-based policies.</p>
<p>By default, Cloudflare will first look for the unique claim name you created and configured in Cloudflare One to represent email (for example, <code>email_identifier</code>) in the <code>id_token</code> JSON response. If you did not configure a unique claim name, Cloudflare will then look for an <code>email</code> claim. Last, if neither claim exists, Cloudflare will look for the UPN claim.</p>
<p>To receive an email claim in the <code>id_token</code> from Microsoft Entra, you must:</p>
<ol>
<li>In the <a href="https://entra.microsoft.com/">Microsoft Entra admin center</a>, go to <strong>Application</strong> &gt; <strong>App registration</strong> &gt; <strong>All applications</strong> and select the relevant application.</li>
<li>Under <strong>Manage</strong>, select <strong>Token configuration</strong>.</li>
<li>Add a claim for email.</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/azure/entra-email-claim.png" alt="Email claim for Entra" /></p>
<pre tabindex="0"><code>The example above includes both a UPN claim and an email claim. Because an email claim was created in the Microsoft Entra configuration, Cloudflare will look for the `email` key-value pair in the JSON response.&#10;</code></pre>
<ol start="4">
<li>
<p>If you gave your email claim another name than <code>email</code>, you must update your configuration in Cloudflare One:</p>
<pre tabindex="0"><code>a. In the [Cloudflare dashboard](https://dash.cloudflare.com/), go to **Zero Trust** &gt; **Integrations** &gt; **Identity providers** &gt; **Azure AD** &gt; **Edit**.&#10;&#10;b. Under **Optional configurations** &gt; **Email claim**, enter the name of the claim representing your organization's email addresses.&#10;</code></pre>
</li>
</ol>
<h4 id="object-id">Object ID</h4>
<p>If you are concerned that users' emails or UPNs may change, you can pass the user's object ID (<code>oid</code>) from Microsoft Entra to Cloudflare Access. To configure Access to receive the object ID, refer to <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/#custom-oidc-claims">custom OIDC claims</a>. No additional configuration is required in Microsoft Entra.</p>
<h2 id="synchronize-users-and-groups">Synchronize users and groups</h2>
<p>The Microsoft Entra ID integration allows you to synchronize IdP groups and automatically deprovision users using <a href="/cloudflare-one/team-and-resources/users/scim/">SCIM</a>.</p>
<p>SCIM affects Access and Gateway policy evaluation differently.</p>
<p>Access evaluates a user's identity and group membership from the SAML assertion or OIDC token returned by the identity provider during authentication. SCIM provides readable group names in the Access policy builder, but Access does not use SCIM group membership to evaluate a login. If you turn on <strong>Enable user deprovisioning</strong>, removing a user from the SCIM application revokes their active Access sessions. You can also configure SCIM to revoke sessions after group membership changes. Access evaluates the updated identity provider data when the user authenticates again.</p>
<p>Gateway evaluates identity-based policies against the <a href="/cloudflare-one/team-and-resources/users/users/">User Registry identity</a>. SCIM updates this identity when users or group memberships change, without waiting for the user to authenticate again. Cloudflare One Client device profiles use the same synchronized identity.</p>
<h3 id="prerequisites">Prerequisites</h3>
<ul>
<li>Microsoft Entra ID P1 or P2 license</li>
</ul>
<h3 id="1-enable-scim-in-cloudflare-one"><ol>
<li>Enable SCIM in Cloudflare One</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Find the Entra ID integration and select <strong>Edit</strong>.</p>
</li>
<li>
<p>Turn on <strong>Enable SCIM</strong> and <strong>Support groups</strong>.</p>
</li>
<li>
<p>(Optional) Configure the following settings:</p>
</li>
</ol>
<ul>
<li><strong>Enable user deprovisioning</strong>: <a href="/cloudflare-one/access-controls/access-settings/session-management/#per-user">Revoke a user's active session</a> when they are removed from the SCIM application in Entra ID. This will invalidate all active Access sessions and prompt for reauthentication for any <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/">Cloudflare One Client session policies</a>.</li>
<li><strong>Remove user seat on deprovision</strong>: <a href="/cloudflare-one/team-and-resources/users/seat-management/">Remove a user's seat</a> from your Cloudflare One account when they are removed from the SCIM application in Entra ID.</li>
<li><strong>SCIM identity update behavior</strong>: Choose what happens in Cloudflare One when the user's identity updates in Entra ID.
<ul>
<li><em>Automatic identity updates</em>: Automatically update the <a href="/cloudflare-one/team-and-resources/users/users/">User Registry identity</a> when Entra ID sends an updated identity or group membership through SCIM. This identity is used for Gateway policies and Cloudflare One Client <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profiles</a>; Access will read the user's updated identity when they reauthenticate.</li>
<li><em>Group membership change reauthentication</em>: <a href="/cloudflare-one/access-controls/access-settings/session-management/#per-user">Revoke a user's active session</a> when their group membership changes in Entra ID. This will invalidate all active Access sessions and prompt for reauthentication for any <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/">Cloudflare One Client session policies</a>. Access will read the user's updated group membership when they reauthenticate.</li>
<li><em>No action</em>: Update the user's identity the next time they reauthenticate to Access or the Cloudflare One Client.</li>
</ul>
</li>
</ul>
<ol start="5">
<li>
<p>Select <strong>Regenerate Secret</strong>. Copy the <strong>SCIM Endpoint</strong> and <strong>SCIM Secret</strong>. You will need to enter these values into Entra ID.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>The SCIM secret never expires, but you can manually regenerate the secret at any time.</p>
<h3 id="2-configure-scim-in-entra-id"><ol start="2">
<li>Configure SCIM in Entra ID</li>
</ol></h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5075.md")
</aside>
<ol>
<li>
<p>In the Microsoft Entra ID menu, go to <strong>Enterprise applications</strong>.</p>
</li>
<li>
<p>Select <strong>New application</strong> &gt; <strong>Create your own application</strong>.</p>
</li>
<li>
<p>Name your application (for example, <code>Cloudflare Access SCIM</code>).</p>
</li>
<li>
<p>Select <strong>Integrate any other application you don't find in the gallery (Non-gallery)</strong>. If offered, do not select any of the gallery applications. Select <strong>Create</strong>.</p>
</li>
<li>
<p>After you have created the application, go to <strong>Provisioning</strong> &gt; select <strong>New Configuration</strong>.</p>
</li>
<li>
<p>In the <strong>Tenant URL</strong> field, enter the <strong>SCIM Endpoint</strong> obtained from your Entra ID integration in Cloudflare One <a href="/cloudflare-one/integrations/identity-providers/entra-id/#1-enable-scim-in-zero-trust">in the previous step</a>.</p>
</li>
<li>
<p>In the <strong>Secret token</strong> field, enter the <strong>SCIM Secret</strong> obtained from your Entra ID integration in Cloudflare One <a href="/cloudflare-one/integrations/identity-providers/entra-id/#1-enable-scim-in-zero-trust">in the previous step</a>.</p>
</li>
<li>
<p>Select <strong>Test Connection</strong> to ensure that the credentials were entered correctly. If the test fails, go to your Entra ID integration in Cloudflare One, select <strong>Regenerate Secret</strong>, select <strong>Save</strong>, and enter your new <strong>SCIM Secret</strong> in the <strong>Secret token</strong> field.</p>
</li>
<li>
<p>Select <strong>Create</strong>.</p>
</li>
<li>
<p>Once the SCIM application is created, <a href="https://learn.microsoft.com/entra/identity/enterprise-apps/assign-user-or-group-access-portal">assign users and groups to the application</a>.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5074.md")
</aside>
<ol start="11">
<li>
<p>Go to <strong>Provisioning</strong> and select <strong>Start provisioning</strong>.</p>
</li>
<li>
<p>For <strong>Provisioning Mode</strong>, the default mode should be set by Microsoft to <em>Automatic</em>.</p>
</li>
<li>
<p>On the <strong>Overview</strong> page in Entra ID, you will see the synchronization status.</p>
</li>
</ol>
<p>To check which users and groups were synchronized, select <strong>Provisioning logs</strong>.</p>
<p>To check if user identities were updated in Cloudflare One, view your <a href="/cloudflare-one/insights/logs/dashboard-logs/scim-logs/">SCIM provisioning logs</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5073.md")
</aside>
<p>To monitor the exchange of identity details between Cloudflare Access and Microsoft Entra ID, go to the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> &gt; <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>SCIM provisioning logs</strong> and view the <a href="/cloudflare-one/insights/logs/dashboard-logs/scim-logs/">SCIM activity logs</a>.</p>
<h3 id="provisioning-attributes">Provisioning attributes</h3>
<p>Provisioning attributes define the user properties that Entra ID will synchronize with Cloudflare Access. To modify your provisioning attributes, go to the <strong>Attribute mapping</strong> and select <strong>Provision Microsoft Entra ID Users</strong>.</p>
<p>If not already configured, Cloudflare recommends enabling the following user attribute mappings:</p>
<table>
<thead>
<tr>
<th>customappsso Attribute</th>
<th>Entra ID Attribute</th>
<th>Recommendation</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>userName</code></td>
<td><code>userPrincipalName</code> or <code>mail</code></td>
<td>Required. Must match the user's email address in Cloudflare One.</td>
</tr>
<tr>
<td><code>emails[type eq &quot;work&quot;].value</code></td>
<td><code>mail</code></td>
<td>Required. Must match the user's email address in Cloudflare One.</td>
</tr>
<tr>
<td><code>name.givenName</code></td>
<td><code>givenName</code></td>
<td>Recommended</td>
</tr>
<tr>
<td><code>name.familyName</code></td>
<td><code>surname</code></td>
<td>Recommended</td>
</tr>
</tbody>
</table>
<h2 id="entra-groups-in-zero-trust-policies">Entra groups in Zero Trust policies</h2>
<h3 id="automatic-entry">Automatic entry</h3>
<p>When <a href="#synchronize-users-and-groups">SCIM synchronization is enabled</a>, your Entra group names will automatically appear in the Access and Gateway policy builders.</p>
<p>If building an Access policy, choose the <em>Azure Groups</em> selector.
<img src="/assets/upstream/images/cloudflare-one/identity/azure/azure-scim-groups.png" alt="Azure group names displayed in the Access policy builder" /></p>
<p>If building a Gateway policy, choose the <a href="/cloudflare-one/traffic-policies/identity-selectors/#user-group-names"><em>User Group Names</em></a> selector.</p>
<h3 id="manual-entry">Manual entry</h3>
<p>You can create Access and Gateway policies for groups that are not synchronized with SCIM. Entra ID exposes directory groups in a format that consists of random strings, the <code>Object Id</code>, that is distinct from the <code>Name</code>.</p>
<ol>
<li>
<p>Make sure you enable <strong>Support groups</strong> as you set up Microsoft Entra ID in Cloudflare One.</p>
</li>
<li>
<p>In your Microsoft Entra dashboard, note the <code>Object Id</code> for the Entra group. In the example below, the group named Admins has an ID of <code>61503835-b6fe-4630-af88-de551dd59a2</code>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/azure/object-id.png" alt="Viewing the Azure group ID on the Azure dashboard" /></p>
<ol start="3">
<li>
<p>If building an Access policy, choose the <em>Azure Groups</em> selector. If building a Gateway policy, choose the <em>User Group IDs</em> selector.</p>
</li>
<li>
<p>In the <strong>Value</strong> field, enter the <code>Object Id</code> for the Entra group.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/azure/configure-group-n.png" alt="Entering an Azure group ID in Cloudflare One" /></p>
<h3 id="nested-groups">Nested groups</h3>
<h4 id="authentication">Authentication</h4>
<p>Access and Gateway policies for an Entra group will also apply to all <a href="https://learn.microsoft.com/entra/fundamentals/how-to-manage-groups#add-a-group-to-another-group">nested groups</a>. For example, if a user belongs to the group <code>US devs</code>, and <code>US devs</code> is part of the broader group <code>Devs</code>, the user would be allowed or blocked by all policies created for <code>Devs</code>.</p>
<h4 id="scim-provisioning">SCIM provisioning</h4>
<p>For SCIM provisioning, <a href="https://learn.microsoft.com/en-us/entra/identity/app-provisioning/how-provisioning-works#assignment-based-scoping">nested groups are not supported</a>. Microsoft Entra ID's SCIM implementation does not send information about nested group memberships to Cloudflare. Only users who are direct members of an explicitly assigned group will be provisioned. To ensure group memberships are correctly synchronized, you must flatten your groups in Entra ID by directly assigning users to the groups you want to provision.</p>
<p>Since the SCIM request from Microsoft does not include nested group information, neither Cloudflare nor Microsoft can provide a notification that nested groups are not being synchronized.</p>
<h2 id="force-user-interaction-during-device-client-reauthentication">Force user interaction during device client reauthentication</h2>
<p>You can require users to re-enter their credentials into Entra ID whenever they <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/">re-authenticate their Cloudflare One Client session</a>. To configure this setting:</p>
<ol>
<li>Make a <code>GET</code> request to the <a href="/api/resources/zero_trust/subresources/identity_providers/">Identity Providers endpoint</a> and copy the response for the Entra ID identity provider.</li>
</ol>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/access/identity_providers/{identity_provider_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<ol start="2">
<li><a href="/api/resources/zero_trust/subresources/identity_providers/methods/update/">Update the Entra ID identity provider</a> using a <code>PUT</code> request. In the request body, include all existing configurations and set the <code>prompt</code> parameter to either <code>login</code> or <code>select_account</code>. For example:</li>
</ol>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/access/identity_providers/{identity_provider_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;id&quot;: &quot;f174e90a-fafe-4643-bbbc-4a0ed4fc8415&quot;,&#10;  &quot;type&quot;: &quot;azureAD&quot;,&#10;  &quot;uid&quot;: &quot;f174e90a-fafe-4643-bbbc-4a0ed4fc8415&quot;,&#10;  &quot;name&quot;: &quot;Entra ID&quot;,&#10;  &quot;version&quot;: &quot;31e74e9b4f033e16b604552091a72295&quot;,&#10;  &quot;config&quot;: {&#10;    &quot;azure_cloud&quot;: &quot;default&quot;,&#10;    &quot;client_id&quot;: &quot;&lt;CLIENT_ID&gt;&quot;,&#10;    &quot;conditional_access_enabled&quot;: false,&#10;    &quot;directory_id&quot;: &quot;&lt;AZURE_DIRECTORY_ID&gt;&quot;,&#10;    &quot;redirect_url&quot;: &quot;https://&lt;TEAM_NAME&gt;.cloudflareaccess.com/cdn-cgi/access/callback&quot;,&#10;    &quot;prompt&quot;: &quot;login&quot;,&#10;    &quot;support_groups&quot;: true&#10;  },&#10;  &quot;scim_config&quot;: {&#10;    &quot;enabled&quot;: true,&#10;    &quot;user_deprovision&quot;: true,&#10;    &quot;seat_deprovision&quot;: false,&#10;    &quot;group_member_deprovision&quot;: false,&#10;    &quot;identity_update_behavior&quot;: &quot;automatic&quot;&#10;  },&#10;  &quot;scim_base_url&quot;: &quot;https://&lt;TEAM_NAME&gt;.cloudflareaccess.com/populations/f174e90a-fafe-4643-bbbc-4a0ed4fc8415/scim/v2&quot;&#10;}&#x27;</code></pre>
