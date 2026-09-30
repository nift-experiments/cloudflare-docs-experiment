---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/adobe-sign-saas/
  description: Integrate Adobe Acrobat Sign with Access.
  full_title: Adobe Acrobat Sign · Cloudflare One docs
  head_html: <title>Adobe Acrobat Sign · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Adobe Acrobat Sign with Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/adobe-sign-saas/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/adobe-sign-saas/index.md"><meta property="og:title" content="Adobe Acrobat Sign · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Adobe Acrobat Sign with Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/adobe-sign-saas/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/adobe-sign-saas/#page","headline":"Adobe Acrobat Sign \u00b7 Cloudflare One docs","description":"Integrate Adobe Acrobat Sign with Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/adobe-sign-saas/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/http-apps/saas-apps/adobe-sign-saas/
  schema: 1
---
<p>This guide covers how to configure <a href="https://helpx.adobe.com/sign/using/enable-saml-single-sign-on.html">Adobe Acrobat Sign</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a Adobe Acrobat Sign account</li>
<li>A <a href="https://helpx.adobe.com/sign/using/claim-domain-names.html">claimed domain</a> in Adobe Acrobat Sign</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, enter <code>Adobe Sign</code> and select the corresponding textbox that appears.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Copy the <strong>Access Entity ID or Issuer</strong>, <strong>Public key</strong>, and <strong>SSO endpoint</strong>.</li>
<li>Keep this window open without selecting <strong>Select configuration</strong>. You will finish this configuration in step <a href="#3-finish-adding-a-saas-application-to-cloudflare-one">3. Finish adding a SaaS application to Cloudflare One</a>.</li>
</ol>
<h2 id="2-add-a-saml-sso-provider-to-adobe-sign"><ol start="2">
<li>Add a SAML SSO provider to Adobe Sign</li>
</ol></h2>
<ol>
<li>In Adobe Acrobat Sign, select your profile picture &gt; your name &gt; <strong>Account Settings</strong> &gt; <strong>SAML Settings</strong>.</li>
<li>Turn <strong>SAML Allowed</strong> on.</li>
<li>Enter a hostname (for example, <code>yourcompanyname</code>). Users can use this URL or <code>https://secure.adobesign.com/public/login</code> to sign in via SSO.</li>
<li>(Optional) For <strong>Single Sign On Login Message</strong>, enter a custom message (for example, <code>Log in via SSO</code>). The default message is <strong>Sign in using your corporate credentials</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID/Issuer URL</strong>: Access Entity ID or Issuer from application configuration in Cloudflare One.</li>
<li><strong>Login URL/SSO Endpoint</strong>: SSO endpoint from application configuration in Cloudflare One.</li>
<li><strong>IdP Certificate</strong>: Public key from application configuration in Cloudflare One. Wrap the certificate in <code>-----BEGIN CERTIFICATE-----</code> and <code>-----END CERTIFICATE-----</code>.</li>
</ul>
</li>
<li>Copy the <strong>Entity ID/SAML Audience</strong> and <strong>Assertion Consumer URL</strong>.</li>
<li>Select <strong>Save</strong>.</li>
</ol>
<h2 id="3-finish-adding-a-saas-application-to-cloudflare-one"><ol start="3">
<li>Finish adding a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In your open Cloudflare One window, fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: Entity ID/SAML Audience from Adobe Acrobat Sign SAML SSO configuration.</li>
<li><strong>Assertion Consumer Service URL</strong>: Assertion Consumer URL from Adobe Acrobat Sign SAML SSO configuration.</li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="4-test-the-integration-and-finalize-configuration"><ol start="4">
<li>Test the integration and finalize configuration</li>
</ol></h2>
<ol>
<li>Open an incognito browser window and go to your Adobe Sign hostname URL or <code>https://secure.adobesign.com/public/login</code>. Select the option to sign in via SSO (<strong>Sign in using your corporate credentials</strong> if you have not configured a custom message). You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4872.md")
</aside>
<ol start="2">
<li>Once this is successful, you can make sign in via SSO mandatory. Select your profile picture &gt; your name &gt; <strong>Account Settings</strong> &gt; <strong>SAML Settings</strong>, and then turn on <strong>SAML Mandatory</strong>. Keeping <strong>Allow Acrobat Sign Account Administrators to log in using their Acrobat Sign Credentials</strong> turned on will allow administrators to log in even if your account experiences SSO issues.</li>
</ol>
