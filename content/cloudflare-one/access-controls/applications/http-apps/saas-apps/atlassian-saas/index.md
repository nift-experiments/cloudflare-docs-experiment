---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/atlassian-saas/
  description: Integrate Atlassian Cloud with Access.
  full_title: Atlassian Cloud · Cloudflare One docs
  head_html: <title>Atlassian Cloud · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Atlassian Cloud with Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/atlassian-saas/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/atlassian-saas/index.md"><meta property="og:title" content="Atlassian Cloud · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Atlassian Cloud with Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/atlassian-saas/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/atlassian-saas/#page","headline":"Atlassian Cloud \u00b7 Cloudflare One docs","description":"Integrate Atlassian Cloud with Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/atlassian-saas/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/http-apps/saas-apps/atlassian-saas/
  schema: 1
---
<p>This guide covers how to configure <a href="https://support.atlassian.com/security-and-access-policies/docs/configure-saml-single-sign-on-with-an-identity-provider/">Atlassian Cloud</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to an Atlassian Cloud account</li>
<li>Atlassian Guard Standard subscription</li>
<li>A <a href="https://support.atlassian.com/user-management/docs/verify-a-domain-to-manage-accounts/">domain</a> verified in Atlassian Cloud</li>
</ul>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, select <em>Atlassian</em>.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Copy the <strong>Access Entity ID or Issuer</strong>, <strong>Public key</strong>, and <strong>SSO endpoint</strong>.</li>
<li>Keep this window open. You will finish this configuration in step <a href="#4-finish-adding-a-saas-application-to-cloudflare-one">4. Finish adding a SaaS application to Cloudflare One</a>.</li>
</ol>
<h2 id="2-create-a-x-509-certificate"><ol start="2">
<li>Create a x.509 certificate</li>
</ol></h2>
<ol>
<li>Paste the <strong>Public key</strong> in a text editor.</li>
<li>Wrap the certificate in <code>-----BEGIN CERTIFICATE-----</code> and <code>-----END CERTIFICATE-----</code>.</li>
</ol>
<h2 id="3-configure-an-identity-provider-and-saml-sso-in-atlassian-cloud"><ol start="3">
<li>Configure an identity provider and SAML SSO in Atlassian Cloud</li>
</ol></h2>
<ol>
<li>In Atlassian Cloud, go to <strong>Security</strong> &gt; <strong>Identity providers</strong>.</li>
<li>Select <strong>Other provider</strong> &gt; <strong>Choose</strong>.</li>
<li>For <strong>Directory name</strong>, enter your desired name. For example, you could enter <code>Cloudflare Access</code>.</li>
<li>Select <strong>Add</strong> &gt; <strong>Set up SAML single sign-on</strong> &gt; <strong>Next</strong>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4870.md")
</aside>
<ol start="5">
<li>Fill in the following fields:
<ul>
<li><strong>Identity provider Entity ID</strong>: Access Entity ID or Issuer from application configuration in Cloudflare One.</li>
<li><strong>Identity provider SSO URL</strong>: SSO endpoint from application configuration in Cloudflare One.</li>
<li><strong>Public x509 certificate</strong>: Paste the entire x.509 certificate from step <a href="#2-create-a-x509-certificate">2. Create a x.509 certificate</a>.</li>
</ul>
</li>
<li>Select <strong>Next</strong>.</li>
<li>Copy the <strong>Service provider entity URL</strong> and <strong>Service provider assertion consumer service URL</strong>.</li>
<li>Select <strong>Next</strong>.</li>
<li>Under <strong>Link domain</strong>, select the domain you want to use with SAML SSO.</li>
<li>Select <strong>Next</strong> &gt; <strong>Stop and save SAML</strong>.</li>
</ol>
<h2 id="4-finish-adding-a-saas-application-to-cloudflare-one"><ol start="4">
<li>Finish adding a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In your open Cloudflare One window, fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: Service provider entity URL from Atlassian Cloud SAML SSO set-up.</li>
<li><strong>Assertion Consumer Service URL</strong>: Service provider assertion consumer service URL from Atlassian Cloud SAML SSO set-up.</li>
<li><strong>Name ID format</strong>: <em>Email</em></li>
</ul>
</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="5-create-an-authentication-policy-to-test-integration"><ol start="5">
<li>Create an authentication policy to test integration</li>
</ol></h2>
<p>To enable SSO for users in Atlassian Cloud, create an <a href="https://support.atlassian.com/security-and-access-policies/docs/configure-authentication-policies-for-your-organization/">Atlassian authentication policy</a>:</p>
<ol>
<li>In Atlassian Cloud, go to <strong>Security</strong> &gt; <strong>Authentication policies</strong>.</li>
<li>Select <strong>Add policy</strong>.</li>
<li>Under <strong>Directory</strong>, select the identity provider you used to configure SAML SSO.</li>
<li>For <strong>Policy name</strong>, enter your desired name.</li>
<li>Select <strong>Add</strong>.</li>
<li>In <strong>Settings</strong>, turn on <strong>Enforce single sign-on</strong>.</li>
<li>In <strong>Members</strong>, select <strong>Add members</strong>.</li>
<li>In <strong>Individual Users</strong>, select your desired test user(s) in the dropdown, and select <strong>Add members</strong>.</li>
<li>In <strong>Settings</strong>, select <strong>Update</strong> &gt; <strong>Update</strong>.</li>
</ol>
<h2 id="6-test-the-integration"><ol start="6">
<li>Test the integration</li>
</ol></h2>
<p>Open an incognito browser window and log in with the credentials of the test user you added to the test authentication policy. You will be redirected to the Cloudflare Access login screen and prompted to sign in with your identity provider. When this is successful, turn on <strong>Enforce single sign-on</strong> in your desired authentication policy, or add the desired users to the application policy created in step <a href="#5-create-an-authentication-policy-to-test-integration">5. Create an Application Policy to test Integration</a>.</p>
