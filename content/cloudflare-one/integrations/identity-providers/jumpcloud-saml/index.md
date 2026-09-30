---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/jumpcloud-saml/
  description: JumpCloud (SAML) in Zero Trust integrations.
  full_title: JumpCloud (SAML) · Cloudflare One docs
  head_html: <title>JumpCloud (SAML) · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="JumpCloud (SAML) in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/jumpcloud-saml/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/jumpcloud-saml/index.md"><meta property="og:title" content="JumpCloud (SAML) · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="JumpCloud (SAML) in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/jumpcloud-saml/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML,SCIM"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/jumpcloud-saml/#page","headline":"JumpCloud (SAML) \u00b7 Cloudflare One docs","description":"JumpCloud (SAML) in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/jumpcloud-saml/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML","SCIM"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/identity-providers/jumpcloud-saml/
  schema: 1
---
<p><a href="https://jumpcloud.com/#platform">JumpCloud</a> provides SSO identity management. Cloudflare Access integrates with JumpCloud as a SAML identity provider.</p>
<p>The following steps are specific to setting up JumpCloud with Cloudflare Access. For more information on configuring JumpCloud SSO application, refer to the <a href="https://jumpcloud.com/support/integrate-with-cloudflare">JumpCloud documentation</a>.</p>
<h2 id="set-up-jumpcloud-as-a-saml-provider">Set up Jumpcloud as a SAML provider</h2>
<h3 id="1-create-an-sso-application-in-jumpcloud"><ol>
<li>Create an SSO application in JumpCloud</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://console.jumpcloud.com/#/home">JumpCloud Admin Portal</a>, go to <strong>SSO Applications</strong>.</p>
</li>
<li>
<p>Select <strong>Add New Application</strong>.</p>
</li>
<li>
<p>In the search bar, enter <code>Cloudflare</code> and select the <strong>Cloudflare Access</strong> application.</p>
</li>
<li>
<p>Select <strong>Next</strong>.</p>
</li>
<li>
<p>In <strong>Display Label</strong>, enter an application name.</p>
</li>
<li>
<p>Select <strong>Save Application</strong>.</p>
</li>
<li>
<p>Review the application summary and select <strong>Configure Application</strong>.</p>
</li>
<li>
<p>In the <strong>SSO</strong> tab, configure the following settings:</p>
<ol>
<li>In <strong>IdP Entity ID</strong>, enter your Cloudflare team domain:</li>
</ol>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/&#10;</code></pre>
<pre tabindex="0"><code>  You can find your team name in the [Cloudflare dashboard](https://dash.cloudflare.com) under **Settings** &gt; **Team name and domain** &gt; **Team name**.&#10;</code></pre>
<ol start="2">
<li>Set both <strong>SP Entity ID</strong> and <strong>ACS URL</strong> to the following callback URL:</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<ol start="3">
<li>
<p>(Optional) Configure SAML attributes that you want to send to Cloudflare Access.</p>
</li>
<li>
<p>Scroll up to <strong>JumpCloud Metadata</strong> and select <strong>Export Metadata</strong>. Save this XML file for use in a <a href="#2-add-jumpcloud-to-zero-trust">later step</a>.</p>
</li>
<li>
<p>In the <strong>User Groups</strong> tab, <a href="https://jumpcloud.com/support/get-started-applications-saml-sso#managing-employee-access-to-applications">assign user groups</a> to this application.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<h3 id="2-add-jumpcloud-to-cloudflare-one"><ol start="2">
<li>Add JumpCloud to Cloudflare One</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Under <strong>Your identity providers</strong>, select <strong>Add new identity provider</strong>.</p>
</li>
<li>
<p>Select <strong>SAML</strong>.</p>
</li>
<li>
<p>Upload your JumpCloud XML metadata file.</p>
</li>
<li>
<p>(Optional) To enable SCIM, refer to <a href="#synchronize-users-and-groups">Synchronize users and groups</a>.</p>
</li>
<li>
<p>(Optional) Under <strong>Optional configurations</strong>, configure <a href="#optional-configurations">additional SAML options</a>.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>You can now <a href="/cloudflare-one/integrations/identity-providers/#test-idps-in-cloudflare-one">test your connection</a> and create <a href="/cloudflare-one/access-controls/policies/">Access policies</a> based on the configured login method and SAML attributes.</p>
<h2 id="synchronize-users-and-groups">Synchronize users and groups</h2>
<p>The JumpCloud integration allows you to synchronize user groups and automatically deprovision users using <a href="/cloudflare-one/team-and-resources/users/scim/">SCIM</a>.</p>
<p>SCIM affects Access and Gateway policy evaluation differently.</p>
<p>Access evaluates a user's identity and group membership from the SAML assertion or OIDC token returned by the identity provider during authentication. SCIM provides readable group names in the Access policy builder, but Access does not use SCIM group membership to evaluate a login. If you turn on <strong>Enable user deprovisioning</strong>, removing a user from the SCIM application revokes their active Access sessions. You can also configure SCIM to revoke sessions after group membership changes. Access evaluates the updated identity provider data when the user authenticates again.</p>
<p>Gateway evaluates identity-based policies against the <a href="/cloudflare-one/team-and-resources/users/users/">User Registry identity</a>. SCIM updates this identity when users or group memberships change, without waiting for the user to authenticate again. Cloudflare One Client device profiles use the same synchronized identity.</p>
<h3 id="1-enable-scim-in-cloudflare-one"><ol>
<li>Enable SCIM in Cloudflare One</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Find the JumpCloud integration and select <strong>Edit</strong>.</p>
</li>
<li>
<p>Turn on <strong>Enable SCIM</strong>.</p>
</li>
<li>
<p>(Optional) Configure the following settings:</p>
</li>
</ol>
<ul>
<li><strong>Enable user deprovisioning</strong>: <a href="/cloudflare-one/access-controls/access-settings/session-management/#per-user">Revoke a user's active session</a> when they are removed from the SCIM application in JumpCloud. This will invalidate all active Access sessions and prompt for reauthentication for any <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/">Cloudflare One Client session policies</a>.</li>
<li><strong>Remove user seat on deprovision</strong>: <a href="/cloudflare-one/team-and-resources/users/seat-management/">Remove a user's seat</a> from your Cloudflare One account when they are removed from the SCIM application in JumpCloud.</li>
<li><strong>SCIM identity update behavior</strong>: Choose what happens in Cloudflare One when the user's identity updates in JumpCloud.
<ul>
<li><em>Automatic identity updates</em>: Automatically update the <a href="/cloudflare-one/team-and-resources/users/users/">User Registry identity</a> when JumpCloud sends an updated identity or group membership through SCIM. This identity is used for Gateway policies and Cloudflare One Client <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profiles</a>; Access will read the user's updated identity when they reauthenticate.</li>
<li><em>Group membership change reauthentication</em>: <a href="/cloudflare-one/access-controls/access-settings/session-management/#per-user">Revoke a user's active session</a> when their group membership changes in JumpCloud. This will invalidate all active Access sessions and prompt for reauthentication for any <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/">Cloudflare One Client session policies</a>. Access will read the user's updated group membership when they reauthenticate.</li>
<li><em>No action</em>: Update the user's identity the next time they reauthenticate to Access or the Cloudflare One Client.</li>
</ul>
</li>
</ul>
<ol start="5">
<li>
<p>Select <strong>Regenerate Secret</strong>. Copy the <strong>SCIM Endpoint</strong> and <strong>SCIM Secret</strong>. You will need to enter these values into JumpCloud.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>The SCIM secret never expires, but you can manually regenerate the secret at any time.</p>
<h3 id="2-configure-scim-in-jumpcloud"><ol start="2">
<li>Configure SCIM in JumpCloud</li>
</ol></h3>
<ol>
<li>In the <a href="https://console.jumpcloud.com/#/home">JumpCloud Admin Portal</a>, go to <strong>SSO Applications</strong>.</li>
<li>Select the Cloudflare application that was created when you <a href="/cloudflare-one/integrations/identity-providers/jumpcloud-saml/#set-up-jumpcloud-as-a-saml-provider">Set up JumpCloud as a SAML provider</a>.</li>
<li>Select the <strong>SSO</strong> tab.</li>
<li>To provision user groups, select <strong>Include group attribute</strong> and enter <code>groups</code>. The group attribute name has to exactly match <code>groups</code> or else it will be sent as a SAML attribute.</li>
<li>Select the <strong>Identity Management</strong> tab.</li>
<li>Make sure that <strong>Enable management of User Groups and Group Membership in this application</strong> is turned on.</li>
<li>Select <strong>Configure</strong>.</li>
<li>In the <strong>Base URL</strong> field, enter the <strong>SCIM Endpoint</strong> obtained from Cloudflare One.</li>
<li>In the <strong>Token Key</strong> field, enter the <strong>SCIM Secret</strong> obtained from Cloudflare One.</li>
<li>Select <strong>Activate</strong>. You will receive a confirmation that the Identity Management integration has been successfully verified.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>To check if user identities were updated in Cloudflare One, view your <a href="/cloudflare-one/insights/logs/dashboard-logs/scim-logs/">SCIM provisioning logs</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5043.md")
</aside>
<h3 id="provisioning-attributes">Provisioning attributes</h3>
<p>Provisioning attributes define the user and group properties that JumpCloud will synchronize with Cloudflare Access. By default, JumpCloud will send the following attributes during a SCIM update event:</p>
<table>
<thead>
<tr>
<th>JumpCloud user attribute</th>
<th>Cloudflare Access attribute</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>email</code></td>
<td><code>email</code></td>
</tr>
<tr>
<td><code>firstname</code></td>
<td><code>givenName</code></td>
</tr>
<tr>
<td><code>lastname</code></td>
<td><code>surname</code></td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>JumpCloud group attribute</th>
<th>Cloudflare Access attribute</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>name</code></td>
<td><code>groups</code></td>
</tr>
</tbody>
</table>
<h2 id="example-api-configuration">Example API configuration</h2>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;config&quot;: {&#10;		&quot;issuer_url&quot;: &quot;jumpcloud&quot;,&#10;		&quot;sso_target_url&quot;: &quot;https://sso.myexample.jumpcloud.com/saml2/cloudflareaccess&quot;,&#10;		&quot;attributes&quot;: [&quot;email&quot;, &quot;name&quot;, &quot;username&quot;],&#10;		&quot;email_attribute_name&quot;: &quot;&quot;,&#10;		&quot;sign_request&quot;: false,&#10;		&quot;idp_public_cert&quot;: &quot;MIIDpDCCAoygAwIBAgIGAV2ka+55MA0GCSqGSIb3DQEBCwUAMIGSMQswCQYDVQQGEwJVUzETMBEG\nA1UEC.....GF/Q2/MHadws97cZg\nuTnQyuOqPuHbnN83d/2l1NSYKCbHt24o&quot;&#10;	},&#10;	&quot;type&quot;: &quot;saml&quot;,&#10;	&quot;name&quot;: &quot;jumpcloud saml example&quot;&#10;}&#10;</code></pre>
