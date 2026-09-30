---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/okta/
  description: Integrate Okta as an identity provider for Cloudflare One.
  full_title: Okta · Cloudflare One docs
  head_html: <title>Okta · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Okta as an identity provider for Cloudflare One."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/okta/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/okta/index.md"><meta property="og:title" content="Okta · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Okta as an identity provider for Cloudflare One."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/okta/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Okta,SCIM"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/okta/#page","headline":"Okta \u00b7 Cloudflare One docs","description":"Integrate Okta as an identity provider for Cloudflare One.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/okta/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Okta","SCIM"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/identity-providers/okta/
  schema: 1
---
<p>Okta provides cloud software that helps companies manage and secure user authentication to modern applications, and helps developers build identity controls into applications, website web services, and devices. You can integrate Okta with Cloudflare One and build rules based on user identity and group membership. Cloudflare One supports Okta integrations using either the OIDC (default) or <a href="/cloudflare-one/integrations/identity-providers/okta-saml/">SAML</a> protocol.</p>
<p>Additionally, you can configure Okta to use risk information from Cloudflare One <a href="/cloudflare-one/team-and-resources/users/risk-score/">user risk scores</a> to create SSO-level policies. For more information, refer to <a href="/cloudflare-one/team-and-resources/users/risk-score/#send-risk-score-to-okta">Send risk score to Okta</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A <a href="/cloudflare-one/setup/">Zero Trust Organization</a> with any subscription tier (including Free)</li>
<li>A <a href="/cloudflare-one/roles-permissions/">Cloudflare One administrator role</a> with <code>Access Edit</code> permissions</li>
</ul>
<h2 id="supported-features">Supported features</h2>
<ul>
<li><strong>SP-initiated SSO</strong>: When a user goes to an Access application, Access redirects them to sign in with Okta.</li>
<li><strong>SCIM provisioning</strong>: Synchronize Okta groups and automatically deprovision users. SCIM currently requires a separate <a href="#synchronize-users-and-groups">custom OIDC application</a>.</li>
</ul>
<h2 id="set-up-okta-as-an-oidc-provider-okta-app-catalog">Set up Okta as an OIDC provider (Okta App Catalog)</h2>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="active-directory-limitation">Active Directory limitation</h3>
@markup("md", "content/.markup/bodies/5041.md")
</aside>
<p>To set up the Okta integration using the Okta Integration Network (OIN) App Catalog:</p>
<ol>
<li>Log in to your Okta admin dashboard.</li>
<li>Go to <strong>Applications</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Browse App Catalog</strong>.</li>
<li>Search for <code>Cloudflare</code> and select the <strong>Cloudflare One</strong> app.</li>
<li>Select <strong>Add integration</strong>.</li>
<li>In <strong>Application label</strong>, enter a name for the application (for example, <code>Cloudflare Access</code>).</li>
<li>In <strong>Team domain</strong>, enter your Cloudflare Zero Trust team name (only the subdomain prefix, do not include <code>.cloudflareaccess.com</code>):</li>
</ol>
<pre tabindex="0"><code class="language-txt">&lt;your-team-name&gt;&#10;</code></pre>
<p>You can find your team name in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> under <strong>Settings</strong> &gt; <strong>Team name and domain</strong> &gt; <strong>Team name</strong>.</p>
<ol start="8">
<li>In the <strong>Sign On</strong> tab, copy the <strong>Client ID</strong> and <strong>Client secret</strong> and paste these into <code>App ID</code> and <code>Client secret</code>.</li>
<li>Copy your Okta Account URL (without the <code>-admin</code> value) and copy it into the Cloudflare Okta setup field.</li>
</ol>
<h2 id="set-up-okta-as-an-oidc-provider-custom-app-integration">Set up Okta as an OIDC provider (Custom App Integration)</h2>
<ol>
<li>
<p>Log in to your Okta admin dashboard and go to <strong>Applications</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Select <strong>Create App Integration</strong>.</p>
</li>
<li>
<p>For the <strong>Sign-in method</strong>, select <strong>OIDC - OpenID Connect</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/okta/okta-1.png" alt="Creating an OIDC application in Okta" /></p>
<ol start="4">
<li>
<p>For the <strong>Application type</strong>, select <strong>Web Application</strong>. Select <strong>Next</strong>.</p>
</li>
<li>
<p>Enter any name for the application. In the <strong>Sign-in redirect URIs</strong> field, enter the following URL:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<p>You can find your team name in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> under <strong>Settings</strong> &gt; <strong>Team name and domain</strong> &gt; <strong>Team name</strong>.</p>
<ol start="6">
<li>
<p>Choose the desired <strong>Assignment</strong> option and select <strong>Save</strong>.</p>
</li>
<li>
<p>From the application view, go to the <strong>Sign On</strong> tab.</p>
</li>
<li>
<p>Scroll down to <strong>Token claims</strong> and select <strong>Show legacy configuration</strong> &gt; <strong>Edit</strong>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/okta/okta-2.png" alt="Configuring the Groups claim filter in Okta" /></p>
<ol start="9">
<li>Set <strong>Groups claim filter</strong> to <em>Matches regex</em> and its value to <code>.*</code>.</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="token-claim-expressions">Token claim expressions</h3>
@markup("md", "content/.markup/bodies/5040.md")
</aside>
<ol start="10">
<li>In the <strong>General</strong> tab, copy the <strong>Client ID</strong> and <strong>Client secret</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/okta/okta-3.png" alt="Finding your Client credentials in Okta" /></p>
<ol start="11">
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Under <strong>Your identity providers</strong>, select <strong>Add new identity provider</strong>. Select <strong>Okta</strong> as your identity provider.</p>
</li>
<li>
<p>Fill in the following information:</p>
<ul>
<li><strong>Name</strong>: Name your identity provider.</li>
<li><strong>App ID</strong>: Enter your Okta client ID.</li>
<li><strong>Client secret</strong>: Enter your Okta client secret.</li>
<li><strong>Okta account URL</strong>: Enter your <a href="https://developer.okta.com/docs/guides/find-your-domain/main/">Okta domain</a>, for example <code>https://my-company.okta.com</code>.</li>
</ul>
</li>
<li>
<p>(Optional) Create an Okta API token and enter it in the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a> under <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong> (the token can be read-only). Use an API token if your Okta tenant has more than 100 groups. This setting is specific to Okta and is not part of SCIM. The token only retrieves Okta group names for the policy builder. Access evaluates group membership from the user's OIDC token during authentication.</p>
</li>
<li>
<p>(Optional) To configure <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/#custom-oidc-claims">custom OIDC claims</a>:</p>
<ol>
<li>In Okta, create a <a href="https://developer.okta.com/docs/guides/customize-authz-server/main/">custom authorization server</a> and ensure that the <code>groups</code> scope is enabled.</li>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, enter the <strong>Authorization Server ID</strong> obtained from Okta.</li>
<li>Under <strong>Optional configurations</strong>, enter the claims that you wish to add to your users' identity.</li>
</ol>
</li>
<li>
<p>(Optional) Enable <a href="https://www.oauth.com/oauth2-servers/pkce/">Proof of Key Exchange (PKCE)</a>. PKCE will be performed on all login attempts.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>To <a href="/cloudflare-one/integrations/identity-providers/#test-idps-in-cloudflare-one">test</a> that your connection is working, select <strong>Test</strong>.</p>
<h2 id="synchronize-users-and-groups">Synchronize users and groups</h2>
<p>The Okta integration allows you to synchronize IdP groups and automatically deprovision users using <a href="/cloudflare-one/team-and-resources/users/scim/">SCIM</a>. To enable SCIM provisioning between Access and Okta, you need two separate app integrations in Okta:</p>
<ul>
<li>The OIDC application you created when adding Okta as an identity provider. You can create this application via the <a href="#set-up-okta-as-an-oidc-provider-okta-app-catalog">Okta App Catalog</a> or via a <a href="#set-up-okta-as-an-oidc-provider-custom-app-integration">Custom App Integration</a>.</li>
<li>A second Okta application of type <strong>SCIM 2.0 Test App (Header Auth)</strong>. This is technically a SAML app but is responsible for sending user and group info via SCIM.</li>
</ul>
<p>SCIM affects Access and Gateway policy evaluation differently.</p>
<p>Access evaluates a user's identity and group membership from the SAML assertion or OIDC token returned by the identity provider during authentication. SCIM provides readable group names in the Access policy builder, but Access does not use SCIM group membership to evaluate a login. If you turn on <strong>Enable user deprovisioning</strong>, removing a user from the SCIM application revokes their active Access sessions. You can also configure SCIM to revoke sessions after group membership changes. Access evaluates the updated identity provider data when the user authenticates again.</p>
<p>Gateway evaluates identity-based policies against the <a href="/cloudflare-one/team-and-resources/users/users/">User Registry identity</a>. SCIM updates this identity when users or group memberships change, without waiting for the user to authenticate again. Cloudflare One Client device profiles use the same synchronized identity.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5039.md")
</aside>
<h3 id="1-enable-scim-in-cloudflare-one"><ol>
<li>Enable SCIM in Cloudflare One</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Find the Okta integration and select <strong>Edit</strong>.</p>
</li>
<li>
<p>Turn on <strong>Enable SCIM</strong>.</p>
</li>
<li>
<p>(Optional) Configure the following settings:</p>
</li>
</ol>
<ul>
<li><strong>Enable user deprovisioning</strong>: <a href="/cloudflare-one/access-controls/access-settings/session-management/#per-user">Revoke a user's active session</a> when they are removed from the SCIM application in Okta. This will invalidate all active Access sessions and prompt for reauthentication for any <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/">Cloudflare One Client session policies</a>.</li>
<li><strong>Remove user seat on deprovision</strong>: <a href="/cloudflare-one/team-and-resources/users/seat-management/">Remove a user's seat</a> from your Cloudflare One account when they are removed from the SCIM application in Okta.</li>
<li><strong>SCIM identity update behavior</strong>: Choose what happens in Cloudflare One when the user's identity updates in Okta.
<ul>
<li><em>Automatic identity updates</em>: Automatically update the <a href="/cloudflare-one/team-and-resources/users/users/">User Registry identity</a> when Okta sends an updated identity or group membership through SCIM. This identity is used for Gateway policies and Cloudflare One Client <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profiles</a>; Access will read the user's updated identity when they reauthenticate.</li>
<li><em>Group membership change reauthentication</em>: <a href="/cloudflare-one/access-controls/access-settings/session-management/#per-user">Revoke a user's active session</a> when their group membership changes in Okta. This will invalidate all active Access sessions and prompt for reauthentication for any <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/">Cloudflare One Client session policies</a>. Access will read the user's updated group membership when they reauthenticate.</li>
<li><em>No action</em>: Update the user's identity the next time they reauthenticate to Access or the Cloudflare One Client.</li>
</ul>
</li>
</ul>
<ol start="5">
<li>
<p>Select <strong>Regenerate Secret</strong>. Copy the <strong>SCIM Endpoint</strong> and <strong>SCIM Secret</strong>. You will need to enter these values into Okta.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>The SCIM secret never expires, but you can manually regenerate the secret at any time.</p>
<h3 id="2-configure-scim-in-okta"><ol start="2">
<li>Configure SCIM in Okta</li>
</ol></h3>
<ol>
<li>
<p>On your Okta admin dashboard, go to <strong>Applications</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Select <strong>Browse App Catalog</strong>.</p>
</li>
<li>
<p>Search for <code>SCIM Header Auth</code> and select <strong>SCIM 2.0 Test App (Header Auth)</strong>.</p>
</li>
<li>
<p>Select <strong>Add Integration</strong>.</p>
</li>
<li>
<p>On the <strong>General Settings</strong> tab, name your application and select <strong>Next</strong>.</p>
</li>
<li>
<p>On the <strong>Sign-on Options</strong> tab, ensure that <strong>SAML 2.0</strong> is selected.</p>
</li>
<li>
<p>Under <strong>Credential Details</strong>, set <strong>Application username format</strong> to either <em>Okta Username</em> or <em>Email</em>. This value will be used for the SCIM <code>userName</code> attribute.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5038.md")
</aside>
<ol start="8">
<li>
<p>Select <strong>Done</strong> to create the integration.</p>
</li>
<li>
<p>On the <strong>Provisioning</strong> tab, select <strong>Configure API Integration</strong>.</p>
</li>
<li>
<p>Select <strong>Enable API integration</strong>.</p>
</li>
<li>
<p>In the <strong>Base URL</strong> field, enter the <strong>SCIM Endpoint</strong> obtained from Cloudflare One.</p>
</li>
<li>
<p>In the <strong>API Token</strong> field, enter the <strong>SCIM Secret</strong> obtained from Cloudflare One.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/okta/enter-scim-values.png" alt="Enter SCIM values into Okta" /></p>
<ol start="13">
<li>
<p>Select <strong>Test API Credentials</strong> to ensure that the credentials were entered correctly. Select <strong>Save</strong>.</p>
</li>
<li>
<p>On the <strong>Provisioning</strong> tab, select <strong>Edit</strong> and enable:</p>
<ul>
<li><strong>Create Users</strong></li>
<li><strong>Update User Attributes</strong></li>
<li><strong>Deactivate Users</strong></li>
</ul>
</li>
</ol>
<p><img src="/assets/upstream/images/cloudflare-one/identity/okta/enable-provisioning.png" alt="Configure provisioning settings in Okta" /></p>
<ol start="15">
<li>
<p>In the <strong>Assignments</strong> tab, add the users you want to synchronize with Cloudflare Access. You can add users in batches by assigning a group. If a user is removed from the application assignment via a either direct user assignment or removed from the group that was assigned to the app, this will trigger a deprovisioning event from Okta to Cloudflare.</p>
</li>
<li>
<p>In the <strong>Push Groups</strong> tab, add the Okta groups you want to synchronize with Cloudflare Access. These groups will display in the Access policy builder and are the group memberships that will be added and removed upon membership change in Okta.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5037.md")
</aside>
<p>To verify the integration, select <strong>View Logs</strong> in the Okta SCIM application.</p>
<p>To check if user identities were updated in Cloudflare One, view your <a href="/cloudflare-one/insights/logs/dashboard-logs/scim-logs/">SCIM provisioning logs</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5036.md")
</aside>
<h2 id="example-api-configuration">Example API Configuration</h2>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;config&quot;: {&#10;		&quot;client_id&quot;: &quot;&lt;your client id&gt;&quot;,&#10;		&quot;client_secret&quot;: &quot;&lt;your client secret&gt;&quot;,&#10;		&quot;okta_account&quot;: &quot;https://dev-abc123.oktapreview.com&quot;&#10;	},&#10;	&quot;type&quot;: &quot;okta&quot;,&#10;	&quot;name&quot;: &quot;my example idp&quot;&#10;}&#10;</code></pre>
<h2 id="troubleshooting">Troubleshooting</h2>
<h3 id="failed-to-fetch-user-group-information-from-the-identity">Failed to fetch user/group information from the identity</h3>
<p>If you see the error <code>Failed to fetch user/group information from the identity</code>, double-check your Okta configuration:</p>
<ul>
<li>If your Okta tenant has more than 100 groups, include an Okta API token in the identity provider configuration. This setting is specific to Okta and is not part of SCIM. The token lets Cloudflare retrieve Okta group names for the policy builder. Access does not use the API token to evaluate a user's group membership during authentication.</li>
<li>If Okta returns more than 100 groups in a user's OIDC token, Okta may omit some group memberships from the token. This is an Okta token claim limitation, not a Cloudflare limit. If a required group is omitted, Cloudflare cannot evaluate policies that depend on that group. To avoid this, narrow the Okta groups claim filter so that only groups used in Cloudflare policies are included. For more information, refer to <a href="https://support.okta.com/help/s/article/limitations-of-group-functions-dynamic-allowlists?language=en_US">Okta's group functions and dynamic allowlists documentation</a>.</li>
<li>The request may be blocked by the <a href="https://help.okta.com/en/prod/Content/Topics/Security/threat-insight/ti-index.htm">ThreatInsights feature</a> within Okta.</li>
</ul>
