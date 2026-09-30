---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/
  description: Reference information for Identity-based policies in Gateway.
  full_title: Identity-based policies · Cloudflare One docs
  head_html: <title>Identity-based policies · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Reference information for Identity-based policies in Gateway."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/index.md"><meta property="og:title" content="Identity-based policies · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Reference information for Identity-based policies in Gateway."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="OIDC,SAML,SCIM"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/#page","headline":"Identity-based policies \u00b7 Cloudflare One docs","description":"Reference information for Identity-based policies in Gateway.","url":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["OIDC","SAML","SCIM"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/traffic-policies/identity-selectors/
  schema: 1
---
<p>With Cloudflare One, you can create Secure Web Gateway policies that filter outbound traffic down to the user identity level. To do that, you can build DNS, HTTP or Network policies using a set of <a href="#identity-based-selectors">identity-based selectors</a>. These selectors require you to deploy the Cloudflare One Client in <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/">Traffic and DNS mode</a>.</p>
<p>For example, you can create different security rules for different teams — block social media for contractors but allow it for marketing.</p>
<p>You may also filter outbound traffic based on additional signals from <a href="/cloudflare-one/reusable-components/posture-checks/">device posture checks</a>.</p>
<h2 id="gateway-identity-checks">Gateway identity checks</h2>
<p>Gateway checks identity when a user logs in or re-authenticates. To check your users' identities and require re-authentication at regular intervals, you can <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/">enforce a Cloudflare One Client session duration</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/4411.md")
</aside>
<p>There are two ways a user can re-authenticate:</p>
<ul>
<li>Log out from an Access-protected application and log back in.</li>
<li>In the Cloudflare One Client, re-authenticate the session by going to <strong>Profile</strong> &gt; <strong>Account information</strong> &gt; <strong>Re-authenticate</strong> <sup><a href="#footnote-1">1</a></sup>. This will open a browser window and prompt the user to log in.</li>
</ul>
<p>To view the identity that Gateway will use when evaluating policies, check the <a href="/cloudflare-one/team-and-resources/users/users/">user registry</a>.</p>
<h3 id="automatic-scim-idp-updates">Automatic SCIM IdP updates</h3>
<p>Gateway will automatically detect changes in user name, title, and group membership for IdPs configured with System for Cross-domain Identity Management (SCIM) provisioning. For more information, refer to <a href="/cloudflare-one/team-and-resources/users/scim/">SCIM provisioning</a>.</p>
<h3 id="extended-email-addresses">Extended email addresses</h3>
<p>Extended email addresses (also known as plus addresses) are variants of an existing email address with <code>+</code> or <code>.</code> modifiers. Many email providers, such as Gmail and Outlook, deliver emails intended for an extended address to its original address. For example, providers will deliver emails sent to <code>contact+123@example.com</code> or <code>con.tact@example.com</code> to <code>contact@example.com</code>.</p>
<p>By default, Gateway will either filter only exact matches or all extended variants depending on the type of policy and action used:</p>
<details class="nb-details"><summary>DNS policies</summary><div class="nb-details-body">
@input("content/.markup/bodies/4412.md")
</div></details>
<details class="nb-details"><summary>Network policies</summary><div class="nb-details-body">
@input("content/.markup/bodies/4413.md")
</div></details>
<details class="nb-details"><summary>HTTP policies</summary><div class="nb-details-body">
@input("content/.markup/bodies/4414.md")
</div></details>
<details class="nb-details"><summary>Other policies</summary><div class="nb-details-body">
@input("content/.markup/bodies/4415.md")
</div></details>
<p>To force Gateway to match all email address variants, go to <strong>Traffic policies</strong> &gt; <strong>Traffic settings</strong> &gt; <strong>Policy settings</strong> and turn on <strong>Match extended email addresses</strong>. This setting applies to all firewall, egress, and resolver policies.</p>
<h2 id="identity-based-selectors">Identity-based selectors</h2>
<h3 id="oidc-claims">OIDC Claims</h3>
<p>Specify a value from a <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/#custom-oidc-claims">custom OIDC claim</a> configured on your identity provider.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4410.md")
</aside>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>OIDC Claims</td>
<td><code>any(identity.oidc_claims[*] == &quot;\&quot;department=engineering\&quot;&quot;)</code></td>
</tr>
</tbody>
</table>
<h3 id="saml-attributes">SAML Attributes</h3>
<p>Specify a value from the SAML Attribute Assertion.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>SAML Attributes</td>
<td><code>identity.saml_attributes == &quot;\&quot;group=finance\&quot;&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="user-email">User Email</h3>
<p>Use this selector to create identity-based Gateway policies based on a user's email.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example value</th>
</tr>
</thead>
<tbody>
<tr>
<td>User Email</td>
<td><code>identity.email == &quot;user-name@company.com&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="user-group-ids">User Group IDs</h3>
<p>Use this selector to create identity-based Gateway policies based on an IdP group ID of which the user is configured as a member in the IdP.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>User Group IDs</td>
<td><code>identity.groups.id == &quot;12jf495bhjd7893ml09o&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="user-group-email">User Group Email</h3>
<p>Use this selector to create identity-based Gateway policies based on an IdP group email address of which the user is configured as a member in the IdP.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>User Group Email</td>
<td><code>identity.groups.email == &quot;contractors@company.com&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="user-group-names">User Group Names</h3>
<p>Use this selector to create identity-based Gateway policies based on an IdP group name of which the user is configured as a member in the IdP.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>User Group Names</td>
<td><code>identity.groups.name == &quot;\&quot;finance\&quot;&quot;</code></td>
</tr>
</tbody>
</table>
<h3 id="user-name">User Name</h3>
<p>Use this selector to create identity-based Gateway policies based on an IdP username for a particular user in the IdP.</p>
<table>
<thead>
<tr>
<th>UI name</th>
<th>API example</th>
</tr>
</thead>
<tbody>
<tr>
<td>User Name</td>
<td><code>identity.name == &quot;user-name&quot;</code></td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="gateway-groups-vs-access-rule-groups">Gateway groups vs. Access rule groups</h3>
@markup("md", "content/.markup/bodies/4409.md")
</aside>
<h2 id="idp-groups-in-gateway">IdP groups in Gateway</h2>
<p>Cloudflare Gateway can integrate with your organization's identity providers (IdPs). Before building a Gateway policy for IdP users or groups, be sure to <a href="/cloudflare-one/integrations/identity-providers/">add the IdP as an authentication method</a>.</p>
<p>Because IdPs expose user groups in different formats, reference the list below to choose the appropriate identity-based selector.</p>
<h3 id="microsoft-entra-id">Microsoft Entra ID</h3>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>User Group IDs</td>
<td><code>61503835-b6fe-4630-af88-de551dd59a2</code></td>
</tr>
</tbody>
</table>
<p><strong>Value</strong> is the <a href="/cloudflare-one/integrations/identity-providers/entra-id/#entra-groups-in-zero-trust-policies">Object Id</a> for an Entra group.</p>
<p>If you enabled user and group synchronization with <a href="/cloudflare-one/integrations/identity-providers/entra-id/#synchronize-users-and-groups">SCIM</a>, the synchronized groups will appear under <em>User Group Names</em>:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>User Group Names</td>
<td><code>SCIM group</code></td>
</tr>
</tbody>
</table>
<h3 id="github">GitHub</h3>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>User Group Names</td>
<td><code>Marketing</code></td>
</tr>
</tbody>
</table>
<h3 id="google">Google</h3>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>User Group Names</td>
<td><code>Marketing</code></td>
</tr>
</tbody>
</table>
<h3 id="okta-oidc">Okta (OIDC)</h3>
<p>If you added Okta as an <a href="/cloudflare-one/integrations/identity-providers/okta/">OIDC provider</a>, use the User Group Names selector:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>User Group Names</td>
<td><code>Marketing</code></td>
</tr>
</tbody>
</table>
<p>The Okta OIDC integration supports user and group synchronization with <a href="/cloudflare-one/integrations/identity-providers/okta/#synchronize-users-and-groups">SCIM</a>.</p>
<h3 id="okta-saml">Okta (SAML)</h3>
<p>If you added Okta as a <a href="/cloudflare-one/integrations/identity-providers/okta-saml/">SAML provider</a>, use the SAML Attributes selector:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Attribute name</th>
<th>Attribute value</th>
</tr>
</thead>
<tbody>
<tr>
<td>SAML Attributes</td>
<td><code>groups</code></td>
<td><code>Marketing</code></td>
</tr>
</tbody>
</table>
<h3 id="generic-saml-idp">Generic SAML IdP</h3>
<p>For a <a href="/cloudflare-one/integrations/identity-providers/generic-saml/">generic SAML provider</a>, use the SAML Attribute selector:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Attribute name</th>
<th>Attribute value</th>
</tr>
</thead>
<tbody>
<tr>
<td>SAML Attributes</td>
<td><code>department</code></td>
<td><code>Marketing</code></td>
</tr>
</tbody>
</table>
<h3 id="generic-oidc-idp">Generic OIDC IdP</h3>
<p>For a <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/">generic OIDC provider</a>, use the OIDC Claims selector to filter traffic based on <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/#custom-oidc-claims">custom OIDC claims</a> configured on your IdP:</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Claim name</th>
<th>Claim value</th>
</tr>
</thead>
<tbody>
<tr>
<td>OIDC Claims</td>
<td><code>department</code></td>
<td><code>Engineering</code></td>
</tr>
</tbody>
</table>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">In Cloudflare One Client version 2026.1 and earlier, select **Preferences** > **Account** > **Re-Authenticate Session**.</li></ol></section>
