---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-saml/
  description: Generic SAML 2.0 in Zero Trust integrations.
  full_title: Generic SAML 2.0 · Cloudflare One docs
  head_html: <title>Generic SAML 2.0 · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Generic SAML 2.0 in Zero Trust integrations."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-saml/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-saml/index.md"><meta property="og:title" content="Generic SAML 2.0 · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Generic SAML 2.0 in Zero Trust integrations."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-saml/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-saml/#page","headline":"Generic SAML 2.0 \u00b7 Cloudflare One docs","description":"Generic SAML 2.0 in Zero Trust integrations.","url":"https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/generic-saml/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/integrations/identity-providers/generic-saml/
  schema: 1
---
<p>Cloudflare One integrates with any identity provider that supports SAML 2.0. If your identity provider is not listed in the integration list of login methods in Cloudflare One, it can be configured using SAML 2.0 (or OpenID if OIDC based). Generic SAML can also be used if you would like to pass additional SAML headers or claims for an IdP in the integration list.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Minimum requirements for identity providers:</p>
<ul>
<li>The IdP must conform to SAML 2.0.</li>
<li>The IdP must provide a <strong>Single sign-on URL</strong>, an <strong>Entity ID or Issuer URL</strong>, and a <strong>Signing certificate</strong>.</li>
<li>The IdP must include the signing public key in the SAML response.</li>
</ul>
<h2 id="1-create-an-application-in-your-identity-provider"><ol>
<li>Create an application in your identity provider</li>
</ol></h2>
<p>Most identity providers allow users to create an <strong>Application</strong>. In this context, an application is a set of parameters that the identity provider will then pass on to Cloudflare to establish an integration.</p>
<p>The typical setup requirements are:</p>
<ol>
<li>Create a new integration in the identity provider with the type set as <strong>SAML</strong>.</li>
<li>Set both the <strong>Entity/Issuer ID</strong> and the <strong>Single sign-on URL</strong> to:</li>
</ol>
<pre tabindex="0"><code class="language-txt">https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback&#10;</code></pre>
<p>You can find your team name in the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> under <strong>Settings</strong> &gt; <strong>Team name and domain</strong> &gt; <strong>Team name</strong>.</p>
<ol start="3">
<li>Set the <strong>Name ID/Email format</strong> to <code>emailAddress</code>.</li>
<li>(Optional) Set the signature policy to <em>Always Sign</em>.</li>
</ol>
<h3 id="optional-upload-saml-metadata">(Optional) Upload SAML metadata</h3>
<p>If your identity provider supports metadata file configuration, you can use the default or identity provider specific metadata endpoint:</p>
<ul>
<li><strong>Default:</strong> <code>https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/saml-metadata</code></li>
<li><strong>Identity provider specific:</strong> <code>https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/&lt;identity-provider-id&gt;/saml-metadata</code>, where <code>&lt;identity-provider-id&gt;</code> is the <code>id</code> value obtained from <a href="/api/resources/zero_trust/subresources/identity_providers/methods/list/">List Access identity providers</a>. Use this endpoint if your IdP requires a configuration not defined in the default metadata file.</li>
</ul>
<p>To download the SAML metadata file, copy-paste the metadata endpoint into a web browser and save the page as an <code>.xml</code> file. Upload this XML file to the identity provider.</p>
<h2 id="2-add-a-saml-identity-provider-to-cloudflare-one"><ol start="2">
<li>Add a SAML identity provider to Cloudflare One</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5067.md")
</div></div>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5064.md")
</aside>
<h2 id="3-test-the-connection"><ol start="3">
<li>Test the connection</li>
</ol></h2>
<p>You can now <a href="/cloudflare-one/integrations/identity-providers/#test-idps-in-cloudflare-one">test the IdP integration</a>. A success response should return the configured SAML attributes.</p>
<h2 id="synchronize-users-and-groups">Synchronize users and groups</h2>
<p>The generic SAML integration allows you to synchronize user groups and automatically deprovision users using <a href="/cloudflare-one/team-and-resources/users/scim/">SCIM</a>.</p>
<p>SCIM affects Access and Gateway policy evaluation differently.</p>
<p>Access evaluates a user's identity and group membership from the SAML assertion or OIDC token returned by the identity provider during authentication. SCIM provides readable group names in the Access policy builder, but Access does not use SCIM group membership to evaluate a login. If you turn on <strong>Enable user deprovisioning</strong>, removing a user from the SCIM application revokes their active Access sessions. You can also configure SCIM to revoke sessions after group membership changes. Access evaluates the updated identity provider data when the user authenticates again.</p>
<p>Gateway evaluates identity-based policies against the <a href="/cloudflare-one/team-and-resources/users/users/">User Registry identity</a>. SCIM updates this identity when users or group memberships change, without waiting for the user to authenticate again. Cloudflare One Client device profiles use the same synchronized identity.</p>
<h3 id="prerequisites-1">Prerequisites</h3>
<p>Your identity provider must support SCIM version 2.0.</p>
<h3 id="1-enable-scim-in-cloudflare-one"><ol>
<li>Enable SCIM in Cloudflare One</li>
</ol></h3>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</p>
</li>
<li>
<p>Find the IdP integration and select <strong>Edit</strong>.</p>
</li>
<li>
<p>Turn on <strong>Enable SCIM</strong>.</p>
</li>
<li>
<p>(Optional) Configure the following settings:</p>
</li>
</ol>
<ul>
<li><strong>Enable user deprovisioning</strong>: <a href="/cloudflare-one/access-controls/access-settings/session-management/#per-user">Revoke a user's active session</a> when they are removed from the SCIM application in IdP. This will invalidate all active Access sessions and prompt for reauthentication for any <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/">Cloudflare One Client session policies</a>.</li>
<li><strong>Remove user seat on deprovision</strong>: <a href="/cloudflare-one/team-and-resources/users/seat-management/">Remove a user's seat</a> from your Cloudflare One account when they are removed from the SCIM application in IdP.</li>
<li><strong>SCIM identity update behavior</strong>: Choose what happens in Cloudflare One when the user's identity updates in IdP.
<ul>
<li><em>Automatic identity updates</em>: Automatically update the <a href="/cloudflare-one/team-and-resources/users/users/">User Registry identity</a> when IdP sends an updated identity or group membership through SCIM. This identity is used for Gateway policies and Cloudflare One Client <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profiles</a>; Access will read the user's updated identity when they reauthenticate.</li>
<li><em>Group membership change reauthentication</em>: <a href="/cloudflare-one/access-controls/access-settings/session-management/#per-user">Revoke a user's active session</a> when their group membership changes in IdP. This will invalidate all active Access sessions and prompt for reauthentication for any <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/">Cloudflare One Client session policies</a>. Access will read the user's updated group membership when they reauthenticate.</li>
<li><em>No action</em>: Update the user's identity the next time they reauthenticate to Access or the Cloudflare One Client.</li>
</ul>
</li>
</ul>
<ol start="5">
<li>
<p>Select <strong>Regenerate Secret</strong>. Copy the <strong>SCIM Endpoint</strong> and <strong>SCIM Secret</strong>. You will need to enter these values into IdP.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<p>The SCIM secret never expires, but you can manually regenerate the secret at any time.</p>
<h3 id="2-configure-scim-in-the-idp"><ol start="2">
<li>Configure SCIM in the IdP</li>
</ol></h3>
<p>Setup instructions vary depending on the identity provider. In your identity provider, you will either need to edit the <a href="#1-create-an-application-in-your-identity-provider">original SSO application</a> or create a new SCIM application. Refer to your identity provider's documentation for more details. For example instructions, refer to our <a href="/cloudflare-one/integrations/identity-providers/okta/#synchronize-users-and-groups">Okta</a> or <a href="/cloudflare-one/integrations/identity-providers/jumpcloud-saml/#synchronize-users-and-groups">JumpCloud</a> guides.</p>
<h4 id="idp-groups">IdP groups</h4>
<p>If you would like to build policies based on IdP groups:</p>
<ul>
<li>Ensure that your IdP sends a <code>groups</code> field. The naming must match exactly (case insensitive). All other values will be sent as a SAML attribute.</li>
<li>If your IdP requires a new SCIM application, ensure that its groups match the groups in the <a href="/cloudflare-one/integrations/identity-providers/generic-saml/#1-create-an-application-in-your-identity-provider">original SSO application</a>. Matching the groups keeps the Gateway identity synchronized with the groups that the IdP returns when the user authenticates to Access.</li>
</ul>
<h3 id="3-verify-scim-provisioning"><ol start="3">
<li>Verify SCIM provisioning</li>
</ol></h3>
<p>To check if user identities were updated in Cloudflare One, view your <a href="/cloudflare-one/insights/logs/dashboard-logs/scim-logs/">SCIM provisioning logs</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5063.md")
</aside>
<h2 id="optional-configurations">Optional configurations</h2>
<p>SAML integrations support additional security and configuration options.</p>
<h3 id="encrypt-saml-assertions">Encrypt SAML assertions</h3>
<p>SAML assertion encryption ensures that SAML assertions sent from your identity provider to Cloudflare Access are encrypted end-to-end.</p>
<p>Without encryption, SAML assertions are transmitted in plaintext after TLS termination, which means they could be visible to browser extensions or client-side malware. With encryption turned on, your IdP encrypts the assertion using a public certificate from Cloudflare, and only Access can decrypt it with the corresponding private key.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/5062.md")
</aside>
<p>To turn on SAML assertion encryption:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</li>
<li>Select your SAML identity provider and select <strong>Edit</strong>.</li>
<li>Under <strong>SAML encryption</strong>, turn on the <strong>Enable SAML encryption</strong> toggle. Access will automatically generate an encryption certificate.</li>
<li>Copy the displayed certificate (in PEM format) or the certificate set ID.</li>
<li>In your identity provider, upload the Cloudflare encryption certificate and turn on assertion encryption. Refer to your IdP documentation for the exact configuration steps.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>After you turn on encryption, Access will reject any unencrypted assertions from the configured IdP. If you turn off encryption, Access will reject any encrypted assertions until encryption is turned back on.</p>
<h4 id="supported-encryption-algorithms">Supported encryption algorithms</h4>
<p>Access supports the following encryption algorithms:</p>
<table>
<thead>
<tr>
<th>Algorithm type</th>
<th>Supported values</th>
</tr>
</thead>
<tbody>
<tr>
<td>Content encryption</td>
<td>AES-128-CBC, AES-256-CBC, AES-128-GCM, AES-256-GCM</td>
</tr>
<tr>
<td>Key transport</td>
<td>RSA-OAEP (XML Encryption 1.0 and 1.1), RSA-1.5</td>
</tr>
</tbody>
</table>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5061.md")
</aside>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="fedramp-environments">FedRAMP environments</h3>
@markup("md", "content/.markup/bodies/5060.md")
</aside>
<h4 id="rotate-encryption-certificates">Rotate encryption certificates</h4>
<p>Encryption certificates are valid for one year. Thirty days before a certificate expires, Access automatically generates a replacement certificate. The expiring certificate remains valid until its expiration date, giving you time to upload the new certificate to your IdP.</p>
<p>To manually rotate a certificate:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Integrations</strong> &gt; <strong>Identity providers</strong>.</li>
<li>Select your SAML identity provider and select <strong>Edit</strong>.</li>
<li>Under <strong>SAML encryption</strong>, select <strong>Rotate certificate</strong>.</li>
<li>Upload the new certificate to your identity provider.</li>
</ol>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/5059.md")
</aside>
<h3 id="sign-saml-authentication-request">Sign SAML authentication request</h3>
<p>This optional configuration signs the <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/">Access JWT</a> with the Cloudflare Access public key to ensure that the JWT is coming from a legitimate source. The Cloudflare public key can be obtained at <code>https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/certs</code>.</p>
<h3 id="require-fresh-authentication-at-the-identity-provider">Require fresh authentication at the identity provider</h3>
<p>You can ask your identity provider to reauthenticate the user for every SAML authentication request. This option applies whether the request is signed or unsigned.</p>
<p>This setting is available through the API. First, retrieve the identity provider's current configuration from the <a href="/api/resources/zero_trust/subresources/identity_providers/methods/get/">Access identity provider endpoint</a>. Then, send the complete configuration to the <a href="/api/resources/zero_trust/subresources/identity_providers/methods/update/">update identity provider endpoint</a> with <code>force_authn</code> set to <code>true</code> in the <code>config</code> object. The default value is <code>false</code>.</p>
<p>When this option is turned on, Access sets <code>ForceAuthn</code> to <code>true</code> in each SAML authentication request. Access may also set <code>ForceAuthn</code> to <code>true</code> when a security check requires the user to reauthenticate, even if <code>force_authn</code> is <code>false</code>.</p>
<h3 id="email-attribute-name">Email attribute name</h3>
<p>Many <a href="/cloudflare-one/access-controls/policies/">Access policies</a> depend on a user's email address. Some identity providers have a different naming for the email address attribute (for example, <code>Email</code>, <code>e-mail</code>, <code>emailAddress</code>). This can typically be checked in the identity provider's SAML test option.</p>
<p>Example in Okta:</p>
<p><img src="/assets/upstream/images/cloudflare-one/identity/saml-assertion.png" alt="Preview the SAML assertion from the Okta dashboard" />
<img src="/assets/upstream/images/cloudflare-one/identity/saml-attributes.png" alt="Determine the email attribute name from the SAML assertion" /></p>
<h3 id="saml-headers-and-attributes">SAML headers and attributes</h3>
<p>Cloudflare Access supports SAML (Security Assertion Markup Language) attributes and SAML headers for all SAML IdP integrations.</p>
<p><a href="#saml-attributes"><strong>SAML attributes</strong></a> refer to specific data points or characteristics that the IdP shares about the authenticated user. These attributes often include details like email address, name, or role, and are passed along to the service provider upon successful authentication.</p>
<p><a href="#saml-headers"><strong>SAML headers</strong></a> are metadata in the SAML protocol communication which convey information about the sender, recipient, and the message itself. These headers can be leveraged to provide extra context or control over the communication.</p>
<h4 id="saml-attributes">SAML attributes</h4>
<p>SAML attributes are added to the <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/">Access JWT</a>. These attributes can then be consumed by self-hosted or SaaS applications connected to Access. Any SAML attribute configured in the SAML integration must also be sent from the IdP.</p>
<p>Example in Okta:</p>
<p><img src="/assets/upstream/images/cloudflare-one/identity/attribute-statements.png" alt="Configure Okta to send SAML attributes" /></p>
<p>How to receive these SAML attributes in Cloudflare:</p>
<p><img src="/assets/upstream/images/cloudflare-one/identity/attributes-cloudflare.png" alt="Configure Cloudflare to receive SAML attributes" /></p>
<h4 id="saml-headers">SAML headers</h4>
<p>If an application specifically requires SAML attributes upon sign-in, then the attributes can be passed as headers. The <strong>Attribute name</strong> should be the value coming from your IdP (for example, <code>department</code>). You can assign any <strong>Header name</strong> to the attribute. The header name will appear in the response headers when Access makes the initial authorization request to <code>https://&lt;your-team-name&gt;.cloudflareaccess.com/cdn-cgi/access/callback</code>.</p>
<h4 id="multi-record-saml-attributes">Multi-record SAML attributes</h4>
<p>Cloudflare Access extends support for multi-record SAML attributes such as groups. These attributes are parsed out and can be individually referenced in policies. This feature enables granular access control and precise user authorization in applications.</p>
<p>Cloudflare Access does not currently support partial attribute value references.</p>
