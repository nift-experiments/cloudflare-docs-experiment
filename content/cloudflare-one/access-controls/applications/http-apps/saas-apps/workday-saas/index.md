---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/workday-saas/
  description: Integrate Workday with Access.
  full_title: Workday · Cloudflare One docs
  head_html: <title>Workday · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Workday with Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/workday-saas/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/workday-saas/index.md"><meta property="og:title" content="Workday · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Workday with Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/workday-saas/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/workday-saas/#page","headline":"Workday \u00b7 Cloudflare One docs","description":"Integrate Workday with Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/workday-saas/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/http-apps/saas-apps/workday-saas/
  schema: 1
---
<p>This guide covers how to configure <a href="https://doc.workday.com/admin-guide/en-us/authentication-and-security/authentication/saml/dan1370796470811.html?toc=1.5.1">Workday</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a Workday account</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, enter <code>Workday</code> and select the corresponding textbox that appears.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: <code>http://www.workday.com</code></li>
<li><strong>Assertion Consumer Service URL</strong>: <code>https://&lt;your-environment&gt;.myworkday.com/&lt;your-tenant&gt;/login-saml.flex</code> for a production account or <code>https://&lt;your-environment&gt;-impl.myworkday.com/&lt;your-tenant&gt;/login-saml.flex</code> for a preview sandbox account</li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Copy the <strong>SSO endpoint</strong>, <strong>Access Entity ID or Issuer</strong>, and <strong>Public key</strong>.</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="2-download-the-metadata-file"><ol start="2">
<li>Download the metadata file</li>
</ol></h2>
<ol>
<li>Paste the SAML Metadata endpoint from application configuration in Cloudflare One in a web browser.</li>
<li>Follow your browser-specific steps to download the URL's contents as an <code>.xml</code> file.</li>
</ol>
<h2 id="3-add-a-saml-sso-provider-to-workday"><ol start="3">
<li>Add a SAML SSO provider to Workday</li>
</ol></h2>
<ol>
<li>In Workday, go to <strong>Account Administration</strong> &gt; <strong>Actions</strong> &gt; <strong>Edit Tenant Setup - Security</strong>.</li>
<li>Under <strong>SAML Setup</strong>, turn on <strong>Enable SAML Authentication</strong>.</li>
<li>In the <strong>SAML Identity Providers</strong> table, select <strong>+</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Identity Provider Name</strong>: Your desired name for the identity provider (for example, <code>Cloudflare Access</code>)</li>
<li><strong>Issuer</strong>: Access Entity ID or Issuer from application configuration in Cloudflare One</li>
<li><strong>IdP SSO Service URL</strong>: SSO endpoint from application configuration in Cloudflare One</li>
</ul>
</li>
<li>Under <strong>x509 Certificate</strong>, select the menu icon &gt; <strong>Create x509 Public Key</strong>.</li>
<li>Under <strong>Name</strong>, enter a unique name (for example, <code>access</code>).</li>
<li>Under <strong>Certificate</strong>, paste the Public key from application configuration in Cloudflare One.</li>
<li>Select <strong>OK</strong>.</li>
<li>If you want to enable SP-initiated login (login initiated by going to your Workday URL), fill in the following fields:
<ul>
<li><strong>SP Initiated</strong>: Turn on.</li>
<li><strong>Service Provider ID</strong>: <code>http://www.workday.com</code></li>
<li><strong>Sign SP-initiated request</strong>: Turn off.</li>
</ul>
</li>
<li>Under <strong>Single Sign-On</strong>, add one or both of the following entries to the <strong>Redirection URLs</strong> grid. For each entry, if your user groups will use the same authentication option to sign in, select <strong>Single URL</strong>. If they will use different authentication options, select <strong>Authentication selector</strong>.
<ul>
<li>IdP-initiated SSO: Under <strong>Login Redirect URL</strong>, enter <code>&lt;your-team-name&gt;.cloudflareaccess.com</code>.</li>
<li>SP-initiated SSO: Under <strong>Login Redirect URL</strong>, enter <code>https://&lt;your-environment&gt;/&lt;your-tenant/login-saml2.htmld</code>.</li>
</ul>
</li>
</ol>
<h2 id="4-test-the-integration"><ol start="4">
<li>Test the integration</li>
</ol></h2>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4838.md")
</aside>
<ol>
<li>In Workday, create an <a href="https://doc.workday.com/admin-guide/en-us/authentication-and-security/authentication/authentication-policies/dan1370796466772.html">authentication rule</a>.</li>
<li>Under <strong>Authentication Conditions</strong>, add conditions that will apply only to your test user.</li>
<li>Under <strong>Allowed Authentication Types</strong>, select <strong>Specific</strong>, then <strong>SAML</strong>.</li>
<li>Select <strong>Done</strong>.</li>
<li>Complete the following step:
<ul>
<li><strong>If you have enabled SP-initiated login</strong>: Open an incognito browser window, go to your Workday URL, and enter your test user's email. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.</li>
<li><strong>If you have not enabled SP-initiated login</strong>: Go to your App Launcher at <code>https://&lt;cloudflare-team-name&gt;.cloudflareaccess.com</code>. Select the <strong>Workday</strong> tile. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.</li>
</ul>
</li>
<li>Once login is successful, you can configure your security settings further, such as adding <a href="https://doc.workday.com/admin-guide/en-us/authentication-and-security/configurable-security/security-groups/user-based-security-groups/dan1370796695367.html?toc=2.2.12.0">user groups</a> or <a href="https://doc.workday.com/admin-guide/en-us/authentication-and-security/authentication/authentication-policies/dan1370796466772.html">authentication rules</a> to configure different login rules for different groups of users.</li>
</ol>
