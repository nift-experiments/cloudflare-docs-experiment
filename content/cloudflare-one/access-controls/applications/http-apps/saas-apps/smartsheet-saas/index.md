---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/smartsheet-saas/
  description: Integrate Smartsheet with Access.
  full_title: Smartsheet · Cloudflare One docs
  head_html: <title>Smartsheet · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Smartsheet with Access."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/smartsheet-saas/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/smartsheet-saas/index.md"><meta property="og:title" content="Smartsheet · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Smartsheet with Access."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/smartsheet-saas/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="SAML"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/smartsheet-saas/#page","headline":"Smartsheet \u00b7 Cloudflare One docs","description":"Integrate Smartsheet with Access.","url":"https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/saas-apps/smartsheet-saas/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["SAML"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/access-controls/applications/http-apps/saas-apps/smartsheet-saas/
  schema: 1
---
<p>This guide covers how to configure <a href="https://help.smartsheet.com/articles/2483123-domain-level-saml-configuration">Smartsheet</a> as a SAML application in Cloudflare One.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>An <a href="/cloudflare-one/integrations/identity-providers/">identity provider</a> configured in Cloudflare One</li>
<li>Admin access to a Smartsheet Enterprise account</li>
<li>A <a href="https://help.smartsheet.com/articles/2483051-domain-management">domain</a> verified in Smartsheet</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4840.md")
</aside>
<h2 id="1-add-a-saas-application-to-cloudflare-one"><ol>
<li>Add a SaaS application to Cloudflare One</li>
</ol></h2>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Access controls</strong> &gt; <strong>Applications</strong>.</li>
<li>Select <strong>Create new application</strong> &gt; <strong>SaaS application</strong>.</li>
<li>For <strong>Application</strong>, enter <code>Smartsheet</code> and select the corresponding textbox that appears.</li>
<li>For the authentication protocol, select <strong>SAML</strong>.</li>
<li>Select <strong>Add application</strong>.</li>
<li>Fill in the following fields:
<ul>
<li><strong>Entity ID</strong>: <code>urn:amazon:cognito:sp:us-east-1_xww1cbP43</code></li>
<li><strong>Assertion Consumer Service URL</strong>: <code>https://saml.authn.smartsheet.com/saml2/idpresponse</code></li>
<li><strong>Name ID format</strong>: <em>Unique ID</em></li>
</ul>
</li>
<li>Copy the <strong>SAML Metadata endpoint</strong>.</li>
<li>Configure <a href="/cloudflare-one/access-controls/policies/">Access policies</a> for the application.</li>
<li>Save the application.</li>
</ol>
<h2 id="2-create-and-test-a-saml-sso-provider-in-smartsheet"><ol start="2">
<li>Create and test a SAML SSO provider in Smartsheet</li>
</ol></h2>
<ol>
<li>In your Smartsheet Admin Center, go to <strong>Settings</strong> &gt; <strong>Authentication</strong> &gt; <strong>Add a SAML IdP</strong>.</li>
<li>In <strong>Other IdP (Customize)</strong>, select <strong>Configure</strong>.</li>
<li>Select <strong>Next</strong>.</li>
<li>Under <strong>XML URL</strong>, paste the SAML Metadata endpoint from application configuration in Cloudflare One.</li>
<li>Under <strong>Name SAML IdP</strong>, enter a name (for example, <code>Cloudflare Access</code>).</li>
<li>Select <strong>Save &amp; Next</strong>.</li>
<li>Select <strong>Verify connection</strong> and sign in via Access. If validation is successful, you will see a <strong>SAML IdP Successfully Connected!</strong> message. Close the configuration verification page.</li>
<li>Turn on <strong>I have successfully verified the connection</strong>.</li>
<li>Select <strong>Save &amp; Next</strong>.</li>
<li>Under <strong>Assign domains to SAML IdP</strong>, select your desired domain.</li>
<li>Select <strong>Save and Next</strong> and then <strong>Finish</strong>.</li>
</ol>
