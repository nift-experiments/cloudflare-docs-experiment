---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/generic-saml-saas/
  description: Generic SAML application in Access.
  full_title: Generic SAML application · Cloudflare One docs
  head_html: <title>Generic SAML application · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Generic SAML application in Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/generic-saml-saas/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/generic-saml-saas/index.md"><meta property="og:title" content="Generic SAML application · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Generic SAML application in Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/generic-saml-saas/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/generic-saml-saas/#page","headline":"Generic SAML application \u00b7 Cloudflare One docs","description":"Generic SAML application in Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/generic-saml-saas/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/http-apps/saas-apps/generic-saml-saas/
  schema: 1
---
<p>This page provides generic instructions for setting up a SaaS application in Cloudflare Access using the SAML authentication protocol.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to the account of the SaaS application</li>
</ul>
<h2 id="1-get-saas-application-urls"><ol>
<li>Get SaaS application URLs</li>
</ol></h2>
<p>Obtain the following URLs from your SaaS application account:</p>
<ul>
<li><strong>Entity ID</strong>: A unique URL issued for your SaaS application, for example <code>https://&lt;your-domain&gt;.my.salesforce.com</code>.</li>
<li><strong>Assertion Consumer Service URL</strong>: The service provider's endpoint for receiving and parsing SAML assertions.</li>
</ul>
<h2 id="2-add-your-application-to-access"><ol start="2">
<li>Add your application to Access</li>
</ol></h2>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Select <strong>Create new application</strong>.</p>
</li>
<li>
<p>Select <strong>SaaS application</strong>.</p>
</li>
<li>
<p>Select your <strong>Application</strong> from the drop-down menu. If your application is not listed, enter a custom name in the <strong>Application</strong> field and select the textbox that appears below.</p>
</li>
<li>
<p>Select <strong>SAML</strong>.</p>
</li>
<li>
<p>Select <strong>Add application</strong>.</p>
</li>
<li>
<p>Enter the <strong>Entity ID</strong> and <strong>Assertion Consumer Service URL</strong> obtained from your SaaS application account.</p>
</li>
<li>
<p>Select the <strong>Name ID Format</strong> expected by your SaaS application (usually <em>Email</em>).</p>
</li>
<li>
<p>(Optional) Configure any additional <a href="#saml-attributes">SAML attribute statements</a> required by your SaaS application.</p>
</li>
<li>
<p>Copy the <strong>SSO endpoint</strong>, <strong>Access Entity ID or Issuer</strong>, and <strong>Public key</strong>.</p>
</li>
</ol>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="idp-groups">IdP groups</h3>
@markup("md", "content/.markup/bodies/4859.md")
</aside>
<ol start="11">
<li></li>
</ol>
<p>Under <strong>Access policies</strong>, add an existing policy or <a href="/cloudflare-one/access-controls/policies/policy-management/">create a new policy</a> to control who can connect to your application. All Access applications are deny by default -- a user must match an Allow policy before they are granted access.</p>
<ol start="12">
<li></li>
</ol>
<p>Configure how users will authenticate:</p>
<ol>
<li>
Select the [identity providers](/cloudflare-one/integrations/identity-providers/) you want to enable for your application.
</li>
<li>
(Recommended) If you plan to only allow access via a single IdP, turn on **Apply instant authentication**. End users will not be shown the [Cloudflare Access login page](/cloudflare-one/reusable-components/custom-pages/access-login-page/). Instead, Cloudflare will redirect users directly to your SSO login event.
</li>
<li> (Optional) Turn on  <b>Authenticate with Cloudflare One Client</b> to allow users to authenticate to the application using their <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/client-sessions/"> Cloudflare One Client session identity</a>. </li>
</ol>
<ol start="13">
<li>
<p>(Optional) Go to <strong>Additional settings</strong> to customize the application experience:</p>
<ul>
<li><strong>App Launcher customization</strong>: Configure how this application appears to users in the <a href="/cloudflare-one/access-controls/access-settings/app-launcher/">App Launcher</a>.</li>
<li></li>
</ul>
</li>
</ol>
<p><strong>Custom block pages</strong>: Choose what users will see when they are denied access to the application.</p>
<ul>
<li><strong>Cloudflare default</strong>: Reload the <a href="/cloudflare-one/reusable-components/custom-pages/access-login-page/">login page</a> and display a block message below the Cloudflare Access logo. The default message is <code>That account does not have access</code>, or you can enter a custom message.</li>
<li><strong>Redirect URL</strong>: Redirect to the specified website.</li>
<li><strong>Custom page template</strong>: Display a <a href="/cloudflare-one/reusable-components/custom-pages/access-block-page/">custom block page</a> hosted in Cloudflare One.</li>
</ul>
<ol start="14">
<li>Select <strong>Create</strong>.</li>
</ol>
<h2 id="3-configure-sso-in-your-saas-application"><ol start="3">
<li>Configure SSO in your SaaS application</li>
</ol></h2>
<p>Next, configure your SaaS application to require users to log in through Cloudflare Access. Refer to your SaaS application documentation for instructions on how to configure a third-party SAML SSO provider. You will need the following values from the Cloudflare One:</p>
<ul>
<li><strong>SSO endpoint</strong></li>
<li><strong>Access Entity ID or Issuer</strong></li>
<li><strong>Public key</strong></li>
</ul>
<p>You can either manually enter this data into your SaaS application or upload a metadata XML file. The metadata is available at the URL: <code>&lt;SSO endpoint&gt;/saml-metadata</code>.</p>
<h3 id="validate-saml-response">Validate SAML Response</h3>
<p>When acting as a SAML identity provider, Cloudflare will sign both the SAML Response and the SAML Assertion using the SHA-256 algorithm. The SaaS application can validate this signature using the <strong>Public key</strong> that you upload to the SaaS application.</p>
<h2 id="4-test-the-integration"><ol start="4">
<li>Test the integration</li>
</ol></h2>
<p>Open an incognito browser window and go to the SaaS application's login URL. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.</p>
<h2 id="saml-attributes">SAML attributes</h2>
<p><a href="/cloudflare-one/integrations/identity-providers/generic-saml/#saml-headers-and-attributes">SAML attributes</a> refer to the user identity characteristics that Cloudflare Access shares with your SAML SaaS application upon successful authentication. By default, Cloudflare Access passes the following attributes (if available) to the SaaS application:</p>
<ul>
<li><code>id</code> - UUID of the user's Access identity</li>
<li><code>name</code> - Full name of the user (for example, <code>John Doe</code>)</li>
<li><code>email</code> - User's email address</li>
<li><code>groups</code> - Identity provider group membership</li>
</ul>
<p>In Access for SaaS, you can add additional SAML attributes or customize the SAML statement sent to the SaaS application. This allows you to integrate SaaS applications which have specific SAML attribute requirements.</p>
<h3 id="saml-attribute-statements">SAML attribute statements</h3>
<p>To send additional SAML attributes to your SaaS application, configure the following fields for each attribute:</p>
<pre tabindex="0"><code>- **Name**: SAML attribute name&#10;- **SAML friendly name**: (Optional) A human readable name for the SAML attribute&#10;- **Name format**: Specify the **Name** format expected by the SaaS application:&#10;		- `Unspecified`: (default) No specific format required.&#10;		- `URI`: Name is in a format such as `urn:ietf:params:scim:schemas:core:2.0:User:userName` or `urn:oid:2.5.4.42`.&#10;		- `Basic`: Name is a normal string such as `userName`.&#10;- **IdP claim**: The identity provider value that should map to this SAML attribute. You can select any [SAML attribute](/cloudflare-one/integrations/identity-providers/generic-saml/#saml-headers-and-attributes) or [OIDC claim](/cloudflare-one/integrations/identity-providers/generic-oidc/#custom-oidc-claims) that was configured in a Cloudflare One IdP integration.&#10;- **Required**: If an attribute is marked as required but is not provided by an IdP, Cloudflare will fail the authentication request and show an error page.&#10;- **Add per IdP claim**: (Optional) If you turned on multiple identity providers for the SaaS application, you can choose different attribute mappings for each IdP. These values will override the parent **IdP claim**.&#10;</code></pre>
<h3 id="jsonata-attribute-transforms">JSONata attribute transforms</h3>
<p>In <strong>Advanced settings</strong> &gt; <strong>Transformation</strong>, you can enter a <a href="https://jsonata.org/">JSONata</a> script that modifies a copy of the <a href="/cloudflare-one/team-and-resources/users/users/">User Registry identity</a>. This is useful for setting default values, excluding email addresses, or ensuring usernames meet arbitrary criteria. Access will send the modified user identity to the SaaS application as SAML attributes.</p>
<p>This corresponds to the <code>saml_attribute_transform_jsonata</code> field in the <a href="/api/resources/zero_trust/subresources/access/subresources/applications/methods/create/">Access applications API</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4858.md")
</aside>
<p>For example, the following JSONata script merges group names into a list and adds an <code>eduPersonPrincipalName</code> field which maps to the user email.</p>
<pre tabindex="0"><code class="language-txt">$merge([$, {&quot;groups&quot;: groups.name, &#x27;eduPersonPrincipalName&#x27;: email}])&#10;</code></pre>
<p>Here is an example of a user identity before applying the JSONata transform:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;account_id&quot;: &quot;699d98642c564d2e855e9661899b7252&quot;,&#10;  &quot;amr&quot;: [&#10;    &quot;pwd&quot;&#10;  ],&#10;  &quot;auth_status&quot;: &quot;NONE&quot;,&#10;  &quot;common_name&quot;: &quot;&quot;,&#10;  &quot;device_id&quot;: &quot;c1744f8b-faa1-48a4-9e5c-02ac921467fa&quot;,&#10;  &quot;device_sessions&quot;: {&#10;    &quot;49e653db-991e-11ee-af26-2243bf8c3428&quot;: {&#10;      &quot;last_authenticated&quot;: 1703004275&#10;    }&#10;  },&#10;  &quot;devicePosture&quot;: {&#10;    &quot;8534a230-e85e-4183-8964-a4b7dcf72986&quot;: {&#10;      &quot;rule_name&quot;: &quot;Warp&quot;,&#10;      &quot;success&quot;: true,&#10;      &quot;type&quot;: &quot;warp&quot;&#10;    }&#10;  },&#10;  &quot;email&quot;: &quot;jdoe@company.com&quot;,&#10;  &quot;gateway_account_id&quot;: &quot;bTSquyUGwLQjYJn8cI8S1h6M6wU&quot;,&#10;  &quot;geo&quot;: {&#10;    &quot;country&quot;: &quot;US&quot;&#10;  },&#10;  &quot;groups&quot;: [&#10;    {&#10;      &quot;id&quot;: &quot;12fdf91a-fb23-41b3-995a-de2f72c61d0e&quot;,&#10;      &quot;name&quot;: &quot;IdentityProtection-RiskyUser-RiskLevel-low&quot;&#10;    },&#10;    {&#10;      &quot;id&quot;: &quot;12348f47-8234-4860-a03f-c2a1513f267b&quot;,&#10;      &quot;name&quot;: &quot;Global Administrator&quot;&#10;    },&#10;    {&#10;      &quot;id&quot;: &quot;11235980-87d7-4917-b0aa-74c01914c40e&quot;,&#10;      &quot;name&quot;: &quot;Application Administrator&quot;&#10;    }&#10;  ],&#10;  &quot;iat&quot;: 1659474397,&#10;  &quot;id&quot;: &quot;OidHvkPt-I-13IBSnd77UJ8cHgsrUpjs3W6_4t6ES7M&quot;,&#10;  &quot;idp&quot;: {&#10;    &quot;id&quot;: &quot;b08e8c0c-a75d-4b3f-8e7b-cd427b7c7b47&quot;,&#10;    &quot;type&quot;: &quot;azureAD&quot;&#10;  }&#10;}&#10;</code></pre>
<p>Result after applying the example JSONata script:</p>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;account_id&quot;: &quot;699d98642c564d2e855e9661899b7252&quot;,&#10;  &quot;amr&quot;: [&#10;    &quot;pwd&quot;&#10;  ],&#10;  &quot;auth_status&quot;: &quot;NONE&quot;,&#10;  &quot;common_name&quot;: &quot;&quot;,&#10;  &quot;device_id&quot;: &quot;c1744f8b-faa1-48a4-9e5c-02ac921467fa&quot;,&#10;  &quot;device_sessions&quot;: {&#10;    &quot;49e653db-991e-11ee-af26-2243bf8c3428&quot;: {&#10;      &quot;last_authenticated&quot;: 1703004275&#10;    }&#10;  },&#10;  &quot;devicePosture&quot;: {&#10;    &quot;8534a230-e85e-4183-8964-a4b7dcf72986&quot;: {&#10;      &quot;rule_name&quot;: &quot;Warp&quot;,&#10;      &quot;success&quot;: true,&#10;      &quot;type&quot;: &quot;warp&quot;&#10;    }&#10;  },&#10;  &quot;email&quot;: &quot;jdoe@company.com&quot;,&#10;  &quot;gateway_account_id&quot;: &quot;bTSquyUGwLQjYJn8cI8S1h6M6wU&quot;,&#10;  &quot;geo&quot;: {&#10;    &quot;country&quot;: &quot;US&quot;&#10;  },&#10;  &quot;groups&quot;: [&#10;    &quot;IdentityProtection-RiskyUser-RiskLevel-low&quot;,&#10;    &quot;Global Administrator&quot;,&#10;    &quot;Application Administrator&quot;&#10;  ],&#10;  &quot;iat&quot;: 1659474397,&#10;  &quot;id&quot;: &quot;OidHvkPt-I-13IBSnd77UJ8cHgsrUpjs3W6_4t6ES7M&quot;,&#10;  &quot;idp&quot;: {&#10;    &quot;id&quot;: &quot;b08e8c0c-a75d-4b3f-8e7b-cd427b7c7b47&quot;,&#10;    &quot;type&quot;: &quot;azureAD&quot;&#10;  },&#10;  &quot;eduPersonPrincipalName&quot;: &quot;jdoe@company.com&quot;&#10;}&#10;</code></pre>
<p>For more JSONata transform use cases, refer to the following examples.</p>
<details class="nb-details"><summary>Remove groups attribute</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4860.md")
</div></details>
<details class="nb-details"><summary>Rename groups field and remove group ID</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4861.md")
</div></details>
<details class="nb-details"><summary>Filter groups by name</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4862.md")
</div></details>
<h3 id="nameid-transform">NameID transform</h3>
<p>By default, Access sends the user's email address as the SAML <code>NameID</code>. Some SaaS applications require a different value, such as an employee ID, a modified email address, or a username from a legacy system.</p>
<p>You can customize the <code>NameID</code> by setting the <code>name_id_transform_jsonata</code> field on the SaaS application via the <a href="/api/resources/zero_trust/subresources/access/subresources/applications/methods/create/">Access applications API</a>. This field accepts a <a href="https://jsonata.org/">JSONata</a> expression that evaluates against the user's identity and must return a single string value. The result replaces the default <code>NameID</code> in the SAML assertion.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4857.md")
</aside>
<p>For example, to modify the user's email so that it includes a <code>+sandbox</code> suffix (useful when connecting multiple instances of the same SaaS app):</p>
<pre tabindex="0"><code class="language-bash">curl --request PUT \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/access/apps/{app_id} \&#10;&#45;-header &quot;Authorization: Bearer {api_token}&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;saas_app&quot;: {&#10;    &quot;auth_type&quot;: &quot;saml&quot;,&#10;    &quot;name_id_transform_jsonata&quot;: &quot;$substringBefore(email, &#x27;\&#x27;&#x27;@&#x27;\&#x27;&#x27;) &amp; &#x27;\&#x27;&#x27;+sandbox@&#x27;\&#x27;&#x27; &amp; $substringAfter(email, &#x27;\&#x27;&#x27;@&#x27;\&#x27;&#x27;)&quot;&#10;  }&#10;}&#x27;&#10;</code></pre>
<p>Given a user with the email <code>jdoe@company.com</code>, this expression produces a <code>NameID</code> of <code>jdoe+sandbox@company.com</code>.</p>
<details class="nb-details"><summary>Use employee ID as NameID</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4863.md")
</div></details>
<details class="nb-details"><summary>Remove NameID transform</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/4864.md")
</div></details>
