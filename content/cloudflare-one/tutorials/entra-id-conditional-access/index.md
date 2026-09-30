---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/tutorials/entra-id-conditional-access/
  description: With Conditional Access in Microsoft Entra ID, administrators can enforce policies on applications and users directly in EntraID.
  full_title: Use Microsoft Entra ID Conditional Access policies in Cloudflare Access · Cloudflare One docs
  head_html: <title>Use Microsoft Entra ID Conditional Access policies in Cloudflare Access · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="With Conditional Access in Microsoft Entra ID, administrators can enforce policies on applications and users directly in EntraID."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/tutorials/entra-id-conditional-access/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/tutorials/entra-id-conditional-access/index.md"><meta property="og:title" content="Use Microsoft Entra ID Conditional Access policies in Cloudflare Access · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="With Conditional Access in Microsoft Entra ID, administrators can enforce policies on applications and users directly in EntraID."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/tutorials/entra-id-conditional-access/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Microsoft Entra ID"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/tutorials/entra-id-conditional-access/#page","headline":"Use Microsoft Entra ID Conditional Access policies in Cloudflare Access \u00b7 Cloudflare One docs","description":"With Conditional Access in Microsoft Entra ID, administrators can enforce policies on applications and users directly in EntraID.","url":"https://developers.cloudflare.com/cloudflare-one/tutorials/entra-id-conditional-access/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Microsoft Entra ID"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/tutorials/entra-id-conditional-access/
  schema: 1
---
<p>With <a href="https://learn.microsoft.com/entra/identity/conditional-access/overview">Conditional Access</a> in Microsoft Entra ID (formerly Azure Active Directory), administrators can enforce policies on applications and users directly in Entra ID. Conditional Access has a set of checks that are specialized to Windows and are often preferred by organizations with Windows power users.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>Make sure you have:</p>
<ul>
<li>Global admin rights to Microsoft Entra ID account</li>
<li>Configured users in the Microsoft Entra ID account</li>
</ul>
<h2 id="set-up-an-identity-provider-for-your-application">Set up an identity provider for your application</h2>
<p>Refer to <a href="/cloudflare-one/integrations/identity-providers/entra-id/#set-up-entra-id-as-an-identity-provider">our IdP setup instructions</a> for Entra ID.</p>
<h2 id="add-api-permission-in-entra-id">Add API permission in Entra ID</h2>
<p>Once the base IdP integration is tested and working, grant permission for Cloudflare to read Conditional Access policies from Entra ID.</p>
<ol>
<li>
<p>In Microsoft Entra ID, go to <strong>App registrations</strong>.</p>
</li>
<li>
<p>Select the application you created for the IdP integration.</p>
</li>
<li>
<p>Go to <strong>API permissions</strong> and select <strong>Add a permission</strong>.</p>
</li>
<li>
<p>Select <strong>Microsoft Graph</strong>.</p>
</li>
<li>
<p>Select <strong>Application permissions</strong> and add <code>Policy.Read.ConditionalAccess</code>.</p>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4305.md")
</aside>
<ol start="6">
<li>Select <strong>Grant admin consent</strong>.</li>
</ol>
<h2 id="configure-conditional-access-in-entra-id">Configure Conditional Access in Entra ID</h2>
<ol>
<li>In Microsoft Entra ID, go to <strong>Enterprise applications</strong> &gt; <strong>Conditional Access</strong>.</li>
<li>Go to <strong>Authentication Contexts</strong>.</li>
<li><a href="https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-cloud-apps#authentication-context">Create an authentication context</a> to reference in your Cloudflare Access policies. Give the authentication context a descriptive name (for example, <code>Require compliant devices</code>).</li>
<li>Next, go to <strong>Policies</strong>.</li>
<li><a href="https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policies">Create a new Conditional Access policy</a> or select an existing policy.</li>
<li>Assign the conditional access policy to an authentication context:
<ol>
<li>In the policy builder, select <strong>Target resources</strong>.</li>
<li>In the <strong>Select what this policy applies to</strong> dropdown, select <em>Authentication context</em>.</li>
<li>Select the authentication context that will use this policy.</li>
<li>Save the policy.</li>
</ol>
</li>
</ol>
<h2 id="sync-conditional-access-with-zero-trust">Sync Conditional Access with Zero Trust</h2>
<p>To import your Conditional Access policies into Cloudflare Access:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Access settings</strong>.</li>
<li>In <strong>Manage your App Launcher</strong>, select <strong>Manage</strong>.</li>
<li>Choose <strong>Login methods</strong>.</li>
<li>Find your Microsoft Entra ID integration and select <strong>Edit</strong>.</li>
<li>Enable <strong>Azure AD Policy Sync</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="create-an-access-application">Create an Access application</h2>
<p>To enforce your Conditional Access policies on a Cloudflare Access application:</p>
<ol>
<li>
<p>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</p>
</li>
<li>
<p>Select <strong>Create new application</strong>.</p>
</li>
<li>
<p>Select <strong>Self-hosted and private</strong>.</p>
</li>
<li>
<p>Select <strong>Add public hostname</strong> and enter the target URL of the protected application.</p>
</li>
<li>
<p>Select <strong>Create new policy</strong> and build an <a href="/cloudflare-one/access-controls/policies/">Access policy</a> using the <em>Azure AD - Auth context</em> selector. For example:</p>
</li>
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
<td>Include</td>
<td>Emails ending in</td>
<td><code>@example.com</code></td>
</tr>
<tr>
<td></td>
<td>Require</td>
<td>Azure AD - Auth context</td>
<td><code>Require compliant devices</code></td>
</tr>
</tbody>
</table>
<ol start="6">
<li>
<p>Add this policy to your application configuration.</p>
</li>
<li>
<p>For <strong>Identity providers</strong>, select your Microsoft Entra ID integration.</p>
</li>
<li>
<p>Follow the remaining <a href="/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/">self-hosted application creation steps</a> to publish the application.</p>
</li>
</ol>
<p>Users will only be allowed access if they pass the Microsoft Entra ID Conditional Access policies associated with this authentication context.</p>
