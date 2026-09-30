---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/salesforce-saas-saml/
  description: Learn to configure Salesforce as a SAML app in Cloudflare One. Follow step-by-step instructions for adding SaaS apps and enabling SSO.
  full_title: Salesforce (SAML) · Cloudflare One docs
  head_html: <title>Salesforce (SAML) · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn to configure Salesforce as a SAML app in Cloudflare One. Follow step-by-step instructions for adding SaaS apps and enabling SSO."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/salesforce-saas-saml/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/salesforce-saas-saml/index.md"><meta property="og:title" content="Salesforce (SAML) · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn to configure Salesforce as a SAML app in Cloudflare One. Follow step-by-step instructions for adding SaaS apps and enabling SSO."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/salesforce-saas-saml/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML,Salesforce"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/salesforce-saas-saml/#page","headline":"Salesforce (SAML) \u00b7 Cloudflare One docs","description":"Learn to configure Salesforce as a SAML app in Cloudflare One. Follow step-by-step instructions for adding SaaS apps and enabling SSO.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/salesforce-saas-saml/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML","Salesforce"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/http-apps/saas-apps/salesforce-saas-saml/
  schema: 1
---
<p>This guide covers how to configure <a href="https://help.salesforce.com/s/articleView?id=sf.sso_saml.htm&amp;type=5">Salesforce</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a Salesforce account</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, select <em>Salesforce</em>.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: <code>https://&lt;your-domain&gt;.my.salesforce.com</code> or <code>https://&lt;your-domain&gt;.my.salesforce.com?so=&lt;your-salesforce-org-id&gt;</code>, if your account was created before summer 2019 or does not have a My Domain subdomain.</li>
<li><strong>Assertion Consumer Service URL</strong>: <code>https://&lt;your-domain&gt;.my.salesforce.com</code> or <code>https://&lt;your-domain&gt;.my.salesforce.com?so=&lt;your-salesforce-org-id&gt;</code>, if your account was created before summer 2019 or does not have a My Domain subdomain.</li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4844.md")
</aside>
<ol start="7">
<li>Copy the <strong>SSO endpoint</strong>, <strong>Public key</strong>, and <strong>Access Entity ID or Issuer</strong>.</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="2-create-a-certificate-file"><ol start="2">
<li>Create a certificate file</li>
</ol></h2>
<ol>
<li>Paste the <strong>Public key</strong> in a text editor.</li>
<li>Wrap the certificate in <code>-----BEGIN CERTIFICATE-----</code> and <code>-----END CERTIFICATE-----</code>.</li>
<li>Set the file extension as <code>.crt</code> and save.</li>
</ol>
<h2 id="3-add-a-saml-sso-provider-to-salesforce"><ol start="3">
<li>Add a SAML SSO provider to Salesforce</li>
</ol></h2>
<ol>
<li>
<p>In Salesforce, go to <strong>Setup</strong>.</p>
</li>
<li>
<p>In the <strong>Quick Find</strong> box, enter <code>single sign-on</code> and select <strong>Single Sign-On Settings</strong>.</p>
</li>
<li>
<p>In <strong>SAML Single Sign-On Settings</strong>, select <strong>New</strong>.</p>
</li>
<li>
<p>Fill in the following fields:</p>
<ul>
<li><strong>Name:</strong> Name of the SSO provider (for example, <code>Cloudflare Access</code>). Users will select this name when signing in to Salesforce.</li>
<li><strong>API name:</strong> (this will pre-populate)</li>
<li><strong>Issuer:</strong> Paste the Access Entity ID or Issuer from application configuration in Cloudflare One.</li>
<li><strong>Identity Provider Certificate</strong>: Upload the <code>.crt</code> certificate file from <a href="#2-create-a-certificate-file">2. Create a certificate file</a>.</li>
<li><strong>Entity ID</strong>: <code>https://&lt;your-domain&gt;.my.salesforce.com</code></li>
<li><strong>SAML Identity type:</strong> If the user's Salesforce username is their email address, select <em>Assertion contains the User's Salesforce username</em>. Otherwise, select <em>Assertion contains the Federation ID from the User object</em> and make sure the user's Federation ID matches their email address.</li>
</ul>
<details class="nb-details"><summary>Configure Federation IDs</summary><div class="nb-details-body">
</li>
</ol>
@markup("md", "content/.markup/bodies/4845.md")
</div></details>
   - **Identity Provider Login URL**: SSO endpoint provided in Cloudflare One
   for this application.
<ol start="5">
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="4-enable-single-sign-on-in-salesforce"><ol start="4">
<li>Enable Single Sign-On in Salesforce</li>
</ol></h2>
<ol>
<li>Configure Single Sign-On settings:
<ol>
<li>In the <strong>Quick Find</strong> box, enter <code>single sign-on</code> and select <strong>Single Sign-On Settings</strong>.</li>
<li>(Optional) To require users to login with Cloudflare Access, turn on <strong>Disable login with Salesforce credentials</strong>.</li>
<li>Turn on <strong>SAML Enabled</strong>.</li>
<li>Turn on <strong>Make federation ID case-insensitive</strong>.</li>
</ol>
</li>
<li></li>
</ol>
<p>Enable Cloudflare Access as an identity provider on your Salesforce domain:</p>
<ol>
<li>In the <strong>Quick Find</strong> box, enter <code>domain</code> and select <strong>My Domain</strong>.</li>
<li>In <strong>Authentication Configuration</strong>, select <strong>Edit</strong>.</li>
<li>In <strong>Authentication Service</strong>, turn on the Cloudflare Access provider.</li>
</ol>
<p>To test, open an incognito browser window and go to your Salesforce domain (<code>https://&lt;your-domain&gt;.my.salesforce.com</code>).</p>
