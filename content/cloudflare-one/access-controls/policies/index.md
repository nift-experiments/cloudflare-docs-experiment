---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/policies/
  description: Configure Policies in Access.
  full_title: Access policies · Cloudflare One docs
  head_html: <title>Access policies · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure Policies in Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/policies/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/policies/index.md"><meta property="og:title" content="Access policies · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure Policies in Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/policies/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/policies/#page","headline":"Access policies \u00b7 Cloudflare One docs","description":"Configure Policies in Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/policies/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/policies/
  schema: 1
---
<p>Cloudflare Access determines who can reach your application by applying the Access policies you configure.</p>
<p>Every Access policy has four building blocks:</p>
<ul>
<li><a href="#actions"><strong>Actions</strong></a>: What happens when a user matches the policy (Allow, Block, Bypass, or Service Auth)</li>
<li><a href="#rule-types"><strong>Rule types</strong></a>: How criteria are combined (Include, Require, or Exclude)</li>
<li><a href="#selectors"><strong>Selectors</strong></a>: The attributes being checked (for example, email domain, country, or device posture)</li>
<li><strong>Values</strong>: The specific values to match against (for example, <code>@example.com</code>)</li>
</ul>
<h2 id="cloudflare-access-policy-actions">Cloudflare Access policy actions</h2>
<p>Actions let you grant or deny permission to a certain user or user group. You can set only one action per policy.</p>
<h3 id="allow">Allow</h3>
<p>The Allow action in Cloudflare Access allows users that meet certain criteria to reach an application behind Access.</p>
<p>The following table shows an example Cloudflare Access Allow policy that lets any user with an <code>@example.com</code> email address, as validated against an IdP, reach the application:</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>Rule type</th>
<th>Selector</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Allow</td>
<td>Include</td>
<td>Emails ending in</td>
<td><code>@example.com</code></td>
</tr>
</tbody>
</table>
<p>You can add a Require rule in the same policy action to enforce additional checks. Finally, if the policy contains an Exclude rule, users meeting that definition are prevented from reaching the application.</p>
<p>For example, the following table shows an Allow policy with Require and Exclude rules. This configuration lets any user from Portugal with an <code>@team.com</code> email address, as validated against an IdP, reach the application, except for <code>user-1</code> and <code>user-2</code>:</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>Rule type</th>
<th>Selector</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Allow</td>
<td>Include</td>
<td>Country</td>
<td><code>Portugal</code></td>
</tr>
<tr>
<td></td>
<td>Require</td>
<td>Emails Ending In</td>
<td><code>@team.com</code></td>
</tr>
<tr>
<td></td>
<td>Exclude</td>
<td>Email</td>
<td><code>user-1@team.com</code>, <code>user-2@team.com</code></td>
</tr>
</tbody>
</table>
<h3 id="block">Block</h3>
<p>The Block action in Cloudflare Access prevents users who meet certain criteria from reaching an application. For example, the following table shows a Block policy that blocks requests from Russian source IPs that are not on your <a href="/cloudflare-one/reusable-components/lists/">list of approved IPs</a>.</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>Rule type</th>
<th>Selector</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Block</td>
<td>Include</td>
<td>Country</td>
<td><code>Russian Federation</code></td>
</tr>
<tr>
<td></td>
<td>Exclude</td>
<td>IP list</td>
<td><code>Corporate IP allowlist</code></td>
</tr>
</tbody>
</table>
<p>Block policies are best used in conjunction with <a href="#allow">Allow policies</a> as a way to carve out exceptions in those Allow policies. Since Access is deny by default, users who do not match a Block policy will still be denied access unless they explicitly match an Allow policy.</p>
<h3 id="bypass">Bypass</h3>
<p>The Bypass action in Cloudflare Access disables Access enforcement for specific traffic.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/4587.md")
</aside>
<p>The Bypass action disables any Access enforcement for traffic that meets the defined rule criteria. Bypass is typically used to enable applications that require specific endpoints to be public.</p>
<p>For example, some applications have an endpoint under the <code>/admin</code> route that must be publicly routable. In this situation, you could create an Access application for the domain <code>test.example.com/admin/&lt;your-url&gt;</code> and add the Bypass policy shown in the following table:</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>Rule type</th>
<th>Selector</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Bypass</td>
<td>Include</td>
<td>Everyone</td>
<td><code>Everyone</code></td>
</tr>
</tbody>
</table>
<p>As part of implementing a Zero Trust security model, Cloudflare does not recommend using Bypass to grant direct permanent access to your internal applications. To enable seamless and secure access for on-network employees, use Cloudflare Tunnel to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/">connect your private network</a> and have users connect through the Cloudflare One Client.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4586.md")
</aside>
<h4 id="bypass-policy-product-incompatibility">Bypass policy product incompatibility</h4>
<p>Bypass policies which contain <a href="/cloudflare-one/reusable-components/posture-checks/">device posture check</a> rules will not function when:</p>
<ul>
<li><a href="/zaraz/">Zaraz</a> is enabled for the zone protected by Access</li>
<li>A <a href="/workers/">Worker</a> intercepts the request</li>
</ul>
<p>To work around these limitations and bypass Access, we recommend changing the policy action to <a href="#service-auth">Service Auth</a>.</p>
<h3 id="service-auth">Service Auth</h3>
<p>Service Auth rules in Cloudflare Access enforce authentication flows that do not require an identity provider IdP login, such as service tokens and mutual TLS.</p>
<p>The following table shows an example Cloudflare Access Service Auth policy configuration:</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>Rule type</th>
<th>Selector</th>
</tr>
</thead>
<tbody>
<tr>
<td>Service Auth</td>
<td>Include</td>
<td>Valid certificate</td>
</tr>
</tbody>
</table>
<h2 id="cloudflare-access-rule-types">Cloudflare Access rule types</h2>
<p>Rule types work like logical operators and determine how your criteria are combined to evaluate a user. All Access policies must contain at least one Include rule. This Include rule defines the initial pool of eligible users who can access an application. You can then add Exclude and Require rules to narrow the scope.</p>
<h3 id="include">Include</h3>
<p>The Include rule in Cloudflare Access is similar to an OR logical operator. In case more than one Include rule is specified, users need to meet only one of the criteria.</p>
<h3 id="exclude">Exclude</h3>
<p>The Exclude rule in Cloudflare Access works like a NOT logical operator. A user meeting any Exclusion criteria will not be allowed access to the application.</p>
<h3 id="require">Require</h3>
<p>The Require rule in Cloudflare Access works like an AND logical operator. A user must meet all specified Require rules to be allowed access.</p>
<h4 id="require-rules-with-or-operators">Require rules with OR operators</h4>
<p>By default, any values added to a Require rule are concatenated by an AND operator. For example, let's say you want to grant access to an application to both the full-time employees and the contractors, and only the ones based in specific countries — say Portugal and the United States. If you set up a rule with the following configuration:</p>
<table>
<thead>
<tr>
<th>Action</th>
<th>Rule type</th>
<th>Selector</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Allow</td>
<td>Require</td>
<td>Country</td>
<td><code>United States</code>, <code>Portugal</code></td>
</tr>
<tr>
<td></td>
<td>Require</td>
<td>Emails ending in</td>
<td><code>@cloudflare.com</code>, <code>@contractors.com</code></td>
</tr>
</tbody>
</table>
<p>This policy requires the user to be in the United States AND Portugal simultaneously, and have an email ending in both <code>@cloudflare.com</code> AND <code>@contractors.com</code>. Therefore, nobody will have access to the application.</p>
<p><strong>Solution:</strong> Use a <a href="/cloudflare-one/access-controls/policies/groups/">rule group</a> to convert AND logic to OR logic within a Require rule.</p>
<ol>
<li>Create a rule group called <code>Country requirements</code> that includes users in Portugal OR the United States:</li>
</ol>
<table>
<thead>
<tr>
<th>Rule type</th>
<th>Selector</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Include</td>
<td>Country</td>
<td><code>United States</code>, <code>Portugal</code></td>
</tr>
</tbody>
</table>
<ol start="2">
<li>Create a policy that requires the rule group, and that also includes users with emails ending in either <code>@cloudflare.com</code> OR <code>@contractors.com</code>:</li>
</ol>
<table>
<thead>
<tr>
<th>Action</th>
<th>Rule type</th>
<th>Selector</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Allow</td>
<td>Require</td>
<td>Rule group</td>
<td><code>Country requirements</code></td>
</tr>
<tr>
<td></td>
<td>Include</td>
<td>Emails ending in</td>
<td><code>@cloudflare.com</code>, <code>@contractors.com</code></td>
</tr>
</tbody>
</table>
<h2 id="cloudflare-access-selectors">Cloudflare Access selectors</h2>
<p>When you add a rule to your Cloudflare Access policy, you will be asked to specify the criteria, or attributes, you want users to meet. These attributes are available for all Access application types, including <a href="/cloudflare-one/access-controls/applications/http-apps/saas-apps/">SaaS</a>, <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted</a>, and <a href="/cloudflare-one/access-controls/applications/non-http/">non-HTTP</a> applications.</p>
<p>Non-identity attributes are polled continuously, meaning they are evaluated with each new HTTP request for changes during the <a href="/cloudflare-one/access-controls/access-settings/session-management/">user session</a>. If you have configured <a href="/cloudflare-one/team-and-resources/users/scim/">SCIM provisioning</a>, you can force a user to re-attest all attributes with Access whenever you revoke the user in the IdP or update their IdP group membership.</p>
<table>
<thead>
<tr>
<th>Selector</th>
<th>Description</th>
<th>Checked at login</th>
<th>Checked continuously<sup>1</sup></th>
<th>Identity-based selector?</th>
</tr>
</thead>
<tbody>
<tr>
<td>Emails</td>
<td><code>you@company.com</code></td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>Emails ending in</td>
<td><code>@company.com</code></td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>External Evaluation</td>
<td>Allows or denies access based on <a href="/cloudflare-one/access-controls/policies/external-evaluation/">custom logic</a> in an external API.</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>IP ranges</td>
<td><code>192.168.100.1/24</code> (supports IPv4/IPv6 addresses and CIDR ranges)</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>Country</td>
<td>Uses the IP address to determine country.</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>Everyone</td>
<td>Allows, denies, or bypasses access to everyone.</td>
<td>✅</td>
<td>❌</td>
<td>❌</td>
</tr>
<tr>
<td>Common Name</td>
<td>The request will need to present a valid certificate with an expected common name.</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>Valid Certificate</td>
<td>The request will need to present any valid client certificate.</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>Service Token</td>
<td>The request will need to present the correct service token headers configured for the specific application. Requires the <a href="#service-auth">Service Auth</a> action.</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>Any Access Service Token</td>
<td>The request will need to present the headers for any <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">service token</a> created for this account. Requires the <a href="#service-auth">Service Auth</a> action.</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>User Risk Score</td>
<td>The user's current <a href="/cloudflare-one/team-and-resources/users/risk-score/">risk score</a> (Low, Medium, High, or Unscored). Matches only the values selected in the rule. This selector only displays for Enterprise plans.</td>
<td>✅</td>
<td>✅</td>
<td>✅</td>
</tr>
<tr>
<td>Linked App Token</td>
<td>Checks for a valid <a href="/cloudflare-one/access-controls/applications/linked-app-token/">OAuth access token</a> issued to a specific Access application. Requires the <a href="#service-auth">Service Auth</a> action.</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>Login Methods</td>
<td>Checks the identity provider used at the time of login.</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>Authentication Method</td>
<td>Checks the <a href="/cloudflare-one/access-controls/policies/mfa-requirements/#identity-provider-based-mfa">multi-factor authentication</a> method used by the user, if supported by the identity provider. To enforce MFA independently of your IdP, refer to <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/">independent MFA</a>.</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>Identity provider group</td>
<td>Checks the user groups configured with your identity provider (IdP). This selector only displays if you use Microsoft Entra ID, GitHub, Google, Okta, or an IdP that provisions groups with <a href="/cloudflare-one/team-and-resources/users/scim/">SCIM</a>.</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>SAML Group</td>
<td>Checks a SAML attribute name / value pair. This selector only displays if you use a <a href="/cloudflare-one/integrations/identity-providers/generic-saml/">generic SAML</a> identity provider.</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>OIDC Claim</td>
<td>Checks an OIDC claim name / value pair. This selector only displays if you use a <a href="/cloudflare-one/integrations/identity-providers/generic-oidc/">generic OIDC</a> identity provider.</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
</tr>
<tr>
<td>Device posture</td>
<td>Checks device posture signals from the Cloudflare One Client or a third-party service provider. This selector only displays after you create a <a href="/cloudflare-one/reusable-components/posture-checks/">device posture check</a>.</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>Warp</td>
<td>Checks that the device is connected to the Cloudflare One Client, including the consumer version. This selector only displays after you enable the <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/require-warp/">WARP posture check</a>.</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>Gateway</td>
<td>Checks that the device is connected to your Zero Trust instance through the Cloudflare One Client. This selector only displays after you enable the <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/require-gateway/">Gateway posture check</a>.</td>
<td>✅</td>
<td>✅</td>
<td>❌</td>
</tr>
<tr>
<td>Cloudflare Account Member</td>
<td>Checks that the user is a member of a specific Cloudflare account. If no account ID is specified, defaults to the current account. This selector only displays if you use the <a href="/cloudflare-one/integrations/identity-providers/cloudflare/">Cloudflare</a> identity provider.</td>
<td>✅</td>
<td>❌</td>
<td>✅</td>
</tr>
</tbody>
</table>
<p><sup>1</sup> For SaaS applications, Access can only enforce policies at the time
of initial sign on and when reissuing the SaaS session. Once the user has
authenticated to the SaaS app, session management falls solely within the
purview of the SaaS app.</p>
<h2 id="connection-context-in-cloudflare-access">Connection context in Cloudflare Access</h2>
<p>Connection context settings allow you to control how users interact with an application after they have been granted access. While <a href="#selectors">selectors</a> determine who can access an application, connection context settings determine what actions users can take during their session. The available connection context settings depend on the application type.</p>
<p>Connection context is configured per policy, allowing you to grant different permissions to different groups of users. For example, you could allow full-time employees to copy data from a remote RDP session while restricting contractors to read-only access.</p>
<table>
<thead>
<tr>
<th>Application type</th>
<th>Available settings</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">Infrastructure (SSH)</a></td>
<td>Allowed UNIX usernames</td>
</tr>
<tr>
<td><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/#connection-settings">Browser-based RDP</a></td>
<td>Clipboard controls, file transfer controls</td>
</tr>
</tbody>
</table>
<h2 id="cloudflare-access-policy-order-of-execution">Cloudflare Access policy order of execution</h2>
<p>Cloudflare Access policies are evaluated based on their action type and order you set. Bypass and Service Auth policies are evaluated first, from top to bottom as shown in the UI. Then, Block and Allow policies are evaluated based on their order from top to bottom.</p>
<p>For example, if you have policies arranged as follows:</p>
<ul>
<li>Allow A</li>
<li>Block B</li>
<li>Service Auth C</li>
<li>Bypass D</li>
<li>Allow E</li>
</ul>
<p>The policies will execute in this order: Service Auth C &gt; Bypass D &gt; Allow A &gt; Block B &gt; Allow E. Once a user matches an Allow or Block policy, evaluation stops and no subsequent policies can override the decision.</p>
<h2 id="common-cloudflare-access-misconfigurations">Common Cloudflare Access misconfigurations</h2>
<p>If you add any of the following rules to an Allow policy, anyone will be able to access your application.</p>
<h3 id="include-everyone">Include everyone</h3>
<p>The following table shows a Cloudflare Access policy that includes everyone:</p>
<table>
<thead>
<tr>
<th>Rule type</th>
<th>Selector</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Include</td>
<td>Everyone</td>
<td><code>Everyone</code></td>
</tr>
</tbody>
</table>
<h3 id="include-all-valid-emails">Include all valid emails</h3>
<p>The following table shows a Cloudflare Access policy that includes all users with valid email login methods:</p>
<table>
<thead>
<tr>
<th>Rule type</th>
<th>Selector</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Include</td>
<td>Login Methods</td>
<td><code>One-time PIN</code></td>
</tr>
</tbody>
</table>
<h2 id="additional-cloudflare-access-resources">Additional Cloudflare Access resources</h2>
<p><a href="/cloudflare-one/api-terraform/">API and Terraform</a> provide programmatic ways to manage your Access policies and configurations.</p>
