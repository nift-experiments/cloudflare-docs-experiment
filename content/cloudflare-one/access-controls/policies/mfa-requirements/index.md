---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/policies/mfa-requirements/
  description: Enforce MFA in Access.
  full_title: Enforce MFA · Cloudflare One docs
  head_html: <title>Enforce MFA · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Enforce MFA in Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/policies/mfa-requirements/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/policies/mfa-requirements/index.md"><meta property="og:title" content="Enforce MFA · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Enforce MFA in Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/policies/mfa-requirements/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML,JSON web token (JWT),Authentication"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/policies/mfa-requirements/#page","headline":"Enforce MFA \u00b7 Cloudflare One docs","description":"Enforce MFA in Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/policies/mfa-requirements/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML","JSON web token (JWT)","Authentication"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/policies/mfa-requirements/
  schema: 1
---
<p>Cloudflare Access supports two methods of enforcing multi-factor authentication (MFA):</p>
<ul>
<li><strong><a href="#identity-provider-based-mfa">Identity provider-based MFA</a></strong> — Require specific MFA methods reported by your identity provider (IdP).</li>
<li><strong><a href="#independent-mfa">Independent MFA</a></strong> — Prompt users for a second factor directly in Access, without relying on a third-party identity provider.</li>
</ul>
<p>For SSH connections to <a href="/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/">infrastructure applications</a>, Access also supports <a href="#infrastructure-applications">independent MFA with PIV and FIDO2 keys</a>.</p>
<h2 id="identity-provider-based-mfa">Identity provider-based MFA</h2>
<p>You can require that users log in with specific MFA methods provided by their identity provider. For example, you can create rules that only allow users to reach a given application if they authenticate with a security key through their IdP.</p>
<p>IdP-based MFA enforcement is only available with the following identity providers:</p>
<ul>
<li><a href="/cloudflare-one/integrations/identity-providers/okta/">Okta</a></li>
<li><a href="/cloudflare-one/integrations/identity-providers/entra-id/">Microsoft Entra ID (formerly Azure AD)</a></li>
<li><a href="/cloudflare-one/integrations/identity-providers/generic-oidc/">Generic OIDC</a></li>
<li><a href="/cloudflare-one/integrations/identity-providers/generic-saml/">Generic SAML 2.0</a></li>
</ul>
<p>To enforce an IdP MFA requirement on an application:</p>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Find the application for which you want to enforce MFA and select <strong>Configure</strong>. Alternatively, <a href="/cloudflare-one/access-controls/applications/http-apps/">create a new application</a>.</p>
</li>
<li>
<p>Go to <strong>Policies</strong>.</p>
</li>
<li>
<p>If your application already has a policy containing an identity requirement, find it and select <strong>Configure</strong>.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4579.md")
</aside>
<ol start="5">
<li>Add the following rule to the policy:</li>
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
<td>Require</td>
<td>Authentication method</td>
<td><code>mfa - multiple-factor authentication</code></td>
</tr>
</tbody>
</table>
<ol start="6">
<li>Save the policy.</li>
</ol>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/4578.md")
</aside>
<h3 id="authentication-methods-in-the-jwt">Authentication methods in the JWT</h3>
<p>When users authenticate with their identity provider, the IdP shares their username with Cloudflare Access. Access writes that value into the <span class="nb-glossary-tooltip" title="JSON web token">JSON Web Token (JWT)</span> generated for the user.</p>
<p>Certain identity providers also share the MFA method presented by the user. Access can add these values into the JWT. For example, if the user authenticated with their password and a security key, the IdP can send a confirmation to Cloudflare Access. Access then stores that method in the JWT issued to the user.</p>
<p>Cloudflare Access follows <a href="https://tools.ietf.org/html/rfc8176">RFC 8176</a>, Authentication Method Reference Values, to define authentication methods.</p>
<h2 id="independent-mfa">Independent MFA</h2>
<p>Independent MFA prompts users for a second factor directly in Access. This allows you to enforce MFA requirements without relying on your IdP's MFA configuration.</p>
<p>You can configure MFA requirements at three levels:</p>
<table>
<thead>
<tr>
<th>Level</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/cloudflare-one/access-controls/access-settings/independent-mfa/">Organization</a></td>
<td>Enforce MFA by default for all applications in your account.</td>
</tr>
<tr>
<td><a href="#configure-independent-mfa-for-an-application">Application</a></td>
<td>Require or turn off MFA for a specific application.</td>
</tr>
<tr>
<td><a href="#configure-independent-mfa-for-a-policy">Policy</a></td>
<td>Require or turn off MFA for users who match a specific policy.</td>
</tr>
</tbody>
</table>
<p>MFA settings use this precedence: <strong>Policy</strong> &gt; <strong>Application</strong> &gt; <strong>Organization</strong>.</p>
<h3 id="prerequisites">Prerequisites</h3>
<p>Before you configure independent MFA on applications or policies, you must <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/">turn on independent MFA</a> at the organization level.</p>
<aside class="nb-aside tip">
@markup("md", "content/.markup/bodies/4577.md")
</aside>
<h3 id="configure-independent-mfa-for-an-application">Configure independent MFA for an application</h3>
<p>Each application has three MFA options:</p>
<table>
<thead>
<tr>
<th>Option</th>
<th>Behavior</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Respect global enforcement setting</strong></td>
<td>Uses the <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/">organization-level</a> MFA configuration. If MFA is required globally, users must complete MFA. If MFA is not required globally, users are not prompted. This is the default.</td>
</tr>
<tr>
<td><strong>Custom MFA settings</strong></td>
<td>Overrides the organization setting with application-specific allowed authenticators and session duration.</td>
</tr>
<tr>
<td><strong>Disable MFA</strong></td>
<td>Users are not prompted for independent MFA when accessing this application, even if MFA is required globally.</td>
</tr>
</tbody>
</table>
<p>To configure MFA for an application:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Find the application you want to configure and select <strong>Configure</strong>.</li>
<li>Scroll down to <strong>Authentication</strong> and select the <strong>MFA</strong>.tab.</li>
<li>Select one of the following options:
<ul>
<li>To inherit the organization setting, select <strong>Respect global enforcement setting</strong>.</li>
<li>To set custom requirements, select <strong>Custom MFA settings</strong>, then configure the <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/#supported-mfa-methods">allowed MFA methods</a> and <a href="#mfa-session-duration">authentication duration</a>.</li>
<li>To exempt the application from MFA, select <strong>Disable MFA</strong>.</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>To configure MFA for an infrastructure application, refer to <a href="#infrastructure-applications">Infrastructure applications</a>.</p>
<h3 id="configure-independent-mfa-for-a-policy">Configure independent MFA for a policy</h3>
<p>Each policy has the same three MFA options described in <a href="#configure-independent-mfa-for-an-application">Configure independent MFA for an application</a>. Policy-level settings override application-level settings.</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Policies</strong>.</li>
<li>Choose an <strong>Allow</strong> policy and select <strong>Configure</strong>.</li>
<li>Under <strong>Multi-factor authentication (MFA)</strong>, select an option:
<ul>
<li>To inherit the application or organization setting, select <strong>Respect global enforcement setting</strong>.</li>
<li>To set custom requirements for users who match this policy, select <strong>Custom MFA settings</strong>, then configure the <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/#supported-mfa-methods">allowed MFA methods</a> and <a href="#mfa-session-duration">authentication duration</a>.</li>
<li>To exempt users who match this policy from MFA, select <strong>Disable MFA</strong>.</li>
</ul>
</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<p>To configure MFA for an infrastructure application policy, refer to <a href="#infrastructure-applications">Infrastructure applications</a>.</p>
<h3 id="mfa-session-duration">MFA session duration</h3>
<p>The MFA session duration determines how long a successful MFA authentication remains valid. After the MFA session expires, the user must complete MFA again on their next Cloudflare Access login in addition to completing IdP authentication. You can require users to complete MFA on each Access login or set a custom duration. MFA session durations are only checked during the login flow and do not affect a user's existing session.</p>
<p>Access checks MFA sessions from most specific to least specific:</p>
<ol>
<li><strong>Policy MFA session duration</strong> — If set, applies to users who match the policy.</li>
<li><strong>Application MFA session duration</strong> — If set, applies to all users accessing the application.</li>
<li><strong>Global MFA session duration</strong> — The default for all applications that do not specify their own duration.</li>
</ol>
<h4 id="require-mfa-on-every-login">Require MFA on every login</h4>
<p>To require MFA every time a user logs in to an application, set the authentication duration to <strong>Require every login</strong>. This prevents Access from caching a successful MFA session.</p>
<ul>
<li><strong>Organization</strong> — Go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Access settings</strong> &gt; <strong>Allow multi-factor authentication (MFA)</strong>. Set <strong>Authentication duration</strong> to <strong>Require every login</strong>. This applies to all applications unless overridden at the application or policy level. For more details, refer to <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/">independent MFA settings</a>.</li>
<li><strong>Application</strong> — Go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong> &gt; select your application &gt; <strong>Configure</strong> &gt; <strong>Authentication</strong> &gt; <strong>MFA</strong> tab. Select <strong>Custom MFA settings</strong> and set <strong>Authentication duration</strong> to <strong>Require every login</strong>.</li>
<li><strong>Policy</strong> — Go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Policies</strong> &gt; select your policy &gt; <strong>Configure</strong>. Under <strong>Multi-factor authentication (MFA)</strong>, select <strong>Custom MFA settings</strong> and set <strong>Authentication duration</strong> to <strong>Require every login</strong>.</li>
</ul>
<p>To configure this for an application via the API, first send a <code>GET</code> request to retrieve the full application configuration, then send a <code>PUT</code> request with the complete application body including the updated <code>mfa_config</code>. Set <code>session_duration</code> to <code>&quot;0m&quot;</code>:</p>
<pre tabindex="0"><code class="language-bash">curl --request PUT \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/access/apps/{app_id} \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;mfa_config&quot;: {&#10;    &quot;mfa_disabled&quot;: false,&#10;    &quot;session_duration&quot;: &quot;0m&quot;&#10;  }&#10;}&#x27;&#10;</code></pre>
<h3 id="precedence-example">Precedence example</h3>
<p>Consider the following configuration:</p>
<pre tabindex="0"><code class="language-mermaid">flowchart TD&#10;    subgraph org[&quot;Organization&quot;]&#10;        orgSettings[&quot;**Apply global MFA settings by default**, &lt;br/&gt;**MFA methods**: Authenticator app + Security key, &lt;br/&gt;**Authentication duration**: 24 hours&quot;]&#10;    end&#10;&#10;    subgraph appA[&quot;Application A&quot;]&#10;        appASettings[&quot;**Respect global enforcement setting**&lt;br/&gt;(inherits organization settings)&quot;]&#10;        subgraph policies[&quot;Policies&quot;]&#10;            policy1[&quot;Policy 1&lt;br/&gt;**Custom MFA settings**,&lt;br/&gt;**MFA methods**: Security keys only,&lt;br/&gt;**Authentication duration**: 1 hour&quot;]&#10;            policy2[&quot;Policy 2&lt;br/&gt;**Disable MFA**&quot;]&#10;        end&#10;    end&#10;&#10;    subgraph appB[&quot;Application B&quot;]&#10;        appBSettings[&quot;**Disable MFA**&quot;]&#10;    end&#10;&#10;    orgSettings --&gt; appASettings&#10;    orgSettings -.-&gt;|&quot;overridden&quot;| appBSettings&#10;    appASettings -.-&gt;|&quot;overridden by&quot;| policy1&#10;    appASettings -.-&gt;|&quot;overridden by&quot;| policy2&#10;</code></pre>
<p>In this example:</p>
<ul>
<li>Users who access Application A and match Policy 1 must use a security key and re-authenticate every hour.</li>
<li>Users who access Application A and match Policy 2 are not prompted for MFA.</li>
<li>Users who access Application A and match neither policy must use an authenticator application or a security key, with a 24-hour session.</li>
<li>Users who access Application B are not prompted for MFA.</li>
</ul>
<h2 id="infrastructure-applications">Infrastructure applications</h2>
<p>Infrastructure applications that use SSH support two infrastructure-only MFA methods. <code>piv_key</code> uses an enrolled Personal Identity Verification (PIV) key. <code>ssh_fido2_key</code> uses an enrolled FIDO2 key. Neither method applies to other Access application types or browser WebAuthn authentication.</p>
<p>You can configure MFA for infrastructure apps at the application level or at the policy level.</p>
<h3 id="configure-mfa-for-an-infrastructure-application">Configure MFA for an infrastructure application</h3>
<p>Select PIV key, FIDO2 key, or both when configuring custom MFA. The corresponding API arrays are <code>[&quot;piv_key&quot;]</code>, <code>[&quot;ssh_fido2_key&quot;]</code>, and <code>[&quot;piv_key&quot;, &quot;ssh_fido2_key&quot;]</code>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4576.md")
</aside>
<details class="nb-details"><summary>Dashboard</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4581.md")
</div></details>
<details class="nb-details"><summary>API</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4582.md")
</div></details>
<h3 id="configure-mfa-for-an-infrastructure-policy">Configure MFA for an infrastructure policy</h3>
<p>You can set different MFA requirements for different SSH usernames by configuring MFA at the policy level. Policy-level MFA settings override application-level settings.</p>
<details class="nb-details"><summary>Dashboard</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4583.md")
</div></details>
<details class="nb-details"><summary>API</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4584.md")
</div></details>
<h3 id="mfa-session-duration-for-ssh">MFA session duration for SSH</h3>
<p>The MFA session duration determines how long users can open new SSH connections without another MFA prompt. Set the duration to <code>0m</code> to require MFA for every new connection. Expiration does not terminate an active connection.</p>
<p>MFA sessions are bound to the user's device. If a user switches to a different device, they must re-authenticate regardless of the remaining session duration.</p>
<p>Session duration is evaluated in the following order:</p>
<ol>
<li><strong>Policy-level duration</strong> — If set, applies to users who match the policy.</li>
<li><strong>Application-level duration</strong> — If no policy-level duration is set, uses the application setting.</li>
<li><strong>Organization-level duration</strong> — If neither policy nor application defines a duration, uses the global setting.</li>
</ol>
<p>When a user matches multiple policies that each define a session duration, Access uses the <strong>shortest</strong> duration across all matching policies.</p>
<h3 id="precedence-and-conflict-resolution">Precedence and conflict resolution</h3>
<p>MFA configuration is evaluated from most specific to least specific: <strong>policy</strong> &gt; <strong>application</strong> &gt; <strong>organization</strong>.</p>
<table>
<thead>
<tr>
<th>Organization MFA</th>
<th>Application MFA</th>
<th>Policy MFA</th>
<th>Result</th>
</tr>
</thead>
<tbody>
<tr>
<td>Required</td>
<td>Required</td>
<td>Required</td>
<td>MFA required</td>
</tr>
<tr>
<td>Required</td>
<td>Required</td>
<td>Disabled</td>
<td>MFA not required (policy wins)</td>
</tr>
<tr>
<td>Required</td>
<td>Disabled</td>
<td>(not set)</td>
<td>MFA not required (application wins)</td>
</tr>
<tr>
<td>Required</td>
<td>(not set)</td>
<td>(not set)</td>
<td>MFA required (organization setting applies)</td>
</tr>
</tbody>
</table>
<p>Organization-level MFA must be enabled for users to enroll PIV keys. Explicit settings at a lower level (policy or application) override higher levels. If no explicit setting exists at a level, the next higher level applies.</p>
